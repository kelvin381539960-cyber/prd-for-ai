---
module: security
description: 身份认证与安全能力层 — OTP验证、生物识别、密码策略。跨模块公共依赖。
version: 1.0
last_updated: 2025-11-11
status: released
depends_on: []
---

# Security 安全/身份认证

## 模块概述

AIX 全局安全能力层，提供统一的身份验证机制。被 account、card、wallet 等多个模块依赖调用。

## 功能清单

| 功能 | 文档 | 调用场景 |
|------|------|----------|
| OTP 验证 | [otp-verification.md](./otp-verification.md) | 注册、登录、重置密码、敏感操作 |
| 生物识别 | [biometric.md](./biometric.md) | 快捷登录、敏感操作二次确认 |
| 密码策略 | [password-policy.md](./password-policy.md) | 注册设置密码、重置密码 |

## 验证场景总览

> 来源：AIX验证场景维护表

| 场景 | 验证方式 | 说明 |
|------|----------|------|
| 注册-邮箱验证 | Email OTP | 6位数字，5分钟有效 |
| 登录-密码验证 | Password | 8-32位，含大小写+数字+符号 |
| 登录-生物识别 | Biometric | 设备端+后端双重验证 |
| 重置密码 | Email OTP + New Password | 验证后设置新密码 |
| 敏感操作 | 按场景配置 | 见具体模块PRD |
