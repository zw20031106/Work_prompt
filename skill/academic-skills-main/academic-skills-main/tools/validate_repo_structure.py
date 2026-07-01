#!/usr/bin/env python3
"""Validate repository structure for the academic-skills project."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT_REQUIRED = [
    "README.md",
    "LICENSE",
    ".gitignore",
    "skills-overview.md",
    "tools/package_all_skills.py",
    "tools/validate_repo_structure.py",
]

SKILL_LAYOUT = {
    "paper-deep-note": [
        "SKILL.md",
        "agents/openai.yaml",
        "references/note_template.md",
        "references/reading_guidelines.md",
    ],
    "survey-writer": [
        "SKILL.md",
        "agents/openai.yaml",
        "references/survey_template.md",
        "references/comparison_dimensions.md",
        "references/related_work_patterns.md",
    ],
    "paper-feishu-digest": [
        "SKILL.md",
        "agents/openai.yaml",
        "scripts/arxiv_digest.py",
        "references/message_template.md",
        "references/operations.md",
    ],
    "review-rebuttal": [
        "SKILL.md",
        "agents/openai.yaml",
        "references/rebuttal_template.md",
        "references/review_taxonomy.md",
        "references/tone_guidelines.md",
    ],
    "experiment-log-summarizer": [
        "SKILL.md",
        "agents/openai.yaml",
        "references/experiment_template.md",
        "references/error_analysis_template.md",
    ],
    "benchmark-extractor": [
        "SKILL.md",
        "agents/openai.yaml",
        "references/extraction_schema.md",
        "references/comparison_table_template.md",
    ],
    "research-gap-finder": [
        "SKILL.md",
        "agents/openai.yaml",
        "references/gap_analysis_template.md",
        "references/problem_framing_template.md",
    ],
    "weekly-lab-update": [
        "SKILL.md",
        "agents/openai.yaml",
        "references/weekly_report_template.md",
        "references/meeting_outline_template.md",
        "references/english_brief_template.md",
    ],
}


def check_paths(base_dir: Path, relative_paths: list[str]) -> list[str]:
    missing = []
    for relative_path in relative_paths:
        if not (base_dir / relative_path).exists():
            missing.append(relative_path)
    return missing


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    errors: list[str] = []

    for relative_path in ROOT_REQUIRED:
        if not (repo_root / relative_path).exists():
            errors.append(f"missing root path: {relative_path}")

    for skill_name, required_paths in SKILL_LAYOUT.items():
        skill_dir = repo_root / skill_name
        if not skill_dir.is_dir():
            errors.append(f"missing skill directory: {skill_name}")
            continue
        for relative_path in check_paths(skill_dir, required_paths):
            errors.append(f"{skill_name}: missing {relative_path}")

    if errors:
        print("Repository validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Repository validation passed.")
    print(f"Checked {len(ROOT_REQUIRED)} root paths.")
    print(f"Checked {len(SKILL_LAYOUT)} skill directories.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
