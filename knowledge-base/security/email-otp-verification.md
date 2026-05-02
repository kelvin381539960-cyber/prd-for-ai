---
module: security
feature: email-otp-verification
version: "1.0"
status: active
source_doc: 历史prd/AIX Security 身份认证需求V1.0 (1).docx
source_section: 8.3 Email OTP认证
last_updated: 2026-05-01
owner: 吴忆锋
depends_on:
  - security/_index
  - security/global-rules
  - account/_index
  - _meta/limits-and-rules
  - _meta/error-code-dictionary
  - _meta/writing-standard
---

# Email OTP Verification 邮箱验证码认证

## 1. 功能定位

Email OTP Verification 用于通过用户邮箱接收并输入 4 位数字验证码，完成 AIX 自有 Email OTP 身份认证。

本文件只沉淀 Email OTP 页面、邮箱掩码展示、输入规则、验证失败处理、锁定规则、重新发送规则和安全限制。OTP、Login Passcode、Biometric、Face Authentication 不在本文重复定义。

## 2. 适用范围

| 维度 | 规则 | 来源 | 备注 |
|---|---|---|---|
| 认证方式 | Email OTP | AIX Security 身份认证需求V1.0 / 7.1 认证方式&限制 | 邮箱验证码 |
| 验证码位数 | 4 位数字 | AIX Security 身份认证需求V1.0 / 8.3.1 Email OTP Verify Page | 用户需输入完整 4 位 |
| 验证码有效期 | 5 分钟 | AIX Security 身份认证需求V1.0 / 8.3.1 Email OTP Verify Page | 过期后需重新获取 |
| 发送方式 | 系统向用户指定邮箱发送包含 4 位数字 OTP 的邮件 | AIX Security 身份认证需求V1.0 / 8.3.1 Email OTP Verify Page | 邮箱来源见页面规则 |
| 邮箱展示 | 取 `user_info` 中的 email 地址，掩码展示 | AIX Security 身份认证需求V1.0 / 8.3.1 Email OTP Verify Page | @ 前首位、末位与邮箱后缀明文，中间按位数展示 `*` |
| 锁定方式 | 场景隔离锁定 | AIX Security 身份认证需求V1.0 / 7.1 认证方式&限制 | 适用于邮箱验证码 |

## 3. 前置条件

| 条件 | 说明 | 来源 |
|---|---|---|
| 用户存在可接收邮件的邮箱 | Email OTP 发送至用户指定邮箱 | AIX Security 身份认证需求V1.0 / 8.3.1 |
| 当前业务场景允许 Email OTP | 是否使用 Email OTP 由 Security 场景矩阵决定 | AIX Security 身份认证需求V1.0 / 7.2 |
| 认证未触发锁定 | 达到失败次数或重发次数上限时不可继续 | AIX Security 身份认证需求V1.0 / 8.3.1 |
| 用户进入 Email OTP Verify Page | 进入页面后自动触发发送 OTP 请求 | AIX Security 身份认证需求V1.0 / 8.3.1 |

## 4. 业务流程

### 4.1 主链路

```text
Business Flow → Email OTP Verify Page → Auto Send Email OTP → User Inputs 4-digit Code → Auto Submit → Success / Failed / Locked
```

### 4.2 业务流程与系统交互时序图

```mermaid
sequenceDiagram
    autonumber
    actor User as User
    participant Business as Business Module
    participant Client as AIX App / Client
    participant Security as Security Module

    Business->>Client: 进入 Email OTP 认证流程
    Client-->>User: 展示 Email OTP Verify Page
    Client->>Security: 页面进入后自动请求发送 Email OTP
    Security-->>Client: 向用户指定邮箱发送 4 位数字 OTP
    Client-->>User: 展示掩码邮箱与验证码输入框
    User->>Client: 输入 4 位数字验证码
    Client->>Client: 仅接受 4 位数字，按顺序输入，删除从最后一位开始
    alt 未输入完整 4 位
        Client-->>User: 停留当前输入状态
    else 已输入完整 4 位
        Client->>Security: 自动提交 Email OTP 校验
        alt 验证成功
            Security-->>Business: 进入下一流程
        else 验证失败但未锁定
            Security-->>Client: 返回失败与剩余次数
            Client-->>User: 展示 Invalid OTP hint 或 Invalid OTP 弹窗
        else 验证失败触发锁定
            Security-->>Client: 返回锁定状态与可重试时间
            Client-->>User: 展示锁定弹窗，退出登录并返回业务流程发起页
        end
    end

    opt User requests resend after 60s countdown
        User->>Client: 点击重新发送
        Client->>Security: 请求重新发送 Email OTP
        alt 未达重发上限
            Security-->>Client: 发送新 Email OTP，旧 OTP 立即失效
        else 达到 24 小时内 3 次重发上限
            Security-->>Client: 返回重发冷却
            Client-->>User: 展示 Too Many requests 弹窗
        end
    end
```

### 4.3 业务逻辑矩阵

| 阶段 | 触发条件 | 前端 / 页面行为 | Security 动作 | 成功结果 | 失败结果 |
|---|---|---|---|---|---|
| 进入页面 | 业务模块进入 Email OTP 认证 | 展示 Email OTP Verify Page | 自动发送 Email OTP 请求 | 用户接收邮箱验证码 | 发送失败规则原文未展开 |
| 邮箱展示 | Email OTP Verify Page 展示 | 展示 `user_info.email` 掩码 | 无 | 用户识别接收邮箱 | 无 |
| 验证码输入 | 用户输入验证码 | 仅接受 4 位数字；按顺序输入；删除从最后一位开始 | 无 | 输入满 4 位后自动提交 | 非数字无效 |
| Email OTP 校验 | 输入满 4 位 | 自动提交，无需确认按钮 | 校验最新一次 Email OTP | 进入下一流程 | Invalid OTP / 剩余次数提示 / 锁定 |
| 重新发送 | 60s 倒数结束 | 用户可请求重新发送 | 发送新 Email OTP，旧 OTP 立即失效 | 用户使用新验证码 | 达到重发上限后冷却 |

## 5. 页面关系总览

本节只表达 Email OTP Verification 涉及的页面节点和弹窗节点。

```mermaid
flowchart LR
    Business[Business Flow]
    EmailOTP[Email OTP Verify Page]
    ExitConfirm[Confirm Exit Popup]
    InvalidHint[Invalid OTP Hint]
    InvalidPopup[Invalid OTP Popup]
    Locked[Too Many Attempts Popup]
    TooManyRequests[Too Many requests Popup]
    Next[Next Business Step]
    Entry[Business Flow Entry]

    Business -->|Require Email OTP| EmailOTP
    EmailOTP -->|Back| ExitConfirm
    ExitConfirm -->|Stay and continue| EmailOTP
    ExitConfirm -->|Leave| Entry

    EmailOTP -->|4 digits entered and valid| Next
    EmailOTP -.->|Invalid, attempts enough| InvalidHint
    EmailOTP -.->|Invalid, attempts low| InvalidPopup
    InvalidPopup -->|Stay and continue| EmailOTP
    InvalidPopup -->|Leave| Entry

    EmailOTP -.->|Locked 20min| Locked
    EmailOTP -.->|Locked 24h / resend cooling| TooManyRequests
    Locked -->|Try again later| Entry
    TooManyRequests -->|Try again later| Entry
```

## 6. 页面卡片与交互规则

### 6.1 Email OTP Verify Page

![Email OTP Verify Page](../assets/security/image10.png)

| 维度 | 内容 |
|---|---|
| 页面目的 | 用户输入邮箱 OTP 完成身份认证 |
| 入口 | 业务模块根据场景矩阵进入 Email OTP 认证 |
| 出口 | 验证成功进入下一业务流程；失败按次数展示 hint / popup / lock |
| 关键规则 | 页面进入后自动发送 OTP；输入完整 4 位后自动提交 |

| 元素 | 类型 | 展示条件 | 交互规则 | 来源 |
|---|---|---|---|---|
| Back | Button | 页面展示时 | 点击弹出 Confirm Exit 弹窗 | 8.3.1 |
| Title | Text | 页面展示时 | 固定文案，原文未给出具体文本 | 8.3.1 |
| Subtitle | Text | 页面展示时 | 固定文案，包含掩码邮箱 | 8.3.1 |
| Email Address | Text | 页面展示时 | 取 `user_info.email` 并掩码展示 | 8.3.1 |
| OTP Input | Input | 页面展示时 | 仅接受 4 位数字；按顺序输入；删除从最后一位开始 | 8.3.1 |
| Auto Submit | System action | 输入满 4 位 | 自动提交验证请求，无需确认按钮 | 8.3.1 |
| Resend | Action | 60s 倒数结束 | 用户可请求重新发送验证码 | 8.3.1 |

邮箱掩码规则：

| 规则 | 示例 | 来源 |
|---|---|---|
| @ 前首位和末位明文，邮箱后缀明文，中间位数用同位数 `*` 展示 | `test43500@gmail.com` → `t*******0@gmail.com` | 8.3.1 |

### 6.2 Confirm Exit Popup

| 元素 | 文案 / 规则 | 来源 |
|---|---|---|
| Title | `Confirm Exit?` | 8.3.1 |
| Content | `Are you sure you want to leave before verification is complete?` | 8.3.1 |
| Stay and continue | 关闭弹窗，停留当前页 | 8.3.1 |
| Leave | 关闭弹窗，返回业务流程发起页 | 8.3.1 |

### 6.3 Invalid OTP 处理

| 触发条件 | 展示方式 | 文案 | 用户动作 | 来源 |
|---|---|---|---|---|
| 验证失败，剩余可尝试次数大于 2 次 | 红字错误 hint | `Invalid OTP` | 继续尝试 | 8.3.1 |
| 验证失败，剩余可尝试次数等于或小于 2 次，且未触发锁定 | Popup | `Invalid OTP` + 剩余次数提示 | Stay and continue / Leave | 8.3.1 |

剩余次数弹窗内容：

| 区间 | Content | 来源 |
|---|---|---|
| 失败次数在 0–5 区间且剩余次数 ≤ 2 | `You have {times} attempts left before being locked out for 20 minutes.` | 8.3.1 |
| 失败次数在 5–10 区间且剩余次数 ≤ 2 | `You have {times} attempts left before being locked out for 24 hours.` | 8.3.1 |

### 6.4 锁定弹窗

| 触发条件 | Title | Content | Button | 用户落点 | 来源 |
|---|---|---|---|---|---|
| 24 小时内连续失败达到 5 次 | `Too Many Attempts` | `You've reached the maximum number of attempts. Please try again in {time}.` | `Try again later` | 退出登录并返回上一级页面 | 8.3.1 / 7.6.2 |
| 24 小时内连续失败达到 10 次 | `Too Many requests` | `You've requested new codes too frequently. Please try again in {time}.` | `Try again later` | 退出登录并返回业务流程发起页 | 8.3.1 |

### 6.5 重新发送与冷却弹窗

| 触发条件 | Title | Content | Button | 用户落点 | 来源 |
|---|---|---|---|---|---|
| 24 小时内重新发送验证码达到 3 次 | `Too Many requests` | `You've requested new codes too frequently. Please try again in {time}.` | `Try again later` | 退出登录并返回业务流程发起页 | 8.3.1 |

## 7. 字段与接口依赖

| 字段 / 能力 | 用途 | 读/写 | 来源 | 备注 |
|---|---|---|---|---|
| user_info.email | Email OTP 接收邮箱 | 读 | 8.3.1 | 页面展示时进行掩码 |
| emailOtpCode | 用户输入验证码 | 读 | 8.3.1 | 4 位数字 |
| emailOtpExpiresAt | Email OTP 有效期 | 读 / 写 | 8.3.1 | 5 分钟 |
| latestEmailOtp | 最新一次发送的 Email OTP | 写 | 8.3.1 | 旧验证码立即失效，仅最后一次有效 |
| failureCount24h | 24 小时失败次数 | 读 / 写 | 7.1 / 8.3.1 | 5 次、10 次锁定判断 |
| remainingAttempts | 剩余可尝试次数 | 读 | 8.3.1 | 用于低次数提醒 |
| resendCount24h | 24 小时重发次数 | 读 / 写 | 8.3.1 | 最多 3 次 |
| lockUntil | 锁定结束时间 | 读 / 写 | 7.1 / 8.3.1 | 20 分钟或 24 小时 |
| requestDevice | 发起请求设备 | 读 | 8.3.1 | 验证码仅限发起请求设备使用 |

## 8. 异常与失败处理

| 场景 | 触发条件 | 用户提示 | 系统动作 | 最终状态 | 来源 |
|---|---|---|---|---|---|
| 非数字输入 | 用户输入非数字字符 | 无明确文案 | 非数字字符无效 | 留在 Email OTP Verify Page | 8.3.1 |
| 未输入完整 4 位 | 用户未完成 4 位输入 | 无明确文案 | 不提交 | 留在 Email OTP Verify Page | 8.3.1 |
| Email OTP 验证失败，剩余次数 > 2 | 验证失败未触发锁定 | `Invalid OTP` | 允许继续尝试 | 留在 Email OTP Verify Page | 8.3.1 |
| Email OTP 验证失败，剩余次数 ≤ 2 | 验证失败未触发锁定 | Invalid OTP 弹窗 | 允许继续尝试或退出 | 当前页 / 业务流程发起页 | 8.3.1 |
| 24 小时内失败 5 次 | 达到第一次锁定阈值 | Too Many Attempts | 锁定 20 分钟 | 返回上一级页面 | 7.1 / 8.3.1 |
| 24 小时内失败 10 次 | 达到第二次锁定阈值 | Too Many requests | 锁定 24 小时 | 返回业务流程发起页 | 7.1 / 8.3.1 |
| 重新发送达到上限 | 24 小时内重发 3 次 | Too Many requests | 触发 20 分钟冷却 | 返回业务流程发起页 | 8.3.1 |
| 旧 Email OTP 被替换 | 用户重新发送 Email OTP | 无 | 旧验证码立即失效 | 仅最新 Email OTP 有效 | 8.3.1 |
| 更换设备验证 | 非发起请求设备使用验证码 | 原文未明确提示 | 验证码无效 | 阻止通过 | 8.3.1 |

## 9. 风控 / 合规边界

| 边界 | 规则 | 影响 | 来源 |
|---|---|---|---|
| 验证码位数 | Email OTP 为 4 位数字 | 控制输入与自动提交条件 | 8.3.1 |
| 验证码有效期 | 5 分钟有效 | 过期后不可继续使用 | 8.3.1 |
| 最新验证码有效 | 每次重新发送生成新随机 OTP，旧 OTP 立即失效 | 防止旧验证码复用 | 8.3.1 |
| 设备限制 | 验证码仅限发起请求设备使用，更换设备无效 | 防止跨设备复用 | 8.3.1 |
| 失败锁定 | 24 小时内失败 5 次锁定 20 分钟；10 次锁定 24 小时 | 防暴力破解 | 7.1 / 8.3.1 |
| 重发冷却 | 24 小时内最多 3 次重发，达到上限后冷却 20 分钟 | 防邮件轰炸与滥用 | 8.3.1 |
| 场景隔离锁定 | Email OTP 使用场景隔离锁定 | 不同业务场景锁定隔离 | 7.1 |

## 10. 来源引用

- (Ref: 历史prd/AIX Security 身份认证需求V1.0 (1).docx / 7.1 认证方式&限制 / V1.0)
- (Ref: 历史prd/AIX Security 身份认证需求V1.0 (1).docx / 7.2 不同场景的验证方式 / V1.0)
- (Ref: 历史prd/AIX Security 身份认证需求V1.0 (1).docx / 7.6.2 Too many failed popup / V1.0)
- (Ref: 历史prd/AIX Security 身份认证需求V1.0 (1).docx / 8.3 Email OTP认证 / V1.0)
- (Ref: knowledge-base/security/_index.md)
- (Ref: knowledge-base/security/global-rules.md)
- (Ref: knowledge-base/changelog/knowledge-gaps.md / Security Email OTP / 2026-05-01)
