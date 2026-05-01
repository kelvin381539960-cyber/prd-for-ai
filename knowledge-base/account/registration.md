---
module: account
feature: registration
version: "1.0"
status: active
source_doc: 历史prd/AIX Card 注册登录需求V1.0.docx
source_section: 7.1 注册功能
last_updated: 2026-05-01
owner: 吴忆锋
depends_on:
  - account/_index
  - security/email-otp-verification
  - _meta/countries-and-regions
  - _meta/status-dictionary
  - _meta/writing-standard
readers: [product, ui, dev, qa, business, ai]
---

# Registration 注册功能

## 1. 功能定位

Registration 用于新用户通过邮箱完成 AIX 账户注册。

注册主链路包括：Navigation Page → Registration Page → Email OTP → Set Password。用户创建密码后即视为注册成功，并自动登录。

AIX Tag 设置为注册后的可选引导能力。用户可以设置，也可以跳过；跳过不影响账户使用。

## 2. 适用范围

| 维度 | 规则 | 来源 | 备注 |
|------|------|------|------|
| 国家 / 地区 | VN / PH / AU | AIX Card 注册登录需求V1.0 / 5 国家线 | 注册模块当前沿用全局国家线 |
| 用户状态 | 未注册用户 | AIX Card 注册登录需求V1.0 / 7.1 注册功能 | 已注册邮箱不可重复注册 |
| 账户状态 | 创建密码成功后生成 UID，账户进入 Active | AIX Card 注册登录需求V1.0 / 6.2 账户说明 | AIX Tag 不再是注册成功前置条件 |
| 认证方式 | Email OTP | AIX Card 注册登录需求V1.0 / 7.1.5；AIX Security 身份认证需求V1.0 | Email OTP 由 Security 模块统一管理 |
| AIX Tag | 可选设置，可跳过 | AIX Card 注册登录需求V1.0 / 2025-11-18 变更记录 | 一旦设置通常不可更改 |

## 3. 前置条件

| 条件 | 说明 | 来源 |
|------|------|------|
| 用户未完成注册 | 注册流程面向新用户 | AIX Card 注册登录需求V1.0 / 7.1 |
| 用户可访问 App Navigation Page | 用户通过入口点击 `Create account` 进入注册 | AIX Card 注册登录需求V1.0 / 7.1.3 |
| 注册邮箱未被占用 | 邮箱全局唯一，不允许重复注册或绑定 | AIX Card 注册登录需求V1.0 / 6.2.5 |
| 用户同意必选协议 | 必选协议勾选后才允许进入 Email OTP | AIX Card 注册登录需求V1.0 / 7.1.4 |

## 4. 标准流程

```text
┌─────────────────┐
│ Navigation Page │
└────────┬────────┘
         │ 点击 Create account
         ▼
┌─────────────────────┐
│ Registration Page   │
│ Email + Referral +  │
│ Agreement           │
└────────┬────────────┘
         │ Email 合法 + 协议已勾选 + Next
         ▼
┌─────────────────────┐
│ Email OTP Page      │
│ security module     │
└────────┬────────────┘
         │ OTP 验证成功
         ▼
┌─────────────────────┐
│ Set Password Page   │
└────────┬────────────┘
         │ 密码创建成功
         ▼
┌─────────────────────┐
│ Account Registered  │
│ UID generated       │
│ Status = Active     │
└────────┬────────────┘
         │ 自动登录
         ▼
┌──────────────────────────────┐
│ Optional Set AIX Tag Guide   │
└─────────────┬────────────────┘
              │
       ┌──────┴──────────┐
       │                 │
       ▼                 ▼
┌──────────────┐   ┌──────────────┐
│ Set AIX Tag  │   │ Skip / Close │
└──────┬───────┘   └──────┬───────┘
       │ 创建成功          │ 不设置 Tag
       ▼                 ▼
┌──────────────────────────────┐
│ Home                         │
└──────────────────────────────┘
```

## 5. 页面关系图

页面关系以 ASCII 图为主。原始页面概览截图仅用于追溯，不作为主规则表达。

```text
Navigation Page
  ├─ Create account → Registration Page
  └─ I already have an account → Login Page

Registration Page
  ├─ Terms of service → Agreement Detail
  ├─ Privacy Policy → Agreement Detail
  ├─ Login → Login Page
  └─ Next → Email OTP Page

Email OTP Page
  ├─ Verify success → Set Password Page
  └─ Verify failed / locked → Security module error handling

Set Password Page
  ├─ Back → Confirm Exit Popup
  ├─ Password valid + Next → Account Registered + Auto Login
  └─ Server error → System busy / server error handling

Optional Set AIX Tag Guide
  ├─ Set Tag → Set AIX Tag Page
  └─ Skip / Close → Home

Set AIX Tag Page
  ├─ Confirm available tag → Confirm your X-Tag Popup → Home
  ├─ Close / Skip → Home
  └─ Network / server / duplicate tag → Error handling
```

## 6. 页面与交互规则

### 6.1 原始 PRD 参考截图

> 以下截图来自原始飞书 PRD，仅用于追溯原始设计上下文。  
> 页面关系以本文 ASCII 图和结构化规则为准。

| 内容 | 截图 |
|------|------|
| 注册流程说明 | `../assets/account/image16.jpeg` |
| 注册页面概览 | `../assets/account/image17.jpeg` |
| Navigation Page UX | `../assets/account/image18.png` |
| Navigation Page Description | `../assets/account/image19.png` |
| Registration Page UX | `../assets/account/image20.png` |
| Registration Page Description | `../assets/account/image21.png` |
| Set Password Page UX | `../assets/account/image22.png` |
| Set Password Page Description | `../assets/account/image23.png` |
| Re-enter Password Page UX | `../assets/account/image24.png` |
| Set AIX Tag Page UX | `../assets/account/image25.png` |
| Set AIX Tag Description | `../assets/account/image26.png`, `../assets/account/image27.png` |

### 6.2 Navigation Page

| 元素 | 类型 | 展示条件 | 交互规则 | 异常 |
|------|------|----------|----------|------|
| 推广引导区 | Content | 默认展示 | 一期写死，后续需在 OBOSS 配置实现 | 无 |
| Create account | Button | 默认展示 | 点击进入 Registration Page | 无 |
| I already have an account | Button | 默认展示 | 点击进入 Login Page | 无 |

### 6.3 Registration Page

| 元素 | 类型 | 展示条件 | 交互规则 | 异常 |
|------|------|----------|----------|------|
| Email 输入框 | TextInput | 默认展示 | 最长 254 字符；实时校验邮箱格式；非空校验 | `Email format is invalid`；`Email should not be empty` |
| Referral code 输入框 | TextInput | 默认展示，可选 | 3-30 字符；仅英文大小写 + 数字；区分大小写 | `Referral code does not exist` |
| Terms of service | Checkbox + Link | 默认展示 | 必选协议；点击链接展示协议全文 | 协议获取失败：`Something went wrong. Please try again later` |
| Privacy Policy | Checkbox + Link | 默认展示 | 必选协议；点击链接展示协议全文 | 协议获取失败：`Something went wrong. Please try again later` |
| Next | Button | Email 合法 + 必选协议已同意 | 点击后进入 Email OTP Page | 邮箱已注册、推荐码不存在、频控、系统异常 |
| Login | Button | 默认展示 | 点击进入 Login Page | 无 |

### 6.4 Email OTP Page

Email OTP Page 由 Security 模块统一管理。

| 元素 | 类型 | 展示条件 | 交互规则 | 异常 |
|------|------|----------|----------|------|
| Email OTP | Security Page | Registration Page 点击 Next 后 | 进入邮箱 OTP 验证流程 | 失败、锁定、重发限制见 `security/email-otp-verification.md` |

### 6.5 Set Password Page

| 元素 | 类型 | 展示条件 | 交互规则 | 异常 |
|------|------|----------|----------|------|
| Back | Navigation | 默认展示 | 点击弹出 Confirm Exit Popup | 用户选择 Leave 返回入口页 |
| Title | Text | 默认展示 | 固定文案：设置密码 | 无 |
| Password | PasswordInput | 默认展示 | 8-32 字符；支持大小写字母、数字、符号；支持显示 / 隐藏切换 | 按规则展示密码错误提示 |
| Next | Button | 密码所有校验通过 | 点击完成密码设置；创建成功后注册完成并自动登录 | 创建失败：`System busy, please try again later` |

密码校验规则：

| 校验项 | 规则 | 错误提示 |
|--------|------|----------|
| 长度 | 8-32 字符 | `Password must be 8-32 characters long` |
| 小写字母 | 至少 1 个 a-z | `Must include at least 1 lowercase letter` |
| 大写字母 | 至少 1 个 A-Z | `Must include at least 1 uppercase letter` |
| 数字 | 至少 1 个 0-9 | `Must include at least 1 number` |
| 符号 | 至少 1 个符号 | `Must include at least 1 symbol` |

### 6.6 Optional Set AIX Tag Page

| 元素 | 类型 | 展示条件 | 交互规则 | 异常 |
|------|------|----------|----------|------|
| Title / Subtitle | Text | 注册成功后可选展示 | 固定文案，引导用户设置唯一 ID | 无 |
| AIX Tag 输入框 | TextInput | 用户选择设置 Tag | 固定前缀 `@` + 自定义部分；3-30 字符；支持大小写字母、数字、下划线、点号 | `Invalid format.` |
| Close / Skip | Button | 默认展示 | 点击后进入 Home；Tag 为空 | 无 |
| Confirm | Button | 格式合法且 Tag 可用 | 点击弹出确认弹窗；确认后提交创建 | Tag 已存在、无网络、服务器异常 |

AIX Tag 格式规则：

| 规则 | 内容 |
|------|------|
| 前缀 | 固定 `@` |
| 字符集 | 大小写字母、数字、下划线 `_`、点号 `.` |
| 长度 | 自定义部分 3-30 字符，不含 `@` |
| 结尾限制 | 不能以下划线 `_` 或点号 `.` 结尾 |
| 连续字符限制 | 不允许连续两个 `_` 或连续两个 `.` |
| 大小写 | 区分大小写 |
| 保留字 | 禁止 admin、support、api、null；不区分大小写 |
| 可变更性 | 设置后通常不可更改 |

## 7. 状态机

### 7.1 账户状态变化

```text
┌──────────────┐
│ Unregistered │
└──────┬───────┘
       │ 创建密码成功
       ▼
┌──────────────┐
│ Active       │
└──────────────┘
```

### 7.2 AIX Tag 设置状态

```text
┌──────────────┐
│ Tag Empty    │
└──────┬───────┘
       │ 用户设置且创建成功
       ▼
┌──────────────┐
│ Tag Created  │
└──────────────┘
```

## 8. 字段与接口依赖

| 字段 / 能力 | 用途 | 读/写 | 来源 | 备注 |
|-------------|------|------|------|------|
| email | 注册账号 | 写 | Registration Page | 全局唯一 |
| referralCode | 推荐码 | 写 | Registration Page | 可选；不存在时提示错误 |
| agreementSnapshot | 协议快照 | 写 | Registration Page | 注册成功后绑定账户，不可更改 |
| password | 登录密码 | 写 | Set Password Page | 8-32 字符，大小写字母 + 数字 + 符号 |
| uid | 用户唯一标识 | 写 | 服务端注册成功后生成 | 生成规则由开发侧定义 |
| deviceId | 设备绑定 | 写 | 注册 / 登录成功 | 单账户最多绑定 1 个 Device ID |
| aixTag | AIX 平台身份标识 | 写 | Optional Set AIX Tag Page | 可选；通常不可更改 |

## 9. 异常与失败处理

| 场景 | 触发条件 | 用户提示 | 系统动作 | 最终状态 | 来源 |
|------|----------|----------|----------|----------|------|
| Email 为空 | 用户未填写 Email | `Email should not be empty` | 阻止 Next | 留在 Registration Page | AIX Card 注册登录需求V1.0 / 7.1.4 |
| Email 格式错误 | Email 不符合格式 | `Email format is invalid` | 阻止 Next | 留在 Registration Page | AIX Card 注册登录需求V1.0 / 7.1.4 |
| Email 已注册 | 后端检测邮箱已存在 | 文档要求明确提示并引导登录；当前知识库记录为 `This email has been used` | 中断注册流程 | 留在 Registration Page / 引导 Login | AIX Card 注册登录需求V1.0 / 7.1.4 |
| 推荐码不存在 | referralCode 无效 | `Referral code does not exist` | 中断注册流程 | 留在 Registration Page | AIX Card 注册登录需求V1.0 / 7.1.4 |
| 协议未勾选 | 必选协议未同意 | Next 不可点击 | 阻止进入 Email OTP | 留在 Registration Page | AIX Card 注册登录需求V1.0 / 7.1.4 |
| 密码格式不合法 | 密码不满足复杂度 | 对应密码校验错误提示 | 阻止提交 | 留在 Set Password Page | AIX Card 注册登录需求V1.0 / 7.1.6 |
| 创建密码失败 | 后端返回服务器错误 | `System busy, please try again later` | 注册失败 | 留在 Set Password Page | AIX Card 注册登录需求V1.0 / 7.1.6 |
| Tag 格式错误 | Tag 不满足格式规则 | `Invalid format.` | 阻止提交 | 留在 Set AIX Tag Page | AIX Card 注册登录需求V1.0 / 7.1.7 |
| Tag 已存在 | Tag 唯一性校验失败 | `Tag already exists. Please try again.` / `This tag is already taken. Try another one.` | 创建失败 | 留在 Set AIX Tag Page | AIX Card 注册登录需求V1.0 / 7.1.7；当前知识库旧文案 |
| Tag 网络异常 | 无网络 | `No internet connection, please check the connection or try again later.` / `Please check your internet connection and try again.` | 创建失败 | 留在 Set AIX Tag Page | AIX Card 注册登录需求V1.0 / 7.1.7；当前知识库旧文案 |

## 10. 风控 / 合规边界

| 边界 | 规则 | 影响 | 来源 |
|------|------|------|------|
| 邮箱唯一性 | 邮箱全局唯一，不允许重复注册或绑定 | 防重复账户 | AIX Card 注册登录需求V1.0 / 6.2.5 |
| 协议快照 | 注册成功后保存用户同意的 Terms of service 与 Privacy Policy 版本快照 | 合规追溯 | AIX Card 注册登录需求V1.0 / 7.1.4 |
| 设备绑定 | 注册 / 登录成功后绑定当前 Device ID | BIO 前提与风控基础 | AIX Card 注册登录需求V1.0 / 6.2.6 |
| Email OTP | 注册必须完成 Email OTP | 账户安全 | AIX Card 注册登录需求V1.0 / 7.1.5；Security 模块 |
| 注册频控 | 当前知识库记录设备指纹、IP、接口总限流 | 防批量注册 | 需与后端限流策略确认 |

## 11. 多角色阅读视角

### UI 视角

- 页面关系以 ASCII 图为准，原页面概览截图只做追溯证据。
- 单页 UI 需要覆盖 Navigation、Registration、Email OTP、Set Password、Optional Set AIX Tag。

### 开发视角

- 创建密码成功即完成注册并生成 UID，AIX Tag 不再是注册完成前置条件。
- Email OTP 调用 Security 模块，注册文档不重复定义 OTP 失败规则。
- 协议快照必须在注册成功后与用户账户绑定存储。

### 测试视角

- 必测：邮箱格式、协议勾选、推荐码不存在、邮箱已注册、Email OTP 成功 / 失败、密码复杂度、创建密码成功、AIX Tag 设置 / 跳过。
- 需要覆盖 AIX Tag 可跳过且不影响进入 Home。

### 业务视角

- 推荐码与 AIX Tag 已解耦，推荐码由系统独立生成，具体规则见 MGM 需求文档。
- AIX Tag 是用户身份标识能力，不是注册成功前置条件。

### AI 复用视角

- 新 PRD 涉及注册流程时，应复用“创建密码即注册成功，AIX Tag 可选”的规则。
- 不得再将 AIX Tag 写成注册完成的强制步骤。

## 12. 待确认事项

| 问题 | 影响范围 | 建议确认人 | 状态 |
|------|----------|------------|------|
| Registration Page 协议复选框在原始 PRD 中有“默认为勾选状态（待合规确定）”，当前知识库旧内容写“默认为不勾选状态”，需确认最终口径 | 注册页 / 合规 | 产品 / 合规 | open |
| Email 已注册提示文案需确认是否统一为 `This email has been used`，还是仅要求“明确提示并引导登录” | 注册页 / 文案 | 产品 / UI | open |
| AIX Tag 错误提示存在两套文案，需以翻译文案表或最新 UI 为准 | Set AIX Tag | 产品 / UI | open |
| 注册频控的设备指纹、IP、接口总限流规则需确认后端实现口径 | 注册风控 | 产品 / 技术 | open |
| Set Password 是否仍存在 Re-enter Password Page 作为确认密码页，需结合最新 UX 确认 | 设置密码 | 产品 / UI / 技术 | open |

## 13. 来源引用

- (Ref: 历史prd/AIX Card 注册登录需求V1.0.docx / 2025-11-18 需求变更日志 / V1.0)
- (Ref: 历史prd/AIX Card 注册登录需求V1.0.docx / 6.2 账户说明 / V1.0)
- (Ref: 历史prd/AIX Card 注册登录需求V1.0.docx / 7.1.3 Navigation Page / V1.0)
- (Ref: 历史prd/AIX Card 注册登录需求V1.0.docx / 7.1.4 Registration Page / V1.0)
- (Ref: 历史prd/AIX Card 注册登录需求V1.0.docx / 7.1.5 邮箱OTP验证页 / V1.0)
- (Ref: 历史prd/AIX Card 注册登录需求V1.0.docx / 7.1.6 Set Password Page / V1.0)
- (Ref: 历史prd/AIX Card 注册登录需求V1.0.docx / 7.1.7 Set Tag Page / V1.0)
- (Ref: knowledge-base/security/email-otp-verification.md)
