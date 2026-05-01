---
module: account
description: 用户账户体系，包含注册、登录、忘记密码三大功能
version: "1.0"
status: released
source_docs:
  - 历史prd/AIX Card 注册登录需求V1.0 (2).docx
source_sections:
  - 5.2 账户说明
  - 7 注册功能
  - 登录功能
  - 忘记密码功能
last_updated: 2026-05-01
owner: 吴忆锋
depends_on:
  - _meta/status-dictionary
  - _meta/countries-and-regions
  - security/global-rules
  - security/otp-verification
  - security/email-otp-verification
  - security/login-passcode-verification
  - security/biometric-verification
readers: [product, ui, dev, qa, business, ai]
---

# Account 账户模块

## 1. 模块定位

Account 模块沉淀 AIX 用户账户体系事实，覆盖用户从进入 App 到完成注册、登录、忘记密码、基础账户状态流转的规则。

本模块是 Wallet、Card、Transaction 等后续业务模块的账户前置基础。

## 2. 功能清单

| 功能 | 文件 | 状态 | 说明 | 来源 |
|------|------|------|------|------|
| 注册 | [registration.md](./registration.md) | released | 邮箱注册 + Email OTP 验证 + 设置密码；AIX Tag 为注册后可选引导 | AIX Card 注册登录需求V1.0 |
| 登录 | [login.md](./login.md) | released | 邮箱 / 手机登录 + 密码验证 + Biometric 快捷登录 | AIX Card 注册登录需求V1.0 |
| 忘记密码 | [password-reset.md](./password-reset.md) | released | 邮箱 / 手机号重置 + 身份验证 + 重设密码 + 自动关闭 BIO | AIX Card 注册登录需求V1.0 |

## 3. 适用范围

| 维度 | 规则 | 来源 | 备注 |
|------|------|------|------|
| 国家 / 地区 | VN / PH / AU | AIX Card 注册登录需求V1.0 | 需后续同步至 `_meta/countries-and-regions.md` |
| 账户状态 | Active / Locked / Banned / Closed | AIX Card 注册登录需求V1.0 / 5.2 账户说明 | 已同步至 `_meta/status-dictionary.md` |
| 设备绑定 | 单账户最多绑定 1 个 Device ID，最多允许 1 个设备同时在线 | AIX Card 注册登录需求V1.0 / 5.2.6 设备绑定策略 | BIO 启用依赖设备绑定 |
| 唯一性 | 邮箱、手机号全局唯一 | AIX Card 注册登录需求V1.0 / 5.2.5 | 不允许重复注册或绑定 |

## 4. 模块依赖

| 依赖对象 | 依赖内容 | 说明 |
|----------|----------|------|
| `_meta/status-dictionary.md` | Account Status | 账户状态统一定义 |
| `_meta/countries-and-regions.md` | 国家线 | VN / PH / AU 支持范围 |
| `security/global-rules.md` | 认证方式、认证有效期、场景矩阵 | 注册、登录、忘记密码依赖身份认证能力 |
| `security/email-otp-verification.md` | Email OTP | 注册、忘记密码依赖 |
| `security/otp-verification.md` | SMS OTP | 登录、忘记密码等场景可依赖 |
| `security/login-passcode-verification.md` | Login Passcode | 登录与敏感操作认证依赖 |
| `security/biometric-verification.md` | Biometric | Quick Login 与 BIO 设置依赖 |

## 5. 核心流程总览

```text
┌──────────────┐
│ Navigation   │
└──────┬───────┘
       │
       ├─────────────── Create account ───────────────┐
       │                                                ▼
       │                                      ┌──────────────────┐
       │                                      │ Registration     │
       │                                      │ Email + Agreement│
       │                                      └────────┬─────────┘
       │                                               ▼
       │                                      ┌──────────────────┐
       │                                      │ Email OTP        │
       │                                      └────────┬─────────┘
       │                                               ▼
       │                                      ┌──────────────────┐
       │                                      │ Set Password     │
       │                                      └────────┬─────────┘
       │                                               ▼
       │                                      ┌──────────────────┐
       │                                      │ Registered       │
       │                                      │ Status = Active  │
       │                                      └────────┬─────────┘
       │                                               ▼
       │                                      ┌──────────────────┐
       │                                      │ Optional AIX Tag │
       │                                      └───────┬────┬─────┘
       │                                              │    │
       │                                      Set Tag │    │ Skip
       │                                              ▼    ▼
       │                                      ┌──────────────────┐
       │                                      │ Home             │
       │                                      └──────────────────┘
       │
       └──────── I already have an account ────────────┐
                                                        ▼
                                               ┌──────────────────┐
                                               │ Login            │
                                               │ Email/Phone/BIO  │
                                               └────────┬─────────┘
                                                        ▼
                                               ┌──────────────────┐
                                               │ Home             │
                                               └──────────────────┘
```

## 6. 账户状态机

```text
┌──────────┐   注册成功   ┌──────────┐
│ 未注册   │ ──────────→ │ Active   │
└──────────┘              └────┬─────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
        ┌──────────┐    ┌──────────┐    ┌──────────┐
        │ Locked   │    │ Banned   │    │ Closed   │
        └────┬─────┘    └──────────┘    └──────────┘
             │
             │ 锁定到期 / 忘记密码重置
             ▼
        ┌──────────┐
        │ Active   │
        └──────────┘
```

| 状态 | 定义 | 触发条件 | 限制 | 解除方式 | 是否终态 |
|------|------|----------|------|----------|----------|
| Active | 账户正常使用中 | 注册成功后 | 无 | - | 否 |
| Locked | 因安全原因临时锁定 | 登录失败超过 N 次 | 不可登录 | 锁定时长到期自动解除；或用户通过忘记密码重置 | 否 |
| Banned | 账户被限制使用，可恢复 | 风控触发对应规则，一期不支持 | 不可登录 | 联系客服处理 | 否 |
| Closed | 账户被注销，不可恢复 | 风控触发对应规则 / 客服手动操作，一期不支持 | 不可登录，所有功能不可用 | 无法解除 | 是 |

## 7. 字段与规则总览

| 规则 / 字段 | 规则内容 | 影响范围 | 来源 |
|-------------|----------|----------|------|
| UID | 服务端在用户注册成功后生成 | 全局账户识别 | AIX Card 注册登录需求V1.0 / 5.2.1 |
| 昵称 | 注册成功后自动生成：随机 4 位英文 + 随机 6 位数字 | ME 模块可修改 | AIX Card 注册登录需求V1.0 / 5.2.4 |
| 邮箱唯一性 | 邮箱全局唯一，不允许重复注册或绑定 | 注册 / 绑定邮箱 | AIX Card 注册登录需求V1.0 / 5.2.5 |
| 手机号唯一性 | 手机号全局唯一，不允许重复注册或绑定 | 登录 / 绑定手机号 | AIX Card 注册登录需求V1.0 / 5.2.5 |
| Device ID | 注册 / 登录成功后自动绑定当前 Device ID | 登录 / BIO | AIX Card 注册登录需求V1.0 / 5.2.6 |
| AIX Tag | 注册成功后可选设置的唯一 ID，用于他人转账识别 | 注册后引导 / 收款 / 转账 | AIX Card 注册登录需求V1.0 / 2025-11-18 变更记录；7.1.7 |
| Referral Code | 由系统独立生成，与 AIX Tag 解耦 | MGM / 注册推荐 | AIX Card 注册登录需求V1.0 / 2025-11-18 变更记录 |

## 8. 异常与失败处理总览

| 场景 | 触发条件 | 用户提示 / 系统动作 | 来源 |
|------|----------|--------------------|------|
| 邮箱已注册 | 注册时输入已存在邮箱 | 提示：`This email has been used` 或明确提示并引导登录 | registration.md |
| 推荐码不存在 | 注册时输入无效 Referral code | 提示：`Referral code does not exist` | registration.md |
| 登录账号不存在 / 未注册 | 登录时账号不存在 | 提示账号信息有误或引导注册 | login.md |
| 账户 Banned | 账户被风控限制 | 不可登录，联系客服处理 | account / security |
| 忘记密码成功 | 用户完成重置密码 | 强制登出，清除 BIO，使用新密码重新登录 | password-reset.md |

## 9. 风控 / 合规边界

| 边界 | 规则 | 影响范围 | 来源 |
|------|------|----------|------|
| 账户唯一性 | 邮箱、手机号全局唯一 | 防重复账户 / 绑定冲突 | AIX Card 注册登录需求V1.0 |
| 设备绑定 | 单账户单设备绑定与单设备在线 | 登录安全 / BIO 前提 | AIX Card 注册登录需求V1.0 |
| 账户状态拦截 | Banned / Closed / Locked 均影响登录能力 | 登录与后续业务入口 | AIX Card 注册登录需求V1.0 |
| 身份认证 | 注册、登录、忘记密码依赖 Security 模块 | 账户安全 | AIX Security 身份认证需求V1.0 |
| 协议快照 | 注册成功后保存用户同意协议版本快照 | 合规追溯 | AIX Card 注册登录需求V1.0 / 7.1.4 |

## 10. 多角色阅读视角

### UI 视角

- 关注 Navigation、Registration、Login、Reset Password、Set Password、Optional AIX Tag、BIO 引导等页面。
- 页面组件与错误提示以各功能文件为准。
- 页面关系图不得仅依赖截图，必须使用 ASCII / Mermaid 表达。

### 开发视角

- 关注 UID、邮箱 / 手机号唯一性、Device ID 绑定、账户状态拦截、BIO 前置条件。
- 身份认证调用应引用 Security 模块，不在 Account 中重复定义认证逻辑。
- AIX Tag 不再是注册成功前置条件，创建密码成功后即注册成功。

### 测试视角

- 覆盖注册主链路、登录主链路、Quick Login、忘记密码、账户状态拦截、唯一性校验、设备绑定边界。
- Locked / Banned / Closed 状态必须单独覆盖。
- 必须覆盖 AIX Tag 可设置与可跳过两条分支。

### 业务视角

- Account 是用户进入 Wallet / Card / Transaction 的前置能力。
- 支持国家线当前为 VN / PH / AU。
- Banned / Closed 一期不支持用户自助解除。
- AIX Tag 是注册后可选身份标识，不影响账户使用。

### AI 复用视角

- 新 PRD 涉及登录态、账户状态、身份认证、设备绑定、手机号 / 邮箱唯一性时，应优先引用本模块。
- 不得在新 PRD 中重新定义 Account Status，应引用 `_meta/status-dictionary.md`。
- 不得将 AIX Tag 写成注册强制步骤。

## 11. 待确认事项

| 问题 | 影响范围 | 建议确认人 | 状态 |
|------|----------|------------|------|
| 登录失败超过 N 次中的 N 需要从 Security 或后端规则中统一确认 | Locked 状态 / 登录风控 | 产品 / 技术 | open |
| 昵称“自动生成”与“需要用户手动设置，见 ME 模块”两种描述需在 ME 重构时确认最终口径 | Account / ME | 产品 | open |
| 支持国家线是否所有 Account 子功能完全一致 | 注册 / 登录 / 忘记密码 | 产品 / 合规 | open |
| Registration Page 协议默认勾选状态在原始 PRD 与当前知识库旧内容中不一致，需确认最终口径 | 注册页 / 合规 | 产品 / 合规 | open |
| AIX Tag 错误提示存在两套文案，需以翻译文案表或最新 UI 为准 | 注册后 AIX Tag 设置 | 产品 / UI | open |

## 12. 来源引用

- (Ref: 历史prd/AIX Card 注册登录需求V1.0 (2).docx / 5.2 账户说明 / V1.0)
- (Ref: 历史prd/AIX Card 注册登录需求V1.0 (2).docx / 2025-11-18 需求变更日志 / V1.0)
- (Ref: 历史prd/AIX Card 注册登录需求V1.0 (2).docx / 7 注册功能 / V1.0)
- (Ref: knowledge-base/account/registration.md)
- (Ref: knowledge-base/account/login.md)
- (Ref: knowledge-base/account/password-reset.md)
- (Ref: knowledge-base/security/global-rules.md)
