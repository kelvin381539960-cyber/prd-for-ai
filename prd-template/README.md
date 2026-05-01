---
type: prd-template-index
version: "1.0"
status: draft
source_doc: IMPLEMENTATION_PLAN.md
source_section: "3.4 PRD Template"
last_updated: 2026-05-01
owner: 吴忆锋
readers: [product, ui, dev, qa, business, ai]
---

# PRD Template

## 1. 目录定位

本目录用于沉淀后续新 PRD 的写作模板。

新 PRD 编写时，不应直接复制历史 PRD，而应按需引用：

```text
_meta + integrations + security/common + 目标业务模块 + prd-template
```

## 2. 模板清单

| 模板 | 文件 | 状态 | 用途 |
|------|------|------|------|
| 标准 PRD 模板 | standard-prd-template.md | 待创建 | 新功能 / 新模块 PRD |
| 变更需求模板 | change-request-template.md | 待创建 | 已有功能改造 |
| 接口对接需求模板 | integration-prd-template.md | 待创建 | DTC / AAI / WalletConnect 等对接 |

## 3. 使用规则

- 写新 PRD 前必须先查 knowledge-base。
- 复用既有规则时必须写来源引用。
- 发现知识库缺口时，必须记录待确认事项。
- 涉及资金、账户、卡、交易、KYC 时，必须包含风控 / 合规边界。
