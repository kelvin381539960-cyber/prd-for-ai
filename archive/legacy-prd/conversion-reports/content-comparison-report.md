# Converted PRD Content Comparison Report

更新时间：2026-05-09

## 结论

本次对 23 份原始 Word PRD 与对应 Markdown README 做了自动化正文覆盖比对，并对自动比对剩余的疑似缺失项逐条人工复核。

- 未发现实际需求正文丢失。
- 图片引用完整性已在 `VALIDATION_REPORT.md` 中校验，缺失为 0。
- 本次比对没有发现 Word 文本框、批注引用需要额外迁移。
- 仍需注意：Markdown 无法 100% 等价还原 Word 的视觉排版、浮动对象、页眉页脚、水印、修订记录展示方式等。

## 比对方法

1. 使用 mammoth 从原始 `.docx` 提取原始正文。
2. 读取转换后的 `archive/legacy-prd/**/README.md`。
3. 对两边文本做归一化处理：去除 Markdown 标记、HTML 标签、HTML entity、空白差异、部分中英文标点差异。
4. 按原始 docx 段落逐段检查是否被 Markdown 覆盖。
5. 对自动比对剩余的疑似缺失项进行人工搜索复核。

## 汇总

| 指标 | 数量 |
|---|---:|
| 文档数 | 23 |
| 原始正文段落总数 | 7264 |
| 自动比对后疑似缺失段落 | 6 |
| 人工复核后确认真实正文缺失 | 0 |
| 含 /tmp 绝对路径 | 0 |
| 发现文本框引用 | 0 |
| 发现批注引用 | 0 |

## 逐文档结果

| # | 源文件 | 段落数 | 自动疑似缺失 | 人工结论 | 表格 | 图片引用 |
|---:|---|---:|---:|---|---:|---:|
| 1 | `archive/historical-prd/card/AIX Card 注册登录需求V1.0 (2).docx` | 373 | 0 | 通过 | 24 | 43 |
| 2 | `archive/historical-prd/app/AIX APP V1.0【Home】.docx` | 271 | 2 | 已复核，非真实缺失 | 13 | 47 |
| 3 | `archive/historical-prd/app/AIX APP V1.0 【FAQ】.docx` | 103 | 0 | 通过 | 3 | 29 |
| 4 | `archive/historical-prd/app/AIX APP V1.0【Transaction & History】 (1).docx` | 361 | 1 | 已复核，非真实缺失 | 15 | 66 |
| 5 | `archive/historical-prd/card/AIX Card V1.0【Application】.docx` | 532 | 1 | 已复核，非真实缺失 | 12 | 62 |
| 6 | `archive/historical-prd/card/AIX Card ME模块需求V1.0 (1).docx` | 227 | 0 | 通过 | 21 | 25 |
| 7 | `archive/historical-prd/card/AIX Card 【manage】模块需求V1.0 .docx` | 318 | 0 | 通过 | 32 | 33 |
| 8 | `archive/historical-prd/card/AIX Card交易【transaction】.docx` | 77 | 0 | 通过 | 10 | 2 |
| 9 | `archive/historical-prd/common/[2025-11-27] AIX+PopUp+banner等能力接入【首页+MGM页面】.docx` | 252 | 0 | 通过 | 5 | 20 |
| 10 | `archive/historical-prd/common/[2026-03-09]AIX+多语言翻译逻辑.docx` | 18 | 0 | 通过 | 1 | 2 |
| 11 | `archive/historical-prd/kyc/AIX WALLET 钱包开户KYC需求V1.0 (1).docx` | 429 | 0 | 通过 | 28 | 28 |
| 12 | `archive/historical-prd/mgm/[2026-03-31]AIX-MGM及邀请码.docx` | 519 | 0 | 通过 | 8 | 31 |
| 13 | `archive/historical-prd/notification/[2025-11-25] AIX+Notification（push及站内信）.docx` | 408 | 0 | 通过 | 32 | 159 |
| 14 | `archive/historical-prd/notification/[2026-03-12]AIX+系统邮件.docx` | 30 | 0 | 通过 | 1 | 2 |
| 15 | `archive/historical-prd/oboss/[AIX]OBOSS MVP.docx` | 722 | 0 | 通过 | 23 | 33 |
| 16 | `archive/historical-prd/oboss/[2026-04-14]AIX-Oboss能力.docx` | 420 | 0 | 通过 | 11 | 55 |
| 17 | `archive/historical-prd/security/AIX Security 身份认证需求V1.0 (1).docx` | 379 | 0 | 通过 | 49 | 19 |
| 18 | `archive/historical-prd/wallet/AIX Wallet V1.0【Asset】.docx` | 124 | 0 | 通过 | 5 | 7 |
| 19 | `archive/historical-prd/wallet/AIX Wallet V1.0【Deposit & Send & Swap 】.docx` | 593 | 0 | 通过 | 22 | 74 |
| 20 | `archive/historical-prd/website/[2025-11-05]AIX-官网需求一期.docx` | 435 | 0 | 通过 | 12 | 65 |
| 21 | `archive/historical-prd/website/[2025-11-20]AIX-外部投放waitlist.docx` | 197 | 1 | 已复核，非真实缺失 | 3 | 3 |
| 22 | `archive/historical-prd/website/[2026-01-04]AIX官网增加waitlist .docx` | 54 | 1 | 已复核，非真实缺失 | 2 | 7 |
| 23 | `archive/historical-prd/website/[2026-04-02]AIX-官网需求二期.docx` | 422 | 0 | 通过 | 11 | 57 |

## 自动疑似缺失项复核

- #2：两个申卡入口规则段落在 README 中存在；误判由 HTML entity `&lt;`、中文/英文符号空格及 `<strong>` 标签导致。
- #4：Lark 文件夹链接在 README 中以自动链接 `<https://...>` 形式存在；误判由链接格式导致。
- #5：常驻申卡入口规则段落在 README 中存在；误判由 HTML entity `&lt;` 和标签/空格差异导致。
- #21：`详见：[BRD] Aix Waitlist` 在 README 中存在；误判由链接文本空格和 Markdown 链接转义导致。
- #22：`详见：[BRD] Aix Waitlist` 在 README 中存在；误判由链接文本空格和 Markdown 链接转义导致。

## 已知边界

- Word 中的视觉排版、浮动图片位置、页眉页脚、分页、水印、字体字号、颜色等不会在 Markdown 中完全等价。
- 部分大图曾转换为 JPEG 压缩版以便落库，因此图片像素级原样保真不作为本次 Markdown 转换目标。
- Word 表格在 Pandoc 输出中多以 HTML table 保留，适合 GitHub 渲染，但纯文本编辑器中可读性会下降。
- 本报告验证的是“需求文字正文是否可在 Markdown 中找到”，不是 Word 视觉版式 1:1 还原。
