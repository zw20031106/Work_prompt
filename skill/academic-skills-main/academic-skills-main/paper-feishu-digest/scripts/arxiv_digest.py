#!/usr/bin/env python3
"""Fetch recent arXiv papers, rank them conservatively, and format a digest."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Iterable
from urllib import error, parse, request
import xml.etree.ElementTree as ET


ARXIV_API_URL = "https://export.arxiv.org/api/query"
ATOM_NS = {"atom": "http://www.w3.org/2005/Atom"}
DEFAULT_CATEGORIES = "cs.AI,cs.CL"
DEFAULT_KEYWORDS = "agent,reasoning,rag,safety review,安全评审"
USER_AGENT = "academic-skills/1.0 (paper-feishu-digest)"
NETWORK_TIMEOUT_SECONDS = 60


@dataclass
class ArxivPaper:
    title: str
    link: str
    summary: str
    updated: str
    relevance_score: int
    matched_keywords: list[str]
    core_contribution: str
    limitation: str
    worth_reading: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fetch recent arXiv papers and build a Chinese digest."
    )
    parser.add_argument(
        "--categories",
        default=DEFAULT_CATEGORIES,
        help="Comma-separated arXiv categories. Default: cs.AI,cs.CL",
    )
    parser.add_argument(
        "--hours",
        type=int,
        default=24,
        help="Look back this many hours from now. Default: 24",
    )
    parser.add_argument(
        "--max-results",
        type=int,
        default=50,
        help="Maximum number of arXiv entries to fetch. Default: 50",
    )
    parser.add_argument(
        "--top-k",
        type=int,
        default=10,
        help="Number of ranked papers to keep. Default: 10",
    )
    parser.add_argument(
        "--keywords",
        default=DEFAULT_KEYWORDS,
        help="Comma-separated ranking keywords.",
    )
    parser.add_argument(
        "--webhook",
        default="",
        help="Optional Feishu webhook URL.",
    )
    parser.add_argument(
        "--post",
        action="store_true",
        help="Post the generated digest to the Feishu webhook.",
    )
    parser.add_argument(
        "--json-out",
        type=Path,
        default=None,
        help="Optional path to write JSON output.",
    )
    parser.add_argument(
        "--md-out",
        type=Path,
        default=None,
        help="Optional path to write Markdown output.",
    )
    return parser.parse_args()


def parse_csv_arg(raw_value: str) -> list[str]:
    return [item.strip() for item in re.split(r"[,;，；]+", raw_value) if item.strip()]


def build_query_url(categories: list[str], max_results: int) -> str:
    category_terms = [f"cat:{category}" for category in categories]
    search_query = " OR ".join(category_terms)
    params = {
        "search_query": search_query,
        "sortBy": "lastUpdatedDate",
        "sortOrder": "descending",
        "start": "0",
        "max_results": str(max_results),
    }
    return f"{ARXIV_API_URL}?{parse.urlencode(params)}"


def fetch_feed(url: str) -> str:
    req = request.Request(url, headers={"User-Agent": USER_AGENT})
    with request.urlopen(req, timeout=NETWORK_TIMEOUT_SECONDS) as response:
        return response.read().decode("utf-8")


def parse_datetime(raw_value: str) -> datetime:
    return datetime.fromisoformat(raw_value.replace("Z", "+00:00"))


def normalize_text(text: str) -> str:
    return " ".join(text.split())


def extract_entries(feed_text: str) -> list[dict[str, str]]:
    root = ET.fromstring(feed_text)
    entries: list[dict[str, str]] = []

    for entry in root.findall("atom:entry", ATOM_NS):
        title = normalize_text(entry.findtext("atom:title", default="", namespaces=ATOM_NS))
        summary = normalize_text(
            entry.findtext("atom:summary", default="", namespaces=ATOM_NS)
        )
        updated = entry.findtext("atom:updated", default="", namespaces=ATOM_NS)
        paper_id = entry.findtext("atom:id", default="", namespaces=ATOM_NS)

        if not title or not updated or not paper_id:
            continue

        entries.append(
            {
                "title": title,
                "summary": summary,
                "updated": updated,
                "link": paper_id,
            }
        )
    return entries


def filter_recent(entries: Iterable[dict[str, str]], hours: int) -> list[dict[str, str]]:
    cutoff = datetime.now(timezone.utc) - timedelta(hours=hours)
    recent = []
    for entry in entries:
        updated_at = parse_datetime(entry["updated"])
        if updated_at >= cutoff:
            recent.append(entry)
    return recent


def score_entry(title: str, summary: str, keywords: list[str]) -> tuple[int, list[str]]:
    text = f"{title} {summary}".lower()
    matched_keywords = []
    score = 0

    for keyword in keywords:
        keyword_lower = keyword.lower()
        if keyword_lower and keyword_lower in text:
            matched_keywords.append(keyword)
            occurrences = text.count(keyword_lower)
            score += max(1, occurrences) * 3

    if any(token in text for token in ("benchmark", "evaluation", "dataset", "leaderboard")):
        score += 1
    if any(token in text for token in ("agent", "tool", "retrieval", "reasoning", "safety")):
        score += 1

    return score, matched_keywords


def infer_core_contribution(title: str, summary: str) -> str:
    lower_title = title.lower()
    lower_summary = summary.lower()
    if any(
        token in lower_summary
        for token in ("we propose", "we present", "we introduce", "this work proposes")
    ) and any(
        token in lower_summary
        for token in ("framework", "system", "pipeline", "agent", "model", "method")
    ):
        return "基于摘要判断，该工作主要提出一套方法、模型或系统流程。"
    if any(token in lower_title for token in ("benchmark", "bench", "dataset", "leaderboard")):
        return "基于摘要判断，该工作更像是在提出数据集、benchmark 或评测框架。"
    if any(token in lower_summary for token in ("framework", "system", "pipeline", "agent")):
        return "基于摘要判断，该工作主要提出一套系统、框架或 agent 流程。"
    if any(token in lower_summary for token in ("reasoning", "retrieval", "rag", "planning")):
        return "基于摘要判断，该工作主要针对推理、检索增强或规划机制提出方法改进。"
    if any(token in lower_summary for token in ("safety", "alignment", "harm", "risk")):
        return "基于摘要判断，该工作主要关注安全性、对齐或风险评估。"
    return "基于摘要判断，该工作提出了一个针对当前任务设定的方法性改进，但细节仍需阅读全文确认。"


def infer_limitation(summary: str) -> str:
    lower_summary = summary.lower()
    if "code" not in lower_summary and "github" not in lower_summary:
        return "摘要未明确说明代码或实现细节，复现可行性暂无法充分判断。"
    if not any(token in lower_summary for token in ("experiment", "evaluation", "benchmark", "dataset")):
        return "摘要未充分说明实验覆盖范围，方法有效性仍需看全文中的评测细节。"
    if any(token in lower_summary for token in ("case study", "human study")):
        return "摘要显示评测可能包含特定场景分析，泛化性仍需结合全文判断。"
    return "基于摘要只能做有限判断，方法边界、失败案例和评测公平性仍需阅读全文确认。"


def infer_worth_reading(score: int, matched_keywords: list[str]) -> str:
    if score >= 8 and matched_keywords:
        return "值得优先看"
    if score >= 4:
        return "可快速浏览"
    return "可暂缓"


def build_ranked_papers(
    entries: list[dict[str, str]], keywords: list[str], top_k: int
) -> list[ArxivPaper]:
    papers: list[ArxivPaper] = []

    for entry in entries:
        score, matched_keywords = score_entry(entry["title"], entry["summary"], keywords)
        papers.append(
            ArxivPaper(
                title=entry["title"],
                link=entry["link"],
                summary=entry["summary"],
                updated=entry["updated"],
                relevance_score=score,
                matched_keywords=matched_keywords,
                core_contribution=infer_core_contribution(entry["title"], entry["summary"]),
                limitation=infer_limitation(entry["summary"]),
                worth_reading=infer_worth_reading(score, matched_keywords),
            )
        )

    papers.sort(
        key=lambda item: (item.relevance_score, parse_datetime(item.updated)),
        reverse=True,
    )
    return papers[:top_k]


def build_markdown(
    papers: list[ArxivPaper],
    categories: list[str],
    hours: int,
    keywords: list[str],
    fetched_count: int,
) -> str:
    lines = [
        "# 今日论文速递",
        "",
        "## 筛选范围",
        f"- 类别：{', '.join(categories)}",
        f"- 时间窗口：最近 {hours} 小时",
        f"- 关键词：{', '.join(keywords) if keywords else '无'}",
        f"- 当前窗口命中论文数：{fetched_count}",
        f"- 最终保留数：{len(papers)}",
        "",
        "## 总览",
        "- 说明：以下判断仅基于 arXiv 摘要，属于快速筛选，不等于全文评审。",
        "",
    ]

    for index, paper in enumerate(papers, start=1):
        matched = ", ".join(paper.matched_keywords) if paper.matched_keywords else "无直接关键词命中"
        lines.extend(
            [
                f"## {index}. {paper.title}",
                f"- 链接：{paper.link}",
                f"- 更新时间：{paper.updated}",
                f"- 关键词命中：{matched}",
                f"- 摘要：{paper.summary}",
                f"- 核心贡献：{paper.core_contribution}",
                f"- 局限：{paper.limitation}",
                f"- 是否值得读：{paper.worth_reading}",
                "",
            ]
        )

    if not papers:
        lines.extend(
            [
                "## 结果说明",
                "- 当前时间窗口内没有筛到满足条件的论文，或 arXiv 返回结果不足。",
                "",
            ]
        )

    return "\n".join(lines).strip() + "\n"


def build_json_payload(
    papers: list[ArxivPaper], categories: list[str], hours: int, keywords: list[str]
) -> dict:
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "categories": categories,
        "hours": hours,
        "keywords": keywords,
        "paper_count": len(papers),
        "papers": [asdict(paper) for paper in papers],
    }


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def post_to_feishu(webhook: str, markdown_text: str) -> None:
    payload = {
        "msg_type": "text",
        "content": {
            "text": markdown_text,
        },
    }
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    req = request.Request(
        webhook,
        data=data,
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "User-Agent": USER_AGENT,
        },
        method="POST",
    )
    with request.urlopen(req, timeout=NETWORK_TIMEOUT_SECONDS) as response:
        response.read()


def main() -> int:
    args = parse_args()
    categories = parse_csv_arg(args.categories)
    keywords = parse_csv_arg(args.keywords)

    if not categories:
        print("ERROR: at least one category is required.", file=sys.stderr)
        return 1
    if args.hours <= 0 or args.max_results <= 0 or args.top_k <= 0:
        print("ERROR: hours, max-results, and top-k must be positive integers.", file=sys.stderr)
        return 1
    if args.post and not args.webhook:
        print("ERROR: --post requires --webhook.", file=sys.stderr)
        return 1

    query_url = build_query_url(categories, args.max_results)

    try:
        feed_text = fetch_feed(query_url)
        entries = extract_entries(feed_text)
        recent_entries = filter_recent(entries, args.hours)
        papers = build_ranked_papers(recent_entries, keywords, args.top_k)
        markdown_text = build_markdown(
            papers,
            categories=categories,
            hours=args.hours,
            keywords=keywords,
            fetched_count=len(recent_entries),
        )
        json_payload = build_json_payload(papers, categories, args.hours, keywords)

        if args.md_out:
            write_text(args.md_out, markdown_text)
        if args.json_out:
            write_json(args.json_out, json_payload)
        if args.post:
            post_to_feishu(args.webhook, markdown_text)

        print(markdown_text)
        return 0
    except ET.ParseError as exc:
        print(f"ERROR: failed to parse arXiv Atom feed: {exc}", file=sys.stderr)
        return 1
    except error.HTTPError as exc:
        print(f"ERROR: HTTP error while accessing remote service: {exc.code}", file=sys.stderr)
        return 1
    except error.URLError as exc:
        print(f"ERROR: network error while accessing remote service: {exc.reason}", file=sys.stderr)
        return 1
    except OSError as exc:
        print(f"ERROR: local I/O failure: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
