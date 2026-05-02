---
module: wallet
feature: transaction-history
version: "1.0"
status: active
source_doc: DTC Wallet OpenAPI Documentation；knowledge-base/wallet/_index.md；knowledge-base/card/card-transaction-flow.md；knowledge-base/changelog/knowledge-gaps.md；用户确认结论 2026-05-01
source_section: Wallet 交易记录；Wallet 交易详情；Search Balance History；Wallet state 枚举；Wallet _index v1.0；Card Transaction Flow v1.2
last_updated: 2026-05-01
owner: 吴忆锋
depends_on:
  - wallet/_index
  - card/card-transaction-flow
  - changelog/knowledge-gaps
---

# Wallet Transaction History 钱包交易记录

## 1. 功能定位

Wallet Transaction History 用于沉淀 AIX Wallet 交易记录、交易详情、交易状态和基础查询字段。

本文件只写 Wallet 交易记录 / 详情相关事实，不统一 Card / Wallet / Swap 全量交易状态。跨模块交易统一层后续由 Transaction 阶段收口。

Card Transaction Flow 的资金归集遗留关联问题继续保留为 deferred gaps，不在本文补写。

## 2. 适用范围

| 范围 | 是否包含 | 说明 |
|---|---|---|
| Wallet 交易记录 | 包含 | 钱包交易列表 / 历史记录能力 |
| Wallet 交易详情 | 包含 | 单笔钱包交易详情查询 |
| Wallet 交易状态 | 包含 | 当前已确认 `state` 枚举 |
| Wallet Search Balance History | 包含 | 查询钱包余额 / 交易历史的基础能力 |
| Card History | 不包含 | Card 交易记录已由 Card Transaction Flow 承接 |
| Card balance 自动归集 | 不包含 | 仅引用已确认字段，关联规则继续 deferred |
| Transaction 统一状态机 | 不包含 | 后续 Transaction 阶段统一收口 |

## 3. 已确认字段

| 字段 | 类型 / 口径 | 用途 | 来源 | 备注 |
|---|---|---|---|---|
| `id` | Long，交易 id | Wallet 交易记录 / 详情出参中的交易 ID | DTC Wallet OpenAPI；用户确认 2026-05-01 | 可作为 Wallet 交易基础 ID |
| `transactionId` | Unique transaction ID from DTC | 单笔钱包交易详情入参 | DTC Wallet OpenAPI；用户确认 2026-05-01 | 与 Card `data.id` / `D-REQUEST-ID` 的关联未确认 |
| `state` | Wallet 交易状态 | 展示 / 判断交易状态 | DTC Wallet OpenAPI；用户确认 2026-05-01 | 枚举见 4.1 |
| `activityType` | 原文已出现字段 | Wallet Search Balance History 返回字段 | DTC Wallet OpenAPI / 4.2.4 | 具体枚举待后续从接口文档补齐 |
| `relatedId` | 原文已出现字段 | Wallet Search Balance History 返回字段 | DTC Wallet OpenAPI / 4.2.4 | 在 Card balance 转 Wallet 场景下取值未确认 |
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

### 4.2 状态边界

当前只确认 `state` 字段和枚举值，不补写以下内容：

| 未确认项 | 处理 |
|---|---|
| 各状态的进入条件 | 后续在 Deposit / Send / Swap 等能力文档中按来源补齐 |
| 各状态的退出条件 | 后续在对应能力文档中补齐 |
| 状态与用户前端展示文案的映射 | 后续结合 PRD / 截图 / Notification 文档确认 |
| 状态与失败原因的映射 | 后续结合接口错误码和业务 PRD 确认 |

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
| Search Balance History | 可查询钱包交易历史 | DTC Wallet OpenAPI / 4.2.4 | 已作为 Wallet 交易历史能力来源 |
| `activityType` | 返回字段之一 | DTC Wallet OpenAPI / 4.2.4 | 枚举待补齐 |
| `relatedId` | 返回字段之一 | DTC Wallet OpenAPI / 4.2.4 | Card balance 转 Wallet 场景取值仍 deferred |
| `time` | 返回字段之一 | DTC Wallet OpenAPI / 4.2.4 | 格式待补齐 |
| `state` | 返回字段之一 | DTC Wallet OpenAPI / 4.2.4；用户确认 | 枚举见 4.1 |

## 6. 与 Card Transaction Flow 的关系

Wallet Transaction History 可以承接 Wallet 交易记录和交易详情本身，但不能直接补齐 Card Transaction Flow 的资金追踪缺口。

| Card 归集链路问题 | 当前处理 |
|---|---|
| Wallet 交易 `id` 如何关联 DTC Card `data.id` | 未确认，保持 deferred gap |
| Wallet 交易 `id` 如何关联 AIX 归集请求 ID | 未确认，保持 deferred gap |
| Wallet 交易 `id` 如何关联 `D-REQUEST-ID` | 未确认，保持 deferred gap |
| Wallet `relatedId` 在 Card balance 转 Wallet 场景取值 | 未确认，保持 deferred gap |
| 最终对账字段组合 | 未确认，保持 deferred gap |

## 7. 不写入事实的内容

以下内容当前不得写入 Wallet 正文作为事实：

1. Wallet `transactionId` 等同于 Card `data.id`。
2. Wallet `relatedId` 等同于 Card `data.id`。
3. Wallet `relatedId` 等同于 AIX 归集请求 ID。
4. `D-REQUEST-ID` 是幂等键。
5. Card balance 转 Wallet 的完整对账链路已经闭环。
6. Card balance 转 Wallet 的入账币种必然等于 card currency。

## 8. 后续待补

| 待补项 | 建议来源 | 处理 |
|---|---|---|
| Wallet 交易记录完整请求 / 响应字段表 | DTC Wallet OpenAPI 原文 | 后续补充 |
| Wallet 交易详情完整请求 / 响应字段表 | DTC Wallet OpenAPI 原文 | 后续补充 |
| `activityType` 枚举 | DTC Wallet OpenAPI 原文 | 后续补充 |
| Wallet 交易筛选条件 | Wallet PRD / 接口文档 / 截图 | 后续补充 |
| Wallet 交易详情页面展示字段 | Wallet PRD / 截图 | 后续补充 |
| Wallet 状态与前端展示文案映射 | PRD / 状态梳理表 / 截图 | 后续补充 |

## 9. 来源引用

- (Ref: DTC Wallet OpenAPI Documentation / Wallet 交易记录)
- (Ref: DTC Wallet OpenAPI Documentation / Wallet 交易详情)
- (Ref: DTC Wallet OpenAPI Documentation / Search Balance History / 4.2.4)
- (Ref: knowledge-base/wallet/_index.md / Wallet 基础字段)
- (Ref: knowledge-base/card/card-transaction-flow.md / v1.2)
- (Ref: knowledge-base/changelog/knowledge-gaps.md / Card Transaction Flow deferred gaps)
- (Ref: 用户确认结论 / 2026-05-01)
