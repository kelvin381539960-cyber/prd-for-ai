---
module: card
feature: card-stage-review
version: "1.1"
status: active
source_doc: IMPLEMENTATION_PLAN.md；knowledge-base/card/_index.md；knowledge-base/card/card-transaction-flow.md；knowledge-base/card/transaction-flow-traceability-checklist.md；knowledge-base/changelog/knowledge-gaps.md
source_section: Card 阶段回扫；Card Transaction Flow v1.1；Traceability Checklist v1.4
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

Card 模块主文件已完成，但当前仍不允许进入 Wallet 批量推进。

本轮已根据 DTC Card Issuing API、DTC Wallet API、Notification PRD、卡交易&钱包交易状态梳理以及用户确认结论，消除一批原阻塞项：DTC 通知字段表、DTC 卡交易 ID、重复通知 ID 规则、自动归集触发类型、Transfer Balance to Wallet 请求字段、Transfer 成功不返回归集业务流水、失败不自动重试、用户通知与 Wallet 展示边界等已明确。

当前 Card 阶段 Gate 结果仍为 `BLOCK`。阻塞原因已从“DTC 字段与接口不明确”收敛为：AIX 内部交易处理 ID、AIX 归集请求 ID、D-REQUEST-ID 保存与关联规则、Wallet 入账流水、Wallet relatedId、查询余额失败处理、人工补偿入口和最终对账字段组合未闭环。

## 2. 回扫范围

| 文件 | 状态 | 回扫结果 |
|---|---|---|
| `_index.md` | active | 功能清单已收口 |
| `application.md` | active | 申卡流程已完成，资金字段缺口已记录 |
| `card-status-and-fields.md` | active | 状态与字段事实源已建立 |
| `card-home.md` | active | 首页展示与入口已完成 |
| `activation.md` | active | 实体卡激活已完成 |
| `pin.md` | active | PIN 能力已完成 |
| `sensitive-info.md` | active | 卡信息安全查看已完成 |
| `card-management.md` | active | 卡管理能力已完成 |
| `card-transaction-flow.md` | active | 已同步本轮确认结果，但资金可追溯链路仍未闭环 |
| `transaction-flow-traceability-checklist.md` | active | 已收敛为后端 / Wallet / 账务待确认问题 |

## 3. 已通过项

| 检查项 | 结果 | 说明 |
|---|---|---|
| 模块边界 | 通过 | Card 与 Security、Wallet、Transaction 边界基本清晰 |
| 状态引用 | 通过 | 后续文件均要求引用 `card-status-and-fields.md` |
| 页面入口 | 通过 | Card Home、Activation、PIN、Sensitive Info、Management 入口已拆分 |
| Security 复用 | 通过 | Face Authentication、OTP、设备认证均引用 Security，不重复定义 |
| 无来源补写 | 通过 | 本轮新增事实均来自 DTC 接口文档、Notification PRD、状态梳理表或用户确认 |
| DTC 通知字段 | 通过 | `Card Transaction Notify` 字段表已明确，`data.id` 为 DTC Transaction ID |
| 通知去重基础 | 部分通过 | 用户确认重复推送 Transaction ID 不变，且无独立 notification id；后端实现仍待确认 |
| 自动归集触发范围 | 通过 | 仅 refund / reversal / deposit 触发；Top-up 已移除 |
| Transfer 请求字段 | 通过 | `transfer-to-wallet` 请求字段为 `cardId`、`amount` |
| Transfer 失败策略 | 部分通过 | 已确认失败不自动重试、告警监控群；人工补偿入口待确认 |

## 4. 已消除的原阻塞项

| 原阻塞项 | 当前结论 | 来源 |
|---|---|---|
| Card Transaction Notification 字段表未明确 | 已明确，DTC 文档提供 `Card Transaction Notify` 字段表 | DTC Card Issuing / 3.4.4 |
| Card Transaction Notification 原始交易 ID 未明确 | 已明确：`data.id` 为 Transaction ID，`originalId` 为 Original Transaction ID | DTC Card Issuing / 3.4.4 |
| 是否有独立 notification id 未明确 | 已确认：没有独立 notification id | 用户确认 2026-05-01 |
| 重复推送时 ID 是否变化未明确 | 已确认：重复推送时 Transaction ID 不变 | 用户确认 2026-05-01 |
| Retrieve Basic Card Info 实际路径待确认 | 已明确：`[POST] /openapi/v1/card/inquiry-card-info` | DTC Card Issuing / 3.2.15 |
| Transfer Balance to Wallet 请求字段未明确 | 已明确：`cardId`、`amount` | DTC Card Issuing / 3.3.3 |
| Transfer Balance to Wallet 成功是否返回业务流水未明确 | 已明确：成功响应只返回 `header.success=true`，用户确认不会有归集业务流水 | DTC Card Issuing / 3.3.3；用户确认 |
| Top-up 是否触发归集未明确 | 已确认：Top-up 不触发，已移除 | 用户确认 2026-05-01 |
| 归集失败是否自动重试未明确 | 已确认：失败不自动重试，告警监控群 | 用户确认 2026-05-01 |
| 用户通知是否代表 Wallet 可见资金未明确 | 已确认：正常代表 Wallet 可见；极端情况可能卡有钱但转 Wallet 失败，用户看不到资金 | 用户确认 2026-05-01 |

## 5. 当前阻塞问题

### 5.1 后端待确认

| 编号 | 问题 | 影响 |
|---|---|---|
| CARD-BLOCK-BE-001 | 收到 `Card Transaction Notify` 后，AIX 是否生成内部交易处理 ID，字段名是什么 | 内部追踪主键不明确 |
| CARD-BLOCK-BE-002 | DTC Webhook 原始报文是否完整落库 | 审计与回放能力不明确 |
| CARD-BLOCK-BE-003 | 后端是否按 `event + data.id` 去重 | 防重复处理规则未落地 |
| CARD-BLOCK-BE-004 | 归集触发是否只判断 `type=REFUND/REVERSAL/DEPOSIT`，还是还需判断 `state` / `indicator` | 触发条件未完全闭环 |
| CARD-BLOCK-BE-005 | 发起 `Transfer Balance to Wallet` 前是否生成归集请求 ID，字段名是什么 | 归集请求不可追踪 |
| CARD-BLOCK-BE-006 | `D-REQUEST-ID` 如何生成、保存，并与归集请求 ID 关联 | 请求追踪链路不明确 |
| CARD-BLOCK-BE-007 | DTC `data.id`、AIX 内部交易处理 ID、归集请求 ID、`D-REQUEST-ID`、钱包流水之间如何串联 | 资金链路不可完整追溯 |
| CARD-BLOCK-BE-008 | 查询 balance 失败如何处理 | 异常分支未闭环 |
| CARD-BLOCK-BE-009 | 归集失败告警后是否有后台人工补偿入口 | 失败后处理路径未闭环 |
| CARD-BLOCK-BE-010 | 除已知系统原因 / 金额大于卡余额外，是否还有其他失败类型与责任分派 | 人工责任边界不完整 |

### 5.2 Wallet / 账务待确认

| 编号 | 问题 | 影响 |
|---|---|---|
| CARD-BLOCK-WALLET-001 | `Transfer Balance to Wallet` 成功后，钱包侧是否生成入账流水 ID，字段名是什么 | 钱包到账追踪不明确 |
| CARD-BLOCK-WALLET-002 | 钱包流水如何关联 DTC `data.id`、AIX 归集请求 ID 或 `D-REQUEST-ID` | 对账链路不明确 |
| CARD-BLOCK-WALLET-003 | Wallet `Search Balance History.relatedId` 在卡余额转 Wallet 场景下取哪个 ID | relatedId 口径不明确 |
| CARD-BLOCK-WALLET-004 | card balance 转 Wallet 后，入账币种是否与 card currency 完全一致 | 币种口径不明确 |
| CARD-BLOCK-WALLET-005 | 钱包入账是否有 pending / success / failed 等状态 | 入账状态闭环不明确 |
| CARD-BLOCK-WALLET-006 | 财务 / 运营最终用哪些字段串起 DTC 通知、AIX 归集请求、DTC transfer 调用和钱包流水 | 对账字段组合未定 |

## 6. 阶段判断

| 判断项 | 结论 |
|---|---|
| Card 页面类能力 | 可作为阶段完成 |
| Card 状态与字段事实源 | 可作为阶段完成 |
| DTC Card Transaction Notify 字段 | 已补齐 |
| 自动归集触发类型 | 已补齐 |
| Transfer to Wallet 请求字段 | 已补齐 |
| Transfer to Wallet 成功业务流水 | 已确认无返回 |
| Card 资金归集链路 | 暂不闭环 |
| 是否进入 Wallet 批量推进 | 暂缓 |

## 7. 后续建议

下一步不再继续追问 DTC 字段表和 transfer-to-wallet 请求 / 响应字段。

应直接向 AIX 后端、Wallet / 账务确认剩余链路问题：AIX 内部交易处理 ID、归集请求 ID、`D-REQUEST-ID` 保存关系、Wallet 入账流水、Wallet `relatedId`、查询余额失败处理、人工补偿入口和最终对账字段组合。

补齐后再执行一次 Card 阶段回扫。只有资金链路可追溯、状态闭环、接口路径明确后，再进入 Wallet 批量推进。

## 8. 来源引用

- (Ref: IMPLEMENTATION_PLAN.md / v3.2 / Stage Review Gate)
- (Ref: knowledge-base/card/_index.md / Card 功能清单 / 2026-05-01)
- (Ref: knowledge-base/card/card-transaction-flow.md / v1.1 / 2026-05-01)
- (Ref: knowledge-base/card/transaction-flow-traceability-checklist.md / v1.4 / 2026-05-01)
- (Ref: knowledge-base/changelog/knowledge-gaps.md / Card Transaction Flow / 2026-05-01)
