---
module: knowledge-base
feature: system-boundary
version: "1.0"
status: active
source_doc: IMPLEMENTATION_PLAN.md；knowledge-base/_ai-query-router.md；knowledge-base/changelog/knowledge-gaps.md；knowledge-base/changelog/final-repository-review.md；knowledge-base/common/dtc.md；knowledge-base/common/aai.md；knowledge-base/common/walletconnect.md；knowledge-base/common/notification.md；knowledge-base/common/errors.md；knowledge-base/transaction/reconciliation.md；knowledge-base/wallet/deposit.md；knowledge-base/card/card-transaction-flow.md；用户确认结论 2026-05-02
source_section: system responsibility boundary；external dependency boundary；AIX / DTC / AAI / WalletConnect / Third-party Wallet / Blockchain / Notification；ALL-GAP usage rules
last_updated: 2026-05-02
owner: 吴忆锋
---

# AIX 系统边界总说明

## 1. 文档定位

本文档用于定义 AIX 知识库中的系统边界、责任边界和外部依赖边界。

本文档不新增业务事实，不替代具体功能文件，不替代 DTC / AAI / WalletConnect 等外部依赖文件，也不替代 `knowledge-base/changelog/knowledge-gaps.md`。

AI 在写需求、查询需求逻辑、判断系统责任时，应使用本文判断：

1. 哪些属于 AIX 自身责任。
2. 哪些属于外部供应商或外部网络能力。
3. 哪些内容可以写入 AIX 需求。
4. 哪些内容只能引用，不能维护。
5. 哪些内容必须进入 ALL-GAP，不能写成事实。

## 2. 总体边界原则

| 原则 | 说明 |
|---|---|
| AIX 只维护自身系统责任 | AIX App、AIX Backend、AIX 管理流程、AIX 用户展示、AIX 通知、AIX 人工处理与告警属于 AIX 边界 |
| 外部系统只维护依赖边界 | DTC、AAI、WalletConnect、第三方钱包、Binance / GTR Wallet、区块链网络只记录 AIX 需要感知的结果、字段、事件和状态 |
| 不维护供应商内部逻辑 | 不写 DTC / AAI 内部系统实现、内部风控逻辑、完整接口说明书、完整错误码表 |
| 不把外部行为写成 AIX 可控行为 | 第三方钱包授权、链上确认、Binance 出款、AAI 识别算法、DTC 内部处理均非 AIX 直接可控 |
| 不确定项统一进 ALL-GAP | 责任边界、字段归属、状态映射、异常闭环无法确认时，必须引用 ALL-GAP |
| 不因需求表达而扩大 AIX 责任 | 需求文档只能写 AIX 能展示、调用、接收、记录、通知、告警、处理的部分 |

## 3. AIX 系统范围

AIX 系统范围包括：

| 范围 | 说明 |
|---|---|
| AIX App | 用户入口、页面展示、按钮交互、表单校验、结果页、交易详情页、错误页、通知跳转 |
| AIX Backend | 调用外部接口、接收 webhook、处理业务状态、写入内部记录、触发通知、触发告警、支撑查询 |
| AIX 知识库 | 沉淀产品事实、系统设计边界、状态规则、流程规则、错误边界、通知边界、待确认项 |
| AIX 运营 / 产品 / 客服处理 | 用户可见解释、人工处理口径、异常跟进、问题定位、ALL-GAP 确认 |
| AIX 资金可见性 | AIX 对用户展示的钱包余额、交易历史、交易详情、入金状态、归集状态 |

AIX 不直接控制：

1. DTC 内部系统处理。
2. AAI 内部 OCR / Liveness / KYC 判断算法。
3. WalletConnect SDK 内部连接实现。
4. 第三方钱包是否授权、是否支付、是否广播交易。
5. Binance / GTR Wallet 内部出款逻辑。
6. 区块链网络确认速度和链上状态。
7. 外部供应商接口字段未来变更。

## 4. AIX App 边界

AIX App 负责：

| 能力 | AIX App 责任 |
|---|---|
| 页面展示 | 展示 Wallet、Card、KYC、Deposit、Transaction 等页面 |
| 用户输入 | 收集 amount、currency、network、exchange、wallet 等用户输入 |
| 前端校验 | 执行 PRD 中已有来源的输入校验 |
| 用户操作 | 触发 Deposit、Connect Wallet、Complete Payment、View Details 等按钮动作 |
| 状态展示 | 展示后端或外部依赖返回并已被 AIX 解释的状态 |
| 错误展示 | 展示已确认错误页、弹窗、Toast、文案 |
| 通知跳转 | 根据 Notification 配置跳转对应页面 |

AIX App 不负责：

1. 判断 DTC 内部状态机。
2. 判断 AAI 内部风控 / 识别原因。
3. 控制第三方钱包授权结果。
4. 控制链上交易确认。
5. 自行生成没有来源的交易状态。
6. 自行补供应商未定义字段。

## 5. AIX Backend 边界

AIX Backend 负责：

| 能力 | AIX Backend 责任 |
|---|---|
| 外部接口调用 | 调用 DTC / AAI / WalletConnect 相关能力 |
| Webhook 接收 | 接收 DTC Card / Wallet / Deposit 相关 webhook |
| 业务处理 | 根据已确认规则处理状态、通知、告警、记录 |
| 交易查询支撑 | 支撑 Transaction History / Detail / Reconciliation 相关查询 |
| 通知触发 | 根据 Notification 规则触发 push / 站内信 / email |
| 告警触发 | 对已确认异常场景发送告警 |
| 记录与审计 | 在已确认规则下记录请求、响应、状态、处理结果 |

AIX Backend 不负责：

1. 维护 DTC 完整接口说明书。
2. 维护 AAI 完整能力说明书。
3. 承担 DTC 内部幂等逻辑，除非已确认。
4. 承担区块链网络确认能力。
5. 承担第三方钱包支付成功率。
6. 保证供应商成功响应后 Wallet 一定已入账，除非已确认。
7. 自动发现所有供应商成功但 AIX 不可见资金的异常，除非已确认。

## 6. DTC 外部依赖边界

DTC 是 AIX 的外部供应商系统，不是 AIX 内部系统。

AIX 可以记录：

| 可记录内容 | 示例 |
|---|---|
| AIX 调用的 DTC 能力 | Deposit Address、Search Balance History、Card Transaction Notify、Transfer Balance to Wallet |
| AIX 需要感知的 DTC 字段 | `data.id`、`originalId`、`activityType`、`state`、`relatedId`、`D-REQUEST-ID` |
| AIX 需要处理的 DTC 状态 | `Risk Withheld`、Deposit `success`、Wallet `state` 枚举 |
| AIX 依赖的 DTC 事件 | Card Transaction Notify、Crypto Txn webhook |
| 影响 AIX 用户体验的 DTC 结果 | 入金成功、under review、归集失败、查询失败 |

AIX 不维护：

1. DTC 内部系统设计。
2. DTC 完整接口字段表。
3. DTC 完整错误码表。
4. DTC 内部风控判断逻辑。
5. DTC 内部资金流转细节。
6. 与 AIX 页面、状态、通知、错误、对账无关的 DTC 字段。

DTC 相关事实主文件：

```text
knowledge-base/common/dtc.md
```

## 7. AAI 外部依赖边界

AAI 是 AIX 的外部 KYC / 识别 / 活体依赖，不是 AIX 内部系统。

AIX 可以记录：

| 可记录内容 | 示例 |
|---|---|
| AIX 调用或接入的 AAI 能力 | OCR、Liveness、KYC 结果 |
| AIX 需要展示的结果 | KYC pending / approved / rejected 等已确认状态 |
| AIX 需要处理的失败原因 | 已确认会影响页面、准入、重试、人工处理的失败结果 |
| AIX 配置边界 | 与 AIX 页面、准入、结果处理有关的配置 |

AIX 不维护：

1. AAI 内部识别算法。
2. AAI 内部风控策略。
3. AAI 完整错误码表。
4. AAI 完整接口说明书。
5. 与 AIX KYC 页面、准入、通知、错误处理无关的 AAI 字段。

AAI 相关事实主文件：

```text
knowledge-base/common/aai.md
knowledge-base/kyc/wallet-kyc.md
```

## 8. WalletConnect / 第三方钱包边界

WalletConnect 是 AIX 接入自托管钱包充值路径的连接能力，不是 AIX 自有钱包系统。

AIX 可以记录：

| 可记录内容 | 示例 |
|---|---|
| AIX 页面路径 | From a Self-custodial Wallet、Deposit confirmation、Result |
| AIX 与 WalletConnect 交互 | token、WebSocket、create_payment_intent、qr_ready、connected、send_payment、payment_info |
| AIX 需要处理的事件 | connected、payment_broadcasted、payment_info、connection_failed、add_whitelist_failed |
| 用户可见结果 | QR / Deeplink、Complete Payment、Deposit successful / progressing / failed |
| 白名单边界 | Approved 后 DTC 自动 add whitelist |

AIX 不控制：

1. 用户是否在第三方钱包 Approved。
2. 用户是否在第三方钱包支付。
3. 第三方钱包是否广播交易。
4. WalletConnect SDK 内部连接机制。
5. 链上交易实际确认速度。
6. 第三方钱包 App 是否安装、是否可用、是否兼容。

WalletConnect 相关事实主文件：

```text
knowledge-base/common/walletconnect.md
knowledge-base/wallet/deposit.md
```

## 9. Binance / GTR Wallet / Exchange 边界

GTR / Exchange 地址充值涉及外部交易所或托管钱包。

AIX 可以记录：

| 可记录内容 | 示例 |
|---|---|
| AIX 支持的入口 | From an Exchange / GTR |
| AIX 支持的 exchange 范围 | 当前支持 Binance，列表可配置 |
| AIX 展示的充值地址 | DTC 分配或返回的 destinationAddress |
| AIX 对用户的提示 | 交易报备、网络、币种、最小金额、风险提示 |
| AIX 接收的结果 | Deposit success / under review / 风控等可感知结果 |

AIX 不控制：

1. Binance 内部出款流程。
2. 交易所是否实际发起链上转账。
3. 用户是否从本人账户转出。
4. 用户是否选错网络、币种或地址。
5. 外部交易所到账 / 出账速度。

## 10. 区块链网络边界

区块链网络是外部基础设施，不属于 AIX / DTC / AAI 内部系统。

AIX 可以记录：

| 可记录内容 | 示例 |
|---|---|
| AIX 支持的 network | PRD 或配置中明确支持的链 |
| 链上交易 hash | `txnHash`、`deposit_transaction_hash` 等已确认字段 |
| 链上广播事件 | `payment_broadcasted` |
| 链上状态对 AIX 的影响 | 等待确认、查询不到交易、超时、success 等 AIX 可感知结果 |

AIX 不控制：

1. 链上确认速度。
2. 链上拥堵。
3. Gas 费用波动。
4. 区块链网络回滚或异常。
5. 用户在第三方钱包设置的 gas 策略。

## 11. Notification 边界

Notification 是 AIX 用户触达能力，负责通知模板、渠道、触发与跳转。

AIX 可以记录：

| 可记录内容 | 示例 |
|---|---|
| 通知触发源 | Webhook→notify、Card Transaction Notify |
| 通知条件 | event / type / state / status / indicator |
| 通知渠道 | push、站内信、email |
| 通知模板参数 | amount、currency、merchant_name、full_name 等 |
| 跳转目标 | 交易详情页、卡交易详情页等 |

AIX 不应写成事实：

1. 通知必然代表 Wallet 已到账。
2. GTR / WalletConnect 所有路径完全复用同一通知。
3. 站内信与 Push 一定完全一致。
4. 通知系统可自动发现所有资金异常。
5. 未在 Notification PRD 中出现的模板参数。

Notification 相关事实主文件：

```text
knowledge-base/common/notification.md
```

## 12. Transaction / Reconciliation 边界

Transaction 是 AIX 跨 Card / Wallet / Deposit 的交易统一层。Reconciliation 用于记录资金追踪和对账边界。

AIX 可以记录：

| 可记录内容 | 示例 |
|---|---|
| 交易历史 | Card History、Wallet Transaction History、Deposit History |
| 交易详情 | Card Detail、Wallet Detail、Deposit Detail |
| 状态来源 | Wallet `state`、Card DTC status、Deposit success / Risk Withheld |
| 资金追踪边界 | Card → Wallet 自动归集、Deposit → Wallet 余额可见性 |
| 对账缺口 | ID 串联、relatedId、transactionId、D-REQUEST-ID、内部处理 ID |

AIX 不得默认：

1. Card Transaction 与 Wallet Transaction 一一对应。
2. Card `data.id` 等同 Wallet `transactionId`。
3. Wallet `relatedId` 等同 Card `data.id`。
4. Deposit success 等同 Wallet `COMPLETED`。
5. Risk Withheld 等同 Wallet `REJECTED`。
6. 通知等同资金到账。

Transaction / Reconciliation 相关事实主文件：

```text
knowledge-base/transaction/history.md
knowledge-base/transaction/detail.md
knowledge-base/transaction/status-model.md
knowledge-base/transaction/reconciliation.md
```

## 13. 可以写入知识库的内容

以下内容可以写入知识库：

1. AIX 页面、按钮、入口、结果页、错误页。
2. AIX 调用外部能力的时机和用途。
3. AIX 接收外部事件后的处理。
4. AIX 对用户展示的状态和文案。
5. AIX 对客服 / 运营 / 产品 / 后端的处理边界。
6. AIX 需要触发的通知、告警、人工处理。
7. AIX 交易历史、交易详情、资金追踪、对账边界。
8. 外部依赖中影响 AIX 系统设计的字段、事件、状态、结果。
9. 不确定项对应的 ALL-GAP 编号和说明。

## 14. 禁止写入知识库的内容

以下内容不得作为 AIX 事实写入知识库：

1. DTC 内部系统逻辑。
2. AAI 内部识别算法。
3. WalletConnect SDK 内部实现。
4. 第三方钱包内部行为。
5. Binance / 交易所内部出款逻辑。
6. 区块链网络内部确认机制。
7. 供应商完整接口说明书。
8. 供应商完整错误码表。
9. 与 AIX 页面、状态、通知、错误、对账、人工处理无关的字段。
10. 没有来源的状态映射。
11. 没有来源的字段关联。
12. 没有来源的错误码和文案。
13. 没有来源的通知触发条件。
14. 没有确认的资金到账时点。
15. 没有确认的系统自动补偿机制。

## 15. AI 写需求时的边界判断规则

AI 写需求时，应先判断一个能力属于哪一类：

| 类型 | 写法 |
|---|---|
| AIX 负责 | 写成明确需求规则 |
| AIX 调用外部系统 | 写成“调用 / 接收 / 展示 / 处理” |
| 外部系统内部逻辑 | 只写外部返回结果，不写内部过程 |
| 外部网络或用户行为 | 写成用户动作或外部结果，不写成 AIX 控制 |
| 未确认边界 | 引用 ALL-GAP，不补结论 |
| 未上线 / 需重做能力 | 标记 deferred，不写成 active |

示例：

| 错误写法 | 正确写法 |
|---|---|
| AIX 判断 DTC 风控并冻结入金 | DTC 返回 Risk Withheld 后，AIX 展示 under review |
| AIX 完成第三方钱包支付 | 用户在第三方钱包确认支付后，AIX 接收 WalletConnect / DTC 返回事件 |
| AIX 识别证件真假 | AIX 接收 AAI KYC / OCR / Liveness 结果并按结果处理 |
| Deposit success 后 Wallet 一定 COMPLETED | Deposit success 与 Wallet `COMPLETED` 映射未确认，见 ALL-GAP-016 |
| 通知成功代表资金到账 | 通知是否以 Wallet 入账为触发点未确认，见 ALL-GAP-065 |

## 16. 与其他文件的关系

| 文件 | 关系 |
|---|---|
| `IMPLEMENTATION_PLAN.md` | 主控计划，定义执行规则和阶段状态 |
| `knowledge-base/_ai-query-router.md` | 查询路由，决定问题应读取哪些事实文件 |
| `knowledge-base/_system-boundary.md` | 系统边界，决定哪些内容属于 AIX 责任 |
| `knowledge-base/changelog/knowledge-gaps.md` | 唯一待确认表 |
| `knowledge-base/common/dtc.md` | DTC 外部依赖边界细化 |
| `knowledge-base/common/aai.md` | AAI 外部依赖边界细化 |
| `knowledge-base/common/walletconnect.md` | WalletConnect 集成边界细化 |
| `knowledge-base/common/notification.md` | 通知边界细化 |
| `knowledge-base/transaction/reconciliation.md` | 资金追踪与对账边界细化 |

## 17. 使用规则

1. 查询系统责任边界时，优先读本文。
2. 查询具体业务规则时，读 `_ai-query-router.md` 指向的功能事实文件。
3. 查询未确认项时，读 `knowledge-gaps.md`。
4. 查询外部依赖细节时，读对应 `common/*.md`。
5. 若本文与功能事实文件冲突，以功能事实文件中的已确认业务事实为准，但必须同步更新本文。
6. 若本文与 ALL-GAP 冲突，以 ALL-GAP 的未确认状态为准，不得写成事实。

## 18. 来源引用

- (Ref: IMPLEMENTATION_PLAN.md / v5.0)
- (Ref: knowledge-base/_ai-query-router.md / v1.0)
- (Ref: knowledge-base/changelog/knowledge-gaps.md / ALL-GAP 总表)
- (Ref: knowledge-base/changelog/final-repository-review.md / v1.5)
- (Ref: knowledge-base/common/dtc.md / v1.5)
- (Ref: knowledge-base/common/aai.md / v1.2)
- (Ref: knowledge-base/common/walletconnect.md / v1.4)
- (Ref: knowledge-base/common/notification.md / v1.3)
- (Ref: knowledge-base/common/errors.md / v1.4)
- (Ref: knowledge-base/transaction/reconciliation.md / v1.1)
- (Ref: knowledge-base/wallet/deposit.md / v1.6)
- (Ref: knowledge-base/card/card-transaction-flow.md / v1.3)
- (Ref: 用户确认结论 / 2026-05-02 / 外部依赖只保留与 AIX 系统设计有关内容；ALL-GAP 留待以后确认)
