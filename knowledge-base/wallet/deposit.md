---
module: wallet
feature: deposit
version: "1.0"
status: active
source_doc: DTC Wallet OpenAPI Documentation；knowledge-base/wallet/_index.md；knowledge-base/wallet/balance.md；knowledge-base/wallet/transaction-history.md；knowledge-base/changelog/knowledge-gaps.md
source_section: Wallet Deposit / Receive / Search Balance History；Wallet _index v1.0；Wallet Balance v1.0；Wallet Transaction History v1.0
last_updated: 2026-05-01
owner: 吴忆锋
depends_on:
  - wallet/_index
  - wallet/balance
  - wallet/transaction-history
  - changelog/knowledge-gaps
---

# Wallet Deposit 钱包充值

## 1. 功能定位

Wallet Deposit 用于沉淀 AIX Wallet 充值相关能力，包括充值入口、充值地址 / 收款地址、链与币种、到账状态、充值记录和异常边界。

本文件当前为 Deposit 基础骨架。由于充值接口、地址生成、链路状态、风控拦截、白名单和用户通知字段尚未完成系统抽取，本文只写已确认的 Wallet 基础事实，并列出待补项。

## 2. 适用范围

| 范围 | 是否包含 | 说明 |
|---|---|---|
| Crypto Deposit | 包含 | 具体链、币种、地址字段待补 |
| Fiat Deposit | 包含 | 是否支持及具体流程待补 |
| Receive / 收款地址 | 部分包含 | 入口和地址能力待 `wallet/receive.md` 进一步拆分 |
| Deposit 交易记录 | 包含 | 引用 `wallet/transaction-history.md` |
| Deposit 后余额变化 | 包含 | 引用 `wallet/balance.md` |
| Card balance 自动归集 | 不包含 | 属于 Card Transaction Flow，且部分关联字段为 deferred gap |
| Send / Withdraw | 不包含 | 后续由 `wallet/send.md` 承接 |
| Swap | 不包含 | 后续由 `wallet/swap.md` 承接 |

## 3. 已确认基础事实

| 项目 | 结论 | 来源 | 备注 |
|---|---|---|---|
| Wallet 交易 ID | Wallet 交易记录 / 详情出参均包含 `id`，Long，交易 id | DTC Wallet OpenAPI；用户确认 2026-05-01 | Deposit 到账记录可引用 Wallet 交易 ID |
| Wallet 详情入参 | 单笔 Wallet 交易详情入参为 `transactionId`，Unique transaction ID from DTC | DTC Wallet OpenAPI；用户确认 2026-05-01 | 与具体 Deposit 链路字段关系待补 |
| Wallet 交易状态 | `state` 枚举为 `PENDING`、`PROCESSING`、`AUTHORIZED`、`COMPLETED`、`REJECTED`、`CLOSED` | DTC Wallet OpenAPI；用户确认 2026-05-01 | Deposit 状态是否完全复用该枚举待原文确认 |
| Search Balance History | 可查询 Wallet 交易 / 余额历史 | DTC Wallet OpenAPI / 4.2.4 | 返回字段包含 `activityType`、`relatedId`、`time`、`state` 等 |

## 4. Deposit 与 Balance 的关系

| 阶段 | 余额影响 | 当前处理 |
|---|---|---|
| 用户获取充值地址 | 不影响余额 | 地址能力待补 |
| 用户发起链上 / 外部充值 | 未确认 | 交易生成时机待补 |
| DTC / Wallet 识别充值 | 可能生成 Wallet 交易记录 | 需从接口文档补齐 |
| 充值处理中 | 可能对应 `PENDING` / `PROCESSING` | 状态映射待补 |
| 充值成功 | Wallet balance 增加 | 具体字段和入账时点待补 |
| 充值失败 / 拒绝 | Wallet balance 不增加或回退 | 失败状态与原因待补 |

## 5. Deposit 与 Transaction History 的关系

Deposit 交易记录与详情应统一引用 Wallet Transaction History 的基础字段。

| 能力 | 关系 |
|---|---|
| Deposit 记录 ID | 使用 Wallet 交易 `id`，具体生成时机待补 |
| Deposit 详情查询 | 通过 `transactionId` 查询 Wallet 单笔交易详情，具体入参来源待补 |
| Deposit 状态 | 引用 Wallet `state` 枚举，具体状态映射待补 |
| Deposit 余额历史 | 通过 Search Balance History 查询，具体 `activityType` / `relatedId` 待补 |

## 6. 状态边界

当前不能直接写死 Deposit 状态机，只能引用 Wallet `state` 枚举。

| Wallet state | Deposit 场景是否适用 | 当前处理 |
|---|---|---|
| `PENDING` | 可能适用 | 待原文确认进入条件 |
| `PROCESSING` | 可能适用 | 待原文确认进入条件 |
| `AUTHORIZED` | 可能适用 | 待原文确认是否用于 Deposit |
| `COMPLETED` | 可能适用 | 待原文确认成功口径 |
| `REJECTED` | 可能适用 | 待原文确认失败 / 拒绝口径 |
| `CLOSED` | 可能适用 | 待原文确认关闭口径 |

## 7. 风控 / 白名单 / 通知边界

Deposit 阶段通常涉及风控、白名单和用户通知，但当前未完成事实抽取。

| 事项 | 当前处理 |
|---|---|
| Deposit 是否需要地址白名单 | 待补，不写成事实 |
| Deposit 是否存在 on-hold / risk rejected 状态 | 待补，不写成事实 |
| Deposit 成功是否推送 push / 站内信 | 待补，不写成事实 |
| Deposit 失败是否通知用户 | 待补，不写成事实 |
| Deposit 风控拦截是否影响 Wallet balance | 待补，不写成事实 |
| Deposit 是否依赖 Travel Rule / Declare | 待补，不写成事实 |

## 8. 与 Card Transaction Flow 的边界

Card balance 自动归集到 Wallet 不是 Wallet Deposit 主流程。

| 项目 | 处理 |
|---|---|
| Card refund / reversal / deposit 触发查卡余额 | 属于 Card Transaction Flow |
| `Transfer Balance to Wallet(cardId, amount=balance)` | 属于 Card Transaction Flow |
| DTC transfer 成功响应无业务流水 | 已在 Card Transaction Flow 记录 |
| Wallet 是否生成对应交易 `id` | Wallet 交易 `id` 已确认存在，但与 Card 归集的关联仍 deferred |
| Wallet `relatedId` 在 Card balance 转 Wallet 场景下取值 | deferred gap，不在 Deposit 补写 |

## 9. 待补字段清单

| 待补项 | 建议来源 | 当前处理 |
|---|---|---|
| Deposit 入口页面规则 | Wallet PRD / 截图 | 待补 |
| Deposit 支持国家 / 币种 / 链 | Wallet PRD / DTC Wallet OpenAPI | 待补 |
| Deposit 地址生成 / 查询接口 | DTC Wallet OpenAPI | 待补 |
| Deposit 地址字段 | DTC Wallet OpenAPI | 待补 |
| Memo / Tag / Network 字段 | DTC Wallet OpenAPI / PRD | 待补 |
| 最小充值金额 | Wallet PRD / 接口文档 | 待补 |
| 确认数规则 | Wallet PRD / 接口文档 | 待补 |
| Deposit 状态映射 | Wallet PRD / DTC Wallet OpenAPI | 待补 |
| Deposit 失败原因 | DTC Wallet OpenAPI / 错误码 | 待补 |
| Deposit 通知规则 | Notification PRD | 待补 |
| Deposit 风控 / on-hold 规则 | 风控 / DTC 文档 / PRD | 待补 |
| Deposit 与 Travel Rule / Declare 的关系 | PRD / 合规文档 | 待补 |

## 10. 不写入事实的内容

以下内容当前不得写成事实：

1. 所有 Deposit 都需要白名单。
2. 所有 Deposit 都需要 Declare。
3. Deposit 成功一定等同于 Wallet balance 立即可用。
4. Deposit 状态完全等同于 Wallet `state` 枚举中的某几个值。
5. Deposit 地址字段、链字段、memo/tag 字段名。
6. Deposit 风控拦截规则。
7. Deposit 成功 / 失败通知文案。
8. Card balance 自动归集属于 Wallet Deposit。

## 11. 阶段影响

本文件可作为 Deposit 主题的基础占位和边界文件。后续应优先补齐 Deposit / Receive 相关 PRD 与 DTC Wallet OpenAPI 原文字段，再进入完整流程沉淀。

## 12. 来源引用

- (Ref: DTC Wallet OpenAPI Documentation / Deposit / Receive / Search Balance History)
- (Ref: knowledge-base/wallet/_index.md / v1.0)
- (Ref: knowledge-base/wallet/balance.md / v1.0)
- (Ref: knowledge-base/wallet/transaction-history.md / v1.0)
- (Ref: knowledge-base/changelog/knowledge-gaps.md / Card Transaction Flow deferred gaps)
