---
module: security
feature: otp-verification
version: 1.0
last_updated: 2025-10-29
authors: [吴忆锋]
status: released
depends_on: []
---

# OTP Verification 邮箱/短信验证码

## 1. 功能概述

统一的一次性验证码机制，通过邮箱发送6位数字验证码，用户输入后完成身份验证。

> ⚠️ 完整详细规则见源文档「AIX Security 身份认证需求V1.0」，此处为跨模块引用摘要。

## 2. 验证码规则

| 规则项 | 说明 |
|--------|------|
| 位数 | 6位纯数字 |
| 有效期 | 5分钟 |
| 发送渠道 | 邮箱（一期） |
| 重发间隔 | 60秒冷却 |
| 错误次数限制 | 待补充（见Security文档） |

## 3. 页面通用交互

| 元素 | 规则 |
|------|------|
| 验证码输入框 | 6位数字输入，自动聚焦 |
| 重新发送按钮 | 60秒倒计时后可点击 |
| 返回按钮 | 返回上一步 |

## 4. 调用方

- `account/registration` — 注册邮箱验证
- `account/login` — 登录身份验证
- `account/password-reset` — 重置密码验证
- `card/*` — 敏感卡操作
- `wallet/*` — 敏感钱包操作

---

> 📌 TODO: 待从「AIX Security 身份认证需求V1.0」完整转译后补充详细内容
