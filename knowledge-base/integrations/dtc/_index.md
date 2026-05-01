---
module: integrations
feature: dtc
version: "1.0"
status: draft
source_doc: DTC接口文档
source_section: TBD
last_updated: 2026-05-01
owner: 吴忆锋
depends_on: [_meta]
readers: [product, dev, qa, ai]
---

# DTC Integration

## 1. 模块定位

本文档用于沉淀 DTC 作为外部渠道提供的钱包、卡、交易、KYC、通知、状态、字段、资金路径等事实。

## 2. 文件清单

| 文件 | 内容 | 状态 |
|------|------|------|
| wallet-api.md | DTC Wallet OpenAPI 事实 | 待创建 |
| card-api.md | DTC Card Issuing API 事实 | 待创建 |
| transaction-notification.md | 交易通知与回调事实 | 待创建 |
| status-and-fields.md | DTC 状态与字段总览 | 待创建 |

## 3. 维护规则

- DTC 原始接口字段不得私自改名。
- 产品展示名称可另行映射，但必须保留 DTC 原始字段。
- 资金路径必须可追溯到接口或通知。
- 与 PRD 冲突时，必须记录冲突。
