---
module: changelog
feature: prd-page-visual-coverage
version: "1.7"
status: active
source_doc: archive/converted-prd/**/README.md
source_section: image references and page-like units
last_updated: 2026-05-09
owner: 吴忆锋
---

# PRD Page Visual Coverage Audit 页面图片覆盖审计

## 1. 目的

本文件用于审计 converted-prd 中的页面截图 / 页面视觉素材，是否已经绑定到 knowledge-base 中对应页面规则位置。

## 2. 当前统计

| 项目 | 数量 |
|---|---:|
| converted-prd 图片引用总数 | 869 |
| 初步识别为页面 / 页面组视觉 | 579 |
| 已绑定到 KB 的页面图（按自动审计口径） | 331 |
| 支撑图 / 流程图 / 接口图 / 数据字典图，已转 supporting-visuals index | 290 |
| Non-runtime visual indexed | 245 |
| 删除线来源，不绑定 runtime | 3 |
| 仍需复核 | 0 |

## 3. 已绑定目标文件

| 批次 | KB 文件 | 图片数 |
|---|---|---:|
| 第一轮 | knowledge-base/common/faq.md | 26 |
| 第一轮 | knowledge-base/home/app-home.md | 21 |
| 第一轮 | knowledge-base/account/login.md | 22 |
| 第一轮 | knowledge-base/account/registration.md | 1 |
| 第一轮 | knowledge-base/transaction/history.md | 17 |
| 第一轮 | knowledge-base/transaction/detail.md | 12 |
| 第一轮 | knowledge-base/card/application.md | 36 |
| 第一轮 | knowledge-base/card/manage/pin.md | 7 |
| 第一轮 | knowledge-base/card/manage/_index.md | 21 |
| 第一轮 | knowledge-base/card/transaction.md | 1 |
| 第一轮 | knowledge-base/kyc/account-opening.md | 19 |
| 第一轮 | knowledge-base/common/notification.md | 15 |
| 第一轮 | knowledge-base/wallet/assets.md | 5 |
| 第一轮 | knowledge-base/wallet/deposit.md | 33 |
| 第一轮 | knowledge-base/wallet/send.md | 4 |
| 第一轮 | knowledge-base/wallet/swap.md | 9 |
| 第二轮 | knowledge-base/account/login.md | 7 |
| 第二轮 | knowledge-base/card/application.md | 13 |
| 第二轮 | knowledge-base/kyc/account-opening.md | 3 |
| 第二轮 | knowledge-base/common/notification.md | 3 |
| 第二轮 | knowledge-base/security/global-rules.md | 9 |
| 第二轮 | knowledge-base/security/otp-verification.md | 1 |
| 第二轮 | knowledge-base/security/face-authentication.md | 4 |
| 第二轮 | knowledge-base/wallet/deposit.md | 14 |

## 4. 绑定规则

1. 页面截图放在对应 KB 文件的 `Page Visuals 页面图索引` 或 `Additional Page Visuals 补充页面图` 中，按页面名分组。
2. 图片使用相对链接引用 `archive/converted-prd` 原始资产，避免重复复制。
3. 删除线页面不进入 runtime 规则，只可登记为 deleted / out_of_scope。
4. Website / OBoss / MGM / Popup Banner / Card Me 等当前没有 runtime KB 承接文件的页面，已承接到 `knowledge-base/non-runtime/`，状态为 visual-only，不混入已有业务事实文件。

## 5. 页面图片覆盖清单（自动识别）

| # | Module | Evidence image | Inferred page | KB target | Kind | Status |
|---:|---|---|---|---|---|---|
| 1 | common/faq | `archive/converted-prd/app/faq/assets/media/image1.png` | 3. 功能需求 | knowledge-base/common/faq.md | PAGE_VISUAL | BOUND_TO_KB |
| 2 | common/faq | `archive/converted-prd/app/faq/assets/media/image2.png` | 3. 功能需求 | knowledge-base/common/faq.md | PAGE_VISUAL | BOUND_TO_KB |
| 3 | common/faq | `archive/converted-prd/app/faq/assets/media/image3.png` | 3. 功能需求 | knowledge-base/common/faq.md | PAGE_VISUAL | BOUND_TO_KB |
| 4 | common/faq | `archive/converted-prd/app/faq/assets/media/image4.png` | Virtual Card  | knowledge-base/common/faq.md | PAGE_VISUAL | BOUND_TO_KB |
| 5 | common/faq | `archive/converted-prd/app/faq/assets/media/image5.png` | Physical Card  | knowledge-base/common/faq.md | PAGE_VISUAL | BOUND_TO_KB |
| 6 | common/faq | `archive/converted-prd/app/faq/assets/media/image2.png` | Physical Card  | knowledge-base/common/faq.md | PAGE_VISUAL | BOUND_TO_KB |
| 7 | common/faq | `archive/converted-prd/app/faq/assets/media/image6.png` | Physical Card  | knowledge-base/common/faq.md | PAGE_VISUAL | BOUND_TO_KB |
| 8 | common/faq | `archive/converted-prd/app/faq/assets/media/image7.png` | Select Crypto  | knowledge-base/common/faq.md | PAGE_VISUAL | BOUND_TO_KB |
| 9 | common/faq | `archive/converted-prd/app/faq/assets/media/image2.png` | Select Crypto  | knowledge-base/common/faq.md | PAGE_VISUAL | BOUND_TO_KB |
| 10 | common/faq | `archive/converted-prd/app/faq/assets/media/image7.png` | Card home  | knowledge-base/common/faq.md | PAGE_VISUAL | BOUND_TO_KB |
| 11 | common/faq | `archive/converted-prd/app/faq/assets/media/image2.png` | Card home  | knowledge-base/common/faq.md | PAGE_VISUAL | BOUND_TO_KB |
| 12 | common/faq | `archive/converted-prd/app/faq/assets/media/image8.png` | Bind Google Wallet  | knowledge-base/common/faq.md | PAGE_VISUAL | BOUND_TO_KB |
| 13 | common/faq | `archive/converted-prd/app/faq/assets/media/image2.png` | Bind Google Wallet  | knowledge-base/common/faq.md | PAGE_VISUAL | BOUND_TO_KB |
| 14 | common/faq | `archive/converted-prd/app/faq/assets/media/image9.png` | Update Phone  | knowledge-base/common/faq.md | PAGE_VISUAL | BOUND_TO_KB |
| 15 | common/faq | `archive/converted-prd/app/faq/assets/media/image2.png` | Update Phone  | knowledge-base/common/faq.md | PAGE_VISUAL | BOUND_TO_KB |
| 16 | common/faq | `archive/converted-prd/app/faq/assets/media/image10.png` | All Transactions  | knowledge-base/common/faq.md | PAGE_VISUAL | BOUND_TO_KB |
| 17 | common/faq | `archive/converted-prd/app/faq/assets/media/image2.png` | All Transactions  | knowledge-base/common/faq.md | PAGE_VISUAL | BOUND_TO_KB |
| 18 | common/faq | `archive/converted-prd/app/faq/assets/media/image11.png` | Transaction Details  | knowledge-base/common/faq.md | PAGE_VISUAL | BOUND_TO_KB |
| 19 | common/faq | `archive/converted-prd/app/faq/assets/media/image2.png` | Transaction Details  | knowledge-base/common/faq.md | PAGE_VISUAL | BOUND_TO_KB |
| 20 | common/faq | `archive/converted-prd/app/faq/assets/media/image12.png` | Crypto Send  | knowledge-base/common/faq.md | PAGE_VISUAL | BOUND_TO_KB |
| 21 | common/faq | `archive/converted-prd/app/faq/assets/media/image2.png` | Crypto Send  | knowledge-base/common/faq.md | PAGE_VISUAL | BOUND_TO_KB |
| 22 | common/faq | `archive/converted-prd/app/faq/assets/media/image13.png` | Crypto Swap  | knowledge-base/common/faq.md | PAGE_VISUAL | BOUND_TO_KB |
| 23 | common/faq | `archive/converted-prd/app/faq/assets/media/image2.png` | Crypto Swap  | knowledge-base/common/faq.md | PAGE_VISUAL | BOUND_TO_KB |
| 24 | common/faq | `archive/converted-prd/app/faq/assets/media/image14.png` | Deposit method  | knowledge-base/common/faq.md | PAGE_VISUAL | BOUND_TO_KB |
| 25 | common/faq | `archive/converted-prd/app/faq/assets/media/image2.png` | Deposit method  | knowledge-base/common/faq.md | PAGE_VISUAL | BOUND_TO_KB |
| 26 | common/faq | `archive/converted-prd/app/faq/assets/media/image15.png` | Receive Crypto  | knowledge-base/common/faq.md | PAGE_VISUAL | BOUND_TO_KB |
| 27 | common/faq | `archive/converted-prd/app/faq/assets/media/image16.png` | 4. Chat with us | knowledge-base/common/faq.md | PAGE_VISUAL | DELETED_SOURCE_NOT_BOUND |
| 28 | common/faq | `archive/converted-prd/app/faq/assets/media/image17.png` | 4. Chat with us | knowledge-base/common/faq.md | PAGE_VISUAL | DELETED_SOURCE_NOT_BOUND |
| 29 | common/faq | `archive/converted-prd/app/faq/assets/media/image18.png` | 4. Chat with us | knowledge-base/common/faq.md | PAGE_VISUAL | DELETED_SOURCE_NOT_BOUND |
| 30 | home | `archive/converted-prd/app/home/assets/media/image1.jpeg` | 3. 全局说明 | knowledge-base/home/app-home.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 31 | home | `archive/converted-prd/app/home/assets/media/image2.jpeg` | 4. 整体流程 | knowledge-base/home/app-home.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 32 | home | `archive/converted-prd/app/home/assets/media/image3.jpeg` | 4. 整体流程 | knowledge-base/home/app-home.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 33 | home | `archive/converted-prd/app/home/assets/media/image4.jpeg` | 4. 整体流程 | knowledge-base/home/app-home.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 34 | home | `archive/converted-prd/app/home/assets/media/image5.jpeg` | 4. 整体流程 | knowledge-base/home/app-home.md | PAGE_VISUAL | BOUND_TO_KB |
| 35 | home | `archive/converted-prd/app/home/assets/media/image6.jpeg` | 4. 整体流程 | knowledge-base/home/app-home.md | PAGE_VISUAL | BOUND_TO_KB |
| 36 | home | `archive/converted-prd/app/home/assets/media/image7.jpeg` | 4. 整体流程 | knowledge-base/home/app-home.md | PAGE_VISUAL | BOUND_TO_KB |
| 37 | home | `archive/converted-prd/app/home/assets/media/image8.jpeg` | 4. 整体流程 | knowledge-base/home/app-home.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 38 | home | `archive/converted-prd/app/home/assets/media/image9.jpeg` | 4. 整体流程 | knowledge-base/home/app-home.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 39 | home | `archive/converted-prd/app/home/assets/media/image10.jpeg` | Set Pin | knowledge-base/home/app-home.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 40 | home | `archive/converted-prd/app/home/assets/media/image11.jpeg` | Set Pin | knowledge-base/home/app-home.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 41 | home | `archive/converted-prd/app/home/assets/media/image12.jpeg` | Set Pin | knowledge-base/home/app-home.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 42 | home | `archive/converted-prd/app/home/assets/media/image13.jpeg` | Set Pin | knowledge-base/home/app-home.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 43 | home | `archive/converted-prd/app/home/assets/media/image14.jpeg` | Set Pin | knowledge-base/home/app-home.md | PAGE_VISUAL | BOUND_TO_KB |
| 44 | home | `archive/converted-prd/app/home/assets/media/image15.jpeg` | Set Pin | knowledge-base/home/app-home.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 45 | home | `archive/converted-prd/app/home/assets/media/image16.jpeg` | 4. 整体流程 | knowledge-base/home/app-home.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 46 | home | `archive/converted-prd/app/home/assets/media/image17.jpeg` | 4. 整体流程 | knowledge-base/home/app-home.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 47 | home | `archive/converted-prd/app/home/assets/media/image18.jpeg` | 4. 整体流程 | knowledge-base/home/app-home.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 48 | home | `archive/converted-prd/app/home/assets/media/image19.jpeg` | 4. 整体流程 | knowledge-base/home/app-home.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 49 | home | `archive/converted-prd/app/home/assets/media/image20.jpeg` | 4. 整体流程 | knowledge-base/home/app-home.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 50 | home | `archive/converted-prd/app/home/assets/media/image21.png` | 申卡入口 | knowledge-base/home/app-home.md | PAGE_VISUAL | BOUND_TO_KB |
| 51 | home | `archive/converted-prd/app/home/assets/media/image22.png` | 6. AIX功能需求 | knowledge-base/home/app-home.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 52 | home | `archive/converted-prd/app/home/assets/media/image23.png` | Waitlist | knowledge-base/home/app-home.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 53 | home | `archive/converted-prd/app/home/assets/media/image24.png` | Waitlist | knowledge-base/home/app-home.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 54 | home | `archive/converted-prd/app/home/assets/media/image25.png` | Waitlist | knowledge-base/home/app-home.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 55 | home | `archive/converted-prd/app/home/assets/media/image26.png` | 未申请开通钱包 | knowledge-base/home/app-home.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 56 | home | `archive/converted-prd/app/home/assets/media/image27.png` | 未申请开通钱包 | knowledge-base/home/app-home.md | PAGE_VISUAL | BOUND_TO_KB |
| 57 | home | `archive/converted-prd/app/home/assets/media/image28.png` | 未申请开通钱包 | knowledge-base/home/app-home.md | PAGE_VISUAL | BOUND_TO_KB |
| 58 | home | `archive/converted-prd/app/home/assets/media/image29.png` | 未申请开通钱包 | knowledge-base/home/app-home.md | PAGE_VISUAL | BOUND_TO_KB |
| 59 | home | `archive/converted-prd/app/home/assets/media/image30.png` | 未申请开通钱包 | knowledge-base/home/app-home.md | PAGE_VISUAL | BOUND_TO_KB |
| 60 | home | `archive/converted-prd/app/home/assets/media/image31.png` | 申卡入口 | knowledge-base/home/app-home.md | PAGE_VISUAL | BOUND_TO_KB |
| 61 | home | `archive/converted-prd/app/home/assets/media/image32.png` | 申卡入口 | knowledge-base/home/app-home.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 62 | home | `archive/converted-prd/app/home/assets/media/image33.jpeg` | 申卡入口 | knowledge-base/home/app-home.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 63 | home | `archive/converted-prd/app/home/assets/media/image34.jpeg` | 申卡入口 | knowledge-base/home/app-home.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 64 | home | `archive/converted-prd/app/home/assets/media/image35.png` | 申卡入口 | knowledge-base/home/app-home.md | PAGE_VISUAL | BOUND_TO_KB |
| 65 | home | `archive/converted-prd/app/home/assets/media/image36.png` | 申卡入口 | knowledge-base/home/app-home.md | PAGE_VISUAL | BOUND_TO_KB |
| 66 | home | `archive/converted-prd/app/home/assets/media/image37.png` | 申卡入口 | knowledge-base/home/app-home.md | PAGE_VISUAL | BOUND_TO_KB |
| 67 | home | `archive/converted-prd/app/home/assets/media/image38.png` | 申卡入口 | knowledge-base/home/app-home.md | PAGE_VISUAL | BOUND_TO_KB |
| 68 | home | `archive/converted-prd/app/home/assets/media/image39.png` | 当前卡片展示 | knowledge-base/home/app-home.md | PAGE_VISUAL | BOUND_TO_KB |
| 69 | home | `archive/converted-prd/app/home/assets/media/image40.png` | 当前卡片展示 | knowledge-base/home/app-home.md | PAGE_VISUAL | BOUND_TO_KB |
| 70 | home | `archive/converted-prd/app/home/assets/media/image41.png` | 申卡入口 | knowledge-base/home/app-home.md | PAGE_VISUAL | BOUND_TO_KB |
| 71 | home | `archive/converted-prd/app/home/assets/media/image42.png` | 申卡入口 | knowledge-base/home/app-home.md | PAGE_VISUAL | BOUND_TO_KB |
| 72 | home | `archive/converted-prd/app/home/assets/media/image43.png` | Select Wallet | knowledge-base/home/app-home.md | PAGE_VISUAL | BOUND_TO_KB |
| 73 | home | `archive/converted-prd/app/home/assets/media/image44.png` | Select Wallet | knowledge-base/home/app-home.md | PAGE_VISUAL | BOUND_TO_KB |
| 74 | home | `archive/converted-prd/app/home/assets/media/image45.png` | Select Wallet | knowledge-base/home/app-home.md | PAGE_VISUAL | BOUND_TO_KB |
| 75 | home | `archive/converted-prd/app/home/assets/media/image46.jpeg` | 7. DTC渠道接口需求 | knowledge-base/home/app-home.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 76 | home | `archive/converted-prd/app/home/assets/media/image47.jpeg` | 7. DTC渠道接口需求 | knowledge-base/home/app-home.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 77 | account | `archive/converted-prd/app/registration-login/assets/media/image1.png` | 1. 需求变更日志 | knowledge-base/account/login.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 78 | account | `archive/converted-prd/app/registration-login/assets/media/image2.png` | 1. 需求变更日志 | knowledge-base/account/login.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 79 | account | `archive/converted-prd/app/registration-login/assets/media/image3.png` | 1. 需求变更日志 | knowledge-base/account/login.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 80 | account | `archive/converted-prd/app/registration-login/assets/media/image4.png` | 1. 需求变更日志 | knowledge-base/account/login.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 81 | account | `archive/converted-prd/app/registration-login/assets/media/image5.png` | 1. 需求变更日志 | knowledge-base/account/login.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 82 | account | `archive/converted-prd/app/registration-login/assets/media/image6.png` | 1. 需求变更日志 | knowledge-base/account/login.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 83 | account | `archive/converted-prd/app/registration-login/assets/media/image7.png` | 1. 需求变更日志 | knowledge-base/account/login.md | PAGE_VISUAL | BOUND_TO_KB |
| 84 | account | `archive/converted-prd/app/registration-login/assets/media/image8.png` | 1. 需求变更日志 | knowledge-base/account/login.md | PAGE_VISUAL | BOUND_TO_KB |
| 85 | account | `archive/converted-prd/app/registration-login/assets/media/image9.png` | 1. 需求变更日志 | knowledge-base/account/login.md | PAGE_VISUAL | BOUND_TO_KB |
| 86 | account | `archive/converted-prd/app/registration-login/assets/media/image10.png` | Enable BIO Page | knowledge-base/account/login.md | PAGE_VISUAL | BOUND_TO_KB |
| 87 | account | `archive/converted-prd/app/registration-login/assets/media/image11.png` | 1. 需求变更日志 | knowledge-base/account/login.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 88 | account | `archive/converted-prd/app/registration-login/assets/media/image12.png` | 1. 需求变更日志 | knowledge-base/account/login.md | PAGE_VISUAL | BOUND_TO_KB |
| 89 | account | `archive/converted-prd/app/registration-login/assets/media/image13.png` | 1. 需求变更日志 | knowledge-base/account/login.md | PAGE_VISUAL | BOUND_TO_KB |
| 90 | account | `archive/converted-prd/app/registration-login/assets/media/image14.jpeg` | 4. 功能结构 | knowledge-base/account/login.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 91 | account | `archive/converted-prd/app/registration-login/assets/media/image15.jpeg` | 6. 全局规则 | knowledge-base/account/login.md | PAGE_VISUAL | BOUND_TO_KB |
| 92 | account | `archive/converted-prd/app/registration-login/assets/media/image16.jpeg` | 7. 需求描述 | knowledge-base/account/login.md | PAGE_VISUAL | BOUND_TO_KB |
| 93 | account | `archive/converted-prd/app/registration-login/assets/media/image17.jpeg` | 7. 需求描述 | knowledge-base/account/login.md | PAGE_VISUAL | BOUND_TO_KB |
| 94 | account | `archive/converted-prd/app/registration-login/assets/media/image18.png` | 7. 需求描述 | knowledge-base/account/login.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 95 | account | `archive/converted-prd/app/registration-login/assets/media/image19.png` | 7. 需求描述 | knowledge-base/account/login.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 96 | account | `archive/converted-prd/app/registration-login/assets/media/image20.png` | 7. 需求描述 | knowledge-base/account/login.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 97 | account | `archive/converted-prd/app/registration-login/assets/media/image21.png` | 7. 需求描述 | knowledge-base/account/login.md | PAGE_VISUAL | BOUND_TO_KB |
| 98 | account | `archive/converted-prd/app/registration-login/assets/media/image22.png` | 7. 需求描述 | knowledge-base/account/login.md | PAGE_VISUAL | BOUND_TO_KB |
| 99 | account | `archive/converted-prd/app/registration-login/assets/media/image23.png` | 7. 需求描述 | knowledge-base/account/login.md | PAGE_VISUAL | BOUND_TO_KB |
| 100 | account | `archive/converted-prd/app/registration-login/assets/media/image24.png` | 7. 需求描述 | knowledge-base/account/login.md | PAGE_VISUAL | BOUND_TO_KB |
| 101 | account | `archive/converted-prd/app/registration-login/assets/media/image23.png` | 7. 需求描述 | knowledge-base/account/login.md | PAGE_VISUAL | BOUND_TO_KB |
| 102 | account | `archive/converted-prd/app/registration-login/assets/media/image25.png` | 7. 需求描述 | knowledge-base/account/login.md | PAGE_VISUAL | BOUND_TO_KB |
| 103 | account | `archive/converted-prd/app/registration-login/assets/media/image26.png` | 7. 需求描述 | knowledge-base/account/login.md | PAGE_VISUAL | BOUND_TO_KB |
| 104 | account | `archive/converted-prd/app/registration-login/assets/media/image27.png` | 7. 需求描述 | knowledge-base/account/login.md | PAGE_VISUAL | BOUND_TO_KB |
| 105 | account | `archive/converted-prd/app/registration-login/assets/media/image28.jpeg` | Login Page | knowledge-base/account/login.md | PAGE_VISUAL | BOUND_TO_KB |
| 106 | account | `archive/converted-prd/app/registration-login/assets/media/image29.jpeg` | Login Page | knowledge-base/account/login.md | PAGE_VISUAL | BOUND_TO_KB |
| 107 | account | `archive/converted-prd/app/registration-login/assets/media/image30.png` | 7. 需求描述 | knowledge-base/account/login.md | PAGE_VISUAL | BOUND_TO_KB |
| 108 | account | `archive/converted-prd/app/registration-login/assets/media/image31.png` | Select Country Page | knowledge-base/account/login.md | PAGE_VISUAL | BOUND_TO_KB |
| 109 | account | `archive/converted-prd/app/registration-login/assets/media/image32.png` | 7. 需求描述 | knowledge-base/account/login.md | PAGE_VISUAL | BOUND_TO_KB |
| 110 | account | `archive/converted-prd/app/registration-login/assets/media/image33.jpeg` | 7. 需求描述 | knowledge-base/account/login.md | PAGE_VISUAL | BOUND_TO_KB |
| 111 | account | `archive/converted-prd/app/registration-login/assets/media/image34.jpeg` | 7. 需求描述 | knowledge-base/account/login.md | PAGE_VISUAL | BOUND_TO_KB |
| 112 | account | `archive/converted-prd/app/registration-login/assets/media/image35.png` | 7. 需求描述 | knowledge-base/account/login.md | PAGE_VISUAL | BOUND_TO_KB |
| 113 | account | `archive/converted-prd/app/registration-login/assets/media/image36.jpeg` | 7. 需求描述 | knowledge-base/account/login.md | PAGE_VISUAL | BOUND_TO_KB |
| 114 | account | `archive/converted-prd/app/registration-login/assets/media/image37.jpeg` | 7. 需求描述 | knowledge-base/account/login.md | PAGE_VISUAL | BOUND_TO_KB |
| 115 | account | `archive/converted-prd/app/registration-login/assets/media/image38.png` | 7. 需求描述 | knowledge-base/account/login.md | PAGE_VISUAL | BOUND_TO_KB |
| 116 | account | `archive/converted-prd/app/registration-login/assets/media/image39.png` | 7. 需求描述 | knowledge-base/account/login.md | PAGE_VISUAL | BOUND_TO_KB |
| 117 | account | `archive/converted-prd/app/registration-login/assets/media/image40.jpeg` | set Password Page | knowledge-base/account/registration.md | PAGE_VISUAL | BOUND_TO_KB |
| 118 | account | `archive/converted-prd/app/registration-login/assets/media/image41.jpeg` | 7. 需求描述 | knowledge-base/account/login.md | PAGE_VISUAL | BOUND_TO_KB |
| 119 | account | `archive/converted-prd/app/registration-login/assets/media/image31.png` | Select Country Page | knowledge-base/account/login.md | PAGE_VISUAL | BOUND_TO_KB |
| 120 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image1.jpeg` | 2. 全局说明 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 121 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image2.png` | 3. 状态及类型处理 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 122 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image3.png` | 3. 状态及类型处理 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 123 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image4.jpeg` | 3. 状态及类型处理 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 124 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image5.png` | 4. 数据字典 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 125 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image6.png` | 4. 数据字典 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 126 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image7.png` | 4. 数据字典 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 127 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image8.png` | 4. 数据字典 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 128 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image9.png` | 4. 数据字典 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 129 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image10.png` | 4. 数据字典 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 130 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image11.png` | 5. 映射关系（交易记录） | knowledge-base/transaction/history.md | PAGE_VISUAL | BOUND_TO_KB |
| 131 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image12.jpeg` | 6. 时区显示 | knowledge-base/transaction/history.md | PAGE_VISUAL | BOUND_TO_KB |
| 132 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image13.png` | 7. AIX前端功能需求 | knowledge-base/transaction/history.md | PAGE_VISUAL | BOUND_TO_KB |
| 133 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image14.png` | 7. AIX前端功能需求 | knowledge-base/transaction/history.md | PAGE_VISUAL | BOUND_TO_KB |
| 134 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image15.png` | 7. AIX前端功能需求 | knowledge-base/transaction/history.md | PAGE_VISUAL | BOUND_TO_KB |
| 135 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image16.png` | 7. AIX前端功能需求 | knowledge-base/transaction/history.md | PAGE_VISUAL | BOUND_TO_KB |
| 136 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image17.png` | 7. AIX前端功能需求 | knowledge-base/transaction/history.md | PAGE_VISUAL | BOUND_TO_KB |
| 137 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image18.png` | Card History | knowledge-base/transaction/history.md | PAGE_VISUAL | BOUND_TO_KB |
| 138 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image19.jpeg` | 7. AIX前端功能需求 | knowledge-base/transaction/history.md | PAGE_VISUAL | BOUND_TO_KB |
| 139 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image20.png` | 7. AIX前端功能需求 | knowledge-base/transaction/history.md | PAGE_VISUAL | BOUND_TO_KB |
| 140 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image21.png` | Card History | knowledge-base/transaction/history.md | PAGE_VISUAL | BOUND_TO_KB |
| 141 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image22.png` | Card History | knowledge-base/transaction/history.md | PAGE_VISUAL | BOUND_TO_KB |
| 142 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image23.png` | Card History | knowledge-base/transaction/history.md | PAGE_VISUAL | BOUND_TO_KB |
| 143 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image24.png` | Card History | knowledge-base/transaction/history.md | PAGE_VISUAL | BOUND_TO_KB |
| 144 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image25.png` | Card History | knowledge-base/transaction/history.md | PAGE_VISUAL | BOUND_TO_KB |
| 145 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image26.png` | Transaction Details | knowledge-base/transaction/detail.md | PAGE_VISUAL | BOUND_TO_KB |
| 146 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image27.png` | Transaction Details | knowledge-base/transaction/detail.md | PAGE_VISUAL | BOUND_TO_KB |
| 147 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image28.png` | Transaction Details | knowledge-base/transaction/detail.md | PAGE_VISUAL | BOUND_TO_KB |
| 148 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image29.png` | Transaction Details | knowledge-base/transaction/detail.md | PAGE_VISUAL | BOUND_TO_KB |
| 149 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image30.png` | Transaction Details | knowledge-base/transaction/detail.md | PAGE_VISUAL | BOUND_TO_KB |
| 150 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image31.png` | Transaction Details | knowledge-base/transaction/detail.md | PAGE_VISUAL | BOUND_TO_KB |
| 151 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image32.png` | Transaction Details | knowledge-base/transaction/detail.md | PAGE_VISUAL | BOUND_TO_KB |
| 152 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image33.png` | Transaction Details | knowledge-base/transaction/detail.md | PAGE_VISUAL | BOUND_TO_KB |
| 153 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image34.png` | Transaction Details | knowledge-base/transaction/detail.md | PAGE_VISUAL | BOUND_TO_KB |
| 154 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image35.jpeg` | Transaction Details | knowledge-base/transaction/detail.md | PAGE_VISUAL | BOUND_TO_KB |
| 155 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image36.png` | Transaction Details | knowledge-base/transaction/detail.md | PAGE_VISUAL | BOUND_TO_KB |
| 156 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image37.png` | Transaction Details | knowledge-base/transaction/detail.md | PAGE_VISUAL | BOUND_TO_KB |
| 157 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image38.png` | Swap | knowledge-base/transaction/history.md | PAGE_VISUAL | BOUND_TO_KB |
| 158 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image39.png` | Swap | knowledge-base/transaction/history.md | PAGE_VISUAL | BOUND_TO_KB |
| 159 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image40.png` | Swap | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 160 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image36.png` | Swap | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 161 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image41.jpeg` | 8. DTC渠道接口需求 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 162 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image42.png` | 8. DTC渠道接口需求 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 163 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image43.png` | 8. DTC渠道接口需求 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 164 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image44.png` | 8. DTC渠道接口需求 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 165 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image45.jpeg` | 8. DTC渠道接口需求 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 166 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image46.png` | 8. DTC渠道接口需求 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 167 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image43.png` | 8. DTC渠道接口需求 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 168 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image47.png` | 8. DTC渠道接口需求 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 169 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image43.png` | 8. DTC渠道接口需求 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 170 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image48.jpeg` | 8. DTC渠道接口需求 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 171 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image49.png` | 8. DTC渠道接口需求 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 172 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image50.png` | 8. DTC渠道接口需求 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 173 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image51.png` | 8. DTC渠道接口需求 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 174 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image52.jpeg` | 8. DTC渠道接口需求 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 175 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image53.png` | 8. DTC渠道接口需求 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 176 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image54.png` | 8. DTC渠道接口需求 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 177 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image55.png` | 8. DTC渠道接口需求 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 178 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image56.jpeg` | 8. DTC渠道接口需求 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 179 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image57.png` | 8. DTC渠道接口需求 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 180 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image58.png` | 8. DTC渠道接口需求 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 181 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image59.png` | 8. DTC渠道接口需求 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 182 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image60.jpeg` | 8. DTC渠道接口需求 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 183 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image61.png` | 8. DTC渠道接口需求 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 184 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image62.png` | 8. DTC渠道接口需求 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 185 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image63.png` | 8. DTC渠道接口需求 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 186 | card/application | `archive/converted-prd/card/application/assets/media/image1.jpeg` | 4. Card申请单状态 | knowledge-base/card/application.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 187 | card/application | `archive/converted-prd/card/application/assets/media/image2.jpeg` | 申卡入口 | knowledge-base/card/application.md | PAGE_VISUAL | BOUND_TO_KB |
| 188 | card/application | `archive/converted-prd/card/application/assets/media/image3.png` | 申卡入口 | knowledge-base/card/application.md | PAGE_VISUAL | BOUND_TO_KB |
| 189 | card/application | `archive/converted-prd/card/application/assets/media/image4.png` | 申卡入口 | knowledge-base/card/application.md | PAGE_VISUAL | BOUND_TO_KB |
| 190 | card/application | `archive/converted-prd/card/application/assets/media/image5.png` | 申卡入口 | knowledge-base/card/application.md | PAGE_VISUAL | BOUND_TO_KB |
| 191 | card/application | `archive/converted-prd/card/application/assets/media/image6.png` | 申卡入口 | knowledge-base/card/application.md | PAGE_VISUAL | BOUND_TO_KB |
| 192 | card/application | `archive/converted-prd/card/application/assets/media/image7.png` | 申卡入口 | knowledge-base/card/application.md | PAGE_VISUAL | BOUND_TO_KB |
| 193 | card/application | `archive/converted-prd/card/application/assets/media/image8.png` | 申卡入口 | knowledge-base/card/application.md | PAGE_VISUAL | BOUND_TO_KB |
| 194 | card/application | `archive/converted-prd/card/application/assets/media/image9.png` | 申卡入口 | knowledge-base/card/application.md | PAGE_VISUAL | BOUND_TO_KB |
| 195 | card/application | `archive/converted-prd/card/application/assets/media/image10.png` | 申卡入口 | knowledge-base/card/application.md | PAGE_VISUAL | BOUND_TO_KB |
| 196 | card/application | `archive/converted-prd/card/application/assets/media/image11.png` | 申卡入口 | knowledge-base/card/application.md | PAGE_VISUAL | BOUND_TO_KB |
| 197 | card/application | `archive/converted-prd/card/application/assets/media/image12.png` | 6. AIX前端功能需求 | knowledge-base/card/application.md | PAGE_VISUAL | BOUND_TO_KB |
| 198 | card/application | `archive/converted-prd/card/application/assets/media/image13.png` | 6. AIX前端功能需求 | knowledge-base/card/application.md | PAGE_VISUAL | BOUND_TO_KB |
| 199 | card/application | `archive/converted-prd/card/application/assets/media/image14.png` | 6. AIX前端功能需求 | knowledge-base/card/application.md | PAGE_VISUAL | BOUND_TO_KB |
| 200 | card/application | `archive/converted-prd/card/application/assets/media/image15.png` | 6. AIX前端功能需求 | knowledge-base/card/application.md | PAGE_VISUAL | BOUND_TO_KB |
| 201 | card/application | `archive/converted-prd/card/application/assets/media/image16.png` | 6. AIX前端功能需求 | knowledge-base/card/application.md | PAGE_VISUAL | BOUND_TO_KB |
| 202 | card/application | `archive/converted-prd/card/application/assets/media/image17.png` | Select Crypto | knowledge-base/card/application.md | PAGE_VISUAL | BOUND_TO_KB |
| 203 | card/application | `archive/converted-prd/card/application/assets/media/image18.png` | Select Crypto | knowledge-base/card/application.md | PAGE_VISUAL | BOUND_TO_KB |
| 204 | card/application | `archive/converted-prd/card/application/assets/media/image19.png` | Select Crypto | knowledge-base/card/application.md | PAGE_VISUAL | BOUND_TO_KB |
| 205 | card/application | `archive/converted-prd/card/application/assets/media/image20.png` | 6. AIX前端功能需求 | knowledge-base/card/application.md | PAGE_VISUAL | BOUND_TO_KB |
| 206 | card/application | `archive/converted-prd/card/application/assets/media/image21.png` | 6. AIX前端功能需求 | knowledge-base/card/application.md | PAGE_VISUAL | BOUND_TO_KB |
| 207 | card/application | `archive/converted-prd/card/application/assets/media/image22.png` | 6. AIX前端功能需求 | knowledge-base/card/application.md | PAGE_VISUAL | BOUND_TO_KB |
| 208 | card/application | `archive/converted-prd/card/application/assets/media/image23.png` | 6. AIX前端功能需求 | knowledge-base/card/application.md | PAGE_VISUAL | BOUND_TO_KB |
| 209 | card/application | `archive/converted-prd/card/application/assets/media/image24.png` | 6. AIX前端功能需求 | knowledge-base/card/application.md | PAGE_VISUAL | BOUND_TO_KB |
| 210 | card/application | `archive/converted-prd/card/application/assets/media/image25.png` | 6. AIX前端功能需求 | knowledge-base/card/application.md | PAGE_VISUAL | BOUND_TO_KB |
| 211 | card/application | `archive/converted-prd/card/application/assets/media/image26.png` | 6. AIX前端功能需求 | knowledge-base/card/application.md | PAGE_VISUAL | BOUND_TO_KB |
| 212 | card/application | `archive/converted-prd/card/application/assets/media/image27.png` | 6. AIX前端功能需求 | knowledge-base/card/application.md | PAGE_VISUAL | BOUND_TO_KB |
| 213 | card/application | `archive/converted-prd/card/application/assets/media/image28.png` | 6. AIX前端功能需求 | knowledge-base/card/application.md | PAGE_VISUAL | BOUND_TO_KB |
| 214 | card/application | `archive/converted-prd/card/application/assets/media/image29.png` | 6. AIX前端功能需求 | knowledge-base/card/application.md | PAGE_VISUAL | BOUND_TO_KB |
| 215 | card/application | `archive/converted-prd/card/application/assets/media/image30.png` | 6. AIX前端功能需求 | knowledge-base/card/application.md | PAGE_VISUAL | BOUND_TO_KB |
| 216 | card/application | `archive/converted-prd/card/application/assets/media/image31.png` | 6. AIX前端功能需求 | knowledge-base/card/application.md | PAGE_VISUAL | BOUND_TO_KB |
| 217 | card/application | `archive/converted-prd/card/application/assets/media/image32.png` | 6. AIX前端功能需求 | knowledge-base/card/application.md | PAGE_VISUAL | BOUND_TO_KB |
| 218 | card/application | `archive/converted-prd/card/application/assets/media/image26.png` | 6. AIX前端功能需求 | knowledge-base/card/application.md | PAGE_VISUAL | BOUND_TO_KB |
| 219 | card/application | `archive/converted-prd/card/application/assets/media/image33.png` | 6. AIX前端功能需求 | knowledge-base/card/application.md | PAGE_VISUAL | BOUND_TO_KB |
| 220 | card/application | `archive/converted-prd/card/application/assets/media/image34.png` | 6. AIX前端功能需求 | knowledge-base/card/application.md | PAGE_VISUAL | BOUND_TO_KB |
| 221 | card/application | `archive/converted-prd/card/application/assets/media/image35.png` | 6. AIX前端功能需求 | knowledge-base/card/application.md | PAGE_VISUAL | BOUND_TO_KB |
| 222 | card/application | `archive/converted-prd/card/application/assets/media/image36.png` | 6. AIX前端功能需求 | knowledge-base/card/application.md | PAGE_VISUAL | BOUND_TO_KB |
| 223 | card/application | `archive/converted-prd/card/application/assets/media/image37.png` | 6. AIX前端功能需求 | knowledge-base/card/application.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 224 | card/application | `archive/converted-prd/card/application/assets/media/image38.png` | 6. AIX前端功能需求 | knowledge-base/card/application.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 225 | card/application | `archive/converted-prd/card/application/assets/media/image39.png` | 6. AIX前端功能需求 | knowledge-base/card/application.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 226 | card/application | `archive/converted-prd/card/application/assets/media/image40.png` | 当前卡片展示 | knowledge-base/card/application.md | PAGE_VISUAL | BOUND_TO_KB |
| 227 | card/application | `archive/converted-prd/card/application/assets/media/image41.png` | 当前卡片展示 | knowledge-base/card/application.md | PAGE_VISUAL | BOUND_TO_KB |
| 228 | card/application | `archive/converted-prd/card/application/assets/media/image42.png` | 当前卡片展示 | knowledge-base/card/application.md | PAGE_VISUAL | BOUND_TO_KB |
| 229 | card/application | `archive/converted-prd/card/application/assets/media/image43.png` | Activate Card | knowledge-base/card/application.md | PAGE_VISUAL | BOUND_TO_KB |
| 230 | card/application | `archive/converted-prd/card/application/assets/media/image44.png` | Activate Card | knowledge-base/card/application.md | PAGE_VISUAL | BOUND_TO_KB |
| 231 | card/application | `archive/converted-prd/card/application/assets/media/image45.png` | Activate Card | knowledge-base/card/application.md | PAGE_VISUAL | BOUND_TO_KB |
| 232 | card/application | `archive/converted-prd/card/application/assets/media/image46.png` | Activate Card | knowledge-base/card/application.md | PAGE_VISUAL | BOUND_TO_KB |
| 233 | card/application | `archive/converted-prd/card/application/assets/media/image47.png` | 申卡入口 | knowledge-base/card/application.md | PAGE_VISUAL | BOUND_TO_KB |
| 234 | card/application | `archive/converted-prd/card/application/assets/media/image48.png` | 申卡入口 | knowledge-base/card/application.md | PAGE_VISUAL | BOUND_TO_KB |
| 235 | card/application | `archive/converted-prd/card/application/assets/media/image49.png` | 申卡入口 | knowledge-base/card/application.md | PAGE_VISUAL | BOUND_TO_KB |
| 236 | card/application | `archive/converted-prd/card/application/assets/media/image50.png` | 申卡入口 | knowledge-base/card/application.md | PAGE_VISUAL | BOUND_TO_KB |
| 237 | card/application | `archive/converted-prd/card/application/assets/media/image51.png` | 申卡入口 | knowledge-base/card/application.md | PAGE_VISUAL | BOUND_TO_KB |
| 238 | card/application | `archive/converted-prd/card/application/assets/media/image52.png` | 当前卡片展示 | knowledge-base/card/application.md | PAGE_VISUAL | BOUND_TO_KB |
| 239 | card/application | `archive/converted-prd/card/application/assets/media/image53.png` | 当前卡片展示 | knowledge-base/card/application.md | PAGE_VISUAL | BOUND_TO_KB |
| 240 | card/application | `archive/converted-prd/card/application/assets/media/image54.png` | Activate card | knowledge-base/card/application.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 241 | card/application | `archive/converted-prd/card/application/assets/media/image55.jpeg` | 7. DTC渠道接口需求 | knowledge-base/card/application.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 242 | card/application | `archive/converted-prd/card/application/assets/media/image56.jpeg` | 7. DTC渠道接口需求 | knowledge-base/card/application.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 243 | card/application | `archive/converted-prd/card/application/assets/media/image57.jpeg` | 7. DTC渠道接口需求 | knowledge-base/card/application.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 244 | card/application | `archive/converted-prd/card/application/assets/media/image58.jpeg` | 7. DTC渠道接口需求 | knowledge-base/card/application.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 245 | card/application | `archive/converted-prd/card/application/assets/media/image59.jpeg` | 7. DTC渠道接口需求 | knowledge-base/card/application.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 246 | card/application | `archive/converted-prd/card/application/assets/media/image60.jpeg` | 7. DTC渠道接口需求 | knowledge-base/card/application.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 247 | card/application | `archive/converted-prd/card/application/assets/media/image61.jpeg` | 7. DTC渠道接口需求 | knowledge-base/card/application.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 248 | card/manage | `archive/converted-prd/card/manage/assets/media/image2.png` | set pin | knowledge-base/card/manage/pin.md | PAGE_VISUAL | BOUND_TO_KB |
| 249 | card/manage | `archive/converted-prd/card/manage/assets/media/image3.png` | 1. 需求变更日志 | knowledge-base/card/manage/_index.md | PAGE_VISUAL | BOUND_TO_KB |
| 250 | card/manage | `archive/converted-prd/card/manage/assets/media/image4.jpeg` | 4. 功能结构 | knowledge-base/card/manage/_index.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 251 | card/manage | `archive/converted-prd/card/manage/assets/media/image5.jpeg` | 6. 全局规则 | knowledge-base/card/manage/_index.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 252 | card/manage | `archive/converted-prd/card/manage/assets/media/image6.jpeg` | 6. 全局规则 | knowledge-base/card/manage/_index.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 253 | card/manage | `archive/converted-prd/card/manage/assets/media/image7.jpeg` | 6. 全局规则 | knowledge-base/card/manage/_index.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 254 | card/manage | `archive/converted-prd/card/manage/assets/media/image8.png` | 6. 全局规则 | knowledge-base/card/manage/_index.md | PAGE_VISUAL | BOUND_TO_KB |
| 255 | card/manage | `archive/converted-prd/card/manage/assets/media/image9.png` | 6. 全局规则 | knowledge-base/card/manage/_index.md | PAGE_VISUAL | BOUND_TO_KB |
| 256 | card/manage | `archive/converted-prd/card/manage/assets/media/image10.png` | 6. 全局规则 | knowledge-base/card/manage/_index.md | PAGE_VISUAL | BOUND_TO_KB |
| 257 | card/manage | `archive/converted-prd/card/manage/assets/media/image11.png` | 6. 全局规则 | knowledge-base/card/manage/_index.md | PAGE_VISUAL | BOUND_TO_KB |
| 258 | card/manage | `archive/converted-prd/card/manage/assets/media/image12.jpeg` | Card home | knowledge-base/card/manage/_index.md | PAGE_VISUAL | BOUND_TO_KB |
| 259 | card/manage | `archive/converted-prd/card/manage/assets/media/image13.jpeg` | Card home | knowledge-base/card/manage/_index.md | PAGE_VISUAL | BOUND_TO_KB |
| 260 | card/manage | `archive/converted-prd/card/manage/assets/media/image14.png` | 7. 需求描述 | knowledge-base/card/manage/_index.md | PAGE_VISUAL | BOUND_TO_KB |
| 261 | card/manage | `archive/converted-prd/card/manage/assets/media/image15.png` | 7. 需求描述 | knowledge-base/card/manage/_index.md | PAGE_VISUAL | BOUND_TO_KB |
| 262 | card/manage | `archive/converted-prd/card/manage/assets/media/image16.png` | 7. 需求描述 | knowledge-base/card/manage/_index.md | PAGE_VISUAL | BOUND_TO_KB |
| 263 | card/manage | `archive/converted-prd/card/manage/assets/media/image17.jpeg` | 7. 需求描述 | knowledge-base/card/manage/_index.md | PAGE_VISUAL | BOUND_TO_KB |
| 264 | card/manage | `archive/converted-prd/card/manage/assets/media/image18.png` | 7. 需求描述 | knowledge-base/card/manage/_index.md | PAGE_VISUAL | BOUND_TO_KB |
| 265 | card/manage | `archive/converted-prd/card/manage/assets/media/image19.png` | Card Home | knowledge-base/card/manage/_index.md | PAGE_VISUAL | BOUND_TO_KB |
| 266 | card/manage | `archive/converted-prd/card/manage/assets/media/image20.png` | Card Home | knowledge-base/card/manage/_index.md | PAGE_VISUAL | BOUND_TO_KB |
| 267 | card/manage | `archive/converted-prd/card/manage/assets/media/image21.png` | Card Home | knowledge-base/card/manage/_index.md | PAGE_VISUAL | BOUND_TO_KB |
| 268 | card/manage | `archive/converted-prd/card/manage/assets/media/image22.jpeg` | Set PIN | knowledge-base/card/manage/pin.md | PAGE_VISUAL | BOUND_TO_KB |
| 269 | card/manage | `archive/converted-prd/card/manage/assets/media/image23.jpeg` | Set PIN | knowledge-base/card/manage/pin.md | PAGE_VISUAL | BOUND_TO_KB |
| 270 | card/manage | `archive/converted-prd/card/manage/assets/media/image24.png` | 7. 需求描述 | knowledge-base/card/manage/_index.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 271 | card/manage | `archive/converted-prd/card/manage/assets/media/image25.png` | Set PIN | knowledge-base/card/manage/pin.md | PAGE_VISUAL | BOUND_TO_KB |
| 272 | card/manage | `archive/converted-prd/card/manage/assets/media/image26.png` | Set PIN | knowledge-base/card/manage/pin.md | PAGE_VISUAL | BOUND_TO_KB |
| 273 | card/manage | `archive/converted-prd/card/manage/assets/media/image27.png` | Set PIN | knowledge-base/card/manage/pin.md | PAGE_VISUAL | BOUND_TO_KB |
| 274 | card/manage | `archive/converted-prd/card/manage/assets/media/image19.png` | Set PIN | knowledge-base/card/manage/pin.md | PAGE_VISUAL | BOUND_TO_KB |
| 275 | card/manage | `archive/converted-prd/card/manage/assets/media/image28.png` | 7. 需求描述 | knowledge-base/card/manage/_index.md | PAGE_VISUAL | BOUND_TO_KB |
| 276 | card/manage | `archive/converted-prd/card/manage/assets/media/image29.jpeg` | 7. 需求描述 | knowledge-base/card/manage/_index.md | PAGE_VISUAL | BOUND_TO_KB |
| 277 | card/manage | `archive/converted-prd/card/manage/assets/media/image30.jpeg` | 7. 需求描述 | knowledge-base/card/manage/_index.md | PAGE_VISUAL | BOUND_TO_KB |
| 278 | card/manage | `archive/converted-prd/card/manage/assets/media/image31.png` | Card Home | knowledge-base/card/manage/_index.md | PAGE_VISUAL | BOUND_TO_KB |
| 279 | card/manage | `archive/converted-prd/card/manage/assets/media/image32.jpeg` | 7. 需求描述 | knowledge-base/card/manage/_index.md | PAGE_VISUAL | BOUND_TO_KB |
| 280 | card/manage | `archive/converted-prd/card/manage/assets/media/image33.jpeg` | 7. 需求描述 | knowledge-base/card/manage/_index.md | PAGE_VISUAL | BOUND_TO_KB |
| 281 | other | `archive/converted-prd/card/me/assets/media/image1.png` | 1. 需求变更日志 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 282 | other | `archive/converted-prd/card/me/assets/media/image2.jpeg` | 1. 需求变更日志 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 283 | other | `archive/converted-prd/card/me/assets/media/image3.jpeg` | 4. 功能结构 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 284 | other | `archive/converted-prd/card/me/assets/media/image4.png` | 6. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 285 | other | `archive/converted-prd/card/me/assets/media/image5.png` | 6. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 286 | other | `archive/converted-prd/card/me/assets/media/image6.png` | 6. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 287 | other | `archive/converted-prd/card/me/assets/media/image7.png` | 6. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 288 | other | `archive/converted-prd/card/me/assets/media/image8.png` | 6. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 289 | other | `archive/converted-prd/card/me/assets/media/image9.png` | 6. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 290 | other | `archive/converted-prd/card/me/assets/media/image10.png` | 6. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 291 | other | `archive/converted-prd/card/me/assets/media/image11.png` | 6. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 292 | other | `archive/converted-prd/card/me/assets/media/image12.png` | Set Password Page | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 293 | other | `archive/converted-prd/card/me/assets/media/image13.png` | Set Password Page | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 294 | other | `archive/converted-prd/card/me/assets/media/image14.png` | Set Password Page | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 295 | other | `archive/converted-prd/card/me/assets/media/image15.png` | Re-enter Password Page | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 296 | other | `archive/converted-prd/card/me/assets/media/image16.jpeg` | 6. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 297 | other | `archive/converted-prd/card/me/assets/media/image17.jpeg` | 6. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 298 | other | `archive/converted-prd/card/me/assets/media/image18.jpeg` | 6. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 299 | other | `archive/converted-prd/card/me/assets/media/image19.jpeg` | 6. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 300 | other | `archive/converted-prd/card/me/assets/media/image20.png` | 6. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 301 | other | `archive/converted-prd/card/me/assets/media/image21.png` | 6. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 302 | other | `archive/converted-prd/card/me/assets/media/image22.png` | 6. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 303 | other | `archive/converted-prd/card/me/assets/media/image23.jpeg` | 6. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 304 | other | `archive/converted-prd/card/me/assets/media/image24.png` | 6. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 305 | other | `archive/converted-prd/card/me/assets/media/image25.png` | 6. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 306 | card/transaction | `archive/converted-prd/card/transaction/assets/media/image1.jpeg` | 4. 功能结构 | knowledge-base/card/transaction.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 307 | card/transaction | `archive/converted-prd/card/transaction/assets/media/image2.jpeg` | 7. 需求描述 | knowledge-base/card/transaction.md | PAGE_VISUAL | BOUND_TO_KB |
| 308 | other | `archive/converted-prd/common/i18n/assets/media/image1.jpeg` | 3. 系统交互 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 309 | other | `archive/converted-prd/common/i18n/assets/media/image2.jpeg` | 3. 系统交互 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 310 | other | `archive/converted-prd/common/popup-banner/assets/media/image1.png` | \ 2025-11-27\ AIX+PopUp+banner等能力接入【首页+MGM页面】 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 311 | other | `archive/converted-prd/common/popup-banner/assets/media/image2.png` | \ 2025-11-27\ AIX+PopUp+banner等能力接入【首页+MGM页面】 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 312 | other | `archive/converted-prd/common/popup-banner/assets/media/image3.png` | \ 2025-11-27\ AIX+PopUp+banner等能力接入【首页+MGM页面】 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 313 | other | `archive/converted-prd/common/popup-banner/assets/media/image4.png` | \ 2025-11-27\ AIX+PopUp+banner等能力接入【首页+MGM页面】 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 314 | other | `archive/converted-prd/common/popup-banner/assets/media/image5.png` | \ 2025-11-27\ AIX+PopUp+banner等能力接入【首页+MGM页面】 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 315 | other | `archive/converted-prd/common/popup-banner/assets/media/image6.png` | \ 2025-11-27\ AIX+PopUp+banner等能力接入【首页+MGM页面】 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 316 | other | `archive/converted-prd/common/popup-banner/assets/media/image7.png` | \ 2025-11-27\ AIX+PopUp+banner等能力接入【首页+MGM页面】 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 317 | other | `archive/converted-prd/common/popup-banner/assets/media/image8.png` | \ 2025-11-27\ AIX+PopUp+banner等能力接入【首页+MGM页面】 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 318 | other | `archive/converted-prd/common/popup-banner/assets/media/image9.png` | \ 2025-11-27\ AIX+PopUp+banner等能力接入【首页+MGM页面】 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 319 | other | `archive/converted-prd/common/popup-banner/assets/media/image10.png` | \ 2025-11-27\ AIX+PopUp+banner等能力接入【首页+MGM页面】 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 320 | other | `archive/converted-prd/common/popup-banner/assets/media/image11.png` | \ 2025-11-27\ AIX+PopUp+banner等能力接入【首页+MGM页面】 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 321 | other | `archive/converted-prd/common/popup-banner/assets/media/image12.png` | \ 2025-11-27\ AIX+PopUp+banner等能力接入【首页+MGM页面】 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 322 | other | `archive/converted-prd/common/popup-banner/assets/media/image13.jpeg` | \ 2025-11-27\ AIX+PopUp+banner等能力接入【首页+MGM页面】 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 323 | other | `archive/converted-prd/common/popup-banner/assets/media/image14.png` | \ 2025-11-27\ AIX+PopUp+banner等能力接入【首页+MGM页面】 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 324 | other | `archive/converted-prd/common/popup-banner/assets/media/image15.png` | \ 2025-11-27\ AIX+PopUp+banner等能力接入【首页+MGM页面】 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 325 | other | `archive/converted-prd/common/popup-banner/assets/media/image16.png` | \ 2025-11-27\ AIX+PopUp+banner等能力接入【首页+MGM页面】 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 326 | other | `archive/converted-prd/common/popup-banner/assets/media/image17.png` | \ 2025-11-27\ AIX+PopUp+banner等能力接入【首页+MGM页面】 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 327 | other | `archive/converted-prd/common/popup-banner/assets/media/image18.png` | \ 2025-11-27\ AIX+PopUp+banner等能力接入【首页+MGM页面】 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 328 | other | `archive/converted-prd/common/popup-banner/assets/media/image19.jpeg` | \ 2025-11-27\ AIX+PopUp+banner等能力接入【首页+MGM页面】 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 329 | other | `archive/converted-prd/common/popup-banner/assets/media/image20.png` | \ 2025-11-27\ AIX+PopUp+banner等能力接入【首页+MGM页面】 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 330 | kyc | `archive/converted-prd/kyc/wallet-opening/assets/media/image1.jpeg` | 4. 功能结构 | knowledge-base/kyc/account-opening.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 331 | kyc | `archive/converted-prd/kyc/wallet-opening/assets/media/image2.jpeg` | 6. 统一规则 | knowledge-base/kyc/account-opening.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 332 | kyc | `archive/converted-prd/kyc/wallet-opening/assets/media/image3.jpeg` | 6. 统一规则 | knowledge-base/kyc/account-opening.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 333 | kyc | `archive/converted-prd/kyc/wallet-opening/assets/media/image4.jpeg` | 7. 需求描述 | knowledge-base/kyc/account-opening.md | PAGE_VISUAL | BOUND_TO_KB |
| 334 | kyc | `archive/converted-prd/kyc/wallet-opening/assets/media/image5.jpeg` | 7. 需求描述 | knowledge-base/kyc/account-opening.md | PAGE_VISUAL | BOUND_TO_KB |
| 335 | kyc | `archive/converted-prd/kyc/wallet-opening/assets/media/image6.jpeg` | 7. 需求描述 | knowledge-base/kyc/account-opening.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 336 | kyc | `archive/converted-prd/kyc/wallet-opening/assets/media/image7.png` | 7. 需求描述 | knowledge-base/kyc/account-opening.md | PAGE_VISUAL | BOUND_TO_KB |
| 337 | kyc | `archive/converted-prd/kyc/wallet-opening/assets/media/image8.png` | 7. 需求描述 | knowledge-base/kyc/account-opening.md | PAGE_VISUAL | BOUND_TO_KB |
| 338 | kyc | `archive/converted-prd/kyc/wallet-opening/assets/media/image9.png` | 7. 需求描述 | knowledge-base/kyc/account-opening.md | PAGE_VISUAL | BOUND_TO_KB |
| 339 | kyc | `archive/converted-prd/kyc/wallet-opening/assets/media/image10.png` | Waitlist | knowledge-base/kyc/account-opening.md | PAGE_VISUAL | BOUND_TO_KB |
| 340 | kyc | `archive/converted-prd/kyc/wallet-opening/assets/media/image11.png` | 7. 需求描述 | knowledge-base/kyc/account-opening.md | PAGE_VISUAL | BOUND_TO_KB |
| 341 | kyc | `archive/converted-prd/kyc/wallet-opening/assets/media/image12.png` | 7. 需求描述 | knowledge-base/kyc/account-opening.md | PAGE_VISUAL | BOUND_TO_KB |
| 342 | kyc | `archive/converted-prd/kyc/wallet-opening/assets/media/image13.png` | 7. 需求描述 | knowledge-base/kyc/account-opening.md | PAGE_VISUAL | BOUND_TO_KB |
| 343 | kyc | `archive/converted-prd/kyc/wallet-opening/assets/media/image14.png` | 7. 需求描述 | knowledge-base/kyc/account-opening.md | PAGE_VISUAL | BOUND_TO_KB |
| 344 | kyc | `archive/converted-prd/kyc/wallet-opening/assets/media/image15.png` | 7. 需求描述 | knowledge-base/kyc/account-opening.md | PAGE_VISUAL | BOUND_TO_KB |
| 345 | kyc | `archive/converted-prd/kyc/wallet-opening/assets/media/image16.png` | Verify Page | knowledge-base/kyc/account-opening.md | PAGE_VISUAL | BOUND_TO_KB |
| 346 | kyc | `archive/converted-prd/kyc/wallet-opening/assets/media/image17.png` | Failed Page | knowledge-base/kyc/account-opening.md | PAGE_VISUAL | BOUND_TO_KB |
| 347 | kyc | `archive/converted-prd/kyc/wallet-opening/assets/media/image18.png` | 7. 需求描述 | knowledge-base/kyc/account-opening.md | PAGE_VISUAL | BOUND_TO_KB |
| 348 | kyc | `archive/converted-prd/kyc/wallet-opening/assets/media/image19.png` | Face Loading | knowledge-base/kyc/account-opening.md | PAGE_VISUAL | BOUND_TO_KB |
| 349 | kyc | `archive/converted-prd/kyc/wallet-opening/assets/media/image6.jpeg` | 7. 需求描述 | knowledge-base/kyc/account-opening.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 350 | kyc | `archive/converted-prd/kyc/wallet-opening/assets/media/image20.png` | Face Loading | knowledge-base/kyc/account-opening.md | PAGE_VISUAL | BOUND_TO_KB |
| 351 | kyc | `archive/converted-prd/kyc/wallet-opening/assets/media/image21.png` | 7. 需求描述 | knowledge-base/kyc/account-opening.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 352 | kyc | `archive/converted-prd/kyc/wallet-opening/assets/media/image22.png` | 7. 需求描述 | knowledge-base/kyc/account-opening.md | PAGE_VISUAL | BOUND_TO_KB |
| 353 | kyc | `archive/converted-prd/kyc/wallet-opening/assets/media/image23.jpeg` | 7. 需求描述 | knowledge-base/kyc/account-opening.md | PAGE_VISUAL | BOUND_TO_KB |
| 354 | kyc | `archive/converted-prd/kyc/wallet-opening/assets/media/image24.png` | 7. 需求描述 | knowledge-base/kyc/account-opening.md | PAGE_VISUAL | BOUND_TO_KB |
| 355 | kyc | `archive/converted-prd/kyc/wallet-opening/assets/media/image25.png` | Verify Page | knowledge-base/kyc/account-opening.md | PAGE_VISUAL | BOUND_TO_KB |
| 356 | kyc | `archive/converted-prd/kyc/wallet-opening/assets/media/image26.png` | Waitlist | knowledge-base/kyc/account-opening.md | PAGE_VISUAL | BOUND_TO_KB |
| 357 | kyc | `archive/converted-prd/kyc/wallet-opening/assets/media/image27.png` | 7. 需求描述 | knowledge-base/kyc/account-opening.md | PAGE_VISUAL | BOUND_TO_KB |
| 358 | other | `archive/converted-prd/mgm/referral-invite-code/assets/media/image1.jpeg` | 5. 整体框架 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 359 | other | `archive/converted-prd/mgm/referral-invite-code/assets/media/image2.jpeg` | 5. 整体框架 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 360 | other | `archive/converted-prd/mgm/referral-invite-code/assets/media/image3.png` | 10. Demo | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 361 | other | `archive/converted-prd/mgm/referral-invite-code/assets/media/image4.png` | 12. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 362 | other | `archive/converted-prd/mgm/referral-invite-code/assets/media/image5.png` | 12. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 363 | other | `archive/converted-prd/mgm/referral-invite-code/assets/media/image6.png` | 12. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 364 | other | `archive/converted-prd/mgm/referral-invite-code/assets/media/image7.png` | 12. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 365 | other | `archive/converted-prd/mgm/referral-invite-code/assets/media/image8.png` | 12. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 366 | other | `archive/converted-prd/mgm/referral-invite-code/assets/media/image9.png` | 12. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 367 | other | `archive/converted-prd/mgm/referral-invite-code/assets/media/image10.png` | 12. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 368 | other | `archive/converted-prd/mgm/referral-invite-code/assets/media/image11.png` | 12. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 369 | other | `archive/converted-prd/mgm/referral-invite-code/assets/media/image12.png` | 12. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 370 | other | `archive/converted-prd/mgm/referral-invite-code/assets/media/image13.png` | 12. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 371 | other | `archive/converted-prd/mgm/referral-invite-code/assets/media/image14.png` | 12. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 372 | other | `archive/converted-prd/mgm/referral-invite-code/assets/media/image15.png` | 12. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 373 | other | `archive/converted-prd/mgm/referral-invite-code/assets/media/image16.png` | 12. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 374 | other | `archive/converted-prd/mgm/referral-invite-code/assets/media/image17.png` | 12. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 375 | other | `archive/converted-prd/mgm/referral-invite-code/assets/media/image18.png` | 12. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 376 | other | `archive/converted-prd/mgm/referral-invite-code/assets/media/image19.png` | 12. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 377 | other | `archive/converted-prd/mgm/referral-invite-code/assets/media/image20.png` | 12. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 378 | other | `archive/converted-prd/mgm/referral-invite-code/assets/media/image21.png` | 12. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 379 | other | `archive/converted-prd/mgm/referral-invite-code/assets/media/image22.png` | 12. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 380 | other | `archive/converted-prd/mgm/referral-invite-code/assets/media/image23.png` | 12. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 381 | other | `archive/converted-prd/mgm/referral-invite-code/assets/media/image24.png` | 12. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 382 | other | `archive/converted-prd/mgm/referral-invite-code/assets/media/image25.png` | 12. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 383 | other | `archive/converted-prd/mgm/referral-invite-code/assets/media/image26.png` | 12. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 384 | other | `archive/converted-prd/mgm/referral-invite-code/assets/media/image27.png` | 12. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 385 | other | `archive/converted-prd/mgm/referral-invite-code/assets/media/image28.png` | 12. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 386 | other | `archive/converted-prd/mgm/referral-invite-code/assets/media/image29.png` | 12. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 387 | other | `archive/converted-prd/mgm/referral-invite-code/assets/media/image30.png` | 12. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 388 | other | `archive/converted-prd/mgm/referral-invite-code/assets/media/image31.png` | 12. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 389 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image1.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 390 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image2.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 391 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image3.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 392 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image4.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 393 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image5.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 394 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image6.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 395 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image7.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 396 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image8.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 397 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image9.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 398 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image10.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 399 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image11.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | BOUND_TO_KB |
| 400 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image12.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | BOUND_TO_KB |
| 401 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image13.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | BOUND_TO_KB |
| 402 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image14.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 403 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image15.jpeg` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 404 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image16.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 405 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image17.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 406 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image18.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 407 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image19.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 408 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image20.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | BOUND_TO_KB |
| 409 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image21.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | BOUND_TO_KB |
| 410 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image22.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | BOUND_TO_KB |
| 411 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image23.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | BOUND_TO_KB |
| 412 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image24.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 413 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image25.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 414 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image26.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | BOUND_TO_KB |
| 415 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image26.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | BOUND_TO_KB |
| 416 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image27.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 417 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image27.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 418 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image28.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 419 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image29.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 420 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image30.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 421 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image31.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 422 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image32.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 423 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image33.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 424 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image34.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 425 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image35.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 426 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image36.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 427 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image37.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 428 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image38.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | BOUND_TO_KB |
| 429 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image39.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 430 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image40.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | BOUND_TO_KB |
| 431 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image40.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | BOUND_TO_KB |
| 432 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image41.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 433 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image41.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 434 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image42.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 435 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image29.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 436 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image30.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 437 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image31.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 438 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image32.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 439 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image33.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 440 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image34.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 441 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image35.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 442 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image36.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 443 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image37.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 444 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image38.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | BOUND_TO_KB |
| 445 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image43.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 446 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image44.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | BOUND_TO_KB |
| 447 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image41.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 448 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image41.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 449 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image45.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 450 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image29.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 451 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image46.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 452 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image31.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 453 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image32.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 454 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image33.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 455 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image34.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 456 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image35.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 457 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image36.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 458 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image37.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 459 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image38.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | BOUND_TO_KB |
| 460 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image47.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 461 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image48.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | BOUND_TO_KB |
| 462 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image48.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | BOUND_TO_KB |
| 463 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image41.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 464 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image41.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 465 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image28.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 466 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image29.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 467 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image30.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 468 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image31.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 469 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image32.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | BOUND_TO_KB |
| 470 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image33.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | BOUND_TO_KB |
| 471 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image34.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | BOUND_TO_KB |
| 472 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image35.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 473 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image36.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 474 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image37.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 475 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image38.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | BOUND_TO_KB |
| 476 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image49.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 477 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image48.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | BOUND_TO_KB |
| 478 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image48.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | BOUND_TO_KB |
| 479 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image50.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 480 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image50.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 481 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image28.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 482 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image29.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 483 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image30.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 484 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image31.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 485 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image32.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | BOUND_TO_KB |
| 486 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image33.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | BOUND_TO_KB |
| 487 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image34.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | BOUND_TO_KB |
| 488 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image35.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 489 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image36.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 490 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image37.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 491 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image38.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | BOUND_TO_KB |
| 492 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image51.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 493 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image52.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | BOUND_TO_KB |
| 494 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image52.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | BOUND_TO_KB |
| 495 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image53.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 496 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image53.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 497 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image28.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 498 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image29.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 499 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image30.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 500 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image31.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 501 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image32.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 502 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image33.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 503 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image34.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 504 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image35.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 505 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image36.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 506 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image37.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 507 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image38.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | BOUND_TO_KB |
| 508 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image54.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 509 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image55.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 510 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image56.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 511 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image57.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 512 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image58.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 513 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image59.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 514 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image60.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 515 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image61.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 516 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image30.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 517 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image62.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 518 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image63.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 519 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image37.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | BOUND_TO_KB |
| 520 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image64.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | BOUND_TO_KB |
| 521 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image65.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | BOUND_TO_KB |
| 522 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image66.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | BOUND_TO_KB |
| 523 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image67.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | BOUND_TO_KB |
| 524 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image68.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | BOUND_TO_KB |
| 525 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image69.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | BOUND_TO_KB |
| 526 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image70.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | BOUND_TO_KB |
| 527 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image71.png` | 1. 加密钱包交易类webhook | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 528 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image72.png` | 1. 加密钱包交易类webhook | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 529 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image73.png` | 2. 卡交易类webhook | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 530 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image74.png` | 3. 卡状态变更 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 531 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image75.png` | 4. 其他可见 | knowledge-base/common/notification.md | PAGE_VISUAL | BOUND_TO_KB |
| 532 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image76.png` | 4. 其他可见 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 533 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image77.png` | 4. 其他可见 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 534 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image78.png` | 4. 其他可见 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 535 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image79.png` | 4. 其他可见 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 536 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image80.png` | 4. 其他可见 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 537 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image81.png` | 4. 其他可见 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 538 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image82.png` | 4. 其他可见 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 539 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image83.png` | 4. 其他可见 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 540 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image29.png` | 4. 其他可见 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 541 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image31.png` | 4. 其他可见 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 542 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image32.png` | 4. 其他可见 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 543 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image33.png` | 4. 其他可见 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 544 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image35.png` | 4. 其他可见 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 545 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image36.png` | 4. 其他可见 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 546 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image37.png` | 4. 其他可见 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 547 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image38.png` | 4. 其他可见 | knowledge-base/common/notification.md | PAGE_VISUAL | BOUND_TO_KB |
| 548 | notification | `archive/converted-prd/notification/system-email/assets/media/image1.jpeg` | 3. demo | knowledge-base/common/notification.md | PAGE_VISUAL | BOUND_TO_KB |
| 549 | notification | `archive/converted-prd/notification/system-email/assets/media/image2.jpeg` | 4. Interface interaction | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 550 | other | `archive/converted-prd/oboss/capabilities/assets/media/image1.jpg` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 551 | other | `archive/converted-prd/oboss/capabilities/assets/media/image2.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 552 | other | `archive/converted-prd/oboss/capabilities/assets/media/image3.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 553 | other | `archive/converted-prd/oboss/capabilities/assets/media/image4.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 554 | other | `archive/converted-prd/oboss/capabilities/assets/media/image5.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 555 | other | `archive/converted-prd/oboss/capabilities/assets/media/image6.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 556 | other | `archive/converted-prd/oboss/capabilities/assets/media/image7.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 557 | other | `archive/converted-prd/oboss/capabilities/assets/media/image8.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 558 | other | `archive/converted-prd/oboss/capabilities/assets/media/image9.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 559 | other | `archive/converted-prd/oboss/capabilities/assets/media/image10.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 560 | other | `archive/converted-prd/oboss/capabilities/assets/media/image11.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 561 | other | `archive/converted-prd/oboss/capabilities/assets/media/image12.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 562 | other | `archive/converted-prd/oboss/capabilities/assets/media/image13.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 563 | other | `archive/converted-prd/oboss/capabilities/assets/media/image14.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 564 | other | `archive/converted-prd/oboss/capabilities/assets/media/image15.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 565 | other | `archive/converted-prd/oboss/capabilities/assets/media/image16.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 566 | other | `archive/converted-prd/oboss/capabilities/assets/media/image17.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 567 | other | `archive/converted-prd/oboss/capabilities/assets/media/image18.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 568 | other | `archive/converted-prd/oboss/capabilities/assets/media/image19.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 569 | other | `archive/converted-prd/oboss/capabilities/assets/media/image20.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 570 | other | `archive/converted-prd/oboss/capabilities/assets/media/image21.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 571 | other | `archive/converted-prd/oboss/capabilities/assets/media/image22.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 572 | other | `archive/converted-prd/oboss/capabilities/assets/media/image23.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 573 | other | `archive/converted-prd/oboss/capabilities/assets/media/image24.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 574 | other | `archive/converted-prd/oboss/capabilities/assets/media/image25.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 575 | other | `archive/converted-prd/oboss/capabilities/assets/media/image26.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 576 | other | `archive/converted-prd/oboss/capabilities/assets/media/image27.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 577 | other | `archive/converted-prd/oboss/capabilities/assets/media/image28.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 578 | other | `archive/converted-prd/oboss/capabilities/assets/media/image29.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 579 | other | `archive/converted-prd/oboss/capabilities/assets/media/image30.jpg` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 580 | other | `archive/converted-prd/oboss/capabilities/assets/media/image31.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 581 | other | `archive/converted-prd/oboss/capabilities/assets/media/image3.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 582 | other | `archive/converted-prd/oboss/capabilities/assets/media/image32.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 583 | other | `archive/converted-prd/oboss/capabilities/assets/media/image33.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 584 | other | `archive/converted-prd/oboss/capabilities/assets/media/image34.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 585 | other | `archive/converted-prd/oboss/capabilities/assets/media/image35.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 586 | other | `archive/converted-prd/oboss/capabilities/assets/media/image36.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 587 | other | `archive/converted-prd/oboss/capabilities/assets/media/image28.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 588 | other | `archive/converted-prd/oboss/capabilities/assets/media/image37.jpg` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 589 | other | `archive/converted-prd/oboss/capabilities/assets/media/image31.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 590 | other | `archive/converted-prd/oboss/capabilities/assets/media/image3.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 591 | other | `archive/converted-prd/oboss/capabilities/assets/media/image38.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 592 | other | `archive/converted-prd/oboss/capabilities/assets/media/image39.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 593 | other | `archive/converted-prd/oboss/capabilities/assets/media/image40.png` | Swap | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 594 | other | `archive/converted-prd/oboss/capabilities/assets/media/image41.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 595 | other | `archive/converted-prd/oboss/capabilities/assets/media/image42.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 596 | other | `archive/converted-prd/oboss/capabilities/assets/media/image43.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 597 | other | `archive/converted-prd/oboss/capabilities/assets/media/image44.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 598 | other | `archive/converted-prd/oboss/capabilities/assets/media/image45.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 599 | other | `archive/converted-prd/oboss/capabilities/assets/media/image46.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 600 | other | `archive/converted-prd/oboss/capabilities/assets/media/image47.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 601 | other | `archive/converted-prd/oboss/capabilities/assets/media/image48.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 602 | other | `archive/converted-prd/oboss/capabilities/assets/media/image49.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 603 | other | `archive/converted-prd/oboss/capabilities/assets/media/image50.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 604 | other | `archive/converted-prd/oboss/capabilities/assets/media/image43.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 605 | other | `archive/converted-prd/oboss/mvp/assets/media/image1.png` | \ AIX\ OBOSS MVP | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 606 | other | `archive/converted-prd/oboss/mvp/assets/media/image2.png` | \ AIX\ OBOSS MVP | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 607 | other | `archive/converted-prd/oboss/mvp/assets/media/image3.png` | \ AIX\ OBOSS MVP | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 608 | other | `archive/converted-prd/oboss/mvp/assets/media/image4.png` | \ AIX\ OBOSS MVP | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 609 | other | `archive/converted-prd/oboss/mvp/assets/media/image5.png` | \ AIX\ OBOSS MVP | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 610 | other | `archive/converted-prd/oboss/mvp/assets/media/image6.png` | \ AIX\ OBOSS MVP | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 611 | other | `archive/converted-prd/oboss/mvp/assets/media/image7.png` | \ AIX\ OBOSS MVP | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 612 | other | `archive/converted-prd/oboss/mvp/assets/media/image8.png` | Notification center | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 613 | other | `archive/converted-prd/oboss/mvp/assets/media/image9.png` | Notification center | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 614 | other | `archive/converted-prd/oboss/mvp/assets/media/image10.png` | \ AIX\ OBOSS MVP | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 615 | other | `archive/converted-prd/oboss/mvp/assets/media/image11.png` | \ AIX\ OBOSS MVP | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 616 | other | `archive/converted-prd/oboss/mvp/assets/media/image12.png` | \ AIX\ OBOSS MVP | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 617 | other | `archive/converted-prd/oboss/mvp/assets/media/image13.png` | \ AIX\ OBOSS MVP | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 618 | other | `archive/converted-prd/oboss/mvp/assets/media/image14.png` | \ AIX\ OBOSS MVP | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 619 | other | `archive/converted-prd/oboss/mvp/assets/media/image15.png` | \ AIX\ OBOSS MVP | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 620 | other | `archive/converted-prd/oboss/mvp/assets/media/image16.png` | Notification center | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 621 | other | `archive/converted-prd/oboss/mvp/assets/media/image17.png` | \ AIX\ OBOSS MVP | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 622 | other | `archive/converted-prd/oboss/mvp/assets/media/image18.png` | \ AIX\ OBOSS MVP | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 623 | other | `archive/converted-prd/oboss/mvp/assets/media/image19.png` | \ AIX\ OBOSS MVP | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 624 | other | `archive/converted-prd/oboss/mvp/assets/media/image20.png` | \ AIX\ OBOSS MVP | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 625 | other | `archive/converted-prd/oboss/mvp/assets/media/image21.png` | \ AIX\ OBOSS MVP | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 626 | other | `archive/converted-prd/oboss/mvp/assets/media/image22.png` | \ AIX\ OBOSS MVP | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 627 | other | `archive/converted-prd/oboss/mvp/assets/media/image23.png` | \ AIX\ OBOSS MVP | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 628 | other | `archive/converted-prd/oboss/mvp/assets/media/image24.png` | \ AIX\ OBOSS MVP | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 629 | other | `archive/converted-prd/oboss/mvp/assets/media/image25.png` | \ AIX\ OBOSS MVP | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 630 | other | `archive/converted-prd/oboss/mvp/assets/media/image26.png` | \ AIX\ OBOSS MVP | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 631 | other | `archive/converted-prd/oboss/mvp/assets/media/image27.png` | \ AIX\ OBOSS MVP | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 632 | other | `archive/converted-prd/oboss/mvp/assets/media/image28.png` | \ AIX\ OBOSS MVP | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 633 | other | `archive/converted-prd/oboss/mvp/assets/media/image29.png` | \ AIX\ OBOSS MVP | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 634 | other | `archive/converted-prd/oboss/mvp/assets/media/image30.png` | \ AIX\ OBOSS MVP | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 635 | other | `archive/converted-prd/oboss/mvp/assets/media/image31.png` | \ AIX\ OBOSS MVP | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 636 | other | `archive/converted-prd/oboss/mvp/assets/media/image32.png` | \ AIX\ OBOSS MVP | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 637 | other | `archive/converted-prd/oboss/mvp/assets/media/image33.png` | \ AIX\ OBOSS MVP | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 638 | other | `archive/converted-prd/security/identity-verification/assets/media/image1.png` | 1. 需求变更日志 | knowledge-base/security/global-rules.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 639 | other | `archive/converted-prd/security/identity-verification/assets/media/image2.png` | Verify Page | knowledge-base/security/otp-verification.md | PAGE_VISUAL | BOUND_TO_KB |
| 640 | other | `archive/converted-prd/security/identity-verification/assets/media/image3.png` | Verify Page | knowledge-base/security/otp-verification.md | PAGE_VISUAL | BOUND_TO_KB |
| 641 | other | `archive/converted-prd/security/identity-verification/assets/media/image4.png` | 7. 全局规则 | knowledge-base/security/global-rules.md | PAGE_VISUAL | BOUND_TO_KB |
| 642 | other | `archive/converted-prd/security/identity-verification/assets/media/image5.png` | 7. 全局规则 | knowledge-base/security/global-rules.md | PAGE_VISUAL | BOUND_TO_KB |
| 643 | other | `archive/converted-prd/security/identity-verification/assets/media/image6.png` | 7. 全局规则 | knowledge-base/security/global-rules.md | PAGE_VISUAL | BOUND_TO_KB |
| 644 | other | `archive/converted-prd/security/identity-verification/assets/media/image7.jpeg` | Verify Page | knowledge-base/security/otp-verification.md | PAGE_VISUAL | BOUND_TO_KB |
| 645 | other | `archive/converted-prd/security/identity-verification/assets/media/image8.png` | 8. 需求描述 | knowledge-base/security/global-rules.md | PAGE_VISUAL | BOUND_TO_KB |
| 646 | other | `archive/converted-prd/security/identity-verification/assets/media/image9.png` | 8. 需求描述 | knowledge-base/security/global-rules.md | PAGE_VISUAL | BOUND_TO_KB |
| 647 | other | `archive/converted-prd/security/identity-verification/assets/media/image10.png` | 8. 需求描述 | knowledge-base/security/global-rules.md | PAGE_VISUAL | BOUND_TO_KB |
| 648 | other | `archive/converted-prd/security/identity-verification/assets/media/image11.png` | 8. 需求描述 | knowledge-base/security/global-rules.md | PAGE_VISUAL | BOUND_TO_KB |
| 649 | other | `archive/converted-prd/security/identity-verification/assets/media/image12.png` | 8. 需求描述 | knowledge-base/security/global-rules.md | PAGE_VISUAL | BOUND_TO_KB |
| 650 | other | `archive/converted-prd/security/identity-verification/assets/media/image13.jpeg` | 8. 需求描述 | knowledge-base/security/global-rules.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 651 | other | `archive/converted-prd/security/identity-verification/assets/media/image14.jpeg` | Face Auth | knowledge-base/security/face-authentication.md | PAGE_VISUAL | BOUND_TO_KB |
| 652 | other | `archive/converted-prd/security/identity-verification/assets/media/image15.jpeg` | Face Auth | knowledge-base/security/face-authentication.md | PAGE_VISUAL | BOUND_TO_KB |
| 653 | other | `archive/converted-prd/security/identity-verification/assets/media/image16.png` | 8. 需求描述 | knowledge-base/security/global-rules.md | PAGE_VISUAL | BOUND_TO_KB |
| 654 | other | `archive/converted-prd/security/identity-verification/assets/media/image17.png` | Face Auth | knowledge-base/security/face-authentication.md | PAGE_VISUAL | BOUND_TO_KB |
| 655 | other | `archive/converted-prd/security/identity-verification/assets/media/image18.png` | Face Auth | knowledge-base/security/face-authentication.md | PAGE_VISUAL | BOUND_TO_KB |
| 656 | other | `archive/converted-prd/security/identity-verification/assets/media/image19.png` | 8. 需求描述 | knowledge-base/security/global-rules.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 657 | wallet/assets | `archive/converted-prd/wallet/asset/assets/media/image1.png` | 4. AIX前端功能需求 | knowledge-base/wallet/assets.md | PAGE_VISUAL | BOUND_TO_KB |
| 658 | wallet/assets | `archive/converted-prd/wallet/asset/assets/media/image2.png` | 4. AIX前端功能需求 | knowledge-base/wallet/assets.md | PAGE_VISUAL | BOUND_TO_KB |
| 659 | wallet/assets | `archive/converted-prd/wallet/asset/assets/media/image3.png` | 4. AIX前端功能需求 | knowledge-base/wallet/assets.md | PAGE_VISUAL | BOUND_TO_KB |
| 660 | wallet/assets | `archive/converted-prd/wallet/asset/assets/media/image4.png` | 4. AIX前端功能需求 | knowledge-base/wallet/assets.md | PAGE_VISUAL | BOUND_TO_KB |
| 661 | wallet/assets | `archive/converted-prd/wallet/asset/assets/media/image5.png` | 4. AIX前端功能需求 | knowledge-base/wallet/assets.md | PAGE_VISUAL | BOUND_TO_KB |
| 662 | wallet/assets | `archive/converted-prd/wallet/asset/assets/media/image6.jpeg` | 5. DTC渠道接口需求 | knowledge-base/wallet/assets.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 663 | wallet/assets | `archive/converted-prd/wallet/asset/assets/media/image7.jpeg` | 5. DTC渠道接口需求 | knowledge-base/wallet/assets.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 664 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image1.png` | 1. 引言 | knowledge-base/wallet/deposit.md | PAGE_VISUAL | BOUND_TO_KB |
| 665 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image2.png` | 1. 引言 | knowledge-base/wallet/deposit.md | PAGE_VISUAL | BOUND_TO_KB |
| 666 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image3.png` | 1. 引言 | knowledge-base/wallet/deposit.md | PAGE_VISUAL | BOUND_TO_KB |
| 667 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image4.png` | 1. 引言 | knowledge-base/wallet/deposit.md | PAGE_VISUAL | BOUND_TO_KB |
| 668 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image5.png` | 1. 引言 | knowledge-base/wallet/deposit.md | PAGE_VISUAL | BOUND_TO_KB |
| 669 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image6.png` | 1. 引言 | knowledge-base/wallet/deposit.md | PAGE_VISUAL | BOUND_TO_KB |
| 670 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image7.jpeg` | 6. AIX前端功能需求 | knowledge-base/wallet/deposit.md | PAGE_VISUAL | BOUND_TO_KB |
| 671 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image8.png` | 6. AIX前端功能需求 | knowledge-base/wallet/deposit.md | PAGE_VISUAL | BOUND_TO_KB |
| 672 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image9.png` | Send Crypto | knowledge-base/wallet/send.md | PAGE_VISUAL | BOUND_TO_KB |
| 673 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image10.png` | Send Crypto | knowledge-base/wallet/send.md | PAGE_VISUAL | BOUND_TO_KB |
| 674 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image11.png` | Send Crypto | knowledge-base/wallet/send.md | PAGE_VISUAL | BOUND_TO_KB |
| 675 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image12.png` | Send Crypto | knowledge-base/wallet/send.md | PAGE_VISUAL | BOUND_TO_KB |
| 676 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image13.png` | 6. AIX前端功能需求 | knowledge-base/wallet/deposit.md | PAGE_VISUAL | BOUND_TO_KB |
| 677 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image14.png` | 6. AIX前端功能需求 | knowledge-base/wallet/deposit.md | PAGE_VISUAL | BOUND_TO_KB |
| 678 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image15.png` | 6. AIX前端功能需求 | knowledge-base/wallet/deposit.md | PAGE_VISUAL | BOUND_TO_KB |
| 679 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image16.png` | Deposit Crypto | knowledge-base/wallet/deposit.md | PAGE_VISUAL | BOUND_TO_KB |
| 680 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image17.png` | Deposit Crypto | knowledge-base/wallet/deposit.md | PAGE_VISUAL | BOUND_TO_KB |
| 681 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image18.png` | Transaction Details | knowledge-base/wallet/deposit.md | PAGE_VISUAL | BOUND_TO_KB |
| 682 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image19.png` | Transaction Details | knowledge-base/wallet/deposit.md | PAGE_VISUAL | BOUND_TO_KB |
| 683 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image20.png` | Transaction Details | knowledge-base/wallet/deposit.md | PAGE_VISUAL | BOUND_TO_KB |
| 684 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image21.jpeg` | 6. AIX前端功能需求 | knowledge-base/wallet/deposit.md | PAGE_VISUAL | BOUND_TO_KB |
| 685 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image22.png` | 6. AIX前端功能需求 | knowledge-base/wallet/deposit.md | PAGE_VISUAL | BOUND_TO_KB |
| 686 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image23.png` | Swap | knowledge-base/wallet/swap.md | PAGE_VISUAL | BOUND_TO_KB |
| 687 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image24.png` | Swap | knowledge-base/wallet/swap.md | PAGE_VISUAL | BOUND_TO_KB |
| 688 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image25.png` | Swap | knowledge-base/wallet/swap.md | PAGE_VISUAL | BOUND_TO_KB |
| 689 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image26.png` | Swap | knowledge-base/wallet/swap.md | PAGE_VISUAL | BOUND_TO_KB |
| 690 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image27.png` | Swap Order | knowledge-base/wallet/swap.md | PAGE_VISUAL | BOUND_TO_KB |
| 691 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image28.png` | Swap Order | knowledge-base/wallet/swap.md | PAGE_VISUAL | BOUND_TO_KB |
| 692 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image29.png` | Swap Order | knowledge-base/wallet/swap.md | PAGE_VISUAL | BOUND_TO_KB |
| 693 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image30.png` | Swap | knowledge-base/wallet/swap.md | PAGE_VISUAL | BOUND_TO_KB |
| 694 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image31.png` | Swap | knowledge-base/wallet/swap.md | PAGE_VISUAL | BOUND_TO_KB |
| 695 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image32.png` | Deposit Crypto | knowledge-base/wallet/deposit.md | PAGE_VISUAL | BOUND_TO_KB |
| 696 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image33.jpeg` | 6. AIX前端功能需求 | knowledge-base/wallet/deposit.md | PAGE_VISUAL | BOUND_TO_KB |
| 697 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image34.png` | 6. AIX前端功能需求 | knowledge-base/wallet/deposit.md | PAGE_VISUAL | BOUND_TO_KB |
| 698 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image35.png` | 6. AIX前端功能需求 | knowledge-base/wallet/deposit.md | PAGE_VISUAL | BOUND_TO_KB |
| 699 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image36.png` | 6. AIX前端功能需求 | knowledge-base/wallet/deposit.md | PAGE_VISUAL | BOUND_TO_KB |
| 700 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image37.png` | 6. AIX前端功能需求 | knowledge-base/wallet/deposit.md | PAGE_VISUAL | BOUND_TO_KB |
| 701 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image38.png` | Deposit Crypto | knowledge-base/wallet/deposit.md | PAGE_VISUAL | BOUND_TO_KB |
| 702 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image39.png` | Deposit Crypto | knowledge-base/wallet/deposit.md | PAGE_VISUAL | BOUND_TO_KB |
| 703 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image40.png` | 6. AIX前端功能需求 | knowledge-base/wallet/deposit.md | PAGE_VISUAL | BOUND_TO_KB |
| 704 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image41.png` | Receive Crypto | knowledge-base/wallet/deposit.md | PAGE_VISUAL | BOUND_TO_KB |
| 705 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image42.png` | Receive Crypto | knowledge-base/wallet/deposit.md | PAGE_VISUAL | BOUND_TO_KB |
| 706 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image43.png` | 6. AIX前端功能需求 | knowledge-base/wallet/deposit.md | PAGE_VISUAL | BOUND_TO_KB |
| 707 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image44.jpeg` | 6. AIX前端功能需求 | knowledge-base/wallet/deposit.md | PAGE_VISUAL | BOUND_TO_KB |
| 708 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image45.png` | 6. AIX前端功能需求 | knowledge-base/wallet/deposit.md | PAGE_VISUAL | BOUND_TO_KB |
| 709 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image46.png` | 6. AIX前端功能需求 | knowledge-base/wallet/deposit.md | PAGE_VISUAL | BOUND_TO_KB |
| 710 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image47.png` | 6. AIX前端功能需求 | knowledge-base/wallet/deposit.md | PAGE_VISUAL | BOUND_TO_KB |
| 711 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image48.png` | 6. AIX前端功能需求 | knowledge-base/wallet/deposit.md | PAGE_VISUAL | BOUND_TO_KB |
| 712 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image49.png` | Deposit Crypto | knowledge-base/wallet/deposit.md | PAGE_VISUAL | BOUND_TO_KB |
| 713 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image50.png` | Deposit Crypto | knowledge-base/wallet/deposit.md | PAGE_VISUAL | BOUND_TO_KB |
| 714 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image51.png` | Deposit Crypto | knowledge-base/wallet/deposit.md | PAGE_VISUAL | BOUND_TO_KB |
| 715 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image52.png` | Deposit Crypto | knowledge-base/wallet/deposit.md | PAGE_VISUAL | BOUND_TO_KB |
| 716 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image53.png` | 6. AIX前端功能需求 | knowledge-base/wallet/deposit.md | PAGE_VISUAL | BOUND_TO_KB |
| 717 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image54.png` | 6. AIX前端功能需求 | knowledge-base/wallet/deposit.md | PAGE_VISUAL | BOUND_TO_KB |
| 718 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image55.png` | 6. AIX前端功能需求 | knowledge-base/wallet/deposit.md | PAGE_VISUAL | BOUND_TO_KB |
| 719 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image56.png` | 6. AIX前端功能需求 | knowledge-base/wallet/deposit.md | PAGE_VISUAL | BOUND_TO_KB |
| 720 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image57.png` | 6. AIX前端功能需求 | knowledge-base/wallet/deposit.md | PAGE_VISUAL | BOUND_TO_KB |
| 721 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image58.png` | 6. AIX前端功能需求 | knowledge-base/wallet/deposit.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 722 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image59.png` | 6. AIX前端功能需求 | knowledge-base/wallet/deposit.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 723 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image60.png` | 6. AIX前端功能需求 | knowledge-base/wallet/deposit.md | PAGE_VISUAL | BOUND_TO_KB |
| 724 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image61.jpeg` | 6. AIX前端功能需求 | knowledge-base/wallet/deposit.md | PAGE_VISUAL | BOUND_TO_KB |
| 725 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image62.png` | Transaction Details | knowledge-base/wallet/deposit.md | PAGE_VISUAL | BOUND_TO_KB |
| 726 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image63.jpeg` | 7. DTC渠道接口需求 | knowledge-base/wallet/deposit.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 727 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image64.jpeg` | 7. DTC渠道接口需求 | knowledge-base/wallet/deposit.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 728 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image65.jpeg` | 7. DTC渠道接口需求 | knowledge-base/wallet/deposit.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 729 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image66.png` | 7. DTC渠道接口需求 | knowledge-base/wallet/deposit.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 730 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image67.jpeg` | 7. DTC渠道接口需求 | knowledge-base/wallet/deposit.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 731 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image68.jpeg` | 7. DTC渠道接口需求 | knowledge-base/wallet/deposit.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 732 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image69.jpeg` | 7. DTC渠道接口需求 | knowledge-base/wallet/deposit.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 733 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image70.jpeg` | 7. DTC渠道接口需求 | knowledge-base/wallet/deposit.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 734 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image71.jpeg` | 7. DTC渠道接口需求 | knowledge-base/wallet/deposit.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 735 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image72.jpeg` | 7. DTC渠道接口需求 | knowledge-base/wallet/deposit.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 736 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image73.jpeg` | 7. DTC渠道接口需求 | knowledge-base/wallet/deposit.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 737 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image63.jpeg` | 7. DTC渠道接口需求 | knowledge-base/wallet/deposit.md | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 738 | other | `archive/converted-prd/website/phase-1/assets/media/image1.jpg` | 4. 需求优先级 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 739 | other | `archive/converted-prd/website/phase-1/assets/media/image2.png` | 4. 需求优先级 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 740 | other | `archive/converted-prd/website/phase-1/assets/media/image3.png` | 4. 需求优先级 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 741 | other | `archive/converted-prd/website/phase-1/assets/media/image4.png` | 4. 需求优先级 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 742 | other | `archive/converted-prd/website/phase-1/assets/media/image5.png` | 4. 需求优先级 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 743 | other | `archive/converted-prd/website/phase-1/assets/media/image6.png` | 4. 需求优先级 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 744 | other | `archive/converted-prd/website/phase-1/assets/media/image7.png` | 4. 需求优先级 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 745 | other | `archive/converted-prd/website/phase-1/assets/media/image8.png` | 4. 需求优先级 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 746 | other | `archive/converted-prd/website/phase-1/assets/media/image9.png` | 4. 需求优先级 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 747 | other | `archive/converted-prd/website/phase-1/assets/media/image10.png` | 4. 需求优先级 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 748 | other | `archive/converted-prd/website/phase-1/assets/media/image11.jpg` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 749 | other | `archive/converted-prd/website/phase-1/assets/media/image12.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 750 | other | `archive/converted-prd/website/phase-1/assets/media/image13.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 751 | other | `archive/converted-prd/website/phase-1/assets/media/image14.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 752 | other | `archive/converted-prd/website/phase-1/assets/media/image15.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 753 | other | `archive/converted-prd/website/phase-1/assets/media/image16.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 754 | other | `archive/converted-prd/website/phase-1/assets/media/image17.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 755 | other | `archive/converted-prd/website/phase-1/assets/media/image18.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 756 | other | `archive/converted-prd/website/phase-1/assets/media/image19.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 757 | other | `archive/converted-prd/website/phase-1/assets/media/image20.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 758 | other | `archive/converted-prd/website/phase-1/assets/media/image21.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 759 | other | `archive/converted-prd/website/phase-1/assets/media/image22.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 760 | other | `archive/converted-prd/website/phase-1/assets/media/image23.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 761 | other | `archive/converted-prd/website/phase-1/assets/media/image24.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 762 | other | `archive/converted-prd/website/phase-1/assets/media/image25.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 763 | other | `archive/converted-prd/website/phase-1/assets/media/image26.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 764 | other | `archive/converted-prd/website/phase-1/assets/media/image27.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 765 | other | `archive/converted-prd/website/phase-1/assets/media/image28.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 766 | other | `archive/converted-prd/website/phase-1/assets/media/image29.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 767 | other | `archive/converted-prd/website/phase-1/assets/media/image30.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 768 | other | `archive/converted-prd/website/phase-1/assets/media/image31.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 769 | other | `archive/converted-prd/website/phase-1/assets/media/image32.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 770 | other | `archive/converted-prd/website/phase-1/assets/media/image33.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 771 | other | `archive/converted-prd/website/phase-1/assets/media/image34.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 772 | other | `archive/converted-prd/website/phase-1/assets/media/image35.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 773 | other | `archive/converted-prd/website/phase-1/assets/media/image36.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 774 | other | `archive/converted-prd/website/phase-1/assets/media/image37.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 775 | other | `archive/converted-prd/website/phase-1/assets/media/image38.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 776 | other | `archive/converted-prd/website/phase-1/assets/media/image39.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 777 | other | `archive/converted-prd/website/phase-1/assets/media/image40.jpg` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 778 | other | `archive/converted-prd/website/phase-1/assets/media/image41.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 779 | other | `archive/converted-prd/website/phase-1/assets/media/image13.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 780 | other | `archive/converted-prd/website/phase-1/assets/media/image42.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 781 | other | `archive/converted-prd/website/phase-1/assets/media/image43.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 782 | other | `archive/converted-prd/website/phase-1/assets/media/image44.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 783 | other | `archive/converted-prd/website/phase-1/assets/media/image45.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 784 | other | `archive/converted-prd/website/phase-1/assets/media/image46.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 785 | other | `archive/converted-prd/website/phase-1/assets/media/image38.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 786 | other | `archive/converted-prd/website/phase-1/assets/media/image47.jpg` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 787 | other | `archive/converted-prd/website/phase-1/assets/media/image41.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 788 | other | `archive/converted-prd/website/phase-1/assets/media/image13.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 789 | other | `archive/converted-prd/website/phase-1/assets/media/image48.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 790 | other | `archive/converted-prd/website/phase-1/assets/media/image49.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 791 | other | `archive/converted-prd/website/phase-1/assets/media/image50.png` | Swap | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 792 | other | `archive/converted-prd/website/phase-1/assets/media/image51.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 793 | other | `archive/converted-prd/website/phase-1/assets/media/image52.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 794 | other | `archive/converted-prd/website/phase-1/assets/media/image53.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 795 | other | `archive/converted-prd/website/phase-1/assets/media/image54.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 796 | other | `archive/converted-prd/website/phase-1/assets/media/image55.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 797 | other | `archive/converted-prd/website/phase-1/assets/media/image56.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 798 | other | `archive/converted-prd/website/phase-1/assets/media/image57.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 799 | other | `archive/converted-prd/website/phase-1/assets/media/image58.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 800 | other | `archive/converted-prd/website/phase-1/assets/media/image59.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 801 | other | `archive/converted-prd/website/phase-1/assets/media/image60.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 802 | other | `archive/converted-prd/website/phase-1/assets/media/image53.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 803 | other | `archive/converted-prd/website/phase-2/assets/media/image1.jpeg` | 3. 需求概况 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 804 | other | `archive/converted-prd/website/phase-2/assets/media/image2.jpeg` | 3. 需求概况 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 805 | other | `archive/converted-prd/website/phase-2/assets/media/image3.jpg` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 806 | other | `archive/converted-prd/website/phase-2/assets/media/image4.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 807 | other | `archive/converted-prd/website/phase-2/assets/media/image5.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 808 | other | `archive/converted-prd/website/phase-2/assets/media/image6.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 809 | other | `archive/converted-prd/website/phase-2/assets/media/image7.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 810 | other | `archive/converted-prd/website/phase-2/assets/media/image8.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 811 | other | `archive/converted-prd/website/phase-2/assets/media/image9.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 812 | other | `archive/converted-prd/website/phase-2/assets/media/image10.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 813 | other | `archive/converted-prd/website/phase-2/assets/media/image11.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 814 | other | `archive/converted-prd/website/phase-2/assets/media/image12.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 815 | other | `archive/converted-prd/website/phase-2/assets/media/image13.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 816 | other | `archive/converted-prd/website/phase-2/assets/media/image14.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 817 | other | `archive/converted-prd/website/phase-2/assets/media/image15.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 818 | other | `archive/converted-prd/website/phase-2/assets/media/image16.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 819 | other | `archive/converted-prd/website/phase-2/assets/media/image17.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 820 | other | `archive/converted-prd/website/phase-2/assets/media/image18.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 821 | other | `archive/converted-prd/website/phase-2/assets/media/image19.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 822 | other | `archive/converted-prd/website/phase-2/assets/media/image20.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 823 | other | `archive/converted-prd/website/phase-2/assets/media/image21.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 824 | other | `archive/converted-prd/website/phase-2/assets/media/image22.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 825 | other | `archive/converted-prd/website/phase-2/assets/media/image23.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL_INDEXED | SUPPORTING_VISUAL_INDEXED |
| 826 | other | `archive/converted-prd/website/phase-2/assets/media/image24.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 827 | other | `archive/converted-prd/website/phase-2/assets/media/image25.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 828 | other | `archive/converted-prd/website/phase-2/assets/media/image26.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 829 | other | `archive/converted-prd/website/phase-2/assets/media/image27.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 830 | other | `archive/converted-prd/website/phase-2/assets/media/image28.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 831 | other | `archive/converted-prd/website/phase-2/assets/media/image29.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 832 | other | `archive/converted-prd/website/phase-2/assets/media/image30.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 833 | other | `archive/converted-prd/website/phase-2/assets/media/image31.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 834 | other | `archive/converted-prd/website/phase-2/assets/media/image32.jpg` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 835 | other | `archive/converted-prd/website/phase-2/assets/media/image33.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 836 | other | `archive/converted-prd/website/phase-2/assets/media/image5.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 837 | other | `archive/converted-prd/website/phase-2/assets/media/image34.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 838 | other | `archive/converted-prd/website/phase-2/assets/media/image35.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 839 | other | `archive/converted-prd/website/phase-2/assets/media/image36.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 840 | other | `archive/converted-prd/website/phase-2/assets/media/image37.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 841 | other | `archive/converted-prd/website/phase-2/assets/media/image38.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 842 | other | `archive/converted-prd/website/phase-2/assets/media/image30.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 843 | other | `archive/converted-prd/website/phase-2/assets/media/image39.jpg` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 844 | other | `archive/converted-prd/website/phase-2/assets/media/image33.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 845 | other | `archive/converted-prd/website/phase-2/assets/media/image5.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 846 | other | `archive/converted-prd/website/phase-2/assets/media/image40.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 847 | other | `archive/converted-prd/website/phase-2/assets/media/image41.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 848 | other | `archive/converted-prd/website/phase-2/assets/media/image42.png` | Swap | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 849 | other | `archive/converted-prd/website/phase-2/assets/media/image43.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 850 | other | `archive/converted-prd/website/phase-2/assets/media/image44.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 851 | other | `archive/converted-prd/website/phase-2/assets/media/image45.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 852 | other | `archive/converted-prd/website/phase-2/assets/media/image46.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 853 | other | `archive/converted-prd/website/phase-2/assets/media/image47.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 854 | other | `archive/converted-prd/website/phase-2/assets/media/image48.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 855 | other | `archive/converted-prd/website/phase-2/assets/media/image49.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 856 | other | `archive/converted-prd/website/phase-2/assets/media/image50.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 857 | other | `archive/converted-prd/website/phase-2/assets/media/image51.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 858 | other | `archive/converted-prd/website/phase-2/assets/media/image52.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 859 | other | `archive/converted-prd/website/phase-2/assets/media/image45.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 860 | other | `archive/converted-prd/website/waitlist-addition/assets/media/image1.jpg` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 861 | other | `archive/converted-prd/website/waitlist-addition/assets/media/image2.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 862 | other | `archive/converted-prd/website/waitlist-addition/assets/media/image3.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 863 | other | `archive/converted-prd/website/waitlist-addition/assets/media/image4.jpeg` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 864 | other | `archive/converted-prd/website/waitlist-addition/assets/media/image5.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 865 | other | `archive/converted-prd/website/waitlist-addition/assets/media/image6.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 866 | other | `archive/converted-prd/website/waitlist-addition/assets/media/image7.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 867 | other | `archive/converted-prd/website/waitlist-campaign/assets/media/image1.jpg` | 4. Demo | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 868 | other | `archive/converted-prd/website/waitlist-campaign/assets/media/image2.jpg` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |
| 869 | other | `archive/converted-prd/website/waitlist-campaign/assets/media/image3.jpg` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | NON_RUNTIME_VISUAL_INDEXED |