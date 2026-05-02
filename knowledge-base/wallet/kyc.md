---
module: wallet
feature: kyc
version: "1.0"
status: active
source_doc: IMPLEMENTATION_PLAN.md；knowledge-base/wallet/_index.md；knowledge-base/wallet/balance.md；knowledge-base/wallet/deposit.md；knowledge-base/wallet/receive.md；knowledge-base/wallet/transaction-history.md；knowledge-base/card/card-transaction-flow.md；knowledge-base/changelog/knowledge-gaps.md
source_section: IMPLEMENTATION_PLAN v3.8 / Wallet KYC；Wallet _index v1.3；Wallet active/deferred boundaries
last_updated: 2026-05-01
owner: 吴忆锋
depends_on:
  - wallet/_index
  - wallet/balance
  - wallet/deposit
  - wallet/receive
  - wallet/transaction-history
  - card/card-transaction-flow
  - changelog/knowledge-gaps
---

# Wallet KYC / 钱包开户前置

## 1. 功能定位

Wallet KYC 用于沉淀 AIX Wallet 能力的开户、准入和 KYC 前置条件。

当前文件为 Wallet KYC 基础占位。由于当前仓库检索未直接命中 Wallet KYC / DTC 钱包开户的完整 PRD 或接口字段，本文只记录 Wallet 阶段已确认边界和待补事项，不补写开户流程、KYC 状态、接口字段或审核规则。

## 2. 当前状态

| 项目 | 当前判断 | 处理 |
|---|---|---|
| Wallet KYC 是否存在 | 作为 Wallet 阶段待转译能力存在 | 已纳入 Wallet 阶段 |
| Wallet KYC 完整流程 | 未确认 | 待 PRD / 接口文档补齐 |
| DTC 钱包开户接口 | 未确认 | 待 DTC Wallet OpenAPI 原文补齐 |
| Wallet 与 Card KYC 的关系 | 未确认 | 不默认复用 Card KYC 细节 |
| Wallet 与 AAI / 身份认证关系 | 未确认 | 不补写 |
| Wallet 开户失败处理 | 未确认 | 不补写 |

## 3. 与其他模块的关系

| 模块 | 关系 | 当前处理 |
|---|---|---|
| Account | Wallet KYC 可能依赖用户账户 | 需后续引用 Account 事实源，当前不补流程 |
| Security | Wallet KYC 可能依赖 OTP、Face Authentication、Passcode 等安全能力 | 需后续引用 Security 事实源，当前不重复定义 |
| Card | Card 申卡与 Wallet 可能共享部分 KYC 前置 | 不默认等同，避免把 Card KYC 写成 Wallet KYC |
| Wallet Balance | Wallet 开户 / KYC 通过后可能影响余额能力可用性 | 当前不补准入规则 |
| Wallet Deposit | GTR / WalletConnect Deposit 可能要求 Wallet 已开户 / KYC 通过 | 待后续按子路径确认 |
| Wallet Receive | Receive 是否要求 Wallet KYC 通过待确认 | 不补写 |
| Send / Swap | 当前 deferred | 不纳入 active KYC 范围 |

## 4. 已确认 Wallet 阶段边界

| 项目 | 结论 | 来源 |
|---|---|---|
| Deposit | active，包含 GTR 和 WalletConnect | 用户确认 2026-05-01；wallet/_index.md |
| Send | deferred，因合规原因未上线 | 用户确认 2026-05-01；wallet/send.md |
| Swap | deferred，因合规原因未上线且需重做 | 用户确认 2026-05-01；wallet/_index.md |
| Wallet 交易记录 | 已建立基础事实源 | wallet/transaction-history.md |
| Wallet Balance | 已建立基础文件 | wallet/balance.md |
| Receive | 已建立基础占位，与 Deposit 子路径关系待确认 | wallet/receive.md |

## 5. 不写入事实的内容

以下内容当前不得写成事实：

1. Wallet KYC 与 Card KYC 完全相同。
2. Wallet KYC 与 AAI KYC 完全相同。
3. Wallet 开户一定在注册时自动完成。
4. Wallet 开户一定在 Card 申卡前完成。
5. GTR / WalletConnect Deposit 一定不需要额外 KYC / Declare / Travel Rule。
6. Wallet KYC 审核状态字段名。
7. Wallet KYC 审核状态枚举。
8. Wallet KYC 失败原因与用户提示。
9. Wallet 开户接口路径、请求字段、响应字段。
10. Wallet KYC 通过后所有 Wallet 能力均可用。

## 6. 待补字段 / 规则清单

| 待补项 | 建议来源 | 当前处理 |
|---|---|---|
| Wallet 开户触发时机 | Wallet PRD / DTC Wallet OpenAPI | 待补 |
| Wallet 开户接口路径 | DTC Wallet OpenAPI | 待补 |
| Wallet 开户请求字段 | DTC Wallet OpenAPI | 待补 |
| Wallet 开户响应字段 | DTC Wallet OpenAPI | 待补 |
| Wallet KYC 状态字段 | Wallet PRD / DTC Wallet OpenAPI / AAI 文档 | 待补 |
| Wallet KYC 状态枚举 | Wallet PRD / DTC Wallet OpenAPI / AAI 文档 | 待补 |
| Wallet KYC 与 Card KYC 关系 | 产品确认 / PRD | 待补 |
| Wallet KYC 与 Deposit 的关系 | GTR / WalletConnect PRD / 合规确认 | 待补 |
| Wallet KYC 与 Receive 的关系 | PRD / 产品确认 | 待补 |
| KYC 失败处理 | PRD / 错误码 / 客服口径 | 待补 |
| KYC 通知规则 | Notification PRD | 待补 |
| KYC 重试 / 重新提交规则 | PRD / AAI / 后端确认 | 待补 |

## 7. Stage Review 关注点

Wallet Stage Review 时，需要确认：

1. Wallet 是否有独立开户 / KYC 流程。
2. Wallet KYC 与 Account / Security / Card KYC 的关系是否明确。
3. Wallet KYC 是否为 GTR / WalletConnect Deposit 的前置条件。
4. Wallet KYC 状态字段和状态枚举是否有来源。
5. Wallet 开户接口路径、请求字段、响应字段是否有来源。
6. KYC 失败分支、重新提交、人工处理、用户提示是否闭环。
7. Send / Swap deferred 能力是否未被纳入 Wallet KYC active 范围。

## 8. 来源引用

- (Ref: IMPLEMENTATION_PLAN.md / v3.8 / Wallet KYC 当前任务)
- (Ref: knowledge-base/wallet/_index.md / v1.3)
- (Ref: knowledge-base/wallet/deposit.md / v1.2)
- (Ref: knowledge-base/wallet/balance.md / v1.0)
- (Ref: knowledge-base/wallet/receive.md / v1.0)
- (Ref: knowledge-base/wallet/transaction-history.md / v1.0)
- (Ref: knowledge-base/card/card-transaction-flow.md / v1.2)
- (Ref: knowledge-base/changelog/knowledge-gaps.md / Card Transaction Flow deferred gaps)
