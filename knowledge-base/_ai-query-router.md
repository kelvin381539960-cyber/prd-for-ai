---
module: knowledge-base
feature: ai-query-router
version: "2.1"
status: active
source_doc: knowledge-base/_system-boundary.md；knowledge-base/changelog/knowledge-gaps.md；knowledge-base/_kb-ingestion-process.md；knowledge-base/wallet/_index.md；knowledge-base/card/_index.md；knowledge-base/transaction/_index.md；knowledge-base/kyc/_index.md；knowledge-base/common/_index.md；knowledge-base/kyc/account-opening.md；用户确认结论 2026-05-02；用户确认结论 2026-05-03
source_section: runtime AI usage；query routing；fact source rules；system boundary usage；ALL-GAP usage；Account Opening / KYC routing；cross-module dependency routing；PRD and KB fact rules
last_updated: 2026-05-03
owner: 吴忆锋
---

# AI 查询路由表 / 使用态入口

## 1. 文档定位

本文档是 AIX 知识库的唯一 AI 日常入口。

AI 查询需求逻辑、写 PRD、判断系统边界、修改知识库时，默认先读本文，再按问题类型读取对应模块事实文件。

本文档只负责路由和使用规则，不新增业务事实，不替代模块事实文件，不替代 `knowledge-base/changelog/knowledge-gaps.md`，不替代 `knowledge-base/_system-boundary.md`。

## 2. 标准读取路径

```text
1. knowledge-base/_ai-query-router.md
2. 对应模块 _index.md
3. 对应模块事实文件
4. knowledge-base/changelog/knowledge-gaps.md
5. 如涉及责任边界，再读 knowledge-base/_system-boundary.md
6. 如需核验来源，再读历史 PRD / DTC / AAI / Notification 原文
```

默认不读取：

```text
IMPLEMENTATION_PLAN.md
*/stage-review.md
moved notice 文件
migrated-reference 文件
历史 checklist / review 类文件
changelog/final-repository-review.md
changelog/refinement-stage-review.md
kyc/wallet-kyc.md
```

### 2.1 跨模块依赖提示

AI 查询时，应先按用户问题定位主模块，但不得把跨模块问题简化成单文件问题。

以下问题必须联动读取多个模块：

| 问题类型 | 主事实文件 | 必须联动读取 |
|---|---|---|
| Deposit / 到账 / 风险拦截 / WalletConnect | `wallet/deposit.md` | `common/dtc.md`、`common/walletconnect.md`、`common/notification.md`、`common/errors.md`、`transaction/status-model.md`、`knowledge-gaps.md`、`_system-boundary.md` |
| KYC / Account Opening / Sub Account / 准入 | `kyc/account-opening.md` | `common/aai.md`、`common/dtc.md`、`common/notification.md`、`knowledge-gaps.md`、`_system-boundary.md` |
| Card 交易 / refund / reversal / 对账 | `card/card-transaction-flow.md` | `transaction/history.md`、`transaction/detail.md`、`transaction/reconciliation.md`、`common/errors.md`、`common/notification.md`、`knowledge-gaps.md`、`_system-boundary.md` |
| Transaction 状态 / ID 串联 / 资金追踪 | `transaction/status-model.md` 或 `transaction/reconciliation.md` | `transaction/history.md`、`transaction/detail.md`、`card/card-transaction-flow.md`、`wallet/deposit.md`、`knowledge-gaps.md`、`_system-boundary.md` |
| PRD 写作 / 知识库修改 | 对应模块事实文件 | `prd-template/standard-prd-template.md`、`knowledge-base/_kb-ingestion-process.md`、`knowledge-gaps.md`、必要时读 `_system-boundary.md` |

遇到以下问题时，必须额外读取 `knowledge-gaps.md` 与 `_system-boundary.md`：

- 状态是否等价
- 外部系统是否负责
- 通知是否代表成功
- 到账是否完成
- 风控拦截如何展示
- ID 是否能串联
- 能力是否 active
- 是否能写入 PRD / 知识库

禁止只读单一模块后直接得出跨系统结论。

## 3. 当前产品范围

AIX 当前知识库覆盖：

| 模块 | 范围 |
|---|---|
| Wallet | Balance、Deposit、Receive、Send 占位 |
| Card | Card Application、Card Home、Activation、PIN、Sensitive Info、Card Management、Card Transaction Flow |
| Transaction | History、Detail、Status Model、Reconciliation |
| KYC | Account Opening / KYC 开户、身份认证、Sub Account、业务准入边界 |
| Common | DTC、AAI、WalletConnect、Notification、Errors、FAQ |

## 4. Active / Deferred 能力

| 能力 | 当前状态 | 使用规则 |
|---|---|---|
| Wallet Balance | active | 读取 `wallet/balance.md` |
| Wallet Deposit | active | 读取 `wallet/deposit.md`；包含 GTR / Exchange 与 WalletConnect / Self-custodial Wallet |
| Wallet Receive | active / 基础版 | 读取 `wallet/receive.md`；未确认边界查 ALL-GAP |
| Wallet Send | deferred | 不写成当前 active 能力 |
| Wallet Swap | deferred | 不写成当前 active 能力 |
| Account Opening / KYC | active | 主事实源为 `kyc/account-opening.md` |
| Wallet Transaction History | active | 主事实源为 `transaction/history.md` |
| Card Transaction Flow | active / partial | 资金追踪与对账缺口查 `transaction/reconciliation.md` 与 ALL-GAP |
| DTC / AAI / WalletConnect | external dependency | 只记录 AIX 设计相关依赖边界，不维护供应商内部逻辑 |

## 5. 快速路由表

| 用户问题类型 | 必读文件 | 需要时再读 | 不应默认读 |
|---|---|---|---|
| 当前知识库如何使用 | `_ai-query-router.md` | 模块 `_index.md` | `IMPLEMENTATION_PLAN.md` |
| 系统责任 / 外部边界 | `_system-boundary.md` | 对应业务事实文件、`knowledge-gaps.md` | 供应商完整原文 |
| 待确认项 / 缺口 | `changelog/knowledge-gaps.md` | 对应模块事实文件 | 模块旧 checklist |
| Deposit 总逻辑 | `wallet/deposit.md` | `common/dtc.md`、`common/walletconnect.md`、`common/notification.md`、`common/errors.md`、`_system-boundary.md` | `wallet/receive.md` |
| GTR / Exchange 地址充值 | `wallet/deposit.md` | `transaction/history.md`、`common/dtc.md`、`knowledge-gaps.md`、`_system-boundary.md` | `common/walletconnect.md` |
| WalletConnect 充值 | `wallet/deposit.md`、`common/walletconnect.md` | `common/dtc.md`、`common/errors.md`、`common/notification.md`、`knowledge-gaps.md`、`_system-boundary.md` | DTC 完整接口说明书 |
| WalletConnect 白名单 / 授权 | `common/walletconnect.md`、`wallet/deposit.md` | `common/dtc.md`、`knowledge-gaps.md`、`_system-boundary.md` | migrated-reference 文件 |
| Risk Withheld / under review | `wallet/deposit.md`、`common/dtc.md`、`common/notification.md` | `transaction/status-model.md`、`knowledge-gaps.md`、`_system-boundary.md` | 直接映射 Wallet state |
| Wallet Balance | `wallet/balance.md` | `transaction/history.md`、`transaction/status-model.md`、`knowledge-gaps.md` | Card 文件 |
| Receive | `wallet/receive.md` | `wallet/deposit.md`、`wallet/balance.md`、`knowledge-gaps.md`、`_system-boundary.md` | 直接复用 Deposit 规则 |
| Send / Swap | `wallet/send.md`、`knowledge-gaps.md` | 历史 PRD 原文 | 写成 active 功能 |
| Wallet 交易历史 | `transaction/history.md` | `wallet/balance.md`、`transaction/status-model.md`、`knowledge-gaps.md` | `wallet/transaction-history.md` |
| Wallet 交易详情 | `transaction/detail.md` | `transaction/history.md`、`transaction/status-model.md`、`knowledge-gaps.md` | Card Detail 规则直接套用 |
| Card 交易展示 | `card/card-transaction-flow.md` | `transaction/detail.md`、`transaction/history.md`、`common/notification.md` | Wallet History 规则直接套用 |
| Card refund / reversal / deposit 自动归集 | `card/card-transaction-flow.md` | `transaction/reconciliation.md`、`common/errors.md`、`knowledge-gaps.md`、`_system-boundary.md` | `wallet/deposit.md` |
| 资金追踪 / 对账 / ID 串联 | `transaction/reconciliation.md` | `card/card-transaction-flow.md`、`transaction/history.md`、`transaction/detail.md`、`knowledge-gaps.md`、`_system-boundary.md` | 旧 checklist |
| Transaction 状态模型 | `transaction/status-model.md` | `transaction/history.md`、`transaction/detail.md`、`knowledge-gaps.md` | 强行合并 Card / Wallet 状态 |
| Account Opening / KYC / 开户准入 | `kyc/account-opening.md` | `common/aai.md`、`common/dtc.md`、`common/notification.md`、`knowledge-gaps.md`、`_system-boundary.md` | `kyc/wallet-kyc.md` |
| DTC Master / Sub Account / D-SUB-ACCOUNT-ID | `kyc/account-opening.md`、`common/dtc.md` | `wallet/deposit.md`、`common/walletconnect.md`、`wallet/balance.md`、`knowledge-gaps.md`、`_system-boundary.md` | DTC 完整供应商说明书 |
| AAI 外部依赖 | `common/aai.md` | `kyc/account-opening.md`、`knowledge-gaps.md`、`_system-boundary.md` | AAI 完整供应商说明 |
| DTC 外部依赖 | `common/dtc.md` | 对应业务事实文件、`knowledge-gaps.md`、`_system-boundary.md` | DTC 完整接口说明书 |
| Notification / Push / 站内信 | `common/notification.md` | `wallet/deposit.md`、`card/card-transaction-flow.md`、`kyc/account-opening.md`、`knowledge-gaps.md`、`_system-boundary.md` | 用业务流程文件替代通知文件 |
| Errors / 错误处理 | `common/errors.md` | `common/walletconnect.md`、`wallet/deposit.md`、`card/card-transaction-flow.md`、`kyc/account-opening.md`、`knowledge-gaps.md` | 自行补错误码表 |
| FAQ / 客服口径 | `common/faq.md` | 对应业务文件、`knowledge-gaps.md` | 自行扩写 FAQ |

## 6. ALL-GAP 使用规则

`knowledge-base/changelog/knowledge-gaps.md` 是唯一待确认表。

| 状态 | AI 使用方式 |
|---|---|
| `deferred` | 未确认，不能写成事实；只能标记为待确认边界 |
| `open` | 未确认，不能写成事实 |
| `resolved-by-user` | 可作为用户确认结论，但需保留边界描述 |
| `resolved` | 可作为已闭环事实引用 |

写需求时，如果逻辑依赖未确认项，必须写成：

```text
当前未确认，见 ALL-GAP-XXX。
```

不得写成：

```text
系统会……
默认……
一定……
应当……
```

## 7. 系统边界规则

涉及以下问题时，必须读取 `knowledge-base/_system-boundary.md`：

1. 某能力是否属于 AIX 责任。
2. 是否能写进 AIX PRD。
3. DTC / AAI / WalletConnect / 第三方钱包 / GTR / 区块链网络的责任归属。
4. 通知是否等同到账。
5. Deposit success、Risk Withheld、Wallet state、Card transaction 是否能做确定映射。
6. 对账、资金追踪、异常补偿、告警责任分派。
7. Account Opening / KYC 与 AAI / DTC Master / Sub Account / Wallet Account 的责任边界。

简版原则：AIX 只维护自身页面、调用、接收、展示、通知、告警、人工处理和记录边界；外部系统只记录 AIX 需要感知的结果、字段、事件和状态，不维护外部系统内部逻辑。

## 8. 禁止事项

AI 使用本知识库时不得：

1. 默认读取建设期过程文件。
2. 把 ALL-GAP deferred / open 项写成事实。
3. 在模块内新增 checklist / TODO / gaps 表。
4. 把 DTC / AAI 写成 AIX 自有系统。
5. 维护供应商完整接口说明书、完整错误码表或内部逻辑。
6. 把 Wallet `transactionId`、Wallet `id`、Wallet `relatedId` 与 Card `data.id` 强行关联。
7. 把 `FIAT_DEPOSIT` 写死为 GTR。
8. 把 `CRYPTO_DEPOSIT` 写死为 WalletConnect。
9. 把 Deposit success 写死为 Wallet `COMPLETED`。
10. 把 Risk Withheld 写死为 Wallet `REJECTED` / `PENDING` / `PROCESSING`。
11. 把通知写成必然到账。
12. 把 Send / Swap 写成 active。
13. 为了回答问题自行补页面、接口、字段、状态、文案。
14. 将外部系统内部逻辑写成 AIX 需求。
15. 把 `D-SUB-ACCOUNT-ID` 与 WalletAccount.clientId 写死为完全等价。
16. 把 KYC Approved 写成 Wallet / Deposit / WalletConnect / Receive 全部可用。
17. 把 `kyc/wallet-kyc.md` 当作当前 KYC 主事实源。

## 9. 标准回答结构

```text
结论：……

已确认事实：
1. ……
2. ……

系统边界：
1. AIX 负责……
2. 外部系统负责 / AIX 不控制……

未确认边界：
1. ……见 ALL-GAP-XXX
2. ……见 ALL-GAP-XXX

引用文件：
- xxx.md
- yyy.md
```

## 10. 来源引用

- (Ref: knowledge-base/_system-boundary.md / system-boundary)
- (Ref: knowledge-base/changelog/knowledge-gaps.md / ALL-GAP 总表)
- (Ref: knowledge-base/wallet/_index.md)
- (Ref: knowledge-base/card/_index.md)
- (Ref: knowledge-base/transaction/_index.md)
- (Ref: knowledge-base/kyc/_index.md)
- (Ref: knowledge-base/kyc/account-opening.md)
- (Ref: knowledge-base/common/_index.md)
- (Ref: 用户确认结论 / 2026-05-02 / 知识库切换为使用态；AI 日常入口为 _ai-query-router.md；KYC 文件名不应带 wallet)
