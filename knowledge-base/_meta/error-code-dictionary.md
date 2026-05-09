---
module: _meta
feature: error-code-dictionary
version: "1.1"
status: source_gap
source_doc: archive/converted-prd/**/README.md；knowledge-base/* 已校准模块
source_section: Converted PRD corpus / statuses, fields, limits, regions, compliance boundaries
last_updated: 2026-05-09
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

## Source alignment additions

本文件当前为 `SOURCE_GAP`：converted-prd 中的错误码与文案仍分散在 KYC、Security、Card Manage、Transaction、Wallet 等模块。已在 `common/errors.md` 补入高频错误文案，后续需按 code / module / trigger / user copy / backend action 抽取全量字典。

| 已知错误码 / 类型 | 说明 | 来源 |
|---|---|---|
| 31031 | PIN 设置失败时使用后端返回文案覆盖默认失败文案 | card/manage |
| FACE_QUALITY_TOO_POOR / USER_TIMEOUT / SIMILARITY_FAILED 等 | Face / KYC 错误码映射来源 | kyc/wallet-opening；security |
| DTC 未知错误码 | 需 Lark 报警通知产品和渠道确定后续处理 | transaction-history |

## 4. 维护规则

- 错误提示必须保留英文原文。
- 错误原因、用户提示、系统动作必须分开写。
- 涉及资金失败时，必须说明资金是否入账、是否冻结、是否需要人工处理。
- 不确定错误码不得写成确定规则。
