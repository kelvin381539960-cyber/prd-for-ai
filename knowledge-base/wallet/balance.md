---
module: wallet
feature: balance
version: "1.3"
status: active
source_doc: DTC Wallet OpenAPI Documentation；DTC接口文档/DTC Wallet OpenAPI Document20260126 (1).docx；knowledge-base/wallet/_index.md；knowledge-base/transaction/history.md；knowledge-base/transaction/status-model.md；knowledge-base/wallet/deposit.md；knowledge-base/card/card-transaction-flow.md；knowledge-base/changelog/knowledge-gaps.md；用户确认结论 2026-05-01；用户确认结论 2026-05-02
source_section: Wallet balance / Search Balance History / 4.2.4；Appendix ActivityType；Transaction History v1.3；Wallet Deposit v1.6；ALL-GAP 总表
last_updated: 2026-05-04
owner: 吴忆锋
depends_on:
  - wallet/_index
  - transaction/history
  - transaction/status-model
  - wallet/deposit
  - card/card-transaction-flow
  - changelog/knowledge-gaps
---

# Wallet Balance 钱包余额

## 1. 功能定位

Wallet Balance 用于沉淀 AIX Wallet 余额相关能力，包括钱包余额展示、余额查询、余额历史、币种口径，以及与 Transaction History 的关系。

本文件只写 Wallet 余额事实，不写 Card balance，也不补写 Card balance 自动归集到 Wallet 的未确认关联链路。

所有未确认问题统一引用 `knowledge-base/changelog/knowledge-gaps.md` 的 ALL-GAP 编号；本文不再维护本地待补字段清单。

## 2. 适用范围

| 范围 | 是否包含 | 说明 |
|---|---|---|
| Wallet 余额展示 | 包含 | 余额展示排序、小额 / 零余额展示规则见 ALL-GAP-056 |
| Wallet 余额查询 | 包含 | 当前余额查询接口和字段边界见 ALL-GAP-055 |
| Wallet 余额历史 | 包含 | 可引用 `Search Balance History`；完整字段表见 ALL-GAP-058 |
| Wallet 交易状态 | 引用 | 引用 `transaction/status-model.md` 中的 Wallet `state` 枚举 |
| ActivityType | 引用 | 引用 Transaction History 已确认 ActivityType |
| Card balance | 不包含 | Card balance 属于 Card Transaction Flow 的查询与归集金额依据 |
| Card balance 转 Wallet 关联链路 | 不包含 | 统一引用 ALL-GAP-017、ALL-GAP-018、ALL-GAP-029 |
| Send / Deposit / Swap 余额变动规则 | 不完整包含 | Deposit 已补部分 Crypto Deposit 依赖；Send / Swap deferred |

## 3. 已确认基础事实

### 3.1 已确认接口最小事实

| 接口 | Endpoint | 用途 | 已确认最小事实 | 边界 |
|---|---|---|---|---|
| Get Balance | `[GET] /openapi/v1/wallet/balance/{currency}` | 查询单币种 Wallet balance | 接口存在；路径中包含 `currency` | 当前可用余额 / 冻结余额 / 总余额字段边界仍见 ALL-GAP-055 |
| Get Wallet Account Balance | `[GET] /openapi/v1/wallet/balances` | 查询全量 Wallet account balances | 接口存在；用于钱包全量币种余额查询 | 返回字段完整结构、排序、零余额展示仍见 ALL-GAP-055、ALL-GAP-056 |
| Search Balance History | `[GET] /openapi/v1/wallet/balance/history/search` | 查询 client wallet transaction history | 返回字段包含 `activityType`、`relatedId`、`time`、`state` 等 | 完整字段表仍见 ALL-GAP-058 |

### 3.2 币种口径分层

Wallet Balance 中的币种必须按来源分层，不得混用：

| 层级 | 含义 | 当前处理 |
|---|---|---|
| AIX 产品支持币种 | AIX PRD 中面向用户展示和操作的稳定币范围 | 当前 Wallet 产品口径主要为 USDC、USDT、WUSD、FDUSD；具体页面排序和展示规则见 ALL-GAP-056 |
| DTC Available Currency | DTC OpenAPI 附录中的可用币种枚举 | 可引用为接口枚举来源，但不得直接等同 AIX 前端展示范围 |
| 接口返回币种 | Get Balance / Get Wallet Account Balance 实际返回的币种 | 字段和过滤边界见 ALL-GAP-055 |
| 前端展示币种 | AIX App 在 Wallet 页面展示给用户的币种 | 以产品规则和配置为准；展示排序、小额 / 零余额规则见 ALL-GAP-056 |

### 3.3 已确认基础事实

| 项目 | 结论 | 来源 | 备注 |
|---|---|---|---|
| Wallet 交易 ID | 钱包交易记录 / 详情出参均包含 `id`，Long，交易 id | DTC Wallet OpenAPI；用户确认 2026-05-01 | 余额变动记录可引用交易 ID，但关联规则见 ALL-GAP-014、ALL-GAP-018 |
| Wallet 详情入参 | 单笔钱包交易详情入参为 `transactionId`，Unique transaction ID from DTC | DTC Wallet OpenAPI；用户确认 2026-05-01 | 与 Card `data.id` / `D-REQUEST-ID` 的关系见 ALL-GAP-018 |
| Wallet 交易状态 | 字段为 `state` | DTC Wallet OpenAPI；用户确认 2026-05-01 | 枚举见 `transaction/status-model.md` |
| Search Balance History | `[GET] /openapi/v1/wallet/balance/history/search` 可查询 client wallet transaction history | DTC Wallet OpenAPI / 4.2.4 | 返回字段包含 `activityType`、`relatedId`、`time`、`state` 等；完整字段表见 ALL-GAP-058 |
| ActivityType | `FIAT_DEPOSIT=6`、`CRYPTO_DEPOSIT=10`、`DTC_WALLET=13`、`CARD_PAYMENT_REFUND=20` 已确认 | DTC Wallet OpenAPI / Appendix ActivityType | 具体业务映射见 ALL-GAP-001、ALL-GAP-002、ALL-GAP-037 |

## 4. Balance 与 Transaction History 的关系

Wallet Balance 不单独定义交易状态。余额变动相关状态统一引用 `transaction/status-model.md`。

| 能力 | 关系 | ALL-GAP 边界 |
|---|---|---|
| 当前余额 | 余额展示或查询的结果 | 查询接口和字段边界见 ALL-GAP-055 |
| 余额历史 | 通过 Search Balance History 查询 | 完整字段表见 ALL-GAP-058 |
| 交易详情 | 通过 Wallet Transaction Detail 查询，入参为 `transactionId` | 完整展示字段见 ALL-GAP-048 |
| 状态展示 | 引用 Wallet `state` 枚举 | 进入 / 退出条件与展示文案见 ALL-GAP-050、ALL-GAP-051 |
| 交易分类 | 引用 ActivityType，但不能把枚举直接等同具体产品路径 | 前端映射见 ALL-GAP-037 |
| 对账追踪 | 依赖 Wallet 交易 `id`、`transactionId`、`relatedId` 等字段 | 具体组合见 ALL-GAP-014、ALL-GAP-018、ALL-GAP-029 |

## 5. Search Balance History 与 ActivityType

| 枚举 | 值 | 含义 | Balance 处理 |
|---|---:|---|---|
| `FIAT_DEPOSIT` | 6 | Fiat Deposit | 可作为法币入金余额历史分类；是否对应 GTR 见 ALL-GAP-001 |
| `CRYPTO_DEPOSIT` | 10 | Stablecoin Deposit | 可作为稳定币 / Crypto 入金余额历史分类；是否对应 WC 见 ALL-GAP-002 |
| `DTC_WALLET` | 13 | DTC Wallet Payment | 可作为 DTC Wallet Payment 分类；前端展示映射见 ALL-GAP-037 |
| `CARD_PAYMENT_REFUND` | 20 | Card Payment Refund | 可作为卡退款入 Wallet 相关分类；对账关联见 ALL-GAP-017、ALL-GAP-018 |

## 6. Wallet state 引用

| 枚举 | 当前处理 |
|---|---|
| `PENDING` | 引用交易状态事实源，不在 Balance 中重新定义进入 / 退出条件 |
| `PROCESSING` | 引用交易状态事实源，不在 Balance 中重新定义进入 / 退出条件 |
| `AUTHORIZED` | 引用交易状态事实源，不在 Balance 中重新定义进入 / 退出条件 |
| `COMPLETED` | 引用交易状态事实源，不在 Balance 中重新定义进入 / 退出条件 |
| `REJECTED` | 引用交易状态事实源，不在 Balance 中重新定义进入 / 退出条件 |
| `CLOSED` | 引用交易状态事实源，不在 Balance 中重新定义进入 / 退出条件 |

DTC Crypto Deposit 中的 `status=102 Risk Withheld` 是 Deposit 外部状态来源，不得直接等同 Wallet `state` 中任一枚举。其对余额展示影响见 ALL-GAP-008。

## 7. 与 Deposit 的关系

| 场景 | Balance 可引用事实 | ALL-GAP 边界 |
|---|---|---|
| GTR Deposit | Deposit 包含 GTR；ActivityType 有 `FIAT_DEPOSIT=6` | GTR 是否使用 FIAT_DEPOSIT 见 ALL-GAP-001；资金可见时点见 ALL-GAP-005、ALL-GAP-016 |
| WalletConnect Deposit | Deposit 包含 WC；DTC Crypto Deposit 规则；ActivityType 有 `CRYPTO_DEPOSIT=10` | WC 是否使用 CRYPTO_DEPOSIT 见 ALL-GAP-002；资金可见时点见 ALL-GAP-005、ALL-GAP-016 |
| Risk Withheld | DTC Crypto Deposit 未加白会 Risk Withheld | 是否计入余额 / 是否展示冻结余额见 ALL-GAP-008 |
| Deposit success | Notification PRD 有 success 通知；payment_info success 会触发资金流转账且可能短延迟 | success 与余额增加 / 可用余额关系见 ALL-GAP-005、ALL-GAP-016 |

## 8. 与 Card balance 的边界

Card balance 与 Wallet balance 必须区分：

| 项目 | 所属模块 | 当前口径 |
|---|---|---|
| Card `balance` | Card Transaction Flow | 通过 `Inquiry Card Basic Info` 查询，作为 `Transfer Balance to Wallet` 的 amount 依据 |
| Wallet balance | Wallet Balance | 当前余额查询接口和字段边界见 ALL-GAP-055 |
| Card balance 转 Wallet | Card Transaction Flow | 已知调用 `Transfer Balance to Wallet(cardId, amount=balance)`；成功响应不返回归集业务流水 |
| Card balance 转 Wallet 后的 Wallet 关联 | Transaction Reconciliation / ALL-GAP | Wallet 交易 `id` / `relatedId` 如何关联 Card `data.id`、AIX 归集请求或 `D-REQUEST-ID` 见 ALL-GAP-014、ALL-GAP-018 |

## 9. 不写入事实的内容

以下内容当前不得写成事实：

1. Wallet balance 中可用余额字段名、冻结余额字段名、总余额字段名。
2. 将 DTC Available Currency 直接等同为 AIX 前端展示币种列表。
3. Wallet balance 与 Card balance 的币种一定一致。
4. Card balance 转 Wallet 后一定能通过 `relatedId` 关联到 Card `data.id`。
5. Wallet `transactionId` 等同于 Card `data.id`。
6. Wallet 余额变动的完整对账字段组合。
7. Wallet 余额查询失败后的用户提示文案。
8. `FIAT_DEPOSIT` 必然等同 GTR。
9. `CRYPTO_DEPOSIT` 必然等同 WalletConnect。
10. Deposit success 必然代表 Wallet balance 立即可用。
11. Risk Withheld 必然进入冻结余额。
12. Search Balance History 完整字段表已确认。

## 10. ALL-GAP 引用

本文不维护独立待补表。Wallet Balance 相关不确定项统一引用 ALL-GAP：

| 编号 | 主题 |
|---|---|
| ALL-GAP-001 | GTR 是否使用 `FIAT_DEPOSIT=6` |
| ALL-GAP-002 | WalletConnect 是否使用 `CRYPTO_DEPOSIT=10` |
| ALL-GAP-005 | `payment_info success` 后 Wallet balance 何时可用 |
| ALL-GAP-008 | Risk Withheld 与 Wallet `state` / 余额关系 |
| ALL-GAP-014 | Wallet `relatedId` 在 Card / GTR / WC 场景取值 |
| ALL-GAP-016 | Deposit success 与 Wallet `state=COMPLETED` 的映射 |
| ALL-GAP-017 | Card Transaction 与 Wallet Transaction 是否一一对应 |
| ALL-GAP-018 | Card / Wallet 关联字段 |
| ALL-GAP-029 | 财务 / 运营最终对账字段组合 |
| ALL-GAP-037 | ActivityType 到 AIX 前端交易类型的映射 |
| ALL-GAP-048 | Wallet Transaction Detail 完整请求 / 响应 / 页面展示 / 复制规则 |
| ALL-GAP-050 | Wallet `state` 进入 / 退出条件 |
| ALL-GAP-051 | Wallet 状态与前端展示文案映射 |
| ALL-GAP-055 | Wallet 当前余额查询接口和字段边界 |
| ALL-GAP-056 | Wallet 余额展示规则 |
| ALL-GAP-057 | Wallet 余额查询失败处理 |
| ALL-GAP-058 | Search Balance History 完整字段表 |

## 11. 历史待补字段到 ALL-GAP 映射

本表用于无损迁移历史问题，不作为新的模块级 checklist。后续只维护 ALL-GAP。

| 原待补项 | 当前 ALL-GAP |
|---|---|
| Wallet 当前余额查询接口路径 | 已确认：`[GET] /openapi/v1/wallet/balance/{currency}` 与 `[GET] /openapi/v1/wallet/balances` |
| Wallet 当前余额请求字段 | 部分已确认：单币种接口路径参数包含 `currency`；其余请求字段边界见 ALL-GAP-055 |
| Wallet 当前余额响应字段 | 部分已确认：接口用于返回余额；完整响应字段边界见 ALL-GAP-055 |
| 可用余额 / 冻结余额 / 总余额字段 | ALL-GAP-055 |
| 余额币种字段 | ALL-GAP-055 |
| 余额展示排序 | ALL-GAP-056 |
| 小额余额 / 零余额展示规则 | ALL-GAP-056 |
| 余额查询失败处理 | ALL-GAP-057 |
| Search Balance History 完整字段表 | ALL-GAP-058 |
| Risk Withheld 对余额展示影响 | ALL-GAP-008 |

## 12. 来源引用

- (Ref: DTC Wallet OpenAPI Document20260126 / 4.2.4 Search Balance History)
- (Ref: DTC Wallet OpenAPI Document20260126 / Appendix ActivityType)
- (Ref: DTC Wallet OpenAPI Document20260126 / 3.4 Crypto Deposit)
- (Ref: knowledge-base/transaction/history.md / v1.3)
- (Ref: knowledge-base/transaction/status-model.md / v1.2)
- (Ref: knowledge-base/wallet/deposit.md / v1.6)
- (Ref: knowledge-base/card/card-transaction-flow.md / v1.3)
- (Ref: knowledge-base/changelog/knowledge-gaps.md / ALL-GAP 总表)
- (Ref: 用户确认结论 / 2026-05-01)
- (Ref: 用户确认结论 / 2026-05-02 / ALL-GAP 唯一总表与无损迁移规则)
