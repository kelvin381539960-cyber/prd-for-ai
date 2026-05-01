---
module: card
feature: transaction-flow-traceability-checklist
version: "1.1"
status: active
source_doc: knowledge-base/card/card-transaction-flow.md；knowledge-base/card/stage-review.md；IMPLEMENTATION_PLAN.md
source_section: Card Transaction Flow 6.3 / 8 / 9 / 10；Card Stage Review 4 / 5；IMPLEMENTATION_PLAN v3.2
last_updated: 2026-05-01
owner: 吴忆锋
depends_on:
  - card/card-transaction-flow
  - card/stage-review
  - changelog/knowledge-gaps
---

# Card Transaction Flow 资金追踪字段确认稿

## 1. 发送对象

DTC / AIX 后端 / Wallet 负责人。

## 2. 背景

Card Transaction Flow 当前已梳理到以下链路：

```text
DTC Card Transaction Notification
→ AIX 判断交易类型
→ 查询卡 balance
→ balance > 0 时发起 Transfer Balance to Wallet
→ 归集成功 / 归集失败告警人工处理
```

当前 Card 阶段 Gate Review 结果为 `BLOCK`。原因不是业务流程未梳理，而是资金归集链路的可追溯字段和异常规则还未确认。

为避免后续出现重复通知、重复归集、归集失败、钱包未到账、人工补单时无法定位，请各方确认下面字段和规则。

> 说明：以下内容均为待确认项，不代表当前已实现或已定稿。

---

## 3. 需要 DTC 确认

请 DTC 侧确认：

1. Card Transaction Notification 的完整字段表：字段名、类型、是否必填、示例值。
2. 通知是否有唯一 ID，例如 event id / notification id。
3. 卡交易是否有原始交易 ID，例如 transaction id。
4. 重复通知时，AIX 应使用哪个字段做幂等去重。
5. 交易类型枚举中，refund / reversal / Top-up / deposit 的准确取值是什么。
6. Retrieve Basic Card Info / 查询卡 balance 的实际接口路径、请求字段、响应字段。
7. balance 字段口径：是可用余额、账面余额，还是当前卡余额。
8. Transfer Balance to Wallet 的请求字段，尤其是 card id、amount、currency、reference / request id。
9. Transfer Balance to Wallet 的响应字段，尤其是归集结果 ID、状态、失败码、失败原因。
10. 归集失败时，哪些失败码可重试，哪些不可重试；重试间隔和最大次数是什么。

请优先回复：字段表、ID 字段、幂等字段、失败码、重试规则。

---

## 4. 需要 AIX 后端确认

请后端确认：

1. 收到 DTC 通知后，AIX 是否生成内部交易 ID；字段名是什么。
2. DTC 原始通知是否完整落库；落库表或日志是否可用于审计和回放。
3. 发起 Transfer Balance to Wallet 前，AIX 是否生成归集请求 ID；字段名是什么。
4. DTC 通知 ID、DTC 原始交易 ID、AIX 内部交易 ID、归集请求 ID 之间如何关联。
5. 查询卡 balance 失败时，是否重试、是否告警、是否进入待处理队列。
6. 归集失败时，系统失败、余额异常、DTC 返回失败分别由谁处理。
7. 重复通知时，是忽略、更新状态，还是重新校验后处理。
8. 是否有后台重试 / 人工补偿入口；如果有，入口和操作边界是什么。

请优先回复：内部交易 ID、归集请求 ID、通知落库、重复通知处理、失败处理责任。

---

## 5. 需要 Wallet / 账务确认

请 Wallet / 账务侧确认：

1. 归集成功后，钱包侧是否生成入账流水 ID；字段名是什么。
2. 钱包入账流水如何关联 DTC 归集结果 ID 或 AIX 归集请求 ID。
3. card balance 转入钱包时，入账币种口径是什么。
4. 钱包入账是否存在 pending / success / failed 等状态。
5. 如果 DTC 归集成功但钱包入账失败，如何处理资金悬挂。
6. 财务对账时，需要哪些字段串起 DTC 通知、归集结果和钱包流水。

请优先回复：钱包入账流水 ID、关联字段、入账状态、入账失败处理。

---

## 6. 建议统一确认表

请各方尽量按下表补充，便于后续写入知识库和接口事实源。

| 链路节点 | 需确认字段 / 规则 | 负责人 | 当前结论 |
|---|---|---|---|
| DTC 通知 | 通知唯一 ID | DTC | 待确认 |
| DTC 交易 | 原始卡交易 ID | DTC | 待确认 |
| AIX 接收 | AIX 内部交易 ID | 后端 | 待确认 |
| 通知落库 | 原始通知落库与审计方式 | 后端 | 待确认 |
| 余额查询 | 查询接口路径、balance 字段口径 | DTC / 后端 | 待确认 |
| 归集请求 | AIX 归集请求 ID / reference 字段 | 后端 / DTC | 待确认 |
| DTC 归集结果 | 归集结果 ID、状态、失败码 | DTC | 待确认 |
| 钱包入账 | 钱包入账流水 ID、入账状态 | Wallet / 账务 | 待确认 |
| 幂等控制 | 重复通知、重复归集的判断字段 | DTC / 后端 | 待确认 |
| 重试策略 | 可重试失败、间隔、最大次数 | DTC / 后端 | 待确认 |
| 异常处理 | 告警、人工补偿、责任分派 | 后端 / Wallet / 运营 | 待确认 |
| 对账闭环 | 通知、归集、钱包流水的关联字段 | DTC / 后端 / Wallet | 待确认 |

---

## 7. 验收口径

Card Transaction Flow 解除阻塞前，至少需要确认以下内容：

1. DTC 通知唯一 ID。
2. DTC 原始卡交易 ID。
3. AIX 内部交易 ID。
4. 归集请求 ID。
5. DTC 归集结果 ID。
6. 钱包入账流水 ID。
7. 幂等规则。
8. 重复通知处理规则。
9. 查询 balance 失败处理。
10. 归集失败重试、告警和人工处理规则。

以上任一关键项未确认，Card 阶段仍保持 `BLOCK`，暂不进入 Wallet 阶段。

---

## 8. 来源引用

- (Ref: knowledge-base/card/card-transaction-flow.md / 6.3 可追溯性当前状态 / 2026-05-01)
- (Ref: knowledge-base/card/card-transaction-flow.md / 8 字段与接口依赖 / 2026-05-01)
- (Ref: knowledge-base/card/card-transaction-flow.md / 9 异常与失败处理 / 2026-05-01)
- (Ref: knowledge-base/card/stage-review.md / 4 阻塞问题 / 2026-05-01)
- (Ref: IMPLEMENTATION_PLAN.md / v3.2 / 18 下一步)
