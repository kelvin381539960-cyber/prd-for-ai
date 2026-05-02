---
module: transaction
feature: detail
version: "1.1"
status: active
source_doc: IMPLEMENTATION_PLAN.md；DTC接口文档/DTC Wallet OpenAPI Document20260126 (1).docx；knowledge-base/transaction/_index.md；knowledge-base/transaction/status-model.md；knowledge-base/transaction/history.md；knowledge-base/card/card-transaction-flow.md；knowledge-base/wallet/transaction-history.md；knowledge-base/wallet/deposit.md；knowledge-base/changelog/knowledge-gaps.md
source_section: Transaction _index v1.0；Transaction Status Model v1.1；Transaction History v1.1；Wallet Transaction History v1.1；Wallet Deposit v1.4；Search Balance History / 4.2.4；Appendix ActivityType
last_updated: 2026-05-01
owner: 吴忆锋
depends_on:
  - transaction/_index
  - transaction/status-model
  - transaction/history
  - card/card-transaction-flow
  - wallet/transaction-history
  - wallet/deposit
  - changelog/knowledge-gaps
---

# Transaction Detail 交易详情

## 1. 功能定位

Transaction Detail 用于统一沉淀 AIX 中 Card Transaction Detail 与 Wallet Transaction Detail 的详情入口、查询入参、字段边界和来源口径。

本文件不合并 Card / Wallet 的详情接口，不将两个模块中的 `transactionId` 视为同一业务字段，不补写未确认的关联关系。

## 2. 详情类型

| 详情类型 | 当前状态 | 来源 | 处理 |
|---|---|---|---|
| Card Transaction Detail | active | Card Transaction Flow | 可引用已确认字段和入口 |
| Wallet Transaction Detail | active / 基础版 | Wallet Transaction History | 可引用 `transactionId` 入参、`id` 出参、`state`、ActivityType 边界 |
| Deposit Transaction Detail | active / 基础版 | Wallet Deposit / Wallet Transaction History | 可引用 Deposit success / Risk Withheld / ActivityType 边界；完整字段待补 |
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

## 4. Wallet Transaction Detail

| 项目 | 当前结论 | 来源 | 备注 |
|---|---|---|---|
| 详情能力 | 存在 Wallet 交易详情能力 | Wallet Transaction History | 基础事实已确认 |
| 查询入参 | `transactionId` | Wallet Transaction History | Unique transaction ID from DTC |
| 详情 ID | 出参包含 `id`，Long，交易 id | Wallet Transaction History | 可引用 |
| 状态字段 | `state` | Wallet Transaction History / Status Model | 枚举已确认，进入 / 退出条件待补 |
| 余额历史关联 | Search Balance History 返回 `relatedId` | Wallet Transaction History | 具体关联规则待补 |
| ActivityType | Search Balance History 使用 ActivityType 分类 | Wallet Transaction History / DTC Wallet OpenAPI | 已确认部分枚举 |

### 4.1 Wallet Detail 可引用字段

| 字段 / 信息 | 当前处理 |
|---|---|
| `transactionId` | 详情查询入参，Unique transaction ID from DTC |
| `id` | Wallet 交易记录 / 详情出参中的 Long 交易 id |
| `state` | Wallet 交易状态字段 |
| `activityType` | Search Balance History 分类字段，已确认部分枚举 |
| `relatedId` | Search Balance History 返回字段，关联口径待补 |
| `time` | Search Balance History 返回字段，格式待补 |

### 4.2 ActivityType 对详情的影响

| 枚举 | 值 | 含义 | Detail 处理 |
|---|---:|---|---|
| `FIAT_DEPOSIT` | 6 | Fiat Deposit | 可作为法币入金详情分类引用；是否对应 GTR 待确认 |
| `CRYPTO_DEPOSIT` | 10 | Stablecoin Deposit | 可作为 Crypto / WalletConnect 入金详情分类引用；是否对应 WC 待确认 |
| `DTC_WALLET` | 13 | DTC Wallet Payment | 可作为 DTC Wallet Payment 详情分类引用 |
| `CARD_PAYMENT_REFUND` | 20 | Card Payment Refund | 可作为 Card refund 入 Wallet 相关详情分类引用；与 Card 归集链路关联仍 deferred |

## 5. Deposit Detail 边界

| 场景 | 可引用事实 | 不得推导 |
|---|---|---|
| Deposit success | DTC Crypto Deposit 加白成功后自动 success；Notification 有 Deposit success | 不得直接等同 Wallet `COMPLETED`；不代表余额立即可用 |
| Deposit Risk Withheld | 未加 senderAddress whitelist 时 `status=102 Risk Withheld`；Notification 有 under review | 不得直接等同 Wallet `REJECTED`、`PENDING`、`PROCESSING` |
| GTR Deposit Detail | Deposit 包含 GTR；`FIAT_DEPOSIT=6` 存在 | 不得写成 GTR 必然等同 FIAT_DEPOSIT |
| WalletConnect Deposit Detail | Deposit 包含 WC；`CRYPTO_DEPOSIT=10` 存在；DTC Crypto Deposit 规则可引用 | 不得写成 WC 必然等同 CRYPTO_DEPOSIT |

## 6. Card Detail 与 Wallet Detail 边界

| 维度 | Card Detail | Wallet Detail | 处理 |
|---|---|---|---|
| 查询入参 | Card Transaction ID | Wallet `transactionId` | 不等同 |
| 交易 ID | DTC Card `data.id` | Wallet `id` / `transactionId` | 不合并 |
| 状态字段 | Card DTC transaction status / state 来源 | Wallet `state`；Deposit `Risk Withheld` / `success` | 并列引用 |
| 详情接口 | Card Transaction Detail Inquiry | Wallet Transaction Detail | 不合并接口 |
| ActivityType | Card 使用 Card 交易类型 / 状态 | Wallet 使用 ActivityType | 不合并分类 |
| 复制字段 | Card Transaction ID 支持复制 | Wallet 是否支持复制待补 | 不套用 Card 规则 |
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

## 8. 待补项

| 编号 | 待补项 | 来源建议 | 当前处理 |
|---|---|---|---|
| TXN-DETAIL-GAP-001 | Wallet Transaction Detail 完整请求字段 | DTC Wallet OpenAPI | 待补 |
| TXN-DETAIL-GAP-002 | Wallet Transaction Detail 完整响应字段 | DTC Wallet OpenAPI | 待补 |
| TXN-DETAIL-GAP-003 | Wallet Detail 页面展示字段 | Wallet PRD / 截图 | 待补 |
| TXN-DETAIL-GAP-004 | Wallet Detail 是否支持复制交易 ID | Wallet PRD / 截图 | 待补 |
| TXN-DETAIL-GAP-005 | Wallet `transactionId` 与交易记录 `id` 的关系 | DTC Wallet OpenAPI / 后端确认 | 待补 |
| TXN-DETAIL-GAP-006 | Wallet `relatedId` 关联规则 | DTC Wallet OpenAPI / 后端确认 | deferred / 待补 |
| TXN-DETAIL-GAP-007 | Card Detail 前端展示字段完整列表 | Transaction & History PRD / 截图 | 待补 |
| TXN-DETAIL-GAP-008 | GTR 与 FIAT_DEPOSIT 的映射 | GTR / WalletConnect PRD | 待补 |
| TXN-DETAIL-GAP-009 | WalletConnect 与 CRYPTO_DEPOSIT 的映射 | WalletConnect PRD | 待补 |
| TXN-DETAIL-GAP-010 | Risk Withheld 在详情页的展示和处理 | DTC / Wallet PRD / Notification | 待补 |

## 9. 来源引用

- (Ref: DTC Wallet OpenAPI Document20260126 / 4.2.4 Search Balance History)
- (Ref: DTC Wallet OpenAPI Document20260126 / Appendix ActivityType)
- (Ref: DTC Wallet OpenAPI Document20260126 / 3.4 Crypto Deposit)
- (Ref: knowledge-base/transaction/status-model.md / v1.1)
- (Ref: knowledge-base/transaction/history.md / v1.1)
- (Ref: knowledge-base/wallet/transaction-history.md / v1.1)
- (Ref: knowledge-base/wallet/deposit.md / v1.4)
- (Ref: knowledge-base/card/card-transaction-flow.md / v1.2)
- (Ref: knowledge-base/changelog/knowledge-gaps.md / deferred gaps)
