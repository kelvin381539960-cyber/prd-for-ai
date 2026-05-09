---
module: account
feature: password-reset
version: "1.1"
status: need_confirmation
source_doc: archive/converted-prd/app/registration-login/README.md；archive/converted-prd/security/identity-verification/README.md
source_section: registration-login / 7.3 忘记密码流程页面；security / 认证方式能力矩阵
last_updated: 2026-05-09
owner: 吴忆锋
depends_on:
  - account/_index
  - login
  - security/_index
  - security/otp-verification
  - security/email-otp-verification
  - security/biometric-verification
---

# Password Reset 忘记密码流程

## 1. Source alignment status

本文件已按新转换历史 PRD 重新校准。结论是：**不能把当前 `password-reset` 文件视为已确认的 active runtime fact。**

原因：`archive/converted-prd/app/registration-login/README.md` 中 `7.3 忘记密码流程页面`、`7.3.1 功能说明`、`7.3.3 Reset Password Page`、`7.3.4 身份验证流程页面`、`7.3.5 设置密码页` 等内容整体以删除线形式呈现。

因此，以下内容只可作为历史痕迹或待确认项，不可作为当前已确认产品事实直接引用：

- 忘记密码入口与页面流程；
- Reset Password Page 的邮箱 / 手机号输入规则；
- 忘记密码后的身份验证链路；
- 密码重置成功后强制登出；
- 密码重置成功后清除 BIO 信息、关闭已开启 BIO。

## 2. What is supported by converted PRD

| 事实 | 状态 | 来源 | 处理 |
|---|---|---|---|
| 历史 PRD 曾包含忘记密码流程章节 | VERIFIED_AS_HISTORICAL | registration-login / 7.3 | 仅作为历史痕迹 |
| 忘记密码后需要清除 BIO、关闭已开启 BIO | NEED_CONFIRMATION | registration-login changelog 有补充记录，但 7.3.1 正文为删除线 | 不作为 active runtime fact |
| 忘记密码涉及身份验证流程 | NEED_CONFIRMATION | registration-login / 7.3.4 删除线引用 Security；security 能力矩阵中出现“忘记密码”场景 | 需要产品确认当前是否启用 |
| 忘记密码可使用 OTP / EMAIL_OTP | NEED_CONFIRMATION | security / 认证方式能力矩阵出现忘记密码场景 | 仅能说明 Security 能力矩阵曾覆盖该场景，不能单独证明 App 当前有入口 |

## 3. Runtime usage rule

在用户或 AI 查询“忘记密码”时：

1. 不得直接回答为已上线 / 已确认流程。
2. 应说明：历史 PRD 中该章节被删除线标记，当前 runtime 规则需要产品确认。
3. 若只问认证能力，可引用 Security 中的 OTP / EMAIL_OTP 能力，但不得反推 App 忘记密码入口已启用。

## 4. 待确认项

| 项目 | 问题 | 建议确认人 |
|---|---|---|
| 忘记密码入口 | 当前 App 是否仍存在 Forgot / Reset Password 入口？ | Product |
| 重置后 BIO 处理 | 是否仍要求清除本地 BIO 并关闭服务端 BIO 开关？ | Product / Security |
| 重置后登录态 | 是否强制登出并要求用新密码重新登录？ | Product / Backend |
| 认证方式 | 当前忘记密码使用 EMAIL_OTP、OTP、Face Auth 还是组合认证？ | Product / Security |

## 5. Sources

- (Ref: archive/converted-prd/app/registration-login/README.md / 7.3 忘记密码流程页面，删除线)
- (Ref: archive/converted-prd/app/registration-login/README.md / 需求变更日志，忘记密码后关闭 BIO 补充记录)
- (Ref: archive/converted-prd/security/identity-verification/README.md / 认证方式能力矩阵，忘记密码场景)
