---
module: changelog
feature: knowledge-gaps
version: "1.3"
status: active
source_doc: IMPLEMENTATION_PLAN.md；knowledge-base/card/card-transaction-flow.md；knowledge-base/card/stage-review.md；knowledge-base/card/transaction-flow-traceability-checklist.md；用户确认结论 2026-05-01
source_section: source-policy；Card Transaction Flow；Card Stage Review；deferred gaps decision
last_updated: 2026-05-01
owner: 吴忆锋
---

# Knowledge Gaps 知识缺口与冲突记录

## 1. 文档定位

本文档用于集中记录知识库转译过程中发现的文档缺口、原文疑似异常、口径冲突和需要后续确认的信息。

功能正文应优先承载稳定事实；不确定事项集中放在本文档，避免污染事实来源正文。

## 2. Card / Transaction Flow deferred gaps

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

## 3. Card / Transaction Flow 已消除缺口

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

## 4. Account / Login

| 编号 | 问题 | 影响范围 | 来源 | 当前处理 | 状态 |
|---|---|---|---|---|---|
| KG-LOGIN-001 | Login Page 原始 PRD Description 列从第 4 项开始，1-3 项仅存在于 UX 截图，缺少可结构化文字规则 | Login Page / 页面元素 | AIX Card 注册登录需求V1.0 / 7.2.4 Login Page | 正文保留截图与已知结构化规则；缺失项不脑补 | open |
| KG-LOGIN-002 | 账号不存在 / 未注册提示为中文原文：`您输入的账号信息有误，请检查或注册新账号。`，英文最终文案缺失 | Login Page / 文案 | AIX Card 注册登录需求V1.0 / 7.2.4 Login Page | 正文保留中文原文，不替换为英文推测 | open |

## 5. 其他历史缺口

本文件当前重点已同步 Card Transaction Flow 缺口。Account / Security / Card 其他历史缺口保持在既有知识库正文与阶段文件中，后续全仓库回扫时再统一归并。
