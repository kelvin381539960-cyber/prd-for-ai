---
module: security
page: login-passcode-verification
title: Login Passcode 认证页面（密码验证）
version: "1.0"
source_doc: "AIX Security 身份认证需求V1.0 (1).docx"
section: "8.4"
---

# 8.4 Login Passcode认证

## 8.4.1 页面概览

![原始PRD参考截图（飞书文档截图，含导航+UI原型+描述）— 仅供参考](../assets/security/image9.png)

## 8.4.2 Login Passcode Verify Page

### 页面截图

![原始PRD参考截图（飞书文档截图，含导航+UI原型+描述）— 仅供参考](../assets/security/image8.png)

### 返回按钮

点击弹出挽留弹窗：

- Title：Confirm Exit?
- Content: Are you sure you want to leave before verification is complete?
- Button:
  - **Stay and continue**: 点击后关闭弹窗，停留在当前页；
  - **Leave**: 点击后关闭弹窗，返回到业务流程发起页；

### 密码输入框

#### 2.1 输入规则

**长度限制**：最长输入32个字符。当用户输入超过32个字符时，前端应禁止其继续输入。

**支持的字符类型：**
- 小写字母：a - z
- 大写字母：A - Z
- 数字：0 - 9
- 符号/特殊字符：常见的标点符号和特殊字符，例如：! @ # $ % ^ & * ( ) _ + - = { } [ ] | \ : " ; ' < > ? , . / 等。

**显示控制：**
- 默认状态：输入框内所有字符以密文形式显示。
- 显示/隐藏切换：输入框右侧必须提供"眼睛"图标。
  - 图标为"闭眼"状态时，显示密文。
  - 用户点击后，密码以明文显示。

### Next按钮

**前端校验规则**：仅当密码输入框非空且字符数不少于8位时，"下一步"按钮才变为可点击。

**点击按钮验证处理规则：**

**验证成功**，进入下一流程。

**验证失败（连续失败次数（0，5） 但剩余可尝试次数 大于2次）**，不触发锁定：
- 红字错误hint提示："Incorrect account or password"。

**验证失败（连续失败次数（0，5） 且剩余可尝试次数 等于或小于2次）**，不触发锁定，弹窗提示：
- Title：Incorrect account or password
- Content：You have {times} attempts left before a {time} lock.
- Button: Stay and continue：关闭弹窗，允许继续尝试。
- Button: Leave：退出登录，返回业务流程发起页。

**验证失败（用户在24小时内连续失败达到 5次）**，触发锁定20分钟，弹窗提示：
- Title：Too Many Attempts
- Content：You've reached the maximum number of attempts. Please try again in {time}.
- "Try again later"按钮，点击后退出登录并返回业务流程发起页。
- 此弹窗复用【7.6.2 Too many failed popup】

**验证失败（连续失败次数（5，10）， 但剩余可尝试次数 大于2次）**，不触发锁定：
- 红字错误hint提示："Incorrect account or password"。

**验证失败（连续失败次数（5，10） 且剩余可尝试次数 等于或小于2次）**，不触发锁定，弹窗提示：
- Title：Incorrect account or password
- Content：You have {times} attempts left before being locked out for 24 hours.
- Button: Stay and continue：关闭弹窗，允许继续尝试。
- Button: Leave：退出登录，返回业务流程发起页。

**验证失败（用户在24小时连续失败达到 10次）**，触发锁定24小时，弹窗提示：
- Title：Too Many Attempts
- Content：You've reached the maximum number of attempts. Please try again in {time}.
- "Try again later"按钮，点击后退出登录并返回业务流程发起页。
