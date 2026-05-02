---
module: transaction
feature: history
version: "1.1"
status: active
source_doc: IMPLEMENTATION_PLAN.md；DTC接口文档/DTC Wallet OpenAPI Document20260126 (1).docx；knowledge-base/transaction/_index.md；knowledge-base/transaction/status-model.md；knowledge-base/card/card-transaction-flow.md；knowledge-base/wallet/transaction-history.md；knowledge-base/wallet/balance.md；knowledge-base/wallet/deposit.md；knowledge-base/changelog/knowledge-gaps.md
source_section: Transaction _index v1.0；Transaction Status Model v1.1；Wallet Transaction History v1.1；Wallet Balance v1.1；Wallet Deposit v1.4；Search Balance History / 4.2.4；Appendix ActivityType
last_updated: 2026-05-01
owner: 吴忆锋
depends_on:
  - transaction/_index
  - transaction/status-model
  - card/card-transaction-flow
  - wallet/transaction-history
  - wallet/balance
  - wallet/deposit
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
| Card Transaction Details | active | Card Transaction Flow | 详情字段在 `transaction/detail.md` 汇总 |
| Wallet Transaction History | active / 基础版 | Wallet Transaction History | 可引用 `id`、`transactionId`、`state`、`activityType` 等基础字段 |
| Wallet Search Balance History | active / 基础版 | DTC Wallet OpenAPI / 4.2.4 | 可引用 endpoint、查询字段、ActivityType、`relatedId`、`time`、`state` |
| Deposit History | active / 基础版 | Wallet Deposit / Wallet Transaction History | 可引用 Deposit success、Risk Withheld、ActivityType 边界；完整状态机待补 |
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
| Search Balance History | `[GET] /openapi/v1/wallet/balance/history/search` 查询 client wallet transaction history | DTC Wallet OpenAPI / 4.2.4 | Wallet 历史能力来源之一 |
| Request filter `currency` | 查询条件之一 | DTC Wallet OpenAPI / 4.2.4 | 前端是否暴露待补 |
| Request filter `type` | 查询条件之一，引用 ActivityType | DTC Wallet OpenAPI / 4.2.4 | 前端展示映射待补 |
| Request filter `yearMonth` / `createTimeStart` | 查询条件之一 | DTC Wallet OpenAPI / 4.2.4 | 完整时间规则待补 |
| `activityType` | ActivityType 分类字段 | DTC Wallet OpenAPI / Appendix ActivityType | 已确认部分枚举 |
| `relatedId` | Search Balance History 返回字段 | DTC Wallet OpenAPI / 4.2.4 | Card / GTR / WC 场景取值仍 deferred |
| `time` | Search Balance History 返回字段 | DTC Wallet OpenAPI / 4.2.4 | 时间格式待补 |

## 6. ActivityType 已确认枚举

| 枚举 | 值 | 含义 | Transaction History 处理 |
|---|---:|---|---|
| `FIAT_DEPOSIT` | 6 | Fiat Deposit | 可作为法币入金历史分类引用；是否对应 GTR 待确认 |
| `CRYPTO_DEPOSIT` | 10 | Stablecoin Deposit | 可作为 Crypto / WalletConnect 入金历史分类引用；是否对应 WC 待确认 |
| `DTC_WALLET` | 13 | DTC Wallet Payment | 可作为 DTC Wallet Payment 历史分类引用 |
| `CARD_PAYMENT_REFUND` | 20 | Card Payment Refund | 可作为 Card refund 入 Wallet 相关分类引用；与 Card 归集链路关联仍 deferred |

## 7. Deposit History 边界

| 场景 | 可引用事实 | 不得推导 |
|---|---|---|
| Deposit success | Notification PRD 有 `event=CRYPTO_TXN`、`type=DEPOSIT`、`state=success` 通知；DTC Crypto Deposit 加白后自动 success | 不得直接等同 Wallet `COMPLETED`；不代表余额立即可用 |
| Deposit Risk Withheld | DTC Crypto Deposit 未加白进入 `status=102 Risk Withheld`；Notification PRD 有 `state=RISK_WITHHELD` under review 通知 | 不得直接等同 Wallet `REJECTED`、`PENDING`、`PROCESSING` |
| GTR Deposit | Deposit 包含 GTR；`FIAT_DEPOSIT=6` 存在 | 不得写成 GTR 必然等同 FIAT_DEPOSIT |
| WalletConnect Deposit | Deposit 包含 WC；`CRYPTO_DEPOSIT=10` 存在；DTC Crypto Deposit 规则可引用 | 不得写成 WC 必然等同 CRYPTO_DEPOSIT |

## 8. Card History 与 Wallet History 边界

| 维度 | Card History | Wallet History | 处理 |
|---|---|---|---|
| 交易 ID | Card `Transaction ID` / DTC `data.id` | Wallet `id` / `transactionId` | 不等同，不混写 |
| 状态字段 | Card DTC transaction status / state 来源 | Wallet `state`；Deposit `Risk Withheld` / `success` | 并列引用，不合并 |
| 详情接口 | Card Transaction Detail Inquiry | Wallet Transaction Detail | `transaction/detail.md` 区分 |
| 历史接口 | `/openapi/v1/card/inquiry-card-transaction` | Wallet 交易记录 / Search Balance History | 不合并路径 |
| 筛选条件 | Type / Crypto / Date | Search Balance History 有 `currency` / `type` / time filters | 不将 Card 筛选条件套用到 Wallet |
| 展示字段 | Merchant、Crypto & Amount、Status、Created Date、Indicator | 待补 | 不将 Card 字段套用到 Wallet |
| 时间范围 | 近 1 年，单次最多 6 个月 | 待补 | 不将 Card 时间范围套用到 Wallet |

## 9. 不写入事实的内容

以下内容当前不得写成事实：

1. Card History 与 Wallet History 使用同一个接口。
2. Card `Transaction ID` 等同于 Wallet `transactionId`。
3. Wallet `relatedId` 等同于 Card `data.id`。
4. Wallet History 也支持 Card History 的 Type / Crypto / Date 筛选规则。
5. Wallet History 也限制最近 1 年、单次 6 个月。
6. Wallet History 展示字段与 Card History 完全一致。
7. Send / Swap History 是当前 active 交易历史。
8. Deposit / Receive 完整状态机已经闭环。
9. `FIAT_DEPOSIT` 必然等同 GTR。
10. `CRYPTO_DEPOSIT` 必然等同 WalletConnect。
11. Deposit success 必然等同 Wallet `COMPLETED`。
12. Risk Withheld 必然等同 Wallet `REJECTED`。

## 10. 待补项

| 编号 | 待补项 | 来源建议 | 当前处理 |
|---|---|---|---|
| TXN-HIS-GAP-001 | Wallet 交易记录完整请求字段 | DTC Wallet OpenAPI | 待补 |
| TXN-HIS-GAP-002 | Wallet 交易记录完整响应字段 | DTC Wallet OpenAPI | 待补 |
| TXN-HIS-GAP-003 | Wallet History 前端筛选条件 | Wallet PRD / DTC Wallet OpenAPI | 待补 |
| TXN-HIS-GAP-004 | Wallet History 时间范围 / 分页规则 | Wallet PRD / DTC Wallet OpenAPI | 待补 |
| TXN-HIS-GAP-005 | Wallet History 展示字段 | Wallet PRD / 截图 | 待补 |
| TXN-HIS-GAP-006 | GTR 与 `FIAT_DEPOSIT` 映射 | GTR PRD / 产品确认 | 待补 |
| TXN-HIS-GAP-007 | WalletConnect 与 `CRYPTO_DEPOSIT` 映射 | WC PRD / 产品确认 | 待补 |
| TXN-HIS-GAP-008 | `relatedId` 在 GTR / WC / Card 归集场景下取值 | DTC / 后端确认 | deferred |
| TXN-HIS-GAP-009 | Receive 是否进入 Wallet History | Receive PRD / 产品确认 | 待补 |
| TXN-HIS-GAP-010 | Card / Wallet 历史是否需要统一入口 | 产品确认 / UX | 待补 |

## 11. 来源引用

- (Ref: DTC Wallet OpenAPI Document20260126 / 4.2.4 Search Balance History)
- (Ref: DTC Wallet OpenAPI Document20260126 / Appendix ActivityType)
- (Ref: DTC Wallet OpenAPI Document20260126 / 3.4 Crypto Deposit)
- (Ref: knowledge-base/transaction/status-model.md / v1.1)
- (Ref: knowledge-base/wallet/transaction-history.md / v1.1)
- (Ref: knowledge-base/wallet/balance.md / v1.1)
- (Ref: knowledge-base/wallet/deposit.md / v1.4)
- (Ref: knowledge-base/card/card-transaction-flow.md / v1.2)
- (Ref: knowledge-base/changelog/knowledge-gaps.md / deferred gaps)
