---
module: changelog
feature: knowledge-gaps
version: "1.0"
status: active
source_doc: IMPLEMENTATION_PLAN.md
source_section: source-policy
last_updated: 2026-05-01
owner: 吴忆锋
---

# Knowledge Gaps 知识缺口与冲突记录

## 1. 文档定位

本文档用于集中记录知识库转译过程中发现的文档缺口、原文疑似异常、口径冲突和需要后续确认的信息。

功能正文应优先承载稳定事实；不确定事项集中放在本文档，避免污染事实来源正文。

## 2. Account / Login

| 编号 | 问题 | 影响范围 | 来源 | 当前处理 | 状态 |
|---|---|---|---|---|---|
| KG-LOGIN-001 | Login Page 原始 PRD Description 列从第 4 项开始，1-3 项仅存在于 UX 截图，缺少可结构化文字规则 | Login Page / 页面元素 | AIX Card 注册登录需求V1.0 / 7.2.4 Login Page | 正文保留截图与已知结构化规则；缺失项不脑补 | open |
| KG-LOGIN-002 | 账号不存在 / 未注册提示为中文原文：`您输入的账号信息有误，请检查或注册新账号。`，英文最终文案缺失 | Login Page / 文案 | AIX Card 注册登录需求V1.0 / 7.2.4 Login Page | 正文保留中文原文，不替换为英文推测 | open |
| KG-LOGIN-003 | `Phone number must be at least 6 digits` 来自当前知识库旧内容，需确认是否为最终翻译文案 | Login Page / Phone 校验 | 当前知识库旧版 login.md | 正文保留该提示并标注来源为当前知识库旧内容 | open |
| KG-LOGIN-004 | 中国和中国台湾选项隐藏规则需确认由后端过滤还是前端过滤 | Select Country Page | AIX Card 注册登录需求V1.0 / 7.2.4.1 Select Country Page | 正文仅写“隐藏”，不判断前后端责任 | open |
| KG-LOGIN-005 | Android 指纹原文出现“若协议已全部勾选”，疑似串入注册协议逻辑 | Biometric Login / Android Fingerprint | AIX Card 注册登录需求V1.0 / 7.2.5 Biometric 登录 | 正文不采纳该疑似串文；保留为缺口记录 | open |
| KG-LOGIN-006 | Enable BIO 的系统授权差异、权限弹窗样式、跳转设置页方式需结合 iOS / Android 实现确认 | Enable BIO Page | AIX Card 注册登录需求V1.0 / 7.2.7 Enable BIO Page | 正文只保留“已授权 / 未授权”业务规则 | open |

## 3. Account / Registration

| 编号 | 问题 | 影响范围 | 来源 | 当前处理 | 状态 |
|---|---|---|---|---|---|
| KG-REG-001 | Registration Email 最长 103 字符，但 Login Email 最长 254 字符，二者口径不一致 | Registration / Login / Email 字段 | AIX Card 注册登录需求V1.0 / 7.1.4；7.2.4 | 正文分别保留原文，不统一改写 | open |
| KG-REG-002 | 协议默认勾选状态存在“待合规确定”口径，需确认最终是否默认勾选 | Registration / 协议同意 / 合规 | AIX Card 注册登录需求V1.0 / 7.1.4 | 正文按最新结构写必选协议，默认状态不扩展解释 | open |
| KG-REG-003 | `Privacy Policy test` 疑似原文笔误，需确认最终页面文案是否为 `Privacy Policy` | Registration / 协议链接 | AIX Card 注册登录需求V1.0 / 7.1.4 | 正文保留原文字段并标注来源 | open |
| KG-REG-004 | Set Password / Re-enter Password 的中文标题是否需要最终英文文案，原文存在中文“设置密码” | Registration / 密码设置页 | AIX Card 注册登录需求V1.0 / 7.1.6 / 7.1.7 | 正文保留原文，不自行翻译 | open |

## 4. Account / Password Reset

| 编号 | 问题 | 影响范围 | 来源 | 当前处理 | 状态 |
|---|---|---|---|---|---|
| KG-PWD-001 | Reset Password Page 的输入字段类型、字段名和格式规则原文未明确 | Password Reset / Reset Password Page | AIX Card 注册登录需求V1.0 / 7.3.3 | 正文使用 `resetInput` 作为占位能力名，并明确原文未定义字段类型 | open |
| KG-PWD-002 | Reset Password Page 输入不合法或为空时的具体错误文案原文未明确 | Password Reset / 异常文案 | AIX Card 注册登录需求V1.0 / 7.3.3 | 正文仅写 Next 不可点击或阻止继续，不补具体文案 | open |
| KG-PWD-003 | 身份验证流程在 Password Reset 中具体采用 OTP、Email OTP 或其他方式，原文仅指向 Security 文档 | Password Reset / Identity Verification | AIX Card 注册登录需求V1.0 / 7.3.4；AIX Security 身份认证需求V1.0 | 正文引用 Security，不在 Account 中重复定义 | open |
| KG-PWD-004 | 密码重置成功后的成功提示、跳转页或登录页落点原文未明确，只明确强制登出并需新密码重新登录 | Password Reset / 成功结果 | AIX Card 注册登录需求V1.0 / 7.3.5 | 正文只写强制登出和新密码重新登录 | open |

## 5. Security / API Reference

| 编号 | 问题 | 影响范围 | 来源 | 当前处理 | 状态 |
|---|---|---|---|---|---|
| KG-SEC-API-001 | `tokenAuthType` 为必填字段，但原文未说明枚举值、含义和与业务场景的映射关系 | Security API / Generate Verification URL | AIX Security 身份认证需求V1.0 / 9.1.1 | 正文保留字段，并标注“原文未给出说明” | open |
| KG-SEC-API-002 | Generate Verification URL 接口未列出失败响应、错误码、重试规则和幂等要求 | Security API / Generate Verification URL | AIX Security 身份认证需求V1.0 / 9.1.1 | 正文不补失败处理，仅记录缺口 | open |
| KG-SEC-API-003 | Query Auth Result 接口未列出 HTTP 失败、系统异常、网络异常、超时等响应字段 | Security API / Query Auth Result | AIX Security 身份认证需求V1.0 / 9.1.2 | 正文仅保留 status = INCOMPLETE / PASS / FAIL | open |
| KG-SEC-API-004 | `INCOMPLETE` 同时包含未验证和验证中，原文未拆分具体状态 | Security API / Query Auth Result / 状态映射 | AIX Security 身份认证需求V1.0 / 9.1.2 | 正文按原文保留，不拆分新状态 | open |
| KG-SEC-API-005 | 原文 `10.1 passport error code` 标题与错误码内容存在口径疑问，错误码多为活体 / 人脸相关错误 | Security API / Error Code Mapping | AIX Security 身份认证需求V1.0 / 10.1 | 正文说明原文标题与内容，不自行重命名事实来源 | open |
| KG-SEC-API-006 | 原文 `9.2 外部接口地址` 仅写“Master sub account 设计方案”，没有可结构化接口地址或字段 | Security API / External API Address | AIX Security 身份认证需求V1.0 / 9.2 | 正文保留缺口，不补接口地址 | open |
| KG-SEC-API-007 | 旧版 api-reference 中“验证处理规则需要列出10次，以及验证错误4、5次提示语优化”属于待定事项，需确认是否仍有效 | Security API / 错误提示规则 | 旧版 knowledge-base/security/api-reference.md / 11 待定事项 | 迁移至 gaps，不放入功能正文 | open |
