---
module: transaction
feature: status-model
version: "1.0"
status: active
source_doc: IMPLEMENTATION_PLAN.md；knowledge-base/transaction/_index.md；knowledge-base/card/card-status-and-fields.md；knowledge-base/card/card-transaction-flow.md；knowledge-base/wallet/transaction-history.md；knowledge-base/wallet/stage-review.md；knowledge-base/changelog/knowledge-gaps.md
source_section: Transaction _index v1.0；Card Status & Fields；Card Transaction Flow v1.2；Wallet Transaction History v1.0；Wallet Stage Review v1.0
last_updated: 2026-05-01
owner: 吴忆锋
depends_on:
  - transaction/_index
  - card/card-status-and-fields
  - card/card-transaction-flow
  - wallet/transaction-history
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
| 不新造状态 | 只引用 Card / Wallet 已确认状态 |
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

## 4. Card 交易状态与类型

Card 交易状态与类型优先引用 `card/card-transaction-flow.md` 和 `card/card-status-and-fields.md`。

| 项目 | 当前已确认 | 来源 | 当前处理 |
|---|---|---|---|
| Card Transaction Notify | DTC 通过 Card Transaction Notify 通知卡交易 | Card Transaction Flow | 可引用 |
| DTC Card Transaction ID | `data.id` 为 Transaction ID | Card Transaction Flow | 可引用 |
| DTC Original Transaction ID | `originalId` 为 Original Transaction ID，选填 | Card Transaction Flow | 可引用 |
| 自动归集触发类型 | `refund` / `reversal` / `deposit` | Card Transaction Flow | 可引用 |
| Top-up | 不触发自动归集 | Card Transaction Flow | 可引用 |
| DTC Transaction Status | 已在 Card Transaction Flow 中引用 DTC 枚举，如 `AUTHORIZED`、`SUCCESS`、`CAPTURED`、`REVERSED`、`CANCELLED`、`REFUNDED`、`DENIED`、`EXPIRED` | Card Transaction Flow / DTC Card Issuing | 可引用，但不与 Wallet state 合并 |

### 4.1 Card 状态使用限制

| 限制 | 说明 |
|---|---|
| 不等同于 Wallet state | Card DTC transaction status 与 Wallet `state` 来源不同 |
| 不补 AIX 内部状态 | AIX 内部交易处理 ID / 状态未确认 |
| 不补归集状态机 | AIX 归集请求 ID、Wallet relatedId、对账字段仍 deferred |
| 不覆盖 Card 页面状态 | Card 状态与卡片状态仍引用 `card-status-and-fields.md` |

## 5. 跨模块状态对照

当前只允许做“来源对照”，不做“语义等价映射”。

| 维度 | Card | Wallet | 当前处理 |
|---|---|---|---|
| 状态字段 | DTC Card Transaction status / state 来源 | Wallet `state` | 并列记录，不合并 |
| 交易 ID | Card `data.id` | Wallet `id` / `transactionId` | 不认为相等 |
| 关联 ID | `originalId`、`processorTransactionId`、`referenceNo` 等 | `relatedId` | 关联规则未确认 |
| 成功态 | Card 有 `SUCCESS` / `CAPTURED` 等来源状态 | Wallet 有 `COMPLETED` | 不做等价映射 |
| 失败态 | Card 有 `DENIED` / `EXPIRED` 等来源状态 | Wallet 有 `REJECTED` / `CLOSED` | 不做等价映射 |

## 6. 不写入事实的内容

以下内容当前不得写成事实：

1. Card `SUCCESS` 等同于 Wallet `COMPLETED`。
2. Card `DENIED` 等同于 Wallet `REJECTED`。
3. Card `data.id` 等同于 Wallet `transactionId`。
4. Wallet `relatedId` 等同于 Card `data.id`。
5. Wallet `relatedId` 等同于 AIX 归集请求 ID。
6. Deposit GTR / WalletConnect 状态机已完整闭环。
7. Receive 状态机已完整闭环。
8. Send / Swap 状态参与当前 active 交易状态模型。
9. Card 归集链路状态已完整闭环。

## 7. 待补状态清单

| 编号 | 待补项 | 来源建议 | 当前处理 |
|---|---|---|---|
| TXN-STATUS-GAP-001 | Wallet `activityType` 枚举 | DTC Wallet OpenAPI | 待补 |
| TXN-STATUS-GAP-002 | Wallet `state` 进入 / 退出条件 | Wallet PRD / DTC Wallet OpenAPI | 待补 |
| TXN-STATUS-GAP-003 | Wallet 状态与前端展示文案映射 | Wallet PRD / 截图 | 待补 |
| TXN-STATUS-GAP-004 | GTR Deposit 状态映射 | GTR PRD / 接口文档 | 待补 |
| TXN-STATUS-GAP-005 | WalletConnect Deposit 状态映射 | WC PRD / 接口文档 | 待补 |
| TXN-STATUS-GAP-006 | Receive 状态映射 | Receive PRD / 接口文档 | 待补 |
| TXN-STATUS-GAP-007 | Card DTC 状态与 AIX 前端展示状态映射 | Card 状态梳理表 / Transaction & History PRD | 待补 |
| TXN-STATUS-GAP-008 | 跨模块最终展示状态是否需要统一文案 | 产品确认 / UX | 待补 |

## 8. 与后续文件关系

| 后续文件 | 使用方式 |
|---|---|
| `transaction/history.md` | 引用本文状态来源，区分 Card History 与 Wallet History |
| `transaction/detail.md` | 引用本文状态来源，区分 Card Detail 与 Wallet Detail |
| `transaction/stage-review.md` | 检查状态来源、状态闭环、deferred gaps 隔离 |

## 9. 来源引用

- (Ref: IMPLEMENTATION_PLAN.md / v3.9 / Transaction 统一层)
- (Ref: knowledge-base/transaction/_index.md / v1.0)
- (Ref: knowledge-base/card/card-status-and-fields.md)
- (Ref: knowledge-base/card/card-transaction-flow.md / v1.2)
- (Ref: knowledge-base/wallet/transaction-history.md / v1.0)
- (Ref: knowledge-base/wallet/stage-review.md / v1.0)
- (Ref: knowledge-base/changelog/knowledge-gaps.md / Card Transaction Flow deferred gaps)
