---
module: common
feature: aai-dependency
version: "1.2"
status: active
source_doc: IMPLEMENTATION_PLAN.md；knowledge-base/common/_index.md；knowledge-base/wallet/kyc.md；knowledge-base/wallet/stage-review.md；knowledge-base/card/stage-review.md；knowledge-base/security/_index.md；用户确认结论 2026-05-02
source_section: IMPLEMENTATION_PLAN v4.3；Common Index v2.1；Wallet KYC v1.0；用户确认：外部依赖只保留与 AIX 系统设计有关内容
last_updated: 2026-05-02
owner: 吴忆锋
depends_on:
  - common/_index
  - wallet/kyc
  - wallet/stage-review
  - card/stage-review
  - security/_index
---

# AAI Dependency 外部依赖边界

## 1. 功能定位

AAI 是 AIX 的外部身份认证 / KYC 供应商能力，不是 AIX 内部系统，也不是本知识库需要维护的供应商系统说明书。

本文只记录与 AIX 系统设计有关的 AAI 依赖边界，不维护 AAI 的完整接口、完整字段、完整错误码、完整审核规则或供应商内部逻辑。

保留范围：

1. AIX 哪些业务能力依赖 AAI 结果。
2. AIX 需要感知哪些结果类型，例如 KYC 是否通过、是否失败、是否需要重试、是否需要人工处理。
3. AIX 侧页面、状态、通知、能力准入、异常处理需要依赖哪些外部结果。
4. AAI 变化可能影响 AIX 哪些模块。

不保留范围：

1. AAI 内部审核逻辑。
2. AAI 完整接口字段。
3. AAI 完整错误码表。
4. AAI 算法、OCR、Liveness、Face Match 的供应商侧细节。
5. 未被 AIX 产品 / 后端 / 前端使用的供应商字段。

## 2. 当前已确认边界

| 项目 | 当前结论 | AIX 侧处理 |
|---|---|---|
| Security 阶段 | OTP / Email OTP / Passcode / BIO / Face Auth / API Reference 已收口 | Common 只引用，不重复定义 |
| Wallet KYC | 已建立基础占位，完整流程和接口待补 | 不默认等同 Card KYC / AAI KYC |
| Card KYC / Wallet KYC 关系 | 未确认 | 不做复用推导 |
| Wallet KYC 是否为 GTR / WalletConnect Deposit 前置 | 未确认 | 不补写准入规则 |
| AAI OCR / Liveness | 供应商能力存在可能性高，但 AIX 实际使用边界待补 | 不补供应商字段，只保留 AIX 依赖结果 |

## 3. AIX 需要关心的 AAI 结果类型

以下不是 AAI 完整状态机，只是 AIX 侧可能需要承接的结果类别。

| 结果类别 | AIX 需要关心的原因 | 当前处理 |
|---|---|---|
| KYC 通过 | 可能影响 Wallet 开户、Deposit、Card 或其他能力准入 | 待补具体业务关系 |
| KYC 未通过 / 失败 | 可能影响页面提示、重新提交、人工处理、通知 | 待补 |
| KYC 审核中 | 可能影响能力锁定、状态展示、用户等待提示 | 待补 |
| 需要用户补充 / 重试 | 可能影响重新提交入口和用户提示 | 待补 |
| 人工处理 | 可能影响运营后台和客服口径 | 待补 |

## 4. 与 AIX 业务模块的关系

| 模块 | 关系 | 当前处理 |
|---|---|---|
| Account | KYC / 身份认证可能依赖账户基础信息 | 不写具体字段，待 Account / KYC PRD 支撑 |
| Security | OTP、Face Auth、Passcode 是 AIX 安全层能力 | 引用 Security，不在 AAI 重写 |
| Card | Card 申卡可能依赖 KYC / 身份认证 | 不默认复用为 Wallet KYC |
| Wallet | Wallet KYC / 钱包开户前置待补 | 只记录准入关系，不维护 AAI 细节 |
| Deposit | GTR / WalletConnect 是否依赖 KYC 待确认 | 不补写 |
| Notification | KYC 结果是否通知待确认 | 不补写通知文案 |
| Errors | KYC 失败 / 重试 / 人工处理待确认 | 不补写错误码 |

## 5. 不写入事实的内容

以下内容不得写成事实：

1. Wallet KYC 与 Card KYC 完全相同。
2. Wallet KYC 与 AAI KYC 完全相同。
3. AAI KYC 状态枚举已确认。
4. Wallet 开户一定在注册时自动完成。
5. Wallet KYC 一定是 GTR / WalletConnect Deposit 前置。
6. KYC 失败 / 重试 / 重新提交规则已确认。
7. OCR / Liveness 字段、接口、错误码已确认。
8. Face Authentication 规则在 Common 中重新定义。
9. AAI 内部审核逻辑。
10. AAI 未提供但由 AIX 推测的字段、状态或错误码。
11. 与 AIX 系统设计无关的供应商字段。

## 6. 待补项

| 编号 | 待补项 | 目标问题 | 当前处理 |
|---|---|---|---|
| AAI-GAP-001 | AIX 实际依赖哪些 AAI 结果 | 哪些结果会影响 AIX 页面、状态、准入、通知、错误 | 待补 |
| AAI-GAP-002 | Wallet KYC 与 Card KYC 关系 | 是否复用、是否独立、是否有差异 | 待补 |
| AAI-GAP-003 | Wallet KYC 与 Deposit 关系 | GTR / WalletConnect 是否必须 KYC 通过 | 待补 |
| AAI-GAP-004 | KYC 失败 / 重试 / 人工处理 | 用户如何重新提交、是否人工介入 | 待补 |
| AAI-GAP-005 | KYC 通知规则 | 是否发 push / 站内信 / email | 待补 |
| AAI-GAP-006 | AAI 结果变化对 AIX 的影响范围 | 供应商状态 / 字段变更会影响哪些 AIX 模块 | 待补 |

## 7. 来源引用

- (Ref: IMPLEMENTATION_PLAN.md / v4.3)
- (Ref: knowledge-base/common/_index.md / v2.1)
- (Ref: knowledge-base/wallet/kyc.md / v1.0)
- (Ref: knowledge-base/wallet/stage-review.md / v1.0)
- (Ref: knowledge-base/card/stage-review.md / v1.3)
- (Ref: knowledge-base/security/_index.md / Security 阶段)
- (Ref: 用户确认结论 / 2026-05-02 / 外部依赖只保留与 AIX 系统设计有关内容)
