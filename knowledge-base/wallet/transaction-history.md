---
module: wallet
feature: transaction-history
version: "1.1"
status: active
source_doc: DTC Wallet OpenAPI Documentation；DTC接口文档/DTC Wallet OpenAPI Document20260126 (1).docx；DTC接口文档/卡交易&钱包交易状态梳理 (1).docx；knowledge-base/wallet/_index.md；knowledge-base/wallet/deposit.md；knowledge-base/common/dtc.md；knowledge-base/changelog/knowledge-gaps.md；用户确认结论 2026-05-01
source_section: Wallet 交易记录；Wallet 交易详情；Search Balance History / 4.2.4；Appendix ActivityType；Wallet state 枚举；Wallet Deposit v1.4
last_updated: 2026-05-01
owner: 吴忆锋
depends_on:
  - wallet/_index
  - wallet/deposit
  - common/dtc
  - card/card-transaction-flow
  - changelog/knowledge-gaps
---

# Wallet Transaction History 钱包交易记录

## 1. 功能定位

Wallet Transaction History 用于沉淀 AIX Wallet 交易记录、交易详情、交易状态和基础查询字段。

本文件只写 Wallet 交易记录 / 详情相关事实，不统一 Card / Wallet / Swap 全量交易状态。跨模块交易统一层由 Transaction 阶段收口。

Card Transaction Flow 的资金归集遗留关联问题继续保留为 deferred gaps，不在本文补写。

## 2. 适用范围

| 范围 | 是否包含 | 说明 |
|---|---|---|
| Wallet 交易记录 | 包含 | 钱包交易列表 / 历史记录能力 |
| Wallet 交易详情 | 包含 | 单笔钱包交易详情查询 |
| Wallet 交易状态 | 包含 | 当前已确认 `state` 枚举 |
| Wallet Search Balance History | 包含 | 查询钱包余额 / 交易历史的基础能力 |
| Wallet ActivityType | 包含 | DTC Wallet OpenAPI Appendix ActivityType 中已确认部分枚举 |
| Card History | 不包含 | Card 交易记录已由 Card Transaction Flow 承接 |
| Card balance 自动归集 | 不包含 | 仅引用已确认字段，关联规则继续 deferred |
| Transaction 统一状态机 | 不包含 | 由 Transaction 阶段统一收口 |

## 3. 已确认字段

| 字段 | 类型 / 口径 | 用途 | 来源 | 备注 |
|---|---|---|---|---|
| `id` | Long，交易 id | Wallet 交易记录 / 详情出参中的交易 ID | DTC Wallet OpenAPI；用户确认 2026-05-01 | 可作为 Wallet 交易基础 ID |
| `transactionId` | Unique transaction ID from DTC | 单笔钱包交易详情入参 | DTC Wallet OpenAPI；用户确认 2026-05-01 | 与 Card `data.id` / `D-REQUEST-ID` 的关联未确认 |
| `state` | Wallet 交易状态 | 展示 / 判断交易状态 | DTC Wallet OpenAPI；用户确认 2026-05-01 | 枚举见 4.1 |
| `activityType` | ActivityType | Wallet Search Balance History 交易分类 | DTC Wallet OpenAPI / 4.2.4 / Appendix ActivityType | 已补部分枚举，见 5.4 |
| `relatedId` | 原文已出现字段 | Wallet Search Balance History 返回字段 | DTC Wallet OpenAPI / 4.2.4 | 在 Card balance 转 Wallet、GTR、WC 场景下取值未确认 |
| `time` | 原文已出现字段 | Wallet Search Balance History 返回字段 | DTC Wallet OpenAPI / 4.2.4 | 时间格式待接口文档确认 |

## 4. Wallet 交易状态

### 4.1 state 枚举

| 枚举 | 状态含义 | 当前说明 |
|---|---|---|
| `PENDING` | 待处理 | 仅确认枚举存在，具体进入 / 退出条件待后续能力文档补充 |
| `PROCESSING` | 处理中 | 仅确认枚举存在，具体进入 / 退出条件待后续能力文档补充 |
| `AUTHORIZED` | 已授权 | 仅确认枚举存在，具体进入 / 退出条件待后续能力文档补充 |
| `COMPLETED` | 已完成 | 仅确认枚举存在，具体进入 / 退出条件待后续能力文档补充 |
| `REJECTED` | 已拒绝 | 仅确认枚举存在，具体失败原因待后续能力文档补充 |
| `CLOSED` | 已关闭 | 仅确认枚举存在，具体关闭条件待后续能力文档补充 |

### 4.2 Deposit 外部状态补充

DTC Crypto Deposit 文档确认存在 `status=102 Risk Withheld`，表示未加 senderAddress whitelist 时交易进入 risky transaction。该状态可作为 Deposit / WalletConnect 风控边界来源，但当前不得直接等同 Wallet `state=REJECTED`、`PENDING` 或 `PROCESSING`。

## 5. 查询能力

### 5.1 Wallet 交易记录

| 能力 | 当前结论 | 来源 | 备注 |
|---|---|---|---|
| 钱包交易记录查询 | 存在 Wallet 交易记录能力 | DTC Wallet OpenAPI；用户确认 2026-05-01 | 出参包含 `id` |
| 交易记录 ID | 出参包含 `id`，Long，交易 id | DTC Wallet OpenAPI；用户确认 2026-05-01 | 与 Card 归集链路的关联未确认 |
| 交易状态 | 出参包含 `state` | DTC Wallet OpenAPI；用户确认 2026-05-01 | 枚举已确认 |

### 5.2 Wallet 交易详情

| 能力 | 当前结论 | 来源 | 备注 |
|---|---|---|---|
| 单笔钱包交易详情 | 存在 Wallet 交易详情能力 | DTC Wallet OpenAPI；用户确认 2026-05-01 | 入参为 `transactionId` |
| 查询入参 | `transactionId`，Unique transaction ID from DTC | DTC Wallet OpenAPI；用户确认 2026-05-01 | 不等同于 Card `data.id`，关联关系未确认 |
| 详情 ID | 出参包含 `id`，Long，交易 id | DTC Wallet OpenAPI；用户确认 2026-05-01 | 可作为 Wallet 交易详情 ID |

### 5.3 Wallet Search Balance History

| 能力 / 字段 | 当前结论 | 来源 | 备注 |
|---|---|---|---|
| Search Balance History | `[GET] /openapi/v1/wallet/balance/history/search` 查询 client wallet transaction history | DTC Wallet OpenAPI / 4.2.4 | Wallet 交易历史能力来源 |
| Request filter `currency` | 查询条件之一 | DTC Wallet OpenAPI / 4.2.4 | 具体是否前端暴露待补 |
| Request filter `type` | 查询条件之一，引用 ActivityType | DTC Wallet OpenAPI / 4.2.4 | 前端映射待补 |
| Request filter `yearMonth` / `createTimeStart` | 查询条件之一 | DTC Wallet OpenAPI / 4.2.4 | 完整时间规则待补 |
| `activityType` | 返回 / 查询分类字段 | DTC Wallet OpenAPI / Appendix ActivityType | 已补部分枚举 |
| `relatedId` | 返回字段之一 | DTC Wallet OpenAPI / 4.2.4 | Card balance 转 Wallet / GTR / WC 场景取值仍 deferred |
| `time` | 返回字段之一 | DTC Wallet OpenAPI / 4.2.4 | 格式待补齐 |
| `state` | 返回字段之一 | DTC Wallet OpenAPI / 4.2.4；用户确认 | 枚举见 4.1 |

### 5.4 ActivityType 已确认枚举

| 枚举 | 值 | 含义 | 当前处理 |
|---|---:|---|---|
| `FIAT_DEPOSIT` | 6 | Fiat Deposit | 可作为 GTR / fiat 入金分类候选；是否对应 GTR 待确认 |
| `CRYPTO_DEPOSIT` | 10 | Stablecoin Deposit | 可作为 Crypto / WalletConnect 入金分类候选；是否对应 WC 待确认 |
| `DTC_WALLET` | 13 | DTC Wallet Payment | 可作为 DTC Wallet Payment 分类引用 |
| `CARD_PAYMENT_REFUND` | 20 | Card Payment Refund | 可作为 Card refund 入 Wallet 相关分类引用；与 Card 归集链路关联仍待确认 |

## 6. 与 Deposit 的关系

| Deposit 场景 | 可引用事实 | 待确认 |
|---|---|---|
| GTR Deposit | Deposit 包含 GTR；`FIAT_DEPOSIT=6` 存在 | GTR 是否使用 FIAT_DEPOSIT；GTR 状态映射 |
| WalletConnect Deposit | Deposit 包含 WC；DTC Crypto Deposit 规则；`CRYPTO_DEPOSIT=10` 存在 | WC 是否使用 CRYPTO_DEPOSIT；WC `transactionId`、`relatedId` 映射 |
| Risk Withheld | DTC Crypto Deposit `status=102 Risk Withheld` | 是否映射到 Wallet `state`；前端展示文案 |
| Deposit success | Notification PRD 有 state=success 通知 | 是否映射到 Wallet `COMPLETED` 待确认 |

## 7. 与 Card Transaction Flow 的关系

Wallet Transaction History 可以承接 Wallet 交易记录和交易详情本身，但不能直接补齐 Card Transaction Flow 的资金追踪缺口。

| Card 归集链路问题 | 当前处理 |
|---|---|
| Wallet 交易 `id` 如何关联 DTC Card `data.id` | 未确认，保持 deferred gap |
| Wallet 交易 `id` 如何关联 AIX 归集请求 ID | 未确认，保持 deferred gap |
| Wallet 交易 `id` 如何关联 `D-REQUEST-ID` | 未确认，保持 deferred gap |
| Wallet `relatedId` 在 Card balance 转 Wallet 场景取值 | 未确认，保持 deferred gap |
| 最终对账字段组合 | 未确认，保持 deferred gap |

## 8. 不写入事实的内容

以下内容当前不得写入 Wallet 正文作为事实：

1. Wallet `transactionId` 等同于 Card `data.id`。
2. Wallet `relatedId` 等同于 Card `data.id`。
3. Wallet `relatedId` 等同于 AIX 归集请求 ID。
4. `D-REQUEST-ID` 是幂等键。
5. Card balance 转 Wallet 的完整对账链路已经闭环。
6. `CRYPTO_DEPOSIT` 必然等同 WalletConnect。
7. `FIAT_DEPOSIT` 必然等同 GTR。
8. Deposit success 必然等同 Wallet `COMPLETED`。
9. Risk Withheld 必然等同 Wallet `REJECTED`。

## 9. 后续待补

| 待补项 | 建议来源 | 处理 |
|---|---|---|
| Wallet 交易记录完整请求 / 响应字段表 | DTC Wallet OpenAPI 原文 | 后续补充 |
| Wallet 交易详情完整请求 / 响应字段表 | DTC Wallet OpenAPI 原文 | 后续补充 |
| ActivityType 完整枚举 | DTC Wallet OpenAPI 原文 | 后续补充 |
| Wallet 交易筛选条件 | Wallet PRD / 接口文档 / 截图 | 后续补充 |
| Wallet 交易详情页面展示字段 | Wallet PRD / 截图 | 后续补充 |
| Wallet 状态与前端展示文案映射 | PRD / 状态梳理表 / 截图 | 后续补充 |
| `relatedId` 取值规则 | DTC / 后端确认 | deferred |

## 10. 来源引用

- (Ref: DTC Wallet OpenAPI Document20260126 / 4.2.4 Search Balance History)
- (Ref: DTC Wallet OpenAPI Document20260126 / Appendix ActivityType)
- (Ref: DTC Wallet OpenAPI Document20260126 / 3.4 Crypto Deposit)
- (Ref: knowledge-base/wallet/deposit.md / v1.4)
- (Ref: knowledge-base/common/dtc.md / v1.2)
- (Ref: knowledge-base/changelog/knowledge-gaps.md / Card Transaction Flow deferred gaps)
- (Ref: 用户确认结论 / 2026-05-01)
