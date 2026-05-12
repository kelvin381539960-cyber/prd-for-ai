---
type: business-confirmation-checklist
status: active
language: zh-CN
last_updated: 2026-05-10
source_file: customer-support-kb/unresolved/pending-confirmation.md
---

# 业务确认清单

本文件用于把 `customer-support-kb/unresolved/pending-confirmation.md` 中的待确认问题转成可审核、可决策、可回填的表格。

所有条目在业务确认前，相关客服知识仍保持 `draft_pending_review`。

## 已应用确认批次

| Date | Confirmation Record | Status |
|---|---|---|
| 2026-05-12 | `customer-support-kb/review/confirmed-decisions-2026-05-12.md` | applied to relevant KB files |

说明：2026-05-12 已确认并回填的内容包括 Registration / Login、KYC、Wallet、Card、Transaction History、Notification 的一部分。未覆盖或用户明确表示不确定的内容继续保持 pending。

## 使用方法

1. 业务、产品、运营、合规或客服负责人逐项确认。
2. 在 `Decision` 中填写：`confirmed`、`rejected`、`internal_only`、`do_not_answer`、`needs_more_info`。
3. 在 `Confirmed Answer / Rule` 中填写可用于客服知识库的最终口径。
4. 如果确认结果可对用户展示，更新对应 `user-facing/` 或 `faq/` 文件。
5. 如果确认结果仅内部使用，更新对应 `agent-internal/` 文件。
6. 如果不可回答，更新 `unresolved/do-not-answer.md`。
7. 完成回填后，在本文件中把 `Status` 改为 `applied`。

## Decision 值说明

| Decision | 含义 | 后续动作 |
|---|---|---|
| `confirmed` | 可作为正式客服口径 | 回填到 user-facing / faq，并考虑改为 confirmed |
| `rejected` | 该内容不适用或已废弃 | 从客服知识中移除或保持不回答 |
| `internal_only` | 仅内部客服可见 | 回填到 agent-internal，不对用户展示 |
| `do_not_answer` | 不应由智能客服回答 | 加入 do-not-answer |
| `needs_more_info` | 信息不足，继续待确认 | 保持 pending |

## 1. Registration / Login

| ID | Question | Impacted KB Files | Suggested Reviewer | Decision | Confirmed Answer / Rule | Status |
|---|---|---|---|---|---|---|
| BR-LOGIN-001 | 当前是否支持邮箱注册、手机号注册，或两者都支持？ | `user-facing/registration-login.md`, `faq/registration-login-faq.md` | Product / Backend |  |  | pending |
| BR-LOGIN-002 | 登录方式是否仍支持邮箱、手机号和 Quick Login / Biometric？ | `user-facing/registration-login.md` | Product / App |  |  | pending |
| BR-LOGIN-003 | 验证码有效期是否可以对用户说明为 5 分钟？ | `user-facing/registration-login.md`, `faq/registration-login-faq.md` | Product / Security |  |  | pending |
| BR-LOGIN-004 | 验证码重发间隔、错误次数、锁定时长、重发次数是否有用户可见口径？ | `user-facing/registration-login.md`, `agent-internal/registration-login-playbook.md` | Product / Security / Risk |  |  | pending |
| BR-LOGIN-005 | 密码规则是否可明确说明为 8-32 位，且包含大小写字母、数字和符号？ | `user-facing/registration-login.md`, `faq/registration-login-faq.md` | Product / Security |  |  | pending |
| BR-LOGIN-006 | 推荐码是否必填？无推荐码时的标准口径是什么？ | `user-facing/registration-login.md`, `faq/registration-login-faq.md` | Product / Growth |  |  | pending |
| BR-LOGIN-007 | AIX Tag / X-Tag 是否仍为注册后的可选设置？是否可跳过？是否不可修改？ | `user-facing/registration-login.md`, `agent-internal/registration-login-playbook.md` | Product / App |  |  | pending |
| BR-LOGIN-008 | Banned / Closed / Locked 等账户状态是否存在？用户可见提示是什么？ | `user-facing/registration-login.md`, `_handoff-rules.md` | Product / Risk / Support |  |  | pending |
| BR-LOGIN-009 | 忘记密码流程是否上线？是否会关闭已开启的生物识别登录？ | `user-facing/registration-login.md`, `faq/registration-login-faq.md` | Product / Security |  |  | pending |
| BR-LOGIN-010 | 单设备绑定、最多一个设备在线等规则是否仍有效？是否可对用户展示？ | `agent-internal/registration-login-playbook.md`, `user-facing/registration-login.md` | Product / Security |  |  | pending |

## 2. KYC / Identity Verification / Wallet Opening

| ID | Question | Impacted KB Files | Suggested Reviewer | Decision | Confirmed Answer / Rule | Status |
|---|---|---|---|---|---|---|
| BR-KYC-001 | KYC 当前完整步骤是否为：选择居住国家/地区、协议确认、证件验证、人脸验证、地址证明、提交审核？ | `user-facing/kyc-wallet-opening.md`, `faq/kyc-faq.md` | Product / Compliance |  |  | pending |
| BR-KYC-002 | KYC 当前审核预计时间是否有官方口径？ | `user-facing/kyc-wallet-opening.md`, `faq/kyc-faq.md` | Compliance / Support |  |  | pending |
| BR-KYC-003 | KYC 支持哪些国家/地区？历史 PH / SG / AU / VN 是否仍有效？ | `user-facing/kyc-wallet-opening.md`, `pending-confirmation.md` | Compliance / Product |  |  | pending |
| BR-KYC-004 | 不支持国家/地区是否进入 Waitlist？Waitlist 当前是否仍有效？ | `user-facing/kyc-wallet-opening.md`, `user-facing/website-faq.md` | Product / Growth |  |  | pending |
| BR-KYC-005 | KYC 失败原因是否允许对用户展示？哪些失败原因可以展示？ | `user-facing/kyc-wallet-opening.md`, `agent-internal/kyc-wallet-opening-playbook.md` | Compliance / Risk / Support |  |  | pending |
| BR-KYC-006 | 用户身份信息填写错误后是否允许重新提交或修改？ | `user-facing/kyc-wallet-opening.md`, `_handoff-rules.md` | Product / Compliance |  |  | pending |
| BR-KYC-007 | Wallet Opening 和 KYC 的关系是否需要明确说明？ | `user-facing/kyc-wallet-opening.md` | Product |  |  | pending |
| BR-KYC-008 | 地址证明是否仍必需？支持哪些文件类型？文件大小限制是否为 16MB？ | `user-facing/kyc-wallet-opening.md`, `faq/kyc-faq.md` | Compliance / Product |  |  | pending |
| BR-KYC-009 | 地址证明签发时间要求是 3 个月、6 个月，还是其他规则？ | `user-facing/kyc-wallet-opening.md` | Compliance |  |  | pending |
| BR-KYC-010 | 人脸验证失败次数限制、Face Loading 超时 30 秒是否可对用户说明？ | `user-facing/kyc-wallet-opening.md`, `faq/kyc-faq.md` | Product / Security |  |  | pending |
| BR-KYC-011 | KYC 申请单长期有效、证件/人脸通过后永久有效等规则是否可对用户展示？ | `agent-internal/kyc-wallet-opening-playbook.md` | Compliance / Product |  |  | pending |
| BR-KYC-012 | 身份验证已过期时的正式用户口径是什么？ | `user-facing/kyc-wallet-opening.md`, `_handoff-rules.md` | Compliance / Support |  |  | pending |

## 3. Wallet Asset / Deposit / Send / Swap

| ID | Question | Impacted KB Files | Suggested Reviewer | Decision | Confirmed Answer / Rule | Status |
|---|---|---|---|---|---|---|
| BR-WALLET-001 | 当前支持哪些币种？FDUSD、USDC、USDT、WUSD 是否仍有效？ | `user-facing/wallet-asset.md`, `user-facing/wallet-deposit-send-swap.md` | Product / Wallet Ops |  |  | pending |
| BR-WALLET-002 | 当前支持哪些链 / 网络？BASE、BSC、ETHEREUM、SOLANA 是否仍有效？ | `user-facing/wallet-deposit-send-swap.md`, `faq/wallet-faq.md` | Product / Wallet Ops |  |  | pending |
| BR-WALLET-003 | 钱包资产页是否只展示稳定币？展示顺序是否固定？ | `user-facing/wallet-asset.md` | Product |  |  | pending |
| BR-WALLET-004 | 钱包总资产是否默认按 USD 估算？汇率异常时的用户口径是什么？ | `user-facing/wallet-asset.md` | Product / Finance Ops |  |  | pending |
| BR-WALLET-005 | Deposit 到账预计时间是否可以对用户说明？ | `user-facing/wallet-deposit-send-swap.md`, `faq/wallet-faq.md` | Wallet Ops / Support |  |  | pending |
| BR-WALLET-006 | Deposit 是否同时支持地址充值和 WalletConnect / 第三方钱包连接充值？ | `user-facing/wallet-deposit-send-swap.md` | Product / Wallet Ops |  |  | pending |
| BR-WALLET-007 | 地址充值是否仅支持特定来源钱包或交易所？是否可对用户说明？ | `user-facing/wallet-deposit-send-swap.md` | Wallet Ops / Compliance |  |  | pending |
| BR-WALLET-008 | WalletConnect 支持的钱包范围是否可对用户说明？ | `user-facing/wallet-deposit-send-swap.md` | Product / Wallet Ops |  |  | pending |
| BR-WALLET-009 | 充值最小金额、单笔限额、手续费、链上确认数是否有用户可见规则？ | `user-facing/wallet-deposit-send-swap.md`, `faq/wallet-faq.md` | Wallet Ops / Finance Ops |  |  | pending |
| BR-WALLET-010 | Send 功能是否当前可用？是否支持手机号、邮箱、X-Tag 收款人识别？ | `user-facing/wallet-deposit-send-swap.md` | Product / Wallet Ops |  |  | pending |
| BR-WALLET-011 | Send 是否需要人脸验证？失败次数和安全限制是否可对用户说明？ | `user-facing/wallet-deposit-send-swap.md`, `agent-internal/wallet-playbook.md` | Product / Security |  |  | pending |
| BR-WALLET-012 | Swap 功能是否当前可用？支持哪些币种互换？ | `user-facing/wallet-deposit-send-swap.md`, `faq/wallet-faq.md` | Product / Wallet Ops |  |  | pending |
| BR-WALLET-013 | Swap 汇率、过期、失败、取消等状态是否有正式用户口径？ | `user-facing/wallet-deposit-send-swap.md` | Product / Wallet Ops |  |  | pending |
| BR-WALLET-014 | 错链、错地址、错币种是否有明确处理口径？ | `faq/wallet-faq.md`, `_handoff-rules.md` | Wallet Ops / Support / Legal |  |  | pending |

## 4. Card Application / Manage / Transaction

| ID | Question | Impacted KB Files | Suggested Reviewer | Decision | Confirmed Answer / Rule | Status |
|---|---|---|---|---|---|---|
| BR-CARD-001 | 当前是否开放卡申请？ | `user-facing/card-application-manage.md`, `faq/card-faq.md` | Product / Card Ops |  |  | pending |
| BR-CARD-002 | 卡申请是否需要先完成钱包开户和 KYC？ | `user-facing/card-application-manage.md` | Product / Compliance |  |  | pending |
| BR-CARD-003 | 当前是否同时支持虚拟卡和实体卡？ | `user-facing/card-application-manage.md`, `faq/card-faq.md` | Product / Card Ops |  |  | pending |
| BR-CARD-004 | 虚拟卡是否自动激活？实体卡是否必须手动激活？ | `user-facing/card-application-manage.md`, `faq/card-faq.md` | Product / Card Ops |  |  | pending |
| BR-CARD-005 | 卡支持哪些国家/地区？PH、VN、AU 是否仍有效？ | `user-facing/card-application-manage.md`, `faq/card-faq.md` | Product / Compliance |  |  | pending |
| BR-CARD-006 | 卡申请失败原因是否可对用户展示？ | `user-facing/card-application-manage.md`, `agent-internal/card-playbook.md` | Card Ops / Support |  |  | pending |
| BR-CARD-007 | 卡费用：年费、申请费、制卡费、邮寄费、交易费、FX 费用等是否有用户口径？ | `user-facing/card-application-manage.md`, `faq/card-faq.md` | Card Ops / Finance Ops |  |  | pending |
| BR-CARD-008 | 卡限额是否有用户可见口径？ | `user-facing/card-application-manage.md` | Card Ops / Compliance |  |  | pending |
| BR-CARD-009 | 单用户最多可申请几张卡？是否允许多张卡同时审核中？ | `user-facing/card-application-manage.md` | Product / Card Ops |  |  | pending |
| BR-CARD-010 | 卡申请是否需要活体/人脸验证？验证过期后是否需要重新验证？ | `user-facing/card-application-manage.md` | Product / Security |  |  | pending |
| BR-CARD-011 | 申请费是否从钱包余额扣除？扣费失败或余额不足的用户口径是什么？ | `user-facing/card-application-manage.md` | Card Ops / Finance Ops |  |  | pending |
| BR-CARD-012 | 卡申请失败后，已扣费用是否退款？退款到哪里？ | `user-facing/card-application-manage.md`, `faq/card-faq.md` | Card Ops / Finance Ops |  |  | pending |
| BR-CARD-013 | 卡冻结、关闭、补发、重开等操作是否支持？ | `user-facing/card-application-manage.md`, `agent-internal/card-playbook.md` | Card Ops / Support |  |  | pending |
| BR-CARD-014 | 卡激活是否需要输入实体卡后四位并设置 PIN？PIN 是 4 位还是 6 位？ | `user-facing/card-application-manage.md`, `faq/card-faq.md` | Card Ops / Product |  |  | pending |
| BR-CARD-015 | PIN 是否仅用于线下交易？是否可以直接对用户说明？ | `user-facing/card-application-manage.md` | Card Ops / Product |  |  | pending |
| BR-CARD-016 | 查看完整卡号、CVC、有效期是否需要身份验证？ | `user-facing/card-application-manage.md` | Security / Card Ops |  |  | pending |
| BR-CARD-017 | 卡交易失败、重复扣款、退款异常的标准处理口径是什么？ | `user-facing/card-application-manage.md`, `faq/card-faq.md` | Card Ops / Support |  |  | pending |
| BR-CARD-018 | 退款是否退回卡余额？是否不退 FX 费用和 Transaction Fee？ | `user-facing/card-application-manage.md`, `faq/card-faq.md` | Card Ops / Finance Ops |  |  | pending |
| BR-CARD-019 | 卡交易相关状态和卡状态的正式中文口径是什么？ | `user-facing/card-application-manage.md`, `agent-internal/card-playbook.md` | Card Ops / Product |  |  | pending |

## 5. Transaction History

| ID | Question | Impacted KB Files | Suggested Reviewer | Decision | Confirmed Answer / Rule | Status |
|---|---|---|---|---|---|---|
| BR-TXN-001 | 当前交易状态有哪些？pending / failed / completed 等正式中文口径是什么？ | `user-facing/transaction-history.md`, `faq/transaction-faq.md` | Product / Ops |  |  | pending |
| BR-TXN-002 | 钱包交易状态 Pending、Success、Refunded、Declined、Under Review、Cancelled 是否仍有效？ | `user-facing/transaction-history.md` | Wallet Ops / Product |  |  | pending |
| BR-TXN-003 | 卡交易状态 Pending、Success、Refunded、Declined 是否仍有效？ | `user-facing/transaction-history.md` | Card Ops / Product |  |  | pending |
| BR-TXN-004 | Deposit 结果页状态和 Swap 状态是否仍有效？ | `user-facing/transaction-history.md`, `user-facing/wallet-deposit-send-swap.md` | Wallet Ops / Product |  |  | pending |
| BR-TXN-005 | 全量交易是否聚合钱包交易、兑换记录和卡交易？ | `user-facing/transaction-history.md` | Product |  |  | pending |
| BR-TXN-006 | 当前交易记录可查询范围是否为近 1 年？卡交易单次查询最多 6 个月是否仍有效？ | `user-facing/transaction-history.md` | Product / Backend |  |  | pending |
| BR-TXN-007 | 交易记录是否支持筛选、搜索、导出？ | `user-facing/transaction-history.md` | Product |  |  | pending |
| BR-TXN-008 | 卡退款中的 REFUND / REVERSAL 是否都对客显示为退款？ | `user-facing/transaction-history.md`, `faq/transaction-faq.md` | Card Ops / Product |  |  | pending |
| BR-TXN-009 | 退款入账位置、手续费是否退还、到账时间是否有正式用户口径？ | `user-facing/transaction-history.md`, `faq/transaction-faq.md` | Card Ops / Finance Ops |  |  | pending |
| BR-TXN-010 | 数据异常 / 网络异常页面的正式用户提示文案是什么？ | `user-facing/transaction-history.md` | Product / Support |  |  | pending |

## 6. Notification / System Email

| ID | Question | Impacted KB Files | Suggested Reviewer | Decision | Confirmed Answer / Rule | Status |
|---|---|---|---|---|---|---|
| BR-NOTIF-001 | 当前支持哪些通知类型？交易、账户、系统、营销活动、身份安全等分类是否仍有效？ | `user-facing/notification-system-email.md`, `faq/notification-faq.md` | Product / CRM |  |  | pending |
| BR-NOTIF-002 | 用户是否可以关闭或管理通知？哪些通知类型可关闭，哪些必须保留？ | `user-facing/notification-system-email.md` | Product / Compliance / CRM |  |  | pending |
| BR-NOTIF-003 | App 内通知设置是否支持 Push、Email、SMS？ | `user-facing/notification-system-email.md` | Product / CRM |  |  | pending |
| BR-NOTIF-004 | 系统通知和营销通知是否有不同默认开启规则？ | `user-facing/notification-system-email.md` | CRM / Compliance |  |  | pending |
| BR-NOTIF-005 | 未读消息红点、数字展示、99+ 规则是否仍有效？一键已读是否上线？ | `user-facing/notification-system-email.md`, `faq/notification-faq.md` | Product / App |  |  | pending |
| BR-NOTIF-006 | 消息详情页是否支持跳转到交易详情或其他业务页？ | `user-facing/notification-system-email.md` | Product / App |  |  | pending |
| BR-NOTIF-007 | 系统邮件发送失败、收不到邮件时的标准排查口径是什么？ | `user-facing/notification-system-email.md`, `faq/notification-faq.md` | CRM / Support |  |  | pending |
| BR-NOTIF-008 | 官方邮件域名或识别方式是否有用户可见说明？ | `user-facing/notification-system-email.md`, `faq/notification-faq.md` | CRM / Security |  |  | pending |
| BR-NOTIF-009 | 系统邮件模板、logo、footer 是否仅内部使用？ | `agent-internal/notification-playbook.md` | CRM / Brand |  |  | pending |
| BR-NOTIF-010 | 用户 notification preference 对系统邮件、营销邮件、Push 的影响是否有客服口径？ | `user-facing/notification-system-email.md`, `agent-internal/notification-playbook.md` | CRM / Compliance |  |  | pending |

## 7. Website / FAQ

| ID | Question | Impacted KB Files | Suggested Reviewer | Decision | Confirmed Answer / Rule | Status |
|---|---|---|---|---|---|---|
| BR-WEB-001 | 官网 Waitlist 是否仍然有效？PC 和移动端是否都支持？ | `user-facing/website-faq.md`, `faq/website-faq.md` | Product / Growth |  |  | pending |
| BR-WEB-002 | Waitlist 是否只收集邮箱和国家/地区，是否还收集用户关注点？ | `user-facing/website-faq.md` | Growth / Product |  |  | pending |
| BR-WEB-003 | Waitlist 是否有奖励、邀请码、排名等机制？ | `user-facing/website-faq.md`, `faq/website-faq.md` | Growth / Legal |  |  | pending |
| BR-WEB-004 | Waitlist 是否存在重复提交限制、IP 频控或提交限制？是否可对用户说明？ | `user-facing/website-faq.md` | Growth / Security |  |  | pending |
| BR-WEB-005 | Waitlist 加入后的通知时间和方式是什么？ | `user-facing/website-faq.md`, `faq/website-faq.md` | Growth / CRM |  |  | pending |
| BR-WEB-006 | 官网 Get the App 下载入口当前是否已上线？下载二维码或应用商店链接是否有效？ | `user-facing/website-faq.md`, `faq/website-faq.md` | Product / Marketing |  |  | pending |
| BR-WEB-007 | 官网 Card / Wallet 页面展示的能力是否与 App 当前能力一致？ | `user-facing/website-faq.md` | Product / Marketing / Legal |  |  | pending |
| BR-WEB-008 | 官网提到的 Visa、Apple Pay、Google Pay、Samsung Pay、700+ wallets、150+ blockchains 等宣传语是否仍可确认？ | `user-facing/website-faq.md` | Product / Legal / Marketing |  |  | pending |
| BR-WEB-009 | 官网免责声明的正式中文客服口径是什么？ | `user-facing/website-faq.md`, `faq/website-faq.md` | Legal / Compliance |  |  | pending |
| BR-WEB-010 | 官网 Help Center / Zendesk 是否已上线？ | `user-facing/website-faq.md`, `user-facing/general-faq.md` | Support / Product |  |  | pending |

## 8. Review Progress Summary

| Area | Total Items | Applied | Pending |
|---|---:|---:|---:|
| Registration / Login | 10 | 0 | 10 |
| KYC / Identity Verification / Wallet Opening | 12 | 0 | 12 |
| Wallet Asset / Deposit / Send / Swap | 14 | 0 | 14 |
| Card Application / Manage / Transaction | 19 | 0 | 19 |
| Transaction History | 10 | 0 | 10 |
| Notification / System Email | 10 | 0 | 10 |
| Website / FAQ | 10 | 0 | 10 |
| **Total** | **85** | **0** | **85** |

## 9. Next Step After Confirmation

When a row is confirmed:

1. Update the relevant customer support KB file.
2. If user-facing, update `user-facing/` and `faq/`.
3. If internal only, update `agent-internal/`.
4. If not answerable, update `unresolved/do-not-answer.md`.
5. Update this checklist row to `applied`.
6. Update `customer-support-kb-task-board.md` changelog.
