---
module: wallet
feature: balance
version: "1.1"
status: active
source_doc: DTC Wallet OpenAPI Documentation；DTC接口文档/DTC Wallet OpenAPI Document20260126 (1).docx；knowledge-base/wallet/_index.md；knowledge-base/wallet/transaction-history.md；knowledge-base/wallet/deposit.md；knowledge-base/card/card-transaction-flow.md；knowledge-base/changelog/knowledge-gaps.md；用户确认结论 2026-05-01
source_section: Wallet balance / Search Balance History / 4.2.4；Appendix ActivityType；Wallet Transaction History v1.1；Wallet Deposit v1.4
last_updated: 2026-05-01
owner: 吴忆锋
depends_on:
  - wallet/_index
  - wallet/transaction-history
  - wallet/deposit
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
| ActivityType | 引用 | 引用 Wallet Transaction History 已确认 ActivityType |
| Card balance | 不包含 | Card balance 属于 Card Transaction Flow 的查询与归集金额依据 |
| Card balance 转 Wallet 关联链路 | 不包含 | 继续保留在 `knowledge-gaps.md` 的 deferred gaps |
| Send / Deposit / Swap 余额变动规则 | 不完整包含 | Deposit 已补部分 Crypto Deposit 依赖；Send / Swap deferred |

## 3. 已确认基础事实

| 项目 | 结论 | 来源 | 备注 |
|---|---|---|---|
| Wallet 交易 ID | 钱包交易记录 / 详情出参均包含 `id`，Long，交易 id | DTC Wallet OpenAPI；用户确认 2026-05-01 | 余额变动记录可引用交易 ID，但关联规则需按接口确认 |
| Wallet 详情入参 | 单笔钱包交易详情入参为 `transactionId`，Unique transaction ID from DTC | DTC Wallet OpenAPI；用户确认 2026-05-01 | 与 Card `data.id` / `D-REQUEST-ID` 的关系未确认 |
| Wallet 交易状态 | 字段为 `state` | DTC Wallet OpenAPI；用户确认 2026-05-01 | 枚举见 `wallet/transaction-history.md` |
| Search Balance History | `[GET] /openapi/v1/wallet/balance/history/search` 可查询 client wallet transaction history | DTC Wallet OpenAPI / 4.2.4 | 返回字段包含 `activityType`、`relatedId`、`time`、`state` 等 |
| ActivityType | `FIAT_DEPOSIT=6`、`CRYPTO_DEPOSIT=10`、`DTC_WALLET=13`、`CARD_PAYMENT_REFUND=20` 已确认 | DTC Wallet OpenAPI / Appendix ActivityType | 具体业务映射仍需确认 |

## 4. Balance 与 Transaction History 的关系

Wallet Balance 不单独定义交易状态。余额变动相关状态统一引用 `wallet/transaction-history.md`。

| 能力 | 关系 |
|---|---|
| 当前余额 | 余额展示或查询的结果，字段表待补齐 |
| 余额历史 | 通过 Search Balance History 查询 |
| 交易详情 | 通过 Wallet Transaction Detail 查询，入参为 `transactionId` |
| 状态展示 | 引用 Wallet `state` 枚举 |
| 交易分类 | 引用 ActivityType，但不能把枚举直接等同具体产品路径 |
| 对账追踪 | 依赖 Wallet 交易 `id`、`transactionId`、`relatedId` 等字段；具体组合待补齐 |

## 5. Search Balance History 与 ActivityType

| 枚举 | 值 | 含义 | Balance 处理 |
|---|---:|---|---|
| `FIAT_DEPOSIT` | 6 | Fiat Deposit | 可作为法币入金余额历史分类；是否对应 GTR 待确认 |
| `CRYPTO_DEPOSIT` | 10 | Stablecoin Deposit | 可作为稳定币 / Crypto 入金余额历史分类；是否对应 WC 待确认 |
| `DTC_WALLET` | 13 | DTC Wallet Payment | 可作为 DTC Wallet Payment 分类 |
| `CARD_PAYMENT_REFUND` | 20 | Card Payment Refund | 可作为卡退款入 Wallet 相关分类；对账关联仍 deferred |

## 6. Wallet state 引用

| 枚举 | 当前处理 |
|---|---|
| `PENDING` | 引用交易历史事实源，不在 Balance 中重新定义进入 / 退出条件 |
| `PROCESSING` | 引用交易历史事实源，不在 Balance 中重新定义进入 / 退出条件 |
| `AUTHORIZED` | 引用交易历史事实源，不在 Balance 中重新定义进入 / 退出条件 |
| `COMPLETED` | 引用交易历史事实源，不在 Balance 中重新定义进入 / 退出条件 |
| `REJECTED` | 引用交易历史事实源，不在 Balance 中重新定义进入 / 退出条件 |
| `CLOSED` | 引用交易历史事实源，不在 Balance 中重新定义进入 / 退出条件 |

DTC Crypto Deposit 中的 `status=102 Risk Withheld` 是 Deposit 外部状态来源，不得直接等同 Wallet `state` 中任一枚举。

## 7. 与 Deposit 的关系

| 场景 | Balance 可引用事实 | 待确认 |
|---|---|---|
| GTR Deposit | Deposit 包含 GTR；ActivityType 有 `FIAT_DEPOSIT=6` | GTR 是否使用 FIAT_DEPOSIT；资金可见时点 |
| WalletConnect Deposit | Deposit 包含 WC；DTC Crypto Deposit 规则；ActivityType 有 `CRYPTO_DEPOSIT=10` | WC 是否使用 CRYPTO_DEPOSIT；资金可见时点 |
| Risk Withheld | DTC Crypto Deposit 未加白会 Risk Withheld | Risk Withheld 时是否计入余额 / 是否展示冻结余额 |
| Deposit success | Notification PRD 有 success 通知 | success 与余额增加 / 可用余额关系待确认 |

## 8. 与 Card balance 的边界

Card balance 与 Wallet balance 必须区分：

| 项目 | 所属模块 | 当前口径 |
|---|---|---|
| Card `balance` | Card Transaction Flow | 通过 `Inquiry Card Basic Info` 查询，作为 `Transfer Balance to Wallet` 的 amount 依据 |
| Wallet balance | Wallet Balance | 需从 DTC Wallet OpenAPI / Wallet PRD 补齐余额字段和展示规则 |
| Card balance 转 Wallet | Card Transaction Flow | 已知调用 `Transfer Balance to Wallet(cardId, amount=balance)`；成功响应不返回归集业务流水 |
| Card balance 转 Wallet 后的 Wallet 关联 | Deferred gap | Wallet 交易 `id` / `relatedId` 如何关联 Card `data.id`、AIX 归集请求或 `D-REQUEST-ID` 未确认 |

## 9. 不写入事实的内容

以下内容当前不得写成事实：

1. Wallet balance 字段名、可用余额字段名、冻结余额字段名。
2. Wallet balance 的币种列表。
3. Wallet balance 与 Card balance 的币种一定一致。
4. Card balance 转 Wallet 后一定能通过 `relatedId` 关联到 Card `data.id`。
5. Wallet `transactionId` 等同于 Card `data.id`。
6. Wallet 余额变动的完整对账字段组合。
7. Wallet 余额查询失败后的用户提示文案。
8. `FIAT_DEPOSIT` 必然等同 GTR。
9. `CRYPTO_DEPOSIT` 必然等同 WalletConnect。
10. Deposit success 必然代表 Wallet balance 立即可用。
11. Risk Withheld 必然进入冻结余额。

## 10. 待补字段清单

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
| Risk Withheld 对余额展示影响 | Wallet PRD / DTC / 产品确认 | 待补 |

## 11. 来源引用

- (Ref: DTC Wallet OpenAPI Document20260126 / 4.2.4 Search Balance History)
- (Ref: DTC Wallet OpenAPI Document20260126 / Appendix ActivityType)
- (Ref: DTC Wallet OpenAPI Document20260126 / 3.4 Crypto Deposit)
- (Ref: knowledge-base/wallet/transaction-history.md / v1.1)
- (Ref: knowledge-base/wallet/deposit.md / v1.4)
- (Ref: knowledge-base/card/card-transaction-flow.md / v1.2)
- (Ref: knowledge-base/changelog/knowledge-gaps.md / Card Transaction Flow deferred gaps)
- (Ref: 用户确认结论 / 2026-05-01)
