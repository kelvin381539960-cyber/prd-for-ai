---
module: common
feature: dtc-integration
version: "1.0"
status: active
source_doc: IMPLEMENTATION_PLAN.md；knowledge-base/common/_index.md；knowledge-base/card/card-transaction-flow.md；knowledge-base/wallet/transaction-history.md；knowledge-base/transaction/stage-review.md；knowledge-base/changelog/knowledge-gaps.md
source_section: IMPLEMENTATION_PLAN v4.0 / Common Integration；Common Index v2.0；Card Transaction Flow v1.2；Wallet Transaction History v1.0；Transaction Stage Review v1.0
last_updated: 2026-05-01
owner: 吴忆锋
depends_on:
  - common/_index
  - card/card-transaction-flow
  - wallet/transaction-history
  - transaction/stage-review
  - changelog/knowledge-gaps
---

# DTC Integration 公共集成边界

## 1. 功能定位

DTC Integration 用于沉淀 AIX 与 DTC 相关的公共接口边界，包括请求头、Webhook、通用字段、错误码和跨模块引用规则。

本文不重写 Card / Wallet 的业务流程，只沉淀 DTC 作为公共外部系统时可复用的事实和边界。

## 2. 当前已确认 DTC 公共事实

| 项目 | 结论 | 来源 | 备注 |
|---|---|---|---|
| `D-REQUEST-ID` | DTC API 请求唯一标识 Header，client-generated unique request identifier | Card Transaction Flow / DTC Card Issuing | 不写成幂等键 |
| Card Transaction Notify | DTC 向 AIX 推送卡交易通知 | Card Transaction Flow | Webhook 示例 |
| Card Transaction ID | `data.id` 为 DTC Card Transaction ID | Card Transaction Flow | 重复推送时 Transaction ID 不变 |
| Original Transaction ID | `originalId` 为 Original Transaction ID，选填 | Card Transaction Flow | Card 交易字段 |
| Transfer Balance to Wallet | `[POST] /openapi/v1/card/transfer-to-wallet` | Card Transaction Flow | 请求字段 `cardId`、`amount` |
| Transfer 成功响应 | 仅返回 `header.success=true`，不返回归集业务流水 | Card Transaction Flow | 不补写 transferId |
| Wallet Transaction Detail | 入参 `transactionId`，Unique transaction ID from DTC | Wallet Transaction History | 与 Card `data.id` 关联未确认 |
| Wallet Transaction ID | Wallet 交易记录 / 详情出参包含 `id`，Long，交易 id | Wallet Transaction History | 与 Card / D-REQUEST-ID 关联未确认 |
| Wallet `state` | `PENDING` / `PROCESSING` / `AUTHORIZED` / `COMPLETED` / `REJECTED` / `CLOSED` | Wallet Transaction History | 进入 / 退出条件待补 |

## 3. Webhook 边界

| Webhook / 通知 | 当前结论 | 来源 | Common 处理 |
|---|---|---|---|
| Card Transaction Notify | DTC 全量通知 AIX 卡交易 | Card Transaction Flow | 可作为 DTC Webhook 公共能力引用 |
| 重复推送 | 重复推送时 Transaction ID 不变 | 用户确认 / Card Transaction Flow | 可作为去重依据基础，但后端实现待确认 |
| 独立 notification id | 无独立 notification id | 用户确认 / Card Transaction Flow | 不再追问 notification id |
| 去重规则 | 可按 `event + data.id` 作为通知去重依据 | Card Transaction Flow | 后端实际实现仍 deferred |

## 4. 请求头与幂等边界

| 项目 | 当前处理 |
|---|---|
| `D-REQUEST-ID` | 已确认是 DTC 请求唯一标识 Header |
| 是否幂等键 | 未确认，不写成事实 |
| 是否必须落库 | 后端实现未确认，保留 deferred gap |
| 是否与 AIX 归集请求 ID 关联 | 未确认，保留 deferred gap |

## 5. DTC Card 接口示例边界

| 接口 / 能力 | 当前结论 | 来源 |
|---|---|---|
| Inquiry Card Basic Info | 查询卡当前 `balance` | Card Transaction Flow |
| Transfer Balance to Wallet | 将卡余额转回 Wallet，入参 `cardId`、`amount` | Card Transaction Flow |
| Transaction History Of Card | 查询 Card History | Card Transaction Flow / Transaction History |
| Detail Of Card Transaction | 查询 Card Transaction Detail | Card Transaction Flow / Transaction Detail |
| Inquiry Card Balance History | 查询卡余额历史，含 `relatedId` 等字段 | Card Transaction Flow |

## 6. DTC Wallet 接口示例边界

| 接口 / 能力 | 当前结论 | 来源 | 备注 |
|---|---|---|---|
| Wallet Transaction History | 存在 Wallet 交易记录能力 | Wallet Transaction History | 完整字段待补 |
| Wallet Transaction Detail | 入参 `transactionId` | Wallet Transaction History | 与 Card `data.id` 不等同 |
| Search Balance History | 返回 `activityType`、`relatedId`、`time`、`state` 等字段 | Wallet Transaction History | `activityType` 枚举待补 |

## 7. 不写入事实的内容

以下内容不得在 DTC 公共文件中写成事实：

1. `D-REQUEST-ID` 是幂等键。
2. Wallet `transactionId` 等同于 Card `data.id`。
3. Wallet `id` 等同于 Card `data.id`。
4. Wallet `relatedId` 等同于 Card `data.id`。
5. Wallet `relatedId` 等同于 AIX 归集请求 ID。
6. Transfer Balance to Wallet 返回 transferId / resultId。
7. AIX 已生成内部交易处理 ID。
8. AIX 已生成归集请求 ID。
9. GTR / WalletConnect 完整 DTC 状态机已闭环。
10. Send / Swap 是当前 active DTC 能力。

## 8. 待补项

| 编号 | 待补项 | 来源建议 | 当前处理 |
|---|---|---|---|
| DTC-GAP-001 | DTC 通用响应结构完整字段 | DTC 接口文档 | 待补 |
| DTC-GAP-002 | DTC 通用错误码表 | DTC 接口文档 | 待补，后续也进入 `common/errors.md` |
| DTC-GAP-003 | `D-REQUEST-ID` 是否支持幂等 | DTC / 后端确认 | deferred |
| DTC-GAP-004 | DTC Wallet `activityType` 枚举 | DTC Wallet OpenAPI | 待补 |
| DTC-GAP-005 | DTC Wallet `relatedId` 关联规则 | DTC Wallet OpenAPI / 后端确认 | deferred |
| DTC-GAP-006 | GTR / WalletConnect DTC 接口路径与字段 | GTR / WC PRD / 接口文档 | 待补 |
| DTC-GAP-007 | Webhook 原始报文落库规则 | 后端确认 | deferred |

## 9. 来源引用

- (Ref: IMPLEMENTATION_PLAN.md / v4.0 / Common Integration)
- (Ref: knowledge-base/common/_index.md / v2.0)
- (Ref: knowledge-base/card/card-transaction-flow.md / v1.2)
- (Ref: knowledge-base/wallet/transaction-history.md / v1.0)
- (Ref: knowledge-base/transaction/stage-review.md / v1.0)
- (Ref: knowledge-base/changelog/knowledge-gaps.md / deferred gaps)
