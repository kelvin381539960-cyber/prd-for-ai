---
module: card
feature: card-stage-review
version: "1.4"
status: active
source_doc: IMPLEMENTATION_PLAN.md；knowledge-base/card/_index.md；knowledge-base/card/card-transaction-flow.md；knowledge-base/card/transaction-flow-traceability-checklist.md；knowledge-base/transaction/reconciliation.md；knowledge-base/changelog/knowledge-gaps.md；用户确认结论 2026-05-01；用户确认结论 2026-05-02
source_section: Card 阶段回扫；Card Transaction Flow；Traceability Checklist；Transaction Reconciliation；ALL-GAP 唯一总表
last_updated: 2026-05-02
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
  - transaction/reconciliation
  - changelog/knowledge-gaps
---

# Card 阶段回扫记录

## 1. 回扫结论

Card 模块主文件已完成。Card Transaction Flow 中仍存在资金可追溯遗留缺口，但经用户确认，当前这些问题暂无答案，先作为 ALL-GAP `deferred` 记录，不继续阻塞其他知识库转译任务。

本次 Gate 结果为：`PARTIAL PASS`。

含义：

- Card 页面类、卡管理类、交易展示类知识库可视为阶段完成。
- Card Transaction Flow 的资金追踪链路仍不是完整闭环。
- 资金追踪 / ID 链路 / 对账边界已由 `transaction/reconciliation.md` 承接。
- 允许继续推进后续 Wallet / Transaction / Common / KYC 等知识库转译。
- 禁止把 ALL-GAP deferred 项写成事实；后续拿到后端 / Wallet / 账务答案后必须回填。

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

## 3. 当前 ALL-GAP 引用

Card 阶段不维护独立 deferred checklist。相关资金追踪问题统一引用：

| 编号 | 主题 | 当前处理 |
|---|---|---|
| ALL-GAP-017 | Card Transaction / refund / reversal / deposit 与 Wallet Transaction 是否存在一一对应关系 | deferred |
| ALL-GAP-018 | 如果存在关联，具体用哪个字段关联 | deferred |
| ALL-GAP-019 | AIX 收到 DTC Card Transaction Notify 后是否生成内部交易处理 ID | deferred |
| ALL-GAP-020 | AIX 发起 Transfer Balance to Wallet 前是否生成归集请求 ID | deferred |
| ALL-GAP-021 | `D-REQUEST-ID` 是否仅是请求唯一标识，还是也承担幂等 / 重试去重作用 | deferred |
| ALL-GAP-022 | DTC Webhook 原始报文是否完整落库，是否可回放 / 查询 | deferred |
| ALL-GAP-023 | 重复通知实际如何去重，是否按 `event + data.id` | deferred |
| ALL-GAP-024 | 自动归集触发是否只依赖 `type=refund/reversal/deposit`，还是还需要判断 state / indicator / amount | deferred |
| ALL-GAP-025 | 查询 Card balance 失败后如何处理 | deferred |
| ALL-GAP-026 | Transfer Balance to Wallet 失败后是否只有告警，是否存在后台人工补偿入口 | deferred |
| ALL-GAP-027 | DTC transfer 成功但 Wallet 未入账是否有系统对账 / 告警机制 | deferred |
| ALL-GAP-028 | Card balance 转 Wallet 后，入账币种是否与 card currency 完全一致 | deferred |
| ALL-GAP-029 | 财务 / 运营最终使用哪些字段串起全链路 | deferred |
| ALL-GAP-036 | Webhook 原始报文落库规则 | deferred |

## 4. 阶段判断

| 判断项 | 结论 |
|---|---|
| Card 页面类能力 | PASS |
| Card 状态与字段事实源 | PASS |
| Card 管理类能力 | PASS |
| Card 交易展示 | PASS |
| Card Transaction Flow 基础事实 | PARTIAL PASS |
| Card 资金可追溯链路 | DEFERRED / 见 ALL-GAP P0 |
| Reconciliation 边界 | 已迁入 `transaction/reconciliation.md` |
| ALL-GAP 唯一源 | PASS |
| 是否允许继续后续知识库转译 | 允许 |
| 是否允许把 ALL-GAP 写成事实 | 不允许 |

## 5. 后续要求

1. 后续 Wallet / Transaction / Common / KYC 阶段可以继续推进。
2. 涉及 Card Transaction Flow 遗留问题时，只能引用 ALL-GAP 编号，不能补写事实。
3. 拿到后端 / Wallet / 账务明确答案后，需要回填：
   - `knowledge-base/card/card-transaction-flow.md`
   - `knowledge-base/transaction/reconciliation.md`
   - `knowledge-base/changelog/knowledge-gaps.md`
   - `knowledge-base/card/stage-review.md`
   - `IMPLEMENTATION_PLAN.md`
4. Card 模块不得再维护独立 checklist / TODO / gaps 表。

## 6. 来源引用

- (Ref: IMPLEMENTATION_PLAN.md / v4.6)
- (Ref: knowledge-base/card/card-transaction-flow.md)
- (Ref: knowledge-base/card/transaction-flow-traceability-checklist.md)
- (Ref: knowledge-base/transaction/reconciliation.md / v1.0)
- (Ref: knowledge-base/changelog/knowledge-gaps.md / ALL-GAP 总表)
- (Ref: 用户确认结论 / 2026-05-01)
- (Ref: 用户确认结论 / 2026-05-02 / ALL-GAP 唯一总表)
