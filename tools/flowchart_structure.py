#!/usr/bin/env python3
"""
flowchart_structure.py

Semi-automatic flowchart structure recognizer.

Purpose:
- Detect flowchart node boxes from a high-resolution image.
- OCR each node box.
- Detect candidate connector lines.
- Export reviewable node / edge tables before anyone writes PRD content.

This tool is intentionally conservative. It does not claim a flowchart is fully
understood. Anything low-confidence is marked as needs_review.

Recommended usage:
    python3 tools/flowchart_structure.py \
      knowledge-base/kyc/_assets/account-opening/image4.jpeg \
      --out tmp/flowchart-image4 \
      --ocr tesseract \
      --lang chi_sim+eng

Optional dependencies:
    pip install opencv-python pillow pytesseract

System dependency for OCR:
    tesseract with Chinese + English language data, e.g. chi_sim and eng.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import os
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

try:
    import cv2  # type: ignore
except Exception:  # pragma: no cover
    cv2 = None

try:
    import numpy as np  # type: ignore
except Exception:  # pragma: no cover
    np = None

try:
    from PIL import Image  # type: ignore
except Exception:  # pragma: no cover
    Image = None


BBox = Tuple[int, int, int, int]  # x, y, w, h


@dataclass
class Node:
    id: str
    text: str
    type: str
    x: int
    y: int
    w: int
    h: int
    confidence: float
    needs_review: bool
    notes: str = ""


@dataclass
class Edge:
    id: str
    from_node: str
    to_node: str
    label: str
    x1: int
    y1: int
    x2: int
    y2: int
    confidence: float
    needs_review: bool
    notes: str = ""


def require_image_stack() -> None:
    missing = []
    if cv2 is None:
        missing.append("opencv-python")
    if np is None:
        missing.append("numpy")
    if Image is None:
        missing.append("pillow")
    if missing:
        raise SystemExit(
            "Missing dependencies: "
            + ", ".join(missing)
            + "\nInstall with: pip install opencv-python pillow numpy pytesseract"
        )


def ensure_out_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def load_image(path: Path):
    require_image_stack()
    image = cv2.imread(str(path))
    if image is None:
        raise SystemExit(f"Cannot read image: {path}")
    return image


def preprocess(image, scale: float, out_dir: Path):
    h, w = image.shape[:2]
    if scale != 1.0:
        image = cv2.resize(image, (int(w * scale), int(h * scale)), interpolation=cv2.INTER_CUBIC)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (3, 3), 0)
    # Adaptive threshold works better for screenshots with uneven compression.
    binary = cv2.adaptiveThreshold(
        gray,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV,
        31,
        9,
    )
    cv2.imwrite(str(out_dir / "preprocessed_binary.png"), binary)
    cv2.imwrite(str(out_dir / "preprocessed_scaled.png"), image)
    return image, gray, binary


def bbox_iou(a: BBox, b: BBox) -> float:
    ax, ay, aw, ah = a
    bx, by, bw, bh = b
    ax2, ay2 = ax + aw, ay + ah
    bx2, by2 = bx + bw, by + bh
    ix1, iy1 = max(ax, bx), max(ay, by)
    ix2, iy2 = min(ax2, bx2), min(ay2, by2)
    iw, ih = max(0, ix2 - ix1), max(0, iy2 - iy1)
    inter = iw * ih
    union = aw * ah + bw * bh - inter
    return inter / union if union else 0.0


def merge_near_duplicate_boxes(boxes: List[BBox], iou_threshold: float = 0.55) -> List[BBox]:
    boxes = sorted(boxes, key=lambda b: b[2] * b[3], reverse=True)
    kept: List[BBox] = []
    for box in boxes:
        if all(bbox_iou(box, k) < iou_threshold for k in kept):
            kept.append(box)
    return sorted(kept, key=lambda b: (b[1], b[0]))


def detect_node_boxes(binary, min_area: int, max_area_ratio: float) -> List[Tuple[BBox, str, float]]:
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    ih, iw = binary.shape[:2]
    max_area = ih * iw * max_area_ratio
    candidates: List[Tuple[BBox, str, float]] = []
    raw_boxes: List[Tuple[BBox, Any]] = []

    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        area = w * h
        if area < min_area or area > max_area:
            continue
        if w < 24 or h < 14:
            continue
        # Avoid treating page border or tiny text strokes as nodes.
        aspect = w / max(h, 1)
        if aspect > 12 or aspect < 0.08:
            continue
        raw_boxes.append(((x, y, w, h), contour))

    merged = merge_near_duplicate_boxes([b for b, _ in raw_boxes])
    contour_by_box: Dict[BBox, Any] = {}
    for box, contour in raw_boxes:
        best = max(merged, key=lambda m: bbox_iou(box, m)) if merged else None
        if best and bbox_iou(box, best) > 0.3:
            contour_by_box[best] = contour

    for box in merged:
        x, y, w, h = box
        contour = contour_by_box.get(box)
        node_type = "process"
        confidence = 0.60
        if contour is not None:
            peri = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.03 * peri, True)
            contour_area = max(cv2.contourArea(contour), 1.0)
            fill_ratio = contour_area / max(w * h, 1)
            if len(approx) == 4 and 0.65 <= w / max(h, 1) <= 1.55 and fill_ratio < 0.72:
                node_type = "decision"
                confidence = 0.72
            elif len(approx) >= 4:
                confidence = 0.68
        candidates.append((box, node_type, confidence))

    return candidates


def crop_with_padding(image, box: BBox, pad: int = 8):
    x, y, w, h = box
    ih, iw = image.shape[:2]
    x1, y1 = max(0, x - pad), max(0, y - pad)
    x2, y2 = min(iw, x + w + pad), min(ih, y + h + pad)
    return image[y1:y2, x1:x2]


def clean_ocr_text(text: str) -> str:
    text = text.replace("\r", "\n")
    lines = [re.sub(r"\s+", " ", line).strip() for line in text.split("\n")]
    lines = [line for line in lines if line]
    return " / ".join(lines)


def ocr_crop(crop, engine: str, lang: str) -> Tuple[str, float, str]:
    if engine == "none":
        return "", 0.0, "OCR disabled"
    if engine == "tesseract":
        try:
            import pytesseract  # type: ignore
        except Exception:
            return "", 0.0, "pytesseract not installed"
        rgb = cv2.cvtColor(crop, cv2.COLOR_BGR2RGB)
        pil_img = Image.fromarray(rgb)
        try:
            data = pytesseract.image_to_data(pil_img, lang=lang, output_type=pytesseract.Output.DICT)
            words: List[str] = []
            confs: List[float] = []
            for text, conf in zip(data.get("text", []), data.get("conf", [])):
                text = str(text).strip()
                if not text:
                    continue
                try:
                    c = float(conf)
                except Exception:
                    c = -1
                if c >= 0:
                    confs.append(c / 100.0)
                words.append(text)
            joined = clean_ocr_text(" ".join(words))
            confidence = sum(confs) / len(confs) if confs else 0.0
            return joined, confidence, ""
        except Exception as exc:
            return "", 0.0, f"tesseract failed: {exc}"
    return "", 0.0, f"unsupported OCR engine: {engine}"


def make_nodes(image, boxes: List[Tuple[BBox, str, float]], ocr: str, lang: str, out_dir: Path) -> List[Node]:
    nodes: List[Node] = []
    crops_dir = out_dir / "node_crops"
    ensure_out_dir(crops_dir)
    for idx, (box, node_type, shape_conf) in enumerate(boxes, start=1):
        crop = crop_with_padding(image, box)
        crop_path = crops_dir / f"N{idx:03d}.png"
        cv2.imwrite(str(crop_path), crop)
        text, ocr_conf, note = ocr_crop(crop, ocr, lang)
        confidence = round((shape_conf + ocr_conf) / 2.0, 3) if text else round(shape_conf * 0.55, 3)
        needs_review = confidence < 0.72 or not text
        x, y, w, h = box
        nodes.append(
            Node(
                id=f"N{idx:03d}",
                text=text,
                type=node_type,
                x=x,
                y=y,
                w=w,
                h=h,
                confidence=confidence,
                needs_review=needs_review,
                notes=note,
            )
        )
    return nodes


def point_to_box_distance(px: int, py: int, node: Node) -> float:
    x1, y1, x2, y2 = node.x, node.y, node.x + node.w, node.y + node.h
    dx = max(x1 - px, 0, px - x2)
    dy = max(y1 - py, 0, py - y2)
    return math.sqrt(dx * dx + dy * dy)


def nearest_node(px: int, py: int, nodes: List[Node], max_distance: int) -> Optional[Tuple[Node, float]]:
    best: Optional[Tuple[Node, float]] = None
    for node in nodes:
        dist = point_to_box_distance(px, py, node)
        if dist <= max_distance and (best is None or dist < best[1]):
            best = (node, dist)
    return best


def detect_edges(binary, nodes: List[Node], max_endpoint_distance: int) -> List[Edge]:
    # Detect straight connector candidates. This does not fully solve arrowheads;
    # all detected edges remain reviewable.
    edges: List[Edge] = []
    lines = cv2.HoughLinesP(
        binary,
        rho=1,
        theta=np.pi / 180,
        threshold=80,
        minLineLength=40,
        maxLineGap=10,
    )
    if lines is None:
        return edges

    seen: set[Tuple[str, str, int, int, int, int]] = set()
    for line in lines[:, 0, :]:
        x1, y1, x2, y2 = map(int, line)
        length = math.hypot(x2 - x1, y2 - y1)
        if length < 40:
            continue
        a = nearest_node(x1, y1, nodes, max_endpoint_distance)
        b = nearest_node(x2, y2, nodes, max_endpoint_distance)
        if not a or not b:
            continue
        n1, d1 = a
        n2, d2 = b
        if n1.id == n2.id:
            continue
        # Direction is a guess. Human must confirm arrow direction.
        key = tuple(sorted([n1.id, n2.id]) + [min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)])
        if key in seen:
            continue
        seen.add(key)
        confidence = max(0.1, min(0.65, 0.65 - (d1 + d2) / max(max_endpoint_distance * 2, 1) * 0.35))
        edges.append(
            Edge(
                id=f"E{len(edges)+1:03d}",
                from_node=n1.id,
                to_node=n2.id,
                label="",
                x1=x1,
                y1=y1,
                x2=x2,
                y2=y2,
                confidence=round(confidence, 3),
                needs_review=True,
                notes="candidate connector; arrow direction and label require review",
            )
        )
    return edges


def draw_debug(image, nodes: List[Node], edges: List[Edge], out_dir: Path) -> None:
    debug = image.copy()
    for node in nodes:
        color = (0, 0, 255) if node.needs_review else (0, 160, 0)
        cv2.rectangle(debug, (node.x, node.y), (node.x + node.w, node.y + node.h), color, 2)
        cv2.putText(debug, node.id, (node.x, max(12, node.y - 6)), cv2.FONT_HERSHEY_SIMPLEX, 0.55, color, 2)
    for edge in edges:
        cv2.line(debug, (edge.x1, edge.y1), (edge.x2, edge.y2), (255, 0, 0), 2)
        mx, my = (edge.x1 + edge.x2) // 2, (edge.y1 + edge.y2) // 2
        cv2.putText(debug, edge.id, (mx, my), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 0, 0), 1)
    cv2.imwrite(str(out_dir / "debug_overlay.png"), debug)


def write_json(path: Path, rows: Iterable[Any]) -> None:
    with path.open("w", encoding="utf-8") as f:
        json.dump([asdict(row) for row in rows], f, ensure_ascii=False, indent=2)


def write_csv(path: Path, rows: List[Any]) -> None:
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    fieldnames = list(asdict(rows[0]).keys())
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(asdict(row))


def write_review_md(out_dir: Path, image_path: Path, nodes: List[Node], edges: List[Edge]) -> None:
    lines: List[str] = []
    lines.append("# Flowchart Structure Review")
    lines.append("")
    lines.append(f"Source image: `{image_path}`")
    lines.append("")
    lines.append("## Review rule")
    lines.append("")
    lines.append("This output is not a source of truth. It is a review aid.")
    lines.append("Any row marked `needs_review=true` must be checked against the original image before writing PRD content.")
    lines.append("")
    lines.append("## Nodes")
    lines.append("")
    lines.append("| id | type | text | bbox | confidence | needs_review | notes |")
    lines.append("|---|---|---|---|---:|---|---|")
    for n in nodes:
        bbox = f"({n.x},{n.y},{n.w},{n.h})"
        text = n.text.replace("|", "\\|")
        notes = n.notes.replace("|", "\\|")
        lines.append(f"| {n.id} | {n.type} | {text} | {bbox} | {n.confidence:.3f} | {str(n.needs_review).lower()} | {notes} |")
    lines.append("")
    lines.append("## Candidate edges")
    lines.append("")
    lines.append("| id | from | to | label | line | confidence | needs_review | notes |")
    lines.append("|---|---|---|---|---|---:|---|---|")
    for e in edges:
        line = f"({e.x1},{e.y1})→({e.x2},{e.y2})"
        notes = e.notes.replace("|", "\\|")
        lines.append(f"| {e.id} | {e.from_node} | {e.to_node} | {e.label} | {line} | {e.confidence:.3f} | {str(e.needs_review).lower()} | {notes} |")
    lines.append("")
    lines.append("## Files")
    lines.append("")
    lines.append("- `debug_overlay.png`: nodes and candidate connectors overlay")
    lines.append("- `preprocessed_scaled.png`: scaled source image")
    lines.append("- `preprocessed_binary.png`: binary image used for detection")
    lines.append("- `node_crops/`: cropped node images for manual OCR review")
    lines.append("- `nodes.json` / `nodes.csv`")
    lines.append("- `edges.json` / `edges.csv`")
    (out_dir / "review.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Recognize flowchart node / edge structure from an image.")
    parser.add_argument("image", type=Path, help="Input flowchart image path")
    parser.add_argument("--out", type=Path, default=Path("tmp/flowchart-structure"), help="Output directory")
    parser.add_argument("--scale", type=float, default=2.0, help="Scale factor before detection / OCR")
    parser.add_argument("--ocr", choices=["none", "tesseract"], default="none", help="OCR engine")
    parser.add_argument("--lang", default="chi_sim+eng", help="OCR language for tesseract")
    parser.add_argument("--min-area", type=int, default=1500, help="Minimum node bbox area after scaling")
    parser.add_argument("--max-area-ratio", type=float, default=0.45, help="Maximum node bbox area ratio")
    parser.add_argument("--max-endpoint-distance", type=int, default=60, help="Max distance from line endpoint to node bbox")
    return parser.parse_args(argv)


def main(argv: Optional[List[str]] = None) -> int:
    args = parse_args(argv)
    ensure_out_dir(args.out)
    image = load_image(args.image)
    scaled, _, binary = preprocess(image, args.scale, args.out)
    box_candidates = detect_node_boxes(binary, min_area=args.min_area, max_area_ratio=args.max_area_ratio)
    nodes = make_nodes(scaled, box_candidates, args.ocr, args.lang, args.out)
    edges = detect_edges(binary, nodes, max_endpoint_distance=args.max_endpoint_distance)
    draw_debug(scaled, nodes, edges, args.out)
    write_json(args.out / "nodes.json", nodes)
    write_json(args.out / "edges.json", edges)
    write_csv(args.out / "nodes.csv", nodes)
    write_csv(args.out / "edges.csv", edges)
    write_review_md(args.out, args.image, nodes, edges)
    print(f"Detected nodes: {len(nodes)}")
    print(f"Candidate edges: {len(edges)}")
    print(f"Needs review nodes: {sum(1 for n in nodes if n.needs_review)}")
    print(f"Outputs written to: {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
