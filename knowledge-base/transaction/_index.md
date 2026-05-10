---
module: transaction
feature: transaction-index
version: "3.1"
status: active
source_doc: archive/legacy-prd/app/transaction-history/README.md；archive/legacy-prd/card/transaction/README.md；archive/legacy-prd/wallet/deposit-send-swap/README.md
source_section: Transaction & History / 状态及类型处理、全量交易、Card History、Transaction Details；Card Transaction；Wallet Deposit/Send/Swap
last_updated: 2026-05-09
owner: 吴忆锋
depends_on:
  - card/transaction
  - transaction/status-model
  - transaction/history
  - transaction/detail
  - transaction/reconciliation
  - wallet/assets
  - wallet/deposit
  - changelog/knowledge-gaps
  - _system-boundary
---

# Transaction 模块索引

> Source alignment note: 本模块已按新转换的 `archive/legacy-prd/app/transaction-history/README.md`、`archive/legacy-prd/card/transaction/README.md`、`archive/legacy-prd/wallet/deposit-send-swap/README.md` 做双向覆盖校验。补齐的关键 Evidence→KB 缺口包括：全量交易去搜索、REVERSAL 按 REFUND 展示、Deposit 详情隐藏 Gas fee、Exchange rate 显示规则、接口异常统一文案、INCREMENTAL_AUTH / CARD_FEE / TRANSFER_IN / TRANSFER_OUT 等类型口径。


## 1. 模块定位

Transaction 统一层用于沉淀 AIX 中跨 Card / Wallet / Deposit 的交易状态、交易历史、交易详情、资金追踪和对账边界。

本模块不是重新定义 Card 或 Wallet 的业务流程，而是在已确认事实基础上建立统一引用关系：

- Card 交易展示引用 Card Transaction 事实源。
- Wallet 资产页最近交易摘要引用 `wallet/assets.md`，但全量 Wallet History 主事实源为 `transaction/history.md`。
- Wallet 交易详情主事实源为 `transaction/detail.md`。
- Card / Wallet / Deposit 的资金追踪与对账边界由 `transaction/reconciliation.md` 承接。
- Card Transaction、Wallet Assets、Wallet Deposit 中的未确认 gaps 不得在 Transaction 阶段补写为事实，统一引用 ALL-GAP。

---

## 2. 当前文件

| 文件 | 状态 | 目标 | 备注 |
|---|---|---|---|
| `transaction/_index.md` | active | 建立 Transaction 统一层边界、状态来源和引用规则 | 当前文件 |
| `transaction/status-model.md` | active | 汇总 Card / Wallet 已确认状态，不脑补完整状态机 | Wallet `state` 主引用源 |
| `transaction/history.md` | active | 汇总 Card History / Wallet Transaction History / Deposit History | Wallet History 主事实源 |
| `transaction/detail.md` | active | 汇总 Card / Wallet 交易详情字段边界 | 保持字段隔离 |
| `transaction/reconciliation.md` | active | 资金追踪 / ID 链路 / 对账边界 | 对应 ALL-GAP P0 |

---

## 3. 与 Wallet 的关系

| Wallet 主题 | 主事实源 | Transaction 处理 | 不得补写 |
|---|---|---|---|
| My Assets 最近交易摘要 | `wallet/assets.md` | 只引用其摘要数据源和展示边界 | 不把它当成全量交易历史 |
| Wallet 全量交易历史 | `transaction/history.md` | 维护 Search Balance History、Wallet History、ActivityType 边界 | 不套用 Card History 的筛选 / 时间范围 |
| Wallet 交易详情 | `transaction/detail.md` | 维护 Wallet Transaction Detail 字段边界 | 不套用 Card Detail 字段 |
| Wallet Deposit 结果进入历史 | `wallet/deposit.md` + `transaction/history.md` | 记录 success、Risk Withheld、ActivityType 等引用边界 | 不把 Deposit success 等同 Wallet `COMPLETED` |
| Wallet 资金追踪 / 对账 | `transaction/reconciliation.md` | 维护 ID 串联、资金追踪、对账缺口 | 不在 Wallet 目录内补对账结论 |

---

## 4. 状态来源边界

| 来源模块 | 可引用内容 | 不可补写内容 |
|---|---|---|
| Card Transaction | Card 状态、Card History、Card Transaction Details、refund / reversal / deposit 归集触发边界 | 不补写 AIX 内部交易 ID、归集请求 ID、Wallet relatedId、对账字段 |
| Wallet Assets | My Assets 最近交易摘要、Total Asset、稳定币资产展示边界 | 不补写 Search Balance History 完整字段，不维护 Wallet History 正文 |
| Wallet Deposit | Deposit active，包含 GTR 与 WalletConnect | 不混写 GTR 与 WalletConnect 的字段、状态、风控规则 |
| Transaction History | Wallet `id`、`transactionId`、`state`、Search Balance History 基础能力 | 不补写 ActivityType 到产品路径映射 |
| Transaction Detail | Card / Wallet 详情字段边界 | 不合并 Card / Wallet 字段 |
| Transaction Reconciliation | 资金追踪、ID 链路、对账边界 | 不补未确认关联规则 |

---

## 5. 已确认状态集合

### 5.1 Wallet state

Wallet 当前已确认交易状态字段为 `state`，枚举为：

| 枚举 | 当前处理 |
|---|---|
| `PENDING` | 可作为 Wallet 交易状态枚举引用；进入 / 退出条件待 ALL-GAP 收敛 |
| `PROCESSING` | 可作为 Wallet 交易状态枚举引用；进入 / 退出条件待 ALL-GAP 收敛 |
| `AUTHORIZED` | 可作为 Wallet 交易状态枚举引用；进入 / 退出条件待 ALL-GAP 收敛 |
| `COMPLETED` | 可作为 Wallet 交易状态枚举引用；不直接等同 Deposit success |
| `REJECTED` | 可作为 Wallet 交易状态枚举引用；不直接等同 Risk Withheld |
| `CLOSED` | 可作为 Wallet 交易状态枚举引用；关闭条件待补 |

### 5.2 Card Transaction 状态

Card Transaction 相关状态、类型、交易详情字段应优先引用 `knowledge-base/card/transaction.md`。

Transaction 阶段不得将 Card 状态与 Wallet 状态强行合并为同一枚举。

---

## 6. 交易历史边界

| 历史类型 | 来源 | 当前处理 |
|---|---|---|
| Card History | Card Transaction PRD / DTC Card Issuing | 由 `transaction/history.md` 汇总 |
| Card Transaction Details | Card Transaction PRD / DTC Card Issuing | 由 `transaction/detail.md` 汇总 |
| My Assets Recent transaction | AIX Wallet Asset PRD / crypto-txn + otc | 由 `wallet/assets.md` 维护页面摘要规则 |
| Wallet Transaction History | DTC Wallet OpenAPI / Search Balance History | 由 `transaction/history.md` 维护主事实 |
| Wallet Transaction Detail | DTC Wallet OpenAPI | 由 `transaction/detail.md` 汇总 |
| Deposit History | Wallet Deposit / DTC Wallet OpenAPI | 由 `transaction/history.md` 汇总边界 |
| Reconciliation | Card / Wallet / DTC / ALL-GAP | 由 `transaction/reconciliation.md` 汇总边界 |

---

## 7. 不写入事实的内容

以下内容当前不得写成事实：

1. Card 与 Wallet 使用同一套交易状态枚举。
2. Wallet `transactionId` 等同于 Card `data.id`。
3. Wallet `relatedId` 等同于 Card `data.id` 或 AIX 归集请求 ID。
4. My Assets Recent transaction 使用 Search Balance History 作为主数据源。
5. GTR 与 WalletConnect Deposit 使用同一套状态 / 风控 / 字段规则。
6. Receive 已确认独立上线。
7. Wallet Deposit / Receive 完整状态机已经闭环。
8. Card Transaction Flow 的资金追踪链路已经完整闭环。
9. Transaction 模块单独维护 checklist / gap 表。

---

## 8. ALL-GAP 引用原则

Transaction 模块不维护独立 checklist。以下问题统一引用 `knowledge-base/changelog/knowledge-gaps.md`：

| 主题 | ALL-GAP |
|---|---|
| GTR / WalletConnect 与 ActivityType 映射 | ALL-GAP-001、ALL-GAP-002 |
| Wallet id / transactionId / relatedId 关系 | ALL-GAP-007、ALL-GAP-014、ALL-GAP-015 |
| Deposit success / Risk Withheld 与 Wallet state | ALL-GAP-008、ALL-GAP-016 |
| Card ↔ Wallet 资金追踪 | ALL-GAP-017 ~ ALL-GAP-029 |
| ActivityType 到 AIX 前端交易类型映射 | ALL-GAP-037 |
| Wallet Transaction Detail 完整字段 | ALL-GAP-048 |
| Search Balance History 完整字段 | ALL-GAP-058 |

---

## 9. 使用规则

1. 查询钱包资产页最近交易摘要时读 `wallet/assets.md`。
2. 查询全量交易历史时读 `transaction/history.md`。
3. 查询交易详情时读 `transaction/detail.md`。
4. 查询交易状态时读 `transaction/status-model.md`。
5. 查询资金追踪 / ID 串联 / 对账时读 `transaction/reconciliation.md`。
6. 查询系统责任边界时读 `knowledge-base/_system-boundary.md`。
7. 不默认读取 stage-review、旧 checklist、migrated-reference 或 moved notice 文件。

---

## Source alignment additions

| 证据规则 | 已落入文件 | 说明 |
|---|---|---|
| 全量交易和卡交易去掉搜索，后续再迭代 | `transaction/history.md` | 不再把 Search 作为已确认入口 |
| 全量交易聚合钱包加密币交易、OTC 兑换记录、卡交易记录 | `transaction/history.md` | 后端分别调用 crypto、otc、card 交易接口后聚合 |
| 卡交易 REVERSAL / type=19 作为退款展示 | `transaction/history.md`、`transaction/status-model.md` | 前端与 REFUND 一样显示 refund-商户名 |
| Deposit 交易详情隐藏 Gas fee item | `transaction/detail.md` | 4月14日更正，Gas fee 不作为当前展示项 |
| Card detail Exchange rate 显示小数点后 6 位并向上取整 | `transaction/detail.md` | Swap detail 的 exchange rate 后端给什么显示什么，不做位数处理 |
| DTC / 服务端 / 网络异常统一文案 | `transaction/history.md` | Data error / No internet connection |

## 10. 来源引用

- (Ref: knowledge-base/card/transaction.md)
- (Ref: knowledge-base/transaction/history.md)
- (Ref: knowledge-base/transaction/detail.md)
- (Ref: knowledge-base/transaction/status-model.md)
- (Ref: knowledge-base/transaction/reconciliation.md)
- (Ref: knowledge-base/wallet/assets.md)
- (Ref: knowledge-base/wallet/deposit.md)
- (Ref: knowledge-base/changelog/knowledge-gaps.md / ALL-GAP 总表)
- (Ref: knowledge-base/_system-boundary.md)
- (Ref: 用户确认结论 / 2026-05-02 / Wallet Transaction History 合并进 Transaction History)
