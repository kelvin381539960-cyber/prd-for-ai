---
module: wallet
feature: wallet-stage-review
version: "1.0"
status: active
source_doc: IMPLEMENTATION_PLAN.md；knowledge-base/wallet/_index.md；knowledge-base/wallet/transaction-history.md；knowledge-base/wallet/balance.md；knowledge-base/wallet/deposit.md；knowledge-base/wallet/receive.md；knowledge-base/wallet/send.md；knowledge-base/wallet/kyc.md；knowledge-base/changelog/knowledge-gaps.md
source_section: Wallet 阶段回扫；IMPLEMENTATION_PLAN v3.8；Wallet active/deferred boundaries
last_updated: 2026-05-01
owner: 吴忆锋
depends_on:
  - wallet/_index
  - wallet/transaction-history
  - wallet/balance
  - wallet/deposit
  - wallet/receive
  - wallet/send
  - wallet/kyc
  - changelog/knowledge-gaps
---

# Wallet 阶段回扫记录

## 1. 回扫结论

Wallet 阶段已完成基础版知识库沉淀，但未达到完整 `PASS`。

本次 Stage Review 结果为：`PARTIAL PASS`。

含义：

- Wallet 基础边界、交易记录、余额、Deposit、Receive、KYC 已建立基础文件。
- Deposit 已恢复为 active，范围包含 GTR 和 WalletConnect，但两条子路径的完整字段、状态、风控、通知和异常边界仍待补。
- Send 与 Swap 因合规原因未上线或需重做，保持 `deferred`，不作为 active 功能事实源。
- Wallet 可进入后续 Transaction 统一层，但不得把待补项写成事实。

## 2. 回扫范围

| 文件 | 状态 | 回扫结果 |
|---|---|---|
| `wallet/_index.md` | active | Wallet 模块边界已建立；Deposit active；Send / Swap deferred |
| `wallet/transaction-history.md` | active / 基础版 | Wallet `id`、`transactionId`、`state` 基础事实已沉淀；完整字段待补 |
| `wallet/balance.md` | active / 基础版 | Balance 边界已建立；余额接口字段待补 |
| `wallet/deposit.md` | active / 基础版 | Deposit 包含 GTR 和 WalletConnect；子路径细节待补 |
| `wallet/receive.md` | active / 基础版 | Receive 基础占位已建立；与 Deposit 子路径关系待确认 |
| `wallet/send.md` | deferred | 因合规原因未上线，不作为 active 功能事实源 |
| `wallet/swap.md` | deferred | 未创建 active 正文；因合规原因未上线且需重做 |
| `wallet/kyc.md` | active / 基础版 | Wallet KYC / 开户前置边界已建立；完整流程和接口待补 |

## 3. 已通过项

| 检查项 | 结果 | 说明 |
|---|---|---|
| 模块边界 | 通过 | Wallet 与 Card、Transaction、Send / Swap deferred 边界已明确 |
| 功能上线状态 | 通过 | Deposit active；Send / Swap deferred；未把未上线功能写成 active |
| Wallet 基础字段 | 部分通过 | Wallet `id`、`transactionId`、`state` 已确认 |
| Wallet 状态枚举 | 通过 | `PENDING` / `PROCESSING` / `AUTHORIZED` / `COMPLETED` / `REJECTED` / `CLOSED` 已沉淀 |
| Card deferred gaps 隔离 | 通过 | 未把 Card 资金追踪遗留项写成 Wallet 事实 |
| Deposit 范围 | 部分通过 | 已确认包含 GTR / WalletConnect；细节待补 |
| KYC 边界 | 部分通过 | 已明确不默认等同 Card KYC / AAI KYC；完整规则待补 |
| 无来源补写 | 通过 | 未把缺失字段、状态、文案、流程写成事实 |

## 4. 当前待补 / deferred 问题

### 4.1 Wallet 通用待补

| 编号 | 问题 | 影响 |
|---|---|---|
| WALLET-GAP-001 | Wallet 当前余额查询接口路径、请求字段、响应字段未完整抽取 | Balance 事实源不完整 |
| WALLET-GAP-002 | 可用余额 / 冻结余额 / 总余额字段未确认 | 余额展示与对账口径不完整 |
| WALLET-GAP-003 | Wallet 交易记录完整请求 / 响应字段表未补齐 | Transaction History 事实源不完整 |
| WALLET-GAP-004 | `activityType` 枚举未补齐 | 交易分类与展示口径不完整 |
| WALLET-GAP-005 | Wallet 状态与前端展示文案映射未确认 | 用户展示不完整 |

### 4.2 Deposit 待补

| 编号 | 问题 | 影响 |
|---|---|---|
| WALLET-DEPOSIT-001 | GTR Deposit 完整流程、接口字段、状态未补齐 | GTR 入金事实源不完整 |
| WALLET-DEPOSIT-002 | WalletConnect Deposit 完整流程、接口字段、状态未补齐 | WalletConnect 入金事实源不完整 |
| WALLET-DEPOSIT-003 | GTR / WalletConnect 是否需要 Declare / Travel Rule 未确认 | 合规边界不完整 |
| WALLET-DEPOSIT-004 | GTR / WalletConnect 是否需要白名单未确认 | 入金前置条件不完整 |
| WALLET-DEPOSIT-005 | on-hold / risk rejected 规则未确认 | 风控异常分支不完整 |
| WALLET-DEPOSIT-006 | Deposit 通知规则未补齐 | 用户通知边界不完整 |
| WALLET-DEPOSIT-007 | GTR 与 WalletConnect 是否共用状态 / 字段 / 风控规则未确认 | 子路径边界不完整 |

### 4.3 Receive 待补

| 编号 | 问题 | 影响 |
|---|---|---|
| WALLET-RECEIVE-001 | Receive 是否独立于 Deposit 上线未确认 | Receive active 状态仍需核验 |
| WALLET-RECEIVE-002 | Receive 地址、链、币种、memo/tag、二维码字段未补齐 | 收款地址事实源不完整 |
| WALLET-RECEIVE-003 | Receive 与 GTR / WalletConnect 的关系未确认 | 可能与 Deposit 子路径重叠 |
| WALLET-RECEIVE-004 | Receive 状态与 Wallet `state` 的映射未确认 | 状态闭环不完整 |

### 4.4 KYC 待补

| 编号 | 问题 | 影响 |
|---|---|---|
| WALLET-KYC-001 | Wallet 是否有独立开户 / KYC 流程未确认 | Wallet 准入规则不完整 |
| WALLET-KYC-002 | Wallet KYC 与 Account / Security / Card KYC 的关系未确认 | 跨模块依赖不完整 |
| WALLET-KYC-003 | Wallet KYC 是否为 GTR / WalletConnect Deposit 前置条件未确认 | 入金准入不完整 |
| WALLET-KYC-004 | Wallet 开户接口路径、请求字段、响应字段未补齐 | 接口事实源不完整 |
| WALLET-KYC-005 | KYC 失败、重试、重新提交、人工处理规则未补齐 | 失败分支不完整 |

### 4.5 Deferred 功能

| 功能 | 当前状态 | 处理 |
|---|---|---|
| Send / Withdraw | deferred | 因合规原因未上线，不作为 active 功能事实源；新方案确认后再转译 |
| Swap | deferred | 因合规原因未上线且需重做；新方案确认后再转译 |

## 5. 阶段判断

| 判断项 | 结论 |
|---|---|
| Wallet 模块边界 | PASS |
| Wallet 交易基础字段 | PARTIAL PASS |
| Wallet Balance | PARTIAL PASS |
| Wallet Deposit | PARTIAL PASS |
| Wallet Receive | PARTIAL PASS |
| Wallet KYC | PARTIAL PASS |
| Send / Swap 上线状态处理 | PASS |
| 是否允许进入 Transaction 统一层 | 允许，带 deferred / 待补项继续 |
| 是否允许把待补项写成事实 | 不允许 |

## 6. 后续要求

1. 进入 Transaction 统一层前，可以引用 Wallet 已确认基础事实：`id`、`transactionId`、`state`、Search Balance History 基础能力、Deposit 包含 GTR / WalletConnect。
2. 不得引用以下内容为事实：GTR / WalletConnect 完整状态机、Declare / Travel Rule、白名单、风控、通知、Receive 独立上线、Wallet KYC 独立流程。
3. Send / Swap 必须继续保持 `deferred`，新方案确认后才能转译。
4. 后续若拿到 Wallet PRD / DTC Wallet OpenAPI 完整字段，应优先回填：`transaction-history.md`、`balance.md`、`deposit.md`、`receive.md`、`kyc.md`。
5. Transaction 阶段应把 Wallet `state` 作为 Wallet 交易状态基础来源，但不得把 Deposit / Receive 子状态脑补为完整状态机。

## 7. 来源引用

- (Ref: IMPLEMENTATION_PLAN.md / v3.8 / Wallet 阶段)
- (Ref: knowledge-base/wallet/_index.md / v1.3)
- (Ref: knowledge-base/wallet/transaction-history.md / v1.0)
- (Ref: knowledge-base/wallet/balance.md / v1.0)
- (Ref: knowledge-base/wallet/deposit.md / v1.2)
- (Ref: knowledge-base/wallet/receive.md / v1.0)
- (Ref: knowledge-base/wallet/send.md / v1.0)
- (Ref: knowledge-base/wallet/kyc.md / v1.0)
- (Ref: knowledge-base/changelog/knowledge-gaps.md / Card Transaction Flow deferred gaps)
