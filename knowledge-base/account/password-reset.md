---
module: account
feature: password-reset
version: 1.0
last_updated: 2025-11-11
authors: [吴忆锋]
status: released
depends_on: [security/otp-verification, security/password-policy]
---

# Password Reset 忘记密码

## 1. 功能概述

用户忘记密码时，通过邮箱验证身份后重新设置登录密码。重置成功后：
- **强制登出**当前账户
- **清除BIO信息**，已开启的BIO自动关闭
- 用户需使用新密码重新登录

## 2. 用户流程

![忘记密码流程图](../assets/account/image12.png)

### 流程步骤（AI-readable）

| 步骤 | 角色 | 动作 | 条件/分支 | 下一步 |
|------|------|------|-----------|--------|
| 1 | 用户 | 在登录页点击"忘记密码" | - | 2 |
| 2 | 用户 | 输入注册邮箱 | - | 3 |
| 3 | 前端 | 校验邮箱格式 | 不通过→错误提示 | 4 |
| 4 | 用户 | 进入身份验证流程 | 见 [security/otp-verification](../security/otp-verification.md) | 5 |
| 5 | 用户 | 设置新密码 | 见 [security/password-policy](../security/password-policy.md) | 6 |
| 6 | 系统 | 重置完成 | 强制登出 + 清除BIO | 7 |
| 7 | 用户 | 使用新密码重新登录 | - | - |

## 3. 页面清单

---

### 3.1 Reset Password Page（重置密码页）

![Reset Password Page](../assets/account/image13.png)

#### 页面元素

| 元素 | 类型 | 规则 |
|------|------|------|
| 返回按钮 | Button | 点击返回上一级页面 |
| 邮箱输入框 | TextInput | 同注册页邮箱校验规则 |
| Next 按钮 | Button | 初始灰色不可点；输入合法且非空→可点击 |

#### Next 按钮逻辑
- 点击后进入身份验证流程页面

---

### 3.2 身份验证流程页面

> 👉 见 [security/otp-verification.md](../security/otp-verification.md)

---

### 3.3 设置新密码页

> 复用注册流程的「Set Password Page」+ 「Re-enter Password Page」模块

#### 与注册时的差异

| 项目 | 注册时 | 重置密码时 |
|------|--------|-----------|
| 成功后行为 | 自动登录→Set Tag | 强制登出→回到登录页 |
| BIO处理 | 无 | 清除BIO信息，关闭BIO开关 |
| Locked状态 | 不涉及 | 重置成功→立即解除Locked状态 |

---

## 4. 安全规则

| 规则 | 说明 |
|------|------|
| 密码重置后强制登出 | 所有设备上的会话失效 |
| BIO自动关闭 | 清除本地BIO密钥 + 后端关闭BIO开关 |
| Locked 解除 | 密码重置成功→账户状态从 Locked 变回 Active |

## 5. 版本记录

| 日期 | 变更内容 | 变更人 |
|------|----------|--------|
| 2025-10-21 | 初稿 | 吴忆锋 |
| 2025-11-11 | 补充：忘记密码后需自动关闭BIO | 吴忆锋 |
