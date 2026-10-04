---
id: 2021_2021-emnlp-main-26_aclanthology-org
title: "Narrative Theory for Computational Narrative Understanding"
year: 2021
authors:
  - Andrew Piper
  - Richard Jean So
  - David Bamman
venue: "EMNLP 2021"
field:
  - NLP
  - Computational Narratology
direction:
  - Narrative Structure
keywords:
  - narrative levels
  - scene detection
  - plotline
  - event hierarchy
status: read
source_path: ../sources/2021_2021-emnlp-main-26_aclanthology-org.pdf
source_archive_path: ""
assets_path: ../assets/2021_2021-emnlp-main-26_aclanthology-org
paper_type: position
---

# Narrative Theory for Computational Narrative Understanding

## 一句话总结

这篇立场论文将分散的计算叙事研究放入统一的叙事学框架，并把事件排序与事件向场景、叙事层、情节线和整体情节的逐级抽象区分开来。

## 研究问题

NLP 中的事件检测、角色建模、时间推理和叙事结构研究如何与经典及后经典叙事理论对齐，从而形成术语一致、问题边界清楚的计算叙事研究框架？

## 核心方法

论文不是新的抽取算法，而是一个理论组织框架。作者以施事者、事件、时间、空间和叙事视角等要素组织既有工作，并讨论这些要素如何支持更高层的叙事结构与社会应用。

## 分章节阅读笔记

### 1 Introduction

论文指出，NLP 已有大量叙事相关任务，但不同工作常使用互不兼容的术语和理论假设。作者的目标是用叙事学统一这些研究方向，而不是提供一个新的端到端系统。

### 2 The elements of narrativity

#### 2.1 Towards a working definition of narrativity

#### 2.2 Agents (E, G)

作者把 agent detection 视为计算叙事学的基础任务，并强调 agent 不应局限于传统命名实体，还包括“车夫”“青蛙”等具有施事能力的普通名词指称。角色建模还依赖属性与关系，但关系识别本身具有歧义，不能仅凭共现直接确定连接或身份。

#### 2.3 Events (F)

本节把事件问题分为两类：事件如何排序，以及事件如何被归并为更高层的功能单元。前者涉及 story 与 discourse 的顺序差异、事件链、时间关系和因果关系；后者涉及 passage-level 与 document-level 的叙事结构。

对 STAGE 最直接的依据来自 Narrative structure 段。作者把 scene 定义为由空间、时间和施事者边界划分的横向故事片段，并把 plotline detection 定义为将跨时间和空间的 scenes 与 narrative levels 组织成更一般的叙事单元。由此提出 `event-scene-level-plotline-plot` 层级。这个层级是理论框架，不规定具体抽取算法。需要特别注意：论文这里使用的是 `scene` 和 `plotline`，并没有把 `episode` 或 `storyline` 作为这条层级的标准名称。

STAGE 与该框架的关系应表述为 screenplay-specific operationalization，而不是完全等同：screenplay scene 是可观察的来源与边界单元；Event 是细粒度动作或变化；若某个系统另用 Episode 表示 scene-like 的中层构造单元，应明确它是工程别名；跨 scene 的发展更适合称为 plotline，而不是直接称为 storyline。movie 提供文档级范围。STAGE 还增加了 character temporal graph，用于表示角色状态、发展和 epistemic access，这超出了该通用层级本身。

#### 2.4 Temporality (I)

论文区分 story 中实际经过的 narrated time 与 discourse 中讲述所占的 narrative time，并进一步讨论 discourse order 与 story order 的错位。事件时间排序是因果理解和 plot 表示的前提，因此时间关系适合在事件已经抽取后单独建模，而不应与实体识别挤在同一次输出中。

#### 2.5 Setting (H)

Setting 不只是地点 NER。作者强调 action 与 setting 相互规定，并指出长文叙事中的普通地点指称（如 house、room）仍有困难的跨文档共指问题。对 SWPM 而言，地点和其他可参与叙事的对象应与角色一起进入实体注册及消歧阶段，再由事件阶段引用。

#### 2.6 Perspective (A, B, C)

Perspective 覆盖 narrator、point of view、focalization 与 dialogue attribution。角色对世界的态度和局部认知依赖可靠的 speaker attribution 与 agent identity，因此应在实体和一阶故事事实已经稳定后建模。论文 §3.3 的 narrative beliefs 指更高阶的社会叙事组织原则，不应直接等同于 SWPM 的角色 epistemic state。

### 3 Scaling up narrative understanding

#### 3.1 Narrative economies

#### 3.2 Narrative responses

#### 3.3 Narrative beliefs

### 4 Conclusion

## 关键公式 / 图表

### 关键图

### 关键表格

## 实验结论

## 局限性与可追问点

## 对我当前研究/项目的启发

1. 在 STAGE 的 Related Work 中明确写出 `event-scene-level-plotline-plot`，说明多层 backbone 有计算叙事学依据。
2. 在 Narrative backbone construction 中说明 STAGE 对该层级的适配关系，同时明确 Episode 不是 scene 的同义词。
3. 不建议为了显得理论丰富而同时加入 text worlds、narremes、event chains 等所有二级引用；这些工作没有直接定义 STAGE 的构造流程。
4. Wallace (2012) 可作为 Storyline 跨段落聚合的补充依据，但只有在正文讨论多条交织 plotlines 时才值得单独引用。
5. SWPM 的离线构建可工程化为四阶段，但应明确这是对论文分类的系统映射，而非论文提出的算法：`Agents and Setting` 建立实体注册表；`Events and Storyworld` 抽取事件与一阶命题；`Perspective and Social Minds` 建模关系、说话者、焦点与角色态度；`Sequence and Structure` 聚合时间、因果、状态变化、scene 与 narrative thread。
6. 后续阶段应接收 source-grounded entity cards，而不是裸 ID。短 ID 用于机器可检验的引用，canonical name、aliases、entity type、来源描述和 mention evidence 用于模型理解；canonical 长 ID 只在最终消歧和落库后生成。
