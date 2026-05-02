---
module: common
feature: aai-integration
version: "1.0"
status: active
source_doc: IMPLEMENTATION_PLAN.md；knowledge-base/common/_index.md；knowledge-base/wallet/kyc.md；knowledge-base/wallet/stage-review.md；knowledge-base/card/stage-review.md；knowledge-base/security/_index.md
source_section: IMPLEMENTATION_PLAN v4.0 / Common Integration；Common Index v2.0；Wallet KYC v1.0；Wallet Stage Review v1.0；Card Stage Review v1.3；Security 阶段
last_updated: 2026-05-01
owner: 吴忆锋
depends_on:
  - common/_index
  - wallet/kyc
  - wallet/stage-review
  - card/stage-review
  - security/_index
---

# AAI Integration 身份认证公共集成边界

## 1. 功能定位

AAI Integration 用于沉淀 AIX 中与 AAI / KYC / OCR / Liveness / Face Authentication 相关的公共集成边界。

本文不重写 Card KYC、Wallet KYC 或 Security 认证流程，只记录跨模块可复用的集成边界和待补项。

## 2. 当前已确认边界

| 项目 | 当前结论 | 来源 | 备注 |
|---|---|---|---|
| Security 阶段 | 已完成，OTP / Email OTP / Passcode / BIO / Face Auth / API Reference 已收口 | Security 阶段 | Common 可引用，不重复定义 |
| Card 阶段 | 已完成基础能力，Card Transaction Flow 留 deferred gaps | Card Stage Review | 不在 AAI 中补 Card 业务规则 |
| Wallet KYC | 已建立基础占位，完整流程和接口待补 | Wallet KYC | 不默认等同 Card KYC / AAI KYC |
| Wallet KYC 与 Account / Security / Card KYC 关系 | 未确认 | Wallet KYC | 待补 |
| Wallet KYC 是否为 GTR / WalletConnect Deposit 前置 | 未确认 | Wallet KYC | 待补 |

## 3. AAI 可沉淀能力范围

| 能力 | 当前处理 |
|---|---|
| OCR | 待补 AAI 文档来源，不写成事实 |
| Liveness | 待补 AAI 文档来源，不写成事实 |
| Face Authentication | Security 已有事实源，Common 只引用边界 |
| KYC 提交 / 审核 | 待补，不写成 Wallet / Card 共用事实 |
| KYC 状态 | 待补，不写状态枚举 |
| KYC 失败 / 重试 | 待补，不写用户提示或流程 |

## 4. 与业务模块的关系

| 模块 | 关系 | Common AAI 处理 |
|---|---|---|
| Account | KYC / 身份认证可能依赖账户信息 | 待补，不写具体流程 |
| Security | OTP、Face Auth、Passcode 等安全能力为公共能力 | 引用 Security，不重复定义 |
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

## 6. 待补项

| 编号 | 待补项 | 来源建议 | 当前处理 |
|---|---|---|---|
| AAI-GAP-001 | AAI OCR 接口与字段 | AAI 接口文档 / PRD | 待补 |
| AAI-GAP-002 | AAI Liveness 接口与字段 | AAI 接口文档 / PRD | 待补 |
| AAI-GAP-003 | AAI KYC 状态枚举 | AAI / KYC PRD | 待补 |
| AAI-GAP-004 | AAI KYC 失败原因 | AAI / KYC PRD / 错误码 | 待补 |
| AAI-GAP-005 | Wallet KYC 与 Card KYC 关系 | 产品确认 / PRD | 待补 |
| AAI-GAP-006 | Wallet KYC 与 Deposit 关系 | GTR / WalletConnect PRD / 合规确认 | 待补 |
| AAI-GAP-007 | KYC 通知规则 | Notification PRD / KYC PRD | 待补 |
| AAI-GAP-008 | KYC 重新提交 / 人工处理规则 | PRD / 后端 / 运营确认 | 待补 |

## 7. 来源引用

- (Ref: IMPLEMENTATION_PLAN.md / v4.0 / Common Integration)
- (Ref: knowledge-base/common/_index.md / v2.0)
- (Ref: knowledge-base/wallet/kyc.md / v1.0)
- (Ref: knowledge-base/wallet/stage-review.md / v1.0)
- (Ref: knowledge-base/card/stage-review.md / v1.3)
- (Ref: knowledge-base/security/_index.md / Security 阶段)
