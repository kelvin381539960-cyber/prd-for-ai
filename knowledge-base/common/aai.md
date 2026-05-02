---
module: common
feature: aai-dependency
version: "1.1"
status: active
source_doc: IMPLEMENTATION_PLAN.md；knowledge-base/common/_index.md；knowledge-base/wallet/kyc.md；knowledge-base/wallet/stage-review.md；knowledge-base/card/stage-review.md；knowledge-base/security/_index.md
source_section: IMPLEMENTATION_PLAN v4.1 / 全仓库回扫；Common Index v2.1；Wallet KYC v1.0；Wallet Stage Review v1.0；Card Stage Review v1.3；Security 阶段
last_updated: 2026-05-01
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

本文只沉淀 AIX 对 AAI 的依赖边界：

1. AIX 使用了哪些 AAI 能力。
2. AIX 依赖哪些身份认证、KYC、OCR、Liveness、Face Authentication 结果。
3. 哪些规则来自 AAI 文档或已确认结论。
4. 哪些业务规则属于 AIX 自己的 Card / Wallet / Security 流程。
5. 出现异常时 AIX 侧已确认或待确认的处理边界。

本文不维护 AAI 内部系统逻辑，不补写 AAI 未提供的状态、字段、错误码或审核规则，也不把 AAI 供应商能力写成 AIX 自有能力。

## 2. 当前已确认边界

| 项目 | 当前结论 | 来源 | AIX 侧处理 |
|---|---|---|---|
| Security 阶段 | OTP / Email OTP / Passcode / BIO / Face Auth / API Reference 已收口 | Security 阶段 | Common 只引用，不重复定义 |
| Card 阶段 | Card Transaction Flow 留 deferred gaps | Card Stage Review | 不在 AAI 中补 Card 业务规则 |
| Wallet KYC | 已建立基础占位，完整流程和接口待补 | Wallet KYC | 不默认等同 Card KYC / AAI KYC |
| Wallet KYC 与 Account / Security / Card KYC 关系 | 未确认 | Wallet KYC | 待补 |
| Wallet KYC 是否为 GTR / WalletConnect Deposit 前置 | 未确认 | Wallet KYC | 待补 |

## 3. AIX 对 AAI 的依赖范围

| 能力 | 当前处理 |
|---|---|
| OCR | 待补 AAI 文档来源，不写成事实 |
| Liveness | 待补 AAI 文档来源，不写成事实 |
| Face Authentication | Security 已有事实源，Common 只记录外部依赖边界 |
| KYC 提交 / 审核 | 待补，不写成 Wallet / Card 共用事实 |
| KYC 状态 | 待补，不写状态枚举 |
| KYC 失败 / 重试 | 待补，不写用户提示或流程 |

## 4. 与 AIX 业务模块的关系

| 模块 | 关系 | Common AAI 处理 |
|---|---|---|
| Account | KYC / 身份认证可能依赖账户信息 | 待补，不写具体流程 |
| Security | OTP、Face Auth、Passcode 等安全能力为 AIX 安全层能力 | 引用 Security，不重复定义 |
| Card | Card 申卡可能依赖 KYC / 身份认证 | 不重写 Card KYC 规则 |
| Wallet | Wallet KYC / 钱包开户前置待补 | 不默认等同 Card KYC |
| Deposit | GTR / WalletConnect 是否依赖 KYC 待确认 | 不补写 |

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

## 6. 待补项

| 编号 | 待补项 | 来源建议 | 当前处理 |
|---|---|---|---|
| AAI-GAP-001 | AIX 实际使用的 AAI OCR 接口与字段 | AAI 接口文档 / PRD | 待补 |
| AAI-GAP-002 | AIX 实际使用的 AAI Liveness 接口与字段 | AAI 接口文档 / PRD | 待补 |
| AAI-GAP-003 | AIX 实际依赖的 AAI KYC 状态枚举 | AAI / KYC PRD | 待补 |
| AAI-GAP-004 | AAI KYC 失败原因中 AIX 需要处理的部分 | AAI / KYC PRD / 错误码 | 待补 |
| AAI-GAP-005 | Wallet KYC 与 Card KYC 关系 | 产品确认 / PRD | 待补 |
| AAI-GAP-006 | Wallet KYC 与 Deposit 关系 | GTR / WalletConnect PRD / 合规确认 | 待补 |
| AAI-GAP-007 | KYC 通知规则 | Notification PRD / KYC PRD | 待补 |
| AAI-GAP-008 | KYC 重新提交 / 人工处理规则 | PRD / 后端 / 运营确认 | 待补 |

## 7. 来源引用

- (Ref: IMPLEMENTATION_PLAN.md / v4.1 / 全仓库回扫)
- (Ref: knowledge-base/common/_index.md / v2.1)
- (Ref: knowledge-base/wallet/kyc.md / v1.0)
- (Ref: knowledge-base/wallet/stage-review.md / v1.0)
- (Ref: knowledge-base/card/stage-review.md / v1.3)
- (Ref: knowledge-base/security/_index.md / Security 阶段)
