---
module: transaction
feature: detail
version: "1.2"
status: active
source_doc: IMPLEMENTATION_PLAN.md；DTC接口文档/DTC Wallet OpenAPI Document20260126 (1).docx；knowledge-base/transaction/_index.md；knowledge-base/transaction/status-model.md；knowledge-base/transaction/history.md；knowledge-base/card/card-transaction-flow.md；knowledge-base/wallet/deposit.md；knowledge-base/changelog/knowledge-gaps.md
source_section: Transaction _index v1.1；Transaction Status Model v1.1；Transaction History v1.2；Wallet Deposit v1.6；Search Balance History / 4.2.4；Appendix ActivityType；ALL-GAP 总表
last_updated: 2026-05-02
owner: 吴忆锋
depends_on:
  - transaction/_index
  - transaction/status-model
  - transaction/history
  - card/card-transaction-flow
  - wallet/deposit
  - changelog/knowledge-gaps
---

# Transaction Detail 交易详情

## 1. 功能定位

Transaction Detail 用于统一沉淀 AIX 中 Card Transaction Detail 与 Wallet Transaction Detail 的详情入口、查询入参、字段边界和来源口径。

本文件不合并 Card / Wallet 的详情接口，不将两个模块中的 `transactionId` 视为同一业务字段，不补写未确认的关联关系。

所有未确认问题统一引用 `knowledge-base/changelog/knowledge-gaps.md` 的 ALL-GAP 编号；本文不再维护独立 TXN-DETAIL-GAP checklist。

## 2. 详情类型

| 详情类型 | 当前状态 | 来源 | 处理 |
|---|---|---|---|
| Card Transaction Detail | active | Card Transaction Flow | 可引用已确认字段和入口 |
| Wallet Transaction Detail | active / 基础版 | Transaction History | 可引用 `transactionId` 入参、`id` 出参、`state`、ActivityType 边界 |
| Deposit Transaction Detail | active / 基础版 | Wallet Deposit / Transaction History | 可引用 Deposit success / Risk Withheld / ActivityType 边界；完整字段见 ALL-GAP |
| Send Transaction Detail | deferred | Wallet Stage Review | Send 未上线，不纳入 active 详情模型 |
| Swap Transaction Detail | deferred | Wallet Stage Review | Swap 未上线 / 需重做，不纳入 active 详情模型 |

## 3. Card Transaction Detail

| 项目 | 当前结论 | 来源 | 备注 |
|---|---|---|---|
| 入口 | Card Home 交易区域、Card History 记录 | Card Transaction Flow | 已确认 |
| 查询接口 | Card Transaction Detail Inquiry | Card Transaction Flow / DTC Card Issuing | 已确认 |
| 查询入参 | 上送 Card Transaction ID | Card Transaction Flow | 与 Wallet `transactionId` 不等同 |
| 交易 ID | DTC Card `data.id` / Transaction ID | Card Transaction Flow | 可引用 |
| 原始交易 ID | `originalId`，Original Transaction ID，选填 | Card Transaction Flow | 可引用 |
| 异步更新 | DTC 异步通知结果需同步更新并展示 | Card Transaction Flow | 已确认 |
| 复制能力 | Transaction ID 支持复制 | Card Transaction Flow | 已确认 |

### 3.1 Card Detail 可引用字段

| 字段 / 信息 | 当前处理 |
|---|---|
| `id` / `data.id` | DTC Card Transaction ID |
| `originalId` | Original Transaction ID，选填 |
| `cardId` | Card 关联字段 |
| `processorTransactionId` | Card 交易关联字段 |
| `referenceNo` | Card 交易关联字段 |
| `amount` / `currency` | Card 交易金额与币种字段 |
| `requestAmount` / `requestCurrency` | 请求金额与请求币种字段 |
| `indicator` | 交易方向字段 |
| `transactionDate` / `transactionTime` / `confirmedTime` / `createdDate` | Card 交易时间字段 |
| `merchantName` | 商户字段 |

Card Detail 前端展示字段完整列表仍需确认，见 ALL-GAP-049。

## 4. Wallet Transaction Detail

| 项目 | 当前结论 | 来源 | 备注 |
|---|---|---|---|
| 详情能力 | 存在 Wallet 交易详情能力 | Transaction History | 基础事实已确认 |
| 查询入参 | `transactionId` | Transaction History | Unique transaction ID from DTC |
| 详情 ID | 出参包含 `id`，Long，交易 id | Transaction History | 可引用 |
| 状态字段 | `state` | Transaction History / Status Model | 枚举已确认，进入 / 退出条件待补 |
| 余额历史关联 | Search Balance History 返回 `relatedId` | Transaction History | 具体关联规则见 ALL-GAP-014 |
| ActivityType | Search Balance History 使用 ActivityType 分类 | Transaction History / DTC Wallet OpenAPI | 已确认部分枚举 |

### 4.1 Wallet Detail 可引用字段

| 字段 / 信息 | 当前处理 |
|---|---|
| `transactionId` | 详情查询入参，Unique transaction ID from DTC |
| `id` | Wallet 交易记录 / 详情出参中的 Long 交易 id |
| `state` | Wallet 交易状态字段 |
| `activityType` | Search Balance History 分类字段，已确认部分枚举 |
| `relatedId` | Search Balance History 返回字段，关联口径待补 |
| `time` | Search Balance History 返回字段，格式待补 |

Wallet Detail 完整请求字段、响应字段、页面展示字段、是否支持复制交易 ID，见 ALL-GAP-048。

### 4.2 ActivityType 对详情的影响

| 枚举 | 值 | 含义 | Detail 处理 |
|---|---:|---|---|
| `FIAT_DEPOSIT` | 6 | Fiat Deposit | 可作为法币入金详情分类引用；是否对应 GTR 见 ALL-GAP-001 |
| `CRYPTO_DEPOSIT` | 10 | Stablecoin Deposit | 可作为 Crypto / WalletConnect 入金详情分类引用；是否对应 WC 见 ALL-GAP-002 |
| `DTC_WALLET` | 13 | DTC Wallet Payment | 可作为 DTC Wallet Payment 详情分类引用 |
| `CARD_PAYMENT_REFUND` | 20 | Card Payment Refund | 可作为 Card refund 入 Wallet 相关详情分类引用；与 Card 归集链路关联见 ALL-GAP-017、ALL-GAP-018 |

## 5. Deposit Detail 边界

| 场景 | 可引用事实 | 不得推导 |
|---|---|---|
| Deposit success | Notification 有 Deposit success；payment_info success 会同步触发资金流转账，理论立即可用但可能很短延迟 | 不得直接等同 Wallet `COMPLETED`；见 ALL-GAP-016 |
| Deposit Risk Withheld | 未加 senderAddress whitelist 时可出现 Risk Withheld；用户确认不触发结果页，详情展示 under review | 不得直接等同 Wallet `REJECTED`、`PENDING`、`PROCESSING`；见 ALL-GAP-008 |
| GTR Deposit Detail | Deposit 包含 GTR；`FIAT_DEPOSIT=6` 存在 | 不得写成 GTR 必然等同 FIAT_DEPOSIT；见 ALL-GAP-001 |
| WalletConnect Deposit Detail | Deposit 包含 WC；`CRYPTO_DEPOSIT=10` 存在；DTC Crypto Deposit 规则可引用 | 不得写成 WC 必然等同 CRYPTO_DEPOSIT；见 ALL-GAP-002 |

## 6. Card Detail 与 Wallet Detail 边界

| 维度 | Card Detail | Wallet Detail | 处理 |
|---|---|---|---|
| 查询入参 | Card Transaction ID | Wallet `transactionId` | 不等同 |
| 交易 ID | DTC Card `data.id` | Wallet `id` / `transactionId` | 不合并 |
| 状态字段 | Card DTC transaction status / state 来源 | Wallet `state`；Deposit `Risk Withheld` / `success` | 并列引用 |
| 详情接口 | Card Transaction Detail Inquiry | Wallet Transaction Detail | 不合并接口 |
| ActivityType | Card 使用 Card 交易类型 / 状态 | Wallet 使用 ActivityType | 不合并分类 |
| 复制字段 | Card Transaction ID 支持复制 | Wallet 是否支持复制见 ALL-GAP-048 | 不套用 Card 规则 |
| 时间字段 | Card 有多个交易时间字段 | Wallet `time` 已知，其他待补 | 不混写 |

## 7. 不写入事实的内容

以下内容当前不得写成事实：

1. Card Transaction ID 等同于 Wallet `transactionId`。
2. Wallet `transactionId` 等同于 Card `data.id`。
3. Wallet `id` 等同于 Card `data.id`。
4. Wallet `relatedId` 等同于 Card `data.id`。
5. Wallet `relatedId` 等同于 AIX 归集请求 ID。
6. Card Detail 与 Wallet Detail 使用同一个详情接口。
7. Wallet Detail 字段与 Card Detail 字段完全一致。
8. Wallet Detail 的复制规则与 Card Detail 一致。
9. Send / Swap Detail 属于当前 active 范围。
10. Card balance 转 Wallet 的资金追踪链路已闭环。
11. `FIAT_DEPOSIT` 必然等同 GTR。
12. `CRYPTO_DEPOSIT` 必然等同 WalletConnect。
13. Deposit success 必然等同 Wallet `COMPLETED`。
14. Risk Withheld 必然等同 Wallet `REJECTED`。

## 8. ALL-GAP 引用

本文不维护独立待补表。Transaction Detail 相关不确定项统一引用 ALL-GAP：

| 编号 | 主题 |
|---|---|
| ALL-GAP-001 | GTR 是否使用 `FIAT_DEPOSIT=6` |
| ALL-GAP-002 | WalletConnect 是否使用 `CRYPTO_DEPOSIT=10` |
| ALL-GAP-007 | `relatedId / transactionId / id` 如何串联 GTR / WalletConnect 入金 |
| ALL-GAP-008 | Risk Withheld 与 Wallet `state` / 余额关系 |
| ALL-GAP-014 | Wallet `relatedId` 在 Card / GTR / WC 场景取值 |
| ALL-GAP-015 | Wallet `transactionId` 与 Wallet `id` 的关系 |
| ALL-GAP-016 | Deposit success 与 Wallet `state=COMPLETED` 的映射 |
| ALL-GAP-017 | Card Transaction 与 Wallet Transaction 是否一一对应 |
| ALL-GAP-018 | Card / Wallet 关联字段 |
| ALL-GAP-048 | Wallet Transaction Detail 完整请求 / 响应 / 页面展示 / 复制规则 |
| ALL-GAP-049 | Card Detail 前端展示字段完整列表 |

## 9. 历史 TXN-DETAIL-GAP 到 ALL-GAP 映射

本表用于无损迁移历史问题，不作为新的模块级 checklist。后续只维护 ALL-GAP。

| 原编号 | 原问题 | 当前 ALL-GAP |
|---|---|---|
| TXN-DETAIL-GAP-001 | Wallet Transaction Detail 完整请求字段 | ALL-GAP-048 |
| TXN-DETAIL-GAP-002 | Wallet Transaction Detail 完整响应字段 | ALL-GAP-048 |
| TXN-DETAIL-GAP-003 | Wallet Detail 页面展示字段 | ALL-GAP-048 |
| TXN-DETAIL-GAP-004 | Wallet Detail 是否支持复制交易 ID | ALL-GAP-048 |
| TXN-DETAIL-GAP-005 | Wallet `transactionId` 与交易记录 `id` 的关系 | ALL-GAP-015 |
| TXN-DETAIL-GAP-006 | Wallet `relatedId` 关联规则 | ALL-GAP-014 |
| TXN-DETAIL-GAP-007 | Card Detail 前端展示字段完整列表 | ALL-GAP-049 |
| TXN-DETAIL-GAP-008 | GTR 与 FIAT_DEPOSIT 的映射 | ALL-GAP-001 |
| TXN-DETAIL-GAP-009 | WalletConnect 与 CRYPTO_DEPOSIT 的映射 | ALL-GAP-002 |
| TXN-DETAIL-GAP-010 | Risk Withheld 在详情页的展示和处理 | ALL-GAP-003、ALL-GAP-008 |

## 10. 来源引用

- (Ref: DTC Wallet OpenAPI Document20260126 / 4.2.4 Search Balance History)
- (Ref: DTC Wallet OpenAPI Document20260126 / Appendix ActivityType)
- (Ref: DTC Wallet OpenAPI Document20260126 / 3.4 Crypto Deposit)
- (Ref: knowledge-base/transaction/status-model.md / v1.1)
- (Ref: knowledge-base/transaction/history.md / v1.2)
- (Ref: knowledge-base/wallet/deposit.md / v1.6)
- (Ref: knowledge-base/card/card-transaction-flow.md / v1.2)
- (Ref: knowledge-base/changelog/knowledge-gaps.md / ALL-GAP 总表)
