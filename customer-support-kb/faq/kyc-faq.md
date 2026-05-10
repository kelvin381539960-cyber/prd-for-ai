---
module: kyc-wallet-opening
audience: customer
visibility: user-facing
language: zh-CN
verification_status: draft_pending_review
last_updated: 2026-05-10
---

# KYC FAQ

## Q: 为什么需要身份验证？

### 推荐回答

身份验证用于保护账户安全，并帮助平台满足必要的合规要求。请按照 App 页面提示提交真实、清晰、完整的信息。

### 分类

- module: kyc-wallet-opening
- intent: why_kyc_required
- visibility: user-facing
- verification_status: draft_pending_review

### 转人工

需要转人工：

- 用户询问具体合规或地区限制。
- 用户无法完成验证。

## Q: KYC 一直在审核中怎么办？

### 推荐回答

如果页面显示正在审核，请耐心等待，并保持 App 通知开启。如果审核时间较长，或页面提示需要补充信息，请按照页面提示操作；如果仍无法完成，建议联系人工客服。

### 分类

- module: kyc-wallet-opening
- intent: kyc_pending
- visibility: user-facing
- verification_status: draft_pending_review

### 转人工

需要转人工：

- 审核长时间无结果。
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
- verification_status: draft_pending_review

### 转人工

需要转人工：

- 多次提交证件仍失败。
- 页面提示证件已被使用、信息不匹配或证件类型不支持。
- 用户无法重新提交。

## Q: 人脸验证失败怎么办？

### 推荐回答

请确保面部清晰可见，环境光线充足，并按照页面指引完成操作。请避免遮挡面部、移动过快或使用模糊画面。

如果多次失败，页面可能会限制继续尝试。建议稍后再试或联系人工客服。

### 分类

- module: kyc-wallet-opening
- intent: face_verification_failed
- visibility: user-facing
- verification_status: draft_pending_review

### 转人工

需要转人工：

- 多次人脸验证失败。
- 页面提示尝试次数过多。
- 用户无法继续验证。

## Q: 地址证明上传失败怎么办？

### 推荐回答

请确认文件清晰、完整，并符合页面要求的格式和大小限制。文件应能清楚显示你的姓名、地址和签发信息。

如果页面提示文件不支持、图片不清晰、地址不匹配或文件过期，请根据页面提示重新上传。

### 分类

- module: kyc-wallet-opening
- intent: proof_of_address_failed
- visibility: user-facing
- verification_status: draft_pending_review

### 转人工

需要转人工：

- 地址证明多次上传失败。
- 用户不清楚文件要求。
- 页面提示信息不匹配或文件不被接受。

## Q: 当前国家或地区无法完成 KYC 怎么办？

### 推荐回答

如果页面提示当前国家/地区暂不支持，请以 App 页面展示为准。你可能需要加入 Waitlist，或根据页面提示选择其他可用选项。

如果你不确定自己的状态，建议联系人工客服确认。

### 分类

- module: kyc-wallet-opening
- intent: unsupported_region_waitlist
- visibility: user-facing
- verification_status: draft_pending_review

### 转人工

需要转人工：

- 用户询问具体支持国家/地区。
- 用户无法加入 Waitlist。
- 用户认为页面国家/地区判断不正确。
