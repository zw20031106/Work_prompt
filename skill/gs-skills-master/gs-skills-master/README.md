# Google Scholar Skills for Claude Code

[English](#english) | [中文](#中文)

| WeChat Official Account (公众号) | WeChat Group (微信群) | Discord |
|:---:|:---:|:---:|
| <img src="qrcode_for_gh_a1c14419b847_258.jpg" width="200"> | <img src="0320.jpg" width="200"> | [Join Discord](https://discord.gg/tGd5vTDASg) |
| 未来论文实验室 | 扫码加入交流群 | English & Chinese |

---

<a id="english"></a>

## English

[Claude Code](https://docs.anthropic.com/en/docs/claude-code) skills that let Claude interact with [Google Scholar](https://scholar.google.com) through Chrome DevTools MCP.

Search papers, track citations, get full-text links, and export to Zotero — all from the Claude Code CLI.

### Prerequisites

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) CLI installed
- Chrome browser with remote debugging enabled
- [Zotero](https://www.zotero.org/) desktop app (optional, for export)
- Python 3 (optional, for Zotero push script)

### Skills

| Skill | Description | Invocation |
|-------|-------------|------------|
| `gs-search` | Keyword search with structured result extraction | `/gs-search deep learning` |
| `gs-advanced-search` | Filtered search: author, journal, date range, exact phrase, title-only | `/gs-advanced-search author:Einstein after:2020 relativity` |
| `gs-cited-by` | Find papers that cite a given paper via data-cid | `/gs-cited-by 0qfs6zbVakoJ` |
| `gs-fulltext` | Get full-text access links: PDF, DOI, Sci-Hub, publisher | `/gs-fulltext 0qfs6zbVakoJ` |
| `gs-navigate-pages` | Pagination for search results | `/gs-navigate-pages next` |
| `gs-export` | Export to Zotero via BibTeX extraction | `/gs-export 0qfs6zbVakoJ` |

### Agent

**`gs-researcher`** — orchestrates all 6 skills. Handles CAPTCHA detection (pauses and asks user to solve manually) and multi-step workflows like "search → track citations → export to Zotero".

### Installation

#### 1. Install Chrome DevTools MCP server

```bash
claude mcp add chrome-devtools -- npx -y chrome-devtools-mcp@latest
```

#### 2. Install Google Scholar skills

```bash
git clone https://github.com/cookjohn/gs-skills.git
cd gs-skills
cp -r skills/ agents/ .claude/
```

Or add to an existing project:

```bash
git clone https://github.com/cookjohn/gs-skills.git /tmp/gs-skills
cp -r /tmp/gs-skills/skills/ your-project/.claude/skills/
cp -r /tmp/gs-skills/agents/ your-project/.claude/agents/
```

#### 3. Start Chrome with remote debugging

```bash
# Windows
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222

# macOS
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222

# Linux
google-chrome --remote-debugging-port=9222
```

#### 4. Launch Claude Code

```bash
claude
```

Skills and agent are picked up automatically. Try `/gs-search deep learning` to verify.

### How It Works

All skills use async `evaluate_script` calls via Chrome DevTools MCP — no screenshot parsing or OCR. Each skill operates in 1-2 tool calls (navigate + evaluate_script), making interactions fast and reliable.

Key design choices:
- **DOM scraping only** — Google Scholar has no public API; all data extraction uses CSS selectors
- **`data-cid` as primary key** — cluster ID used across all skills for citation tracking, export, and cross-referencing
- **Single async script per operation** — replaces multi-step snapshot → click → wait_for patterns
- **BibTeX via navigate_page** — bypasses CORS restrictions on `scholar.googleusercontent.com`
- **CAPTCHA-aware** — detects Google Scholar CAPTCHA and pauses for manual resolution

### Project Structure

```
skills/
├── gs-search/SKILL.md              # Basic keyword search
├── gs-advanced-search/SKILL.md     # Filtered search (author, journal, date, etc.)
├── gs-cited-by/SKILL.md            # Citation tracking via data-cid
├── gs-fulltext/SKILL.md            # Full-text access links (PDF, DOI, Sci-Hub)
├── gs-navigate-pages/SKILL.md      # Result pagination
├── gs-export/                      # BibTeX export & Zotero push
│   ├── SKILL.md
│   └── scripts/
│       └── push_to_zotero.py       # Zotero Connector API client
agents/
└── gs-researcher.md                # Agent: orchestrates all skills
```

---

<a id="中文"></a>

## 中文

| 公众号 | 微信交流群 | Discord |
|:---:|:---:|:---:|
| <img src="qrcode_for_gh_a1c14419b847_258.jpg" width="200"> | <img src="0320.jpg" width="200"> | [加入 Discord](https://discord.gg/tGd5vTDASg) |
| 未来论文实验室 | 扫码加入交流群 | 中英文交流 |

让 [Claude Code](https://docs.anthropic.com/en/docs/claude-code) 通过 Chrome DevTools MCP 操控 [Google Scholar (谷歌学术)](https://scholar.google.com) 的技能集。

支持论文搜索、引用追踪、全文获取、导出到 Zotero 等功能，全部在 Claude Code 命令行中完成。

### 前置要求

- 已安装 [Claude Code](https://docs.anthropic.com/en/docs/claude-code) CLI
- Chrome 浏览器（需开启远程调试）
- [Zotero](https://www.zotero.org/) 桌面版（可选，用于导出）
- Python 3（可选，用于 Zotero 推送脚本）

### 技能列表

| 技能 | 描述 | 调用方式 |
|------|------|----------|
| `gs-search` | 关键词搜索，返回结构化结果 | `/gs-search deep learning` |
| `gs-advanced-search` | 高级搜索：作者、期刊、时间、精确短语、仅标题 | `/gs-advanced-search author:Einstein after:2020 relativity` |
| `gs-cited-by` | 引用追踪：查找引用了某篇论文的所有文献 | `/gs-cited-by 0qfs6zbVakoJ` |
| `gs-fulltext` | 全文获取：PDF、DOI、Sci-Hub、出版商链接 | `/gs-fulltext 0qfs6zbVakoJ` |
| `gs-navigate-pages` | 搜索结果翻页 | `/gs-navigate-pages next` |
| `gs-export` | 通过 BibTeX 导出到 Zotero | `/gs-export 0qfs6zbVakoJ` |

### 智能体

**`gs-researcher`** — 统一调度全部 6 个技能。自动检测验证码（暂停并提示用户手动完成），支持"搜索 → 引用追踪 → 导出到 Zotero"等复合工作流。

### 安装步骤

#### 1. 安装 Chrome DevTools MCP 服务器

```bash
claude mcp add chrome-devtools -- npx -y chrome-devtools-mcp@latest
```

#### 2. 安装 Google Scholar 技能

```bash
git clone https://github.com/cookjohn/gs-skills.git
cd gs-skills
cp -r skills/ agents/ .claude/
```

或添加到已有项目：

```bash
git clone https://github.com/cookjohn/gs-skills.git /tmp/gs-skills
cp -r /tmp/gs-skills/skills/ your-project/.claude/skills/
cp -r /tmp/gs-skills/agents/ your-project/.claude/agents/
```

#### 3. 启动 Chrome 远程调试

```bash
# Windows
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222

# macOS
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222

# Linux
google-chrome --remote-debugging-port=9222
```

#### 4. 启动 Claude Code

```bash
claude
```

技能和智能体会自动加载。输入 `/gs-search deep learning` 验证是否正常工作。

### 工作原理

所有技能通过 Chrome DevTools MCP 的 `evaluate_script` 异步执行 JavaScript，无需截图识别或 OCR。每个技能仅需 1-2 次工具调用（导航 + 执行脚本），快速且稳定。

核心设计：
- **纯 DOM 解析** — Google Scholar 无公开 API，所有数据通过 CSS 选择器提取
- **`data-cid` 作为主键** — 集群 ID 贯穿所有技能，用于引用追踪、导出和交叉引用
- **单次异步脚本** — 取代多步骤 snapshot → click → wait_for 模式
- **navigate_page 获取 BibTeX** — 绕过 `scholar.googleusercontent.com` 的 CORS 限制
- **验证码感知** — 检测到 Google Scholar 验证码时自动暂停，等待用户手动完成

---

## License

MIT
