---
module: common
feature: notification
version: "1.1"
status: active
source_doc: IMPLEMENTATION_PLAN.md；knowledge-base/common/_index.md；knowledge-base/card/card-transaction-flow.md；knowledge-base/wallet/deposit.md；knowledge-base/common/walletconnect.md；knowledge-base/common/errors.md；knowledge-base/wallet/stage-review.md；knowledge-base/transaction/stage-review.md；[2025-11-25] AIX+Notification（push及站内信）.docx
source_section: IMPLEMENTATION_PLAN v4.1 / 全仓库回扫；Common Index v2.0；Card Transaction Flow v1.2；Wallet Deposit v1.3；WalletConnect v1.1；Notification PRD 卡相关；Wallet Stage Review v1.0
last_updated: 2026-05-01
owner: 吴忆锋
depends_on:
  - common/_index
  - common/walletconnect
  - common/errors
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

## 5. Deposit 通知边界

Deposit 当前 active，包含 GTR 和 WalletConnect。两条子路径通知规则必须分开确认。

| 通知场景 | GTR | WalletConnect | 当前处理 |
|---|---|---|---|
| 入金成功通知 | 待补 | 待补 | 不写成事实 |
| 入金失败通知 | 待补 | 待补 | 不写成事实 |
| on-hold 通知 | 待补 | 待补 | 不写成事实 |
| risk rejected 通知 | 待补 | 待补 | 不写成事实 |
| Declare / Travel Rule 待处理通知 | 待补 | 待补 | 不写成事实 |
| 资金可见 / 入账完成通知 | 待补 | 待补 | 不写成事实 |

## 6. WalletConnect 通知重点问题

| 问题 | 当前处理 |
|---|---|
| 钱包连接成功是否通知 | 待补，不默认存在 |
| 钱包连接失败是否通知 | 待补，不默认存在 |
| 用户拒绝授权是否通知 | 待补，不默认存在 |
| 入金已发起是否通知 | 待补，不默认存在 |
| 入金 on-hold 是否通知 | 待补，不默认存在 |
| 入金 rejected 是否通知 | 待补，不默认存在 |
| 入金 completed 是否通知 | 待补，不默认存在 |
| 通知是否跳转交易详情 | 待补，不默认复用卡通知跳转 |

## 7. Send / Swap 通知边界

| 能力 | 当前状态 | Notification 处理 |
|---|---|---|
| Send / Withdraw | deferred，未上线 | 不归档 active 通知规则 |
| Swap | deferred，未上线且需重做 | 不归档 active 通知规则 |

## 8. 不写入事实的内容

以下内容不得写成事实：

1. 所有 Wallet Deposit 成功 / 失败通知已确认。
2. GTR 和 WalletConnect 使用同一套通知模板。
3. GTR 和 WalletConnect 使用同一套通知触发条件。
4. 收到卡退款成功通知必然代表 Wallet 已到账。
5. 通知系统可自动发现 DTC transfer 成功但 Wallet 未到账。
6. WalletConnect 钱包连接成功 / 失败一定会通知。
7. WalletConnect 通知一定跳转交易详情。
8. Send / Swap 有当前 active 通知规则。
9. 未在 Notification PRD 中出现的模板参数。
10. 未确认的 push / 站内信文案。

## 9. 待补项

| 编号 | 待补项 | 来源建议 | 当前处理 |
|---|---|---|---|
| NOTIF-GAP-001 | GTR Deposit 通知规则 | Notification PRD / GTR PRD | 待补 |
| NOTIF-GAP-002 | WalletConnect Deposit 通知规则 | Notification PRD / WC PRD | 待补 |
| NOTIF-GAP-003 | Wallet on-hold / risk rejected 通知 | Notification PRD / 风控 PRD | 待补 |
| NOTIF-GAP-004 | Wallet KYC 通知规则 | Notification PRD / KYC PRD | 待补 |
| NOTIF-GAP-005 | 通知模板完整文案 | Notification PRD | 待补 |
| NOTIF-GAP-006 | 站内信与 Push 是否一致 | Notification PRD / 产品确认 | 待补 |
| NOTIF-GAP-007 | 通知失败重试 / 补发策略 | 后端确认 | 待补 |
| NOTIF-GAP-008 | Deposit 通知跳转目标 | Notification PRD / 产品确认 | 待补 |
| NOTIF-GAP-009 | Deposit 通知是否以 Wallet 入账为触发点 | 后端 / 产品确认 | 待补 |

## 10. 来源引用

- (Ref: IMPLEMENTATION_PLAN.md / v4.1 / 全仓库回扫)
- (Ref: knowledge-base/common/_index.md / v2.0)
- (Ref: knowledge-base/card/card-transaction-flow.md / v1.2)
- (Ref: knowledge-base/wallet/deposit.md / v1.3)
- (Ref: knowledge-base/common/walletconnect.md / v1.1)
- (Ref: knowledge-base/common/errors.md / v1.0)
- (Ref: knowledge-base/wallet/stage-review.md / v1.0)
- (Ref: knowledge-base/transaction/stage-review.md / v1.0)
- (Ref: [2025-11-25] AIX+Notification（push及站内信）.docx / 卡相关通知)
