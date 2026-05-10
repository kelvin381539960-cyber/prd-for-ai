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

如果 App 当前提供卡申请入口，你可以按照页面提示选择卡类型、卡片信息和支付币种，并提交申请。申请前请确保账户信息、钱包开户和身份验证状态符合页面要求。

具体是否可申请、支持地区、费用、限额、卡数量和审核要求，请以 App 页面提示为准。

### 分类

- module: card
- intent: card_application
- visibility: user-facing
- verification_status: draft_pending_review

### 转人工

需要转人工：

- 用户看不到申请入口。
- 卡申请失败或长时间无结果。
- 用户询问未确认的费用、限额、支持地区或卡数量。

## Q: 卡申请一直在审核中怎么办？

### 推荐回答

请耐心等待页面状态更新，并保持 App 通知开启。如果长时间没有结果，或你需要确认申请状态，建议联系人工客服。

### 分类

- module: card
- intent: card_application_pending
- visibility: user-facing
- verification_status: draft_pending_review

### 转人工

需要转人工：

- 审核长时间无结果。
- 用户需要确认申请状态。
- 页面提示失败但原因不清楚。

## Q: 实体卡怎么激活？

### 推荐回答

如果你收到实体卡，请在 App 的卡管理页面查看是否有激活入口，并按照页面提示输入卡片信息、完成必要验证和 PIN 设置。

如果激活失败，请检查输入的卡片信息是否正确，并稍后重试；如果仍失败，建议联系人工客服。

### 分类

- module: card
- intent: physical_card_activation
- visibility: user-facing
- verification_status: draft_pending_review

### 转人工

需要转人工：

- 激活失败。
- 用户无法找到激活入口。
- 用户输入信息正确但无法继续。

## Q: 如何设置或修改卡 PIN？

### 推荐回答

你可以在 App 的卡管理页面查看是否有设置、修改或重置 PIN 的入口。PIN 用于部分线下交易，请按照页面提示设置并妥善保管。

如果两次输入不一致，或页面提示设置失败，请重新输入；多次失败时建议联系人工客服。

### 分类

- module: card
- intent: card_pin
- visibility: user-facing
- verification_status: draft_pending_review

### 转人工

需要转人工：

- PIN 设置、修改或重置失败。
- 用户忘记 PIN 且无法在 App 中重置。
- 页面提示系统错误。

## Q: 如何锁定或解锁卡？

### 推荐回答

如果 App 提供锁卡功能，你可以在卡管理页面操作。锁定后，卡可能无法继续用于支付；如果需要恢复使用，可以按照页面提示进行解锁。

如果你怀疑卡丢失、被盗用或存在异常交易，请立即联系人工客服。

### 分类

- module: card
- intent: lock_unlock_card
- visibility: user-facing
- verification_status: draft_pending_review

### 转人工

需要转人工：

- 用户无法解锁卡。
- 卡疑似丢失、被盗刷或被他人使用。
- 页面提示锁卡/解锁失败。

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

## Q: 卡退款什么时候到账？

### 推荐回答

退款入账位置、金额和处理时间可能受到卡交易和渠道规则影响。请先查看 App 页面状态；如果长时间未到账，建议联系人工客服，并提供交易时间、金额、商户名称和截图。

### 分类

- module: card
- intent: card_refund
- visibility: user-facing
- verification_status: draft_pending_review

### 转人工

需要转人工：

- 退款长时间未到账。
- 退款金额与预期不一致。
- 用户询问手续费是否退还。
