---
module: card
feature: transaction-flow-traceability-checklist
version: "1.3"
status: active
source_doc: DTC接口文档/DTC Card Issuing API Document_20260310 (1).pdf；DTC Wallet OpenAPI Documentation；[2025-11-25] AIX+Notification（push及站内信）；AIX Card交易【transaction】；AIX APP V1.0【Transaction & History】；knowledge-base/card/card-transaction-flow.md；knowledge-base/card/stage-review.md；IMPLEMENTATION_PLAN.md
source_section: Card Issuing 2.4 / 3.3.3 / 3.3.4 / 3.3.5 / 3.3.7 / 3.4 / 3.4.4 / Appendix A / Appendix B；Wallet 4.2.4；Notification 卡相关；IMPLEMENTATION_PLAN v3.2
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

本文档用于 Card Transaction Flow Gate Review 阻塞期间，将“文档已明确”和“仍需 DTC / 后端 / Wallet 确认”的事项拆开，避免重复向负责人追问已在历史 PRD、DTC 接口文档或通知配置中存在的信息。

确认前，仍未闭环的字段不得写入功能正文作为已生效规则。

---

## 2. Review 后已消除的问题

以下内容已能从历史 PRD、DTC 接口文档或通知配置中找到，不再作为对外确认问题。

| 编号 | 原问题 | Review 结论 | 来源 |
|---|---|---|---|
| RESOLVED-001 | Card Transaction Flow 是否由 DTC 通知触发 | 已明确：DTC 通过 `Card Transaction Notification / Card Transaction Notify` 通知 AIX 卡交易 | AIX Card交易【transaction】/ 7.3；DTC Card Issuing / 3.4.4 |
| RESOLVED-002 | 哪些交易类型进入自动归集 | 历史 PRD 写明 AIX 判断 `type` 是否为 `refund` / `reversal` / `Top-up` / `deposit`；不匹配则终止 | AIX Card交易【transaction】/ 7.3 |
| RESOLVED-003 | DTC Card Transaction Notify 字段表是否存在 | 已明确：DTC 接口文档提供 `Card Transaction Notify` 字段表 | DTC Card Issuing / 3.4.4 |
| RESOLVED-004 | DTC 通知里的卡交易 ID | 已明确：`id` 为 `Transaction ID`，必填；可作为 DTC 卡交易记录 ID | DTC Card Issuing / 3.4.4 |
| RESOLVED-005 | DTC 原始交易 ID 字段 | 已明确：`originalId` 为 `Original Transaction ID`，选填 | DTC Card Issuing / 3.4.4 |
| RESOLVED-006 | 通知基础关联字段 | 已明确：通知包含 `clientId`、`cardId`、`cardToken`、`truncatedCardNumber`、`processorTransactionId`、`referenceNo`、`acquirerReferenceNo` 等字段 | DTC Card Issuing / 3.4.4 |
| RESOLVED-007 | 通知金额与币种字段 | 已明确：通知包含 `amount`、`currency`、`requestAmount`、`requestCurrency`、`indicator` | DTC Card Issuing / 3.4.4 |
| RESOLVED-008 | 通知交易时间字段 | 已明确：通知包含 `transactionDate`、`transactionTime`、`confirmedTime`、`createdDate` | DTC Card Issuing / 3.4.4 |
| RESOLVED-009 | 查询卡余额使用哪个接口 | 已明确：调用 `Retrieve Basic Card Info / Inquiry Card Basic Info` 查询卡余额；接口路径为 `[POST] /openapi/v1/card/inquiry-card-info` | AIX Card交易【transaction】/ 7.3；DTC Card Issuing / 3.2.15 |
| RESOLVED-010 | balance 字段是否存在及用途 | 已明确：`Inquiry Card Basic Info` 响应含 `balance`；历史 PRD 写明该字段作为归集金额依据 | DTC Card Issuing / 3.2.15；AIX Card交易【transaction】/ 7.3 |
| RESOLVED-011 | 归集金额如何计算 | 已明确：当 `balance > 0` 时，调用 transfer to wallet，入参 `amount = balance` | AIX Card交易【transaction】/ 7.3 |
| RESOLVED-012 | balance = 0 如何处理 | 已明确：当卡当前余额 `balance = 0` 时，流程终止 | AIX Card交易【transaction】/ 7.3 |
| RESOLVED-013 | Transfer Balance to Wallet 接口路径 | 已明确：接口路径为 `[POST] /openapi/v1/card/transfer-to-wallet` | DTC Card Issuing / 3.3.3 |
| RESOLVED-014 | Transfer Balance to Wallet 请求字段 | 已明确：请求字段只有 `cardId` 与 `amount`，均为必填 | DTC Card Issuing / 3.3.3 |
| RESOLVED-015 | Transfer Balance to Wallet 成功响应字段 | 已明确：示例仅返回 `header.success = true`，未返回业务结果 ID | DTC Card Issuing / 3.3.3 |
| RESOLVED-016 | Transfer Balance to Wallet 错误码 | 已明确：可能错误码包括 `00006`、`20004`、`31005`、`31006`、`31022`、`31033`、`31038` | DTC Card Issuing / 3.3.3 |
| RESOLVED-017 | DTC API 请求追踪 Header | 已明确：请求 Header 需要 `D-REQUEST-ID`，描述为 client-generated unique request identifier | DTC Card Issuing / 2.4 |
| RESOLVED-018 | 卡交易列表接口路径和字段 | 已明确：`[POST] /openapi/v1/card/inquiry-card-transaction`，返回 `id`、`type`、`state`、`cardId`、`originalId`、`processorTransactionId`、`amount`、`currency`、`referenceNo` 等字段 | DTC Card Issuing / 3.3.4 |
| RESOLVED-019 | 卡交易详情接口路径和字段 | 已明确：`[POST] /openapi/v1/card/inquiry-card-transaction-detail`，入参为 `transactionId`，响应字段与交易列表基本一致 | DTC Card Issuing / 3.3.5 |
| RESOLVED-020 | 卡余额历史查询字段 | 已明确：`[POST] /openapi/v1/card/inquiry-card-balance-history`，支持 `relatedId`，返回 `id`、`type`、`balanceBefore`、`changeAmount`、`balanceAfter`、`currency`、`relatedId` | DTC Card Issuing / 3.3.7 |
| RESOLVED-021 | DTC CardTransactionType 枚举 | 已明确：`1 Top-up`、`2 Purchase`、`3 Purchase reversal`、`4 Mismatch debit`、`5 Mismatch reversal`、`6 No auth settlement`、`99 Others` | DTC Card Issuing / Appendix B |
| RESOLVED-022 | DTC Transaction Status 枚举 | 已明确：`PENDING 0`、`AUTHORIZED 101`、`SUCCESS 200`、`CAPTURED 221`、`REVERSED 301`、`CANCELLED 302` 等 | DTC Card Issuing / Appendix B |
| RESOLVED-023 | DTC DeniedReason 枚举 | 已明确包含 `INSUFFICIENT_FUNDS`、`INVALID_ORIGINAL_TRANSACTION`、`INVALID_TRANSACTION`、`INVALID_AMOUNT`、`SYSTEM_ERROR`、`INSTITUTION_LIMIT` 等 | DTC Card Issuing / Appendix B |
| RESOLVED-024 | 归集失败是否需要告警 | 已明确：若回退失败，发送异常告警至监控群，并人工介入处理 | AIX Card交易【transaction】/ 7.3 |
| RESOLVED-025 | 归集失败责任初始分派 | 已明确：系统原因由开发跟进；交易金额大于卡余额由产品侧跟进 | AIX Card交易【transaction】/ 7.3 |
| RESOLVED-026 | 归集成功后的业务结果 | 已明确：若成功，资金已转入用户钱包，流程结束 | AIX Card交易【transaction】/ 7.3 |
| RESOLVED-027 | 钱包交易历史查询能力 | 已明确：Wallet `Search Balance History` 可查询钱包交易历史，返回 `activityType`、`relatedId`、`time`、`state` 等字段 | DTC Wallet OpenAPI / 4.2.4 |
| RESOLVED-028 | 卡交易成功是否通知用户 | 已明确：通知配置存在“卡交易成功”，触发源为 `3.4.4 Card Transaction Notify`，条件包含 `indicator=debit`、`status=101 AUTHORIZED`，跳转卡交易详情页 | AIX Notification / 卡相关 |
| RESOLVED-029 | 卡退款成功是否通知用户 | 已明确：通知配置存在“卡退款成功”，触发源为 `3.4.4 Card Transaction Notify`，条件包含 `indicator=credit`，并列出 refund / reversed 场景，跳转卡交易详情页 | AIX Notification / 卡相关 |
| RESOLVED-030 | 用户通知字段参数 | 已明确：卡交易 / 退款通知参数包含 `merchant_name`、`amount`、`currency`、`transaction_time`，文案参数还包含 `full_name`、`last 4` | AIX Notification / 卡相关 |

---

## 3. Review 后仍需确认的问题

以下问题在现有可读文档中仍未闭环，继续保留为对外确认项。

### 3.1 需要 DTC 确认

请 DTC 优先确认以下内容：

1. `Card Transaction Notify.id` 是否可作为异步通知去重键；若 DTC 会重复推送同一交易，重复通知时 `id` 是否保持一致。
2. Webhook 是否存在独立的 notification event id。当前文档只看到 `event = CARD_TRANSACTION` 和 `data.id = Transaction ID`，未看到独立通知流水。
3. 历史 PRD 的 `refund / reversal / Top-up / deposit` 与 DTC 当前 `CardTransactionType` 枚举如何映射。DTC 文档当前枚举为 `Top-up / Purchase / Purchase reversal / Mismatch debit / Mismatch reversal / No auth settlement / Others`，未直接出现 `refund` 或 `deposit`。
4. Notification 配置中的 `type=purchase / INCREMENTAL AUTH / refund / reversed`、`status=capture / success` 与 DTC 文档中的数字枚举如何对应。
5. `Transfer Balance to Wallet` 成功响应当前仅返回 `header.success = true`，是否另有 DTC 归集结果 ID / transaction id / balance history id 可用于对账。
6. `D-REQUEST-ID` 是否仅用于请求追踪与签名，还是 DTC 侧也按该字段做幂等控制。
7. 重复发起 `Transfer Balance to Wallet` 时，DTC 是否支持幂等；若支持，幂等键是否为 `D-REQUEST-ID`。
8. `31022 Fund Transfer Failed, Please try again` 是否可自动重试；其他错误码是否可重试；重试间隔和最大次数是什么。
9. `Transfer Balance to Wallet` 成功后，是否会生成 `Card Balance History` 记录；若会，`relatedId` 应关联卡交易 `id`、`D-REQUEST-ID`，还是其他流水。

### 3.2 需要 AIX 后端确认

请后端确认以下内容：

1. 收到 `Card Transaction Notify` 后，AIX 内部是否生成交易处理 ID；字段名是什么。
2. AIX 是否完整落库 DTC Webhook 原始报文，包括 `event`、`clientId`、`data.id`、`originalId`、`processorTransactionId`、`referenceNo`、`state`、`type`、`indicator` 等字段。
3. AIX 对重复 Webhook 的去重规则是什么：建议至少基于 `event + data.id` 判断，但需后端确认。
4. 发起 `Transfer Balance to Wallet` 前，AIX 是否生成内部归集请求 ID；字段名是什么。
5. AIX 发起 `Transfer Balance to Wallet` 时，`D-REQUEST-ID` 如何生成、保存并与内部归集请求 ID 关联。
6. DTC 卡交易 `id`、AIX 内部交易处理 ID、AIX 归集请求 ID、`D-REQUEST-ID`、后续钱包流水之间如何关联。
7. 查询 `balance` 失败时，是否重试、是否告警、是否进入待处理队列。
8. 归集失败进入人工处理后，是否有后台重试 / 人工补偿入口；如果有，入口和操作边界是什么。
9. 已知“系统原因开发跟进、金额大于卡余额产品跟进”之外，是否还有其他失败类型与责任分派。

### 3.3 需要 Wallet / 账务确认

请 Wallet / 账务侧确认以下内容：

1. `Transfer Balance to Wallet` 成功后，钱包侧是否生成入账流水 ID；字段名是什么。
2. 钱包流水如何关联卡交易 `id`、AIX 归集请求 ID 或 `D-REQUEST-ID`。
3. Wallet `Search Balance History.relatedId` 在卡余额转钱包场景下应取哪个 ID。
4. card balance 转入钱包时，入账币种口径是否与 card currency 完全一致。
5. 钱包入账是否存在 pending / success / failed 等状态；如存在，字段与枚举是什么。
6. 如果 DTC `Transfer Balance to Wallet` 返回成功但钱包侧入账失败，如何处理资金悬挂。
7. 财务对账时，需要哪些字段串起 DTC 卡交易通知、AIX 归集请求、DTC 归集结果和钱包流水。

---

## 4. 对外发送精简版

可直接复制以下内容发给 DTC / 后端 / Wallet 负责人。

```text
各位好，Card Transaction Flow 当前卡在资金归集链路可追溯字段未闭环。已根据 DTC Card Issuing API、DTC Wallet API 和 Notification 配置先消除一轮问题，现在只剩以下关键点需要确认。

已确认信息：
1. DTC Card Transaction Notify 字段表已存在，通知字段包含 id、type、state、clientId、cardId、originalId、processorTransactionId、indicator、amount、currency、requestAmount、requestCurrency、merchantName、referenceNo、transactionDate、transactionTime、confirmedTime、createdDate 等。
2. id 是 DTC Card Transaction ID；originalId 是 Original Transaction ID。
3. Transfer Balance to Wallet 路径为 [POST] /openapi/v1/card/transfer-to-wallet。
4. Transfer Balance to Wallet 请求字段只有 cardId 和 amount。
5. Transfer Balance to Wallet 成功响应示例只返回 header.success=true，没有业务结果 ID。
6. API 请求 Header 有 D-REQUEST-ID，描述为客户端生成的唯一请求标识。
7. DTC CardTransactionType 枚举为：1 Top-up、2 Purchase、3 Purchase reversal、4 Mismatch debit、5 Mismatch reversal、6 No auth settlement、99 Others。
8. Transaction Status 包含 101 AUTHORIZED、200 SUCCESS、221 CAPTURED、301 REVERSED、302 CANCELLED 等。
9. Notification 已配置卡交易成功和卡退款成功通知，均由 Card Transaction Notify 触发，跳转卡交易详情页。

还需要确认：

DTC：
1. Card Transaction Notify 的 data.id 是否可作为重复通知去重键；重复推送时 id 是否保持一致。
2. 是否存在独立 notification event id；如果没有，是否建议用 event + data.id 去重。
3. 历史 PRD 的 refund / reversal / Top-up / deposit 与 DTC 当前 CardTransactionType 枚举如何映射。
4. Notification 中的 purchase / INCREMENTAL AUTH / refund / reversed、capture / success 与 DTC 数字枚举如何对应。
5. Transfer Balance to Wallet 是否有归集结果 ID；当前文档成功响应未返回业务流水。
6. D-REQUEST-ID 是否支持幂等，还是仅用于请求追踪 / 签名。
7. 31022 及其他失败码的重试规则：哪些可重试、间隔、最大次数。
8. Transfer Balance to Wallet 成功后，是否可通过 Card Balance History 或其他接口查询归集流水；relatedId 应关联哪个 ID。

后端：
1. AIX 内部交易处理 ID、归集请求 ID 字段名。
2. DTC Webhook 原始报文是否完整落库。
3. 重复通知去重规则。
4. DTC transaction id、AIX 内部交易 ID、归集请求 ID、D-REQUEST-ID、钱包流水之间如何关联。
5. 查询 balance 失败如何处理。
6. 是否有后台重试 / 人工补偿入口。

Wallet / 账务：
1. 钱包入账流水 ID 字段名。
2. 钱包流水如何关联卡交易 id、AIX 归集请求 ID 或 D-REQUEST-ID。
3. Wallet Search Balance History.relatedId 在卡余额转钱包场景下取哪个 ID。
4. 入账币种、入账状态、入账失败处理。
5. 对账需要哪些字段串起 DTC 通知、归集请求、DTC 结果和钱包流水。
```

---

## 5. Gate Review 判断

本次 Review 已消除大量“字段表是否存在 / 接口路径 / 请求字段 / 交易枚举 / 用户通知配置”类问题，但仍不能解除 Card 阶段 `BLOCK`。

原因：资金链路仍缺少或未闭环以下关键项：

1. Webhook 去重键是否可用 `event + data.id`。
2. 历史 PRD 交易类型与 DTC 当前枚举的映射关系。
3. AIX 内部交易处理 ID。
4. AIX 归集请求 ID。
5. `D-REQUEST-ID` 是否具备幂等语义。
6. DTC 归集结果 ID / 归集流水。当前接口文档成功响应未返回。
7. 钱包入账流水 ID。
8. Transfer Balance to Wallet 成功后如何与钱包流水 / Balance History 关联。
9. 查询余额失败与归集失败的自动重试规则。
10. 钱包入账失败的资金悬挂处理。

只有上述关键项确认后，才可更新 `card-transaction-flow.md`、`knowledge-gaps.md`、`stage-review.md`，并重新执行 Card Stage Review。

---

## 6. 来源引用

- (Ref: DTC Card Issuing API Document_20260310 (1).pdf / 2.4 Request Signature)
- (Ref: DTC Card Issuing API Document_20260310 (1).pdf / 3.3.3 transfer to wallet)
- (Ref: DTC Card Issuing API Document_20260310 (1).pdf / 3.3.4 Transaction History Of Card)
- (Ref: DTC Card Issuing API Document_20260310 (1).pdf / 3.3.5 Detail Of Card Transaction)
- (Ref: DTC Card Issuing API Document_20260310 (1).pdf / 3.3.7 Inquiry Card Balance History)
- (Ref: DTC Card Issuing API Document_20260310 (1).pdf / 3.4 WebHook / 3.4.4 Card Transaction Notify)
- (Ref: DTC Card Issuing API Document_20260310 (1).pdf / Appendix A Response Codes / Appendix B Enum List)
- (Ref: DTC Wallet OpenAPI Documentation / 4.2.4 Search Balance History)
- (Ref: [2025-11-25] AIX+Notification（push及站内信）/ 卡相关 / 卡交易成功 / 卡退款成功)
- (Ref: AIX Card交易【transaction】/ 7.3 / 8.1)
- (Ref: IMPLEMENTATION_PLAN.md / v3.2 / Stage Review Gate)
