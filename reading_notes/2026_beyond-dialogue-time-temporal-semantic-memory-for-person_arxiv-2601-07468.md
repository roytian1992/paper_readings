---
id: 2026_beyond-dialogue-time-temporal-semantic-memory-for-person_arxiv-2601-07468
title: "Beyond Dialogue Time: Temporal Semantic Memory for Personalized LLM Agents"
year: 2026
authors:
  - Miao Su
  - Yucan Guo
  - Zhongni Hou
  - Long Bai
  - Zixuan Li
  - Yufei Zhang
  - Guojun Yin
  - Wei Lin
  - Xiaolong Jin
  - Jiafeng Guo
  - Xueqi Cheng
venue: ""
field:
  - NLP
  - AI Agents
direction:
  - LLM Memory
  - Personalization
  - Retrieval
keywords:
  - Temporal Semantic Memory
  - TSM
  - semantic timeline
  - durative memory
  - personalized LLM agents
status: read
source_path: ""
source_archive_path: ../sources/2026_beyond-dialogue-time-temporal-semantic-memory-for-person_arxiv-2601-07468_source.tar.gz
assets_path: ../assets/2026_beyond-dialogue-time-temporal-semantic-memory-for-person_arxiv-2601-07468
paper_type: research
---

# Beyond Dialogue Time: Temporal Semantic Memory for Personalized LLM Agents

## 一句话总结

本文提出 Temporal Semantic Memory (TSM)，把个性化 LLM agent 的长期记忆从“按对话发生时间存取”推进到“按事件真实发生时间与持续状态存取”，从而更好地支持多轮、多会话和时间敏感的用户记忆问答。

## 研究问题

论文关注个性化对话 agent 中记忆的时间建模问题。作者指出，现有记忆系统通常把聊天轮次发生的 dialogue time 当成主要时间信号，但用户在对话中常常谈论过去事件、未来计划或持续状态，事件的实际发生时间与对话时间并不总是一致。与此同时，许多方法把记忆保存为孤立的 point-wise entries，容易把一段连续经历拆成碎片，难以恢复持续时间、长期偏好和演化状态。这两个问题会导致 agent 在检索长期记忆时出现时间错位或上下文不完整，尤其影响 temporal reasoning、multi-session understanding 和 knowledge update 类问题。

## 核心方法

TSM 的核心是把记忆组织为“语义时间线 + 持续性记忆”的层级结构。构建阶段先从对话中抽取带有效时间的事实，形成 temporal knowledge graph (TKG)，用它记录 episodic memory；随后按时间片和语义相关性聚合实体与对话上下文，形成 topic 和 persona 两类 durative memory，用来表示跨时间持续存在的主题、偏好和用户特征。利用阶段先解析查询中的 semantic-time constraint，再在 topic、persona 和 raw dialogue chunks 中做 dense retrieval，并用时间过滤、TKG 证据映射和时间优先的 reranking 返回更符合查询时间意图的记忆。更新机制上，TSM 用轻量在线图更新维护事实和有效时间，再周期性进行 summary consolidation，降低长期运行中的更新成本。

## 分章节阅读笔记

### 1 Introduction

作者指出，传统对话记忆通常按消息写入时间组织，但用户说“去年搬家”“下个月开始新工作”时，事件时间与对话时间不同。TSM 因此把 temporal grounding 作为个性化记忆的核心问题，并进一步区分一次性事件和跨时间持续的主题/人格状态。

### 2 Related Work

相关工作分为 agent memory 与 graph-structured memory 两类。前者提供对话摘要、向量检索和长期用户画像，但通常弱化真实事件时间；后者能够表达实体与关系，却常把时间当作普通属性，缺少对持续状态和语义时间约束的统一检索。TSM 的定位是把 temporal knowledge graph、层级摘要和时间感知检索放进同一条记忆管线。

### 2.1 Agent Memory

作者认为现有系统主要在“保存什么”和“怎么召回”上优化，却较少处理事实何时成立、何时失效以及用户状态如何延续。只按 embedding 相似度召回，容易把过时偏好与当前状态混合；只按最近对话召回，又无法回答跨会话的历史时间问题。

### 2.2 Graph-structured Memory

图结构适合连接人物、事件、主题和关系，但静态图难以表示“在某段时间内成立”的边。TSM 将有效时间、时间粒度和证据对话片段保留在图边/节点上，并让图结构服务于时间过滤与证据追溯，而不是仅作为关系可视化。

### 3 Methodology

方法由构建、利用和更新三部分组成。离线/初始构建将对话拆成带时间的事实和实体状态；在线查询先解析时间约束，再选择 episodic、topic、persona 或原始片段证据；更新阶段通过局部图修改和周期性 consolidation 控制长期成本。

### 3.1 Preliminary

论文区分 dialogue time 与 event time，并将事实表示为带有效区间的时间知识单元。时间既可以是明确日期，也可以是相对表达、顺序关系或未知值；系统不应把无法确定的时间强行归一化为精确时间。

### 3.2 Overview

TSM 的层级结构包括 episodic memory、topic memory 和 persona memory。episodic 层保留具体事件证据；topic 层把多个事件聚合为一段持续讨论；persona 层表示跨话题稳定但仍可更新的用户属性。查询时三层协同，既能回答“发生了什么”，也能回答“当时用户是什么状态”。

### 3.3 Duration-aware Memory Construction

构建阶段先抽取事实、主体、客体、关系和 temporal expression，再为事实附加有效起止时间、来源和置信度。持续性记忆不是简单复制事实，而是把在连续时间内重复出现、语义相近且状态稳定的事实聚合为 topic/persona 轨迹。

### 3.3.1 Episodic Memory Construction

Episodic memory 以对话中的具体事件为基本单元，保留事件发生时间、参与实体、关系变化和原始对话证据。它适合回答一次性经历、时间顺序和“当时说了什么”，也是后续摘要和纠错的可回溯底层。

### 3.3.2 Durative Memory Construction

Durative memory 通过时间片和语义相关性聚合 episodic facts。topic memory 描述一段持续讨论或活动，persona memory 描述偏好、职业、习惯等跨时间属性；当新事实与旧事实冲突时，系统用时间和证据强度更新状态，而不是把冲突文本并列塞入 prompt。

### 3.4 Semantic-time Guided Memory Utilization

查询首先识别 semantic-time constraint，例如“当时”“后来”“目前”“在某次旅行期间”。系统据此过滤候选事实，再在 topic、persona 和 raw chunks 中做 dense retrieval，最后将时间相关性、语义相似度和 TKG 证据映射用于 reranking。这样可以避免仅按文本相似度召回错误时间段的用户信息。

### 3.5 Hierarchical Memory Update

更新分为轻量在线更新与周期性 consolidation。在线阶段只修改受新对话直接影响的图节点、时间区间和冲突边；周期性阶段再把重复 episodic facts 压缩成 topic/persona summary。该设计在实时性和记忆紧凑性之间折中，也使错误可以回溯到原始对话。

### 4 Experiments

实验在 LoCoMo 和 LongMemEval 上比较 TSM 与时间无关的检索/摘要基线，重点观察时间问答、事件记忆、用户画像和多会话一致性。除整体 QA 指标外，作者通过消融检验 episodic/durative 分层、时间约束和层级更新各自的贡献。

### 4.1 Experimental Setup

主要比较包括仅用原始对话、向量检索、时间线/图记忆以及 TSM。评价同时关注回答正确性和检索成本，避免把更长的上下文输入误当成记忆结构本身的收益。

### 4.2 Main Results

TSM 在需要真实事件时间、多轮关系和状态持续性的任务上优于基线；在只需从短文本直接定位答案的题目上，轻量检索有时已经足够。结果支持论文的核心判断：时间建模带来的收益集中在 temporal reasoning 和跨会话状态恢复，而不是所有问题都同等受益。

### 4.3 Ablation Study

去掉时间信息会明显损害时间敏感问题；去掉 durative memory 会使长期偏好和持续主题破碎；去掉层级更新则增加冗余并降低新旧状态区分能力。消融说明 TSM 的提升来自“时间 + 层级 + 图证据”的组合，而不是单一 reranker。

### 5 Conclusions

TSM 将个性化 agent memory 从按聊天顺序存取，推进到按事件真实时间、持续状态和语义时间约束组织。论文的主要贡献是：用 TKG 保留 episodic evidence，用 topic/persona 层表示 duration-aware memory，用时间引导的多视图检索回答跨会话问题，并用分层更新维持长期可用性。作者的结果表明，时间语义是长期个性化记忆的重要检索轴，但系统仍应在简单问题上保持轻量，避免为所有查询付出图构建和多阶段检索成本。

## 关键公式 / 图表

### 关键图

- [Figure 1: existing methods vs. TSM](../assets/2026_beyond-dialogue-time-temporal-semantic-memory-for-person_arxiv-2601-07468/figures/source_figure_001_comparison-of-existing-methods-vs-with-semantic.png)
- [Figure 2: memory consolidation framework](../assets/2026_beyond-dialogue-time-temporal-semantic-memory-for-person_arxiv-2601-07468/figures/source_figure_002_the-overall-framework-of-memory-consolidation-co.png)
- [Figure 3: case study](../assets/2026_beyond-dialogue-time-temporal-semantic-memory-for-person_arxiv-2601-07468/figures/source_figure_003_case-study-of.png)

### 关键表格

## 实验结论

TSM 的优势主要出现在需要区分事件发生时间、恢复持续状态和处理跨会话冲突的任务；它不意味着层级图记忆在所有 QA 上都优于直接检索。论文更可靠的结论是：把时间作为记忆结构和检索控制信号，能减少 temporal misalignment，并使长期用户画像更可更新。

## 局限性与可追问点

- 时间抽取与事实合并本身可能出错，错误会沿图、摘要和 persona 层传播。
- 相对时间、模糊时间和跨文化时间表达的归一化仍依赖模型判断。
- 周期性 consolidation 的触发频率、成本和长期遗忘策略需要更长时间部署验证。

## 对我当前研究/项目的启发

可以把 event time、valid interval 和 dialogue time 分成不同字段，检索时先用问题中的时间约束过滤，再进行语义召回；对持续性用户属性则维护带证据的状态轨迹，而不是覆盖式写入一条最新摘要。
