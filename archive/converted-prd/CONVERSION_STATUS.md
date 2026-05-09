# 历史 PRD 转 Markdown 任务表

更新时间：2026-05-09

## 状态说明

| 状态 | 含义 |
|---|---|
| DONE | 已完成转换、图片落库、路径校验、过程文件清理 |
| TODO | 待转换 |
| IN_PROGRESS | 正在转换中 |
| BLOCKED | 转换受阻，需要处理 |

## 转换规则

- 原始文件统一保留在 `archive/historical-prd/`，不移动、不删除。
- 转换后的 Markdown 统一放在 `archive/converted-prd/<domain>/<slug>/README.md`。
- 图片统一放在对应目录的 `assets/media/`。
- 默认使用 Pandoc 转换，优先保留 Word 表格结构。
- 转换完成后清理历史目录下的试转 `.md`、报告、临时 assets 目录。
- 每份文档完成后更新本表状态，避免遗漏。

## 任务总览

| 序号 | 状态 | 源文件 | 目标目录 | 备注 |
|---:|---|---|---|---|
| 1 | DONE | `archive/historical-prd/card/AIX Card 注册登录需求V1.0 (2).docx` | `archive/converted-prd/app/registration-login/` | 已完成；43 个图片引用，41 个唯一图片文件，0 缺失；表格保留为 HTML table |
| 2 | DONE | `archive/historical-prd/app/AIX APP V1.0【Home】.docx` | `archive/converted-prd/app/home/` | 已完成；图片引用 47，图片文件 47，缺失 0；HTML 表格 8 |
| 3 | DONE | `archive/historical-prd/app/AIX APP V1.0 【FAQ】.docx` | `archive/converted-prd/app/faq/` | 已完成；图片引用 29，图片文件 18，缺失 0；HTML 表格 3 |
| 4 | DONE | `archive/historical-prd/app/AIX APP V1.0【Transaction & History】 (1).docx` | `archive/converted-prd/app/transaction-history/` | 已完成；图片引用 66，图片文件 63，缺失 0；HTML 表格 11 |
| 5 | DONE | `archive/historical-prd/card/AIX Card V1.0【Application】.docx` | `archive/converted-prd/card/application/` | 已完成；图片引用 62，图片文件 61，缺失 0；HTML 表格 6 |
| 6 | DONE | `archive/historical-prd/card/AIX Card ME模块需求V1.0 (1).docx` | `archive/converted-prd/card/me/` | 已完成；图片引用 25，图片文件 25，缺失 0；HTML 表格 18 |
| 7 | DONE | `archive/historical-prd/card/AIX Card 【manage】模块需求V1.0 .docx` | `archive/converted-prd/card/manage/` | 已完成；图片引用 33，图片文件 32，缺失 0；HTML 表格 29 |
| 8 | DONE | `archive/historical-prd/card/AIX Card交易【transaction】.docx` | `archive/converted-prd/card/transaction/` | 已完成；图片引用 2，图片文件 2，缺失 0；HTML 表格 5 |
| 9 | DONE | `archive/historical-prd/common/[2025-11-27] AIX+PopUp+banner等能力接入【首页+MGM页面】.docx` | `archive/converted-prd/common/popup-banner/` | 已完成；图片引用 20，图片文件 20，缺失 0；HTML 表格 4 |
| 10 | DONE | `archive/historical-prd/common/[2026-03-09]AIX+多语言翻译逻辑.docx` | `archive/converted-prd/common/i18n/` | 已完成；图片引用 2，图片文件 2，缺失 0；HTML 表格 0 |
| 11 | DONE | `archive/historical-prd/kyc/AIX WALLET 钱包开户KYC需求V1.0 (1).docx` | `archive/converted-prd/kyc/wallet-opening/` | 已完成；图片引用 28，图片文件 27，缺失 0；HTML 表格 22 |
| 12 | TODO | `archive/historical-prd/mgm/[2026-03-31]AIX-MGM及邀请码.docx` | `archive/converted-prd/mgm/referral-invite-code/` |  |
| 13 | DONE | `archive/historical-prd/notification/[2025-11-25] AIX+Notification（push及站内信）.docx` | `archive/converted-prd/notification/push-inbox/` | 已完成；图片引用 159，图片文件 83，缺失 0；HTML 表格 25 |
| 14 | DONE | `archive/historical-prd/notification/[2026-03-12]AIX+系统邮件.docx` | `archive/converted-prd/notification/system-email/` | 已完成；图片引用 2，图片文件 2，缺失 0；HTML 表格 0 |
| 15 | TODO | `archive/historical-prd/oboss/[AIX]OBOSS MVP.docx` | `archive/converted-prd/oboss/mvp/` |  |
| 16 | TODO | `archive/historical-prd/oboss/[2026-04-14]AIX-Oboss能力.docx` | `archive/converted-prd/oboss/capabilities/` | 源文件较大，转换后需重点检查图片和表格 |
| 17 | DONE | `archive/historical-prd/security/AIX Security 身份认证需求V1.0 (1).docx` | `archive/converted-prd/security/identity-verification/` | 已完成；图片引用 19，图片文件 19，缺失 0；HTML 表格 38 |
| 18 | DONE | `archive/historical-prd/wallet/AIX Wallet V1.0【Asset】.docx` | `archive/converted-prd/wallet/asset/` | 已完成；图片引用 7，图片文件 7，缺失 0；HTML 表格 2 |
| 19 | TODO | `archive/historical-prd/wallet/AIX Wallet V1.0【Deposit & Send & Swap 】.docx` | `archive/converted-prd/wallet/deposit-send-swap/` |  |
| 20 | TODO | `archive/historical-prd/website/[2025-11-05]AIX-官网需求一期.docx` | `archive/converted-prd/website/phase-1/` | 源文件较大，转换后需重点检查图片和表格 |
| 21 | TODO | `archive/historical-prd/website/[2025-11-20]AIX-外部投放waitlist.docx` | `archive/converted-prd/website/waitlist-campaign/` | 源文件较大，转换后需重点检查图片和表格 |
| 22 | TODO | `archive/historical-prd/website/[2026-01-04]AIX官网增加waitlist .docx` | `archive/converted-prd/website/waitlist-addition/` | 源文件较大，转换后需重点检查图片和表格 |
| 23 | TODO | `archive/historical-prd/website/[2026-04-02]AIX-官网需求二期.docx` | `archive/converted-prd/website/phase-2/` | 源文件较大，转换后需重点检查图片和表格 |

## 执行顺序建议

1. 先转换中小文件，验证批量流程稳定性。
2. 再转换 10MB 以上的大文件。
3. 最后转换 30MB 以上的大文件：官网一期、官网二期、OBOSS 能力。

## 当前进度

| 指标 | 数量 |
|---|---:|
| 历史 docx 总数 | 23 |
| 已完成 | 15 |
| 待转换 | 8 |
| 受阻 | 0 |
