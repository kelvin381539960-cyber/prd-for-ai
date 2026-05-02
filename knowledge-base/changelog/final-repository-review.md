---
module: changelog
feature: final-repository-review
version: "1.2"
status: active
source_doc: IMPLEMENTATION_PLAN.md；knowledge-base/changelog/refinement-stage-review.md；knowledge-base/card/stage-review.md；knowledge-base/wallet/stage-review.md；knowledge-base/transaction/stage-review.md；knowledge-base/common/stage-review.md；knowledge-base/common/dtc.md；knowledge-base/common/aai.md；knowledge-base/changelog/knowledge-gaps.md
source_section: IMPLEMENTATION_PLAN v4.3；补材料与精修阶段阶段性回扫；各阶段 Stage Review；deferred gaps
last_updated: 2026-05-01
owner: 吴忆锋
---

# 全仓库回扫记录

## 1. 回扫结论

本轮知识库转译已完成主链路阶段推进，并完成一轮补材料与精修阶段性回填。最终仓库状态仍为：`PARTIAL PASS`。

含义：

- Account 与 Security 已完成并通过。
- Card、Wallet、Transaction、Common / Integration 均已完成基础版沉淀，但保留 deferred / 待补项。
- Send / Swap 因合规原因未上线或需重做，保持 deferred。
- Deposit 为 active，范围限定为 GTR / WalletConnect。
- DTC / AAI 已修正为外部依赖边界，不作为供应商系统说明书维护。
- DTC Crypto Deposit、Deposit Notification、Wallet Search Balance History、ActivityType、Risk Withheld / success 已完成阶段性真实材料回填。
- Card / Wallet 资金追踪链路中未确认的 ID、relatedId、对账字段继续保留为 deferred gaps。
- 当前知识库可作为 AI 使用的基础事实层，但不能把待补项当作已确认规则。

## 2. 阶段状态总表

| 阶段 | Gate 结果 | 说明 |
|---|---|---|
| Account | PASS | Login / Registration / Password Reset 已完成 |
| Security | PASS | OTP / Email OTP / Passcode / BIO / Face Auth / API Reference 已收口 |
| Card | PARTIAL PASS | 页面与卡管能力完成；Transaction Flow 资金追踪留 deferred gaps |
| Wallet | PARTIAL PASS | Deposit active；Crypto Deposit / Search Balance History / ActivityType 已部分回填；GTR / WC 产品流程待补 |
| Transaction | PARTIAL PASS | 状态、历史、详情边界完成；ActivityType / Risk Withheld 已同步；状态映射和字段细节待补 |
| Common / Integration | PARTIAL PASS | DTC / AAI 外部依赖边界、Notification、WC、Errors、FAQ 边界完成；部分真实材料已回填 |
| 全仓库回扫 | PARTIAL PASS | 状态一致，可继续后续补材料与精修 |
| 补材料与精修 | PARTIAL PASS | P0 Deposit / Wallet History 已阶段性回填，未达到最终 PASS |

## 3. 本轮补材料已确认事实

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

## 4. 文件完整性检查

| 模块 | 核心文件 | 状态 |
|---|---|---|
| Card | `_index`、application、status、home、activation、pin、sensitive-info、management、transaction-flow、stage-review、traceability-checklist | 已完成基础版 |
| Wallet | `_index`、transaction-history、balance、deposit、receive、send、kyc、stage-review | 已完成基础版；Deposit / History / Balance 已部分真实材料回填；send deferred |
| Transaction | `_index`、status-model、history、detail、stage-review | 已完成基础版；状态 / 历史 / 详情已同步 ActivityType 与 Risk Withheld 边界 |
| Common | `_index`、dtc、notification、walletconnect、errors、aai、faq、stage-review | 已完成基础版；DTC / Notification / WalletConnect / Errors 已部分真实材料回填 |
| Changelog | knowledge-gaps、final-repository-review、refinement-stage-review | 已完成 |

## 5. Active / Deferred 状态检查

| 功能 | 当前状态 | 检查结果 |
|---|---|---|
| Deposit | active | 正确；范围限定 GTR / WalletConnect |
| Send / Withdraw | deferred | 正确；未上线，不作为 active 功能事实源 |
| Swap | deferred | 正确；未上线且需重做，不作为 active 功能事实源 |
| Card Transaction Flow | active + deferred gaps | 正确；基础事实可用，资金追踪链路不闭环 |
| WalletConnect | active 公共边界 | 正确；作为 Deposit 子路径边界，可引用 DTC Crypto Deposit 依赖；完整产品流程待补 |
| DTC | external dependency | 正确；只记录 AIX 对 DTC 的依赖边界，不维护 DTC 内部逻辑 |
| AAI | external dependency | 正确；只记录 AIX 对 AAI 的依赖边界，不维护 AAI 内部逻辑 |
| Receive | active 基础占位 | 需后续确认是否独立上线 |

## 6. 一致性检查

| 检查项 | 结果 |
|---|---|
| 是否仍把 Card Gate 写成 BLOCK | 否；已调整为 PARTIAL PASS + deferred gaps |
| 是否把 Deposit 错误标记为 deferred | 否；已恢复 active，限定 GTR / WalletConnect |
| 是否把 Send 写成 active | 否；保持 deferred |
| 是否把 Swap 写成 active | 否；保持 deferred |
| 是否把 `D-REQUEST-ID` 写成幂等键 | 否 |
| 是否把 Card / Wallet ID 强行关联 | 否 |
| 是否把通知写成必然 Wallet 到账 | 否 |
| 是否把 DTC / AAI 写成供应商系统说明书 | 否；已改为外部依赖边界 |
| 是否把 `FIAT_DEPOSIT` 写死为 GTR | 否 |
| 是否把 `CRYPTO_DEPOSIT` 写死为 WalletConnect | 否 |
| 是否把 Deposit success 写死为 Wallet `COMPLETED` | 否 |
| 是否把 Risk Withheld 写死为 Wallet `REJECTED` / `PENDING` / `PROCESSING` | 否 |
| 是否把 Wallet `relatedId` 与 Card / GTR / WC 强行关联 | 否 |

## 7. 仍需保留的关键 gaps

| 编号 | gap | 影响 |
|---|---|---|
| FINAL-GAP-001 | GTR 是否使用 `FIAT_DEPOSIT=6` | GTR 历史分类未闭环 |
| FINAL-GAP-002 | WalletConnect 是否使用 `CRYPTO_DEPOSIT=10` | WC 历史分类未闭环 |
| FINAL-GAP-003 | GTR / WC 是否都适用 senderAddress whitelist 规则 | 白名单产品规则未闭环 |
| FINAL-GAP-004 | WalletConnect senderAddress 获取方式 | WC 加白路径未闭环 |
| FINAL-GAP-005 | Declare / Travel Rule 触发条件 | 合规流程未闭环 |
| FINAL-GAP-006 | `relatedId` 在 GTR / WC / Card 归集场景下的具体取值 | 对账链路未闭环 |
| FINAL-GAP-007 | Deposit success 与 Wallet `state=COMPLETED` 的关系 | 状态机未闭环 |
| FINAL-GAP-008 | Risk Withheld 与 Wallet `state` 的关系 | 状态机未闭环 |
| FINAL-GAP-009 | Deposit success 后余额何时可见 / 可用 | 余额展示未闭环 |
| FINAL-GAP-010 | Risk Withheld 时是否展示冻结余额 | 余额展示未闭环 |
| FINAL-GAP-011 | GTR / WC 人工处理、客服口径、告警规则 | 异常闭环未完成 |
| FINAL-GAP-012 | Wallet KYC / AAI 实际接口、状态、失败处理 | KYC 外部依赖未补齐 |
| FINAL-GAP-013 | FAQ / 客服口径原文 | AI 面向用户答复仍缺口径来源 |

## 8. 后续补材料优先级

| 优先级 | 补充项 | 目标文件 |
|---|---|---|
| P0 | GTR / WalletConnect 页面入口、用户路径、状态展示、Declare / Travel Rule、余额可见时点、人工处理 | wallet/deposit、common/walletconnect、common/errors、common/notification |
| P0 | `relatedId`、`transactionId`、ActivityType 到 AIX 前端交易类型的映射 | wallet/transaction-history、transaction/status-model、common/dtc |
| P1 | AIX 实际依赖的 Wallet KYC / AAI 状态、接口、失败处理 | wallet/kyc、common/aai |
| P1 | 通用错误码、错误页、告警和人工补偿入口 | common/errors |
| P2 | FAQ 原文和客服口径 | common/faq |

## 9. 最终判断

当前仓库已可作为 AIX AI 知识库的基础版本使用，但应标记为：

`PARTIAL PASS / 基础事实层完成 / P0 Deposit 与 Wallet History 已阶段性回填 / 待补材料继续回填`

使用限制：

- 可引用已确认事实。
- 不可引用 deferred gaps 为事实。
- 不可把未上线功能作为 active 能力。
- 不可把待补状态机、错误码、通知、合规规则补写完整。
- 不可把 DTC / AAI 当作 AIX 自有系统或供应商系统说明书维护。
- 不可把 ActivityType、Risk Withheld、Deposit success 与具体产品路径或 Wallet state 做未确认等价映射。

## 10. 来源引用

- (Ref: IMPLEMENTATION_PLAN.md / v4.3)
- (Ref: knowledge-base/changelog/refinement-stage-review.md / v1.0)
- (Ref: knowledge-base/common/dtc.md / v1.3)
- (Ref: knowledge-base/common/aai.md / v1.1)
- (Ref: knowledge-base/wallet/deposit.md / v1.4)
- (Ref: knowledge-base/wallet/transaction-history.md / v1.1)
- (Ref: knowledge-base/wallet/balance.md / v1.1)
- (Ref: knowledge-base/transaction/status-model.md / v1.1)
- (Ref: knowledge-base/transaction/history.md / v1.1)
- (Ref: knowledge-base/transaction/detail.md / v1.1)
- (Ref: knowledge-base/changelog/knowledge-gaps.md / deferred gaps)
