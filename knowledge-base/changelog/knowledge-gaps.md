---
module: changelog
feature: knowledge-gaps
version: "1.4"
status: active
source_doc: IMPLEMENTATION_PLAN.md；knowledge-base/card/card-transaction-flow.md；knowledge-base/card/stage-review.md；knowledge-base/card/transaction-flow-traceability-checklist.md；knowledge-base/wallet/transaction-history.md；knowledge-base/common/dtc.md；用户确认结论 2026-05-01；用户确认结论 2026-05-02
source_section: source-policy；Card Transaction Flow；Card Stage Review；deferred gaps decision；traceability follow-up list
last_updated: 2026-05-02
owner: 吴忆锋
---

# Knowledge Gaps 知识缺口与冲突记录

## 1. 文档定位

本文档用于集中记录知识库转译过程中发现的文档缺口、原文疑似异常、口径冲突和需要后续确认的信息。

功能正文应优先承载稳定事实；不确定事项集中放在本文档，避免污染事实来源正文。

当前用户已确认：资金追踪链路相关问题短期无法得到答案，先整理为待回头确认清单，不阻塞后续非资金链路内容继续推进。

## 2. 资金追踪链路待回头确认清单

以下清单用于后续统一向后端 / Wallet / DTC / 账务确认。当前全部保持 `deferred`，不得写入功能正文作为事实。

| 编号 | 待确认问题 | 需要确认对象 | 影响 | 当前处理 |
|---|---|---|---|---|
| TRACE-FOLLOWUP-001 | Card Transaction / refund / reversal / deposit 与 Wallet Transaction 是否存在一一对应关系 | 后端 / Wallet / 账务 | 决定是否能从卡交易追踪到钱包入账 | deferred |
| TRACE-FOLLOWUP-002 | 如果存在关联，具体用哪个字段关联：Card `data.id`、Wallet `transactionId`、Wallet `id`、`relatedId`、`D-REQUEST-ID`、AIX 内部 ID 或其他字段 | 后端 / Wallet / 账务 | 决定对账字段组合 | deferred |
| TRACE-FOLLOWUP-003 | AIX 收到 DTC Card Transaction Notify 后是否生成内部交易处理 ID，字段名是什么 | 后端 | 影响内部处理链路追踪 | deferred |
| TRACE-FOLLOWUP-004 | AIX 发起 Transfer Balance to Wallet 前是否生成归集请求 ID，字段名是什么 | 后端 / 账务 | 影响归集请求追踪 | deferred |
| TRACE-FOLLOWUP-005 | `D-REQUEST-ID` 是否仅是请求唯一标识，还是也承担幂等 / 重试去重作用 | 后端 / DTC | 影响请求幂等和重试设计 | deferred |
| TRACE-FOLLOWUP-006 | DTC Webhook 原始报文是否完整落库，是否可回放 / 查询 | 后端 / 运维 | 影响审计、排障、补偿 | deferred |
| TRACE-FOLLOWUP-007 | 重复通知实际如何去重，是否按 `event + data.id` | 后端 | 影响重复推送处理 | deferred |
| TRACE-FOLLOWUP-008 | 自动归集触发是否只依赖 `type=refund/reversal/deposit`，还是还需要判断 state / indicator / amount | 后端 / 产品 | 影响归集触发准确性 | deferred |
| TRACE-FOLLOWUP-009 | 查询 Card balance 失败后如何处理：告警、重试、跳过、人工介入 | 后端 / 运维 | 影响资金遗漏风险 | deferred |
| TRACE-FOLLOWUP-010 | Transfer Balance to Wallet 失败后是否只有告警，是否存在后台人工补偿入口 | 后端 / 运维 / 账务 | 影响异常闭环 | deferred |
| TRACE-FOLLOWUP-011 | DTC transfer 成功但 Wallet 未入账，是否有系统对账 / 告警机制；若无，是否只靠用户反馈 | 后端 / Wallet / 账务 | 影响用户资金可见性和风险发现 | deferred |
| TRACE-FOLLOWUP-012 | Wallet `relatedId` 在 Card balance 转 Wallet、GTR、WalletConnect 场景下分别取什么值 | Wallet / DTC / 后端 | 影响 Wallet History 关联和对账 | deferred |
| TRACE-FOLLOWUP-013 | Deposit success 与 Wallet `state=COMPLETED` 是否存在确定映射 | Wallet / 后端 | 影响状态展示 | deferred |
| TRACE-FOLLOWUP-014 | Risk Withheld 与 Wallet `state` 是否存在映射，是否影响冻结余额 / 可用余额 | Wallet / 后端 / 产品 | 影响余额展示和用户提示 | deferred |
| TRACE-FOLLOWUP-015 | GTR 是否使用 `FIAT_DEPOSIT=6`，WalletConnect 是否使用 `CRYPTO_DEPOSIT=10` | Wallet / 后端 / 产品 | 影响交易分类和筛选 | deferred |
| TRACE-FOLLOWUP-016 | Deposit success 后余额何时对用户可见 / 可用 | Wallet / 后端 / 产品 | 影响用户体验和 FAQ 口径 | deferred |
| TRACE-FOLLOWUP-017 | Card balance 转 Wallet 后，入账币种是否与 card currency 完全一致 | Wallet / 账务 | 影响币种对账 | deferred |
| TRACE-FOLLOWUP-018 | 财务 / 运营最终使用哪些字段串起 DTC 通知、AIX 处理、DTC transfer、Wallet 交易、用户反馈 | 账务 / 运营 / 后端 | 影响最终对账 SOP | deferred |

## 3. Card / Transaction Flow deferred gaps

以下问题当前暂无答案，经用户确认先跳过并继续其他知识库转译。状态统一标记为 `deferred`，不得写入功能正文作为事实。

| 编号 | 问题 | 影响范围 | 来源 | 当前处理 | 状态 |
|---|---|---|---|---|---|
| KG-CARD-TXN-001 | AIX 收到 `Card Transaction Notify` 后是否生成内部交易处理 ID，字段名未确认 | Card Transaction Flow / 内部追踪 | card-transaction-flow.md；stage-review.md | 暂无答案，后续后端确认后回填 | deferred |
| KG-CARD-TXN-002 | DTC Webhook 原始报文是否完整落库未确认 | Card Transaction Flow / 审计 / 回放 | card-transaction-flow.md；stage-review.md | 暂无答案，后续后端确认后回填 | deferred |
| KG-CARD-TXN-003 | 后端重复通知处理是否按 `event + data.id` 去重未确认 | Card Transaction Flow / 幂等 / 防重复 | 用户确认重复推送 Transaction ID 不变；DTC 无独立 notification id | 去重依据基础已明确，实现规则待后端回填 | deferred |
| KG-CARD-TXN-004 | 自动归集触发是否只判断 `type=REFUND/REVERSAL/DEPOSIT`，还是还需判断 `state` / `indicator` 未确认 | Card Transaction Flow / 归集触发 | 用户确认只关注 refund / reversal / deposit；DTC 枚举已补齐 | 触发类型已写入正文，附加状态判断待后端回填 | deferred |
| KG-CARD-TXN-005 | AIX 发起 `Transfer Balance to Wallet` 前是否生成归集请求 ID，字段名未确认 | Card Transaction Flow / 归集追踪 | stage-review.md；traceability-checklist.md | 暂无答案，后续后端确认后回填 | deferred |
| KG-CARD-TXN-006 | `D-REQUEST-ID` 如何生成、保存，并与归集请求 ID 关联未确认 | Card Transaction Flow / 请求追踪 / 幂等 | DTC Card Issuing / 2.4；traceability-checklist.md | 仅写 DTC 文档中的请求唯一标识，不写成幂等键 | deferred |
| KG-CARD-TXN-007 | DTC `data.id`、AIX 内部交易处理 ID、AIX 归集请求 ID、`D-REQUEST-ID`、Wallet 交易 `id` 之间的链路关系未确认 | Card Transaction Flow / 资金可追溯 | stage-review.md；traceability-checklist.md | 暂无答案，后续确认后回填 | deferred |
| KG-CARD-TXN-008 | 查询卡 `balance` 失败后的处理规则未确认 | Card Transaction Flow / 异常处理 | AIX Card交易【transaction】/ 9 | 暂无答案，后续确认后回填 | deferred |
| KG-CARD-TXN-009 | 归集失败告警后是否存在后台人工补偿入口未确认 | Card Transaction Flow / 人工处理 | 用户确认失败不自动重试；AIX Card交易【transaction】/ 7.3 | 暂无答案，后续确认后回填 | deferred |
| KG-CARD-TXN-010 | 除系统原因 / 金额大于卡余额外，其他失败类型与责任分派未确认 | Card Transaction Flow / 异常责任 | AIX Card交易【transaction】/ 7.3 | 暂无答案，后续确认后回填 | deferred |
| KG-CARD-TXN-011 | Wallet 交易 `id` 如何关联 DTC `data.id`、AIX 归集请求 ID 或 `D-REQUEST-ID` 未确认 | Card Transaction Flow / Wallet 入账 / 对账 | 用户确认 Wallet 交易记录 / 详情有 `id`；关联规则未说明 | 暂无答案，后续 Wallet / 账务确认后回填 | deferred |
| KG-CARD-TXN-012 | Wallet `Search Balance History.relatedId` 在卡余额转 Wallet 场景下取哪个 ID 未确认 | Card Transaction Flow / Wallet relatedId | DTC Wallet OpenAPI / 4.2.4 | 暂无答案，后续 Wallet / 账务确认后回填 | deferred |
| KG-CARD-TXN-013 | card balance 转 Wallet 后，入账币种是否与 card currency 完全一致未确认 | Card Transaction Flow / 币种口径 | traceability-checklist.md | 暂无答案，后续 Wallet / 账务确认后回填 | deferred |
| KG-CARD-TXN-014 | 财务 / 运营最终使用哪些字段串起 DTC 通知、AIX 归集请求、DTC transfer 调用和 Wallet 交易 `id` 未确认 | Card Transaction Flow / 对账字段 | 用户确认尚未定 | 暂无答案，后续确认后回填 | deferred |

## 4. Card / Transaction Flow 已消除缺口

| 编号 | 原问题 | 处理结果 | 来源 | 状态 |
|---|---|---|---|---|
| KG-CARD-TXN-RESOLVED-001 | DTC Card Transaction Notify 字段表不可读 / 未确认 | 已补齐字段表来源，不再作为缺口 | DTC Card Issuing / 3.4.4 | resolved |
| KG-CARD-TXN-RESOLVED-002 | DTC 卡交易 ID 未明确 | 已明确 `data.id` 为 Transaction ID | DTC Card Issuing / 3.4.4 | resolved |
| KG-CARD-TXN-RESOLVED-003 | DTC 原始交易 ID 未明确 | 已明确 `originalId` 为 Original Transaction ID，选填 | DTC Card Issuing / 3.4.4 | resolved |
| KG-CARD-TXN-RESOLVED-004 | 重复推送时 Transaction ID 是否变化未明确 | 用户确认重复推送时 Transaction ID 不变 | 用户确认 2026-05-01 | resolved |
| KG-CARD-TXN-RESOLVED-005 | 是否存在独立 notification id 未明确 | 用户确认没有独立 notification id | 用户确认 2026-05-01 | resolved |
| KG-CARD-TXN-RESOLVED-006 | Top-up 是否触发自动归集未明确 | 用户确认 Top-up 已移除，不触发自动归集 | 用户确认 2026-05-01 | resolved |
| KG-CARD-TXN-RESOLVED-007 | 自动归集触发类型不清晰 | 已收敛为 refund / reversal / deposit | 用户确认 2026-05-01；DTC Card Issuing / Appendix B | resolved |
| KG-CARD-TXN-RESOLVED-008 | `Inquiry Card Basic Info` 实际路径待确认 | 已明确为 `[POST] /openapi/v1/card/inquiry-card-info` | DTC Card Issuing / 3.2.15 | resolved |
| KG-CARD-TXN-RESOLVED-009 | `Transfer Balance to Wallet` 请求字段待确认 | 已明确请求字段为 `cardId`、`amount` | DTC Card Issuing / 3.3.3 | resolved |
| KG-CARD-TXN-RESOLVED-010 | `Transfer Balance to Wallet` 成功是否返回归集业务流水未确认 | 已明确 DTC 成功响应仅返回 `header.success=true`，用户确认不会有归集流水 | DTC Card Issuing / 3.3.3；用户确认 2026-05-01 | resolved |
| KG-CARD-TXN-RESOLVED-011 | 归集失败是否自动重试未确认 | 用户确认不自动重试，发送异常告警至监控群 | 用户确认 2026-05-01 | resolved |
| KG-CARD-TXN-RESOLVED-012 | DTC transfer 成功但 Wallet 未入账如何发现未明确 | 用户确认当前无法系统自动发现，靠用户反馈 | 用户确认 2026-05-01 | resolved |
| KG-CARD-TXN-RESOLVED-013 | 用户收到退款 / 卡交易成功通知是否代表 Wallet 可见资金未明确 | 用户确认正常代表 Wallet 可见，极端情况下可能卡有钱但转 Wallet 失败 | 用户确认 2026-05-01 | resolved |
| KG-CARD-TXN-RESOLVED-014 | Wallet 入账是否有交易 ID 未确认 | 已确认钱包交易记录 / 详情出参均包含 `id`，Long，交易 id | DTC Wallet OpenAPI；用户确认 2026-05-01 | resolved |
| KG-CARD-TXN-RESOLVED-015 | Wallet 单笔交易详情查询入参未确认 | 已确认入参为 `transactionId`，Unique transaction ID from DTC；但与 Card `data.id` / `D-REQUEST-ID` 的关联未说明 | DTC Wallet OpenAPI；用户确认 2026-05-01 | resolved |
| KG-CARD-TXN-RESOLVED-016 | Wallet 入账状态字段与枚举未确认 | 已确认字段为 `state`，枚举为 `PENDING`、`PROCESSING`、`AUTHORIZED`、`COMPLETED`、`REJECTED`、`CLOSED` | DTC Wallet OpenAPI；用户确认 2026-05-01 | resolved |

## 5. Account / Login

| 编号 | 问题 | 影响范围 | 来源 | 当前处理 | 状态 |
|---|---|---|---|---|---|
| KG-LOGIN-001 | Login Page 原始 PRD Description 列从第 4 项开始，1-3 项仅存在于 UX 截图，缺少可结构化文字规则 | Login Page / 页面元素 | AIX Card 注册登录需求V1.0 / 7.2.4 Login Page | 正文保留截图与已知结构化规则；缺失项不脑补 | open |
| KG-LOGIN-002 | 账号不存在 / 未注册提示为中文原文：`您输入的账号信息有误，请检查或注册新账号。`，英文最终文案缺失 | Login Page / 文案 | AIX Card 注册登录需求V1.0 / 7.2.4 Login Page | 正文保留中文原文，不替换为英文推测 | open |

## 6. 其他历史缺口

本文件当前重点已同步 Card Transaction Flow 缺口。Account / Security / Card 其他历史缺口保持在既有知识库正文与阶段文件中，后续全仓库回扫时再统一归并。
