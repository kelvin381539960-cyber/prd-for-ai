---
module: _meta
feature: error-code-dictionary
version: "1.0"
status: draft
source_doc: IMPLEMENTATION_PLAN.md
source_section: "4. 推荐目录结构"
last_updated: 2026-05-01
owner: 吴忆锋
readers: [product, ui, dev, qa, business, ai]
---

# Error Code Dictionary 错误码与提示字典

## 1. 文档定位

本文档用于沉淀 AIX 错误码、失败原因、前端提示、系统动作与兜底处理。

## 2. 错误分类

| 分类 | 适用模块 | 示例 | 来源 | 状态 |
|------|----------|------|------|------|
| Network Error | common | 网络异常页 / 弹窗 | 待补充 | draft |
| Server Error | common | 服务器异常页 / 弹窗 | 待补充 | draft |
| OTP Error | security | Invalid OTP / Too Many Attempts | 待补充 | draft |
| KYC Error | wallet / security | Document / Face / POA 失败 | 待补充 | draft |
| Card Error | card | 申卡 / 激活 / PIN 失败 | 待补充 | draft |
| Transaction Error | transaction / wallet | 余额不足 / 风控拦截 / 交易失败 | 待补充 | draft |

## 3. 错误记录模板

| 错误码 | 标准错误名 | 触发条件 | 用户提示 | 系统动作 | 是否可重试 | 来源 | 备注 |
|--------|------------|----------|----------|----------|------------|------|------|
| TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |

## 4. 维护规则

- 错误提示必须保留英文原文。
- 错误原因、用户提示、系统动作必须分开写。
- 涉及资金失败时，必须说明资金是否入账、是否冻结、是否需要人工处理。
- 不确定错误码不得写成确定规则。
