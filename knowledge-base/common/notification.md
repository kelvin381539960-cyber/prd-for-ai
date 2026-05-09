---
module: common
feature: notification
version: "2.0"
status: active
source_doc: archive/converted-prd/notification/push-inbox/README.md；archive/converted-prd/notification/system-email/README.md
source_section: Notification push/inbox / 接入链路、Push、消息中心、通知设置、Webhook；System Email / interface interaction
last_updated: 2026-05-09
owner: 吴忆锋
readers: [product, ui, dev, qa, business, ai]
depends_on:
  - common/_index
  - common/errors
  - wallet/_index
  - card/_index
  - transaction/_index
---

# Notification Push / 站内信公共能力

## 1. 文档定位

本文沉淀 AIX App Notification 公共能力，包括 Push、站内信 / 消息中心、通知偏好、Webhook 接入边界、System Email 边界，以及与业务模块的触发关系。

本文不维护每一条 System Notification 模板正文全集。模板正文以源 PRD 引用的 AIX System Notification / AIX System Notification + content 表为内容源；本文维护能力、字段、路由、状态和边界。

## 2. Source alignment status

本文件已按 `archive/converted-prd/notification/push-inbox/README.md` 和 `archive/converted-prd/notification/system-email/README.md` 重写，原 `SOURCE_GAP` 已收口为 `ALIGNED`。

## 3. 通知平台链路

| 环节 | 规则 |
|---|---|
| App Backend | App Backend 调用 message-center |
| message-center | 对上游接收到的消息进行过滤、push、存储等操作 |
| 消息存储 | 存储到 DB 的消息展示在用户消息列表中 |
| Push | message-center 对符合要求的消息发送到 message-push-system，再由 message-push-system 推送到 App Client |
| 锁屏通知 | Push 是用户锁屏时的系统通知 |
| device-token | Push 依赖 App 上报用户 device-token，用于确认推送设备 |

## 4. 接入方式

| 接入方式 | 说明 |
|---|---|
| 系统 API 调用通知 | 业务系统通过 API 触发通知 |
| OBoss 配置调用通知 | 运营 / 配置侧通过 OBoss 配置触达 |
| Webhook 接入 | Wallet、Card、Card Status 等外部事件通过 webhook 推送后触发业务处理和通知 |
| System Email | 已实现 MoEngage standard protocol，技术上可发送 emails；模板和 body 配置仍以 system email PRD 待确认项为边界 |

## 5. 合规原则

| 类型 | 规则 |
|---|---|
| 金融信息 | 合规优先 |
| 营销类通知 | 需要用户明确同意 |
| 通知类信息 | 需要标注机构信息和联系方式 |
| 加密资产相关通知 | 需要提示风险，不承诺收益 |

## 6. Push 规则

| 规则 | 结论 |
|---|---|
| Push 基础字段 | title / body 仍需保留，用于老消息兼容以及 push 消息展示 |
| Push 可发送前置 | 系统设置通知开关开启、user status = active |
| 停止推送状态 | inactive / Closed / banned 停止全部消息推送 |
| Push 发送优先级 | user status > user notification preference > FC & DND |
| Promotion / System | 若 category 为 promotion 或 system，需用户 notification preference 包含 push |
| 字符长度限制 | Push 可展示字符长度限制在源 PRD 中为待定，不沉淀具体数值 |
| 点击行为 | 点击 push 跳转至 OBoss 配置的链接 |

## 7. Notification Center / 消息中心

| 规则 | 结论 |
|---|---|
| 入口 | Home page 右上角 metab-notifications |
| 一键已读 | 点击后将所有消息标记为已读，toast：`全部已读` |
| 未读红点 | 有未读消息显示小红点，已读消息不显示红点 |
| 分类红点 | 分类下有未读消息时 Category tag 展示红点 |
| 列表点击 | 点击消息后列表页未读标识消失 |
| Me tab 未读数字 | 未读消息超过 100 条展示 `99+` |
| 返回 Me tab | 进入消息列表返回 Me tab 后红点消失但数字保留 |
| 消息标题 | 若有 Key title 展示 Key title，否则取 Title 展示 |

## 8. Notification Category

| 一级分类 | 二级 / 类型范围 |
|---|---|
| Transaction | Payment、Withdrawal、deposit、Transfer、Swap、Refund、Card application、abnormal transaction 等 |
| Card | Card transaction、Card status、Card delivery / activation 等由业务触发 |
| Security / Support | 安全与支持类通知，具体模板依赖 AIX System Notification 表 |
| Promotion | 受用户偏好与合规同意约束 |
| System | 系统类消息，受 system notification preference 约束 |

## 9. Notification Preference / 通知设置

| 项目 | 规则 |
|---|---|
| 设置入口 | APP - 我的 - 设置 - 通知设置 |
| Channel | SMS / Email / Push |
| 用户注册默认值 | promotions(email/push/sms) 全部开启；system(email/push/sms) 全部开启 |
| 用户注销默认值 | promotions(email/push/sms) 全部关闭；system(email/push/sms) 全部开启 |
| MoEngage 同步 | “同步 MoEngage user subscribe status 至 user notification preference”为删除线，不沉淀为 confirmed fact |

## 10. Webhook 接入

| Webhook 类型 | 规则 |
|---|---|
| 加密钱包交易类 webhook | 属于 Notification 源文档 webhook 接入范围，需按 Wallet 交易状态触发通知 |
| 卡交易类 webhook | 卡消费成功依赖 webhook 状态；卡退款成功依赖 refund / reversal 等交易状态 |
| 卡状态变更 webhook | 收到 webhook 后，后端根据 cardId 定位对应卡记录，并以 newCardStatus 作为最新状态来源，同步更新 AIX 卡状态 |
| Card transaction | 交易展示 / 退款 / REVERSAL 具体口径以 `card/transaction.md` 与 `transaction/status-model.md` 为准 |
| Wallet transaction | Deposit / Send / Swap 结果页和交易详情以 Wallet 与 Transaction 模块为准 |

## 11. System Notification 模板边界

| 项目 | 规则 |
|---|---|
| 模板来源 | 源 PRD 多处引用 AIX System Notification / AIX System Notification + content 表 |
| KB 处理 | 本文件不复制整张外部表；具体 title / body / status icon 以外部表或后续专门模板字典为准 |
| Key title | 消息标题存在 Key title 时优先展示 Key title，否则展示 Title |
| Status icon | 具体 icon 映射依赖模板内容源，不在本文自行推导 |
| 业务触发 | 业务模块只记录触发边界，具体模板由 Notification 内容源配置 |

## 12. System Email

| 项目 | 规则 |
|---|---|
| 技术现状 | 已实现 MoEngage standard protocol，技术层面可以发送 emails |
| Template 设计 | system email template 包括 logo banner + body + footer，设计团队处理中 |
| Content 来源 | System email content 指向 AIX System Notification + content |
| 待确认 | system email / promotion email 的 template 和 body 是否配置在 MoEngage，以及是否调用 Create Email Template API，为源文档待确认项 |
| 数据埋点 | 待定，不沉淀为 confirmed fact |
| 数据分析 | 待定，不沉淀为 confirmed fact |

## 13. 业务模块边界

| 业务模块 | Notification 负责 | 业务模块负责 |
|---|---|---|
| Wallet | 通知链路、消息中心展示、Webhook 接入边界 | Deposit / Send / Swap 的业务结果、交易状态、结果页 |
| Card | 卡交易 / 卡状态通知接入边界 | 卡状态、卡交易、卡管理业务规则 |
| Transaction | 异常文案和通知展示边界 | 交易类型、状态、详情字段 |
| Security | 安全通知展示边界 | OTP / Face / BIO / Passcode 认证规则 |
| OBoss | 配置调用通知能力边界 | OBoss 具体配置字段和运营后台能力 |

## 14. 不写入事实的内容

1. MoEngage subscribe status 同步为删除线，不作为 confirmed fact。
2. Push 可展示字符长度限制为待定，不写具体数值。
3. System Email template / body 是否配置在 MoEngage 为待确认，不写成已完成事实。
4. System Email 数据埋点、数据分析需求待定，不写成 confirmed fact。
5. 本文件不复制 AIX System Notification + content 全量模板正文。

## 15. Sources

- (Ref: archive/converted-prd/notification/push-inbox/README.md)
- (Ref: archive/converted-prd/notification/system-email/README.md)
- (Ref: knowledge-base/card/transaction.md)
- (Ref: knowledge-base/transaction/status-model.md)
- (Ref: knowledge-base/wallet/deposit.md)
- (Ref: knowledge-base/wallet/send.md)
- (Ref: knowledge-base/wallet/swap.md)
