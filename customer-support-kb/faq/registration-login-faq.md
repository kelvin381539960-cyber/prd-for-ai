---
module: registration-login
audience: customer
visibility: user-facing
language: zh-CN
verification_status: draft_pending_review
last_updated: 2026-05-10
---

# 注册与登录 FAQ

## Q: 注册时提示邮箱格式无效怎么办？

### 推荐回答

请检查邮箱是否填写完整，例如是否包含用户名、`@` 和邮箱域名。如果邮箱为空或格式不正确，页面可能会提示邮箱格式无效。

如果确认邮箱正确但仍无法继续，建议稍后重试或联系人工客服。

### 分类

- module: registration-login
- intent: invalid_email_format
- visibility: user-facing
- verification_status: draft_pending_review

### 转人工

需要转人工：

- 用户确认邮箱正确但一直无法注册。
- 页面持续报错或系统繁忙。

## Q: 推荐码提示不存在怎么办？

### 推荐回答

请确认推荐码是否输入完整，且没有多余空格或错误字符。如果页面提示推荐码不存在，请向邀请人确认推荐码是否正确。

如果仍然无法使用，建议联系人工客服协助确认。

### 分类

- module: registration-login
- intent: referral_code_invalid
- visibility: user-facing
- verification_status: draft_pending_review

### 转人工

需要转人工：

- 用户确认推荐码正确但仍无法使用。
- 用户不确定是否必须填写推荐码。

## Q: 收不到验证码怎么办？

### 推荐回答

请先确认邮箱或手机号是否填写正确，并检查网络连接、短信拦截、邮箱垃圾邮件或广告邮件文件夹。你也可以等待一段时间后重新发送验证码。

如果多次尝试后仍无法收到验证码，建议联系人工客服协助检查。

### 分类

- module: registration-login
- intent: verification_code_not_received
- visibility: user-facing
- verification_status: draft_pending_review

### 转人工

需要转人工：

- 多次尝试仍收不到验证码。
- 用户无法访问原邮箱或手机号。
- 页面提示账户受限或异常。

## Q: 设置密码时一直无法通过怎么办？

### 推荐回答

请按照页面提示设置密码。密码通常需要满足长度要求，并包含字母、数字和符号。如果页面提示两次密码不一致，请重新输入并确保两次完全相同。

如果多次尝试仍无法完成，建议联系人工客服。

### 分类

- module: registration-login
- intent: password_rule_error
- visibility: user-facing
- verification_status: draft_pending_review

### 转人工

需要转人工：

- 用户确认符合规则但仍无法继续。
- 页面提示系统错误或提交失败。

## Q: Quick Login 或生物识别登录失败怎么办？

### 推荐回答

你可以先改用普通登录方式。Quick Login 通常依赖设备是否支持并已开启人脸或指纹识别。如果多次失败，请检查手机系统的人脸或指纹设置。

如果仍无法登录，建议联系人工客服。

### 分类

- module: registration-login
- intent: biometric_login_failed
- visibility: user-facing
- verification_status: draft_pending_review

### 转人工

需要转人工：

- 用户普通登录也失败。
- 页面提示账户锁定或安全风险。
- 用户怀疑账户异常。

## Q: 忘记密码怎么办？

### 推荐回答

请在登录页面查看是否有找回或重置密码入口，并按照页面提示完成验证。如果你无法访问原邮箱或手机号，建议联系人工客服协助处理。

### 分类

- module: registration-login
- intent: forgot_password
- visibility: user-facing
- verification_status: draft_pending_review

### 转人工

需要转人工：

- 用户无法访问原邮箱或手机号。
- 用户无法完成验证。
- 用户怀疑账户存在安全风险。
