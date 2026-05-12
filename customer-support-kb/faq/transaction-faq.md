---
module: transaction-history
audience: customer
visibility: user-facing
language: zh-CN
verification_status: draft_pending_review
last_updated: 2026-05-10
---

# 交易记录 FAQ

## Q: 如何查看交易记录？

### 推荐回答

你可以在 App 的交易记录入口查看相关交易信息。交易记录可能包含钱包充值、接收、发送、兑换、卡消费、卡退款、申卡扣费或退款等类型。具体可见类型请以 App 当前页面为准。

### 分类

- module: transaction-history
- intent: view_transactions
- visibility: user-facing
- verification_status: draft_pending_review

### 转人工

需要转人工：

- 用户找不到交易记录入口。
- 用户认为交易记录缺失。

## Q: 交易一直显示处理中怎么办？

### 推荐回答

部分交易需要等待网络、商户、卡组织、钱包或系统处理后才会更新状态。你可以先刷新页面并稍后查看。

如果交易长时间保持处理中，或金额、资产、卡余额显示异常，建议联系人工客服。

### 分类

- module: transaction-history
- intent: transaction_pending
- visibility: user-facing
- verification_status: draft_pending_review

### 转人工

需要转人工：

- 交易长时间处理中。
- 交易金额或状态异常。
- 用户要求撤销、追回或赔偿。

## Q: 找不到交易记录怎么办？

### 推荐回答

请先确认是否选择了正确的账户、卡、资产、时间范围或交易类型。你也可以刷新页面后重试。

如果仍然找不到，建议联系人工客服协助核查。

### 分类

- module: transaction-history
- intent: transaction_missing
- visibility: user-facing
- verification_status: draft_pending_review

### 转人工

需要转人工：

- 用户仍找不到交易记录。
- 交易涉及资金异常。
- 用户无法提供基本交易信息但需要核查。

## Q: 交易失败怎么办？

### 推荐回答

请先查看交易详情页或页面提示。失败可能与余额、账户状态、商户、网络、链上状态或系统处理有关。

如果失败后资产、卡余额或交易状态异常，建议联系人工客服进一步核查。

### 分类

- module: transaction-history
- intent: transaction_failed
- visibility: user-facing
- verification_status: draft_pending_review

### 转人工

需要转人工：

- 交易失败后资产或卡余额异常。
- 页面没有明确失败原因。
- 用户要求撤销、追回或赔偿。

## Q: 卡退款什么时候到账？

### 推荐回答

如果商户发起退款，相关记录可能会在卡交易或交易详情中展示。退款金额、入账位置、手续费是否退还和处理时间可能受商户及通道规则影响，请以 App 页面展示和人工客服核查结果为准。

### 分类

- module: transaction-history
- intent: card_refund_status
- visibility: user-facing
- verification_status: draft_pending_review

### 转人工

需要转人工：

- 退款长时间未到账。
- 退款金额与预期不一致。
- 用户询问手续费是否退还。

## Q: 页面提示数据异常或网络异常怎么办？

### 推荐回答

请先检查网络连接并刷新页面。如果页面持续提示数据异常、网络异常或加载失败，建议稍后重试；如果问题持续存在，请联系人工客服。

### 分类

- module: transaction-history
- intent: transaction_page_error
- visibility: user-facing
- verification_status: draft_pending_review

### 转人工

需要转人工：

- 页面持续无法加载。
- 用户急需核查交易状态。
- 涉及资金异常。
