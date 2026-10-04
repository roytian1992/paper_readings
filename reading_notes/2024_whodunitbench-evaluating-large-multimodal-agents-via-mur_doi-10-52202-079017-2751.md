---
id: 2024_whodunitbench-evaluating-large-multimodal-agents-via-mur_doi-10-52202-079017-2751
title: "WhodunitBench: Evaluating Large Multimodal Agents via Murder Mystery Games"
year: 2024
authors:
  - Junlin Xie
  - Ruifei Zhang
  - Zhihong Chen
  - Xiang Wan
  - Guanbin Li
venue: "NeurIPS 2024 Datasets and Benchmarks"
field:
  - Artificial Intelligence
  - Multimodal Learning
direction:
  - Agent Evaluation
  - Naturalistic Narrative Data
keywords:
  - WhodunitBench
  - murder mystery
  - private clues
  - multimodal agents
status: read
source_path: ../sources/2024_whodunitbench-evaluating-large-multimodal-agents-via-mur_doi-10-52202-079017-2751.pdf
source_archive_path: ""
assets_path: ../assets/2024_whodunitbench-evaluating-large-multimodal-agents-via-mur_doi-10-52202-079017-2751
paper_type: benchmark
---

# WhodunitBench: Evaluating Large Multimodal Agents via Murder Mystery Games

## 一句话总结

WhodunitBench 用 50 个多模态剧本杀同时构建对战 arena 与 perception-interaction-cognition 诊断链，但论文和仓库都没有为原剧本提供可转授 IP 许可。

## 研究问题

静态 QA 不能充分测试 agent 在动态、不完全信息环境中同时感知长文本/图像、扮演角色、选择询问对象并完成多步推理的能力。

## 核心方法

领域专家筛选 50 个剧本并清洗 OCR、图像线索和时间线。CoE 包含 1,911 个感知题（283 LS、1,103 TRI、525 MRI）与 1,308 个多步推理题，共 3,219 个闭式题，另有开放式凶手动机/手法、关键线索和关键角色标注。arena 以凶手/非凶手阵营胜率评价，CoE 用八个指标拆解能力。

## 分章节阅读笔记

### 1 Introduction

把 murder mystery 作为需要多模态感知、高层 cognition、role play 和 decision making 的组合环境。

### 2 Related Work

对比静态 benchmark 与较简单文本游戏，强调多阶段、信息不完整和长链推理。

### 3 WhodunitBench: Construction

五名专家从公开网站/产业平台选择剧本，十名专家标题与 reasoning chains，三名专家复核。感知题覆盖长剧本和两类图像；推理题的 distractors 由 GPT-4 生成后人工修订。

### 4 WhodunitBench: Arena-style Evaluation

五种 LMA 与 naive murderer 或彼此对战。非凶手平均 win ratio 从 Yi-Vision 11.1% 到 GPT-4V 24.2%；强模型扮凶手并不总更难识别，可能因过度发言暴露。

### 5 WhodunitBench: Chain of Evaluation (CoE)

指标为 LSU/TIU/MIU、role-play、scenario progression、询问关键角色、MMR 与 CMD。Direct 设置平均分 Yi-Vision 21.57、Qwen 22.45、Gemini 41.81、Claude 40.19、GPT-4V 45.84。CoT 并非总有益；质例出现无关提问、忘记阵营和虚构 NPC。

### 6 Limitations and Potential Societal Impact

interaction 与 reasoning 纠缠，任务不覆盖全部推理类型，长剧本与多模态 API 使评测昂贵。

### 7 Conclusion

作者把低胜率和低 CoE 分数解释为当前 LMA 对动态组合任务仍不足。

### Appendix A.3 Dataset Documentation and A.5 Author Statement

原剧本来自公开网站，作者承认知识产权属于原作者/平台，不主张其权利，且明确数据集不在任何 copyright/IP license 下；团队只拥有标注版权。固定仓库 `jun0wanan/WhodunitBench-Murder_Mystery_Games@8ef9b20b6551561e165274185ef25fc290fee267` 含 50 个 Dataset 目录但无 LICENSE。

## 关键公式 / 图表

### 关键图

### 关键表格

## 实验结论

当前 LMA 在基础感知外的互动和多步推理仍弱；CoE 比单一胜率提供更细诊断，但论文没有跨 seed 误差条或独立人工验证所有自动指标。

## 局限性与可追问点

自动 GPT-4 评分、单次对战和服务版本影响稳定性。版权说明与“open source”宣传不能混同；无许可证意味着不能按开放 benchmark 再分发。

## 对我当前研究/项目的启发

可复用的是 schema 思路：world truth、private/public clues、reasoning chain 和 staged reveal；不可复用的是原始 payload。项目自创世界应保留同样的 access-interaction-action-reasoning 分解。
