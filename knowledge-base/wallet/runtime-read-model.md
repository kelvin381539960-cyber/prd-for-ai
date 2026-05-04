---
module: wallet
feature: runtime-read-model
version: "1.0"
status: active
source_doc: knowledge-base/wallet/_index.md；knowledge-base/wallet/balance.md；knowledge-base/wallet/deposit.md；knowledge-base/wallet/receive.md；knowledge-base/wallet/send.md；knowledge-base/transaction/history.md；knowledge-base/transaction/reconciliation.md；knowledge-base/kyc/account-opening.md；knowledge-base/changelog/knowledge-gaps.md；knowledge-base/changelog/decision-log/2026-05-01-send-compliance.md；knowledge-base/changelog/decision-log/2026-05-02-deposit-active.md；knowledge-base/changelog/decision-log/2026-05-02-receive-deferred.md
source_section: Wallet runtime read order；module boundary；decision logs；ALL-GAP 总表
last_updated: 2026-05-04
owner: 吴忆锋
depends_on:
  - wallet/_index
  - wallet/balance
  - wallet/deposit
  - wallet/receive
  - wallet/send
  - transaction/history
  - transaction/reconciliation
  - kyc/account-opening
  - changelog/knowledge-gaps
  - changelog/decision-log/2026-05-01-send-compliance
  - changelog/decision-log/2026-05-02-deposit-active
  - changelog/decision-log/2026-05-02-receive-deferred
---

# Wallet Runtime Read Model

## 1. 目标

本文件定义 Wallet 知识库在 Agent / AI / PM 使用时的读取顺序、优先级、fallback 规则和禁止读取规则。

Runtime Read Model 不新增业务事实，只规定读取策略。业务事实仍以对应模块文件和 ALL-GAP 为准。

## 2. 总读取原则

1. 查询 Wallet 能力时，先读 `wallet/_index.md`，再按场景读取对应主事实文件。
2. active 文件优先于 deferred / placeholder 文件。
3. 已确认事实优先于 ALL-GAP；未确认内容只能引用 ALL-GAP，不得补写为事实。
4. Wallet 目录不承接 Account Opening / KYC 主事实，也不承接统一交易历史主事实。
5. 旧 PRD、旧流程、历史 checklist、moved notice、stage-review，不作为 runtime 默认读取源。

## 3. 场景读取顺序

| 用户问题 / 场景 | 第一读取 | 第二读取 | Fallback / 边界 |
|---|---|---|---|
| Wallet 模块有哪些能力 | `wallet/_index.md` | 本文件 | 不直接读取历史 PRD |
| 钱包余额 / 币种 / 当前余额查询 | `wallet/balance.md` | `transaction/history.md` | 字段缺口见 ALL-GAP-055 / 056 / 057 / 058 |
| GTR / Exchange 地址充值 | `wallet/deposit.md` | `wallet/balance.md`、`transaction/history.md` | GTR 与 ActivityType、relatedId 映射见 ALL-GAP-001 / 007 / 014 |
| WalletConnect / Self-custodial Wallet 充值 | `wallet/deposit.md` | `common/walletconnect.md`、`transaction/history.md` | WC 与 ActivityType、relatedId、payment_info 映射见 ALL-GAP-002 / 007 / 012 / 014 |
| Deposit 状态 / 结果页 / 异常 | `wallet/deposit.md` | `transaction/status-model.md`、`common/errors.md` | DTC numeric state、Wallet state、用户展示状态不得混用；映射缺口见 ALL-GAP-062 |
| Receive / 收款地址 | `wallet/deposit.md` | `wallet/receive.md` | `wallet/receive.md` 当前为 deferred placeholder，只作核验清单，不作 active 事实源 |
| Send / Withdraw | `wallet/send.md` | `transaction/history.md` | 当前 deferred；不得读取旧 Send / Withdraw 流程作为 active 事实 |
| Swap | Wallet 索引判断 deferred | 需要新 PRD / 新接口文档 | 当前不在 Wallet active 事实层 |
| Wallet Transaction History | `transaction/history.md` | `transaction/status-model.md` | Wallet 目录不维护交易历史主事实 |
| Wallet 对账 / 资金追踪 | `transaction/reconciliation.md` | `transaction/history.md`、`wallet/balance.md` | Card / GTR / WC 关联字段见 ALL-GAP-014 / 018 / 029 |
| Wallet 开户 / KYC / Sub Account / D-SUB-ACCOUNT-ID | `kyc/account-opening.md` | `_system-boundary.md` | Wallet 目录不维护 KYC 主事实 |
| Wallet 通知 | `common/notification.md` | `wallet/deposit.md` | Wallet 文件不得自行补通知文案；覆盖缺口见 ALL-GAP-010 / 062 |

## 4. 文件优先级

| 优先级 | 文件类型 | 规则 |
|---:|---|---|
| 1 | 当前 active 主事实文件 | `_index.md`、`balance.md`、`deposit.md` |
| 2 | 跨模块主事实文件 | `transaction/history.md`、`transaction/status-model.md`、`kyc/account-opening.md`、`transaction/reconciliation.md` |
| 3 | 公共能力文件 | `common/walletconnect.md`、`common/notification.md`、`common/errors.md`、`common/dtc.md` |
| 4 | ALL-GAP 总表 | 仅用于引用未确认项，不得当成已确认事实 |
| 5 | decision-log | 用于解释状态、边界和迁移决策 |
| 6 | deferred / placeholder 文件 | `receive.md`、`send.md` 等，仅用于说明不可用或待确认范围 |
| 7 | 历史 PRD / migrated reference | 非 runtime 默认读取源，只能在重新转译或审计时使用 |

## 5. 禁止读取 / 禁止推断规则

以下规则用于防止 Agent 误读：

1. 不得将 `wallet/receive.md` 作为当前 active Receive 功能事实源。
2. 不得将旧 Send / Withdraw PRD 内容作为当前 active Send / Withdraw 事实。
3. 不得把 Deposit 的 GTR 路径和 WalletConnect 路径默认合并。
4. 不得把 DTC Available Currency 直接等同于 AIX 前端展示币种。
5. 不得把 DTC numeric state 直接等同 Wallet `state` 或用户展示文案。
6. 不得把 `FIAT_DEPOSIT=6` 必然等同 GTR。
7. 不得把 `CRYPTO_DEPOSIT=10` 必然等同 WalletConnect。
8. 不得把 Deposit success 必然等同 Wallet `COMPLETED` 或余额立即可用。
9. 不得把 Risk Withheld 直接等同 Wallet `REJECTED / PENDING / PROCESSING`。
10. 不得在 Wallet 目录补写 KYC、Transaction History、Notification、Reconciliation 的主事实。

## 6. 推荐回答策略

Agent 在回答 Wallet 问题时，应按以下方式组织结论：

1. 先说明当前可确认事实。
2. 再说明当前状态：active / deferred / placeholder。
3. 对未确认项引用 ALL-GAP 编号。
4. 对跨模块内容给出主事实源路径。
5. 不用历史 PRD 直接覆盖当前 active 事实。

## 7. 场景示例

### 7.1 用户问：钱包余额怎么查？

读取顺序：

1. `wallet/_index.md`
2. `wallet/balance.md`
3. 如涉及交易历史，再读 `transaction/history.md`

回答边界：

- 可确认 Get Balance / Get Wallet Account Balance 存在。
- 可确认 Search Balance History 存在。
- 可用余额 / 冻结余额字段、展示排序、失败处理仍引用 ALL-GAP。

### 7.2 用户问：如何充值？

读取顺序：

1. `wallet/_index.md`
2. `wallet/deposit.md`
3. 如涉及 WalletConnect 细节，再读 `common/walletconnect.md`

回答边界：

- Deposit 当前 active。
- 包含 GTR / Exchange 地址充值与 WalletConnect 充值。
- GTR 与 WalletConnect 不共用白名单、状态和结果页规则。

### 7.3 用户问：Receive 是否上线？

读取顺序：

1. `wallet/_index.md`
2. `wallet/runtime-read-model.md`
3. `wallet/receive.md`

回答边界：

- Receive 当前为 deferred / placeholder。
- 不能作为独立 active 功能事实源。
- 地址充值能力应读 `wallet/deposit.md`。

### 7.4 用户问：Send 是否可用？

读取顺序：

1. `wallet/_index.md`
2. `wallet/send.md`
3. `changelog/decision-log/2026-05-01-send-compliance.md`

回答边界：

- Send / Withdraw 当前 deferred。
- 因合规原因未上线。
- 旧方案不得直接作为当前事实。

## 8. 与 ALL-GAP 的关系

Runtime Read Model 不替代 ALL-GAP。遇到以下问题必须转向 ALL-GAP：

| 问题类型 | ALL-GAP |
|---|---|
| GTR / WC 与 ActivityType 映射 | ALL-GAP-001 / 002 |
| Deposit transactionId / relatedId / id 串联 | ALL-GAP-007 / 014 |
| Risk Withheld 与 Wallet state / 余额关系 | ALL-GAP-008 |
| Deposit success 与 Wallet COMPLETED 映射 | ALL-GAP-016 |
| Wallet balance 字段和展示规则 | ALL-GAP-055 / 056 / 057 / 058 |
| Receive 是否独立上线及页面字段 | ALL-GAP-059 / 060 / 061 / 062 |
| 状态模型跨层映射 | ALL-GAP-062 |

## 9. 来源引用

- (Ref: knowledge-base/wallet/_index.md)
- (Ref: knowledge-base/wallet/balance.md)
- (Ref: knowledge-base/wallet/deposit.md)
- (Ref: knowledge-base/wallet/receive.md)
- (Ref: knowledge-base/wallet/send.md)
- (Ref: knowledge-base/transaction/history.md)
- (Ref: knowledge-base/transaction/reconciliation.md)
- (Ref: knowledge-base/kyc/account-opening.md)
- (Ref: knowledge-base/changelog/knowledge-gaps.md)
- (Ref: knowledge-base/changelog/decision-log/2026-05-01-send-compliance.md)
- (Ref: knowledge-base/changelog/decision-log/2026-05-02-deposit-active.md)
- (Ref: knowledge-base/changelog/decision-log/2026-05-02-receive-deferred.md)
