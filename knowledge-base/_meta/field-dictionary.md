---
module: _meta
feature: field-dictionary
version: "1.0"
status: draft
source_doc: IMPLEMENTATION_PLAN.md
source_section: "4. 推荐目录结构"
last_updated: 2026-05-01
owner: 吴忆锋
readers: [product, dev, qa, ai]
---

# Field Dictionary 字段字典

## 1. 文档定位

本文档用于沉淀 AIX 全局字段定义、字段来源、读写关系、脱敏规则和前后端展示规则。

字段字典优先服务开发、测试、接口对接、数据校验和 AI PRD 复用。

## 2. 字段分类

| 分类 | 适用模块 | 示例 | 来源 | 状态 |
|------|----------|------|------|------|
| Account Fields | account | UID / email / mobile / deviceId | 待补充 | draft |
| Security Fields | security | challengeId / token / expireTime | 待补充 | draft |
| Wallet Fields | wallet | balance / currency / mainNet | 待补充 | draft |
| Card Fields | card | cardStatus / cardNumber / cvc / expiryDate | 待补充 | draft |
| Transaction Fields | transaction | txnId / referenceNo / amount / status | 待补充 | draft |
| Growth Fields | growth | referralCode / bannerId / popupId | 待补充 | draft |

## 3. 字段记录模板

| 字段名 | 标准名称 | 类型 | 含义 | 读/写 | 脱敏规则 | 来源接口/页面 | 来源文档 | 备注 |
|--------|----------|------|------|------|----------|--------------|----------|------|
| TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |

## 4. 维护规则

- 字段必须标明来源接口或来源 PRD。
- 同一字段不得重复定义多个含义。
- 涉及敏感信息时，必须写脱敏规则。
- 涉及资金金额时，必须写币种、精度、舍入规则。
