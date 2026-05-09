---
module: _meta
feature: countries-and-regions
version: "1.1"
status: source_gap
source_doc: archive/converted-prd/**/README.md；knowledge-base/* 已校准模块
source_section: Converted PRD corpus / statuses, fields, limits, regions, compliance boundaries
last_updated: 2026-05-09
owner: 吴忆锋
readers: [product, ui, dev, qa, business, ai]
---

# Countries and Regions 国家与地区

## 1. 文档定位

本文档用于沉淀 AIX 全局国家线、地区、电话区号、支持范围与限制范围。

国家线会影响注册、KYC、钱包、卡申请、邮寄地址、Waitlist、官网外部投放等模块。

## 2. 当前支持国家线

| 国家 / 地区 | Code | 状态 | 适用模块 | 来源 | 备注 |
|-------------|------|------|----------|------|------|
| Vietnam | VN | 待确认 | 全局 | 待补充 | 历史 PRD 多处出现 |
| Philippines | PH | 待确认 | 全局 | 待补充 | 历史 PRD 多处出现 |
| Australia | AU | 待确认 | 全局 | 待补充 | 历史 PRD 多处出现 |

## 3. 维护规则

- 国家线必须标注来源。
- 不同模块国家线不一致时，必须记录冲突。
- 涉及制裁、高风险地区、卡申请地区、KYC 居住地时，必须标记合规边界。

## 4. 待补充

- 从 `Countries and Regions list - 国家地区电话区号.csv` 补齐区号与地区列表。
- 从 Card / Wallet / KYC / Website PRD 中补齐模块级国家线。
- 从 DTC 接口文档中确认卡片与钱包支持国家差异。

## Source alignment additions

| 类型 | 国家 / 地区 | 来源 |
|---|---|---|
| Card Application Phase 1 | Philippines、Vietnam、Australia | card/application |
| KYC 国家线 | 以 wallet-opening PRD 的国家线 / 居住国白名单规则为准 | kyc/wallet-opening |
| POA 国家校验 | POA 国家需与用户填报居住国匹配，且申请国家需在白名单 | kyc/wallet-opening |
| Phone country code | 登录 / 注册国家区号规则存在删除线和待确认，不能作为已确认全量国家线 | registration-login |
