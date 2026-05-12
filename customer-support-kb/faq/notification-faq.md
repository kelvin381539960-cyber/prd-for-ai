---
module: notification-system-email
audience: customer
visibility: user-facing
language: zh-CN
verification_status: draft_pending_review
last_updated: 2026-05-10
---

# 通知与系统邮件 FAQ

## Q: 收不到 App 推送怎么办？

### 推荐回答

请先确认手机系统通知权限是否开启，并检查 App 内通知设置、网络连接和 App 是否为最新版本。

如果你关闭了某些通知类型，可能无法收到对应提醒。涉及账户安全、交易、身份验证等重要信息时，建议保持通知开启。

### 分类

- module: notification-system-email
- intent: push_not_received
- visibility: user-facing
- verification_status: draft_pending_review

### 转人工

需要转人工：

- 用户持续收不到重要通知。
- 通知内容与账户操作不一致。
- 用户怀疑账户安全异常。

## Q: 在哪里查看站内信？

### 推荐回答

你可以在 App 的通知或消息入口查看站内信。消息可能包含交易、账户、系统、活动、安全等类型，具体分类和展示内容请以 App 页面为准。

### 分类

- module: notification-system-email
- intent: inbox_location
- visibility: user-facing
- verification_status: draft_pending_review

### 转人工

需要转人工：

- 用户找不到通知或消息入口。
- 重要交易或账户通知没有显示。

## Q: 如何把消息标记为已读？

### 推荐回答

如果消息列表提供“一键已读”或点击消息查看详情的功能，你可以按照页面提示操作。未读消息通常会有红点或数字提示，查看后可能会更新为已读状态。

### 分类

- module: notification-system-email
- intent: mark_as_read
- visibility: user-facing
- verification_status: draft_pending_review

### 转人工

需要转人工：

- 未读数量显示异常。
- 消息无法打开或无法标记已读。

## Q: 收不到系统邮件怎么办？

### 推荐回答

请先确认邮箱地址是否填写正确，并检查收件箱、垃圾邮件、广告邮件或邮箱拦截设置。你也可以稍后重新尝试发送。

如果多次尝试后仍收不到邮件，建议联系人工客服。

### 分类

- module: notification-system-email
- intent: system_email_not_received
- visibility: user-facing
- verification_status: draft_pending_review

### 转人工

需要转人工：

- 多次尝试仍收不到邮件。
- 用户需要修改邮箱。
- 用户怀疑邮件异常。

## Q: 收到可疑邮件怎么办？

### 推荐回答

请不要点击可疑链接，也不要向任何人提供密码、验证码、私钥或敏感账户信息。如果你怀疑邮件异常，建议联系人工客服确认。

### 分类

- module: notification-system-email
- intent: suspicious_email
- visibility: user-facing
- verification_status: draft_pending_review

### 转人工

需要转人工：

- 用户怀疑收到钓鱼邮件。
- 通知内容与账户操作不一致。
