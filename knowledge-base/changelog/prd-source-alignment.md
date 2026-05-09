---
module: knowledge-base
feature: prd-source-alignment
version: "1.0"
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

## 状态说明

| 状态 | 含义 |
|---|---|
| TODO | 待审计 |
| AUDITING | 审计中 |
| ALIGNED | 已按 converted-prd 校准 |
| NEED_CONFIRMATION | 知识库事实与历史 PRD 不完全一致，或历史 PRD 无明确依据 |
| CONFLICT | 多份历史 PRD 之间存在冲突 |
| OUT_OF_SCOPE | 不纳入 runtime knowledge-base |

## Source Corpus

| 域 | converted-prd 来源 |
|---|---|
| account / registration-login | `archive/converted-prd/app/registration-login/README.md` |
| home | `archive/converted-prd/app/home/README.md` |
| faq | `archive/converted-prd/app/faq/README.md` |
| transaction-history | `archive/converted-prd/app/transaction-history/README.md` |
| card application | `archive/converted-prd/card/application/README.md` |
| card manage | `archive/converted-prd/card/manage/README.md` |
| card transaction | `archive/converted-prd/card/transaction/README.md` |
| common popup/banner | `archive/converted-prd/common/popup-banner/README.md` |
| i18n | `archive/converted-prd/common/i18n/README.md` |
| kyc | `archive/converted-prd/kyc/wallet-opening/README.md` |
| mgm | `archive/converted-prd/mgm/referral-invite-code/README.md` |
| notification | `archive/converted-prd/notification/push-inbox/README.md`；`archive/converted-prd/notification/system-email/README.md` |
| oboss | `archive/converted-prd/oboss/mvp/README.md`；`archive/converted-prd/oboss/capabilities/README.md` |
| security | `archive/converted-prd/security/identity-verification/README.md` |
| wallet | `archive/converted-prd/wallet/asset/README.md`；`archive/converted-prd/wallet/deposit-send-swap/README.md` |
| website | `archive/converted-prd/website/**/README.md`，当前 OUT_OF_SCOPE |

## Alignment Tasks

| # | 状态 | knowledge-base 文件 | converted-prd 依据 | 备注 |
|---:|---|---|---|---|
| 1 | TODO | `knowledge-base/account/_index.md` | `archive/converted-prd/app/registration-login/README.md` | 账户入口索引 |
| 2 | TODO | `knowledge-base/account/registration.md` | `archive/converted-prd/app/registration-login/README.md` | 注册 |
| 3 | TODO | `knowledge-base/account/login.md` | `archive/converted-prd/app/registration-login/README.md` | 登录 |
| 4 | TODO | `knowledge-base/account/password-reset.md` | `archive/converted-prd/app/registration-login/README.md` | 忘记密码 |
| 5 | TODO | `knowledge-base/home/_index.md` | `archive/converted-prd/app/home/README.md` | 首页索引 |
| 6 | TODO | `knowledge-base/home/app-home.md` | `archive/converted-prd/app/home/README.md` | 首页 |
| 7 | TODO | `knowledge-base/common/faq.md` | `archive/converted-prd/app/faq/README.md` | FAQ |
| 8 | TODO | `knowledge-base/transaction/_index.md` | `archive/converted-prd/app/transaction-history/README.md` | 交易索引 |
| 9 | TODO | `knowledge-base/transaction/history.md` | `archive/converted-prd/app/transaction-history/README.md` | 全量交易历史 |
| 10 | TODO | `knowledge-base/transaction/detail.md` | `archive/converted-prd/app/transaction-history/README.md` | 交易详情 |
| 11 | TODO | `knowledge-base/transaction/status-model.md` | `archive/converted-prd/app/transaction-history/README.md` | 交易状态 |
| 12 | TODO | `knowledge-base/card/_index.md` | `archive/converted-prd/card/application/README.md`；`archive/converted-prd/card/manage/README.md`；`archive/converted-prd/card/transaction/README.md` | Card 索引 |
| 13 | TODO | `knowledge-base/card/application.md` | `archive/converted-prd/card/application/README.md`；`archive/converted-prd/app/home/README.md` | 申卡 |
| 14 | TODO | `knowledge-base/card/card-home.md` | `archive/converted-prd/app/home/README.md`；`archive/converted-prd/card/application/README.md` | 卡入口 / 卡首页 |
| 15 | TODO | `knowledge-base/card/manage/_index.md` | `archive/converted-prd/card/manage/README.md` | 卡管索引 |
| 16 | TODO | `knowledge-base/card/manage/activation.md` | `archive/converted-prd/card/manage/README.md` | 激活 |
| 17 | TODO | `knowledge-base/card/manage/pin.md` | `archive/converted-prd/card/manage/README.md` | PIN |
| 18 | TODO | `knowledge-base/card/manage/sensitive-info.md` | `archive/converted-prd/card/manage/README.md` | 敏感信息 |
| 19 | TODO | `knowledge-base/card/manage/status-and-operations.md` | `archive/converted-prd/card/manage/README.md` | 状态和操作 |
| 20 | TODO | `knowledge-base/card/transaction.md` | `archive/converted-prd/card/transaction/README.md` | 卡交易 |
| 21 | TODO | `knowledge-base/card/transaction-detail.md` | `archive/converted-prd/card/transaction/README.md`；`archive/converted-prd/app/transaction-history/README.md` | 卡交易详情 |
| 22 | TODO | `knowledge-base/wallet/_index.md` | `archive/converted-prd/wallet/asset/README.md`；`archive/converted-prd/wallet/deposit-send-swap/README.md` | 钱包索引 |
| 23 | TODO | `knowledge-base/wallet/assets.md` | `archive/converted-prd/wallet/asset/README.md` | 钱包资产 |
| 24 | TODO | `knowledge-base/wallet/deposit.md` | `archive/converted-prd/wallet/deposit-send-swap/README.md` | 充值 / 转账 / 兑换 |
| 25 | TODO | `knowledge-base/kyc/_index.md` | `archive/converted-prd/kyc/wallet-opening/README.md` | KYC 索引 |
| 26 | TODO | `knowledge-base/kyc/account-opening.md` | `archive/converted-prd/kyc/wallet-opening/README.md` | 钱包开户 / KYC |
| 27 | TODO | `knowledge-base/security/_index.md` | `archive/converted-prd/security/identity-verification/README.md`；`archive/converted-prd/app/registration-login/README.md` | Security 索引 |
| 28 | TODO | `knowledge-base/security/*.md` | `archive/converted-prd/security/identity-verification/README.md`；`archive/converted-prd/app/registration-login/README.md` | OTP / BIO / Face / Password |
| 29 | TODO | `knowledge-base/common/notification.md` | `archive/converted-prd/notification/push-inbox/README.md`；`archive/converted-prd/notification/system-email/README.md` | 通知 / 邮件 |
| 30 | TODO | `knowledge-base/common/errors.md` | 多份 converted-prd 中的错误码 / 文案 | 错误文案字典 |
| 31 | TODO | `knowledge-base/_meta/*.md` | 多份 converted-prd | 状态、字段、限制、地区等字典 |
| 32 | OUT_OF_SCOPE | Website / Marketing facts | `archive/converted-prd/website/**/README.md` | 当前 runtime KB 明确排除 website |

## Progress

| 指标 | 数量 |
|---|---:|
| 总任务 | 32 |
| ALIGNED | 0 |
| NEED_CONFIRMATION | 0 |
| CONFLICT | 0 |
| TODO | 31 |
| OUT_OF_SCOPE | 1 |

## Batch Notes

- 2026-05-09：创建本审计任务表。下一步从 account 模块开始校准。
