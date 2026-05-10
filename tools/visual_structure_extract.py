#!/usr/bin/env python3
"""
visual_structure_extract.py

Practical visual-structure extraction wrapper for PRD evidence review.

This tool uses mature libraries instead of custom OCR:
- PaddleOCR 2.x: Chinese / English OCR text boxes.
- PP-Structure 2.x: optional layout / region extraction.
- OpenCV: deterministic overlays, flowchart node-shape candidates, and
  connector candidates.

It does not write PRD content. It produces review artifacts so a human can
confirm text, nodes, arrows, and branch labels before PRD updates.

Install:
    pip install -r tools/requirements-visual.txt

Check environment:
    python3 tools/visual_structure_extract.py --check-env

Examples:
    python3 tools/visual_structure_extract.py image.png --mode general --out tmp/visual

    python3 tools/visual_structure_extract.py page.png --mode ui --structure ppstructure --out tmp/ui

    python3 tools/visual_structure_extract.py flowchart.png \
      --mode flowchart \
      --structure ppstructure \
      --detect-flow-nodes \
      --detect-connectors \
      --out tmp/flowchart
"""

from __future__ import annotations

import argparse
import csv
import importlib.util
import json
import math
import re
import shutil
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Iterable, List, Optional, Sequence, Tuple


BBox = Tuple[int, int, int, int]


@dataclass
class EnvStatus:
    name: str
    installed: bool
    version: str
    status: str
    notes: str = ""


@dataclass
class TextBlock:
    id: str
    text: str
    bbox: List[List[int]]
    center_x: int
    center_y: int
    confidence: float
    engine: str
    needs_review: bool
    notes: str = ""


@dataclass
class Region:
    id: str
    type: str
    text: str
    bbox: List[List[int]]
    center_x: int
    center_y: int
    confidence: float
    engine: str
    needs_review: bool
    notes: str = ""


@dataclass
class FlowNode:
    id: str
    type: str
    text: str
    bbox: List[List[int]]
    center_x: int
    center_y: int
    confidence: float
    source: str
    text_block_ids: str
    needs_review: bool
    notes: str = ""


@dataclass
class ConnectorCandidate:
    id: str
    from_node: str
    to_node: str
    label: str
    line: List[List[int]]
    confidence: float
    needs_review: bool
    notes: str = "candidate connector; arrow direction and branch label require manual review"


def package_version(package: str) -> str:
    try:
        from importlib.metadata import version
    except Exception:  # pragma: no cover
        try:
            from importlib_metadata import version  # type: ignore
        except Exception:
            return "unknown"
    try:
        return version(package)
    except Exception:
        return "not-installed"


def major_version(text: str) -> Optional[int]:
    m = re.match(r"^\s*(\d+)", text or "")
    return int(m.group(1)) if m else None


def check_environment() -> List[EnvStatus]:
    specs = [
        ("paddleocr", "paddleocr", True),
        ("paddle", "paddlepaddle", True),
        ("cv2", "opencv-python-headless", False),
        ("numpy", "numpy", False),
        ("PIL", "Pillow", False),
    ]
    rows: List[EnvStatus] = []
    for module, package, required in specs:
        installed = importlib.util.find_spec(module) is not None
        ver = package_version(package) if installed else "not-installed"
        status = "ok" if installed else ("missing" if required else "optional-missing")
        notes = ""
        if module == "paddleocr" and installed:
            major = major_version(ver)
            if major is not None and major >= 3:
                status = "unsupported"
                notes = "This tool targets PaddleOCR 2.x + PP-Structure 2.x. Install tools/requirements-visual.txt."
        rows.append(EnvStatus(module, installed, ver, status, notes))
    return rows


def print_env_status() -> int:
    rows = check_environment()
    print(json.dumps([asdict(r) for r in rows], ensure_ascii=False, indent=2))
    bad = [r for r in rows if r.status in {"missing", "unsupported"}]
    return 2 if bad else 0


def require_paddleocr2() -> None:
    ver = package_version("paddleocr")
    if ver in {"not-installed", "unknown"}:
        raise SystemExit("PaddleOCR is not installed. Run: pip install -r tools/requirements-visual.txt")
    major = major_version(ver)
    if major is not None and major >= 3:
        raise SystemExit(
            f"Unsupported PaddleOCR version: {ver}. This tool targets PaddleOCR 2.x. "
            "Run: pip install -r tools/requirements-visual.txt"
        )


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def normalize_text(value: Any) -> str:
    if value is None:
        return ""
    text = str(value).replace("\r", "\n")
    return " / ".join(" ".join(line.split()) for line in text.split("\n") if line.strip())


def polygon_to_bbox(poly: Sequence[Sequence[float]]) -> BBox:
    xs = [int(round(p[0])) for p in poly]
    ys = [int(round(p[1])) for p in poly]
    x1, y1 = min(xs), min(ys)
    x2, y2 = max(xs), max(ys)
    return x1, y1, max(1, x2 - x1), max(1, y2 - y1)


def bbox_to_poly(x: int, y: int, w: int, h: int) -> List[List[int]]:
    return [[x, y], [x + w, y], [x + w, y + h], [x, y + h]]


def center_of(poly: Sequence[Sequence[int]]) -> Tuple[int, int]:
    if not poly:
        return 0, 0
    x, y, w, h = polygon_to_bbox(poly)
    return x + w // 2, y + h // 2


def in_poly_bbox(px: int, py: int, poly: Sequence[Sequence[int]], pad: int = 0) -> bool:
    x, y, w, h = polygon_to_bbox(poly)
    return x - pad <= px <= x + w + pad and y - pad <= py <= y + h + pad


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


def sort_position(row: Any) -> Tuple[int, int]:
    return getattr(row, "center_y", 0), getattr(row, "center_x", 0)


def run_paddle_ocr(image_path: Path, lang: str, use_angle_cls: bool) -> List[TextBlock]:
    require_paddleocr2()
    try:
        from paddleocr import PaddleOCR  # type: ignore
    except Exception as exc:
        raise SystemExit(f"Cannot import PaddleOCR: {exc}")

    try:
        ocr = PaddleOCR(use_angle_cls=use_angle_cls, lang=lang, show_log=False)
    except TypeError:
        ocr = PaddleOCR(use_angle_cls=use_angle_cls, lang=lang)
    raw = ocr.ocr(str(image_path), cls=use_angle_cls)

    rows: List[Any] = []
    if isinstance(raw, list):
        if len(raw) == 1 and isinstance(raw[0], list):
            rows = raw[0]
        else:
            rows = raw

    blocks: List[TextBlock] = []
    for idx, item in enumerate(rows, start=1):
        try:
            box = item[0]
            text = normalize_text(item[1][0])
            score = float(item[1][1])
            poly = [[int(round(p[0])), int(round(p[1]))] for p in box]
        except Exception:
            continue
        cx, cy = center_of(poly)
        blocks.append(
            TextBlock(
                id=f"T{idx:03d}",
                text=text,
                bbox=poly,
                center_x=cx,
                center_y=cy,
                confidence=round(score, 4),
                engine="paddleocr2",
                needs_review=score < 0.85 or not text,
            )
        )
    return sorted(blocks, key=sort_position)


def run_ppstructure(image_path: Path, lang: str) -> List[Region]:
    require_paddleocr2()
    try:
        from paddleocr import PPStructure  # type: ignore
    except Exception as exc:
        raise SystemExit(f"Cannot import PPStructure from PaddleOCR 2.x: {exc}")

    try:
        engine = PPStructure(show_log=False, lang=lang, recovery=False)
    except TypeError:
        engine = PPStructure(lang=lang, recovery=False)
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
        cx, cy = center_of(poly)
        res = item.get("res")
        parts: List[str] = []
        if isinstance(res, list):
            for r in res:
                if isinstance(r, dict):
                    parts.append(normalize_text(r.get("text") or r.get("html") or ""))
        elif isinstance(res, dict):
            parts.append(normalize_text(res.get("text") or res.get("html") or ""))
        regions.append(
            Region(
                id=f"R{idx:03d}",
                type=typ,
                text=" / ".join(p for p in parts if p),
                bbox=poly,
                center_x=cx,
                center_y=cy,
                confidence=0.0,
                engine="ppstructure2",
                needs_review=True,
                notes="PP-Structure region; model-dependent result that must be reviewed",
            )
        )
    return sorted(regions, key=sort_position)


def load_cv_image(image_path: Path):
    try:
        import cv2  # type: ignore
    except Exception as exc:
        raise SystemExit(f"OpenCV is required for overlays or flowchart detection: {exc}")
    image = cv2.imread(str(image_path))
    if image is None:
        raise SystemExit(f"Cannot read image: {image_path}")
    return cv2, image


def binary_for_cv(image, scale: float):
    import cv2  # type: ignore
    if scale != 1.0:
        h, w = image.shape[:2]
        image = cv2.resize(image, (int(w * scale), int(h * scale)), interpolation=cv2.INTER_CUBIC)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (3, 3), 0)
    binary = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 31, 9)
    return image, binary


def detect_flow_node_shapes(image_path: Path, scale: float, min_area: int, max_area_ratio: float) -> List[FlowNode]:
    import cv2  # type: ignore
    cv2, image = load_cv_image(image_path)
    scaled, binary = binary_for_cv(image, scale)
    ih, iw = binary.shape[:2]
    max_area = ih * iw * max_area_ratio
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    nodes: List[FlowNode] = []
    seen: List[BBox] = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        area = w * h
        if area < min_area or area > max_area or w < 32 or h < 20:
            continue
        aspect = w / max(h, 1)
        if aspect > 15 or aspect < 0.06:
            continue
        dup = False
        for sx, sy, sw, sh in seen:
            ix1, iy1 = max(x, sx), max(y, sy)
            ix2, iy2 = min(x + w, sx + sw), min(y + h, sy + sh)
            inter = max(0, ix2 - ix1) * max(0, iy2 - iy1)
            union = area + sw * sh - inter
            if union and inter / union > 0.65:
                dup = True
                break
        if dup:
            continue
        seen.append((x, y, w, h))
        peri = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.03 * peri, True)
        fill_ratio = max(cv2.contourArea(contour), 1.0) / max(area, 1)
        node_type = "process_candidate"
        if len(approx) == 4 and 0.65 <= aspect <= 1.55 and fill_ratio < 0.72:
            node_type = "decision_candidate"
        poly = bbox_to_poly(x, y, w, h)
        cx, cy = center_of(poly)
        nodes.append(
            FlowNode(
                id=f"N{len(nodes)+1:03d}",
                type=node_type,
                text="",
                bbox=poly,
                center_x=cx,
                center_y=cy,
                confidence=0.70,
                source="opencv_shape",
                text_block_ids="",
                needs_review=True,
                notes="OpenCV shape candidate; confirm text, type, and whether this is a flow node",
            )
        )
    return sorted(nodes, key=sort_position)


def attach_text_to_nodes(nodes: List[FlowNode], text_blocks: List[TextBlock], padding: int = 8) -> List[FlowNode]:
    used: set[str] = set()
    for node in nodes:
        attached = [b for b in text_blocks if in_poly_bbox(b.center_x, b.center_y, node.bbox, padding)]
        attached = sorted(attached, key=sort_position)
        if attached:
            node.text = " / ".join(b.text for b in attached if b.text)
            node.text_block_ids = ",".join(b.id for b in attached)
            avg = sum(b.confidence for b in attached) / len(attached)
            node.confidence = round((node.confidence + avg) / 2, 4)
            node.needs_review = True
            used.update(b.id for b in attached)
        else:
            node.notes += "; no OCR text attached"
    for block in text_blocks:
        if block.id in used:
            continue
        nodes.append(
            FlowNode(
                id=f"N{len(nodes)+1:03d}",
                type="text_only_candidate",
                text=block.text,
                bbox=block.bbox,
                center_x=block.center_x,
                center_y=block.center_y,
                confidence=block.confidence,
                source="ocr_text",
                text_block_ids=block.id,
                needs_review=True,
                notes="OCR text not attached to a detected shape; may be node text, branch label, or annotation",
            )
        )
    return sorted(nodes, key=sort_position)


def nearest_node(px: int, py: int, nodes: List[FlowNode], max_distance: int) -> Optional[Tuple[FlowNode, float]]:
    best: Optional[Tuple[FlowNode, float]] = None
    for n in nodes:
        x, y, w, h = polygon_to_bbox(n.bbox)
        dx = max(x - px, 0, px - (x + w))
        dy = max(y - py, 0, py - (y + h))
        d = math.hypot(dx, dy)
        if d <= max_distance and (best is None or d < best[1]):
            best = (n, d)
    return best


def detect_connectors(image_path: Path, nodes: List[FlowNode], scale: float, max_endpoint_distance: int, out_dir: Path) -> List[ConnectorCandidate]:
    import cv2  # type: ignore
    import numpy as np  # type: ignore
    cv2, image = load_cv_image(image_path)
    scaled, binary = binary_for_cv(image, scale)
    lines = cv2.HoughLinesP(binary, rho=1, theta=np.pi / 180, threshold=100, minLineLength=50, maxLineGap=8)
    debug = scaled.copy()
    out: List[ConnectorCandidate] = []
    seen = set()
    if lines is not None:
        for raw in lines[:, 0, :]:
            x1, y1, x2, y2 = [int(v) for v in raw]
            if math.hypot(x2 - x1, y2 - y1) < 50:
                continue
            a = nearest_node(x1, y1, nodes, max_endpoint_distance)
            b = nearest_node(x2, y2, nodes, max_endpoint_distance)
            frm = to = ""
            conf = 0.35
            if a and b and a[0].id != b[0].id:
                frm, to = a[0].id, b[0].id
                conf = max(0.35, min(0.65, 0.65 - (a[1] + b[1]) / max(max_endpoint_distance * 2, 1) * 0.25))
            key = (frm, to, min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2))
            if key in seen:
                continue
            seen.add(key)
            out.append(
                ConnectorCandidate(
                    id=f"C{len(out)+1:03d}",
                    from_node=frm,
                    to_node=to,
                    label="",
                    line=[[x1, y1], [x2, y2]],
                    confidence=round(conf, 4),
                    needs_review=True,
                )
            )
            cv2.line(debug, (x1, y1), (x2, y2), (255, 0, 0), 2)
            cv2.putText(debug, out[-1].id, ((x1 + x2) // 2, (y1 + y2) // 2), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 0, 0), 1)
    cv2.imwrite(str(out_dir / "connectors_overlay.png"), debug)
    cv2.imwrite(str(out_dir / "opencv_binary.png"), binary)
    return out


def draw_overlay(image_path: Path, out_dir: Path, text_blocks: List[TextBlock], regions: List[Region], nodes: List[FlowNode]) -> None:
    import cv2  # type: ignore
    cv2, image = load_cv_image(image_path)
    for r in regions:
        if not r.bbox:
            continue
        pts = [(int(p[0]), int(p[1])) for p in r.bbox]
        for i in range(len(pts)):
            cv2.line(image, pts[i], pts[(i + 1) % len(pts)], (0, 0, 220), 2)
        cv2.putText(image, r.id, (pts[0][0], max(12, pts[0][1] - 4)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 220), 1)
    for b in text_blocks:
        pts = [(int(p[0]), int(p[1])) for p in b.bbox]
        for i in range(len(pts)):
            cv2.line(image, pts[i], pts[(i + 1) % len(pts)], (0, 150, 0), 2)
        cv2.putText(image, b.id, (pts[0][0], max(12, pts[0][1] - 4)), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 150, 0), 1)
    for n in nodes:
        pts = [(int(p[0]), int(p[1])) for p in n.bbox]
        for i in range(len(pts)):
            cv2.line(image, pts[i], pts[(i + 1) % len(pts)], (180, 0, 180), 2)
        cv2.putText(image, n.id, (pts[0][0], max(12, pts[0][1] - 8)), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (180, 0, 180), 2)
    cv2.imwrite(str(out_dir / "review_overlay.png"), image)


def write_confirmation(path: Path, nodes: List[FlowNode], connectors: List[ConnectorCandidate]) -> None:
    fields = ["row_type", "id", "confirmed", "text_or_label_confirmed", "type_confirmed", "from_node_confirmed", "to_node_confirmed", "notes"]
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for n in nodes:
            w.writerow({"row_type": "node", "id": n.id, "confirmed": "false", "text_or_label_confirmed": n.text, "type_confirmed": n.type, "from_node_confirmed": "", "to_node_confirmed": "", "notes": "Confirm exact text, node type, and whether this is a business-flow node."})
        for c in connectors:
            w.writerow({"row_type": "connector", "id": c.id, "confirmed": "false", "text_or_label_confirmed": c.label, "type_confirmed": "connector", "from_node_confirmed": c.from_node, "to_node_confirmed": c.to_node, "notes": "Confirm arrow direction and branch label from original image."})


def write_review(out_dir: Path, image: Path, mode: str, text_blocks: List[TextBlock], regions: List[Region], nodes: List[FlowNode], connectors: List[ConnectorCandidate]) -> None:
    lines: List[str] = [
        "# Visual Structure Extraction Review",
        "",
        f"Source image: `{image}`",
        f"Mode: `{mode}`",
        "",
        "## Status",
        "",
        f"- Text blocks: {len(text_blocks)}",
        f"- Regions: {len(regions)}",
        f"- Flow node candidates: {len(nodes)}",
        f"- Connector candidates: {len(connectors)}",
        f"- Text blocks needing review: {sum(1 for x in text_blocks if x.needs_review)}",
        f"- Flow nodes needing review: {sum(1 for x in nodes if x.needs_review)}",
        "",
        "## Review rule",
        "",
        "This output is not a source of truth. It is evidence extracted by PaddleOCR / PP-Structure plus deterministic OpenCV helpers.",
        "Before PRD writing, manually confirm text, node identity, connector direction, and branch labels against the original image.",
        "",
        "## Text blocks",
        "",
        "| id | text | confidence | needs_review | bbox |",
        "|---|---|---:|---|---|",
    ]
    for b in text_blocks:
        lines.append(f"| {b.id} | {b.text.replace('|', '\\|')} | {b.confidence:.4f} | {str(b.needs_review).lower()} | `{json.dumps(b.bbox, ensure_ascii=False)}` |")
    if regions:
        lines += ["", "## Regions", "", "| id | type | text | needs_review | bbox | notes |", "|---|---|---|---|---|---|"]
        for r in regions:
            lines.append(f"| {r.id} | {r.type} | {r.text.replace('|', '\\|')} | {str(r.needs_review).lower()} | `{json.dumps(r.bbox, ensure_ascii=False)}` | {r.notes.replace('|', '\\|')} |")
    if mode == "flowchart":
        lines += ["", "## Flow node candidates", "", "| id | type | text | source | text_blocks | confidence | needs_review | bbox | notes |", "|---|---|---|---|---|---:|---|---|---|"]
        for n in nodes:
            lines.append(f"| {n.id} | {n.type} | {n.text.replace('|', '\\|')} | {n.source} | {n.text_block_ids} | {n.confidence:.4f} | {str(n.needs_review).lower()} | `{json.dumps(n.bbox, ensure_ascii=False)}` | {n.notes.replace('|', '\\|')} |")
        lines += ["", "## Connector candidates", "", "| id | from | to | label | confidence | needs_review | line | notes |", "|---|---|---|---|---:|---|---|---|"]
        for c in connectors:
            lines.append(f"| {c.id} | {c.from_node} | {c.to_node} | {c.label} | {c.confidence:.4f} | {str(c.needs_review).lower()} | `{json.dumps(c.line, ensure_ascii=False)}` | {c.notes.replace('|', '\\|')} |")
    lines += [
        "",
        "## Output files",
        "",
        "- `review_overlay.png`: text / region / node overlay for manual review",
        "- `text_blocks.csv` / `text_blocks.json`",
        "- `regions.csv` / `regions.json`",
    ]
    if mode == "flowchart":
        lines += ["- `flow_nodes.csv` / `flow_nodes.json`", "- `connectors.csv` / `connectors.json`", "- `confirmation_template.csv`: fill this before using results as PRD evidence", "- `connectors_overlay.png` and `opencv_binary.png` when connectors are detected"]
    lines += ["", "## Required next step", "", "Use `confirmation_template.csv` or `review.md` to produce a human-confirmed table. Only the confirmed table may be used for PRD updates."]
    (out_dir / "review.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Extract visual structure from images using PaddleOCR/PP-Structure/OpenCV.")
    p.add_argument("image", type=Path, nargs="?", help="Input image path")
    p.add_argument("--check-env", action="store_true", help="Check dependencies and exit")
    p.add_argument("--mode", choices=["general", "ui", "flowchart"], default="general")
    p.add_argument("--out", type=Path, default=Path("tmp/visual-structure"))
    p.add_argument("--ocr", choices=["paddle", "none"], default="paddle")
    p.add_argument("--lang", default="ch")
    p.add_argument("--no-angle-cls", action="store_true")
    p.add_argument("--structure", choices=["none", "ppstructure"], default="none")
    p.add_argument("--detect-flow-nodes", action="store_true")
    p.add_argument("--detect-connectors", action="store_true")
    p.add_argument("--opencv-scale", type=float, default=2.0)
    p.add_argument("--min-node-area", type=int, default=1600)
    p.add_argument("--max-node-area-ratio", type=float, default=0.45)
    p.add_argument("--max-endpoint-distance", type=int, default=80)
    return p.parse_args(argv)


def main(argv: Optional[List[str]] = None) -> int:
    args = parse_args(argv)
    if args.check_env:
        return print_env_status()
    if not args.image:
        raise SystemExit("Missing image path. Use --check-env to check dependencies without an image.")
    if not args.image.exists():
        raise SystemExit(f"Input image does not exist: {args.image}")
    ensure_dir(args.out)
    shutil.copyfile(args.image, args.out / args.image.name)

    text_blocks: List[TextBlock] = []
    regions: List[Region] = []
    nodes: List[FlowNode] = []
    connectors: List[ConnectorCandidate] = []

    if args.ocr == "paddle":
        text_blocks = run_paddle_ocr(args.image, lang=args.lang, use_angle_cls=not args.no_angle_cls)
    if args.structure == "ppstructure":
        regions = run_ppstructure(args.image, lang=args.lang)

    if args.mode == "flowchart":
        if args.detect_flow_nodes:
            nodes = detect_flow_node_shapes(args.image, scale=args.opencv_scale, min_area=args.min_node_area, max_area_ratio=args.max_node_area_ratio)
            nodes = attach_text_to_nodes(nodes, text_blocks)
        else:
            for b in text_blocks:
                nodes.append(FlowNode(f"N{len(nodes)+1:03d}", "text_only_candidate", b.text, b.bbox, b.center_x, b.center_y, b.confidence, "ocr_text", b.id, True, "Decide manually whether this is a node, branch label, or annotation."))
        if args.detect_connectors:
            connectors = detect_connectors(args.image, nodes, scale=args.opencv_scale, max_endpoint_distance=args.max_endpoint_distance, out_dir=args.out)

    try:
        draw_overlay(args.image, args.out, text_blocks, regions, nodes)
    except SystemExit as exc:
        (args.out / "overlay_skipped.txt").write_text(str(exc), encoding="utf-8")

    write_json(args.out / "text_blocks.json", text_blocks)
    write_csv(args.out / "text_blocks.csv", text_blocks)
    write_json(args.out / "regions.json", regions)
    write_csv(args.out / "regions.csv", regions)
    if args.mode == "flowchart":
        write_json(args.out / "flow_nodes.json", nodes)
        write_csv(args.out / "flow_nodes.csv", nodes)
        write_json(args.out / "connectors.json", connectors)
        write_csv(args.out / "connectors.csv", connectors)
        write_confirmation(args.out / "confirmation_template.csv", nodes, connectors)

    write_review(args.out, args.image, args.mode, text_blocks, regions, nodes, connectors)
    print(f"Mode: {args.mode}")
    print(f"Text blocks: {len(text_blocks)}")
    print(f"Regions: {len(regions)}")
    print(f"Flow node candidates: {len(nodes)}")
    print(f"Connector candidates: {len(connectors)}")
    print(f"Outputs written to: {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
