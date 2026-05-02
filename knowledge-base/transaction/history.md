---
module: transaction
feature: history
version: "1.0"
status: active
source_doc: IMPLEMENTATION_PLAN.md；knowledge-base/transaction/_index.md；knowledge-base/transaction/status-model.md；knowledge-base/card/card-transaction-flow.md；knowledge-base/wallet/transaction-history.md；knowledge-base/wallet/stage-review.md；knowledge-base/changelog/knowledge-gaps.md
source_section: Transaction _index v1.0；Transaction Status Model v1.0；Card Transaction Flow v1.2；Wallet Transaction History v1.0；Wallet Stage Review v1.0
last_updated: 2026-05-01
owner: 吴忆锋
depends_on:
  - transaction/_index
  - transaction/status-model
  - card/card-transaction-flow
  - wallet/transaction-history
  - wallet/stage-review
  - changelog/knowledge-gaps
---

# Transaction History 交易历史

## 1. 功能定位

Transaction History 用于统一沉淀 AIX 中 Card History 与 Wallet Transaction History 的边界、入口、查询字段和展示限制。

本文件不是全局交易流水表设计，不合并 Card / Wallet 字段来源，不补写未确认状态机。

## 2. 历史记录类型

| 历史类型 | 当前状态 | 来源 | 处理 |
|---|---|---|---|
| Card History | active | Card Transaction Flow | 可引用已确认字段和规则 |
| Card Home Recent Transactions | active | Card Transaction Flow | 作为 Card 首页交易摘要入口 |
| Card Transaction Details | active | Card Transaction Flow | 详情字段后续在 `transaction/detail.md` 汇总 |
| Wallet Transaction History | active / 基础版 | Wallet Transaction History | 可引用 `id`、`transactionId`、`state` 等基础字段 |
| Wallet Search Balance History | active / 基础版 | Wallet Transaction History | 可引用 `activityType`、`relatedId`、`time`、`state`，但枚举待补 |
| Send / Swap History | deferred | Wallet Stage Review | 当前不纳入 active Transaction History |

## 3. Card History 已确认规则

| 规则 | 当前结论 | 来源 |
|---|---|---|
| 数据范围 | 可查看最近 1 年内卡交易数据 | Card Transaction Flow / Transaction & History PRD |
| 单次查询范围 | 单次最多查询 6 个月 | Card Transaction Flow / Transaction & History PRD |
| 默认查询 | 默认按当前月份查询，默认显示最新 10 条 | Card Transaction Flow / Transaction & History PRD |
| 分页 | 每页 10 条，滑动加载更多 | Card Transaction Flow / Transaction & History PRD |
| 筛选 | 支持按 Type、Crypto、Date 组合筛选 | Card Transaction Flow / Transaction & History PRD |
| 过滤 | 需过滤 TOP_UP 和 REVERSAL_TO_ACCOUNT 类型 | Card Transaction Flow / Transaction & History PRD |
| 详情入口 | 点击单条记录进入 Transaction Details | Card Transaction Flow / Transaction & History PRD |

## 4. Card Home Recent Transactions 已确认规则

| 规则 | 当前结论 | 来源 |
|---|---|---|
| 展示条数 | Card Home 展示最近 3 条卡交易记录 | Card Transaction Flow / Application PRD |
| 接口 | 进入页面调用 `/openapi/v1/card/inquiry-card-transaction` | Card Transaction Flow / DTC Card Issuing |
| 空态 | 无交易数据时展示占位符 | Card Transaction Flow / Application PRD |
| 排序 | 有交易数据时按交易时间降序排列 | Card Transaction Flow / Application PRD |
| 展示字段 | 展示 Merchant name、Crypto & Amount、Status、Created Date、Indicator | Card Transaction Flow / Application PRD |

## 5. Wallet Transaction History 已确认规则

| 规则 / 字段 | 当前结论 | 来源 | 备注 |
|---|---|---|---|
| Wallet 交易记录能力 | 存在 Wallet 交易记录能力 | Wallet Transaction History | 完整请求 / 响应字段待补 |
| Wallet 交易详情能力 | 存在 Wallet 交易详情能力 | Wallet Transaction History | 入参为 `transactionId` |
| `id` | Wallet 交易记录 / 详情出参均包含 `id`，Long，交易 id | Wallet Transaction History | 可作为 Wallet 交易基础 ID |
| `transactionId` | 单笔 Wallet 交易详情入参，Unique transaction ID from DTC | Wallet Transaction History | 不等同于 Card `data.id` |
| `state` | Wallet 交易状态字段 | Wallet Transaction History | 枚举引用 `transaction/status-model.md` |
| Search Balance History | 可查询 Wallet 交易 / 余额历史 | Wallet Transaction History | 字段待补 |
| `activityType` | Search Balance History 返回字段 | Wallet Transaction History | 枚举待补 |
| `relatedId` | Search Balance History 返回字段 | Wallet Transaction History | Card balance 转 Wallet 场景取值 deferred |
| `time` | Search Balance History 返回字段 | Wallet Transaction History | 时间格式待补 |

## 6. Card History 与 Wallet History 边界

| 维度 | Card History | Wallet History | 处理 |
|---|---|---|---|
| 交易 ID | Card `Transaction ID` / DTC `data.id` | Wallet `id` / `transactionId` | 不等同，不混写 |
| 状态字段 | Card DTC transaction status / state 来源 | Wallet `state` | 并列引用，不合并 |
| 详情接口 | Card Transaction Detail Inquiry | Wallet Transaction Detail | 后续 `transaction/detail.md` 区分 |
| 历史接口 | `/openapi/v1/card/inquiry-card-transaction` | Wallet 交易记录 / Search Balance History | 不合并路径 |
| 筛选条件 | Type / Crypto / Date | 待补 | 不将 Card 筛选条件套用到 Wallet |
| 展示字段 | Merchant、Crypto & Amount、Status、Created Date、Indicator | 待补 | 不将 Card 字段套用到 Wallet |
| 时间范围 | 近 1 年，单次最多 6 个月 | 待补 | 不将 Card 时间范围套用到 Wallet |

## 7. 不写入事实的内容

以下内容当前不得写成事实：

1. Card History 与 Wallet History 使用同一个接口。
2. Card `Transaction ID` 等同于 Wallet `transactionId`。
3. Wallet `relatedId` 等同于 Card `data.id`。
4. Wallet History 也支持 Card History 的 Type / Crypto / Date 筛选规则。
5. Wallet History 也限制最近 1 年、单次 6 个月。
6. Wallet History 展示字段与 Card History 完全一致。
7. Send / Swap History 是当前 active 交易历史。
8. Deposit / Receive 完整状态机已经闭环。

## 8. 待补项

| 编号 | 待补项 | 来源建议 | 当前处理 |
|---|---|---|---|
| TXN-HIS-GAP-001 | Wallet 交易记录完整请求字段 | DTC Wallet OpenAPI | 待补 |
| TXN-HIS-GAP-002 | Wallet 交易记录完整响应字段 | DTC Wallet OpenAPI | 待补 |
| TXN-HIS-GAP-003 | Wallet History 筛选条件 | Wallet PRD / DTC Wallet OpenAPI | 待补 |
| TXN-HIS-GAP-004 | Wallet History 时间范围 / 分页规则 | Wallet PRD / DTC Wallet OpenAPI | 待补 |
| TXN-HIS-GAP-005 | Wallet History 展示字段 | Wallet PRD / 截图 | 待补 |
| TXN-HIS-GAP-006 | Deposit GTR / WalletConnect 历史记录分类 | GTR / WalletConnect PRD | 待补 |
| TXN-HIS-GAP-007 | Receive 是否进入 Wallet History | Receive PRD / 产品确认 | 待补 |
| TXN-HIS-GAP-008 | Card / Wallet 历史是否需要统一入口 | 产品确认 / UX | 待补 |

## 9. 与后续 Detail 文件关系

`transaction/detail.md` 应在本文基础上继续拆分：

| 详情类型 | 处理 |
|---|---|
| Card Transaction Detail | 引用 Card Transaction Flow 中的 Card Transaction Detail Inquiry |
| Wallet Transaction Detail | 引用 Wallet Transaction History 中的 `transactionId` 入参和 `id` 出参 |
| Card / Wallet 字段对照 | 只做来源对照，不做字段等价合并 |

## 10. 来源引用

- (Ref: IMPLEMENTATION_PLAN.md / v3.9 / Transaction 统一层)
- (Ref: knowledge-base/transaction/_index.md / v1.0)
- (Ref: knowledge-base/transaction/status-model.md / v1.0)
- (Ref: knowledge-base/card/card-transaction-flow.md / v1.2)
- (Ref: knowledge-base/wallet/transaction-history.md / v1.0)
- (Ref: knowledge-base/wallet/stage-review.md / v1.0)
- (Ref: knowledge-base/changelog/knowledge-gaps.md / Card Transaction Flow deferred gaps)
