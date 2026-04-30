---
module: security
feature: password-policy
version: 1.0
last_updated: 2025-10-29
authors: [吴忆锋]
status: released
depends_on: []
---

# Password Policy 密码策略

## 1. 功能概述

AIX 全局统一的密码安全规范，适用于注册设置密码和重置密码场景。

## 2. 密码规则

### 2.1 基本要求

| 规则项 | 要求 |
|--------|------|
| 最小长度 | 8 字符 |
| 最大长度 | 32 字符 |
| 超出限制 | 前端禁止继续输入，Toast：`密码最长32个字符` |

### 2.2 复杂度要求（全部必须满足）

| 类型 | 范围 | 缺失提示 |
|------|------|----------|
| 小写字母 | a-z | `Password must include a lowercase letter` |
| 大写字母 | A-Z | `Password must include an uppercase letter` |
| 数字 | 0-9 | `Password must include a number` |
| 特殊符号 | `! @ # $ % ^ & * ( ) _ + - = { } [ ] \| \ : " ; ' < > ? , . /` 等 | `Password must include a supported symbol` |

### 2.3 显示控制

| 状态 | 说明 |
|------|------|
| 默认 | 密文显示（圆点•或星号*） |
| 眼睛图标-闭眼 | 密文 |
| 眼睛图标-睁眼 | 明文 |
| 切换 | 点击眼睛图标切换明文/密文 |

## 3. 校验时机

| 场景 | 校验时机 |
|------|----------|
| 注册 - Set Password Page | **失焦后校验**（blur event） |
| 注册 - Re-enter Password Page | **实时动态校验**（onChange） |
| 重置密码 | 同上两种页面规则 |

## 4. 确认密码（Re-enter）

| 规则项 | 说明 |
|--------|------|
| 一致性校验 | 与第一次输入对比 |
| 不一致提示 | `Passwords do not match. Please try again.` |

## 5. 调用方

- `account/registration` — 设置密码 + 确认密码
- `account/password-reset` — 重设密码 + 确认密码
