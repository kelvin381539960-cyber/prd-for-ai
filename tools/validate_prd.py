#!/usr/bin/env python3
"""
Validate PRD files under requirements/.

Default mode is intentionally lightweight:
- validate formal PRD files already written to Git;
- do not validate Canvas drafts;
- do not require brief / research / review files to exist;
- validate paths, front matter basics, repository source paths, local image links,
  and ALL-GAP references when present.

Use --strict for stronger checks in release/review contexts.

Usage:
  python3 tools/validate_prd.py
  python3 tools/validate_prd.py requirements/2026-05/account/change-email.md
  python3 tools/validate_prd.py --strict requirements/2026-05/account/change-email.md
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
REQUIREMENTS_DIR = ROOT / "requirements"
KNOWLEDGE_GAPS = ROOT / "knowledge-base" / "changelog" / "knowledge-gaps.md"

ALLOWED_PRD_STATUS = {"draft", "review", "approved", "deprecated"}
ALLOWED_BRIEF_STATUS = {"confirmed", "skipped_questions_confirmed"}
ALLOWED_REVIEW_CONCLUSIONS = {"pass", "needs_revision", "blocked_by_confirmation"}
HELPER_PREFIXES = ("_brief-", "_review-", "_research-")
REQ_PATH_RE = re.compile(r"^requirements/\d{4}-\d{2}/[^/]+/[^/]+\.md$")
FM_BOUNDARY = re.compile(r"^---\s*$", re.MULTILINE)
LOCAL_IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")


@dataclass
class ValidationResult:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)

    def extend(self, other: "ValidationResult") -> None:
        self.errors.extend(other.errors)
        self.warnings.extend(other.warnings)


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


def strip_quotes(value: str) -> str:
    value = value.strip()
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        return value[1:-1]
    return value


def fm_scalar(fm: str, key: str) -> str | None:
    pattern = re.compile(rf"^{re.escape(key)}:\s*(.*?)\s*$", re.MULTILINE)
    match = pattern.search(fm)
    if not match:
        return None
    value = strip_quotes(match.group(1).strip())
    return value or None


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
        return [scalar]

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
        if not stripped:
            continue
        if indent <= base_indent and not stripped.startswith("- "):
            break
        if stripped.startswith("- "):
            item = strip_quotes(stripped[2:].strip())
            if item:
                values.append(item)

    return values


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


def require_existing_repo_path(result: ValidationResult, owner: Path, value: str, field_name: str) -> None:
    if not value:
        result.error(f"{rel(owner)}: {field_name} is empty")
        return
    if "://" in value:
        result.error(f"{rel(owner)}: {field_name} must be a repository path, got URL: {value}")
        return
    target = ROOT / value
    if not target.exists():
        result.error(f"{rel(owner)}: {field_name} points to missing file: {value}")


def validate_brief(result: ValidationResult, prd_path: Path, brief_path_raw: str) -> None:
    brief_path = ROOT / brief_path_raw
    if not brief_path.is_file():
        result.error(f"{rel(prd_path)}: brief path points to missing file: {brief_path_raw}")
        return

    fm, _body = extract_front_matter(read_text(brief_path))
    if fm is None:
        result.error(f"{brief_path_raw}: missing front matter")
        return

    brief_type = fm_scalar(fm, "type")
    if brief_type != "prd-brief":
        result.error(f"{brief_path_raw}: type must be prd-brief, got {brief_type!r}")

    brief_status = fm_scalar(fm, "brief_status") or fm_scalar(fm, "status")
    if brief_status and brief_status not in ALLOWED_BRIEF_STATUS:
        result.error(
            f"{brief_path_raw}: brief_status/status must be one of {sorted(ALLOWED_BRIEF_STATUS)}, "
            f"got {brief_status!r}"
        )

    target_prd = fm_scalar(fm, "target_prd")
    if target_prd and target_prd != rel(prd_path):
        result.error(
            f"{brief_path_raw}: target_prd should point to {rel(prd_path)}, got {target_prd!r}"
        )


def validate_review_if_present(result: ValidationResult, prd_path: Path) -> None:
    review_path = prd_path.with_name(f"_review-{prd_path.stem}.md")
    if not review_path.is_file():
        return

    fm, body = extract_front_matter(read_text(review_path))
    if fm is None:
        result.warn(f"{rel(review_path)}: review file exists but has no front matter")
        text_for_conclusion = body
    else:
        review_type = fm_scalar(fm, "type")
        if review_type and review_type != "prd-review":
            result.error(f"{rel(review_path)}: type must be prd-review when set, got {review_type!r}")
        conclusion = fm_scalar(fm, "review_conclusion") or fm_scalar(fm, "conclusion")
        if conclusion and conclusion not in ALLOWED_REVIEW_CONCLUSIONS:
            result.error(
                f"{rel(review_path)}: review_conclusion/conclusion must be one of "
                f"{sorted(ALLOWED_REVIEW_CONCLUSIONS)}, got {conclusion!r}"
            )
            return
        if conclusion:
            return
        text_for_conclusion = body

    found = any(token in text_for_conclusion for token in ALLOWED_REVIEW_CONCLUSIONS)
    if not found:
        result.warn(
            f"{rel(review_path)}: review file exists but no review conclusion found "
            f"({', '.join(sorted(ALLOWED_REVIEW_CONCLUSIONS))})"
        )


def validate_gap_refs(
    result: ValidationResult,
    prd_path: Path,
    source_files: list[str],
    source_doc: str | None,
    open_gap_refs: list[str],
) -> None:
    if not open_gap_refs:
        return

    gap_path = "knowledge-base/changelog/knowledge-gaps.md"
    source_doc_mentions_gap = bool(source_doc and gap_path in source_doc)
    if gap_path not in source_files and not source_doc_mentions_gap:
        result.error(
            f"{rel(prd_path)}: open_gap_refs is set but sources do not include {gap_path}"
        )

    if not KNOWLEDGE_GAPS.is_file():
        result.error(f"{rel(prd_path)}: knowledge-gaps file is missing")
        return

    gap_text = read_text(KNOWLEDGE_GAPS)
    for gap_ref in open_gap_refs:
        if gap_ref not in gap_text:
            result.error(f"{rel(prd_path)}: open_gap_ref not found in knowledge-gaps: {gap_ref}")


def validate_local_images(result: ValidationResult, prd_path: Path, body: str) -> None:
    for match in LOCAL_IMAGE_RE.finditer(body):
        raw = match.group(1).strip()
        if not raw or raw.startswith("http://") or raw.startswith("https://") or raw.startswith("#"):
            continue
        image_path = raw.split("#", 1)[0].split("?", 1)[0]
        target = (prd_path.parent / image_path).resolve()
        if not target.exists():
            result.error(f"{rel(prd_path)}: local image/prototype path is missing: {raw}")


def has_heading(body: str, number: str) -> bool:
    return bool(re.search(rf"^##\s+{re.escape(number)}[\.．、\s]", body, re.MULTILINE))


def validate_sections(result: ValidationResult, prd_path: Path, body: str, strict: bool) -> None:
    for number, label in (("0", "文档信息"), ("1", "功能结论")):
        if not has_heading(body, number):
            result.error(f"{rel(prd_path)}: missing required section {number} ({label})")

    if "来源引用" not in body:
        result.error(f"{rel(prd_path)}: missing 来源引用 section")

    if strict:
        for number in ("2", "3"):
            if not has_heading(body, number):
                result.error(f"{rel(prd_path)}: strict mode requires section {number}")

    if has_heading(body, "2") and "sequenceDiagram" not in body:
        result.warn(f"{rel(prd_path)}: section 2 exists but no Mermaid sequenceDiagram found")

    if has_heading(body, "3") and "flowchart" not in body:
        result.warn(f"{rel(prd_path)}: section 3 exists but no Mermaid flowchart found")


def validate_prd(path: Path, strict: bool) -> ValidationResult:
    result = ValidationResult()
    rel_path = rel(path)

    if not REQ_PATH_RE.match(rel_path):
        result.error(
            f"{rel_path}: PRD path should match requirements/YYYY-MM/<module>/<feature>.md"
        )

    text = read_text(path)
    fm, body = extract_front_matter(text)
    if fm is None:
        result.error(f"{rel_path}: missing front matter")
        return result

    doc_type = fm_scalar(fm, "type")
    if doc_type != "prd":
        result.error(f"{rel_path}: type must be prd, got {doc_type!r}")

    status = fm_scalar(fm, "status")
    if status not in ALLOWED_PRD_STATUS:
        result.error(
            f"{rel_path}: status must be one of {sorted(ALLOWED_PRD_STATUS)}, got {status!r}"
        )

    brief_path = fm_scalar(fm, "brief_path") or fm_scalar(fm, "brief")
    if brief_path:
        validate_brief(result, path, brief_path)
    elif strict:
        result.error(f"{rel_path}: strict mode requires brief_path or brief")

    brief_status = fm_scalar(fm, "brief_status")
    if brief_status and brief_status not in ALLOWED_BRIEF_STATUS:
        result.error(
            f"{rel_path}: brief_status must be one of {sorted(ALLOWED_BRIEF_STATUS)}, got {brief_status!r}"
        )

    source_files = fm_list(fm, "source_files")
    source_doc = fm_scalar(fm, "source_doc")
    if source_files:
        for source in source_files:
            require_existing_repo_path(result, path, source, "source_files")
    elif strict:
        result.error(f"{rel_path}: strict mode requires source_files")
    elif not source_doc:
        result.error(f"{rel_path}: missing source_files or legacy source_doc")
    else:
        result.warn(f"{rel_path}: uses legacy source_doc; prefer structured source_files")

    open_gap_refs = fm_list(fm, "open_gap_refs")
    validate_gap_refs(result, path, source_files, source_doc, open_gap_refs)
    validate_sections(result, path, body, strict)
    validate_local_images(result, path, body)
    validate_review_if_present(result, path)

    return result


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate PRD workflow files.")
    parser.add_argument(
        "paths",
        nargs="*",
        help="Optional files or directories to validate. Defaults to requirements/**/*.md.",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Enable stricter checks for release/review contexts.",
    )
    args = parser.parse_args()

    prd_files = discover_prd_files(args.paths)
    result = ValidationResult()

    for path in prd_files:
        result.extend(validate_prd(path, strict=args.strict))

    for warning in result.warnings:
        print(f"validate_prd: warning: {warning}", file=sys.stderr)

    if result.errors:
        print("validate_prd: FAILED", file=sys.stderr)
        for error in result.errors:
            print(f"  - {error}", file=sys.stderr)
        return 1

    mode = "strict" if args.strict else "default"
    print(f"validate_prd: ok ({len(prd_files)} PRD file(s), mode={mode})", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
