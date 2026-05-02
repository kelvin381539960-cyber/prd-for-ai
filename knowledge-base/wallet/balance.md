---
module: wallet
feature: balance
version: "1.0"
status: active
source_doc: DTC Wallet OpenAPI Documentation；knowledge-base/wallet/_index.md；knowledge-base/wallet/transaction-history.md；knowledge-base/card/card-transaction-flow.md；knowledge-base/changelog/knowledge-gaps.md；用户确认结论 2026-05-01
source_section: Wallet balance / Search Balance History；Wallet Transaction History v1.0；Wallet _index v1.0；Card Transaction Flow v1.2
last_updated: 2026-05-01
owner: 吴忆锋
depends_on:
  - wallet/_index
  - wallet/transaction-history
  - card/card-transaction-flow
  - changelog/knowledge-gaps
---

# Wallet Balance 钱包余额

## 1. 功能定位

Wallet Balance 用于沉淀 AIX Wallet 余额相关能力，包括钱包余额展示、余额查询、余额历史、币种口径，以及与 Wallet Transaction History 的关系。

本文件只写 Wallet 余额事实，不写 Card balance，也不补写 Card balance 自动归集到 Wallet 的未确认关联链路。

## 2. 适用范围

| 范围 | 是否包含 | 说明 |
|---|---|---|
| Wallet 余额展示 | 包含 | 余额展示规则待后续从 Wallet PRD / 截图补齐 |
| Wallet 余额查询 | 包含 | 接口字段待从 DTC Wallet OpenAPI 原文补齐 |
| Wallet 余额历史 | 包含 | 可引用 `Search Balance History` |
| Wallet 交易状态 | 引用 | 引用 `wallet/transaction-history.md` 中的 `state` 枚举 |
| Card balance | 不包含 | Card balance 属于 Card Transaction Flow 的查询与归集金额依据 |
| Card balance 转 Wallet 关联链路 | 不包含 | 继续保留在 `knowledge-gaps.md` 的 deferred gaps |
| Send / Deposit / Swap 余额变动规则 | 不完整包含 | 后续在对应能力文档中补齐 |

## 3. 已确认基础事实

| 项目 | 结论 | 来源 | 备注 |
|---|---|---|---|
| Wallet 交易 ID | 钱包交易记录 / 详情出参均包含 `id`，Long，交易 id | DTC Wallet OpenAPI；用户确认 2026-05-01 | 余额变动记录可引用交易 ID，但关联规则需按接口确认 |
| Wallet 详情入参 | 单笔钱包交易详情入参为 `transactionId`，Unique transaction ID from DTC | DTC Wallet OpenAPI；用户确认 2026-05-01 | 与 Card `data.id` / `D-REQUEST-ID` 的关系未确认 |
| Wallet 交易状态 | 字段为 `state` | DTC Wallet OpenAPI；用户确认 2026-05-01 | 枚举见 `wallet/transaction-history.md` |
| Search Balance History | 可查询钱包交易 / 余额历史 | DTC Wallet OpenAPI / 4.2.4 | 返回字段包含 `activityType`、`relatedId`、`time`、`state` 等 |

## 4. Balance 与 Transaction History 的关系

Wallet Balance 不单独定义交易状态。余额变动相关状态统一引用 `wallet/transaction-history.md`。

| 能力 | 关系 |
|---|---|
| 当前余额 | 余额展示或查询的结果，字段表待补齐 |
| 余额历史 | 通过 Search Balance History 查询 |
| 交易详情 | 通过 Wallet Transaction Detail 查询，入参为 `transactionId` |
| 状态展示 | 引用 Wallet `state` 枚举 |
| 对账追踪 | 依赖 Wallet 交易 `id`、`transactionId`、`relatedId` 等字段；具体组合待补齐 |

## 5. Wallet state 引用

| 枚举 | 当前处理 |
|---|---|
| `PENDING` | 引用交易历史事实源，不在 Balance 中重新定义进入 / 退出条件 |
| `PROCESSING` | 引用交易历史事实源，不在 Balance 中重新定义进入 / 退出条件 |
| `AUTHORIZED` | 引用交易历史事实源，不在 Balance 中重新定义进入 / 退出条件 |
| `COMPLETED` | 引用交易历史事实源，不在 Balance 中重新定义进入 / 退出条件 |
| `REJECTED` | 引用交易历史事实源，不在 Balance 中重新定义进入 / 退出条件 |
| `CLOSED` | 引用交易历史事实源，不在 Balance 中重新定义进入 / 退出条件 |

## 6. 与 Card balance 的边界

Card balance 与 Wallet balance 必须区分：

| 项目 | 所属模块 | 当前口径 |
|---|---|---|
| Card `balance` | Card Transaction Flow | 通过 `Inquiry Card Basic Info` 查询，作为 `Transfer Balance to Wallet` 的 amount 依据 |
| Wallet balance | Wallet Balance | 需从 DTC Wallet OpenAPI / Wallet PRD 补齐余额字段和展示规则 |
| Card balance 转 Wallet | Card Transaction Flow | 已知调用 `Transfer Balance to Wallet(cardId, amount=balance)`；成功响应不返回归集业务流水 |
| Card balance 转 Wallet 后的 Wallet 关联 | Deferred gap | Wallet 交易 `id` / `relatedId` 如何关联 Card `data.id`、AIX 归集请求或 `D-REQUEST-ID` 未确认 |

## 7. 不写入事实的内容

以下内容当前不得写成事实：

1. Wallet balance 字段名、可用余额字段名、冻结余额字段名。
2. Wallet balance 的币种列表。
3. Wallet balance 与 Card balance 的币种一定一致。
4. Card balance 转 Wallet 后一定能通过 `relatedId` 关联到 Card `data.id`。
5. Wallet `transactionId` 等同于 Card `data.id`。
6. Wallet 余额变动的完整对账字段组合。
7. Wallet 余额查询失败后的用户提示文案。

## 8. 待补字段清单

| 待补项 | 建议来源 | 当前处理 |
|---|---|---|
| Wallet 当前余额查询接口路径 | DTC Wallet OpenAPI 原文 | 待补 |
| Wallet 当前余额请求字段 | DTC Wallet OpenAPI 原文 | 待补 |
| Wallet 当前余额响应字段 | DTC Wallet OpenAPI 原文 | 待补 |
| 可用余额 / 冻结余额 / 总余额字段 | DTC Wallet OpenAPI / Wallet PRD | 待补 |
| 余额币种字段 | DTC Wallet OpenAPI / Wallet PRD | 待补 |
| 余额展示排序 | Wallet PRD / 截图 | 待补 |
| 小额余额 / 零余额展示规则 | Wallet PRD / 截图 | 待补 |
| 余额查询失败处理 | Wallet PRD / 接口错误码 | 待补 |
| Search Balance History 完整字段表 | DTC Wallet OpenAPI | 待补 |

## 9. 阶段影响

Wallet Balance 当前为基础文件，可被后续 Deposit / Receive / Send / Swap 引用。

但由于当前余额查询接口路径和响应字段尚未系统抽取，本文件暂不作为完整余额接口事实源。后续拿到 DTC Wallet OpenAPI 原文解析结果后，需要补充接口字段表。

## 10. 来源引用

- (Ref: DTC Wallet OpenAPI Documentation / Wallet balance / Search Balance History)
- (Ref: knowledge-base/wallet/_index.md / v1.0)
- (Ref: knowledge-base/wallet/transaction-history.md / v1.0)
- (Ref: knowledge-base/card/card-transaction-flow.md / v1.2)
- (Ref: knowledge-base/changelog/knowledge-gaps.md / Card Transaction Flow deferred gaps)
- (Ref: 用户确认结论 / 2026-05-01)
