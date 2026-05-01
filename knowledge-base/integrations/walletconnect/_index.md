---
module: integrations
feature: walletconnect
version: "1.0"
status: draft
source_doc: DTC接口文档 / 历史prd
source_section: TBD
last_updated: 2026-05-01
owner: 吴忆锋
depends_on: [_meta, wallet]
readers: [product, dev, qa, ai]
---

# WalletConnect Integration

## 1. 模块定位

本文档用于沉淀 WalletConnect 在自托管钱包充值、DeepLink、QR、钱包选择、交易报备、地址加白等场景中的外部能力事实。

## 2. 文件清单

| 文件 | 内容 | 状态 |
|------|------|------|
| deposit-flow.md | WalletConnect 充值流程事实 | 待创建 |

## 3. 维护规则

- 必须区分 WalletConnect 协议限制、DTC 实现限制、AIX 产品限制。
- iOS / Android 唤起差异必须标记来源。
- 充值资金路径、风控拦截、交易报备、地址加白必须可追溯。
