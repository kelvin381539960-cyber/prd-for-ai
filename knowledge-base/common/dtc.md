---
module: common
feature: dtc-dependency
version: "1.3"
status: active
source_doc: IMPLEMENTATION_PLAN.md；DTC接口文档/DTC Wallet OpenAPI Document20260126 (1).docx；DTC接口文档/卡交易&钱包交易状态梳理 (1).docx；knowledge-base/wallet/deposit.md；knowledge-base/wallet/transaction-history.md；knowledge-base/wallet/balance.md；knowledge-base/transaction/history.md；knowledge-base/transaction/detail.md；knowledge-base/common/walletconnect.md；knowledge-base/common/notification.md；knowledge-base/common/errors.md；knowledge-base/changelog/knowledge-gaps.md
source_section: DTC Wallet OpenAPI / 3.4 Crypto Deposit；4.2.4 Search Balance History；4.4 Crypto；4.6 Webhook Service；Appendix ActivityType；Transaction History v1.1；Transaction Detail v1.1
last_updated: 2026-05-01
owner: 吴忆锋
depends_on:
  - wallet/deposit
  - wallet/transaction-history
  - wallet/balance
  - transaction/history
  - transaction/detail
  - common/walletconnect
  - common/notification
  - common/errors
  - changelog/knowledge-gaps
---

# DTC Dependency 外部依赖边界

## 1. 功能定位

DTC 是 AIX 的外部供应商系统，不是 AIX 内部系统，也不是本知识库需要维护的供应商系统说明书。

本文只沉淀 AIX 对 DTC 的依赖边界：AIX 使用了哪些 DTC 能力、依赖哪些字段 / 状态 / 回调 / 响应、哪些规则来自 DTC 文档、哪些不能由 AIX 假设。

## 2. 当前已确认 DTC 依赖事实

| 项目 | 结论 | 来源 | AIX 侧处理 |
|---|---|---|---|
| DTC Wallet OpenAPI | DTC Wallet OpenAPI 是第三方集成 DTC Wallet solutions 的 JSON REST API | DTC Wallet OpenAPI / Overview | 作为外部依赖，不维护 DTC 内部逻辑 |
| DTC 时间 | 时间相关值默认基于 Singapore Timezone | DTC Wallet OpenAPI / Overview | AIX 展示或对账需注意时区 |
| API 安全 | HTTPS 必须；IP whitelist 可选；OAuth 2.0；Signature | DTC Wallet OpenAPI / Security Standards | 记录为接入依赖，不补实现 |
| Crypto Deposit | Crypto business 包含 whitelisting、deposit、withdrawal | DTC Wallet OpenAPI / 3.4 Crypto Deposit | 可作为 WalletConnect / Crypto Deposit 依赖边界 |
| Deposit Address | destinationAddress 由 DTC 自动分配，调用 `[POST] /openapi/v1/crypto-account/deposit-address/search-obj` 返回充值收款地址 | DTC Wallet OpenAPI / 3.4 Crypto Deposit | 用于 Deposit 收款地址来源 |
| Sender Address Whitelist | Crypto 充值涉及 senderAddress 和 destinationAddress，用户需将 senderAddress 加入 whitelist 并 enable | DTC Wallet OpenAPI / 3.4 Crypto Deposit | 只作为 Crypto Deposit 规则；是否所有 GTR / WC 场景适用仍需按路径确认 |
| Risk Withheld | 未添加 senderAddress 白名单时，交易会被设为 risky transaction，status=102 Risk Withheld | DTC Wallet OpenAPI / 3.4 Crypto Deposit | 可作为 Deposit 风控 / on-hold 边界 |
| Whitelist 后自动成功 | 用户继续加白并 enable 后，交易会自动变为 success | DTC Wallet OpenAPI / 3.4 Crypto Deposit | 只记录 DTC 规则，不补 AIX 页面处理 |
| Search Balance History | `[GET] /openapi/v1/wallet/balance/history/search` 查询 client wallet transaction history | DTC Wallet OpenAPI / 4.2.4 | Wallet History 来源之一 |
| ActivityType | `FIAT_DEPOSIT=6`、`CRYPTO_DEPOSIT=10`、`DTC_WALLET=13`、`CARD_PAYMENT_REFUND=20` | DTC Wallet OpenAPI / Appendix ActivityType | 可用于 Wallet 交易分类，不等同产品路径 |
| Card Transaction Notify | DTC 全量通知 AIX 卡交易 | Card Transaction Flow / DTC Card Issuing | AIX 只针对 refund / reversal / deposit 触发查卡余额和归集 |
| `D-REQUEST-ID` | DTC API 请求唯一标识 Header | Card Transaction Flow / DTC Card Issuing | 只记录为请求唯一标识；不写成幂等键 |

## 3. Crypto Deposit / WalletConnect 依赖边界

DTC 文档描述的是 Crypto Deposit 通用依赖，不直接等同于 AIX WalletConnect 完整产品流程。AIX 可以引用以下外部依赖事实：

| 依赖点 | 已确认 | 仍需 AIX 确认 |
|---|---|---|
| 收款地址 | DTC 自动分配 destinationAddress | AIX 页面如何展示 / 复制 / 二维码 |
| 发送地址 | Crypto 充值涉及 senderAddress | WalletConnect 场景如何获取 / 校验 senderAddress |
| 白名单 | senderAddress 需要加入 whitelist 并 enable | GTR / WC 是否同一规则；加白发生在入金前还是入金后 |
| 风控状态 | 未加白会进入 Risk Withheld，status=102 | AIX 对客展示状态、通知、人工处理 |
| 状态恢复 | 加白成功后交易自动变为 success | AIX 是否监听 webhook / 刷新交易状态 |

## 4. Wallet History / Balance History 依赖边界

| 能力 | 已确认 | 待补 |
|---|---|---|
| Search Balance History endpoint | `[GET] /openapi/v1/wallet/balance/history/search` | 完整 response 字段 |
| Request filters | `currency`、`type`、`yearMonth`、`createTimeStart` 等 | 完整分页字段和前端是否暴露 |
| `type` | 引用 ActivityType | 前端展示分类映射 |
| `relatedId` | Search Balance History / Card Balance History 中存在相关字段 | Wallet `relatedId` 在 GTR / WC / Card 归集场景下的具体取值仍未确认 |
| `activityType` | ActivityType 枚举已部分确认 | 完整枚举是否全部用于 AIX 待确认 |
| `state` | Wallet 交易状态字段 | 与 Deposit `success` / `Risk Withheld` 的映射待补 |

## 5. ActivityType 边界

| 枚举 | 值 | 含义 | AIX 侧处理 |
|---|---:|---|---|
| `FIAT_DEPOSIT` | 6 | Fiat Deposit | 可作为法币入金分类引用；不得直接写成 GTR |
| `CRYPTO_DEPOSIT` | 10 | Stablecoin Deposit | 可作为 Crypto / Stablecoin 入金分类引用；不得直接写成 WalletConnect |
| `DTC_WALLET` | 13 | DTC Wallet Payment | 可作为 DTC Wallet Payment 分类引用 |
| `CARD_PAYMENT_REFUND` | 20 | Card Payment Refund | 可作为卡退款相关分类引用；与 Card 归集链路关联仍 deferred |

## 6. Webhook / Notification 依赖边界

| 场景 | 已确认 | 来源 |
|---|---|---|
| Deposit success 通知触发 | Notification 表记录：Webhook→notify，event=`CRYPTO_TXN`，type=`DEPOSIT`，state=`success` | Notification PRD / sheet4 |
| Deposit Risk Withheld 通知触发 | Notification 表记录：Webhook→notify，event=`CRYPTO_TXN`，type=`DEPOSIT`，state=`RISK_WITHHELD` | Notification PRD / sheet4 |
| Webhook 具体逻辑 | Notification 表备注“具体逻辑待定义” | Notification PRD / sheet4 |

## 7. 不写入事实的内容

以下内容不得在 DTC 外部依赖文件中写成事实：

1. `D-REQUEST-ID` 是幂等键。
2. Wallet `transactionId` 等同于 Card `data.id`。
3. Wallet `id` 等同于 Card `data.id`。
4. Wallet `relatedId` 等同于 Card `data.id` 或 AIX 归集请求 ID。
5. DTC Crypto Deposit 规则自动等同于所有 GTR / WalletConnect 产品流程。
6. `FIAT_DEPOSIT` 必然等同 GTR。
7. `CRYPTO_DEPOSIT` 必然等同 WalletConnect。
8. Deposit `success` 必然等同 Wallet `COMPLETED`。
9. `Risk Withheld` 必然等同 Wallet `REJECTED` / `PENDING` / `PROCESSING`。
10. 所有 Deposit 都一定需要 Declare / Travel Rule。
11. Transfer Balance to Wallet 返回 transferId / resultId。
12. DTC 内部系统实现逻辑。
13. DTC 未提供但由 AIX 推测的字段、状态或错误码。

## 8. 待补项

| 编号 | 待补项 | 来源建议 | 当前处理 |
|---|---|---|---|
| DTC-GAP-001 | DTC Wallet Search Balance History 完整 response 字段 | DTC Wallet OpenAPI | 待补 |
| DTC-GAP-002 | `relatedId` 在 GTR / WC / Card 归集场景的具体取值 | DTC / 后端确认 | deferred |
| DTC-GAP-003 | GTR / WalletConnect 是否全部适用 Crypto Deposit whitelist 规则 | GTR / WC PRD / 产品确认 | 待补 |
| DTC-GAP-004 | `D-REQUEST-ID` 是否支持幂等 | DTC / 后端确认 | deferred |
| DTC-GAP-005 | Webhook 原始报文落库规则 | 后端确认 | deferred |
| DTC-GAP-006 | ActivityType 到 AIX 前端交易类型的映射 | 产品 / UX / 前端确认 | 待补 |

## 9. 来源引用

- (Ref: DTC Wallet OpenAPI Document20260126 / 3.4 Crypto Deposit)
- (Ref: DTC Wallet OpenAPI Document20260126 / 4.2.4 Search Balance History)
- (Ref: DTC Wallet OpenAPI Document20260126 / Appendix ActivityType)
- (Ref: [2025-11-25] AIX+Notification / Deposit rows)
- (Ref: knowledge-base/transaction/history.md / v1.1)
- (Ref: knowledge-base/transaction/detail.md / v1.1)
- (Ref: knowledge-base/wallet/transaction-history.md / v1.1)
- (Ref: knowledge-base/wallet/balance.md / v1.1)
- (Ref: knowledge-base/changelog/knowledge-gaps.md / deferred gaps)
