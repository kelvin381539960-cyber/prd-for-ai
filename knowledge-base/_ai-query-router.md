---
module: knowledge-base
feature: ai-query-router
version: "1.1"
status: active
source_doc: IMPLEMENTATION_PLAN.md；knowledge-base/_system-boundary.md；knowledge-base/changelog/knowledge-gaps.md；knowledge-base/changelog/final-repository-review.md；knowledge-base/wallet/_index.md；knowledge-base/transaction/_index.md；knowledge-base/kyc/_index.md；knowledge-base/common/_index.md；knowledge-base/card/_index.md；用户确认结论 2026-05-02
source_section: AI knowledge base usage；query routing；fact source rules；system boundary usage rules；ALL-GAP usage rules
last_updated: 2026-05-02
owner: 吴忆锋
---

# AI 查询路由表 / 使用说明

## 1. 文档定位

本文档用于指导 AI 在查询 AIX 知识库、写需求、改需求、回答需求逻辑时，如何高效读取事实来源。

本文档不新增业务事实，不替代功能文档，不替代 `knowledge-base/changelog/knowledge-gaps.md`，不替代 `knowledge-base/_system-boundary.md`。

AI 使用知识库时，默认按以下顺序读取：

```text
1. IMPLEMENTATION_PLAN.md
2. knowledge-base/_ai-query-router.md
3. 对应模块 _index.md
4. 对应功能事实文件
5. knowledge-base/changelog/knowledge-gaps.md
```

如果问题涉及系统责任、外部依赖、AIX 与供应商边界、是否应写入需求，则必须额外读取：

```text
knowledge-base/_system-boundary.md
```

其中：

- `IMPLEMENTATION_PLAN.md` 是主控计划，决定当前阶段、目录边界、禁止事项。
- `_ai-query-router.md` 只负责告诉 AI 应该读哪些文件。
- `_system-boundary.md` 负责判断 AIX 与外部系统责任边界。
- 模块 `_index.md` 负责确认模块结构和主事实源。
- 功能事实文件负责回答业务逻辑。
- `knowledge-gaps.md` 只负责确认不确定项，不能把 deferred / open 项当事实。

## 2. 总体查询原则

| 原则 | 要求 |
|---|---|
| 不全仓库乱扫 | 先按问题类型定位模块和文件 |
| 先主控，后事实 | 必须先读 `IMPLEMENTATION_PLAN.md` |
| 先主事实源，后辅助文件 | 优先读取路由表中的“必读文件” |
| 涉及责任边界读系统边界 | 涉及 AIX / 外部系统责任划分时，必须读取 `_system-boundary.md` |
| 遇到不确定项查 ALL-GAP | 任何 deferred / open 项不得写成事实 |
| 外部依赖只看边界 | DTC / AAI 不作为供应商说明书阅读，只读 AIX 设计相关边界 |
| 不用 moved notice 当事实 | `wallet/kyc.md`、`wallet/transaction-history.md` 只作为旧路径提示 |
| 不补不存在的规则 | 来源没有的页面、接口、状态、文案、错误码不得脑补 |

## 3. 快速路由表

| 用户问题类型 | 必读文件 | 需要时再读 | 不应优先读 |
|---|---|---|---|
| 当前仓库状态 / 执行规则 | `IMPLEMENTATION_PLAN.md` | `knowledge-base/changelog/final-repository-review.md` | 历史 PRD 原文 |
| 系统边界 / 责任边界 | `knowledge-base/_system-boundary.md` | `common/dtc.md`、`common/aai.md`、`common/walletconnect.md` | 直接读供应商原文 |
| AIX 是否负责某能力 | `knowledge-base/_system-boundary.md` | 对应业务事实文件、`knowledge-gaps.md` | 只看功能 PRD |
| 待确认项 / 缺口 / deferred | `knowledge-base/changelog/knowledge-gaps.md` | 对应模块事实文件 | 模块内旧 checklist |
| Deposit / 入金总逻辑 | `wallet/deposit.md` | `common/notification.md`、`common/errors.md`、`common/dtc.md`、`_system-boundary.md` | `wallet/receive.md` |
| GTR / Exchange 地址充值 | `wallet/deposit.md` | `common/dtc.md`、`transaction/history.md`、`knowledge-gaps.md`、`_system-boundary.md` | `common/walletconnect.md` |
| WalletConnect 充值 | `common/walletconnect.md`、`wallet/deposit.md` | `common/errors.md`、`common/notification.md`、`common/dtc.md`、`knowledge-gaps.md`、`_system-boundary.md` | `wallet/receive.md` |
| WalletConnect 白名单 / 授权 | `common/walletconnect.md`、`wallet/deposit.md` | `common/dtc.md`、`knowledge-gaps.md`、`_system-boundary.md` | DTC 原始完整说明书 |
| WalletConnect 异常 / 支付失败 | `common/errors.md`、`common/walletconnect.md` | `wallet/deposit.md`、`knowledge-gaps.md`、`_system-boundary.md` | `common/notification.md` |
| Risk Withheld / under review | `wallet/deposit.md`、`common/dtc.md`、`common/notification.md` | `common/errors.md`、`transaction/status-model.md`、`knowledge-gaps.md`、`_system-boundary.md` | 直接映射 Wallet state |
| Wallet Balance / 余额展示 | `wallet/balance.md` | `transaction/history.md`、`transaction/status-model.md`、`knowledge-gaps.md` | `card/card-transaction-flow.md` |
| Receive / 收款 | `wallet/receive.md` | `wallet/deposit.md`、`wallet/balance.md`、`knowledge-gaps.md`、`_system-boundary.md` | 直接复用 Deposit 规则 |
| Send / Withdrawal | `wallet/send.md` | `wallet/stage-review.md`、`IMPLEMENTATION_PLAN.md` | 写成 active 功能 |
| Swap | `wallet/stage-review.md`、`IMPLEMENTATION_PLAN.md` | 历史 PRD 原文 | 写成 active 功能 |
| Wallet 交易历史 | `transaction/history.md` | `wallet/balance.md`、`transaction/status-model.md`、`knowledge-gaps.md` | `wallet/transaction-history.md` |
| Wallet 交易详情 | `transaction/detail.md` | `transaction/history.md`、`transaction/status-model.md`、`knowledge-gaps.md` | Card Detail 规则直接套用 |
| Card 交易展示 | `card/card-transaction-flow.md` | `transaction/detail.md`、`transaction/history.md`、`common/notification.md` | Wallet History 规则直接套用 |
| Card refund / reversal / deposit 自动归集 | `card/card-transaction-flow.md` | `transaction/reconciliation.md`、`common/errors.md`、`knowledge-gaps.md`、`_system-boundary.md` | `wallet/deposit.md` |
| 资金追踪 / 对账 / ID 串联 | `transaction/reconciliation.md` | `card/card-transaction-flow.md`、`transaction/history.md`、`transaction/detail.md`、`knowledge-gaps.md`、`_system-boundary.md` | 模块内旧 checklist |
| Transaction 状态模型 | `transaction/status-model.md` | `transaction/history.md`、`transaction/detail.md`、`knowledge-gaps.md` | 强行合并 Card / Wallet 状态 |
| KYC / Wallet KYC | `kyc/wallet-kyc.md` | `common/aai.md`、`knowledge-gaps.md`、`_system-boundary.md` | `wallet/kyc.md` |
| AAI 外部依赖 | `common/aai.md` | `kyc/wallet-kyc.md`、`knowledge-gaps.md`、`_system-boundary.md` | AAI 完整供应商说明 |
| DTC 外部依赖 | `common/dtc.md` | 业务相关文件、`knowledge-gaps.md`、`_system-boundary.md` | DTC 完整接口说明书 |
| Notification / Push / 站内信 | `common/notification.md` | `wallet/deposit.md`、`card/card-transaction-flow.md`、`wallet/receive.md`、`knowledge-gaps.md`、`_system-boundary.md` | 业务流程文件替代通知文件 |
| Errors / 错误处理 | `common/errors.md` | `common/walletconnect.md`、`wallet/deposit.md`、`card/card-transaction-flow.md`、`knowledge-gaps.md` | 自行补错误码表 |
| FAQ / 客服口径 | `common/faq.md` | 对应业务文件、`knowledge-gaps.md` | 自行扩写 FAQ |

## 4. 按任务类型的读取策略

### 4.1 写 PRD / 新需求

读取顺序：

```text
1. IMPLEMENTATION_PLAN.md
2. knowledge-base/_ai-query-router.md
3. 对应模块 _index.md
4. 对应功能事实文件
5. common/errors.md / common/notification.md / common/dtc.md（如涉及）
6. knowledge-base/_system-boundary.md（如涉及责任边界或外部系统）
7. knowledge-base/changelog/knowledge-gaps.md
```

写作规则：

- 只写已确认事实。
- 需要引用未确认项时，用 `ALL-GAP-XXX` 标记，不补结论。
- 如果涉及资金、状态、通知、错误处理，必须查对应 Common / Transaction 文件。
- 如果需求涉及 DTC / AAI / WalletConnect / 第三方钱包 / 区块链，只写 AIX 系统设计相关边界。

### 4.2 查询某个业务逻辑

读取顺序：

```text
1. IMPLEMENTATION_PLAN.md
2. knowledge-base/_ai-query-router.md
3. 路由表对应的必读文件
4. knowledge-base/_system-boundary.md（如涉及责任边界）
5. knowledge-base/changelog/knowledge-gaps.md
```

回答规则：

- 先回答已确认逻辑。
- 再列出未确认边界。
- 不要把 ALL-GAP 的问题当作结论。
- 不要把外部系统内部逻辑写成 AIX 责任。

### 4.3 修改已有知识库

读取顺序：

```text
1. IMPLEMENTATION_PLAN.md
2. knowledge-base/_ai-query-router.md
3. 被修改文件
4. 该模块 _index.md
5. knowledge-base/_system-boundary.md（如涉及责任边界）
6. knowledge-base/changelog/knowledge-gaps.md
```

修改规则：

- 不允许新增模块级 checklist / TODO / gaps 表。
- 新发现的不确定项必须先进 ALL-GAP。
- 如果清理旧问题，必须保留旧问题到 ALL-GAP 的映射。
- 不允许因为精简而丢失问题颗粒度。

### 4.4 回答“是否已确认”类问题

读取顺序：

```text
1. knowledge-base/changelog/knowledge-gaps.md
2. 对应功能事实文件
3. knowledge-base/_system-boundary.md（如涉及责任归属）
4. IMPLEMENTATION_PLAN.md
```

判断规则：

| 情况 | 回答方式 |
|---|---|
| 功能文件有明确事实，ALL-GAP 无冲突 | 可回答“已确认” |
| 功能文件有事实，但 ALL-GAP 有相关 deferred / open | 回答“部分确认，边界未确认” |
| 只有 ALL-GAP，没有事实文件结论 | 回答“未确认” |
| ALL-GAP 已 resolved-by-user | 回答“已由用户确认”，并引用用户确认结论所在文件 |
| 涉及外部系统责任 | 先查 `_system-boundary.md`，再判断是否属于 AIX 可控范围 |

## 5. 模块主事实源

| 模块 | 主事实源 | 说明 |
|---|---|---|
| Knowledge Base Control | `IMPLEMENTATION_PLAN.md`、`_ai-query-router.md`、`_system-boundary.md` | 主控计划、查询路由、系统边界 |
| Account | `account/*` | Login / Registration / Password Reset |
| Security | `security/*` | OTP / Email OTP / Passcode / BIO / Face Auth / API Reference |
| Card | `card/card-transaction-flow.md`、`card/*` | 卡交易、卡状态、卡管理 |
| Wallet | `wallet/deposit.md`、`wallet/balance.md`、`wallet/receive.md`、`wallet/send.md` | 钱包产品能力 |
| Transaction | `transaction/history.md`、`transaction/detail.md`、`transaction/status-model.md`、`transaction/reconciliation.md` | 跨 Card / Wallet / Deposit 的交易统一层 |
| KYC | `kyc/wallet-kyc.md` | KYC 主事实源 |
| Common | `common/dtc.md`、`common/aai.md`、`common/walletconnect.md`、`common/notification.md`、`common/errors.md`、`common/faq.md` | 公共能力和外部依赖边界 |
| Changelog | `changelog/knowledge-gaps.md`、`changelog/final-repository-review.md` | 唯一待确认表和阶段收口记录 |

## 6. 旧路径处理

| 旧路径 | 当前处理 |
|---|---|
| `wallet/kyc.md` | moved notice；KYC 主事实源为 `kyc/wallet-kyc.md` |
| `wallet/transaction-history.md` | moved notice；交易历史主事实源为 `transaction/history.md` |
| `card/transaction-flow-traceability-checklist.md` | migrated-reference；仅作历史追溯，不作为新的 checklist |

AI 不得把 moved notice 或 migrated-reference 当作当前业务主事实源。

## 7. ALL-GAP 使用规则

| 状态 | AI 应如何使用 |
|---|---|
| `deferred` | 未确认，不能写成事实；可引用为待确认边界 |
| `open` | 未确认，不能写成事实；需要后续补答案 |
| `resolved-by-user` | 可作为用户已确认结论，但仍需看具体描述 |
| `resolved` | 已闭环，可作为确认项引用 |

写需求时，如果某条逻辑依赖 ALL-GAP 的 deferred / open 项，必须写成：

```text
当前未确认，见 ALL-GAP-XXX。
```

不能写成：

```text
系统会……
一定会……
默认……
应当……
```

## 8. 高风险问题必须查的文件

| 高风险问题 | 必查文件 |
|---|---|
| 资金是否到账 | `wallet/balance.md`、`transaction/history.md`、`transaction/reconciliation.md`、`knowledge-gaps.md`、`_system-boundary.md` |
| 交易状态如何展示 | `transaction/status-model.md`、`transaction/detail.md`、`knowledge-gaps.md` |
| 通知是否代表到账 | `common/notification.md`、`transaction/reconciliation.md`、`knowledge-gaps.md`、`_system-boundary.md` |
| Risk Withheld 如何处理 | `wallet/deposit.md`、`common/dtc.md`、`common/errors.md`、`knowledge-gaps.md`、`_system-boundary.md` |
| Card refund 是否归集到 Wallet | `card/card-transaction-flow.md`、`transaction/reconciliation.md`、`knowledge-gaps.md` |
| WalletConnect 是否需要白名单 | `common/walletconnect.md`、`wallet/deposit.md`、`common/dtc.md`、`knowledge-gaps.md`、`_system-boundary.md` |
| DTC 字段是否可用 | `common/dtc.md`、对应业务文件、`knowledge-gaps.md`、`_system-boundary.md` |
| AAI / KYC 结果是否影响准入 | `kyc/wallet-kyc.md`、`common/aai.md`、`knowledge-gaps.md`、`_system-boundary.md` |
| 某能力是否属于 AIX 责任 | `_system-boundary.md`、对应业务文件、`knowledge-gaps.md` |

## 9. 禁止使用方式

AI 使用本知识库时，不得：

1. 跳过 `IMPLEMENTATION_PLAN.md`。
2. 不看路由表就全仓库乱搜。
3. 涉及责任边界时跳过 `_system-boundary.md`。
4. 把 ALL-GAP deferred / open 项写成事实。
5. 把 DTC / AAI 当作 AIX 自有系统。
6. 把供应商完整接口文档当作知识库维护目标。
7. 把 Wallet `transactionId`、Wallet `id`、Wallet `relatedId` 与 Card `data.id` 强行关联。
8. 把 `FIAT_DEPOSIT` 写死为 GTR。
9. 把 `CRYPTO_DEPOSIT` 写死为 WalletConnect。
10. 把 Deposit success 写死为 Wallet `COMPLETED`。
11. 把 Risk Withheld 写死为 Wallet `REJECTED` / `PENDING` / `PROCESSING`。
12. 把通知写成必然到账。
13. 把 Send / Swap 写成 active。
14. 把旧 moved notice 当主事实源。
15. 为了回答问题而自行补页面、接口、字段、状态、文案。
16. 将外部系统内部逻辑写成 AIX 需求。

## 10. 标准回答结构

当 AI 基于知识库回答需求逻辑时，建议使用：

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

当 AI 写需求时，建议使用：

```text
需求背景：引用已确认事实
业务规则：只写已确认逻辑
系统边界：明确 AIX 与外部系统责任
异常处理：只写已有来源的异常
待确认项：引用 ALL-GAP 编号
不纳入范围：明确排除未上线 / 未确认 / 外部不可控能力
```

## 11. 来源引用

- (Ref: IMPLEMENTATION_PLAN.md / v5.1)
- (Ref: knowledge-base/_system-boundary.md / v1.0)
- (Ref: knowledge-base/changelog/knowledge-gaps.md / ALL-GAP 总表)
- (Ref: knowledge-base/changelog/final-repository-review.md / v1.5)
- (Ref: knowledge-base/wallet/_index.md)
- (Ref: knowledge-base/transaction/_index.md)
- (Ref: knowledge-base/kyc/_index.md)
- (Ref: knowledge-base/common/_index.md)
- (Ref: knowledge-base/card/_index.md)
- (Ref: 用户确认结论 / 2026-05-02 / ALL-GAP 留待以后确认，当前工作收口完成；外部依赖只保留与 AIX 系统设计有关内容)
