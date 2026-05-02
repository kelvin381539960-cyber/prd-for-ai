---
module: common
feature: dtc-dependency
version: "1.6"
status: active
source_doc: DTC接口文档/Master sub account 设计方案 (2).docx；DTC接口文档/DTC Wallet OpenAPI Document20260126 (1).docx；DTC接口文档/卡交易&钱包交易状态梳理 (1).docx；knowledge-base/kyc/account-opening.md；knowledge-base/wallet/deposit.md；knowledge-base/wallet/balance.md；knowledge-base/transaction/history.md；knowledge-base/transaction/detail.md；knowledge-base/transaction/reconciliation.md；knowledge-base/common/walletconnect.md；knowledge-base/common/notification.md；knowledge-base/common/errors.md；knowledge-base/changelog/knowledge-gaps.md；knowledge-base/_system-boundary.md；用户确认结论 2026-05-02
source_section: Master / Sub Account；D-SUB-ACCOUNT-ID；WalletAccount；DTC Wallet OpenAPI / 3.4 Crypto Deposit；4.2.4 Search Balance History；Appendix ActivityType；ALL-GAP 总表
last_updated: 2026-05-02
owner: 吴忆锋
depends_on:
  - kyc/account-opening
  - wallet/deposit
  - wallet/balance
  - transaction/history
  - transaction/detail
  - transaction/reconciliation
  - common/walletconnect
  - common/notification
  - common/errors
  - changelog/knowledge-gaps
  - _system-boundary
---

# DTC Dependency 外部依赖边界

## 1. 功能定位

DTC 是 AIX 的外部供应商系统，不是 AIX 内部系统，也不是本知识库需要维护的供应商系统说明书。

本文只保留与 AIX 系统设计有关的 DTC 依赖边界：哪些 DTC 能力会影响 AIX 页面、状态、字段、通知、错误处理、资金追踪、对账、开户和外部账户上下文。

所有未确认问题统一引用 `knowledge-base/changelog/knowledge-gaps.md` 的 ALL-GAP 编号；本文不维护本地 DTC-GAP checklist，也不保留历史 DTC-GAP 映射表。

不维护范围：

1. DTC 完整产品说明。
2. DTC 内部系统逻辑。
3. DTC 完整接口字段。
4. DTC 完整错误码表。
5. 未被 AIX 产品 / 前端 / 后端 / 对账使用的供应商字段。
6. DTC Master / Sub Account 内部实现。

## 2. 当前已确认且影响 AIX 设计的 DTC 依赖事实

| 项目 | 结论 | AIX 设计影响 |
|---|---|---|
| DTC 时间 | 时间相关值默认基于 Singapore Timezone | AIX 展示、查询、对账需注意时区 |
| Master / Sub Account | DTC 存在 Master Account / Sub Account 账户模型，Sub Account 注册在 Master Account 下 | 影响 Account Opening / KYC、用户外部账户上下文、Wallet 能力准入 |
| `D-SUB-ACCOUNT-ID` | DTC 请求头，表示 Master Account 下注册的 Sub Account ID | 影响 WalletConnect、Wallet Account、Deposit、Balance、History 等能力的外部账户上下文 |
| WalletAccount | DTC Wallet Account 对象包含 `id`、`clientId`、`status`、`currency`、`balance`、`label`、`createdDate`、`lastUpdatedDate` 等字段 | 影响 Wallet Account 状态、余额、币种和账户可用性判断 |
| Deposit Address | `destinationAddress` 由 DTC 自动分配，接口返回充值收款地址 | 影响 AIX Deposit 页面展示、复制、二维码 |
| Sender Address Whitelist | Crypto 充值涉及 `senderAddress` / `destinationAddress`；`senderAddress` 需 whitelist 并 enable | 影响 WalletConnect / Deposit 白名单、准入、异常状态；产品边界见 ALL-GAP-044 |
| Risk Withheld | 未添加 `senderAddress` 白名单时，交易进入 `status=102 Risk Withheld` | 影响 AIX under review 状态、通知、错误处理、客服口径；余额 / state 关系见 ALL-GAP-008 |
| Whitelist 后自动成功 | 用户继续加白并 enable 后交易自动变为 success | 影响 AIX 状态刷新、通知、余额可见时点；通知覆盖见 ALL-GAP-010 |
| Search Balance History | `[GET] /openapi/v1/wallet/balance/history/search` 查询 client wallet transaction history | 影响 Wallet History / Balance History / Transaction History；完整字段见 ALL-GAP-058 |
| ActivityType | `FIAT_DEPOSIT=6`、`CRYPTO_DEPOSIT=10`、`DTC_WALLET=13`、`CARD_PAYMENT_REFUND=20` | 影响 AIX 交易分类、筛选、展示和对账；前端映射见 ALL-GAP-037 |
| Card Transaction Notify | DTC 全量通知 AIX 卡交易 | 影响 Card 交易展示、自动归集触发、通知处理 |
| `D-REQUEST-ID` | DTC API 请求唯一标识 Header | 影响请求追踪；是否承担幂等 / 去重见 ALL-GAP-021 |

## 3. Master / Sub Account 设计边界

DTC Master / Sub Account 是外部账户模型，不是 AIX 内部账户模型。

| 对象 | 当前边界 | AIX 可记录 | 不得推导 |
|---|---|---|---|
| Master Account | DTC 账户体系中的主账户 | AIX 需要知道 Sub Account 注册在 Master Account 下 | 不写 DTC master 内部配置、内部权限、内部资金结构 |
| Sub Account | 注册在 Master Account 下的子账户 | AIX 可记录其作为用户外部账户上下文的一部分 | 不写成 AIX user 与 Sub Account 必然一一对应，除非后端确认 |
| `D-SUB-ACCOUNT-ID` | DTC 请求 Header，用于标识 Sub Account | AIX 可记录其对 WalletConnect、Wallet Account、Deposit、Balance、History 的上下文作用 | 不写成与 WalletAccount.clientId 完全等价，除非 DTC / 后端确认 |
| WalletAccount | DTC 钱包账户对象 | AIX 可记录字段存在及其影响 Wallet 页面、余额、状态和准入 | 不推导 WalletAccount 创建时机、失败补偿或状态枚举完整映射 |

与 Account Opening / KYC 的关系：

```text
AIX user
→ Account Opening / KYC
→ 外部 KYC 结果
→ DTC Sub Account / Wallet Account 上下文
→ Wallet Balance / Deposit / WalletConnect / History 等能力
```

以上是运行时依赖边界，不代表每一步创建顺序均已确认。以下内容仍需 ALL-GAP 管理：

1. AIX user 与 DTC Sub Account 是否一一对应。
2. KYC Approved 后是否立即创建 DTC Sub Account。
3. Sub Account 创建失败时 AIX 是否有补偿、告警或人工处理。
4. `D-SUB-ACCOUNT-ID` 与 WalletAccount.clientId 的准确关系。
5. WalletAccount.status 与 AIX 页面 / 能力准入的映射。

主事实源：`knowledge-base/kyc/account-opening.md`

## 4. Deposit / WalletConnect 设计边界

DTC Crypto Deposit 规则可作为 AIX Deposit / WalletConnect 的外部依赖来源，但不能直接等同完整产品流程。

| DTC 依赖 | AIX 可使用 | ALL-GAP 边界 |
|---|---|---|
| `D-SUB-ACCOUNT-ID` | WalletConnect / Deposit / Wallet 相关请求的外部账户上下文 | 是否作为产品入口前置、是否与 KYC Approved 绑定见 ALL-GAP-031 |
| DTC 分配 `destinationAddress` | Deposit 收款地址来源 | 页面展示、复制、二维码、链 / 币种展示见 ALL-GAP-060 |
| `senderAddress` whitelist | 白名单 / 风控边界 | GTR / WC 是否都适用、Declare / Travel Rule / 白名单边界见 ALL-GAP-044 |
| Risk Withheld | under review / 风控状态来源 | 前端状态、余额影响、人工处理见 ALL-GAP-008、ALL-GAP-039 |
| success | Deposit success 来源之一 | 是否等同 Wallet `COMPLETED`、余额何时可用见 ALL-GAP-005、ALL-GAP-016 |

## 5. Wallet History / Balance History 设计边界

| 能力 | AIX 可使用 | 不得推导 |
|---|---|---|
| Search Balance History endpoint | Wallet 余额历史 / 交易历史来源 | 不补完整接口说明书；完整字段表见 ALL-GAP-058 |
| `currency`、`type`、`yearMonth`、`createTimeStart` | 可作为查询条件边界 | 不默认前端全部展示 |
| `relatedId` | 可作为关联字段存在事实 | 不强行关联 Card / GTR / WC；取值见 ALL-GAP-014 |
| `activityType` | 可作为交易分类来源 | 不直接等同具体产品路径；前端映射见 ALL-GAP-037 |
| `state` | 可作为 Wallet 交易状态字段 | 不直接等同 Deposit success / Risk Withheld；状态映射见 ALL-GAP-008、ALL-GAP-016 |
| WalletAccount fields | 可作为 DTC 钱包账户字段存在事实 | 不补字段枚举之外的业务含义、状态迁移或可用性规则 |

## 6. ActivityType 边界

| 枚举 | 值 | 含义 | AIX 侧处理 |
|---|---:|---|---|
| `FIAT_DEPOSIT` | 6 | Fiat Deposit | 可作为法币入金分类来源；不得直接写成 GTR，见 ALL-GAP-001 |
| `CRYPTO_DEPOSIT` | 10 | Stablecoin Deposit | 可作为 Crypto / Stablecoin 入金分类来源；不得直接写成 WalletConnect，见 ALL-GAP-002 |
| `DTC_WALLET` | 13 | DTC Wallet Payment | 可作为 DTC Wallet Payment 分类来源；前端映射见 ALL-GAP-037 |
| `CARD_PAYMENT_REFUND` | 20 | Card Payment Refund | 可作为卡退款相关分类来源；与 Card 归集链路关联见 ALL-GAP-017、ALL-GAP-018 |

## 7. Webhook / Notification 设计边界

| 场景 | 已确认 | AIX 设计影响 |
|---|---|---|
| Deposit success 通知触发 | Webhook → notify，event=`CRYPTO_TXN`，type=`DEPOSIT`，state=`success` | 影响通知规则、跳转、用户感知；覆盖范围见 ALL-GAP-010 |
| Deposit Risk Withheld 通知触发 | Webhook → notify，event=`CRYPTO_TXN`，type=`DEPOSIT`，state=`RISK_WITHHELD` | 影响 under review 通知、用户提示；余额 / state 关系见 ALL-GAP-008 |
| Webhook 具体逻辑 | Notification 表备注“具体逻辑待定义” | 不补后端实现；原始报文落库见 ALL-GAP-022、ALL-GAP-036 |

## 8. 不写入事实的内容

以下内容不得在 DTC 外部依赖文件中写成事实：

1. `D-REQUEST-ID` 是幂等键。
2. Wallet `transactionId` 等同于 Card `data.id`。
3. Wallet `id` 等同于 Card `data.id`。
4. Wallet `relatedId` 等同于 Card `data.id` 或 AIX 归集请求 ID。
5. DTC Crypto Deposit 规则自动等同于所有 GTR / WalletConnect 产品流程。
6. `FIAT_DEPOSIT` 必然等同 GTR。
7. `CRYPTO_DEPOSIT` 必然等同 WalletConnect。
8. Deposit `success` 必然等同 Wallet `COMPLETED`。
9. `Risk Withheld` 必然等同 Wallet `REJECTED` / `PENDING` / `PROCESSING`。
10. 所有 Deposit 都一定需要 Declare / Travel Rule。
11. Transfer Balance to Wallet 返回 transferId / resultId。
12. `D-SUB-ACCOUNT-ID` 与 WalletAccount.clientId 完全等价。
13. KYC Approved 一定立即创建 DTC Sub Account。
14. DTC Sub Account 创建失败时 AIX 一定自动补偿。
15. WalletAccount.status 已完整映射到 AIX 能力准入。
16. DTC 内部系统实现逻辑。
17. DTC 未提供但由 AIX 推测的字段、状态或错误码。
18. 与 AIX 系统设计无关的供应商字段。

## 9. ALL-GAP 引用

本文不维护独立待补表。DTC 相关不确定项统一引用 ALL-GAP：

| 编号 | 主题 |
|---|---|
| ALL-GAP-001 | GTR 是否使用 `FIAT_DEPOSIT=6` |
| ALL-GAP-002 | WalletConnect 是否使用 `CRYPTO_DEPOSIT=10` |
| ALL-GAP-008 | Risk Withheld 与 Wallet `state` / 余额关系 |
| ALL-GAP-010 | GTR / WalletConnect 是否复用 Deposit success / under review 通知 |
| ALL-GAP-014 | Wallet `relatedId` 在 Card / GTR / WC 场景取值 |
| ALL-GAP-016 | Deposit success 与 Wallet `state=COMPLETED` 的映射 |
| ALL-GAP-017 | Card Transaction 与 Wallet Transaction 是否一一对应 |
| ALL-GAP-018 | Card / Wallet 关联字段 |
| ALL-GAP-021 | `D-REQUEST-ID` 是否承担幂等 / 去重 |
| ALL-GAP-022 | Webhook 原始报文是否完整落库 |
| ALL-GAP-031 | Account Opening / KYC 是否为 GTR / WalletConnect Deposit 前置 |
| ALL-GAP-036 | Webhook 原始报文落库规则 |
| ALL-GAP-037 | ActivityType 到 AIX 前端交易类型的映射 |
| ALL-GAP-043 | DTC 通用响应结构和通用错误码边界 |
| ALL-GAP-044 | WalletConnect Declare / Travel Rule / 白名单规则边界 |
| ALL-GAP-058 | Search Balance History 完整字段表 |
| 新增待确认 | AIX user 与 DTC Sub Account 是否一一对应、`D-SUB-ACCOUNT-ID` 与 WalletAccount.clientId 关系、Sub Account 创建失败处理、WalletAccount.status 与 AIX 准入映射 |

## 10. 来源引用

- (Ref: DTC接口文档/Master sub account 设计方案 (2).docx / Master Account / Sub Account / D-SUB-ACCOUNT-ID)
- (Ref: DTC Wallet OpenAPI Document20260126 / D-SUB-ACCOUNT-ID / WalletAccount)
- (Ref: DTC Wallet OpenAPI Document20260126 / 3.4 Crypto Deposit)
- (Ref: DTC Wallet OpenAPI Document20260126 / 4.2.4 Search Balance History)
- (Ref: DTC Wallet OpenAPI Document20260126 / Appendix ActivityType)
- (Ref: [2025-11-25] AIX+Notification / Deposit rows)
- (Ref: knowledge-base/kyc/account-opening.md / Account Opening / KYC / Sub Account / WalletAccount)
- (Ref: knowledge-base/transaction/history.md)
- (Ref: knowledge-base/transaction/detail.md)
- (Ref: knowledge-base/transaction/reconciliation.md)
- (Ref: knowledge-base/wallet/balance.md)
- (Ref: knowledge-base/wallet/deposit.md)
- (Ref: knowledge-base/changelog/knowledge-gaps.md / ALL-GAP 总表)
- (Ref: knowledge-base/_system-boundary.md)
- (Ref: 用户确认结论 / 2026-05-02 / 外部依赖只保留与 AIX 系统设计有关内容；KYC 文件名不应带 wallet)
