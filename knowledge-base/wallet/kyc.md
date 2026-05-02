---
module: wallet
feature: kyc
version: "1.1"
status: active
source_doc: IMPLEMENTATION_PLAN.md；knowledge-base/wallet/_index.md；knowledge-base/wallet/deposit.md；knowledge-base/common/aai.md；knowledge-base/security/_index.md；knowledge-base/changelog/knowledge-gaps.md；用户确认结论 2026-05-02
source_section: IMPLEMENTATION_PLAN v4.3；Wallet KYC；AAI Dependency v1.2；用户确认：外部依赖只保留与 AIX 系统设计有关内容
last_updated: 2026-05-02
owner: 吴忆锋
depends_on:
  - wallet/_index
  - wallet/deposit
  - common/aai
  - security/_index
  - changelog/knowledge-gaps
---

# Wallet KYC / 钱包开户前置

## 1. 功能定位

Wallet KYC 用于沉淀 AIX Wallet 能力的开户、准入和 KYC 前置条件。

本文不维护 AAI / DTC 等供应商完整接口或内部规则，只记录与 AIX 系统设计有关的 KYC 边界：哪些 Wallet 能力可能依赖 KYC、KYC 结果如何影响页面 / 状态 / 准入 / 通知 / 错误处理，以及哪些关系仍需确认。

## 2. 当前状态

| 项目 | 当前判断 | 处理 |
|---|---|---|
| Wallet KYC 是否存在 | 作为 Wallet 阶段待转译能力存在 | 已纳入 Wallet 阶段 |
| Wallet KYC 完整流程 | 未确认 | 待 PRD / 截图 / 已确认结论补齐 |
| Wallet 与 Card KYC 的关系 | 未确认 | 不默认复用 Card KYC 细节 |
| Wallet 与 AAI / 身份认证关系 | AAI 只作为外部依赖边界 | 不维护 AAI 内部字段 |
| Wallet 开户失败处理 | 未确认 | 不补写 |
| Wallet KYC 与 Deposit 关系 | 未确认 | 不补写 GTR / WalletConnect 准入规则 |

## 3. AIX 侧需要关心的 KYC 设计问题

| 问题 | 为什么影响 AIX 系统设计 | 当前处理 |
|---|---|---|
| Wallet 是否需要独立开户 / KYC | 影响 Wallet 初始化、能力开关、页面入口 | 待补 |
| Wallet KYC 是否复用 Card KYC | 影响 Account / Card / Wallet 的状态复用和数据一致性 | 待补 |
| KYC 是否为 Deposit 前置 | 影响 GTR / WalletConnect 是否允许进入、是否拦截 | 待补 |
| KYC 失败是否允许重试 | 影响用户路径、错误提示、重新提交入口 | 待补 |
| KYC 审核中是否限制 Wallet 能力 | 影响页面状态、按钮可用性、交易能力 | 待补 |
| KYC 结果是否触发通知 | 影响 Notification 规则 | 待补 |
| KYC 是否需要人工处理 | 影响运营后台、客服口径、异常闭环 | 待补 |

## 4. 与其他模块的关系

| 模块 | 关系 | 当前处理 |
|---|---|---|
| Account | Wallet KYC 可能依赖用户账户基础信息 | 当前不补字段 |
| Security | Wallet KYC 可能依赖 OTP、Face Authentication、Passcode 等安全能力 | 引用 Security，不重复定义 |
| Card | Card 申卡与 Wallet 可能共享部分 KYC 前置 | 不默认等同，避免把 Card KYC 写成 Wallet KYC |
| Wallet Balance | Wallet 开户 / KYC 通过后可能影响余额能力可用性 | 当前不补准入规则 |
| Wallet Deposit | GTR / WalletConnect Deposit 可能要求 Wallet 已开户 / KYC 通过 | 待后续按子路径确认 |
| Wallet Receive | Receive 是否要求 Wallet KYC 通过待确认 | 不补写 |
| Send / Swap | 当前 deferred | 不纳入 active KYC 范围 |
| AAI | 外部身份认证 / KYC 供应商能力 | 只记录 AIX 依赖结果，不维护供应商细节 |

## 5. 已确认 Wallet 阶段边界

| 项目 | 结论 | 来源 |
|---|---|---|
| Deposit | active，包含 GTR 和 WalletConnect | 用户确认 2026-05-01；wallet/_index.md |
| Send | deferred，因合规原因未上线 | 用户确认 2026-05-01；wallet/send.md |
| Swap | deferred，因合规原因未上线且需重做 | 用户确认 2026-05-01；wallet/_index.md |
| Wallet 交易记录 | 已建立基础事实源 | wallet/transaction-history.md |
| Wallet Balance | 已建立基础文件 | wallet/balance.md |
| Receive | 已建立基础占位，与 Deposit 子路径关系待确认 | wallet/receive.md |

## 6. 不写入事实的内容

以下内容当前不得写成事实：

1. Wallet KYC 与 Card KYC 完全相同。
2. Wallet KYC 与 AAI KYC 完全相同。
3. Wallet 开户一定在注册时自动完成。
4. Wallet 开户一定在 Card 申卡前完成。
5. GTR / WalletConnect Deposit 一定需要或不需要 Wallet KYC。
6. Wallet KYC 审核状态字段名。
7. Wallet KYC 审核状态枚举。
8. Wallet KYC 失败原因与用户提示。
9. Wallet 开户接口路径、请求字段、响应字段。
10. Wallet KYC 通过后所有 Wallet 能力均可用。
11. AAI / DTC 供应商内部审核逻辑。
12. 与 AIX 系统设计无关的供应商字段。

## 7. 待补字段 / 规则清单

| 待补项 | 目标问题 | 当前处理 |
|---|---|---|
| Wallet 开户触发时机 | 注册后自动？进入 Wallet 自动？用户主动触发？ | 待补 |
| Wallet KYC 与 Card KYC 关系 | 复用 / 独立 / 部分复用 | 待补 |
| Wallet KYC 与 Deposit 的关系 | GTR / WalletConnect 是否必须通过 KYC | 待补 |
| Wallet KYC 与 Receive 的关系 | Receive 是否依赖 Wallet KYC | 待补 |
| KYC 状态对页面和按钮影响 | 哪些状态下可看余额 / 可入金 / 可查看历史 | 待补 |
| KYC 失败处理 | 是否可重试、是否人工处理、是否有客服口径 | 待补 |
| KYC 通知规则 | 是否通知、通知渠道、跳转目标 | 待补 |
| AAI 结果变化影响范围 | 供应商结果变化会影响哪些 AIX 模块 | 待补 |

## 8. Stage Review 关注点

Wallet KYC 后续回扫时，需要确认：

1. Wallet 是否有独立开户 / KYC 流程。
2. Wallet KYC 与 Account / Security / Card KYC 的关系是否明确。
3. Wallet KYC 是否为 GTR / WalletConnect Deposit 的前置条件。
4. KYC 状态是否影响页面、按钮、余额、入金和历史记录。
5. KYC 失败分支、重新提交、人工处理、用户提示是否闭环。
6. Send / Swap deferred 能力是否未被纳入 Wallet KYC active 范围。
7. AAI 依赖是否只保留 AIX 系统设计需要的结果边界。

## 9. 来源引用

- (Ref: IMPLEMENTATION_PLAN.md / v4.3)
- (Ref: knowledge-base/wallet/_index.md / v1.3)
- (Ref: knowledge-base/wallet/deposit.md / v1.4)
- (Ref: knowledge-base/common/aai.md / v1.2)
- (Ref: knowledge-base/security/_index.md / Security 阶段)
- (Ref: knowledge-base/changelog/knowledge-gaps.md / deferred gaps)
- (Ref: 用户确认结论 / 2026-05-02 / 外部依赖只保留与 AIX 系统设计有关内容)
