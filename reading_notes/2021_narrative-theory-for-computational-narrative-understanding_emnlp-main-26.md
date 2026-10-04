---
id: 2021_narrative-theory-for-computational-narrative-understanding_emnlp-main-26
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
source_path: ../sources/2021_narrative-theory-for-computational-narrative-understanding_emnlp-main-26.pdf
source_archive_path: ""
assets_path: ../assets/2021_narrative-theory-for-computational-narrative-understanding_emnlp-main-26
paper_type: research
---

# Narrative Theory for Computational Narrative Understanding

## 一句话总结

论文将计算叙事理解放在“事件如何被组织、排序并置于叙事视角中”的框架下讨论，并明确区分局部场景组织与跨场景情节线组织。

## 研究问题

如何把事件、人物、时间、空间和叙事视角联系起来，使计算模型不仅识别孤立事件，也能理解更高层次的叙事结构。

## 核心方法

这是一篇理论与研究议程型论文，不提出一个可直接运行的事件聚合算法。与本项目最相关的结构是：`event → scene → plotline → plot`。其中，事件构成故事世界的基本行动单元；scene 用于组织局部、连续且具有共同叙事边界的事件；plotline 将跨越时间和空间、由相关人物持续参与的多个 scene 组织成更一般的叙事单元；plot 则是更高层次的整体结构。

## 分章节阅读笔记

### 1 Introduction

论文的出发点是：NLP 已经能够识别实体、事件和情感，但这些局部识别结果还没有被组织成可解释的叙事结构。作者因此把计算叙事理解放回 narratology 的概念体系中，主张模型需要同时表示故事世界中的事件，以及文本如何选择、排序和解释这些事件。论文不是提出新的 benchmark 或单一模型，而是为后续计算工作提供共享术语、结构层级和问题清单。

### 2 The elements of narrativity

#### 2.1 Towards a working definition of narrativity

作者把 narrativity 理解为对状态变化的组织：叙事至少包含一组相互关联的事件、参与者、时间/空间条件和某种呈现视角。这个定义同时区分 story（故事世界中发生了什么）与 discourse（文本以什么顺序、由谁、以何种焦点呈现），因此不能把叙事简单等同于事件列表。

#### 2.2 Agents (E, G)

人物或行动者不是静态实体标签，而是事件中承担行动、感知、目标和关系变化的参与者。计算模型需要识别谁在做什么、对谁做、拥有何种目标或能力，并跟踪同一角色在不同场景中的持续性。作者也提醒，人物分类和人物网络只能提供结构线索，不能替代事件和叙事视角的解释。

#### 2.3 Events (F)

### 2.3 Events (F)

论文把事件视为叙事世界的核心行动单元，并指出事件建模有两个相互关联的问题：事件的时间排序，以及把事件分类或组织到更一般的功能单元中。事件序列不仅支持时间推理，也支持因果关系、事件链和脚本结构的建模。

论文在叙事结构部分给出层级方案：`event–scene–level–plotline–plot`。这里的 scene 解决局部的横向边界问题；plotline 则把 scene 和叙事层级组织成跨时间、跨空间、由相关人物贯穿的更一般单元。论文强调这是计算叙事研究中的结构化方向，而不是一个已经统一解决的工程算法。

#### 2.4 Temporality (I)

时间包含至少三层：故事时间中的事件先后、文本叙述的 discourse order，以及持续时间、频率和回溯/预叙等叙事操作。模型若只按段落顺序读取，会把倒叙误判成世界中的时间顺序；因此需要显式保留事件时间、叙述位置和二者之间的偏离。

#### 2.5 Setting (H)

Setting 不只是地点字段，也包括社会制度、物理环境、物件和事件发生的约束。场景变化会改变人物可执行的行动、关系和目标。作者将 setting 视为事件解释的条件变量，强调实体识别、地点抽取和地理关系只有在与事件、时间和人物绑定后，才具有叙事意义。

#### 2.6 Perspective (A, B, C)

Perspective 说明信息由谁感知、谁叙述，以及读者能获得哪些知识。论文区分 narrator、focalizer 和 character belief 等层次；同一事件在不同角色视角下可能具有不同信息状态和解释。对计算模型而言，视角建模意味着要区分文本断言、角色信念和作者/叙述者的全知信息，避免把不可靠叙述当作故事事实。

### 3 Higher-level issues

#### 3.1 Narrative economies

叙事通过省略、重复、延迟揭示和信息分配控制读者注意力。所谓 narrative economy 关注文本在有限篇幅中如何选择哪些事件、关系和背景进入叙述，以及这些选择如何塑造理解。未来模型不仅要抽取“存在什么”，还要解释“为什么此处呈现这一信息”。

#### 3.2 Narrative responses

叙事理解还包括读者反应，例如悬念、惊讶、同理心和情绪变化。这些反应不是文本表面标签，而是由事件预期、视角限制、信息揭示顺序和人物目标共同产生。作者因此建议把读者反应作为可计算的高层目标，并与事件/视角结构连接起来。

#### 3.3 Narrative beliefs

叙事中的 belief 既包括人物对世界的信念，也包括读者在阅读过程中形成的假设。人物可能拥有错误或不完整的信息，文本也可能故意让读者暂时接受错误解释。计算叙事系统应表示信念的来源、时间和更新，而不能把所有句子直接合并成一个全局真值库。

### 4 Conclusion

论文的结论是，计算叙事理解需要一个由 narratology 提供的组织框架，把事件、行动者、时间、场景、视角以及更高层次的情节结构连接起来。作者特别强调 `event → scene → plotline → plot` 的层级视角：事件是局部行动单元，scene 组织连续的局部情境，plotline 连接跨场景的角色与目标发展，plot 才是整体叙事结构。这个框架的价值不在于给出唯一实现，而在于为数据集、标注体系和模型评估提供可对齐的问题分解。

## 关键公式 / 图表

### 关键图

### 关键表格

## 实验结论

本文没有传统意义上的模型实验。其主要产出是理论映射和研究议程：已有 NLP 任务可以分别对应事件、人物、时间、场景或情绪，但跨层级的 scene/plotline 建模、视角与信念跟踪、以及叙事经济和读者反应仍缺少统一评测。

## 局限性与可追问点

- 论文提出的是概念框架和研究议程，没有规定 scene 或 plotline 的唯一抽取算法。
- event、scene、plotline 的边界依赖时间、人物、空间、因果和叙事层级，不能只靠相邻文本切分。
- 论文中的 plotline 不等同于简单 summary；它需要保留跨场景的参与者、发展和关系线索。

## 对我当前研究/项目的启发

SWPM 当前的 `event_bundle` 是检索时的一跳证据闭包，`cross_event_bundle` 是跨事件派生导航视图，`scene_bundle` 是请求/投影视图级打包；它们都不能直接等同于论文中的离线 scene 层。当前 `RecordType` 也没有正式的 scene、episode 或 plotline 类型。

因此，LoCoMo 的 multi-hop 可能受到一个结构性限制：多个相关事件虽然各自被抽取并可单独召回，但它们之间缺少稳定的、可检索的中间结构。更合适的改进方向是离线构建 evidence-linked 的 scene 级派生视图，保留事件成员、时间范围、共享人物/地点、状态变化、因果或信息传播边，并回指原子 W/B/D；写作任务再在线根据请求把多个 scene 组织成 plotline，而不是离线生成未来情节。
