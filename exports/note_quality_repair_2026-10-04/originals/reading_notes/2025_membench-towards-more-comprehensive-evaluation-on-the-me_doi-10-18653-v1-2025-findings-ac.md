---
id: 2025_membench-towards-more-comprehensive-evaluation-on-the-me_doi-10-18653-v1-2025-findings-ac
title: "MemBench: Towards More Comprehensive Evaluation on the Memory of LLM-based Agents"
year: 2025
authors:
  - Haoran Tan
  - Zeyu Zhang
  - Chen Ma
  - Xu Chen
  - Quanyu Dai
  - Zhenhua Dong
venue: "Findings of ACL 2025"
field:
  - Natural Language Processing
  - Artificial Intelligence
direction:
  - Agent Memory Evaluation
keywords:
  - MemBench
  - agent memory
  - factual memory
  - reflective memory
status: read
source_path: ../sources/2025_membench-towards-more-comprehensive-evaluation-on-the-me_doi-10-18653-v1-2025-findings-ac.pdf
source_archive_path: ""
assets_path: ../assets/2025_membench-towards-more-comprehensive-evaluation-on-the-me_doi-10-18653-v1-2025-findings-ac
paper_type: research
---

# MemBench: Towards More Comprehensive Evaluation on the Memory of LLM-based Agents

## 一句话总结

MemBench 用“参与/观察 x 事实/反思”合成数据和 accuracy、retrieval recall、读写延迟、容量曲线四类指标，比较七种 agent memory mechanisms。

## 研究问题

长期助理记忆评测不能只测第一人称事实 recall，还需覆盖第三人称观察、跨证据偏好归纳、效率与历史增长后的性能退化。

## 核心方法

论文从 500 个合成 user relation graphs 生成约 65k sessions、53k questions，以 MovieLens、Food、Goodreads 和 GPT-4o-mini 构造偏好证据，并用无关 news noise 扩展上下文。评测把消息逐轮摄取，再比较 Full/Recent/Retrieval Memory、Generative Agents、MemoryBank、MemGPT 和 SCMemory。

## 分章节阅读笔记

- 第 3 节：核对关系图采样、参与/观察场景、事实/反思标签、四类指标及 Table 2 数据量。
- 第 4 节：核对普通/100k 抽样方案、Tables 3-5 主结果、容量曲线与 backbone 对比。
- Limitations/Appendices：确认结构化合成数据边界、完整类别统计与 prompts。

## 关键公式 / 图表

### 关键图

### 关键表格

Table 3/4 中 RetrievalMemory 在 100k factual 和 reflective 条件通常最强；MemoryBank write time 与 MemGPT read time 明显高于简单检索。主表长上下文子集样本较小且未报告不确定性。

## 实验结论

长历史下简单 retrieval 可优于 full/recent context 与复杂压缩机制，但系统结果高度依赖 reader backbone、chunking 和实现成本，不能只按 memory mechanism 名称归因。

## 局限性与可追问点

数据是结构化、模板化和 LLM 生成的个人画像；reflective memory 主要是偏好/情绪归纳，不等于 false belief 或自然叙事认知。官方固定 revision 没有 LICENSE 文件，README 只有 MIT 徽章，数据许可仍需澄清。

## 对我当前研究/项目的启发

可借鉴参与/观察输入和 accuracy/recall/cost/capacity 分解；不应把它当作 private-mind、authority 或 branch-lifecycle 证据。项目级完整笔记见 `SharedWorldsPrivateMinds/literature/reading_notes/tan2025membench.md`。
