#!/usr/bin/env python3
"""
visual_structure_extract.py

Mature-library wrapper for image / visual structure extraction.

This tool does NOT implement OCR or layout recognition from scratch. It wraps
battle-tested engines when available and standardizes their outputs into
reviewable files before anyone writes PRD content.

Supported modes:
- general: OCR text blocks + optional layout regions.
- ui: OCR text blocks + coarse UI/text region review artifacts.
- flowchart: OCR text blocks + optional OpenCV candidate connector extraction.

Primary engines:
- PaddleOCR: OCR text boxes for Chinese + English.
- PP-Structure: optional layout / table / region extraction.
- LayoutParser: optional layout model wrapper when installed/configured.
- OpenCV: optional candidate connector detection for flowcharts only.

Important:
- This tool is an evidence extraction helper, not a source of truth.
- Outputs marked needs_review=true must be checked against the original image.
- It never writes PRD content directly.

Examples:
    python3 tools/visual_structure_extract.py \
      knowledge-base/kyc/_assets/account-opening/image4.jpeg \
      --mode flowchart \
      --out tmp/visual-image4 \
      --ocr paddle \
      --structure ppstructure \
      --opencv-connectors

    python3 tools/visual_structure_extract.py page.png --mode ui --out tmp/ui-page --ocr paddle

Dependencies are listed in tools/requirements-visual.txt.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import shutil
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple


BBox = Tuple[int, int, int, int]  # x, y, w, h
Point = Tuple[int, int]


@dataclass
class TextBlock:
    id: str
    text: str
    bbox: List[List[int]]
    confidence: float
    engine: str
    needs_review: bool
    notes: str = ""


@dataclass
class Region:
    id: str
    type: str
    bbox: List[List[int]]
    confidence: float
    engine: str
    needs_review: bool
    text: str = ""
    notes: str = ""


@dataclass
class ConnectorCandidate:
    id: str
    x1: int
    y1: int
    x2: int
    y2: int
    confidence: float
    needs_review: bool
    notes: str = "candidate connector; arrow direction and branch label require manual review"


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def polygon_to_bbox(poly: Sequence[Sequence[float]]) -> BBox:
    xs = [int(round(p[0])) for p in poly]
    ys = [int(round(p[1])) for p in poly]
    x1, y1 = min(xs), min(ys)
    x2, y2 = max(xs), max(ys)
    return x1, y1, max(1, x2 - x1), max(1, y2 - y1)


def bbox_to_poly(x: int, y: int, w: int, h: int) -> List[List[int]]:
    return [[x, y], [x + w, y], [x + w, y + h], [x, y + h]]


def normalize_text(value: Any) -> str:
    if value is None:
        return ""
    text = str(value).replace("\r", "\n")
    parts = [" ".join(line.split()) for line in text.split("\n")]
    return " / ".join([p for p in parts if p])


def write_json(path: Path, rows: Iterable[Any]) -> None:
    with path.open("w", encoding="utf-8") as f:
        json.dump([asdict(row) for row in rows], f, ensure_ascii=False, indent=2)


def write_csv(path: Path, rows: Sequence[Any]) -> None:
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    fields = list(asdict(rows[0]).keys())
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            data = asdict(row)
            for key, value in list(data.items()):
                if isinstance(value, (list, dict)):
                    data[key] = json.dumps(value, ensure_ascii=False)
            writer.writerow(data)


def run_paddle_ocr(image_path: Path, lang: str, use_angle_cls: bool) -> List[TextBlock]:
    try:
        from paddleocr import PaddleOCR  # type: ignore
    except Exception as exc:
        raise SystemExit(
            "PaddleOCR is not installed. Install visual dependencies first:\n"
            "  pip install -r tools/requirements-visual.txt\n"
            f"Import error: {exc}"
        )

    ocr = PaddleOCR(use_angle_cls=use_angle_cls, lang=lang, show_log=False)
    raw = ocr.ocr(str(image_path), cls=use_angle_cls)
    blocks: List[TextBlock] = []

    # PaddleOCR output is commonly: [ [ [box], (text, score) ], ... ] or nested per page.
    rows: List[Any] = []
    if raw and isinstance(raw, list):
        if len(raw) == 1 and isinstance(raw[0], list):
            rows = raw[0]
        else:
            rows = raw

    for idx, item in enumerate(rows, start=1):
        try:
            box = item[0]
            text = normalize_text(item[1][0])
            score = float(item[1][1])
        except Exception:
            continue
        blocks.append(
            TextBlock(
                id=f"T{idx:03d}",
                text=text,
                bbox=[[int(round(p[0])), int(round(p[1]))] for p in box],
                confidence=round(score, 4),
                engine="paddleocr",
                needs_review=score < 0.85 or not text,
            )
        )
    return blocks


def run_ppstructure(image_path: Path, lang: str) -> List[Region]:
    try:
        from paddleocr import PPStructure  # type: ignore
    except Exception as exc:
        raise SystemExit(
            "PP-Structure is not available. Install PaddleOCR visual dependencies first:\n"
            "  pip install -r tools/requirements-visual.txt\n"
            f"Import error: {exc}"
        )

    engine = PPStructure(show_log=False, lang=lang, recovery=False)
    raw = engine(str(image_path))
    regions: List[Region] = []
    for idx, item in enumerate(raw or [], start=1):
        typ = str(item.get("type", "unknown"))
        bbox = item.get("bbox")
        if isinstance(bbox, (list, tuple)) and len(bbox) == 4:
            x1, y1, x2, y2 = [int(round(v)) for v in bbox]
            poly = bbox_to_poly(x1, y1, max(1, x2 - x1), max(1, y2 - y1))
        else:
            poly = []
        res = item.get("res")
        text = ""
        if isinstance(res, list):
            text_parts = []
            for r in res:
                if isinstance(r, dict):
                    text_parts.append(normalize_text(r.get("text") or r.get("html") or ""))
            text = " / ".join([p for p in text_parts if p])
        elif isinstance(res, dict):
            text = normalize_text(res.get("text") or res.get("html") or "")
        regions.append(
            Region(
                id=f"R{idx:03d}",
                type=typ,
                bbox=poly,
                confidence=0.0,
                engine="ppstructure",
                needs_review=True,
                text=text,
                notes="PP-Structure region; confidence unavailable or model-dependent",
            )
        )
    return regions


def run_layoutparser_placeholder(image_path: Path) -> List[Region]:
    # LayoutParser requires a model config chosen by the user. We keep this as a
    # clearly documented hook instead of silently using a random model.
    try:
        import layoutparser as lp  # type: ignore  # noqa: F401
    except Exception as exc:
        raise SystemExit(
            "LayoutParser is not installed/configured. Install it and add a model config before using --structure layoutparser.\n"
            f"Import error: {exc}"
        )
    raise SystemExit(
        "LayoutParser wrapper is available as a hook, but no default model is configured.\n"
        "Use --structure ppstructure, or extend run_layoutparser_placeholder() with an approved model config."
    )


def load_image_with_cv2(image_path: Path):
    try:
        import cv2  # type: ignore
    except Exception as exc:
        raise SystemExit(f"OpenCV not installed. Install opencv-python. Import error: {exc}")
    image = cv2.imread(str(image_path))
    if image is None:
        raise SystemExit(f"Cannot read image: {image_path}")
    return cv2, image


def detect_opencv_connectors(image_path: Path, out_dir: Path, scale: float) -> List[ConnectorCandidate]:
    try:
        import numpy as np  # type: ignore
    except Exception as exc:
        raise SystemExit(f"NumPy not installed. Install numpy. Import error: {exc}")
    cv2, image = load_image_with_cv2(image_path)
    h, w = image.shape[:2]
    if scale != 1.0:
        image = cv2.resize(image, (int(w * scale), int(h * scale)), interpolation=cv2.INTER_CUBIC)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    binary = cv2.adaptiveThreshold(
        gray,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV,
        31,
        9,
    )
    lines = cv2.HoughLinesP(binary, rho=1, theta=np.pi / 180, threshold=100, minLineLength=50, maxLineGap=8)
    connectors: List[ConnectorCandidate] = []
    debug = image.copy()
    if lines is not None:
        seen = set()
        for raw in lines[:, 0, :]:
            x1, y1, x2, y2 = [int(v) for v in raw]
            length = math.hypot(x2 - x1, y2 - y1)
            if length < 50:
                continue
            key = (min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2))
            if key in seen:
                continue
            seen.add(key)
            connectors.append(
                ConnectorCandidate(
                    id=f"C{len(connectors)+1:03d}",
                    x1=x1,
                    y1=y1,
                    x2=x2,
                    y2=y2,
                    confidence=0.4,
                    needs_review=True,
                )
            )
            cv2.line(debug, (x1, y1), (x2, y2), (255, 0, 0), 2)
            cv2.putText(debug, connectors[-1].id, ((x1 + x2) // 2, (y1 + y2) // 2), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 0, 0), 1)
    cv2.imwrite(str(out_dir / "connectors_overlay.png"), debug)
    cv2.imwrite(str(out_dir / "opencv_binary.png"), binary)
    return connectors


def draw_text_overlay(image_path: Path, out_dir: Path, text_blocks: List[TextBlock], regions: List[Region]) -> None:
    if not text_blocks and not regions:
        return
    cv2, image = load_image_with_cv2(image_path)
    for block in text_blocks:
        if not block.bbox:
            continue
        pts = [(int(p[0]), int(p[1])) for p in block.bbox]
        for i in range(len(pts)):
            cv2.line(image, pts[i], pts[(i + 1) % len(pts)], (0, 150, 0), 2)
        x, y = pts[0]
        cv2.putText(image, block.id, (x, max(12, y - 4)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 150, 0), 1)
    for region in regions:
        if not region.bbox:
            continue
        pts = [(int(p[0]), int(p[1])) for p in region.bbox]
        for i in range(len(pts)):
            cv2.line(image, pts[i], pts[(i + 1) % len(pts)], (0, 0, 220), 2)
        x, y = pts[0]
        cv2.putText(image, region.id, (x, max(12, y - 4)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 220), 1)
    cv2.imwrite(str(out_dir / "text_regions_overlay.png"), image)


def write_review_md(
    out_dir: Path,
    image_path: Path,
    mode: str,
    text_blocks: List[TextBlock],
    regions: List[Region],
    connectors: List[ConnectorCandidate],
) -> None:
    lines: List[str] = []
    lines.append("# Visual Structure Extraction Review")
    lines.append("")
    lines.append(f"Source image: `{image_path}`")
    lines.append(f"Mode: `{mode}`")
    lines.append("")
    lines.append("## Review rule")
    lines.append("")
    lines.append("This output is not a source of truth. It is an extraction aid from mature OCR/layout engines.")
    lines.append("Before PRD writing, manually confirm text, coordinates, connector direction, and branch labels against the original image.")
    lines.append("")
    lines.append("## Text blocks")
    lines.append("")
    lines.append("| id | text | confidence | needs_review | bbox | engine | notes |")
    lines.append("|---|---|---:|---|---|---|---|")
    for b in text_blocks:
        text = b.text.replace("|", "\\|")
        bbox = json.dumps(b.bbox, ensure_ascii=False)
        notes = b.notes.replace("|", "\\|")
        lines.append(f"| {b.id} | {text} | {b.confidence:.4f} | {str(b.needs_review).lower()} | `{bbox}` | {b.engine} | {notes} |")
    lines.append("")
    lines.append("## Regions")
    lines.append("")
    lines.append("| id | type | text | confidence | needs_review | bbox | engine | notes |")
    lines.append("|---|---|---|---:|---|---|---|---|")
    for r in regions:
        text = r.text.replace("|", "\\|")
        bbox = json.dumps(r.bbox, ensure_ascii=False)
        notes = r.notes.replace("|", "\\|")
        lines.append(f"| {r.id} | {r.type} | {text} | {r.confidence:.4f} | {str(r.needs_review).lower()} | `{bbox}` | {r.engine} | {notes} |")
    if mode == "flowchart":
        lines.append("")
        lines.append("## Connector candidates")
        lines.append("")
        lines.append("| id | line | confidence | needs_review | notes |")
        lines.append("|---|---|---:|---|---|")
        for c in connectors:
            line = f"({c.x1},{c.y1})→({c.x2},{c.y2})"
            notes = c.notes.replace("|", "\\|")
            lines.append(f"| {c.id} | {line} | {c.confidence:.4f} | {str(c.needs_review).lower()} | {notes} |")
    lines.append("")
    lines.append("## Output files")
    lines.append("")
    lines.append("- `text_blocks.json` / `text_blocks.csv`")
    lines.append("- `regions.json` / `regions.csv`")
    lines.append("- `text_regions_overlay.png` when OpenCV is installed")
    if mode == "flowchart":
        lines.append("- `connectors.json` / `connectors.csv` when `--opencv-connectors` is used")
        lines.append("- `connectors_overlay.png` when `--opencv-connectors` is used")
    lines.append("")
    lines.append("## Next step")
    lines.append("")
    lines.append("Create a human-confirmed node / region / connector table before editing PRD content.")
    (out_dir / "review.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Extract visual structure from images using mature OCR/layout engines.")
    parser.add_argument("image", type=Path, help="Input image path")
    parser.add_argument("--mode", choices=["general", "ui", "flowchart"], default="general", help="Extraction mode")
    parser.add_argument("--out", type=Path, default=Path("tmp/visual-structure"), help="Output directory")
    parser.add_argument("--ocr", choices=["paddle", "none"], default="paddle", help="OCR engine")
    parser.add_argument("--lang", default="ch", help="PaddleOCR language, e.g. ch, en")
    parser.add_argument("--no-angle-cls", action="store_true", help="Disable PaddleOCR angle classifier")
    parser.add_argument("--structure", choices=["none", "ppstructure", "layoutparser"], default="none", help="Optional layout engine")
    parser.add_argument("--opencv-connectors", action="store_true", help="Detect candidate connector lines for flowchart mode")
    parser.add_argument("--connector-scale", type=float, default=2.0, help="Scale factor for OpenCV connector detection")
    return parser.parse_args(argv)


def main(argv: Optional[List[str]] = None) -> int:
    args = parse_args(argv)
    ensure_dir(args.out)
    if not args.image.exists():
        raise SystemExit(f"Input image does not exist: {args.image}")

    shutil.copyfile(args.image, args.out / args.image.name)

    text_blocks: List[TextBlock] = []
    regions: List[Region] = []
    connectors: List[ConnectorCandidate] = []

    if args.ocr == "paddle":
        text_blocks = run_paddle_ocr(args.image, lang=args.lang, use_angle_cls=not args.no_angle_cls)

    if args.structure == "ppstructure":
        regions = run_ppstructure(args.image, lang=args.lang)
    elif args.structure == "layoutparser":
        regions = run_layoutparser_placeholder(args.image)

    if args.mode == "flowchart" and args.opencv_connectors:
        connectors = detect_opencv_connectors(args.image, args.out, scale=args.connector_scale)

    try:
        draw_text_overlay(args.image, args.out, text_blocks, regions)
    except SystemExit:
        # OpenCV is optional unless connector detection was requested.
        pass

    write_json(args.out / "text_blocks.json", text_blocks)
    write_csv(args.out / "text_blocks.csv", text_blocks)
    write_json(args.out / "regions.json", regions)
    write_csv(args.out / "regions.csv", regions)
    if args.mode == "flowchart":
        write_json(args.out / "connectors.json", connectors)
        write_csv(args.out / "connectors.csv", connectors)

    write_review_md(args.out, args.image, args.mode, text_blocks, regions, connectors)

    print(f"Mode: {args.mode}")
    print(f"Text blocks: {len(text_blocks)}")
    print(f"Regions: {len(regions)}")
    print(f"Connectors: {len(connectors)}")
    print(f"Outputs written to: {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
