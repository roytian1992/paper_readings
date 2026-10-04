---
id: 2024_deciphering-digital-detectives-understanding-llm-behavio_doi-10-18653-v1-2024-findings-ac
title: "Deciphering Digital Detectives: Understanding LLM Behaviors and Capabilities in Multi-Agent Mystery Games"
year: 2024
authors:
  - Dekun Wu
  - Haochen Shi
  - Zhiyuan Sun
  - Bang Liu
venue: "Findings of ACL 2024"
field:
  - Natural Language Processing
  - Artificial Intelligence
direction:
  - Multi-Agent Evaluation
  - Naturalistic Narrative Data
keywords:
  - Jubensha
  - Digital Detectives
  - private information
  - multi-agent
status: read
source_path: ../sources/2024_deciphering-digital-detectives-understanding-llm-behavio_doi-10-18653-v1-2024-findings-ac.pdf
source_archive_path: ""
assets_path: ../assets/2024_deciphering-digital-detectives-understanding-llm-behavio_doi-10-18653-v1-2024-findings-ac
paper_type: benchmark
---

# Deciphering Digital Detectives: Understanding LLM Behaviors and Capabilities in Multi-Agent Mystery Games

## 一句话总结

ThinkThrice 让多个 LLM 持有不同中文剧本杀角色剧本并轮流互动，以 memory retrieval、self-refinement 和 self-verification 改善信息交换，再用事实题、跨角色推理和凶手识别做诊断。

## 研究问题

剧本杀包含长文本、角色私有信息、对抗合作和多轮推理；单独看 win rate 无法区分 agent 是否真正获取并使用了案件信息。

## 核心方法

1,115 个中文游戏被转成统一 JSON；角色数 1--20（均值 6.52），长度 4k--518k tokens（均值 129k），并含图像/音频/视频，但论文实验只用文本。每个角色拥有私有向量库，MR 取 top 5 历史观察，SR 分解问题并从自己的剧本补充事实，SV 将答案拆成事实与剧本核验。

## 分章节阅读笔记

### 1 Introduction

提出数据、多人游戏框架、两类细粒度评测和三阶段 prompting 模块四项贡献。

### 2 Related Work

将 Jubensha 与 Werewolf/Avalon 区分：前者背景、角色和关系每局变化，文本与推理负担更重。

### 3 Jubensha Dataset

数据来自中文在线来源，含 host manual、上帝视角复盘、线索和角色剧本。作者用 OCR 等工具统一成 Markdown/JSON。论文称共享时限于 academic non-commercial fair use，但没有说明底层剧本权利已获许可。

### 4 The ThinkThrice Framework for Jubensha Games

4--5 个 LLM 角色同步轮流行动，固定 host 控制流程。SR 的目标是提高有限轮次内的信息量；SV 以真实性与事实数量阈值重试，并保存最高分答案。

### 5 Evaluating LLM-based Agents in Jubensha Games

正式实验仅选 4 个游戏：LLM 生成 720 个 factual questions，人工构造 56 个需要组合不同角色信息的 inferential questions。

### 6 Experiment

Table 6 无 MR 时 own/other accuracy 为 0.770/0.305；完整 MR+SR+SV(N=3) 为 0.772/0.498。聊天与全剧本的 OpenAI embedding similarity 从 0.062 升至 0.831。完整组合也有最高 civilian win、murderer identification 和推理表现；full-script access 仍明显更好。

### 7 Future Work

作者计划扩大实验游戏、自动生成推理题、加入 micro metrics 和多模态/多结局脚本。

### 8 Conclusion

结论聚焦信息获取和推理，而不是把胜负当成唯一 agent 能力指标。

### Ethical Considerations and Limitations

数据限中文，API 成本高，GPT 版本更新影响复现。固定仓库 `jackwu502/ThinkThrice@d0903987ec0d9e286f62323c363251361ba57e40` 无 LICENSE，数据需表单申请，README 仍将事实/推理评测代码标为未发布。

## 关键公式 / 图表

### 关键图

### 关键表格

## 实验结论

信息获取是独立瓶颈；检索、补全和核验能提高覆盖与任务结果，但完整私有信息 oracle 仍显著更强。相似度指标只测文本覆盖，不等于事实或 belief 正确。

## 局限性与可追问点

4 个游戏不足以代表 1,115 个来源；没有稳定完整复现包。最重要的是公开可访问与 fair use 不能授予第三方再分发/衍生权，因而数据只能作受限参考。

## 对我当前研究/项目的启发

truth replay、role scripts、clue rounds 与 cross-role QA 很适合 world/private-mind schema；但应在作者创作或明确许可的等价世界上实现，并把 access、inference 与 action 指标分开。
