---
module: _meta
feature: field-dictionary
version: "1.1"
status: source_gap
source_doc: archive/converted-prd/**/README.md；knowledge-base/* 已校准模块
source_section: Converted PRD corpus / statuses, fields, limits, regions, compliance boundaries
last_updated: 2026-05-09
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

## Source alignment additions

| 字段 | 含义 / 用途 | 来源 |
|---|---|---|
| UID | 注册成功后服务端生成的用户 ID | registration-login |
| DeviceID / deviceId | 唯一识别用户客户端设备，用于设备绑定、可信设备判断和风控 | security；registration-login |
| AIX Tag | 用户标识 / 收款人相关字段，Send 场景需要后续完整沉淀 | wallet/deposit-send-swap |
| cardId | 卡记录定位字段，卡状态变更 webhook 根据 cardId 定位卡记录 | notification/push-inbox；card/manage |
| newCardStatus | 卡状态变更 webhook 的最新卡状态来源 | notification/push-inbox |
| requestAmount / requestCurrency | Card Transaction Detail 中的法币交易金额和币种 | transaction-history |
| dtcQuoteId | OTC Swap 一次性报价标识，用后失效 | wallet/deposit-send-swap |
| title / body | Push 基础字段，保留用于老消息兼容和 push 展示 | notification/push-inbox |

## 4. 维护规则

- 字段必须标明来源接口或来源 PRD。
- 同一字段不得重复定义多个含义。
- 涉及敏感信息时，必须写脱敏规则。
- 涉及资金金额时，必须写币种、精度、舍入规则。
