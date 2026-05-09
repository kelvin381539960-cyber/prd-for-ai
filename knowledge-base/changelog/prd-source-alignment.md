---
module: knowledge-base
feature: prd-source-alignment
version: "1.1"
status: active
source_doc: archive/converted-prd/README.md；archive/converted-prd/CONTENT_COMPARISON_REPORT.md；archive/converted-prd/VALIDATION_REPORT.md
source_section: converted-prd full corpus
last_updated: 2026-05-09
owner: 吴忆锋
---

# PRD Source Alignment Task

目标：把 `knowledge-base/` 中的业务事实，严格校准到新转换的历史 PRD：`archive/converted-prd/`。

## 原则

1. `archive/converted-prd/` 是本轮知识库校准的证据层。
2. `knowledge-base/` 只保留能被 `archive/converted-prd` 明确支持的事实。
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
| account / registration | `archive/converted-prd/app/registration-login/README.md` | `archive/converted-prd/security/identity-verification/README.md` | 注册页定义主流程；Security 定义 OTP、Face Auth、BIO、锁定、验证规则 |
| account / login | `archive/converted-prd/app/registration-login/README.md` | `archive/converted-prd/security/identity-verification/README.md` | 登录页定义入口和页面；Security 定义验证与锁定规则 |
| account / password-reset | `archive/converted-prd/app/registration-login/README.md` | `archive/converted-prd/security/identity-verification/README.md` | 忘记密码流程涉及 OTP、密码规则、Face Auth 等 |
| security | `archive/converted-prd/security/identity-verification/README.md` | `archive/converted-prd/app/registration-login/README.md` | Security 是能力 PRD；注册登录提供调用场景 |
| card application | `archive/converted-prd/card/application/README.md` | `archive/converted-prd/app/home/README.md`；`archive/converted-prd/kyc/wallet-opening/README.md`；`archive/converted-prd/security/identity-verification/README.md` | 申卡入口在 Home；申卡前置依赖钱包开户/KYC、Face Auth |
| wallet deposit/send/swap | `archive/converted-prd/wallet/deposit-send-swap/README.md` | `archive/converted-prd/security/identity-verification/README.md`；`archive/converted-prd/kyc/wallet-opening/README.md`；`archive/converted-prd/app/transaction-history/README.md` | 转账/兑换涉及身份验证、钱包开户、交易记录 |
| transaction | `archive/converted-prd/app/transaction-history/README.md` | `archive/converted-prd/card/transaction/README.md`；`archive/converted-prd/wallet/deposit-send-swap/README.md` | 全量交易整合 Wallet / Card / Swap 等来源 |
| notification | `archive/converted-prd/notification/push-inbox/README.md` | `archive/converted-prd/notification/system-email/README.md`；业务触发 PRD | Push、站内信、系统邮件分别核对 |

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
| account / registration-login | `archive/converted-prd/app/registration-login/README.md`；`archive/converted-prd/security/identity-verification/README.md` |
| home | `archive/converted-prd/app/home/README.md` |
| faq | `archive/converted-prd/app/faq/README.md` |
| transaction-history | `archive/converted-prd/app/transaction-history/README.md`；`archive/converted-prd/card/transaction/README.md`；`archive/converted-prd/wallet/deposit-send-swap/README.md` |
| card application | `archive/converted-prd/card/application/README.md`；`archive/converted-prd/app/home/README.md`；`archive/converted-prd/kyc/wallet-opening/README.md`；`archive/converted-prd/security/identity-verification/README.md` |
| card manage | `archive/converted-prd/card/manage/README.md`；`archive/converted-prd/security/identity-verification/README.md` |
| card transaction | `archive/converted-prd/card/transaction/README.md`；`archive/converted-prd/app/transaction-history/README.md` |
| common popup/banner | `archive/converted-prd/common/popup-banner/README.md` |
| i18n | `archive/converted-prd/common/i18n/README.md` |
| kyc | `archive/converted-prd/kyc/wallet-opening/README.md` |
| mgm | `archive/converted-prd/mgm/referral-invite-code/README.md`；`archive/converted-prd/app/registration-login/README.md` |
| notification | `archive/converted-prd/notification/push-inbox/README.md`；`archive/converted-prd/notification/system-email/README.md` |
| oboss | `archive/converted-prd/oboss/mvp/README.md`；`archive/converted-prd/oboss/capabilities/README.md` |
| security | `archive/converted-prd/security/identity-verification/README.md`；`archive/converted-prd/app/registration-login/README.md` |
| wallet | `archive/converted-prd/wallet/asset/README.md`；`archive/converted-prd/wallet/deposit-send-swap/README.md`；`archive/converted-prd/security/identity-verification/README.md`；`archive/converted-prd/kyc/wallet-opening/README.md` |
| website | `archive/converted-prd/website/**/README.md`，当前 OUT_OF_SCOPE |

## Alignment Tasks

| # | 状态 | knowledge-base 文件 | converted-prd 依据 | 备注 |
|---:|---|---|---|---|
| 1 | NEED_CONFIRMATION | `knowledge-base/account/_index.md` | `archive/converted-prd/app/registration-login/README.md`；`archive/converted-prd/security/identity-verification/README.md` | Account 索引已更新；Login / Password Reset 因删除线或证据不完整同步标待确认 |
| 2 | ALIGNED | `knowledge-base/account/registration.md` | `archive/converted-prd/app/registration-login/README.md`；`archive/converted-prd/security/identity-verification/README.md` | registration.md 已按 registration-login + security 证据校准；Locked 不作为账户状态沉淀 |
| 3 | NEED_CONFIRMATION | `knowledge-base/account/login.md` | `archive/converted-prd/app/registration-login/README.md`；`archive/converted-prd/security/identity-verification/README.md` | login.md 已更新来源与风险说明；Email/Phone 输入范围、Forgot password 入口需确认 |
| 4 | NEED_CONFIRMATION | `knowledge-base/account/password-reset.md` | `archive/converted-prd/app/registration-login/README.md`；`archive/converted-prd/security/identity-verification/README.md` | password-reset.md 已重写为待确认；7.3 忘记密码正文为删除线，不能作为 active runtime fact |
| 5 | ALIGNED | `knowledge-base/home/_index.md` | `archive/converted-prd/app/home/README.md` | home/_index.md 已按 Home + FAQ 证据更新，明确首页查询入口与跨模块边界 |
| 6 | ALIGNED | `knowledge-base/home/app-home.md` | `archive/converted-prd/app/home/README.md` | app-home.md 已补齐 Evidence→KB 缺口：钱包状态、申卡入口、卡片展示、FAQ、核心交易入口、刷新规则 |
| 7 | SOURCE_GAP | `knowledge-base/common/faq.md` | `archive/converted-prd/app/faq/README.md` | common/faq.md 已登记 SOURCE_GAP：converted FAQ 与旧 xlsx FAQ 口径不一致，需后续按 converted-prd 全量重写 |
| 8 | ALIGNED | `knowledge-base/transaction/_index.md` | `archive/converted-prd/app/transaction-history/README.md`；`archive/converted-prd/card/transaction/README.md`；`archive/converted-prd/wallet/deposit-send-swap/README.md` | transaction/_index.md 已按三份 converted-prd 更新证据范围和补齐规则索引 |
| 9 | ALIGNED | `knowledge-base/transaction/history.md` | `archive/converted-prd/app/transaction-history/README.md`；`archive/converted-prd/card/transaction/README.md`；`archive/converted-prd/wallet/deposit-send-swap/README.md` | history.md 已补齐全量交易聚合、去搜索、过滤类型、REVERSAL退款、异常文案、时间分组 |
| 10 | ALIGNED | `knowledge-base/transaction/detail.md` | `archive/converted-prd/app/transaction-history/README.md`；`archive/converted-prd/card/transaction/README.md`；`archive/converted-prd/wallet/deposit-send-swap/README.md` | detail.md 已补齐 Card/Crypto/Swap 详情差异、Gas fee隐藏、Exchange rate展示和可选字段隐藏 |
| 11 | ALIGNED | `knowledge-base/transaction/status-model.md` | `archive/converted-prd/app/transaction-history/README.md`；`archive/converted-prd/card/transaction/README.md`；`archive/converted-prd/wallet/deposit-send-swap/README.md` | status-model.md 已补齐全量交易类型/状态、原始类型展示范围和 REVERSAL 退款处理 |
| 12 | ALIGNED | `knowledge-base/card/_index.md` | `archive/converted-prd/card/application/README.md`；`archive/converted-prd/card/manage/README.md`；`archive/converted-prd/card/transaction/README.md`；`archive/converted-prd/security/identity-verification/README.md` | card/_index.md 已更新 converted-prd 证据范围，并登记 Card Home 跨文档冲突 |
| 13 | ALIGNED | `knowledge-base/card/application.md` | `archive/converted-prd/card/application/README.md`；`archive/converted-prd/app/home/README.md`；`archive/converted-prd/kyc/wallet-opening/README.md`；`archive/converted-prd/security/identity-verification/README.md` | application.md 已补齐申卡资格、入口、费用、多币种支付、Face Auth、Billing/Mailing、MGM减免费、结果页等规则 |
| 14 | CONFLICT | `knowledge-base/card/card-home.md` | `archive/converted-prd/app/home/README.md`；`archive/converted-prd/card/application/README.md`；`archive/converted-prd/card/manage/README.md` | card-home.md 已补齐展示规则，但 Home PRD 与 Card Application PRD 对部分首页卡片点击跳转存在冲突，待产品确认 |
| 15 | TODO | `knowledge-base/card/manage/_index.md` | `archive/converted-prd/card/manage/README.md`；`archive/converted-prd/security/identity-verification/README.md` | 卡管索引 |
| 16 | TODO | `knowledge-base/card/manage/activation.md` | `archive/converted-prd/card/manage/README.md`；`archive/converted-prd/security/identity-verification/README.md` | 激活；如涉及 OTP/Face/BIO 需看 Security |
| 17 | TODO | `knowledge-base/card/manage/pin.md` | `archive/converted-prd/card/manage/README.md`；`archive/converted-prd/security/identity-verification/README.md` | PIN；如涉及验证需看 Security |
| 18 | TODO | `knowledge-base/card/manage/sensitive-info.md` | `archive/converted-prd/card/manage/README.md`；`archive/converted-prd/security/identity-verification/README.md` | 敏感信息；身份验证必须同步看 Security |
| 19 | TODO | `knowledge-base/card/manage/status-and-operations.md` | `archive/converted-prd/card/manage/README.md` | 状态和操作 |
| 20 | TODO | `knowledge-base/card/transaction.md` | `archive/converted-prd/card/transaction/README.md`；`archive/converted-prd/app/transaction-history/README.md` | 卡交易 |
| 21 | TODO | `knowledge-base/card/transaction-detail.md` | `archive/converted-prd/card/transaction/README.md`；`archive/converted-prd/app/transaction-history/README.md` | 卡交易详情 |
| 22 | TODO | `knowledge-base/wallet/_index.md` | `archive/converted-prd/wallet/asset/README.md`；`archive/converted-prd/wallet/deposit-send-swap/README.md`；`archive/converted-prd/kyc/wallet-opening/README.md`；`archive/converted-prd/security/identity-verification/README.md` | 钱包索引 |
| 23 | TODO | `knowledge-base/wallet/assets.md` | `archive/converted-prd/wallet/asset/README.md`；`archive/converted-prd/wallet/deposit-send-swap/README.md`；`archive/converted-prd/kyc/wallet-opening/README.md` | 钱包资产 |
| 24 | TODO | `knowledge-base/wallet/deposit.md` | `archive/converted-prd/wallet/deposit-send-swap/README.md`；`archive/converted-prd/security/identity-verification/README.md`；`archive/converted-prd/kyc/wallet-opening/README.md`；`archive/converted-prd/app/transaction-history/README.md` | 充值 / 转账 / 兑换；需核对身份验证与交易记录 |
| 25 | TODO | `knowledge-base/kyc/_index.md` | `archive/converted-prd/kyc/wallet-opening/README.md`；`archive/converted-prd/app/home/README.md` | KYC 索引 |
| 26 | TODO | `knowledge-base/kyc/account-opening.md` | `archive/converted-prd/kyc/wallet-opening/README.md`；`archive/converted-prd/app/home/README.md`；`archive/converted-prd/card/application/README.md` | 钱包开户 / KYC；卡申请前置也要核对 |
| 27 | TODO | `knowledge-base/security/_index.md` | `archive/converted-prd/security/identity-verification/README.md`；`archive/converted-prd/app/registration-login/README.md` | Security 索引 |
| 28 | TODO | `knowledge-base/security/*.md` | `archive/converted-prd/security/identity-verification/README.md`；`archive/converted-prd/app/registration-login/README.md`；`archive/converted-prd/card/manage/README.md`；`archive/converted-prd/wallet/deposit-send-swap/README.md` | OTP / BIO / Face / Password；需看调用场景 |
| 29 | TODO | `knowledge-base/common/notification.md` | `archive/converted-prd/notification/push-inbox/README.md`；`archive/converted-prd/notification/system-email/README.md`；相关业务触发 PRD | 通知 / 邮件；触发场景需回看业务 PRD |
| 30 | TODO | `knowledge-base/common/errors.md` | 多份 converted-prd 中的错误码 / 文案 | 错误文案字典 |
| 31 | TODO | `knowledge-base/_meta/*.md` | 多份 converted-prd | 状态、字段、限制、地区等字典 |
| 32 | OUT_OF_SCOPE | Website / Marketing facts | `archive/converted-prd/website/**/README.md` | 当前 runtime KB 明确排除 website |

## Progress

| 指标 | 数量 |
|---|---:|
| 总任务 | 32 |
| ALIGNED | 9 |
| NEED_CONFIRMATION | 3 |
| CONFLICT | 1 |
| SOURCE_GAP | 1 |
| TODO | 17 |
| OUT_OF_SCOPE | 1 |

## Batch Notes

- 2026-05-09：完成 Card Application / Card Home 第一段。card index 和 application 标 ALIGNED；card-home 标 CONFLICT，原因是 Home PRD 与 Card Application PRD 对 Processing、Pending activation、Active 未设置 PIN、Frozen 的首页点击跳转存在冲突。

- 2026-05-09：完成 Transaction 批次。transaction index/history/detail/status-model 标 ALIGNED；补齐全量交易去搜索、REVERSAL 退款、Gas fee 隐藏、Exchange rate、异常文案、原始类型展示范围等 Evidence→KB 缺口。

- 2026-05-09：完成 Home + FAQ 批次。Home index/app-home 标 ALIGNED；FAQ 标 SOURCE_GAP，原因是 converted FAQ 与旧 xlsx FAQ 口径不一致，需按 converted-prd 单独重写。

- 2026-05-09：创建本审计任务表。下一步从 account 模块开始校准。
- 2026-05-09：补充交叉证据规则。Account / Registration / Login / Password Reset 不能只看注册登录 PRD，必须同时核对 Security 身份认证 PRD；后续 Card / Wallet / Transaction / Notification 同理按主证据 + 支撑证据执行。
- 2026-05-09：完成 account 第一批校准：registration 标 ALIGNED；account index / login / password-reset 标 NEED_CONFIRMATION，原因是 Login 输入方式和 Password Reset 入口在 converted-prd 中存在删除线或证据不完整。
- 2026-05-09：补充双向覆盖校验规则。后续每个模块必须同时检查 KB → Evidence 和 Evidence → KB，防止“知识库有但无证据”和“证据有但知识库漏写”两类问题。
