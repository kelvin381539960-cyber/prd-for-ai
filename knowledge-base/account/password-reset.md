---
module: account
page: password-reset
title: 忘记密码流程
source_doc: "AIX Card 注册登录需求V1.0 (2).docx"
version: "1.0"
last_updated: 2025-01-20
country_support: [VN, PH, AU]
status: active
tags: [password-reset, forgot-password, account, security, bio]
---

# AIX Card 注册登录需求 V1.0 — 忘记密码流程

> 本文档由原始 PRD（飞书导出 .docx）100% 原文转译为结构化 Markdown，未做任何内容精简或归纳。
> 项目背景、项目目的、国家线、账户规则等全局信息见 [registration.md](./registration.md) 章节2-5。

---

## 7.3 忘记密码流程页面

### 7.3.1 功能说明

当用户重置密码后，需要清除BIO信息，已开启的BIO需要自动关闭。

### 7.3.2 页面概览

> 原始PRD参考截图（飞书文档截图，含忘记密码流程所有页面概览）

![忘记密码页面概览](../assets/account/image40.jpeg)

---

### 7.3.3 Reset Password Page（重置密码页）

#### UX 参考截图

> 原始PRD参考截图（飞书文档截图，含重置密码页UI原型 — 多状态展示同一页面）

| 状态 | UX截图 |
|------|--------|
| 默认状态 | ![Reset Password Page UX](../assets/account/image41.jpeg) |

#### 功能说明

**1. 返回按钮**

- 点击返回上一级页面

**2. 下一步按钮**

- 初始为灰色不可点击；当输入合法且非空时高亮可点击。
- 点击进入身份验证流程页面

---

### 7.3.4 身份验证流程页面

> 详细需求见：AIX Security 身份认证需求V1.0

---

### 7.3.5 设置密码页

**功能说明：**
- 复用设置密码页模块（详见 [registration.md → 7.6 Set Password Page](./registration.md#76-set-password-page设置密码页)）

**安全规则：**
- 密码重置成功后，系统将强制登出当前账户，用户需使用新密码重新登录。
