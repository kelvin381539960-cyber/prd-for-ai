---
module: changelog
feature: prd-page-visual-coverage
version: "1.0"
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
| 流程图 / 接口图 / 数据字典等支撑图 | 290 |

## 3. 绑定规则

1. 页面截图应放在对应 KB 页面规则章节附近，或在该文件的 Page Visuals 索引中明确指向页面规则。
2. 删除线页面不进入 runtime 规则，只可登记为 deleted / out_of_scope。
3. 流程图、接口时序图、数据字典图不强制放入页面规则，但可作为 supporting visual。
4. 当前阶段优先绑定 PAGE_VISUAL，后续再按需要补 supporting visual。

## 4. 页面图片覆盖清单（初步自动识别）

| # | Module | Evidence image | Inferred page | KB target | Kind | Status |
|---:|---|---|---|---|---|---|
| 1 | common/faq | `archive/converted-prd/app/faq/assets/media/image1.png` | 3. 功能需求 | knowledge-base/common/faq.md | PAGE_VISUAL | TODO_BIND |
| 2 | common/faq | `archive/converted-prd/app/faq/assets/media/image2.png` | 3. 功能需求 | knowledge-base/common/faq.md | PAGE_VISUAL | TODO_BIND |
| 3 | common/faq | `archive/converted-prd/app/faq/assets/media/image3.png` | 3. 功能需求 | knowledge-base/common/faq.md | PAGE_VISUAL | TODO_BIND |
| 4 | common/faq | `archive/converted-prd/app/faq/assets/media/image4.png` | Virtual Card  | knowledge-base/common/faq.md | PAGE_VISUAL | TODO_BIND |
| 5 | common/faq | `archive/converted-prd/app/faq/assets/media/image5.png` | Physical Card  | knowledge-base/common/faq.md | PAGE_VISUAL | TODO_BIND |
| 6 | common/faq | `archive/converted-prd/app/faq/assets/media/image2.png` | Physical Card  | knowledge-base/common/faq.md | PAGE_VISUAL | TODO_BIND |
| 7 | common/faq | `archive/converted-prd/app/faq/assets/media/image6.png` | Physical Card  | knowledge-base/common/faq.md | PAGE_VISUAL | TODO_BIND |
| 8 | common/faq | `archive/converted-prd/app/faq/assets/media/image7.png` | Select Crypto  | knowledge-base/common/faq.md | PAGE_VISUAL | TODO_BIND |
| 9 | common/faq | `archive/converted-prd/app/faq/assets/media/image2.png` | Select Crypto  | knowledge-base/common/faq.md | PAGE_VISUAL | TODO_BIND |
| 10 | common/faq | `archive/converted-prd/app/faq/assets/media/image7.png` | Card home  | knowledge-base/common/faq.md | PAGE_VISUAL | TODO_BIND |
| 11 | common/faq | `archive/converted-prd/app/faq/assets/media/image2.png` | Card home  | knowledge-base/common/faq.md | PAGE_VISUAL | TODO_BIND |
| 12 | common/faq | `archive/converted-prd/app/faq/assets/media/image8.png` | Bind Google Wallet  | knowledge-base/common/faq.md | PAGE_VISUAL | TODO_BIND |
| 13 | common/faq | `archive/converted-prd/app/faq/assets/media/image2.png` | Bind Google Wallet  | knowledge-base/common/faq.md | PAGE_VISUAL | TODO_BIND |
| 14 | common/faq | `archive/converted-prd/app/faq/assets/media/image9.png` | Update Phone  | knowledge-base/common/faq.md | PAGE_VISUAL | TODO_BIND |
| 15 | common/faq | `archive/converted-prd/app/faq/assets/media/image2.png` | Update Phone  | knowledge-base/common/faq.md | PAGE_VISUAL | TODO_BIND |
| 16 | common/faq | `archive/converted-prd/app/faq/assets/media/image10.png` | All Transactions  | knowledge-base/common/faq.md | PAGE_VISUAL | TODO_BIND |
| 17 | common/faq | `archive/converted-prd/app/faq/assets/media/image2.png` | All Transactions  | knowledge-base/common/faq.md | PAGE_VISUAL | TODO_BIND |
| 18 | common/faq | `archive/converted-prd/app/faq/assets/media/image11.png` | Transaction Details  | knowledge-base/common/faq.md | PAGE_VISUAL | TODO_BIND |
| 19 | common/faq | `archive/converted-prd/app/faq/assets/media/image2.png` | Transaction Details  | knowledge-base/common/faq.md | PAGE_VISUAL | TODO_BIND |
| 20 | common/faq | `archive/converted-prd/app/faq/assets/media/image12.png` | Crypto Send  | knowledge-base/common/faq.md | PAGE_VISUAL | TODO_BIND |
| 21 | common/faq | `archive/converted-prd/app/faq/assets/media/image2.png` | Crypto Send  | knowledge-base/common/faq.md | PAGE_VISUAL | TODO_BIND |
| 22 | common/faq | `archive/converted-prd/app/faq/assets/media/image13.png` | Crypto Swap  | knowledge-base/common/faq.md | PAGE_VISUAL | TODO_BIND |
| 23 | common/faq | `archive/converted-prd/app/faq/assets/media/image2.png` | Crypto Swap  | knowledge-base/common/faq.md | PAGE_VISUAL | TODO_BIND |
| 24 | common/faq | `archive/converted-prd/app/faq/assets/media/image14.png` | Deposit method  | knowledge-base/common/faq.md | PAGE_VISUAL | TODO_BIND |
| 25 | common/faq | `archive/converted-prd/app/faq/assets/media/image2.png` | Deposit method  | knowledge-base/common/faq.md | PAGE_VISUAL | TODO_BIND |
| 26 | common/faq | `archive/converted-prd/app/faq/assets/media/image15.png` | Receive Crypto  | knowledge-base/common/faq.md | PAGE_VISUAL | TODO_BIND |
| 27 | common/faq | `archive/converted-prd/app/faq/assets/media/image16.png` | 4. Chat with us | knowledge-base/common/faq.md | PAGE_VISUAL | TODO_BIND |
| 28 | common/faq | `archive/converted-prd/app/faq/assets/media/image17.png` | 4. Chat with us | knowledge-base/common/faq.md | PAGE_VISUAL | TODO_BIND |
| 29 | common/faq | `archive/converted-prd/app/faq/assets/media/image18.png` | 4. Chat with us | knowledge-base/common/faq.md | PAGE_VISUAL | TODO_BIND |
| 30 | home | `archive/converted-prd/app/home/assets/media/image1.jpeg` | 3. 全局说明 | knowledge-base/home/app-home.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 31 | home | `archive/converted-prd/app/home/assets/media/image2.jpeg` | 4. 整体流程 | knowledge-base/home/app-home.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 32 | home | `archive/converted-prd/app/home/assets/media/image3.jpeg` | 4. 整体流程 | knowledge-base/home/app-home.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 33 | home | `archive/converted-prd/app/home/assets/media/image4.jpeg` | 4. 整体流程 | knowledge-base/home/app-home.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 34 | home | `archive/converted-prd/app/home/assets/media/image5.jpeg` | 4. 整体流程 | knowledge-base/home/app-home.md | PAGE_VISUAL | TODO_BIND |
| 35 | home | `archive/converted-prd/app/home/assets/media/image6.jpeg` | 4. 整体流程 | knowledge-base/home/app-home.md | PAGE_VISUAL | TODO_BIND |
| 36 | home | `archive/converted-prd/app/home/assets/media/image7.jpeg` | 4. 整体流程 | knowledge-base/home/app-home.md | PAGE_VISUAL | TODO_BIND |
| 37 | home | `archive/converted-prd/app/home/assets/media/image8.jpeg` | 4. 整体流程 | knowledge-base/home/app-home.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 38 | home | `archive/converted-prd/app/home/assets/media/image9.jpeg` | 4. 整体流程 | knowledge-base/home/app-home.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 39 | home | `archive/converted-prd/app/home/assets/media/image10.jpeg` | Set Pin | knowledge-base/home/app-home.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 40 | home | `archive/converted-prd/app/home/assets/media/image11.jpeg` | Set Pin | knowledge-base/home/app-home.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 41 | home | `archive/converted-prd/app/home/assets/media/image12.jpeg` | Set Pin | knowledge-base/home/app-home.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 42 | home | `archive/converted-prd/app/home/assets/media/image13.jpeg` | Set Pin | knowledge-base/home/app-home.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 43 | home | `archive/converted-prd/app/home/assets/media/image14.jpeg` | Set Pin | knowledge-base/home/app-home.md | PAGE_VISUAL | TODO_BIND |
| 44 | home | `archive/converted-prd/app/home/assets/media/image15.jpeg` | Set Pin | knowledge-base/home/app-home.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 45 | home | `archive/converted-prd/app/home/assets/media/image16.jpeg` | 4. 整体流程 | knowledge-base/home/app-home.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 46 | home | `archive/converted-prd/app/home/assets/media/image17.jpeg` | 4. 整体流程 | knowledge-base/home/app-home.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 47 | home | `archive/converted-prd/app/home/assets/media/image18.jpeg` | 4. 整体流程 | knowledge-base/home/app-home.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 48 | home | `archive/converted-prd/app/home/assets/media/image19.jpeg` | 4. 整体流程 | knowledge-base/home/app-home.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 49 | home | `archive/converted-prd/app/home/assets/media/image20.jpeg` | 4. 整体流程 | knowledge-base/home/app-home.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 50 | home | `archive/converted-prd/app/home/assets/media/image21.png` | 申卡入口 | knowledge-base/home/app-home.md | PAGE_VISUAL | TODO_BIND |
| 51 | home | `archive/converted-prd/app/home/assets/media/image22.png` | 6. AIX功能需求 | knowledge-base/home/app-home.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 52 | home | `archive/converted-prd/app/home/assets/media/image23.png` | Waitlist | knowledge-base/home/app-home.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 53 | home | `archive/converted-prd/app/home/assets/media/image24.png` | Waitlist | knowledge-base/home/app-home.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 54 | home | `archive/converted-prd/app/home/assets/media/image25.png` | Waitlist | knowledge-base/home/app-home.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 55 | home | `archive/converted-prd/app/home/assets/media/image26.png` | 未申请开通钱包 | knowledge-base/home/app-home.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 56 | home | `archive/converted-prd/app/home/assets/media/image27.png` | 未申请开通钱包 | knowledge-base/home/app-home.md | PAGE_VISUAL | TODO_BIND |
| 57 | home | `archive/converted-prd/app/home/assets/media/image28.png` | 未申请开通钱包 | knowledge-base/home/app-home.md | PAGE_VISUAL | TODO_BIND |
| 58 | home | `archive/converted-prd/app/home/assets/media/image29.png` | 未申请开通钱包 | knowledge-base/home/app-home.md | PAGE_VISUAL | TODO_BIND |
| 59 | home | `archive/converted-prd/app/home/assets/media/image30.png` | 未申请开通钱包 | knowledge-base/home/app-home.md | PAGE_VISUAL | TODO_BIND |
| 60 | home | `archive/converted-prd/app/home/assets/media/image31.png` | 申卡入口 | knowledge-base/home/app-home.md | PAGE_VISUAL | TODO_BIND |
| 61 | home | `archive/converted-prd/app/home/assets/media/image32.png` | 申卡入口 | knowledge-base/home/app-home.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 62 | home | `archive/converted-prd/app/home/assets/media/image33.jpeg` | 申卡入口 | knowledge-base/home/app-home.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 63 | home | `archive/converted-prd/app/home/assets/media/image34.jpeg` | 申卡入口 | knowledge-base/home/app-home.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 64 | home | `archive/converted-prd/app/home/assets/media/image35.png` | 申卡入口 | knowledge-base/home/app-home.md | PAGE_VISUAL | TODO_BIND |
| 65 | home | `archive/converted-prd/app/home/assets/media/image36.png` | 申卡入口 | knowledge-base/home/app-home.md | PAGE_VISUAL | TODO_BIND |
| 66 | home | `archive/converted-prd/app/home/assets/media/image37.png` | 申卡入口 | knowledge-base/home/app-home.md | PAGE_VISUAL | TODO_BIND |
| 67 | home | `archive/converted-prd/app/home/assets/media/image38.png` | 申卡入口 | knowledge-base/home/app-home.md | PAGE_VISUAL | TODO_BIND |
| 68 | home | `archive/converted-prd/app/home/assets/media/image39.png` | 当前卡片展示 | knowledge-base/home/app-home.md | PAGE_VISUAL | TODO_BIND |
| 69 | home | `archive/converted-prd/app/home/assets/media/image40.png` | 当前卡片展示 | knowledge-base/home/app-home.md | PAGE_VISUAL | TODO_BIND |
| 70 | home | `archive/converted-prd/app/home/assets/media/image41.png` | 申卡入口 | knowledge-base/home/app-home.md | PAGE_VISUAL | TODO_BIND |
| 71 | home | `archive/converted-prd/app/home/assets/media/image42.png` | 申卡入口 | knowledge-base/home/app-home.md | PAGE_VISUAL | TODO_BIND |
| 72 | home | `archive/converted-prd/app/home/assets/media/image43.png` | Select Wallet | knowledge-base/home/app-home.md | PAGE_VISUAL | TODO_BIND |
| 73 | home | `archive/converted-prd/app/home/assets/media/image44.png` | Select Wallet | knowledge-base/home/app-home.md | PAGE_VISUAL | TODO_BIND |
| 74 | home | `archive/converted-prd/app/home/assets/media/image45.png` | Select Wallet | knowledge-base/home/app-home.md | PAGE_VISUAL | TODO_BIND |
| 75 | home | `archive/converted-prd/app/home/assets/media/image46.jpeg` | 7. DTC渠道接口需求 | knowledge-base/home/app-home.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 76 | home | `archive/converted-prd/app/home/assets/media/image47.jpeg` | 7. DTC渠道接口需求 | knowledge-base/home/app-home.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 77 | account | `archive/converted-prd/app/registration-login/assets/media/image1.png` | 1. 需求变更日志 | knowledge-base/account/login.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 78 | account | `archive/converted-prd/app/registration-login/assets/media/image2.png` | 1. 需求变更日志 | knowledge-base/account/login.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 79 | account | `archive/converted-prd/app/registration-login/assets/media/image3.png` | 1. 需求变更日志 | knowledge-base/account/login.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 80 | account | `archive/converted-prd/app/registration-login/assets/media/image4.png` | 1. 需求变更日志 | knowledge-base/account/login.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 81 | account | `archive/converted-prd/app/registration-login/assets/media/image5.png` | 1. 需求变更日志 | knowledge-base/account/login.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 82 | account | `archive/converted-prd/app/registration-login/assets/media/image6.png` | 1. 需求变更日志 | knowledge-base/account/login.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 83 | account | `archive/converted-prd/app/registration-login/assets/media/image7.png` | 1. 需求变更日志 | knowledge-base/account/login.md | PAGE_VISUAL | TODO_BIND |
| 84 | account | `archive/converted-prd/app/registration-login/assets/media/image8.png` | 1. 需求变更日志 | knowledge-base/account/login.md | PAGE_VISUAL | TODO_BIND |
| 85 | account | `archive/converted-prd/app/registration-login/assets/media/image9.png` | 1. 需求变更日志 | knowledge-base/account/login.md | PAGE_VISUAL | TODO_BIND |
| 86 | account | `archive/converted-prd/app/registration-login/assets/media/image10.png` | Enable BIO Page | knowledge-base/account/login.md | PAGE_VISUAL | TODO_BIND |
| 87 | account | `archive/converted-prd/app/registration-login/assets/media/image11.png` | 1. 需求变更日志 | knowledge-base/account/login.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 88 | account | `archive/converted-prd/app/registration-login/assets/media/image12.png` | 1. 需求变更日志 | knowledge-base/account/login.md | PAGE_VISUAL | TODO_BIND |
| 89 | account | `archive/converted-prd/app/registration-login/assets/media/image13.png` | 1. 需求变更日志 | knowledge-base/account/login.md | PAGE_VISUAL | TODO_BIND |
| 90 | account | `archive/converted-prd/app/registration-login/assets/media/image14.jpeg` | 4. 功能结构 | knowledge-base/account/login.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 91 | account | `archive/converted-prd/app/registration-login/assets/media/image15.jpeg` | 6. 全局规则 | knowledge-base/account/login.md | PAGE_VISUAL | TODO_BIND |
| 92 | account | `archive/converted-prd/app/registration-login/assets/media/image16.jpeg` | 7. 需求描述 | knowledge-base/account/login.md | PAGE_VISUAL | TODO_BIND |
| 93 | account | `archive/converted-prd/app/registration-login/assets/media/image17.jpeg` | 7. 需求描述 | knowledge-base/account/login.md | PAGE_VISUAL | TODO_BIND |
| 94 | account | `archive/converted-prd/app/registration-login/assets/media/image18.png` | 7. 需求描述 | knowledge-base/account/login.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 95 | account | `archive/converted-prd/app/registration-login/assets/media/image19.png` | 7. 需求描述 | knowledge-base/account/login.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 96 | account | `archive/converted-prd/app/registration-login/assets/media/image20.png` | 7. 需求描述 | knowledge-base/account/login.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 97 | account | `archive/converted-prd/app/registration-login/assets/media/image21.png` | 7. 需求描述 | knowledge-base/account/login.md | PAGE_VISUAL | TODO_BIND |
| 98 | account | `archive/converted-prd/app/registration-login/assets/media/image22.png` | 7. 需求描述 | knowledge-base/account/login.md | PAGE_VISUAL | TODO_BIND |
| 99 | account | `archive/converted-prd/app/registration-login/assets/media/image23.png` | 7. 需求描述 | knowledge-base/account/login.md | PAGE_VISUAL | TODO_BIND |
| 100 | account | `archive/converted-prd/app/registration-login/assets/media/image24.png` | 7. 需求描述 | knowledge-base/account/login.md | PAGE_VISUAL | TODO_BIND |
| 101 | account | `archive/converted-prd/app/registration-login/assets/media/image23.png` | 7. 需求描述 | knowledge-base/account/login.md | PAGE_VISUAL | TODO_BIND |
| 102 | account | `archive/converted-prd/app/registration-login/assets/media/image25.png` | 7. 需求描述 | knowledge-base/account/login.md | PAGE_VISUAL | TODO_BIND |
| 103 | account | `archive/converted-prd/app/registration-login/assets/media/image26.png` | 7. 需求描述 | knowledge-base/account/login.md | PAGE_VISUAL | TODO_BIND |
| 104 | account | `archive/converted-prd/app/registration-login/assets/media/image27.png` | 7. 需求描述 | knowledge-base/account/login.md | PAGE_VISUAL | TODO_BIND |
| 105 | account | `archive/converted-prd/app/registration-login/assets/media/image28.jpeg` | Login Page | knowledge-base/account/login.md | PAGE_VISUAL | TODO_BIND |
| 106 | account | `archive/converted-prd/app/registration-login/assets/media/image29.jpeg` | Login Page | knowledge-base/account/login.md | PAGE_VISUAL | TODO_BIND |
| 107 | account | `archive/converted-prd/app/registration-login/assets/media/image30.png` | 7. 需求描述 | knowledge-base/account/login.md | PAGE_VISUAL | TODO_BIND |
| 108 | account | `archive/converted-prd/app/registration-login/assets/media/image31.png` | Select Country Page | knowledge-base/account/login.md | PAGE_VISUAL | TODO_BIND |
| 109 | account | `archive/converted-prd/app/registration-login/assets/media/image32.png` | 7. 需求描述 | knowledge-base/account/login.md | PAGE_VISUAL | TODO_BIND |
| 110 | account | `archive/converted-prd/app/registration-login/assets/media/image33.jpeg` | 7. 需求描述 | knowledge-base/account/login.md | PAGE_VISUAL | TODO_BIND |
| 111 | account | `archive/converted-prd/app/registration-login/assets/media/image34.jpeg` | 7. 需求描述 | knowledge-base/account/login.md | PAGE_VISUAL | TODO_BIND |
| 112 | account | `archive/converted-prd/app/registration-login/assets/media/image35.png` | 7. 需求描述 | knowledge-base/account/login.md | PAGE_VISUAL | TODO_BIND |
| 113 | account | `archive/converted-prd/app/registration-login/assets/media/image36.jpeg` | 7. 需求描述 | knowledge-base/account/login.md | PAGE_VISUAL | TODO_BIND |
| 114 | account | `archive/converted-prd/app/registration-login/assets/media/image37.jpeg` | 7. 需求描述 | knowledge-base/account/login.md | PAGE_VISUAL | TODO_BIND |
| 115 | account | `archive/converted-prd/app/registration-login/assets/media/image38.png` | 7. 需求描述 | knowledge-base/account/login.md | PAGE_VISUAL | TODO_BIND |
| 116 | account | `archive/converted-prd/app/registration-login/assets/media/image39.png` | 7. 需求描述 | knowledge-base/account/login.md | PAGE_VISUAL | TODO_BIND |
| 117 | account | `archive/converted-prd/app/registration-login/assets/media/image40.jpeg` | set Password Page | knowledge-base/account/login.md | PAGE_VISUAL | TODO_BIND |
| 118 | account | `archive/converted-prd/app/registration-login/assets/media/image41.jpeg` | 7. 需求描述 | knowledge-base/account/login.md | PAGE_VISUAL | TODO_BIND |
| 119 | account | `archive/converted-prd/app/registration-login/assets/media/image31.png` | Select Country Page | knowledge-base/account/login.md | PAGE_VISUAL | TODO_BIND |
| 120 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image1.jpeg` | 2. 全局说明 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 121 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image2.png` | 3. 状态及类型处理 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 122 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image3.png` | 3. 状态及类型处理 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 123 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image4.jpeg` | 3. 状态及类型处理 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 124 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image5.png` | 4. 数据字典 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 125 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image6.png` | 4. 数据字典 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 126 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image7.png` | 4. 数据字典 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 127 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image8.png` | 4. 数据字典 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 128 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image9.png` | 4. 数据字典 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 129 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image10.png` | 4. 数据字典 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 130 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image11.png` | 5. 映射关系（交易记录） | knowledge-base/transaction/history.md | PAGE_VISUAL | TODO_BIND |
| 131 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image12.jpeg` | 6. 时区显示 | knowledge-base/transaction/history.md | PAGE_VISUAL | TODO_BIND |
| 132 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image13.png` | 7. AIX前端功能需求 | knowledge-base/transaction/history.md | PAGE_VISUAL | TODO_BIND |
| 133 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image14.png` | 7. AIX前端功能需求 | knowledge-base/transaction/history.md | PAGE_VISUAL | TODO_BIND |
| 134 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image15.png` | 7. AIX前端功能需求 | knowledge-base/transaction/history.md | PAGE_VISUAL | TODO_BIND |
| 135 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image16.png` | 7. AIX前端功能需求 | knowledge-base/transaction/history.md | PAGE_VISUAL | TODO_BIND |
| 136 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image17.png` | 7. AIX前端功能需求 | knowledge-base/transaction/history.md | PAGE_VISUAL | TODO_BIND |
| 137 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image18.png` | Card History | knowledge-base/transaction/history.md | PAGE_VISUAL | TODO_BIND |
| 138 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image19.jpeg` | 7. AIX前端功能需求 | knowledge-base/transaction/history.md | PAGE_VISUAL | TODO_BIND |
| 139 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image20.png` | 7. AIX前端功能需求 | knowledge-base/transaction/history.md | PAGE_VISUAL | TODO_BIND |
| 140 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image21.png` | Card History | knowledge-base/transaction/history.md | PAGE_VISUAL | TODO_BIND |
| 141 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image22.png` | Card History | knowledge-base/transaction/history.md | PAGE_VISUAL | TODO_BIND |
| 142 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image23.png` | Card History | knowledge-base/transaction/history.md | PAGE_VISUAL | TODO_BIND |
| 143 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image24.png` | Card History | knowledge-base/transaction/history.md | PAGE_VISUAL | TODO_BIND |
| 144 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image25.png` | Card History | knowledge-base/transaction/history.md | PAGE_VISUAL | TODO_BIND |
| 145 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image26.png` | Transaction Details | knowledge-base/transaction/history.md | PAGE_VISUAL | TODO_BIND |
| 146 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image27.png` | Transaction Details | knowledge-base/transaction/history.md | PAGE_VISUAL | TODO_BIND |
| 147 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image28.png` | Transaction Details | knowledge-base/transaction/history.md | PAGE_VISUAL | TODO_BIND |
| 148 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image29.png` | Transaction Details | knowledge-base/transaction/history.md | PAGE_VISUAL | TODO_BIND |
| 149 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image30.png` | Transaction Details | knowledge-base/transaction/history.md | PAGE_VISUAL | TODO_BIND |
| 150 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image31.png` | Transaction Details | knowledge-base/transaction/history.md | PAGE_VISUAL | TODO_BIND |
| 151 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image32.png` | Transaction Details | knowledge-base/transaction/history.md | PAGE_VISUAL | TODO_BIND |
| 152 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image33.png` | Transaction Details | knowledge-base/transaction/history.md | PAGE_VISUAL | TODO_BIND |
| 153 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image34.png` | Transaction Details | knowledge-base/transaction/history.md | PAGE_VISUAL | TODO_BIND |
| 154 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image35.jpeg` | Transaction Details | knowledge-base/transaction/history.md | PAGE_VISUAL | TODO_BIND |
| 155 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image36.png` | Transaction Details | knowledge-base/transaction/history.md | PAGE_VISUAL | TODO_BIND |
| 156 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image37.png` | Transaction Details | knowledge-base/transaction/history.md | PAGE_VISUAL | TODO_BIND |
| 157 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image38.png` | Swap | knowledge-base/transaction/history.md | PAGE_VISUAL | TODO_BIND |
| 158 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image39.png` | Swap | knowledge-base/transaction/history.md | PAGE_VISUAL | TODO_BIND |
| 159 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image40.png` | Swap | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 160 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image36.png` | Swap | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 161 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image41.jpeg` | 8. DTC渠道接口需求 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 162 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image42.png` | 8. DTC渠道接口需求 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 163 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image43.png` | 8. DTC渠道接口需求 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 164 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image44.png` | 8. DTC渠道接口需求 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 165 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image45.jpeg` | 8. DTC渠道接口需求 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 166 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image46.png` | 8. DTC渠道接口需求 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 167 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image43.png` | 8. DTC渠道接口需求 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 168 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image47.png` | 8. DTC渠道接口需求 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 169 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image43.png` | 8. DTC渠道接口需求 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 170 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image48.jpeg` | 8. DTC渠道接口需求 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 171 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image49.png` | 8. DTC渠道接口需求 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 172 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image50.png` | 8. DTC渠道接口需求 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 173 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image51.png` | 8. DTC渠道接口需求 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 174 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image52.jpeg` | 8. DTC渠道接口需求 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 175 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image53.png` | 8. DTC渠道接口需求 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 176 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image54.png` | 8. DTC渠道接口需求 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 177 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image55.png` | 8. DTC渠道接口需求 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 178 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image56.jpeg` | 8. DTC渠道接口需求 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 179 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image57.png` | 8. DTC渠道接口需求 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 180 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image58.png` | 8. DTC渠道接口需求 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 181 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image59.png` | 8. DTC渠道接口需求 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 182 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image60.jpeg` | 8. DTC渠道接口需求 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 183 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image61.png` | 8. DTC渠道接口需求 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 184 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image62.png` | 8. DTC渠道接口需求 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 185 | transaction | `archive/converted-prd/app/transaction-history/assets/media/image63.png` | 8. DTC渠道接口需求 | knowledge-base/transaction/history.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 186 | card/application | `archive/converted-prd/card/application/assets/media/image1.jpeg` | 4. Card申请单状态 | knowledge-base/card/application.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 187 | card/application | `archive/converted-prd/card/application/assets/media/image2.jpeg` | 申卡入口 | knowledge-base/card/application.md | PAGE_VISUAL | TODO_BIND |
| 188 | card/application | `archive/converted-prd/card/application/assets/media/image3.png` | 申卡入口 | knowledge-base/card/application.md | PAGE_VISUAL | TODO_BIND |
| 189 | card/application | `archive/converted-prd/card/application/assets/media/image4.png` | 申卡入口 | knowledge-base/card/application.md | PAGE_VISUAL | TODO_BIND |
| 190 | card/application | `archive/converted-prd/card/application/assets/media/image5.png` | 申卡入口 | knowledge-base/card/application.md | PAGE_VISUAL | TODO_BIND |
| 191 | card/application | `archive/converted-prd/card/application/assets/media/image6.png` | 申卡入口 | knowledge-base/card/application.md | PAGE_VISUAL | TODO_BIND |
| 192 | card/application | `archive/converted-prd/card/application/assets/media/image7.png` | 申卡入口 | knowledge-base/card/application.md | PAGE_VISUAL | TODO_BIND |
| 193 | card/application | `archive/converted-prd/card/application/assets/media/image8.png` | 申卡入口 | knowledge-base/card/application.md | PAGE_VISUAL | TODO_BIND |
| 194 | card/application | `archive/converted-prd/card/application/assets/media/image9.png` | 申卡入口 | knowledge-base/card/application.md | PAGE_VISUAL | TODO_BIND |
| 195 | card/application | `archive/converted-prd/card/application/assets/media/image10.png` | 申卡入口 | knowledge-base/card/application.md | PAGE_VISUAL | TODO_BIND |
| 196 | card/application | `archive/converted-prd/card/application/assets/media/image11.png` | 申卡入口 | knowledge-base/card/application.md | PAGE_VISUAL | TODO_BIND |
| 197 | card/application | `archive/converted-prd/card/application/assets/media/image12.png` | 6. AIX前端功能需求 | knowledge-base/card/application.md | PAGE_VISUAL | TODO_BIND |
| 198 | card/application | `archive/converted-prd/card/application/assets/media/image13.png` | 6. AIX前端功能需求 | knowledge-base/card/application.md | PAGE_VISUAL | TODO_BIND |
| 199 | card/application | `archive/converted-prd/card/application/assets/media/image14.png` | 6. AIX前端功能需求 | knowledge-base/card/application.md | PAGE_VISUAL | TODO_BIND |
| 200 | card/application | `archive/converted-prd/card/application/assets/media/image15.png` | 6. AIX前端功能需求 | knowledge-base/card/application.md | PAGE_VISUAL | TODO_BIND |
| 201 | card/application | `archive/converted-prd/card/application/assets/media/image16.png` | 6. AIX前端功能需求 | knowledge-base/card/application.md | PAGE_VISUAL | TODO_BIND |
| 202 | card/application | `archive/converted-prd/card/application/assets/media/image17.png` | Select Crypto | knowledge-base/card/application.md | PAGE_VISUAL | TODO_BIND |
| 203 | card/application | `archive/converted-prd/card/application/assets/media/image18.png` | Select Crypto | knowledge-base/card/application.md | PAGE_VISUAL | TODO_BIND |
| 204 | card/application | `archive/converted-prd/card/application/assets/media/image19.png` | Select Crypto | knowledge-base/card/application.md | PAGE_VISUAL | TODO_BIND |
| 205 | card/application | `archive/converted-prd/card/application/assets/media/image20.png` | 6. AIX前端功能需求 | knowledge-base/card/application.md | PAGE_VISUAL | TODO_BIND |
| 206 | card/application | `archive/converted-prd/card/application/assets/media/image21.png` | 6. AIX前端功能需求 | knowledge-base/card/application.md | PAGE_VISUAL | TODO_BIND |
| 207 | card/application | `archive/converted-prd/card/application/assets/media/image22.png` | 6. AIX前端功能需求 | knowledge-base/card/application.md | PAGE_VISUAL | TODO_BIND |
| 208 | card/application | `archive/converted-prd/card/application/assets/media/image23.png` | 6. AIX前端功能需求 | knowledge-base/card/application.md | PAGE_VISUAL | TODO_BIND |
| 209 | card/application | `archive/converted-prd/card/application/assets/media/image24.png` | 6. AIX前端功能需求 | knowledge-base/card/application.md | PAGE_VISUAL | TODO_BIND |
| 210 | card/application | `archive/converted-prd/card/application/assets/media/image25.png` | 6. AIX前端功能需求 | knowledge-base/card/application.md | PAGE_VISUAL | TODO_BIND |
| 211 | card/application | `archive/converted-prd/card/application/assets/media/image26.png` | 6. AIX前端功能需求 | knowledge-base/card/application.md | PAGE_VISUAL | TODO_BIND |
| 212 | card/application | `archive/converted-prd/card/application/assets/media/image27.png` | 6. AIX前端功能需求 | knowledge-base/card/application.md | PAGE_VISUAL | TODO_BIND |
| 213 | card/application | `archive/converted-prd/card/application/assets/media/image28.png` | 6. AIX前端功能需求 | knowledge-base/card/application.md | PAGE_VISUAL | TODO_BIND |
| 214 | card/application | `archive/converted-prd/card/application/assets/media/image29.png` | 6. AIX前端功能需求 | knowledge-base/card/application.md | PAGE_VISUAL | TODO_BIND |
| 215 | card/application | `archive/converted-prd/card/application/assets/media/image30.png` | 6. AIX前端功能需求 | knowledge-base/card/application.md | PAGE_VISUAL | TODO_BIND |
| 216 | card/application | `archive/converted-prd/card/application/assets/media/image31.png` | 6. AIX前端功能需求 | knowledge-base/card/application.md | PAGE_VISUAL | TODO_BIND |
| 217 | card/application | `archive/converted-prd/card/application/assets/media/image32.png` | 6. AIX前端功能需求 | knowledge-base/card/application.md | PAGE_VISUAL | TODO_BIND |
| 218 | card/application | `archive/converted-prd/card/application/assets/media/image26.png` | 6. AIX前端功能需求 | knowledge-base/card/application.md | PAGE_VISUAL | TODO_BIND |
| 219 | card/application | `archive/converted-prd/card/application/assets/media/image33.png` | 6. AIX前端功能需求 | knowledge-base/card/application.md | PAGE_VISUAL | TODO_BIND |
| 220 | card/application | `archive/converted-prd/card/application/assets/media/image34.png` | 6. AIX前端功能需求 | knowledge-base/card/application.md | PAGE_VISUAL | TODO_BIND |
| 221 | card/application | `archive/converted-prd/card/application/assets/media/image35.png` | 6. AIX前端功能需求 | knowledge-base/card/application.md | PAGE_VISUAL | TODO_BIND |
| 222 | card/application | `archive/converted-prd/card/application/assets/media/image36.png` | 6. AIX前端功能需求 | knowledge-base/card/application.md | PAGE_VISUAL | TODO_BIND |
| 223 | card/application | `archive/converted-prd/card/application/assets/media/image37.png` | 6. AIX前端功能需求 | knowledge-base/card/application.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 224 | card/application | `archive/converted-prd/card/application/assets/media/image38.png` | 6. AIX前端功能需求 | knowledge-base/card/application.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 225 | card/application | `archive/converted-prd/card/application/assets/media/image39.png` | 6. AIX前端功能需求 | knowledge-base/card/application.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 226 | card/application | `archive/converted-prd/card/application/assets/media/image40.png` | 当前卡片展示 | knowledge-base/card/application.md | PAGE_VISUAL | TODO_BIND |
| 227 | card/application | `archive/converted-prd/card/application/assets/media/image41.png` | 当前卡片展示 | knowledge-base/card/application.md | PAGE_VISUAL | TODO_BIND |
| 228 | card/application | `archive/converted-prd/card/application/assets/media/image42.png` | 当前卡片展示 | knowledge-base/card/application.md | PAGE_VISUAL | TODO_BIND |
| 229 | card/application | `archive/converted-prd/card/application/assets/media/image43.png` | Activate Card | knowledge-base/card/application.md | PAGE_VISUAL | TODO_BIND |
| 230 | card/application | `archive/converted-prd/card/application/assets/media/image44.png` | Activate Card | knowledge-base/card/application.md | PAGE_VISUAL | TODO_BIND |
| 231 | card/application | `archive/converted-prd/card/application/assets/media/image45.png` | Activate Card | knowledge-base/card/application.md | PAGE_VISUAL | TODO_BIND |
| 232 | card/application | `archive/converted-prd/card/application/assets/media/image46.png` | Activate Card | knowledge-base/card/application.md | PAGE_VISUAL | TODO_BIND |
| 233 | card/application | `archive/converted-prd/card/application/assets/media/image47.png` | 申卡入口 | knowledge-base/card/application.md | PAGE_VISUAL | TODO_BIND |
| 234 | card/application | `archive/converted-prd/card/application/assets/media/image48.png` | 申卡入口 | knowledge-base/card/application.md | PAGE_VISUAL | TODO_BIND |
| 235 | card/application | `archive/converted-prd/card/application/assets/media/image49.png` | 申卡入口 | knowledge-base/card/application.md | PAGE_VISUAL | TODO_BIND |
| 236 | card/application | `archive/converted-prd/card/application/assets/media/image50.png` | 申卡入口 | knowledge-base/card/application.md | PAGE_VISUAL | TODO_BIND |
| 237 | card/application | `archive/converted-prd/card/application/assets/media/image51.png` | 申卡入口 | knowledge-base/card/application.md | PAGE_VISUAL | TODO_BIND |
| 238 | card/application | `archive/converted-prd/card/application/assets/media/image52.png` | 当前卡片展示 | knowledge-base/card/application.md | PAGE_VISUAL | TODO_BIND |
| 239 | card/application | `archive/converted-prd/card/application/assets/media/image53.png` | 当前卡片展示 | knowledge-base/card/application.md | PAGE_VISUAL | TODO_BIND |
| 240 | card/application | `archive/converted-prd/card/application/assets/media/image54.png` | Activate card | knowledge-base/card/application.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 241 | card/application | `archive/converted-prd/card/application/assets/media/image55.jpeg` | 7. DTC渠道接口需求 | knowledge-base/card/application.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 242 | card/application | `archive/converted-prd/card/application/assets/media/image56.jpeg` | 7. DTC渠道接口需求 | knowledge-base/card/application.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 243 | card/application | `archive/converted-prd/card/application/assets/media/image57.jpeg` | 7. DTC渠道接口需求 | knowledge-base/card/application.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 244 | card/application | `archive/converted-prd/card/application/assets/media/image58.jpeg` | 7. DTC渠道接口需求 | knowledge-base/card/application.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 245 | card/application | `archive/converted-prd/card/application/assets/media/image59.jpeg` | 7. DTC渠道接口需求 | knowledge-base/card/application.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 246 | card/application | `archive/converted-prd/card/application/assets/media/image60.jpeg` | 7. DTC渠道接口需求 | knowledge-base/card/application.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 247 | card/application | `archive/converted-prd/card/application/assets/media/image61.jpeg` | 7. DTC渠道接口需求 | knowledge-base/card/application.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 248 | card/manage | `archive/converted-prd/card/manage/assets/media/image2.png` | set pin | knowledge-base/card/manage/_index.md | PAGE_VISUAL | TODO_BIND |
| 249 | card/manage | `archive/converted-prd/card/manage/assets/media/image3.png` | 1. 需求变更日志 | knowledge-base/card/manage/_index.md | PAGE_VISUAL | TODO_BIND |
| 250 | card/manage | `archive/converted-prd/card/manage/assets/media/image4.jpeg` | 4. 功能结构 | knowledge-base/card/manage/_index.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 251 | card/manage | `archive/converted-prd/card/manage/assets/media/image5.jpeg` | 6. 全局规则 | knowledge-base/card/manage/_index.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 252 | card/manage | `archive/converted-prd/card/manage/assets/media/image6.jpeg` | 6. 全局规则 | knowledge-base/card/manage/_index.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 253 | card/manage | `archive/converted-prd/card/manage/assets/media/image7.jpeg` | 6. 全局规则 | knowledge-base/card/manage/_index.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 254 | card/manage | `archive/converted-prd/card/manage/assets/media/image8.png` | 6. 全局规则 | knowledge-base/card/manage/_index.md | PAGE_VISUAL | TODO_BIND |
| 255 | card/manage | `archive/converted-prd/card/manage/assets/media/image9.png` | 6. 全局规则 | knowledge-base/card/manage/_index.md | PAGE_VISUAL | TODO_BIND |
| 256 | card/manage | `archive/converted-prd/card/manage/assets/media/image10.png` | 6. 全局规则 | knowledge-base/card/manage/_index.md | PAGE_VISUAL | TODO_BIND |
| 257 | card/manage | `archive/converted-prd/card/manage/assets/media/image11.png` | 6. 全局规则 | knowledge-base/card/manage/_index.md | PAGE_VISUAL | TODO_BIND |
| 258 | card/manage | `archive/converted-prd/card/manage/assets/media/image12.jpeg` | Card home | knowledge-base/card/manage/_index.md | PAGE_VISUAL | TODO_BIND |
| 259 | card/manage | `archive/converted-prd/card/manage/assets/media/image13.jpeg` | Card home | knowledge-base/card/manage/_index.md | PAGE_VISUAL | TODO_BIND |
| 260 | card/manage | `archive/converted-prd/card/manage/assets/media/image14.png` | 7. 需求描述 | knowledge-base/card/manage/_index.md | PAGE_VISUAL | TODO_BIND |
| 261 | card/manage | `archive/converted-prd/card/manage/assets/media/image15.png` | 7. 需求描述 | knowledge-base/card/manage/_index.md | PAGE_VISUAL | TODO_BIND |
| 262 | card/manage | `archive/converted-prd/card/manage/assets/media/image16.png` | 7. 需求描述 | knowledge-base/card/manage/_index.md | PAGE_VISUAL | TODO_BIND |
| 263 | card/manage | `archive/converted-prd/card/manage/assets/media/image17.jpeg` | 7. 需求描述 | knowledge-base/card/manage/_index.md | PAGE_VISUAL | TODO_BIND |
| 264 | card/manage | `archive/converted-prd/card/manage/assets/media/image18.png` | 7. 需求描述 | knowledge-base/card/manage/_index.md | PAGE_VISUAL | TODO_BIND |
| 265 | card/manage | `archive/converted-prd/card/manage/assets/media/image19.png` | Card Home | knowledge-base/card/manage/_index.md | PAGE_VISUAL | TODO_BIND |
| 266 | card/manage | `archive/converted-prd/card/manage/assets/media/image20.png` | Card Home | knowledge-base/card/manage/_index.md | PAGE_VISUAL | TODO_BIND |
| 267 | card/manage | `archive/converted-prd/card/manage/assets/media/image21.png` | Card Home | knowledge-base/card/manage/_index.md | PAGE_VISUAL | TODO_BIND |
| 268 | card/manage | `archive/converted-prd/card/manage/assets/media/image22.jpeg` | Set PIN | knowledge-base/card/manage/_index.md | PAGE_VISUAL | TODO_BIND |
| 269 | card/manage | `archive/converted-prd/card/manage/assets/media/image23.jpeg` | Set PIN | knowledge-base/card/manage/_index.md | PAGE_VISUAL | TODO_BIND |
| 270 | card/manage | `archive/converted-prd/card/manage/assets/media/image24.png` | 7. 需求描述 | knowledge-base/card/manage/_index.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 271 | card/manage | `archive/converted-prd/card/manage/assets/media/image25.png` | Set PIN | knowledge-base/card/manage/_index.md | PAGE_VISUAL | TODO_BIND |
| 272 | card/manage | `archive/converted-prd/card/manage/assets/media/image26.png` | Set PIN | knowledge-base/card/manage/_index.md | PAGE_VISUAL | TODO_BIND |
| 273 | card/manage | `archive/converted-prd/card/manage/assets/media/image27.png` | Set PIN | knowledge-base/card/manage/_index.md | PAGE_VISUAL | TODO_BIND |
| 274 | card/manage | `archive/converted-prd/card/manage/assets/media/image19.png` | Set PIN | knowledge-base/card/manage/_index.md | PAGE_VISUAL | TODO_BIND |
| 275 | card/manage | `archive/converted-prd/card/manage/assets/media/image28.png` | 7. 需求描述 | knowledge-base/card/manage/_index.md | PAGE_VISUAL | TODO_BIND |
| 276 | card/manage | `archive/converted-prd/card/manage/assets/media/image29.jpeg` | 7. 需求描述 | knowledge-base/card/manage/_index.md | PAGE_VISUAL | TODO_BIND |
| 277 | card/manage | `archive/converted-prd/card/manage/assets/media/image30.jpeg` | 7. 需求描述 | knowledge-base/card/manage/_index.md | PAGE_VISUAL | TODO_BIND |
| 278 | card/manage | `archive/converted-prd/card/manage/assets/media/image31.png` | Card Home | knowledge-base/card/manage/_index.md | PAGE_VISUAL | TODO_BIND |
| 279 | card/manage | `archive/converted-prd/card/manage/assets/media/image32.jpeg` | 7. 需求描述 | knowledge-base/card/manage/_index.md | PAGE_VISUAL | TODO_BIND |
| 280 | card/manage | `archive/converted-prd/card/manage/assets/media/image33.jpeg` | 7. 需求描述 | knowledge-base/card/manage/_index.md | PAGE_VISUAL | TODO_BIND |
| 281 | other | `archive/converted-prd/card/me/assets/media/image1.png` | 1. 需求变更日志 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 282 | other | `archive/converted-prd/card/me/assets/media/image2.jpeg` | 1. 需求变更日志 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 283 | other | `archive/converted-prd/card/me/assets/media/image3.jpeg` | 4. 功能结构 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 284 | other | `archive/converted-prd/card/me/assets/media/image4.png` | 6. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL | OUT_OF_SCOPE |
| 285 | other | `archive/converted-prd/card/me/assets/media/image5.png` | 6. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL | OUT_OF_SCOPE |
| 286 | other | `archive/converted-prd/card/me/assets/media/image6.png` | 6. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL | OUT_OF_SCOPE |
| 287 | other | `archive/converted-prd/card/me/assets/media/image7.png` | 6. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL | OUT_OF_SCOPE |
| 288 | other | `archive/converted-prd/card/me/assets/media/image8.png` | 6. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 289 | other | `archive/converted-prd/card/me/assets/media/image9.png` | 6. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 290 | other | `archive/converted-prd/card/me/assets/media/image10.png` | 6. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 291 | other | `archive/converted-prd/card/me/assets/media/image11.png` | 6. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 292 | other | `archive/converted-prd/card/me/assets/media/image12.png` | Set Password Page | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 293 | other | `archive/converted-prd/card/me/assets/media/image13.png` | Set Password Page | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 294 | other | `archive/converted-prd/card/me/assets/media/image14.png` | Set Password Page | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 295 | other | `archive/converted-prd/card/me/assets/media/image15.png` | Re-enter Password Page | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 296 | other | `archive/converted-prd/card/me/assets/media/image16.jpeg` | 6. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 297 | other | `archive/converted-prd/card/me/assets/media/image17.jpeg` | 6. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 298 | other | `archive/converted-prd/card/me/assets/media/image18.jpeg` | 6. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 299 | other | `archive/converted-prd/card/me/assets/media/image19.jpeg` | 6. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 300 | other | `archive/converted-prd/card/me/assets/media/image20.png` | 6. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL | OUT_OF_SCOPE |
| 301 | other | `archive/converted-prd/card/me/assets/media/image21.png` | 6. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL | OUT_OF_SCOPE |
| 302 | other | `archive/converted-prd/card/me/assets/media/image22.png` | 6. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL | OUT_OF_SCOPE |
| 303 | other | `archive/converted-prd/card/me/assets/media/image23.jpeg` | 6. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 304 | other | `archive/converted-prd/card/me/assets/media/image24.png` | 6. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL | OUT_OF_SCOPE |
| 305 | other | `archive/converted-prd/card/me/assets/media/image25.png` | 6. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 306 | card/transaction | `archive/converted-prd/card/transaction/assets/media/image1.jpeg` | 4. 功能结构 | knowledge-base/card/transaction.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 307 | card/transaction | `archive/converted-prd/card/transaction/assets/media/image2.jpeg` | 7. 需求描述 | knowledge-base/card/transaction.md | PAGE_VISUAL | TODO_BIND |
| 308 | other | `archive/converted-prd/common/i18n/assets/media/image1.jpeg` | 3. 系统交互 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL | OUT_OF_SCOPE |
| 309 | other | `archive/converted-prd/common/i18n/assets/media/image2.jpeg` | 3. 系统交互 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL | OUT_OF_SCOPE |
| 310 | other | `archive/converted-prd/common/popup-banner/assets/media/image1.png` | \ 2025-11-27\ AIX+PopUp+banner等能力接入【首页+MGM页面】 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 311 | other | `archive/converted-prd/common/popup-banner/assets/media/image2.png` | \ 2025-11-27\ AIX+PopUp+banner等能力接入【首页+MGM页面】 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 312 | other | `archive/converted-prd/common/popup-banner/assets/media/image3.png` | \ 2025-11-27\ AIX+PopUp+banner等能力接入【首页+MGM页面】 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 313 | other | `archive/converted-prd/common/popup-banner/assets/media/image4.png` | \ 2025-11-27\ AIX+PopUp+banner等能力接入【首页+MGM页面】 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 314 | other | `archive/converted-prd/common/popup-banner/assets/media/image5.png` | \ 2025-11-27\ AIX+PopUp+banner等能力接入【首页+MGM页面】 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 315 | other | `archive/converted-prd/common/popup-banner/assets/media/image6.png` | \ 2025-11-27\ AIX+PopUp+banner等能力接入【首页+MGM页面】 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 316 | other | `archive/converted-prd/common/popup-banner/assets/media/image7.png` | \ 2025-11-27\ AIX+PopUp+banner等能力接入【首页+MGM页面】 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 317 | other | `archive/converted-prd/common/popup-banner/assets/media/image8.png` | \ 2025-11-27\ AIX+PopUp+banner等能力接入【首页+MGM页面】 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 318 | other | `archive/converted-prd/common/popup-banner/assets/media/image9.png` | \ 2025-11-27\ AIX+PopUp+banner等能力接入【首页+MGM页面】 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 319 | other | `archive/converted-prd/common/popup-banner/assets/media/image10.png` | \ 2025-11-27\ AIX+PopUp+banner等能力接入【首页+MGM页面】 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 320 | other | `archive/converted-prd/common/popup-banner/assets/media/image11.png` | \ 2025-11-27\ AIX+PopUp+banner等能力接入【首页+MGM页面】 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 321 | other | `archive/converted-prd/common/popup-banner/assets/media/image12.png` | \ 2025-11-27\ AIX+PopUp+banner等能力接入【首页+MGM页面】 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 322 | other | `archive/converted-prd/common/popup-banner/assets/media/image13.jpeg` | \ 2025-11-27\ AIX+PopUp+banner等能力接入【首页+MGM页面】 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 323 | other | `archive/converted-prd/common/popup-banner/assets/media/image14.png` | \ 2025-11-27\ AIX+PopUp+banner等能力接入【首页+MGM页面】 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 324 | other | `archive/converted-prd/common/popup-banner/assets/media/image15.png` | \ 2025-11-27\ AIX+PopUp+banner等能力接入【首页+MGM页面】 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 325 | other | `archive/converted-prd/common/popup-banner/assets/media/image16.png` | \ 2025-11-27\ AIX+PopUp+banner等能力接入【首页+MGM页面】 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 326 | other | `archive/converted-prd/common/popup-banner/assets/media/image17.png` | \ 2025-11-27\ AIX+PopUp+banner等能力接入【首页+MGM页面】 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 327 | other | `archive/converted-prd/common/popup-banner/assets/media/image18.png` | \ 2025-11-27\ AIX+PopUp+banner等能力接入【首页+MGM页面】 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 328 | other | `archive/converted-prd/common/popup-banner/assets/media/image19.jpeg` | \ 2025-11-27\ AIX+PopUp+banner等能力接入【首页+MGM页面】 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 329 | other | `archive/converted-prd/common/popup-banner/assets/media/image20.png` | \ 2025-11-27\ AIX+PopUp+banner等能力接入【首页+MGM页面】 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 330 | kyc | `archive/converted-prd/kyc/wallet-opening/assets/media/image1.jpeg` | 4. 功能结构 | knowledge-base/kyc/account-opening.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 331 | kyc | `archive/converted-prd/kyc/wallet-opening/assets/media/image2.jpeg` | 6. 统一规则 | knowledge-base/kyc/account-opening.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 332 | kyc | `archive/converted-prd/kyc/wallet-opening/assets/media/image3.jpeg` | 6. 统一规则 | knowledge-base/kyc/account-opening.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 333 | kyc | `archive/converted-prd/kyc/wallet-opening/assets/media/image4.jpeg` | 7. 需求描述 | knowledge-base/kyc/account-opening.md | PAGE_VISUAL | TODO_BIND |
| 334 | kyc | `archive/converted-prd/kyc/wallet-opening/assets/media/image5.jpeg` | 7. 需求描述 | knowledge-base/kyc/account-opening.md | PAGE_VISUAL | TODO_BIND |
| 335 | kyc | `archive/converted-prd/kyc/wallet-opening/assets/media/image6.jpeg` | 7. 需求描述 | knowledge-base/kyc/account-opening.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 336 | kyc | `archive/converted-prd/kyc/wallet-opening/assets/media/image7.png` | 7. 需求描述 | knowledge-base/kyc/account-opening.md | PAGE_VISUAL | TODO_BIND |
| 337 | kyc | `archive/converted-prd/kyc/wallet-opening/assets/media/image8.png` | 7. 需求描述 | knowledge-base/kyc/account-opening.md | PAGE_VISUAL | TODO_BIND |
| 338 | kyc | `archive/converted-prd/kyc/wallet-opening/assets/media/image9.png` | 7. 需求描述 | knowledge-base/kyc/account-opening.md | PAGE_VISUAL | TODO_BIND |
| 339 | kyc | `archive/converted-prd/kyc/wallet-opening/assets/media/image10.png` | Waitlist | knowledge-base/kyc/account-opening.md | PAGE_VISUAL | TODO_BIND |
| 340 | kyc | `archive/converted-prd/kyc/wallet-opening/assets/media/image11.png` | 7. 需求描述 | knowledge-base/kyc/account-opening.md | PAGE_VISUAL | TODO_BIND |
| 341 | kyc | `archive/converted-prd/kyc/wallet-opening/assets/media/image12.png` | 7. 需求描述 | knowledge-base/kyc/account-opening.md | PAGE_VISUAL | TODO_BIND |
| 342 | kyc | `archive/converted-prd/kyc/wallet-opening/assets/media/image13.png` | 7. 需求描述 | knowledge-base/kyc/account-opening.md | PAGE_VISUAL | TODO_BIND |
| 343 | kyc | `archive/converted-prd/kyc/wallet-opening/assets/media/image14.png` | 7. 需求描述 | knowledge-base/kyc/account-opening.md | PAGE_VISUAL | TODO_BIND |
| 344 | kyc | `archive/converted-prd/kyc/wallet-opening/assets/media/image15.png` | 7. 需求描述 | knowledge-base/kyc/account-opening.md | PAGE_VISUAL | TODO_BIND |
| 345 | kyc | `archive/converted-prd/kyc/wallet-opening/assets/media/image16.png` | Verify Page | knowledge-base/kyc/account-opening.md | PAGE_VISUAL | TODO_BIND |
| 346 | kyc | `archive/converted-prd/kyc/wallet-opening/assets/media/image17.png` | Failed Page | knowledge-base/kyc/account-opening.md | PAGE_VISUAL | TODO_BIND |
| 347 | kyc | `archive/converted-prd/kyc/wallet-opening/assets/media/image18.png` | 7. 需求描述 | knowledge-base/kyc/account-opening.md | PAGE_VISUAL | TODO_BIND |
| 348 | kyc | `archive/converted-prd/kyc/wallet-opening/assets/media/image19.png` | Face Loading | knowledge-base/kyc/account-opening.md | PAGE_VISUAL | TODO_BIND |
| 349 | kyc | `archive/converted-prd/kyc/wallet-opening/assets/media/image6.jpeg` | 7. 需求描述 | knowledge-base/kyc/account-opening.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 350 | kyc | `archive/converted-prd/kyc/wallet-opening/assets/media/image20.png` | Face Loading | knowledge-base/kyc/account-opening.md | PAGE_VISUAL | TODO_BIND |
| 351 | kyc | `archive/converted-prd/kyc/wallet-opening/assets/media/image21.png` | 7. 需求描述 | knowledge-base/kyc/account-opening.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 352 | kyc | `archive/converted-prd/kyc/wallet-opening/assets/media/image22.png` | 7. 需求描述 | knowledge-base/kyc/account-opening.md | PAGE_VISUAL | TODO_BIND |
| 353 | kyc | `archive/converted-prd/kyc/wallet-opening/assets/media/image23.jpeg` | 7. 需求描述 | knowledge-base/kyc/account-opening.md | PAGE_VISUAL | TODO_BIND |
| 354 | kyc | `archive/converted-prd/kyc/wallet-opening/assets/media/image24.png` | 7. 需求描述 | knowledge-base/kyc/account-opening.md | PAGE_VISUAL | TODO_BIND |
| 355 | kyc | `archive/converted-prd/kyc/wallet-opening/assets/media/image25.png` | Verify Page | knowledge-base/kyc/account-opening.md | PAGE_VISUAL | TODO_BIND |
| 356 | kyc | `archive/converted-prd/kyc/wallet-opening/assets/media/image26.png` | Waitlist | knowledge-base/kyc/account-opening.md | PAGE_VISUAL | TODO_BIND |
| 357 | kyc | `archive/converted-prd/kyc/wallet-opening/assets/media/image27.png` | 7. 需求描述 | knowledge-base/kyc/account-opening.md | PAGE_VISUAL | TODO_BIND |
| 358 | other | `archive/converted-prd/mgm/referral-invite-code/assets/media/image1.jpeg` | 5. 整体框架 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 359 | other | `archive/converted-prd/mgm/referral-invite-code/assets/media/image2.jpeg` | 5. 整体框架 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 360 | other | `archive/converted-prd/mgm/referral-invite-code/assets/media/image3.png` | 10. Demo | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL | OUT_OF_SCOPE |
| 361 | other | `archive/converted-prd/mgm/referral-invite-code/assets/media/image4.png` | 12. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 362 | other | `archive/converted-prd/mgm/referral-invite-code/assets/media/image5.png` | 12. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 363 | other | `archive/converted-prd/mgm/referral-invite-code/assets/media/image6.png` | 12. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 364 | other | `archive/converted-prd/mgm/referral-invite-code/assets/media/image7.png` | 12. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 365 | other | `archive/converted-prd/mgm/referral-invite-code/assets/media/image8.png` | 12. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 366 | other | `archive/converted-prd/mgm/referral-invite-code/assets/media/image9.png` | 12. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 367 | other | `archive/converted-prd/mgm/referral-invite-code/assets/media/image10.png` | 12. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 368 | other | `archive/converted-prd/mgm/referral-invite-code/assets/media/image11.png` | 12. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 369 | other | `archive/converted-prd/mgm/referral-invite-code/assets/media/image12.png` | 12. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 370 | other | `archive/converted-prd/mgm/referral-invite-code/assets/media/image13.png` | 12. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 371 | other | `archive/converted-prd/mgm/referral-invite-code/assets/media/image14.png` | 12. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 372 | other | `archive/converted-prd/mgm/referral-invite-code/assets/media/image15.png` | 12. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 373 | other | `archive/converted-prd/mgm/referral-invite-code/assets/media/image16.png` | 12. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 374 | other | `archive/converted-prd/mgm/referral-invite-code/assets/media/image17.png` | 12. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 375 | other | `archive/converted-prd/mgm/referral-invite-code/assets/media/image18.png` | 12. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 376 | other | `archive/converted-prd/mgm/referral-invite-code/assets/media/image19.png` | 12. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 377 | other | `archive/converted-prd/mgm/referral-invite-code/assets/media/image20.png` | 12. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 378 | other | `archive/converted-prd/mgm/referral-invite-code/assets/media/image21.png` | 12. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 379 | other | `archive/converted-prd/mgm/referral-invite-code/assets/media/image22.png` | 12. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 380 | other | `archive/converted-prd/mgm/referral-invite-code/assets/media/image23.png` | 12. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 381 | other | `archive/converted-prd/mgm/referral-invite-code/assets/media/image24.png` | 12. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 382 | other | `archive/converted-prd/mgm/referral-invite-code/assets/media/image25.png` | 12. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 383 | other | `archive/converted-prd/mgm/referral-invite-code/assets/media/image26.png` | 12. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 384 | other | `archive/converted-prd/mgm/referral-invite-code/assets/media/image27.png` | 12. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 385 | other | `archive/converted-prd/mgm/referral-invite-code/assets/media/image28.png` | 12. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 386 | other | `archive/converted-prd/mgm/referral-invite-code/assets/media/image29.png` | 12. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 387 | other | `archive/converted-prd/mgm/referral-invite-code/assets/media/image30.png` | 12. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 388 | other | `archive/converted-prd/mgm/referral-invite-code/assets/media/image31.png` | 12. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 389 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image1.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 390 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image2.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 391 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image3.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 392 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image4.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 393 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image5.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 394 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image6.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 395 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image7.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 396 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image8.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 397 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image9.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 398 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image10.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 399 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image11.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | TODO_BIND |
| 400 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image12.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | TODO_BIND |
| 401 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image13.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | TODO_BIND |
| 402 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image14.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 403 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image15.jpeg` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 404 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image16.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 405 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image17.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 406 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image18.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 407 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image19.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 408 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image20.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | TODO_BIND |
| 409 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image21.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | TODO_BIND |
| 410 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image22.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | TODO_BIND |
| 411 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image23.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | TODO_BIND |
| 412 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image24.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 413 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image25.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 414 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image26.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | TODO_BIND |
| 415 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image26.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | TODO_BIND |
| 416 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image27.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 417 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image27.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 418 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image28.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 419 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image29.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 420 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image30.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 421 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image31.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 422 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image32.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 423 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image33.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 424 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image34.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 425 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image35.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 426 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image36.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 427 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image37.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 428 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image38.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | TODO_BIND |
| 429 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image39.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 430 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image40.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | TODO_BIND |
| 431 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image40.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | TODO_BIND |
| 432 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image41.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 433 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image41.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 434 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image42.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 435 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image29.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 436 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image30.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 437 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image31.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 438 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image32.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 439 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image33.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 440 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image34.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 441 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image35.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 442 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image36.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 443 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image37.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 444 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image38.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | TODO_BIND |
| 445 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image43.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 446 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image44.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | TODO_BIND |
| 447 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image41.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 448 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image41.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 449 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image45.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 450 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image29.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 451 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image46.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 452 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image31.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 453 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image32.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 454 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image33.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 455 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image34.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 456 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image35.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 457 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image36.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 458 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image37.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 459 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image38.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | TODO_BIND |
| 460 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image47.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 461 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image48.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | TODO_BIND |
| 462 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image48.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | TODO_BIND |
| 463 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image41.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 464 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image41.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 465 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image28.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 466 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image29.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 467 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image30.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 468 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image31.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 469 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image32.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | TODO_BIND |
| 470 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image33.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | TODO_BIND |
| 471 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image34.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | TODO_BIND |
| 472 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image35.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 473 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image36.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 474 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image37.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 475 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image38.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | TODO_BIND |
| 476 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image49.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 477 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image48.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | TODO_BIND |
| 478 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image48.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | TODO_BIND |
| 479 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image50.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 480 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image50.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 481 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image28.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 482 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image29.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 483 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image30.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 484 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image31.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 485 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image32.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | TODO_BIND |
| 486 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image33.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | TODO_BIND |
| 487 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image34.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | TODO_BIND |
| 488 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image35.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 489 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image36.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 490 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image37.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 491 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image38.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | TODO_BIND |
| 492 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image51.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 493 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image52.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | TODO_BIND |
| 494 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image52.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | TODO_BIND |
| 495 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image53.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 496 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image53.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 497 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image28.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 498 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image29.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 499 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image30.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 500 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image31.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 501 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image32.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 502 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image33.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 503 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image34.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 504 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image35.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 505 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image36.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 506 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image37.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 507 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image38.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | TODO_BIND |
| 508 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image54.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 509 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image55.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 510 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image56.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 511 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image57.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 512 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image58.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 513 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image59.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 514 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image60.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 515 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image61.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 516 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image30.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 517 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image62.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 518 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image63.png` | 1. 修订记录 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 519 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image37.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | TODO_BIND |
| 520 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image64.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | TODO_BIND |
| 521 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image65.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | TODO_BIND |
| 522 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image66.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | TODO_BIND |
| 523 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image67.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | TODO_BIND |
| 524 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image68.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | TODO_BIND |
| 525 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image69.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | TODO_BIND |
| 526 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image70.png` | 1. 修订记录 | knowledge-base/common/notification.md | PAGE_VISUAL | TODO_BIND |
| 527 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image71.png` | 1. 加密钱包交易类webhook | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 528 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image72.png` | 1. 加密钱包交易类webhook | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 529 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image73.png` | 2. 卡交易类webhook | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 530 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image74.png` | 3. 卡状态变更 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 531 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image75.png` | 4. 其他可见 | knowledge-base/common/notification.md | PAGE_VISUAL | TODO_BIND |
| 532 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image76.png` | 4. 其他可见 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 533 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image77.png` | 4. 其他可见 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 534 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image78.png` | 4. 其他可见 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 535 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image79.png` | 4. 其他可见 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 536 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image80.png` | 4. 其他可见 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 537 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image81.png` | 4. 其他可见 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 538 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image82.png` | 4. 其他可见 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 539 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image83.png` | 4. 其他可见 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 540 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image29.png` | 4. 其他可见 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 541 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image31.png` | 4. 其他可见 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 542 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image32.png` | 4. 其他可见 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 543 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image33.png` | 4. 其他可见 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 544 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image35.png` | 4. 其他可见 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 545 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image36.png` | 4. 其他可见 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 546 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image37.png` | 4. 其他可见 | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 547 | notification | `archive/converted-prd/notification/push-inbox/assets/media/image38.png` | 4. 其他可见 | knowledge-base/common/notification.md | PAGE_VISUAL | TODO_BIND |
| 548 | notification | `archive/converted-prd/notification/system-email/assets/media/image1.jpeg` | 3. demo | knowledge-base/common/notification.md | PAGE_VISUAL | TODO_BIND |
| 549 | notification | `archive/converted-prd/notification/system-email/assets/media/image2.jpeg` | 4. Interface interaction | knowledge-base/common/notification.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 550 | other | `archive/converted-prd/oboss/capabilities/assets/media/image1.jpg` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 551 | other | `archive/converted-prd/oboss/capabilities/assets/media/image2.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 552 | other | `archive/converted-prd/oboss/capabilities/assets/media/image3.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 553 | other | `archive/converted-prd/oboss/capabilities/assets/media/image4.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 554 | other | `archive/converted-prd/oboss/capabilities/assets/media/image5.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 555 | other | `archive/converted-prd/oboss/capabilities/assets/media/image6.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 556 | other | `archive/converted-prd/oboss/capabilities/assets/media/image7.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 557 | other | `archive/converted-prd/oboss/capabilities/assets/media/image8.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 558 | other | `archive/converted-prd/oboss/capabilities/assets/media/image9.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 559 | other | `archive/converted-prd/oboss/capabilities/assets/media/image10.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 560 | other | `archive/converted-prd/oboss/capabilities/assets/media/image11.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL | OUT_OF_SCOPE |
| 561 | other | `archive/converted-prd/oboss/capabilities/assets/media/image12.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL | OUT_OF_SCOPE |
| 562 | other | `archive/converted-prd/oboss/capabilities/assets/media/image13.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL | OUT_OF_SCOPE |
| 563 | other | `archive/converted-prd/oboss/capabilities/assets/media/image14.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL | OUT_OF_SCOPE |
| 564 | other | `archive/converted-prd/oboss/capabilities/assets/media/image15.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL | OUT_OF_SCOPE |
| 565 | other | `archive/converted-prd/oboss/capabilities/assets/media/image16.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL | OUT_OF_SCOPE |
| 566 | other | `archive/converted-prd/oboss/capabilities/assets/media/image17.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL | OUT_OF_SCOPE |
| 567 | other | `archive/converted-prd/oboss/capabilities/assets/media/image18.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL | OUT_OF_SCOPE |
| 568 | other | `archive/converted-prd/oboss/capabilities/assets/media/image19.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL | OUT_OF_SCOPE |
| 569 | other | `archive/converted-prd/oboss/capabilities/assets/media/image20.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL | OUT_OF_SCOPE |
| 570 | other | `archive/converted-prd/oboss/capabilities/assets/media/image21.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL | OUT_OF_SCOPE |
| 571 | other | `archive/converted-prd/oboss/capabilities/assets/media/image22.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 572 | other | `archive/converted-prd/oboss/capabilities/assets/media/image23.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 573 | other | `archive/converted-prd/oboss/capabilities/assets/media/image24.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 574 | other | `archive/converted-prd/oboss/capabilities/assets/media/image25.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 575 | other | `archive/converted-prd/oboss/capabilities/assets/media/image26.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 576 | other | `archive/converted-prd/oboss/capabilities/assets/media/image27.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 577 | other | `archive/converted-prd/oboss/capabilities/assets/media/image28.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 578 | other | `archive/converted-prd/oboss/capabilities/assets/media/image29.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 579 | other | `archive/converted-prd/oboss/capabilities/assets/media/image30.jpg` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 580 | other | `archive/converted-prd/oboss/capabilities/assets/media/image31.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 581 | other | `archive/converted-prd/oboss/capabilities/assets/media/image3.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 582 | other | `archive/converted-prd/oboss/capabilities/assets/media/image32.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 583 | other | `archive/converted-prd/oboss/capabilities/assets/media/image33.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 584 | other | `archive/converted-prd/oboss/capabilities/assets/media/image34.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 585 | other | `archive/converted-prd/oboss/capabilities/assets/media/image35.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 586 | other | `archive/converted-prd/oboss/capabilities/assets/media/image36.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 587 | other | `archive/converted-prd/oboss/capabilities/assets/media/image28.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 588 | other | `archive/converted-prd/oboss/capabilities/assets/media/image37.jpg` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 589 | other | `archive/converted-prd/oboss/capabilities/assets/media/image31.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 590 | other | `archive/converted-prd/oboss/capabilities/assets/media/image3.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 591 | other | `archive/converted-prd/oboss/capabilities/assets/media/image38.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 592 | other | `archive/converted-prd/oboss/capabilities/assets/media/image39.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 593 | other | `archive/converted-prd/oboss/capabilities/assets/media/image40.png` | Swap | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 594 | other | `archive/converted-prd/oboss/capabilities/assets/media/image41.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 595 | other | `archive/converted-prd/oboss/capabilities/assets/media/image42.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 596 | other | `archive/converted-prd/oboss/capabilities/assets/media/image43.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 597 | other | `archive/converted-prd/oboss/capabilities/assets/media/image44.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 598 | other | `archive/converted-prd/oboss/capabilities/assets/media/image45.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 599 | other | `archive/converted-prd/oboss/capabilities/assets/media/image46.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 600 | other | `archive/converted-prd/oboss/capabilities/assets/media/image47.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 601 | other | `archive/converted-prd/oboss/capabilities/assets/media/image48.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 602 | other | `archive/converted-prd/oboss/capabilities/assets/media/image49.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 603 | other | `archive/converted-prd/oboss/capabilities/assets/media/image50.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 604 | other | `archive/converted-prd/oboss/capabilities/assets/media/image43.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 605 | other | `archive/converted-prd/oboss/mvp/assets/media/image1.png` | \ AIX\ OBOSS MVP | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL | OUT_OF_SCOPE |
| 606 | other | `archive/converted-prd/oboss/mvp/assets/media/image2.png` | \ AIX\ OBOSS MVP | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 607 | other | `archive/converted-prd/oboss/mvp/assets/media/image3.png` | \ AIX\ OBOSS MVP | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL | OUT_OF_SCOPE |
| 608 | other | `archive/converted-prd/oboss/mvp/assets/media/image4.png` | \ AIX\ OBOSS MVP | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 609 | other | `archive/converted-prd/oboss/mvp/assets/media/image5.png` | \ AIX\ OBOSS MVP | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 610 | other | `archive/converted-prd/oboss/mvp/assets/media/image6.png` | \ AIX\ OBOSS MVP | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 611 | other | `archive/converted-prd/oboss/mvp/assets/media/image7.png` | \ AIX\ OBOSS MVP | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 612 | other | `archive/converted-prd/oboss/mvp/assets/media/image8.png` | Notification center | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 613 | other | `archive/converted-prd/oboss/mvp/assets/media/image9.png` | Notification center | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL | OUT_OF_SCOPE |
| 614 | other | `archive/converted-prd/oboss/mvp/assets/media/image10.png` | \ AIX\ OBOSS MVP | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 615 | other | `archive/converted-prd/oboss/mvp/assets/media/image11.png` | \ AIX\ OBOSS MVP | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 616 | other | `archive/converted-prd/oboss/mvp/assets/media/image12.png` | \ AIX\ OBOSS MVP | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 617 | other | `archive/converted-prd/oboss/mvp/assets/media/image13.png` | \ AIX\ OBOSS MVP | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 618 | other | `archive/converted-prd/oboss/mvp/assets/media/image14.png` | \ AIX\ OBOSS MVP | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 619 | other | `archive/converted-prd/oboss/mvp/assets/media/image15.png` | \ AIX\ OBOSS MVP | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 620 | other | `archive/converted-prd/oboss/mvp/assets/media/image16.png` | Notification center | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 621 | other | `archive/converted-prd/oboss/mvp/assets/media/image17.png` | \ AIX\ OBOSS MVP | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 622 | other | `archive/converted-prd/oboss/mvp/assets/media/image18.png` | \ AIX\ OBOSS MVP | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL | OUT_OF_SCOPE |
| 623 | other | `archive/converted-prd/oboss/mvp/assets/media/image19.png` | \ AIX\ OBOSS MVP | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 624 | other | `archive/converted-prd/oboss/mvp/assets/media/image20.png` | \ AIX\ OBOSS MVP | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 625 | other | `archive/converted-prd/oboss/mvp/assets/media/image21.png` | \ AIX\ OBOSS MVP | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 626 | other | `archive/converted-prd/oboss/mvp/assets/media/image22.png` | \ AIX\ OBOSS MVP | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 627 | other | `archive/converted-prd/oboss/mvp/assets/media/image23.png` | \ AIX\ OBOSS MVP | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 628 | other | `archive/converted-prd/oboss/mvp/assets/media/image24.png` | \ AIX\ OBOSS MVP | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 629 | other | `archive/converted-prd/oboss/mvp/assets/media/image25.png` | \ AIX\ OBOSS MVP | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 630 | other | `archive/converted-prd/oboss/mvp/assets/media/image26.png` | \ AIX\ OBOSS MVP | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 631 | other | `archive/converted-prd/oboss/mvp/assets/media/image27.png` | \ AIX\ OBOSS MVP | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 632 | other | `archive/converted-prd/oboss/mvp/assets/media/image28.png` | \ AIX\ OBOSS MVP | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 633 | other | `archive/converted-prd/oboss/mvp/assets/media/image29.png` | \ AIX\ OBOSS MVP | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 634 | other | `archive/converted-prd/oboss/mvp/assets/media/image30.png` | \ AIX\ OBOSS MVP | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 635 | other | `archive/converted-prd/oboss/mvp/assets/media/image31.png` | \ AIX\ OBOSS MVP | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 636 | other | `archive/converted-prd/oboss/mvp/assets/media/image32.png` | \ AIX\ OBOSS MVP | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 637 | other | `archive/converted-prd/oboss/mvp/assets/media/image33.png` | \ AIX\ OBOSS MVP | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 638 | other | `archive/converted-prd/security/identity-verification/assets/media/image1.png` | 1. 需求变更日志 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL | OUT_OF_SCOPE |
| 639 | other | `archive/converted-prd/security/identity-verification/assets/media/image2.png` | Verify Page | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 640 | other | `archive/converted-prd/security/identity-verification/assets/media/image3.png` | Verify Page | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 641 | other | `archive/converted-prd/security/identity-verification/assets/media/image4.png` | 7. 全局规则 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 642 | other | `archive/converted-prd/security/identity-verification/assets/media/image5.png` | 7. 全局规则 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 643 | other | `archive/converted-prd/security/identity-verification/assets/media/image6.png` | 7. 全局规则 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 644 | other | `archive/converted-prd/security/identity-verification/assets/media/image7.jpeg` | Verify Page | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 645 | other | `archive/converted-prd/security/identity-verification/assets/media/image8.png` | 8. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 646 | other | `archive/converted-prd/security/identity-verification/assets/media/image9.png` | 8. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 647 | other | `archive/converted-prd/security/identity-verification/assets/media/image10.png` | 8. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 648 | other | `archive/converted-prd/security/identity-verification/assets/media/image11.png` | 8. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 649 | other | `archive/converted-prd/security/identity-verification/assets/media/image12.png` | 8. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 650 | other | `archive/converted-prd/security/identity-verification/assets/media/image13.jpeg` | 8. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL | OUT_OF_SCOPE |
| 651 | other | `archive/converted-prd/security/identity-verification/assets/media/image14.jpeg` | Face Auth | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 652 | other | `archive/converted-prd/security/identity-verification/assets/media/image15.jpeg` | Face Auth | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 653 | other | `archive/converted-prd/security/identity-verification/assets/media/image16.png` | 8. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 654 | other | `archive/converted-prd/security/identity-verification/assets/media/image17.png` | Face Auth | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 655 | other | `archive/converted-prd/security/identity-verification/assets/media/image18.png` | Face Auth | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 656 | other | `archive/converted-prd/security/identity-verification/assets/media/image19.png` | 8. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL | OUT_OF_SCOPE |
| 657 | wallet/assets | `archive/converted-prd/wallet/asset/assets/media/image1.png` | 4. AIX前端功能需求 | knowledge-base/wallet/assets.md | PAGE_VISUAL | TODO_BIND |
| 658 | wallet/assets | `archive/converted-prd/wallet/asset/assets/media/image2.png` | 4. AIX前端功能需求 | knowledge-base/wallet/assets.md | PAGE_VISUAL | TODO_BIND |
| 659 | wallet/assets | `archive/converted-prd/wallet/asset/assets/media/image3.png` | 4. AIX前端功能需求 | knowledge-base/wallet/assets.md | PAGE_VISUAL | TODO_BIND |
| 660 | wallet/assets | `archive/converted-prd/wallet/asset/assets/media/image4.png` | 4. AIX前端功能需求 | knowledge-base/wallet/assets.md | PAGE_VISUAL | TODO_BIND |
| 661 | wallet/assets | `archive/converted-prd/wallet/asset/assets/media/image5.png` | 4. AIX前端功能需求 | knowledge-base/wallet/assets.md | PAGE_VISUAL | TODO_BIND |
| 662 | wallet/assets | `archive/converted-prd/wallet/asset/assets/media/image6.jpeg` | 5. DTC渠道接口需求 | knowledge-base/wallet/assets.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 663 | wallet/assets | `archive/converted-prd/wallet/asset/assets/media/image7.jpeg` | 5. DTC渠道接口需求 | knowledge-base/wallet/assets.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 664 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image1.png` | 1. 引言 | knowledge-base/wallet/deposit.md / send.md / swap.md | PAGE_VISUAL | TODO_BIND |
| 665 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image2.png` | 1. 引言 | knowledge-base/wallet/deposit.md / send.md / swap.md | PAGE_VISUAL | TODO_BIND |
| 666 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image3.png` | 1. 引言 | knowledge-base/wallet/deposit.md / send.md / swap.md | PAGE_VISUAL | TODO_BIND |
| 667 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image4.png` | 1. 引言 | knowledge-base/wallet/deposit.md / send.md / swap.md | PAGE_VISUAL | TODO_BIND |
| 668 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image5.png` | 1. 引言 | knowledge-base/wallet/deposit.md / send.md / swap.md | PAGE_VISUAL | TODO_BIND |
| 669 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image6.png` | 1. 引言 | knowledge-base/wallet/deposit.md / send.md / swap.md | PAGE_VISUAL | TODO_BIND |
| 670 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image7.jpeg` | 6. AIX前端功能需求 | knowledge-base/wallet/deposit.md / send.md / swap.md | PAGE_VISUAL | TODO_BIND |
| 671 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image8.png` | 6. AIX前端功能需求 | knowledge-base/wallet/deposit.md / send.md / swap.md | PAGE_VISUAL | TODO_BIND |
| 672 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image9.png` | Send Crypto | knowledge-base/wallet/deposit.md / send.md / swap.md | PAGE_VISUAL | TODO_BIND |
| 673 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image10.png` | Send Crypto | knowledge-base/wallet/deposit.md / send.md / swap.md | PAGE_VISUAL | TODO_BIND |
| 674 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image11.png` | Send Crypto | knowledge-base/wallet/deposit.md / send.md / swap.md | PAGE_VISUAL | TODO_BIND |
| 675 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image12.png` | Send Crypto | knowledge-base/wallet/deposit.md / send.md / swap.md | PAGE_VISUAL | TODO_BIND |
| 676 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image13.png` | 6. AIX前端功能需求 | knowledge-base/wallet/deposit.md / send.md / swap.md | PAGE_VISUAL | TODO_BIND |
| 677 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image14.png` | 6. AIX前端功能需求 | knowledge-base/wallet/deposit.md / send.md / swap.md | PAGE_VISUAL | TODO_BIND |
| 678 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image15.png` | 6. AIX前端功能需求 | knowledge-base/wallet/deposit.md / send.md / swap.md | PAGE_VISUAL | TODO_BIND |
| 679 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image16.png` | Deposit Crypto | knowledge-base/wallet/deposit.md / send.md / swap.md | PAGE_VISUAL | TODO_BIND |
| 680 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image17.png` | Deposit Crypto | knowledge-base/wallet/deposit.md / send.md / swap.md | PAGE_VISUAL | TODO_BIND |
| 681 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image18.png` | Transaction Details | knowledge-base/wallet/deposit.md / send.md / swap.md | PAGE_VISUAL | TODO_BIND |
| 682 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image19.png` | Transaction Details | knowledge-base/wallet/deposit.md / send.md / swap.md | PAGE_VISUAL | TODO_BIND |
| 683 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image20.png` | Transaction Details | knowledge-base/wallet/deposit.md / send.md / swap.md | PAGE_VISUAL | TODO_BIND |
| 684 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image21.jpeg` | 6. AIX前端功能需求 | knowledge-base/wallet/deposit.md / send.md / swap.md | PAGE_VISUAL | TODO_BIND |
| 685 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image22.png` | 6. AIX前端功能需求 | knowledge-base/wallet/deposit.md / send.md / swap.md | PAGE_VISUAL | TODO_BIND |
| 686 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image23.png` | Swap | knowledge-base/wallet/deposit.md / send.md / swap.md | PAGE_VISUAL | TODO_BIND |
| 687 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image24.png` | Swap | knowledge-base/wallet/deposit.md / send.md / swap.md | PAGE_VISUAL | TODO_BIND |
| 688 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image25.png` | Swap | knowledge-base/wallet/deposit.md / send.md / swap.md | PAGE_VISUAL | TODO_BIND |
| 689 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image26.png` | Swap | knowledge-base/wallet/deposit.md / send.md / swap.md | PAGE_VISUAL | TODO_BIND |
| 690 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image27.png` | Swap Order | knowledge-base/wallet/deposit.md / send.md / swap.md | PAGE_VISUAL | TODO_BIND |
| 691 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image28.png` | Swap Order | knowledge-base/wallet/deposit.md / send.md / swap.md | PAGE_VISUAL | TODO_BIND |
| 692 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image29.png` | Swap Order | knowledge-base/wallet/deposit.md / send.md / swap.md | PAGE_VISUAL | TODO_BIND |
| 693 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image30.png` | Swap | knowledge-base/wallet/deposit.md / send.md / swap.md | PAGE_VISUAL | TODO_BIND |
| 694 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image31.png` | Swap | knowledge-base/wallet/deposit.md / send.md / swap.md | PAGE_VISUAL | TODO_BIND |
| 695 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image32.png` | Deposit Crypto | knowledge-base/wallet/deposit.md / send.md / swap.md | PAGE_VISUAL | TODO_BIND |
| 696 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image33.jpeg` | 6. AIX前端功能需求 | knowledge-base/wallet/deposit.md / send.md / swap.md | PAGE_VISUAL | TODO_BIND |
| 697 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image34.png` | 6. AIX前端功能需求 | knowledge-base/wallet/deposit.md / send.md / swap.md | PAGE_VISUAL | TODO_BIND |
| 698 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image35.png` | 6. AIX前端功能需求 | knowledge-base/wallet/deposit.md / send.md / swap.md | PAGE_VISUAL | TODO_BIND |
| 699 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image36.png` | 6. AIX前端功能需求 | knowledge-base/wallet/deposit.md / send.md / swap.md | PAGE_VISUAL | TODO_BIND |
| 700 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image37.png` | 6. AIX前端功能需求 | knowledge-base/wallet/deposit.md / send.md / swap.md | PAGE_VISUAL | TODO_BIND |
| 701 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image38.png` | Deposit Crypto | knowledge-base/wallet/deposit.md / send.md / swap.md | PAGE_VISUAL | TODO_BIND |
| 702 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image39.png` | Deposit Crypto | knowledge-base/wallet/deposit.md / send.md / swap.md | PAGE_VISUAL | TODO_BIND |
| 703 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image40.png` | 6. AIX前端功能需求 | knowledge-base/wallet/deposit.md / send.md / swap.md | PAGE_VISUAL | TODO_BIND |
| 704 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image41.png` | Receive Crypto | knowledge-base/wallet/deposit.md / send.md / swap.md | PAGE_VISUAL | TODO_BIND |
| 705 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image42.png` | Receive Crypto | knowledge-base/wallet/deposit.md / send.md / swap.md | PAGE_VISUAL | TODO_BIND |
| 706 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image43.png` | 6. AIX前端功能需求 | knowledge-base/wallet/deposit.md / send.md / swap.md | PAGE_VISUAL | TODO_BIND |
| 707 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image44.jpeg` | 6. AIX前端功能需求 | knowledge-base/wallet/deposit.md / send.md / swap.md | PAGE_VISUAL | TODO_BIND |
| 708 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image45.png` | 6. AIX前端功能需求 | knowledge-base/wallet/deposit.md / send.md / swap.md | PAGE_VISUAL | TODO_BIND |
| 709 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image46.png` | 6. AIX前端功能需求 | knowledge-base/wallet/deposit.md / send.md / swap.md | PAGE_VISUAL | TODO_BIND |
| 710 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image47.png` | 6. AIX前端功能需求 | knowledge-base/wallet/deposit.md / send.md / swap.md | PAGE_VISUAL | TODO_BIND |
| 711 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image48.png` | 6. AIX前端功能需求 | knowledge-base/wallet/deposit.md / send.md / swap.md | PAGE_VISUAL | TODO_BIND |
| 712 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image49.png` | Deposit Crypto | knowledge-base/wallet/deposit.md / send.md / swap.md | PAGE_VISUAL | TODO_BIND |
| 713 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image50.png` | Deposit Crypto | knowledge-base/wallet/deposit.md / send.md / swap.md | PAGE_VISUAL | TODO_BIND |
| 714 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image51.png` | Deposit Crypto | knowledge-base/wallet/deposit.md / send.md / swap.md | PAGE_VISUAL | TODO_BIND |
| 715 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image52.png` | Deposit Crypto | knowledge-base/wallet/deposit.md / send.md / swap.md | PAGE_VISUAL | TODO_BIND |
| 716 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image53.png` | 6. AIX前端功能需求 | knowledge-base/wallet/deposit.md / send.md / swap.md | PAGE_VISUAL | TODO_BIND |
| 717 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image54.png` | 6. AIX前端功能需求 | knowledge-base/wallet/deposit.md / send.md / swap.md | PAGE_VISUAL | TODO_BIND |
| 718 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image55.png` | 6. AIX前端功能需求 | knowledge-base/wallet/deposit.md / send.md / swap.md | PAGE_VISUAL | TODO_BIND |
| 719 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image56.png` | 6. AIX前端功能需求 | knowledge-base/wallet/deposit.md / send.md / swap.md | PAGE_VISUAL | TODO_BIND |
| 720 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image57.png` | 6. AIX前端功能需求 | knowledge-base/wallet/deposit.md / send.md / swap.md | PAGE_VISUAL | TODO_BIND |
| 721 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image58.png` | 6. AIX前端功能需求 | knowledge-base/wallet/deposit.md / send.md / swap.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 722 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image59.png` | 6. AIX前端功能需求 | knowledge-base/wallet/deposit.md / send.md / swap.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 723 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image60.png` | 6. AIX前端功能需求 | knowledge-base/wallet/deposit.md / send.md / swap.md | PAGE_VISUAL | TODO_BIND |
| 724 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image61.jpeg` | 6. AIX前端功能需求 | knowledge-base/wallet/deposit.md / send.md / swap.md | PAGE_VISUAL | TODO_BIND |
| 725 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image62.png` | Transaction Details | knowledge-base/wallet/deposit.md / send.md / swap.md | PAGE_VISUAL | TODO_BIND |
| 726 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image63.jpeg` | 7. DTC渠道接口需求 | knowledge-base/wallet/deposit.md / send.md / swap.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 727 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image64.jpeg` | 7. DTC渠道接口需求 | knowledge-base/wallet/deposit.md / send.md / swap.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 728 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image65.jpeg` | 7. DTC渠道接口需求 | knowledge-base/wallet/deposit.md / send.md / swap.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 729 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image66.png` | 7. DTC渠道接口需求 | knowledge-base/wallet/deposit.md / send.md / swap.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 730 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image67.jpeg` | 7. DTC渠道接口需求 | knowledge-base/wallet/deposit.md / send.md / swap.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 731 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image68.jpeg` | 7. DTC渠道接口需求 | knowledge-base/wallet/deposit.md / send.md / swap.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 732 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image69.jpeg` | 7. DTC渠道接口需求 | knowledge-base/wallet/deposit.md / send.md / swap.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 733 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image70.jpeg` | 7. DTC渠道接口需求 | knowledge-base/wallet/deposit.md / send.md / swap.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 734 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image71.jpeg` | 7. DTC渠道接口需求 | knowledge-base/wallet/deposit.md / send.md / swap.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 735 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image72.jpeg` | 7. DTC渠道接口需求 | knowledge-base/wallet/deposit.md / send.md / swap.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 736 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image73.jpeg` | 7. DTC渠道接口需求 | knowledge-base/wallet/deposit.md / send.md / swap.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 737 | wallet | `archive/converted-prd/wallet/deposit-send-swap/assets/media/image63.jpeg` | 7. DTC渠道接口需求 | knowledge-base/wallet/deposit.md / send.md / swap.md | NON_PAGE_OR_SUPPORTING_VISUAL | TODO_BIND |
| 738 | other | `archive/converted-prd/website/phase-1/assets/media/image1.jpg` | 4. 需求优先级 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 739 | other | `archive/converted-prd/website/phase-1/assets/media/image2.png` | 4. 需求优先级 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 740 | other | `archive/converted-prd/website/phase-1/assets/media/image3.png` | 4. 需求优先级 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 741 | other | `archive/converted-prd/website/phase-1/assets/media/image4.png` | 4. 需求优先级 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL | OUT_OF_SCOPE |
| 742 | other | `archive/converted-prd/website/phase-1/assets/media/image5.png` | 4. 需求优先级 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL | OUT_OF_SCOPE |
| 743 | other | `archive/converted-prd/website/phase-1/assets/media/image6.png` | 4. 需求优先级 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL | OUT_OF_SCOPE |
| 744 | other | `archive/converted-prd/website/phase-1/assets/media/image7.png` | 4. 需求优先级 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL | OUT_OF_SCOPE |
| 745 | other | `archive/converted-prd/website/phase-1/assets/media/image8.png` | 4. 需求优先级 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL | OUT_OF_SCOPE |
| 746 | other | `archive/converted-prd/website/phase-1/assets/media/image9.png` | 4. 需求优先级 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 747 | other | `archive/converted-prd/website/phase-1/assets/media/image10.png` | 4. 需求优先级 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 748 | other | `archive/converted-prd/website/phase-1/assets/media/image11.jpg` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 749 | other | `archive/converted-prd/website/phase-1/assets/media/image12.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 750 | other | `archive/converted-prd/website/phase-1/assets/media/image13.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 751 | other | `archive/converted-prd/website/phase-1/assets/media/image14.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 752 | other | `archive/converted-prd/website/phase-1/assets/media/image15.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 753 | other | `archive/converted-prd/website/phase-1/assets/media/image16.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 754 | other | `archive/converted-prd/website/phase-1/assets/media/image17.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 755 | other | `archive/converted-prd/website/phase-1/assets/media/image18.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 756 | other | `archive/converted-prd/website/phase-1/assets/media/image19.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 757 | other | `archive/converted-prd/website/phase-1/assets/media/image20.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 758 | other | `archive/converted-prd/website/phase-1/assets/media/image21.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL | OUT_OF_SCOPE |
| 759 | other | `archive/converted-prd/website/phase-1/assets/media/image22.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL | OUT_OF_SCOPE |
| 760 | other | `archive/converted-prd/website/phase-1/assets/media/image23.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL | OUT_OF_SCOPE |
| 761 | other | `archive/converted-prd/website/phase-1/assets/media/image24.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL | OUT_OF_SCOPE |
| 762 | other | `archive/converted-prd/website/phase-1/assets/media/image25.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL | OUT_OF_SCOPE |
| 763 | other | `archive/converted-prd/website/phase-1/assets/media/image26.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL | OUT_OF_SCOPE |
| 764 | other | `archive/converted-prd/website/phase-1/assets/media/image27.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL | OUT_OF_SCOPE |
| 765 | other | `archive/converted-prd/website/phase-1/assets/media/image28.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL | OUT_OF_SCOPE |
| 766 | other | `archive/converted-prd/website/phase-1/assets/media/image29.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL | OUT_OF_SCOPE |
| 767 | other | `archive/converted-prd/website/phase-1/assets/media/image30.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL | OUT_OF_SCOPE |
| 768 | other | `archive/converted-prd/website/phase-1/assets/media/image31.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL | OUT_OF_SCOPE |
| 769 | other | `archive/converted-prd/website/phase-1/assets/media/image32.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 770 | other | `archive/converted-prd/website/phase-1/assets/media/image33.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 771 | other | `archive/converted-prd/website/phase-1/assets/media/image34.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 772 | other | `archive/converted-prd/website/phase-1/assets/media/image35.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 773 | other | `archive/converted-prd/website/phase-1/assets/media/image36.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 774 | other | `archive/converted-prd/website/phase-1/assets/media/image37.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 775 | other | `archive/converted-prd/website/phase-1/assets/media/image38.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 776 | other | `archive/converted-prd/website/phase-1/assets/media/image39.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 777 | other | `archive/converted-prd/website/phase-1/assets/media/image40.jpg` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 778 | other | `archive/converted-prd/website/phase-1/assets/media/image41.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 779 | other | `archive/converted-prd/website/phase-1/assets/media/image13.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 780 | other | `archive/converted-prd/website/phase-1/assets/media/image42.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 781 | other | `archive/converted-prd/website/phase-1/assets/media/image43.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 782 | other | `archive/converted-prd/website/phase-1/assets/media/image44.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 783 | other | `archive/converted-prd/website/phase-1/assets/media/image45.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 784 | other | `archive/converted-prd/website/phase-1/assets/media/image46.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 785 | other | `archive/converted-prd/website/phase-1/assets/media/image38.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 786 | other | `archive/converted-prd/website/phase-1/assets/media/image47.jpg` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 787 | other | `archive/converted-prd/website/phase-1/assets/media/image41.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 788 | other | `archive/converted-prd/website/phase-1/assets/media/image13.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 789 | other | `archive/converted-prd/website/phase-1/assets/media/image48.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 790 | other | `archive/converted-prd/website/phase-1/assets/media/image49.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 791 | other | `archive/converted-prd/website/phase-1/assets/media/image50.png` | Swap | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 792 | other | `archive/converted-prd/website/phase-1/assets/media/image51.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 793 | other | `archive/converted-prd/website/phase-1/assets/media/image52.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 794 | other | `archive/converted-prd/website/phase-1/assets/media/image53.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 795 | other | `archive/converted-prd/website/phase-1/assets/media/image54.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 796 | other | `archive/converted-prd/website/phase-1/assets/media/image55.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 797 | other | `archive/converted-prd/website/phase-1/assets/media/image56.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 798 | other | `archive/converted-prd/website/phase-1/assets/media/image57.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 799 | other | `archive/converted-prd/website/phase-1/assets/media/image58.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 800 | other | `archive/converted-prd/website/phase-1/assets/media/image59.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 801 | other | `archive/converted-prd/website/phase-1/assets/media/image60.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 802 | other | `archive/converted-prd/website/phase-1/assets/media/image53.png` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 803 | other | `archive/converted-prd/website/phase-2/assets/media/image1.jpeg` | 3. 需求概况 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 804 | other | `archive/converted-prd/website/phase-2/assets/media/image2.jpeg` | 3. 需求概况 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 805 | other | `archive/converted-prd/website/phase-2/assets/media/image3.jpg` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 806 | other | `archive/converted-prd/website/phase-2/assets/media/image4.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 807 | other | `archive/converted-prd/website/phase-2/assets/media/image5.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 808 | other | `archive/converted-prd/website/phase-2/assets/media/image6.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 809 | other | `archive/converted-prd/website/phase-2/assets/media/image7.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 810 | other | `archive/converted-prd/website/phase-2/assets/media/image8.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 811 | other | `archive/converted-prd/website/phase-2/assets/media/image9.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 812 | other | `archive/converted-prd/website/phase-2/assets/media/image10.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 813 | other | `archive/converted-prd/website/phase-2/assets/media/image11.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 814 | other | `archive/converted-prd/website/phase-2/assets/media/image12.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 815 | other | `archive/converted-prd/website/phase-2/assets/media/image13.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL | OUT_OF_SCOPE |
| 816 | other | `archive/converted-prd/website/phase-2/assets/media/image14.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL | OUT_OF_SCOPE |
| 817 | other | `archive/converted-prd/website/phase-2/assets/media/image15.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL | OUT_OF_SCOPE |
| 818 | other | `archive/converted-prd/website/phase-2/assets/media/image16.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL | OUT_OF_SCOPE |
| 819 | other | `archive/converted-prd/website/phase-2/assets/media/image17.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL | OUT_OF_SCOPE |
| 820 | other | `archive/converted-prd/website/phase-2/assets/media/image18.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL | OUT_OF_SCOPE |
| 821 | other | `archive/converted-prd/website/phase-2/assets/media/image19.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL | OUT_OF_SCOPE |
| 822 | other | `archive/converted-prd/website/phase-2/assets/media/image20.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL | OUT_OF_SCOPE |
| 823 | other | `archive/converted-prd/website/phase-2/assets/media/image21.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL | OUT_OF_SCOPE |
| 824 | other | `archive/converted-prd/website/phase-2/assets/media/image22.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL | OUT_OF_SCOPE |
| 825 | other | `archive/converted-prd/website/phase-2/assets/media/image23.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | NON_PAGE_OR_SUPPORTING_VISUAL | OUT_OF_SCOPE |
| 826 | other | `archive/converted-prd/website/phase-2/assets/media/image24.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 827 | other | `archive/converted-prd/website/phase-2/assets/media/image25.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 828 | other | `archive/converted-prd/website/phase-2/assets/media/image26.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 829 | other | `archive/converted-prd/website/phase-2/assets/media/image27.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 830 | other | `archive/converted-prd/website/phase-2/assets/media/image28.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 831 | other | `archive/converted-prd/website/phase-2/assets/media/image29.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 832 | other | `archive/converted-prd/website/phase-2/assets/media/image30.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 833 | other | `archive/converted-prd/website/phase-2/assets/media/image31.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 834 | other | `archive/converted-prd/website/phase-2/assets/media/image32.jpg` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 835 | other | `archive/converted-prd/website/phase-2/assets/media/image33.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 836 | other | `archive/converted-prd/website/phase-2/assets/media/image5.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 837 | other | `archive/converted-prd/website/phase-2/assets/media/image34.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 838 | other | `archive/converted-prd/website/phase-2/assets/media/image35.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 839 | other | `archive/converted-prd/website/phase-2/assets/media/image36.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 840 | other | `archive/converted-prd/website/phase-2/assets/media/image37.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 841 | other | `archive/converted-prd/website/phase-2/assets/media/image38.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 842 | other | `archive/converted-prd/website/phase-2/assets/media/image30.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 843 | other | `archive/converted-prd/website/phase-2/assets/media/image39.jpg` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 844 | other | `archive/converted-prd/website/phase-2/assets/media/image33.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 845 | other | `archive/converted-prd/website/phase-2/assets/media/image5.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 846 | other | `archive/converted-prd/website/phase-2/assets/media/image40.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 847 | other | `archive/converted-prd/website/phase-2/assets/media/image41.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 848 | other | `archive/converted-prd/website/phase-2/assets/media/image42.png` | Swap | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 849 | other | `archive/converted-prd/website/phase-2/assets/media/image43.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 850 | other | `archive/converted-prd/website/phase-2/assets/media/image44.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 851 | other | `archive/converted-prd/website/phase-2/assets/media/image45.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 852 | other | `archive/converted-prd/website/phase-2/assets/media/image46.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 853 | other | `archive/converted-prd/website/phase-2/assets/media/image47.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 854 | other | `archive/converted-prd/website/phase-2/assets/media/image48.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 855 | other | `archive/converted-prd/website/phase-2/assets/media/image49.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 856 | other | `archive/converted-prd/website/phase-2/assets/media/image50.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 857 | other | `archive/converted-prd/website/phase-2/assets/media/image51.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 858 | other | `archive/converted-prd/website/phase-2/assets/media/image52.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 859 | other | `archive/converted-prd/website/phase-2/assets/media/image45.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 860 | other | `archive/converted-prd/website/waitlist-addition/assets/media/image1.jpg` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 861 | other | `archive/converted-prd/website/waitlist-addition/assets/media/image2.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 862 | other | `archive/converted-prd/website/waitlist-addition/assets/media/image3.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 863 | other | `archive/converted-prd/website/waitlist-addition/assets/media/image4.jpeg` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 864 | other | `archive/converted-prd/website/waitlist-addition/assets/media/image5.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 865 | other | `archive/converted-prd/website/waitlist-addition/assets/media/image6.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 866 | other | `archive/converted-prd/website/waitlist-addition/assets/media/image7.png` | 4. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 867 | other | `archive/converted-prd/website/waitlist-campaign/assets/media/image1.jpg` | 4. Demo | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 868 | other | `archive/converted-prd/website/waitlist-campaign/assets/media/image2.jpg` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |
| 869 | other | `archive/converted-prd/website/waitlist-campaign/assets/media/image3.jpg` | 5. 需求描述 | OUT_OF_SCOPE_OR_UNMAPPED | PAGE_VISUAL | OUT_OF_SCOPE |