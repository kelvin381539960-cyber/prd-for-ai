---
module: common
feature: walletconnect-integration
version: "1.0"
status: active
source_doc: IMPLEMENTATION_PLAN.md；knowledge-base/common/_index.md；knowledge-base/wallet/deposit.md；knowledge-base/wallet/receive.md；knowledge-base/wallet/stage-review.md；knowledge-base/common/dtc.md；knowledge-base/common/notification.md
source_section: IMPLEMENTATION_PLAN v4.0 / Common Integration；Common Index v2.0；Wallet Deposit v1.2；Wallet Receive v1.0；Wallet Stage Review v1.0；DTC Integration v1.0；Notification v1.0
last_updated: 2026-05-01
owner: 吴忆锋
depends_on:
  - common/_index
  - common/dtc
  - common/notification
  - wallet/deposit
  - wallet/receive
  - wallet/stage-review
---

# WalletConnect Integration 公共集成边界

## 1. 功能定位

WalletConnect Integration 用于沉淀 AIX WalletConnect 入金相关的公共集成边界，包括第三方钱包连接、入金路径、状态、风控、Declare / Travel Rule、白名单和通知的待确认范围。

本文只确认 WalletConnect 属于 Deposit 的一条入金路径，不补写未确认的 WalletConnect 完整流程、接口字段、状态机或合规规则。

## 2. 当前已确认事实

| 项目 | 结论 | 来源 | 备注 |
|---|---|---|---|
| Deposit 能力存在 | Deposit 包含 GTR 和 WalletConnect | Wallet Deposit / 用户确认 | WalletConnect 属于 Deposit 子路径 |
| WalletConnect 当前归属 | Wallet Deposit 子路径 | Wallet Deposit | 不属于 Send / Swap |
| Send | deferred，未上线 | Wallet Stage Review | 不纳入 WalletConnect active 能力 |
| Swap | deferred，未上线且需重做 | Wallet Stage Review | 不纳入 WalletConnect active 能力 |
| Wallet 交易基础字段 | `id`、`transactionId`、`state` 已确认 | Wallet Transaction History | 具体 WalletConnect 关联关系待补 |

## 3. WalletConnect 与 Deposit 的关系

| 维度 | 当前处理 |
|---|---|
| WalletConnect 是否是 Deposit 子路径 | 是，已确认属于 Deposit |
| WalletConnect 是否等同所有 Deposit | 否，Deposit 还包含 GTR |
| WalletConnect 与 GTR 是否共用字段 / 状态 | 未确认，不写成事实 |
| WalletConnect 是否进入 Wallet Transaction History | 待补 |
| WalletConnect 是否影响 Wallet Balance | 待补 |
| WalletConnect 是否触发通知 | 待补 |

## 4. 合规 / 风控 / 白名单边界

| 问题 | 当前处理 |
|---|---|
| WalletConnect 是否必须 Declare | 待补，不写成事实 |
| WalletConnect 什么情况下必须 Declare | 待补，不写成事实 |
| WalletConnect 什么情况下不需要 Declare | 待补，不写成事实 |
| WalletConnect 是否需要地址白名单 | 待补，不写成事实 |
| WalletConnect 是否存在 on-hold | 待补，不写成事实 |
| WalletConnect 是否存在 risk rejected | 待补，不写成事实 |
| WalletConnect 风控拦截后是否入 Wallet balance | 待补，不写成事实 |

## 5. 与 DTC 的关系

| 项目 | 当前处理 |
|---|---|
| WalletConnect 是否使用 DTC Wallet 接口 | 待补 |
| WalletConnect 入金交易 ID | 待补 |
| WalletConnect 与 Wallet `transactionId` 的关系 | 待补 |
| WalletConnect 与 Wallet `relatedId` 的关系 | 待补 |
| WalletConnect 失败错误码 | 待补 |
| WalletConnect Webhook / 回调 | 待补 |

## 6. 与 Notification 的关系

| 通知 | 当前处理 |
|---|---|
| WalletConnect 入金成功通知 | 待补 |
| WalletConnect 入金失败通知 | 待补 |
| WalletConnect on-hold 通知 | 待补 |
| WalletConnect Declare 待处理通知 | 待补 |
| WalletConnect risk rejected 通知 | 待补 |

## 7. 不写入事实的内容

以下内容当前不得写成事实：

1. WalletConnect 与 GTR 使用同一套流程。
2. WalletConnect 与 GTR 使用同一套字段。
3. WalletConnect 与 GTR 使用同一套状态机。
4. WalletConnect 一定需要 Declare。
5. WalletConnect 一定不需要 Declare。
6. WalletConnect 一定需要白名单。
7. WalletConnect 已确认完整支持所有第三方钱包。
8. WalletConnect 入金成功一定立即增加可用余额。
9. WalletConnect 成功 / 失败通知已确认。
10. WalletConnect 属于 Send 或 Swap。

## 8. 待补项

| 编号 | 待补项 | 来源建议 | 当前处理 |
|---|---|---|---|
| WC-GAP-001 | WalletConnect 完整入金流程 | WalletConnect PRD / 截图 / 接口文档 | 待补 |
| WC-GAP-002 | WalletConnect 支持钱包范围 | PRD / 产品确认 | 待补 |
| WC-GAP-003 | WalletConnect 支持币种 / 链 | PRD / DTC Wallet OpenAPI | 待补 |
| WC-GAP-004 | WalletConnect Declare / Travel Rule 规则 | 合规 PRD / 产品确认 | 待补 |
| WC-GAP-005 | WalletConnect 白名单规则 | PRD / 合规确认 | 待补 |
| WC-GAP-006 | WalletConnect 风控 / on-hold / rejected 状态 | 风控 / DTC / PRD | 待补 |
| WC-GAP-007 | WalletConnect 钱包交易字段映射 | DTC Wallet OpenAPI / 后端确认 | 待补 |
| WC-GAP-008 | WalletConnect 通知规则 | Notification PRD / WC PRD | 待补 |
| WC-GAP-009 | WalletConnect 失败原因和用户提示 | PRD / 错误码 / 客服口径 | 待补 |

## 9. 来源引用

- (Ref: IMPLEMENTATION_PLAN.md / v4.0 / Common Integration)
- (Ref: knowledge-base/common/_index.md / v2.0)
- (Ref: knowledge-base/wallet/deposit.md / v1.2)
- (Ref: knowledge-base/wallet/receive.md / v1.0)
- (Ref: knowledge-base/wallet/stage-review.md / v1.0)
- (Ref: knowledge-base/common/dtc.md / v1.0)
- (Ref: knowledge-base/common/notification.md / v1.0)
