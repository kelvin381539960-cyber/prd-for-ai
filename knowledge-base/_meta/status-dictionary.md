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
| Account Status | Active / Locked / Banned / Closed | account | AIX Card 注册登录需求V1.0 | seeded |
| IVS Status | INITIAL / VALIDATING / DONE / EXPIRED | security | AIX Security 身份认证需求V1.0 | seeded |
| KYC Status | 待补充 | wallet / security | 待补充 | draft |
| Card Status | 待补充 | card | 待补充 | draft |
| Card Transaction Status | 待补充 | transaction | 待补充 | draft |
| Crypto Transaction State | 待补充 | wallet / transaction | 待补充 | draft |
| OTC Status | 待补充 | wallet / transaction | 待补充 | draft |

## 3. Account Status

| 状态值 | 标准名称 | 含义 | 是否终态 | 可迁移到 | 来源 | 备注 |
|--------|----------|------|----------|----------|------|------|
| Active | Active | 账户正常使用中 | 否 | Locked / Banned / Closed | AIX Card 注册登录需求V1.0 / 5.2 账户说明 | 注册成功后进入 |
| Locked | Locked | 因安全原因临时锁定 | 否 | Active | AIX Card 注册登录需求V1.0 / 5.2 账户说明 | 锁定到期或忘记密码重置后解除 |
| Banned | Banned | 账户被限制使用，可恢复 | 否 | Active（需客服 / 风控处理） | AIX Card 注册登录需求V1.0 / 5.2 账户说明 | 一期不支持 |
| Closed | Closed | 账户被注销，不可恢复 | 是 | 无 | AIX Card 注册登录需求V1.0 / 5.2 账户说明 | 一期不支持 |

## 4. IVS Status

| 状态值 | 标准名称 | 含义 | 是否终态 | 可迁移到 | 来源 | 备注 |
|--------|----------|------|----------|----------|------|------|
| INITIAL | INITIAL | 发起挑战初始化，create challenge | 否 | VALIDATING / EXPIRED | AIX Security 身份认证需求V1.0 / 7.5 身份认证状态机 | 非终态 |
| VALIDATING | VALIDATING | 验证中 | 否 | DONE / EXPIRED | AIX Security 身份认证需求V1.0 / 7.5 身份认证状态机 | 非终态 |
| DONE | DONE | 验证成功完成 | 是 | 无 | AIX Security 身份认证需求V1.0 / 7.5 身份认证状态机 | 终态 |
| EXPIRED | EXPIRED | 已过期，流程终止 | 是 | 无 | AIX Security 身份认证需求V1.0 / 7.5 身份认证状态机 | 终态 |

## 5. 待补充状态

| 分类 | 适用模块 | 待补充内容 | 优先级 |
|------|----------|------------|--------|
| KYC Status | wallet / security | KYC 审核、证件、活体、POA 状态 | P0 |
| Card Status | card | 卡申请、实体卡、虚拟卡、冻结、激活、注销状态 | P0 |
| Transaction Status | transaction | 卡交易、钱包交易、退款、失败、风控拦截状态 | P0 |
| Crypto Transaction State | wallet / transaction | GTR、WalletConnect、链上充值、提现状态 | P0 |
| OTC Status | wallet / transaction | 法币交易、兑换相关状态 | P1 |

## 6. 维护规则

- 状态必须标明来源。
- 渠道原始状态、后端状态、前端展示状态需分开记录。
- 资金和交易相关状态必须能闭环。
- 无法闭环时必须标记“冲突 / 待确认”。
