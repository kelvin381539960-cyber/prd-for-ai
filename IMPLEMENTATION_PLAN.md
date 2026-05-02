# prd-for-ai 实施计划

版本：v4.3  
状态：补材料与精修阶段阶段性 PARTIAL PASS，继续补前端展示 / GTR / WalletConnect / KYC 细节  
适用仓库：`prd-for-ai`  
更新时间：2026-05-01

## 1. 文档定位

本文件是 `prd-for-ai` 仓库的长期实施主控文件。后续每次开始执行前，必须先读取本文件，确认当前阶段、当前模块、待办任务和验收标准，再继续执行。

本文件优先级高于临时对话结论。若临时任务与本实施计划冲突，必须先更新本实施计划，再执行具体任务。

## 2. 强制执行原则

1. `IMPLEMENTATION_PLAN.md` 是唯一主控计划。
2. 每次开始任务前，必须先读取本文件。
3. 如果用户临时要求与本文件冲突，先更新本文件，再执行任务。
4. 不允许跳阶段；但允许将无法短期确认且不影响其他模块转译的事项记录为 deferred gap 后继续。
5. 所有内容必须来源于历史 PRD、接口文档、截图、已确认结论或已存在知识库。
6. 禁止无来源补流程、补页面、补字段、补状态、补文案。
7. 每完成一个能力块，必须同步更新本文件；阶段完成后必须执行 Stage Review。
8. Stage Review 结果只能是 `PASS`、`PARTIAL PASS` 或 `BLOCK`。
9. 涉及账户、卡、钱包、交易、资金处理的阶段，Stage Review 必须检查状态闭环、接口一致性、字段来源、失败分支和可追溯性。
10. 涉及资金处理时，必须确认通知 ID、业务 ID、请求 ID、结果流水、入账流水、幂等键、重试策略和异常责任分派；不能确认时必须记录 deferred gap。
11. 未上线且需重做的功能不得作为 active 功能事实归档；只能标记为 `deferred` 或 `redesign-required`。
12. DTC / AAI 是外部供应商依赖，不是 AIX 内部系统；知识库只记录 AIX 实际使用到的外部依赖边界，不维护供应商内部系统逻辑或完整系统说明书。

---

## 3. Stage Review Gate 机制

| 检查项 | 标准 |
|---|---|
| 状态闭环 | 状态有来源、有进入、有退出、有失败分支 |
| 流程闭环 | 主流程、异常流程、人工处理路径可闭合 |
| 接口一致 | 接口路径、字段、返回、错误码不存在未处理冲突 |
| 字段来源 | 关键字段来自原始 PRD、接口文档或已确认知识库 |
| 无脑补事实 | 文档缺失必须写 gaps，不得写成事实 |
| 资金可追溯 | 涉及资金时必须能串起通知、处理、结果、入账、对账；不能确认时必须记录 deferred gap |
| 功能上线状态 | 未上线 / 需重做功能必须标记 deferred，不能写成 active 事实 |
| 外部依赖边界 | DTC / AAI 等供应商系统只能记录 AIX 依赖边界，不维护其内部逻辑 |
| 实施计划同步 | Gate 结果必须写回 `IMPLEMENTATION_PLAN.md` |

---

## 4. 阶段实施路线表

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
| 9 | 补材料与精修 | 阶段性 PARTIAL PASS | 按 P0/P1/P2 回填真实材料 | Deposit / Wallet History / DTC / Notification / Errors 已阶段性回填 | 继续补前端展示、GTR / WC 产品流程、KYC / AAI |

---

## 5. 阶段 9：补材料与精修进度

| 子任务 | 状态 | 已完成 / 当前边界 | 目标文件 |
|---|---|---|---|
| DTC Crypto Deposit 外部依赖 | 已完成阶段性回填 | whitelisting / deposit / withdrawal、senderAddress、destinationAddress、Risk Withheld、success | wallet/deposit、common/dtc、common/walletconnect、common/errors |
| Deposit Notification | 已完成阶段性回填 | Deposit success、Deposit under review / Risk Withheld 通知规则、模板参数和跳转边界 | common/notification、wallet/deposit |
| Wallet Search Balance History | 已完成阶段性回填 | endpoint、查询条件边界、`activityType` / `relatedId` / `state` / `time` | wallet/transaction-history、wallet/balance、transaction/history |
| ActivityType | 已完成阶段性回填 | `FIAT_DEPOSIT=6`、`CRYPTO_DEPOSIT=10`、`DTC_WALLET=13`、`CARD_PAYMENT_REFUND=20` | wallet/transaction-history、wallet/balance、transaction/status-model、transaction/history、transaction/detail、common/dtc |
| Transaction 统一层同步 | 已完成阶段性回填 | Deposit History / Deposit Detail / Risk Withheld / success 边界已同步 | transaction/status-model、transaction/history、transaction/detail |
| 阶段性回扫 | 已完成 | `knowledge-base/changelog/refinement-stage-review.md` 已生成，结论 `PARTIAL PASS` | changelog/refinement-stage-review |
| GTR 产品流程 | 待补 | GTR 是否使用 `FIAT_DEPOSIT`、页面入口、状态、风控、通知覆盖待确认 | wallet/deposit、transaction/history |
| WalletConnect 产品流程 | 待补 | WC 是否使用 `CRYPTO_DEPOSIT`、senderAddress 获取、SDK / 页面流程、状态展示待确认 | wallet/deposit、common/walletconnect |
| Declare / Travel Rule | 待补 | 触发条件、用户路径、通知 / 状态影响待确认 | wallet/deposit、common/walletconnect、common/errors |
| Wallet KYC / AAI | 待补 | AIX 实际依赖的 KYC 状态、OCR / Liveness / 失败处理待补 | wallet/kyc、common/aai |
| FAQ / 客服口径 | 待补 | GTR / WC / Risk Withheld / Deposit success 等客服口径待补 | common/faq |

---

## 6. 当前已确认事实

| 事实 | 来源 | 使用限制 |
|---|---|---|
| Crypto business includes whitelisting, deposit, and withdrawal | DTC Wallet OpenAPI / 3.4 Crypto Deposit | 仅作为 DTC 外部依赖边界，不等同完整 AIX 产品流程 |
| Crypto 充值涉及 senderAddress 和 destinationAddress | DTC Wallet OpenAPI / 3.4 Crypto Deposit | WalletConnect 如何获取 senderAddress 待补 |
| destinationAddress 由 DTC 自动分配 | DTC Wallet OpenAPI / 3.4 Crypto Deposit | AIX 展示、复制、二维码待补 |
| senderAddress 需要 whitelist 并 enable | DTC Wallet OpenAPI / 3.4 Crypto Deposit | GTR / WC 是否全部适用仍待确认 |
| 未加白进入 `status=102 Risk Withheld` | DTC Wallet OpenAPI / 3.4 Crypto Deposit | 不等同 Wallet `REJECTED` / `PENDING` / `PROCESSING` |
| 加白成功后自动变为 success | DTC Wallet OpenAPI / 3.4 Crypto Deposit | 不等同 Wallet `COMPLETED`；余额可见时点待补 |
| Search Balance History endpoint 为 `[GET] /openapi/v1/wallet/balance/history/search` | DTC Wallet OpenAPI / 4.2.4 | 完整响应字段、分页和前端筛选待补 |
| `FIAT_DEPOSIT=6` | DTC Wallet OpenAPI / Appendix ActivityType | 不得写死为 GTR |
| `CRYPTO_DEPOSIT=10` | DTC Wallet OpenAPI / Appendix ActivityType | 不得写死为 WalletConnect |
| `DTC_WALLET=13` | DTC Wallet OpenAPI / Appendix ActivityType | 仅作为分类来源 |
| `CARD_PAYMENT_REFUND=20` | DTC Wallet OpenAPI / Appendix ActivityType | 与 Card 归集链路关联仍 deferred |
| Deposit success 通知 | Notification PRD / Deposit row | 不代表所有 Deposit 子路径状态机闭环 |
| Deposit under review / Risk Withheld 通知 | Notification PRD / Deposit row | 不代表 Declare / Travel Rule 流程闭环 |

---

## 7. 当前状态

| 模块 | 状态 | Gate 结果 | 说明 |
|---|---|---|---|
| Account | 已完成 | PASS | Login / Registration / Password Reset 已完成 |
| Security | 已完成 | PASS | Security 阶段全部收口 |
| Card / 页面与卡管能力 | 已完成 | PASS | Application / Home / Activation / PIN / Sensitive Info / Management 已完成 |
| Card / Transaction Flow | 已完成但留 deferred gaps | PARTIAL PASS | 资金追踪部分 deferred |
| Wallet | 已完成基础版 + 部分真实材料回填 | PARTIAL PASS | Deposit active；Send / Swap deferred；Crypto Deposit / ActivityType 已补，GTR / WC 细节待补 |
| Transaction | 已完成基础版 + 部分真实材料回填 | PARTIAL PASS | Wallet History / Detail / ActivityType / Risk Withheld 边界已补，状态映射待补 |
| Common / Integration | 已完成基础版 + 部分真实材料回填 | PARTIAL PASS | DTC / Notification / Errors / WalletConnect 已补部分真实材料，AAI 待补 |
| 全仓库回扫 | 已完成基础版 | PARTIAL PASS | 状态一致，可继续补材料与精修 |
| 补材料与精修 | 当前执行 | PARTIAL PASS | P0 Deposit / Wallet History 已阶段性回填，继续补 GTR / WC / KYC / FAQ |

---

## 8. 下一步

当前执行点：

1. 继续在历史 PRD / DTC 接口文档中补前端展示与业务流程。
2. 优先补：GTR / WalletConnect 页面入口、用户路径、状态展示、Declare / Travel Rule、余额可见时点、人工处理。
3. 其次补：Wallet KYC / AAI 外部依赖边界。
4. 最后补：FAQ / 客服口径。

当前禁止事项：

- 不得把 Send / Swap 写成当前已上线能力。
- 不得把 `FIAT_DEPOSIT` 写死为 GTR。
- 不得把 `CRYPTO_DEPOSIT` 写死为 WalletConnect。
- 不得把 Deposit success 写死为 Wallet `COMPLETED`。
- 不得把 Risk Withheld 写死为 Wallet `REJECTED` / `PENDING` / `PROCESSING`。
- 不得把 Wallet `relatedId` 与 Card / GTR / WC 强行关联。
- 不得把 DTC / AAI 写成 AIX 自有系统或供应商系统说明书。
- 不得新增无来源状态、字段、接口、文案或页面规则。
