---
module: transaction
feature: status-model
version: "1.2"
status: active
source_doc: IMPLEMENTATION_PLAN.md；DTC接口文档/DTC Wallet OpenAPI Document20260126 (1).docx；DTC接口文档/卡交易&钱包交易状态梳理 (1).docx；knowledge-base/transaction/_index.md；knowledge-base/card/card-transaction-flow.md；knowledge-base/transaction/history.md；knowledge-base/wallet/deposit.md；knowledge-base/changelog/knowledge-gaps.md
source_section: Transaction _index v1.1；Transaction History v1.2；Wallet Deposit v1.6；DTC Wallet OpenAPI / 3.4 Crypto Deposit；Appendix ActivityType；Card Transaction Flow v1.2；ALL-GAP 总表
last_updated: 2026-05-02
owner: 吴忆锋
depends_on:
  - transaction/_index
  - card/card-status-and-fields
  - card/card-transaction-flow
  - transaction/history
  - wallet/deposit
  - wallet/stage-review
  - changelog/knowledge-gaps
---

# Transaction Status Model 交易状态模型

## 1. 功能定位

Transaction Status Model 用于汇总 Card / Wallet 已确认交易状态和状态边界，作为后续交易历史、交易详情、客服查询和用户展示的统一引用层。

本文件不创建新的状态枚举，不强行合并 Card 与 Wallet 状态机，只整理已确认来源。

所有未确认问题统一引用 `knowledge-base/changelog/knowledge-gaps.md` 的 ALL-GAP 编号；本文不再维护独立 TXN-STATUS-GAP checklist。

## 2. 总体原则

| 原则 | 说明 |
|---|---|
| 不新造状态 | 只引用 Card / Wallet / DTC 文档中已确认状态 |
| 不强行合并 | Card 与 Wallet 状态可并列存在，不合并成一个全局枚举 |
| 不补进入 / 退出条件 | 来源未明确时，只列状态值，不补状态机；见 ALL-GAP-050 |
| 不写模块级 gap | 未确认项统一引用 ALL-GAP |
| 不纳入未上线能力 | Send / Swap 当前 deferred，不进入 active 状态模型 |

## 3. Wallet 交易状态

Wallet 当前已确认状态字段为 `state`。

| 状态值 | 来源 | 当前可用范围 | ALL-GAP 边界 |
|---|---|---|---|
| `PENDING` | Transaction History | Wallet 交易记录 / 详情状态展示 | 进入 / 退出条件见 ALL-GAP-050；前端文案见 ALL-GAP-051 |
| `PROCESSING` | Transaction History | Wallet 交易记录 / 详情状态展示 | 进入 / 退出条件见 ALL-GAP-050；前端文案见 ALL-GAP-051 |
| `AUTHORIZED` | Transaction History | Wallet 交易记录 / 详情状态展示 | 进入 / 退出条件见 ALL-GAP-050；前端文案见 ALL-GAP-051 |
| `COMPLETED` | Transaction History | Wallet 交易记录 / 详情状态展示 | 与 Deposit success 的映射见 ALL-GAP-016 |
| `REJECTED` | Transaction History | Wallet 交易记录 / 详情状态展示 | 失败原因和责任边界见 ALL-GAP-038、ALL-GAP-039 |
| `CLOSED` | Transaction History | Wallet 交易记录 / 详情状态展示 | 关闭条件见 ALL-GAP-050 |

### 3.1 Wallet 状态使用限制

| 限制 | 说明 |
|---|---|
| 不等同于 Deposit 状态机 | GTR / WalletConnect 具体状态映射见 ALL-GAP-001、ALL-GAP-002、ALL-GAP-016 |
| 不等同于 Receive 状态机 | Receive 是否独立上线及状态映射见 ALL-GAP-052 |
| 不覆盖 Send / Swap | Send / Swap 当前 deferred，不纳入 active 状态模型 |
| 不推导余额状态 | Balance 的可用 / 冻结 / 总余额字段未补齐；Risk Withheld 与余额关系见 ALL-GAP-008 |

## 4. Deposit / Crypto 外部状态

| 状态 / 结果 | 来源 | 当前处理 | 不得推导 |
|---|---|---|---|
| `Risk Withheld` / `status=102` | DTC Wallet OpenAPI / 3.4 Crypto Deposit | 用户确认不触发结果页，详情展示 under review | 不得等同 Wallet `REJECTED`、`PENDING` 或 `PROCESSING`；余额关系见 ALL-GAP-008 |
| `success` | DTC Wallet OpenAPI / Crypto Deposit；Notification Deposit row | 可作为 Deposit success 通知来源；payment_info success 会触发资金流转账但可能有很短延迟 | 不得直接等同 Wallet `COMPLETED`；见 ALL-GAP-016 |

## 5. ActivityType 分类

ActivityType 是 Wallet balance / transaction history 的交易分类，不是完整状态机。

| 枚举 | 值 | 含义 | 当前处理 |
|---|---:|---|---|
| `FIAT_DEPOSIT` | 6 | Fiat Deposit | 可作为法币入金分类引用；是否对应 GTR 见 ALL-GAP-001 |
| `CRYPTO_DEPOSIT` | 10 | Stablecoin Deposit | 可作为 Crypto / WalletConnect 入金分类引用；是否对应 WC 见 ALL-GAP-002 |
| `DTC_WALLET` | 13 | DTC Wallet Payment | 可作为 DTC Wallet Payment 分类引用；前端展示映射见 ALL-GAP-037 |
| `CARD_PAYMENT_REFUND` | 20 | Card Payment Refund | 可作为 Card refund 入 Wallet 相关分类引用；与 Card 归集链路关联见 ALL-GAP-017、ALL-GAP-018 |

## 6. Card 交易状态与类型

Card 交易状态与类型优先引用 `card/card-transaction-flow.md` 和 `card/card-status-and-fields.md`。

| 项目 | 当前已确认 | 来源 | 当前处理 |
|---|---|---|---|
| Card Transaction Notify | DTC 通过 Card Transaction Notify 通知卡交易 | Card Transaction Flow | 可引用 |
| DTC Card Transaction ID | `data.id` 为 Transaction ID | Card Transaction Flow | 可引用 |
| DTC Original Transaction ID | `originalId` 为 Original Transaction ID，选填 | Card Transaction Flow | 可引用 |
| 自动归集触发类型 | `refund` / `reversal` / `deposit` | Card Transaction Flow | 可引用；附加判断见 ALL-GAP-024 |
| Top-up | 不触发自动归集 | Card Transaction Flow | 可引用 |
| DTC Transaction Status | Card Transaction Flow 中已有 DTC 交易状态来源 | Card Transaction Flow / DTC Card Issuing | 可引用，但不与 Wallet state 合并；前端展示映射见 ALL-GAP-053 |

## 7. 跨模块状态对照

当前只允许做“来源对照”，不做“语义等价映射”。

| 维度 | Card | Wallet / Deposit | 当前处理 |
|---|---|---|---|
| 状态字段 | DTC Card Transaction status / state 来源 | Wallet `state`；Deposit `Risk Withheld` / `success` | 并列记录，不合并 |
| 交易 ID | Card `data.id` | Wallet `id` / `transactionId` | 不认为相等；关联见 ALL-GAP-018 |
| 关联 ID | `originalId`、`processorTransactionId`、`referenceNo` 等 | `relatedId` | 关联规则见 ALL-GAP-014、ALL-GAP-018 |
| 成功态 | Card 有来源状态 | Wallet 有 `COMPLETED`；Deposit 有 `success` | 不做等价映射 |
| 失败 / 风控态 | Card 有来源状态 | Wallet 有 `REJECTED` / `CLOSED`；Deposit 有 `Risk Withheld` | 不做等价映射 |
| 展示文案 | Card 前端展示待确认 | Wallet / Deposit 前端展示待确认 | 是否统一文案见 ALL-GAP-054 |

## 8. 不写入事实的内容

以下内容当前不得写成事实：

1. Card 成功态等同于 Wallet `COMPLETED`。
2. Deposit `success` 等同于 Wallet `COMPLETED`。
3. Risk Withheld 等同于 Wallet `REJECTED`。
4. Card 失败态等同于 Wallet `REJECTED`。
5. Card `data.id` 等同于 Wallet `transactionId`。
6. Wallet `relatedId` 等同于 Card `data.id`。
7. Wallet `relatedId` 等同于 AIX 归集请求 ID。
8. `CRYPTO_DEPOSIT` 必然等同 WalletConnect。
9. `FIAT_DEPOSIT` 必然等同 GTR。
10. Deposit GTR / WalletConnect 状态机已完整闭环。
11. Send / Swap 状态参与当前 active 交易状态模型。
12. Card / Wallet / Deposit 前端展示状态已统一。

## 9. ALL-GAP 引用

本文不维护独立待补表。Transaction Status 相关不确定项统一引用 ALL-GAP：

| 编号 | 主题 |
|---|---|
| ALL-GAP-001 | GTR 是否使用 `FIAT_DEPOSIT=6` |
| ALL-GAP-002 | WalletConnect 是否使用 `CRYPTO_DEPOSIT=10` |
| ALL-GAP-008 | Risk Withheld 与 Wallet `state` / 余额关系 |
| ALL-GAP-016 | Deposit success 与 Wallet `state=COMPLETED` 的映射 |
| ALL-GAP-024 | 自动归集触发附加判断 |
| ALL-GAP-037 | ActivityType 到 AIX 前端交易类型的映射 |
| ALL-GAP-050 | Wallet `state` 进入 / 退出条件 |
| ALL-GAP-051 | Wallet 状态与前端展示文案映射 |
| ALL-GAP-052 | Receive 是否独立上线及状态映射 |
| ALL-GAP-053 | Card DTC 状态与 AIX 前端展示状态映射 |
| ALL-GAP-054 | 跨模块最终展示状态是否需要统一文案 |

## 10. 历史 TXN-STATUS-GAP 到 ALL-GAP 映射

本表用于无损迁移历史问题，不作为新的模块级 checklist。后续只维护 ALL-GAP。

| 原编号 | 原问题 | 当前 ALL-GAP |
|---|---|---|
| TXN-STATUS-GAP-001 | Wallet `state` 进入 / 退出条件 | ALL-GAP-050 |
| TXN-STATUS-GAP-002 | Wallet 状态与前端展示文案映射 | ALL-GAP-051 |
| TXN-STATUS-GAP-003 | GTR Deposit 与 `FIAT_DEPOSIT`、Wallet `state` 的映射 | ALL-GAP-001、ALL-GAP-016 |
| TXN-STATUS-GAP-004 | WalletConnect Deposit 与 `CRYPTO_DEPOSIT`、Wallet `state` 的映射 | ALL-GAP-002、ALL-GAP-016 |
| TXN-STATUS-GAP-005 | `Risk Withheld` 对前端展示、余额、通知、状态的完整影响 | ALL-GAP-003、ALL-GAP-008、ALL-GAP-010 |
| TXN-STATUS-GAP-006 | Receive 状态映射 | ALL-GAP-052 |
| TXN-STATUS-GAP-007 | Card DTC 状态与 AIX 前端展示状态映射 | ALL-GAP-053 |
| TXN-STATUS-GAP-008 | 跨模块最终展示状态是否需要统一文案 | ALL-GAP-054 |

## 11. 来源引用

- (Ref: DTC Wallet OpenAPI Document20260126 / 3.4 Crypto Deposit)
- (Ref: DTC Wallet OpenAPI Document20260126 / Appendix ActivityType)
- (Ref: knowledge-base/transaction/history.md / v1.2)
- (Ref: knowledge-base/wallet/deposit.md / v1.6)
- (Ref: knowledge-base/card/card-transaction-flow.md / v1.2)
- (Ref: knowledge-base/changelog/knowledge-gaps.md / ALL-GAP 总表)
