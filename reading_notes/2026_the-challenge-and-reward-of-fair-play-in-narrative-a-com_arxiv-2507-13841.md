---
id: 2026_the-challenge-and-reward-of-fair-play-in-narrative-a-com_arxiv-2507-13841
title: "The Challenge and Reward of Fair Play in Narrative: A Computational Approach"
year: 2026
authors:
  - Eitan Wagner
  - Renana Keydar
  - Omri Abend
venue: ""
field:
  - Natural Language Processing
  - Narrative Intelligence
direction:
  - Reader Modeling
  - Narrative Evaluation
keywords:
  - fair play
  - surprise
  - coherence
  - reader modes
  - detective fiction
status: read
source_path: ../sources/2026_the-challenge-and-reward-of-fair-play-in-narrative-a-com_arxiv-2507-13841.pdf
source_archive_path: ""
assets_path: ../assets/2026_the-challenge-and-reward-of-fair-play-in-narrative-a-com_arxiv-2507-13841
paper_type: research
---

# The Challenge and Reward of Fair Play in Narrative: A Computational Approach

## 一句话总结

论文把侦探故事中的 surprise、coherence 和 fair play 写成读者对凶手的概率更新问题，并指出揭晓前推断与揭晓后回看必须作为不同 reader modes 处理。

## 研究问题

一个结局若完全无法预料会显得不连贯，若一路显而易见又不惊讶。论文研究单一智能读者的惊讶-连贯权衡，以及公平推理故事如何借助“读完结局后重新解释旧线索”的 hindsight gap 同时取得两者。

## 核心方法

对每个故事前缀，reader model 输出 culprit 分布。作者区分 gullible、brilliant、actual 与 know-it-all readers，以交叉熵定义 weak/strong surprise，以 brilliant reader 对真凶的逐步支持定义 coherence。理论上，单一 reader 的 strong surprise 与 coherence 受 intelligence gap 上界约束；fair play 则比较 actual reader 在 forward 和 hindsight 模式下的差异。

## 分章节阅读笔记

### 2 The Probabilistic Framework

故事被表示为按段落展开的前缀，隐藏变量是 culprit。2.2--2.4 的理想 reader 类型不是心理学人口模型，而是用于分解信息不足、推理能力和外部真值访问的计算角色。

### 3 The Coherence-Surprise Tradeoffs

3.1--3.3 给出 surprise、coherence 和上界；故事越长，在同一智能差距下维持 strong surprise 与逐步 coherence 越难。3.4 的关键是 hindsight gap：实际读者看到 resolution 后能重新解释先前证据，因此 forward surprise 不必排斥 retrospective coherence。

### 4 Experimental Setup

生成故事为 25 段、每模型 10 篇，先由 o1-mini/o3-mini 过滤有效案例。指标使用多个 LLM reader 估计 culprit distributions；真实文本来自 Poirot 与 Sherlock Holmes，另做人类量表实验。

### 5 Results

100 篇生成故事中自动 coherence 与 surprise 的相关为 `r=-0.095`、不显著；36 篇有人类 coherence 的子集为 `r=-0.383`、`p<.05`。真实故事中 Poirot 更惊讶（0.642 vs 0.342），Sherlock 人评 coherence 更高（0.751 vs 0.661），但 fair-play 指标 Poirot 更高（0.325 vs 0.067）。54 篇有人评生成故事的平均 upper-bound/actual-reader fair play 为 0.242/0.127。

### 6 Discussion and Conclusion

主张是公平推理来自模式切换，而非一个静态 reader 同时“既知道又不知道”。主观 fairness 与 coherence 的相关（`r=.65`）明显高于与 surprise（`r=-.13`），但自动指标与人评只低度相关。

### 7 Methods

本节补充生成模型、reader estimation、统计检验和 20 人的人体实验细节。Data Availability 只承诺 acceptance 后公开；截至 2026-07-15 未找到可固定官方仓库。

## 关键公式 / 图表

### 关键图

### 关键表格

## 实验结论

理论和实验共同支持“揭晓前/揭晓后 reader mode 分离”。但指标更适合相对比较，不是绝对文学质量或公平性的定论。

## 局限性与可追问点

人类样本小；主 fair-play 指标是上界；设置限于 25 段、单一 distractor、已知 suspects 和 whodunit。读者可能利用模型生成这一元信息，mode collapse 也会混淆结果。自动 reader 与真实读者的相关性仍低。

## 对我当前研究/项目的启发

SharedWorldsPrivateMinds 应把 reader 在 reveal 前后的状态保存为不同 discourse-time projections，不能覆盖成一个状态；但这种 reader culprit distribution 不能冒充角色私有 belief ledger。该指标可做次级叙事评价，不应替代 authority、access 和 update correctness。
