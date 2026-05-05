---
module: card
feature: card-index
version: "3.1"
status: active
source_doc: knowledge-base/card/application.md；knowledge-base/card/card-home.md；knowledge-base/card/manage/_index.md；knowledge-base/card/transaction.md；knowledge-base/card/transaction-detail.md；knowledge-base/changelog/knowledge-gaps.md；knowledge-base/_system-boundary.md
source_section: Card runtime structure；Card Application；Card Home；Card Manage；Card Transaction；Card Transaction Detail；ALL-GAP；system boundary
last_updated: 2026-05-05
owner: 吴忆锋
readers: [product, ui, dev, qa, business, ai]
---

# Card 模块索引

## 1. 模块定位

Card 模块按原始 PRD 的产品边界拆分为：申卡、Card Home、Card Manage、Card Transaction、Card Transaction Detail。

Card 目录不再把 Manage、Transaction、Transaction Detail 和全局 Transaction & History 混在同一个文件里。

## 2. 当前文件

| 文件 | 状态 | 定位 |
|---|---|---|
| `card/_index.md` | active | Card 模块索引 |
| `card/application.md` | active | Card 申请、计划选择、费用、申卡资格、申请提交和结果 |
| `card/card-home.md` | active | Card 模块首页，包含卡片展示、状态卡片、操作入口、Recent Transactions 入口 |
| `card/manage/_index.md` | active | Card Manage 子模块索引 |
| `card/manage/status-and-operations.md` | active | 卡状态、操作限制矩阵、Lock / Unlock / Terminate 边界 |
| `card/manage/activation.md` | active | 实体卡激活、后四位校验、激活后续流转 |
| `card/manage/sensitive-info.md` | active | Card detail、PAN / EXP / CVV / CVC、敏感信息认证后查看 |
| `card/manage/pin.md` | active | Set PIN、Change PIN、Reset PIN、PIN 公钥和 OTP |
| `card/transaction.md` | active | Card 交易通知后的卡余额回退 Wallet 流程 |
| `card/transaction-detail.md` | active | Card History、Card Transaction Details、Card 交易列表 / 详情展示 |

## 3. 原始 PRD 对应关系

| 原始 PRD | 当前知识库位置 | 说明 |
|---|---|---|
| `AIX Card V1.0【Application】.docx` | `card/application.md` | 申卡主事实源 |
| `AIX APP V1.0【Home】.docx` | `home/app-home.md`、`card/card-home.md` | App Home 归 Home；Card 模块首页归 Card Home |
| `AIX Card 【manage】模块需求V1.0 .docx` | `card/manage/*` | Manage 按独立功能拆分 |
| `AIX Card交易【transaction】.docx` | `card/transaction.md` | Card 交易通知后的资金回退主事实源 |
| `AIX APP V1.0【Transaction & History】 (1).docx` | `card/transaction-detail.md`、`transaction/*` | Card 交易列表 / 详情归 Card；全局交易历史、状态、对账归 Transaction |

## 4. 查询入口规则

| 查询主题 | 优先读取 |
|---|---|
| 申卡、卡计划、费用、邮寄、申请结果 | `card/application.md` |
| Card 模块首页、状态卡片、操作入口、Recent Transactions 入口 | `card/card-home.md` |
| 卡状态、操作权限、Lock / Unlock / Terminate 边界 | `card/manage/status-and-operations.md` |
| 实体卡激活、后四位校验、Set PIN 联动 | `card/manage/activation.md` |
| PIN 设置、Change PIN、Reset PIN、PIN 公钥和 OTP | `card/manage/pin.md` |
| Card detail、PAN / EXP / CVV / CVC、敏感信息认证后查看 | `card/manage/sensitive-info.md` |
| Card Transaction Notification、卡余额回退 Wallet、Transfer Balance to Wallet | `card/transaction.md` |
| Card History、Card Transaction Details、Card 交易列表 / 详情展示 | `card/transaction-detail.md` |
| 全局交易历史 / 详情 / 状态 / 对账 | `transaction/history.md`、`transaction/detail.md`、`transaction/status-model.md`、`transaction/reconciliation.md` |
| 未确认项 / ID 串联 / 对账 | `changelog/knowledge-gaps.md`、`transaction/reconciliation.md` |

## 5. 与其他模块边界

| 模块 | 关系 | 边界 |
|---|---|---|
| Home | App 首页整体结构在 `home/app-home.md`；Card 首页只维护 Card 模块页面 | 不把 App Home 全局结构写进 Card |
| KYC | 申卡可能依赖 KYC / Account Opening | KYC 主事实在 `kyc/account-opening.md` |
| Wallet | 卡余额回退到 Wallet 涉及 Wallet 记录和余额 | Wallet 主事实在 `wallet/`，对账在 `transaction/` |
| Security | 敏感信息、Unlock、PIN Reset 等可能依赖身份认证 | 认证规则在 `security/` |
| Transaction | 全局交易历史、详情、状态和对账需要统一交易模块承接 | Card 只维护 Card 场景下的交易处理和展示边界 |
| Common / Notification | 卡状态变更和卡交易通知模板由 Notification 维护 | Card 不维护通知模板 |

## 6. 不写入事实的内容

1. 不把 `card/card-home.md` 当作 App 全局首页事实源。
2. 不把全局交易状态机写在 Card Home 或 Card Transaction Detail 中。
3. 不把 Card `data.id`、`D-REQUEST-ID`、Wallet `transactionId`、Wallet `relatedId` 写死为同一 ID。
4. 不把 KYC Approved 写成一定可申卡。
5. 不把 DTC Sub Account、WalletAccount、Card Account 的关系写死为一一对应。
6. 不把 Terminate Card 单独写成完整 PRD；当前只作为 Manage 操作边界和待确认项。
7. 不把旧 `card/card-management.md` 当作运行态入口。

## 7. 来源引用

- (Ref: knowledge-base/card/application.md)
- (Ref: knowledge-base/card/card-home.md)
- (Ref: knowledge-base/card/manage/_index.md)
- (Ref: knowledge-base/card/transaction.md)
- (Ref: knowledge-base/card/transaction-detail.md)
- (Ref: knowledge-base/transaction/reconciliation.md)
- (Ref: knowledge-base/changelog/knowledge-gaps.md)
- (Ref: knowledge-base/_system-boundary.md)
