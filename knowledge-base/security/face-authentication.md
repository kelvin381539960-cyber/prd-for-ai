---
module: security
page: face-authentication
title: 活体识别认证（DTC 侧人脸识别）
version: "1.0"
source_doc: "AIX Security 身份认证需求V1.0 (1).docx"
section: "8.6"
---

# 8.6 活体识别认证

## 8.6.1 流程说明

![原始PRD参考截图（飞书文档截图，含导航+UI原型+描述）— 仅供参考](../assets/security/image14.jpeg)

## 8.6.2 页面概览

![原始PRD参考截图（飞书文档截图，含导航+UI原型+描述）— 仅供参考](../assets/security/image15.jpeg)

> liveness采集失败不会计费，采集成功才会计费

---

## 8.6.3 Face Auth Guide Page

### 页面截图

![原始PRD参考截图（飞书文档截图，含导航+UI原型+描述）— 仅供参考](../assets/security/image16.png)

### 页面说明

本页面为活体识别流程的入口引导页，用于向用户展示识别前的注意事项。

### 返回按钮

点击后返回至上一级页面，中断当前识别流程。

### "Start" 按钮

**未锁定状态：** 用户点击后，系统调用AAI的H5页开始做活体采集；

**锁定状态：** 用户失败次数过多，后端返回被锁定，点击按钮弹窗拦截：
- Title：Facial Verification Locked
- Content：You've reached the maximum attempts for facial verification. Please try again after [MM-DD hh:mm].
- MM-DD hh:mm为解锁时间
- OK按钮：点击按钮，返回流程入口页

### 安全限制规则

系统需基于用户账户维度，需执行以下限制：

- **规则一**：24小时内累计失败 5次，该面部验证功能将被系统锁定 20分钟。
- **规则二**：24小时内累计失败 10次，该面部验证功能将被系统锁定 24小时。
- **规则三**：24小时内，接口层面连续发起20次则锁20min，验证成功后清零重新计算。

**计数与清零：**
- 规则一和规则二的累计失败判断：DTC返回face result=fail才算失败，其他结果不算失败（其他结果不计费）
- 清零规则：人脸验证通过后则清零。

---

## 8.6.4 Liveness Scan Page（AAI页面）

### 页面截图

![原始PRD参考截图（飞书文档截图，含导航+UI原型+描述）— 仅供参考](../assets/security/image17.png)

### 页面说明

当用户进入submission received页面时，AAI已经有了face 比对结果。

点击按钮，跳转到Face Auth Loading Page。

---

## 8.6.5 Face Auth Loading Page

### 页面截图

![原始PRD参考截图（飞书文档截图，含导航+UI原型+描述）— 仅供参考](../assets/security/image18.png)

### 返回按钮

点击弹出挽留弹窗：
- Title：Confirm Exit?
- Content: Are you sure you want to leave before verification is complete?
- Button:
  - **Stay and continue**: 点击后关闭弹窗，停留在当前页；
  - **Leave**: 点击后关闭弹窗，返回到业务流程入口页；

### 页面说明

当 AAI 返回活体识别成功时，跳转至本页面。

页面加载后，以固定时间间隔向后台接口发送请求，查询认证结果状态：

- **成功**：当后端返回成功状态时，页面自动跳转至业务流程的下一页面；
- **失败**：后端查询DTC，DTC返回FAIL / EXPIRED / incomplete / 空值，那么判断为失败：自动跳转至 Face Auth Failed Page。
- **网络异常**：进入Network Error Page
- **系统异常**：进入Server Error Page
- **超时**：若等待超过30秒仍未收到结果，进入Loading Failed Page

---

## 8.6.6 Face Auth Failed Page

### 页面截图

![原始PRD参考截图（飞书文档截图，含导航+UI原型+描述）— 仅供参考](../assets/security/image19.png)

### 页面说明

当 AAI 返回活体识别失败结果时，跳转至本页面。用户可选择重新尝试或退出流程。

### 返回按钮

点击按钮，返回业务流程入口页。

### 页面文案

- 固定主文案：固定显示 "Verification failed."。
- 后端返回face result为空值，那么展示文案：Liveness check failed. Please try again.
- 后端返回face result为FAIL / EXPIRED / incomplete，那么展示Face Comparison API错误码映射中的映射前端提示文案

### Try again按钮

**正常状态：** 点击该按钮将返回身份认证入口页。

**锁定状态：** 当账户触发安全锁时，点击按钮弹窗提示：
- 文案：For your account security, facial verification is temporarily unavailable. Please try again after [解锁时间]。
- 确认按钮：点击直接返回至流程入口页。
