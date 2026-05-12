---
module: kyc-wallet-opening
audience: customer
visibility: user-facing
language: zh-CN
verification_status: partial_confirmed
last_updated: 2026-05-12
---

# KYC FAQ

## Q: 为什么需要身份验证？

### 推荐回答

身份验证用于保护账户安全，并帮助平台满足必要的合规要求。请按照 App 页面提示提交真实、清晰、完整的信息。

### 分类

- module: kyc-wallet-opening
- intent: why_kyc_required
- visibility: user-facing
- verification_status: confirmed

### 转人工

需要转人工：

- 用户询问具体合规或地区限制。
- 用户无法完成验证。

## Q: 当前 KYC 支持哪些国家或地区？

### 推荐回答

当前 KYC 仅支持 PH。其他国家或地区后续会陆续开放，请以 App 页面提示为准。

如果页面提示当前国家或地区暂不支持，用户会进入 Waitlist。

### 分类

- module: kyc-wallet-opening
- intent: kyc_supported_region
- visibility: user-facing
- verification_status: confirmed

### 转人工

需要转人工：

- 用户认为地区判断不正确。
- 用户无法进入 Waitlist。

## Q: KYC 审核需要多久？

### 推荐回答

KYC 审核最长 3 个工作日。请保持 App 通知开启，并留意页面状态更新。

如果超过 3 个工作日仍没有结果，或页面提示需要补充信息，建议联系人工客服。

### 分类

- module: kyc-wallet-opening
- intent: kyc_review_time
- visibility: user-facing
- verification_status: confirmed

### 转人工

需要转人工：

- 超过 3 个工作日仍无结果。
- 用户无法重新提交。
- 页面提示失败但原因不清楚。

## Q: 证件扫描失败怎么办？

### 推荐回答

请确保上传或拍摄的证件清晰、完整、光线充足，并且证件类型符合页面要求。避免反光、遮挡、裁切或上传模糊图片。

如果页面仍然提示无法识别或信息不匹配，请按照页面提示重新提交，或联系人工客服。

### 分类

- module: kyc-wallet-opening
- intent: document_verification_failed
- visibility: user-facing
- verification_status: partial_confirmed

### 转人工

需要转人工：

- 多次提交证件仍失败。
- 用户无法重新提交。

## Q: 人脸验证失败怎么办？

### 推荐回答

请确保面部清晰可见，环境光线充足，并按照页面指引完成操作。请避免遮挡面部、移动过快或使用模糊画面。

如果页面提示尝试次数过多、锁定或超时，请按页面提示稍后重试；如果仍无法继续，建议联系人工客服。

### 分类

- module: kyc-wallet-opening
- intent: face_verification_failed
- visibility: user-facing
- verification_status: confirmed

### 转人工

需要转人工：

- 多次人脸验证失败。
- 页面提示尝试次数过多。
- 用户无法继续验证。

## Q: 地址证明有什么要求？

### 推荐回答

地址证明为必需材料。文件大小限制为 16MB，签发时间需在 6 个月内。

请确认文件清晰、完整，并能清楚显示你的姓名、地址和签发信息。具体支持的文件类型请以 App 页面提示为准。

### 分类

- module: kyc-wallet-opening
- intent: proof_of_address_requirement
- visibility: user-facing
- verification_status: partial_confirmed

### 转人工

需要转人工：

- 地址证明多次上传失败。
- 用户不清楚文件要求。
- 页面提示信息不匹配或文件不被接受。

## Q: 身份信息填错后能修改吗？

### 推荐回答

是否可以重新提交或修改，需要看具体发生在哪个环节。请先按照 App 页面提示操作。

如果页面没有修改入口，或你已经提交审核，建议联系人工客服协助处理。

### 分类

- module: kyc-wallet-opening
- intent: identity_info_correction
- visibility: user-facing
- verification_status: confirmed

### 转人工

需要转人工：

- 用户已提交审核后需要修改信息。
- 页面没有重新提交或修改入口。
