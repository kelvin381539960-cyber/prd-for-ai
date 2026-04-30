---
module: security
page: email-otp-verification
title: Email OTP 认证页面（邮箱验证码）
version: "1.0"
source_doc: "AIX Security 身份认证需求V1.0 (1).docx"
section: "8.3"
---

# 8.3 Email OTP认证

## 8.3.1 Email OTP Verify Page

### 页面截图

![原始PRD参考截图（飞书文档截图，含导航+UI原型+描述）— 仅供参考](../assets/security/image10.png)

### 页面规则

进入页面后，自动触达发送otp的请求。

### 返回按钮

点击弹出挽留弹窗：

- Title：Confirm Exit?
- Content: Are you sure you want to leave before verification is complete?
- Button:
  - **Stay and continue**: 点击后关闭弹窗，停留在当前页；
  - **Leave**: 点击后关闭弹窗，返回到业务流程发起页；

### 标题/副标题

固定文案。

**邮箱地址**：取user_info中的email 地址，掩码展示，邮箱@之前的首位和末位以及邮箱后缀明文展示，中间位数用掩码*展示，*的展示个数与位数相同；

举例：用户email地址为：test43500@gmail.com，前端展示为：t*******0@gmail.com；

### 密码输入框

#### 4.1 验证码发送与接收

系统需向用户指定的邮箱发送一封包含 **4位数字验证码（OTP）** 的邮件。

用户需在验证页面输入收到的完整4位验证码。

验证码5分钟有效期。

#### 4.2 验证码输入规则

- 输入框仅接受4位数字输入，非数字字符无效。
- 用户必须按顺序依次输入每一位数字。
- 删除操作仅支持从最后一位开始逐位向前删除。

#### 4.3 自动提交验证

当系统检测到用户已输入完4位验证码时，应自动触发提交验证请求，无需用户手动点击确认按钮。

#### 4.4 验证处理规则

**验证成功**，进入下一流程。

**验证失败（连续失败次数（0，5） 但剩余可尝试次数 大于2次）**，不触发锁定：
- 红字错误hint提示："Invalid OTP"。

**验证失败（连续失败次数（0，5） 且剩余可尝试次数 等于或小于2次）**，不触发锁定，弹窗提示：
- Title：Invalid OTP
- Content：You have {times} attempts left before being locked out for 20 minutes.
- Button: Stay and continue：关闭弹窗，允许继续尝试。
- Button: Leave：退出登录，返回业务流程发起页。

**验证失败（用户在24小时内连续失败等于 5次）**，触发锁定20分钟，弹窗提示：
- Title：Too Many Attempts
- Content：You've reached the maximum number of attempts. Please try again in {time}.
- "Try again later"按钮，点击后退出登录并返回上一级页面。
- 此弹窗复用【7.6.2 Too many failed popup】

**验证失败（连续失败次数（5，10）， 但剩余可尝试次数 大于2次）**，不触发锁定：
- 红字错误hint提示："Invalid OTP"。

**验证失败（连续失败次数（5，10） 且剩余可尝试次数 等于或小于2次）**，不触发锁定，弹窗提示：
- Title：Invalid OTP
- Content：You have {times} attempts left before being locked out for 24 hours.
- Button: Stay and continue：关闭弹窗，允许继续尝试。
- Button: Leave：退出登录，返回业务流程发起页。

**验证失败（用户在24小时连续失败达到 10次）**，触发锁定24小时，弹窗提示：
- Title：Too Many requests
- Content：You've requested new codes too frequently. Please try again in {time}.
- "Try again later"按钮，点击后退出登录并返回业务流程发起页。

#### 4.5 重新发送规则

60s倒数结束，用户可请求重新发送验证码。

**冷却限制**：用户在 24 小时内最多可执行 3 次验证码"重新发送"操作。达到上限后，系统将触发20分钟的冷却期，弹窗提示：
- Title：Too Many requests
- Content：You've requested new codes too frequently. Please try again in {time}.
- "Try again later"按钮，点击后退出登录并返回业务流程发起页。

**验证码安全规则：**
- 每次重新发送验证码后，之前的旧验证码立即失效，仅以最新发送的验证码为准。
- 该验证码仅限发起请求的设备使用，更换设备无效。

### 其他规则

每次发送otp都是新的随机生成的，验证的时候以最后一次发送的有效。
