---
module: home
feature: app-home
version: "1.0"
status: active
source_doc: archive/historical-prd/app/AIX APP V1.0【Home】.docx；knowledge-base/card/card-home.md；knowledge-base/wallet/_index.md；knowledge-base/changelog/knowledge-gaps.md
source_section: AIX APP Home；Card Home entry；Wallet entry；runtime scope
last_updated: 2026-05-05
owner: 吴忆锋
readers: [product, ui, dev, qa, business, ai]
---

# App Home 首页

## 1. 文档定位

本文是 AIX App 首页的运行态事实源，用于承接 App 内首页整体结构和跨模块入口边界。

本文不承接官网首页、Web Marketing 页面、运营投放落地页、Popup / Banner 配置系统、MGM 页面或 Waitlist 外部投放页。

## 2. 已确认范围

| 首页能力 | 当前处理 | 主事实源 |
|---|---|---|
| App 首页整体结构 | 本文维护 | `home/app-home.md` |
| Card 首页区块 / Card 入口 | 本文只维护入口边界 | 具体 Card 页面见 `card/card-home.md` |
| Wallet / Asset 入口 | 本文只维护入口边界 | 具体 Wallet 能力见 `wallet/` |
| 交易入口 | 本文只维护入口边界 | 交易历史和详情见 `transaction/` |
| FAQ / Notification / Errors | 首页如引用公共能力，只记录边界 | 具体事实见 `common/` |

## 3. 首页与模块边界

| 首页区块 / 入口 | 可能跳转 | 边界说明 |
|---|---|---|
| Card 区块 | Card Home / Card Application / Card Details | 首页只决定是否展示入口和跳转，不维护 Card 状态矩阵 |
| Wallet / Asset 区块 | Wallet Balance / Deposit / Transaction History | 首页不维护余额字段、Deposit 流程或交易状态 |
| Transaction 区块 | Transaction History / Details | 首页不维护交易状态模型 |
| FAQ / Help 入口 | FAQ 或对应业务帮助页 | FAQ 主事实在 `common/faq.md` |
| Notification 入口 | Notification Center / 站内信 | Notification 主事实在 `common/notification.md` |

## 4. Card 首页区块边界

AIX APP Home 原始文档中存在 Card 相关首页内容。当前处理如下：

1. App 首页上的 Card 区块、入口和跳转边界由本文记录。
2. Card 模块自己的首页、卡片状态、操作入口、Recent Transactions、物流、FAQ 等由 `card/card-home.md` 维护。
3. Card 状态、敏感信息、PIN、激活、Lock / Unlock、卡交易归集由 `card/manage/_index.md` 维护。
4. 不得把 App Home 上的 Card 区块直接当成 Card 模块完整事实源。

## 5. 暂不入库内容

以下内容即使在历史 PRD 中存在，也暂不进入 Home 运行态事实源：

| 内容 | 处理 |
|---|---|
| 官网首页 | 暂不入库 |
| Web / Marketing 页面 | 暂不入库 |
| 外部投放 waitlist | 暂不入库 |
| Popup / Banner 运营配置 | 暂不入库 |
| MGM 页面 | 暂不入库 |
| OBoss / 后台首页 | 暂不入库 |

## 6. 待确认事项

| 问题 | 影响范围 | 当前处理 |
|---|---|---|
| AIX APP Home 原始文档是否需要全量转译为首页结构、区块顺序和交互规则 | Home | 当前仅建立 Home 模块入口和跨模块边界 |
| 首页 Card 区块与 `card/card-home.md` 的字段边界是否有冲突 | Home / Card | 以 Card 模块事实源维护卡状态和操作 |
| 首页 Wallet / Asset 区块是否需要单独拆资产首页 | Home / Wallet | 暂不新增 Asset 模块 |
| 首页 Popup / Banner 是否后续入库 | Home / Operation | 当前暂不入库 |

## 7. 不得推导的内容

1. 不得把 App Home 等同官网 Home。
2. 不得把首页 Card 区块等同 Card 模块完整首页。
3. 不得在 Home 中定义 Card 状态矩阵、Wallet 余额字段、交易状态或通知模板。
4. 不得从历史 Popup / Banner / MGM 文档补写 Home 运营配置能力。
5. 不得把未全量转译的 Home 原文细节写成已确认运行态事实。

## 8. 来源引用

- (Ref: archive/historical-prd/app/AIX APP V1.0【Home】.docx)
- (Ref: knowledge-base/card/card-home.md)
- (Ref: knowledge-base/card/manage/_index.md)
- (Ref: knowledge-base/wallet/_index.md)
- (Ref: knowledge-base/transaction/_index.md)
- (Ref: knowledge-base/common/faq.md)
- (Ref: knowledge-base/common/notification.md)
- (Ref: knowledge-base/changelog/knowledge-gaps.md)
