---
module: common
feature: walletconnect-integration
version: "1.2"
status: active
source_doc: IMPLEMENTATION_PLAN.md；DTC接口文档/DTC Wallet OpenAPI Document20260126 (1).docx；knowledge-base/wallet/deposit.md；knowledge-base/common/dtc.md；knowledge-base/common/notification.md；knowledge-base/common/errors.md
source_section: DTC Wallet OpenAPI / 3.4 Crypto Deposit；4.2.4 Search Balance History；Appendix ActivityType；Wallet Deposit v1.4；DTC Dependency v1.2
last_updated: 2026-05-01
owner: 吴忆锋
depends_on:
  - common/_index
  - common/dtc
  - common/notification
  - common/errors
  - wallet/deposit
  - wallet/stage-review
---

# WalletConnect Integration 公共集成边界

## 1. 功能定位

WalletConnect Integration 用于沉淀 AIX WalletConnect 入金相关的公共集成边界，包括第三方钱包连接、入金路径、DTC Crypto Deposit 外部依赖、状态、风控、白名单、通知和错误处理。

本文只确认 WalletConnect 属于 Deposit 的一条入金路径，并引用 DTC Crypto Deposit 已确认的外部依赖规则。不补写未确认的 WalletConnect 页面流程、SDK 交互、Declare / Travel Rule 规则或 AIX 内部处理。

## 2. 当前已确认事实

| 项目 | 结论 | 来源 | 备注 |
|---|---|---|---|
| Deposit 能力存在 | Deposit 包含 GTR 和 WalletConnect | Wallet Deposit / 用户确认 | WalletConnect 属于 Deposit 子路径 |
| WalletConnect 当前归属 | Wallet Deposit 子路径 | Wallet Deposit | 不属于 Send / Swap |
| WalletConnect 与 GTR 关系 | 二者并列，不能默认共用流程、字段、状态、风控、通知 | Wallet Deposit v1.4 | 需拆分处理 |
| DTC Crypto Deposit | Crypto business includes whitelisting、deposit、withdrawal | DTC Wallet OpenAPI / 3.4 | 可作为 WC 外部依赖边界 |
| Deposit 地址 | DTC 自动分配 destinationAddress，接口 `[POST] /openapi/v1/crypto-account/deposit-address/search-obj` 返回 deposit recipient address | DTC Wallet OpenAPI / 3.4 | AIX 页面展示待补 |
| 白名单 | senderAddress 需要加入 whitelist 并 enable | DTC Wallet OpenAPI / 3.4 | WC 如何获取 senderAddress 待补 |
| Risk Withheld | 未加 senderAddress 白名单时，交易进入 `status=102 Risk Withheld` | DTC Wallet OpenAPI / 3.4 | AIX 展示 / 通知 / 人工处理待补 |
| 加白后状态 | add whitelist successful 后，交易自动变为 success | DTC Wallet OpenAPI / 3.4 | AIX 是否监听 / 刷新待补 |
| Send | deferred，未上线 | Wallet Stage Review | 不纳入 WalletConnect active 能力 |
| Swap | deferred，未上线且需重做 | Wallet Stage Review | 不纳入 WalletConnect active 能力 |

## 3. WalletConnect 入金链路结构

| 阶段 | 当前处理 | 来源 / 待补 |
|---|---|---|
| 入口展示 | 待补 | WalletConnect PRD / 截图 |
| 三方钱包连接 | 待补 | WalletConnect PRD / SDK / 接口文档 |
| 钱包授权 / 用户确认 | 待补 | WalletConnect PRD / 钱包交互说明 |
| 入金发起 | DTC Crypto Deposit 涉及 senderAddress / destinationAddress | DTC Wallet OpenAPI / 3.4 |
| 收款地址 | DTC 自动分配 destinationAddress | DTC Wallet OpenAPI / 3.4 |
| 发送地址 | senderAddress 需加白并 enable | DTC Wallet OpenAPI / 3.4 |
| Risk Withheld | 未加白会进入 `status=102 Risk Withheld` | DTC Wallet OpenAPI / 3.4 |
| Success | 加白成功后自动变为 success | DTC Wallet OpenAPI / 3.4 |
| Wallet 余额可见 | 待补 | 产品 / 后端 / DTC Wallet OpenAPI |
| 交易记录生成 | 待补 | DTC Wallet OpenAPI / 后端确认 |
| 通知触发 | Deposit success / Risk Withheld 有 Notification 记录；具体逻辑待定义 | Notification PRD / sheet4 |

## 4. 合规 / 风控 / 白名单边界

| 问题 | 当前处理 |
|---|---|
| WalletConnect 是否必须 Declare | 待补，不写成事实 |
| WalletConnect 什么情况下必须 Declare | 待补，不写成事实 |
| WalletConnect 什么情况下不需要 Declare | 待补，不写成事实 |
| WalletConnect 是否需要地址白名单 | DTC Crypto Deposit 已确认 senderAddress 需要 whitelist；是否作为 WC 产品前置仍待确认 |
| WalletConnect 加白发生在入金前还是入金后 | DTC 说明未加白会 Risk Withheld，用户后续加白成功后交易自动 success；AIX 产品路径待补 |
| WalletConnect 是否存在 on-hold | 可引用 `Risk Withheld` 作为 DTC 外部状态来源 |
| WalletConnect 是否存在 risk rejected | DTC 文档确认 Risk Withheld，不等同所有 rejected 场景 |
| WalletConnect 风控拦截后是否入 Wallet balance | 待补，不写成事实 |
| WalletConnect 风控拦截后用户是否可见资金 | 待补，不写成事实 |

## 5. 与 DTC 的关系

| 项目 | 当前处理 |
|---|---|
| WalletConnect 是否使用 DTC Wallet 接口 | 可引用 DTC Crypto Deposit / Deposit Address / Crypto Transaction / Balance History 相关能力；AIX 具体调用链待补 |
| WalletConnect 入金交易 ID | CryptoTransaction 中 `id` 为 Transaction ID；与 AIX / Wallet `transactionId` 映射待补 |
| WalletConnect 与 Wallet `transactionId` 的关系 | 待补 |
| WalletConnect 与 Wallet `id` 的关系 | 待补 |
| WalletConnect 与 Wallet `relatedId` 的关系 | 待补 |
| WalletConnect 与 Search Balance History `activityType` 的关系 | ActivityType 有 `CRYPTO_DEPOSIT=10 Stablecoin Deposit`；具体 WC 分类待补 |
| WalletConnect 失败错误码 | 待补 |
| WalletConnect Webhook / 回调 | Notification 记录 Deposit success / Risk Withheld 来自 Webhook→notify，但具体逻辑待定义 |

## 6. 与 Notification 的关系

| 通知 | 当前处理 |
|---|---|
| WalletConnect 入金成功通知 | Notification 记录 Deposit success：event=`CRYPTO_TXN`、type=`DEPOSIT`、state=`success`；是否专属于 WC 待补 |
| WalletConnect Risk Withheld / under review 通知 | Notification 记录 Deposit under review：event=`CRYPTO_TXN`、type=`DEPOSIT`、state=`RISK_WITHHELD`；是否专属于 WC 待补 |
| WalletConnect 入金失败通知 | 待补 |
| WalletConnect Declare 待处理通知 | 待补 |
| WalletConnect 钱包连接失败通知 | 待补，不能默认存在 |
| WalletConnect 通知跳转 | Notification 记录跳转交易详情页；具体 WC 跳转目标待确认 |

## 7. 与 Errors 的关系

| 错误 / 异常 | 当前处理 |
|---|---|
| 用户取消连接 / 拒绝授权 | 待补 |
| 第三方钱包连接失败 | 待补 |
| 未加白 | DTC Crypto Deposit 确认为 Risk Withheld |
| 加白后状态恢复 | DTC Crypto Deposit 确认为自动变 success |
| 入金失败 | 待补 |
| 钱包余额未更新 | 待补 |
| 人工处理 / 客服口径 | 待补 |

## 8. 不写入事实的内容

以下内容当前不得写成事实：

1. WalletConnect 与 GTR 使用同一套流程、字段、状态机、风控规则或通知规则。
2. DTC Crypto Deposit 规则自动等同于所有 WalletConnect 产品交互。
3. WalletConnect 一定需要 Declare。
4. WalletConnect 一定不需要 Declare。
5. WalletConnect 入金成功一定立即增加可用余额。
6. WalletConnect 成功 / 失败通知已完整确认。
7. WalletConnect 属于 Send 或 Swap。
8. WalletConnect 的 `transactionId`、`id`、`relatedId` 关联规则已确认。
9. `Risk Withheld` 等同所有 risk rejected / on-hold 场景。

## 9. 待补项

| 编号 | 待补项 | 来源建议 | 当前处理 |
|---|---|---|---|
| WC-GAP-001 | WalletConnect 完整页面与 SDK 流程 | WalletConnect PRD / 截图 / SDK 文档 | 待补 |
| WC-GAP-002 | WalletConnect 支持钱包范围 | PRD / 产品确认 | 待补 |
| WC-GAP-003 | WalletConnect 支持币种 / 链 | PRD / DTC Wallet OpenAPI | 待补 |
| WC-GAP-004 | WalletConnect Declare / Travel Rule 规则 | 合规 PRD / 产品确认 | 待补 |
| WC-GAP-005 | WalletConnect senderAddress 获取和加白路径 | PRD / 后端确认 | 待补 |
| WC-GAP-006 | WalletConnect 钱包交易字段映射 | DTC Wallet OpenAPI / 后端确认 | 待补 |
| WC-GAP-007 | WalletConnect 失败原因和用户提示 | PRD / 错误码 / 客服口径 | 待补 |
| WC-GAP-008 | WalletConnect 与 GTR 的差异表 | GTR / WC PRD | 待补 |

## 10. 来源引用

- (Ref: DTC Wallet OpenAPI Document20260126 / 3.4 Crypto Deposit)
- (Ref: DTC Wallet OpenAPI Document20260126 / 4.2.4 Search Balance History)
- (Ref: DTC Wallet OpenAPI Document20260126 / Appendix ActivityType)
- (Ref: [2025-11-25] AIX+Notification / Deposit rows)
- (Ref: knowledge-base/wallet/deposit.md / v1.4)
- (Ref: knowledge-base/common/dtc.md / v1.2)
