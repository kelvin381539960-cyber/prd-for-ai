---
module: card
feature: transaction-flow-traceability-checklist
version: "1.4"
status: active
source_doc: DTC接口文档/DTC Card Issuing API Document_20260310 (1).pdf；DTC Wallet OpenAPI Documentation；[2025-11-25] AIX+Notification（push及站内信）；卡交易&钱包交易状态梳理；AIX Card交易【transaction】；AIX APP V1.0【Transaction & History】；knowledge-base/card/card-transaction-flow.md；knowledge-base/card/stage-review.md；IMPLEMENTATION_PLAN.md；用户确认结论 2026-05-01
source_section: Card Issuing 2.4 / 3.3.3 / 3.3.4 / 3.3.5 / 3.3.7 / 3.4 / 3.4.4 / Appendix A / Appendix B；Wallet 4.2.4；Notification 卡相关；卡交易&钱包交易状态梳理；IMPLEMENTATION_PLAN v3.2
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

本文档用于 Card Transaction Flow Gate Review 阻塞期间，将“文档已明确 / 用户已确认”和“仍需 DTC / 后端 / Wallet 确认”的事项拆开，避免重复追问已明确事项。

确认前，仍未闭环的字段不得写入功能正文作为已生效规则。

---

## 2. Review 后已消除的问题

以下内容已能从历史 PRD、DTC 接口文档、通知配置、状态梳理表或用户确认中找到，不再作为对外确认问题。

| 编号 | 原问题 | Review 结论 | 来源 |
|---|---|---|---|
| RESOLVED-001 | Card Transaction Flow 是否由 DTC 通知触发 | 已明确：DTC 通过 `Card Transaction Notification / Card Transaction Notify` 通知 AIX 卡交易 | AIX Card交易【transaction】/ 7.3；DTC Card Issuing / 3.4.4 |
| RESOLVED-002 | DTC Webhook 重复推送时交易 ID 是否变化 | 已确认：重复推送时 `Transaction ID` 不变 | 用户确认 2026-05-01 |
| RESOLVED-003 | Webhook 是否存在独立 notification event id | 已确认：不存在独立 notification id；可按 `event + data.id` 作为通知去重依据 | 用户确认 2026-05-01；DTC Card Issuing / 3.4.4 |
| RESOLVED-004 | 哪些交易类型进入自动归集 | 已确认：AIX 收到 DTC 全量通知后，只针对 `refund` / `reversal` / `deposit` 触发查卡余额；`Top-up` 已移除；其他交易类型不触发自动归集 | 用户确认 2026-05-01；AIX Card交易【transaction】/ 7.3 |
| RESOLVED-005 | DTC 交易类型枚举是否支持 refund / reversal / deposit | 已明确：DTC Transaction Type 包含 `REFUND = 18`、`REVERSAL = 19`、`DEPOSIT = 22`；也包含 `TOP_UP = 1`，但 AIX 归集触发范围不再包含 Top-up | DTC Card Issuing / Appendix B；用户确认 2026-05-01 |
| RESOLVED-006 | Notification 表里的 type / status 是什么口径 | 已补充：卡交易&钱包交易状态梳理表用于 AIX 对客展示状态梳理，不作为自动归集触发规则 | 卡交易&钱包交易状态梳理；用户确认 2026-05-01 |
| RESOLVED-007 | DTC Card Transaction Notify 字段表是否存在 | 已明确：DTC 接口文档提供 `Card Transaction Notify` 字段表 | DTC Card Issuing / 3.4.4 |
| RESOLVED-008 | DTC 通知里的卡交易 ID | 已明确：`id` 为 `Transaction ID`，必填；可作为 DTC 卡交易记录 ID | DTC Card Issuing / 3.4.4 |
| RESOLVED-009 | DTC 原始交易 ID 字段 | 已明确：`originalId` 为 `Original Transaction ID`，选填 | DTC Card Issuing / 3.4.4 |
| RESOLVED-010 | 通知基础关联字段 | 已明确：通知包含 `clientId`、`cardId`、`cardToken`、`truncatedCardNumber`、`processorTransactionId`、`referenceNo`、`acquirerReferenceNo` 等字段 | DTC Card Issuing / 3.4.4 |
| RESOLVED-011 | 通知金额与币种字段 | 已明确：通知包含 `amount`、`currency`、`requestAmount`、`requestCurrency`、`indicator` | DTC Card Issuing / 3.4.4 |
| RESOLVED-012 | 通知交易时间字段 | 已明确：通知包含 `transactionDate`、`transactionTime`、`confirmedTime`、`createdDate` | DTC Card Issuing / 3.4.4 |
| RESOLVED-013 | 查询卡余额使用哪个接口 | 已明确：调用 `Retrieve Basic Card Info / Inquiry Card Basic Info` 查询卡余额；接口路径为 `[POST] /openapi/v1/card/inquiry-card-info` | AIX Card交易【transaction】/ 7.3；DTC Card Issuing / 3.2.15 |
| RESOLVED-014 | balance 字段是否存在及用途 | 已明确：`Inquiry Card Basic Info` 响应含 `balance`；历史 PRD 写明该字段作为归集金额依据 | DTC Card Issuing / 3.2.15；AIX Card交易【transaction】/ 7.3 |
| RESOLVED-015 | 归集金额如何计算 | 已明确：当 `balance > 0` 时，调用 transfer to wallet，入参 `amount = balance` | AIX Card交易【transaction】/ 7.3 |
| RESOLVED-016 | balance = 0 如何处理 | 已明确：当卡当前余额 `balance = 0` 时，流程终止 | AIX Card交易【transaction】/ 7.3 |
| RESOLVED-017 | Transfer Balance to Wallet 接口路径 | 已明确：接口路径为 `[POST] /openapi/v1/card/transfer-to-wallet` | DTC Card Issuing / 3.3.3 |
| RESOLVED-018 | Transfer Balance to Wallet 请求字段 | 已明确：请求字段只有 `cardId` 与 `amount`，均为必填 | DTC Card Issuing / 3.3.3 |
| RESOLVED-019 | Transfer Balance to Wallet 成功响应字段 | 已明确：示例仅返回 `header.success = true`；用户确认不会返回归集业务流水 | DTC Card Issuing / 3.3.3；用户确认 2026-05-01 |
| RESOLVED-020 | Transfer Balance to Wallet 错误码 | 已明确：可能错误码包括 `00006`、`20004`、`31005`、`31006`、`31022`、`31033`、`31038` | DTC Card Issuing / 3.3.3 |
| RESOLVED-021 | DTC API 请求追踪 Header | 已明确：请求 Header 需要 `D-REQUEST-ID`，描述为 client-generated unique request identifier；文档未明确其幂等语义，因此不将其写成 DTC 幂等键 | DTC Card Issuing / 2.4 |
| RESOLVED-022 | 归集失败是否自动重试 | 已确认：失败不重试，发送异常告警至监控群 | 用户确认 2026-05-01；AIX Card交易【transaction】/ 7.3 |
| RESOLVED-023 | 卡交易列表接口路径和字段 | 已明确：`[POST] /openapi/v1/card/inquiry-card-transaction`，返回 `id`、`type`、`state`、`cardId`、`originalId`、`processorTransactionId`、`amount`、`currency`、`referenceNo` 等字段 | DTC Card Issuing / 3.3.4 |
| RESOLVED-024 | 卡交易详情接口路径和字段 | 已明确：`[POST] /openapi/v1/card/inquiry-card-transaction-detail`，入参为 `transactionId`，响应字段与交易列表基本一致 | DTC Card Issuing / 3.3.5 |
| RESOLVED-025 | 卡余额历史查询字段 | 已明确：`[POST] /openapi/v1/card/inquiry-card-balance-history`，支持 `relatedId`，返回 `id`、`type`、`balanceBefore`、`changeAmount`、`balanceAfter`、`currency`、`relatedId` | DTC Card Issuing / 3.3.7 |
| RESOLVED-026 | DTC Transaction Status 枚举 | 已明确：`PENDING 0`、`AUTHORIZED 101`、`SUCCESS 200`、`CAPTURED 221`、`REVERSED 301`、`CANCELLED 302`、`REFUNDED 401`、`DENIED 900`、`EXPIRED 990` | DTC Card Issuing / Appendix B |
| RESOLVED-027 | DTC DeniedReason 枚举 | 已明确包含 `INSUFFICIENT_FUNDS`、`INVALID_ORIGINAL_TRANSACTION`、`INVALID_TRANSACTION`、`INVALID_AMOUNT`、`SYSTEM_ERROR`、`INSTITUTION_LIMIT` 等 | DTC Card Issuing / Appendix B |
| RESOLVED-028 | 归集失败责任初始分派 | 已明确：系统原因由开发跟进；交易金额大于卡余额由产品侧跟进 | AIX Card交易【transaction】/ 7.3 |
| RESOLVED-029 | 归集成功后的业务结果 | 已明确：若成功，资金已转入用户钱包，流程结束 | AIX Card交易【transaction】/ 7.3 |
| RESOLVED-030 | 钱包交易历史查询能力 | 已明确：Wallet `Search Balance History` 可查询钱包交易历史，返回 `activityType`、`relatedId`、`time`、`state` 等字段 | DTC Wallet OpenAPI / 4.2.4 |
| RESOLVED-031 | 卡交易成功是否通知用户 | 已明确：通知配置存在“卡交易成功”，触发源为 `3.4.4 Card Transaction Notify`，条件包含 `indicator=debit`、`status=101 AUTHORIZED`，跳转卡交易详情页 | AIX Notification / 卡相关 |
| RESOLVED-032 | 卡退款成功是否通知用户 | 已明确：通知配置存在“卡退款成功”，触发源为 `3.4.4 Card Transaction Notify`，条件包含 `indicator=credit`，并列出 refund / reversed 场景，跳转卡交易详情页 | AIX Notification / 卡相关 |
| RESOLVED-033 | 用户通知字段参数 | 已明确：卡交易 / 退款通知参数包含 `merchant_name`、`amount`、`currency`、`transaction_time`，文案参数还包含 `full_name`、`last 4` | AIX Notification / 卡相关 |
| RESOLVED-034 | 用户通知与钱包入账关系 | 已确认：正常情况下用户收到退款 / 卡交易成功通知后，预期资金已归集至 Wallet；极端情况下可能出现卡已收到钱但转 Wallet 失败，此时用户看不到资金，因为对外只展示 Wallet 资金，不展示卡资金 | 用户确认 2026-05-01 |
| RESOLVED-035 | DTC transfer 成功但钱包未入账如何发现 | 已确认：系统无法自动发现，主要依赖用户反馈 | 用户确认 2026-05-01 |

---

## 3. Review 后仍需确认的问题

以下问题在现有文档与用户确认中仍未闭环，继续保留为待确认项。

### 3.1 需要 AIX 后端确认

请后端确认以下内容：

1. 收到 `Card Transaction Notify` 后，AIX 内部是否生成交易处理 ID；字段名是什么。
2. AIX 是否完整落库 DTC Webhook 原始报文，包括 `event`、`clientId`、`data.id`、`originalId`、`processorTransactionId`、`referenceNo`、`state`、`type`、`indicator` 等字段。
3. AIX 对重复 Webhook 的去重规则是否为 `event + data.id`；已知 DTC 重复推送时 `Transaction ID` 不变，且无独立 notification id。
4. AIX 归集触发条件是否只判断交易类型为 `REFUND = 18`、`REVERSAL = 19`、`DEPOSIT = 22`，还是还需要额外判断 `state` / `indicator`。
5. 发起 `Transfer Balance to Wallet` 前，AIX 是否生成内部归集请求 ID；字段名是什么。
6. AIX 发起 `Transfer Balance to Wallet` 时，`D-REQUEST-ID` 如何生成、保存，并与内部归集请求 ID 关联。
7. DTC 卡交易 `data.id`、AIX 内部交易处理 ID、AIX 归集请求 ID、`D-REQUEST-ID`、后续钱包流水之间如何关联。
8. 查询 `balance` 失败时如何处理：是否告警、是否进入待处理队列、是否人工介入。
9. 归集失败告警后，是否有后台人工补偿入口；如果有，入口和操作边界是什么。
10. 已知“系统原因开发跟进、金额大于卡余额产品跟进”之外，是否还有其他失败类型与责任分派。

### 3.2 需要 Wallet / 账务确认

请 Wallet / 账务侧确认以下内容：

1. `Transfer Balance to Wallet` 成功后，钱包侧是否生成入账流水 ID；字段名是什么。
2. 钱包流水如何关联卡交易 `data.id`、AIX 归集请求 ID 或 `D-REQUEST-ID`。
3. Wallet `Search Balance History.relatedId` 在卡余额转钱包场景下应取哪个 ID。
4. card balance 转入 wallet 时，入账币种口径是否与 card currency 完全一致。
5. 钱包入账是否存在 pending / success / failed 等状态；如存在，字段与枚举是什么。
6. 财务 / 运营最终对账时，用哪些字段串起 DTC 卡交易通知、AIX 归集请求、DTC transfer 调用和钱包流水。

---

## 4. 当前对外发送精简版

可直接复制以下内容发给后端 / Wallet / 账务负责人。

```text
各位好，Card Transaction Flow 资金归集链路已消除一轮问题，现在主要剩后端、Wallet 和账务链路确认。

已确认：
1. DTC Card Transaction Notify 重复推送时 Transaction ID 不变。
2. DTC 没有独立 notification id，可按 event + data.id 作为通知去重依据。
3. AIX 只针对 refund / reversal / deposit 触发查卡余额和 transfer-to-wallet；Top-up 已移除，其他交易类型不触发。
4. DTC Transaction Type 中对应类型包括 REFUND=18、REVERSAL=19、DEPOSIT=22。
5. Transfer Balance to Wallet 路径为 [POST] /openapi/v1/card/transfer-to-wallet，请求字段只有 cardId 和 amount。
6. Transfer Balance to Wallet 成功响应只返回 header.success=true，不返回归集流水。
7. 归集失败不自动重试，发送异常告警至监控群。
8. 正常情况下用户收到退款 / 卡交易成功通知后，预期资金已进入 Wallet；极端情况下可能卡有钱但转 Wallet 失败，用户无法看到资金，因为前端只展示 Wallet 资金，不展示卡资金。
9. DTC transfer 成功但钱包未入账时，当前无法系统自动发现，主要依赖用户反馈。

仍需确认：

后端：
1. 收到 Card Transaction Notify 后，AIX 是否生成内部交易处理 ID；字段名是什么。
2. DTC Webhook 原始报文是否完整落库。
3. 重复通知是否按 event + data.id 去重。
4. 归集触发条件是否只判断 type=REFUND/REVERSAL/DEPOSIT，还是还要判断 state / indicator。
5. 发起 Transfer Balance to Wallet 前是否生成归集请求 ID；字段名是什么。
6. D-REQUEST-ID 如何生成、保存，并与归集请求 ID 关联。
7. DTC data.id、AIX 内部交易处理 ID、归集请求 ID、D-REQUEST-ID、钱包流水之间如何串联。
8. 查询 balance 失败如何处理。
9. 归集失败告警后是否有后台人工补偿入口。

Wallet / 账务：
1. Transfer Balance to Wallet 成功后，钱包侧是否生成入账流水 ID；字段名是什么。
2. 钱包流水如何关联 DTC data.id、AIX 归集请求 ID 或 D-REQUEST-ID。
3. Wallet Search Balance History.relatedId 在卡余额转钱包场景下取哪个 ID。
4. card balance 转 wallet 的入账币种和入账状态字段是什么。
5. 最终对账用哪些字段串起 DTC 通知、AIX 归集请求、DTC transfer 调用和钱包流水。
```

---

## 5. Gate Review 判断

本次 Review 已消除 DTC 通知去重、独立通知 ID、交易类型范围、Top-up 是否触发、transfer-to-wallet 是否返回归集流水、归集失败是否重试、用户通知与钱包展示关系等问题。

Card 阶段仍不能解除 `BLOCK`，原因是资金链路仍缺少或未闭环以下关键项：

1. AIX 内部交易处理 ID。
2. AIX 归集请求 ID。
3. AIX 对 `D-REQUEST-ID` 的生成、保存和关联规则。
4. DTC `data.id` → AIX 处理记录 → 归集请求 → Wallet 流水的链路关系。
5. Wallet 入账流水 ID。
6. Wallet `relatedId` 在卡余额转钱包场景下的取值。
7. 查询余额失败处理。
8. 归集失败后的人工补偿入口。
9. 最终对账字段组合。

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
- (Ref: 卡交易&钱包交易状态梳理 / 卡交易状态映射)
- (Ref: AIX Card交易【transaction】/ 7.3 / 8.1)
- (Ref: 用户确认结论 / 2026-05-01)
- (Ref: IMPLEMENTATION_PLAN.md / v3.2 / Stage Review Gate)
