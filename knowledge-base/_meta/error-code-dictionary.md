---
module: _meta
feature: error-code-dictionary
version: "2.0"
status: active
source_doc: archive/legacy-prd/**/README.md；knowledge-base/* 已校准模块
source_section: converted PRD corpus / error code dictionary
last_updated: 2026-05-09
owner: 吴忆锋
readers: [product, ui, dev, qa, business, ai]
---

# Error Code Dictionary 错误码与提示字典

## 1. 文档定位

本文沉淀已确认的错误码 / 错误类型索引。完整用户文案详见 common/errors.md；模块内详细规则仍以模块文档为准。

## 2. 已确认错误码 / 错误类型

| Code / Type | 模块 | 说明 | 处理 | 来源 |
|---|---|---|---|---|
| 31031 | Card PIN | PIN 设置失败时使用后端返回文案覆盖默认失败文案 | 展示后端文案 | card/manage/pin.md |
| FACE_QUALITY_TOO_POOR | KYC / Face | Face / KYC 错误码映射来源之一 | 按 KYC / Security 映射展示 | kyc/account-opening.md；security/face-authentication.md |
| USER_TIMEOUT | KYC / Face | Face 超时 / 用户超时相关错误 | 进入 Face Failed / Loading Failed 规则 | kyc/account-opening.md；security/face-authentication.md |
| SIMILARITY_FAILED | KYC / Face | Face comparison 相似度失败 | 按错误码映射展示 | kyc/account-opening.md |
| PROOF_DOCUMENT_MATCHING_FAILED | KYC / POA | POA 资料匹配失败 | 按 POA error code 映射展示 | kyc/account-opening.md |
| DATA_VERIFICATION_FAILED | KYC | 数据验证失败 | 按 KYC 错误码映射展示 | kyc/account-opening.md |
| USER_SUBMISSION_FAILED | KYC | 用户提交失败 | 按 KYC 错误码映射展示 | kyc/account-opening.md |
| DTC unknown error | Transaction / Card | DTCPay 返回当前错误码之外的其他错误 | Lark 报警，等待产品和渠道确认 | card/transaction-detail.md |
| FAIL / EXPIRED / incomplete / empty | Face Auth | DTC 返回失败、过期、不完整或空值 | 进入 Face Auth Failed Page | security/face-authentication.md |

## 3. 锁定类错误

| 场景 | 阈值 | 结果 | 来源 |
|---|---|---|---|
| OTP / Email OTP / Login Passcode / Face Auth | 24 小时内失败 5 次 | 锁定 20 分钟 | security/global-rules.md |
| OTP / Email OTP / Login Passcode / Face Auth | 24 小时内失败 10 次 | 锁定 24 小时 | security/global-rules.md |
| Face Auth / KYC API | 接口连续发起 20 次 | 锁定 20 分钟 | security/face-authentication.md；kyc/account-opening.md |

## 4. Sources

- (Ref: knowledge-base/common/errors.md)
- (Ref: knowledge-base/security/global-rules.md)
- (Ref: knowledge-base/kyc/account-opening.md)
- (Ref: knowledge-base/card/manage/pin.md)
- (Ref: knowledge-base/card/transaction-detail.md)
