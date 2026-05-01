---
module: card
feature: transaction-flow-traceability-checklist
version: "1.0"
status: active
source_doc: knowledge-base/card/card-transaction-flow.md；knowledge-base/card/stage-review.md；IMPLEMENTATION_PLAN.md
source_section: Card Transaction Flow 6.3 / 8 / 9 / 10；Card Stage Review 4 / 5；IMPLEMENTATION_PLAN v3.0
last_updated: 2026-05-01
owner: 吴忆锋
depends_on:
  - card/card-transaction-flow
  - card/stage-review
  - changelog/knowledge-gaps
---

# Card Transaction Flow 追踪字段确认清单

## 1. 文档定位

本文档用于向 DTC / 后端确认 Card Transaction Flow 的资金追踪字段、幂等规则、重试策略和异常处理口径。

本文档不是最终接口事实源。以下字段均为“需确认项”，不得在确认前写入功能正文作为已生效规则。

## 2. 当前阻塞结论

Card Transaction Flow 已完成业务流程转译，但资金归集链路暂不闭环。

阻塞原因：DTC 通知、AIX 内部处理、归集请求、DTC 归集结果、钱包入账之间缺少明确关联字段。若不补齐，后续出现重复通知、归集失败、钱包未到账、人工补单时无法完整追溯。

## 3. 需 DTC 确认的问题

| 编号 | 问题 | 必须确认内容 | 影响 |
|---|---|---|---|
| DTC-001 | Card Transaction Notification 字段表 | 完整请求字段、字段类型、是否必填 | 通知入库与排查 |
| DTC-002 | DTC 原始交易 ID | 是否有唯一 transaction id / event id | 通知去重与链路追踪 |
| DTC-003 | 通知幂等键 | 重复通知时使用哪个字段判断重复 | 防止重复归集 |
| DTC-004 | 交易类型枚举 | refund / reversal / Top-up / deposit 的准确枚举值 | 类型判断 |
| DTC-005 | 查询卡余额接口 | Retrieve Basic Card Info 的实际接口路径、请求字段、响应字段 | balance 查询 |
| DTC-006 | balance 字段口径 | balance 是可用余额、账面余额还是当前卡余额 | 归集金额依据 |
| DTC-007 | Transfer Balance to Wallet 请求字段 | card id、amount、currency、reference 字段 | 归集提交 |
| DTC-008 | Transfer Balance to Wallet 响应字段 | 结果状态、归集流水、失败码、失败原因 | 结果确认 |
| DTC-009 | 失败码 | 系统失败、余额不足、重复请求、参数错误等错误码 | 异常分派 |
| DTC-010 | 重试策略 | 哪些失败可重试、重试间隔、最大次数 | 自动恢复 |

## 4. 需 AIX 后端确认的问题

| 编号 | 问题 | 必须确认内容 | 影响 |
|---|---|---|---|
| AIX-BE-001 | AIX 内部交易 ID | 收到 DTC 通知后生成哪个内部 ID | 内部追踪 |
| AIX-BE-002 | 通知入库表 | 原始通知如何落库 | 审计与回放 |
| AIX-BE-003 | 归集请求 ID | 调用 Transfer Balance to Wallet 前是否生成 request id | 幂等与排查 |
| AIX-BE-004 | 通知与归集关联 | DTC 通知 ID、AIX 交易 ID、归集请求 ID 的关联关系 | 链路闭环 |
| AIX-BE-005 | 查询余额失败处理 | 是否重试、是否告警、是否进入待处理队列 | 异常闭环 |
| AIX-BE-006 | 归集失败处理 | 系统失败、余额异常、DTC 失败的处理责任 | 人工分派 |
| AIX-BE-007 | 重复通知处理 | 重复通知是否直接忽略、更新状态或重新校验 | 防重复处理 |
| AIX-BE-008 | 人工补偿入口 | 失败后是否有后台重试或人工补偿能力 | 运营处理 |

## 5. 需 Wallet / 账务确认的问题

| 编号 | 问题 | 必须确认内容 | 影响 |
|---|---|---|---|
| WALLET-001 | 钱包入账流水 ID | 归集成功后钱包侧生成哪个流水 ID | 到账追踪 |
| WALLET-002 | 归集到账币种 | card balance 转入钱包时币种口径 | 用户展示与对账 |
| WALLET-003 | 入账状态 | 钱包入账是否存在 pending / success / failed | 状态闭环 |
| WALLET-004 | 对账字段 | 钱包流水如何关联 DTC 归集结果 | 财务对账 |
| WALLET-005 | 入账失败处理 | DTC 成功但钱包入账失败如何处理 | 资金悬挂处理 |

## 6. 推荐链路字段模型（待确认）

以下为建议补齐的字段模型，不代表当前已实现。

| 链路节点 | 建议字段 | 用途 | 状态 |
|---|---|---|---|
| DTC 通知 | `dtcEventId` | 通知唯一标识 | 待确认 |
| DTC 交易 | `dtcTransactionId` | 原始卡交易标识 | 待确认 |
| AIX 接收 | `aixTransactionId` | AIX 内部交易标识 | 待确认 |
| 余额查询 | `balanceInquiryId` | 查询卡余额请求标识 | 待确认 |
| 归集请求 | `transferRequestId` | AIX 发起归集请求标识 | 待确认 |
| DTC 归集结果 | `dtcTransferId` | DTC 归集结果标识 | 待确认 |
| 钱包入账 | `walletLedgerId` | 钱包入账流水标识 | 待确认 |
| 幂等控制 | `idempotencyKey` | 防止重复归集 | 待确认 |

## 7. 建议状态机（待确认）

以下为建议补齐的内部处理状态，不代表当前已实现。

```text
RECEIVED_NOTIFICATION
→ TYPE_CHECKED
→ BALANCE_QUERIED
→ TRANSFER_SUBMITTED
→ TRANSFER_SUCCESS / TRANSFER_FAILED
→ WALLET_POSTED / MANUAL_REVIEW
```

## 8. 验收口径

只有以下信息被确认后，Card 阶段才可解除阻塞：

| 验收项 | 是否必须 | 说明 |
|---|---|---|
| DTC 通知唯一 ID | 是 | 用于去重与追踪 |
| DTC 原始交易 ID | 是 | 用于关联卡交易 |
| AIX 内部交易 ID | 是 | 用于系统内追踪 |
| 归集请求 ID | 是 | 用于幂等与重试 |
| DTC 归集结果 ID | 是 | 用于归集结果确认 |
| 钱包入账流水 ID | 是 | 用于到账和对账 |
| 幂等规则 | 是 | 防止重复归集 |
| 重试与告警策略 | 是 | 防止资金悬挂 |
| 失败责任分派 | 是 | 区分研发、产品、运营处理 |

## 9. 后续动作

1. 将本文档问题发给 DTC / 后端 / Wallet 负责人确认。
2. 收到确认后更新 `card-transaction-flow.md`。
3. 同步更新 `knowledge-gaps.md` 中 Card Transaction Flow 缺口状态。
4. 重新执行 `card/stage-review.md`。
5. 阻塞解除后再进入 Wallet 批量推进。

## 10. 来源引用

- (Ref: knowledge-base/card/card-transaction-flow.md / 6.3 可追溯性当前状态 / 2026-05-01)
- (Ref: knowledge-base/card/card-transaction-flow.md / 8 字段与接口依赖 / 2026-05-01)
- (Ref: knowledge-base/card/card-transaction-flow.md / 9 异常与失败处理 / 2026-05-01)
- (Ref: knowledge-base/card/stage-review.md / 4 阻塞问题 / 2026-05-01)
- (Ref: IMPLEMENTATION_PLAN.md / v3.0 / 18 下一步)
