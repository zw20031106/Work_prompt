# 操作说明

## arXiv 抓取

- 使用 arXiv Atom API。
- 时间过滤基于论文更新时间。
- 结果排序应先按关键词相关性，再按更新时间做辅助排序。

## 飞书推送

- 仅在显式提供 `--webhook` 且同时指定 `--post` 时发送请求。
- webhook 推送失败时，不要丢失本地输出。
- 默认发送简单文本消息，不依赖额外认证流程。

## 安全与稳定性

- 不要在日志中打印完整 webhook。
- 网络错误、XML 解析错误、超时都应给出明确报错。
- 当关键词为空时，允许退化为按时间窗口列出最新论文。

## 推荐操作流程

1. 先执行本地输出：
   `python paper-feishu-digest\scripts\arxiv_digest.py --md-out digest.md --json-out digest.json`
2. 检查内容是否合理。
3. 需要共享时，再追加 `--webhook` 与 `--post`。
