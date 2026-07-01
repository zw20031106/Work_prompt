---
name: paper-deep-note
description: produce a chinese deep reading note for a single academic paper when the input is a pdf, arxiv link, title with abstract, or paper excerpts and the user needs a grounded reading card, contribution summary, reproduction risks, or reading priority judgment.
---

# Paper Deep Note

用这个 skill 处理单篇论文精读。优先输出中文精读卡，强调研究问题、方法、证据、局限和对当前研究的启发。

## 工作流

1. 先判断输入证据级别：全文、局部正文、摘要、仅标题。
2. 明确声明判断边界。
3. 按 `references/note_template.md` 输出结构化精读卡。
4. 在需要判断是否值得继续读时，参考 `references/reading_guidelines.md`。

## 输入处理规则

- 接收 PDF、arXiv 链接、标题加摘要、正文片段或用户自述笔记。
- 如果只有摘要或标题，明确写出“仅基于摘要判断”或“仅基于标题与摘要判断”。
- 如果实验设置、数据集、指标或结果未在输入中明确给出，直接标记为未知，不要补全想象内容。
- 如果用户给出的是局部正文，区分“原文明确给出”和“由局部内容推测”。

## 输出规则

- 默认输出完整精读卡。
- 如果用户只想快速筛论文，保留相同字段，但压缩每项长度。
- 在“优势”“局限”“复现难点”“启发”部分，优先给出和 AI / NLP / LLM / Agent / RAG / Safety 研究直接相关的判断。
- 在“是否值得精读”部分，只使用以下标签之一：
  - `值得精读`
  - `值得速读`
  - `可暂缓`

## 证据与表述约束

- 不要假装读过未提供的全文。
- 不要把论文 claim 直接改写成既定事实。
- 不要编造实验结果、消融结论、数据集细节或开源状态。
- 如果判断主要基于摘要，弱化关于方法细节和实验设计的断言。

## 何时读引用文件

- 始终读取 `references/note_template.md` 以保持输出结构稳定。
- 在判断阅读优先级、复现难点或阅读深度时，读取 `references/reading_guidelines.md`。

## 默认交付

- 默认给出长版中文精读卡。
- 如果信息不足，在卡片顶部先给出“输入覆盖范围说明”。
