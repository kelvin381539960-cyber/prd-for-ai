---
module: notification-system-email
audience: customer
visibility: user-facing
language: zh-CN
verification_status: partial_confirmed
last_updated: 2026-05-12
---

# 通知与系统邮件 FAQ

## Q: App 通知设置支持哪些方式？

### 推荐回答

当前 App 通知设置支持 Push、Email、SMS。具体哪些通知类型可以开启或关闭，请以 App 页面展示为准。

### 分类

- module: notification-system-email
- intent: notification_channels
- visibility: user-facing
- verification_status: confirmed

### 转人工

用户无法修改通知设置，或设置后仍收不到通知时，建议转人工。

## Q: 收不到 App 推送怎么办？

### 推荐回答

请先确认手机系统通知权限是否开启，并检查 App 内通知设置、网络连接和 App 是否为最新版本。

如果你关闭了某些通知类型，可能无法收到对应提醒。涉及账户安全、交易、身份验证等重要信息时，建议保持通知开启。

### 分类

- module: notification-system-email
- intent: push_not_received
- visibility: user-facing
- verification_status: partial_confirmed

### 转人工

需要转人工：

- 用户持续收不到重要通知。
- 通知内容与账户操作不一致。
- 用户怀疑账户安全异常。

## Q: 收不到系统邮件怎么办？

### 推荐回答

请先确认邮箱地址是否填写正确，并检查收件箱、垃圾邮件、广告邮件或邮箱拦截设置。你也可以稍后重新尝试发送。

如果多次尝试后仍收不到邮件，建议联系人工客服。

### 分类

- module: notification-system-email
- intent: system_email_not_received
- visibility: user-facing
- verification_status: partial_confirmed

### 转人工

需要转人工：

- 多次尝试仍收不到邮件。
- 用户需要修改邮箱。
- 用户怀疑邮件异常。

## Q: 收到可疑邮件怎么办？

### 推荐回答

请不要点击可疑链接，也不要向任何人提供密码、验证码、私钥或敏感账户信息。

可疑邮件的处理规则仍需进一步确认。在确认前，建议联系人工客服核查。

### 分类

- module: notification-system-email
- intent: suspicious_email
- visibility: user-facing
- verification_status: partial_confirmed

### 转人工

建议转人工。
