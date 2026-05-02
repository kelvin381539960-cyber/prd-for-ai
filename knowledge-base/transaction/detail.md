---
module: transaction
feature: detail
version: "1.0"
status: active
source_doc: IMPLEMENTATION_PLAN.md；knowledge-base/transaction/_index.md；knowledge-base/transaction/status-model.md；knowledge-base/transaction/history.md；knowledge-base/card/card-transaction-flow.md；knowledge-base/wallet/transaction-history.md；knowledge-base/wallet/stage-review.md；knowledge-base/changelog/knowledge-gaps.md
source_section: Transaction _index v1.0；Transaction Status Model v1.0；Transaction History v1.0；Card Transaction Flow v1.2；Wallet Transaction History v1.0
last_updated: 2026-05-01
owner: 吴忆锋
depends_on:
  - transaction/_index
  - transaction/status-model
  - transaction/history
  - card/card-transaction-flow
  - wallet/transaction-history
  - wallet/stage-review
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
| Wallet Transaction Detail | active / 基础版 | Wallet Transaction History | 可引用 `transactionId` 入参和 `id` 出参 |
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

Card Detail 字段应优先引用 Card Transaction Flow 和 DTC Card Issuing 已确认内容。

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

### 4.1 Wallet Detail 可引用字段

当前 Wallet Detail 仅能引用已确认基础字段：

| 字段 / 信息 | 当前处理 |
|---|---|
| `transactionId` | 详情查询入参，Unique transaction ID from DTC |
| `id` | Wallet 交易记录 / 详情出参中的 Long 交易 id |
| `state` | Wallet 交易状态字段 |
| `activityType` | Search Balance History 返回字段，枚举待补 |
| `relatedId` | Search Balance History 返回字段，关联口径待补 |
| `time` | Search Balance History 返回字段，格式待补 |

## 5. Card Detail 与 Wallet Detail 边界

| 维度 | Card Detail | Wallet Detail | 处理 |
|---|---|---|---|
| 查询入参 | Card Transaction ID | Wallet `transactionId` | 不等同 |
| 交易 ID | DTC Card `data.id` | Wallet `id` / `transactionId` | 不合并 |
| 状态字段 | Card DTC transaction status / state 来源 | Wallet `state` | 并列引用 |
| 详情接口 | Card Transaction Detail Inquiry | Wallet Transaction Detail | 不合并接口 |
| 复制字段 | Card Transaction ID 支持复制 | Wallet 是否支持复制待补 | 不套用 Card 规则 |
| 时间字段 | Card 有多个交易时间字段 | Wallet `time` 已知，其他待补 | 不混写 |

## 6. 不写入事实的内容

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

## 7. 待补项

| 编号 | 待补项 | 来源建议 | 当前处理 |
|---|---|---|---|
| TXN-DETAIL-GAP-001 | Wallet Transaction Detail 完整请求字段 | DTC Wallet OpenAPI | 待补 |
| TXN-DETAIL-GAP-002 | Wallet Transaction Detail 完整响应字段 | DTC Wallet OpenAPI | 待补 |
| TXN-DETAIL-GAP-003 | Wallet Detail 页面展示字段 | Wallet PRD / 截图 | 待补 |
| TXN-DETAIL-GAP-004 | Wallet Detail 是否支持复制交易 ID | Wallet PRD / 截图 | 待补 |
| TXN-DETAIL-GAP-005 | Wallet `transactionId` 与交易记录 `id` 的关系 | DTC Wallet OpenAPI / 后端确认 | 待补 |
| TXN-DETAIL-GAP-006 | Wallet `relatedId` 关联规则 | DTC Wallet OpenAPI / 后端确认 | deferred / 待补 |
| TXN-DETAIL-GAP-007 | Card Detail 前端展示字段完整列表 | Transaction & History PRD / 截图 | 待补 |
| TXN-DETAIL-GAP-008 | Deposit GTR / WalletConnect Detail 字段差异 | GTR / WalletConnect PRD | 待补 |

## 8. 与其他 Transaction 文件关系

| 文件 | 关系 |
|---|---|
| `transaction/status-model.md` | 提供 Card / Wallet 状态来源边界 |
| `transaction/history.md` | 提供 Card / Wallet 历史记录入口和列表边界 |
| `transaction/detail.md` | 当前文件，聚焦详情入口、入参、字段边界 |
| `transaction/stage-review.md` | 后续检查详情字段来源和 deferred gaps 隔离 |

## 9. 来源引用

- (Ref: IMPLEMENTATION_PLAN.md / v3.9 / Transaction 统一层)
- (Ref: knowledge-base/transaction/_index.md / v1.0)
- (Ref: knowledge-base/transaction/status-model.md / v1.0)
- (Ref: knowledge-base/transaction/history.md / v1.0)
- (Ref: knowledge-base/card/card-transaction-flow.md / v1.2)
- (Ref: knowledge-base/wallet/transaction-history.md / v1.0)
- (Ref: knowledge-base/wallet/stage-review.md / v1.0)
- (Ref: knowledge-base/changelog/knowledge-gaps.md / Card Transaction Flow deferred gaps)
