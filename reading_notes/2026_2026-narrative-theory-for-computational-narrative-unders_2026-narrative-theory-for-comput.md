---
id: 2026_2026-narrative-theory-for-computational-narrative-unders_2026-narrative-theory-for-comput
title: "2026_narrative-theory-for-computational-narrative-understandi_narrative-theory-for-computation"
year: 2026
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
status: reading
source_path: ../sources/2026_2026-narrative-theory-for-computational-narrative-unders_2026-narrative-theory-for-comput.pdf
source_archive_path: ""
assets_path: ../assets/2026_2026-narrative-theory-for-computational-narrative-unders_2026-narrative-theory-for-comput
paper_type: research
---

# 2026_narrative-theory-for-computational-narrative-understandi_narrative-theory-for-computation

## 一句话总结

论文将计算叙事理解放在“事件如何被组织、排序并置于叙事视角中”的框架下讨论，并明确区分局部场景组织与跨场景情节线组织。

## 研究问题

如何把事件、人物、时间、空间和叙事视角联系起来，使计算模型不仅识别孤立事件，也能理解更高层次的叙事结构。

## 核心方法

这是一篇理论与研究议程型论文，不提出一个可直接运行的事件聚合算法。与本项目最相关的结构是：`event → scene → plotline → plot`。其中，事件构成故事世界的基本行动单元；scene 用于组织局部、连续且具有共同叙事边界的事件；plotline 将跨越时间和空间、由相关人物持续参与的多个 scene 组织成更一般的叙事单元；plot 则是更高层次的整体结构。

## 分章节阅读笔记

<!-- 待从论文原文目录或真实章节标题补齐；不要使用通用占位章节。 -->

### 2.3 Events (F)

论文把事件视为叙事世界的核心行动单元，并指出事件建模有两个相互关联的问题：事件的时间排序，以及把事件分类或组织到更一般的功能单元中。事件序列不仅支持时间推理，也支持因果关系、事件链和脚本结构的建模。

论文在叙事结构部分给出层级方案：`event–scene–level–plotline–plot`。这里的 scene 解决局部的横向边界问题；plotline 则把 scene 和叙事层级组织成跨时间、跨空间、由相关人物贯穿的更一般单元。论文强调这是计算叙事研究中的结构化方向，而不是一个已经统一解决的工程算法。

## 关键公式 / 图表

### 关键图

### 关键表格

## 实验结论

## 局限性与可追问点

- 论文提出的是概念框架和研究议程，没有规定 scene 或 plotline 的唯一抽取算法。
- event、scene、plotline 的边界依赖时间、人物、空间、因果和叙事层级，不能只靠相邻文本切分。
- 论文中的 plotline 不等同于简单 summary；它需要保留跨场景的参与者、发展和关系线索。

## 对我当前研究/项目的启发

SWPM 当前的 `event_bundle` 是检索时的一跳证据闭包，`cross_event_bundle` 是跨事件派生导航视图，`scene_bundle` 是请求/投影视图级打包；它们都不能直接等同于论文中的离线 scene 层。当前 `RecordType` 也没有正式的 scene、episode 或 plotline 类型。

因此，LoCoMo 的 multi-hop 可能受到一个结构性限制：多个相关事件虽然各自被抽取并可单独召回，但它们之间缺少稳定的、可检索的中间结构。更合适的改进方向是离线构建 evidence-linked 的 scene 级派生视图，保留事件成员、时间范围、共享人物/地点、状态变化、因果或信息传播边，并回指原子 W/B/D；写作任务再在线根据请求把多个 scene 组织成 plotline，而不是离线生成未来情节。
