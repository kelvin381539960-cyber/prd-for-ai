---
module: account
feature: login
version: 1.0
last_updated: 2025-11-11
authors: [吴忆锋]
status: released
depends_on: [security/otp-verification, security/biometric, security/password-policy]
---

# Login 登录

## 1. 功能概述

已注册用户通过邮箱/手机号 + 密码登录，或通过 Biometric 快捷登录 AIX Card。

## 2. 用户流程

![登录流程图](../assets/account/image2.png)

### 流程步骤（AI-readable）

| 步骤 | 角色 | 动作 | 条件/分支 | 下一步 |
|------|------|------|-----------|--------|
| 1 | 用户 | 打开APP，进入 Navigation Page | - | 2 |
| 2 | 用户 | 点击 "I already have an account" | - | 3 |
| 3 | 用户 | 输入邮箱/手机号 | - | 4 |
| 4 | 前端 | 格式校验 | 不通过→错误提示 | 5 |
| 5 | 后端 | 校验账号存在性、账号状态 | 不存在→提示 / Banned→提示 | 6 |
| 6 | 用户 | 进入身份验证流程 | 见 [security/](../security/) | 7 |
| 7 | 系统 | 验证通过，检测BIO状态 | 已启用BIO→首页 / 未启用→Enable BIO Page | 8 |
| 8 | 用户 | (可选) 启用BIO | 跳过→首页 | 9 |
| 9 | 系统 | 进入APP首页 | - | - |

**Biometric 快捷登录路径：**

| 步骤 | 角色 | 动作 | 条件/分支 | 下一步 |
|------|------|------|-----------|--------|
| 1 | 用户 | 点击 Quick Login | 需本地有BIO密钥 | 2 |
| 2 | 设备 | 拉起生物识别验证 | - | 3 |
| 3 | 设备 | 验证结果 | 成功→后端验证 / 失败→弹窗处理 | 4 |
| 4 | 后端 | 验证BIO签名 | 成功→进入首页 / 失败→清除BIO，跳转手动登录 | - |

## 3. 页面清单

---

### 3.1 Navigation Page（引导页）

> 复用注册功能 Navigation Page，见 [registration.md#31](./registration.md#31-navigation-page引导页)

---

### 3.2 Login Page（登录页）

![Login Page](../assets/account/image8.png)

#### 页面元素

| 元素 | 类型 | 规则 | 必填 |
|------|------|------|------|
| Email/Phone 输入框 | TextInput | 支持邮箱或手机号 | ✅ |
| 国家区号选择器 | Picker | 点击打开国家列表 | 仅手机号时 |
| Next 按钮 | Button | 输入非空+格式通过→可点击 | - |
| Quick Login 按钮 | Button | 仅本地有BIO密钥时显示 | - |
| 协议复选框 | Checkbox | 同注册页 | ✅ |

#### Next 按钮逻辑

| 场景 | 处理 |
|------|------|
| 账号不存在/未注册 | 提示：`您输入的账号信息有误，请检查或注册新账号` |
| 手机号少于6位 | 提示：`Phone number must be at least 6 digits` |
| 账号被 Banned | 提示：`Account locked. Please contact customer support.` |
| 正常 | 跳转身份验证流程页 |

#### Quick Login 按钮

- **显示条件**：App本地检测到可用的 Biometric 密钥信息
- **功能**：点击触发 Biometric 登录流程（见 3.4）

---

### 3.3 Select Country Page（国家选择页）

![Select Country Page](../assets/account/image9.png)

#### 页面规则

- 展示全部国家列表（参考国家和地区list）
- 后端隐藏：中国、中国台湾
- 排序规则：`new Intl.Collator('vi-VN').compare`

#### 常用地区（置顶）

- 澳大利亚
- 新加坡
- 菲律宾
- 越南

---

### 3.4 Biometric 登录

![Biometric Login](../assets/account/image10.png)

#### iOS 人脸识别

| 步骤 | 处理 |
|------|------|
| 点击 Quick Login | 拉起设备人脸验证 |
| 设备端验证通过 | → 后端验证 BIO 签名 |
| 后端验证成功 | → 进入下一步流程 |
| 后端验证失败 | → 弹窗提示错误 + 清除本地BIO + 后端关闭BIO开关 → 跳转手动登录 |
| 设备端验证失败（单数次） | 系统弹窗：`Try FaceID Again` / `Cancel` |
| 设备端验证失败（双数次） | 弹窗：`Cancel` / `Use Other Methods` → 跳转手动登录 |

#### iOS 指纹识别

| 步骤 | 处理 |
|------|------|
| 设备端验证失败（第1次/每轮） | 系统弹窗：`Cancel` |
| 设备端验证失败（第2次/每轮） | 弹窗：`Cancel` / `Use another method` |
| 失败5次（第3轮第1次） | 指纹被锁，引导用户使用其他方式 |

#### Android 人脸 / 指纹

| 步骤 | 处理 |
|------|------|
| 失败弹窗 | 系统弹窗，以各机型实际展示为准 |
| 失败次数限制 | 不限制，以各机型实际限制为准 |
| 超过设备限制次数 | 弹窗提示错误 + `Use another method` → 跳转手动登录 + 清除本地BIO + 隐藏 Quick Login 按钮 |

---

### 3.5 身份验证流程页面

> 👉 见 [security/otp-verification.md](../security/otp-verification.md)

---

### 3.6 Enable BIO Page（BIO启用引导页）

![Enable BIO Page](../assets/account/image11.png)

#### 页面规则

| 条件 | 行为 |
|------|------|
| 未启用BIO | 引导进入此页面 |
| 已启用BIO | 跳过，直接进入APP首页 |
| 手机系统未开启人脸/指纹 | 不弹出引导页，直接进入首页 |

#### 页面元素

| 元素 | 类型 | 规则 |
|------|------|------|
| 关闭按钮 | Button | 点击直接进入首页，Toast：`Login success` |
| 图片 & 标题 & 副标题 | Static | 固定文案 |
| Enable now 按钮 | Button | 点击检测设备BIO权限 |

#### Enable now 按钮逻辑

| 设备权限状态 | 处理 |
|--------------|------|
| 已授权 | 直接调起生物认证流程 |
| 未授权 | 弹窗引导至系统权限设置 |

#### 特殊处理

- 需调用身份认证接口
- 登录后 **5分钟内**：无需再次身份验证
- 登录后 **5分钟后**：需身份验证后再设置

---

## 4. 版本记录

| 日期 | 变更内容 | 变更人 |
|------|----------|--------|
| 2025-10-21 | 初稿 | 吴忆锋 |
| 2025-10-29 | 登录密码规则调整 | 吴忆锋 |
| 2025-11-11 | 补充BIO相关规则 | 吴忆锋 |
