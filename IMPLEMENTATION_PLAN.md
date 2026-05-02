# prd-for-ai 实施计划

版本：v4.2  
状态：全仓库回扫 PARTIAL PASS，进入补材料与精修阶段  
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
19. 未上线且需重做的功能不得作为 active 功能事实归档；只能标记为 `deferred` 或 `redesign-required`。
20. DTC / AAI 是外部供应商依赖，不是 AIX 内部系统；知识库只记录 AIX 实际使用到的外部依赖边界，不维护供应商内部系统逻辑或完整系统说明书。

---

## 3. Stage Review Gate 机制

### 3.1 触发时机

| 触发点 | 是否 Gate | 说明 |
|---|---|---|
| 单个文件完成 | 否 | 只更新文件状态或模块 `_index.md` |
| 单个能力块完成 | 否 | 如 Activation / PIN / Card Home |
| 一个阶段完成 | 是 | 如 Account / Security / Card / Wallet / Transaction / Common |
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
| 功能上线状态 | 未上线 / 需重做功能必须标记 deferred，不能写成 active 事实 |
| 外部依赖边界 | DTC / AAI 等供应商系统只能记录 AIX 依赖边界，不维护其内部逻辑 |
| gaps 完整 | 未确认事项必须进入 `knowledge-gaps.md` 或阶段 review |
| 实施计划同步 | Gate 结果必须写回 `IMPLEMENTATION_PLAN.md` |

---

## 11. 阶段实施路线表

| 阶段 | 名称 | 当前状态 | 目标 | 阶段产出 | 下一步 |
|---|---|---|---|---|---|
| 1 | Account 样板 | 已完成 | 固化知识库写法 | Login / Registration / Password Reset | 已完成 |
| 2 | 基础规则沉淀 | 部分完成 | 建立长期规则 | Writing Standard / Source Rules | 持续完善 |
| 3 | Security 标准化 | 已完成 | 统一认证事实源 | OTP / Email OTP / Passcode / BIO / Face Auth / API Reference | 已完成 |
| 4 | Card 批量推进 | PARTIAL PASS | 转译卡模块 | Application / Status & Fields / Home / Manage / Transaction | 遗留资金追踪项 deferred |
| 5 | Wallet 批量推进 | PARTIAL PASS | 转译钱包模块 | KYC / Balance / Deposit / Receive / Transaction History | Wallet 细节继续待补 |
| 6 | Transaction 统一层 | PARTIAL PASS | 统一交易状态 | Card / Wallet / History / Detail | 待补项继续保留 |
| 7 | Common / Integration | PARTIAL PASS | 抽公共能力与外部依赖边界 | DTC Dependency / AAI Dependency / WC / Error / FAQ / Notification | 待补项继续保留 |
| 8 | 全仓库回扫 | PARTIAL PASS | 去重复、补引用、核对状态 | 字段 / 状态 / 来源 / gaps / index | 已生成最终回扫记录 |
| 9 | 补材料与精修 | 当前执行 | 按 P0/P1/P2 回填真实材料 | Deposit / DTC Wallet / AAI / Errors / FAQ | 优先补 GTR / WalletConnect |

---

## 12. 阶段内任务拆解

### 12.7 阶段 7：Common / Integration（PARTIAL PASS）

| 子任务 | 状态 | 说明 |
|---|---|---|
| common/_index.md | 已完成 | 已建立公共能力索引与外部依赖边界 |
| common/dtc.md | 已完成基础版 | 已改为 DTC Dependency 外部依赖边界；不维护 DTC 内部逻辑 |
| common/aai.md | 已完成基础版 | 已改为 AAI Dependency 外部依赖边界；不维护 AAI 内部逻辑 |
| common/walletconnect.md | 已完成基础版 | 已汇总 WalletConnect 入金公共边界；流程、Declare、白名单、风控待补 |
| common/errors.md | 已完成基础版 | 已汇总错误处理、告警、人工处理边界；错误码与文案待补 |
| common/notification.md | 已完成基础版 | 已汇总 push / 站内信通知边界；Deposit / WC 通知待补 |
| common/faq.md | 已完成基础版 | 已建立 FAQ 分类和答复来源边界；原文待补 |
| common/stage-review.md | 已完成 | Common / Integration 阶段回扫已更新，结论为 `PARTIAL PASS` |

### 12.8 阶段 8：全仓库回扫（PARTIAL PASS）

| 子任务 | 状态 | 说明 |
|---|---|---|
| 全仓库文件清单回扫 | 已完成 | 核心模块文件已齐全 |
| Frontmatter 回扫 | 已完成基础检查 | 关键文件已具备 frontmatter，后续可继续自动化精查 |
| Stage Review 回扫 | 已完成 | 各阶段 Gate 结果已同步 |
| Deferred gaps 回扫 | 已完成 | deferred gaps 未被写成事实 |
| Active / deferred 功能状态回扫 | 已完成 | Deposit active；Send / Swap deferred |
| 引用与重复内容回扫 | 已完成基础检查 | 关键重复风险已隔离 |
| 最终回扫记录 | 已完成 | `knowledge-base/changelog/final-repository-review.md` 已生成并更新到 v1.1 |

### 12.9 阶段 9：补材料与精修（当前执行）

| 优先级 | 子任务 | 状态 | 目标文件 |
|---|---|---|---|
| P0 | GTR / WalletConnect 入金流程、字段、状态、风控、通知 | 当前最高优先级 | wallet/deposit、common/walletconnect、common/notification、common/errors |
| P0 | AIX 实际依赖的 DTC Wallet 字段、activityType、relatedId 规则 | 待补 | wallet/transaction-history、transaction/status-model、common/dtc |
| P0 | Card / Wallet 资金追踪 ID 关联规则 | 待补 | card/card-transaction-flow、changelog/knowledge-gaps |
| P1 | AIX 实际依赖的 Wallet KYC / AAI 状态、接口、失败处理 | 待补 | wallet/kyc、common/aai |
| P1 | 通用错误码、错误页、告警和人工补偿入口 | 待补 | common/errors |
| P2 | FAQ 原文和客服口径 | 待补 | common/faq |

---

## 17. 当前状态（同步修正）

| 模块 | 状态 | Gate 结果 | 说明 |
|---|---|---|---|
| Account | 已完成 | PASS | Login / Registration / Password Reset 已完成 |
| Security | 已完成 | PASS | Security 阶段全部收口 |
| Card / 页面与卡管能力 | 已完成 | PASS | Application / Home / Activation / PIN / Sensitive Info / Management 已完成 |
| Card / Transaction Flow | 已完成但留 deferred gaps | PARTIAL PASS | 资金追踪部分 deferred |
| Wallet | 已完成基础版 | PARTIAL PASS | Deposit active；Send / Swap deferred；细节待补 |
| Transaction | 已完成基础版 | PARTIAL PASS | 已建立状态、历史、详情边界；待补项继续保留 |
| Common / Integration | 已完成基础版 | PARTIAL PASS | 已建立公共能力与外部依赖边界；待补项继续保留 |
| 全仓库回扫 | 已完成基础版 | PARTIAL PASS | 状态一致，可进入补材料与精修 |
| 补材料与精修 | 当前执行 | 未评审 | 优先补 GTR / WalletConnect |

---

## 18. 下一步（同步更新）

当前执行点：

1. 进入补材料与精修阶段。
2. 下一步优先补 GTR / WalletConnect 入金流程、字段、状态、风控、通知。
3. 目标文件：`wallet/deposit.md`、`common/walletconnect.md`、`common/notification.md`、`common/errors.md`。
4. 如果缺少真实 PRD / 接口 / 截图，不得补写事实，只能列待确认问题。

当前禁止事项：

- 不得把 Send / Swap 写成当前已上线能力。
- 不得把 Wallet Deposit / Receive 待补状态脑补成完整状态机。
- 不得把 AIX 内部交易 ID、归集请求 ID、Wallet 关联规则、Wallet relatedId、对账字段写成事实。
- 不得把 `D-REQUEST-ID` 写成幂等键。
- 不得把 DTC / AAI 写成 AIX 自有系统或供应商系统说明书。
- 不得新增无来源状态、字段或接口。
- 不得删除 Card Transaction Flow deferred gaps。
