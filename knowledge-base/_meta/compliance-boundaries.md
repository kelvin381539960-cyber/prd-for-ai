---
module: _meta
feature: compliance-boundaries
version: "1.0"
status: draft
source_doc: IMPLEMENTATION_PLAN.md
source_section: "4. 推荐目录结构"
last_updated: 2026-05-01
owner: 吴忆锋
readers: [product, dev, qa, business, ai]
---

# Compliance Boundaries 合规边界

## 1. 文档定位

本文档用于沉淀 AIX 涉及 KYC、AML、制裁、高风险地区、资金路径、交易报备、卡与钱包合规边界的全局规则。

## 2. 合规边界分类

| 分类 | 适用模块 | 示例 | 来源 | 状态 |
|------|----------|------|------|------|
| KYC Boundary | wallet / security / card | 开户、申卡、活体、证件验证 | 待补充 | draft |
| AML / Risk Boundary | wallet / transaction | 风控拦截、资金 hold、交易报备 | 待补充 | draft |
| Sanction Boundary | card / wallet | 高风险地区、制裁地区过滤 | 待补充 | draft |
| Travel Rule Boundary | wallet | GTR、WalletConnect、地址充值 | 待补充 | draft |
| Funds Traceability | wallet / card / transaction | 资金入账、冻结、退款、回退钱包 | 待补充 | draft |

## 3. 记录模板

| 边界名称 | 适用场景 | 规则内容 | 资金影响 | 系统动作 | 用户影响 | 来源 | 待确认 |
|----------|----------|----------|----------|----------|----------|------|--------|
| TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |

## 4. 维护规则

- 涉及资金路径必须可追溯。
- 涉及交易失败必须说明资金状态。
- 涉及 KYC / AML / 制裁必须明确支持范围与禁止范围。
- 合规不确定时，不得推断，必须标记待确认。
