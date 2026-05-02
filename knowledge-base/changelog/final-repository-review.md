---
module: changelog
feature: final-repository-review
version: "1.5"
status: active
source_doc: IMPLEMENTATION_PLAN.md；knowledge-base/changelog/refinement-stage-review.md；knowledge-base/changelog/knowledge-gaps.md；knowledge-base/wallet/_index.md；knowledge-base/wallet/deposit.md；knowledge-base/wallet/balance.md；knowledge-base/wallet/receive.md；knowledge-base/transaction/_index.md；knowledge-base/transaction/history.md；knowledge-base/transaction/detail.md；knowledge-base/transaction/status-model.md；knowledge-base/transaction/reconciliation.md；knowledge-base/kyc/_index.md；knowledge-base/kyc/wallet-kyc.md；knowledge-base/card/card-transaction-flow.md；knowledge-base/card/transaction-flow-traceability-checklist.md；knowledge-base/common/dtc.md；knowledge-base/common/aai.md；knowledge-base/common/walletconnect.md；knowledge-base/common/notification.md；knowledge-base/common/errors.md；用户确认结论 2026-05-02
source_section: IMPLEMENTATION_PLAN v4.8；ALL-GAP v1.12；无损 gap 迁移；KYC 独立；Wallet Transaction History 合并；Transaction Reconciliation；外部依赖收窄原则
last_updated: 2026-05-02
owner: 吴忆锋
---

# 全仓库回扫记录

## 1. 收口结论

本轮知识库已完成结构边界重构、补材料阶段性回填，以及主干模块的无损 gap 迁移。当前仓库状态为：`PARTIAL PASS / 基础事实层完成 / ALL-GAP 统一待确认`。

含义：

- Account 与 Security 已完成并通过。
- Card、Wallet、Transaction、KYC、Common / Integration 均已形成基础事实层。
- Send / Swap 因未上线或需重做，保持 `deferred`。
- Deposit 为 `active`，范围限定为 GTR / Exchange 地址充值与 WalletConnect / Self-custodial Wallet 充值。
- KYC 已独立为 `knowledge-base/kyc/`，Wallet 目录不再维护 KYC 主事实。
- Wallet Transaction History 已合并至 `transaction/history.md`，Wallet 目录不再维护交易历史主事实。
- `transaction/reconciliation.md` 已承接资金追踪 / ID 链路 / 对账边界。
- DTC / AAI 已收窄为外部依赖边界，只保留影响 AIX 系统设计的内容。
- 全模块不确定项已统一至 `knowledge-base/changelog/knowledge-gaps.md` 的 ALL-GAP 总表。
- 主干模块级 gap / checklist / 待补清单已完成无损迁移：旧编号或旧待补项均保留到 ALL-GAP 映射。
- 当前知识库可作为 AI 使用的基础事实层，但不能把 ALL-GAP 中的 deferred / open 项当作已确认规则。

## 2. 当前目录边界

| 目录 | 定位 | 当前规则 |
|---|---|---|
| `wallet/` | 钱包产品能力 | 只维护 Balance / Deposit / Receive / Send；`kyc.md` 与 `transaction-history.md` 仅作为 moved notice |
| `transaction/` | 跨 Card / Wallet / Deposit 的交易统一层 | 维护 status-model、history、detail、reconciliation |
| `kyc/` | KYC / 业务准入能力 | 维护 wallet-kyc；AAI 仍保留在 common/aai 作为外部依赖 |
| `common/` | 公共能力和外部依赖边界 | 维护 dtc、aai、walletconnect、notification、errors、faq |
| `changelog/` | 变更、回扫、唯一待确认表 | `knowledge-gaps.md` 是唯一 ALL-GAP 总表 |

## 3. 无损 gap 迁移结果

本轮已迁移的历史分散问题类型：

| 原类型 / 来源 | 当前处理 |
|---|---|
| `DEP-GAP` | 已迁入 ALL-GAP，并在 `wallet/deposit.md` 保留映射 |
| `ERR-GAP` | 已迁入 ALL-GAP，并在 `common/errors.md` 保留映射 |
| `TXN-DETAIL-GAP` | 已迁入 ALL-GAP，并在 `transaction/detail.md` 保留映射 |
| `TXN-STATUS-GAP` | 已迁入 ALL-GAP，并在 `transaction/status-model.md` 保留映射 |
| Card traceability checklist 的 `BE-*` / `WALLET-*` | 已迁入 ALL-GAP，原文件改为 `migrated-reference` |
| Wallet Balance 待补字段 | 已迁入 ALL-GAP，并在 `wallet/balance.md` 保留映射 |
| Wallet Receive 待补字段 | 已迁入 ALL-GAP，并在 `wallet/receive.md` 保留映射 |
| `DTC-GAP` | 已迁入 ALL-GAP，并在 `common/dtc.md` 保留映射 |
| `NOTIF-GAP` | 已迁入 ALL-GAP，并在 `common/notification.md` 保留映射 |

迁移原则：

1. 不删除历史问题。
2. 不用概括性文字替代原问题。
3. 模块正文只保留事实和 ALL-GAP 引用。
4. 旧编号 / 旧待补项只作为迁移追溯，不再作为新的待确认表维护。

## 4. 外部依赖收窄原则

DTC / AAI 等供应商能力不作为供应商系统说明书维护。

只保留：

1. 影响 AIX 页面、状态、按钮、准入、通知、错误处理、人工处理、资金追踪、对账的依赖。
2. AIX 实际使用或需要感知的结果、字段、状态、事件。
3. 供应商变化会影响 AIX 产品 / 前端 / 后端 / 运营处理的边界。

不保留：

1. 供应商内部系统逻辑。
2. 完整接口说明书。
3. 完整字段表。
4. 完整错误码表。
5. 与 AIX 系统设计无关的供应商字段。

## 5. 阶段状态总表

| 阶段 | Gate 结果 | 说明 |
|---|---|---|
| Account | PASS | Login / Registration / Password Reset 已完成；少量文案 / 截图结构缺口进 ALL-GAP |
| Security | PASS | OTP / Email OTP / Passcode / BIO / Face Auth / API Reference 已收口 |
| Card | PARTIAL PASS | 页面与卡管能力完成；Transaction Flow 资金追踪留 ALL-GAP P0 |
| Wallet | PARTIAL PASS | 钱包产品能力完成基础版；Deposit active；KYC / Transaction History 已迁出；Send / Swap deferred |
| Transaction | PARTIAL PASS | 状态、历史、详情、资金追踪边界完成基础版；对账字段仍留 ALL-GAP |
| KYC | PARTIAL PASS | 已独立目录；Wallet KYC 已迁移；Card KYC / Wallet KYC 关系待确认 |
| Common / Integration | PARTIAL PASS | DTC / AAI / WalletConnect / Notification / Errors / FAQ 边界完成基础版 |
| 全仓库回扫 | PARTIAL PASS | 主干结构边界、旧引用、无损 gap 迁移已阶段性完成 |
| 补材料与精修 | PARTIAL PASS | Deposit / WalletConnect / Errors / FAQ / ALL-GAP / 目录结构 / 无损迁移已阶段性收口 |

## 6. 本轮结构调整结果

| 调整项 | 结果 |
|---|---|
| KYC 独立 | 新增并维护 `kyc/_index.md`、`kyc/wallet-kyc.md` |
| Wallet KYC 旧路径 | `wallet/kyc.md` 改为 moved notice |
| Wallet Transaction History 合并 | 主事实合并至 `transaction/history.md` |
| Wallet Transaction History 旧路径 | `wallet/transaction-history.md` 改为 moved notice |
| Transaction Reconciliation | 新增并维护 `transaction/reconciliation.md` |
| Wallet index | 已更新为只承接钱包产品能力 |
| Transaction index | 已更新为承接 history / detail / status / reconciliation |
| 主控计划 | `IMPLEMENTATION_PLAN.md` 升级到 v4.8 |
| ALL-GAP 总表 | 升级到 v1.12，已作为唯一待确认表并加 P0 / P1 / P2 优先级 |

## 7. 文件完整性检查

| 模块 | 核心文件 | 状态 |
|---|---|---|
| Card | `_index`、application、status、home、activation、pin、sensitive-info、management、transaction-flow、stage-review、traceability-checklist | 基础版完成；资金追踪问题统一进 ALL-GAP |
| Wallet | `_index`、balance、deposit、receive、send、kyc、transaction-history、stage-review | 产品能力完成基础版；kyc / transaction-history 为 moved notice |
| Transaction | `_index`、status-model、history、detail、reconciliation、stage-review | 基础版完成；history 承接 Wallet History；reconciliation 承接对账边界 |
| KYC | `_index`、wallet-kyc | 已独立；AAI 仍在 common/aai |
| Common | `_index`、dtc、notification、walletconnect、errors、aai、faq、stage-review | 基础版完成；外部依赖已收窄 |
| Changelog | knowledge-gaps、final-repository-review、refinement-stage-review | ALL-GAP 为唯一待确认表 |

## 8. 一致性检查

| 检查项 | 结果 |
|---|---|
| 是否把 Send 写成 active | 否；保持 deferred |
| 是否把 Swap 写成 active | 否；保持 deferred |
| 是否把 KYC 主事实继续维护在 Wallet | 否；已迁移至 `kyc/wallet-kyc.md` |
| 是否把 Wallet Transaction History 主事实继续维护在 Wallet | 否；已迁移至 `transaction/history.md` |
| 是否新增资金追踪边界文件 | 是；`transaction/reconciliation.md` |
| 是否把 `D-REQUEST-ID` 写成幂等键 | 否 |
| 是否把 Card / Wallet ID 强行关联 | 否 |
| 是否把通知写成必然 Wallet 到账 | 否 |
| 是否把 DTC / AAI 写成供应商系统说明书 | 否；只保留外部依赖边界 |
| 是否把 `FIAT_DEPOSIT` 写死为 GTR | 否；见 ALL-GAP-001 |
| 是否把 `CRYPTO_DEPOSIT` 写死为 WalletConnect | 否；见 ALL-GAP-002 |
| 是否把 Deposit success 写死为 Wallet `COMPLETED` | 否；见 ALL-GAP-016 |
| 是否把 Risk Withheld 写死为 Wallet `REJECTED` / `PENDING` / `PROCESSING` | 否；见 ALL-GAP-008 |
| 是否把 Wallet `relatedId` 与 Card / GTR / WC 强行关联 | 否；见 ALL-GAP-014 |
| 是否允许模块级 checklist / TODO / gaps 表 | 否；唯一来源为 `knowledge-gaps.md` |
| 是否允许迁移时丢失问题 | 否；旧 gap / 待补项已保留映射 |

## 9. 当前关键 ALL-GAP 引用

| 优先级 | 编号 | 主题 |
|---|---|---|
| P0 | ALL-GAP-007 | `relatedId / transactionId / id` 如何串联 GTR / WalletConnect 入金 |
| P0 | ALL-GAP-008 | Risk Withheld 与 Wallet `state` / 余额关系 |
| P0 | ALL-GAP-014 | Wallet `relatedId` 在 Card / GTR / WC 场景取值 |
| P0 | ALL-GAP-017 | Card Transaction 与 Wallet Transaction 是否一一对应 |
| P0 | ALL-GAP-018 | Card / Wallet 关联字段 |
| P0 | ALL-GAP-019 | AIX 内部交易处理 ID |
| P0 | ALL-GAP-020 | AIX 归集请求 ID |
| P0 | ALL-GAP-021 | `D-REQUEST-ID` 是否承担幂等 / 去重 |
| P0 | ALL-GAP-022 | Webhook 原始报文是否完整落库 |
| P0 | ALL-GAP-024 | 自动归集触发附加判断 |
| P0 | ALL-GAP-025 | 查询 Card balance 失败处理 |
| P0 | ALL-GAP-026 | Transfer Balance to Wallet 失败补偿入口 |
| P0 | ALL-GAP-027 | DTC transfer 成功但 Wallet 未到账发现机制 |
| P0 | ALL-GAP-029 | 财务 / 运营最终对账字段组合 |
| P0 | ALL-GAP-036 | Webhook 原始报文落库规则 |

## 10. 后续执行建议

| 顺序 | 事项 | 目标 |
|---|---|---|
| 1 | 关键词残留抽查 | 搜索 `待补项`、`checklist`、`TODO`、`GAP-`，如发现真实待确认项则迁入 ALL-GAP |
| 2 | 优先确认 P0 ALL-GAP | 收敛资金、对账、状态闭环和资产可见性 |
| 3 | 再处理 P1 / P2 | 流程体验、文案、FAQ、低频展示 |
| 4 | 确认后反向回填 | 更新 ALL-GAP 状态，并同步回填相关功能文件 |
| 5 | 最后做 Stage Review | 用 PASS / PARTIAL PASS / BLOCK 更新主控状态 |

## 11. 最终判断

当前仓库可作为 AIX AI 知识库的基础版本使用，但应标记为：

`PARTIAL PASS / 基础事实层完成 / Deposit 与 WalletConnect 已阶段性回填 / KYC 已独立 / Wallet History 已并入 Transaction / Reconciliation 已建立 / ALL-GAP 统一待确认 / 主干无损 gap 迁移完成`

使用限制：

- 可引用已确认事实。
- 不可引用 ALL-GAP deferred / open 项为事实。
- 不可把未上线功能作为 active 能力。
- 不可把待补状态机、错误码、通知、合规规则补写完整。
- 不可把 DTC / AAI 当作 AIX 自有系统或供应商系统说明书维护。
- 不可维护与 AIX 系统设计无关的供应商字段、错误码、接口说明或内部逻辑。
- 不可把 ActivityType、Risk Withheld、Deposit success 与具体产品路径或 Wallet state 做未确认等价映射。
- 不可在模块文档内新增 checklist / TODO / gaps 表。
- 不可因精简、合并、改写、迁移导致历史问题丢失。

## 12. 来源引用

- (Ref: IMPLEMENTATION_PLAN.md / v4.8)
- (Ref: knowledge-base/changelog/knowledge-gaps.md / v1.12 / ALL-GAP 总表)
- (Ref: knowledge-base/changelog/refinement-stage-review.md / v1.0)
- (Ref: knowledge-base/wallet/_index.md / v1.4)
- (Ref: knowledge-base/wallet/deposit.md / v1.6)
- (Ref: knowledge-base/wallet/balance.md / v1.2)
- (Ref: knowledge-base/wallet/receive.md / v1.1)
- (Ref: knowledge-base/transaction/_index.md / v1.1)
- (Ref: knowledge-base/transaction/history.md / v1.3)
- (Ref: knowledge-base/transaction/detail.md / v1.2)
- (Ref: knowledge-base/transaction/status-model.md / v1.2)
- (Ref: knowledge-base/transaction/reconciliation.md / v1.1)
- (Ref: knowledge-base/card/card-transaction-flow.md / v1.3)
- (Ref: knowledge-base/card/transaction-flow-traceability-checklist.md / v1.6 migrated-reference)
- (Ref: knowledge-base/kyc/_index.md / v1.0)
- (Ref: knowledge-base/kyc/wallet-kyc.md / v1.0)
- (Ref: knowledge-base/common/dtc.md / v1.5)
- (Ref: knowledge-base/common/aai.md / v1.2)
- (Ref: knowledge-base/common/walletconnect.md / v1.4)
- (Ref: knowledge-base/common/notification.md / v1.3)
- (Ref: knowledge-base/common/errors.md / v1.4)
- (Ref: 用户确认结论 / 2026-05-02 / KYC 独立，common/aai.md 不迁移，Wallet Transaction History 合并进 Transaction History，ALL-GAP 唯一总表与无损迁移规则)
