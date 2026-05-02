---
module: transaction
feature: transaction-stage-review
version: "1.1"
status: active
source_doc: IMPLEMENTATION_PLAN.md；knowledge-base/transaction/_index.md；knowledge-base/transaction/status-model.md；knowledge-base/transaction/history.md；knowledge-base/transaction/detail.md；knowledge-base/transaction/reconciliation.md；knowledge-base/card/card-transaction-flow.md；knowledge-base/wallet/stage-review.md；knowledge-base/changelog/knowledge-gaps.md；用户确认结论 2026-05-02
source_section: Transaction 阶段回扫；IMPLEMENTATION_PLAN v4.6；Wallet Transaction History 合并；Transaction Reconciliation 新增；ALL-GAP 唯一总表
last_updated: 2026-05-02
owner: 吴忆锋
depends_on:
  - transaction/_index
  - transaction/status-model
  - transaction/history
  - transaction/detail
  - transaction/reconciliation
  - card/card-transaction-flow
  - wallet/stage-review
  - changelog/knowledge-gaps
---

# Transaction 阶段回扫记录

## 1. 回扫结论

Transaction 统一层已完成基础版知识库沉淀，并已承接 Wallet Transaction History 主事实和资金追踪 / 对账边界。

本次 Stage Review 结果为：`PARTIAL PASS`。

含义：

- 已建立 Card / Wallet / Deposit 的交易状态、交易历史、交易详情和对账边界。
- `transaction/history.md` 已成为 Wallet Transaction History 主事实源。
- `transaction/reconciliation.md` 已新增，用于承接资金追踪、ID 链路、Webhook 落库和对账边界。
- 已明确 Card 与 Wallet 状态不强行合并。
- 已明确 Card Transaction ID、Wallet `transactionId`、Wallet `id`、Wallet `relatedId` 不得混写。
- Send / Swap 继续保持 `deferred`，不进入 active Transaction 统一层。
- 所有不确定项统一引用 ALL-GAP，不在 Transaction 模块维护独立 checklist / gaps。

## 2. 回扫范围

| 文件 | 状态 | 回扫结果 |
|---|---|---|
| `transaction/_index.md` | active | 已建立 Transaction 统一层边界，并补充 reconciliation 定位 |
| `transaction/status-model.md` | active | 已汇总 Card / Wallet 已确认状态来源，未强行合并状态机 |
| `transaction/history.md` | active | 已合并 Wallet Transaction History，并区分 Card / Wallet / Deposit History |
| `transaction/detail.md` | active | 已区分 Card Detail 与 Wallet Detail 字段边界 |
| `transaction/reconciliation.md` | active | 已新增资金追踪 / ID 链路 / 对账边界，只引用 ALL-GAP |

## 3. 已通过项

| 检查项 | 结果 | 说明 |
|---|---|---|
| 模块边界 | 通过 | Transaction 不重写 Card / Wallet 流程，只做统一引用层 |
| 状态来源 | 通过 | Card / Wallet 状态来源已分开记录 |
| 状态合并控制 | 通过 | 未将 Card 状态与 Wallet `state` 强行等价 |
| History 边界 | 通过 | Wallet Transaction History 已合并进 Transaction History |
| Detail 边界 | 通过 | Card Detail 与 Wallet Detail 已分开 |
| Reconciliation 边界 | 通过 | 已新增资金追踪 / 对账边界文件 |
| ID 口径隔离 | 通过 | 未将 Card `data.id`、Wallet `transactionId`、Wallet `id`、`relatedId` 写成同一字段 |
| 未上线功能隔离 | 通过 | Send / Swap 保持 deferred |
| ALL-GAP 唯一源 | 通过 | 不再维护 Transaction 模块级 gap 编号 |

## 4. 当前 ALL-GAP 引用

Transaction 阶段不维护独立 gap。相关不确定项统一引用：

| 编号 | 主题 | 影响 |
|---|---|---|
| ALL-GAP-001 | GTR 是否使用 `FIAT_DEPOSIT=6` | GTR 历史分类、筛选、统计 |
| ALL-GAP-002 | WalletConnect 是否使用 `CRYPTO_DEPOSIT=10` | WC 历史分类、筛选、统计 |
| ALL-GAP-007 | `relatedId / transactionId / id` 如何串联 GTR / WalletConnect 入金 | Deposit 入金记录追踪 |
| ALL-GAP-008 | Risk Withheld 与 Wallet `state` / 余额关系 | 状态和余额展示 |
| ALL-GAP-014 | Wallet `relatedId` 在 Card / GTR / WC 场景取值 | Wallet History 关联和对账 |
| ALL-GAP-015 | Wallet `transactionId` 与 Wallet `id` 的关系 | 交易详情查询和引用口径 |
| ALL-GAP-016 | Deposit success 与 Wallet `state=COMPLETED` 映射 | 状态模型 |
| ALL-GAP-017 | Card Transaction 与 Wallet Transaction 是否一一对应 | Card → Wallet 追踪 |
| ALL-GAP-018 | Card / Wallet 关联字段 | 对账字段组合 |
| ALL-GAP-021 | `D-REQUEST-ID` 是否承担幂等 / 去重 | 请求幂等和重试设计 |
| ALL-GAP-022 | Webhook 原始报文是否落库 | 审计、排障、补偿 |
| ALL-GAP-027 | DTC transfer 成功但 Wallet 未入账发现机制 | 资金可见性和风险发现 |
| ALL-GAP-029 | 财务 / 运营最终对账字段组合 | 对账 SOP |
| ALL-GAP-037 | ActivityType 到 AIX 前端交易类型映射 | 交易历史展示和筛选 |

## 5. 阶段判断

| 判断项 | 结论 |
|---|---|
| Transaction 模块边界 | PASS |
| Status Model | PARTIAL PASS |
| History | PARTIAL PASS |
| Detail | PARTIAL PASS |
| Reconciliation | PARTIAL PASS |
| Send / Swap deferred 隔离 | PASS |
| ID 口径隔离 | PASS |
| ALL-GAP 唯一源 | PASS |
| 资金追踪完整闭环 | DEFERRED |
| 是否允许继续后续回扫 | 允许，带 ALL-GAP 继续 |
| 是否允许把 ALL-GAP 写成事实 | 不允许 |

## 6. 后续要求

1. Common / Integration 和后续回扫阶段可引用 Transaction 已确认边界。
2. 不得将 Card 与 Wallet 状态强行合并为统一状态机。
3. 不得将 Card `data.id`、Wallet `transactionId`、Wallet `id`、Wallet `relatedId` 写成同一字段。
4. 不得把 Send / Swap 写成 active 交易类型。
5. Wallet History 新事实写入 `transaction/history.md`。
6. 资金追踪 / ID 链路 / 对账新事实写入 `transaction/reconciliation.md`。
7. 所有不确定项只进入 `knowledge-base/changelog/knowledge-gaps.md` 的 ALL-GAP 总表。

## 7. 来源引用

- (Ref: IMPLEMENTATION_PLAN.md / v4.6)
- (Ref: knowledge-base/transaction/_index.md / v1.1)
- (Ref: knowledge-base/transaction/status-model.md / v1.1)
- (Ref: knowledge-base/transaction/history.md / v1.2)
- (Ref: knowledge-base/transaction/detail.md / v1.1)
- (Ref: knowledge-base/transaction/reconciliation.md / v1.0)
- (Ref: knowledge-base/card/card-transaction-flow.md / v1.2)
- (Ref: knowledge-base/wallet/stage-review.md / v1.1)
- (Ref: knowledge-base/changelog/knowledge-gaps.md / ALL-GAP 总表)
- (Ref: 用户确认结论 / 2026-05-02 / Wallet Transaction History 合并进 Transaction History)
