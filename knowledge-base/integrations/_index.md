---
module: integrations
description: 外部系统事实源，沉淀 DTC、AAI、WalletConnect 等外部能力、接口、字段、状态与限制
version: "1.0"
status: draft
source_docs: [DTC接口文档, 历史prd]
last_updated: 2026-05-01
owner: 吴忆锋
depends_on: [_meta]
readers: [product, dev, qa, ai]
---

# Integrations 外部系统事实源

## 1. 模块定位

本模块用于沉淀外部系统事实，避免 DTC、AAI、WalletConnect 等能力散落在各业务模块中重复解释。

业务模块应引用 integrations 中的接口、字段、状态、回调、限制和资金路径事实。

## 2. 子模块清单

| 子模块 | 文件目录 | 内容 | 状态 |
|--------|----------|------|------|
| DTC | `dtc/` | Wallet API、Card API、交易通知、状态与字段 | draft |
| AAI | `aai/` | KYC、证件、活体、人脸比对能力 | draft |
| WalletConnect | `walletconnect/` | 外部钱包连接、充值、DeepLink / QR 能力 | draft |

## 3. 维护规则

- 外部系统原始事实优先来自 `DTC接口文档/`。
- 与业务 PRD 冲突时，记录冲突，不自行拍板。
- 涉及资金路径时，必须写清资金状态、系统动作与人工介入条件。

## 4. 待确认事项

| 问题 | 影响范围 | 建议确认人 | 状态 |
|------|----------|------------|------|
| 待拆分 DTC Wallet / Card / Notification 具体接口事实 | wallet / card / transaction | 产品 / 技术 / DTC | open |
