---
module: _meta
feature: countries-and-regions
version: "2.0"
status: active
source_doc: archive/converted-prd/**/README.md；knowledge-base/* 已校准模块
source_section: converted PRD corpus / countries and regions
last_updated: 2026-05-09
owner: 吴忆锋
readers: [product, ui, dev, qa, business, ai]
---

# Countries and Regions 国家与地区

## 1. 文档定位

本文记录已在 converted-prd 和已校准 KB 中确认的国家、地区、国家线和区域限制。

## 2. 已确认国家 / 地区规则

| 场景 | 国家 / 地区 | 规则 | 来源 |
|---|---|---|---|
| Card Application Phase 1 | Philippines、Vietnam、Australia | Phase 1 支持地区，后续可配置 | card/application.md |
| KYC 国家线 | 以 Wallet Opening KYC PRD 的国家线 / 居住国白名单为准 | 具体白名单不在本文展开 | kyc/account-opening.md |
| POA 国家校验 | POA 国家需与用户填报居住国匹配，申请国家需在白名单 | 不匹配则进入 KYC 失败 / 拒绝规则 | kyc/account-opening.md |
| Phone country code | 登录 / 注册国家区号部分存在删除线与待确认 | 不作为完整国家线沉淀 | account/login.md |
| Physical card delivery | 实体卡地址与交付规则以 Card Application / Card Manage 为准 | FAQ 中 delivery time 仅作帮助说明 | card/application.md；common/faq.md |

## 3. 不得推导

1. 不得从 FAQ 的普通用户解释反推出国家线。
2. 不得把 Phone Country Code 当成 KYC 居住国白名单。
3. 不得把 Phase 1 Card 支持国家扩展到 Wallet / KYC 全量支持国家。

## 4. Sources

- (Ref: archive/converted-prd/card/application/README.md)
- (Ref: archive/converted-prd/kyc/wallet-opening/README.md)
- (Ref: archive/converted-prd/app/registration-login/README.md)
