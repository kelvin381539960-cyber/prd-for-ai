---
module: common
feature: notification
version: "1.2"
status: active
source_doc: IMPLEMENTATION_PLAN.md；[2025-11-25] AIX+Notification（push及站内信）.docx；DTC接口文档/DTC Wallet OpenAPI Document20260126 (1).docx；knowledge-base/wallet/deposit.md；knowledge-base/common/walletconnect.md；knowledge-base/common/errors.md
source_section: Notification PRD / Deposit rows；DTC Wallet OpenAPI / 4.6 Webhook Service；Wallet Deposit v1.4；WalletConnect v1.2
last_updated: 2026-05-01
owner: 吴忆锋
depends_on:
  - common/_index
  - common/walletconnect
  - common/errors
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
| 钱包充值成功 | Webhook→notify | `event=CRYPTO_TXN`，`type=DEPOSIT`，`state=success` | 交易详情页 | Notification PRD / Deposit row |
| 钱包充值冻结 / under review | Webhook→notify | `event=CRYPTO_TXN`，`type=DEPOSIT`，`state=RISK_WITHHELD` | 交易详情页 | Notification PRD / Deposit row |

## 3. 已确认通知参数

| 通知类型 | 参数 | 来源 | 备注 |
|---|---|---|---|
| 卡交易 / 卡退款通知 | `merchant_name` | Notification PRD | 商户名称 |
| 卡交易 / 卡退款通知 | `amount` | Notification PRD | 金额 |
| 卡交易 / 卡退款通知 | `currency` | Notification PRD | 币种 |
| 卡交易 / 卡退款通知 | `transaction_time` | Notification PRD | 交易时间 |
| 卡交易 / 卡退款通知 | `full_name` | Notification PRD | 用户姓名 |
| 卡交易 / 卡退款通知 | `last 4` | Notification PRD | 卡号后 4 位 |
| 钱包充值成功 | `amount`、`currency` | Notification PRD / Deposit row | 模板参数 |
| 钱包充值冻结 / under review | `full_name`、`deposit_transaction_hash`、`amount`、`currency` | Notification PRD / Deposit row | 模板参数 |

## 4. Deposit 通知边界

Deposit 当前 active，包含 GTR 和 WalletConnect。现有 Notification PRD 明确的是 Deposit 通用通知，不足以证明 GTR 与 WalletConnect 各自完整通知规则完全相同。

| 通知场景 | 已确认 | 未确认 |
|---|---|---|
| 钱包充值成功 | `event=CRYPTO_TXN`、`type=DEPOSIT`、`state=success` 触发；跳转交易详情页；渠道为 in-app Notification 及 push | 是否覆盖 GTR / WC 所有路径、具体 webhook 逻辑 |
| 钱包充值冻结 / under review | `event=CRYPTO_TXN`、`type=DEPOSIT`、`state=RISK_WITHHELD` 触发；跳转交易详情页；渠道为 Email、in-app Notification 及 push | 是否覆盖 GTR / WC 所有路径、review 后续处理 |
| 入金失败通知 | 未确认 | 不写成事实 |
| Declare / Travel Rule 待处理通知 | 未确认 | 不写成事实 |
| 资金可见 / 入账完成通知 | 未确认 | 不写成除 success 外的独立事实 |

## 5. Deposit 通知文案边界

| 通知 | 已确认文案 / key | 来源 |
|---|---|---|
| 钱包充值成功 push title | `deposit_successful` | Notification PRD / Deposit row |
| 钱包充值成功 push body | `your_aix_pay_wallet_received` | Notification PRD / Deposit row |
| 钱包充值成功英文展示 | Title: `Deposit successful`; Body: `Your AIX Pay wallet received %1$s %2$s.` | Notification PRD / Deposit row |
| 钱包充值冻结 push title | `deposit_under_review` | Notification PRD / Deposit row |
| 钱包充值冻结 push body | `your_deposit_of_3s_4s` | Notification PRD / Deposit row |
| 钱包充值冻结邮件 title | `action_required_for` | Notification PRD / Deposit row |
| 钱包充值冻结邮件 body | `hi_1s_your_stablecoin_deposit` | Notification PRD / Deposit row |

## 6. 通知与业务结果边界

| 场景 | 当前结论 | 来源 | 处理 |
|---|---|---|---|
| 卡退款 / 卡交易成功通知 | 正常情况下用户收到通知后，预期资金已归集至 Wallet | 用户确认 / Card Transaction Flow | 可作为正常用户预期 |
| 极端异常 | 卡有钱但转 Wallet 失败时，用户可能看不到资金 | 用户确认 / Card Transaction Flow | 不得写成通知必然等于 Wallet 到账 |
| DTC transfer 成功但 Wallet 未到账 | 当前无法系统自动发现，主要依赖用户反馈 | 用户确认 / Card Transaction Flow | 不得写成通知可自动发现异常 |
| 钱包充值成功通知 | Notification PRD 显示 success 通知 | 不代表所有 Deposit 子路径状态机完整闭环 |
| 钱包充值冻结通知 | Notification PRD 显示 Risk Withheld / under review 通知 | 不代表 Declare / Travel Rule 流程已完整确认 |

## 7. WalletConnect 通知重点问题

| 问题 | 当前处理 |
|---|---|
| 钱包连接成功是否通知 | 待补，不默认存在 |
| 钱包连接失败是否通知 | 待补，不默认存在 |
| 用户拒绝授权是否通知 | 待补，不默认存在 |
| 入金已发起是否通知 | 待补，不默认存在 |
| 入金 on-hold / Risk Withheld 是否通知 | Deposit under review 已有通用通知；是否专属于 WC 待确认 |
| 入金 rejected 是否通知 | 待补，不默认存在 |
| 入金 completed 是否通知 | Deposit success 已有通用通知；是否专属于 WC 待确认 |
| 通知是否跳转交易详情 | Deposit 通知记录跳转交易详情页；WC 具体跳转目标待确认 |

## 8. Send / Swap 通知边界

| 能力 | 当前状态 | Notification 处理 |
|---|---|---|
| Send / Withdraw | deferred，未上线 | 不归档 active 通知规则 |
| Swap | deferred，未上线且需重做 | 不归档 active 通知规则 |

## 9. 不写入事实的内容

以下内容不得写成事实：

1. GTR 和 WalletConnect 使用同一套通知模板。
2. GTR 和 WalletConnect 使用同一套通知触发条件。
3. 钱包充值成功通知覆盖所有 Deposit 子路径和所有异常后恢复场景。
4. 通知系统可自动发现 DTC transfer 成功但 Wallet 未到账。
5. WalletConnect 钱包连接成功 / 失败一定会通知。
6. WalletConnect 通知一定跳转交易详情。
7. Send / Swap 有当前 active 通知规则。
8. 未在 Notification PRD 中出现的模板参数。

## 10. 待补项

| 编号 | 待补项 | 来源建议 | 当前处理 |
|---|---|---|---|
| NOTIF-GAP-001 | GTR Deposit 是否完全复用 Deposit success / Risk Withheld 通知 | GTR PRD / 产品确认 | 待补 |
| NOTIF-GAP-002 | WalletConnect Deposit 是否完全复用 Deposit success / Risk Withheld 通知 | WC PRD / 产品确认 | 待补 |
| NOTIF-GAP-003 | Wallet 入金失败通知 | Notification PRD / 风控 PRD | 待补 |
| NOTIF-GAP-004 | Wallet KYC 通知规则 | Notification PRD / KYC PRD | 待补 |
| NOTIF-GAP-005 | 站内信与 Push 是否完全一致 | Notification PRD / 产品确认 | 待补 |
| NOTIF-GAP-006 | 通知失败重试 / 补发策略 | 后端确认 | 待补 |
| NOTIF-GAP-007 | Deposit 通知是否以 Wallet 入账为触发点 | 后端 / 产品确认 | 待补 |

## 11. 来源引用

- (Ref: [2025-11-25] AIX+Notification / Deposit success row)
- (Ref: [2025-11-25] AIX+Notification / Deposit under review row)
- (Ref: DTC Wallet OpenAPI Document20260126 / 4.6 Webhook Service)
- (Ref: knowledge-base/wallet/deposit.md / v1.4)
- (Ref: knowledge-base/common/walletconnect.md / v1.2)
- (Ref: knowledge-base/common/errors.md / v1.1)
