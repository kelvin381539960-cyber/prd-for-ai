# AIX Card 注册登录需求V1.0 (2) Pandoc 转换报告

- 源文件：`archive/historical-prd/card/AIX Card 注册登录需求V1.0 (2).docx`
- Pandoc Markdown 输出：`archive/historical-prd/card/AIX Card 注册登录需求V1.0 (2).pandoc.md`
- Pandoc 图片目录：`archive/historical-prd/card/assets/aix-card-registration-login-v1-0-2-pandoc/media/`
- 原始 docx：未删除、未修改
- 转换工具：Pandoc 3.8.2.1
- 转换命令：`pandoc reg.docx -f docx -t gfm --extract-media=assets/aix-card-registration-login-v1-0-2-pandoc --wrap=none --markdown-headings=atx -o "AIX Card 注册登录需求V1.0 (2).pandoc.md"`

## 转换结果

- Markdown 文件大小：47702 bytes
- docx 表格数：24
- Pandoc HTML 表格数：21
- Pandoc Markdown 表格行数：15
- docx drawing 数：43
- Pandoc 图片引用数（HTML img）：43
- Pandoc 普通 Markdown 图片引用数：0
- Pandoc 唯一图片文件数：41
- Pandoc 图片总大小：8500119 bytes
- 图片引用缺失数：0
- 链接数量：HTML 链接 10 + Markdown 链接 9
- Pandoc 转换 stderr 告警：无

## 与上一版 mammoth 转换对比

| 项目 | mammoth 版 | Pandoc 版 |
|---|---:|---:|
| Markdown 文件大小 | 34,746 bytes | 47702 bytes |
| 图片引用 | 43 个 Markdown 图片 | 43 个 HTML img |
| 图片文件 | 43 个 | 41 个唯一文件（重复图片复用） |
| 表格保留 | 基本扁平化为段落 | 21 个 HTML 表格 + 若干 Markdown 表格行 |
| 标题层级 | 通过后处理补了部分标题 | 通过后处理补了部分标题，表格内标题保留在表格中 |
| 适合用途 | 搜索、纯文本阅读 | 更适合保留 Word 表格版式 |

## 校验结论

- Pandoc 版明显比 mammoth 版更好地保留了 Word 表格结构。
- 图片引用本地校验通过：通过。
- 关键章节和关键需求短语均可在 Markdown 中命中。
- 自动文本比对中的少量“疑似缺失”主要来自 HTML entity、删除线、表格标签和 Markdown 转义差异；抽样复核后，未发现实际需求正文丢失。

## 注意事项

- Pandoc 为了保留复杂表格，生成了大量 HTML table；GitHub 可以渲染，但纯 Markdown 编辑器显示会比较重。
- Pandoc 使用 HTML `<img>` 标签来保留图片尺寸，而不是 `![]()` 语法。
- 一些被 Word 标记为删除线的内容会以 `<del>...</del>` 或 `~~...~~` 形式保留；这属于信息保留，不是丢失。
- 图片引用数为 43，但唯一图片文件数为 41，原因是重复图片被 Pandoc 复用到同一个文件。

## 重复图片引用

- assets/aix-card-registration-login-v1-0-2-pandoc/media/image23.png
- assets/aix-card-registration-login-v1-0-2-pandoc/media/image31.png
