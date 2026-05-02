---
module: transaction
feature: transaction-index
version: "2.0"
status: active
source_doc: knowledge-base/card/card-transaction-flow.md；knowledge-base/card/card-status-and-fields.md；knowledge-base/transaction/history.md；knowledge-base/transaction/detail.md；knowledge-base/transaction/status-model.md；knowledge-base/transaction/reconciliation.md；knowledge-base/wallet/balance.md；knowledge-base/wallet/deposit.md；knowledge-base/wallet/receive.md；knowledge-base/changelog/knowledge-gaps.md；knowledge-base/_system-boundary.md；用户确认结论 2026-05-02
source_section: Transaction 使用态统一层；Wallet Transaction History 合并；Transaction Reconciliation；ALL-GAP 总表
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
  - _system-boundary
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
| `transaction/history.md` | active | 汇总 Card History / Wallet Transaction History / Deposit History | Wallet History 主事实源 |
| `transaction/detail.md` | active | 汇总 Card / Wallet 交易详情字段边界 | 保持字段隔离 |
| `transaction/reconciliation.md` | active | 资金追踪 / ID 链路 / 对账边界 | 对应 ALL-GAP P0 |

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

## 8. 使用规则

1. 查询交易历史时读 `transaction/history.md`。
2. 查询交易详情时读 `transaction/detail.md`。
3. 查询交易状态时读 `transaction/status-model.md`。
4. 查询资金追踪 / ID 串联 / 对账时读 `transaction/reconciliation.md`。
5. 查询系统责任边界时读 `knowledge-base/_system-boundary.md`。
6. 不默认读取 stage-review、旧 checklist、migrated-reference 或 moved notice 文件。

## 9. 来源引用

- (Ref: knowledge-base/card/card-transaction-flow.md)
- (Ref: knowledge-base/card/card-status-and-fields.md)
- (Ref: knowledge-base/transaction/history.md)
- (Ref: knowledge-base/transaction/detail.md)
- (Ref: knowledge-base/transaction/status-model.md)
- (Ref: knowledge-base/transaction/reconciliation.md)
- (Ref: knowledge-base/wallet/balance.md)
- (Ref: knowledge-base/wallet/deposit.md)
- (Ref: knowledge-base/wallet/receive.md)
- (Ref: knowledge-base/changelog/knowledge-gaps.md / ALL-GAP 总表)
- (Ref: knowledge-base/_system-boundary.md)
- (Ref: 用户确认结论 / 2026-05-02 / Wallet Transaction History 合并进 Transaction History)
