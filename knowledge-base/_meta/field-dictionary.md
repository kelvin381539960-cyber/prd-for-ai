---
module: _meta
feature: field-dictionary
version: "2.0"
status: active
source_doc: archive/legacy-prd/**/README.md；knowledge-base/* 已校准模块
source_section: converted PRD corpus / field dictionary
last_updated: 2026-05-09
owner: 吴忆锋
readers: [product, ui, dev, qa, business, ai]
---

# Field Dictionary 字段字典

## 1. 文档定位

本文记录跨模块常用字段的含义和来源，避免不同模块重复定义或误用。

## 2. 用户 / 设备字段

| 字段 | 含义 | 来源 |
|---|---|---|
| UID | 注册成功后服务端生成的用户 ID | account/registration.md |
| DeviceID / deviceId | 唯一识别用户客户端设备，用于设备绑定、可信设备判断和风控 | security/global-rules.md；account/registration.md |
| Email | 注册 / 登录 / Email OTP 等场景使用；登录输入范围存在待确认 | account/registration.md；security/email-otp-verification.md |
| Phone | OTP / Send recipient 等场景使用 | security/otp-verification.md；wallet/send.md |
| AIX Tag / X-Tag | Send recipient 可使用的收款人标识之一 | wallet/send.md |

## 3. Card 字段

| 字段 | 含义 | 来源 |
|---|---|---|
| cardId | 卡记录定位字段；卡状态变更 webhook 根据 cardId 定位卡记录 | common/notification.md；card/manage/_index.md |
| newCardStatus | 卡状态变更 webhook 的最新卡状态来源 | common/notification.md |
| cardHolderName | Get Card Basic Info 返回，Card detail 使用 | card/manage/sensitive-info.md |
| cardNumber / PAN | Get Card Sensitive Info 返回完整卡号 | card/manage/sensitive-info.md |
| expiryDate | Get Card Sensitive Info 返回有效期 | card/manage/sensitive-info.md |
| cvc | Get Card Sensitive Info 返回 CVC / CVV | card/manage/sensitive-info.md |
| requestAmount / requestCurrency | Card Transaction Detail 中的法币交易金额和币种 | transaction/detail.md；card/transaction-detail.md |

## 4. Wallet / Transaction 字段

| 字段 | 含义 | 来源 |
|---|---|---|
| currency | 币种，如 USDC、USDT、WUSD、FDUSD | wallet/assets.md |
| balance | 钱包余额 | wallet/assets.md |
| dtcQuoteId | OTC Swap 一次性报价标识，用后失效 | wallet/swap.md |
| txnId | Crypto transaction detail 查询单笔交易详情使用 | transaction/detail.md |
| otc_id | Swap detail 查询 OTC 交易详情使用 | transaction/detail.md |
| transactionId | Card Transaction Detail 查询交易详情使用 | card/transaction-detail.md |

## 5. Notification 字段

| 字段 | 含义 | 来源 |
|---|---|---|
| title | Push 基础字段，保留用于老消息兼容和 push 展示 | common/notification.md |
| body | Push 基础字段，保留用于老消息兼容和 push 展示 | common/notification.md |
| Key title | 消息标题优先展示字段 | common/notification.md |
| category | Notification 分类，如 promotion / system / transaction | common/notification.md |
| device-token | Push 依赖 App 上报 device-token 确认推送设备 | common/notification.md |

## 6. Sources

- (Ref: knowledge-base/* 已校准模块)
