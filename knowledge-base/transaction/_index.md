---
module: transaction
feature: transaction-index
version: "1.0"
status: active
source_doc: IMPLEMENTATION_PLAN.md；knowledge-base/card/card-transaction-flow.md；knowledge-base/card/card-status-and-fields.md；knowledge-base/wallet/transaction-history.md；knowledge-base/wallet/balance.md；knowledge-base/wallet/deposit.md；knowledge-base/wallet/receive.md；knowledge-base/wallet/stage-review.md；knowledge-base/changelog/knowledge-gaps.md
source_section: IMPLEMENTATION_PLAN v3.9 / Transaction 统一层；Card Transaction Flow v1.2；Wallet Transaction History v1.0；Wallet Stage Review v1.0
last_updated: 2026-05-01
owner: 吴忆锋
depends_on:
  - card/card-transaction-flow
  - card/card-status-and-fields
  - wallet/transaction-history
  - wallet/balance
  - wallet/deposit
  - wallet/receive
  - wallet/stage-review
  - changelog/knowledge-gaps
---

# Transaction 模块索引

## 1. 模块定位

Transaction 统一层用于沉淀 AIX 中跨 Card / Wallet 的交易状态、交易历史、交易详情和展示边界。

本模块不是重新定义 Card 或 Wallet 的业务流程，而是在已确认事实基础上建立统一引用关系：

- Card 交易展示引用 Card Transaction Flow 与 Card 状态事实源。
- Wallet 交易展示引用 Wallet Transaction History。
- Card Transaction Flow 与 Wallet 阶段中的 deferred gaps 不得在 Transaction 阶段补写为事实。
- Send / Swap 当前为 deferred，不纳入 active Transaction 统一层。

## 2. 当前阶段任务

| 文件 | 状态 | 目标 | 备注 |
|---|---|---|---|
| `transaction/_index.md` | active | 建立 Transaction 统一层边界、状态来源和引用规则 | 当前文件 |
| `transaction/status-model.md` | Todo | 汇总 Card / Wallet 已确认状态，不脑补完整状态机 | 后续执行 |
| `transaction/history.md` | Todo | 汇总 Card History / Wallet Transaction History 的边界 | 后续执行 |
| `transaction/detail.md` | Todo | 汇总 Card / Wallet 交易详情字段边界 | 后续执行 |
| `transaction/stage-review.md` | Todo | Transaction 阶段完成后执行 Stage Review | 后续执行 |

## 3. 状态来源边界

| 来源模块 | 可引用内容 | 不可补写内容 |
|---|---|---|
| Card Status & Fields | Card 状态、卡字段、卡操作限制 | 不重新定义卡状态 |
| Card Transaction Flow | Card Transaction Notify、Card History、Card Transaction Details、refund / reversal / deposit 归集触发边界 | 不补写 AIX 内部交易 ID、归集请求 ID、Wallet relatedId、对账字段 |
| Wallet Transaction History | Wallet `id`、`transactionId`、`state`、Search Balance History 基础能力 | 不补写 activityType 枚举、Deposit / Receive 完整状态机 |
| Wallet Balance | Wallet balance 基础边界 | 不补写余额接口字段、可用 / 冻结 / 总余额字段 |
| Wallet Deposit | Deposit active，包含 GTR 和 WalletConnect | 不混写 GTR 与 WalletConnect 的字段 / 状态 / 风控规则 |
| Wallet Receive | Receive 基础占位 | 不默认 Receive 独立上线，也不默认等同 Deposit |
| Wallet Send | deferred | 不纳入 active 交易状态统一 |
| Wallet Swap | deferred | 不纳入 active 交易状态统一 |

## 4. 已确认状态集合

### 4.1 Wallet state

Wallet 当前已确认交易状态字段为 `state`，枚举为：

| 枚举 | 当前处理 |
|---|---|
| `PENDING` | 可作为 Wallet 交易状态枚举引用；进入 / 退出条件待补 |
| `PROCESSING` | 可作为 Wallet 交易状态枚举引用；进入 / 退出条件待补 |
| `AUTHORIZED` | 可作为 Wallet 交易状态枚举引用；进入 / 退出条件待补 |
| `COMPLETED` | 可作为 Wallet 交易状态枚举引用；进入 / 退出条件待补 |
| `REJECTED` | 可作为 Wallet 交易状态枚举引用；失败原因待补 |
| `CLOSED` | 可作为 Wallet 交易状态枚举引用；关闭条件待补 |

### 4.2 Card Transaction 状态

Card Transaction 相关状态、类型、交易详情字段应优先引用：

- `knowledge-base/card/card-transaction-flow.md`
- `knowledge-base/card/card-status-and-fields.md`

Transaction 阶段不得将 Card 状态与 Wallet 状态强行合并为同一枚举。

## 5. 交易历史边界

| 历史类型 | 来源 | 当前处理 |
|---|---|---|
| Card History | Card Transaction Flow / Transaction & History PRD | 后续由 `transaction/history.md` 汇总 |
| Card Transaction Details | Card Transaction Flow / DTC Card Issuing | 后续由 `transaction/detail.md` 汇总 |
| Wallet Transaction History | Wallet Transaction History | 后续由 `transaction/history.md` 汇总 |
| Wallet Transaction Detail | Wallet Transaction History | 后续由 `transaction/detail.md` 汇总 |
| Send / Swap History | deferred | 当前不纳入 active 统一层 |

## 6. 不写入事实的内容

以下内容当前不得写成事实：

1. Card 与 Wallet 使用同一套交易状态枚举。
2. Wallet `transactionId` 等同于 Card `data.id`。
3. Wallet `relatedId` 等同于 Card `data.id` 或 AIX 归集请求 ID。
4. GTR 与 WalletConnect Deposit 使用同一套状态 / 风控 / 字段规则。
5. Receive 已确认独立上线。
6. Send 已上线。
7. Swap 已上线。
8. Wallet Deposit / Receive 完整状态机已经闭环。
9. Card Transaction Flow 的资金追踪链路已经完整闭环。

## 7. Transaction 阶段输出要求

| 输出 | 要求 |
|---|---|
| `status-model.md` | 只汇总已确认状态，未确认进入 / 退出条件必须标注待补 |
| `history.md` | 区分 Card History 与 Wallet History，不合并字段来源 |
| `detail.md` | 区分 Card Transaction Detail 与 Wallet Transaction Detail，不混写 `transactionId` |
| `stage-review.md` | 检查状态闭环、字段来源、deferred gaps 隔离、未上线功能是否被误归档 |

## 8. Stage Review 关注点

Transaction 阶段完成后必须检查：

1. Card / Wallet 状态是否只引用已确认来源。
2. 是否存在把不同模块状态强行合并的问题。
3. Card History 与 Wallet History 的字段来源是否清晰。
4. Card Detail 与 Wallet Detail 的 `transactionId` 口径是否隔离。
5. Send / Swap 是否保持 deferred。
6. Deposit / Receive 的待补状态是否没有被写成完整状态机。
7. Card / Wallet 资金追踪 deferred gaps 是否仍保留。

## 9. 来源引用

- (Ref: IMPLEMENTATION_PLAN.md / v3.9 / Transaction 统一层)
- (Ref: knowledge-base/card/card-transaction-flow.md / v1.2)
- (Ref: knowledge-base/card/card-status-and-fields.md)
- (Ref: knowledge-base/wallet/transaction-history.md / v1.0)
- (Ref: knowledge-base/wallet/balance.md / v1.0)
- (Ref: knowledge-base/wallet/deposit.md / v1.2)
- (Ref: knowledge-base/wallet/receive.md / v1.0)
- (Ref: knowledge-base/wallet/stage-review.md / v1.0)
- (Ref: knowledge-base/changelog/knowledge-gaps.md / Card Transaction Flow deferred gaps)
