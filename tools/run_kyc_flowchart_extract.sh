#!/usr/bin/env bash
set -euo pipefail

# One-click runner for the KYC chapter 3 business flowchart.
#
# It extracts OCR text, flow node candidates, connector candidates, overlays,
# and a manual confirmation template from:
#   knowledge-base/kyc/_assets/account-opening/image4.jpeg
#
# The output is review evidence only. It is not PRD truth until humans confirm
# confirmation_template.csv.

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
IMAGE_PATH="${1:-knowledge-base/kyc/_assets/account-opening/image4.jpeg}"
OUT_DIR="${2:-tmp/flowchart-image4}"
DOCKER_IMAGE="${DOCKER_IMAGE:-prd-visual-tools}"

cd "$ROOT_DIR"

if [[ ! -f "$IMAGE_PATH" ]]; then
  echo "[error] Image not found: $IMAGE_PATH" >&2
  exit 1
fi

mkdir -p "$OUT_DIR"
LOG_FILE="$OUT_DIR/run.log"

run_with_python() {
  echo "[info] Running with local python3" | tee "$LOG_FILE"
  python3 tools/visual_structure_extract.py --check-env | tee -a "$LOG_FILE"
  python3 tools/visual_structure_extract.py \
    "$IMAGE_PATH" \
    --mode flowchart \
    --out "$OUT_DIR" \
    --ocr paddle \
    --structure ppstructure \
    --detect-flow-nodes \
    --detect-connectors \
    2>&1 | tee -a "$LOG_FILE"
}

run_with_docker() {
  echo "[info] Running with Docker image: $DOCKER_IMAGE" | tee "$LOG_FILE"
  if ! docker image inspect "$DOCKER_IMAGE" >/dev/null 2>&1; then
    echo "[info] Building Docker image: $DOCKER_IMAGE" | tee -a "$LOG_FILE"
    docker build -f tools/Dockerfile.visual -t "$DOCKER_IMAGE" . 2>&1 | tee -a "$LOG_FILE"
  fi

  docker run --rm \
    -v "$ROOT_DIR":/workspace \
    "$DOCKER_IMAGE" \
    python3 tools/visual_structure_extract.py --check-env 2>&1 | tee -a "$LOG_FILE"

  docker run --rm \
    -v "$ROOT_DIR":/workspace \
    "$DOCKER_IMAGE" \
    python3 tools/visual_structure_extract.py \
      "$IMAGE_PATH" \
      --mode flowchart \
      --out "$OUT_DIR" \
      --ocr paddle \
      --structure ppstructure \
      --detect-flow-nodes \
      --detect-connectors \
      2>&1 | tee -a "$LOG_FILE"
}

if command -v docker >/dev/null 2>&1; then
  run_with_docker
elif command -v python3 >/dev/null 2>&1; then
  run_with_python
else
  echo "[error] Neither docker nor python3 is available." >&2
  echo "        Install Docker, then run:" >&2
  echo "        bash tools/run_kyc_flowchart_extract.sh" >&2
  exit 1
fi

cat <<EOF | tee -a "$LOG_FILE"

[done] Extraction artifacts written to: $OUT_DIR

Review these files first:
- $OUT_DIR/review.md
- $OUT_DIR/review_overlay.png
- $OUT_DIR/confirmation_template.csv
- $OUT_DIR/flow_nodes.csv
- $OUT_DIR/connectors.csv

PRD writing rule:
- Do not use raw OCR / connector candidates as fact.
- Fill and confirm $OUT_DIR/confirmation_template.csv first.
- Only the confirmed node / connector table may be used to rewrite section 3.2.
EOF
