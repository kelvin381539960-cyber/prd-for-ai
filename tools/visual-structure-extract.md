# Visual Structure Extractor

`tools/visual_structure_extract.py` 是图片结构提取工具，用于把流程图、UI 截图、普通图片转成可校对的证据材料。

它不直接生成 PRD，不直接认定业务事实。

## 适用范围

| 场景 | 能力 | 结果可信度 |
|---|---|---|
| 流程图 | OCR 文本、流程节点候选、连线候选、确认模板 | 需要人工确认 |
| UI 页面截图 | OCR 文本、版面区域、覆盖图 | 需要人工归属到页面区域 |
| 普通图片 | OCR 文本块、坐标、覆盖图 | 需要人工确认 |

## 不适用范围

- 自动完整还原业务流程。
- 自动判断箭头方向和分支条件。
- 自动生成 PRD 正文。
- 替代人工确认。

## 环境安装

当前稳定路径固定为 PaddleOCR 2.x + PP-Structure 2.x。

```bash
pip install -r tools/requirements-visual.txt
```

检查环境：

```bash
python3 tools/visual_structure_extract.py --check-env
```

如果安装到 PaddleOCR 3.x，脚本会提示不支持。PaddleOCR 3.x 的 API 和 PP-Structure 入口与 2.x 不同，需要单独适配。

## 流程图解析

```bash
python3 tools/visual_structure_extract.py \
  knowledge-base/kyc/_assets/account-opening/image4.jpeg \
  --mode flowchart \
  --out tmp/flowchart-image4 \
  --ocr paddle \
  --structure ppstructure \
  --detect-flow-nodes \
  --detect-connectors
```

输出：

| 文件 | 用途 |
|---|---|
| `review.md` | 人工校对入口 |
| `review_overlay.png` | OCR / 区域 / 节点覆盖图 |
| `text_blocks.csv` | OCR 文本块 |
| `regions.csv` | PP-Structure 区域 |
| `flow_nodes.csv` | 流程节点候选 |
| `connectors.csv` | 连线候选 |
| `confirmation_template.csv` | 人工确认模板 |
| `connectors_overlay.png` | 连线候选覆盖图 |

## PRD 写入规则

PRD 只能使用人工确认后的结果。

流程：

```text
原图
→ visual_structure_extract.py 输出候选材料
→ 人工确认 confirmation_template.csv
→ 形成确认版节点-连线表
→ 再写 PRD 的业务流程 / 时序图
```

`text_blocks.csv`、`flow_nodes.csv`、`connectors.csv` 只是候选材料，不是事实来源。

## UI 页面截图解析

```bash
python3 tools/visual_structure_extract.py page.png \
  --mode ui \
  --out tmp/ui-page \
  --ocr paddle \
  --structure ppstructure
```

UI 解析只能辅助提取页面文案和区域，不能自动判断页面逻辑。页面说明仍需按照 PRD 模板的“左图右说明”和“页面级层级归属”规则人工整理。

## 通用图片 OCR

```bash
python3 tools/visual_structure_extract.py image.png \
  --mode general \
  --out tmp/general-image \
  --ocr paddle
```

## 质量门槛

用于 PRD 前，必须确认：

- 节点文字是否与原图一致。
- 是否漏节点。
- 连线方向是否正确。
- 分支条件是否正确。
- 状态 / 页面 / 弹窗 / 拦截归属是否正确。
- 所有 `confirmed=false` 的行都不能写入 PRD。
