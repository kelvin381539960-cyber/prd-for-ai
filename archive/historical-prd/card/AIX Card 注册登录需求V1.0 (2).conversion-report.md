# AIX Card 注册登录需求V1.0 (2) 转换报告

- 源文件：`archive/historical-prd/card/AIX Card 注册登录需求V1.0 (2).docx`
- Markdown 输出：`archive/historical-prd/card/AIX Card 注册登录需求V1.0 (2).md`
- 图片目录：`archive/historical-prd/card/assets/aix-card-registration-login-v1-0-2/`
- 原始 docx：未删除、未修改
- 转换工具：mammoth convertToMarkdown（当前执行环境未安装 Pandoc）

## 转换结果

- Markdown 文件大小：34,746 bytes
- Markdown 图片引用数：43
- 已写入仓库图片数：43
- 图片总大小：8,587,234 bytes
- Markdown 标题数：21
- Markdown 表格样式行数：0
- 本地转换时图片引用缺失数：0

## 写入情况

已写入以下文件：

- `archive/historical-prd/card/AIX Card 注册登录需求V1.0 (2).md`
- `archive/historical-prd/card/AIX Card 注册登录需求V1.0 (2).conversion-report.md`
- `archive/historical-prd/card/assets/aix-card-registration-login-v1-0-2/image01.png` ~ `image43.png/jpg`

## 校验结论

- Markdown 文件已生成。
- 43 张图片已全部提取并写入仓库。
- Markdown 中图片路径使用相对路径：`assets/aix-card-registration-login-v1-0-2/...`。
- 原始 Word 文件保留不动。

## 转换告警

转换工具返回以下样式告警，表示 Word 中存在未定义/未识别的段落样式；这通常不会导致正文丢失，但可能导致标题层级、样式、缩进无法完全还原：

- Paragraph style with ID 1 was referenced but not defined in the document
- Paragraph style with ID 2 was referenced but not defined in the document
- Paragraph style with ID 7 was referenced but not defined in the document
- Paragraph style with ID 3 was referenced but not defined in the document
- Paragraph style with ID 8 was referenced but not defined in the document
- Paragraph style with ID 9 was referenced but not defined in the document
- Paragraph style with ID 4 was referenced but not defined in the document
- Unrecognised paragraph style: 'null' (Style ID: 1)
- Unrecognised paragraph style: 'null' (Style ID: 2)
- Unrecognised paragraph style: 'null' (Style ID: 7)
- Unrecognised paragraph style: 'null' (Style ID: 3)
- Unrecognised paragraph style: 'null' (Style ID: 8)
- Unrecognised paragraph style: 'null' (Style ID: 9)
- Unrecognised paragraph style: 'null' (Style ID: 4)

## 已知风险

- Word 的浮动图、文本框、SmartArt、批注、修订、页眉页脚、水印等无法保证在 Markdown 中等价保留。
- 复杂表格可能被转换为段落或简化结构，需要人工抽检。
- 本次转换适合作为“历史 PRD 转 Markdown”的试转样本，用于检查正文结构、图片显示和可读性。