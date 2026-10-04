---
id: 2026_foresci-evaluating-llm-agents-for-forward-looking-ai-res_3634-foresci-evaluating-llm-ag
title: "ForeSci: Evaluating LLM Agents for Forward-Looking AI Research Judgment"
year: 2026
authors: []
venue: ""
field:
  - AI
  - Science of Science
direction:
  - Research Agents
  - Scientific Forecasting
keywords:
  - ForeSci
  - research agents
  - future alignment
status: read
source_path: ../sources/2026_foresci-evaluating-llm-agents-for-forward-looking-ai-res_3634-foresci-evaluating-llm-ag.pdf
source_archive_path: ""
assets_path: ../assets/2026_foresci-evaluating-llm-agents-for-forward-looking-ai-res_3634-foresci-evaluating-llm-ag
paper_type: benchmark
---

# ForeSci: Evaluating LLM Agents for Forward-Looking AI Research Judgment

## 一句话总结

ForeSci 用严格时间截断的 500 个任务评估 LLM 及 research agent 对未来 AI 研究方向的判断能力，并将生成时可用的历史证据与事后验证证据分离。

## 研究问题

在只能访问问题截止时间之前知识的条件下，LLM agent 能否对方向预测、瓶颈与机会发现、战略研究规划和投稿定位作出可追溯且与未来发展一致的判断？

## 核心方法

从四个快速发展的 AI 领域构造 cutoff-aligned 离线知识库和四类决策任务，用原生 LLM、Hybrid RAG 与研究代理进行回答，并从事实支持、未来目标对齐、证据可追溯性和评审说服力四个维度评价。

## 分章节阅读笔记

### 1 Introduction

ForeSci 将 research-agent 评测从“能否回答已有文献问题”推进到“在历史截点上能否作出面向未来的研究判断”。论文构造 500 个任务，覆盖 LLM agents、LLM fine-tuning/post-training、RAG/retrieval structuring 和 visual generative modeling 四个快速变化领域，并严格隐藏 cutoff 之后的论文。核心难点是同时控制信息边界和任务可推断性，避免系统利用 hindsight 或随机猜测未来事件。

### 2 Related Work

作者将 ForeSci 与 autonomous research agent、scientific forecasting 和 temporal-integrity benchmark 区分开来。已有工作多测 literature QA、代码执行、idea novelty 或未来论文相似度；ForeSci 关注宏观研究决策，包括方向预测、瓶颈与机会发现、战略规划和 venue positioning。

### 3 The ForeSci Framework

给定问题 `q`、cutoff `t`、截止时间前知识库 `K<=t` 和任务类型 `f`，系统只能从 `K<=t` 生成答案，cutoff 之后的验证目标 `G>t` 只在评估时可见。数据构建先收集并筛选领域论文，再诱导随时间演化的 taxonomy graph，抽取方向、方法演化、瓶颈、可行性/风险和 venue-community 等证据资产。

#### 3.1 Problem Formulation

问题形式要求 agent 输出一个面向未来的研究判断，而不是复述一篇已发表论文。生成 backbone 在相关 cutoff 前已发布，禁用 web search，所有外部证据来自离线知识库，从而把“研究能力”与“未来信息泄漏”分开。

#### 3.2 Data Collection and Filtering

四个领域共形成数千篇 cutoff-aligned 文档和 500 个任务。作者先做领域相关性筛选，再做 benchmark-core 筛选，保留能支撑方向、瓶颈和方法演化判断的核心/支持论文，并按三个月、六个月或 venue deadline 形成不同时间边界。

#### 3.3 Taxonomy Construction

每个领域和 cutoff 构建动态图 `T(d,t)=(V,E)`，节点聚合代表性论文和支持论文，边记录方法演化。LLM 初步抽取 taxonomy 与高阶信号，人工专家检查证据强度和时间有效性；这样任务选项不是凭空生成，而是从历史可见的研究轨迹中构造。

#### 3.4 Task Families

四类任务分别要求预测会加速的技术方向、识别根瓶颈及其一跳机会、在约束下排序研究议程、以及将项目定位到合适 venue/community。每类任务的隐藏目标由 cutoff 后的方法演化、瓶颈变化或 venue 信号诱导，并与 cutoff 前证据对齐。

### 4 Evaluation

ForeSci 使用四个互补指标：Prediction Factuality 检查原子事实支持，Future-Target Alignment 检查是否选对未来方向/排序，Evidence Traceability 检查判断是否能回溯到可见证据，Reviewer Persuasiveness 以任务特定 rubric 评价论证质量。四项分开报告，避免“引用很多但方向错”被单一总分掩盖。

### 5 Results

实验比较 native LLM、Hybrid RAG 以及 CoI-style、ResearchAgent-style、ARIS-style 三种离线适配 agent，覆盖 Qwen3-235B、GPT-5.2、GLM-4.6 和 Gemini-3 等 backbone。总体上 agent workflow 往往提高 traceability 和部分 factuality，但最优方法随任务族、backbone 和指标变化，没有一个系统全面胜出。

#### 5.1 Evaluation of LLM Agents

显式证据组织通常比纯 native LLM 更可追溯；但 retrieval 质量并不自动转化为正确研究选择。不同 agent 在 direction forecasting、bottleneck discovery、planning 和 venue positioning 上表现不一致，说明 research judgement 不是单一能力。

#### 5.2 Diagnostic Audit

作者发现 evidence-decision decoupling：系统可能引用了相关论文，却预测了错误的研究对象、因果角色、干预方式或时间范围。这个失败模式解释了为什么 factuality/traceability 较高时，future-target alignment 仍可能较低。

#### 5.3 Prospective Use: Dynamic Forecasting Beyond Retrospective Evaluation

同一构建管线可在新 cutoff 上生成未评分的 prospective forecast artifacts。该模式让 benchmark 随新文献刷新，并把研究 agent 的答案、证据和未来验证目标保存为可审计的时间切片。

### 6 Conclusion

ForeSci 证明，面向未来的 AI research judgement 可以被转化为具有严格时间边界、离线知识库和隐藏未来目标的 benchmark。实验显示，agentic workflow 在证据可追溯性和部分事实支持上有帮助，但不能保证研究方向判断正确；最重要的诊断是“证据—决策脱钩”。因此评测研究 agent 时，应把事实、未来目标、证据使用和说服力分开测量，而不是把文献引用数量当作 foresight 的代理。

## 关键公式 / 图表

### 关键图

### 关键表格

## 实验结论

核心结论是“有证据”与“作出正确的未来决策”是两件事。ForeSci 的时间截断和 prospective 模式为研究 agent 提供了可重复的未来对齐评测，但结果只支持受控 AI 领域和任务族内的结论。

## 局限性与可追问点

- 任务集中在四个快速变化的 AI 子领域，不能直接代表其他科学领域。
- 未来目标、事实和 persuasive rubric 部分依赖 LLM judge 与人工构造，仍存在评价偏差。
- 论文测的是论文可见信号，无法覆盖未发表工作、私有实验和 tacit community knowledge。
- 需要研究更长预测窗口、跨语言任务以及真正在线部署后的 calibration。

## 对我当前研究/项目的启发

对科研判断系统，应把“证据是否支持”“预测是否命中未来目标”“证据是否真的支撑决策”拆成独立字段和审计步骤；研究 proposal 生成不能只用引用相似度或流畅度作为目标。
