---
id: 2024_evaluating-very-long-term-conversational-memory-of-llm-a_doi-10-18653-v1-2024-acl-long-74
title: "Evaluating Very Long-Term Conversational Memory of LLM Agents"
year: 2024
authors: []
venue: "ACL 2024"
field:
  - NLP
  - Machine Learning
direction:
  - LLM Agents
  - Long-Term Memory
keywords:
  - LoCoMo
  - long-term conversation
  - memory benchmark
status: read
source_path: ../sources/2024_evaluating-very-long-term-conversational-memory-of-llm-a_doi-10-18653-v1-2024-acl-long-74.pdf
source_archive_path: ""
assets_path: ../assets/2024_evaluating-very-long-term-conversational-memory-of-llm-a_doi-10-18653-v1-2024-acl-long-74
paper_type: benchmark
---

# Evaluating Very Long-Term Conversational Memory of LLM Agents

## 一句话总结

LoCoMo 用 temporal event graphs 与 generative agents 构造 10 条人工修订的超长对话和 1,986 QA，分别评价 QA、event summarization 与 multimodal response continuity。

## 研究问题

约五 session 的旧 benchmark 无法测试多月时间、因果、更新与 persona continuity；论文构造平均 588 turns、27.2 sessions、16,618 tokens 的 stress test。

## 核心方法

两位 GPT-3.5 agents 由 persona 和 6-12 month event graph 驱动；session summary 与 turn observations 形成记忆；annotators 修正约 15% turns，并保留 answer turn IDs。

## 分章节阅读笔记

### 1 Introduction

提出超长对话 memory 的三任务评价框架。

### 2 Related Work

覆盖 long-term dialogue、multimodal dialogue 与 synthetic benchmark construction。

### 3 Generative Pipeline for LoCoMo

定义 persona、temporal event graph、agent memory 与 human verification。

### 4 LoCoMo Evaluation Benchmark

QA 含 single/multi-hop、temporal、open-domain、adversarial；另有 event summary 与 multimodal generation。

### 5 Experimental Setup

比较 truncated base models、long-context models 与 dialog/observation/summary RAG。

### 6 Experimental Results

Long-context/RAG 有帮助，但 temporal/adversarial 和 long-range factual summarization 仍弱。

### 7 Conclusion

将结论限定为 model comprehension in synthetic-edited very-long conversations。

## 关键公式 / 图表

### 关键图

### 关键表格

## 实验结论

Human QA F1 87.9，GPT-4 Turbo 51.6；observation-RAG top-5 为 43.3，raw-dialog top-5 为 38.8。

## 局限性与可追问点

仅 10 条主对话，closed-LLM generation，English-only，视觉连续性弱；数据为 CC BY-NC 4.0。

## 对我当前研究/项目的启发

完整 source-grounded project note：`SharedWorldsPrivateMinds/literature/reading_notes/maharana2024locomo.md`。
