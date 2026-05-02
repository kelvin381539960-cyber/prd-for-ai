---
module: wallet
feature: wallet-index
version: "1.4"
status: active
source_doc: IMPLEMENTATION_PLAN.md；knowledge-base/wallet/deposit.md；knowledge-base/wallet/balance.md；knowledge-base/wallet/receive.md；knowledge-base/wallet/send.md；knowledge-base/transaction/history.md；knowledge-base/kyc/wallet-kyc.md；knowledge-base/changelog/knowledge-gaps.md；用户确认结论 2026-05-02
source_section: Wallet 模块结构调整；KYC 独立；Wallet Transaction History 合并至 Transaction History；ALL-GAP 总表
last_updated: 2026-05-02
owner: 吴忆锋
depends_on:
  - wallet/balance
  - wallet/deposit
  - wallet/receive
  - wallet/send
  - transaction/history
  - kyc/wallet-kyc
  - changelog/knowledge-gaps
---

# Wallet 模块索引

## 1. 模块定位

Wallet 模块用于沉淀 AIX 钱包产品能力，包括余额展示、入金、收款和已 deferred 的 Send。

Wallet 目录不再承接 KYC 主事实，也不再承接交易历史统一层：

| 原归属 | 当前主事实源 |
|---|---|
| `wallet/kyc.md` | `kyc/wallet-kyc.md` |
| `wallet/transaction-history.md` | `transaction/history.md` |

Deposit 能力存在，包含 GTR / Exchange 地址充值和 WalletConnect / Self-custodial Wallet 充值，属于当前 Wallet active 能力。

Send 和 Swap 因合规原因未上线或需重做，不进入当前 active 功能归档。相关旧方案不得作为当前正式功能事实源。

涉及 Card 资金归集时，Wallet 目录只引用已确认事实，未确认链路统一进入 ALL-GAP 总表。

## 2. 当前文件

| 文件 | 状态 | 目标 | 备注 |
|---|---|---|---|
| `wallet/_index.md` | active | 建立 Wallet 模块边界、能力清单与依赖关系 | 当前文件 |
| `wallet/balance.md` | active | 转译钱包余额、币种、余额展示与查询接口 | 钱包产品能力 |
| `wallet/deposit.md` | active | 转译 GTR / WalletConnect 入金能力 | 已补 GTR / WC 流程、异常、结果状态 |
| `wallet/receive.md` | active | 转译 Receive / 收款地址相关能力 | 与 Deposit 子路径关系待来源确认 |
| `wallet/send.md` | deferred | Send 因合规原因未上线 | 不作为 active 功能事实源 |
| `wallet/kyc.md` | moved | 兼容入口 | 主事实源为 `kyc/wallet-kyc.md` |
| `wallet/transaction-history.md` | moved | 兼容入口 | 主事实源为 `transaction/history.md` |
| `wallet/stage-review.md` | active | Wallet 阶段 Gate Review | 后续需同步结构调整结论 |

## 3. 能力边界

| 能力域 | 当前处理 | 不包含 | 备注 |
|---|---|---|---|
| Balance | Wallet 目录维护 | Card balance | Card balance 仅在 Card Transaction Flow 中作为归集金额依据 |
| Deposit | Wallet 目录维护 | Send / Swap | 包含 GTR 和 WalletConnect；按子路径拆分 |
| Receive | Wallet 目录维护 | Deposit 旧方案 | Receive 是否独立上线需按来源确认 |
| Send / Withdraw | deferred | 当前 active 功能正文 | 因合规原因未上线 |
| Swap | deferred | 当前 active 功能正文 | 因合规原因未上线且需重做 |
| Wallet KYC / 开户 | KYC 目录维护 | Wallet 目录不再维护 KYC 主事实 | 见 `kyc/wallet-kyc.md` |
| Transaction History | Transaction 目录维护 | Wallet 目录不再维护交易历史正文 | 见 `transaction/history.md` |
| Reconciliation | Transaction 目录维护 | Wallet 不维护对账链路 | 见 `transaction/reconciliation.md` |
| Notification | Common 目录维护 | Wallet 不补通知文案 | 需引用 Notification PRD |

## 4. Deposit 子路径

| 子路径 | 当前状态 | 说明 |
|---|---|---|
| GTR / Exchange 地址充值 | active | 当前支持 Binance，列表可配置；自动交易报备，不需要交易声明，也不用校验地址白名单 |
| WalletConnect / Self-custodial Wallet 充值 | active | Approved 后自动 add whitelist；send_payment 后进入支付和 payment_info 轮询 |
| 其他 Deposit 旧方案 | 未确认 | 不得默认归档为 active |

## 5. 已确认 Wallet 相关基础字段

| 字段 / 能力 | 结论 | 主事实源 | 备注 |
|---|---|---|---|
| Wallet 交易 `id` | 钱包交易记录 / 详情出参均包含 `id`，Long，交易 id | transaction/history.md | 关联规则见 ALL-GAP-015、ALL-GAP-018 |
| Wallet 详情入参 `transactionId` | 单笔钱包交易详情入参为 `transactionId`，Unique transaction ID from DTC | transaction/history.md | 与 Card `data.id` / `D-REQUEST-ID` 的关系见 ALL-GAP |
| Wallet 交易 `state` | 枚举为 `PENDING`、`PROCESSING`、`AUTHORIZED`、`COMPLETED`、`REJECTED`、`CLOSED` | transaction/status-model.md | 不等同 Deposit 外部状态 |
| Wallet Search Balance History | 可查询钱包交易历史，返回 `activityType`、`relatedId`、`time`、`state` 等字段 | transaction/history.md | `relatedId` 取值见 ALL-GAP-014 |

## 6. 与 ALL-GAP 的关系

以下内容不得在 Wallet 阶段补写为事实，只引用 ALL-GAP：

| ALL-GAP | 主题 |
|---|---|
| ALL-GAP-001 | GTR 是否使用 `FIAT_DEPOSIT=6` |
| ALL-GAP-002 | WalletConnect 是否使用 `CRYPTO_DEPOSIT=10` |
| ALL-GAP-007 | `relatedId / transactionId / id` 如何串联 GTR / WalletConnect 入金 |
| ALL-GAP-008 | Risk Withheld 与 Wallet `state` / 余额关系 |
| ALL-GAP-014 | Wallet `relatedId` 在 Card / GTR / WC 场景取值 |
| ALL-GAP-030 | Wallet KYC 与 Card KYC 关系 |
| ALL-GAP-031 | Wallet KYC 是否为 GTR / WalletConnect Deposit 前置 |

## 7. 转译顺序建议

| 顺序 | 文件 | 原因 |
|---|---|---|
| 1 | `wallet/balance.md` | 余额是 Deposit / Receive 的共用基础 |
| 2 | `wallet/deposit.md` | Deposit 已确认存在，需拆 GTR / WalletConnect |
| 3 | `wallet/receive.md` | 收款地址能力需与 Deposit 子路径边界确认 |
| 4 | `transaction/history.md` | Wallet Transaction History 已迁移至 Transaction 统一层 |
| 5 | `kyc/wallet-kyc.md` | Wallet KYC 已迁移至 KYC 模块 |
| 6 | `wallet/stage-review.md` | 完成 Wallet 阶段 Gate Review |

暂不推进：

| 文件 | 原因 |
|---|---|
| `wallet/send.md` | 因合规原因未上线，只保留 deferred 占位 |
| `wallet/swap.md` | 因合规原因未上线且需重做，新方案确认后再转译 |

## 8. Stage Review 关注点

Wallet 阶段完成后必须检查：

1. Wallet 产品能力是否只保留 Balance / Deposit / Receive / Send。
2. KYC 主事实是否已迁移至 `kyc/wallet-kyc.md`。
3. Transaction History 主事实是否已迁移至 `transaction/history.md`。
4. Deposit、Receive、余额的接口路径和字段来源是否明确。
5. GTR / WalletConnect 是否拆分清楚。
6. Send / Swap 是否保持 deferred，没有被写成 active 功能事实。
7. 与 Card Transaction Flow 的 deferred gaps 是否保持隔离，未被写成事实。
8. 所有不确定项是否只引用 ALL-GAP 编号。

## 9. 来源引用

- (Ref: IMPLEMENTATION_PLAN.md / v4.5)
- (Ref: knowledge-base/wallet/deposit.md / v1.5)
- (Ref: knowledge-base/transaction/history.md / v1.2)
- (Ref: knowledge-base/kyc/wallet-kyc.md / v1.0)
- (Ref: knowledge-base/changelog/knowledge-gaps.md / ALL-GAP 总表)
- (Ref: 用户确认结论 / 2026-05-02 / KYC 独立，Wallet Transaction History 合并进 Transaction History)
