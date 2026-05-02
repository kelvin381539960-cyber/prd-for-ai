---
module: common
feature: dtc-dependency
version: "1.1"
status: active
source_doc: IMPLEMENTATION_PLAN.md；knowledge-base/common/_index.md；knowledge-base/card/card-transaction-flow.md；knowledge-base/wallet/transaction-history.md；knowledge-base/transaction/stage-review.md；knowledge-base/changelog/knowledge-gaps.md
source_section: IMPLEMENTATION_PLAN v4.1 / 全仓库回扫；Common Index v2.1；Card Transaction Flow v1.2；Wallet Transaction History v1.0；Transaction Stage Review v1.0
last_updated: 2026-05-01
owner: 吴忆锋
depends_on:
  - common/_index
  - card/card-transaction-flow
  - wallet/transaction-history
  - transaction/stage-review
  - changelog/knowledge-gaps
---

# DTC Dependency 外部依赖边界

## 1. 功能定位

DTC 是 AIX 的外部供应商系统，不是 AIX 内部系统，也不是本知识库需要维护的供应商系统说明书。

本文只沉淀 AIX 对 DTC 的依赖边界：

1. AIX 调用了哪些 DTC 能力。
2. AIX 依赖哪些 DTC 字段、状态、回调和响应。
3. 哪些规则来自 DTC 文档或已确认结论。
4. 哪些内容不能由 AIX 侧假设。
5. 出现异常时 AIX 侧已确认或待确认的处理边界。

本文不维护 DTC 内部系统逻辑，不补写 DTC 未提供的接口规则，也不把 DTC 供应商能力写成 AIX 自有能力。

## 2. 当前已确认 DTC 依赖事实

| 项目 | 结论 | 来源 | AIX 侧处理 |
|---|---|---|---|
| `D-REQUEST-ID` | DTC API 请求唯一标识 Header，client-generated unique request identifier | Card Transaction Flow / DTC Card Issuing | 只记录为请求唯一标识；不写成幂等键 |
| Card Transaction Notify | DTC 向 AIX 推送卡交易通知 | Card Transaction Flow | AIX 依赖该回调处理卡交易事件 |
| Card Transaction ID | `data.id` 为 DTC Card Transaction ID | Card Transaction Flow | 重复推送时 Transaction ID 不变，可作为通知去重基础 |
| Original Transaction ID | `originalId` 为 Original Transaction ID，选填 | Card Transaction Flow | AIX 可引用该字段展示 / 追踪原始交易 |
| Transfer Balance to Wallet | `[POST] /openapi/v1/card/transfer-to-wallet` | Card Transaction Flow | AIX 调用该能力做卡余额归集 |
| Transfer 成功响应 | 仅返回 `header.success=true`，不返回归集业务流水 | Card Transaction Flow | AIX 不能补写 transferId / resultId |
| Wallet Transaction Detail | 入参 `transactionId`，Unique transaction ID from DTC | Wallet Transaction History | 与 Card `data.id` 关联未确认 |
| Wallet Transaction ID | Wallet 交易记录 / 详情出参包含 `id`，Long，交易 id | Wallet Transaction History | 与 Card / D-REQUEST-ID 关联未确认 |
| Wallet `state` | `PENDING` / `PROCESSING` / `AUTHORIZED` / `COMPLETED` / `REJECTED` / `CLOSED` | Wallet Transaction History | 进入 / 退出条件待补 |

## 3. DTC 回调 / Webhook 依赖边界

| Webhook / 通知 | 当前结论 | 来源 | AIX 侧边界 |
|---|---|---|---|
| Card Transaction Notify | DTC 全量通知 AIX 卡交易 | Card Transaction Flow | AIX 只针对 refund / reversal / deposit 触发查卡余额和归集 |
| 重复推送 | 重复推送时 Transaction ID 不变 | 用户确认 / Card Transaction Flow | 可作为去重基础，但后端实现仍待确认 |
| 独立 notification id | 无独立 notification id | 用户确认 / Card Transaction Flow | 不再追问 notification id |
| 去重规则 | 可按 `event + data.id` 作为通知去重依据 | Card Transaction Flow | 后端实际实现仍 deferred |

## 4. 请求头与幂等边界

| 项目 | 当前处理 |
|---|---|
| `D-REQUEST-ID` | 已确认是 DTC 请求唯一标识 Header |
| 是否幂等键 | 未确认，不写成事实 |
| 是否必须落库 | AIX 后端实现未确认，保留 deferred gap |
| 是否与 AIX 归集请求 ID 关联 | 未确认，保留 deferred gap |

## 5. AIX 已依赖的 DTC Card 能力

| 接口 / 能力 | 当前结论 | 来源 | AIX 侧用途 |
|---|---|---|---|
| Inquiry Card Basic Info | 查询卡当前 `balance` | Card Transaction Flow | 用于判断是否需要把卡余额转回 Wallet |
| Transfer Balance to Wallet | 入参 `cardId`、`amount` | Card Transaction Flow | 用于卡余额归集 |
| Transaction History Of Card | 查询 Card History | Card Transaction Flow / Transaction History | 用于卡交易历史展示 |
| Detail Of Card Transaction | 查询 Card Transaction Detail | Card Transaction Flow / Transaction Detail | 用于卡交易详情展示 |
| Inquiry Card Balance History | 查询卡余额历史，含 `relatedId` 等字段 | Card Transaction Flow | 关联规则仍待补 |

## 6. AIX 已依赖的 DTC Wallet 能力

| 接口 / 能力 | 当前结论 | 来源 | AIX 侧用途 / 备注 |
|---|---|---|---|
| Wallet Transaction History | 存在 Wallet 交易记录能力 | Wallet Transaction History | 完整字段待补 |
| Wallet Transaction Detail | 入参 `transactionId` | Wallet Transaction History | 与 Card `data.id` 不等同 |
| Search Balance History | 返回 `activityType`、`relatedId`、`time`、`state` 等字段 | Wallet Transaction History | `activityType` 枚举待补 |

## 7. 不写入事实的内容

以下内容不得在 DTC 外部依赖文件中写成事实：

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
11. DTC 内部系统实现逻辑。
12. DTC 未提供但由 AIX 推测的字段、状态或错误码。

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

- (Ref: IMPLEMENTATION_PLAN.md / v4.1 / 全仓库回扫)
- (Ref: knowledge-base/common/_index.md / v2.1)
- (Ref: knowledge-base/card/card-transaction-flow.md / v1.2)
- (Ref: knowledge-base/wallet/transaction-history.md / v1.0)
- (Ref: knowledge-base/transaction/stage-review.md / v1.0)
- (Ref: knowledge-base/changelog/knowledge-gaps.md / deferred gaps)
