---
module: wallet
audience: customer
visibility: user-facing
language: zh-CN
verification_status: draft_pending_review
last_updated: 2026-05-10
---

# 钱包 FAQ

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
