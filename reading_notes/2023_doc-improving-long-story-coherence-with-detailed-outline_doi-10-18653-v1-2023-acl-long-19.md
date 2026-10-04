---
id: 2023_doc-improving-long-story-coherence-with-detailed-outline_doi-10-18653-v1-2023-acl-long-19
title: "DOC: Improving Long Story Coherence With Detailed Outline Control"
year: 2023
authors: []
venue: "ACL 2023"
field:
  - NLP
  - Computational Creativity
direction:
  - Story Generation
keywords:
  - DOC
  - outline control
  - coherence
status: read
source_path: ../sources/2023_doc-improving-long-story-coherence-with-detailed-outline_doi-10-18653-v1-2023-acl-long-19.pdf
source_archive_path: ""
assets_path: ../assets/2023_doc-improving-long-story-coherence-with-detailed-outline_doi-10-18653-v1-2023-acl-long-19
paper_type: research
---

# DOC: Improving Long Story Coherence With Detailed Outline Control

## 一句话总结

DOC 用 breadth-first detailed outline 和 FUDGE-style token controller 把约 3,500-word stories 的创作决策前移到计划阶段，提高 outline relevance，但 leaf realization 仍不完整。

## 研究问题

粗 outline 不足以约束长篇 drafting，而细 outline 又使自然语言约束更难满足；论文同时增强 planning granularity 与 decoding-time control。

## 核心方法

Outliner 递归生成、过滤、排序 events 并检测 setting/characters；controller 用 passage-summary discriminator 逐 token 调整 OPT-175B logits，动态增强 constraint strength。

## 分章节阅读笔记

### 1 Introduction

定位为 Re3 的 detailed planning/control extension。

### 2 Related Work

覆盖 hierarchical generation、controlled generation 与 interactive writing。

### 3 Detailed Outline Control

详述 outliner tree、candidate filters、character development、drafting 和 controller。

### 4 Evaluation

20-story main comparison 和 20-run human-interactive comparison；每个 passage pair 三人标注。

### 5 Analysis

两大组件都改善 relevance；leaf faithfulness 只有 58.5%。

### 6 Discussion

指出 evaluation、long-range consistency、领域/语言迁移和更长文本扩展问题。

## 关键公式 / 图表

### 关键图

### 关键表格

## 实验结论

相对 matched OPT-175B Re3，DOC coherent/relevant/interesting preference 为 67.6/65.3/60.1%；interactive quality preference 为 75%。

## 局限性与可追问点

依赖 OPT-175B、InstructGPT、多 filters 和约 2,000 A100 hours；future outline context 对 character-facing tasks 会构成泄露。

## 对我当前研究/项目的启发

完整 source-grounded project note：`SharedWorldsPrivateMinds/literature/reading_notes/yang2023doc.md`。
