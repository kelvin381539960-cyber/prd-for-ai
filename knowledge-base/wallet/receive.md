---
module: wallet
feature: receive
version: "1.1"
status: deferred
reason: no confirmed product existence
source_doc: IMPLEMENTATION_PLAN.md；DTC Wallet OpenAPI Documentation；knowledge-base/wallet/_index.md；knowledge-base/wallet/balance.md；knowledge-base/transaction/history.md；knowledge-base/transaction/status-model.md；knowledge-base/wallet/deposit.md；knowledge-base/changelog/knowledge-gaps.md；用户确认结论 2026-05-01；用户确认结论 2026-05-02
source_section: Wallet Receive；Wallet _index v1.4；Wallet Balance v1.2；Transaction History v1.3；Wallet Deposit v1.6；ALL-GAP 总表
last_updated: 2026-05-02
owner: 吴忆锋
depends_on:
  - wallet/_index
  - wallet/balance
  - transaction/history
  - transaction/status-model
  - wallet/deposit
  - changelog/knowledge-gaps
---

# Wallet Receive 占位 钱包收款

## 1. 功能定位

Wallet Receive 当前为占位模块，仅用于记录收款能力核验范围，不作为 active 产品事实源。，包括收款入口、地址展示、链 / 币种选择、二维码 / 复制能力、交易记录承接和与 Deposit 的边界。

重要限制：Receive 是否独立上线、是否与 Deposit 同源、是否受 Deposit 规则影响，均未确认。当前本文仅作为 Receive 独立能力的基础占位；不得默认复用 Deposit 旧方案，也不得默认等同 GTR / WalletConnect Deposit。

所有未确认问题统一引用 `knowledge-base/changelog/knowledge-gaps.md` 的 ALL-GAP 编号；本文不再维护本地待补字段清单。

## 2. 当前状态（占位）

| 项目 | 当前判断 | 处理 |
|---|---|---|
| Receive 是否等同 Deposit | 未确认 | 不默认等同，见 ALL-GAP-059 |
| Receive 是否已独立上线 | 未确认 | 暂以 active 基础占位记录，待来源核验，见 ALL-GAP-059 |
| Receive 是否受 Deposit 合规 / 规则影响 | 未确认 | Stage Review 时必须检查，见 ALL-GAP-059、ALL-GAP-062 |
| Deposit | active，包含 GTR / Exchange 和 WalletConnect | 不直接作为 Receive 事实来源 |
| Send / Swap | deferred | 与 Receive 无直接关系 |

如后续确认 Receive 属于未上线或需重做能力，则本文件应改为 `status: deferred`。

## 3. 适用范围

| 范围 | 是否包含 | 说明 |
|---|---|---|
| 收款入口 | 包含 | 入口位置、页面文案、交互见 ALL-GAP-060 |
| 地址展示 | 包含 | 地址字段见 ALL-GAP-060 |
| 地址复制 | 包含 | 是否支持复制见 ALL-GAP-060 |
| 二维码展示 | 包含 | 是否支持二维码及生成规则见 ALL-GAP-060 |
| 链 / 币种选择 | 包含 | 支持范围见 ALL-GAP-061 |
| Memo / Tag | 包含 | 是否存在及字段名见 ALL-GAP-060 |
| 收款后交易记录 | 包含 | 引用 `transaction/history.md`，记录生成时机见 ALL-GAP-062 |
| 收款后余额变化 | 包含 | 引用 `wallet/balance.md`，余额影响见 ALL-GAP-055、ALL-GAP-062 |
| Deposit 具体流程 | 不包含 | GTR / WalletConnect 分别由 `wallet/deposit.md` 承接 |
| Send / Withdraw | 不包含 | `wallet/send.md` 承接，当前 deferred |

## 4. 已确认可引用的基础事实

| 项目 | 结论 | 来源 | 备注 |
|---|---|---|---|
| Wallet 交易 ID | Wallet 交易记录 / 详情出参均包含 `id`，Long，交易 id | DTC Wallet OpenAPI；用户确认 2026-05-01 | 可用于收款后交易记录，但生成规则见 ALL-GAP-062 |
| Wallet 详情入参 | 单笔 Wallet 交易详情入参为 `transactionId`，Unique transaction ID from DTC | DTC Wallet OpenAPI；用户确认 2026-05-01 | 与 Receive 地址 / 入账记录关系见 ALL-GAP-062 |
| Wallet 交易状态 | `state` 枚举为 `PENDING`、`PROCESSING`、`AUTHORIZED`、`COMPLETED`、`REJECTED`、`CLOSED` | DTC Wallet OpenAPI；用户确认 2026-05-01 | Receive 场景状态映射见 ALL-GAP-052、ALL-GAP-062 |
| Search Balance History | 可查询 Wallet 交易 / 余额历史 | DTC Wallet OpenAPI / 4.2.4 | `activityType` / `relatedId` 口径见 ALL-GAP-014、ALL-GAP-037、ALL-GAP-058 |
| Deposit | Deposit 为 active，包含 GTR 和 WalletConnect | 用户确认 2026-05-02；Wallet Deposit v1.6 | 不代表 Receive 等同 Deposit |

## 5. Receive 与 Deposit 的边界

| 问题 | 当前处理 |
|---|---|
| Receive 是否只是 Deposit 的页面入口 | 未确认，不写成事实；见 ALL-GAP-059 |
| Receive 地址是否来自 Deposit 地址接口 | 未确认，不写成事实；见 ALL-GAP-060 |
| Receive 成功是否等于 Deposit 成功 | 未确认，不写成事实；见 ALL-GAP-062 |
| Receive 是否涉及 Declare / Travel Rule | 未确认，不写成事实；见 ALL-GAP-044、ALL-GAP-062 |
| Receive 是否受 Deposit 合规或外部规则影响 | 未确认，Stage Review 必查；见 ALL-GAP-059、ALL-GAP-062 |

## 6. Receive 与 Balance / Transaction History 的关系

| 能力 | 关系 | 当前处理 |
|---|---|---|
| 地址展示 | 用户获得收款地址 | 字段见 ALL-GAP-060 |
| 外部转入 | 可能触发 Wallet 入账 | 流程见 ALL-GAP-059、ALL-GAP-062 |
| 余额变化 | 成功入账后影响 Wallet balance | 入账时点和字段见 ALL-GAP-055、ALL-GAP-062 |
| 交易记录 | 成功或处理中记录可能进入 Wallet Transaction History | 记录生成时机见 ALL-GAP-062 |
| 交易详情 | 通过 Wallet `transactionId` 查询 | transactionId 来源见 ALL-GAP-015、ALL-GAP-062 |
| 状态展示 | 引用 Wallet `state` 枚举 | Receive 状态映射见 ALL-GAP-052、ALL-GAP-062 |

## 7. ALL-GAP 引用

本文不维护独立待补表。Receive 相关不确定项统一引用 ALL-GAP：

| 编号 | 主题 |
|---|---|
| ALL-GAP-014 | Wallet `relatedId` 在 Card / GTR / WC 场景取值 |
| ALL-GAP-015 | Wallet `transactionId` 与 Wallet `id` 的关系 |
| ALL-GAP-044 | WalletConnect Declare / Travel Rule / 白名单规则边界 |
| ALL-GAP-052 | Receive 是否独立上线及状态映射 |
| ALL-GAP-055 | Wallet 当前余额查询接口和字段边界 |
| ALL-GAP-058 | Search Balance History 完整字段表 |
| ALL-GAP-059 | Receive 上线状态与 Deposit 关系 |
| ALL-GAP-060 | Receive 页面、地址与交互字段 |
| ALL-GAP-061 | Receive 支持范围 |
| ALL-GAP-062 | Receive 入账状态、失败 / on-hold 与通知规则 |

## 8. 历史待补字段到 ALL-GAP 映射

本表用于无损迁移历史问题，不作为新的模块级 checklist。后续只维护 ALL-GAP。

| 原待补项 | 当前 ALL-GAP |
|---|---|
| Receive 是否已上线 | ALL-GAP-059 |
| Receive 与 Deposit 关系 | ALL-GAP-059 |
| Receive 入口页面 | ALL-GAP-060 |
| 支持国家 / 用户范围 | ALL-GAP-061 |
| 支持币种 | ALL-GAP-061 |
| 支持链 / network | ALL-GAP-061 |
| 收款地址字段 | ALL-GAP-060 |
| Memo / Tag 字段 | ALL-GAP-060 |
| 二维码生成规则 | ALL-GAP-060 |
| 复制地址交互 | ALL-GAP-060 |
| 地址刷新 / 复用规则 | ALL-GAP-060 |
| 收款成功状态 | ALL-GAP-062 |
| 收款失败 / on-hold 状态 | ALL-GAP-062 |
| 通知规则 | ALL-GAP-062 |

## 9. 不写入事实的内容

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

## 10. Stage Review 关注点

Wallet Stage Review 时，需要重点判断：

1. Receive 是否是独立上线能力。
2. Receive 是否受 Deposit 合规或外部规则影响。
3. Receive 是否应继续保持 active，还是改为 deferred。
4. Receive 地址、链、币种、memo/tag 字段是否有来源。
5. Receive 状态与 Wallet `state` 枚举是否可闭环。
6. Receive 失败 / on-hold / risk rejected 是否有处理路径。

## 11. 来源引用

- (Ref: IMPLEMENTATION_PLAN.md / v4.7)
- (Ref: knowledge-base/wallet/_index.md / v1.4)
- (Ref: knowledge-base/wallet/balance.md / v1.2)
- (Ref: knowledge-base/transaction/history.md / v1.3)
- (Ref: knowledge-base/transaction/status-model.md / v1.2)
- (Ref: knowledge-base/wallet/deposit.md / v1.6)
- (Ref: DTC Wallet OpenAPI Documentation / Wallet 交易记录 / Search Balance History)
- (Ref: knowledge-base/changelog/knowledge-gaps.md / ALL-GAP 总表)
- (Ref: 用户确认结论 / 2026-05-01)
- (Ref: 用户确认结论 / 2026-05-02 / Deposit active、ALL-GAP 唯一总表与无损迁移规则)
