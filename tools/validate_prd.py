#!/usr/bin/env python3
"""
Validate PRD workflow files under requirements/.

This tool is intentionally static and conservative:
- it checks repository paths, front matter, source links, brief links, and section skeletons;
- it does not rewrite files;
- it only requires review notes after a PRD reaches review / approved status.

Usage:
  python3 tools/validate_prd.py
  python3 tools/validate_prd.py requirements/2026-05/card/card-transaction-detail.md
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
REQUIREMENTS_DIR = ROOT / "requirements"
KNOWLEDGE_GAPS = ROOT / "knowledge-base" / "changelog" / "knowledge-gaps.md"

ALLOWED_PRD_STATUS = {"draft", "review", "approved", "deprecated"}
ALLOWED_BRIEF_STATUS = {"confirmed", "skipped_questions_confirmed"}
HELPER_PREFIXES = ("_brief-", "_review-")
SECTION_NUMBERS = tuple(str(i) for i in range(0, 11))

FM_BOUNDARY = re.compile(r"^---\s*$", re.MULTILINE)
REQ_PATH_RE = re.compile(r"^requirements/\d{4}-\d{2}/[^/]+/[^/]+\.md$")


def rel(path: Path) -> str:
    return path.resolve().relative_to(ROOT).as_posix()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def extract_front_matter(text: str) -> tuple[str | None, str]:
    if not text.startswith("---"):
        return None, text
    bounds = list(FM_BOUNDARY.finditer(text))
    if len(bounds) < 2:
        return None, text
    fm = text[bounds[0].end() : bounds[1].start()]
    body = text[bounds[1].end() :].lstrip("\n")
    return fm, body


def fm_scalar(fm: str, key: str) -> str | None:
    pattern = re.compile(rf"^{re.escape(key)}:\s*(.*?)\s*$", re.MULTILINE)
    match = pattern.search(fm)
    if not match:
        return None
    value = match.group(1).strip()
    if value == "":
        return None
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        return value[1:-1]
    return value


def fm_list(fm: str, key: str) -> list[str]:
    scalar = fm_scalar(fm, key)
    if scalar is None:
        if not re.search(rf"^{re.escape(key)}:\s*$", fm, re.MULTILINE):
            return []
    elif scalar == "[]":
        return []
    elif scalar.startswith("[") and scalar.endswith("]"):
        inner = scalar[1:-1].strip()
        if not inner:
            return []
        return [strip_quotes(item.strip()) for item in inner.split(",") if item.strip()]
    else:
        return [strip_quotes(scalar)]

    lines = fm.splitlines()
    values: list[str] = []
    in_key = False
    base_indent = 0

    for line in lines:
        if re.match(rf"^{re.escape(key)}:\s*$", line):
            in_key = True
            base_indent = len(line) - len(line.lstrip(" "))
            continue

        if not in_key:
            continue

        stripped = line.strip()
        indent = len(line) - len(line.lstrip(" "))

        if stripped == "":
            continue

        if indent <= base_indent and not stripped.startswith("- "):
            break

        if stripped.startswith("- "):
            item = stripped[2:].strip()
            if item:
                values.append(strip_quotes(item))

    return values


def strip_quotes(value: str) -> str:
    value = value.strip()
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        return value[1:-1]
    return value


def is_candidate_prd(path: Path) -> bool:
    name = path.name
    if name == "_index.md" or name.startswith(HELPER_PREFIXES):
        return False
    return path.suffix == ".md" and REQUIREMENTS_DIR in path.resolve().parents


def discover_prd_files(paths: Iterable[str]) -> list[Path]:
    if paths:
        files: list[Path] = []
        for raw in paths:
            path = (ROOT / raw).resolve() if not Path(raw).is_absolute() else Path(raw)
            if path.is_dir():
                files.extend(p for p in path.rglob("*.md") if is_candidate_prd(p))
            elif path.is_file():
                files.append(path)
            else:
                print(f"validate_prd: path not found: {raw}", file=sys.stderr)
                return []
        return sorted(set(files))

    if not REQUIREMENTS_DIR.is_dir():
        return []

    return sorted(p for p in REQUIREMENTS_DIR.rglob("*.md") if is_candidate_prd(p))


def require_existing_repo_path(
    errors: list[str], owner: Path, value: str, field_name: str
) -> None:
    if not value:
        errors.append(f"{rel(owner)}: {field_name} is empty")
        return

    if "://" in value:
        errors.append(f"{rel(owner)}: {field_name} must be a repository path, got URL: {value}")
        return

    target = ROOT / value
    if not target.exists():
        errors.append(f"{rel(owner)}: {field_name} points to missing file: {value}")


def validate_brief(errors: list[str], prd_path: Path, brief_path_raw: str) -> None:
    brief_path = ROOT / brief_path_raw
    if not brief_path.is_file():
        errors.append(f"{rel(prd_path)}: brief_path points to missing file: {brief_path_raw}")
        return

    fm, _body = extract_front_matter(read_text(brief_path))
    if fm is None:
        errors.append(f"{brief_path_raw}: missing front matter")
        return

    brief_type = fm_scalar(fm, "type")
    if brief_type != "prd-brief":
        errors.append(f"{brief_path_raw}: type must be prd-brief, got {brief_type!r}")

    brief_status = fm_scalar(fm, "brief_status")
    if brief_status not in ALLOWED_BRIEF_STATUS:
        errors.append(
            f"{brief_path_raw}: brief_status must be one of {sorted(ALLOWED_BRIEF_STATUS)}, "
            f"got {brief_status!r}"
        )

    target_prd = fm_scalar(fm, "target_prd")
    if target_prd and target_prd != rel(prd_path):
        errors.append(
            f"{brief_path_raw}: target_prd should point to {rel(prd_path)}, got {target_prd!r}"
        )


def validate_sections(errors: list[str], prd_path: Path, body: str) -> None:
    found: set[str] = set()
    for match in re.finditer(r"^##\s+(\d+)[\.．、\s]", body, re.MULTILINE):
        found.add(match.group(1))

    missing = [num for num in SECTION_NUMBERS if num not in found]
    if missing:
        errors.append(
            f"{rel(prd_path)}: missing standard section headings for section(s): "
            + ", ".join(missing)
        )


def validate_review_note(errors: list[str], prd_path: Path, status: str) -> None:
    if status not in {"review", "approved"}:
        return

    review_path = prd_path.with_name(f"_review-{prd_path.stem}.md")
    if not review_path.is_file():
        errors.append(
            f"{rel(prd_path)}: status={status} requires review note {rel(review_path)}"
        )


def validate_gap_refs(
    errors: list[str], prd_path: Path, source_files: list[str], open_gap_refs: list[str]
) -> None:
    if not open_gap_refs:
        return

    if "knowledge-base/changelog/knowledge-gaps.md" not in source_files:
        errors.append(
            f"{rel(prd_path)}: open_gap_refs is set but source_files does not include "
            "knowledge-base/changelog/knowledge-gaps.md"
        )

    if not KNOWLEDGE_GAPS.is_file():
        errors.append(f"{rel(prd_path)}: knowledge-gaps file is missing")
        return

    gap_text = read_text(KNOWLEDGE_GAPS)
    for gap_ref in open_gap_refs:
        if gap_ref not in gap_text:
            errors.append(f"{rel(prd_path)}: open_gap_ref not found in knowledge-gaps: {gap_ref}")


def validate_prd(path: Path) -> list[str]:
    errors: list[str] = []
    rel_path = rel(path)

    if not REQ_PATH_RE.match(rel_path):
        errors.append(
            f"{rel_path}: PRD path should match requirements/YYYY-MM/<module>/<feature>.md"
        )

    text = read_text(path)
    fm, body = extract_front_matter(text)
    if fm is None:
        return [f"{rel_path}: missing front matter"]

    doc_type = fm_scalar(fm, "type")
    if doc_type != "prd":
        errors.append(f"{rel_path}: type must be prd, got {doc_type!r}")

    status = fm_scalar(fm, "status")
    if status not in ALLOWED_PRD_STATUS:
        errors.append(
            f"{rel_path}: status must be one of {sorted(ALLOWED_PRD_STATUS)}, got {status!r}"
        )
        status = ""

    brief_path = fm_scalar(fm, "brief_path")
    if not brief_path:
        errors.append(f"{rel_path}: missing brief_path")
    else:
        validate_brief(errors, path, brief_path)

    brief_status = fm_scalar(fm, "brief_status")
    if brief_status not in ALLOWED_BRIEF_STATUS:
        errors.append(
            f"{rel_path}: brief_status must be one of {sorted(ALLOWED_BRIEF_STATUS)}, "
            f"got {brief_status!r}"
        )

    source_files = fm_list(fm, "source_files")
    if not source_files:
        errors.append(f"{rel_path}: source_files must contain at least one source file")
    else:
        for source in source_files:
            require_existing_repo_path(errors, path, source, "source_files")

    open_gap_refs = fm_list(fm, "open_gap_refs")
    validate_gap_refs(errors, path, source_files, open_gap_refs)

    validate_sections(errors, path, body)
    validate_review_note(errors, path, status)

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate PRD workflow files.")
    parser.add_argument(
        "paths",
        nargs="*",
        help="Optional files or directories to validate. Defaults to requirements/**/*.md.",
    )
    args = parser.parse_args()

    prd_files = discover_prd_files(args.paths)
    errors: list[str] = []

    for path in prd_files:
        errors.extend(validate_prd(path))

    if errors:
        print("validate_prd: FAILED", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        return 1

    print(f"validate_prd: ok ({len(prd_files)} PRD file(s))", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
