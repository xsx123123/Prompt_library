---
### 第一部分：各Cluster详细解析
#### Cluster 0
1. **推断结论**
   - Level 1: Epidermis（表皮）
   - Level 2: Homeostatic epidermal cells（稳态表皮细胞）
2. **推断依据与Marker解析**
   - Level 1 依据：高表达脂质转移蛋白家族基因（IPR注释明确为脂质转移蛋白DIR1-like、植物脂质转移蛋白结构域），是植物表皮细胞合成角质层的经典特异性Marker，p_val_adj均小于1e-200，特异性极强；同时高表达阿拉伯半乳糖蛋白（AGP），为表皮细胞壁常见成分。
   - Level 2 依据：未检测到增殖或应激相关Marker，为成熟稳态的表皮细胞。
3. **污染/Doublet评估**：无跨组织Marker共表达，无质体或应激污染，判定为正常细胞。

#### Cluster 1
1. **推断结论**
   - Level 1: Meristem（分生组织）
   - Level 2: Proliferating meristematic cells（增殖态分生细胞）
2. **推断依据与Marker解析**
   - Level 1 依据：高表达全套组蛋白家族基因（H1、H2A、H2B、H3、H4），组蛋白活跃表达是细胞分裂间期DNA复制的典型特征，为茎尖分生组织细胞的核心Marker，所有组蛋白基因p_val_adj均为0，特异性极强。
   - Level 2 依据：组蛋白高表达指示细胞处于活跃增殖状态，无M期特异性Marker，为间期增殖细胞。
3. **污染/Doublet评估**：无跨组织Marker共表达，无其他污染，判定为正常细胞。

#### Cluster 3
1. **推断结论**
   - Level 1: Unknown
   - Level 2: Unknown
2. **推断依据与Marker解析**
   - 仅检测到2个差异基因，分别为甘氨酸富集蛋白、富亮氨酸重复类伸展蛋白，均为细胞壁通用成分，无明确组织特异性功能注释，不足以判定细胞类型。
3. **污染/Doublet评估**：无跨组织Marker共表达，无明显污染，需后续补充Marker验证。

#### Cluster 6
1. **推断结论**
   - Level 1: Unknown
   - Level 2: Unknown
2. **推断依据与Marker解析**
   - 仅检测到1个差异基因，为硫胺素噻唑合成酶（Thi4家族），为质体通用代谢酶，无明确组织特异性，不足以判定细胞类型。
3. **污染/Doublet评估**：无明显污染，需后续补充Marker验证。

#### Cluster 7
1. **推断结论**
   - Level 1: Meristem（分生组织）
   - Level 2: Proliferating meristematic cells（增殖态分生细胞）
2. **推断依据与Marker解析**
   - Level 1 依据：与Cluster 1类似，高表达全套组蛋白家族基因（H1、H2A、H2B、H3、H4），所有差异基因p_val_adj均为0，为分生组织的典型特征。
   - Level 2 依据：组蛋白高表达指示细胞处于活跃DNA复制/增殖状态。
3. **污染/Doublet评估**：无跨组织Marker共表达，无其他污染，判定为正常细胞。

#### Cluster 8
1. **推断结论**
   - Level 1: Epidermis（表皮）
   - Level 2: Differentiated epidermal cells（分化态表皮细胞）
2. **推断依据与Marker解析**
   - Level 1 依据：高表达植物非特异性脂质转移蛋白（nsLTP，PF00234结构域），为表皮细胞经典Marker，p_val_adj为0，特异性极强；同时高表达甘氨酸富集蛋白，为表皮细胞壁常见成分。
   - Level 2 依据：无增殖Marker，为分化成熟的表皮细胞。
3. **污染/Doublet评估**：无跨组织Marker共表达，无其他污染，判定为正常细胞。

#### Cluster 9
1. **推断结论**
   - Level 1: Stele（中柱/维管组织）
   - Level 2: Developing vascular cells（发育中维管细胞）
2. **推断依据与Marker解析**
   - Level 1 依据：高表达WAT1（WALLS ARE THIN 1）同源基因，拟南芥WAT1特异性表达于维管组织，调控次生壁沉积和木质部分化，为中柱组织的可靠Marker。
   - Level 2 依据：WAT1表达指示细胞处于维管分化早期阶段。
3. **污染/Doublet评估**：无跨组织Marker共表达，无其他污染，可信度中等，需补充维管Marker验证。

#### Cluster 11
1. **推断结论**
   - Level 1: Stele（中柱/维管组织）
   - Level 2: Developing vascular cells（发育中维管细胞）
2. **推断依据与Marker解析**
   - Level 1 依据：高表达热精胺合成酶ACL5（ACAULIS5，拟南芥同源基因AT5G19530），ACL5特异性表达于维管组织，调控导管分子分化；同时高表达WAT1同源基因，均为维管组织的核心Marker。此外检测到生长素响应蛋白IAA、Dof锌指转录因子，参与维管发育调控。
   - Level 2 依据：ACL5、WAT1表达指示细胞处于活跃的维管分化状态。
3. **污染/Doublet评估**：无跨组织Marker共表达，无其他污染，可信度中等。

#### Cluster 14
1. **推断结论**
   - Level 1: Unknown
   - Level 2: Unknown
2. **推断依据与Marker解析**
   - 仅检测到2个差异基因，分别为果胶裂解酶、橡胶延伸因子（REF），均为细胞壁代谢通用基因，无明确组织特异性，不足以判定细胞类型。
3. **污染/Doublet评估**：无明显污染，需后续补充Marker验证。

#### Cluster 16
1. **推断结论**
   - Level 1: Meristem（分生组织）
   - Level 2: Mitotic (M-phase) meristematic cells（有丝分裂期分生细胞）
2. **推断依据与Marker解析**
   - Level 1 依据：高表达一系列细胞有丝分裂M期特异性Marker，包括纺锤体组装相关TPX2、G2/M期Cyclin B、细胞板形成相关KNOLLE（syntaxin）、纺锤体检查点蛋白Mad2、驱动蛋白Kinesin等，均为分裂期分生细胞的特征性Marker，p_val_adj均为0，特异性极强。
   - Level 2 依据：所有Marker均指向细胞处于有丝分裂M期，为分生组织中正在进行细胞分裂的亚群。
3. **污染/Doublet评估**：无跨组织Marker共表达，无其他污染，判定为正常细胞。

#### Cluster 17
1. **推断结论**
   - Level 1: Epidermis（表皮）
   - Level 2: Homeostatic epidermal cells（稳态表皮细胞）
2. **推断依据与Marker解析**
   - Level 1 依据：高表达阿拉伯半乳糖蛋白（AGP9/17/18），为表皮细胞壁的特征性成分；同时高表达质膜水通道蛋白PIP1，在表皮细胞中普遍高表达用于水分运输。
   - Level 2 依据：无增殖或应激Marker，为稳态表皮细胞。
3. **污染/Doublet评估**：无跨组织Marker共表达，无其他污染，可信度中等，需补充表皮特异性Marker验证。

#### Cluster 18
1. **推断结论**
   - Level 1: Unknown
   - Level 2: Unknown
2. **推断依据与Marker解析**
   - 仅检测到1个无任何功能注释的差异基因，无有效信息支持细胞类型判定。
3. **污染/Doublet评估**：无明显污染，需后续人工复核。

#### Cluster 19
1. **推断结论**
   - Level 1: Stele（中柱/维管组织）
   - Level 2: Developing tracheary elements (PCD stage)（发育中导管分子，程序性死亡阶段）
2. **推断依据与Marker解析**
   - Level 1 依据：高表达木瓜类半胱氨酸蛋白酶，为导管分子分化过程中程序性细胞死亡（PCD）的核心Marker，拟南芥中该类酶特异性表达于正在分化的木质部导管细胞。同时高表达异黄酮还原酶类，参与木质素前体代谢，支持维管组织身份。
   - Level 2 依据：半胱氨酸蛋白酶高表达指示细胞处于PCD阶段，为分化后期的导管分子。
3. **污染/Doublet评估**：无跨组织Marker共表达，无其他污染，可信度中等。

#### Cluster 21
1. **推断结论**
   - Level 1: Unknown
   - Level 2: Unknown
2. **推断依据与Marker解析**
   - 仅检测到1个植蓝素（Phytocyanin）家族基因，为细胞壁通用铜蛋白，无明确组织特异性，不足以判定细胞类型。
3. **污染/Doublet评估**：无明显污染，需后续补充Marker验证。

#### Cluster 23
1. **推断结论**
   - Level 1: Stress-responsive cells（应激响应细胞）
   - Level 2: ROS scavenging stress-responsive cells（活性氧清除型应激细胞）
2. **推断依据与Marker解析**
   - Level 1 依据：高表达一系列活性氧清除、重金属解毒相关基因，包括硫氧还蛋白、重金属结合蛋白HIPP、金属硫蛋白、紫色酸性磷酸酶，均为细胞应对氧化胁迫的典型Marker。
   - Level 2 依据：所有Marker均指向活性氧清除通路，可能为原生质体制备过程中诱导的应激细胞亚群，或茎尖中固有胁迫响应细胞。
3. **污染/Doublet评估**：无跨组织Marker共表达，无其他污染，可信度中等，建议结合应激基因特征进一步验证。

#### Cluster 24
1. **推断结论**
   - Level 1: Epidermis（表皮）
   - Level 2: Protodermal (L1 layer) meristematic cells（原表皮层（L1层）分生细胞）
2. **推断依据与Marker解析**
   - Level 1 依据：高表达原表皮因子1（Protodermal factor 1, PDF1），为茎尖分生组织最外层L1层（原表皮）的经典特异性Marker，拟南芥中PDF1仅在原表皮细胞表达，特异性极强。同时高表达甘氨酸富集蛋白，为原表皮细胞壁成分。
   - Level 2 依据：PDF1是茎尖分生组织原表皮层的特征性Marker，指示细胞为未完全分化的原表皮分生细胞。
3. **污染/Doublet评估**：无跨组织Marker共表达，无其他污染，可信度极高。

#### Cluster 25
1. **推断结论**
   - Level 1: Unknown
   - Level 2: Unknown
2. **推断依据与Marker解析**
   - 仅检测到1个无任何功能注释的差异基因，无有效信息支持细胞类型判定。
3. **污染/Doublet评估**：无明显污染，需后续人工复核。

#### Cluster 26
1. **推断结论**
   - Level 1: Meristem（分生组织）
   - Level 2: Proliferating meristematic cells（增殖态分生细胞）
2. **推断依据与Marker解析**
   - Level 1 依据：高表达全套组蛋白家族基因（H1、H2A、H2B、H3、H4），p_val_adj均接近0，为分生组织细胞的典型特征。
   - Level 2 依据：组蛋白高表达指示细胞处于活跃DNA复制/增殖状态。
3. **污染/Doublet评估**：无跨组织Marker共表达，无其他污染，判定为正常细胞。

#### Cluster 28
1. **推断结论**
   - Level 1: Unknown
   - Level 2: Unknown
2. **推断依据与Marker解析**
   - 仅检测到2个差异基因，分别为BURP结构域蛋白、水通道蛋白NIP2-1，均为通用功能蛋白，无明确组织特异性，不足以判定细胞类型。
3. **污染/Doublet评估**：无明显污染，需后续补充Marker验证。
---
### 第二部分：全景注释汇总表
| Cluster | Level 1: 细胞大类 | Level 2: 具体亚型/状态 | 关键 Marker (或同源功能) | 可信度 (High/Medium/Low) | 备注 |
|---------|------------------|----------------------|------------------------|----------------|------|
| 0 | Epidermis | Homeostatic epidermal cells | Lipid transfer protein, Arabinogalactan protein | High | 经典表皮细胞特征 |
| 1 | Meristem | Proliferating meristematic cells | Histone H1/H2A/H2B/H3/H4 | High | 间期增殖态分生细胞 |
| 3 | Unknown | Unknown | Glycine rich protein, LRR extensin-like | Low | 缺乏组织特异性Marker，需验证 |
| 6 | Unknown | Unknown | Thiamine thiazole synthase (Thi4) | Low | 仅检测到通用代谢酶，需验证 |
| 7 | Meristem | Proliferating meristematic cells | Histone H1/H2A/H2B/H3/H4 | High | 间期增殖态分生细胞 |
| 8 | Epidermis | Differentiated epidermal cells | Non-specific lipid transfer protein (nsLTP) | High | 分化成熟表皮细胞 |
| 9 | Stele | Developing vascular cells | WAT1 (WALLS ARE THIN 1) | Medium | 维管发育早期细胞，需补充Marker验证 |
| 11 | Stele | Developing vascular cells | ACL5 (ACAULIS5), WAT1, AUX/IAA | Medium | 活跃分化的维管细胞 |
| 14 | Unknown | Unknown | Pectate lyase, Rubber elongation factor | Low | 仅检测到细胞壁代谢通用基因，需验证 |
| 16 | Meristem | Mitotic (M-phase) meristematic cells | TPX2, Cyclin B, KNOLLE, Mad2, Kinesin | High | 有丝分裂期分生细胞亚群 |
| 17 | Epidermis | Homeostatic epidermal cells | Arabinogalactan protein (AGP), PIP1 aquaporin | Medium | 推测为表皮细胞，需验证 |
| 18 | Unknown | Unknown | 无功能注释基因 | Low | 无有效注释信息，需人工复核 |
| 19 | Stele | Developing tracheary elements (PCD stage) | Papain-like cysteine protease | Medium | 处于程序性死亡阶段的木质部导管细胞 |
| 21 | Unknown | Unknown | Phytocyanin (early nodulin-like) | Low | 仅检测到通用细胞壁蛋白，需验证 |
| 23 | Stress-responsive cells | ROS scavenging stress-responsive cells | Thioredoxin, HIPP, Metallothionein | Medium | 高表达抗氧化基因，可能为原生质体制备应激亚群 |
| 24 | Epidermis | Protodermal (L1 layer) meristematic cells | Protodermal factor 1 (PDF1) | High | 茎尖分生组织L1层原表皮细胞，特异性极高 |
| 25 | Unknown | Unknown | 无功能注释基因 | Low | 无有效注释信息，需人工复核 |
| 26 | Meristem | Proliferating meristematic cells | Histone H1/H2A/H2B/H3/H4 | High | 间期增殖态分生细胞 |
| 28 | Unknown | Unknown | BURP domain protein, NIP2-1 aquaporin | Low | 缺乏组织特异性Marker，需验证 |
---
### 第三部分：自动化提取JSON输出
```json
{
  "annotations": [
    {
      "cluster": "0",
      "level_1": "Epidermis",
      "level_2": "Homeostatic epidermal cells",
      "key_markers": ["Lipid transfer protein", "Arabinogalactan protein"],
      "confidence": "High",
      "is_doublet": false
    },
    {
      "cluster": "1",
      "level_1": "Meristem",
      "level_2": "Proliferating meristematic cells",
      "key_markers": ["Histone H1", "Histone H2A", "Histone H2B", "Histone H3", "Histone H4"],
      "confidence": "High",
      "is_doublet": false
    },
    {
      "cluster": "3",
      "level_1": "Unknown",
      "level_2": "Unknown",
      "key_markers": ["Glycine rich protein", "LRR extensin-like"],
      "confidence": "Low",
      "is_doublet": false
    },
    {
      "cluster": "6",
      "level_1": "Unknown",
      "level_2": "Unknown",
      "key_markers": ["Thiamine thiazole synthase (Thi4)"],
      "confidence": "Low",
      "is_doublet": false
    },
    {
      "cluster": "7",
      "level_1": "Meristem",
      "level_2": "Proliferating meristematic cells",
      "key_markers": ["Histone H1",