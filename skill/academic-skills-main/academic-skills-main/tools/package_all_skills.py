#!/usr/bin/env python3
"""Package all skills in the repository into zip archives."""

from __future__ import annotations

import argparse
import sys
import zipfile
from pathlib import Path


SKILL_NAMES = [
    "paper-deep-note",
    "survey-writer",
    "paper-feishu-digest",
    "review-rebuttal",
    "experiment-log-summarizer",
    "benchmark-extractor",
    "research-gap-finder",
    "weekly-lab-update",
]

REQUIRED_SKILL_FILES = [
    "SKILL.md",
    "agents/openai.yaml",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Package all academic skills into zip archives."
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Repository root. Defaults to the parent of tools/.",
    )
    parser.add_argument(
        "--dist",
        type=Path,
        default=None,
        help="Output directory for zip packages. Defaults to <repo-root>/dist.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show planned package actions without writing zip files.",
    )
    return parser.parse_args()


def verify_skill_dir(skill_dir: Path) -> list[str]:
    missing = []
    for relative_path in REQUIRED_SKILL_FILES:
        if not (skill_dir / relative_path).is_file():
            missing.append(relative_path)
    return missing


def iter_skill_files(skill_dir: Path):
    for path in sorted(skill_dir.rglob("*")):
        if path.is_file():
            yield path


def package_skill(skill_dir: Path, dist_dir: Path, dry_run: bool) -> Path:
    archive_path = dist_dir / f"{skill_dir.name}.zip"
    if dry_run:
        return archive_path

    dist_dir.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(archive_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for file_path in iter_skill_files(skill_dir):
            archive_name = file_path.relative_to(skill_dir.parent)
            archive.write(file_path, archive_name)
    return archive_path


def main() -> int:
    args = parse_args()
    repo_root = args.repo_root.resolve()
    dist_dir = (args.dist or repo_root / "dist").resolve()

    errors: list[str] = []
    packaged: list[Path] = []

    for skill_name in SKILL_NAMES:
        skill_dir = repo_root / skill_name
        if not skill_dir.is_dir():
            errors.append(f"missing skill directory: {skill_dir}")
            continue

        missing = verify_skill_dir(skill_dir)
        if missing:
            joined = ", ".join(missing)
            errors.append(f"{skill_name}: missing required files: {joined}")
            continue

        archive_path = package_skill(skill_dir, dist_dir, args.dry_run)
        packaged.append(archive_path)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    action = "would package" if args.dry_run else "packaged"
    for archive_path in packaged:
        print(f"{action}: {archive_path}")
    print(f"total skills: {len(packaged)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
