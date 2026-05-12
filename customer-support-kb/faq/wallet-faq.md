---
module: wallet
audience: customer
visibility: user-facing
language: zh-CN
verification_status: partial_confirmed
last_updated: 2026-05-12
---

# 钱包 FAQ

## Q: 当前支持哪些币种？

### 推荐回答

当前支持 FDUSD、USDC、USDT、WUSD。

### 分类

- module: wallet
- intent: supported_assets
- visibility: user-facing
- verification_status: confirmed

### 转人工

通常不需要转人工，除非用户的问题涉及异常资产显示或余额异常。

## Q: 当前支持哪些网络？

### 推荐回答

当前支持 BASE、BSC、ETHEREUM、SOLANA。

### 分类

- module: wallet
- intent: supported_networks
- visibility: user-facing
- verification_status: confirmed

### 转人工

用户不确定充值网络时，建议转人工确认后再操作。

## Q: 充值多久到账？

### 推荐回答

充值到账时间不完全固定，仅可作为参考：ETH 网络可能约 10-15 分钟，其他网络可能约 1-5 分钟。

实际到账时间会受到链上状态、网络拥堵和系统处理影响，请以链上状态和 App 页面展示为准。

### 分类

- module: wallet
- intent: deposit_arrival_time
- visibility: user-facing
- verification_status: confirmed

### 转人工

需要转人工：

- 链上成功但 App 未到账。
- 到账时间明显异常。

## Q: 充值前需要注意什么？

### 推荐回答

充值前请确认币种、网络、地址和最低充值要求是否正确。如果使用第三方钱包，也要确认第三方钱包内的网络和资产与 App 页面选择一致。

如果你不确定，请先不要转账，建议联系人工客服确认。

### 分类

- module: wallet
- intent: deposit_before_transfer_check
- visibility: user-facing
- verification_status: confirmed

### 转人工

需要转人工：

- 用户不确定应选择哪个网络。
- 用户不确定资产是否受支持。
- 用户已发起转账但信息可能填写错误。

## Q: Send 功能当前可以用吗？

### 推荐回答

Send 功能当前不可用。通过手机号、邮箱或 X-Tag 查找收款人的能力当前也不可用。

### 分类

- module: wallet
- intent: send_availability
- visibility: user-facing
- verification_status: confirmed

### 转人工

通常不需要转人工。

## Q: Swap 功能当前可以用吗？

### 推荐回答

Swap 功能当前不可用，因此暂不支持币种互换。

### 分类

- module: wallet
- intent: swap_availability
- visibility: user-facing
- verification_status: confirmed

### 转人工

通常不需要转人工。

## Q: 充值不到账怎么办？

### 推荐回答

请先确认充值的币种、网络和地址是否正确，并查看链上交易是否已完成。如果链上已确认但 App 内长时间未到账，建议联系人工客服，并准备好交易哈希、币种、网络、金额和时间。

### 分类

- module: wallet
- intent: deposit_not_received
- visibility: user-facing
- verification_status: partial_confirmed

### 转人工

需要转人工：

- 链上成功但 App 未到账。
- 用户疑似选错网络、地址或币种。
- 资产余额异常。

## Q: 选错网络、地址或币种怎么办？

### 推荐回答

如果你已经发起转账，请尽快联系人工客服，并准备好交易哈希、币种、网络、地址、金额和时间。

请注意，充错链、地址或币种时，无法保证找回。具体情况需要人工进一步核查。

### 分类

- module: wallet
- intent: wrong_network_address_asset
- visibility: user-facing
- verification_status: confirmed

### 转人工

需要转人工。
