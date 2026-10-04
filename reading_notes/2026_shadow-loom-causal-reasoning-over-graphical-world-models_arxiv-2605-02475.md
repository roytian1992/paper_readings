---
id: 2026_shadow-loom-causal-reasoning-over-graphical-world-models_arxiv-2605-02475
title: "Shadow-Loom: Causal Reasoning over Graphical World Models of Narratives"
year: 2026
authors:
  - David Wilmot
venue: ""
field:
  - Artificial Intelligence
  - Natural Language Processing
direction:
  - Narrative World Models
  - Causal Reasoning
keywords:
  - Shadow-Loom
  - mystery
  - dramatic irony
  - suspense
  - surprise
status: read
source_path: ../sources/2026_shadow-loom-causal-reasoning-over-graphical-world-models_arxiv-2605-02475.pdf
source_archive_path: ""
assets_path: ../assets/2026_shadow-loom-causal-reasoning-over-graphical-world-models_arxiv-2605-02475
paper_type: system
---

# Shadow-Loom: Causal Reasoning over Graphical World Models of Narratives

## 一句话总结

Shadow-Loom 提出一个把事实/反事实世界、角色信念、fabula/syuzhet 时间与 mystery、irony、suspense、surprise 评分放在一起的类型化图流水线，但目前只有手写 fixture 的内部回归证据。

## 研究问题

作者希望叙事系统既能做结构化因果与心智推断，又能把结果约束性地渲染成文本，并用可审计中间状态避免让 LLM 自由文本推理承担全部正确性。

## 核心方法

`WorldStateV1` 包含实体、事件、信念、地点、信息通道与因果/社会/空间边，保存 fabula time、syuzhet index 和 factual/shadow `world_id`。版本 DAG 以 sibling fork 表示 counterfactual，不改写 canon。LLM 负责抽取、CreativeBrief 和渲染，确定性代码负责图运算、叙事评分、审计与重试。

## 分章节阅读笔记

### 1 Introduction

论文把贡献定位为已有因果、叙事学、ToM 与工程模式的组合，而非单个新算法，并强调 LLM 只位于系统边界。

### 2 Pipeline overview

五阶段为多 agent 抽取/校验、causal physics、narrative physics、typed brief + constrained renderer、再抽取审计/重试。工具接口约四十项。

### 3 Formal model and narrative metrics

因果层使用 observation、do 和 counterfactual 术语，以 Impact、Inertia、affordance gating 更新。叙事层对 mystery、dramatic irony、suspense、surprise 及 trait trajectories 打分。这里是工程定义，不是可识别 SCM 的估计过程。

### 4 Internal sanity checks

20 个 hand-authored `example_worlds` fixtures 各取 7 个 syuzhet anchors。每项 metric 有 162 个有效评价；mystery 最小/中位/最大约 0.17/0.53/1，irony 0/0.45/0.90，suspense 0/0.16/0.39，surprise 0/0.03/0.24。canonical signatures 用于回归，但没有外部 ground truth。

### 5 Rationale for the design choices

作者解释类型化状态、版本 DAG、双时间轴、边界 LLM 和结构化 brief 的取舍；这些选择主要以可审计性和故障隔离为依据。

### 7 Limitations and future evaluation

没有外部数据或 headline benchmark；指标尚未经 reader validation；抽取误差会传播；当前证据是 unit-test/fixture 级。未来工作包括人评、消融和系统基线。

### Appendices

附录给出 schema、Macbeth 等 fixture、评分 worked examples 和 UI/MCP 细节。论文称代码采用 AGPL-3.0-or-later 加平行商业许可，但指定 GitHub 仓库在 2026-07-15 返回 404，无法核对 LICENSE 或固定 revision。

## 关键公式 / 图表

### 关键图

### 关键表格

## 实验结论

现有数字只说明作者定义的 fixture 能产生预期曲线，不能证明文本抽取、反事实或读者效应在真实数据上有效。

## 局限性与可追问点

需要独立 benchmark、人工 reader validation、抽取准确率、与强基线的相同预算比较及可访问代码。因果术语目前不能支持 SCM identification claim。

## 对我当前研究/项目的启发

它是高度接近的同期概念邻居，因此本项目不能主张首次组合 world graph、belief、fabula/syuzhet 和 fork。差异必须通过 authority/legal projection、promotion 不变性、统一 substrate 对分离 stores 的受控实验、source-grounded adapters 与 generation/simulation 双任务证据建立。
