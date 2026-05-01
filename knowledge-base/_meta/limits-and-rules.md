---
module: _meta
feature: limits-and-rules
version: "1.0"
status: draft
source_doc: IMPLEMENTATION_PLAN.md
source_section: "4. 推荐目录结构"
last_updated: 2026-05-01
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

## 4. 维护规则

- 限制规则必须写清维度：用户、账户、设备、手机号、邮箱、卡、钱包、IP。
- 次数与时间窗口必须精确记录。
- 可配置项必须标记配置来源。
- 规则缺失时必须写入待确认事项。
