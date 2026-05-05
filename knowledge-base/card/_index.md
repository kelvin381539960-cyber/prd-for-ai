---
module: card
feature: card-index
version: "2.0"
status: active
source_doc: knowledge-base/card/application.md；knowledge-base/card/card-home.md；knowledge-base/card/card-management.md；knowledge-base/changelog/knowledge-gaps.md；knowledge-base/_system-boundary.md
source_section: Card runtime structure；Card Application；Card Home；Card Management；ALL-GAP；system boundary
last_updated: 2026-05-05
owner: 吴忆锋
readers: [product, ui, dev, qa, business, ai]
---

# Card 模块索引

## 1. 模块定位

Card 模块只保留运行态事实文件，不再按激活、PIN、敏感信息、状态字典、交易归集等子动作拆成大量平级文件。

当前 Card 目录负责沉淀：申卡、Card 模块首页、卡管理与卡交易相关边界。

## 2. 当前文件

| 文件 | 状态 | 定位 |
|---|---|---|
| `card/_index.md` | active | Card 模块索引 |
| `card/application.md` | active | Card 申请、计划选择、费用、申卡资格、申请提交和结果 |
| `card/card-home.md` | active | Card 模块首页，包含卡片展示、状态卡片、操作入口、Recent Transactions 入口 |
| `card/card-management.md` | active | 卡状态与字段、实体卡激活、PIN、敏感信息、Lock / Unlock / Terminate、卡交易通知与归集 |

## 3. 已合并的旧文件

| 旧文件 | 当前去向 |
|---|---|
| `card/activation.md` | 已并入 `card/card-management.md` |
| `card/pin.md` | 已并入 `card/card-management.md` |
| `card/sensitive-info.md` | 已并入 `card/card-management.md` |
| `card/card-status-and-fields.md` | 已并入 `card/card-management.md` |
| `card/card-transaction-flow.md` | 已并入 `card/card-management.md` |

## 4. 查询入口规则

| 查询主题 | 优先读取 |
|---|---|
| 申卡、卡计划、费用、邮寄、申请结果 | `card/application.md` |
| Card 模块首页、状态卡片、操作入口、Recent Transactions 入口 | `card/card-home.md` |
| 卡状态、字段、操作限制矩阵 | `card/card-management.md` |
| 实体卡激活、后四位校验、Set PIN 联动 | `card/card-management.md` |
| PIN 设置、Change PIN、Reset PIN、PIN 公钥和 OTP | `card/card-management.md` |
| Card detail、PAN / EXP / CVV / CVC、敏感信息认证后查看 | `card/card-management.md` |
| Lock / Unlock / Terminate | `card/card-management.md` |
| 卡交易通知、自动归集、Transfer Balance to Wallet、交易展示边界 | `card/card-management.md`，必要时联动 `transaction/reconciliation.md` |
| 卡交易历史 / 详情统一状态 | `transaction/history.md`、`transaction/detail.md`、`transaction/status-model.md` |
| 未确认项 / ID 串联 / 对账 | `changelog/knowledge-gaps.md`、`transaction/reconciliation.md` |

## 5. 与其他模块边界

| 模块 | 关系 | 边界 |
|---|---|---|
| Home | App 首页整体结构在 `home/app-home.md`；Card 首页只维护 Card 模块页面 | 不把 App Home 全局结构写进 Card |
| KYC | 申卡可能依赖 KYC / Account Opening | KYC 主事实在 `kyc/account-opening.md` |
| Wallet | 卡余额归集到 Wallet 涉及 Wallet 记录和余额 | Wallet 主事实在 `wallet/`，对账在 `transaction/` |
| Security | 查看敏感信息、Unlock、PIN Reset 等可能依赖身份认证 | 认证规则在 `security/` |
| Transaction | 卡交易历史、详情、状态和对账需要统一交易模块承接 | Card 只维护卡交易触发和展示边界 |
| Common / Notification | 卡状态变更和卡交易通知模板由 Notification 维护 | Card 不维护通知模板 |

## 6. 不写入事实的内容

1. 不把 `card/card-home.md` 当作 App 全局首页事实源。
2. 不把 Card 交易状态机写在 Card Home 中。
3. 不把 Card `data.id`、`D-REQUEST-ID`、Wallet `transactionId`、Wallet `relatedId` 写死为同一 ID。
4. 不把 KYC Approved 写成一定可申卡。
5. 不把 DTC Sub Account、WalletAccount、Card Account 的关系写死为一一对应。
6. 不把 Terminate Card 直接落为当前 AIX 页面能力，除非有页面流程来源。
7. 不把旧已合并文件作为运行态入口。

## 7. 来源引用

- (Ref: knowledge-base/card/application.md)
- (Ref: knowledge-base/card/card-home.md)
- (Ref: knowledge-base/card/card-management.md)
- (Ref: knowledge-base/transaction/reconciliation.md)
- (Ref: knowledge-base/changelog/knowledge-gaps.md)
- (Ref: knowledge-base/_system-boundary.md)
