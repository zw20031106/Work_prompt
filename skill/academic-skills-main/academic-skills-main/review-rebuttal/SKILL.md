---
name: review-rebuttal
description: analyze academic reviews and draft a professional rebuttal when the input includes reviewer comments, a meta-review, paper abstract, or user supplied experiment status and the user needs concern classification, response strategy, risk warnings, or a rebuttal draft without inventing evidence.
---

# Review Rebuttal

用这个 skill 处理投稿后的 reviewer comments、meta-review 和 rebuttal 草稿。重点是拆 concerns、区分补实验与澄清项、组织回复策略，并保持专业克制的语气。

## 工作流

1. 逐个 reviewer 拆分意见，再汇总跨 reviewer 的共性 concern。
2. 参考 `references/review_taxonomy.md` 给 concern 分类。
3. 参考 `references/tone_guidelines.md` 约束语气和风险表达。
4. 参考 `references/rebuttal_template.md` 生成回复框架和草稿。

## 输入处理规则

- 接收 review 全文、meta-review、论文摘要、补充实验现状、作者说明。
- 如果用户只给摘要和 review，不要假装知道论文正文细节。
- 如果用户说“我们还没做这个实验”，在草稿中写成计划或澄清，不要写成已有结果。
- 支持多个 reviewer 合并分析，但要保留 reviewer 之间的差异。

## 输出规则

- 默认输出以下部分：
  - 审稿意见拆分
  - concern 分类
  - 必须补实验的点
  - 更适合澄清的点
  - 回复策略
  - rebuttal 草稿
  - 高风险表述提醒
- 如果 reviewer 之间有冲突，单独指出，不要强行统一。
- 如果 meta-review 明确压住了某些意见，优先围绕 meta-review 组织总体策略。

## 证据与表述约束

- 不得编造实验、额外消融或人工分析结果。
- 不得假装已经补完实验。
- 不得使用对抗性或情绪化表述。
- 不要把 reviewer 的误解简单归咎于 reviewer 能力不足，应改写为“论文表述仍可更清楚地说明……”。

## 何时读引用文件

- 始终读取 `references/rebuttal_template.md`。
- 在 concern 分类时读取 `references/review_taxonomy.md`。
- 在起草回复时读取 `references/tone_guidelines.md`。
