---
module: common
feature: walletconnect-integration
version: "1.1"
status: active
source_doc: IMPLEMENTATION_PLAN.md；knowledge-base/common/_index.md；knowledge-base/wallet/deposit.md；knowledge-base/wallet/receive.md；knowledge-base/wallet/stage-review.md；knowledge-base/common/dtc.md；knowledge-base/common/notification.md；knowledge-base/common/errors.md
source_section: IMPLEMENTATION_PLAN v4.1 / 全仓库回扫；Common Index v2.0；Wallet Deposit v1.3；Wallet Receive v1.0；Wallet Stage Review v1.0；DTC Integration v1.0；Notification v1.0；Errors v1.0
last_updated: 2026-05-01
owner: 吴忆锋
depends_on:
  - common/_index
  - common/dtc
  - common/notification
  - common/errors
  - wallet/deposit
  - wallet/receive
  - wallet/stage-review
---

# WalletConnect Integration 公共集成边界

## 1. 功能定位

WalletConnect Integration 用于沉淀 AIX WalletConnect 入金相关的公共集成边界，包括第三方钱包连接、入金路径、状态、风控、Declare / Travel Rule、白名单、通知和错误处理的待确认范围。

本文只确认 WalletConnect 属于 Deposit 的一条入金路径，不补写未确认的 WalletConnect 完整流程、接口字段、状态机或合规规则。

## 2. 当前已确认事实

| 项目 | 结论 | 来源 | 备注 |
|---|---|---|---|
| Deposit 能力存在 | Deposit 包含 GTR 和 WalletConnect | Wallet Deposit / 用户确认 | WalletConnect 属于 Deposit 子路径 |
| WalletConnect 当前归属 | Wallet Deposit 子路径 | Wallet Deposit | 不属于 Send / Swap |
| WalletConnect 与 GTR 关系 | 二者并列，不能默认共用流程、字段、状态、风控、通知 | Wallet Deposit v1.3 | 需拆分处理 |
| Send | deferred，未上线 | Wallet Stage Review | 不纳入 WalletConnect active 能力 |
| Swap | deferred，未上线且需重做 | Wallet Stage Review | 不纳入 WalletConnect active 能力 |
| Wallet 交易基础字段 | `id`、`transactionId`、`state` 已确认 | Wallet Transaction History | 具体 WalletConnect 关联关系待补 |

## 3. WalletConnect 入金链路结构

以下结构仅用于后续补材料时定位缺口，不代表流程已确认。

| 阶段 | 当前处理 | 待补来源 |
|---|---|---|
| 入口展示 | 待补 | WalletConnect PRD / 截图 |
| 三方钱包连接 | 待补 | WalletConnect PRD / SDK / 接口文档 |
| 钱包授权 / 用户确认 | 待补 | WalletConnect PRD / 钱包交互说明 |
| 入金发起 | 待补 | WalletConnect PRD / DTC Wallet OpenAPI |
| DTC / AIX 识别入金 | 待补 | DTC / 后端确认 |
| on-hold / risk rejected | 待补 | 风控 / 合规 / DTC 文档 |
| Wallet 余额可见 | 待补 | 产品 / 后端 / DTC Wallet OpenAPI |
| 交易记录生成 | 待补 | DTC Wallet OpenAPI / 后端确认 |
| 通知触发 | 待补 | Notification PRD / WC PRD |

## 4. WalletConnect 与 Deposit 的关系

| 维度 | 当前处理 |
|---|---|
| WalletConnect 是否是 Deposit 子路径 | 是，已确认属于 Deposit |
| WalletConnect 是否等同所有 Deposit | 否，Deposit 还包含 GTR |
| WalletConnect 与 GTR 是否共用字段 / 状态 | 未确认，不写成事实 |
| WalletConnect 是否进入 Wallet Transaction History | 待补 |
| WalletConnect 是否影响 Wallet Balance | 待补 |
| WalletConnect 是否触发通知 | 待补 |
| WalletConnect 是否有独立错误码 / 失败原因 | 待补 |

## 5. 合规 / 风控 / 白名单边界

| 问题 | 当前处理 |
|---|---|
| WalletConnect 是否必须 Declare | 待补，不写成事实 |
| WalletConnect 什么情况下必须 Declare | 待补，不写成事实 |
| WalletConnect 什么情况下不需要 Declare | 待补，不写成事实 |
| WalletConnect 是否需要地址白名单 | 待补，不写成事实 |
| WalletConnect 加白发生在入金前还是入金后 | 待补，不写成事实 |
| WalletConnect 是否存在 on-hold | 待补，不写成事实 |
| WalletConnect 是否存在 risk rejected | 待补，不写成事实 |
| WalletConnect 风控拦截后是否入 Wallet balance | 待补，不写成事实 |
| WalletConnect 风控拦截后用户是否可见资金 | 待补，不写成事实 |

## 6. 与 DTC 的关系

| 项目 | 当前处理 |
|---|---|
| WalletConnect 是否使用 DTC Wallet 接口 | 待补 |
| WalletConnect 入金交易 ID | 待补 |
| WalletConnect 与 Wallet `transactionId` 的关系 | 待补 |
| WalletConnect 与 Wallet `id` 的关系 | 待补 |
| WalletConnect 与 Wallet `relatedId` 的关系 | 待补 |
| WalletConnect 与 Search Balance History `activityType` 的关系 | 待补 |
| WalletConnect 失败错误码 | 待补 |
| WalletConnect Webhook / 回调 | 待补 |

## 7. 与 Notification 的关系

| 通知 | 当前处理 |
|---|---|
| WalletConnect 入金成功通知 | 待补 |
| WalletConnect 入金失败通知 | 待补 |
| WalletConnect on-hold 通知 | 待补 |
| WalletConnect Declare 待处理通知 | 待补 |
| WalletConnect risk rejected 通知 | 待补 |
| WalletConnect 钱包连接失败通知 | 待补，不能默认存在 |

## 8. 与 Errors 的关系

| 错误 / 异常 | 当前处理 |
|---|---|
| 用户取消连接 / 拒绝授权 | 待补 |
| 第三方钱包连接失败 | 待补 |
| 入金失败 | 待补 |
| 风控拦截 | 待补 |
| on-hold | 待补 |
| 钱包余额未更新 | 待补 |
| 人工处理 / 客服口径 | 待补 |

## 9. 不写入事实的内容

以下内容当前不得写成事实：

1. WalletConnect 与 GTR 使用同一套流程。
2. WalletConnect 与 GTR 使用同一套字段。
3. WalletConnect 与 GTR 使用同一套状态机。
4. WalletConnect 一定需要 Declare。
5. WalletConnect 一定不需要 Declare。
6. WalletConnect 一定需要白名单。
7. WalletConnect 一定不需要白名单。
8. WalletConnect 已确认完整支持所有第三方钱包。
9. WalletConnect 入金成功一定立即增加可用余额。
10. WalletConnect 成功 / 失败通知已确认。
11. WalletConnect 属于 Send 或 Swap。
12. WalletConnect 的 `transactionId`、`id`、`relatedId` 关联规则已确认。

## 10. 待补项

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
| WC-GAP-010 | WalletConnect 与 GTR 的差异表 | GTR / WC PRD | 待补 |

## 11. 来源引用

- (Ref: IMPLEMENTATION_PLAN.md / v4.1 / 全仓库回扫)
- (Ref: knowledge-base/common/_index.md / v2.0)
- (Ref: knowledge-base/wallet/deposit.md / v1.3)
- (Ref: knowledge-base/wallet/receive.md / v1.0)
- (Ref: knowledge-base/wallet/stage-review.md / v1.0)
- (Ref: knowledge-base/common/dtc.md / v1.0)
- (Ref: knowledge-base/common/notification.md / v1.0)
- (Ref: knowledge-base/common/errors.md / v1.0)
