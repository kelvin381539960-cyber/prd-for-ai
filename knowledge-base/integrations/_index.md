---
module: integrations
description: 外部系统事实源，沉淀 DTC、AAI、WalletConnect 等外部能力、接口、字段、状态与限制
version: "1.1"
status: active
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
| DTC | `dtc/_index.md` | AIX 对 DTC 的外部依赖边界、字段、状态、回调、资金路径 | active |
| AAI | `aai/_index.md` | AIX 对 AAI 的外部身份认证 / KYC 依赖边界 | active |
| WalletConnect | `walletconnect/_index.md` | WalletConnect 充值、DeepLink / QR、授权、白名单与异常边界 | active |

## 3. 维护规则

- 外部系统原始事实优先来自 `external-docs/dtc/`。
- 与业务 PRD 冲突时，记录冲突，不自行拍板。
- 涉及资金路径时，必须写清资金状态、系统动作与人工介入条件。

## 4. 使用规则

1. 查询 DTC / AAI / WalletConnect 外部依赖时，先读本索引，再读对应子模块 `_index.md`。
2. 外部系统只记录 AIX 需要感知的能力、字段、事件、状态和限制。
3. 不维护供应商完整接口说明书、完整错误码表或内部实现逻辑。
4. 未确认项统一进入 `knowledge-base/changelog/knowledge-gaps.md`。
