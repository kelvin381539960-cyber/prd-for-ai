---
module: _meta
feature: glossary
version: "1.0"
status: draft
source_doc: IMPLEMENTATION_PLAN.md
source_section: "Phase 1"
last_updated: 2026-05-01
owner: 吴忆锋
readers: [product, ui, dev, qa, business, ai]
---

# Glossary 术语表

## 1. 文档定位

本文档用于沉淀 AIX PRD 知识库中的统一术语。

同一概念在全知识库中只能使用一个标准名称。禁止同义词混用。

## 2. 术语表

| 术语 | 标准名称 | 定义 | 适用模块 | 来源 | 状态 |
|------|----------|------|----------|------|------|
| AIX | AIX | AIX 项目产品名称 | 全局 | 待补充 | draft |
| DTC | DTC | 外部合作方，提供钱包、卡片、交易、KYC 等能力 | integrations / wallet / card / transaction | 待补充 | draft |
| AAI | AAI | 第三方身份验证服务提供方 | integrations / security / wallet | 待补充 | draft |
| WalletConnect | WalletConnect | 外部钱包连接与充值能力 | integrations / wallet | 待补充 | draft |
| IVS | IVS | Identity Verification Service，身份认证服务 | security | 待补充 | draft |
| KYC | KYC | Know Your Customer，开户与身份核验流程 | wallet / security | 待补充 | draft |

## 3. 待补充

- 从历史 PRD 中补齐全部业务术语。
- 从 DTC 接口文档中补齐字段与状态术语。
- 统一 Card / Wallet / Transaction 中重复概念命名。
