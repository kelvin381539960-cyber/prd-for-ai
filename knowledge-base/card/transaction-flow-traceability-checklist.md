---
module: card
feature: transaction-flow-traceability-checklist
version: "1.6"
status: migrated-reference
source_doc: DTC接口文档/DTC Card Issuing API Document_20260310 (1).pdf；DTC Wallet OpenAPI Documentation；[2025-11-25] AIX+Notification（push及站内信）；卡交易&钱包交易状态梳理；AIX Card交易【transaction】；AIX APP V1.0【Transaction & History】；knowledge-base/card/card-transaction-flow.md；knowledge-base/card/stage-review.md；knowledge-base/transaction/reconciliation.md；knowledge-base/changelog/knowledge-gaps.md；IMPLEMENTATION_PLAN.md；用户确认结论 2026-05-01；用户确认结论 2026-05-02
source_section: Card Issuing 2.4 / 3.3.3 / 3.3.4 / 3.3.5 / 3.3.7 / 3.4.4 / Appendix A-B；Wallet 钱包交易记录 / 钱包交易详情 / state 枚举；Notification 卡相关；ALL-GAP 总表
last_updated: 2026-05-02
owner: 吴忆锋
depends_on:
  - card/card-transaction-flow
  - card/stage-review
  - transaction/reconciliation
  - changelog/knowledge-gaps
---

# Card Transaction Flow 资金追踪字段确认稿

## 1. 文档定位

本文档是 Card Transaction Flow 资金追踪历史确认稿，当前状态为 `migrated-reference`。

本文档不再作为模块级 checklist / gaps 表维护。历史未确认项已无损迁移到 `knowledge-base/changelog/knowledge-gaps.md` 的 ALL-GAP 总表；后续只维护 ALL-GAP。

本文档只保留两类内容：

1. Review 后已消除 / 已确认的问题，用于避免重复追问。
2. 历史 BE / WALLET 问题到 ALL-GAP 的映射，用于追溯。

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

## 3. 历史 BE 问题到 ALL-GAP 映射

| 原编号 | 原问题 | 当前 ALL-GAP |
|---|---|---|
| BE-001 | 收到 `Card Transaction Notify` 后，AIX 内部是否生成交易处理 ID；字段名是什么 | ALL-GAP-019 |
| BE-002 | AIX 是否完整落库 DTC Webhook 原始报文，包括 `event`、`clientId`、`data.id`、`originalId`、`processorTransactionId`、`referenceNo`、`state`、`type`、`indicator` 等字段 | ALL-GAP-022、ALL-GAP-036 |
| BE-003 | AIX 对重复 Webhook 的去重规则是否为 `event + data.id` | ALL-GAP-023 |
| BE-004 | AIX 归集触发条件是否只判断交易类型为 `REFUND = 18`、`REVERSAL = 19`、`DEPOSIT = 22`，还是还需要额外判断 `state` / `indicator` | ALL-GAP-024 |
| BE-005 | 发起 `Transfer Balance to Wallet` 前，AIX 是否生成内部归集请求 ID；字段名是什么 | ALL-GAP-020 |
| BE-006 | AIX 发起 `Transfer Balance to Wallet` 时，`D-REQUEST-ID` 如何生成、保存，并与内部归集请求 ID 关联 | ALL-GAP-021 |
| BE-007 | DTC 卡交易 `data.id`、AIX 内部交易处理 ID、AIX 归集请求 ID、`D-REQUEST-ID`、钱包交易 `id` 之间如何关联 | ALL-GAP-017、ALL-GAP-018、ALL-GAP-019、ALL-GAP-020、ALL-GAP-021 |
| BE-008 | 查询 `balance` 失败时如何处理：是否告警、是否进入待处理队列、是否人工介入 | ALL-GAP-025 |
| BE-009 | 归集失败告警后，是否有后台人工补偿入口；如果有，入口和操作边界是什么 | ALL-GAP-026 |
| BE-010 | 已知“系统原因开发跟进、金额大于卡余额产品跟进”之外，是否还有其他失败类型与责任分派 | ALL-GAP-039 |

## 4. 历史 WALLET / 账务问题到 ALL-GAP 映射

| 原编号 | 原问题 | 当前 ALL-GAP |
|---|---|---|
| WALLET-001 | 钱包交易 `id` 如何与 DTC 卡交易 `data.id`、AIX 归集请求 ID 或 `D-REQUEST-ID` 关联 | ALL-GAP-017、ALL-GAP-018 |
| WALLET-002 | Wallet `Search Balance History.relatedId` 在卡余额转 wallet 场景下应取哪个 ID | ALL-GAP-014 |
| WALLET-003 | card balance 转入 wallet 时，入账币种口径是否与 card currency 完全一致 | ALL-GAP-028 |
| WALLET-004 | 财务 / 运营最终对账时，用哪些字段串起 DTC 卡交易通知、AIX 归集请求、DTC transfer 调用和钱包交易 `id` | ALL-GAP-029 |

## 5. 当前 Gate Review 判断

Card Transaction Flow 不再标记为 `BLOCK`，而是 `PARTIAL PASS`。

原因：已明确的接口、字段和用户确认结论已可支持当前知识库继续推进；资金追踪与对账缺口已统一迁移到 ALL-GAP，并由 `transaction/reconciliation.md` 承接边界。

未确认项不得写成事实。后续收到后端 / Wallet / 账务确认后，统一回填：

1. `knowledge-base/changelog/knowledge-gaps.md`
2. `knowledge-base/card/card-transaction-flow.md`
3. `knowledge-base/transaction/reconciliation.md`
4. `knowledge-base/card/stage-review.md`
5. `IMPLEMENTATION_PLAN.md`

## 6. 来源引用

- (Ref: DTC Card Issuing API Document_20260310 (1).pdf / 2.4 Request Signature)
- (Ref: DTC Card Issuing API Document_20260310 (1).pdf / 3.3.3 transfer to wallet)
- (Ref: DTC Card Issuing API Document_20260310 (1).pdf / 3.3.4 Transaction History Of Card)
- (Ref: DTC Card Issuing API Document_20260310 (1).pdf / 3.3.5 Detail Of Card Transaction)
- (Ref: DTC Card Issuing API Document_20260310 (1).pdf / 3.3.7 Inquiry Card Balance History)
- (Ref: DTC Card Issuing API Document_20260310 (1).pdf / 3.4.4 Card Transaction Notify)
- (Ref: DTC Wallet OpenAPI Documentation / 钱包交易记录 / 钱包交易详情 / state 枚举)
- (Ref: [2025-11-25] AIX+Notification（push及站内信）/ 卡相关 / 卡交易成功 / 卡退款成功)
- (Ref: 卡交易&钱包交易状态梳理 / 卡交易状态映射)
- (Ref: knowledge-base/card/card-transaction-flow.md / v1.2)
- (Ref: knowledge-base/transaction/reconciliation.md / v1.0)
- (Ref: knowledge-base/changelog/knowledge-gaps.md / ALL-GAP 总表)
- (Ref: 用户确认结论 / 2026-05-01)
- (Ref: 用户确认结论 / 2026-05-02 / ALL-GAP 唯一总表与无损迁移规则)
