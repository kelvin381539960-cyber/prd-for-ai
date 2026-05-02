# prd-for-ai 实施计划

版本：v4.1  
状态：Common / Integration 阶段 PARTIAL PASS，全仓库回扫当前执行  
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
| 未上线功能写成 active | 未上线或需重做功能被归档为当前生效能力 |

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
| 7 | Common / Integration | PARTIAL PASS | 抽公共能力 | DTC / AAI / WC / Error / FAQ / Notification | 待补项继续保留 |
| 8 | 全仓库回扫 | 当前执行 | 去重复、补引用、核对状态 | 字段 / 状态 / 来源 / gaps / index | 创建全仓库回扫记录 |

---

## 12. 阶段内任务拆解

### 12.4 阶段 4：Card 批量推进（PARTIAL PASS）

| 子任务 | 状态 | 说明 |
|---|---|---|
| card/_index.md | 已完成 | Card 模块边界与功能清单已收口 |
| application.md | 已完成 | 申卡流程、资格、费用、币种、地区、卡类型、自动扣款、接口依赖已收口；缺口已记录 |
| card-status-and-fields.md | 已完成 | 卡状态、字段、接口路径、操作限制缺口已收口 |
| card-home.md | 已完成 | 卡首页、展示、入口、交易摘要和 FAQ 已收口 |
| activation.md | 已完成 | 实体卡激活流程已收口 |
| pin.md | 已完成 | PIN 相关能力已收口 |
| sensitive-info.md | 已完成 | 卡信息安全查看流程已收口 |
| card-management.md | 已完成 | 卡管理操作、状态边界、接口依赖与失败处理已收口 |
| card-transaction-flow.md | 已完成但有 deferred gaps | DTC 字段、归集触发类型、transfer-to-wallet 字段、Wallet 交易 id 和 Wallet state 已确认；AIX 内部 ID、归集请求、Wallet 关联规则和对账链路 deferred |
| stage-review.md | 已完成 | Card 阶段回扫已更新，结论为 `PARTIAL PASS` |
| transaction-flow-traceability-checklist.md | 已完成 | 已收敛为 deferred gaps 记录 |

### 12.5 阶段 5：Wallet 批量推进（PARTIAL PASS）

| 子任务 | 状态 | 说明 |
|---|---|---|
| wallet/_index.md | 已完成 | 已建立 Wallet 模块边界；Deposit active；Send / Swap deferred |
| wallet/transaction-history.md | 已完成基础版 | 已建立 Wallet 交易记录、详情、state 基础事实源；字段待补 |
| wallet/balance.md | 已完成基础版 | 已建立钱包余额基础文件；接口字段待补 |
| wallet/deposit.md | 已完成基础版 | Deposit 存在，包含 GTR 和 WalletConnect；需继续补细节 |
| wallet/receive.md | 已完成基础版 | 已建立 Receive 基础占位；与 Deposit 子路径关系待确认 |
| wallet/send.md | deferred | 因合规原因未上线，不作为 active 功能事实源 |
| wallet/kyc.md | 已完成基础版 | Wallet KYC / 开户前置边界已建立，完整流程待补 |
| wallet/swap.md | deferred | 因合规原因未上线且需重做；新方案确认后再转译 |
| wallet/stage-review.md | 已完成 | Wallet 阶段回扫已更新，结论为 `PARTIAL PASS` |

### 12.6 阶段 6：Transaction 统一层（PARTIAL PASS）

| 子任务 | 状态 | 说明 |
|---|---|---|
| transaction/_index.md | 已完成 | 已建立 Transaction 统一层边界、状态来源和引用规则 |
| transaction/status-model.md | 已完成 | 已汇总 Card / Wallet 已确认状态，未脑补完整状态机 |
| transaction/history.md | 已完成 | 已汇总 Card History / Wallet Transaction History 的边界 |
| transaction/detail.md | 已完成 | 已汇总 Card / Wallet 交易详情字段边界 |
| transaction/stage-review.md | 已完成 | Transaction 阶段回扫已更新，结论为 `PARTIAL PASS` |

### 12.7 阶段 7：Common / Integration（PARTIAL PASS）

| 子任务 | 状态 | 说明 |
|---|---|---|
| common/_index.md | 已完成 | 已建立公共能力索引与边界 |
| common/dtc.md | 已完成基础版 | 已汇总 DTC 请求头、Webhook、接口边界；错误码待补 |
| common/notification.md | 已完成基础版 | 已汇总 push / 站内信通知边界；Deposit / WC 通知待补 |
| common/walletconnect.md | 已完成基础版 | 已汇总 WalletConnect 入金公共边界；流程、Declare、白名单、风控待补 |
| common/errors.md | 已完成基础版 | 已汇总错误处理、告警、人工处理边界；错误码与文案待补 |
| common/aai.md | 已完成基础版 | 已汇总 AAI / KYC / OCR / Liveness / Face Auth 边界；接口和状态待补 |
| common/faq.md | 已完成基础版 | 已建立 FAQ 分类和答复来源边界；原文待补 |
| common/stage-review.md | 已完成 | Common / Integration 阶段回扫已更新，结论为 `PARTIAL PASS` |

### 12.8 阶段 8：全仓库回扫（当前执行）

| 子任务 | 状态 | 说明 |
|---|---|---|
| 全仓库文件清单回扫 | Todo | 检查模块文件是否齐全、状态是否一致 |
| Frontmatter 回扫 | Todo | 检查 module / feature / version / status / source_doc / depends_on |
| Stage Review 回扫 | Todo | 检查各阶段 Gate 结果是否同步 |
| Deferred gaps 回扫 | Todo | 检查 deferred gaps 是否被误写为事实 |
| Active / deferred 功能状态回扫 | Todo | 检查 Send / Swap 等未上线功能是否仍为 deferred |
| 引用与重复内容回扫 | Todo | 检查跨文档重复和错误引用 |
| 最终回扫记录 | Todo | 生成全仓库回扫结论 |

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
| Common / Integration | 已完成基础版 | PARTIAL PASS | 已建立公共能力边界；待补项继续保留 |
| 全仓库回扫 | 当前执行 | 未评审 | 检查文件完整性、状态一致性、引用和 gaps |

---

## 18. 下一步（同步更新）

当前执行点：

1. 执行全仓库回扫，检查文件完整性、frontmatter、Stage Review、deferred gaps、active/deferred 状态和引用关系。
2. 全仓库回扫可引用各模块 Stage Review 结论，但不能补写 deferred gaps。
3. 重点检查 Send / Swap 是否仍为 deferred；Deposit 是否 active 且限定 GTR / WalletConnect；Card / Wallet 资金追踪缺口是否仍在 gaps 中。
4. 生成最终回扫记录。

当前禁止事项：

- 不得把 Send / Swap 写成当前已上线能力。
- 不得把 Wallet Deposit / Receive 待补状态脑补成完整状态机。
- 不得把 AIX 内部交易 ID、归集请求 ID、Wallet 关联规则、Wallet relatedId、对账字段写成事实。
- 不得把 `D-REQUEST-ID` 写成幂等键。
- 不得新增无来源状态、字段或接口。
- 不得删除 Card Transaction Flow deferred gaps。
