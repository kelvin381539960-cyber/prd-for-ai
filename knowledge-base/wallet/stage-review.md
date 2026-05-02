---
module: wallet
feature: wallet-stage-review
version: "1.1"
status: active
source_doc: IMPLEMENTATION_PLAN.md；knowledge-base/wallet/_index.md；knowledge-base/wallet/balance.md；knowledge-base/wallet/deposit.md；knowledge-base/wallet/receive.md；knowledge-base/wallet/send.md；knowledge-base/kyc/wallet-kyc.md；knowledge-base/transaction/history.md；knowledge-base/transaction/reconciliation.md；knowledge-base/changelog/knowledge-gaps.md；用户确认结论 2026-05-02
source_section: Wallet 阶段回扫；IMPLEMENTATION_PLAN v4.6；KYC 独立；Wallet Transaction History 合并至 Transaction History；ALL-GAP 唯一总表
last_updated: 2026-05-02
owner: 吴忆锋
depends_on:
  - wallet/_index
  - wallet/balance
  - wallet/deposit
  - wallet/receive
  - wallet/send
  - kyc/wallet-kyc
  - transaction/history
  - transaction/reconciliation
  - changelog/knowledge-gaps
---

# Wallet 阶段回扫记录

## 1. 回扫结论

Wallet 阶段已完成钱包产品能力基础版知识库沉淀，但未达到完整 `PASS`。

本次 Stage Review 结果为：`PARTIAL PASS`。

含义：

- Wallet 目录当前只承接钱包产品能力：Balance、Deposit、Receive、Send。
- Deposit 为 active，范围包含 GTR / Exchange 地址充值与 WalletConnect / Self-custodial Wallet 充值。
- Send 与 Swap 因合规原因未上线或需重做，保持 `deferred`，不作为 active 功能事实源。
- KYC 主事实已迁移至 `knowledge-base/kyc/wallet-kyc.md`。
- Wallet Transaction History 主事实已合并至 `knowledge-base/transaction/history.md`。
- 资金追踪 / ID 链路 / 对账边界由 `knowledge-base/transaction/reconciliation.md` 承接。
- 所有不确定项统一引用 `knowledge-base/changelog/knowledge-gaps.md` 的 ALL-GAP 编号，Wallet 模块不再维护独立 checklist / gaps。

## 2. 回扫范围

| 文件 | 状态 | 回扫结果 |
|---|---|---|
| `wallet/_index.md` | active | Wallet 模块边界已更新；只承接钱包产品能力 |
| `wallet/balance.md` | active | Balance 边界已建立；余额字段和可用性细节仍按 ALL-GAP 收敛 |
| `wallet/deposit.md` | active | GTR / Exchange 与 WalletConnect 流程、异常和结果状态已阶段性回填 |
| `wallet/receive.md` | active / 基础版 | Receive 基础占位已建立；与 Deposit 子路径关系待来源确认 |
| `wallet/send.md` | deferred | 因合规原因未上线，不作为 active 功能事实源 |
| `wallet/swap.md` | deferred | 因合规原因未上线且需重做，不创建 active 功能正文 |
| `wallet/kyc.md` | moved | 兼容入口，主事实源为 `kyc/wallet-kyc.md` |
| `wallet/transaction-history.md` | moved | 兼容入口，主事实源为 `transaction/history.md` |

## 3. 已通过项

| 检查项 | 结果 | 说明 |
|---|---|---|
| 目录边界 | 通过 | Wallet 只承接产品能力；KYC 与 Transaction History 已迁出 |
| 功能上线状态 | 通过 | Deposit active；Send / Swap deferred；未把未上线功能写成 active |
| Deposit 范围 | 通过 | 已拆分 GTR / Exchange 与 WalletConnect 两条子路径 |
| WalletConnect 关键流程 | 部分通过 | token、WebSocket、create_payment_intent、自动加白、send_payment、payment_info 已回填 |
| GTR 关键流程 | 部分通过 | Select Asset、Select Network、Receive Crypto、Get Deposit Address、Binance / GTR Wallet 转账已回填 |
| KYC 边界 | 通过 | Wallet KYC 已迁入 KYC 模块，不再由 Wallet 目录维护主事实 |
| Transaction History 边界 | 通过 | Wallet History 已迁入 Transaction 模块，不再由 Wallet 目录维护主事实 |
| ALL-GAP 唯一源 | 通过 | Wallet 不再维护模块级待确认表，只引用 ALL-GAP |
| 无来源补写 | 通过 | 未把缺失字段、状态、文案、流程写成事实 |

## 4. 当前 ALL-GAP 引用

Wallet 阶段不维护独立 gap。相关不确定项统一引用：

| 编号 | 主题 | 影响 |
|---|---|---|
| ALL-GAP-001 | GTR 是否使用 `FIAT_DEPOSIT=6` | 交易历史分类、筛选、统计 |
| ALL-GAP-002 | WalletConnect 是否使用 `CRYPTO_DEPOSIT=10` | 交易历史分类、筛选、统计 |
| ALL-GAP-007 | `relatedId / transactionId / id` 如何串联 GTR / WalletConnect 入金 | 入金记录追踪和对账 |
| ALL-GAP-008 | Risk Withheld 与 Wallet `state` / 余额关系 | 详情状态、余额展示、状态筛选 |
| ALL-GAP-009 | GTR 地址充值是否有与 WalletConnect 相同的结果页 | GTR 充值完成体验 |
| ALL-GAP-010 | GTR / WalletConnect 是否复用 Deposit success / under review 通知 | 通知触发与跳转 |
| ALL-GAP-011 | GTR 异常处理和客服口径 | 异常闭环 |
| ALL-GAP-012 | WalletConnect `payment_info false / Transaction not found` 后续处理 | 状态不明场景 |
| ALL-GAP-013 | WalletConnect 失败是否需要告警 | 排障和监控 |
| ALL-GAP-030 | Wallet KYC 与 Card KYC 关系 | 准入状态复用 |
| ALL-GAP-031 | Wallet KYC 是否为 GTR / WalletConnect Deposit 前置 | Deposit 入口拦截 |
| ALL-GAP-032 | Wallet 开户触发时机 | Wallet 初始化 |
| ALL-GAP-033 | KYC 失败 / 重试 / 人工处理规则 | KYC 异常闭环 |

## 5. 阶段判断

| 判断项 | 结论 |
|---|---|
| Wallet 产品能力目录边界 | PASS |
| Wallet Balance | PARTIAL PASS |
| Wallet Deposit | PARTIAL PASS |
| Wallet Receive | PARTIAL PASS |
| Wallet KYC 归属 | PASS，已迁至 KYC 模块 |
| Wallet Transaction History 归属 | PASS，已迁至 Transaction 模块 |
| Send / Swap 上线状态处理 | PASS |
| 资金追踪 / 对账 | PARTIAL PASS，见 Transaction Reconciliation 与 ALL-GAP |
| 是否允许继续后续回扫 | 允许，带 ALL-GAP 继续 |
| 是否允许把 ALL-GAP 写成事实 | 不允许 |

## 6. 后续要求

1. Wallet 目录后续只维护 Balance、Deposit、Receive、Send 等产品能力。
2. Wallet KYC 新事实写入 `kyc/wallet-kyc.md`。
3. Wallet Transaction History 新事实写入 `transaction/history.md`。
4. 资金追踪 / 对账新事实写入 `transaction/reconciliation.md`，并同步 ALL-GAP。
5. Send / Swap 必须继续保持 `deferred`，新方案确认后才能转译。
6. 所有不确定项只能写入 `knowledge-base/changelog/knowledge-gaps.md`，不得在 Wallet 文件中新增 checklist / TODO / gaps 表。

## 7. 来源引用

- (Ref: IMPLEMENTATION_PLAN.md / v4.6)
- (Ref: knowledge-base/wallet/_index.md / v1.4)
- (Ref: knowledge-base/wallet/deposit.md / v1.5)
- (Ref: knowledge-base/kyc/wallet-kyc.md / v1.0)
- (Ref: knowledge-base/transaction/history.md / v1.2)
- (Ref: knowledge-base/transaction/reconciliation.md / v1.0)
- (Ref: knowledge-base/changelog/knowledge-gaps.md / ALL-GAP 总表)
- (Ref: 用户确认结论 / 2026-05-02 / KYC 独立，Wallet Transaction History 合并进 Transaction History)
