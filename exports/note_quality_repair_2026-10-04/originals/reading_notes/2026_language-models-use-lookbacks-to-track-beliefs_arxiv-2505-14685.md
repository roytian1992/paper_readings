---
id: 2026_language-models-use-lookbacks-to-track-beliefs_arxiv-2505-14685
title: "Language Models use Lookbacks to Track Beliefs"
year: 2026
authors:
  - Nikhil Prakash
  - Natalie Shapira
  - Arnab Sen Sharma
  - Christoph Riedl
  - Yonatan Belinkov
  - Tamar Rott Shaham
  - David Bau
  - Atticus Geiger
venue: "ICLR 2026"
field:
  - Natural Language Processing
  - Artificial Intelligence
direction:
  - Theory of Mind
  - Mechanistic Interpretability
keywords:
  - CausalToM
  - belief tracking
  - lookbacks
  - false belief
  - causal mediation
status: read
source_path: ../sources/2026_language-models-use-lookbacks-to-track-beliefs_arxiv-2505-14685.pdf
source_archive_path: ""
assets_path: ../assets/2026_language-models-use-lookbacks-to-track-beliefs_arxiv-2505-14685
paper_type: research
---

# Language Models use Lookbacks to Track Beliefs

## 一句话总结

论文用 CausalToM 与 causal interventions 发现高性能 Llama/Qwen 在简单 belief tracking 成功样本上使用 ordering IDs 和 binding、answer、visibility lookbacks。

## 研究问题

行为正确率无法区分表面匹配与系统性 belief-tracking computation，需要用可控 counterfactuals 干预内部变量。

## 核心方法

CausalToM 用四种模板控制 character/object/state/order/visibility；作者在 80 个模型已答对的样本上用 activation patching 与 causal abstraction 对齐高层 pointer-like algorithm 和 residual-stream subspaces。

## 分章节阅读笔记

- 第 3-6 节：核对数据、模型、interchange intervention、三类 lookback 和 visibility 更新。
- Appendices B-O：核对行为表、BigToM 初步迁移、跨模型与三角色扩展。

## 关键公式 / 图表

### 关键图

### 关键表格

## 实验结论

受控成功样本支持分阶段 binding/retrieval 的因果机制；相同模式在 405B/Qwen full residual 上出现，但 BigToM subspaces 不共享，三角色 visibility 也不能稳定解决。

## 局限性与可追问点

结论条件化于答对的 80 个高度规则样本；prompt 明示 belief rules，BigToM 证据仅 preliminary，官方仓库无 LICENSE。

## 对我当前研究/项目的启发

可借鉴 visibility counterfactual 和 binding/answer 分解，但外部 typed graph contract 不等同于模型神经 lookback。完整笔记见 `SharedWorldsPrivateMinds/literature/reading_notes/prakash2026lookbacks.md`。
