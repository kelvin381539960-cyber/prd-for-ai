---
module: wallet
feature: deposit
version: "1.1"
status: deferred
source_doc: DTC Wallet OpenAPI Documentation；knowledge-base/wallet/_index.md；knowledge-base/wallet/balance.md；knowledge-base/wallet/transaction-history.md；knowledge-base/changelog/knowledge-gaps.md；用户确认结论 2026-05-01
source_section: Wallet Deposit / Receive / Search Balance History；Wallet _index v1.0；Wallet Balance v1.0；Wallet Transaction History v1.0；compliance redesign decision
last_updated: 2026-05-01
owner: 吴忆锋
depends_on:
  - wallet/_index
  - wallet/balance
  - wallet/transaction-history
  - changelog/knowledge-gaps
---

# Wallet Deposit 钱包充值

## 1. 当前状态

Wallet Deposit 当前状态为 `deferred`。

因合规原因，Deposit 未上线且需要重做，因此本文不作为当前已上线功能的正式知识库事实源。

本文仅保留以下用途：

1. 标记 Deposit 不进入当前 active 功能归档。
2. 记录已知边界，避免后续误把旧方案写成事实。
3. 为未来 Deposit 新方案重做时保留待确认清单。

## 2. 处理原则

| 原则 | 说明 |
|---|---|
| 不归档为 active 功能 | Deposit 未上线，不能作为当前功能事实源 |
| 不沉淀旧流程 | 不把旧 Deposit 流程、字段、状态、风控规则写成事实 |
| 不补接口字段 | 即使 DTC Wallet OpenAPI 中存在相关能力，也不代表 AIX 当前上线 |
| 不影响 Receive / Send / Balance | 可继续推进已上线或基础能力 |
| 新方案另起 | Deposit 合规重做后，应基于新 PRD / 新接口文档重新转译 |

## 3. 与 Wallet 其他模块的关系

| 模块 | 当前处理 |
|---|---|
| `wallet/balance.md` | 继续保留，作为钱包余额基础能力 |
| `wallet/transaction-history.md` | 继续保留，作为钱包交易记录与状态基础事实源 |
| `wallet/receive.md` | 是否继续需看 Receive 是否独立上线；不得默认等同于 Deposit |
| `wallet/send.md` | 可继续推进，前提是来源明确 |
| `wallet/swap.md` | 与 Deposit 相同，因合规原因未上线且需重做，不进入 active 功能归档 |
| `wallet/stage-review.md` | Wallet Gate Review 时需检查 Deposit / Swap 是否仍为 deferred |

## 4. 已确认基础事实但不构成 Deposit 上线事实

以下字段仍是 Wallet 通用基础事实，但不能因此推导 Deposit 已上线：

| 项目 | 结论 | 来源 | 备注 |
|---|---|---|---|
| Wallet 交易 ID | Wallet 交易记录 / 详情出参均包含 `id`，Long，交易 id | DTC Wallet OpenAPI；用户确认 2026-05-01 | 通用 Wallet 交易事实 |
| Wallet 详情入参 | 单笔 Wallet 交易详情入参为 `transactionId`，Unique transaction ID from DTC | DTC Wallet OpenAPI；用户确认 2026-05-01 | 通用 Wallet 详情事实 |
| Wallet 交易状态 | `state` 枚举为 `PENDING`、`PROCESSING`、`AUTHORIZED`、`COMPLETED`、`REJECTED`、`CLOSED` | DTC Wallet OpenAPI；用户确认 2026-05-01 | 通用 Wallet 状态事实 |
| Search Balance History | 可查询 Wallet 交易 / 余额历史 | DTC Wallet OpenAPI / 4.2.4 | 通用 Wallet 历史能力 |

## 5. 不写入事实的内容

以下内容当前不得写成事实：

1. Deposit 已上线。
2. Deposit 入口、页面、用户路径已生效。
3. Deposit 支持的币种、链、地址字段、memo/tag 字段。
4. Deposit 充值成功 / 失败状态机。
5. Deposit 是否需要白名单。
6. Deposit 是否需要 Declare / Travel Rule。
7. Deposit 风控拦截规则。
8. Deposit 成功 / 失败通知文案。
9. Deposit 成功一定会生成 Wallet balance 可用余额。
10. Deposit 旧方案可直接用于新方案。

## 6. 未来重做待确认清单

| 待确认项 | 新方案需要提供的来源 |
|---|---|
| 是否上线 Crypto Deposit | 新 PRD / 合规确认 |
| 是否上线 Fiat Deposit | 新 PRD / 合规确认 |
| 支持国家 / 地区 | 新 PRD / 合规确认 |
| 支持币种 / 链 | 新 PRD / DTC Wallet OpenAPI / 合规确认 |
| 充值地址生成 / 查询方式 | 新接口文档 |
| memo / tag / network 字段 | 新接口文档 |
| 最小充值金额与确认数 | 新 PRD / 接口文档 |
| 充值状态机 | 新 PRD / DTC 状态枚举 |
| on-hold / risk rejected 规则 | 风控 / 合规 / DTC 文档 |
| Declare / Travel Rule 规则 | 合规 PRD |
| 用户通知规则 | Notification PRD 更新版 |
| 客服 / 人工处理边界 | 运营 / 后台 PRD |

## 7. 来源引用

- (Ref: 用户确认结论 / 2026-05-01 / Deposit 因合规原因未上线且需重做)
- (Ref: DTC Wallet OpenAPI Documentation / Wallet 通用交易记录与状态)
- (Ref: knowledge-base/wallet/_index.md / Wallet 模块边界)
- (Ref: knowledge-base/wallet/balance.md / Wallet Balance v1.0)
- (Ref: knowledge-base/wallet/transaction-history.md / Wallet Transaction History v1.0)
