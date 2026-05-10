---
module: card
audience: customer
visibility: user-facing
language: zh-CN
verification_status: draft_pending_review
last_updated: 2026-05-10
---

# 卡 FAQ

## Q: 如何申请卡？

### 推荐回答

如果 App 当前提供卡申请入口，你可以按照页面提示提交申请。申请前请确保账户信息和身份验证状态符合页面要求。具体是否可申请、支持地区、费用、限额和审核要求，请以 App 页面提示为准。

### 分类

- module: card
- intent: card_application
- visibility: user-facing
- verification_status: draft_pending_review

### 转人工

需要转人工：

- 用户看不到申请入口。
- 卡申请失败或长时间无结果。
- 用户询问未确认的费用、限额或支持地区。

## Q: 卡交易失败怎么办？

### 推荐回答

请先确认卡状态、交易金额、商户信息和网络状态。如果交易失败、重复扣款或金额异常，建议联系人工客服，并准备好交易时间、金额、商户名称和页面截图。

### 分类

- module: card
- intent: card_transaction_failed
- visibility: user-facing
- verification_status: draft_pending_review

### 转人工

需要转人工：

- 重复扣款。
- 金额异常。
- 卡被冻结或无法使用。
