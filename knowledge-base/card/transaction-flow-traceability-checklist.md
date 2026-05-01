---
module: card
feature: transaction-flow-traceability-checklist
version: "1.5"
status: active
source_doc: DTC接口文档/DTC Card Issuing API Document_20260310 (1).pdf；DTC Wallet OpenAPI Documentation；[2025-11-25] AIX+Notification（push及站内信）；卡交易&钱包交易状态梳理；AIX Card交易【transaction】；AIX APP V1.0【Transaction & History】；knowledge-base/card/card-transaction-flow.md；knowledge-base/card/stage-review.md；IMPLEMENTATION_PLAN.md；用户确认结论 2026-05-01
source_section: Card Issuing 2.4 / 3.3.3 / 3.3.4 / 3.3.5 / 3.3.7 / 3.4.4 / Appendix A-B；Wallet 钱包交易记录 / 钱包交易详情 / state 枚举；Notification 卡相关；Card Transaction Flow v1.2
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

本文档用于 Card Transaction Flow Gate Review 阻塞期间，将“文档已明确 / 用户已确认”和“仍需后端 / Wallet / 账务确认”的事项拆开，避免重复追问已明确事项。

确认前，仍未闭环的字段不得写入功能正文作为已生效规则。

---

## 2. Review 后已消除的问题

| 编号 | 原问题 | Review 结论 | 来源 |
|---|---|---|---|
| RESOLVED-001 | Card Transaction Flow 是否由 DTC 通知触发 | DTC 通过 `Card Transaction Notification / Card Transaction Notify` 通知 AIX 卡交易 | AIX Card交易【transaction】/ 7.3；DTC Card Issuing / 3.4.4 |
| RESOLVED-002 | DTC Webhook 重复推送时交易 ID 是否变化 | 重复推送时 `Transaction ID` 不变 | 用户确认 2026-05-01 |
| RESOLVED-003 | Webhook 是否存在独立 notification event id | 不存在独立 notification id；可按 `event + data.id` 作为通知去重依据 | 用户确认 2026-05-01；DTC Card Issuing / 3.4.4 |
| RESOLVED-004 | 哪些交易类型进入自动归集 | AIX 收到 DTC 全量通知后，只针对 `refund` / `reversal` / `deposit` 触发查卡余额；`Top-up` 已移除；其他交易类型不触发自动归集 | 用户确认 2026-05-01；AIX Card交易【transaction】/ 7.3 |
| RESOLVED-005 | DTC 交易类型枚举是否支持 refund / reversal / deposit | DTC Transaction Type 包含 `REFUND = 18`、`REVERSAL = 19`、`DEPOSIT = 22`；也包含 `TOP_UP = 1`，但 AIX 归集触发范围不再包含 Top-up | DTC Card Issuing / Appendix B；用户确认 2026-05-01 |
| RESOLVED-006 | Notification 表里的 type / status 是什么口径 | 卡交易&钱包交易状态梳理表用于 AIX 对客展示状态梳理，不作为自动归集触发规则 | 卡交易&钱包交易状态梳理；用户确认 2026-05-01 |
| RESOLVED-007 | DTC Card Transaction Notify 字段表是否存在 | DTC 接口文档提供 `Card Transaction Notify` 字段表 | DTC Card Issuing / 3.4.4 |
| RESOLVED-008 | DTC 通知里的卡交易 ID | `id` 为 `Transaction ID`，必填；可作为 DTC 卡交易记录 ID | DTC Card Issuing / 3.4.4 |
| RESOLVED-009 | DTC 原始交易 ID 字段 | `originalId` 为 `Original Transaction ID`，选填 | DTC Card Issuing / 3.4.4 |
| RESOLVED-010 | 查询卡余额使用哪个接口 | 调用 `Inquiry Card Basic Info` 查询卡余额；接口路径为 `[POST] /openapi/v1/card/inquiry-card-info` | AIX Card交易【transaction】/ 7.3；DTC Card Issuing / 3.2.15 |
| RESOLVED-011 | balance 字段是否存在及用途 | `Inquiry Card Basic Info` 响应含 `balance`；该字段作为归集金额依据 | DTC Card Issuing / 3.2.15；AIX Card交易【transaction】/ 7.3 |
| RESOLVED-012 | 归集金额如何计算 | 当 `balance > 0` 时，调用 transfer to wallet，入参 `amount = balance` | AIX Card交易【transaction】/ 7.3 |
| RESOLVED-013 | Transfer Balance to Wallet 接口路径 | `[POST] /openapi/v1/card/transfer-to-wallet` | DTC Card Issuing / 3.3.3 |
| RESOLVED-014 | Transfer Balance to Wallet 请求字段 | 请求字段只有 `cardId` 与 `amount`，均为必填 | DTC Card Issuing / 3.3.3 |
| RESOLVED-015 | Transfer Balance to Wallet 成功响应字段 | 示例仅返回 `header.success = true`；用户确认不会返回归集业务流水 | DTC Card Issuing / 3.3.3；用户确认 2026-05-01 |
| RESOLVED-016 | Transfer Balance to Wallet 错误码 | 可能错误码包括 `00006`、`20004`、`31005`、`31006`、`31022`、`31033`、`31038` | DTC Card Issuing / 3.3.3 |
| RESOLVED-017 | DTC API 请求追踪 Header | 请求 Header 需要 `D-REQUEST-ID`，描述为 client-generated unique request identifier；文档未明确其幂等语义，因此不写成 DTC 幂等键 | DTC Card Issuing / 2.4 |
| RESOLVED-018 | 归集失败是否自动重试 | 失败不重试，发送异常告警至监控群 | 用户确认 2026-05-01；AIX Card交易【transaction】/ 7.3 |
| RESOLVED-019 | 卡交易列表 / 详情接口 | 卡交易列表、卡交易详情接口和 `transactionId` 入参已明确 | DTC Card Issuing / 3.3.4 / 3.3.5 |
| RESOLVED-020 | 卡余额历史查询字段 | `inquiry-card-balance-history` 支持 `relatedId`，返回 `id`、`type`、`balanceBefore`、`changeAmount`、`balanceAfter`、`currency`、`relatedId` | DTC Card Issuing / 3.3.7 |
| RESOLVED-021 | DTC Transaction Status 枚举 | 包含 `PENDING 0`、`AUTHORIZED 101`、`SUCCESS 200`、`CAPTURED 221`、`REVERSED 301`、`CANCELLED 302`、`REFUNDED 401`、`DENIED 900`、`EXPIRED 990` | DTC Card Issuing / Appendix B |
| RESOLVED-022 | 钱包交易记录 / 详情是否有交易 ID | 钱包交易记录和详情出参均包含 `id`，类型 Long，含义为交易 id | 用户确认 2026-05-01；DTC Wallet OpenAPI |
| RESOLVED-023 | 单笔钱包交易详情入参 | 单笔钱包交易详情入参为 `transactionId`，含义为 Unique transaction ID from DTC；但未说明与 Card `data.id` 或 `D-REQUEST-ID` 的关联 | 用户确认 2026-05-01；DTC Wallet OpenAPI |
| RESOLVED-024 | 钱包入账状态字段与枚举 | 钱包交易状态字段为 `state`；枚举为 `PENDING`、`PROCESSING`、`AUTHORIZED`、`COMPLETED`、`REJECTED`、`CLOSED` | 用户确认 2026-05-01；DTC Wallet OpenAPI |
| RESOLVED-025 | 用户通知与钱包入账关系 | 正常情况下用户收到退款 / 卡交易成功通知后，预期资金已归集至 Wallet；极端情况下可能卡已收到钱但转 Wallet 失败，此时用户看不到资金 | 用户确认 2026-05-01 |
| RESOLVED-026 | DTC transfer 成功但钱包未入账如何发现 | 当前无法系统自动发现，主要依赖用户反馈 | 用户确认 2026-05-01 |

---

## 3. Review 后仍需确认的问题

### 3.1 需要 AIX 后端确认

| 编号 | 问题 |
|---|---|
| BE-001 | 收到 `Card Transaction Notify` 后，AIX 内部是否生成交易处理 ID；字段名是什么。 |
| BE-002 | AIX 是否完整落库 DTC Webhook 原始报文，包括 `event`、`clientId`、`data.id`、`originalId`、`processorTransactionId`、`referenceNo`、`state`、`type`、`indicator` 等字段。 |
| BE-003 | AIX 对重复 Webhook 的去重规则是否为 `event + data.id`。 |
| BE-004 | AIX 归集触发条件是否只判断交易类型为 `REFUND = 18`、`REVERSAL = 19`、`DEPOSIT = 22`，还是还需要额外判断 `state` / `indicator`。 |
| BE-005 | 发起 `Transfer Balance to Wallet` 前，AIX 是否生成内部归集请求 ID；字段名是什么。 |
| BE-006 | AIX 发起 `Transfer Balance to Wallet` 时，`D-REQUEST-ID` 如何生成、保存，并与内部归集请求 ID 关联。 |
| BE-007 | DTC 卡交易 `data.id`、AIX 内部交易处理 ID、AIX 归集请求 ID、`D-REQUEST-ID`、钱包交易 `id` 之间如何关联。 |
| BE-008 | 查询 `balance` 失败时如何处理：是否告警、是否进入待处理队列、是否人工介入。 |
| BE-009 | 归集失败告警后，是否有后台人工补偿入口；如果有，入口和操作边界是什么。 |
| BE-010 | 已知“系统原因开发跟进、金额大于卡余额产品跟进”之外，是否还有其他失败类型与责任分派。 |

### 3.2 需要 Wallet / 账务确认

| 编号 | 问题 |
|---|---|
| WALLET-001 | 钱包交易 `id` 如何与 DTC 卡交易 `data.id`、AIX 归集请求 ID 或 `D-REQUEST-ID` 关联。当前只确认钱包交易详情入参是 `transactionId`，未确认关联规则。 |
| WALLET-002 | Wallet `Search Balance History.relatedId` 在卡余额转 wallet 场景下应取哪个 ID。 |
| WALLET-003 | card balance 转入 wallet 时，入账币种口径是否与 card currency 完全一致。 |
| WALLET-004 | 财务 / 运营最终对账时，用哪些字段串起 DTC 卡交易通知、AIX 归集请求、DTC transfer 调用和钱包交易 `id`。 |

---

## 4. Gate Review 判断

本次 Review 继续消除 Wallet 侧三个问题：钱包交易记录 / 详情均有 `id`，钱包详情入参为 `transactionId`，钱包交易状态字段为 `state` 且枚举已明确。

Card 阶段仍不能解除 `BLOCK`，原因是资金链路仍缺少或未闭环以下关键项：

1. AIX 内部交易处理 ID。
2. AIX 归集请求 ID。
3. AIX 对 `D-REQUEST-ID` 的生成、保存和关联规则。
4. DTC `data.id` → AIX 处理记录 → 归集请求 → Wallet 交易 `id` 的链路关系。
5. Wallet `relatedId` 在卡余额转 wallet 场景下的取值。
6. 查询余额失败处理。
7. 归集失败后的人工补偿入口。
8. 最终对账字段组合。

只有上述关键项确认后，才可更新 `card-transaction-flow.md`、`knowledge-gaps.md`、`stage-review.md`，并重新执行 Card Stage Review。

---

## 5. 来源引用

- (Ref: DTC Card Issuing API Document_20260310 (1).pdf / 2.4 Request Signature)
- (Ref: DTC Card Issuing API Document_20260310 (1).pdf / 3.3.3 transfer to wallet)
- (Ref: DTC Card Issuing API Document_20260310 (1).pdf / 3.3.4 Transaction History Of Card)
- (Ref: DTC Card Issuing API Document_20260310 (1).pdf / 3.3.5 Detail Of Card Transaction)
- (Ref: DTC Card Issuing API Document_20260310 (1).pdf / 3.3.7 Inquiry Card Balance History)
- (Ref: DTC Card Issuing API Document_20260310 (1).pdf / 3.4.4 Card Transaction Notify)
- (Ref: DTC Wallet OpenAPI Documentation / 钱包交易记录 / 钱包交易详情 / state 枚举)
- (Ref: [2025-11-25] AIX+Notification（push及站内信）/ 卡相关 / 卡交易成功 / 卡退款成功)
- (Ref: 卡交易&钱包交易状态梳理 / 卡交易状态映射)
- (Ref: 用户确认结论 / 2026-05-01)
- (Ref: IMPLEMENTATION_PLAN.md / v3.3 / Stage Review Gate)
