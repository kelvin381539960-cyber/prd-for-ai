---
module: changelog
feature: knowledge-gaps
version: "1.9"
status: active
source_doc: IMPLEMENTATION_PLAN.md；knowledge-base/wallet/deposit.md；knowledge-base/card/card-transaction-flow.md；knowledge-base/card/stage-review.md；knowledge-base/card/transaction-flow-traceability-checklist.md；knowledge-base/wallet/transaction-history.md；knowledge-base/wallet/kyc.md；knowledge-base/common/dtc.md；knowledge-base/common/aai.md；knowledge-base/common/errors.md；knowledge-base/common/stage-review.md；knowledge-base/transaction/detail.md；knowledge-base/transaction/status-model.md；用户确认结论 2026-05-01；用户确认结论 2026-05-02
source_section: source-policy；all-module centralized confirmation table；Card Transaction Flow；Wallet Deposit；Wallet KYC；Common DTC / AAI；Common Stage Review；Transaction Detail；Transaction Status Model；deferred gaps decision；single global checklist rule
last_updated: 2026-05-02
owner: 吴忆锋
---

# Knowledge Gaps 知识缺口与冲突记录

## 1. 文档定位

本文档是全仓库唯一的待确认事项总表。

所有模块的不确定项、缺口、冲突、待确认问题，统一写入本文档的 `全模块待确认总表`。功能正文只保留稳定事实，或引用 `ALL-GAP-XXX` 编号，不再分散维护独立 checklist / TODO / gaps 表。

当前用户已确认：所有模块的不确定项应集中在一张总表里，后续统一批量确认；短期无法确认的问题标记为 `deferred`，不阻塞后续知识库推进。

## 2. 全模块待确认总表

> 使用规则：所有新发现的不确定项，优先追加到本表；功能正文只保留稳定事实。用户后续可一次性按编号回复确认结果。

| 编号 | 优先级 | 模块 | 待确认问题 | 当前已知 / 背景 | 需要确认对象 | 影响 | 当前状态 |
|---|---|---|---|---|---|---|---|
| ALL-GAP-001 | P1 | Wallet / Deposit | GTR 是否使用 `FIAT_DEPOSIT=6` | DTC ActivityType 中存在 `FIAT_DEPOSIT=6`，但用户确认先 deferred，未确认是否对应 GTR / Exchange 地址充值 | Wallet / 后端 / 产品 | 影响交易历史分类、筛选、统计 | deferred |
| ALL-GAP-002 | P1 | Wallet / Deposit | WalletConnect 是否使用 `CRYPTO_DEPOSIT=10` | DTC ActivityType 中存在 `CRYPTO_DEPOSIT=10`，但用户确认先 deferred，未确认是否对应 WalletConnect / Self-custodial Wallet 充值 | Wallet / 后端 / 产品 | 影响交易历史分类、筛选、统计 | deferred |
| ALL-GAP-003 | P0 | Wallet / Deposit | Risk Withheld 是否进入 AIX 结果页 | 用户确认 Risk Withheld 是异步返回，不触发充值结果页；用户查询交易详情时状态为 under review | 产品 / 前端 / 后端 | 影响结果页和详情页状态展示 | resolved-by-user |
| ALL-GAP-004 | P1 | Wallet / Deposit | Refunded 状态是否有 AIX 对客结果页 | 用户确认没有 AIX 对客结果页 | 产品 / 前端 | 影响 Refunded 展示边界 | resolved-by-user |
| ALL-GAP-005 | P0 | Wallet / Deposit | `payment_info success` 后 Wallet balance 何时可用 | 用户确认 payment_info success 是信息流成功，会同步触发资金流转账，理论立即可用，实际会有很短延迟 | Wallet / 后端 / 产品 | 影响成功页、余额展示和 FAQ 口径 | resolved-by-user |
| ALL-GAP-006 | P1 | Wallet / Deposit | WalletConnect 授权有效期按 1 天还是 7 天 | 用户确认：AIX 侧按 1 天；DTC 7 天是 DTC 内部逻辑，不作为 AIX 对客有效期 | 产品 / 后端 | 影响授权有效期展示和重连规则 | resolved-by-user |
| ALL-GAP-007 | P0 | Wallet / Deposit | `relatedId / transactionId / id` 如何串联 GTR / WalletConnect 入金 | 用户确认继续 deferred | Wallet / 后端 / 账务 | 影响交易详情、交易历史和对账 | deferred |
| ALL-GAP-008 | P0 | Wallet / Deposit | Risk Withheld 与 Wallet `state` 是否存在映射，是否影响冻结余额 / 可用余额 | 已确认不触发结果页，详情页展示 under review；与 Wallet state / 余额字段关系仍未确认 | Wallet / 后端 / 产品 | 影响余额展示、交易详情、状态筛选 | deferred |
| ALL-GAP-009 | P1 | Wallet / Deposit | GTR 地址充值是否有与 WalletConnect 相同的结果页 | PRD 未像 WC 一样定义明确结果页 | 产品 / 前端 | 影响 GTR 充值完成后的页面体验 | deferred |
| ALL-GAP-010 | P1 | Wallet / Deposit | GTR / WalletConnect 是否都复用 Deposit success / under review 通知 | Notification 有 Deposit 通用通知，但未确认是否覆盖所有子路径和恢复场景 | 产品 / 后端 / Notification | 影响通知触发与跳转 | deferred |
| ALL-GAP-011 | P1 | Wallet / Deposit | GTR 异常处理和客服口径 | 已知非 Binance、非本人账户、错误网络、错误地址、低于最小金额有风险；后台 / 客服处理未确认 | 产品 / 运营 / 客服 | 影响异常闭环 | deferred |
| ALL-GAP-012 | P1 | Wallet / Deposit | WalletConnect `payment_info false / Transaction not found` 的后续处理 | DTC 文档有 Transaction not found，当前只写待异常处理 | 后端 / 产品 / 运维 | 影响状态不明场景 | deferred |
| ALL-GAP-013 | P2 | Wallet / Deposit | WalletConnect 失败是否需要告警 | PRD 主要定义页面处理，未确认是否进入监控或告警 | 后端 / 运维 | 影响排障和监控 | deferred |
| ALL-GAP-014 | P0 | Wallet / Transaction | Wallet `relatedId` 在 Card balance 转 Wallet、GTR、WalletConnect 场景下分别取什么值 | Search Balance History 有 `relatedId` 字段，但取值规则未确认 | Wallet / DTC / 后端 | 影响 Wallet History 关联和对账 | deferred |
| ALL-GAP-015 | P1 | Wallet / Transaction | Wallet `transactionId` 与 Wallet `id` 的关系 | 已确认详情入参为 `transactionId`，出参有 Long `id`，但二者关系未确认 | Wallet / 后端 | 影响交易详情查询和引用口径 | deferred |
| ALL-GAP-016 | P1 | Wallet / Transaction | Deposit success 与 Wallet `state=COMPLETED` 是否存在确定映射 | 当前不能写死；用户已确认 payment_info success 理论触发资金流转账但可能短延迟 | Wallet / 后端 | 影响状态模型 | deferred |
| ALL-GAP-017 | P0 | Card / Wallet Traceability | Card Transaction / refund / reversal / deposit 与 Wallet Transaction 是否存在一一对应关系 | 资金追踪链路未闭环 | 后端 / Wallet / 账务 | 决定是否能从卡交易追踪到钱包入账 | deferred |
| ALL-GAP-018 | P0 | Card / Wallet Traceability | 如果存在关联，具体用哪个字段关联 | 候选：Card `data.id`、Wallet `transactionId`、Wallet `id`、`relatedId`、`D-REQUEST-ID`、AIX 内部 ID 或其他字段 | 后端 / Wallet / 账务 | 决定对账字段组合 | deferred |
| ALL-GAP-019 | P0 | Card / Transaction Flow | AIX 收到 DTC Card Transaction Notify 后是否生成内部交易处理 ID，字段名是什么 | 未确认内部处理 ID | 后端 | 影响内部处理链路追踪 | deferred |
| ALL-GAP-020 | P0 | Card / Transaction Flow | AIX 发起 Transfer Balance to Wallet 前是否生成归集请求 ID，字段名是什么 | 未确认归集请求 ID | 后端 / 账务 | 影响归集请求追踪 | deferred |
| ALL-GAP-021 | P0 | Card / Transaction Flow | `D-REQUEST-ID` 是否仅是请求唯一标识，还是也承担幂等 / 重试去重作用 | 当前只写 DTC 请求唯一标识，不写成幂等键 | 后端 / DTC | 影响请求幂等和重试设计 | deferred |
| ALL-GAP-022 | P0 | Card / Transaction Flow | DTC Webhook 原始报文是否完整落库，是否可回放 / 查询 | 未确认 webhook 原始报文落库规则 | 后端 / 运维 | 影响审计、排障、补偿 | deferred |
| ALL-GAP-023 | P1 | Card / Transaction Flow | 重复通知实际如何去重，是否按 `event + data.id` | 用户确认重复推送 Transaction ID 不变，DTC 无独立 notification id | 后端 | 影响重复推送处理 | deferred |
| ALL-GAP-024 | P0 | Card / Transaction Flow | 自动归集触发是否只依赖 `type=refund/reversal/deposit`，还是还需要判断 state / indicator / amount | 用户确认只关注 refund / reversal / deposit；附加判断未确认 | 后端 / 产品 | 影响归集触发准确性 | deferred |
| ALL-GAP-025 | P0 | Card / Transaction Flow | 查询 Card balance 失败后如何处理 | 未确认告警、重试、跳过、人工介入 | 后端 / 运维 | 影响资金遗漏风险 | deferred |
| ALL-GAP-026 | P0 | Card / Transaction Flow | Transfer Balance to Wallet 失败后是否只有告警，是否存在后台人工补偿入口 | 用户确认失败不自动重试，发送异常告警至监控群；补偿入口未确认 | 后端 / 运维 / 账务 | 影响异常闭环 | deferred |
| ALL-GAP-027 | P0 | Card / Transaction Flow | DTC transfer 成功但 Wallet 未入账，是否有系统对账 / 告警机制 | 用户确认当前无法系统自动发现，主要靠用户反馈 | 后端 / Wallet / 账务 | 影响用户资金可见性和风险发现 | deferred |
| ALL-GAP-028 | P1 | Card / Transaction Flow | Card balance 转 Wallet 后，入账币种是否与 card currency 完全一致 | 未确认 | Wallet / 账务 | 影响币种对账 | deferred |
| ALL-GAP-029 | P0 | Card / Transaction Flow | 财务 / 运营最终使用哪些字段串起 DTC 通知、AIX 处理、DTC transfer、Wallet 交易、用户反馈 | 用户确认尚未定 | 账务 / 运营 / 后端 | 影响最终对账 SOP | deferred |
| ALL-GAP-030 | P1 | Wallet / KYC | Wallet KYC 与 Card KYC 关系 | 未确认复用 / 独立 / 部分复用 | 产品 / KYC / 后端 | 影响准入和状态复用 | deferred |
| ALL-GAP-031 | P1 | Wallet / KYC | Wallet KYC 是否为 GTR / WalletConnect Deposit 前置 | 未确认 | 产品 / 合规 / 后端 | 影响 Deposit 入口拦截 | deferred |
| ALL-GAP-032 | P1 | Wallet / KYC | Wallet 开户触发时机 | 注册后自动、进入 Wallet 自动、用户主动触发未确认 | 产品 / 后端 | 影响 Wallet 初始化 | deferred |
| ALL-GAP-033 | P1 | Wallet / KYC | KYC 失败 / 重试 / 人工处理规则 | 未确认用户如何重试、是否人工介入 | 产品 / KYC / 运营 | 影响异常闭环 | deferred |
| ALL-GAP-034 | P2 | Wallet / KYC | KYC 结果是否触发通知 | 未确认 push / 站内信 / email | 产品 / Notification | 影响通知规则 | deferred |
| ALL-GAP-035 | P1 | Common / AAI | AIX 实际依赖哪些 AAI 结果 | 已收窄为 AIX 设计边界，但具体结果类型未补齐 | 产品 / 后端 / KYC | 影响页面、准入、错误处理 | deferred |
| ALL-GAP-036 | P0 | Common / DTC | Webhook 原始报文落库规则 | 与 Card / Wallet 排障、对账相关 | 后端 / 运维 | 影响审计、排障、补偿 | deferred |
| ALL-GAP-037 | P1 | Common / DTC | ActivityType 到 AIX 前端交易类型的映射 | 已知部分 DTC ActivityType，不确认 AIX 前端展示映射 | 产品 / 前端 / 后端 | 影响交易历史筛选和展示 | deferred |
| ALL-GAP-038 | P2 | Common / Errors | 通用错误页文案与错误码映射 | 当前只写已有 PRD / FAQ 文案，不补通用错误码表 | 产品 / UX / 后端 | 影响全局错误处理 | deferred |
| ALL-GAP-039 | P1 | Common / Errors | 告警规则、监控群、责任分派 | 部分 Card 归集失败已确认告警，其他场景未确认 | 后端 / 运维 / 产品 | 影响异常闭环 | deferred |
| ALL-GAP-040 | P2 | Common / FAQ | FAQ Row 14：How can I check the delivery status of my physical card? 无答案 | FAQ 原文缺失答案 | 产品 / 客服 | 影响客服口径 | open |
| ALL-GAP-041 | P2 | Account / Login | Login Page 原始 PRD Description 列从第 4 项开始，1-3 项仅存在于 UX 截图，缺少可结构化文字规则 | 正文保留截图与已知结构化规则 | 产品 / UX | 影响 Login 页面结构化沉淀 | open |
| ALL-GAP-042 | P2 | Account / Login | 账号不存在 / 未注册提示英文最终文案缺失 | 中文原文：`您输入的账号信息有误，请检查或注册新账号。` | 产品 / UX / 文案 | 影响英文文案 | open |
| ALL-GAP-043 | P1 | Common / DTC | DTC 通用响应结构和通用错误码边界 | Common Stage Review 原 COMMON-GAP-001 提到 DTC 通用响应结构和错误码表未补齐；当前不维护完整供应商说明书，但 AIX 统一错误处理所需边界仍需确认 | 后端 / DTC / 产品 | 影响接口统一处理、错误处理、排障 | deferred |
| ALL-GAP-044 | P1 | Common / WalletConnect / Compliance | WalletConnect Declare / Travel Rule / 白名单规则边界 | Common Stage Review 原 COMMON-GAP-004 提到 WC Declare / Travel Rule / 白名单规则未确认；当前已确认 WC Approved 后自动 add whitelist，但 Declare / Travel Rule 的触发和展示边界仍未完整确认 | 产品 / 合规 / 后端 | 影响合规前置、异常处理、用户提示 | deferred |
| ALL-GAP-045 | P1 | Common / Notification | 通知失败重试 / 补发策略 | Common Stage Review 原 COMMON-GAP-006 提到通知失败重试 / 补发策略未确认 | 后端 / Notification / 运维 | 影响通知可靠性和用户感知 | deferred |
| ALL-GAP-046 | P1 | Common / AAI / KYC | AAI OCR / Liveness / KYC 状态和失败原因边界 | Common Stage Review 原 COMMON-GAP-009 提到 AAI OCR / Liveness / KYC 状态和失败原因未补齐；当前只收窄为 AIX 依赖边界 | 产品 / KYC / 后端 | 影响准入、失败提示、人工处理 | deferred |
| ALL-GAP-047 | P2 | Common / FAQ | FAQ 原文和客服口径完整性 | Common Stage Review 原 COMMON-GAP-010 提到 FAQ 原文和客服口径未补齐；当前只确认 Row 14 明确缺失，其他口径仍需以原文为准 | 产品 / 客服 | 影响客服答复完整性 | deferred |
| ALL-GAP-048 | P1 | Transaction / Detail | Wallet Transaction Detail 完整请求 / 响应 / 页面展示 / 复制规则 | Transaction Detail 原 TXN-DETAIL-GAP-001~004 提到 Wallet Detail 完整请求字段、响应字段、页面展示字段、是否支持复制交易 ID 未补齐 | 产品 / 前端 / 后端 / Wallet | 影响 Wallet 交易详情页展示和交互 | deferred |
| ALL-GAP-049 | P1 | Transaction / Detail | Card Detail 前端展示字段完整列表 | Transaction Detail 原 TXN-DETAIL-GAP-007 提到 Card Detail 前端展示字段完整列表待补 | 产品 / 前端 | 影响 Card 交易详情页展示完整性 | deferred |
| ALL-GAP-050 | P1 | Transaction / Status | Wallet `state` 进入 / 退出条件 | Transaction Status Model 原 TXN-STATUS-GAP-001 提到 Wallet `state` 进入 / 退出条件未补齐 | 后端 / Wallet / 产品 | 影响 Wallet 状态机和用户状态理解 | deferred |
| ALL-GAP-051 | P1 | Transaction / Status | Wallet 状态与前端展示文案映射 | Transaction Status Model 原 TXN-STATUS-GAP-002 提到 Wallet 状态与前端展示文案映射未确认 | 产品 / 前端 / UX | 影响交易历史和详情页状态展示 | deferred |
| ALL-GAP-052 | P1 | Wallet / Receive / Transaction | Receive 是否独立上线及状态映射 | Transaction Status Model 原 TXN-STATUS-GAP-006 提到 Receive 状态映射未确认 | 产品 / 后端 / 前端 | 影响 Receive 是否进入 active 交易状态模型 | deferred |
| ALL-GAP-053 | P1 | Card / Transaction | Card DTC 状态与 AIX 前端展示状态映射 | Transaction Status Model 原 TXN-STATUS-GAP-007 提到 Card DTC 状态与 AIX 前端展示状态映射待补 | 产品 / 前端 / 后端 | 影响 Card 交易历史和详情页状态展示 | deferred |
| ALL-GAP-054 | P2 | Transaction / UX | 跨模块最终展示状态是否需要统一文案 | Transaction Status Model 原 TXN-STATUS-GAP-008 提到跨模块最终展示状态是否需要统一文案 | 产品 / UX | 影响 Card / Wallet / Deposit 统一体验 | deferred |

## 3. 优先级定义

| 优先级 | 定义 | 处理原则 |
|---|---|---|
| P0 | 影响资金、对账、状态闭环、用户资产可见性、核心链路追踪 | 优先找后端 / Wallet / 账务确认；未确认前不得写成事实 |
| P1 | 影响页面准入、状态展示、流程体验、分类筛选、KYC 边界 | 可继续推进其他模块，但后续需要确认 |
| P2 | 影响文案、FAQ、低优先、非核心体验 | 不阻塞主链路，可最后统一处理 |

## 4. 已消除 / 已确认项

| 编号 | 原问题 | 处理结果 | 来源 | 状态 |
|---|---|---|---|---|
| RESOLVED-001 | DTC Card Transaction Notify 字段表不可读 / 未确认 | 已补齐字段表来源，不再作为缺口 | DTC Card Issuing / 3.4.4 | resolved |
| RESOLVED-002 | DTC 卡交易 ID 未明确 | 已明确 `data.id` 为 Transaction ID | DTC Card Issuing / 3.4.4 | resolved |
| RESOLVED-003 | DTC 原始交易 ID 未明确 | 已明确 `originalId` 为 Original Transaction ID，选填 | DTC Card Issuing / 3.4.4 | resolved |
| RESOLVED-004 | 重复推送时 Transaction ID 是否变化未明确 | 用户确认重复推送时 Transaction ID 不变 | 用户确认 2026-05-01 | resolved |
| RESOLVED-005 | 是否存在独立 notification id 未明确 | 用户确认没有独立 notification id | 用户确认 2026-05-01 | resolved |
| RESOLVED-006 | Top-up 是否触发自动归集未明确 | 用户确认 Top-up 已移除，不触发自动归集 | 用户确认 2026-05-01 | resolved |
| RESOLVED-007 | 自动归集触发类型不清晰 | 已收敛为 refund / reversal / deposit | 用户确认 2026-05-01；DTC Card Issuing / Appendix B | resolved |
| RESOLVED-008 | `Inquiry Card Basic Info` 实际路径待确认 | 已明确为 `[POST] /openapi/v1/card/inquiry-card-info` | DTC Card Issuing / 3.2.15 | resolved |
| RESOLVED-009 | `Transfer Balance to Wallet` 请求字段待确认 | 已明确请求字段为 `cardId`、`amount` | DTC Card Issuing / 3.3.3 | resolved |
| RESOLVED-010 | `Transfer Balance to Wallet` 成功是否返回归集业务流水未确认 | 已明确 DTC 成功响应仅返回 `header.success=true`，用户确认不会有归集流水 | DTC Card Issuing / 3.3.3；用户确认 2026-05-01 | resolved |
| RESOLVED-011 | 归集失败是否自动重试未确认 | 用户确认不自动重试，发送异常告警至监控群 | 用户确认 2026-05-01 | resolved |
| RESOLVED-012 | DTC transfer 成功但 Wallet 未入账如何发现未明确 | 用户确认当前无法系统自动发现，靠用户反馈 | 用户确认 2026-05-01 | resolved |
| RESOLVED-013 | 用户收到退款 / 卡交易成功通知是否代表 Wallet 可见资金未明确 | 用户确认正常代表 Wallet 可见，极端情况下可能卡有钱但转 Wallet 失败 | 用户确认 2026-05-01 | resolved |
| RESOLVED-014 | Wallet 入账是否有交易 ID 未确认 | 已确认钱包交易记录 / 详情出参均包含 `id`，Long，交易 id | DTC Wallet OpenAPI；用户确认 2026-05-01 | resolved |
| RESOLVED-015 | Wallet 单笔交易详情查询入参未确认 | 已确认入参为 `transactionId`，Unique transaction ID from DTC；但与 Card `data.id` / `D-REQUEST-ID` 的关联未说明 | DTC Wallet OpenAPI；用户确认 2026-05-01 | resolved |
| RESOLVED-016 | Wallet 入账状态字段与枚举未确认 | 已确认字段为 `state`，枚举为 `PENDING`、`PROCESSING`、`AUTHORIZED`、`COMPLETED`、`REJECTED`、`CLOSED` | DTC Wallet OpenAPI；用户确认 2026-05-01 | resolved |

## 5. 使用规则

1. 所有新增不确定项，统一追加到“全模块待确认总表”。
2. 功能正文不得把 `deferred` 或 `open` 的问题写成事实。
3. 功能正文如需提及未确认事项，只引用 `ALL-GAP-XXX` 编号，不再展开维护模块级 checklist。
4. 用户后续确认后，应更新本表状态，并同步回填对应功能文件。
5. 已确认但仍有实现细节缺口的问题，可标记为 `resolved-by-user`，并在影响文件中写入边界。
6. 已彻底闭环的问题可迁移至“已消除 / 已确认项”。
7. `IMPLEMENTATION_PLAN.md` 只维护阶段状态和执行规则，不再维护另一套待确认清单。
