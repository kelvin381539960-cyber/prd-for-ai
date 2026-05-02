---
module: wallet
feature: receive
version: "1.0"
status: active
source_doc: IMPLEMENTATION_PLAN.md；DTC Wallet OpenAPI Documentation；knowledge-base/wallet/_index.md；knowledge-base/wallet/balance.md；knowledge-base/wallet/transaction-history.md；knowledge-base/wallet/deposit.md；用户确认结论 2026-05-01
source_section: IMPLEMENTATION_PLAN v3.6 / Receive；Wallet _index v1.1；Wallet Balance v1.0；Wallet Transaction History v1.0；Deposit deferred decision
last_updated: 2026-05-01
owner: 吴忆锋
depends_on:
  - wallet/_index
  - wallet/balance
  - wallet/transaction-history
  - wallet/deposit
---

# Wallet Receive 钱包收款

## 1. 功能定位

Wallet Receive 用于沉淀 AIX Wallet 收款地址相关能力，包括收款入口、地址展示、链 / 币种选择、二维码 / 复制能力、交易记录承接和与 Deposit 的边界。

重要限制：Deposit 因合规原因未上线且需重做，因此 Receive 不得默认复用 Deposit 旧方案。本文仅作为 Receive 独立能力的基础占位；是否已上线、是否可用、是否与 Deposit 同源，仍需来源确认。

## 2. 当前状态

| 项目 | 当前判断 | 处理 |
|---|---|---|
| Receive 是否等同 Deposit | 未确认 | 不默认等同 |
| Receive 是否已独立上线 | 未确认 | 暂以 active 基础占位记录，待来源核验 |
| Receive 是否受 Deposit 合规重做影响 | 未确认 | Stage Review 时必须检查 |
| Deposit 旧方案 | deferred | 不引用旧方案作为 Receive 事实 |
| Swap 旧方案 | deferred | 与 Receive 无直接关系 |

如后续确认 Receive 也属于未上线 Deposit 旧方案的一部分，则本文件应改为 `status: deferred`。

## 3. 适用范围

| 范围 | 是否包含 | 说明 |
|---|---|---|
| 收款入口 | 包含 | 入口位置、页面文案、交互待补 |
| 地址展示 | 包含 | 地址字段待补 |
| 地址复制 | 包含 | 是否支持复制待补 |
| 二维码展示 | 包含 | 是否支持二维码待补 |
| 链 / 币种选择 | 包含 | 支持范围待补 |
| Memo / Tag | 包含 | 是否存在待补 |
| 收款后交易记录 | 包含 | 引用 `wallet/transaction-history.md` |
| 收款后余额变化 | 包含 | 引用 `wallet/balance.md` |
| Deposit 旧流程 | 不包含 | 因合规原因 deferred |
| Send / Withdraw | 不包含 | 后续由 `wallet/send.md` 承接 |

## 4. 已确认可引用的基础事实

| 项目 | 结论 | 来源 | 备注 |
|---|---|---|---|
| Wallet 交易 ID | Wallet 交易记录 / 详情出参均包含 `id`，Long，交易 id | DTC Wallet OpenAPI；用户确认 2026-05-01 | 可用于收款后交易记录，但生成规则待补 |
| Wallet 详情入参 | 单笔 Wallet 交易详情入参为 `transactionId`，Unique transaction ID from DTC | DTC Wallet OpenAPI；用户确认 2026-05-01 | 与 Receive 地址 / 入账记录关系待补 |
| Wallet 交易状态 | `state` 枚举为 `PENDING`、`PROCESSING`、`AUTHORIZED`、`COMPLETED`、`REJECTED`、`CLOSED` | DTC Wallet OpenAPI；用户确认 2026-05-01 | Receive 场景状态映射待补 |
| Search Balance History | 可查询 Wallet 交易 / 余额历史 | DTC Wallet OpenAPI / 4.2.4 | `activityType` / `relatedId` 具体口径待补 |
| Deposit 状态 | Deposit 为 deferred | 用户确认 2026-05-01 | 不作为 Receive 事实来源 |

## 5. Receive 与 Deposit 的边界

| 问题 | 当前处理 |
|---|---|
| Receive 是否只是 Deposit 的页面入口 | 未确认，不写成事实 |
| Receive 地址是否来自 Deposit 地址接口 | 未确认，不写成事实 |
| Receive 成功是否等于 Deposit 成功 | 未确认，不写成事实 |
| Receive 是否涉及 Declare / Travel Rule | 未确认，不写成事实 |
| Receive 是否受合规重做影响 | 未确认，Stage Review 必查 |

## 6. Receive 与 Balance / Transaction History 的关系

| 能力 | 关系 | 当前处理 |
|---|---|---|
| 地址展示 | 用户获得收款地址 | 字段待补 |
| 外部转入 | 可能触发 Wallet 入账 | 流程待补 |
| 余额变化 | 成功入账后影响 Wallet balance | 入账时点和字段待补 |
| 交易记录 | 成功或处理中记录可能进入 Wallet Transaction History | 记录生成时机待补 |
| 交易详情 | 通过 Wallet `transactionId` 查询 | transactionId 来源待补 |
| 状态展示 | 引用 Wallet `state` 枚举 | Receive 状态映射待补 |

## 7. 待补字段清单

| 待补项 | 建议来源 | 当前处理 |
|---|---|---|
| Receive 是否已上线 | 产品确认 / 发布记录 / PRD | 待补 |
| Receive 与 Deposit 关系 | 产品确认 / PRD | 待补 |
| Receive 入口页面 | PRD / 截图 | 待补 |
| 支持国家 / 用户范围 | PRD / 合规确认 | 待补 |
| 支持币种 | PRD / DTC Wallet OpenAPI | 待补 |
| 支持链 / network | PRD / DTC Wallet OpenAPI | 待补 |
| 收款地址字段 | DTC Wallet OpenAPI | 待补 |
| Memo / Tag 字段 | DTC Wallet OpenAPI / PRD | 待补 |
| 二维码生成规则 | PRD / 前端设计 | 待补 |
| 复制地址交互 | PRD / 截图 | 待补 |
| 地址刷新 / 复用规则 | DTC Wallet OpenAPI / PRD | 待补 |
| 收款成功状态 | DTC Wallet OpenAPI / PRD | 待补 |
| 收款失败 / on-hold 状态 | DTC Wallet OpenAPI / 风控 / 合规文档 | 待补 |
| 通知规则 | Notification PRD | 待补 |

## 8. 不写入事实的内容

以下内容当前不得写成事实：

1. Receive 已上线。
2. Receive 等同于 Deposit。
3. Receive 可直接使用 Deposit 旧方案。
4. Receive 支持某个具体币种或链。
5. Receive 地址字段名、memo/tag 字段名。
6. Receive 成功一定生成 Wallet `COMPLETED` 交易。
7. Receive 成功一定立即增加可用余额。
8. Receive 不受合规限制。
9. Receive 不需要 Declare / Travel Rule。
10. Receive 成功 / 失败通知文案。

## 9. Stage Review 关注点

Wallet Stage Review 时，需要重点判断：

1. Receive 是否是独立上线能力。
2. Receive 是否受 Deposit 合规重做影响。
3. Receive 是否应继续保持 active，还是改为 deferred。
4. Receive 地址、链、币种、memo/tag 字段是否有来源。
5. Receive 状态与 Wallet `state` 枚举是否可闭环。
6. Receive 失败 / on-hold / risk rejected 是否有处理路径。

## 10. 来源引用

- (Ref: IMPLEMENTATION_PLAN.md / v3.6 / Wallet Receive 当前任务)
- (Ref: knowledge-base/wallet/_index.md / v1.1 / Deposit 与 Swap deferred)
- (Ref: knowledge-base/wallet/balance.md / v1.0)
- (Ref: knowledge-base/wallet/transaction-history.md / v1.0)
- (Ref: knowledge-base/wallet/deposit.md / v1.1 / Deposit deferred)
- (Ref: DTC Wallet OpenAPI Documentation / Wallet 交易记录 / Search Balance History)
- (Ref: 用户确认结论 / 2026-05-01 / Deposit 与 Swap 合规重做)
