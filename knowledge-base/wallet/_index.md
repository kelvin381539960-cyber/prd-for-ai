---
module: wallet
feature: wallet-index
version: "2.0"
status: active
source_doc: knowledge-base/wallet/deposit.md；knowledge-base/wallet/balance.md；knowledge-base/wallet/receive.md；knowledge-base/wallet/send.md；knowledge-base/transaction/history.md；knowledge-base/kyc/wallet-kyc.md；knowledge-base/changelog/knowledge-gaps.md；knowledge-base/_system-boundary.md；用户确认结论 2026-05-02
source_section: Wallet 模块使用态结构；KYC 独立；Wallet Transaction History 合并至 Transaction History；ALL-GAP 总表
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
  - _system-boundary
---

# Wallet 模块索引

## 1. 模块定位

Wallet 模块用于沉淀 AIX 钱包产品能力，包括余额展示、入金、收款和 deferred 的 Send。

Wallet 目录只承接钱包产品能力，不承接 KYC 主事实，也不承接交易历史统一层：

| 能力 | 当前主事实源 |
|---|---|
| Wallet KYC | `kyc/wallet-kyc.md` |
| Wallet Transaction History | `transaction/history.md` |
| Wallet Reconciliation / 对账 | `transaction/reconciliation.md` |

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

已迁出能力：

| 原能力 | 当前主事实源 | 使用规则 |
|---|---|---|
| Wallet KYC | `kyc/wallet-kyc.md` | 不从 Wallet 目录读取 KYC 主事实 |
| Wallet Transaction History | `transaction/history.md` | 不从 Wallet 目录读取交易历史主事实 |

## 3. 能力边界

| 能力域 | 当前处理 | 不包含 | 备注 |
|---|---|---|---|
| Balance | Wallet 目录维护 | Card balance | Card balance 仅在 Card Transaction Flow 中作为归集金额依据 |
| Deposit | Wallet 目录维护 | Send / Swap | 包含 GTR 和 WalletConnect；按子路径拆分 |
| Receive | Wallet 目录维护 | Deposit 旧方案 | Receive 是否独立上线需按来源确认 |
| Send / Withdraw | deferred | 当前 active 功能正文 | 因合规原因未上线 |
| Swap | deferred | 当前 active 功能正文 | 因合规原因未上线且需重做 |
| Wallet KYC / 开户 | KYC 目录维护 | Wallet 目录不维护 KYC 主事实 | 见 `kyc/wallet-kyc.md` |
| Transaction History | Transaction 目录维护 | Wallet 目录不维护交易历史正文 | 见 `transaction/history.md` |
| Reconciliation | Transaction 目录维护 | Wallet 不维护对账链路 | 见 `transaction/reconciliation.md` |
| Notification | Common 目录维护 | Wallet 不补通知文案 | 需引用 Notification 事实源 |

## 4. Deposit 子路径

| 子路径 | 当前状态 | 说明 |
|---|---|---|
| GTR / Exchange 地址充值 | active | 当前支持 Binance，列表可配置；自动交易报备，不需要交易声明，也不用校验地址白名单 |
| WalletConnect / Self-custodial Wallet 充值 | active | Approved 后自动 add whitelist；send_payment 后进入支付和 payment_info 轮询 |
| 其他 Deposit 旧方案 | 未确认 | 不得默认归档为 active |

## 5. 已确认 Wallet 相关基础字段

| 字段 / 能力 | 结论 | 主事实源 | 备注 |
|---|---|---|---|
| Wallet 交易 `id` | 钱包交易记录 / 详情出参均包含 `id`，Long，交易 id | `transaction/history.md` | 关联规则见 ALL-GAP-015、ALL-GAP-018 |
| Wallet 详情入参 `transactionId` | 单笔钱包交易详情入参为 `transactionId`，Unique transaction ID from DTC | `transaction/history.md` | 与 Card `data.id` / `D-REQUEST-ID` 的关系见 ALL-GAP |
| Wallet 交易 `state` | 枚举为 `PENDING`、`PROCESSING`、`AUTHORIZED`、`COMPLETED`、`REJECTED`、`CLOSED` | `transaction/status-model.md` | 不等同 Deposit 外部状态 |
| Wallet Search Balance History | 可查询钱包交易历史，返回 `activityType`、`relatedId`、`time`、`state` 等字段 | `transaction/history.md` | `relatedId` 取值见 ALL-GAP-014 |

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

## 7. 使用规则

1. 查询 Wallet 产品能力时，先读本索引，再读对应 Wallet 事实文件。
2. 查询 KYC 时，读 `kyc/wallet-kyc.md`。
3. 查询交易历史时，读 `transaction/history.md`。
4. 查询资金追踪 / 对账时，读 `transaction/reconciliation.md`。
5. 查询系统责任边界时，读 `knowledge-base/_system-boundary.md`。
6. 不默认读取 moved notice、stage-review、历史 checklist 或 migrated-reference 文件。

## 8. 来源引用

- (Ref: knowledge-base/wallet/deposit.md)
- (Ref: knowledge-base/wallet/balance.md)
- (Ref: knowledge-base/wallet/receive.md)
- (Ref: knowledge-base/wallet/send.md)
- (Ref: knowledge-base/transaction/history.md)
- (Ref: knowledge-base/kyc/wallet-kyc.md)
- (Ref: knowledge-base/transaction/reconciliation.md)
- (Ref: knowledge-base/changelog/knowledge-gaps.md / ALL-GAP 总表)
- (Ref: knowledge-base/_system-boundary.md)
- (Ref: 用户确认结论 / 2026-05-02 / KYC 独立，Wallet Transaction History 合并进 Transaction History)
