---
module: security
page: api-reference
title: 外部接口依赖 + 错误码映射
version: "1.0"
source_doc: "AIX Security 身份认证需求V1.0 (1).docx"
section: "9-10"
---

# 外部接口依赖

## 9.1 外部接口清单

### 9.1.1 生成url

**请求路径：**

`[POST] /openapi/v1/ekyc/get-verification-url`

**请求参数：**

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| query.successRedirectUrl | string | 是 | 验证成功后跳转的回调 URL |
| query.failureRedirectUrl | string | 是 | 验证失败后跳转的回调 URL |
| tokenAuthType | string | 是 | |

**响应：**

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| urlExpiredTime | string | 是 | url 过期时间 |
| requestId | string | 是 | 用来获取验证结果 |

### 9.1.2 查询验证结果

**请求路径：**

`[GET] /openapi/v1/ekyc/get-auth-result/{requestId}`

**请求参数：**

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| requestId | string | 是 | |

**响应：**

| 字段 | 类型 | 说明 |
|------|------|------|
| token | string | 验证成功时才会返回 |
| tokenExpiredTime | string | token过期时间 |
| status | string | 状态：INCOMPLETE（包含未验证和验证中），PASS 成功，FAIL 失败(需要重新生成url) |

## 9.2 外部接口地址

Master sub account 设计方案

---

# 10. 接口错误码映射

## 10.1 passport error code

| API 错误码 (code) | 解释 | AIX映射前端提示文案 |
|---|---|---|
| LIVENESS_ATTACK | 检测到活体攻击风险/疑似非真人操作 | Liveness verification failed. Please try again in a well-lit environment. |
| SIMILARITY_FAILED | 人脸比对失败/与证件照不一致 | Face verification failed. Please make sure your face matches your ID photo. |
| UNABLE_GET_IMAGE | 未获取到有效人脸图片 | Unable to capture a clear face image. Please try again. |
| PARAMETER_ERROR | 请求参数异常 | Face verification could not be completed at this time. Please try again later. |
| USER_TIMEOUT | 用户超时 | Face verification timed out. Please try again. |
| RETRY_COUNT_REACH_MAX | 重试次数已达上限 | You have reached the maximum number of attempts. Please try again later. |
| FACE_QUALITY_TOO_POOR | 人脸图片质量过低 | Face image quality is too poor. Please try again in better lighting. |
| ERROR | 通用错误 | Face verification could not be completed at this time. Please try again later. |
| DEFAULT | 兜底文案 | The identity document could not be verified. Please ensure it is valid and try again. |

---

# 11. 待定事项

验证处理规则：需要列出来10次，以及验证错误4，5次的提示语优化。
