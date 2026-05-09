---
module: _meta
feature: limits-and-rules
version: "2.0"
status: active
source_doc: archive/converted-prd/**/README.md；knowledge-base/* 已校准模块
source_section: converted PRD corpus / limits and rules
last_updated: 2026-05-09
owner: 吴忆锋
readers: [product, ui, dev, qa, business, ai]
---

# Limits and Rules 限制与规则

## 1. 文档定位

本文沉淀跨模块限制、阈值、有效期、数量限制和计算规则。

## 2. Account / Security

| 规则 | 结论 | 来源 |
|---|---|---|
| Password 长度 | 8-32 字符 | security/password-policy.md |
| Password 复杂度 | 需包含大小写、数字、符号 / supported symbol | security/password-policy.md |
| OTP / Email OTP | 4 位数字，5 分钟有效 | security/otp-verification.md；security/email-otp-verification.md |
| Resend | 24 小时内最多 3 次，触发 20 分钟冷却 | security/otp-verification.md；security/email-otp-verification.md |
| OTP 失败 5 次 | 锁定 20 分钟 | security/global-rules.md |
| OTP 失败 10 次 | 锁定 24 小时 | security/global-rules.md |
| Face Auth 失败 | 5 次锁 20 分钟；10 次锁 24 小时；接口连续 20 次锁 20 分钟 | security/face-authentication.md |
| IVS Token | DTC 实际 10 分钟，AIX 按 5 分钟校验 | security/global-rules.md |

## 3. KYC

| 规则 | 结论 | 来源 |
|---|---|---|
| Face Loading | 超过 30 秒无结果进入 Loading Failed | kyc/account-opening.md |
| 申请单 | 自创建后长期有效 | kyc/account-opening.md |
| Passport / Face 成功 | 通过后不会再变为失败状态 | kyc/account-opening.md |

## 4. Card

| 规则 | 结论 | 来源 |
|---|---|---|
| Card 数量 | 待激活、已激活、审核中、已冻结之和限制 5 张，可配置 | card/application.md；home/app-home.md |
| 一人在途 | 一个用户可申请多张卡，但仅可一张在途；DTC 可配置是否限制 | card/application.md |
| Virtual Card fee | USD 5 | card/application.md；common/faq.md |
| Physical Card fee | USD 10 | card/application.md；common/faq.md |
| PIN | 6 位 | card/manage/pin.md |
| PIN 简单规则 | 任一数字出现超过 3 次会被 DTC 拒绝 | card/manage/pin.md |
| Card detail exchange rate | 小数点后 6 位，向上取整 | transaction/detail.md |

## 5. Wallet / Transaction

| 规则 | 结论 | 来源 |
|---|---|---|
| 稳定币范围 | USDC、USDT、WUSD、FDUSD | wallet/assets.md |
| Total Asset | USDT余额*Rate1 + USDC余额*Rate2 + WUSD余额*Rate3 + FDUSD余额*Rate4 | wallet/assets.md |
| WalletConnect deeplink | 5 分钟有效 | wallet/deposit.md |
| WalletConnect 授权 | 1 天有效 | wallet/deposit.md |
| dtcQuoteId | Swap 一次性报价标识，用后失效 | wallet/swap.md |
| Swap detail exchange rate | 后端给什么显示什么，不做位数处理 | transaction/detail.md；wallet/swap.md |
| Transaction Search | 全量交易和卡交易去掉搜索，后续迭代 | transaction/history.md |

## 6. Notification

| 规则 | 结论 | 来源 |
|---|---|---|
| Me tab unread | 超过 100 条展示 99+ | common/notification.md |
| Push preference priority | user status > user notification preference > FC & DND | common/notification.md |
| Push length | 待定，不写具体数值 | common/notification.md |

## 7. Sources

- (Ref: knowledge-base/* 已校准模块)
