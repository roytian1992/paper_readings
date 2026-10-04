---
id: 2023_how-far-are-large-language-models-from-agents-with-theor_arxiv-2310-03051
title: "How FaR Are Large Language Models From Agents with Theory-of-Mind?"
year: 2023
authors:
  - Pei Zhou
  - Aman Madaan
  - Srividya Pranavi Potharaju
  - Aditya Gupta
  - Kevin R. McKee
  - Ari Holtzman
  - Jay Pujara
  - Xiang Ren
  - Swaroop Mishra
  - Aida Nematzadeh
  - Shyam Upadhyay
  - Manaal Faruqui
venue: "arXiv:2310.03051"
field:
  - Natural Language Processing
  - Artificial Intelligence
direction:
  - Theory of Mind
keywords:
  - T4D
  - Theory of Mind
  - false belief
  - action selection
status: read
source_path: ../sources/2023_how-far-are-large-language-models-from-agents-with-theor_arxiv-2310-03051.pdf
source_archive_path: ""
assets_path: ../assets/2023_how-far-are-large-language-models-from-agents-with-theor_arxiv-2310-03051
paper_type: research
---

# How FaR Are Large Language Models From Agents with Theory-of-Mind?

## 一句话总结

T4D 将 false-belief QA 改成 belief-conditioned action selection，显示 GPT-4 在 ToMi 达到 93% 时，T4D 只有 50%；Foresee-and-Reflect prompt 将其提高到 71.4%。

## 研究问题

模型会回答角色相信什么，不代表它能主动找出信息缺口并选择对角色有帮助的行动。

## 核心方法

约 500 条清洗 ToMi stories 被程序转换为“谁最需要正确位置信息”的多选题；FaR 先预测未来困难，再反思 action。20 位 raters 验证约 80 条样本的一致性。

## 分章节阅读笔记

- 第 3-4 节：核对转换规则、人类一致性、ToMi/T4D 差距与 oracle hints。
- 第 5-6 节：核对 FaR、消融、三个结构变化集与 Faux Pas 迁移。

## 关键公式 / 图表

### 关键图

### 关键表格

## 实验结论

行动相关的 latent inference identification 是独立瓶颈；FaR 有效但 noisy foresight 可将 GPT-4 降至 42%。

## 局限性与可追问点

行动仍是短模板多选，没有真实执行或后续状态更新；正确角色来自原 ToMi question target，且模型版本停留在 2023。

## 对我当前研究/项目的启发

必须同时评估 belief access 与 belief-conditioned action，而不能用 QA 代替角色模拟。完整笔记见 `SharedWorldsPrivateMinds/literature/reading_notes/zhou2023t4d.md`。
