# prd-for-ai 实施计划

版本：v3.5  
状态：Card 阶段 PARTIAL PASS，资金追踪遗留项 deferred，允许继续后续阶段  
适用仓库：`prd-for-ai`  
更新时间：2026-05-01

## 1. 文档定位

本文件是 `prd-for-ai` 仓库的长期实施主控文件。

后续每次开始执行前，必须先读取本文件，确认当前阶段、当前模块、待办任务和验收标准，再继续执行。

本文件优先级高于临时对话结论。若临时任务与本实施计划冲突，必须先更新本文件，再执行具体任务。

## 2. 强制执行原则

1. `IMPLEMENTATION_PLAN.md` 是唯一主控计划。
2. 每次开始任务前，必须先读取本文件。
3. 如果用户临时要求与本文件冲突，先更新本文件，再执行任务。
4. 不允许跳阶段；但允许将无法短期确认且不影响其他模块转译的事项记录为 deferred gap 后继续。
5. 不允许用新的模块清单替代阶段计划。
6. 模块清单只能作为阶段内的执行子任务。
7. 若发现本实施计划不符合当前真实进度，必须先修正实施计划，再继续执行。
8. 所有内容必须来源于历史 PRD、接口文档、截图、已确认结论或已存在知识库。
9. 允许跨文档、跨模块引用已确认事实。
10. 禁止无来源补流程、补页面、补字段、补状态、补文案。
11. 每完成一个能力块，必须同步更新本文件；单文件未形成能力块时，可只更新模块 `_index.md`。
12. 每个阶段完成后，必须执行 Stage Review，不得跳过。
13. Stage Review 结果只能是 `PASS`、`PARTIAL PASS` 或 `BLOCK`。
14. 未执行 Stage Review，或 Stage Review 未达到 `PASS` / 用户确认可带 deferred gap 继续，不得进入下一阶段。
15. `BLOCK` 时必须停止推进，输出阻塞点、影响范围、确认清单和下一步确认对象。
16. 涉及账户、卡、钱包、交易、资金处理的阶段，Stage Review 必须检查状态闭环、接口一致性、字段来源、失败分支和可追溯性。
17. 涉及资金处理时，必须确认通知 ID、业务 ID、请求 ID、结果流水、入账流水、幂等键、重试策略和异常责任分派；缺任一关键项时默认不得为 `PASS`，但用户明确确认短期无答案且允许继续时，可标记为 `deferred gap` 并以 `PARTIAL PASS` 进入后续转译。
18. Stage Review 完成后，必须同步更新本文件中的阶段状态和下一步。

---

## 3. Stage Review Gate 机制

### 3.1 触发时机

| 触发点 | 是否 Gate | 说明 |
|---|---|---|
| 单个文件完成 | 否 | 只更新文件状态或模块 `_index.md` |
| 单个能力块完成 | 否 | 如 Activation / PIN / Card Home |
| 一个阶段完成 | 是 | 如 Account / Security / Card / Wallet / Transaction |
| 发现资金、状态、接口冲突 | 是 | 立即进入 Gate 判断 |
| 涉及资金链路 | 是 | 必须重点检查可追溯性 |

### 3.2 Gate 结果

| 结果 | 含义 | 后续动作 |
|---|---|---|
| `PASS` | 阶段可进入下一阶段 | 更新实施计划，进入下一阶段 |
| `PARTIAL PASS` | 非阻塞部分可引用，遗留问题进入 gaps | 标注可用范围与限制；若用户确认可继续，则进入下一阶段 |
| `BLOCK` | 阶段不可继续 | 停止推进，输出阻塞项与确认清单 |

### 3.3 Gate 检查项

| 检查项 | 标准 |
|---|---|
| 状态闭环 | 状态有来源、有进入、有退出、有失败分支 |
| 流程闭环 | 主流程、异常流程、人工处理路径可闭合 |
| 接口一致 | 接口路径、字段、返回、错误码不存在未处理冲突 |
| 字段来源 | 关键字段来自原始 PRD、接口文档或已确认知识库 |
| 规则一致 | 不同文档之间没有未处理冲突 |
| 无脑补事实 | 文档缺失必须写 gaps，不得写成事实 |
| 资金可追溯 | 涉及资金时必须能串起通知、处理、结果、入账、对账；不能确认时必须记录 deferred gap |
| gaps 完整 | 未确认事项必须进入 `knowledge-gaps.md` 或阶段 review |
| 实施计划同步 | Gate 结果必须写回 `IMPLEMENTATION_PLAN.md` |

### 3.4 BLOCK 标准

命中任一项默认 `BLOCK`，除非用户确认可作为 deferred gap 后继续：

| 阻塞项 | 说明 |
|---|---|
| 资金路径不可追溯 | 缺通知 ID、请求 ID、结果流水、入账流水、幂等或重试 |
| 状态机不闭环 | 状态无法判断进入、退出或失败分支 |
| 关键接口路径冲突 | 无法判断研发应接哪个接口 |
| 关键字段缺失 | ID、amount、currency、status 等关键字段缺失 |
| 前后规则冲突 | 两个事实源规则不一致且未确认取舍 |
| 失败分支无法闭环 | 失败后无重试、告警、人工处理或最终状态 |
| 来源不足但写成事实 | 文档未确认内容被写入正文 |

---

## 11. 阶段实施路线表

| 阶段 | 名称 | 当前状态 | 目标 | 阶段产出 | 下一步 |
|---|---|---|---|---|---|
| 1 | Account 样板 | 已完成 | 固化知识库写法 | Login / Registration / Password Reset | 已完成 |
| 2 | 基础规则沉淀 | 部分完成 | 建立长期规则 | Writing Standard / Source Rules | 持续完善 |
| 3 | Security 标准化 | 已完成 | 统一认证事实源 | OTP / Email OTP / Passcode / BIO / Face Auth / API Reference | 已完成 |
| 4 | Card 批量推进 | PARTIAL PASS | 转译卡模块 | Application / Status & Fields / Home / Manage / Transaction | 遗留资金追踪项 deferred，继续后续阶段 |
| 5 | Wallet 批量推进 | 当前执行 | 转译钱包模块 | KYC / Send / Swap / Receive / Deposit | 开始 Wallet 知识库转译 |
| 6 | Transaction 统一层 | 未开始 | 统一交易状态 | Card / Wallet / Swap / History | Wallet 后执行 |
| 7 | Common / Integration | 未开始 | 抽公共能力 | DTC / AAI / WC / Error / FAQ | Transaction 后执行 |
| 8 | 全仓库回扫 | 未开始 | 去重复、补引用 | 字段 / 状态 / 来源 / gaps | 最后执行 |

---

## 12. 阶段内任务拆解

### 12.4 阶段 4：Card 批量推进（PARTIAL PASS）

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
| card-transaction-flow.md | 已完成但有 deferred gaps | 已同步 DTC 字段、通知去重基础、归集触发类型、transfer-to-wallet 字段、失败不重试、Wallet 交易 id 和 Wallet state 等确认结论；AIX 内部 ID、归集请求、Wallet 关联规则和对账链路暂时 deferred |
| stage-review.md | 已完成 | Card 阶段回扫已更新，结论为 `PARTIAL PASS`，允许继续后续转译 |
| transaction-flow-traceability-checklist.md | 已完成 | 已收敛为 deferred gaps 记录 |

### 12.5 阶段 5：Wallet 批量推进（当前执行）

| 子任务 | 状态 | 说明 |
|---|---|---|
| wallet/_index.md | Todo | 建立 Wallet 模块边界、能力清单与依赖关系 |
| wallet/kyc.md | Todo | 转译 Wallet KYC / DTC 钱包开户与前置条件 |
| wallet/balance.md | Todo | 转译钱包余额、币种、余额展示与查询接口 |
| wallet/deposit.md | Todo | 转译 Crypto / Fiat Deposit，含地址、白名单、风险拦截与通知边界 |
| wallet/receive.md | Todo | 转译 Receive / Deposit Address / Whitelist Address 相关能力 |
| wallet/send.md | Todo | 转译 Crypto Withdraw / Send 相关能力 |
| wallet/swap.md | Todo | 转译 Swap / OTC / Quote / Order 相关能力 |
| wallet/transaction-history.md | Todo | 转译 Wallet Search Balance History、交易详情、状态与展示字段 |
| wallet/stage-review.md | Todo | Wallet 阶段完成后执行 Stage Review |

---

## 17. 当前状态（同步修正）

| 模块 | 状态 | Gate 结果 | 说明 |
|---|---|---|---|
| Account | 已完成 | PASS | Login / Registration / Password Reset 已完成 |
| Security | 已完成 | PASS | Security 阶段全部收口 |
| Card / 页面与卡管能力 | 已完成 | PASS | Application / Home / Activation / PIN / Sensitive Info / Management 已完成 |
| Card / Transaction Flow | 已完成但留 deferred gaps | PARTIAL PASS | DTC 通知字段、交易 ID、触发类型、transfer-to-wallet 字段、失败不重试、Wallet 交易 id 和 Wallet state 已确认；AIX 内部追踪、Wallet 关联规则和对账链路 deferred |
| Card / Traceability Checklist | 已完成 | deferred gap 支撑材料 | 遗留问题已转入 `knowledge-gaps.md` |
| Wallet | 当前执行 | 未评审 | 开始 Wallet 批量推进 |

---

## 18. 下一步（同步更新）

当前执行点：

1. 暂不继续追 Card Transaction Flow 遗留问题；保留在 `knowledge-gaps.md`，状态为 `deferred`。
2. 开始 Wallet 阶段转译，优先建立 `knowledge-base/wallet/_index.md`。
3. Wallet 阶段可引用 Card Transaction Flow 已确认事实；遇到 deferred gap 时只能标注为未确认，不能补写事实。
4. Wallet 每完成一个能力块，更新对应文件和本实施计划。
5. Wallet 阶段完成后执行 Wallet Stage Review。

当前禁止事项：

- 不得把 AIX 内部交易 ID、归集请求 ID、Wallet 关联规则、Wallet relatedId、对账字段写成事实。
- 不得新增无来源状态、字段或接口。
- 不得把 Transaction 统一层提前混入 Wallet 阶段正文。
- 不得删除 Card Transaction Flow deferred gaps。
