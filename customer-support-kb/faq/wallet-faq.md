---
module: wallet
audience: customer
visibility: user-facing
language: zh-CN
verification_status: draft_pending_review
last_updated: 2026-05-10
---

# 钱包 FAQ

## Q: 充值前需要注意什么？

### 推荐回答

充值前请确认币种、网络、地址和最低充值要求是否正确。如果使用第三方钱包，也要确认第三方钱包内的网络和资产与 App 页面选择一致。

如果你不确定，请先不要转账，建议联系人工客服确认。

### 分类

- module: wallet
- intent: deposit_before_transfer_check
- visibility: user-facing
- verification_status: draft_pending_review

### 转人工

需要转人工：

- 用户不确定应选择哪个网络。
- 用户不确定资产是否受支持。
- 用户已发起转账但信息可能填写错误。

## Q: 充值不到账怎么办？

### 推荐回答

请先确认充值的币种、网络和地址是否正确，并查看链上交易是否已完成。如果链上已确认但 App 内长时间未到账，建议联系人工客服，并准备好交易哈希、币种、网络、金额和时间。

### 分类

- module: wallet
- intent: deposit_not_received
- visibility: user-facing
- verification_status: draft_pending_review

### 转人工

需要转人工：

- 链上成功但 App 未到账。
- 用户疑似选错网络、地址或币种。
- 资产余额异常。

## Q: 资产余额不对怎么办？

### 推荐回答

请先刷新页面并确认网络连接正常。如果你刚完成充值、发送、兑换或卡交易，资产余额可能需要等待相关交易状态更新后才会变化。若余额长时间异常，建议联系人工客服。

### 分类

- module: wallet
- intent: balance_issue
- visibility: user-facing
- verification_status: draft_pending_review

### 转人工

需要转人工：

- 余额长时间异常。
- 用户怀疑资产丢失。
- 交易后资产状态不一致。

## Q: 发送资产失败怎么办？

### 推荐回答

请先查看页面提示，并确认收款人、资产、金额和余额是否正确。如果页面提示余额不足、验证失败或系统暂时无法处理，请按页面提示操作。

如果发送失败后资产状态异常，或交易长时间处理中，建议联系人工客服。

### 分类

- module: wallet
- intent: send_failed
- visibility: user-facing
- verification_status: draft_pending_review

### 转人工

需要转人工：

- 发送失败后资产状态异常。
- 用户要求撤销或追回。
- 交易长时间处理中。

## Q: 兑换资产失败怎么办？

### 推荐回答

请先查看页面提示，并确认卖出资产、买入资产、金额和页面展示的汇率信息。如果兑换显示处理中，请等待页面状态更新。

如果长时间没有变化，或兑换失败后资产状态异常，建议联系人工客服。

### 分类

- module: wallet
- intent: swap_failed
- visibility: user-facing
- verification_status: draft_pending_review

### 转人工

需要转人工：

- 兑换长时间处理中。
- 兑换失败后资产状态异常。
- 用户询问未确认的汇率、费用或限额。

## Q: 选错网络、地址或币种怎么办？

### 推荐回答

如果你已经发起转账，请尽快联系人工客服，并准备好交易哈希、币种、网络、地址、金额和时间。请注意，区块链转账通常无法保证撤回或找回，具体处理结果需要人工进一步核查。

### 分类

- module: wallet
- intent: wrong_network_address_asset
- visibility: user-facing
- verification_status: draft_pending_review

### 转人工

需要转人工：

- 用户已使用错误网络、地址或币种转账。
- 用户要求找回、撤销或赔偿。
