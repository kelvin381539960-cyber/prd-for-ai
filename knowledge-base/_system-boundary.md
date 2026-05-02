---
module: knowledge-base
feature: system-boundary
version: "2.1"
status: active
source_doc: knowledge-base/_ai-query-router.md；knowledge-base/changelog/knowledge-gaps.md；knowledge-base/kyc/account-opening.md；knowledge-base/common/dtc.md；knowledge-base/common/aai.md；knowledge-base/common/walletconnect.md；knowledge-base/common/notification.md；knowledge-base/common/errors.md；knowledge-base/transaction/reconciliation.md；knowledge-base/wallet/deposit.md；knowledge-base/card/card-transaction-flow.md；用户确认结论 2026-05-02
source_section: runtime system responsibility boundary；Account Opening / KYC；AIX / KUN / AAI / DTC Master Sub Account / WalletAccount；external dependency boundary；ALL-GAP usage rules
last_updated: 2026-05-02
owner: 吴忆锋
---

# AIX 系统边界总说明

## 1. 文档定位

本文档用于定义 AIX 知识库中的系统责任边界和外部依赖边界。

本文档是边界争议裁判文件，不是 AI 每次查询的默认入口。AI 日常查询先读 `knowledge-base/_ai-query-router.md`；当问题涉及系统责任、外部依赖、是否能写入 AIX 需求时，再读取本文。

本文档不新增业务事实，不替代具体功能文件，不替代 `knowledge-base/changelog/knowledge-gaps.md`。

## 2. 总体边界原则

| 原则 | 说明 |
|---|---|
| AIX 只维护自身系统责任 | AIX App、AIX Backend、AIX 管理流程、AIX 用户展示、AIX 通知、AIX 人工处理与告警属于 AIX 边界 |
| 外部系统只维护依赖边界 | DTC、AAI、KUN、WalletConnect、第三方钱包、Binance / GTR Wallet、区块链网络只记录 AIX 需要感知的结果、字段、事件和状态 |
| 不维护供应商内部逻辑 | 不写 DTC / AAI / KUN 内部系统实现、内部风控逻辑、完整接口说明书、完整错误码表 |
| 不把外部行为写成 AIX 可控行为 | 第三方钱包授权、链上确认、Binance 出款、AAI 识别算法、DTC 内部处理均非 AIX 直接可控 |
| 不确定项统一进 ALL-GAP | 责任边界、字段归属、状态映射、异常闭环无法确认时，必须引用 ALL-GAP |
| 不因需求表达扩大 AIX 责任 | 需求文档只能写 AIX 能展示、调用、接收、记录、通知、告警、处理的部分 |

## 3. AIX 负责范围

| 范围 | 说明 |
|---|---|
| AIX App | 页面展示、按钮交互、表单校验、权限引导、结果页、交易详情页、错误页、通知跳转 |
| AIX Backend | 调用外部接口、接收 webhook、处理业务状态、写入内部记录、触发通知、触发告警、支撑查询 |
| AIX Account Opening / KYC 承接 | 发起开户 / KYC 流程、展示状态、承接外部结果、控制 AIX 侧准入、处理失败 / 重试 / 通知边界 |
| AIX 知识库 | 沉淀产品事实、系统设计边界、状态规则、流程规则、错误边界、通知边界、待确认项 |
| AIX 运营 / 产品 / 客服处理 | 用户可见解释、人工处理口径、异常跟进、问题定位、ALL-GAP 确认 |
| AIX 资金可见性 | AIX 对用户展示的钱包余额、交易历史、交易详情、入金状态、归集状态 |

## 4. AIX 不直接控制范围

AIX 不直接控制：

1. DTC 内部系统处理。
2. DTC Master / Sub Account / WalletAccount 内部模型实现。
3. AAI 内部 OCR / Liveness / Face Comparison / KYC 判断算法。
4. KUN 内部 KYC 会话、供应商编排或审核承接逻辑。
5. WalletConnect SDK 内部连接实现。
6. 第三方钱包是否授权、是否支付、是否广播交易。
7. Binance / GTR Wallet 内部出款逻辑。
8. 区块链网络确认速度和链上状态。
9. 外部供应商接口字段未来变更。

## 5. 外部依赖边界

### 5.1 DTC

DTC 是 AIX 的外部供应商系统，不是 AIX 内部系统。

AIX 可以记录：

- AIX 调用的 DTC 能力。
- AIX 需要感知的 DTC 字段、状态、事件和响应结果。
- 影响 AIX 页面、状态、通知、错误、人工处理、资金追踪、开户上下文和对账的 DTC 结果。
- DTC Master / Sub Account、`D-SUB-ACCOUNT-ID`、WalletAccount 对 AIX Wallet / Deposit / WalletConnect / Balance / History 的依赖边界。

AIX 不维护：

- DTC 内部系统设计。
- DTC 完整接口字段表。
- DTC 完整错误码表。
- DTC 内部风控判断逻辑。
- DTC Master / Sub Account 内部实现。
- 与 AIX 页面、状态、通知、错误、对账、开户准入无关的 DTC 字段。

主事实源：`knowledge-base/common/dtc.md`

### 5.2 AAI

AAI 是 AIX 的外部 KYC / 识别 / 活体依赖，不是 AIX 内部系统。

AIX 可以记录：

- AIX 调用或接入的 AAI 能力。
- AIX 需要展示或处理的 Passport OCR、Liveness、Face Comparison、POA、KYC 结果。
- 与 AIX 准入、失败提示、重试、人工处理有关的 AAI 结果边界。
- AIX 页面如何根据外部结果跳转，例如 Identity Scan、Face Scan、Face Loading、Face Failed、Loading Failed。

AIX 不维护：

- AAI 内部识别算法。
- AAI 内部风控策略。
- AAI 完整错误码表。
- AAI 完整接口说明书。
- AAI 内部状态机。

主事实源：

- `knowledge-base/common/aai.md`
- `knowledge-base/kyc/account-opening.md`

### 5.3 KUN

KUN 是 Account Opening / KYC 流程中的外部或中间承接系统。当前知识库只记录其对 AIX KYC 流程的边界影响，不维护 KUN 内部实现。

AIX 可以记录：

- AIX / KUN / AAI 在开户 KYC 流程中的交互方向。
- KUN 作为 KYC 会话、供应商链路或结果承接方时，对 AIX 页面、状态、轮询、结果展示的影响。
- KUN 返回或承接结果对 AIX 后续处理的边界。

AIX 不维护：

- KUN 内部会话模型。
- KUN 内部供应商编排。
- KUN 内部审核规则。
- KUN 完整接口字段和错误码。

主事实源：`knowledge-base/kyc/account-opening.md`

### 5.4 WalletConnect / 第三方钱包

WalletConnect 是 AIX 接入自托管钱包充值路径的连接能力，不是 AIX 自有钱包系统。

AIX 可以记录：

- AIX 页面路径。
- AIX 与 WalletConnect 的交互事件。
- AIX 需要处理的连接、授权、支付、失败事件。
- 用户可见结果和错误处理边界。
- WalletConnect 对 `D-SUB-ACCOUNT-ID` 等外部账户上下文的依赖。

AIX 不控制：

- 用户是否在第三方钱包 Approved。
- 用户是否在第三方钱包支付。
- 第三方钱包是否广播交易。
- WalletConnect SDK 内部连接机制。
- 链上交易实际确认速度。
- 第三方钱包 App 是否安装、可用、兼容。

主事实源：

- `knowledge-base/common/walletconnect.md`
- `knowledge-base/wallet/deposit.md`
- `knowledge-base/kyc/account-opening.md`

### 5.5 Binance / GTR Wallet / Exchange

GTR / Exchange 地址充值涉及外部交易所或托管钱包。

AIX 可以记录：

- AIX 支持的入口。
- AIX 支持的 exchange 范围。
- AIX 展示的充值地址。
- AIX 对用户的提示。
- AIX 接收并展示的 Deposit 结果。
- GTR / Exchange Deposit 是否依赖 Account Opening / KYC 或 Sub Account 的待确认边界。

AIX 不控制：

- Binance 内部出款流程。
- 交易所是否实际发起链上转账。
- 用户是否从本人账户转出。
- 用户是否选错网络、币种或地址。
- 外部交易所到账 / 出账速度。

### 5.6 区块链网络

区块链网络是外部基础设施，不属于 AIX / DTC / AAI / KUN 内部系统。

AIX 可以记录：

- AIX 支持的 network。
- 链上交易 hash。
- 链上广播事件。
- 链上状态对 AIX 可见结果的影响。

AIX 不控制：

- 链上确认速度。
- 链上拥堵。
- Gas 费用波动。
- 区块链网络回滚或异常。
- 用户在第三方钱包设置的 gas 策略。

## 6. Account Opening / KYC 边界

Account Opening / KYC 是 AIX 侧承接用户开户、身份验证、外部账户上下文和业务准入的能力域。

主事实源：`knowledge-base/kyc/account-opening.md`

### 6.1 AIX 可以写成需求的内容

AIX 可以写：

1. 用户进入 KYC Loading、KYC Start、Select Residence Country、Waitlist、Identity Verify、Identity Scan、Face Guide、Face Scan、Face Loading、Address Upload、KYC Submission Success 等页面。
2. AIX 页面如何根据 `Pending`、`failed`、`Under review`、`Rejected`、`Approved` 等状态分流。
3. AIX 如何展示网络异常、系统异常、超时、扫描失败、Face Failed、Loading Failed。
4. AIX 如何承接 AAI / KUN 返回的 OCR、Face、POA、KYC 结果。
5. AIX 如何根据 KYC 结果触发通知、控制页面入口、限制重试或进入等待状态。
6. AIX 如何记录与 DTC Sub Account / WalletAccount 相关的外部账户上下文。
7. AIX 如何引用 ALL-GAP 标记未确认的准入、字段映射、失败补偿和人工处理边界。

### 6.2 AIX 不得写成事实的内容

AIX 不得默认写：

1. AAI 内部如何判断证件真假。
2. AAI 内部如何完成 Face Comparison。
3. KUN 内部如何创建 KYC session 或编排供应商。
4. DTC 内部如何创建 Master / Sub Account。
5. KYC Approved 一定立即创建 DTC Sub Account。
6. AIX user 与 DTC Sub Account 一定一一对应。
7. `D-SUB-ACCOUNT-ID` 与 WalletAccount.clientId 一定完全等价。
8. WalletAccount.status 已完整映射到 AIX 的所有能力准入。
9. KYC Approved 一定代表 Wallet / Deposit / WalletConnect / Receive 全部可用。
10. Card KYC 与 Account Opening / KYC 完全相同。

### 6.3 责任分工

| 范围 | AIX 负责 | 外部系统负责 |
|---|---|---|
| 页面与交互 | 展示 KYC 页面、权限弹窗、状态、失败、重试、锁定、waitlist、结果页 | 无 |
| 身份识别结果 | 接收、展示、处理外部结果 | AAI / KUN 执行 OCR、Liveness、Face Comparison、POA 等外部能力 |
| 状态分流 | 根据可见状态控制 AIX 页面和入口 | 外部系统提供或承接状态来源 |
| 外部账户上下文 | 保存和使用 AIX 可见的 Sub Account / WalletAccount 上下文 | DTC 维护 Master / Sub Account / WalletAccount 外部账户模型 |
| 能力准入 | 根据已确认规则控制 AIX 入口、按钮、提示和用户路径 | DTC / AAI / KUN 提供外部结果或账户状态 |
| 通知 | 触发和展示 AIX 通知 | Notification 服务或外部渠道投递结果 |
| 异常处理 | 展示错误页、限制重试、引导用户、告警或人工跟进 | 外部系统返回失败、超时、拒绝、审核中等结果 |

## 7. Notification 边界

Notification 是 AIX 用户触达能力，负责通知模板、渠道、触发与跳转。

AIX 可以记录：

- 通知触发源。
- 通知条件。
- 通知渠道。
- 通知模板参数。
- 通知跳转目标。
- KYC Approved / Rejected / Failed、Deposit success / Risk Withheld 等结果对通知的影响。

AIX 不应写成事实：

1. 通知必然代表 Wallet 已到账。
2. GTR / WalletConnect 所有路径完全复用同一通知。
3. 站内信与 Push 一定完全一致。
4. 通知系统可自动发现所有资金异常。
5. 未在 Notification PRD 中出现的模板参数。
6. KYC Approved 通知必然代表 DTC Sub Account 已创建成功。

主事实源：`knowledge-base/common/notification.md`

## 8. Transaction / Reconciliation 边界

Transaction 是 AIX 跨 Card / Wallet / Deposit 的交易统一层。Reconciliation 用于记录资金追踪和对账边界。

AIX 可以记录：

- 交易历史。
- 交易详情。
- 状态来源。
- 资金追踪边界。
- 对账缺口。

AIX 不得默认：

1. Card Transaction 与 Wallet Transaction 一一对应。
2. Card `data.id` 等同 Wallet `transactionId`。
3. Wallet `relatedId` 等同 Card `data.id`。
4. Deposit success 等同 Wallet `COMPLETED`。
5. Risk Withheld 等同 Wallet `REJECTED`。
6. 通知等同资金到账。

主事实源：

- `knowledge-base/transaction/history.md`
- `knowledge-base/transaction/detail.md`
- `knowledge-base/transaction/status-model.md`
- `knowledge-base/transaction/reconciliation.md`

## 9. 可以写入知识库的内容

以下内容可以写入知识库：

1. AIX 页面、按钮、入口、结果页、错误页。
2. AIX 调用外部能力的时机和用途。
3. AIX 接收外部事件后的处理。
4. AIX 对用户展示的状态和文案。
5. AIX 对客服 / 运营 / 产品 / 后端的处理边界。
6. AIX 需要触发的通知、告警、人工处理。
7. AIX 交易历史、交易详情、资金追踪、对账边界。
8. Account Opening / KYC 中 AIX 可见的页面、状态、结果、通知、失败、重试、准入边界。
9. 外部依赖中影响 AIX 系统设计的字段、事件、状态、结果。
10. 不确定项对应的 ALL-GAP 编号和说明。

## 10. 禁止写入知识库的内容

以下内容不得作为 AIX 事实写入知识库：

1. DTC 内部系统逻辑。
2. DTC Master / Sub Account 内部实现。
3. AAI 内部识别算法。
4. KUN 内部供应商编排或审核逻辑。
5. WalletConnect SDK 内部实现。
6. 第三方钱包内部行为。
7. Binance / 交易所内部出款逻辑。
8. 区块链网络内部确认机制。
9. 供应商完整接口说明书。
10. 供应商完整错误码表。
11. 与 AIX 页面、状态、通知、错误、对账、人工处理无关的字段。
12. 没有来源的状态映射。
13. 没有来源的字段关联。
14. 没有来源的错误码和文案。
15. 没有来源的通知触发条件。
16. 没有确认的资金到账时点。
17. 没有确认的系统自动补偿机制。
18. 没有确认的 Account Opening / KYC 与 Deposit / WalletConnect / Card KYC 关系。

## 11. AI 写需求时的边界判断规则

| 类型 | 写法 |
|---|---|
| AIX 负责 | 写成明确需求规则 |
| AIX 调用外部系统 | 写成“调用 / 接收 / 展示 / 处理” |
| 外部系统内部逻辑 | 只写外部返回结果，不写内部过程 |
| 外部网络或用户行为 | 写成用户动作或外部结果，不写成 AIX 控制 |
| 外部账户模型 | 只写 AIX 需要使用的账户上下文和字段边界，不写供应商内部账户实现 |
| 未确认边界 | 引用 ALL-GAP，不补结论 |
| 未上线 / 需重做能力 | 标记 deferred，不写成 active |

示例：

| 错误写法 | 正确写法 |
|---|---|
| AIX 判断 DTC 风控并冻结入金 | DTC 返回 Risk Withheld 后，AIX 展示 under review |
| AIX 完成第三方钱包支付 | 用户在第三方钱包确认支付后，AIX 接收 WalletConnect / DTC 返回事件 |
| AIX 识别证件真假 | AIX 接收 AAI KYC / OCR / Liveness 结果并按结果处理 |
| AIX 创建 DTC Sub Account 的内部账户结构 | AIX 使用 DTC 返回或配置的 Sub Account 上下文；创建时机和失败补偿见 ALL-GAP |
| KYC Approved 后 WalletConnect 一定可用 | KYC Approved 与 WalletConnect 准入关系需区分产品入口前置和 `D-SUB-ACCOUNT-ID` 技术依赖，见 ALL-GAP-031 |
| Deposit success 后 Wallet 一定 COMPLETED | Deposit success 与 Wallet `COMPLETED` 映射未确认，见 ALL-GAP-016 |
| 通知成功代表资金到账 | 通知是否以 Wallet 入账为触发点未确认，见 ALL-GAP-065 |

## 12. 与其他文件的关系

| 文件 | 关系 |
|---|---|
| `knowledge-base/_ai-query-router.md` | AI 日常查询入口，决定问题应读取哪些事实文件 |
| `knowledge-base/_system-boundary.md` | 系统边界，决定哪些内容属于 AIX 责任 |
| `knowledge-base/changelog/knowledge-gaps.md` | 唯一待确认表 |
| `knowledge-base/kyc/account-opening.md` | Account Opening / KYC 主事实源 |
| `knowledge-base/common/dtc.md` | DTC 外部依赖边界细化 |
| `knowledge-base/common/aai.md` | AAI 外部依赖边界细化 |
| `knowledge-base/common/walletconnect.md` | WalletConnect 集成边界细化 |
| `knowledge-base/common/notification.md` | 通知边界细化 |
| `knowledge-base/transaction/reconciliation.md` | 资金追踪与对账边界细化 |

## 13. 使用规则

1. 查询系统责任边界时，优先读本文。
2. 查询具体业务规则时，读 `_ai-query-router.md` 指向的功能事实文件。
3. 查询 Account Opening / KYC、Sub Account、KYC 结果与能力准入时，读 `kyc/account-opening.md`。
4. 查询未确认项时，读 `knowledge-gaps.md`。
5. 查询外部依赖细节时，读对应 `common/*.md`。
6. 若本文与功能事实文件冲突，以功能事实文件中的已确认业务事实为准，但必须同步更新本文。
7. 若本文与 ALL-GAP 冲突，以 ALL-GAP 的未确认状态为准，不得写成事实。

## 14. 来源引用

- (Ref: knowledge-base/_ai-query-router.md / runtime query router)
- (Ref: knowledge-base/changelog/knowledge-gaps.md / ALL-GAP 总表)
- (Ref: knowledge-base/kyc/account-opening.md)
- (Ref: knowledge-base/common/dtc.md)
- (Ref: knowledge-base/common/aai.md)
- (Ref: knowledge-base/common/walletconnect.md)
- (Ref: knowledge-base/common/notification.md)
- (Ref: knowledge-base/common/errors.md)
- (Ref: knowledge-base/transaction/reconciliation.md)
- (Ref: knowledge-base/wallet/deposit.md)
- (Ref: knowledge-base/card/card-transaction-flow.md)
- (Ref: 用户确认结论 / 2026-05-02 / 知识库切换为使用态；外部依赖只保留与 AIX 系统设计有关内容；KYC 文件名不应带 wallet)
