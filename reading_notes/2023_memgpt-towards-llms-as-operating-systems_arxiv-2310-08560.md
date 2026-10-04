---
id: 2023_memgpt-towards-llms-as-operating-systems_arxiv-2310-08560
title: "MemGPT: Towards LLMs as Operating Systems"
year: 2023
authors:
  - Charles Packer
  - Sarah Wooders
  - Kevin Lin
  - Vivian Fang
  - Shishir G. Patil
  - Ion Stoica
  - Joseph E. Gonzalez
venue: ""
field:
  - NLP
  - Systems
direction:
  - LLM Agents
  - Long-context LLM
  - Memory
keywords:
  - MemGPT
  - MemoryGPT
  - virtual context management
  - LLM OS
  - hierarchical memory
status: read
source_path: ""
source_archive_path: ../sources/2023_memgpt-towards-llms-as-operating-systems_arxiv-2310-08560_source.tar.gz
assets_path: ../assets/2023_memgpt-towards-llms-as-operating-systems_arxiv-2310-08560
paper_type: research
---

# MemGPT: Towards LLMs as Operating Systems

## 一句话总结

MemGPT 将 LLM 的固定上下文窗口视为类似操作系统“物理内存”的稀缺资源，通过分层记忆、函数调用和事件驱动控制流，让模型在对话和文档分析中主动把信息写入、检索并换入上下文，从而近似获得更长甚至“无限”的可用上下文。

## 研究问题

论文关注的问题是：当 LLM 的上下文窗口固定且扩展成本很高时，如何让模型仍能处理长对话、长文档和跨多源信息整合任务。作者指出，单纯扩大 transformer context 会带来注意力计算成本，并且长上下文模型也可能无法稳定利用中间位置的信息；因此需要一种不依赖无限扩展上下文长度的系统方法。

## 核心方法

MemGPT 的核心方法是 virtual context management。系统把 prompt tokens 划分为 system instructions、working context 和 FIFO queue，并在上下文之外维护 external context，包括 archival storage 和 recall storage。LLM 通过函数调用自主管理这些存储层：在 memory pressure warning 出现时保存重要信息，在回答问题时搜索并分页取回外部记忆，并通过 `request_heartbeat=true` 触发连续函数调用，使模型能够在一次用户请求中执行多步检索、更新和推理。这个设计借鉴了操作系统中的分层内存、分页、缺页处理和中断式控制流。

## 分章节阅读笔记

### 1 Introduction

引言首先把问题定位在固定上下文窗口对 LLM 应用能力的限制上。LLM 已经成为对话式 AI 和很多应用的基础，但标准 transformer 架构仍然依赖有限长度的输入上下文。对于长对话，模型只能看到最近若干轮消息；对于长文档，模型只能处理短文本片段。这使得模型在需要长期连续交互、用户记忆、跨文档分析或长文本推理时很容易丢失关键信息。

作者强调，直接扩大 context window 并不是充分解法。一方面，self-attention 的计算和显存开销随上下文长度增长而快速上升；另一方面，即使模型拥有更长上下文，已有研究也显示模型不一定能有效使用全部上下文，尤其容易忽视上下文中间位置的信息。因此，论文要解决的不是“如何训练一个无限长上下文模型”，而是“如何在继续使用固定上下文模型的前提下，给用户和应用提供近似无限上下文的能力”。

MemGPT 的关键类比来自操作系统的 virtual memory paging。传统 OS 中，应用并不直接关心真实物理内存是否足够，而是通过虚拟内存获得更大的地址空间；OS 会把暂时不用的数据换出到磁盘，并在需要时再换入主内存。论文把这个思想迁移到 LLM：context window 相当于 main memory 或 physical memory，外部数据库/存储相当于 disk，MemGPT 充当一个面向 LLM 的“操作系统”，负责让模型决定哪些信息应该留在当前 prompt 中，哪些信息应该被写入外部存储，以及何时把历史信息重新检索回来。

![Memory creation](../assets/2023_memgpt-towards-llms-as-operating-systems_arxiv-2310-08560/figures/intro_figure_memory_creation.png)

这张 memory creation 图说明了引言中的一个核心机制：当系统检测到上下文空间不足时，会向 MemGPT 发出类似 memory pressure 的提醒；MemGPT 随后可以把当前对话中重要但即将被挤出上下文的信息写入持久记忆。这里的重点不是简单摘要，而是让模型主动判断哪些信息值得保存。

![Memory search](../assets/2023_memgpt-towards-llms-as-operating-systems_arxiv-2310-08560/figures/intro_figure_memory_search.png)

memory search 图对应另一个方向：当回答当前问题所需的信息不在上下文中时，MemGPT 可以搜索 out-of-context data，并把相关结果重新带入当前上下文。这样，模型的可用信息不再局限于 prompt 中直接可见的 token，而是可以通过函数调用在外部记忆中分页查找。

引言还指出，function calling 是 MemGPT 能够实现这种机制的技术前提。通过函数调用，LLM agent 可以读写外部数据源、修改自己的上下文，并决定何时把控制权交回用户。更重要的是，函数调用不只用于检索，还用于控制流：模型可以在一次任务中多次调用函数、检查返回结果、继续检索或更新上下文，然后再生成最终回答。这使 MemGPT 能够迭代地调整当前上下文，而不是被动接受一次性拼接好的 prompt。

![System flow](../assets/2023_memgpt-towards-llms-as-operating-systems_arxiv-2310-08560/figures/intro_figure_system_flow.png)

system flow 图给出了引言层面的整体架构。固定上下文 LLM processor 被放在一个分层记忆系统中：输入侧的 main context 包括 system instructions、working context 和 FIFO queue；输出侧的 completion tokens 会被 function executor 解释为函数调用；函数再负责在 main context 与 external context 之间移动信息。图中提到的 `request_heartbeat=true` 是 function chaining 的关键标志，它允许一次函数调用结束后立即触发下一轮 LLM 推理，从而支持多步检索和多步记忆管理。

引言最后用两个应用域说明 MemGPT 的验证目标。第一类是 document analysis，因为真实文档可能远超模型上下文窗口，并且跨文档任务需要从多个来源整合信息。第二类是 conversational agents，因为长期对话需要记住用户事实、偏好、事件和 persona，以保持一致性和个性化。作者的论证路径是：如果 MemGPT 能在这两个高度依赖长期上下文的场景中优于固定上下文基线，就能说明 OS-inspired memory management 对 LLM 系统是有实际价值的。

这一节在全文中的作用是建立问题框架：有限上下文不是单纯的模型规模问题，也可以被看作系统层的资源管理问题。MemGPT 的贡献因此不是提出一个新的 transformer 架构，而是提出一种 LLM 系统设计范式，把上下文管理、外部记忆、函数调用和事件驱动控制流组合起来，让固定上下文模型获得更长程的工作能力。

### 2 MemGPT (MemoryGPT)

这一章正式给出 MemGPT 的系统设计。作者先把 MemGPT 的记忆架构分成两大类：`main context` 和 `external context`。`main context` 指当前会被送入 LLM 推理的 prompt tokens，相当于操作系统中的主内存、物理内存或 RAM；只要信息在 main context 中，LLM processor 就能在本轮推理时直接访问。`external context` 指固定上下文窗口之外的所有信息，相当于磁盘或外部存储；这些信息不会被模型自动看到，必须通过函数调用显式移动到 main context 里，才会参与生成。

这个区分是理解 MemGPT 的基础：它不是把所有历史都塞进 prompt，而是承认 prompt 是稀缺资源，再设计一套机制让 LLM 自己管理哪些内容进入 prompt、哪些内容留在外部存储。换句话说，MemGPT 的目标不是消除上下文限制，而是在限制存在时进行资源调度。

### 2.1 Main context (prompt tokens)

`main context` 被拆成三个连续区域：`system instructions`、`working context` 和 `FIFO queue`。这三个区域共同组成 LLM 每次推理时实际看到的输入。

`system instructions` 是只读区域，类似系统内核给 agent 的固定运行规则。它描述 MemGPT 的控制流、不同记忆层级的用途，以及可调用函数的使用方式，例如什么时候检索外部数据、什么时候写入记忆。这个区域的作用是让 LLM 具备“如何管理自己上下文”的操作规程。

`working context` 是固定大小、可读写的非结构化文本块，但只能通过 MemGPT 的函数调用修改。在对话场景中，它用于保存用户和 agent persona 的关键事实、偏好、长期目标或其他稳定信息。它可以理解为当前 agent 的高优先级工作记忆：内容不一定来自最近消息，但应该是持续影响后续对话的核心状态。

`FIFO queue` 保存滚动消息历史，包括用户与 agent 的对话、系统消息、memory warning、函数调用输入和函数返回结果。它采用先进先出方式维持最近上下文；当旧消息被逐出时，队列第一个位置还会保存一个递归摘要，用来保留被移除消息的大致脉络。这个设计把“短期原文历史”和“压缩后的远期历史”放在同一个上下文区域中，但更细粒度的历史仍会保存在外部 recall storage 里。

### 2.2 Queue Manager

`Queue Manager` 负责在 `FIFO queue` 和 `recall storage` 之间管理消息。新消息进入系统后，Queue Manager 会把它追加到 FIFO queue，拼接当前 prompt tokens，并触发 LLM 生成 completion tokens。与此同时，输入消息和模型输出都会写入 `recall storage`，也就是 MemGPT 的消息数据库。之后如果 LLM 通过函数调用检索到这些历史消息，Queue Manager 会把检索结果重新追加到队列后方，使其重新进入当前上下文窗口。

Queue Manager 的另一个职责是处理上下文溢出。作者设计了两个阈值：`warning token count` 和 `flush token count`。当 prompt tokens 超过 warning 阈值，例如上下文窗口的 70% 时，系统会向队列插入一条 memory pressure warning，提醒 LLM 队列即将被逐出。这个提醒给 LLM 留出主动处理的机会：它可以把 FIFO queue 中重要信息写入 working context，或写入 `archival storage`，也就是可读写、可保存任意长度文本对象的外部数据库。

当 prompt tokens 达到 flush 阈值，例如上下文窗口的 100% 时，Queue Manager 会真正释放空间：它会逐出一定数量的消息，例如 50% 上下文窗口对应的消息量，并用已有递归摘要和被逐出消息生成新的递归摘要。被逐出的消息不再直接可见，但会永久留在 recall storage 中，之后仍可通过函数调用找回。这里的关键点是，MemGPT 把“丢出上下文”与“彻底遗忘”分开了：上下文窗口只负责当前可见性，外部存储负责长期可恢复性。

### 2.3 Function executor (handling of completion tokens)

`Function executor` 负责解释和执行 LLM 生成的函数调用，是 MemGPT 能够自主管理记忆的执行层。LLM 不只是生成自然语言回答，还可以输出结构化函数调用；MemGPT 解析这些输出、验证参数，如果合法就执行对应函数，再把执行结果或运行错误反馈回 LLM。这个反馈循环让模型能够根据外部操作结果调整后续行为。

在作者的设计里，记忆编辑和检索都是 self-directed 的。系统并不是由用户显式指定“请保存这条信息”或“请检索某段历史”，而是通过 system instructions 中的记忆层级说明和函数 schema，引导 LLM 自己判断何时移动信息。例如，对话历史变长时，LLM 可以主动保存关键用户事实；当前任务需要旧信息时，LLM 可以检索 recall 或 archival storage；如果当前 working context 中的信息过时，LLM 也可以更新它。

![Memory correction](../assets/2023_memgpt-towards-llms-as-operating-systems_arxiv-2310-08560/figures/method_figure_memory_correction.png)

这张 memory correction 图对应 Function executor 的一个重要能力：MemGPT 不只是“追加记忆”，还可以修改已经存储的工作记忆。当用户提供新信息、纠正旧信息或上下文状态发生变化时，模型可以通过函数调用更新 working context，使 agent 的长期状态与当前对话保持一致。

作者还强调上下文限制意识对 self-editing 很关键。MemGPT 会通过 token 限制警告提示 LLM 进行记忆管理；检索机制也要考虑 token 预算，因此采用 pagination，避免一次检索把上下文撑爆。这一点很实际：如果外部记忆检索不受控，系统只是把“长上下文问题”转化成“检索结果过长问题”，仍然无法稳定运行。

原文在这里插入一个上下文长度对比表，说明不同模型/API 的上下文窗口仍然有限，即使较长窗口也只对应有限消息轮数。

| Model / API name | Open? | Context tokens | Approx. messages |
|---|---:|---:|---:|
| Llama (1) | yes | 2k | 20 |
| Llama 2 | yes | 4k | 60 |
| GPT-3.5 Turbo (release) | no | 4k | 60 |
| Mistral 7B | yes | 8k | 140 |
| GPT-4 (release) | no | 8k | 140 |
| GPT-3.5 Turbo | no | 16k | 300 |
| GPT-4 | no | 32k | ~600 |
| Claude 2 | no | 100k | ~2000 |
| GPT-4 Turbo | no | 128k | ~2600 |
| Yi-34B-200k | yes | 200k | ~4000 |

表格的作用不是给出最新模型排行，而是支撑论文的系统设计动机：即便上下文窗口已经从几千 token 扩展到十万甚至二十万 token，长期对话和大规模文档任务仍可能超过窗口；而且更大的窗口并不自动解决有效利用问题。

### 2.4 Control flow and function chaining

MemGPT 的控制流是事件驱动的。`events` 是触发 LLM 推理的通用输入，可以是用户消息、系统消息、上下文容量警告、用户交互事件，例如用户登录或上传文档，也可以是定时事件。MemGPT 会先用 parser 把这些事件转换成普通文本消息，追加到 main context，然后交给 LLM processor 推理。

`function chaining` 解决的是多步任务中的连续工具调用问题。很多实际任务不能靠一次检索完成，例如翻页查看多个检索结果、从多个文档中收集证据、或在多个外部数据源之间组合信息。MemGPT 允许函数调用携带一个特殊标志，请求函数执行完后立即把控制权交回 LLM processor。这样，函数输出会被加入 main context，模型马上进行下一轮推理，并决定是否继续调用函数。

如果函数调用没有这个标志，系统就进入 `yield` 状态：MemGPT 暂停 LLM processor，直到下一个外部事件到来，例如用户发来新消息或定时中断触发。这个设计使 MemGPT 能在“自主连续处理”和“等待用户/系统事件”之间切换。它也是 MemGPT 与普通 RAG 或一次性工具调用的区别之一：MemGPT 的记忆访问可以成为一个多步控制流程，而不只是生成前的一次检索。

本章的核心结论是，MemGPT 把 LLM agent 的上下文窗口重构成一个可管理的系统资源。`main context` 定义当前可见内存，`Queue Manager` 管理短期消息和溢出，`Function executor` 执行自主管理动作，`function chaining` 支持多步检索与控制流。这个系统设计为后续实验中的长对话一致性、个性化开场、多文档 QA 和 nested KV 多跳检索提供了机制基础。

### 3 Experiments

实验章的目标是验证 MemGPT 是否真的能把“系统层的记忆管理”转化为长上下文任务中的性能收益。作者选择了两个长上下文场景：一类是 conversational agents，关注长期对话中的一致性和参与感；另一类是 document analysis，关注长文档、多文档和多跳信息检索。实验并不是只比较一个固定模型，而是把 MemGPT 接到不同底座模型上，包括 GPT-3.5 Turbo、GPT-4 和 GPT-4 Turbo，以观察底座模型能力对 MemGPT 的影响。

论文中的模型版本需要按当时实验设置理解：`GPT-4 Turbo` 指 `gpt-4-1106-preview`，上下文窗口为 128k；`GPT-4` 指 `gpt-4-0613`，上下文窗口为 8192；`GPT-3.5 Turbo` 指 `gpt-3.5-turbo-1106`，上下文窗口为 16385。作者关心的问题不是单纯“哪个模型更强”，而是：当同一个底座模型加上 MemGPT 后，是否比固定上下文使用方式更能处理长期信息。

### 3.1 MemGPT for conversational agents

对话代理实验围绕两个长期交互能力展开：`Consistency` 和 `Engagement`。一致性要求 agent 能让新事实、偏好和事件与过去对话保持一致；参与感要求 agent 能主动利用长期用户信息，让回复更个性化、更像连续关系中的自然对话。作者使用 Multi-Session Chat (MSC) 数据集作为基础，因为 MSC 本身包含多轮多会话对话，并要求角色在多个 session 中保持一致 persona。

这里的实验设计和前面系统章节直接对应：如果 MemGPT 的 recall storage、working context 和函数检索机制有效，那么 agent 应该能从过去会话中找回信息，并把它用于当前回复；如果没有有效记忆，模型即使语言能力强，也会因为看不到历史而难以保持一致或个性化。

### 3.1.1 Deep memory retrieval task (consistency)

Deep Memory Retrieval (DMR) 是作者为测试一致性新构造的任务。任务形式是：用户问 agent 一个明确依赖过去会话的问题，而且正确答案范围很窄。作者用额外的 LLM 根据 MSC 的前五个 session 生成这些 QA 对，第六个 session 只包含一个问答回合，用来测试 agent 是否能利用过去会话知识回答。

评价指标有两类。第一类是 LLM judge 判断生成回答是否与 gold response 一致，得到 accuracy；第二类是 ROUGE-L recall。作者特别使用 recall，是因为模型生成回复往往比 gold answer 更长，单纯用精确匹配或普通重叠指标会惩罚这种 verbosity。固定上下文 baseline 能看到过去五段对话的有损摘要；MemGPT 则能访问完整历史，但必须通过分页检索把相关记忆带回 main context。

| Model | Accuracy | ROUGE-L (R) |
|---|---:|---:|
| GPT-3.5 Turbo | 38.7% | 0.394 |
| + MemGPT | 66.9% | 0.629 |
| GPT-4 | 32.1% | 0.296 |
| + MemGPT | 92.5% | 0.814 |
| GPT-4 Turbo | 35.3% | 0.359 |
| + MemGPT | 93.4% | 0.827 |

结果显示，加上 MemGPT 后三个底座模型都明显提升。GPT-4 和 GPT-4 Turbo 的提升尤其大，从三成左右 accuracy 提升到九成以上。这个结果支持作者的核心主张：长期对话中的失败不只是语言模型能力不足，而是缺少可访问、可检索的长期记忆。MemGPT 通过完整历史存储和分页检索，让模型能够在需要时找回过去信息，从而保持回答一致。

### 3.1.2 Conversation opener task (engagement)

Conversation opener 任务测试 agent 是否能在新会话开始时主动生成有参与感的开场白。一个好的 opener 不只是泛泛问候，而应该引用用户或 persona 中的长期信息。作者用生成 opener 与 gold persona labels 的相似度，以及与人工 opener 的相似度来评估，指标包括 `SIM-1`、`SIM-3` 和 `SIM-H`。

| Method | SIM-1 | SIM-3 | SIM-H |
|---|---:|---:|---:|
| Human | 0.800 | 0.800 | 1.000 |
| GPT-3.5 Turbo | 0.830 | 0.812 | 0.817 |
| GPT-4 | 0.868 | 0.843 | 0.773 |
| GPT-4 Turbo | 0.857 | 0.828 | 0.767 |

这张表说明 MemGPT 生成的 opener 在 persona 相似度上能够达到甚至超过人工 opener。作者观察到，MemGPT 的 opener 通常更长，也覆盖更多 persona 信息；这有助于提高与 persona labels 的相似度，但也意味着它不一定在自然度或简洁性上完全等同于人工开场。对论文论证而言，这个实验主要说明 working context 中保存的长期用户信息能被实际用于生成，而不仅仅是被动存储。

### 3.2 MemGPT for document analysis

文档分析实验检验的是 MemGPT 在非对话场景中的长上下文能力。作者指出，很多真实文档远超常见上下文窗口，例如法律或金融文档可能达到百万 token；而实际分析任务还经常需要跨多个长文档建立联系。这个场景与对话不同：对话强调长期用户状态，文档分析强调从大规模外部文本中检索、翻页和整合信息。

![Document QA example](../assets/2023_memgpt-towards-llms-as-operating-systems_arxiv-2310-08560/figures/experiments_figure_docqa_example.png)

图中的 document QA 示例展示了 MemGPT 如何把 Wikipedia 文档库加载到 archival storage 中，再通过函数调用检索相关片段，把分页结果拉入 main context。这对应方法章节中的 external context 和 function chaining：文档库不需要一次性塞进 prompt，而是由 agent 在任务过程中按需查询。

### 3.2.1 Multi-document question-answering

Multi-document QA 实验采用 Liu et al. 的 retriever-reader 文档问答任务。问题来自 NaturalQuestions-Open，retriever 先从 Wikipedia 文档中找出相关文档，reader model 再根据提供的文档回答问题。作者比较固定上下文 baseline 与 MemGPT，并观察随着检索文档数 $K$ 增加，回答准确率如何变化。

在固定上下文 baseline 中，top-$K$ 文档由独立 retriever 取出并直接放入 prompt，模型只能使用当前 prompt 中的文档。如果 gold document 没有被放进 prompt，模型原则上就无法正确回答。MemGPT 的设置不同：完整嵌入文档集被加载进 archival storage，底层用 PostgreSQL + pgvector + HNSW 进行向量检索；MemGPT 可以通过 archival search 多次检索和翻页，因此可访问文档数量不受一次 prompt 容量限制。

![Document QA results](../assets/2023_memgpt-towards-llms-as-operating-systems_arxiv-2310-08560/figures/experiments_figure_docqa_results.png)

结果图表达的趋势是：固定上下文方法可以通过增加 $K$ 暂时提升有效上下文，但随着需要压缩或截断更多文档，性能会下降；MemGPT 的表现对输入文档长度增加更稳定，因为它不是一次性塞入所有候选文档，而是通过检索分页按需获取。作者还指出，这个任务对所有方法都不容易，因为 embedding-based retriever 本身可能把 gold document 排在很后面。MemGPT 理论上可以通过分页继续找，但实际中 agent 往往会在检索完全部数据库之前停止，这构成了一个重要边界：MemGPT 扩展了可访问范围，但仍依赖模型是否愿意、是否能够持续执行足够检索步骤。

### 3.2.2 Nested key-value retrieval (KV)

Nested KV 是作者新提出的合成多跳检索任务，用来更直接地测试 MemGPT 是否能把多个查询串联起来。原始 KV 任务中，每个 key 和 value 都是 UUID，模型给定一个 key，需要返回对应 value。Nested KV 把任务变成多跳：某个 value 可能本身又是另一个 key，因此 agent 必须继续查找，直到找到不再作为 key 出现的最终 value。

![Nested KV example](../assets/2023_memgpt-towards-llms-as-operating-systems_arxiv-2310-08560/figures/experiments_figure_nested_kv_example.png)

这个示例展示了两层嵌套查找：初始 key 指向一个 value，而这个 value 又是下一次查询的 key；MemGPT 需要连续调用查询函数，直到最终 value 的查询只返回一个结果，说明它不再是中间 key。这个任务特别适合检验 function chaining，因为正确解题不是“找到一个相关片段”，而是必须按步骤重复检索、判断和继续。

![Nested KV results](../assets/2023_memgpt-towards-llms-as-operating-systems_arxiv-2310-08560/figures/experiments_figure_nested_kv_results.png)

结果显示，普通 GPT-3.5、GPT-4 和 GPT-4 Turbo 在嵌套层数增加时都会迅速下降。GPT-3.5 在 1 层嵌套就降到 0% accuracy，主要失败模式是直接返回第一跳 value；GPT-4 和 GPT-4 Turbo 更强，但到 3 层左右也失败。MemGPT + GPT-4 则基本不受嵌套层数影响，说明它能通过函数查询反复执行多跳查找。MemGPT + GPT-4 Turbo 和 MemGPT + GPT-3.5 虽然好于对应 baseline，但到 2 层后也开始下降，作者把原因归为没有执行足够多次 lookup。

这一节的实验结论可以概括为：MemGPT 的优势在需要长期记忆、分页检索和多步函数调用的任务中最明显。对话实验说明它能找回长期用户信息，文档 QA 说明它能把大规模文档库放在 prompt 外按需检索，Nested KV 说明 function chaining 能支持明确的多跳查询。不过这些结果也显示 MemGPT 不是万能检索器：性能仍依赖底座模型的函数调用能力、检索排序质量，以及 agent 是否持续执行足够的检索/查询步骤。

### 4 Related Work

相关工作部分把 MemGPT 放在三个研究脉络中：长上下文 LLM、检索增强模型和 LLM agents。作者的写法很简洁，但定位很明确：MemGPT 不是要替代这些方向，而是把它们组合成一种面向长期上下文管理的系统架构。

`Long-context LLMs` 这一类工作试图直接扩大模型可处理的上下文长度。作者提到的路线包括稀疏注意力、低秩近似、神经记忆，以及把模型上下文窗口扩展到超过原始训练长度的方法。MemGPT 与这类工作的关系是互补的：长上下文模型越强，MemGPT 的 `main context` 就越大，相当于操作系统中的物理内存变大；但 MemGPT 的主要贡献不在于扩大这块“物理内存”，而在于增加层级化外部记忆和换入换出机制。因此，长上下文模型可以成为 MemGPT 的底座，但不能取代 MemGPT 的系统层记忆管理。

`Retrieval-Augmented Models` 这一类工作把外部检索结果补充到 LLM 输入中。MemGPT 的 external memory 明显继承了这一脉络：模型可以从外部存储中取回相关信息，再把它放入上下文。作者特别提到 FLARE 这类主动检索方法，以及把 retrieval 和 Chain-of-Thought 交错用于多步问答的方法。MemGPT 与普通 RAG 的区别在于，它不只是生成前检索一次相关文本，而是让 LLM 在运行过程中通过函数调用读写记忆、翻页检索、更新工作上下文，并决定是否继续检索。也就是说，检索在 MemGPT 中被纳入了一个可迭代的控制流。

`LLMs as agents` 这一类工作关注让 LLM 在交互环境中规划、调用工具和执行行动。作者提到的相关例子包括具有记忆和规划能力的生成式代理、WebGPT 的网页搜索与分页、ReAct 中推理与行动交错，以及 AgentBench 对交互式 agent 能力的评测。MemGPT 与这些工作的关系在于，它同样把 LLM 当作能够行动的 agent，但更聚焦于“长期用户输入记忆”这个问题：agent 不只是为了完成一次网页搜索、一次游戏任务或一次工具调用，而是要在多轮、多会话、甚至长期运行过程中持续维护可用记忆。

这一节的核心定位可以概括为：长上下文 LLM 提供更大的 main memory，RAG 提供外部信息访问能力，agent 研究提供函数调用和交互控制框架；MemGPT 的贡献是把这些能力组织成类似 OS 的分层记忆系统，使 LLM 能主动管理自己的上下文资源。这个定位也解释了为什么实验既包括长期对话，也包括文档 QA 和 nested KV：作者要证明 MemGPT 不是单一检索技巧，而是一种通用的记忆管理框架。

### 5 Conclusion

结论部分回到论文的中心命题：LLM 的有限上下文窗口可以被看作一种系统资源限制，而 MemGPT 尝试用操作系统思想来管理这种限制。作者把本文贡献概括为一个受 OS 启发的 LLM 系统：通过类似传统操作系统的分层内存和控制流设计，MemGPT 让固定上下文 LLM 获得“更大上下文资源”的错觉。

结论再次强调两个验证场景。对于 document analysis，MemGPT 能处理超过底座模型上下文窗口的长文本，通过把相关内容在 main context 和 external context 之间换入换出，避免一次性塞入全部文档。对于 conversational agents，MemGPT 支持长期记忆、一致性和随对话演化的状态维护，使 agent 能在扩展对话中保留并更新用户相关信息。

作者认为，MemGPT 的意义不只在于某个具体任务得分，而在于说明 OS 技术中的 hierarchical memory management 和 interrupt/control flow 思想可以迁移到 AI 系统设计中。固定上下文窗口仍然存在，但系统可以通过记忆层级、外部存储、函数调用和事件驱动控制流，把 LLM 的可用工作范围扩展到窗口之外。

结论也提出了未来方向：把 MemGPT 应用于其他具有巨大或无界上下文的任务；接入不同类型的记忆层，例如数据库、缓存或其他存储技术；进一步改进控制流和记忆管理策略。这些方向说明作者把 MemGPT 视为一个开放的系统框架，而不是只服务于本文实验的单一实现。

这一节的作用是把全文收束到系统设计层面的主张：MemGPT 不是试图从模型结构上消灭上下文限制，而是通过 OS-style memory management 最大化固定上下文 LLM 的可用能力。其证据来自前面的长对话和文档分析实验，但作者也承认后续仍有大量策略、存储层和控制流设计可以继续探索。

## 关键公式 / 图表

### 关键图

### 关键表格

## 实验结论

实验总体支持 MemGPT 的核心主张：在需要长期对话记忆、按需检索和多步查询的任务中，系统化的外部记忆管理能显著改善固定上下文 LLM 的表现。DMR 任务中，MemGPT 让 GPT-4/GPT-4 Turbo 的一致性问答准确率从约三成提升到九成以上；conversation opener 任务中，MemGPT 能利用 persona/长期信息生成更贴合用户背景的开场；document QA 中，MemGPT 通过 archival storage 和分页检索降低了一次性上下文塞入的限制；Nested KV 中，MemGPT + GPT-4 能稳定完成多层 key-value 查找，显示 function chaining 对多跳任务有实际作用。

同时，实验也暴露出边界：MemGPT 仍依赖底座模型的函数调用能力、外部检索排序质量，以及 agent 是否能持续执行足够多的检索步骤。GPT-3.5 版本在函数调用和多跳控制上明显较弱；document QA 中，如果检索器把 gold document 排得很靠后，MemGPT 理论上可以继续翻页，但实际 agent 可能提前停止。

## 局限性与可追问点

本文没有系统展开一个独立的 limitations 章节，但从实验和结论可以看出几个边界。

MemGPT 的效果高度依赖底座模型的函数调用和控制能力。Nested KV 中，GPT-3.5 和 GPT-4 Turbo 版本的 MemGPT 仍会因为没有执行足够 lookup 而失败，说明“有外部记忆”和“会正确持续使用外部记忆”是两件事。

外部检索质量仍是瓶颈。Document QA 中，如果 embedding retriever 把 gold document 排在很靠后的位置，MemGPT 理论上可以继续分页查找，但实际 agent 可能提前停止。因此后续需要研究更稳健的检索策略、停止条件和检索失败恢复机制。

记忆写入策略的质量尚未被充分拆解。论文展示了 memory pressure warning、working context 更新和 archival/recall storage，但哪些信息该保存、何时覆盖、如何避免错误记忆或过时记忆污染后续回答，仍值得单独评估。

实验主要验证文档分析和对话代理两个场景，还不能直接说明 MemGPT 在所有长上下文任务上都有效。特别是高风险领域、多用户记忆隔离、隐私删除、长期记忆安全边界等问题，本文没有深入讨论。

可追问的问题包括：MemGPT 的 memory policy 能否自动学习或优化；不同 memory tier 应如何设计索引和压缩策略；函数调用失败时是否需要显式规划器或验证器；长期运行后 working context 与 archival memory 如何去重、纠错和版本化；在真实用户场景中，长期记忆带来的个性化收益如何与隐私和可控性平衡。

## 对我当前研究/项目的启发
