---
module: _meta
feature: glossary
version: "1.1"
status: source_gap
source_doc: archive/converted-prd/**/README.md；knowledge-base/* 已校准模块
source_section: Converted PRD corpus / statuses, fields, limits, regions, compliance boundaries
last_updated: 2026-05-09
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

## Source alignment additions

| 术语 | 定义 | 来源 |
|---|---|---|
| converted-prd | 由历史 Word PRD 转换得到的 Markdown 证据层 | archive/converted-prd |
| ALIGNED | 知识库文件已完成 KB→Evidence 与 Evidence→KB 双向覆盖校验 | prd-source-alignment |
| SOURCE_GAP | converted-prd 中有关键规则，但知识库尚未完整结构化覆盖 | prd-source-alignment |
| NEED_CONFIRMATION | 源 PRD 删除线、待定或证据不足，需产品确认 | prd-source-alignment |
| CONFLICT | 多份 converted-prd 对同一事实存在冲突，不能自行裁决 | prd-source-alignment |
| DTC | 卡 / 钱包 / KYC 等外部渠道或服务依赖方，具体接口以模块 PRD 为准 | 多模块 |
| OBoss | 运营配置 / 通知 / Popup / Banner 等能力相关平台 | notification；oboss |
