# prd-for-ai 实施计划

版本：v3.1  
状态：Card 阶段回扫阻塞  
适用仓库：`prd-for-ai`  
更新时间：2026-05-01

## 1. 文档定位

本文件是 `prd-for-ai` 仓库的长期实施主控文件。

后续每次开始执行前，必须先读取本文件，确认当前阶段、当前模块、待办任务和验收标准，再继续执行。

本文件优先级高于临时对话结论。若临时任务与本实施计划冲突，必须先更新本实施计划，再执行具体任务。

## 2. 强制执行原则

1. `IMPLEMENTATION_PLAN.md` 是唯一主控计划。
2. 每次开始任务前，必须先读取本文件。
3. 如果用户临时要求与本文件冲突，先更新本文件，再执行任务。
4. 不允许跳阶段。
5. 不允许用新的模块清单替代阶段计划。
6. 模块清单只能作为阶段内的执行子任务。
7. 若发现本实施计划不符合当前真实进度，必须先修正实施计划，再继续执行。
8. 所有内容必须来源于历史 PRD、接口文档、截图、已确认结论或已存在知识库。
9. 允许跨文档、跨模块引用已确认事实。
10. 禁止无来源补流程、补页面、补字段、补状态、补文案。
11. 每完成一个能力块，必须同步更新本文件；单文件未形成能力块时，可只更新模块 `_index.md`。

---

## 11. 阶段实施路线表

| 阶段 | 名称 | 当前状态 | 目标 | 阶段产出 | 下一步 |
|---|---|---|---|---|---|
| 1 | Account 样板 | 已完成 | 固化知识库写法 | Login / Registration / Password Reset | 已完成 |
| 2 | 基础规则沉淀 | 部分完成 | 建立长期规则 | Writing Standard / Source Rules | 持续完善 |
| 3 | Security 标准化 | 已完成 | 统一认证事实源 | OTP / Email OTP / Passcode / BIO / Face Auth / API Reference | 已完成 |
| 4 | Card 批量推进 | 阻塞 | 转译卡模块 | Application / Status & Fields / Home / Manage / Transaction | 等待追踪字段确认 |
| 5 | Wallet 批量推进 | 未开始 | 转译钱包模块 | KYC / Send / Swap / Receive / Deposit | 等 Card 阻塞解除 |
| 6 | Transaction 统一层 | 未开始 | 统一交易状态 | Card / Wallet / Swap / History | Card / Wallet 后执行 |
| 7 | Common / Integration | 未开始 | 抽公共能力 | DTC / AAI / WC / Error / FAQ | Transaction 后执行 |
| 8 | 全仓库回扫 | 未开始 | 去重复、补引用 | 字段 / 状态 / 来源 / gaps | 最后执行 |

---

## 12. 阶段内任务拆解

### 12.4 阶段 4：Card 批量推进（阻塞）

| 子任务 | 状态 | 说明 |
|---|---|---|
| card/_index.md | 已完成 | Card 模块边界与功能清单已收口 |
| application.md | 已完成 | 申卡流程、资格、费用、币种、地区、卡类型、自动扣款、接口依赖已收口；缺口已记录 |
| card-status-and-fields.md | 已完成 | 卡状态、字段、接口路径、操作限制缺口已收口 |
| card-home.md | 已完成 | 卡首页、展示、入口、交易摘要、物流信息和 FAQ 已收口 |
| activation.md | 已完成 | 实体卡激活流程已收口 |
| pin.md | 已完成 | PIN 相关能力已收口 |
| sensitive-info.md | 已完成 | 卡信息安全查看流程已收口 |
| card-management.md | 已完成 | 卡管理操作、状态边界、接口依赖与失败处理已收口 |
| card-transaction-flow.md | 已完成但阻塞 | 卡交易通知、目标类型判断、余额查询、归集处理、交易展示边界已收口；追踪字段未闭环 |
| stage-review.md | 已完成 | Card 阶段回扫完成，结论为暂缓进入 Wallet |
| transaction-flow-traceability-checklist.md | 已完成 | 已形成 DTC / 后端 / Wallet 需确认清单 |

---

## 17. 当前状态（同步修正）

| 模块 | 状态 | 说明 |
|---|---|---|
| Account | 已完成 | Login / Registration / Password Reset 已完成 |
| Security | 已完成 | Security 阶段全部收口 |
| Card / 页面与卡管能力 | 已完成 | Application / Home / Activation / PIN / Sensitive Info / Management 已完成 |
| Card / Transaction Flow | 阻塞 | 资金归集链路缺少可追溯字段闭环 |
| Card / Traceability Checklist | 已完成 | 已生成确认清单，等待 DTC / 后端 / Wallet 确认 |
| Wallet | 未开始 | 等 Card 阻塞解除后执行 |

---

## 18. 下一步（同步更新）

当前执行点：

1. 将 `knowledge-base/card/transaction-flow-traceability-checklist.md` 发给 DTC / 后端 / Wallet 确认
2. 等待确认 DTC 通知字段、AIX 内部交易 ID、归集请求 ID、归集结果流水、钱包入账流水、幂等键、重试策略
3. 收到确认后更新 `card-transaction-flow.md`、`knowledge-gaps.md`、`stage-review.md`
4. 重新执行 Card 阶段回扫

当前禁止事项：

- 不得直接跳到 Wallet
- 不得把未确认流水字段写成事实
- 不得新增无来源状态、字段或接口
- 不得把 Transaction 统一层提前混入 Card 阶段正文
