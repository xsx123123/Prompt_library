# sc-Annotation Agent: 从线性脚本到智能科学家

本项目旨在将传统的“数据驱动型”单细胞注释脚本升级为一个具有**自主推理、外部知识检索和自我修正能力**的智能体（Agent）。

## 1. 项目现状 (Current State)

目前的流程是一个**线性自动化脚本**：
- **输入**：包含差异表达基因（DEGs）的 CSV 文件。
- **处理**：
    - 预处理数据（保留 Top 15 Markers 并提取 InterPro/GO 描述）。
    - 结合 `module.yaml` 配置的 LLM（如 Doubao-2.0）发送单次 Prompt。
    - 使用预设的系统提示词（`prompt/*.md`）进行推理。
- **输出**：生成 JSON 格式的注释结果和 Markdown 报告。
- **局限**：
    - **知识孤岛**：仅依赖模型预训练知识，无法实时验证罕见基因。
    - **单向决策**：缺乏自检机制，容易产生生物学常识错误（幻觉）。
    - **静态参考**：本地参考 CSV（如 `plant_marker_ann.csv`）未与模型深度集成。

---

## 2. Agent 升级目标 (The Vision)

升级后的 **sc-Annotation Agent** 将作为一个“数字科学家”工作，具备以下特质：
1. **主动探索**：遇到不确定的 Marker 时，自动通过 **MyGene.info API** 检索功能背景。
2. **多维思考**：不仅看 Fold Change，还能理解组织背景约束。
3. **闭环审阅**：引入“标注者-审阅者”对抗机制，确保结果符合生物学常识。
4. **长效记忆**：记录注释逻辑，保持多样本间命名的一致性。

---

## 3. Agent 架构设计 (Architecture)

### 3.1 核心组件 (Core Modules)

| 组件 | 名称 | 职责 |
| :--- | :--- | :--- |
| **Brain (LLM)** | 推理引擎 | 基于 ReAct (Thought/Act/Observation) 框架进行任务调度。 |
| **Tools** | 技能插件 | `Search_Gene_Info` (MyGene API), `Local_DB_Lookup`, `Python_Executor`。 |
| **Memory** | 知识上下文 | 存储样本背景、物种信息及已确认的标注逻辑。 |
| **Validator** | 逻辑守卫 | 检查标注结果是否违反组织特异性或 Marker 互斥逻辑。 |

### 3.2 关键工作流 (The Loop)
1. **任务接收**：解析 DEGs 数据，提取 Top Markers。
2. **初步思考**：AI 分析初步特征，识别“模糊基因”。
3. **工具调用**：**[关键步]** 调用 `MyGene.info` 获取基因功能摘要、同源信息。
4. **合成推理**：结合外部证据和本地参考库（`test/*.csv`）生成注释初稿。
5. **自我审阅**：Validator 模块进行查错（如：植物根部出现叶肉细胞）。
6. **最终交付**：输出带证据链（Evidence Trace）的结构化报告。

---

## 4. 待开发任务清单 (Roadmap)

### 第一阶段：能力增强 (Tools Integration)
- [ ] **MyGene 工具集成**：封装 `MyGeneInfoClient`，支持根据物种查询基因 Summary。
- [ ] **本地知识库集成**：让 Agent 能自动读取并参考 `plant_marker_ann.csv` 等本地数据。
- [ ] **Prompt 升级**：编写支持 `Action/Observation` 结构的 ReAct 提示词。

### 第二阶段：逻辑闭环 (Reasoning & Review)
- [ ] **实现 Reflection 循环**：增加一轮“自我批评”提示词，强制 AI 寻找标注漏洞。
- [ ] **组织背景约束库**：建立一个简单的 `tissue_constraints.json`（例如：脑 = 无上皮细胞）。

### 第三阶段：交互与优化 (UI & UX)
- [ ] **证据可视化**：在最终报告中展示 Agent 查询 MyGene 的原始记录。
- [ ] **置信度评分**：为每个 Cluster 的注释结果标注置信度分数等级。

---

## 5. 预期文件结构 (Future Structure)

```text
scRNA-seq/Annotation/
├── agents/
│   ├── annotator.py       # 标注执行逻辑
│   └── reviewer.py        # 结果审阅逻辑
├── tools/
│   ├── mygene_api.py      # MyGene.info 接口封装
│   └── local_db.py        # 本地 CSV 检索工具
├── prompt/
│   ├── react_core.md      # 核心推理提示词
│   └── reviewer_logic.md  # 审阅逻辑提示词
├── knowledge/
│   └── tissue_map.yaml    # 组织-细胞类型先验约束
└── cluster_agent_main.py  # Agent 入口程序
```

---

## 6. 开发笔记 (Notes)
- *注意：* 处理植物数据时，MyGene 的覆盖度可能有限，需优先保障同源基因映射逻辑。
- *注意：* 调用的 `doubao-seed-2-0-pro` 具备超长上下文，可一次性喂入更多基因背景。
