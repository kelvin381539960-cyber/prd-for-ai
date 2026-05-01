---
module: card
feature: card-stage-review
version: "1.3"
status: active
source_doc: IMPLEMENTATION_PLAN.md；knowledge-base/card/_index.md；knowledge-base/card/card-transaction-flow.md；knowledge-base/card/transaction-flow-traceability-checklist.md；knowledge-base/changelog/knowledge-gaps.md；用户确认结论 2026-05-01
source_section: Card 阶段回扫；Card Transaction Flow v1.2；Traceability Checklist v1.5；deferred gaps decision
last_updated: 2026-05-01
owner: 吴忆锋
depends_on:
  - card/_index
  - card/application
  - card/card-status-and-fields
  - card/card-home
  - card/activation
  - card/pin
  - card/sensitive-info
  - card/card-management
  - card/card-transaction-flow
  - card/transaction-flow-traceability-checklist
  - changelog/knowledge-gaps
---

# Card 阶段回扫记录

## 1. 回扫结论

Card 模块主文件已完成。Card Transaction Flow 中仍存在资金可追溯遗留缺口，但经用户确认，当前这些问题暂无答案，先作为 `deferred gap` 记录，不继续阻塞其他知识库转译任务。

本次 Gate 结果调整为：`PARTIAL PASS`。

含义：

- Card 页面类、卡管理类、交易展示类知识库可视为阶段完成。
- Card Transaction Flow 的资金追踪链路仍不是完整闭环。
- 允许继续推进后续 Wallet / Transaction / Common 等知识库转译。
- 禁止把 deferred gap 写成事实；后续拿到后端 / Wallet / 账务答案后必须回填。

## 2. 已确认并沉淀的事项

| 项目 | 结论 | 来源 |
|---|---|---|
| DTC 卡交易通知字段 | `Card Transaction Notify` 字段表已明确 | DTC Card Issuing / 3.4.4 |
| DTC 卡交易 ID | `data.id` 为 Transaction ID | DTC Card Issuing / 3.4.4 |
| 重复通知 | 重复推送时 Transaction ID 不变 | 用户确认 2026-05-01 |
| 独立 notification id | 无独立 notification id | 用户确认 2026-05-01 |
| 自动归集触发类型 | 仅 refund / reversal / deposit；Top-up 不触发 | 用户确认 2026-05-01 |
| 查余额接口 | `[POST] /openapi/v1/card/inquiry-card-info` | DTC Card Issuing / 3.2.15 |
| transfer-to-wallet | `[POST] /openapi/v1/card/transfer-to-wallet`，请求字段为 `cardId`、`amount` | DTC Card Issuing / 3.3.3 |
| transfer 成功响应 | 只返回 `header.success=true`，不返回归集业务流水 | DTC Card Issuing / 3.3.3；用户确认 |
| 归集失败策略 | 不自动重试，告警监控群 | 用户确认 2026-05-01 |
| Wallet 交易 ID | 钱包交易记录 / 详情出参均包含 `id`，Long，交易 id | DTC Wallet OpenAPI；用户确认 |
| Wallet 交易详情入参 | `transactionId`，Unique transaction ID from DTC | DTC Wallet OpenAPI；用户确认 |
| Wallet 交易状态 | `state = PENDING / PROCESSING / AUTHORIZED / COMPLETED / REJECTED / CLOSED` | DTC Wallet OpenAPI；用户确认 |

## 3. Deferred gaps

以下问题暂时没有答案，转入 `knowledge-gaps.md` 长期记录，不再阻塞继续推进。

| 编号 | 问题 | 当前处理 |
|---|---|---|
| CARD-DEFER-BE-001 | AIX 是否生成内部交易处理 ID，字段名是什么 | deferred gap |
| CARD-DEFER-BE-002 | DTC Webhook 原始报文是否完整落库 | deferred gap |
| CARD-DEFER-BE-003 | 后端是否按 `event + data.id` 去重 | deferred gap |
| CARD-DEFER-BE-004 | 归集触发是否还需判断 `state` / `indicator` | deferred gap |
| CARD-DEFER-BE-005 | AIX 是否生成归集请求 ID，字段名是什么 | deferred gap |
| CARD-DEFER-BE-006 | `D-REQUEST-ID` 如何生成、保存，并与归集请求 ID 关联 | deferred gap |
| CARD-DEFER-BE-007 | DTC `data.id`、AIX 内部交易处理 ID、归集请求 ID、`D-REQUEST-ID`、Wallet 交易 `id` 之间如何串联 | deferred gap |
| CARD-DEFER-BE-008 | 查询 balance 失败如何处理 | deferred gap |
| CARD-DEFER-BE-009 | 归集失败告警后是否有后台人工补偿入口 | deferred gap |
| CARD-DEFER-BE-010 | 其他失败类型和责任分派 | deferred gap |
| CARD-DEFER-WALLET-001 | Wallet 交易 `id` 如何关联 DTC `data.id`、AIX 归集请求 ID 或 `D-REQUEST-ID` | deferred gap |
| CARD-DEFER-WALLET-002 | Wallet `Search Balance History.relatedId` 在卡余额转 Wallet 场景下取哪个 ID | deferred gap |
| CARD-DEFER-WALLET-003 | card balance 转 Wallet 后，入账币种是否与 card currency 完全一致 | deferred gap |
| CARD-DEFER-WALLET-004 | 最终对账字段组合 | deferred gap |

## 4. 阶段判断

| 判断项 | 结论 |
|---|---|
| Card 页面类能力 | PASS |
| Card 状态与字段事实源 | PASS |
| Card 管理类能力 | PASS |
| Card 交易展示 | PASS |
| Card Transaction Flow 基础事实 | PARTIAL PASS |
| Card 资金可追溯链路 | DEFERRED |
| 是否允许继续后续知识库转译 | 允许 |
| 是否允许把 deferred gaps 写成事实 | 不允许 |

## 5. 后续要求

1. 后续 Wallet / Transaction 阶段可以继续推进。
2. 涉及 Card Transaction Flow 遗留问题时，只能引用为 `deferred gap`，不能补写事实。
3. 拿到后端 / Wallet / 账务明确答案后，需要回填：
   - `knowledge-base/card/card-transaction-flow.md`
   - `knowledge-base/card/transaction-flow-traceability-checklist.md`
   - `knowledge-base/changelog/knowledge-gaps.md`
   - `knowledge-base/card/stage-review.md`
   - `IMPLEMENTATION_PLAN.md`

## 6. 来源引用

- (Ref: IMPLEMENTATION_PLAN.md / v3.5 / Stage Review Gate)
- (Ref: knowledge-base/card/card-transaction-flow.md / v1.2)
- (Ref: knowledge-base/card/transaction-flow-traceability-checklist.md / v1.5)
- (Ref: knowledge-base/changelog/knowledge-gaps.md / Card Transaction Flow deferred gaps)
- (Ref: 用户确认结论 / 2026-05-01)
