---
module: _meta
feature: status-dictionary
version: "2.0"
status: active
source_doc: archive/converted-prd/**/README.md；knowledge-base/* 已校准模块
source_section: converted PRD corpus / status dictionary
last_updated: 2026-05-09
owner: 吴忆锋
readers: [product, ui, dev, qa, business, ai]
---

# Status Dictionary 状态字典

## 1. 文档定位

本文沉淀跨模块状态、状态来源、展示边界和禁止混用规则。

## 2. Account / Security 状态

| 状态域 | 状态 | 说明 | 来源 |
|---|---|---|---|
| Account | Active | 注册成功后账户状态 | account/registration.md |
| Account | Banned | 账户不可登录 | account/_index.md；account/login.md |
| Account | Closed | 账户不可登录 | account/_index.md |
| Account | Locked | 不作为 Account Status 沉淀；源 PRD 中为删除线 | account/_index.md |
| Security Lock | Locked | OTP / Email OTP / Login Passcode / Face Auth 的场景锁定 | security/global-rules.md |

## 3. KYC 状态

| 状态 | 说明 | Home 映射 | 来源 |
|---|---|---|---|
| Pending / 无开户记录 | 未完成开户 | 显示未申请开通钱包面板 | kyc/account-opening.md；home/app-home.md |
| Under Review | 审核中 | 显示审核中面板，3 Steps Finished | kyc/account-opening.md；home/app-home.md |
| Failed | 审核失败 | 显示审核失败面板，可 Reactivate Now | kyc/account-opening.md；home/app-home.md |
| Rejected | 审核拒绝 | 隐藏激活钱包入口 | kyc/account-opening.md；home/app-home.md |
| Approved | 审核通过 | 展示资产面板 | kyc/account-opening.md；home/app-home.md |

## 4. Card 状态

| 状态 | 说明 | 来源 |
|---|---|---|
| Processing | 审核中 / 在途 | card/application.md；card/card-home.md |
| Pending activation | 待激活 | card/application.md；card/manage/activation.md |
| Active | 已激活 | card/manage/_index.md |
| Frozen / Suspended | 冻结 / 锁定类卡状态 | card/manage/status-and-operations.md |
| Terminated / Cancelled | 申卡失败 / 取消等场景可能用于 MGM 减免费解冻 | card/application.md |

注意：Home PRD 与 Card Application PRD 对 Processing、Pending activation、Active 未设置 PIN、Frozen 的首页点击跳转存在冲突，状态解释不得直接推出唯一跳转。

## 5. Transaction 状态

| 状态 | 说明 | 来源 |
|---|---|---|
| Pending | 待处理 | transaction/status-model.md |
| Success | 成功 | transaction/status-model.md |
| Refunded | 已退款 | transaction/status-model.md |
| Declined | 被拒绝 / 失败类展示 | transaction/status-model.md |
| Under Review | 风控审核 / Risk Withheld 等场景可引用，但不得等同 Wallet REJECTED | transaction/status-model.md |
| Cancelled | 已取消 | transaction/status-model.md |

## 6. Transaction 原始类型

| 来源 | 原始类型 | AIX 处理 | 来源文件 |
|---|---|---|---|
| Crypto | DEPOSIT、TRANSFER_IN、TRANSFER_OUT、CARD_FEE_DEBIT、CARD_FEE_REFUND | 可进入全量交易展示 | transaction/status-model.md |
| Card | PURCHASE、CASH_WITHDRAWAL、REFUND、INCREMENTAL_AUTH | 可进入全量交易 / Card History 展示 | transaction/status-model.md |
| Card | REVERSAL / type=19 | 作为退款展示，前端与 REFUND 一样显示 refund-商户名称 | transaction/status-model.md |
| OTC | 兑换记录 | 展示为 Swap；Swap 列表不显示交易状态 | transaction/status-model.md |

## 7. Notification 状态

| 状态域 | 状态 | 说明 | 来源 |
|---|---|---|---|
| User status | active | 满足其他条件时可推送 | common/notification.md |
| User status | inactive / Closed / banned | 停止全部消息推送 | common/notification.md |
| Message read | read / unread | 未读显示红点，已读不显示 | common/notification.md |

## 8. Sources

- (Ref: knowledge-base/* 已校准模块)
