#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import json
import yaml
import argparse
import time
import re
from datetime import datetime
import pandas as pd
from openai import OpenAI
from loguru import logger
from rich.console import Console
from rich.panel import Panel
from rich.status import Status
from rich.markdown import Markdown
from rich.table import Table
from rich.text import Text

# 初始化 Rich Console
console = Console()

# 基础 Loguru 配置：仅保留终端 ERROR 输出
logger.remove()
logger.add(sys.stderr, level="ERROR")

def init_detailed_logging(project_id):
    """根据项目 ID 和时间戳动态初始化本地日志文件"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_filename = f"{project_id}_{timestamp}.log"
    logger.add(
        log_filename, 
        level="DEBUG", 
        format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {message}",
        encoding="utf-8"
    )
    return log_filename

def parse_price(price_str):
    """从价格字符串中提取数值 (例如 '3.2￥/Mtokens' -> 3.2)"""
    if not price_str: return 0.0
    match = re.search(r"(\d+\.?\d*)", str(price_str))
    return float(match.group(1)) if match else 0.0

def load_module_config(file_path="module.yaml"):
    """加载模型提供商配置"""
    if not os.path.exists(file_path):
        console.print(f"[bold red]错误: 缺少核心配置文件 {file_path}[/bold red]")
        sys.exit(1)
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except Exception as e:
        console.print(f"[bold red]解析 {file_path} 失败: {e}[/bold red]")
        sys.exit(1)

class SingleCellAnnotator:
    def __init__(self, provider_config):
        self.config = provider_config['model_provider']
        env_key_name = self.config.get('api_key_env', 'OPENAI_API_KEY')
        self.api_key = os.getenv(env_key_name)
        
        if not self.api_key:
            logger.critical(f"Missing {env_key_name} environment variable")
            console.print(f"[bold red]错误: 未找到 {env_key_name} 环境变量。[/bold red]")
            sys.exit(1)
            
        self.client = OpenAI(
            base_url=self.config.get('base_url'),
            api_key=self.api_key,
            timeout=self.config.get('timeout', 300)
        )

    def load_system_prompt(self, file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Prompt 文件不存在: {file_path}")
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()

    def load_and_format_csv(self, file_path, top_n=15):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"CSV 文件不存在: {file_path}")
        
        df = pd.read_csv(file_path)
        logger.debug(f"Raw CSV columns: {list(df.columns)}")

        # 1. 定义核心列映射 (每类只取一个最匹配的)
        core_map = {
            'cluster': ['cluster', 'Cluster'],
            'gene': ['gene', 'gene_id', 'gene_id_fix', 'gene_name', 'Gene', 'gene_short_name'],
            'avg_log2FC': ['avg_log2FC', 'avg_logFC', 'log2FC', 'Log2FC'],
            'p_val_adj': ['p_val_adj', 'padj', 'p.adj']
        }
        
        selected_core = {}
        for target, aliases in core_map.items():
            for alias in aliases:
                if alias in df.columns:
                    selected_core[target] = alias
                    break

        # 2. 定义必须保留的功能关键词 (匹配所有包含这些词的列)
        func_keywords = ['interpro', 'pfam', 'arabidopsis', 'ath', 'at_', 'description', 'func', 'note', 'definition', 'homolog']
        
        # 3. 筛选最终保留的列
        keep_cols = list(selected_core.values())
        for col in df.columns:
            if col in keep_cols: continue
            # 如果列名包含功能关键词，则保留
            if any(key in col.lower() for key in func_keywords):
                keep_cols.append(col)
        
        logger.debug(f"Columns kept for AI: {keep_cols}")
        
        # 4. 提取数据并排序
        if 'cluster' in selected_core:
            df_filtered = df[keep_cols]
            sort_cols = [selected_core['cluster']]
            if 'avg_log2FC' in selected_core:
                sort_cols.append(selected_core['avg_log2FC'])
            
            top_markers = df_filtered.sort_values(
                by=sort_cols, 
                ascending=[True, False]
            ).groupby(selected_core['cluster']).head(top_n)
        else:
            top_markers = df.head(top_n * 5) # 兜底逻辑

        return top_markers.to_csv(index=False)

    def annotate(self, system_prompt, user_background, csv_data):
        user_prompt = f"背景：{user_background}\n数据：\n{csv_data}"
        model_name = self.config.get('name', 'AI Model')
        model_id = self.config.get('model_id')
        timeout_val = self.config.get('timeout', 300)
        max_gen_tokens = self.config.get('max_tokens', 4096)
        
        start_time = time.time()
        with Status(f"[bold yellow]正在请求 {model_name} 进行智能注释...", spinner="dots") as status:
            try:
                response = self.client.chat.completions.create(
                    model=model_id,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt}
                    ],
                    temperature=self.config.get('temperature', 0.1),
                    timeout=timeout_val,
                    max_tokens=max_gen_tokens  # 显式控制生成上限
                )
                duration = time.time() - start_time
                
                # 检查输出是否完整
                if response.choices[0].finish_reason == 'length':
                    console.print("\n[bold orange3]⚠ 警告: 模型生成由于长度限制而发生截断！[/bold orange3]")
                    console.print("[dim]建议：继续在 module.yaml 中调大 max_tokens，或精简 Prompt 中的内容。[/dim]")
                
                return response, duration
            except Exception as e:
                # 检查是否为超时异常
                if "timeout" in str(e).lower():
                    console.print(f"\n[bold red]✕ {model_name} 请求超时 ({timeout_val}s)！[/bold red]")
                else:
                    logger.exception(f"API call to {model_name} failed")
                    console.print(f"\n[red]API 调用发生错误: {e}[/red]")
                return None, 0

def print_beautiful_help():
    title = Text("\n🧬 Single Cell AI Annotator", style="bold magenta")
    console.print(title)
    desc = "基于 AI 大模型的单细胞集群自动化注释工具。\n模型配置：[cyan]module.yaml[/cyan] | 任务配置：[cyan]config.json[/cyan]"
    console.print(Panel(desc, title="[cyan]工具描述[/cyan]", expand=False))
    table = Table(title="[bold yellow]参数说明[/bold yellow]", header_style="bold cyan", show_lines=True)
    table.add_column("参数 (Short/Long)", style="green", no_wrap=True)
    table.add_column("说明", style="white")
    table.add_row("-j, --project", "项目 ID/名称，用于区分日志和任务。")
    table.add_row("-c, --config", "指定任务 JSON 配置文件。")
    table.add_row("-i, --csv", "Marker 差异基因 CSV 文件路径。")
    table.add_row("-s, --species", "样本物种信息。")
    table.add_row("-o, --out", "结果保存路径。")
    console.print(table)

def get_args():
    parser = argparse.ArgumentParser(description="单细胞 AI 注释工具", add_help=False)
    parser.add_argument("-h", "--help", action="store_true")
    parser.add_argument("-j", "--project", type=str, help="项目名称")
    parser.add_argument("-c", "--config", type=str, help="配置文件路径")
    parser.add_argument("-i", "--csv", type=str, help="差异基因 CSV 路径")
    parser.add_argument("-o", "--out", type=str, help="输出文件路径")
    parser.add_argument("-p", "--prompt", type=str, help="Prompt 文件路径")
    parser.add_argument("-n", "--top-n", type=int, help="Top 基因数")
    parser.add_argument("-s", "--species", type=str, help="物种")
    parser.add_argument("-t", "--tissue", type=str, help="组织")
    parser.add_argument("-d", "--condition", type=str, help="条件")
    return parser

def merge_config(args):
    config = {
        "project_id": "default_proj",
        "prompt_file": "annotation_prompt.md",
        "csv_file": None,
        "output_file": "AI_annotation_result.md",
        "background": {"species": "未知", "tissue": "未知", "condition": "未知"},
        "top_n": 30
    }
    target_config_file = args.config if args.config else "config.json"
    if os.path.exists(target_config_file):
        with open(target_config_file, 'r', encoding='utf-8') as f:
            file_conf = json.load(f)
            if "background" in file_conf:
                config["background"].update(file_conf["background"])
                del file_conf["background"]
            config.update(file_conf)
    if args.project: config["project_id"] = args.project
    if args.csv: config["csv_file"] = args.csv
    if args.out: config["output_file"] = args.out
    if args.prompt: config["prompt_file"] = args.prompt
    if args.top_n: config["top_n"] = args.top_n
    if args.species: config["background"]["species"] = args.species
    if args.tissue: config["background"]["tissue"] = args.tissue
    if args.condition: config["background"]["condition"] = args.condition
    return config

def main():
    parser = get_args()
    args = parser.parse_args()
    if len(sys.argv) == 1 or args.help:
        print_beautiful_help()
        sys.exit(0)

    module_config = load_module_config()
    config = merge_config(args)
    if not config.get("csv_file"):
        console.print("[bold red]错误: 必须指定输入数据文件！[/bold red]")
        sys.exit(1)

    log_file = init_detailed_logging(config["project_id"])
    logger.info(f"--- Task Started: Project={config['project_id']} ---")

    provider = module_config['model_provider']
    table = Table(box=None, show_header=False)
    table.add_row("[cyan]Project:[/cyan]", f"[bold]{config['project_id']}[/bold]")
    table.add_row("[cyan]AI Engine:[/cyan]", f"{provider.get('name')} ({provider.get('model_id')})")
    table.add_row("[cyan]Log File:[/cyan]", f"[dim]{log_file}[/dim]")
    table.add_row("[cyan]Species/Tissue:[/cyan]", f"{config['background']['species']} / {config['background']['tissue']}")
    console.print(Panel(table, title="[bold blue]Annotation Engine Active[/bold blue]", expand=False))

    try:
        annotator = SingleCellAnnotator(module_config)
        system_prompt = annotator.load_system_prompt(config["prompt_file"])
        csv_data_str = annotator.load_and_format_csv(config["csv_file"], top_n=config["top_n"])
        
        bg = config["background"]
        bg_str = f"物种：{bg['species']}。组织：{bg['tissue']}。状态：{bg['condition']}。"
        
        response, duration = annotator.annotate(system_prompt, bg_str, csv_data_str)

        if response:
            ai_reply = response.choices[0].message.content
            usage = response.usage
            
            # 计算费用
            i_price = parse_price(provider.get('input_price', 0))
            o_price = parse_price(provider.get('output_price', 0))
            i_cost = (usage.prompt_tokens / 1000000) * i_price
            o_cost = (usage.completion_tokens / 1000000) * o_price
            total_cost = i_cost + o_cost

            with open(config["output_file"], 'w', encoding='utf-8') as f:
                f.write(ai_reply)
            
            console.print(f"\n[bold green]✓ 注释完成！结果已存至 {config['output_file']}[/bold green]")
            console.print("\n[dim]结果预览:[/dim]")
            console.print(Panel(Markdown(ai_reply[:500] + "..."), border_style="dim"))
            
            tps = usage.completion_tokens / duration if duration > 0 else 0
            stats_str = (
                f"[dim]Tokens: {usage.total_tokens} (P: {usage.prompt_tokens}, C: {usage.completion_tokens}) | "
                f"Speed: {tps:.2f} tokens/s | Time: {duration:.2f}s[/dim]\n"
                f"[dim]Cost:   Input: ￥{i_cost:.6f}, Output: ￥{o_cost:.6f}, Total: ￥{total_cost:.6f}[/dim]"
            )
            console.print(stats_str)
            
            logger.info(f"Usage Stats - Prompt: {usage.prompt_tokens}, Completion: {usage.completion_tokens}, Total: {usage.total_tokens}")
            logger.info(f"Cost Breakdown - Input: ￥{i_cost:.6f}, Output: ￥{o_cost:.6f}, Total: ￥{total_cost:.6f}")
            logger.info(f"Performance - Time: {duration:.2f}s, Speed: {tps:.2f} tokens/s")
            
    except Exception as e:
        logger.critical(f"Unhandled exception: {e}", exc_info=True)
        console.print(f"[bold red]运行时出错: {e}[/bold red]")

if __name__ == "__main__":
    main()
