---
module: transaction
feature: transaction-stage-review
version: "1.0"
status: active
source_doc: IMPLEMENTATION_PLAN.md；knowledge-base/transaction/_index.md；knowledge-base/transaction/status-model.md；knowledge-base/transaction/history.md；knowledge-base/transaction/detail.md；knowledge-base/card/card-transaction-flow.md；knowledge-base/wallet/stage-review.md；knowledge-base/changelog/knowledge-gaps.md
source_section: Transaction 阶段回扫；IMPLEMENTATION_PLAN v3.9；Transaction _index v1.0；Status Model v1.0；History v1.0；Detail v1.0
last_updated: 2026-05-01
owner: 吴忆锋
depends_on:
  - transaction/_index
  - transaction/status-model
  - transaction/history
  - transaction/detail
  - card/card-transaction-flow
  - wallet/stage-review
  - changelog/knowledge-gaps
---

# Transaction 阶段回扫记录

## 1. 回扫结论

Transaction 统一层已完成基础版知识库沉淀，阶段结果为：`PARTIAL PASS`。

含义：

- 已建立 Card / Wallet 交易状态、交易历史、交易详情的统一边界。
- 已明确 Card 与 Wallet 状态不强行合并。
- 已明确 Card Transaction ID、Wallet `transactionId`、Wallet `id`、Wallet `relatedId` 不得混写。
- Send / Swap 继续保持 `deferred`，不进入 active Transaction 统一层。
- Deposit active，但 GTR / WalletConnect 的完整状态、风控、通知仍待补。
- 可以进入 Common / Integration 阶段，但不得把 Transaction 待补项写成事实。

## 2. 回扫范围

| 文件 | 状态 | 回扫结果 |
|---|---|---|
| `transaction/_index.md` | active | 已建立 Transaction 统一层边界 |
| `transaction/status-model.md` | active | 已汇总 Card / Wallet 已确认状态来源，未强行合并状态机 |
| `transaction/history.md` | active | 已区分 Card History 与 Wallet Transaction History |
| `transaction/detail.md` | active | 已区分 Card Detail 与 Wallet Detail 字段边界 |

## 3. 已通过项

| 检查项 | 结果 | 说明 |
|---|---|---|
| 模块边界 | 通过 | Transaction 不重写 Card / Wallet 流程，只做统一引用层 |
| 状态来源 | 通过 | Card / Wallet 状态来源已分开记录 |
| 状态合并控制 | 通过 | 未将 Card 状态与 Wallet `state` 强行等价 |
| History 边界 | 通过 | Card History 与 Wallet History 已分开 |
| Detail 边界 | 通过 | Card Detail 与 Wallet Detail 已分开 |
| ID 口径隔离 | 通过 | 未将 Card `data.id`、Wallet `transactionId`、Wallet `id`、`relatedId` 写成同一字段 |
| 未上线功能隔离 | 通过 | Send / Swap 保持 deferred |
| deferred gaps 隔离 | 通过 | 未把 Card / Wallet 遗留资金追踪问题写成事实 |

## 4. 当前待补问题

| 编号 | 问题 | 影响 | 当前处理 |
|---|---|---|---|
| TXN-GAP-001 | Wallet `activityType` 枚举未补齐 | Wallet 交易分类与展示口径不完整 | 待补 |
| TXN-GAP-002 | Wallet `state` 进入 / 退出条件未补齐 | Wallet 状态机不完整 | 待补 |
| TXN-GAP-003 | Wallet 状态与前端展示文案映射未确认 | 用户展示口径不完整 | 待补 |
| TXN-GAP-004 | GTR Deposit 状态映射未补齐 | GTR 入金历史与详情不完整 | 待补 |
| TXN-GAP-005 | WalletConnect Deposit 状态映射未补齐 | WC 入金历史与详情不完整 | 待补 |
| TXN-GAP-006 | Receive 是否独立上线及状态映射未确认 | Receive 交易历史边界不完整 | 待补 |
| TXN-GAP-007 | Wallet History 完整请求 / 响应字段未补齐 | Wallet History 事实源不完整 | 待补 |
| TXN-GAP-008 | Wallet Detail 完整请求 / 响应字段未补齐 | Wallet Detail 事实源不完整 | 待补 |
| TXN-GAP-009 | Card Detail 前端展示字段完整列表待补 | Card Detail 展示层不完整 | 待补 |
| TXN-GAP-010 | Card / Wallet 是否需要统一交易入口未确认 | 产品信息架构不完整 | 待补 |
| TXN-GAP-011 | Card Transaction Flow 资金追踪 deferred gaps 未回填 | 资金追踪不可完整闭环 | deferred |
| TXN-GAP-012 | Wallet relatedId 与 Card / Deposit / Wallet 交易的关联规则未确认 | 对账链路不完整 | deferred |

## 5. 阶段判断

| 判断项 | 结论 |
|---|---|
| Transaction 模块边界 | PASS |
| Status Model | PARTIAL PASS |
| History | PARTIAL PASS |
| Detail | PARTIAL PASS |
| Send / Swap deferred 隔离 | PASS |
| ID 口径隔离 | PASS |
| 资金追踪完整闭环 | DEFERRED |
| 是否允许进入 Common / Integration | 允许，带待补项继续 |
| 是否允许把待补项写成事实 | 不允许 |

## 6. 后续要求

1. Common / Integration 阶段可引用 Transaction 已确认边界。
2. 不得将 Card 与 Wallet 状态强行合并为统一状态机。
3. 不得将 Card `data.id`、Wallet `transactionId`、Wallet `id`、Wallet `relatedId` 写成同一字段。
4. 不得把 Send / Swap 写成 active 交易类型。
5. 后续如拿到 Wallet / DTC / 产品确认材料，应优先回填：
   - Wallet `activityType` 枚举
   - Wallet `state` 进入 / 退出条件
   - GTR / WalletConnect 状态映射
   - Wallet History / Detail 完整字段
   - Card / Wallet 统一入口产品口径
6. Card / Wallet 资金追踪 deferred gaps 继续保留，直到后端 / Wallet / 账务确认。

## 7. 来源引用

- (Ref: IMPLEMENTATION_PLAN.md / v3.9 / Transaction 统一层)
- (Ref: knowledge-base/transaction/_index.md / v1.0)
- (Ref: knowledge-base/transaction/status-model.md / v1.0)
- (Ref: knowledge-base/transaction/history.md / v1.0)
- (Ref: knowledge-base/transaction/detail.md / v1.0)
- (Ref: knowledge-base/card/card-transaction-flow.md / v1.2)
- (Ref: knowledge-base/wallet/stage-review.md / v1.0)
- (Ref: knowledge-base/changelog/knowledge-gaps.md / deferred gaps)
