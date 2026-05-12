---
module: transaction-history
audience: customer
visibility: user-facing
language: zh-CN
verification_status: partial_confirmed
last_updated: 2026-05-12
---

# 交易记录 FAQ

## Q: 交易记录包含哪些类型？

### 推荐回答

交易记录会聚合钱包交易、兑换记录和卡交易。

### 分类

- module: transaction-history
- intent: transaction_types
- visibility: user-facing
- verification_status: confirmed

### 转人工

用户认为交易记录缺失时，建议转人工。

## Q: 当前有哪些交易状态？

### 推荐回答

当前有效状态包括：pending、success、failed、refunded、cancelled、declined、under review。

这些状态的正式中文口径仍在确认中，请以 App 当前页面展示为准。

### 分类

- module: transaction-history
- intent: transaction_statuses
- visibility: user-facing
- verification_status: partial_confirmed

### 转人工

用户不理解某个状态或状态长时间不变化时，建议转人工。

## Q: 交易记录支持搜索或导出吗？

### 推荐回答

第一期交易记录只支持筛选，不支持搜索和导出。

### 分类

- module: transaction-history
- intent: transaction_filter_search_export
- visibility: user-facing
- verification_status: confirmed

### 转人工

通常不需要转人工。

## Q: 交易一直显示处理中怎么办？

### 推荐回答

部分交易需要等待网络、商户、卡组织、钱包或系统处理后才会更新状态。你可以先刷新页面并稍后查看。

如果交易长时间保持处理中，或金额、资产、卡余额显示异常，建议联系人工客服。

### 分类

- module: transaction-history
- intent: transaction_pending
- visibility: user-facing
- verification_status: partial_confirmed

### 转人工

需要转人工：

- 交易长时间处理中。
- 交易金额或状态异常。
- 用户要求撤销、追回或赔偿。

## Q: 卡退款怎么显示？

### 推荐回答

卡退款里的 REFUND / REVERSAL 都对用户显示为“退款”。退款金额、入账位置、手续费是否退还和处理时间仍需进一步确认，请以 App 页面展示和人工客服核查结果为准。

### 分类

- module: transaction-history
- intent: card_refund_display
- visibility: user-facing
- verification_status: partial_confirmed

### 转人工

需要转人工：

- 退款长时间未到账。
- 退款金额与预期不一致。
- 用户询问手续费是否退还。

## Q: 找不到交易记录怎么办？

### 推荐回答

请先确认是否使用了正确的筛选条件。第一期交易记录支持筛选，但不支持搜索和导出。

如果仍然找不到，建议联系人工客服协助核查。

### 分类

- module: transaction-history
- intent: transaction_missing
- visibility: user-facing
- verification_status: partial_confirmed

### 转人工

需要转人工：

- 用户仍找不到交易记录。
- 交易涉及资金异常。
