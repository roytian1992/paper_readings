# Narrative Memory as Constrained Generation 调研

更新时间：2026-06-10

## 新的核心创新点

这个课题不应再写成“叙述时间线 != 真实时间线”和“多角色多视角记忆”两个并列创新点。更准确的 formulation 是：

> 叙事记忆是一种受限生成问题：系统需要把按真实时间组织的实际记忆 M1，受角色主观记忆 M2 和叙事目的约束，生成/更新为按写作呈现顺序组织的 discourse memory M3。

三类 memory：

- **M1 Truth Memory**：按真实时间顺序组织的完整故事真相。
- **M2 Character Memory**：每个角色的可知、误知、推断和 false belief。
- **M3 Discourse Memory**：按写作/阅读顺序组织的呈现状态，包括读者已知、伏笔、悬念、反转和 reveal schedule。

核心不是“存三份 memory”，而是：

> 如何从 M1 到 M3 做 constrained realization，使文本既符合真实故事世界，又不能泄露当前 POV 角色和读者尚不该知道的信息，同时服务叙事目的。

## 文件说明

- [00_problem_formulation.md](00_problem_formulation.md)：新的问题定义和与已有工作的精确边界。
- [01_strict_related_work.md](01_strict_related_work.md)：严格相关工作，即已经处理 story world 到 discourse realization、focalization、reader knowledge、character belief、reveal control 的工作。
- [02_direct_related_work.md](02_direct_related_work.md)：直接相关但不完全命中的工作，包括 LLM/agent memory、长篇故事生成、非线性故事生成、ToM。
- [03_benchmarks.md](03_benchmarks.md)：可用 benchmark 和它们与本问题的差距。
- [04_literary_narratology_sources.md](04_literary_narratology_sources.md)：文学细读和叙事学材料源，可用于 stress test 和标注 schema 设计。
- [papers.tsv](papers.tsv)：论文/benchmark 清单。

## 一句话区别

与最接近的 Multi-Agent Character Simulation 相比：

> 它把写作呈现顺序当作给定 presentation outline 和最终 rewrite 目标；我们把 discourse memory M3 当作可调、可更新、可验证的状态，研究如何在角色知识边界和叙事目标约束下从真实记忆 M1 受限生成 M3。

## 调研后的判断

新 formulation 下，之前遗漏的经典 computational narrative 工作反而更关键，尤其是：

- focalization / point-of-view narrative generation；
- reader-model-based suspense generation；
- character belief / false belief narrative planning；
- flashback、foreshadowing、reveal order 控制。

这些工作说明“受限呈现”不是无人做过；你们的新意需要落在 LLM/agent memory 场景下的统一状态表示、可调 M3、自动评测和长篇生成。
