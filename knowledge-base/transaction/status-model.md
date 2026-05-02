---
module: transaction
feature: status-model
version: "1.1"
status: active
source_doc: IMPLEMENTATION_PLAN.md；DTC接口文档/DTC Wallet OpenAPI Document20260126 (1).docx；DTC接口文档/卡交易&钱包交易状态梳理 (1).docx；knowledge-base/transaction/_index.md；knowledge-base/card/card-transaction-flow.md；knowledge-base/wallet/transaction-history.md；knowledge-base/wallet/deposit.md；knowledge-base/changelog/knowledge-gaps.md
source_section: Transaction _index v1.0；Wallet Transaction History v1.1；Wallet Deposit v1.4；DTC Wallet OpenAPI / 3.4 Crypto Deposit；Appendix ActivityType；Card Transaction Flow v1.2
last_updated: 2026-05-01
owner: 吴忆锋
depends_on:
  - transaction/_index
  - card/card-status-and-fields
  - card/card-transaction-flow
  - wallet/transaction-history
  - wallet/deposit
  - wallet/stage-review
  - changelog/knowledge-gaps
---

# Transaction Status Model 交易状态模型

## 1. 功能定位

Transaction Status Model 用于汇总 Card / Wallet 已确认交易状态和状态边界，作为后续交易历史、交易详情、客服查询和用户展示的统一引用层。

本文件不创建新的状态枚举，不强行合并 Card 与 Wallet 状态机，只整理已确认来源。

## 2. 总体原则

| 原则 | 说明 |
|---|---|
| 不新造状态 | 只引用 Card / Wallet / DTC 文档中已确认状态 |
| 不强行合并 | Card 与 Wallet 状态可并列存在，不合并成一个全局枚举 |
| 不补进入 / 退出条件 | 来源未明确时，只列状态值，不补状态机 |
| 不写 deferred gaps | Card / Wallet 遗留追踪项继续保留在 gaps |
| 不纳入未上线能力 | Send / Swap 当前 deferred，不进入 active 状态模型 |

## 3. Wallet 交易状态

Wallet 当前已确认状态字段为 `state`。

| 状态值 | 来源 | 当前可用范围 | 未确认项 |
|---|---|---|---|
| `PENDING` | Wallet Transaction History | Wallet 交易记录 / 详情状态展示 | 进入 / 退出条件待补 |
| `PROCESSING` | Wallet Transaction History | Wallet 交易记录 / 详情状态展示 | 进入 / 退出条件待补 |
| `AUTHORIZED` | Wallet Transaction History | Wallet 交易记录 / 详情状态展示 | 进入 / 退出条件待补 |
| `COMPLETED` | Wallet Transaction History | Wallet 交易记录 / 详情状态展示 | 进入 / 退出条件待补 |
| `REJECTED` | Wallet Transaction History | Wallet 交易记录 / 详情状态展示 | 失败原因和责任边界待补 |
| `CLOSED` | Wallet Transaction History | Wallet 交易记录 / 详情状态展示 | 关闭条件待补 |

### 3.1 Wallet 状态使用限制

| 限制 | 说明 |
|---|---|
| 不等同于 Deposit 状态机 | GTR / WalletConnect 具体状态映射待补 |
| 不等同于 Receive 状态机 | Receive 是否独立上线及状态映射待补 |
| 不覆盖 Send / Swap | Send / Swap 当前 deferred，不纳入 active 状态模型 |
| 不推导余额状态 | Balance 的可用 / 冻结 / 总余额字段未补齐 |

## 4. Deposit / Crypto 外部状态

DTC Crypto Deposit 中存在 `status=102 Risk Withheld`，表示未加 senderAddress whitelist 时交易进入 risky transaction；用户继续加白并 enable 后，交易会自动变为 success。

| 状态 / 结果 | 来源 | 当前处理 | 不得推导 |
|---|---|---|---|
| `Risk Withheld` / `status=102` | DTC Wallet OpenAPI / 3.4 Crypto Deposit | 可作为 Deposit / WalletConnect 风控、under review、on-hold 类边界来源 | 不得等同 Wallet `REJECTED`、`PENDING` 或 `PROCESSING` |
| `success` | DTC Wallet OpenAPI / Crypto Deposit；Notification Deposit row | 可作为 Deposit success 通知来源 | 不得直接等同 Wallet `COMPLETED` |

## 5. ActivityType 分类

ActivityType 是 Wallet balance / transaction history 的交易分类，不是完整状态机。

| 枚举 | 值 | 含义 | 当前处理 |
|---|---:|---|---|
| `FIAT_DEPOSIT` | 6 | Fiat Deposit | 可作为法币入金分类引用；是否对应 GTR 待确认 |
| `CRYPTO_DEPOSIT` | 10 | Stablecoin Deposit | 可作为 Crypto / WalletConnect 入金分类引用；是否对应 WC 待确认 |
| `DTC_WALLET` | 13 | DTC Wallet Payment | 可作为 DTC Wallet Payment 分类引用 |
| `CARD_PAYMENT_REFUND` | 20 | Card Payment Refund | 可作为 Card refund 入 Wallet 相关分类引用；与 Card 归集链路关联仍待确认 |

## 6. Card 交易状态与类型

Card 交易状态与类型优先引用 `card/card-transaction-flow.md` 和 `card/card-status-and-fields.md`。

| 项目 | 当前已确认 | 来源 | 当前处理 |
|---|---|---|---|
| Card Transaction Notify | DTC 通过 Card Transaction Notify 通知卡交易 | Card Transaction Flow | 可引用 |
| DTC Card Transaction ID | `data.id` 为 Transaction ID | Card Transaction Flow | 可引用 |
| DTC Original Transaction ID | `originalId` 为 Original Transaction ID，选填 | Card Transaction Flow | 可引用 |
| 自动归集触发类型 | `refund` / `reversal` / `deposit` | Card Transaction Flow | 可引用 |
| Top-up | 不触发自动归集 | Card Transaction Flow | 可引用 |
| DTC Transaction Status | 已在 Card Transaction Flow 中引用 DTC 枚举，如 `AUTHORIZED`、`SUCCESS`、`CAPTURED`、`REVERSED`、`CANCELLED`、`REFUNDED`、`DENIED`、`EXPIRED` | Card Transaction Flow / DTC Card Issuing | 可引用，但不与 Wallet state 合并 |

## 7. 跨模块状态对照

当前只允许做“来源对照”，不做“语义等价映射”。

| 维度 | Card | Wallet / Deposit | 当前处理 |
|---|---|---|---|
| 状态字段 | DTC Card Transaction status / state 来源 | Wallet `state`；Deposit `Risk Withheld` / `success` | 并列记录，不合并 |
| 交易 ID | Card `data.id` | Wallet `id` / `transactionId` | 不认为相等 |
| 关联 ID | `originalId`、`processorTransactionId`、`referenceNo` 等 | `relatedId` | 关联规则未确认 |
| 成功态 | Card 有 `SUCCESS` / `CAPTURED` 等来源状态 | Wallet 有 `COMPLETED`；Deposit 有 `success` | 不做等价映射 |
| 失败 / 风控态 | Card 有 `DENIED` / `EXPIRED` 等来源状态 | Wallet 有 `REJECTED` / `CLOSED`；Deposit 有 `Risk Withheld` | 不做等价映射 |

## 8. 不写入事实的内容

以下内容当前不得写成事实：

1. Card `SUCCESS` 等同于 Wallet `COMPLETED`。
2. Deposit `success` 等同于 Wallet `COMPLETED`。
3. Risk Withheld 等同于 Wallet `REJECTED`。
4. Card `DENIED` 等同于 Wallet `REJECTED`。
5. Card `data.id` 等同于 Wallet `transactionId`。
6. Wallet `relatedId` 等同于 Card `data.id`。
7. Wallet `relatedId` 等同于 AIX 归集请求 ID。
8. `CRYPTO_DEPOSIT` 必然等同 WalletConnect。
9. `FIAT_DEPOSIT` 必然等同 GTR。
10. Deposit GTR / WalletConnect 状态机已完整闭环。
11. Send / Swap 状态参与当前 active 交易状态模型。

## 9. 待补状态清单

| 编号 | 待补项 | 来源建议 | 当前处理 |
|---|---|---|---|
| TXN-STATUS-GAP-001 | Wallet `state` 进入 / 退出条件 | Wallet PRD / DTC Wallet OpenAPI | 待补 |
| TXN-STATUS-GAP-002 | Wallet 状态与前端展示文案映射 | Wallet PRD / 截图 | 待补 |
| TXN-STATUS-GAP-003 | GTR Deposit 与 `FIAT_DEPOSIT`、Wallet `state` 的映射 | GTR PRD / 接口文档 | 待补 |
| TXN-STATUS-GAP-004 | WalletConnect Deposit 与 `CRYPTO_DEPOSIT`、Wallet `state` 的映射 | WC PRD / 接口文档 | 待补 |
| TXN-STATUS-GAP-005 | `Risk Withheld` 对前端展示、余额、通知、状态的完整影响 | DTC / Wallet PRD / Notification | 待补 |
| TXN-STATUS-GAP-006 | Receive 状态映射 | Receive PRD / 接口文档 | 待补 |
| TXN-STATUS-GAP-007 | Card DTC 状态与 AIX 前端展示状态映射 | Card 状态梳理表 / Transaction & History PRD | 待补 |
| TXN-STATUS-GAP-008 | 跨模块最终展示状态是否需要统一文案 | 产品确认 / UX | 待补 |

## 10. 来源引用

- (Ref: DTC Wallet OpenAPI Document20260126 / 3.4 Crypto Deposit)
- (Ref: DTC Wallet OpenAPI Document20260126 / Appendix ActivityType)
- (Ref: knowledge-base/wallet/transaction-history.md / v1.1)
- (Ref: knowledge-base/wallet/deposit.md / v1.4)
- (Ref: knowledge-base/card/card-transaction-flow.md / v1.2)
- (Ref: knowledge-base/changelog/knowledge-gaps.md / Card Transaction Flow deferred gaps)
