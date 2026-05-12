---
module: card
audience: customer
visibility: user-facing
language: zh-CN
verification_status: partial_confirmed
last_updated: 2026-05-12
---

# 卡 FAQ

## Q: 当前可以申请卡吗？

### 推荐回答

当前开放卡申请。申请卡前，你需要先完成 KYC 和钱包开户。

### 分类

- module: card
- intent: card_application_available
- visibility: user-facing
- verification_status: confirmed

### 转人工

用户看不到申请入口或申请失败时，建议转人工。

## Q: 当前支持虚拟卡和实体卡吗？

### 推荐回答

当前支持虚拟卡和实体卡。虚拟卡会自动激活，实体卡需要用户手动激活。

### 分类

- module: card
- intent: card_type
- visibility: user-facing
- verification_status: confirmed

### 转人工

实体卡激活失败时，建议转人工。

## Q: 卡支持哪些国家或地区？

### 推荐回答

当前卡支持全球大多数国家/地区。具体是否支持你的所在地，请以 App 页面提示为准。

### 分类

- module: card
- intent: card_supported_regions
- visibility: user-facing
- verification_status: confirmed

### 转人工

用户所在地页面提示不可申请时，建议转人工确认。

## Q: 如何申请卡？

### 推荐回答

你可以在 App 的卡申请入口按照页面提示选择卡类型、卡片信息和支付币种，并提交申请。申请前需要先完成 KYC 和钱包开户。

具体费用、限额、卡数量和审核要求，请以 App 页面提示为准。

### 分类

- module: card
- intent: card_application
- visibility: user-facing
- verification_status: confirmed

### 转人工

需要转人工：

- 用户看不到申请入口。
- 卡申请失败或长时间无结果。

## Q: 卡申请失败原因可以告诉我吗？

### 推荐回答

卡申请失败原因可以根据页面提示向你说明，但具体风控拒绝原因不能说明。

如果页面没有明确说明，或你无法重新提交申请，建议联系人工客服。

### 分类

- module: card
- intent: card_application_failed_reason
- visibility: user-facing
- verification_status: confirmed

### 转人工

需要转人工：

- 用户询问具体风控拒绝原因。
- 页面没有明确失败原因。

## Q: 单个用户最多可以申请几张卡？

### 推荐回答

单个用户最多可以申请 5 张卡。

### 分类

- module: card
- intent: card_limit_count
- visibility: user-facing
- verification_status: confirmed

### 转人工

通常不需要转人工。

## Q: 实体卡怎么激活？

### 推荐回答

实体卡需要手动激活。激活时需要输入实体卡后四位，并设置 6 位 PIN。

如果激活失败，请检查输入的卡片信息是否正确，并稍后重试；如果仍失败，建议联系人工客服。

### 分类

- module: card
- intent: physical_card_activation
- visibility: user-facing
- verification_status: confirmed

### 转人工

需要转人工：

- 激活失败。
- 用户无法找到激活入口。
- 用户输入信息正确但无法继续。

## Q: 卡 PIN 是几位？

### 推荐回答

卡 PIN 为 6 位数。请按照页面提示设置并妥善保管。

### 分类

- module: card
- intent: card_pin_length
- visibility: user-facing
- verification_status: confirmed

### 转人工

PIN 设置、修改或重置失败时，建议转人工。

## Q: 卡是否支持冻结、关闭、补发或重开？

### 推荐回答

支持卡冻结、关闭、补发和重开。注销卡和补发卡需要联系人工客服。

如果你怀疑卡丢失、被盗刷或被他人使用，请立即联系人工客服。

### 分类

- module: card
- intent: card_manage_actions
- visibility: user-facing
- verification_status: confirmed

### 转人工

注销卡、补发卡、丢失或疑似盗刷时，需要转人工。

## Q: 卡申请失败后已扣费怎么办？

### 推荐回答

如果卡申请失败后已经扣费，费用会原路返回。

### 分类

- module: card
- intent: card_application_fee_refund
- visibility: user-facing
- verification_status: confirmed

### 转人工

费用长时间未退回时，建议转人工。

## Q: 卡交易失败、重复扣款或退款异常怎么办？

### 推荐回答

卡交易失败、重复扣款、退款异常需要按具体场景处理。请联系人工客服，并准备好交易时间、金额、商户名称、交易状态和页面截图。

退款是否退回卡余额、FX 费用和 transaction fee 是否退还，目前仍需进一步确认，请以人工客服核查结果为准。

### 分类

- module: card
- intent: card_transaction_issue
- visibility: user-facing
- verification_status: partial_confirmed

### 转人工

需要转人工。
