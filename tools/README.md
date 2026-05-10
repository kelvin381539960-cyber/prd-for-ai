---
type: tools-index
status: active
last_updated: 2026-05-05
---

# Tools

本目录存放维护本仓库用的辅助脚本。

工具可以用于提取表格、转换来源文件、检查链接、校验 front matter 或生成索引。

工具不得承载 PRD、业务事实、reference data 或外部原始文档。

## 当前工具

| 工具 | 用途 | 示例 |
|---|---|---|
| `validate_prd.py` | 校验 `requirements/` 下的 PRD 是否符合写作 workflow | `python3 tools/validate_prd.py` |
| `extract_docx_tables.py` | 从 DOCX 来源文件中提取表格为 Markdown 或 CSV | `python3 tools/extract_docx_tables.py path/to/file.docx --out tmp/tables.md` |
| `extract_tables.py` | 兼容入口，转调 `extract_docx_tables.py` | `python3 tools/extract_tables.py path/to/file.docx` |
| `visual_structure_extract.py` | 基于成熟库封装图片结构提取：PaddleOCR 2.x / PP-Structure 2.x 做 OCR 与区域识别，OpenCV 可选做流程图节点与候选连线；输出确认模板，不直接生成 PRD。说明见 `tools/visual-structure-extract.md`，Docker 环境见 `tools/Dockerfile.visual` | `python3 tools/visual_structure_extract.py path/to/image.png --mode flowchart --out tmp/visual --ocr paddle --structure ppstructure --detect-flow-nodes --detect-connectors` |

## validate_prd.py

默认扫描 `requirements/**/*.md`，忽略 `_index.md`、`_brief-*.md` 和 `_review-*.md`。

检查内容包括：

- PRD 路径是否符合 `requirements/YYYY-MM/<module>/<feature>.md`；
- 是否有 front matter；
- `type` 是否为 `prd`；
- `status` 是否为 `draft` / `review` / `approved` / `deprecated`；
- 是否有 `brief_path`，且对应 brief 是否存在；
- `brief_status` 是否为 `confirmed` / `skipped_questions_confirmed`；
- `source_files` 是否存在且指向有效仓库路径；
- `open_gap_refs` 是否能在 `knowledge-base/changelog/knowledge-gaps.md` 中找到；
- PRD 正文是否包含标准模板第 0–10 章；
- `review` / `approved` 状态是否已有 `_review-<feature>.md`。

用法：

```bash
python3 tools/validate_prd.py
python3 tools/validate_prd.py requirements/2026-05/card/card-transaction-detail.md
python3 tools/validate_prd.py requirements/2026-05/card/
```

## extract_docx_tables.py

表格编号使用从 0 开始的索引，与 `python-docx` 的 `document.tables` 顺序一致。

用法：

```bash
# 提取所有表格为 Markdown 并输出到 stdout
python3 tools/extract_docx_tables.py archive/historical-prd/card/source.docx

# 提取指定表格为 Markdown
python3 tools/extract_docx_tables.py archive/historical-prd/card/source.docx --tables 0,2-4 --out tmp/tables.md

# 提取单个表格为 CSV
python3 tools/extract_docx_tables.py archive/historical-prd/card/source.docx --tables 5 --format csv --out tmp/table-5.csv
```
