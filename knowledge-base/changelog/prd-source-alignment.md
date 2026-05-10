---
module: knowledge-base
feature: prd-source-alignment
version: "2.1"
status: completed_pending_product_decision
source_doc: archive/legacy-prd/README.md；archive/legacy-prd/CONTENT_COMPARISON_REPORT.md；archive/legacy-prd/VALIDATION_REPORT.md
source_section: converted-prd full corpus
last_updated: 2026-05-09
owner: 吴忆锋
---

# PRD Source Alignment Task

目标：把 `knowledge-base/` 中的业务事实，严格校准到新转换的历史 PRD：`archive/legacy-prd/`。

## 原则

1. `archive/legacy-prd/` 是本轮知识库校准的证据层。
2. `knowledge-base/` 只保留能被 `archive/legacy-prd` 明确支持的事实。
3. 找不到历史 PRD 依据的内容，不直接删除；先标为 `NEED_CONFIRMATION` 或移入 `knowledge-gaps.md`。
4. 历史 PRD 之间冲突时，不自行判断当前规则；标为 `CONFLICT`，等待用户确认。
5. 官网 / Website / Marketing PRD 暂不进入 runtime knowledge-base，除非用户明确要求。
6. 每批更新后，必须更新本表状态。
7. 审计不能只看主 PRD；凡是业务链路依赖其他能力 PRD，必须同步纳入证据。例如注册登录涉及邮箱 OTP、密码、BIO、Face Auth、账户锁定等时，必须同时核对 `registration-login` 和 `security/identity-verification` 两份 converted-prd。
8. 必须做双向覆盖校验：不仅检查 `knowledge-base` 里的事实是否有证据，也要检查 converted-prd 证据里明确存在的关键规则是否已经进入对应知识库文件。证据有、知识库没有的关键规则，标为 `SOURCE_GAP` 并补充到知识库，或在确认为非 runtime 范围时标 `OUT_OF_SCOPE`。

## 证据使用规则

| 类型 | 说明 | 处理规则 |
|---|---|---|
| Primary evidence | 直接描述该业务模块的 PRD | 默认作为该知识库文件的主来源 |
| Supporting evidence | 被主链路调用或约束的能力 PRD | 必须同步核对，尤其是 Security、KYC、Wallet、Notification、OBOSS |
| Cross-module evidence | 另一个模块中定义了入口、状态、限制或异常文案 | 作为补充来源，需在知识库中标明来源 |
| Conflict evidence | 两份 PRD 对同一事实描述不一致 | 标 `CONFLICT`，不自行裁决 |
| Missing evidence | 知识库事实找不到 converted-prd 支持 | 标 `NEED_CONFIRMATION` |
| Source coverage gap | converted-prd 中有明确规则，但知识库未覆盖 | 标 `SOURCE_GAP`；若属于 runtime 知识，应补入知识库；若属于 Website/Marketing/废弃删除线等非 runtime 范围，标 `OUT_OF_SCOPE` 或 `NEED_CONFIRMATION` |

### 关键交叉证据

| 知识库域 | Primary evidence | Supporting evidence | 说明 |
|---|---|---|---|
| account / registration | `archive/legacy-prd/app/registration-login/README.md` | `archive/legacy-prd/security/identity-verification/README.md` | 注册页定义主流程；Security 定义 OTP、Face Auth、BIO、锁定、验证规则 |
| account / login | `archive/legacy-prd/app/registration-login/README.md` | `archive/legacy-prd/security/identity-verification/README.md` | 登录页定义入口和页面；Security 定义验证与锁定规则 |
| account / password-reset | `archive/legacy-prd/app/registration-login/README.md` | `archive/legacy-prd/security/identity-verification/README.md` | 忘记密码流程涉及 OTP、密码规则、Face Auth 等 |
| security | `archive/legacy-prd/security/identity-verification/README.md` | `archive/legacy-prd/app/registration-login/README.md` | Security 是能力 PRD；注册登录提供调用场景 |
| card application | `archive/legacy-prd/card/application/README.md` | `archive/legacy-prd/app/home/README.md`；`archive/legacy-prd/kyc/wallet-opening/README.md`；`archive/legacy-prd/security/identity-verification/README.md` | 申卡入口在 Home；申卡前置依赖钱包开户/KYC、Face Auth |
| wallet deposit/send/swap | `archive/legacy-prd/wallet/deposit-send-swap/README.md` | `archive/legacy-prd/security/identity-verification/README.md`；`archive/legacy-prd/kyc/wallet-opening/README.md`；`archive/legacy-prd/app/transaction-history/README.md` | 转账/兑换涉及身份验证、钱包开户、交易记录 |
| transaction | `archive/legacy-prd/app/transaction-history/README.md` | `archive/legacy-prd/card/transaction/README.md`；`archive/legacy-prd/wallet/deposit-send-swap/README.md` | 全量交易整合 Wallet / Card / Swap 等来源 |
| notification | `archive/legacy-prd/notification/push-inbox/README.md` | `archive/legacy-prd/notification/system-email/README.md`；业务触发 PRD | Push、站内信、系统邮件分别核对 |

## 状态说明

| 状态 | 含义 |
|---|---|
| TODO | 待审计 |
| AUDITING | 审计中 |
| ALIGNED | 已按 converted-prd 校准 |
| NEED_CONFIRMATION | 知识库事实与历史 PRD 不完全一致，或历史 PRD 无明确依据 |
| CONFLICT | 多份历史 PRD 之间存在冲突 |
| OUT_OF_SCOPE | 不纳入 runtime knowledge-base |
| SOURCE_GAP | converted-prd 证据中有关键规则，但对应知识库文件尚未覆盖 |

## 双向覆盖校验清单

每个模块审计时必须同时完成两类检查：

| 检查方向 | 问题 | 结果处理 |
|---|---|---|
| KB → Evidence | 知识库里的事实是否能在 converted-prd 中找到明确依据？ | 找不到则标 `NEED_CONFIRMATION`，不得继续当作 confirmed fact |
| Evidence → KB | converted-prd 里的关键规则是否已经进入知识库？ | 未覆盖则标 `SOURCE_GAP`，并补入知识库或说明不纳入原因 |

Evidence → KB 至少要抽取并检查这些规则类型：

| 规则类型 | 例子 | 处理要求 |
|---|---|---|
| 流程 / 页面入口 | 注册、登录、申卡、充值、转账、交易详情入口 | 需进入对应模块主文档或索引 |
| 状态 / 状态流转 | Account Status、Card Status、Transaction Status、KYC Status | 需进入模块文档或 `_meta/status-dictionary.md` |
| 字段 / 输入规则 | Email、手机号、AIX Tag、密码、金额、币种、网络 | 需进入字段规则或对应页面规则 |
| 校验 / 频控 / 限制 | OTP 锁定、失败次数、冷却期、设备限制、国家隐藏规则 | 需进入模块规则或 Security / Common 规则 |
| 错误文案 | `Account locked...`、`Invalid OTP`、格式错误提示 | 需进入 `common/errors.md` 或对应页面规则 |
| 跨模块依赖 | KYC 前置、Face Auth、BIO、Notification、OBOSS | 需在主模块标明 supporting evidence |
| 删除线 / 废弃内容 | Word 转换中的 `<del>` 或 `~~...~~` | 不直接沉淀为 confirmed fact；标 `NEED_CONFIRMATION` 或说明历史废弃 |
| 待定事项 / TBD | PRD 的待定事项章节 | 不沉淀为 confirmed fact；进入待确认项 |

只有同时满足以下条件，任务才能标为 `ALIGNED`：

1. 该知识库文件中的关键事实都有 converted-prd 证据支持；
2. 对应 converted-prd 的关键 runtime 规则已被知识库覆盖；
3. 未覆盖的证据规则均已登记为 `SOURCE_GAP` / `OUT_OF_SCOPE` / `NEED_CONFIRMATION`；
4. 删除线、历史废弃、待定事项没有被错误沉淀为 confirmed fact。

## Source Corpus

| 域 | converted-prd 来源 |
|---|---|
| account / registration-login | `archive/legacy-prd/app/registration-login/README.md`；`archive/legacy-prd/security/identity-verification/README.md` |
| home | `archive/legacy-prd/app/home/README.md` |
| faq | `archive/legacy-prd/app/faq/README.md` |
| transaction-history | `archive/legacy-prd/app/transaction-history/README.md`；`archive/legacy-prd/card/transaction/README.md`；`archive/legacy-prd/wallet/deposit-send-swap/README.md` |
| card application | `archive/legacy-prd/card/application/README.md`；`archive/legacy-prd/app/home/README.md`；`archive/legacy-prd/kyc/wallet-opening/README.md`；`archive/legacy-prd/security/identity-verification/README.md` |
| card manage | `archive/legacy-prd/card/manage/README.md`；`archive/legacy-prd/security/identity-verification/README.md` |
| card transaction | `archive/legacy-prd/card/transaction/README.md`；`archive/legacy-prd/app/transaction-history/README.md` |
| common popup/banner | `archive/legacy-prd/common/popup-banner/README.md` |
| i18n | `archive/legacy-prd/common/i18n/README.md` |
| kyc | `archive/legacy-prd/kyc/wallet-opening/README.md` |
| mgm | `archive/legacy-prd/mgm/referral-invite-code/README.md`；`archive/legacy-prd/app/registration-login/README.md` |
| notification | `archive/legacy-prd/notification/push-inbox/README.md`；`archive/legacy-prd/notification/system-email/README.md` |
| oboss | `archive/legacy-prd/oboss/mvp/README.md`；`archive/legacy-prd/oboss/capabilities/README.md` |
| security | `archive/legacy-prd/security/identity-verification/README.md`；`archive/legacy-prd/app/registration-login/README.md` |
| wallet | `archive/legacy-prd/wallet/asset/README.md`；`archive/legacy-prd/wallet/deposit-send-swap/README.md`；`archive/legacy-prd/security/identity-verification/README.md`；`archive/legacy-prd/kyc/wallet-opening/README.md` |
| website | `archive/legacy-prd/website/**/README.md`，当前 OUT_OF_SCOPE |

## Alignment Tasks

| # | 状态 | knowledge-base 文件 | converted-prd 依据 | 备注 |
|---:|---|---|---|---|
| 1 | ALIGNED | `knowledge-base/account/_index.md` | `archive/legacy-prd/app/registration-login/README.md`；`archive/legacy-prd/security/identity-verification/README.md` | Account 索引已按删除线=已删除规则收口；Password Reset / Forgot Password 不纳入 runtime，Security 锁定独立维护 |
| 2 | ALIGNED | `knowledge-base/account/registration.md` | `archive/legacy-prd/app/registration-login/README.md`；`archive/legacy-prd/security/identity-verification/README.md` | registration.md 已按 registration-login + security 证据校准；Locked 不作为账户状态沉淀 |
| 3 | ALIGNED | `knowledge-base/account/login.md` | `archive/legacy-prd/app/registration-login/README.md`；`archive/legacy-prd/security/identity-verification/README.md` | login.md 已按删除线=已删除规则收口；Forgot Password / Password Reset 不作为 active Login 入口 |
| 4 | OUT_OF_SCOPE | `knowledge-base/account/password-reset.md` | `archive/legacy-prd/app/registration-login/README.md`；`archive/legacy-prd/security/identity-verification/README.md` | password-reset.md 已改为 deleted_out_of_scope；源 PRD 删除线内容不纳入 runtime 逻辑 |
| 5 | ALIGNED | `knowledge-base/home/_index.md` | `archive/legacy-prd/app/home/README.md` | home/_index.md 已按 Home + FAQ 证据更新，明确首页查询入口与跨模块边界 |
| 6 | ALIGNED | `knowledge-base/home/app-home.md` | `archive/legacy-prd/app/home/README.md` | app-home.md 已补齐 Evidence→KB 缺口：钱包状态、申卡入口、卡片展示、FAQ、核心交易入口、刷新规则 |
| 7 | ALIGNED | `knowledge-base/common/faq.md` | `archive/legacy-prd/app/faq/README.md` | common/faq.md 已按 converted FAQ 全量重写：FAQ 展示规则、Zendesk Section、场景入口、首页/申卡 FAQ 已收口 |
| 8 | ALIGNED | `knowledge-base/transaction/_index.md` | `archive/legacy-prd/app/transaction-history/README.md`；`archive/legacy-prd/card/transaction/README.md`；`archive/legacy-prd/wallet/deposit-send-swap/README.md` | transaction/_index.md 已按三份 converted-prd 更新证据范围和补齐规则索引 |
| 9 | ALIGNED | `knowledge-base/transaction/history.md` | `archive/legacy-prd/app/transaction-history/README.md`；`archive/legacy-prd/card/transaction/README.md`；`archive/legacy-prd/wallet/deposit-send-swap/README.md` | history.md 已补齐全量交易聚合、去搜索、过滤类型、REVERSAL退款、异常文案、时间分组 |
| 10 | ALIGNED | `knowledge-base/transaction/detail.md` | `archive/legacy-prd/app/transaction-history/README.md`；`archive/legacy-prd/card/transaction/README.md`；`archive/legacy-prd/wallet/deposit-send-swap/README.md` | detail.md 已补齐 Card/Crypto/Swap 详情差异、Gas fee隐藏、Exchange rate展示和可选字段隐藏 |
| 11 | ALIGNED | `knowledge-base/transaction/status-model.md` | `archive/legacy-prd/app/transaction-history/README.md`；`archive/legacy-prd/card/transaction/README.md`；`archive/legacy-prd/wallet/deposit-send-swap/README.md` | status-model.md 已补齐全量交易类型/状态、原始类型展示范围和 REVERSAL 退款处理 |
| 12 | ALIGNED | `knowledge-base/card/_index.md` | `archive/legacy-prd/card/application/README.md`；`archive/legacy-prd/card/manage/README.md`；`archive/legacy-prd/card/transaction/README.md`；`archive/legacy-prd/security/identity-verification/README.md` | card/_index.md 已更新 converted-prd 证据范围，并登记 Card Home 跨文档冲突 |
| 13 | ALIGNED | `knowledge-base/card/application.md` | `archive/legacy-prd/card/application/README.md`；`archive/legacy-prd/app/home/README.md`；`archive/legacy-prd/kyc/wallet-opening/README.md`；`archive/legacy-prd/security/identity-verification/README.md` | application.md 已补齐申卡资格、入口、费用、多币种支付、Face Auth、Billing/Mailing、MGM减免费、结果页等规则 |
| 14 | CONFLICT | `knowledge-base/card/card-home.md` | `archive/legacy-prd/app/home/README.md`；`archive/legacy-prd/card/application/README.md`；`archive/legacy-prd/card/manage/README.md` | card-home.md 已补齐展示规则，但 Home PRD 与 Card Application PRD 对部分首页卡片点击跳转存在冲突，待产品确认 |
| 15 | ALIGNED | `knowledge-base/card/manage/_index.md` | `archive/legacy-prd/card/manage/README.md`；`archive/legacy-prd/security/identity-verification/README.md` | Card Manage index 已补齐激活/PIN/敏感信息/状态操作证据索引和 Security 支撑边界 |
| 16 | ALIGNED | `knowledge-base/card/manage/activation.md` | `archive/legacy-prd/card/manage/README.md`；`archive/legacy-prd/security/identity-verification/README.md` | activation.md 已补齐后四位校验、激活成功 toast、失败页、接口路径和 autoDebit 删除线边界 |
| 17 | ALIGNED | `knowledge-base/card/manage/pin.md` | `archive/legacy-prd/card/manage/README.md`；`archive/legacy-prd/security/identity-verification/README.md` | pin.md 已补齐 6 位 PIN、引导弹窗、Confirm PIN、AAI 后 set/reset、公钥接口、31031、PIN 简单规则 |
| 18 | ALIGNED | `knowledge-base/card/manage/sensitive-info.md` | `archive/legacy-prd/card/manage/README.md`；`archive/legacy-prd/security/identity-verification/README.md` | sensitive-info.md 已补齐 Basic/Sensitive Info 字段来源、复制 toast、接口失败 toast |
| 19 | ALIGNED | `knowledge-base/card/manage/status-and-operations.md` | `archive/legacy-prd/card/manage/README.md` | status-and-operations.md 已补齐 Freeze/Unfreeze、网络/服务端错误、Lock/Unlock 文案和接口路径 |
| 20 | ALIGNED | `knowledge-base/card/transaction.md` | `archive/legacy-prd/card/transaction/README.md`；`archive/legacy-prd/app/transaction-history/README.md` | card/transaction.md 已补齐 DTC 通知、资金回退、REVERSAL type=19、展示范围、异常文案 |
| 21 | ALIGNED | `knowledge-base/card/transaction-detail.md` | `archive/legacy-prd/card/transaction/README.md`；`archive/legacy-prd/app/transaction-history/README.md` | card/transaction-detail.md 已补齐 Card History/Details、去搜索、状态说明、Exchange rate、可选字段隐藏和 DTC 未知错误处理 |
| 22 | ALIGNED | `knowledge-base/wallet/_index.md` | `archive/legacy-prd/wallet/asset/README.md`；`archive/legacy-prd/wallet/deposit-send-swap/README.md`；`archive/legacy-prd/kyc/wallet-opening/README.md`；`archive/legacy-prd/security/identity-verification/README.md` | wallet/_index.md 已更新 Wallet Asset + Deposit/Send/Swap + KYC/Security/Transaction 证据边界，并登记 Send/Swap 缺口 |
| 23 | ALIGNED | `knowledge-base/wallet/assets.md` | `archive/legacy-prd/wallet/asset/README.md`；`archive/legacy-prd/wallet/deposit-send-swap/README.md`；`archive/legacy-prd/kyc/wallet-opening/README.md` | assets.md 已补齐稳定币范围、Total Asset、汇率异常、排序、隐藏余额、Recent transaction、Withdraw隐藏 |
| 24 | ALIGNED | `knowledge-base/wallet/deposit.md` | `archive/legacy-prd/wallet/deposit-send-swap/README.md`；`archive/legacy-prd/security/identity-verification/README.md`；`archive/legacy-prd/kyc/wallet-opening/README.md`；`archive/legacy-prd/app/transaction-history/README.md` | deposit.md 只承接 Deposit/GTR/WalletConnect；已新增 wallet/send.md 和 wallet/swap.md 收口 Send/Swap SOURCE_GAP |
| 25 | ALIGNED | `knowledge-base/kyc/_index.md` | `archive/legacy-prd/kyc/wallet-opening/README.md`；`archive/legacy-prd/app/home/README.md` | kyc/_index.md 已按 KYC + Home + Card Application + Security converted-prd 更新证据边界 |
| 26 | ALIGNED | `knowledge-base/kyc/account-opening.md` | `archive/legacy-prd/kyc/wallet-opening/README.md`；`archive/legacy-prd/app/home/README.md`；`archive/legacy-prd/card/application/README.md` | account-opening.md 已补齐 Waitlist页面级拦截、Face 30秒超时、长期有效、Face锁定、Home钱包面板映射、申卡前置 |
| 27 | ALIGNED | `knowledge-base/security/_index.md` | `archive/legacy-prd/security/identity-verification/README.md`；`archive/legacy-prd/app/registration-login/README.md` | security/_index.md 已按 Security + Registration + Card Manage + Wallet converted-prd 更新证据边界和缺口索引 |
| 28 | ALIGNED | `knowledge-base/security/*.md` | `archive/legacy-prd/security/identity-verification/README.md`；`archive/legacy-prd/app/registration-login/README.md`；`archive/legacy-prd/card/manage/README.md`；`archive/legacy-prd/wallet/deposit-send-swap/README.md` | security/*.md 已补齐 BIO跳过认证、DeviceID、锁定矩阵、IVS有效期、验证码重发冷却、设备绑定、Quick Login BIO处理、API/密码规则等 |
| 29 | ALIGNED | `knowledge-base/common/notification.md` | `archive/legacy-prd/notification/push-inbox/README.md`；`archive/legacy-prd/notification/system-email/README.md`；相关业务触发 PRD | common/notification.md 已重写为 Notification 公共能力文档，覆盖 Push、消息中心、通知设置、Webhook、System Email 边界 |
| 30 | ALIGNED | `knowledge-base/common/errors.md` | 多份 converted-prd 中的错误码 / 文案 | common/errors.md 已重写为统一错误字典，覆盖已校准模块的错误文案、toast、popup、failed page 和异常边界 |
| 31 | ALIGNED | `knowledge-base/_meta/*.md` | 多份 converted-prd | _meta/*.md 已重写为状态、字段、限制、地区、合规、错误码、术语字典，SOURCE_GAP 收口 |
| 32 | OUT_OF_SCOPE | Website / Marketing facts | `archive/legacy-prd/website/**/README.md` | 当前 runtime KB 明确排除 website |

## Progress

| 指标 | 数量 |
|---|---:|
| 总任务 | 32 |
| ALIGNED | 29 |
| NEED_CONFIRMATION | 0 |
| CONFLICT | 1 |
| SOURCE_GAP | 0 |
| TODO | 0 |
| OUT_OF_SCOPE | 2 |

## Batch Notes

- 2026-05-09：按用户确认更新删除线规则：删除线内容等同已删除。Account index 和 login 改为 ALIGNED；password-reset 改为 OUT_OF_SCOPE / deleted_out_of_scope；NEED_CONFIRMATION 归零。

- 2026-05-09：收口 _meta SOURCE_GAP。7 个 _meta 文件重写为状态、字段、限制、地区、合规、错误码、术语字典，任务 31 改为 ALIGNED。SOURCE_GAP 归零；剩余 NEED_CONFIRMATION / CONFLICT 为源证据待确认项，不能强行裁决。

- 2026-05-09：收口 common/notification SOURCE_GAP。common/notification.md 重写为 Notification 公共能力文档，覆盖 Push、消息中心、通知设置、Webhook、System Email 边界，任务 29 改为 ALIGNED。

- 2026-05-09：收口 common/errors SOURCE_GAP。common/errors.md 重写为统一错误字典，覆盖 Account/Security/KYC/Card/Wallet/Transaction/Notification 的已确认错误文案、toast、popup、failed page 和异常边界，任务 30 改为 ALIGNED。

- 2026-05-09：收口 FAQ SOURCE_GAP。common/faq.md 按 archive/legacy-prd/app/faq/README.md 重写，旧 xlsx 不再作为主事实来源，任务 7 改为 ALIGNED。

- 2026-05-09：收口 Wallet SOURCE_GAP。新增 wallet/send.md 和 wallet/swap.md；wallet/deposit.md 改为只承接 Deposit/GTR/WalletConnect，任务 24 改为 ALIGNED。

- 2026-05-09：完成最终 TODO 批次。common/errors 和 _meta/*.md 标 SOURCE_GAP；已补本轮审计发现的高频错误、状态、字段、限制、国家/地区、合规边界、术语，但全量字典化仍需后续专项结构化。至此原 32 项任务无 TODO。

- 2026-05-09：完成 Notification 批次。common/notification.md 标 SOURCE_GAP；已补基础通知链路、Push规则、消息中心、通知设置、Webhook和System email边界，但全量模板、OBoss配置通知、Webhook全量事件、系统邮件模板实现仍需后续结构化。

- 2026-05-09：完成 Security 批次。security index 和 security/*.md 标 ALIGNED；补齐 BIO登录跳过认证、DeviceID、OTP/Email OTP/Passcode/Face锁定矩阵、IVS 10/5分钟有效期、验证码重发冷却与设备绑定、Quick Login BIO清理、API路径、密码策略等 Evidence→KB 缺口。

- 2026-05-09：完成 KYC 批次。kyc index / account-opening 标 ALIGNED；补齐 Waitlist 页面级拦截、Face Loading 30秒超时、申请单长期有效、Face 失败锁定、Home 钱包面板映射、Card 申卡前置依赖等 Evidence→KB 缺口。

- 2026-05-09：完成 Wallet 批次。wallet index / assets 标 ALIGNED；deposit 标 SOURCE_GAP，原因是 Deposit 已补齐但源 PRD 中 Send / Swap 完整流程尚未沉淀为独立 KB。

- 2026-05-09：完成 Card Transaction 批次。card/transaction 和 card/transaction-detail 标 ALIGNED；补齐 DTC 通知、REVERSAL type=19、卡交易展示范围、去搜索、Exchange rate、DTC未知错误处理等规则。

- 2026-05-09：完成 Card Manage 批次。manage index / activation / pin / sensitive-info / status-and-operations 标 ALIGNED；补齐激活、6位PIN、公钥、31031、敏感信息、Freeze/Unfreeze、网络/服务端错误等 Evidence→KB 缺口。

- 2026-05-09：完成 Card Application / Card Home 第一段。card index 和 application 标 ALIGNED；card-home 标 CONFLICT，原因是 Home PRD 与 Card Application PRD 对 Processing、Pending activation、Active 未设置 PIN、Frozen 的首页点击跳转存在冲突。

- 2026-05-09：完成 Transaction 批次。transaction index/history/detail/status-model 标 ALIGNED；补齐全量交易去搜索、REVERSAL 退款、Gas fee 隐藏、Exchange rate、异常文案、原始类型展示范围等 Evidence→KB 缺口。

- 2026-05-09：完成 Home + FAQ 批次。Home index/app-home 标 ALIGNED；FAQ 标 SOURCE_GAP，原因是 converted FAQ 与旧 xlsx FAQ 口径不一致，需按 converted-prd 单独重写。

- 2026-05-09：创建本审计任务表。下一步从 account 模块开始校准。
- 2026-05-09：补充交叉证据规则。Account / Registration / Login / Password Reset 不能只看注册登录 PRD，必须同时核对 Security 身份认证 PRD；后续 Card / Wallet / Transaction / Notification 同理按主证据 + 支撑证据执行。
- 2026-05-09：完成 account 第一批校准：registration 标 ALIGNED；account index / login / password-reset 标 NEED_CONFIRMATION，原因是 Login 输入方式和 Password Reset 入口在 converted-prd 中存在删除线或证据不完整。
- 2026-05-09：补充双向覆盖校验规则。后续每个模块必须同时检查 KB → Evidence 和 Evidence → KB，防止“知识库有但无证据”和“证据有但知识库漏写”两类问题。

## Final Completion Boundary

- 2026-05-09：已完成所有可执行的 PRD source alignment 工作。TODO=0，SOURCE_GAP=0。
- 删除线内容已按用户确认视为删除并从 runtime 逻辑排除；剩余 CONFLICT 是 active PRD 互相冲突导致，已单独整理到 `knowledge-base/changelog/prd-source-confirmation-needed.md`。
- 在产品裁决前，不得强行裁决 Card Home 冲突。
