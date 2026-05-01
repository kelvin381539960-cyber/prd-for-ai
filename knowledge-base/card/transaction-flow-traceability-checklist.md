---
module: card
feature: transaction-flow-traceability-checklist
version: "1.2"
status: active
source_doc: AIX Card交易【transaction】.docx；AIX Card V1.0【Application】.docx；AIX APP V1.0【Transaction & History】.docx；knowledge-base/card/card-transaction-flow.md；knowledge-base/card/stage-review.md；IMPLEMENTATION_PLAN.md
source_section: Card Transaction Flow 6.3 / 8 / 9 / 10；Card Stage Review 4 / 5；IMPLEMENTATION_PLAN v3.2；AIX Card交易【transaction】7.3 / 8.1；Application 6.2；Transaction & History 6.1 / 6.2 / 6.3
last_updated: 2026-05-01
owner: 吴忆锋
depends_on:
  - card/card-transaction-flow
  - card/stage-review
  - changelog/knowledge-gaps
---

# Card Transaction Flow 资金追踪字段确认稿

## 1. 文档定位

本文档不是原文 PRD 转译正文，也不是接口事实源。

本文档用于 Card Transaction Flow Gate Review 阻塞期间，将“原文已明确”和“仍需 DTC / 后端 / Wallet 确认”的事项拆开，避免重复向负责人追问已在历史 PRD 或接口文档中存在的信息。

确认前，仍未闭环的字段不得写入功能正文作为已生效规则。

---

## 2. Review 后已消除的问题

以下内容已能从历史 PRD 或现有知识库找到，不再作为对外确认问题。

| 编号 | 原问题 | Review 结论 | 来源 |
|---|---|---|---|
| RESOLVED-001 | Card Transaction Flow 是否由 DTC 通知触发 | 已明确：DTC 检测发生交易后，通过 `Card Transaction Notification` 向 AIX 发送交易通知 | AIX Card交易【transaction】/ 7.3 |
| RESOLVED-002 | 哪些交易类型进入自动归集 | 已明确：AIX 收到通知后先校验 `type` 是否为 `refund` / `reversal` / `Top-up` / `deposit`；不匹配则终止 | AIX Card交易【transaction】/ 7.3 |
| RESOLVED-003 | 查询卡余额使用哪个接口 | 已明确：调用 `Retrieve Basic Card Info` 主动查询当前卡余额；接口路径为 `[POST] /openapi/v1/card/inquiry-card-info` | AIX Card交易【transaction】/ 7.3；AIX Card V1.0【Application】/ 6.2 |
| RESOLVED-004 | balance 字段是否存在及用途 | 已明确：DTC 返回最新卡 `balance`，记录接口字段为 `balance`；该字段作为后续归集金额依据 | AIX Card交易【transaction】/ 7.3 |
| RESOLVED-005 | 归集金额如何计算 | 已明确：当 `balance > 0` 时，AIX 调用 transfer to wallet，入参 `amount = balance` | AIX Card交易【transaction】/ 7.3 |
| RESOLVED-006 | balance = 0 如何处理 | 已明确：当卡当前余额 `balance = 0` 时，流程终止 | AIX Card交易【transaction】/ 7.3 |
| RESOLVED-007 | 资金归集接口路径 | 已明确：`Transfer Balance to Wallet` 接口路径为 `openapi/v1/card/transfer-to-wallet` | AIX Card交易【transaction】/ 8.1 |
| RESOLVED-008 | 归集失败是否需要告警 | 已明确：若回退失败，发送异常告警至监控群，并人工介入处理 | AIX Card交易【transaction】/ 7.3 |
| RESOLVED-009 | 归集失败责任初始分派 | 已明确：系统原因由开发跟进；交易金额大于卡余额由产品侧跟进 | AIX Card交易【transaction】/ 7.3 |
| RESOLVED-010 | 归集成功后的业务结果 | 已明确：若成功，资金已转入用户钱包，流程结束 | AIX Card交易【transaction】/ 7.3 |
| RESOLVED-011 | 卡交易列表接口路径 | 已明确：`Transaction History of Card` 路径为 `[POST] /openapi/v1/card/inquiry-card-transaction` | AIX APP V1.0【Transaction & History】/ 6.1 / 7.1 |
| RESOLVED-012 | 卡交易详情接口与查询 ID | 已明确：进入 Card Transaction Details 后，上送 `Transaction ID` 获取最新交易记录；接口为 `Card Transaction Detail Inquiry` | AIX APP V1.0【Transaction & History】/ 5.3 / 6.2 |
| RESOLVED-013 | Card Transaction Notify 是否存在 | 已明确：`Card Transaction Notify` 用于接收 DTC Webhook 异步通知卡交易记录 | AIX APP V1.0【Transaction & History】/ 6.3 |

---

## 3. Review 后仍需确认的问题

以下问题在现有可读原文中仍未闭环，继续保留为对外确认项。

### 3.1 需要 DTC 确认

请 DTC 优先确认以下内容：

1. `Card Transaction Notification / Card Transaction Notify` 的完整字段表：字段名、类型、是否必填、示例值。
2. 通知是否有唯一 ID，例如 event id / notification id；若有，字段名是什么。
3. 通知中的原始卡交易 ID 是哪个字段；是否就是前端详情页使用的 `Transaction ID`。
4. 通知中 `type` 字段的真实枚举值：是否与 PRD 中的 `refund` / `reversal` / `Top-up` / `deposit` 完全一致，包括大小写和下划线格式。
5. `Transfer Balance to Wallet` 的完整请求字段：是否有 card id、amount、currency、reference / request id 等字段。
6. `Transfer Balance to Wallet` 的完整响应字段：是否有归集结果 ID、状态、失败码、失败原因。
7. 重复通知时，AIX 应使用哪个字段做幂等去重。
8. 重复发起 `Transfer Balance to Wallet` 时，DTC 侧是否支持幂等；幂等键字段是什么。
9. 归集失败时，哪些失败码可重试，哪些不可重试；重试间隔和最大次数是什么。
10. `Card Transaction Notification` 与 `Transfer Balance to Wallet` 结果之间，DTC 侧是否有可关联字段。

### 3.2 需要 AIX 后端确认

请后端确认以下内容：

1. 收到 DTC 通知后，AIX 是否生成内部交易 ID；字段名是什么。
2. DTC 原始通知是否完整落库；落库表或日志是否可用于审计和回放。
3. 发起 `Transfer Balance to Wallet` 前，AIX 是否生成归集请求 ID；字段名是什么。
4. DTC 通知 ID、DTC 原始交易 ID、AIX 内部交易 ID、归集请求 ID 之间如何关联。
5. 查询 `balance` 失败时，是否重试、是否告警、是否进入待处理队列。
6. 重复通知时，是忽略、更新状态，还是重新校验后处理。
7. 归集失败进入人工处理后，是否有后台重试 / 人工补偿入口；如果有，入口和操作边界是什么。
8. 已知“系统原因开发跟进、金额大于卡余额产品跟进”之外，是否还有其他失败类型与责任分派。

### 3.3 需要 Wallet / 账务确认

请 Wallet / 账务侧确认以下内容：

1. 归集成功后，钱包侧是否生成入账流水 ID；字段名是什么。
2. 钱包入账流水如何关联 DTC 归集结果 ID 或 AIX 归集请求 ID。
3. card balance 转入钱包时，入账币种口径是什么。
4. 钱包入账是否存在 pending / success / failed 等状态。
5. 如果 DTC 归集成功但钱包入账失败，如何处理资金悬挂。
6. 财务对账时，需要哪些字段串起 DTC 通知、归集结果和钱包流水。

---

## 4. 对外发送精简版

可直接复制以下内容发给 DTC / 后端 / Wallet 负责人。

```text
各位好，Card Transaction Flow 当前卡在资金归集链路可追溯字段未闭环，需要请 DTC / 后端 / Wallet 一起确认。

已从历史 PRD 确认的信息：
1. DTC 通过 Card Transaction Notification / Card Transaction Notify 通知 AIX 卡交易。
2. AIX 判断 type 是否为 refund / reversal / Top-up / deposit；不匹配则终止。
3. 匹配后调用 Retrieve Basic Card Info 查询当前卡 balance。
4. Retrieve Basic Card Info 路径为 [POST] /openapi/v1/card/inquiry-card-info。
5. balance > 0 时调用 Transfer Balance to Wallet，amount = balance。
6. Transfer Balance to Wallet 路径为 openapi/v1/card/transfer-to-wallet。
7. balance = 0 时终止。
8. 归集失败需告警到监控群并人工介入；系统原因开发跟进，金额大于卡余额产品跟进。

还需要确认：

DTC：
1. Card Transaction Notification / Notify 的完整字段表。
2. 通知唯一 ID、原始卡交易 ID 字段名。
3. type 的真实枚举值是否与 refund / reversal / Top-up / deposit 一致。
4. Transfer Balance to Wallet 的完整请求 / 响应字段，尤其是归集结果 ID、状态、失败码、失败原因。
5. 通知幂等字段、归集幂等字段、可重试失败码、重试间隔、最大次数。

后端：
1. AIX 内部交易 ID、归集请求 ID 字段名。
2. DTC 通知 ID、DTC 原始交易 ID、AIX 内部交易 ID、归集请求 ID 的关联关系。
3. 原始通知是否落库，是否支持审计 / 回放。
4. 查询 balance 失败怎么处理。
5. 重复通知怎么处理。
6. 是否有后台重试 / 人工补偿入口。

Wallet / 账务：
1. 钱包入账流水 ID 字段名。
2. 钱包流水如何关联 DTC 归集结果 ID 或 AIX 归集请求 ID。
3. 入账币种、入账状态、入账失败处理。
4. 对账需要哪些字段串起 DTC 通知、归集结果和钱包流水。
```

---

## 5. Gate Review 判断

本次 Review 只能消除部分重复确认项，不能解除 Card 阶段 `BLOCK`。

原因：资金链路仍缺少通知唯一 ID、原始交易 ID、AIX 内部交易 ID、归集请求 ID、DTC 归集结果 ID、钱包入账流水 ID、幂等键、重试规则和钱包入账失败处理等闭环字段。

只有上述关键项确认后，才可更新 `card-transaction-flow.md`、`knowledge-gaps.md`、`stage-review.md`，并重新执行 Card Stage Review。

---

## 6. 来源引用

- (Ref: AIX Card交易【transaction】.docx / 7.3 流程说明 / 2026-01-04)
- (Ref: AIX Card交易【transaction】.docx / 8.1 外部接口清单 / 2026-01-04)
- (Ref: AIX Card V1.0【Application】.docx / 6.2 Retrieve Basic Card Info / 2026-01-04)
- (Ref: AIX APP V1.0【Transaction & History】.docx / 5.3 Card Transaction Details / 2026-01-04)
- (Ref: AIX APP V1.0【Transaction & History】.docx / 6.1 Transaction History of Card / 2026-01-04)
- (Ref: AIX APP V1.0【Transaction & History】.docx / 6.2 Card Transaction Detail Inquiry / 2026-01-04)
- (Ref: AIX APP V1.0【Transaction & History】.docx / 6.3 Card Transaction Notify / 2026-01-04)
- (Ref: IMPLEMENTATION_PLAN.md / v3.2 / Stage Review Gate / 2026-05-01)
