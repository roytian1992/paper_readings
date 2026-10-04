---
id: 2024_memorybank-enhancing-large-language-models-with-long-ter_arxiv-2305-10250
title: "MemoryBank: Enhancing Large Language Models with Long-Term Memory"
year: 2024
authors:
  - Wanjun Zhong
  - Lianghong Guo
  - Qiqi Gao
  - He Ye
  - Yanlin Wang
venue: "AAAI 2024"
field:
  - NLP
  - Machine Learning
direction:
  - LLM Agents
  - Long-Term Memory
keywords:
  - MemoryBank
  - Ebbinghaus forgetting curve
  - long-term memory
status: read
source_path: ../sources/2024_memorybank-enhancing-large-language-models-with-long-ter_arxiv-2305-10250.pdf
source_archive_path: ""
assets_path: ../assets/2024_memorybank-enhancing-large-language-models-with-long-ter_arxiv-2305-10250
paper_type: system
---

# MemoryBank: Enhancing Large Language Models with Long-Term Memory

## 一句话总结

MemoryBank 组合 timestamped dialogue、hierarchical event/personality summaries、dense retrieval 与简化 Ebbinghaus decay，为 companion LLM 提供可插拔长期记忆。

## 研究问题

无状态 LLM 无法在持续互动中回忆用户经历、更新画像或个性化回应，论文构建外部 memory storage/retrieval/update layer。

## 核心方法

每个 dialogue turn 和 summary 编码入 FAISS；LLM 生成 daily/global event 与 personality summaries；retention 使用 $R=e^{-t/S}$，召回时 `S += 1` 并重置时间。

## 分章节阅读笔记

### 1 Introduction

提出 long-term companion memory 的需求与 SiliconFriend demo。

### 2 MemoryBank: A Novel Memory Mechanism Tailored for LLMs

定义 storage、dense retrieval 和 exploratory forgetting/reinforcement。

### 3 SiliconFriend

把 MemoryBank 接到 ChatGPT、ChatGLM、BELLE，并使用 38k online psychological dialogues 调优部分模型。

### 4 Experiments

15 virtual users、10 days、194 bilingual probes；human annotators 评分 retrieval/correctness/coherence/ranking。

### 5 Related Works

定位于 conversational memory 与 external-memory mechanisms。

### 6 Conclusion

结论主要来自具备 MemoryBank 的三 backbone 比较，缺少 no-memory quantitative control。

## 关键公式 / 图表

### 关键图

### 关键表格

## 实验结论

ChatGPT variant 的 English retrieval/correctness/coherence 为 0.763/0.716/0.912，但表格不能分离 backbone 与 MemoryBank effect。

## 局限性与可追问点

无 no-memory 或 forgetting ablation；数据主要合成，评分协议报告不足，personality inference 和 recall reinforcement 可能累积偏差。

## 对我当前研究/项目的启发

完整 source-grounded project note：`SharedWorldsPrivateMinds/literature/reading_notes/zhong2024memorybank.md`。
