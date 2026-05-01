# prd-for-ai 实施计划

版本：v1.5  
状态：执行中  
适用仓库：`prd-for-ai`  
更新时间：2026-05-01

## 1. 文档定位

本文件是 `prd-for-ai` 仓库的长期实施主控文件。

本项目会跨多个对话、多个时间段持续推进。后续每次开始执行前，必须先读取本文件，确认当前阶段、当前模块、待办任务和验收标准，再继续执行。

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
| 3 | Security 标准化 | 进行中（AIX OTP类已完成） | 统一认证事实源 | OTP / Email OTP / Passcode / BIO / IVS | 继续 Login Passcode |
| 4 | Card 批量推进 | 未开始 | 转译卡模块 | Application / Manage / Transaction | 等 Security 完成 |
| 5 | Wallet 批量推进 | 未开始 | 转译钱包模块 | KYC / Send / Swap / Receive / Deposit | 等 Security 完成 |
| 6 | Transaction 统一层 | 未开始 | 统一交易状态 | Card / Wallet / Swap / History | Card / Wallet 后执行 |
| 7 | Common / Integration | 未开始 | 抽公共能力 | DTC / AAI / WC / Error / FAQ | Transaction 后执行 |
| 8 | 全仓库回扫 | 未开始 | 去重复、补引用 | 字段 / 状态 / 来源 / gaps | 最后执行 |

---

## 12. 阶段内任务拆解

### 12.3 阶段 3：Security 标准化（已更新进度）

| 子任务 | 状态 | 说明 |
|---|---|---|
| security/_index.md | 已完成 | Security 模块边界与功能清单已收口 |
| global-rules.md | 已完成 | 全局认证规则、场景矩阵、优先级、有效期、状态机已收口 |
| otp-verification.md | 已完成 | 短信 OTP 已标准化 |
| email-otp-verification.md | 已完成 | 邮箱 OTP 已标准化 |
| login-passcode-verification.md | 未开始 | 下一步执行 |
| biometric-verification.md | 未开始 | 待执行 |
| face-authentication.md | 未开始 | 待执行 |
| api-reference.md | 未开始 | 待执行 |

---

## 17. 当前状态（同步修正）

| 模块 | 状态 | 说明 |
|---|---|---|
| Account / Login | 已完成 | 样板完成 |
| Account / Registration | 已完成 | 已按原 PRD 重构 |
| Account / Password Reset | 已完成 | 已标准化 |
| Account / _index | 已完成 | 模块收口 |
| Security / index | 已完成 | 模块边界完成 |
| Security / global-rules | 已完成 | 认证核心规则完成 |
| Security / OTP | 已完成 | 短信 OTP 完成 |
| Security / Email OTP | 已完成 | 邮箱 OTP 完成 |
| Security / Passcode | 未开始 | 下一步 |
| Security / BIO | 未开始 | 待执行 |
| Security / Face Auth | 未开始 | 待执行 |

---

## 18. 下一步（同步更新）

当前执行点：

1. 开始 `login-passcode-verification.md`
2. 按同样标准结构重构
3. 不重复 global rules
4. 完成后判断是否形成能力块；若形成，更新实施计划

当前禁止事项：

- 不得跳到 Card / Wallet
- 不得重复写 global rules
- 不得在未引用来源的情况下补规则
