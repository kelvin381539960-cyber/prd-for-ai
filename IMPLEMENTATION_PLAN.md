# prd-for-ai 实施计划

版本：v2.8  
状态：执行中  
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
| 4 | Card 批量推进 | 当前阶段 | 转译卡模块 | Application / Status & Fields / Home / Manage / Transaction | 继续 card-transaction-flow.md |
| 5 | Wallet 批量推进 | 未开始 | 转译钱包模块 | KYC / Send / Swap / Receive / Deposit | 等 Card 完成 |
| 6 | Transaction 统一层 | 未开始 | 统一交易状态 | Card / Wallet / Swap / History | Card / Wallet 后执行 |
| 7 | Common / Integration | 未开始 | 抽公共能力 | DTC / AAI / WC / Error / FAQ | Transaction 后执行 |
| 8 | 全仓库回扫 | 未开始 | 去重复、补引用 | 字段 / 状态 / 来源 / gaps | 最后执行 |

---

## 12. 阶段内任务拆解

### 12.3 阶段 3：Security 标准化（已完成）

| 子任务 | 状态 | 说明 |
|---|---|---|
| security/_index.md | 已完成 | Security 模块边界与功能清单已收口 |
| global-rules.md | 已完成 | 全局认证规则、场景矩阵、优先级、有效期、状态机已收口 |
| otp-verification.md | 已完成 | 短信 OTP 已标准化 |
| email-otp-verification.md | 已完成 | 邮箱 OTP 已标准化 |
| login-passcode-verification.md | 已完成 | Login Passcode 已标准化 |
| biometric-verification.md | 已完成 | 设备生物识别已标准化，已与 Face Authentication 分离 |
| face-authentication.md | 已完成 | DTC / AAI 侧活体识别已标准化 |
| api-reference.md | 已完成 | 外部验证 URL、结果查询、错误码映射与接口缺口已收口 |

### 12.4 阶段 4：Card 批量推进（当前阶段）

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
| card-transaction-flow.md | 未开始 | 下一步执行，卡交易关联流程 |

---

## 17. 当前状态（同步修正）

| 模块 | 状态 | 说明 |
|---|---|---|
| Account / Login | 已完成 | 样板完成 |
| Account / Registration | 已完成 | 已按原 PRD 重构 |
| Account / Password Reset | 已完成 | 已标准化 |
| Account / _index | 已完成 | 模块收口 |
| Security | 已完成 | Security 阶段全部收口 |
| Card / _index | 已完成 | Card 模块边界完成 |
| Card / Application | 已完成 | 申卡流程完成，缺口已记录 |
| Card / Status & Fields | 已完成 | 状态展示组、字段字典、接口路径表、缺口记录已建立 |
| Card / Home | 已完成 | 首页展示与入口完成 |
| Card / Activation | 已完成 | 实体卡激活完成，缺口已记录 |
| Card / PIN | 已完成 | PIN 能力完成，缺口已记录 |
| Card / Sensitive Info | 已完成 | 卡信息安全查看完成，缺口已记录 |
| Card / Management | 已完成 | 卡管理能力完成，缺口已记录 |
| Card / Transaction Flow | 未开始 | 下一步 |

---

## 18. 下一步（同步更新）

当前执行点：

1. 开始 `card/card-transaction-flow.md`
2. 只写卡交易关联流程、状态边界、接口依赖与失败处理
3. 必须引用 `card-status-and-fields.md`，不得重新定义卡状态
4. 涉及资金处理必须明确可追溯字段和文档缺口
5. 完成后进入 Card 阶段回扫

当前禁止事项：

- 不得直接跳到 Wallet
- 不得重复写 Security 认证规则
- 不得重新发明 Card 状态
- 不得把 Wallet 模块流程混入 Card Transaction Flow 正文
