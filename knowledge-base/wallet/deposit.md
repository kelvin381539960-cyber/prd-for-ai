---
module: wallet
feature: deposit
version: "1.4"
status: active
source_doc: DTC Wallet OpenAPI Documentation；DTC接口文档/DTC Wallet OpenAPI Document20260126 (1).docx；[2025-11-25] AIX+Notification（push及站内信）.docx；knowledge-base/wallet/_index.md；knowledge-base/wallet/balance.md；knowledge-base/wallet/transaction-history.md；knowledge-base/common/walletconnect.md；knowledge-base/common/notification.md；knowledge-base/common/errors.md；knowledge-base/changelog/knowledge-gaps.md；用户确认结论 2026-05-01
source_section: DTC Wallet OpenAPI / 3.4 Crypto Deposit；4.2.4 Search Balance History；Appendix ActivityType；Notification Deposit rows；Wallet Deposit / GTR / WalletConnect
last_updated: 2026-05-01
owner: 吴忆锋
depends_on:
  - wallet/_index
  - wallet/balance
  - wallet/transaction-history
  - common/walletconnect
  - common/notification
  - common/errors
  - common/dtc
  - changelog/knowledge-gaps
---

# Wallet Deposit 钱包充值

## 1. 当前状态

Wallet Deposit 当前状态为 `active`。

根据用户确认，Deposit 能力存在，包含两条已确认入金路径：

1. GTR Deposit。
2. WalletConnect Deposit。

需要注意：GTR 与 WalletConnect 只能作为两条并列子路径处理。除非来源明确，不得默认二者使用同一套字段、状态、风控、白名单、Declare / Travel Rule 或通知规则。

## 2. 模块定位

Wallet Deposit 用于沉淀 AIX Wallet 入金相关能力，包括 GTR 入金、WalletConnect 入金、入金交易记录、余额变化、状态和异常边界。

DTC Wallet OpenAPI 中存在 Crypto Deposit 规则：Crypto business 包含 whitelisting、deposit、withdrawal；Crypto 充值涉及 senderAddress 与 destinationAddress；destinationAddress 由 DTC 自动分配；senderAddress 需要加入 whitelist 并 enable；未加白时交易会进入 `status=102 Risk Withheld`；加白成功后交易会自动变为 success。

上述是 DTC Crypto Deposit 外部依赖事实，不等同于 GTR / WalletConnect 的完整产品流程。AIX 侧页面、入口、Declare / Travel Rule、通知跳转、人工处理仍需按 PRD / 产品确认补齐。

## 3. Deposit 子路径总览

| 子路径 | 当前状态 | 当前可写事实 | 当前不可写事实 |
|---|---|---|---|
| GTR Deposit | active / 待补细节 | Deposit 包含 GTR | 完整流程、字段、状态、风控、通知、Declare、白名单是否完全适用 |
| WalletConnect Deposit | active / 待补细节 | Deposit 包含 WalletConnect；可引用 DTC Crypto Deposit 外部依赖边界 | 完整页面流程、授权流程、字段映射、Declare、通知、人工处理 |
| 其他 Deposit 旧方案 | 未确认 | 不写 | 不得默认归档为 active |
| Send | deferred | 不属于 Deposit active 范围 | 不写成当前已上线 |
| Swap | deferred | 不属于 Deposit active 范围 | 不写成当前已上线 |

## 4. DTC Crypto Deposit 已确认依赖事实

| 项目 | 已确认事实 | 来源 | AIX 处理 |
|---|---|---|---|
| Crypto Deposit 范围 | Crypto business includes whitelisting, deposit, and withdrawal | DTC Wallet OpenAPI / 3.4 Crypto Deposit | 作为外部依赖边界 |
| 发送 / 收款地址 | Crypto recharge involves senderAddress and destinationAddress | DTC Wallet OpenAPI / 3.4 Crypto Deposit | AIX 需区分来源地址和收款地址 |
| 收款地址来源 | destinationAddress 由 DTC 自动分配；调用 `[POST] /openapi/v1/crypto-account/deposit-address/search-obj` 返回 deposit recipient address | DTC Wallet OpenAPI / 3.4 Crypto Deposit | 可作为 Deposit 收款地址来源 |
| 白名单规则 | senderAddress 需要加入 whitelist 并 enable | DTC Wallet OpenAPI / 3.4 Crypto Deposit | 可作为 Crypto Deposit 规则；是否完全覆盖 GTR / WC 待确认 |
| 未加白结果 | 未加 senderAddress whitelist 时，交易会被设为 risky transaction，`status=102 Risk Withheld` | DTC Wallet OpenAPI / 3.4 Crypto Deposit | 可作为 on-hold / 风控状态来源 |
| 加白后结果 | 用户继续加白并 enable 后，交易会自动变为 success | DTC Wallet OpenAPI / 3.4 Crypto Deposit | AIX 是否监听状态变化 / 通知需补 |

## 5. GTR Deposit

### 5.1 当前可确认

| 项目 | 结论 | 来源 |
|---|---|---|
| GTR 属于 Deposit 子路径 | 是 | 用户确认 2026-05-01 |
| GTR 当前是否 active | 是，作为 Deposit active 子路径 | 用户确认 2026-05-01 |
| GTR 是否等同 WalletConnect | 否，需拆分处理 | 用户确认 Deposit 包含两条路径 |

### 5.2 GTR 待补事项

| 问题 | 当前处理 | 影响 |
|---|---|---|
| GTR 入金触发方式 | 待补 | 无法形成完整流程 |
| GTR 入口 / 页面路径 | 待补 | 无法形成用户路径 |
| GTR 支持币种 / 链 | 待补 | 无法形成资产边界 |
| GTR 入金交易 ID 字段 | 待补 | 无法形成交易追踪 |
| GTR 入金状态映射 | 待补 | 无法形成状态闭环 |
| GTR 是否适用 DTC Crypto Deposit whitelist 规则 | 待补 | 合规 / 风控边界不完整 |
| GTR 是否需要 Declare / Travel Rule | 待补 | 合规边界不完整 |
| GTR on-hold / risk rejected 展示 | 可引用 `Risk Withheld` 作为 DTC 状态来源，但 AIX 展示待补 | 异常分支不完整 |
| GTR 成功 / 失败通知 | 待补 | 用户通知边界不完整 |
| GTR 资金可见时点 | 待补 | Wallet balance 变化口径不完整 |

## 6. WalletConnect Deposit

### 6.1 当前可确认

| 项目 | 结论 | 来源 |
|---|---|---|
| WalletConnect 属于 Deposit 子路径 | 是 | 用户确认 2026-05-01 |
| WalletConnect 当前是否 active | 是，作为 Deposit active 子路径 | 用户确认 2026-05-01 |
| WalletConnect 是否等同 GTR | 否，需拆分处理 | 用户确认 Deposit 包含两条路径 |
| WalletConnect 不属于 Send / Swap | 是 | common/walletconnect.md |
| WalletConnect 可引用的 DTC 外部依赖 | Crypto Deposit 涉及 senderAddress / destinationAddress / whitelist / Risk Withheld / success | DTC Wallet OpenAPI / 3.4 Crypto Deposit |

### 6.2 WalletConnect 待补事项

| 问题 | 当前处理 | 影响 |
|---|---|---|
| WalletConnect 连接 / 授权流程 | 待补 | 无法形成完整用户路径 |
| WalletConnect 支持钱包范围 | 待补 | 无法形成三方钱包边界 |
| WalletConnect 支持币种 / 链 | 待补 | 无法形成资产边界 |
| WalletConnect senderAddress 获取方式 | 待补 | 无法判断 whitelist 规则如何落地 |
| WalletConnect destinationAddress 展示方式 | DTC 自动分配地址已确认；AIX 展示待补 | 页面边界待补 |
| WalletConnect 入金交易 ID 字段 | 待补 | 无法形成交易追踪 |
| WalletConnect 入金状态映射 | 可引用 DTC `Risk Withheld` / success；完整状态待补 | 状态闭环不完整 |
| WalletConnect 是否需要 Declare / Travel Rule | 待补 | 合规边界不完整 |
| WalletConnect on-hold / risk rejected 规则 | DTC 未加白会 Risk Withheld 已确认；AIX 展示和处理待补 | 异常分支不完整 |
| WalletConnect 成功 / 失败通知 | Deposit success / under review 通知触发见 Notification；完整规则待补 | 用户通知边界不完整 |
| WalletConnect 资金可见时点 | 待补 | Wallet balance 变化口径不完整 |

## 7. Deposit 与 Balance / History 的关系

| 能力 | 当前可引用 | 当前待补 |
|---|---|---|
| Deposit 收款地址 | DTC `deposit-address/search-obj` 返回 deposit recipient address | AIX 页面展示、复制、二维码、链 / 币种选择 |
| Deposit 记录 ID | Wallet 交易 `id` 存在 | GTR / WC 记录生成时机 |
| Deposit 详情查询 | Wallet 详情入参 `transactionId` 存在 | GTR / WC transactionId 来源 |
| Deposit 状态 | DTC Crypto Deposit 有 Risk Withheld / success 规则；Wallet `state` 枚举存在 | GTR / WC 与 Wallet `state` 的映射 |
| Deposit 余额历史 | Search Balance History 存在，ActivityType 包含 `CRYPTO_DEPOSIT=10`、`FIAT_DEPOSIT=6` | GTR / WC `relatedId` 取值 |

## 8. Deposit 通知边界

| 通知 | GTR | WalletConnect | 当前处理 |
|---|---|---|---|
| 入金成功通知 | 待补 | Notification 表记录 `event=CRYPTO_TXN`、`type=DEPOSIT`、`state=success` | 可写入通知事实，但具体 webhook 逻辑仍待定义 |
| 入金冻结 / review 通知 | 待补 | Notification 表记录 `event=CRYPTO_TXN`、`type=DEPOSIT`、`state=RISK_WITHHELD` | 可写入通知事实，但具体 webhook 逻辑仍待定义 |
| 入金失败通知 | 待补 | 待补 | 无来源，不写成事实 |
| Declare / Travel Rule 通知 | 待补 | 待补 | 需合规 / Notification 来源 |

## 9. Deposit 错误与人工处理边界

| 场景 | GTR | WalletConnect | 当前处理 |
|---|---|---|---|
| 未加白 | 是否适用待确认 | DTC Crypto Deposit 已确认：未加白会 Risk Withheld | AIX 页面 / 用户提示待补 |
| 加白后状态恢复 | 是否适用待确认 | DTC Crypto Deposit 已确认：加白成功后自动变 success | AIX 是否通知 / 刷新待补 |
| 入金失败原因 | 待补 | 待补 | 需错误码 / PRD |
| 用户反馈处理 | 待补 | 待补 | 需客服 / 运营口径 |
| 人工补偿 | 待补 | 待补 | 需后台 / 后端确认 |

## 10. 不写入事实的内容

以下内容当前不得写成事实：

1. GTR 与 WalletConnect 使用同一套字段、状态或风控规则。
2. DTC Crypto Deposit 规则自动等同于所有 GTR / WalletConnect 产品规则。
3. 所有 Deposit 都需要 Declare。
4. 所有 Deposit 都不需要 Declare。
5. Deposit 成功一定等同于 Wallet balance 立即可用。
6. Deposit 状态完全等同于 Wallet `state` 枚举中的某几个值。
7. Deposit 成功 / 失败通知文案已完整确认。
8. Card balance 自动归集属于 Wallet Deposit。
9. WalletConnect 属于 Send 或 Swap。
10. GTR / WalletConnect 的 `relatedId` 取值已确认。

## 11. 后续补材料清单

| 优先级 | 待补项 | 目标来源 |
|---|---|---|
| P0 | GTR 完整流程、入口、字段、状态、失败处理 | GTR PRD / 接口文档 / 截图 |
| P0 | WalletConnect 完整流程、入口、字段、状态、失败处理 | WC PRD / 接口文档 / 截图 |
| P0 | GTR / WC Declare / Travel Rule 规则 | 合规 PRD / 产品确认 |
| P0 | GTR / WC 是否完全适用 Crypto Deposit whitelist 规则 | GTR / WC PRD / 产品确认 |
| P0 | GTR / WC 通知跳转、文案、前端展示 | Notification PRD / 已确认结论 |
| P1 | GTR / WC 客服与人工处理口径 | 客服 / 运营 / 后台 PRD |

## 12. 来源引用

- (Ref: DTC Wallet OpenAPI Document20260126 / 3.4 Crypto Deposit)
- (Ref: DTC Wallet OpenAPI Document20260126 / 4.2.4 Search Balance History)
- (Ref: DTC Wallet OpenAPI Document20260126 / Appendix ActivityType)
- (Ref: [2025-11-25] AIX+Notification / Deposit rows)
- (Ref: 用户确认结论 / 2026-05-01 / Deposit 包含 GTR 和 WalletConnect)
