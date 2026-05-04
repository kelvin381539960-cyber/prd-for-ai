---
module: wallet
feature: send
version: "1.0"
status: deferred
source_doc: IMPLEMENTATION_PLAN.md；knowledge-base/wallet/_index.md；knowledge-base/wallet/balance.md；knowledge-base/transaction/history.md；用户确认结论 2026-05-01
source_section: Wallet Send / Withdraw 占位；compliance launch decision；Wallet _index v2.1；Transaction History
last_updated: 2026-05-01
owner: 吴忆锋
depends_on:
  - wallet/_index
  - wallet/balance
  - transaction/history
---

# Wallet Send / Withdraw 占位 钱包发送 / 提现

## 1. 当前状态

Wallet Send 当前状态为 `deferred`。

因合规原因，Send 未上线，不进入当前 active 功能归档。

本文仅作为占位，用于明确：旧 Send / Withdraw 方案不得写入当前正式知识库事实层。后续如合规方案重做并重新上线，需要基于新 PRD、新接口文档和已确认结论重新转译。

## 2. 处理原则

| 原则 | 说明 |
|---|---|
| 不归档为 active 功能 | Send 未上线，不能作为当前生效能力 |
| 不沉淀旧流程 | 不把旧 Send / Withdraw 流程、字段、状态、风控规则写成事实 |
| 不补接口字段 | 即使接口文档存在相关能力，也不代表 AIX 当前上线 |
| 不影响 Balance / Transaction History | Wallet 基础余额和交易记录能力继续保留 |
| 新方案另起 | Send 合规方案确认后再重新转译 |

## 3. 与 Wallet 其他模块的关系

| 模块 | 当前处理 |
|---|---|
| `wallet/balance.md` | 继续保留，作为钱包余额基础能力 |
| `transaction/history.md` | 继续保留，作为钱包交易记录与状态基础事实源；Wallet 目录不再维护交易历史主事实 |
| `wallet/receive.md` | 继续保持独立核验，不默认等同 Deposit |
| `wallet/deposit.md` | active，包含 GTR / Exchange 地址充值与 WalletConnect 充值；不受 Send / Withdraw deferred 状态影响 |
| `wallet/swap.md` | deferred，因合规原因未上线且需重做 |
| Wallet Gate Review | 需检查 Send / Withdraw 与 Swap 是否仍为 deferred；Deposit 当前为 active，不应被 Send 状态传导 |

## 4. 已确认基础事实但不构成 Send 上线事实

| 项目 | 结论 | 来源 | 备注 |
|---|---|---|---|
| Wallet 交易 ID | Wallet 交易记录 / 详情出参均包含 `id`，Long，交易 id | DTC Wallet OpenAPI；用户确认 2026-05-01 | 通用 Wallet 交易事实 |
| Wallet 详情入参 | 单笔 Wallet 交易详情入参为 `transactionId`，Unique transaction ID from DTC | DTC Wallet OpenAPI；用户确认 2026-05-01 | 通用 Wallet 详情事实 |
| Wallet 交易状态 | `state` 枚举为 `PENDING`、`PROCESSING`、`AUTHORIZED`、`COMPLETED`、`REJECTED`、`CLOSED` | DTC Wallet OpenAPI；用户确认 2026-05-01 | 通用 Wallet 状态事实 |
| Search Balance History | 可查询 Wallet 交易 / 余额历史 | DTC Wallet OpenAPI / 4.2.4 | 通用 Wallet 历史能力 |

## 5. 不写入事实的内容

以下内容当前不得写成事实：

1. Send 已上线。
2. Withdraw 已上线。
3. Send / Withdraw 入口、页面、用户路径已生效。
4. Send / Withdraw 支持币种、链、地址字段、memo/tag 字段。
5. Send / Withdraw 手续费规则。
6. Send / Withdraw 限额规则。
7. Send / Withdraw 风控拦截规则。
8. Send / Withdraw 是否需要 Travel Rule / Declare。
9. Send / Withdraw 是否需要白名单。
10. Send / Withdraw 状态机与失败原因。
11. Send / Withdraw 成功 / 失败通知文案。
12. 旧 Send / Withdraw 方案可直接用于新方案。

## 6. 未来重做待确认清单

| 待确认项 | 新方案需要提供的来源 |
|---|---|
| 是否上线 Send / Withdraw | 新 PRD / 合规确认 |
| 支持国家 / 地区 | 新 PRD / 合规确认 |
| 支持币种 / 链 | 新 PRD / DTC Wallet OpenAPI / 合规确认 |
| 地址输入 / 地址簿 / 白名单规则 | 新 PRD / 合规确认 |
| memo / tag / network 字段 | 新接口文档 |
| 手续费与最小提现金额 | 新 PRD / 接口文档 |
| 限额规则 | 新 PRD / 合规 / 风控文档 |
| Travel Rule / Declare 规则 | 合规 PRD |
| 风控拦截 / on-hold 规则 | 风控 / 合规 / DTC 文档 |
| 状态机 | 新 PRD / DTC 状态枚举 |
| 用户通知规则 | Notification PRD 更新版 |
| 客服 / 人工处理边界 | 运营 / 后台 PRD |

## 7. 来源引用

- (Ref: 用户确认结论 / 2026-05-01 / Send 因合规原因未上线)
- (Ref: knowledge-base/wallet/_index.md / Wallet 模块边界)
- (Ref: knowledge-base/wallet/balance.md / Wallet Balance v1.0)
- (Ref: knowledge-base/transaction/history.md / Wallet Transaction History 主事实源)
