---
module: wallet
feature: wallet-index
version: "1.0"
status: active
source_doc: IMPLEMENTATION_PLAN.md；DTC Wallet OpenAPI Documentation；DTC接口文档/DTC Card Issuing API Document_20260310 (1).pdf；knowledge-base/card/card-transaction-flow.md；knowledge-base/changelog/knowledge-gaps.md；用户确认结论 2026-05-01
source_section: IMPLEMENTATION_PLAN v3.5 / 12.5；DTC Wallet 钱包交易记录 / 钱包交易详情 / Search Balance History；Card Transaction Flow v1.2；Card deferred gaps
last_updated: 2026-05-01
owner: 吴忆锋
depends_on:
  - card/card-transaction-flow
  - changelog/knowledge-gaps
  - _meta/writing-standard
---

# Wallet 模块索引

## 1. 模块定位

Wallet 模块用于沉淀 AIX 钱包相关能力，包括钱包开户 / KYC 前置、余额展示、充值 / 收款、提现 / 发送、Swap、钱包交易记录与交易详情。

本阶段从 Wallet 事实源开始转译，不回填 Card Transaction Flow 的 deferred gaps。

涉及 Card 资金归集时，只引用已确认事实：

- DTC Card Transaction Notify 已明确。
- `data.id` 为 DTC Card Transaction ID。
- `Transfer Balance to Wallet` 请求字段为 `cardId`、`amount`。
- 成功响应仅返回 `header.success=true`，不返回归集业务流水。
- Wallet 交易记录 / 详情出参包含 `id`，Long，交易 id。
- Wallet 单笔交易详情入参为 `transactionId`，Unique transaction ID from DTC。
- Wallet 交易状态字段为 `state`，枚举为 `PENDING`、`PROCESSING`、`AUTHORIZED`、`COMPLETED`、`REJECTED`、`CLOSED`。

未确认的 Card 归集链路问题继续保留在 `knowledge-gaps.md`，不得在 Wallet 正文中补写为事实。

## 2. 当前阶段任务

| 文件 | 状态 | 目标 | 备注 |
|---|---|---|---|
| `wallet/_index.md` | active | 建立 Wallet 模块边界、能力清单与依赖关系 | 当前文件 |
| `wallet/kyc.md` | Todo | 转译 Wallet KYC / DTC 钱包开户与前置条件 | 后续执行 |
| `wallet/balance.md` | Todo | 转译钱包余额、币种、余额展示与查询接口 | 后续执行 |
| `wallet/deposit.md` | Todo | 转译 Crypto / Fiat Deposit，含地址、白名单、风险拦截与通知边界 | 后续执行 |
| `wallet/receive.md` | Todo | 转译 Receive / Deposit Address / Whitelist Address 相关能力 | 后续执行 |
| `wallet/send.md` | Todo | 转译 Crypto Withdraw / Send 相关能力 | 后续执行 |
| `wallet/swap.md` | Todo | 转译 Swap / OTC / Quote / Order 相关能力 | 后续执行 |
| `wallet/transaction-history.md` | Todo | 转译 Wallet Search Balance History、交易详情、状态与展示字段 | 后续执行 |
| `wallet/stage-review.md` | Todo | Wallet 阶段完成后执行 Stage Review | 后续执行 |

## 3. 能力边界

| 能力域 | 包含 | 不包含 | 备注 |
|---|---|---|---|
| Wallet KYC / 开户 | 钱包能力前置条件、钱包账户创建、KYC 依赖 | Card 申卡 KYC 细节 | 需引用 Account / Security / KYC 事实源 |
| Balance | 钱包余额、币种、可用余额、展示规则、余额接口 | Card balance | Card balance 仅在 Card Transaction Flow 中作为归集金额依据 |
| Deposit / Receive | 充值地址、收款地址、链、币种、白名单、充值状态 | Card 自动归集 | Card 自动归集是 Card Transaction Flow，不归入 Wallet Deposit 主流程 |
| Send / Withdraw | 提现 / 转出、地址、手续费、链路状态 | Card Transfer Balance to Wallet | 需区分钱包主动转出与卡余额归集 |
| Swap | 报价、下单、兑换状态、失败处理 | Card 消费 / 退款 | 后续由 Swap 文档独立收口 |
| Transaction History | Wallet 交易列表、交易详情、状态字段、筛选展示 | Card History 交易展示 | 后续 Transaction 统一层再做跨模块状态统一 |
| Notification | Wallet 相关通知触发、push / 站内信边界 | Card 通知正文 | 需引用 Notification PRD，不补文案 |

## 4. 已确认 Wallet 基础字段

| 字段 / 能力 | 结论 | 来源 | 备注 |
|---|---|---|---|
| Wallet 交易 `id` | 钱包交易记录 / 详情出参均包含 `id`，Long，交易 id | DTC Wallet OpenAPI；用户确认 2026-05-01 | 可作为 Wallet 交易基础 ID |
| Wallet 详情入参 `transactionId` | 单笔钱包交易详情入参为 `transactionId`，Unique transaction ID from DTC | DTC Wallet OpenAPI；用户确认 2026-05-01 | 与 Card `data.id` / `D-REQUEST-ID` 的关系未确认 |
| Wallet 交易 `state` | 枚举为 `PENDING`、`PROCESSING`、`AUTHORIZED`、`COMPLETED`、`REJECTED`、`CLOSED` | DTC Wallet OpenAPI；用户确认 2026-05-01 | 可用于 Wallet 交易记录与详情 |
| Wallet Search Balance History | 可查询钱包交易历史，返回 `activityType`、`relatedId`、`time`、`state` 等字段 | DTC Wallet OpenAPI / 4.2.4 | `relatedId` 在卡余额转 Wallet 场景下仍是 deferred gap |

## 5. 与 Card deferred gaps 的关系

以下内容不得在 Wallet 阶段补写为事实：

| Deferred gap | 当前处理 |
|---|---|
| AIX 内部交易处理 ID | 继续保留在 `knowledge-gaps.md` |
| AIX 归集请求 ID | 继续保留在 `knowledge-gaps.md` |
| `D-REQUEST-ID` 与归集请求 ID 的关联 | 继续保留在 `knowledge-gaps.md` |
| Wallet 交易 `id` 与 Card `data.id` / AIX 归集请求 / `D-REQUEST-ID` 的关联 | 继续保留在 `knowledge-gaps.md` |
| Wallet `relatedId` 在卡余额转 Wallet 场景下取值 | 继续保留在 `knowledge-gaps.md` |
| Card balance 转 Wallet 入账币种是否完全等同于 card currency | 继续保留在 `knowledge-gaps.md` |
| 最终对账字段组合 | 继续保留在 `knowledge-gaps.md` |

## 6. 转译顺序建议

| 顺序 | 文件 | 原因 |
|---|---|---|
| 1 | `wallet/transaction-history.md` | 已有 Wallet `id`、`transactionId`、`state` 等接口字段，可优先形成 Wallet 状态与交易事实源 |
| 2 | `wallet/balance.md` | 余额是 Deposit / Send / Swap 的共用基础 |
| 3 | `wallet/deposit.md` | 充值链路通常涉及到账状态、通知和风控拦截 |
| 4 | `wallet/receive.md` | 与 Deposit 地址和收款地址能力相关 |
| 5 | `wallet/send.md` | 涉及提现、地址、手续费、失败处理和安全校验 |
| 6 | `wallet/swap.md` | 涉及报价、订单、成交和失败状态 |
| 7 | `wallet/kyc.md` | 如 Wallet 开户 / KYC 资料已在其他模块前置，可在 Wallet 阶段中后段收口 |
| 8 | `wallet/stage-review.md` | 完成 Wallet 阶段 Gate Review |

## 7. Stage Review 关注点

Wallet 阶段完成后必须检查：

1. Wallet 状态是否闭环。
2. 充值、提现、Swap、交易历史的接口路径和字段来源是否明确。
3. amount、currency、chain、address、fee、status、transactionId 等关键字段是否有来源。
4. 失败分支是否有明确状态、告警、人工处理或用户提示。
5. 与 Card Transaction Flow 的 deferred gaps 是否保持隔离，未被写成事实。
6. 与后续 Transaction 统一层的边界是否清晰。

## 8. 来源引用

- (Ref: IMPLEMENTATION_PLAN.md / v3.5 / 12.5 阶段 5：Wallet 批量推进)
- (Ref: DTC Wallet OpenAPI Documentation / Wallet 交易记录 / 钱包交易详情 / Search Balance History)
- (Ref: DTC Card Issuing API Document_20260310 (1).pdf / 3.3.3 transfer to wallet)
- (Ref: knowledge-base/card/card-transaction-flow.md / v1.2)
- (Ref: knowledge-base/changelog/knowledge-gaps.md / Card Transaction Flow deferred gaps)
- (Ref: 用户确认结论 / 2026-05-01)
