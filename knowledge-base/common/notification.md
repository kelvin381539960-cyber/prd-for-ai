---
module: common
feature: notification
version: "1.1"
status: source_gap
source_doc: archive/converted-prd/notification/push-inbox/README.md；archive/converted-prd/notification/system-email/README.md
source_section: Notification push/inbox / 消息接入、Push、消息中心、Webhook、通知设置；System Email / system email interface interaction
last_updated: 2026-05-09
owner: 吴忆锋
depends_on:
  - common/_index
  - integrations/walletconnect
  - common/errors
  - wallet/deposit
  - changelog/knowledge-gaps
---

# Notification Push / 站内信公共能力

> Source alignment note: 本文件已按 converted-prd 做双向覆盖校验。由于 `archive/converted-prd/notification/push-inbox/README.md` 范围很大，现有 KB 尚未完整沉淀消息中心、分类、通知设置、OBoss 配置、Webhook 全量通知和系统邮件能力，因此本文件状态标为 `SOURCE_GAP`。


## 1. 功能定位

Notification 用于沉淀 AIX 跨模块通知能力，包括 push、站内信、触发源、触发条件、模板参数、跳转目标和业务边界。

本文不重写业务流程；业务文件只引用通知结果。通知触发条件和模板参数必须来自 Notification PRD、截图、接口文档或已确认结论。

所有未确认问题统一引用 `knowledge-base/changelog/knowledge-gaps.md` 的 ALL-GAP 编号；本文不再维护本地 NOTIF-GAP checklist。

## 2. 已确认通知能力

| 通知 | 触发源 | 条件 | 跳转目标 | 来源 |
|---|---|---|---|---|
| 卡交易成功 | Card Transaction Notify | `indicator=debit`，`status=101 AUTHORIZED` | 卡交易详情页 | Notification PRD；Card Transaction Flow |
| 卡退款成功 | Card Transaction Notify | `indicator=credit`，refund / reversed 场景 | 卡交易详情页 | Notification PRD；Card Transaction Flow |
| 钱包充值成功 | Webhook→notify | `event=CRYPTO_TXN`，`type=DEPOSIT`，`state=success` | 交易详情页 | Notification PRD / Deposit row |
| 钱包充值冻结 / under review | Webhook→notify | `event=CRYPTO_TXN`，`type=DEPOSIT`，`state=RISK_WITHHELD` | 交易详情页 | Notification PRD / Deposit row |

## 3. 已确认通知参数

| 通知类型 | 参数 | 来源 | 备注 |
|---|---|---|---|
| 卡交易 / 卡退款通知 | `merchant_name` | Notification PRD | 商户名称 |
| 卡交易 / 卡退款通知 | `amount` | Notification PRD | 金额 |
| 卡交易 / 卡退款通知 | `currency` | Notification PRD | 币种 |
| 卡交易 / 卡退款通知 | `transaction_time` | Notification PRD | 交易时间 |
| 卡交易 / 卡退款通知 | `full_name` | Notification PRD | 用户姓名 |
| 卡交易 / 卡退款通知 | `last 4` | Notification PRD | 卡号后 4 位 |
| 钱包充值成功 | `amount`、`currency` | Notification PRD / Deposit row | 模板参数 |
| 钱包充值冻结 / under review | `full_name`、`deposit_transaction_hash`、`amount`、`currency` | Notification PRD / Deposit row | 模板参数 |

## 4. Deposit 通知边界

Deposit 当前 active，包含 GTR 和 WalletConnect。现有 Notification PRD 明确的是 Deposit 通用通知，不足以证明 GTR 与 WalletConnect 各自完整通知规则完全相同。

| 通知场景 | 已确认 | ALL-GAP 边界 |
|---|---|---|
| 钱包充值成功 | `event=CRYPTO_TXN`、`type=DEPOSIT`、`state=success` 触发；跳转交易详情页；渠道为 in-app Notification 及 push | 是否覆盖 GTR / WC 所有路径、具体 webhook 逻辑见 ALL-GAP-010；是否以 Wallet 入账为触发点见 ALL-GAP-065 |
| 钱包充值冻结 / under review | `event=CRYPTO_TXN`、`type=DEPOSIT`、`state=RISK_WITHHELD` 触发；跳转交易详情页；渠道为 Email、in-app Notification 及 push | 是否覆盖 GTR / WC 所有路径、review 后续处理见 ALL-GAP-010、ALL-GAP-008 |
| 入金失败通知 | 未确认 | 不写成事实；见 ALL-GAP-063 |
| Declare / Travel Rule 待处理通知 | 未确认 | 不写成事实；见 ALL-GAP-044 |
| 资金可见 / 入账完成通知 | 未确认 | 不写成除 success 外的独立事实；见 ALL-GAP-065 |

## 5. Deposit 通知文案边界

| 通知 | 已确认文案 / key | 来源 |
|---|---|---|
| 钱包充值成功 push title | `deposit_successful` | Notification PRD / Deposit row |
| 钱包充值成功 push body | `your_aix_pay_wallet_received` | Notification PRD / Deposit row |
| 钱包充值成功英文展示 | Title: `Deposit successful`; Body: `Your AIX Pay wallet received %1$s %2$s.` | Notification PRD / Deposit row |
| 钱包充值冻结 push title | `deposit_under_review` | Notification PRD / Deposit row |
| 钱包充值冻结 push body | `your_deposit_of_3s_4s` | Notification PRD / Deposit row |
| 钱包充值冻结邮件 title | `action_required_for` | Notification PRD / Deposit row |
| 钱包充值冻结邮件 body | `hi_1s_your_stablecoin_deposit` | Notification PRD / Deposit row |

## 6. 通知与业务结果边界

| 场景 | 当前结论 | 来源 / ALL-GAP | 处理 |
|---|---|---|---|
| 卡退款 / 卡交易成功通知 | 正常情况下用户收到通知后，预期资金已归集至 Wallet | 用户确认 / Card Transaction Flow | 可作为正常用户预期 |
| 极端异常 | 卡有钱但转 Wallet 失败时，用户可能看不到资金 | 用户确认 / Card Transaction Flow | 不得写成通知必然等于 Wallet 到账 |
| DTC transfer 成功但 Wallet 未到账 | 当前无法系统自动发现，主要依赖用户反馈 | 用户确认 / ALL-GAP-027 | 不得写成通知可自动发现异常 |
| 钱包充值成功通知 | Notification PRD 显示 success 通知 | ALL-GAP-010、ALL-GAP-065 | 不代表所有 Deposit 子路径状态机完整闭环；不代表一定以 Wallet 入账为触发点 |
| 钱包充值冻结通知 | Notification PRD 显示 Risk Withheld / under review 通知 | ALL-GAP-008、ALL-GAP-010 | 不代表 Declare / Travel Rule 流程已完整确认 |

## 7. WalletConnect / Deposit 通知重点问题

| 问题 | 当前处理 |
|---|---|
| 钱包连接成功是否通知 | 未确认，不默认存在；见 ALL-GAP-010 / ALL-GAP-063 边界 |
| 钱包连接失败是否通知 | 未确认，不默认存在；见 ALL-GAP-013、ALL-GAP-063 |
| 用户拒绝授权是否通知 | 未确认，不默认存在；见 ALL-GAP-013、ALL-GAP-063 |
| 入金已发起是否通知 | 未确认，不默认存在；见 ALL-GAP-063、ALL-GAP-065 |
| 入金 on-hold / Risk Withheld 是否通知 | Deposit under review 已有通用通知；是否覆盖 WC / GTR 全路径见 ALL-GAP-010 |
| 入金 rejected 是否通知 | 未确认，不默认存在；见 ALL-GAP-063 |
| 入金 completed 是否通知 | Deposit success 已有通用通知；是否覆盖 WC / GTR 全路径见 ALL-GAP-010 |
| 通知是否跳转交易详情 | Deposit 通知记录跳转交易详情页；WC 具体跳转目标见 ALL-GAP-010 |

## 8. 不写入事实的内容

以下内容不得写成事实：

1. GTR 和 WalletConnect 使用同一套通知模板。
2. GTR 和 WalletConnect 使用同一套通知触发条件。
3. 钱包充值成功通知覆盖所有 Deposit 子路径和所有异常后恢复场景。
4. 通知系统可自动发现 DTC transfer 成功但 Wallet 未到账。
5. WalletConnect 钱包连接成功 / 失败一定会通知。
6. WalletConnect 通知一定跳转交易详情。
7. 未在 Notification PRD 中出现的模板参数。
8. Deposit 通知一定以 Wallet 入账为触发点。
9. 站内信与 Push 的模板、触发、参数一定完全一致。

## 9. ALL-GAP 引用

本文不维护独立待补表。Notification 相关不确定项统一引用 ALL-GAP：

| 编号 | 主题 |
|---|---|
| ALL-GAP-010 | GTR / WalletConnect 是否复用 Deposit success / under review 通知 |
| ALL-GAP-013 | WalletConnect 失败是否需要告警 |
| ALL-GAP-027 | DTC transfer 成功但 Wallet 未入账发现机制 |
| ALL-GAP-034 | KYC 结果是否触发通知 |
| ALL-GAP-044 | WalletConnect Declare / Travel Rule / 白名单规则边界 |
| ALL-GAP-045 | 通知失败重试 / 补发策略 |
| ALL-GAP-062 | Receive 入账状态、失败 / on-hold 与通知规则 |
| ALL-GAP-063 | Wallet 入金失败通知规则 |
| ALL-GAP-064 | 站内信与 Push 是否完全一致 |
| ALL-GAP-065 | Deposit 通知是否以 Wallet 入账为触发点 |

## 10. 历史 NOTIF-GAP 到 ALL-GAP 映射

本表用于无损迁移历史问题，不作为新的模块级 checklist。后续只维护 ALL-GAP。

| 原编号 | 原问题 | 当前 ALL-GAP |
|---|---|---|
| NOTIF-GAP-001 | GTR Deposit 是否完全复用 Deposit success / Risk Withheld 通知 | ALL-GAP-010 |
| NOTIF-GAP-002 | WalletConnect Deposit 是否完全复用 Deposit success / Risk Withheld 通知 | ALL-GAP-010 |
| NOTIF-GAP-003 | Wallet 入金失败通知 | ALL-GAP-063 |
| NOTIF-GAP-004 | Wallet KYC 通知规则 | ALL-GAP-034 |
| NOTIF-GAP-005 | 站内信与 Push 是否完全一致 | ALL-GAP-064 |
| NOTIF-GAP-006 | 通知失败重试 / 补发策略 | ALL-GAP-045 |
| NOTIF-GAP-007 | Deposit 通知是否以 Wallet 入账为触发点 | ALL-GAP-065 |

## Source alignment additions

### A. 已补齐的基础通知能力

| 规则 | 结论 | 来源 |
|---|---|---|
| 通知平台链路 | App Backend 调用 message-center；message-center 对上游消息进行过滤、push、存储；存储到 DB 的消息展示在用户消息列表 | push/inbox / 接入说明 |
| Push 链路 | 符合要求的消息发送到 message-push-system，再推送至 App Client 锁屏通知 | push/inbox / 接入说明 |
| device-token | Push 依赖 App 上报用户 device-token，用于确认推送设备 | push/inbox / 接入说明 |
| 接入方式 | 支持系统 API 调用通知和 OBoss 配置调用通知 | push/inbox / 需求概况 |
| 合规原则 | 金融信息合规优先；营销类需用户明确同意；通知类需标注机构信息和联系方式；涉及加密资产需提示风险，不承诺收益 | push/inbox / 需求背景 |
| Push 基础字段 | title / body 仍需保留，用于老消息兼容以及 push 消息展示 | push/inbox / Push字段 |
| Push 可发送前置 | 系统设置通知开关开启、user status=active；inactive/Closed/banned 停止全部消息推送 | push/inbox / push规则 |
| Push 发送优先级 | user status > user notification preference > FC & DND | push/inbox / push规则 |
| Push 点击 | 点击 push 跳转至 OBoss 配置链接 | push/inbox / push规则 |

### B. 消息中心 / 站内信规则

| 规则 | 结论 | 来源 |
|---|---|---|
| 入口 | Home page 右上角 metab-notifications | push/inbox / Notification Center |
| 一键已读 | 点击后将所有消息标记为已读，toast：全部已读 | push/inbox / Notification Center |
| 未读红点 | 有未读消息显示小红点，已读消息不显示红点 | push/inbox / Notification Center |
| 分类红点 | 分类下有未读消息时 Category tag 展示红点 | push/inbox / Notification Center |
| 列表点击 | 点击消息后列表页未读标识消失 | push/inbox / Notification Center |
| 未读数字 | Me tab 未读消息数字超过 100 条展示 99+；进入消息列表返回 Me tab 后红点消失但数字保留 | push/inbox / Me tab |
| 消息标题 | 若有 Key title 展示 Key title，否则取 Title 展示 | push/inbox / Notification cards |
| 一级/二级分类 | Transaction 下包括 Payment、Withdrawal、deposit、Transfer、Swap、Refund、Card application、abnormal transaction 等 | push/inbox / Notification Category |

### C. 通知设置

| 规则 | 结论 | 来源 |
|---|---|---|
| 通知设置入口 | APP - 我的 - 设置 - 通知设置 | push/inbox / 通知设置 |
| 用户注册默认值 | promotions(email/push/sms) 全部开启；system(email/push/sms) 全部开启 | push/inbox / notification preference |
| 用户注销默认值 | promotions(email/push/sms) 全部关闭；system(email/push/sms) 全部开启 | push/inbox / notification preference |
| MoEngage 同步 | “同步 MoEngage user subscribe status 至 user notification preference”在源文档为删除线，不沉淀为 confirmed fact | push/inbox / notification preference |
| Channel | SMS / Email / Push | push/inbox / notification preference |

### D. Webhook source rules

| Webhook | 结论 | 来源 |
|---|---|---|
| 加密钱包交易类 webhook | 属于 Notification 源文档 webhook 接入范围，需按 Wallet 交易状态触发通知 | push/inbox / Webhook接入 |
| 卡交易类 webhook | 卡消费成功依赖 status=101 AUTHORIZED；卡退款成功依赖 refund/reversal 等交易状态 | push/inbox / 修订记录 / webhook |
| 卡状态变更 webhook | 收到 webhook 后，后端根据 cardId 定位卡记录，并以 newCardStatus 作为最新状态来源，同步更新 AIX 卡状态 | push/inbox / 3 卡状态变更 |

### E. System email

| 规则 | 结论 | 来源 |
|---|---|---|
| 技术现状 | 已实现 MoEngage standard protocol，技术层面可以发送 emails | system-email / 需求概况 |
| 模板设计 | system email template 包括 logo banner + body + footer，设计团队处理中 | system-email / 需求概况 |
| 内容来源 | System email content 指向 AIX System Notification + content | system-email / 需求概况 |
| 待确认 | system email / promotion email 的 template 和 body 是否配置在 MoEngage，以及是否调用 Create Email Template API，均为待确认问题 | system-email / demo |
| 数据埋点 / 数据分析 | 待定，不沉淀为 confirmed fact | system-email / 数据埋点、数据分析需求 |

### F. Source gaps to resolve

| 缺口 | 说明 | 处理 |
|---|---|---|
| 全量消息模板 | 源文档大量引用 AIX System Notification + content 表格，当前 KB 未完整结构化所有 template key / title / body / status icon | SOURCE_GAP，后续需要单独抽取模板清单 |
| OBoss 配置通知 | 当前 KB 未完整沉淀 OBoss 配置调用通知、人群、FC&DND、跳转链接配置规则 | SOURCE_GAP |
| Webhook 全量事件 | 当前 KB 只覆盖 Deposit/Card 关键项，未完整沉淀所有 wallet/card/status webhook 事件 | SOURCE_GAP |
| Notification Center 全量页面字段 | 消息列表、详情、分类、状态标识等已补基础规则，但未完整结构化每张卡片字段 | SOURCE_GAP |
| System Email 模板实现 | 系统邮件模板和 body 是否配置在 MoEngage 仍为源文档待确认项 | NEED_CONFIRMATION |

### G. Runtime usage rule

在通知规则全量结构化前，回答具体通知模板、字段、跳转、状态 icon、OBoss 配置或系统邮件实现细节时，必须回查 `archive/converted-prd/notification/push-inbox/README.md` 与 `archive/converted-prd/notification/system-email/README.md`，不得只依赖本文件。

## 11. 来源引用

- (Ref: [2025-11-25] AIX+Notification / Deposit success row)
- (Ref: [2025-11-25] AIX+Notification / Deposit under review row)
- (Ref: DTC Wallet OpenAPI Document20260126 / 4.6 Webhook Service)
- (Ref: knowledge-base/wallet/deposit.md / v1.6)
- (Ref: knowledge-base/wallet/deposit.md / v1.1)
- (Ref: knowledge-base/integrations/walletconnect/_index.md / v1.4)
- (Ref: knowledge-base/common/errors.md / v1.4)
- (Ref: knowledge-base/changelog/knowledge-gaps.md / ALL-GAP 总表)
- (Ref: 用户确认结论 / 2026-05-02 / ALL-GAP 唯一总表与无损迁移规则)
