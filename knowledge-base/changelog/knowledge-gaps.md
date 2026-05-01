---
module: changelog
feature: knowledge-gaps
version: "1.1"
status: active
source_doc: IMPLEMENTATION_PLAN.md；knowledge-base/card/card-transaction-flow.md；knowledge-base/card/stage-review.md；knowledge-base/card/transaction-flow-traceability-checklist.md
source_section: source-policy；Card Transaction Flow；Card Stage Review
last_updated: 2026-05-01
owner: 吴忆锋
---

# Knowledge Gaps 知识缺口与冲突记录

## 1. 文档定位

本文档用于集中记录知识库转译过程中发现的文档缺口、原文疑似异常、口径冲突和需要后续确认的信息。

功能正文应优先承载稳定事实；不确定事项集中放在本文档，避免污染事实来源正文。

## 2. Card / Transaction Flow

| 编号 | 问题 | 影响范围 | 来源 | 当前处理 | 状态 |
|---|---|---|---|---|---|
| KG-CARD-TXN-001 | AIX 收到 `Card Transaction Notify` 后是否生成内部交易处理 ID，字段名未确认 | Card Transaction Flow / 内部追踪 | card-transaction-flow.md；stage-review.md | 正文不补字段名；等待后端确认 | open |
| KG-CARD-TXN-002 | DTC Webhook 原始报文是否完整落库未确认 | Card Transaction Flow / 审计 / 回放 | card-transaction-flow.md；stage-review.md | 记录为后端待确认 | open |
| KG-CARD-TXN-003 | 后端重复通知处理是否按 `event + data.id` 去重未确认 | Card Transaction Flow / 幂等 / 防重复 | 用户确认重复推送 Transaction ID 不变；DTC 无独立 notification id | 正文写去重依据为可用基础，但实现规则仍待后端确认 | open |
| KG-CARD-TXN-004 | 自动归集触发是否只判断 `type=REFUND/REVERSAL/DEPOSIT`，还是还需判断 `state` / `indicator` 未确认 | Card Transaction Flow / 归集触发 | 用户确认只关注 refund / reversal / deposit；DTC 枚举已补齐 | 触发类型已写入正文；附加状态判断待后端确认 | open |
| KG-CARD-TXN-005 | AIX 发起 `Transfer Balance to Wallet` 前是否生成归集请求 ID，字段名未确认 | Card Transaction Flow / 归集追踪 | stage-review.md；traceability-checklist.md | 正文不补字段名；等待后端确认 | open |
| KG-CARD-TXN-006 | `D-REQUEST-ID` 如何生成、保存，并与归集请求 ID 关联未确认 | Card Transaction Flow / 请求追踪 / 幂等 | DTC Card Issuing / 2.4；traceability-checklist.md | 仅写 DTC 文档中的请求唯一标识，不写成幂等键 | open |
| KG-CARD-TXN-007 | DTC `data.id`、AIX 内部交易处理 ID、AIX 归集请求 ID、`D-REQUEST-ID`、钱包流水之间的链路关系未确认 | Card Transaction Flow / 资金可追溯 | stage-review.md；traceability-checklist.md | 阶段继续 BLOCK | open |
| KG-CARD-TXN-008 | 查询卡 `balance` 失败后的处理规则未确认 | Card Transaction Flow / 异常处理 | AIX Card交易【transaction】/ 9 | 正文仅标记待确认 | open |
| KG-CARD-TXN-009 | 归集失败告警后是否存在后台人工补偿入口未确认 | Card Transaction Flow / 人工处理 | 用户确认失败不自动重试；AIX Card交易【transaction】/ 7.3 | 记录为后端待确认 | open |
| KG-CARD-TXN-010 | 除系统原因 / 金额大于卡余额外，其他失败类型与责任分派未确认 | Card Transaction Flow / 异常责任 | AIX Card交易【transaction】/ 7.3 | 记录为后端待确认 | open |
| KG-CARD-TXN-011 | `Transfer Balance to Wallet` 成功后 Wallet 侧是否生成入账流水 ID，字段名未确认 | Card Transaction Flow / Wallet 入账 | DTC Wallet OpenAPI / 4.2.4；traceability-checklist.md | 记录为 Wallet / 账务待确认 | open |
| KG-CARD-TXN-012 | Wallet 流水如何关联 DTC `data.id`、AIX 归集请求 ID 或 `D-REQUEST-ID` 未确认 | Card Transaction Flow / 对账 | traceability-checklist.md | 记录为 Wallet / 账务待确认 | open |
| KG-CARD-TXN-013 | Wallet `Search Balance History.relatedId` 在卡余额转 Wallet 场景下取哪个 ID 未确认 | Card Transaction Flow / Wallet relatedId | DTC Wallet OpenAPI / 4.2.4 | 记录为 Wallet / 账务待确认 | open |
| KG-CARD-TXN-014 | card balance 转 Wallet 后，入账币种是否与 card currency 完全一致未确认 | Card Transaction Flow / 币种口径 | traceability-checklist.md | 记录为 Wallet / 账务待确认 | open |
| KG-CARD-TXN-015 | 钱包入账是否有 pending / success / failed 等状态未确认 | Card Transaction Flow / 入账状态 | DTC Wallet OpenAPI / 4.2.4 | 记录为 Wallet / 账务待确认 | open |
| KG-CARD-TXN-016 | 财务 / 运营最终使用哪些字段串起 DTC 通知、AIX 归集请求、DTC transfer 调用和钱包流水未确认 | Card Transaction Flow / 对账字段 | 用户确认尚未定 | 记录为 Wallet / 账务待确认；阶段继续 BLOCK | open |

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

## 4. Account / Login

| 编号 | 问题 | 影响范围 | 来源 | 当前处理 | 状态 |
|---|---|---|---|---|---|
| KG-LOGIN-001 | Login Page 原始 PRD Description 列从第 4 项开始，1-3 项仅存在于 UX 截图，缺少可结构化文字规则 | Login Page / 页面元素 | AIX Card 注册登录需求V1.0 / 7.2.4 Login Page | 正文保留截图与已知结构化规则；缺失项不脑补 | open |
| KG-LOGIN-002 | 账号不存在 / 未注册提示为中文原文：`您输入的账号信息有误，请检查或注册新账号。`，英文最终文案缺失 | Login Page / 文案 | AIX Card 注册登录需求V1.0 / 7.2.4 Login Page | 正文保留中文原文，不替换为英文推测 | open |

## 5. 其他历史缺口

本文件当前重点已同步 Card Transaction Flow 缺口。Account / Security / Card 其他历史缺口保持在既有知识库正文与阶段文件中，后续全仓库回扫时再统一归并。
