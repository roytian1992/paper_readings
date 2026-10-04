# 阅读笔记完整性修复与核验

开始：2026-10-04；完成：2026-10-05。

本轮将 **23 篇正文解读不足的笔记**按本地原论文重写，并在相关段落内嵌入 **91 张原图**。正文覆盖包括研究问题、真实章节、方法与公式含义、主要结果与消融（原文有则解读）、限制和最终结论；原文无实验的论文没有虚构实验。

完成标准遵循本次要求：正文解读完成即可，不要求逐一翻译全部附录。Re³ 正文以 Discussion 收束；Shadow-Loom 没有独立 Conclusion，已覆盖至 §7 Limitations and future evaluation；Fair Play 的 Methods 位于结论之后，也已完整补入。

## 本轮重写清单

| 笔记 | 正文字符数（不含 YAML） | 内嵌原图 | 正文收束/补读范围 |
|---|---:|---:|---|
| [Narrative Theory](../../reading_notes/2021_narrative-theory-for-computational-narrative-understanding_emnlp-main-26.md) | 10,211 | 2 | 4 Conclusion |
| [StoRM / Reader Models](../../reading_notes/2022_guiding-neural-story-generation-with-reader-models_arxiv-2112-08596.md) | 8,779 | 3 | 6 Broader Impact 与阅读边界 |
| [Re³](../../reading_notes/2022_re3-generating-longer-stories-with-recursive-reprompting_arxiv-2210-06774.md) | 8,170 | 5 | 6 Discussion |
| [Dramatron](../../reading_notes/2023_co-writing-screenplays-and-theatre-scripts-with-language_arxiv-2209-14958.md) | 10,048 | 6 | 8 Conclusions |
| [T4D / FaR](../../reading_notes/2023_how-far-are-large-language-models-from-agents-with-theor_arxiv-2310-03051.md) | 7,887 | 5 | 7 Conclusion |
| [Digital Detectives / ThinkThrice](../../reading_notes/2024_deciphering-digital-detectives-understanding-llm-behavio_doi-10-18653-v1-2024-findings-ac.md) | 9,021 | 4 | 8 Conclusion 与局限 |
| [LoCoMo](../../reading_notes/2024_evaluating-very-long-term-conversational-memory-of-llm-a_doi-10-18653-v1-2024-acl-long-74.md) | 10,184 | 4 | 8 Limitations 与 9 Broader Impacts |
| [MemoryBank](../../reading_notes/2024_memorybank-enhancing-large-language-models-with-long-ter_arxiv-2305-10250.md) | 7,811 | 4 | 6 Conclusion |
| [WhodunitBench](../../reading_notes/2024_whodunitbench-evaluating-large-multimodal-agents-via-mur_doi-10-52202-079017-2751.md) | 9,343 | 4 | 7 Conclusion |
| [MemBench](../../reading_notes/2025_membench-towards-more-comprehensive-evaluation-on-the-me_doi-10-18653-v1-2025-findings-ac.md) | 10,246 | 5 | 5 Conclusion 与 Limitations |
| [P2P](../../reading_notes/2026_11697-p2p-automated-paper-to-p_11697-p2p-automated-paper-to-p.md) | 11,598 | 4 | 6 Conclusion |
| [TSM / Beyond Dialogue Time](../../reading_notes/2026_beyond-dialogue-time-temporal-semantic-memory-for-person_arxiv-2601-07468.md) | 10,793 | 3 | 5 Conclusions 与 Limitations |
| [CoPA](../../reading_notes/2026_copa-benchmarking-personalized-question-answering-with-d_arxiv-2604-14773.md) | 11,648 | 5 | 7 Conclusion、Limitations 与 Ethics Statement |
| [MemoryAgentBench](../../reading_notes/2026_evaluating-memory-in-llm-agents-via-incremental-multi-tu_arxiv-2507-05257.md) | 11,655 | 3 | 5 Conclusion、Ethics 与 Reproducibility |
| [EvoMemBench](../../reading_notes/2026_evomembench-benchmarking-agent-memory-from-a-self-evolvi_arxiv-2605-18421.md) | 11,740 | 4 | 6 Conclusion 与证据边界 |
| [ForeSci](../../reading_notes/2026_foresci-evaluating-llm-agents-for-forward-looking-ai-res_3634-foresci-evaluating-llm-ag.md) | 10,402 | 4 | 6 Conclusion |
| [Lookbacks](../../reading_notes/2026_language-models-use-lookbacks-to-track-beliefs_arxiv-2505-14685.md) | 10,080 | 8 | 8 Conclusion |
| [FAS](../../reading_notes/2026_learning-to-predict-future-aligned-research-proposals-wi_fas.md) | 11,615 | 4 | 6 Conclusion（p.8） |
| [NKW](../../reading_notes/2026_narrative-knowledge-weaver-narrative-centric-retrieval-a_paper.md) | 13,555 | 2 | 6 Conclusion（p.8） |
| [NWM](../../reading_notes/2026_narrative-world-model-narratology-grounded-writer-memory_arxiv-2607-05577.md) | 13,447 | 4 | 9 Conclusion（p.9–10） |
| [SciImpact](../../reading_notes/2026_sciimpact-a-multi-dimensional-multi-field-benchmark-for_sciimpact.md) | 11,012 | 4 | 5 Conclusion（p.9） |
| [Shadow-Loom](../../reading_notes/2026_shadow-loom-causal-reasoning-over-graphical-world-models_arxiv-2605-02475.md) | 11,233 | 1 | §1–7；补读 A 的核心机制及 B.8 内部审计 |
| [Fair Play](../../reading_notes/2026_the-challenge-and-reward-of-fair-play-in-narrative-a-com_arxiv-2507-13841.md) | 14,354 | 3 | §1–6 Conclusion + §7 Methods |

## 同时修复的问题

- RF-Mem 原笔记的 §4 Related Works 为空，现已依据 `chapter/5rela.tex` 补齐三条相关工作脉络。
- 清理原有笔记中 66 个没有内容的模板标题；保留已经在正文中完成的图表、结果和限制解读，并修正 DGM/Agents’ Room 的图表标题层级。
- ReMe 的指示函数使用兼容写法 `\mathbf{1}`；本轮将它纳入全库公式检查。
- 同步 23 篇重写笔记的章节与图像来源到 `metadata/papers.jsonl`，刷新索引。原始笔记和元数据备份在 [originals](originals/)。

## 关键内容纠正示例

| 论文 | 已纠正或明确标注的内容 |
|---|---|
| P2P | 补全生成/数据/实验；严格区分人工“更好”与“更好或持平”；XGBoost 的 KL 并非表中最佳；消融并非所有指标单调提高。 |
| Narrative Theory | narrative economies 是社会中的叙事生产/流通；narrative beliefs 是深层社会故事，并非局部角色信念数据库。 |
| FAS / NWM | 区分相对百分比与百分点；保留基线更强、去类型不降分和未达显著性的结果；未来生成实验未冒充已验证结果。 |
| TSM / CoPA / SciImpact / ForeSci | 原稿的数值、数量或日期前后不一致均就近说明，没有擅自改成一致结果。 |
| Shadow-Loom | 区分系统设计/内部样例与外部验证；按详细附录说明 EFK、Beta 更新，并标注正文版本差异及样本数矛盾。 |

## 核验结果与实际范围

- 全库 43 篇笔记已检查本地来源和图片链接；共 243 处图片引用均可定位且图片文件可解码，错误 0。
- 39 篇含数学表达式的笔记，共 1,401 个表达式通过 KaTeX 语法检查，解析错误 0。这验证数学语法兼容性，不替代具体 Markdown 客户端的界面测试。
- 23 篇重写稿逐篇对照原文，原图经过裁切检查并有来源页码；P2P、Narrative Theory、Lookbacks、Shadow-Loom 又经另一位阅读代理独立复查。
- 其余 20 篇主要做正文结构、空标题、图片/来源链接和数学语法检查；本轮未把它们宣称为重新全文精读。RF-Mem 的空缺章节另行补读。
- 图表数值来自相应论文；未运行论文的外部代码或复现实验。原文未报告的统计显著性、泛化效果和读者验证没有被补写成事实。

## 可复查记录

- [逐篇核验与图像来源汇总](final_audit.json)
- [数学表达式解析结果](math_audit.json)
- [记忆论文及三篇独立复查记录](memory_notes_source_audit.md)
- [叙事论文核验记录](narrative_agent_audit.json)
- [科研评测与 Fair Play 核验记录](research_notes_quality.json)
- [空标题清理记录](additional_cleanup.json)

每篇新图片的原始页码与裁切坐标另保存在相应 assets 目录的来源 JSON 中；索引与笔记仍位于原来的路径。
