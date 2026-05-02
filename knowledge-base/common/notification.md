---
module: common
feature: notification
version: "1.0"
status: active
source_doc: IMPLEMENTATION_PLAN.md；knowledge-base/common/_index.md；knowledge-base/card/card-transaction-flow.md；knowledge-base/wallet/deposit.md；knowledge-base/wallet/stage-review.md；knowledge-base/transaction/stage-review.md；[2025-11-25] AIX+Notification（push及站内信）.docx
source_section: IMPLEMENTATION_PLAN v4.0 / Common Integration；Common Index v2.0；Card Transaction Flow v1.2；Notification PRD 卡相关；Wallet Stage Review v1.0
last_updated: 2026-05-01
owner: 吴忆锋
depends_on:
  - common/_index
  - card/card-transaction-flow
  - wallet/deposit
  - wallet/stage-review
  - transaction/stage-review
---

# Notification Push / 站内信公共能力

## 1. 功能定位

Notification 用于沉淀 AIX 跨模块通知能力，包括 push、站内信、触发源、触发条件、模板参数、跳转目标和业务边界。

本文不重写业务流程；业务文件只引用通知结果。通知触发条件和模板参数必须来自 Notification PRD、截图、接口文档或已确认结论。

## 2. 已确认通知能力

| 通知 | 触发源 | 条件 | 跳转目标 | 来源 |
|---|---|---|---|---|
| 卡交易成功 | Card Transaction Notify | `indicator=debit`，`status=101 AUTHORIZED` | 卡交易详情页 | Notification PRD；Card Transaction Flow |
| 卡退款成功 | Card Transaction Notify | `indicator=credit`，refund / reversed 场景 | 卡交易详情页 | Notification PRD；Card Transaction Flow |

## 3. 已确认通知参数

| 通知类型 | 参数 | 来源 | 备注 |
|---|---|---|---|
| 卡交易 / 卡退款通知 | `merchant_name` | Notification PRD | 商户名称 |
| 卡交易 / 卡退款通知 | `amount` | Notification PRD | 金额 |
| 卡交易 / 卡退款通知 | `currency` | Notification PRD | 币种 |
| 卡交易 / 卡退款通知 | `transaction_time` | Notification PRD | 交易时间 |
| 卡交易 / 卡退款通知 | `full_name` | Notification PRD | 用户姓名 |
| 卡交易 / 卡退款通知 | `last 4` | Notification PRD | 卡号后 4 位 |

## 4. 通知与业务结果边界

| 场景 | 当前结论 | 来源 | 处理 |
|---|---|---|---|
| 卡退款 / 卡交易成功通知 | 正常情况下用户收到通知后，预期资金已归集至 Wallet | 用户确认 / Card Transaction Flow | 可作为正常用户预期 |
| 极端异常 | 卡有钱但转 Wallet 失败时，用户可能看不到资金 | 用户确认 / Card Transaction Flow | 不得写成通知必然等于 Wallet 到账 |
| DTC transfer 成功但 Wallet 未到账 | 当前无法系统自动发现，主要依赖用户反馈 | 用户确认 / Card Transaction Flow | 不得写成通知可自动发现异常 |

## 5. Wallet / Deposit 通知边界

Deposit 当前 active，包含 GTR 和 WalletConnect，但通知规则尚未补齐。

| 项目 | 当前处理 |
|---|---|
| GTR Deposit 成功通知 | 待补，不写成事实 |
| GTR Deposit 失败通知 | 待补，不写成事实 |
| WalletConnect Deposit 成功通知 | 待补，不写成事实 |
| WalletConnect Deposit 失败通知 | 待补，不写成事实 |
| on-hold / risk rejected 通知 | 待补，不写成事实 |
| Declare / Travel Rule 相关通知 | 待补，不写成事实 |

## 6. Send / Swap 通知边界

| 能力 | 当前状态 | Notification 处理 |
|---|---|---|
| Send / Withdraw | deferred，未上线 | 不归档 active 通知规则 |
| Swap | deferred，未上线且需重做 | 不归档 active 通知规则 |

## 7. 不写入事实的内容

以下内容不得写成事实：

1. 所有 Wallet Deposit 成功 / 失败通知已确认。
2. GTR 和 WalletConnect 使用同一套通知模板。
3. 收到卡退款成功通知必然代表 Wallet 已到账。
4. 通知系统可自动发现 DTC transfer 成功但 Wallet 未到账。
5. Send / Swap 有当前 active 通知规则。
6. 未在 Notification PRD 中出现的模板参数。
7. 未确认的 push / 站内信文案。

## 8. 待补项

| 编号 | 待补项 | 来源建议 | 当前处理 |
|---|---|---|---|
| NOTIF-GAP-001 | Deposit GTR 通知规则 | Notification PRD / GTR PRD | 待补 |
| NOTIF-GAP-002 | WalletConnect Deposit 通知规则 | Notification PRD / WC PRD | 待补 |
| NOTIF-GAP-003 | Wallet on-hold / risk rejected 通知 | Notification PRD / 风控 PRD | 待补 |
| NOTIF-GAP-004 | Wallet KYC 通知规则 | Notification PRD / KYC PRD | 待补 |
| NOTIF-GAP-005 | 通知模板完整文案 | Notification PRD | 待补 |
| NOTIF-GAP-006 | 站内信与 Push 是否一致 | Notification PRD / 产品确认 | 待补 |
| NOTIF-GAP-007 | 通知失败重试 / 补发策略 | 后端确认 | 待补 |

## 9. 来源引用

- (Ref: IMPLEMENTATION_PLAN.md / v4.0 / Common Integration)
- (Ref: knowledge-base/common/_index.md / v2.0)
- (Ref: knowledge-base/card/card-transaction-flow.md / v1.2)
- (Ref: knowledge-base/wallet/deposit.md / v1.2)
- (Ref: knowledge-base/wallet/stage-review.md / v1.0)
- (Ref: knowledge-base/transaction/stage-review.md / v1.0)
- (Ref: [2025-11-25] AIX+Notification（push及站内信）.docx / 卡相关通知)
