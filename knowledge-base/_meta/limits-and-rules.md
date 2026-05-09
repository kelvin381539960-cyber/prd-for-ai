---
module: _meta
feature: limits-and-rules
version: "1.1"
status: source_gap
source_doc: archive/converted-prd/**/README.md；knowledge-base/* 已校准模块
source_section: Converted PRD corpus / statuses, fields, limits, regions, compliance boundaries
last_updated: 2026-05-09
owner: 吴忆锋
readers: [product, dev, qa, business, ai]
---

# Limits and Rules 限制与规则

## 1. 文档定位

本文档用于沉淀 AIX 全局限制、次数、冷却、锁定、限额、可配置规则。

## 2. 规则分类

| 分类 | 适用模块 | 示例 | 来源 | 状态 |
|------|----------|------|------|------|
| Authentication Limits | security | OTP 失败次数、锁定时间 | 待补充 | draft |
| KYC Limits | wallet / security | Face 失败次数、锁定时间 | 待补充 | draft |
| Card Limits | card | 申卡张数、在途卡限制 | 待补充 | draft |
| Wallet Limits | wallet | 转账、兑换、充值限制 | 待补充 | draft |
| Transaction Limits | transaction | 金额、状态、频率限制 | 待补充 | draft |
| Configurable Rules | 全局 | 可配置币种、国家、费用 | 待补充 | draft |

## 3. 规则记录模板

| 规则名 | 规则内容 | 适用模块 | 触发条件 | 系统动作 | 用户提示 | 是否可配置 | 来源 | 备注 |
|--------|----------|----------|----------|----------|----------|------------|------|------|
| TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |

## Source alignment additions

| 限制 / 规则 | 结论 | 来源 |
|---|---|---|
| Card 数量 | 待激活、已激活、审核中、已冻结之和限制 5 张，可配置 | home；card/application |
| 一人在途 | 一个用户可申请多张卡，但仅可一张在途；DTC 可配置是否限制 | card/application |
| Password | 8-32 字符，需大小写、数字、符号 / supported symbol | registration-login；security |
| PIN | 6 位；任一数字出现超过 3 次会被 DTC 拒绝 | card/manage |
| OTP / Email OTP | 4 位数字，5 分钟有效；24 小时 resend 最多 3 次，触发 20 分钟冷却 | security |
| Face Auth | 5 次失败锁 20 分钟，10 次失败锁 24 小时；接口连续 20 次锁 20 分钟 | security；kyc |
| IVS Token | DTC 实际 10 分钟，AIX 按 5 分钟校验 | security |
| WalletConnect deeplink | 5 分钟有效；授权有效期 1 天 | wallet/deposit-send-swap |
| Card detail exchange rate | 小数点后 6 位，向上取整 | transaction-history |
| Swap detail exchange rate | 后端给什么显示什么，不做位数处理 | transaction-history |

## 4. 维护规则

- 限制规则必须写清维度：用户、账户、设备、手机号、邮箱、卡、钱包、IP。
- 次数与时间窗口必须精确记录。
- 可配置项必须标记配置来源。
- 规则缺失时必须写入待确认事项。
