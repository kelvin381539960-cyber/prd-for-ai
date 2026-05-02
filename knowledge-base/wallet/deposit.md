---
module: wallet
feature: deposit
version: "1.3"
status: active
source_doc: DTC Wallet OpenAPI Documentation；knowledge-base/wallet/_index.md；knowledge-base/wallet/balance.md；knowledge-base/wallet/transaction-history.md；knowledge-base/common/walletconnect.md；knowledge-base/common/notification.md；knowledge-base/common/errors.md；knowledge-base/changelog/knowledge-gaps.md；用户确认结论 2026-05-01
source_section: Wallet Deposit / GTR / WalletConnect；Wallet _index v1.3；Wallet Balance v1.0；Wallet Transaction History v1.0；Common WalletConnect v1.0；deposit scope correction；deposit refinement
last_updated: 2026-05-01
owner: 吴忆锋
depends_on:
  - wallet/_index
  - wallet/balance
  - wallet/transaction-history
  - common/walletconnect
  - common/notification
  - common/errors
  - changelog/knowledge-gaps
---

# Wallet Deposit 钱包充值

## 1. 当前状态

Wallet Deposit 当前状态为 `active`。

根据用户确认，Deposit 能力存在，包含两条已确认入金路径：

1. GTR Deposit。
2. WalletConnect Deposit。

此前将整个 Deposit 模块标记为 deferred 的口径过宽，已修正。

需要注意：GTR 与 WalletConnect 只能作为两条并列子路径处理。除非来源明确，不得默认二者使用同一套字段、状态、风控、白名单、Declare / Travel Rule 或通知规则。

## 2. 模块定位

Wallet Deposit 用于沉淀 AIX Wallet 入金相关能力，包括 GTR 入金、WalletConnect 入金、入金交易记录、余额变化、状态和异常边界。

本文当前重点是拆分 GTR / WalletConnect 结构，并列出各自待补事项。未确认字段、状态、风控、通知和合规规则不得写成事实。

## 3. Deposit 子路径总览

| 子路径 | 当前状态 | 当前可写事实 | 当前不可写事实 |
|---|---|---|---|
| GTR Deposit | active / 待补细节 | Deposit 包含 GTR | 完整流程、字段、状态、风控、通知、Declare、白名单 |
| WalletConnect Deposit | active / 待补细节 | Deposit 包含 WalletConnect | 完整流程、字段、状态、风控、通知、Declare、白名单 |
| 其他 Deposit 旧方案 | 未确认 | 不写 | 不得默认归档为 active |
| Send | deferred | 不属于 Deposit active 范围 | 不写成当前已上线 |
| Swap | deferred | 不属于 Deposit active 范围 | 不写成当前已上线 |

## 4. GTR Deposit

### 4.1 当前可确认

| 项目 | 结论 | 来源 |
|---|---|---|
| GTR 属于 Deposit 子路径 | 是 | 用户确认 2026-05-01 |
| GTR 当前是否 active | 是，作为 Deposit active 子路径 | 用户确认 2026-05-01 |
| GTR 是否等同 WalletConnect | 否，需拆分处理 | 用户确认 Deposit 包含两条路径 |

### 4.2 GTR 待补事项

| 问题 | 当前处理 | 影响 |
|---|---|---|
| GTR 入金触发方式 | 待补 | 无法形成完整流程 |
| GTR 入口 / 页面路径 | 待补 | 无法形成用户路径 |
| GTR 支持币种 / 链 | 待补 | 无法形成资产边界 |
| GTR 入金交易 ID 字段 | 待补 | 无法形成交易追踪 |
| GTR 入金状态映射 | 待补 | 无法形成状态闭环 |
| GTR 是否需要 Declare / Travel Rule | 待补 | 合规边界不完整 |
| GTR 是否需要白名单 | 待补 | 前置条件不完整 |
| GTR on-hold / risk rejected 规则 | 待补 | 异常分支不完整 |
| GTR 成功 / 失败通知 | 待补 | 用户通知边界不完整 |
| GTR 资金可见时点 | 待补 | Wallet balance 变化口径不完整 |

## 5. WalletConnect Deposit

### 5.1 当前可确认

| 项目 | 结论 | 来源 |
|---|---|---|
| WalletConnect 属于 Deposit 子路径 | 是 | 用户确认 2026-05-01 |
| WalletConnect 当前是否 active | 是，作为 Deposit active 子路径 | 用户确认 2026-05-01 |
| WalletConnect 是否等同 GTR | 否，需拆分处理 | 用户确认 Deposit 包含两条路径 |
| WalletConnect 不属于 Send / Swap | 是 | common/walletconnect.md |

### 5.2 WalletConnect 待补事项

| 问题 | 当前处理 | 影响 |
|---|---|---|
| WalletConnect 连接 / 授权流程 | 待补 | 无法形成完整用户路径 |
| WalletConnect 支持钱包范围 | 待补 | 无法形成三方钱包边界 |
| WalletConnect 支持币种 / 链 | 待补 | 无法形成资产边界 |
| WalletConnect 入金交易 ID 字段 | 待补 | 无法形成交易追踪 |
| WalletConnect 入金状态映射 | 待补 | 无法形成状态闭环 |
| WalletConnect 是否需要 Declare / Travel Rule | 待补 | 合规边界不完整 |
| WalletConnect 是否需要白名单 | 待补 | 前置条件不完整 |
| WalletConnect on-hold / risk rejected 规则 | 待补 | 异常分支不完整 |
| WalletConnect 成功 / 失败通知 | 待补 | 用户通知边界不完整 |
| WalletConnect 资金可见时点 | 待补 | Wallet balance 变化口径不完整 |

## 6. Deposit 与 Balance 的关系

| 阶段 | GTR | WalletConnect | 当前处理 |
|---|---|---|---|
| 用户发起入金 | 待补 | 待补 | 不补写触发方式 |
| AIX / DTC 识别入金 | 待补 | 待补 | 不补写识别规则 |
| 入金处理中 | 待补 | 待补 | 不补写状态映射 |
| 入金成功 | Wallet balance 增加的具体时点待补 | Wallet balance 增加的具体时点待补 | 不写成立即可用 |
| 入金失败 / 拒绝 / on-hold | 待补 | 待补 | 不补写余额影响 |

## 7. Deposit 与 Transaction History 的关系

Deposit 交易记录与详情应统一引用 Wallet Transaction History 的基础字段，但不得补写具体关联规则。

| 能力 | 当前可引用 | 当前待补 |
|---|---|---|
| Deposit 记录 ID | Wallet 交易 `id` 存在 | GTR / WC 记录生成时机 |
| Deposit 详情查询 | Wallet 详情入参 `transactionId` 存在 | GTR / WC transactionId 来源 |
| Deposit 状态 | Wallet `state` 枚举存在 | GTR / WC 状态映射 |
| Deposit 余额历史 | Search Balance History 存在 | GTR / WC `activityType`、`relatedId` 取值 |

## 8. GTR 与 WalletConnect 不得混写的规则

| 事项 | 处理 |
|---|---|
| 字段 | 不得默认共用 |
| 状态机 | 不得默认共用 |
| 风控规则 | 不得默认共用 |
| 白名单规则 | 不得默认共用 |
| Declare / Travel Rule | 不得默认共用 |
| 通知规则 | 不得默认共用 |
| 用户提示 | 不得默认共用 |
| 资金可见时点 | 不得默认共用 |

## 9. 与 Card Transaction Flow 的边界

Card balance 自动归集到 Wallet 不是 Wallet Deposit 主流程。

| 项目 | 处理 |
|---|---|
| Card refund / reversal / deposit 触发查卡余额 | 属于 Card Transaction Flow |
| `Transfer Balance to Wallet(cardId, amount=balance)` | 属于 Card Transaction Flow |
| DTC transfer 成功响应无业务流水 | 已在 Card Transaction Flow 记录 |
| Wallet 是否生成对应交易 `id` | Wallet 交易 `id` 已确认存在，但与 Card 归集的关联仍 deferred |
| Wallet `relatedId` 在 Card balance 转 Wallet 场景下取值 | deferred gap，不在 Deposit 补写 |

## 10. Deposit 通知边界

| 通知 | GTR | WalletConnect | 当前处理 |
|---|---|---|---|
| 入金成功通知 | 待补 | 待补 | 需 Notification PRD / 已确认结论 |
| 入金失败通知 | 待补 | 待补 | 需 Notification PRD / 已确认结论 |
| on-hold 通知 | 待补 | 待补 | 需风控 / Notification 来源 |
| risk rejected 通知 | 待补 | 待补 | 需风控 / Notification 来源 |
| Declare / Travel Rule 通知 | 待补 | 待补 | 需合规 / Notification 来源 |

## 11. Deposit 错误与人工处理边界

| 场景 | GTR | WalletConnect | 当前处理 |
|---|---|---|---|
| 入金失败原因 | 待补 | 待补 | 需错误码 / PRD |
| 风控拦截 | 待补 | 待补 | 需风控规则 |
| on-hold | 待补 | 待补 | 需状态和处理路径 |
| 用户反馈处理 | 待补 | 待补 | 需客服 / 运营口径 |
| 人工补偿 | 待补 | 待补 | 需后台 / 后端确认 |

## 12. 不写入事实的内容

以下内容当前不得写成事实：

1. GTR 与 WalletConnect 使用同一套字段、状态或风控规则。
2. 所有 Deposit 都需要白名单。
3. 所有 Deposit 都不需要白名单。
4. 所有 Deposit 都需要 Declare。
5. 所有 Deposit 都不需要 Declare。
6. Deposit 成功一定等同于 Wallet balance 立即可用。
7. Deposit 状态完全等同于 Wallet `state` 枚举中的某几个值。
8. Deposit 风控拦截规则已确认。
9. Deposit 成功 / 失败通知文案已确认。
10. Card balance 自动归集属于 Wallet Deposit。
11. WalletConnect 属于 Send 或 Swap。
12. GTR / WalletConnect 的 `relatedId` 取值已确认。

## 13. 后续补材料清单

| 优先级 | 待补项 | 目标来源 |
|---|---|---|
| P0 | GTR 完整流程、入口、字段、状态、失败处理 | GTR PRD / 接口文档 / 截图 |
| P0 | WalletConnect 完整流程、入口、字段、状态、失败处理 | WC PRD / 接口文档 / 截图 |
| P0 | GTR / WC Declare / Travel Rule 规则 | 合规 PRD / 产品确认 |
| P0 | GTR / WC 白名单规则 | 合规 PRD / 产品确认 |
| P0 | GTR / WC on-hold / risk rejected 规则 | 风控 / DTC / PRD |
| P0 | GTR / WC 通知规则 | Notification PRD / 已确认结论 |
| P1 | GTR / WC 客服与人工处理口径 | 客服 / 运营 / 后台 PRD |

## 14. 来源引用

- (Ref: 用户确认结论 / 2026-05-01 / Deposit 包含 GTR 和 WalletConnect)
- (Ref: DTC Wallet OpenAPI Documentation / Wallet 通用交易记录与状态)
- (Ref: knowledge-base/wallet/_index.md / Wallet 模块边界)
- (Ref: knowledge-base/wallet/balance.md / Wallet Balance v1.0)
- (Ref: knowledge-base/wallet/transaction-history.md / Wallet Transaction History v1.0)
- (Ref: knowledge-base/common/walletconnect.md / v1.0)
- (Ref: knowledge-base/common/notification.md / v1.0)
- (Ref: knowledge-base/common/errors.md / v1.0)
- (Ref: knowledge-base/changelog/knowledge-gaps.md / Card Transaction Flow deferred gaps)
