---
module: account
feature: password-reset
version: "1.0"
status: active
source_doc: 历史prd/AIX Card 注册登录需求V1.0.docx
source_section: 7.3 忘记密码流程页面
last_updated: 2026-05-01
owner: 吴忆锋
depends_on:
  - account/_index
  - registration
  - login
  - security/global-rules
  - security/otp-verification
  - security/email-otp-verification
  - security/login-passcode-verification
  - security/biometric-verification
  - _meta/status-dictionary
  - _meta/writing-standard
readers: [product, ui, dev, qa, business, ai]
---

# Password Reset 忘记密码流程

## 1. 功能定位

Password Reset 用于用户忘记登录密码时，通过邮箱或手机号发起身份验证，并在验证通过后重新设置登录密码。

密码重置成功后，系统必须强制登出当前账户，用户需使用新密码重新登录；同时已开启的 BIO 需要自动关闭。

## 2. 适用范围

| 维度 | 规则 | 来源 | 备注 |
|------|------|------|------|
| 用户状态 | 已注册用户 | AIX Card 注册登录需求V1.0 / 7.3 忘记密码流程页面 | 未注册账号需按登录 / 注册逻辑处理 |
| 入口 | Login Page 的 Forgot Password 入口 | AIX Card 注册登录需求V1.0 / 7.3 | 当前知识库按登录页入口处理 |
| 重置方式 | Email / Phone 输入后进入身份验证流程 | AIX Card 注册登录需求V1.0 / 7.3.3 | Reset Password Page 复用登录输入能力 |
| 身份认证 | OTP / Email OTP | AIX Card 注册登录需求V1.0 / 7.3.4；AIX Security 身份认证需求V1.0 | 认证逻辑由 Security 模块管理 |
| BIO 处理 | 重置密码成功后自动关闭 BIO | AIX Card 注册登录需求V1.0 / 2025-11-11 变更记录；7.3.1 | 必须清除 BIO 信息 |

## 3. 前置条件

| 条件 | 说明 | 来源 |
|------|------|------|
| 用户点击 Forgot Password | 从 Login Page 进入 Password Reset | 当前知识库登录页结构 |
| 用户输入邮箱或手机号 | Reset Password Page 支持 Email / Phone 切换 | AIX Card 注册登录需求V1.0 / 7.3.3 |
| 输入合法且非空 | Next 才可点击 | AIX Card 注册登录需求V1.0 / 7.3.3 |
| 身份验证通过 | 通过后进入设置密码页 | AIX Card 注册登录需求V1.0 / 7.3.4 |

## 4. 标准流程

```text
┌──────────────┐
│ Login Page   │
└──────┬───────┘
       │ 点击 Forgot Password
       ▼
┌─────────────────────┐
│ Reset Password Page │
│ Email / Phone       │
└────────┬────────────┘
         │ 输入合法 + Next
         ▼
┌─────────────────────┐
│ Identity Verification│
│ OTP / Email OTP     │
└────────┬────────────┘
         │ 验证成功
         ▼
┌─────────────────────┐
│ Set Password Page   │
└────────┬────────────┘
         │ 新密码设置成功
         ▼
┌──────────────────────────────┐
│ Reset Success                │
│ Force logout                 │
│ Disable BIO                  │
└────────┬─────────────────────┘
         ▼
┌─────────────────────┐
│ Login Page          │
└─────────────────────┘
```

## 5. 页面关系图

页面关系以 ASCII 图为主。原始页面概览截图仅用于追溯，不作为主规则表达。

```text
Login Page
  └─ Forgot Password → Reset Password Page

Reset Password Page
  ├─ Back → Login Page
  ├─ Email tab
  │   └─ Email valid + Next → Identity Verification
  └─ Phone tab
      ├─ Country Code → Select Country Page → Reset Password Page
      └─ Phone valid + Next → Identity Verification

Identity Verification
  ├─ Success → Set Password Page
  └─ Failed / Locked → Security module error handling

Set Password Page
  ├─ Back → Confirm Exit Popup
  └─ Password valid + Next → Reset Success

Reset Success
  ├─ Force logout
  ├─ Disable BIO
  └─ Return to Login Page
```

## 6. 页面与交互规则

### 6.1 原始 PRD 参考截图

> 以下截图来自原始飞书 PRD，仅用于追溯原始设计上下文。  
> 页面关系以本文 ASCII 图和结构化规则为准。

| 内容 | 截图 |
|------|------|
| 忘记密码页面概览 | `../assets/account/image40.jpeg` |
| Reset Password Page UX | `../assets/account/image41.jpeg` |

### 6.2 Reset Password Page

| 元素 | 类型 | 展示条件 | 交互规则 | 异常 |
|------|------|----------|----------|------|
| Back | Navigation | 默认展示 | 点击返回上一级页面 | 无 |
| Email / Phone 切换 | Tab | 默认展示 | 默认选中 Email；用户可切换 Phone | 切换保留规则需确认 |
| Email 输入框 | TextInput | Email tab | 最长 254 字符；校验邮箱格式；不能为空 | `Email format is invalid`；`Email should not be empty` |
| Country Code | Selector | Phone tab | 点击进入 Country Select Page | 隐藏规则复用 Login |
| Phone 输入框 | TextInput | Phone tab | 仅允许数字；最长 20 位 | 手机格式规则需与 Login / ME 统一 |
| Next | Button | 输入合法且非空 | 点击进入身份验证流程页面 | 账号不存在、认证失败、锁定等见 Security / Login |

### 6.3 Identity Verification

身份验证流程由 Security 模块统一管理。

| 元素 | 类型 | 展示条件 | 交互规则 | 异常 |
|------|------|----------|----------|------|
| OTP / Email OTP | Security Page | Reset Password Page 点击 Next 后 | 验证成功后进入 Set Password Page | 失败、锁定、重发限制见 Security 模块 |

### 6.4 Set Password Page

设置密码页复用 Registration 中的 Set Password Page。

| 元素 | 类型 | 展示条件 | 交互规则 | 异常 |
|------|------|----------|----------|------|
| Password | PasswordInput | 身份验证成功后 | 8-32 字符；大小写字母 + 数字 + 符号；支持显示 / 隐藏切换 | 密码复杂度错误提示 |
| Next | Button | 密码校验通过 | 点击提交新密码 | 创建失败 / 系统异常 |

密码规则以 `registration.md → Set Password Page` 为准。

## 7. 状态机

### 7.1 密码重置状态

```text
┌──────────────┐
│ Reset Start  │
└──────┬───────┘
       │ 输入账号并提交
       ▼
┌──────────────┐
│ Verifying    │
└──────┬───────┘
       │ 验证成功
       ▼
┌──────────────┐
│ Set Password │
└──────┬───────┘
       │ 新密码设置成功
       ▼
┌──────────────┐
│ Reset Done   │
└──────────────┘
```

### 7.2 BIO 状态变化

```text
┌──────────────┐
│ BIO Enabled  │
└──────┬───────┘
       │ 密码重置成功
       ▼
┌──────────────┐
│ BIO Disabled │
└──────────────┘
```

## 8. 字段与接口依赖

| 字段 / 能力 | 用途 | 读/写 | 来源 | 备注 |
|-------------|------|------|------|------|
| email | 找回密码账号 | 读 | Reset Password Page | 最长 254 字符 |
| phone | 找回密码账号 | 读 | Reset Password Page | 仅数字，最长 20 位 |
| countryCode | 手机国家 / 地区区号 | 读 | Reset Password Page | 复用 Login Country Select |
| verificationResult | 身份验证结果 | 读 | Security 模块 | 成功后进入 Set Password Page |
| newPassword | 新登录密码 | 写 | Set Password Page | 复用注册密码规则 |
| bioEnabled | BIO 状态 | 写 | Password Reset Success | 重置成功后必须关闭 |
| loginSession | 登录态 | 写 | Password Reset Success | 重置成功后强制登出 |

## 9. 异常与失败处理

| 场景 | 触发条件 | 用户提示 | 系统动作 | 最终状态 | 来源 |
|------|----------|----------|----------|----------|------|
| Email 为空 | Email tab 未输入 | `Email should not be empty` | 阻止 Next | 留在 Reset Password Page | AIX Card 注册登录需求V1.0 / 7.3.3 |
| Email 格式错误 | Email 格式不合法 | `Email format is invalid` | 阻止 Next | 留在 Reset Password Page | AIX Card 注册登录需求V1.0 / 7.3.3 |
| Phone 格式错误 | Phone 不满足规则 | 待统一 | 阻止 Next | 留在 Reset Password Page | AIX Card 注册登录需求V1.0 / 7.3.3 |
| 身份验证失败 | OTP / Email OTP 验证失败 | 按 Security 模块规则 | 阻止进入设置密码页 | 留在认证流程 | AIX Security 身份认证需求V1.0 |
| 身份验证锁定 | 失败次数达到锁定阈值 | 按 Security 模块规则 | 进入锁定处理 | 认证流程中断 | AIX Security 身份认证需求V1.0 |
| 新密码不合法 | 密码不满足复杂度 | 按 Registration 密码规则 | 阻止提交 | 留在 Set Password Page | AIX Card 注册登录需求V1.0 / 7.1.6 |
| 密码重置成功 | 后端成功更新密码 | 强制登出，清除 BIO | 用户需重新登录 | Login Page | AIX Card 注册登录需求V1.0 / 7.3.1；7.3.5 |

## 10. 风控 / 合规边界

| 边界 | 规则 | 影响 | 来源 |
|------|------|------|------|
| 身份验证 | 找回密码必须完成 OTP / Email OTP 等身份验证 | 防止账号被盗重置 | AIX Card 注册登录需求V1.0 / 7.3.4；Security 模块 |
| 强制登出 | 密码重置成功后强制登出当前账户 | 旧登录态失效 | AIX Card 注册登录需求V1.0 / 7.3.5 |
| BIO 自动关闭 | 密码重置成功后清除 BIO 信息，已开启 BIO 自动关闭 | 防止旧 BIO 凭证继续使用 | AIX Card 注册登录需求V1.0 / 2025-11-11 变更记录 |
| 密码复杂度 | 新密码复用注册密码规则 | 账户安全 | AIX Card 注册登录需求V1.0 / 7.1.6 |

## 11. 多角色阅读视角

### UI 视角

- 页面关系以 ASCII 图为准，原页面概览截图只做追溯证据。
- 重点页面：Reset Password Page、Identity Verification、Set Password Page。

### 开发视角

- 密码重置成功后必须同时处理：更新密码、强制登出、关闭 BIO。
- 身份验证规则复用 Security，不在本文件重复定义 OTP 失败次数与锁定规则。

### 测试视角

- 必测 Email 找回、Phone 找回、身份验证成功 / 失败 / 锁定、密码复杂度、重置成功后旧密码不可登录、新密码可登录、BIO 自动关闭。

### 业务视角

- 忘记密码是账户找回能力，不改变账户主体身份。
- 重置成功后用户必须重新登录，已开启的 BIO 需重新设置。

### AI 复用视角

- 新 PRD 涉及密码重置、强制登出、关闭 BIO 时，应优先引用本文件。
- 不得省略“重置成功后自动关闭 BIO”规则。

## 12. 待确认事项

| 问题 | 影响范围 | 建议确认人 | 状态 |
|------|----------|------------|------|
| Reset Password Page 的 Phone 格式校验是否完全复用 Login Page，需确认最终口径 | Reset Password / Login | 产品 / 技术 | open |
| Reset Password Page 的账号不存在提示文案需确认英文最终口径 | Reset Password | 产品 / UI | open |
| 密码重置成功后是否需要展示成功页 / Toast，当前文档只明确强制登出和重新登录 | Reset Password Result | 产品 / UI | open |
| 关闭 BIO 的系统动作需确认：仅清除本地凭证，还是同时后端关闭该设备 BIO 开关 | Reset Password / Biometric | 产品 / 技术 | open |
| Set Password 是否仍存在确认密码页，需结合最新 UX 确认 | Reset Password / Registration | 产品 / UI / 技术 | open |

## 13. 来源引用

- (Ref: 历史prd/AIX Card 注册登录需求V1.0.docx / 2025-11-11 需求变更日志 / V1.0)
- (Ref: 历史prd/AIX Card 注册登录需求V1.0.docx / 7.3.1 功能说明 / V1.0)
- (Ref: 历史prd/AIX Card 注册登录需求V1.0.docx / 7.3.2 页面概览 / V1.0)
- (Ref: 历史prd/AIX Card 注册登录需求V1.0.docx / 7.3.3 Reset Password Page / V1.0)
- (Ref: 历史prd/AIX Card 注册登录需求V1.0.docx / 7.3.4 身份验证流程页面 / V1.0)
- (Ref: 历史prd/AIX Card 注册登录需求V1.0.docx / 7.3.5 设置密码页 / V1.0)
- (Ref: knowledge-base/account/registration.md)
- (Ref: knowledge-base/security/global-rules.md)
