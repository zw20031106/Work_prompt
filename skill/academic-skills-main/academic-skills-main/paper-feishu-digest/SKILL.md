---
name: paper-feishu-digest
description: monitor recent arxiv papers and produce a chinese digest when the user needs a filtered paper watchlist, a ranked update for agent or rag related topics, or an optional feishu webhook push from recent cs.ai or cs.cl submissions.
---

# Paper Feishu Digest

用这个 skill 抓取最近时间窗口内的 arXiv 论文，按相关性做保守排序，生成中文速递，并在需要时推送到飞书 webhook。

## 默认场景

- 类别：`cs.AI,cs.CL`
- 时间窗口：`24` 小时
- 关键词：`agent,reasoning,rag,safety review,安全评审`
- 输出数量：`top 10`
- 输出语言：中文

## 工作流

1. 优先调用 `scripts/arxiv_digest.py` 获取最近论文并生成结构化结果。
2. 依据 `references/message_template.md` 组织最终消息格式。
3. 如果需要发飞书，参考 `references/operations.md` 中的操作约束。

## 输入处理规则

- 接收类别、时间窗口、最大抓取数量、关键词、top-k、webhook 等参数。
- 如果用户没有给参数，使用默认场景。
- 如果用户只需要离线摘要，不要主动发 webhook。
- 如果 webhook 缺失或无效，继续输出 Markdown / JSON，不要静默失败。

## 输出规则

- 每篇论文至少输出：
  - 标题
  - 链接
  - 摘要
  - 核心贡献
  - 局限
  - 是否值得读
- “核心贡献”“局限”“是否值得读”只能基于摘要做保守判断。
- 明确标注这是“基于 arXiv 摘要的快速筛选”，不是全文评审。

## 脚本使用

优先使用脚本，而不是手写抓取逻辑。

```powershell
python paper-feishu-digest\scripts\arxiv_digest.py --hours 24 --top-k 10
```

常见参数：

- `--categories`
- `--hours`
- `--max-results`
- `--top-k`
- `--keywords`
- `--webhook`
- `--post`
- `--json-out`
- `--md-out`

## 证据与表述约束

- 不要把摘要判断写成全文结论。
- 不要把“值得读”写成绝对推荐，给出简短理由。
- 如果 API 返回结果不足，明确告诉用户当前窗口内样本有限。

## 何时读引用文件

- 始终读取 `references/message_template.md` 以保持消息结构一致。
- 在执行 webhook 推送或说明运维约束时读取 `references/operations.md`。
