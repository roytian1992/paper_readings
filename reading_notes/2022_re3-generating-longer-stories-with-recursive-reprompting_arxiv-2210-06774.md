---
id: 2022_re3-generating-longer-stories-with-recursive-reprompting_arxiv-2210-06774
title: "Re3: Generating Longer Stories With Recursive Reprompting and Revision"
year: 2022
authors:
  - Kevin Yang
  - Yuandong Tian
  - Nanyun Peng
  - Dan Klein
venue: "EMNLP 2022"
field:
  - NLP
  - Computational Creativity
direction:
  - Story Generation
keywords:
  - Re3
  - long-form generation
  - entity consistency
status: read
source_path: ../sources/2022_re3-generating-longer-stories-with-recursive-reprompting_arxiv-2210-06774.pdf
source_archive_path: ""
assets_path: ../assets/2022_re3-generating-longer-stories-with-recursive-reprompting_arxiv-2210-06774
paper_type: research
---

# Re3: Generating Longer Stories With Recursive Reprompting and Revision

## 一句话总结

Re3 将长故事生成拆成 Plan、Draft、Rewrite、Edit，用结构化计划、动态历史摘要和候选重排生成 2,000-2,500 word stories；character-only factual edit 对主指标没有可靠增益。

## 研究问题

有限窗口的 rolling generation 会在多千词跨度偏离 premise、破坏全局 plot 并产生事实矛盾，论文研究能否用接近人类写作流程的模块化反复提示缓解这些问题。

## 核心方法

Plan 生成 setting、characters 和三点 outline；Draft 按当前 outline point 重组 premise、相关角色、远期 outline summaries、近期 summary 和上一段原文；Rewrite 用 coherence/relevance rerankers 选候选；Edit 用 character attribute dictionary 检测并尝试修正冲突。

## 分章节阅读笔记

### 1 Introduction

定义多千词自动故事生成中的长程 plot coherence、premise relevance 与 factual consistency 问题。

### 2 Related Work

将 Re3 定位在 outline planning、rewrite/reranking、local editing 和 human-in-the-loop writing 之间。

### 3 Recursive Reprompting and Revision

四模块均以自然语言计划和动态上下文为接口；完整机制与结果边界见项目笔记。

### 4 Evaluation

100 个 premises、同 GPT-3-175B rolling baselines、每对三位 Mechanical Turk annotators；agreement 很低。

### 5 Analysis

Plan/Rewrite 有贡献，Edit 主指标无明显增益；controlled contradiction detector ROC-AUC 为 0.684。

### 6 Discussion

系统仍缺 setting、event、theme、pace 和 foreshadowing 等长程连续性。

## 关键公式 / 图表

### 关键图

### 关键表格

## 实验结论

相对 rolling baseline，coherent/relevant 从 45.7/44.0 提升到 60.0/64.0；但 human-evaluation Fleiss kappa 多数接近 0。

## 局限性与可追问点

模型调用极多、阈值手工选择、Edit 仅覆盖 character attributes，而且时变事实容易被误判为矛盾。

## 对我当前研究/项目的启发

完整 source-grounded project note：`SharedWorldsPrivateMinds/literature/reading_notes/yang2022re3.md`。
