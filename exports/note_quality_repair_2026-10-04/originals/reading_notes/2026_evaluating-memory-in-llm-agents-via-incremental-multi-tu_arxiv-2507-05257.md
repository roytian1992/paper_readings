---
id: 2026_evaluating-memory-in-llm-agents-via-incremental-multi-tu_arxiv-2507-05257
title: "Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions"
year: 2026
authors:
  - Yuanzhe Hu
  - Yu Wang
  - Julian McAuley
venue: "ICLR 2026"
field:
  - Natural Language Processing
  - Artificial Intelligence
direction:
  - Agent Memory Evaluation
keywords:
  - MemoryAgentBench
  - agent memory
  - incremental interaction
  - conflict resolution
status: read
source_path: ../sources/2026_evaluating-memory-in-llm-agents-via-incremental-multi-tu_arxiv-2507-05257.pdf
source_archive_path: ""
assets_path: ../assets/2026_evaluating-memory-in-llm-agents-via-incremental-multi-tu_arxiv-2507-05257
paper_type: research
---

# Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions

## 一句话总结

MemoryAgentBench 将 13 个异质任务切成增量 chunks，用 2,071 questions 分别测 accurate retrieval、test-time learning、long-range understanding 和 selective forgetting。

## 研究问题

静态长上下文 QA 无法反映 agent 逐步摄取、压缩、更新和读取历史的过程，也缺少覆盖局部检索、从历史学习、全局理解与冲突更新的统一 harness。

## 核心方法

统一 episode 先逐 chunk 发送带 memorization instruction 的 user messages，再对同一历史提多题。数据重组 RULER、LongMemEval、InfinityBench、DetectiveQA、ReDial、MQUAKE 等，并新增 EventQA 与 FactConsolidation；比较 long-context、RAG 和 agentic-memory agents。

## 分章节阅读笔记

- 第 3 节：核对四能力定义、13 个任务、增量注入协议和一次构建多次查询设计。
- 第 4 节：核对 Table 3 主结果、chunk/top-k/backbone 消融和 FactConsolidation 短上下文验证。
- Appendices B-I：核对 2,071-question 统计、metrics、prompts、成本与 overwrite-policy 分析。

## 关键公式 / 图表

### 关键图

### 关键表格

Table 3 中 GPT-5-mini overall 60.6；BM25 的 AR average 60.5 高于 GPT-4o-mini 49.2，但 RAG 在 TTL/LRU 明显受限。FactConsolidation-MH 主表最高 28.0，多数方法不超过 7.0。

## 实验结论

增量 memory evaluation 应按能力拆分；细 chunks 有利局部检索但损害全局整合，扩大 top-k 同时提高 reader 成本。冲突题的失败包含 retrieval、serial resolution 和 answer assembly，不能归因于单一“遗忘”模块。

## 局限性与可追问点

静态文本切块加显式记忆指令不等于自然长期交互；overall 混合 Accuracy、Recall@5、F1 与 LLM judge。发布存在 code MIT、paper CC BY 4.0、HF card MIT 与上游数据条款并存的问题。

## 对我当前研究/项目的启发

借鉴逐 chunk ingest、一次构建多次查询和分能力报告；FactConsolidation 可启发确定性 update-resolution 诊断，但不能替代 authority/time/private projection/branch lifecycle tests。项目级完整笔记见 `SharedWorldsPrivateMinds/literature/reading_notes/memoryagentbench2026.md`。
