---
module: registration-login
audience: customer
visibility: user-facing
language: zh-CN
verification_status: partial_confirmed
last_updated: 2026-05-12
---

# 注册与登录 FAQ

## Q: 当前可以用手机号注册吗？

### 推荐回答

当前仅支持邮箱注册，暂不支持手机号注册。手机号注册未来可能支持，请以后续 App 页面提示为准。

### 分类

- module: registration-login
- intent: phone_registration
- visibility: user-facing
- verification_status: confirmed

### 转人工

通常不需要转人工，除非用户邮箱注册失败或页面持续报错。

## Q: 当前支持哪些登录方式？

### 推荐回答

当前支持邮箱登录、手机号登录和生物识别登录。生物识别登录也就是 Quick Login，通常依赖你的设备是否支持并已开启人脸或指纹识别。

### 分类

- module: registration-login
- intent: login_methods
- visibility: user-facing
- verification_status: confirmed

### 转人工

需要转人工：

- 用户普通登录也失败。
- 页面提示账户锁定或安全风险。
- 用户怀疑账户异常。

## Q: 验证码有效期是多久？

### 推荐回答

验证码有效期为 5 分钟。请使用最新收到的验证码。重新发送验证码后，旧验证码可能会失效。

如果页面提示验证码无效、过期、发送过于频繁或尝试次数过多，请按页面提示稍后重试。

### 分类

- module: registration-login
- intent: verification_code_validity
- visibility: user-facing
- verification_status: confirmed

### 转人工

需要转人工：

- 多次尝试仍收不到验证码。
- 页面持续提示错误或账户异常。

## Q: 密码规则是什么？

### 推荐回答

当前登录密码规则可以说明为：8-32 位，并包含大小写字母、数字和符号。请按照页面提示设置密码，并确保两次输入完全一致。

### 分类

- module: registration-login
- intent: password_rule
- visibility: user-facing
- verification_status: confirmed

### 转人工

需要转人工：

- 用户确认符合规则但仍无法继续。
- 页面提示系统错误或提交失败。

## Q: 推荐码是必填吗？

### 推荐回答

推荐码是选填项。没有推荐码也可以继续注册。

如果你有推荐码，请确认输入完整，且没有多余空格或错误字符。

### 分类

- module: registration-login
- intent: referral_code_optional
- visibility: user-facing
- verification_status: confirmed

### 转人工

需要转人工：

- 用户确认推荐码正确但仍无法使用。

## Q: AIX Tag / X-Tag 是必填吗？

### 推荐回答

AIX Tag / X-Tag 当前存在，但不是必填项。你可以按照页面提示选择是否设置。

### 分类

- module: registration-login
- intent: x_tag_optional
- visibility: user-facing
- verification_status: confirmed

### 转人工

通常不需要转人工，除非页面无法继续或提示异常。

## Q: 收不到验证码怎么办？

### 推荐回答

请先确认邮箱或手机号是否填写正确，并检查网络连接、短信拦截、邮箱垃圾邮件或广告邮件文件夹。你也可以等待一段时间后重新发送验证码。

如果多次尝试后仍无法收到验证码，建议联系人工客服协助检查。

### 分类

- module: registration-login
- intent: verification_code_not_received
- visibility: user-facing
- verification_status: partial_confirmed

### 转人工

需要转人工：

- 多次尝试仍收不到验证码。
- 用户无法访问原邮箱或手机号。
- 页面提示账户受限或异常。

## Q: 账号被锁定、关闭或限制怎么办？

### 推荐回答

如果页面提示账户被锁定、关闭、限制或存在安全风险，请联系人工客服处理。智能客服无法直接判断或说明具体原因。

### 分类

- module: registration-login
- intent: account_locked_or_limited
- visibility: user-facing
- verification_status: confirmed

### 转人工

需要转人工。
