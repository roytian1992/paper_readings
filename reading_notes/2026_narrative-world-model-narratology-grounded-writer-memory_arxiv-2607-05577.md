---
id: 2026_narrative-world-model-narratology-grounded-writer-memory_arxiv-2607-05577
title: "Narrative World Model: Narratology-Grounded Writer Memory for Long-Form Fiction"
year: 2026
authors:
  - Mohammad Saifullah
  - Thomas Kornmaier
  - Taaha Kazi
  - Vasu Sharma
  - Aditya Sanjiv Kanade
  - Aanand Kumar Yadav
venue: ""
field: []
direction: []
keywords: []
status: reading
source_path: ../sources/2026_narrative-world-model-narratology-grounded-writer-memory_arxiv-2607-05577.pdf
source_archive_path: ""
assets_path: ../assets/2026_narrative-world-model-narratology-grounded-writer-memory_arxiv-2607-05577
paper_type: research
---

# Narrative World Model: Narratology-Grounded Writer Memory for Long-Form Fiction

## 一句话总结

论文提出 Narrative World Model（NWM）：用带有叙事语义的、按章节和有效区间组织的记忆记录，再通过查询条件化的混合检索和一跳关联，为长篇写作提供跨章节、因果安全的证据包。

## 研究问题

普通向量检索、平面事实记忆和通用时间知识图谱容易找不到或混淆长篇叙事中的跨章节关系，尤其是角色知道什么、信息何时揭示、事件顺序与揭示顺序的差异、setup/payoff，以及关系和状态变化。

## 核心方法

- 发布流程：接受的章节先抽取为带章节锚点和证据跨度的 typed records，再合并到累积 registry；编辑章节时从该章重新抽取并使下游派生边失效。
- 时间安全：写入时给每条记录标记来源章节，读取时再次限制来源章节 `<= n`，其中 `n` 是当前 checkpoint。
- 记忆内容：chapter digest、scene/event、character state、relationship state、object state、plot/promise、narrative function 和 world fact；重点是知识边界、reveal order、open/closed payoff、focalization 和 dramatic function。
- 检索：先做 checkpoint 过滤，再用 BM25 + dense vector + RRF 选 seed，随后做有邻居上限的一跳 typed graph expansion，最后组装固定大小的异构证据包。
- 论文将改进归因于叙事结构和 query-conditioned retrieval，而不是图更大或类型标签更多；正文和附录还显示去掉读者侧类型标签并不会降低结果。

## 分章节阅读笔记

### 3 Narrative World Model

NWM 将记忆定义为已完成文本的发布结果，而不是未来意图。核心约束是 `M_n = Publish(C_n, M_{n-1})`、`X_{n+1} = Retrieve(M_n, O_{n+1})`：第 `n+1` 个单元只能使用已经发布到第 `n` 个 checkpoint 的信息。记录被合并到角色、关系、地点、物体、线程和 promise 等 registry，但历史状态不删除。

### 3.2 Schema Updates and Global Registries

论文建议把以下字段视为 writer-facing 语义，而不是只存在于内部图边：场景/事件的地点、参与者、事件顺序和揭示顺序；角色的目标、知道/未知、状态、位置和关系变化；对象的拥有者、位置和条件；plot/promise 的结构角色和 open/closed payoff；叙事功能的焦点人物、dramatic beat、turn/reversal。

### 3.3 Temporal Knowledge Graph

每条边带来源章节、证据、有效区间和置信度。查询“截至第 n 章的状态”时，选择在该 checkpoint 有效的最新边，但保留更早的边供历史重建。这里的边界不是简单的“最近一条记录”，而是 `source chapter <= checkpoint` 加上有效区间判断。

### 3.5 Query-Conditioned Hybrid Retrieval

检索分为四步：因果截止、BM25/向量/RRF seed ranking、一跳 typed neighborhood expansion、固定大小的异构 evidence packet。论文强调 query conditioning 是关键：同一份记忆如果按章节前缀整体序列化并截断，会把已经存在的正确证据丢在截断点之后。

### 4 Evaluation: Narrative Memory QA

论文将 multi-hop 定义为需要至少两个不同章节证据的问题，并通过 top-1 360-word chunk 无法独立回答的 hardness filter 排除伪 multi-hop。它把 single-hop control、multi-hop hop 数、focalization/epistemic、reveal-vs-event order、dramatic shape/setup-payoff 和组合问题分开评估。

### Appendix A.1 Query-Conditioned Hybrid Retrieval

`<= n` 是论文最重要的硬边界：写入时每条记录保存来源章节，读取时再次过滤来源章节不大于 checkpoint。检索预算限制的是最终 reader evidence packet，不等同于限制离线记忆规模。邻居上限和最终 packet 上限是检索实现参数，论文没有把它们当作叙事语义。

<!-- 待从论文原文目录或真实章节标题补齐；不要使用通用占位章节。 -->

## 关键公式 / 图表

### 关键图

### 关键表格

## 实验结论

论文报告的核心现象是：query-conditioned graph retrieval 明显优于把完整 current-state memory 按位置截断的 State Memory；后者的失败主要来自证据已经存在但被位置截断，而不是抽取缺失。类型标签本身不是主要增益来源，真正重要的是记录是否表示了叙事结构，以及检索是否能把相关记录和关联证据一起取出。

## 局限性与可追问点

- 论文是预印本，NWM 的不少结构字段由作者设计，部分边界和超参数仍需要更多跨语料验证。
- 正文描述了一跳扩展和邻居上限，但没有给出足够细的 production-level seed、neighbor 和 packet 参数配置。
- 论文主要验证 narrative-memory QA，不等价于已经证明长篇连续生成一定提升。
- 其 `narrative level` 仍与 scene、plotline 分开；普通章节或 session 不能直接当作 embedded narrative level。

## 对我当前研究/项目的启发

### 已经具备的能力

- V3 已有 `story_validity`、`discourse_validity`、`temporal_relation`、`epistemic_state`、`narrative_thread`、`narrative_explanation` 和 evidence closure，能够表达大部分时间、认知、关系、线程和因果信息。
- `GraphViewSpec.before_unit_order` 在 canonical projection 中已经执行 `< checkpoint` 过滤；`LegalViewToolBackend` 也有 temporal/causal path、reveal 和 state-history 处理。
- V3 已有 BM25/向量融合、一跳事件 bundle、scene/plotline 派生 hierarchy，并且原子 W/B 不被派生摘要替换。

### 当前最值得补齐的边界

1. 将 checkpoint 约束统一施加到 derived cross-event index 和 narrative hierarchy 的加载、搜索及 closure 返回，而不仅依赖底层 legal view；不能允许全量 sidecar 以 `allow_canonical_superset` 方式直接跨 checkpoint 使用。
2. 在派生节点中显式携带 story-time、discourse/reveal-time、focalizer/holder 和 validity 来源；当前 hierarchy 主要保存普通 time range，不能完整表达“事件发生时间”和“读者得知时间”的分离。
3. 将 `narrative_thread` 的 `open/advanced/resolved/abandoned` 作为 setup/payoff 导航依据，而不只是 plotline summary 的文本词面。
4. 对 object/location/state 使用有效区间重建“旧但仍然有效”的当前状态，不能只按最近 source unit 取值。
5. R1 仍然采用“query seed + 关联扩展”的模式：先召回答案相关的 W/B/D 记录，再补同一事件、同一线程、同一 reveal 或同一关系变化的邻接记录；最终保持原子 evidence closure。

### 对 SWPM 的简化落地判断

不需要引入 NWM 的新平行记忆系统，也不需要把 type label 原样暴露给生成模型。保留 W/B/D/H：W/B 继续承载原子事实、状态和角色认知，D 承载 scene/plotline/plot、reveal、thread 和跨事件发展，H 只保留在线 request-local 推演。优先补齐 checkpoint、双时间、有效区间和 query-conditioned 一跳关联四个边界。
