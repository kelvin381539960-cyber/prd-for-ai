---
module: security
description: 身份认证公共能力层，覆盖 AIX 自有认证、设备生物识别、DTC 侧活体认证与跨业务场景认证规则
version: "1.0"
status: active
source_docs:
  - 历史prd/AIX Security 身份认证需求V1.0 (1).docx
source_sections:
  - 6 客户端对接方式
  - 7.1 认证方式 & 限制
  - 7.2 不同场景的验证方式
  - 7.3 验证优先级
  - 7.4 验证有效期说明
  - 7.5 身份认证状态机
last_updated: 2026-05-01
owner: 吴忆锋
countries: [VN, PH, AU]
depends_on:
  - _meta/status-dictionary
  - _meta/error-code-dictionary
  - _meta/limits-and-rules
  - _meta/compliance-boundaries
  - account
  - integrations/dtc
  - integrations/aai
readers: [product, ui, dev, qa, business, ai]
---

# Security 身份认证模块

## 1. 模块定位

Security 模块是 AIX 的身份认证公共能力层，沉淀 OTP、Email OTP、Login Passcode、Biometric、DTC Face Authentication、认证有效期、认证状态机、通用认证弹窗等事实。

本模块供 Account、Wallet、Card、Transaction 等业务模块复用。业务模块不应重复定义认证方式、认证优先级、认证失败次数、认证有效期等规则。

## 2. 功能清单

| 功能 / 文件 | 状态 | 内容 | 来源 |
|-------------|------|------|------|
| [global-rules.md](global-rules.md) | active | 认证方式、场景矩阵、优先级、有效期、状态机、通用弹窗 | AIX Security 身份认证需求V1.0 / 6-7 |
| [otp-verification.md](otp-verification.md) | active | OTP 认证页面（短信验证码） | AIX Security 身份认证需求V1.0 |
| [email-otp-verification.md](email-otp-verification.md) | active | Email OTP 认证页面（邮箱验证码） | AIX Security 身份认证需求V1.0 |
| [login-passcode-verification.md](login-passcode-verification.md) | active | Login Passcode 认证页面（密码验证） | AIX Security 身份认证需求V1.0 |
| [biometric-verification.md](biometric-verification.md) | active | Biometric 设备生物识别认证 | AIX Security 身份认证需求V1.0 |
| [face-authentication.md](face-authentication.md) | active | DTC 侧活体识别 / 人脸比对认证 | AIX Security 身份认证需求V1.0 |
| [api-reference.md](api-reference.md) | active | 外部接口依赖 + 错误码映射 | AIX Security 身份认证需求V1.0 |

## 3. 适用范围

| 维度 | 规则 | 来源 | 备注 |
|------|------|------|------|
| 国家 / 地区 | VN / PH / AU | AIX Security 身份认证需求V1.0 | 需后续同步至 `_meta/countries-and-regions.md` |
| 接入方式 | AIX 客户端通过 H5 内嵌 WebView 接入身份认证服务 | global-rules.md / 6 | 覆盖 AIX 自有认证与 DTC 身份核验服务 |
| 认证类型 | OTP / Email OTP / Login Passcode / Biometric / Face Authentication | global-rules.md / 7.1 | 业务模块按场景复用 |
| 认证场景 | 注册、登录、BIO 授权、手机号、密码、钱包地址、兑换、转账、提现、申卡、敏感卡信息、激活卡、PIN 等 | global-rules.md / 7.2 | 部分场景走 DTC，部分走 AIX 自有认证 |

## 4. 模块依赖

| 依赖对象 | 依赖内容 | 说明 |
|----------|----------|------|
| `_meta/status-dictionary.md` | IVS Status | INITIAL / VALIDATING / DONE / EXPIRED |
| `_meta/error-code-dictionary.md` | 错误提示 | Too Many Attempts、Verification Expired 等 |
| `_meta/limits-and-rules.md` | 次数、锁定、有效期 | OTP、Email OTP、Passcode、Face Authentication 等限制 |
| `_meta/compliance-boundaries.md` | KYC / Face / 资金场景认证边界 | Withdraw、Card Application、Sensitive Card Info 等 |
| `account` | 登录态、账户状态、Device ID、BIO 前提 | Account 依赖 Security，Security 也读取 Account 状态 |
| `integrations/dtc` | DTC 侧 Document Verification / Liveness / Face Comparison | KYC、申卡、提现、卡敏感信息等场景 |
| `integrations/aai` | 外部身份验证能力 | 证件、活体、人脸相关能力后续需拆清 |

## 5. 认证方式总览

| 认证方式 | Type | 安全程度 | 定义 | 限制规则 | 锁定方式 |
|----------|------|----------|------|----------|----------|
| OTP | 你拥有的 | 高 | 4 位数字密码，通过短信发送默认当前用户账户绑定的手机号码发送 | 24 小时内失败 5 次 → 锁定 20 分钟；24 小时内失败 10 次 → 锁定 24 小时 | 全局共享锁定 |
| Email OTP | 你拥有的 | 中 | 4 位数字密码，通过邮件发送 | 24 小时内失败 5 次 → 锁定 20 分钟；24 小时内失败 10 次 → 锁定 24 小时 | 场景隔离锁定 |
| Login Passcode | 你知道的 | 高 | 大小写英文 + 数字 + 符号 | 24 小时内失败 5 次 → 锁定 20 分钟；24 小时内失败 10 次 → 锁定 24 小时 | 场景隔离锁定 |
| Biometric | 你本人的 | 中 | 根据用户设备中的人脸 / 指纹等验证用户 | 无失败次数限制。前端返回失败 → 禁用该功能至用户重新授权 | 设备失败 → 禁用至重新授权 |
| Face Authentication | 你本人的 | 高 | DTC 侧活体验证 + 人脸相似度验证。当前阈值：活体验证 90，人脸相似度 70 | 24 小时内失败 5 次 → 锁定 20 分钟；24 小时内失败 10 次 → 锁定 24 小时 | 场景隔离锁定 |

## 6. 场景矩阵总览

| 场景 | DTC | AIX | 备注 |
|------|-----|-----|------|
| 注册 | ❌ | EMAIL_OTP | Account 注册依赖 |
| 登录 | ❌ | OTP / EMAIL_OTP / Login_PASSCODE / BIO | Bio 登录目前可直接跳过其他认证 |
| Biometric 授权 | ❌ | Login_PASSCODE | 完成手动登录后 5 分钟内免再次身份认证 |
| 首次绑定手机号 | ❌ | OTP |  |
| 更换手机号 | ❌ | OTP |  |
| 修改密码 | ❌ | Login_PASSCODE / OTP / IVS_DEVICE_BIOMETRICS |  |
| 忘记密码 | ❌ | OTP / EMAIL_OTP |  |
| 开户 + KYC | Document Verification / Liveness Detection / Face Comparison | ❌ | DTC 侧认证 |
| 钱包地址 | ❌ | OTP / EMAIL_OTP / IVS_DEVICE_BIOMETRICS |  |
| 充值 | ❌ | ❌ |  |
| 兑换 | ❌ | OTP / EMAIL_OTP / IVS_DEVICE_BIOMETRICS |  |
| 转账 | ❌ | OTP / EMAIL_OTP / IVS_DEVICE_BIOMETRICS |  |
| Crypto Withdraw | Face Authentication | ❌ | DTC 侧认证 |
| Fiat Withdraw | Face Authentication | ❌ | DTC 侧认证 |
| 卡申请 | Face Authentication | ❌ | DTC 侧认证 |
| 查看卡敏感信息 | Face Authentication | ❌ | DTC 侧认证 |
| 激活卡 | Face Authentication | ❌ | DTC 侧认证 |
| 设置 PIN | Face Authentication | ❌ | DTC 侧认证 |
| 重置 PIN | Face Authentication | ❌ | DTC 侧认证 |
| 冻结卡 | ❌ | ❌ |  |
| 解冻卡 | ❌ | OTP / IVS_DEVICE_BIOMETRICS |  |
| 注销卡 | ❌ | ❌ |  |

## 7. 认证优先级

| 优先级 | 认证方式 | 条件说明 |
|--------|----------|----------|
| 1 | Biometric | 必须满足：前端未清除本地生物识别凭证 |
| 2 | Login Passcode |  |
| 3 | OTP | 用户已绑定手机号 |
| 4 | Email OTP |  |

若当前认证方式不满足使用条件，系统将自动跳过，并进入下一优先级的认证方式。

## 8. 认证有效期与状态机

### 8.1 有效期

| 类型 | 有效期 | 免重认证逻辑 |
|------|--------|--------------|
| DTC 活体识别 | 5 分钟 | 根据 DTC 返回的 token 有效期判断。5 分钟内重复调用 → 免再次活体。该免重认证逻辑支持跨不同业务场景生效 |
| AIX 自有认证 | 无缓存 | 每次操作均需重新认证 |
| 验证挑战中有效期 | 10 分钟 | 发起身份验证请求后生成 Challenge，会话 10 分钟内有效 |
| 验证挑战后有效期 | 10 分钟 | 身份验证成功后生成短期认证凭证，用于后续业务操作 |

### 8.2 IVS 状态机

| 状态值 | 说明 | 是否终态 |
|--------|------|----------|
| INITIAL | 发起挑战初始化，create challenge | 否 |
| VALIDATING | 验证中 | 否 |
| DONE | 验证成功完成 | 是 |
| EXPIRED | 已过期，流程终止 | 是 |

```text
┌──────────┐
│ INITIAL  │
└────┬─────┘
     ▼
┌──────────┐
│VALIDATING│
└────┬─────┘
     ├──────────── 成功 ────────────┐
     ▼                              ▼
┌──────────┐                 ┌──────────┐
│ EXPIRED  │                 │ DONE     │
└──────────┘                 └──────────┘
```

## 9. 通用页面与弹窗

| 能力 | 场景 | 用户提示 / 动作 | 来源 |
|------|------|----------------|------|
| IVS Verification Expired Popup | 用户完成 IVS 后返回业务流程，提交时认证已过期 | Title: `Verification Expired`; Button: `Try Again` | global-rules.md / 7.6.1 |
| Too Many Attempts Popup | 认证失败次数达到锁定阈值 | Title: `Too Many Attempts`; Button: `Try again later` | global-rules.md / 7.6.2 |
| BIO 设备锁定提示 | 设备生物识别被系统暂时禁用 | 提示用户解锁设备后再尝试 | global-rules.md / 7.6.2 |
| Account interception popup | 账户被 banned，无法发起身份认证流程 | 点击按钮关闭弹窗，留在当前页 | global-rules.md / 7.6.3 |

## 10. 多角色阅读视角

### UI 视角

- 关注 OTP、Email OTP、Login Passcode、Biometric、Face Authentication、通用认证过期和失败弹窗。
- 所有页面截图保留在 `knowledge-base/assets/security/`。

### 开发视角

- 关注认证方式选择、优先级跳转、Challenge 状态、有效期、失败锁定、DTC 与 AIX 自有认证边界。
- 业务模块不得私自实现认证规则，应引用 Security 模块。

### 测试视角

- 覆盖每种认证方式主流程、失败次数、锁定时间、过期处理、方式降级、DTC 活体 5 分钟免重认证。
- 覆盖不同业务场景的认证矩阵。

### 业务视角

- Security 是卡、钱包、交易等敏感操作的前置安全能力。
- 需区分 AIX 自有认证与 DTC 侧身份核验。

### AI 复用视角

- 新 PRD 涉及敏感操作、身份验证、交易确认、申卡、提现、查看敏感卡信息时，必须优先引用本模块。
- 不得在新 PRD 中重复定义认证方式、优先级、锁定规则和有效期。

## 11. 待确认事项

| 问题 | 影响范围 | 建议确认人 | 状态 |
|------|----------|------------|------|
| DTC 活体识别“向 AIX 返回 5 分钟、DTC 实际 10 分钟”与“验证挑战后凭证 10 分钟”的产品表现边界需在具体业务模块中继续校准 | Card / Wallet / Transaction | 产品 / 技术 / DTC | open |
| AAI 与 DTC 在证件、活体、人脸能力上的边界需在 integrations/aai 与 integrations/dtc 中拆清 | KYC / Face / Card | 产品 / 技术 | open |
| 冻结卡、注销卡场景无需认证的业务原因不在当前文档中解释，后续卡模块重构时需确认是否仍然有效 | Card | 产品 / 技术 | open |

## 12. 来源引用

- (Ref: 历史prd/AIX Security 身份认证需求V1.0 (1).docx / 6 客户端对接方式 / V1.0)
- (Ref: 历史prd/AIX Security 身份认证需求V1.0 (1).docx / 7.1 认证方式 & 限制 / V1.0)
- (Ref: 历史prd/AIX Security 身份认证需求V1.0 (1).docx / 7.2 不同场景的验证方式 / V1.0)
- (Ref: 历史prd/AIX Security 身份认证需求V1.0 (1).docx / 7.3 验证优先级 / V1.0)
- (Ref: 历史prd/AIX Security 身份认证需求V1.0 (1).docx / 7.4 验证有效期说明 / V1.0)
- (Ref: knowledge-base/security/global-rules.md)
