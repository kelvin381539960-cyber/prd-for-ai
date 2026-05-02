# prd-for-ai 实施计划

版本：v4.6  
状态：补材料与精修阶段阶段性 PARTIAL PASS；KYC 已独立，Wallet Transaction History 已合并至 Transaction History  
适用仓库：`prd-for-ai`  
更新时间：2026-05-02

## 1. 文档定位

本文件是 `prd-for-ai` 仓库的长期实施主控文件。后续每次开始执行前，必须先读取本文件，确认当前阶段、当前模块、执行规则和验收标准，再继续执行。

本文件优先级高于临时对话结论。若临时任务与本实施计划冲突，必须先更新本实施计划，再执行具体任务。

待确认事项的唯一事实源为：

`knowledge-base/changelog/knowledge-gaps.md`

本文件不再维护另一套待确认清单。

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
10. 涉及资金处理时，必须确认通知 ID、业务 ID、请求 ID、结果流水、入账流水、幂等键、重试策略和异常责任分派；不能确认时必须记录到 `knowledge-base/changelog/knowledge-gaps.md` 的 `ALL-GAP-XXX` 总表。
11. 未上线且需重做的功能不得作为 active 功能事实归档；只能标记为 `deferred` 或 `redesign-required`。
12. DTC / AAI 是外部供应商依赖，不是 AIX 内部系统；知识库只记录与 AIX 系统设计有关的外部依赖边界，不维护供应商内部逻辑、完整接口说明书、完整错误码表或与 AIX 无关的供应商字段。
13. 所有模块禁止单独维护 checklist / TODO / gaps 表；功能正文只允许写已确认事实，或引用 `ALL-GAP-XXX` 编号。
14. Wallet 目录只承接钱包产品能力；KYC 主事实源在 `knowledge-base/kyc/`；交易历史主事实源在 `knowledge-base/transaction/`。

---

## 3. 当前知识库目录边界

| 目录 | 定位 | 当前规则 |
|---|---|---|
| `wallet/` | 钱包产品能力 | 只保留 Balance / Deposit / Receive / Send；KYC 与 Transaction History 仅保留兼容入口 |
| `transaction/` | 跨 Card / Wallet / Deposit 的交易统一层 | 维护 status-model、history、detail、reconciliation |
| `kyc/` | KYC / 业务准入能力 | 维护 wallet-kyc；AAI 仍保留在 common/aai 作为外部依赖 |
| `common/` | 公共能力和外部依赖边界 | 维护 dtc、aai、walletconnect、notification、errors、faq |
| `changelog/` | 变更、回扫、唯一待确认表 | `knowledge-gaps.md` 是唯一 ALL-GAP 总表 |

---

## 4. Stage Review Gate 机制

| 检查项 | 标准 |
|---|---|
| 状态闭环 | 状态有来源、有进入、有退出、有失败分支 |
| 流程闭环 | 主流程、异常流程、人工处理路径可闭合 |
| 接口一致 | 接口路径、字段、返回、错误码不存在未处理冲突 |
| 字段来源 | 关键字段来自原始 PRD、接口文档或已确认知识库 |
| 无脑补事实 | 文档缺失必须写入 ALL-GAP 总表，不得写成事实 |
| 资金可追溯 | 涉及资金时必须能串起通知、处理、结果、入账、对账；不能确认时必须记录 ALL-GAP |
| 功能上线状态 | 未上线 / 需重做功能必须标记 deferred，不能写成 active 事实 |
| 外部依赖边界 | DTC / AAI 等供应商系统只能记录影响 AIX 系统设计的依赖边界，不维护其内部逻辑或完整说明书 |
| 待确认唯一源 | 所有待确认项必须集中到 `knowledge-base/changelog/knowledge-gaps.md`，不得分散在模块文档 |
| 目录边界 | KYC 不挂在 Wallet；Wallet Transaction History 主事实归 Transaction；Wallet 只保留钱包产品能力 |
| 实施计划同步 | Gate 结果必须写回 `IMPLEMENTATION_PLAN.md`，但不重复维护问题清单 |

---

## 5. 阶段实施路线表

| 阶段 | 名称 | 当前状态 | 目标 | 阶段产出 | 下一步 |
|---|---|---|---|---|---|
| 1 | Account 样板 | 已完成 | 固化知识库写法 | Login / Registration / Password Reset | 已完成 |
| 2 | 基础规则沉淀 | 部分完成 | 建立长期规则 | Writing Standard / Source Rules | 持续完善 |
| 3 | Security 标准化 | 已完成 | 统一认证事实源 | OTP / Email OTP / Passcode / BIO / Face Auth / API Reference | 已完成 |
| 4 | Card 批量推进 | PARTIAL PASS | 转译卡模块 | Application / Status & Fields / Home / Manage / Transaction | 遗留资金追踪项已集中至 ALL-GAP |
| 5 | Wallet 批量推进 | PARTIAL PASS | 转译钱包模块 | Balance / Deposit / Receive / Send | KYC 与 Transaction History 已迁出 |
| 6 | Transaction 统一层 | PARTIAL PASS | 统一交易状态、历史、详情、对账 | Status / History / Detail / Reconciliation | P0 对账缺口继续进 ALL-GAP |
| 7 | KYC 独立层 | PARTIAL PASS | 沉淀 KYC / 准入边界 | wallet-kyc | 待补 Card KYC / Wallet KYC 关系 |
| 8 | Common / Integration | PARTIAL PASS | 抽公共能力与外部依赖边界 | DTC / AAI / WC / Error / FAQ / Notification | DTC / AAI 已收窄为系统设计边界 |
| 9 | 全仓库回扫 | PARTIAL PASS | 去重复、补引用、核对状态 | 字段 / 状态 / 来源 / gaps / index | 已生成最终回扫记录 |
| 10 | 补材料与精修 | 阶段性 PARTIAL PASS | 按 P0/P1/P2 回填真实材料 | Deposit / WalletConnect / Errors / FAQ / ALL-GAP / 目录结构已阶段性回填 | 继续清理分散 gaps，并优先收敛 P0 ALL-GAP |

---

## 6. 阶段 10：补材料与精修进度

| 子任务 | 状态 | 已完成 / 当前边界 | 目标文件 |
|---|---|---|---|
| DTC Crypto Deposit 外部依赖 | 已完成阶段性回填并收窄 | 只保留影响 AIX Deposit、Wallet History、通知、状态、错误、对账的设计边界 | wallet/deposit、common/dtc、common/walletconnect、common/errors |
| AAI 外部依赖 | 已完成边界收窄 | 只保留影响 AIX KYC 准入、页面状态、通知、错误、人工处理的结果边界 | common/aai、kyc/wallet-kyc |
| KYC 独立目录 | 已完成阶段性迁移 | 新建 `kyc/_index.md`、`kyc/wallet-kyc.md`；`wallet/kyc.md` 改为 moved notice | kyc、wallet/kyc |
| Transaction History 合并 | 已完成阶段性迁移 | `wallet/transaction-history.md` 合并至 `transaction/history.md`；旧文件改为 moved notice | transaction/history、wallet/transaction-history |
| Transaction Reconciliation | 已完成阶段性新增 | 新增资金追踪 / 对账边界文件，只引用 ALL-GAP | transaction/reconciliation |
| Deposit / GTR / WalletConnect 流程 | 已完成阶段性回填 | GTR / Exchange 地址充值、WalletConnect 主流程、自动加白、异常分流、结果状态图已补 | wallet/deposit、common/walletconnect、common/errors |
| Deposit Notification | 已完成阶段性回填 | Deposit success、Deposit under review / Risk Withheld 通知规则、模板参数和跳转边界 | common/notification、wallet/deposit |
| Wallet Search Balance History | 已完成阶段性回填 | endpoint、查询条件边界、`activityType` / `relatedId` / `state` / `time` | transaction/history、wallet/balance |
| ActivityType | 已完成阶段性回填 | `FIAT_DEPOSIT=6`、`CRYPTO_DEPOSIT=10`、`DTC_WALLET=13`、`CARD_PAYMENT_REFUND=20`，但不等同产品路径 | transaction/history、transaction/status-model、common/dtc |
| FAQ / 客服口径 | 已完成基础回填 | 已按 FAQ Excel 原文落库，不自行编造新增 | common/faq |
| ALL-GAP 总表 | 已完成阶段性收口 | 所有模块不确定项统一进入 `knowledge-base/changelog/knowledge-gaps.md`，已加 P0 / P1 / P2 优先级 | changelog/knowledge-gaps |
| 分散 gap 清理 | 当前执行 | 后续模块只引用 ALL-GAP 编号，不再维护独立 checklist | wallet、card、transaction、common、kyc |
| P0 gap 收敛 | 待执行 | 资金、对账、状态闭环、用户资产可见性优先确认 | changelog/knowledge-gaps |

---

## 7. 当前已确认事实

| 事实 | 来源 | 使用限制 |
|---|---|---|
| Deposit 包含 GTR / Exchange 地址充值与 WalletConnect / Self-custodial Wallet 充值 | AIX Wallet PRD / 用户确认 | 两条路径不默认共用字段、白名单、异常或结果页 |
| GTR 当前支持 Binance，列表可配置 | AIX Wallet PRD | 不得写成所有 Exchange 均支持 |
| GTR 钱包充值自动交易报备，不需要交易声明，也不用校验地址白名单 | AIX Wallet PRD | 不等同 WalletConnect 白名单逻辑 |
| WalletConnect Approved 后 DTC 自动 add whitelist | AIX Wallet PRD / DTC WalletConnect Archive | 只作为 WC 路径规则 |
| WalletConnect AIX 对客授权有效期按 1 天 | 用户确认 2026-05-02 | DTC 7 天为其内部逻辑，不作为 AIX 对客有效期 |
| Risk Withheld 不触发充值结果页 | 用户确认 2026-05-02 | 用户查询交易详情时状态为 under review |
| Refunded 没有 AIX 对客结果页 | 用户确认 2026-05-02 | 不补 Refunded 结果页 |
| payment_info success 是信息流成功，会同步触发资金流转账 | 用户确认 2026-05-02 | 理论立即可用，实际可能有很短延迟 |
| Search Balance History endpoint 为 `[GET] /openapi/v1/wallet/balance/history/search` | DTC Wallet OpenAPI / 4.2.4 | 不维护完整接口说明书；只作为 AIX Wallet History 来源 |
| `FIAT_DEPOSIT=6` | DTC Wallet OpenAPI / Appendix ActivityType | 不得写死为 GTR；见 ALL-GAP-001 |
| `CRYPTO_DEPOSIT=10` | DTC Wallet OpenAPI / Appendix ActivityType | 不得写死为 WalletConnect；见 ALL-GAP-002 |
| Deposit success 通知 | Notification PRD / Deposit row | 不代表所有 Deposit 子路径状态机闭环 |
| Deposit under review / Risk Withheld 通知 | Notification PRD / Deposit row | 不代表 Declare / Travel Rule 流程闭环 |
| AAI / KYC 外部依赖 | 用户确认 / common/aai | 只保留影响 AIX 准入、页面状态、通知、错误、人工处理的结果边界 |

---

## 8. 当前状态

| 模块 | 状态 | Gate 结果 | 说明 |
|---|---|---|---|
| Account | 已完成 | PASS | Login / Registration / Password Reset 已完成；少量文案 / 截图结构缺口进 ALL-GAP |
| Security | 已完成 | PASS | Security 阶段全部收口 |
| Card / 页面与卡管能力 | 已完成 | PASS | Application / Home / Activation / PIN / Sensitive Info / Management 已完成 |
| Card / Transaction Flow | 已完成但留 deferred gaps | PARTIAL PASS | 资金追踪部分集中至 ALL-GAP P0 |
| Wallet | 已完成基础版 + Deposit 深度回填 + 目录边界调整 | PARTIAL PASS | Deposit active；Send / Swap deferred；KYC / History 已迁出 |
| Transaction | 已完成基础版 + History 合并 + Reconciliation 新增 | PARTIAL PASS | Wallet History 主事实已合并，资金追踪边界进 reconciliation / ALL-GAP |
| KYC | 已独立 | PARTIAL PASS | Wallet KYC 已迁移；Card KYC / Wallet KYC 关系待 ALL-GAP 收敛 |
| Common / Integration | 已完成基础版 + 部分真实材料回填 | PARTIAL PASS | DTC / AAI 已收窄为系统设计边界；Notification / Errors / WalletConnect 已补真实材料 |
| 全仓库回扫 | 已完成基础版 | PARTIAL PASS | 状态一致，可继续补材料与精修 |
| 补材料与精修 | 当前执行 | PARTIAL PASS | 当前重点：清理分散 gaps、统一引用 ALL-GAP、优先确认 P0 |

---

## 9. 下一步

当前执行点：

1. 回扫重点模块文档，移除分散的待确认表 / TODO / gaps，仅保留 ALL-GAP 编号引用。
2. 优先清理：wallet/deposit、common/errors、common/walletconnect、transaction/detail、card/transaction-flow、stage-review 文件。
3. 更新 final-repository-review，反映 KYC 独立、History 合并、Reconciliation 新增。
4. 后续按 ALL-GAP 优先级收敛：先 P0，再 P1，最后 P2。
5. 外部依赖继续保持“只保留 AIX 系统设计相关内容”的原则。

当前禁止事项：

- 不得把 Send / Swap 写成当前已上线能力。
- 不得把 `FIAT_DEPOSIT` 写死为 GTR。
- 不得把 `CRYPTO_DEPOSIT` 写死为 WalletConnect。
- 不得把 Deposit success 写死为 Wallet `COMPLETED`。
- 不得把 Risk Withheld 写死为 Wallet `REJECTED` / `PENDING` / `PROCESSING`。
- 不得把 Wallet `relatedId` 与 Card / GTR / WC 强行关联。
- 不得把 DTC / AAI 写成 AIX 自有系统或供应商系统说明书。
- 不得维护与 AIX 系统设计无关的供应商字段、错误码、接口说明或内部逻辑。
- 不得在任何模块文档单独维护 checklist / TODO / gaps 表。
- 不得新增无来源状态、字段、接口、文案或页面规则。
