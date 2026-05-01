---
module: _meta
feature: status-dictionary
version: "1.0"
status: draft
source_doc: IMPLEMENTATION_PLAN.md
source_section: "4. 推荐目录结构"
last_updated: 2026-05-01
owner: 吴忆锋
readers: [product, dev, qa, business, ai]
---

# Status Dictionary 状态字典

## 1. 文档定位

本文档用于沉淀 AIX 全局状态定义、状态来源、状态映射、终态与迁移规则。

状态字典优先服务开发、测试、交易链路、卡链路、钱包链路和 AI PRD 复用。

## 2. 状态分类

| 分类 | 示例 | 适用模块 | 来源 | 状态 |
|------|------|----------|------|------|
| Account Status | Active / Locked / Banned / Closed | account | 待补充 | draft |
| IVS Status | INITIAL / VALIDATING / DONE / EXPIRED | security | 待补充 | draft |
| KYC Status | 待补充 | wallet / security | 待补充 | draft |
| Card Status | 待补充 | card | 待补充 | draft |
| Card Transaction Status | 待补充 | transaction | 待补充 | draft |
| Crypto Transaction State | 待补充 | wallet / transaction | 待补充 | draft |
| OTC Status | 待补充 | wallet / transaction | 待补充 | draft |

## 3. 状态记录模板

| 状态值 | 标准名称 | 含义 | 是否终态 | 可迁移到 | 来源 | 备注 |
|--------|----------|------|----------|----------|------|------|
| TBD | TBD | TBD | TBD | TBD | TBD | TBD |

## 4. 维护规则

- 状态必须标明来源。
- 渠道原始状态、后端状态、前端展示状态需分开记录。
- 资金和交易相关状态必须能闭环。
- 无法闭环时必须标记“冲突 / 待确认”。
