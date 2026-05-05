---
module: wallet
feature: wallet-index
version: "3.0"
status: active
source_doc: knowledge-base/wallet/deposit.md；knowledge-base/wallet/balance.md；knowledge-base/transaction/history.md；knowledge-base/kyc/account-opening.md；knowledge-base/changelog/knowledge-gaps.md；knowledge-base/_system-boundary.md
source_section: Wallet runtime structure；Balance；Deposit；Transaction；KYC boundary；ALL-GAP
last_updated: 2026-05-05
owner: 吴忆锋
depends_on:
  - wallet/balance
  - wallet/deposit
  - transaction/history
  - kyc/account-opening
  - changelog/knowledge-gaps
  - _system-boundary
---

# Wallet 模块索引

## 1. 模块定位

Wallet 模块用于沉淀 AIX 钱包运行态事实，目前只保留余额展示和入金能力。

Wallet 目录不承接开户 / KYC 主事实，也不承接交易历史统一层。

| 能力 | 当前主事实源 |
|---|---|
| Account Opening / KYC / 钱包开户准入 | `kyc/account-opening.md` |
| Wallet Transaction History | `transaction/history.md` |
| Wallet Reconciliation / 对账 | `transaction/reconciliation.md` |

## 2. 当前文件

| 文件 | 状态 | 目标 |
|---|---|---|
| `wallet/_index.md` | active | Wallet 模块边界、能力清单与依赖关系 |
| `wallet/balance.md` | active | 钱包余额、币种、余额展示与查询接口 |
| `wallet/deposit.md` | active | GTR / Exchange 地址充值与 WalletConnect 入金能力 |

## 3. 已删除 / 不维护能力

| 能力 | 当前处理 | 原因 |
|---|---|---|
| Receive | 删除，不作为独立能力维护 | 当前没有独立 Receive 产品能力；地址充值归入 Deposit |
| Send | 删除，不作为能力维护 | 实际没有上线能力 |
| Swap | 删除，不作为能力维护 | 实际没有上线能力 |

## 4. 能力边界

| 能力域 | 当前处理 | 不包含 |
|---|---|---|
| Balance | Wallet 目录维护 | Card balance、交易详情、对账链路 |
| Deposit | Wallet 目录维护 | Send / Swap / 独立 Receive |
| Account Opening / KYC / 开户准入 | KYC 目录维护 | Wallet 目录不维护 KYC 主事实 |
| Transaction History | Transaction 目录维护 | Wallet 目录不维护交易历史正文 |
| Reconciliation | Transaction 目录维护 | Wallet 不维护对账链路 |
| Notification | Common 目录维护 | Wallet 不补通知文案 |

## 5. Deposit 子路径

| 子路径 | 当前状态 | 说明 |
|---|---|---|
| GTR / Exchange 地址充值 | active | 当前支持 Binance，列表可配置；自动交易报备，不需要交易声明，也不用校验地址白名单 |
| WalletConnect / Self-custodial Wallet 充值 | active | Approved 后自动 add whitelist；send_payment 后进入支付和 payment_info 轮询 |
| 其他 Deposit 旧方案 | 未确认 | 不得默认归档为 active |

## 6. 已确认 Wallet 基础字段

| 字段 / 能力 | 结论 | 主事实源 | 备注 |
|---|---|---|---|
| Wallet 交易 `id` | 钱包交易记录 / 详情出参均包含 `id`，Long，交易 id | `transaction/history.md` | 关联规则见 ALL-GAP |
| Wallet 详情入参 `transactionId` | 单笔钱包交易详情入参为 `transactionId`，Unique transaction ID from DTC | `transaction/history.md` | 与 Card `data.id` / `D-REQUEST-ID` 的关系见 ALL-GAP |
| Wallet 交易 `state` | 枚举为 `PENDING`、`PROCESSING`、`AUTHORIZED`、`COMPLETED`、`REJECTED`、`CLOSED` | `transaction/status-model.md` | 不等同 Deposit 外部状态 |
| Wallet Search Balance History | 可查询钱包交易历史，返回 `activityType`、`relatedId`、`time`、`state` 等字段 | `transaction/history.md` | `relatedId` 取值见 ALL-GAP |

## 7. 与 ALL-GAP 的关系

以下内容不得在 Wallet 阶段补写为事实，只引用 ALL-GAP：

| ALL-GAP | 主题 |
|---|---|
| ALL-GAP-001 | GTR 是否使用 `FIAT_DEPOSIT=6` |
| ALL-GAP-002 | WalletConnect 是否使用 `CRYPTO_DEPOSIT=10` |
| ALL-GAP-007 | `relatedId / transactionId / id` 如何串联 GTR / WalletConnect 入金 |
| ALL-GAP-008 | Risk Withheld 与 Wallet `state` / 余额关系 |
| ALL-GAP-014 | Wallet `relatedId` 在 Card / GTR / WC 场景取值 |
| ALL-GAP-030 | Account Opening / KYC 与 Card KYC 关系 |
| ALL-GAP-031 | Account Opening / KYC 是否为 GTR / WalletConnect Deposit 前置 |

## 8. 使用规则

1. 查询 Wallet 产品能力时，先读本索引，再读对应 Wallet 事实文件。
2. 查询入金、地址充值、WalletConnect 充值时，读 `wallet/deposit.md`。
3. 查询余额时，读 `wallet/balance.md`。
4. 查询开户、KYC、Sub Account、`D-SUB-ACCOUNT-ID` 或 Wallet 能力准入时，读 `kyc/account-opening.md`。
5. 查询交易历史时，读 `transaction/history.md`。
6. 查询资金追踪 / 对账时，读 `transaction/reconciliation.md`。
7. 不得把 Receive、Send、Swap 写成当前 active 能力。

## 9. 来源引用

- (Ref: knowledge-base/wallet/deposit.md)
- (Ref: knowledge-base/wallet/balance.md)
- (Ref: knowledge-base/transaction/history.md)
- (Ref: knowledge-base/kyc/account-opening.md)
- (Ref: knowledge-base/transaction/reconciliation.md)
- (Ref: knowledge-base/changelog/knowledge-gaps.md / ALL-GAP 总表)
- (Ref: knowledge-base/_system-boundary.md)
