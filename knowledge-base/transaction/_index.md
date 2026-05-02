---
module: transaction
feature: transaction-index
version: "1.1"
status: active
source_doc: IMPLEMENTATION_PLAN.md；knowledge-base/card/card-transaction-flow.md；knowledge-base/card/card-status-and-fields.md；knowledge-base/transaction/history.md；knowledge-base/transaction/reconciliation.md；knowledge-base/wallet/balance.md；knowledge-base/wallet/deposit.md；knowledge-base/wallet/receive.md；knowledge-base/changelog/knowledge-gaps.md；用户确认结论 2026-05-02
source_section: Transaction 统一层；Wallet Transaction History 合并；Transaction Reconciliation 新增；ALL-GAP 总表
last_updated: 2026-05-02
owner: 吴忆锋
depends_on:
  - card/card-transaction-flow
  - card/card-status-and-fields
  - transaction/status-model
  - transaction/history
  - transaction/detail
  - transaction/reconciliation
  - wallet/balance
  - wallet/deposit
  - wallet/receive
  - changelog/knowledge-gaps
---

# Transaction 模块索引

## 1. 模块定位

Transaction 统一层用于沉淀 AIX 中跨 Card / Wallet / Deposit 的交易状态、交易历史、交易详情、资金追踪和对账边界。

本模块不是重新定义 Card 或 Wallet 的业务流程，而是在已确认事实基础上建立统一引用关系：

- Card 交易展示引用 Card Transaction Flow 与 Card 状态事实源。
- Wallet 交易展示主事实源为 `transaction/history.md`。
- Card / Wallet / Deposit 的资金追踪与对账边界由 `transaction/reconciliation.md` 承接。
- Card Transaction Flow 与 Wallet 阶段中的 deferred gaps 不得在 Transaction 阶段补写为事实，统一引用 ALL-GAP。
- Send / Swap 当前为 deferred，不纳入 active Transaction 统一层。

## 2. 当前文件

| 文件 | 状态 | 目标 | 备注 |
|---|---|---|---|
| `transaction/_index.md` | active | 建立 Transaction 统一层边界、状态来源和引用规则 | 当前文件 |
| `transaction/status-model.md` | active | 汇总 Card / Wallet 已确认状态，不脑补完整状态机 | 已建立基础事实 |
| `transaction/history.md` | active | 汇总 Card History / Wallet Transaction History / Deposit History | 已合并原 `wallet/transaction-history.md` |
| `transaction/detail.md` | active | 汇总 Card / Wallet 交易详情字段边界 | 保持字段隔离 |
| `transaction/reconciliation.md` | active | 资金追踪 / ID 链路 / 对账边界 | 新增，对应 ALL-GAP P0 |
| `transaction/stage-review.md` | active | Transaction 阶段完成后执行 Stage Review | 后续需同步结构调整结论 |

## 3. 状态来源边界

| 来源模块 | 可引用内容 | 不可补写内容 |
|---|---|---|
| Card Status & Fields | Card 状态、卡字段、卡操作限制 | 不重新定义卡状态 |
| Card Transaction Flow | Card Transaction Notify、Card History、Card Transaction Details、refund / reversal / deposit 归集触发边界 | 不补写 AIX 内部交易 ID、归集请求 ID、Wallet relatedId、对账字段 |
| Transaction History | Wallet `id`、`transactionId`、`state`、Search Balance History 基础能力 | 不补写 ActivityType 到产品路径映射 |
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
| `PENDING` | 可作为 Wallet 交易状态枚举引用；进入 / 退出条件待 ALL-GAP 收敛 |
| `PROCESSING` | 可作为 Wallet 交易状态枚举引用；进入 / 退出条件待 ALL-GAP 收敛 |
| `AUTHORIZED` | 可作为 Wallet 交易状态枚举引用；进入 / 退出条件待 ALL-GAP 收敛 |
| `COMPLETED` | 可作为 Wallet 交易状态枚举引用；不直接等同 Deposit success |
| `REJECTED` | 可作为 Wallet 交易状态枚举引用；不直接等同 Risk Withheld |
| `CLOSED` | 可作为 Wallet 交易状态枚举引用；关闭条件待补 |

### 4.2 Card Transaction 状态

Card Transaction 相关状态、类型、交易详情字段应优先引用：

- `knowledge-base/card/card-transaction-flow.md`
- `knowledge-base/card/card-status-and-fields.md`

Transaction 阶段不得将 Card 状态与 Wallet 状态强行合并为同一枚举。

## 5. 交易历史边界

| 历史类型 | 来源 | 当前处理 |
|---|---|---|
| Card History | Card Transaction Flow / Transaction & History PRD | 由 `transaction/history.md` 汇总 |
| Card Transaction Details | Card Transaction Flow / DTC Card Issuing | 由 `transaction/detail.md` 汇总 |
| Wallet Transaction History | DTC Wallet OpenAPI / Search Balance History | 由 `transaction/history.md` 维护主事实 |
| Wallet Transaction Detail | DTC Wallet OpenAPI | 由 `transaction/detail.md` 汇总 |
| Deposit History | Wallet Deposit / DTC Wallet OpenAPI | 由 `transaction/history.md` 汇总边界 |
| Reconciliation | Card / Wallet / DTC / ALL-GAP | 由 `transaction/reconciliation.md` 汇总边界 |
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
10. Transaction 模块单独维护 checklist / gap 表。

## 7. ALL-GAP 引用原则

Transaction 模块不维护独立 checklist。以下问题统一引用 `knowledge-base/changelog/knowledge-gaps.md`：

| 主题 | ALL-GAP |
|---|---|
| GTR / WalletConnect 与 ActivityType 映射 | ALL-GAP-001、ALL-GAP-002 |
| Wallet id / transactionId / relatedId 关系 | ALL-GAP-007、ALL-GAP-014、ALL-GAP-015 |
| Deposit success / Risk Withheld 与 Wallet state | ALL-GAP-008、ALL-GAP-016 |
| Card ↔ Wallet 资金追踪 | ALL-GAP-017 ~ ALL-GAP-029 |
| Webhook 落库与排障 | ALL-GAP-022、ALL-GAP-036 |

## 8. Transaction 阶段输出要求

| 输出 | 要求 |
|---|---|
| `status-model.md` | 只汇总已确认状态，未确认进入 / 退出条件必须引用 ALL-GAP |
| `history.md` | 区分 Card History 与 Wallet History，不合并字段来源 |
| `detail.md` | 区分 Card Transaction Detail 与 Wallet Transaction Detail，不混写 `transactionId` |
| `reconciliation.md` | 只沉淀资金追踪和对账边界，引用 ALL-GAP，不新增 checklist |
| `stage-review.md` | 检查状态闭环、字段来源、ALL-GAP 引用、未上线功能是否被误归档 |

## 9. Stage Review 关注点

Transaction 阶段完成后必须检查：

1. Card / Wallet 状态是否只引用已确认来源。
2. 是否存在把不同模块状态强行合并的问题。
3. Card History 与 Wallet History 的字段来源是否清晰。
4. Card Detail 与 Wallet Detail 的 `transactionId` 口径是否隔离。
5. Reconciliation 是否只引用 ALL-GAP，不单独维护待确认清单。
6. Send / Swap 是否保持 deferred。
7. Deposit / Receive 的待补状态是否没有被写成完整状态机。
8. Card / Wallet 资金追踪 deferred gaps 是否仍统一在 ALL-GAP。

## 10. 来源引用

- (Ref: IMPLEMENTATION_PLAN.md / v4.5)
- (Ref: knowledge-base/card/card-transaction-flow.md / v1.2)
- (Ref: knowledge-base/card/card-status-and-fields.md)
- (Ref: knowledge-base/transaction/history.md / v1.2)
- (Ref: knowledge-base/transaction/reconciliation.md / v1.0)
- (Ref: knowledge-base/wallet/balance.md)
- (Ref: knowledge-base/wallet/deposit.md / v1.5)
- (Ref: knowledge-base/wallet/receive.md)
- (Ref: knowledge-base/changelog/knowledge-gaps.md / ALL-GAP 总表)
- (Ref: 用户确认结论 / 2026-05-02 / Wallet Transaction History 合并进 Transaction History)
