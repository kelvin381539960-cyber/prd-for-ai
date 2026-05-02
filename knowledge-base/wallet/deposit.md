---
module: wallet
feature: deposit
version: "1.2"
status: active
source_doc: DTC Wallet OpenAPI Documentation；knowledge-base/wallet/_index.md；knowledge-base/wallet/balance.md；knowledge-base/wallet/transaction-history.md；knowledge-base/changelog/knowledge-gaps.md；用户确认结论 2026-05-01
source_section: Wallet Deposit / GTR / WalletConnect；Wallet _index v1.3；Wallet Balance v1.0；Wallet Transaction History v1.0；deposit scope correction
last_updated: 2026-05-01
owner: 吴忆锋
depends_on:
  - wallet/_index
  - wallet/balance
  - wallet/transaction-history
  - changelog/knowledge-gaps
---

# Wallet Deposit 钱包充值

## 1. 当前状态

Wallet Deposit 当前状态为 `active`。

根据用户确认，Deposit 能力是存在的，包含 GTR 和 WalletConnect 两类入金路径。此前将整个 Deposit 模块标记为 deferred 的口径过宽，已修正。

需要注意：Deposit 下可能仍存在因合规原因需要重做或调整的旧方案 / 子路径。该类内容不得自动写入 active 事实；必须按 GTR、WalletConnect 或其他具体路径分别确认。

## 2. 模块定位

Wallet Deposit 用于沉淀 AIX Wallet 入金相关能力，包括 GTR 入金、WalletConnect 入金、入金交易记录、余额变化、状态和异常边界。

本文当前只建立 Deposit 的模块边界与已确认基础事实。具体 GTR / WalletConnect 的字段、状态、风控、通知和用户路径，需要继续从历史 PRD、接口文档、截图或已确认结论中补齐。

## 3. Deposit 子路径

| 子路径 | 当前状态 | 说明 |
|---|---|---|
| GTR Deposit | active / 待补细节 | 用户确认 Deposit 包含 GTR；具体字段、状态、失败处理待补 |
| WalletConnect Deposit | active / 待补细节 | 用户确认 Deposit 包含 WalletConnect；具体字段、状态、失败处理待补 |
| 其他 Deposit 旧方案 | 未确认 | 不得默认归档为 active；需按来源确认 |
| Swap | deferred | 仍按合规原因未上线 / 需重做处理 |
| Send | deferred | 仍按合规原因未上线处理 |

## 4. 适用范围

| 范围 | 是否包含 | 说明 |
|---|---|---|
| GTR 入金 | 包含 | 具体流程待补 |
| WalletConnect 入金 | 包含 | 具体流程待补 |
| Deposit 交易记录 | 包含 | 引用 `wallet/transaction-history.md` |
| Deposit 后余额变化 | 包含 | 引用 `wallet/balance.md` |
| Deposit 通知 | 待补 | 需引用 Notification PRD 或已确认通知配置 |
| Deposit 风控 / on-hold | 待补 | 需从 DTC / 风控 / PRD 补齐 |
| Deposit Declare / Travel Rule | 待补 | 需从合规 PRD 或确认结论补齐 |
| Card balance 自动归集 | 不包含 | 属于 Card Transaction Flow，且部分关联字段为 deferred gap |
| Send / Withdraw | 不包含 | Send 当前 deferred |
| Swap | 不包含 | Swap 当前 deferred |

## 5. 已确认基础事实

| 项目 | 结论 | 来源 | 备注 |
|---|---|---|---|
| Deposit 能力存在 | Deposit 包含 GTR 和 WalletConnect | 用户确认 2026-05-01 | 需要继续拆分子路径 |
| Wallet 交易 ID | Wallet 交易记录 / 详情出参均包含 `id`，Long，交易 id | DTC Wallet OpenAPI；用户确认 2026-05-01 | Deposit 到账记录可引用 Wallet 交易 ID |
| Wallet 详情入参 | 单笔 Wallet 交易详情入参为 `transactionId`，Unique transaction ID from DTC | DTC Wallet OpenAPI；用户确认 2026-05-01 | 与具体 Deposit 链路字段关系待补 |
| Wallet 交易状态 | `state` 枚举为 `PENDING`、`PROCESSING`、`AUTHORIZED`、`COMPLETED`、`REJECTED`、`CLOSED` | DTC Wallet OpenAPI；用户确认 2026-05-01 | Deposit 状态是否完全复用该枚举待原文确认 |
| Search Balance History | 可查询 Wallet 交易 / 余额历史 | DTC Wallet OpenAPI / 4.2.4 | 返回字段包含 `activityType`、`relatedId`、`time`、`state` 等 |

## 6. Deposit 与 Balance 的关系

| 阶段 | 余额影响 | 当前处理 |
|---|---|---|
| 用户通过 GTR / WalletConnect 发起入金 | 未确认 | 交易生成时机待补 |
| DTC / AIX 识别入金 | 可能生成 Wallet 交易记录 | 需从接口文档 / PRD 补齐 |
| 入金处理中 | 可能对应 `PENDING` / `PROCESSING` 等状态 | 状态映射待补 |
| 入金成功 | Wallet balance 增加 | 具体字段和入账时点待补 |
| 入金失败 / 拒绝 / on-hold | Wallet balance 不增加或进入异常处理 | 失败状态与原因待补 |

## 7. Deposit 与 Transaction History 的关系

Deposit 交易记录与详情应统一引用 Wallet Transaction History 的基础字段。

| 能力 | 关系 |
|---|---|
| Deposit 记录 ID | 使用 Wallet 交易 `id`，具体生成时机待补 |
| Deposit 详情查询 | 通过 `transactionId` 查询 Wallet 单笔交易详情，具体入参来源待补 |
| Deposit 状态 | 引用 Wallet `state` 枚举，具体状态映射待补 |
| Deposit 余额历史 | 通过 Search Balance History 查询，具体 `activityType` / `relatedId` 待补 |

## 8. GTR / WalletConnect 待拆分问题

| 问题 | GTR | WalletConnect | 当前处理 |
|---|---|---|---|
| 入金触发方式 | 待补 | 待补 | 需从 PRD / 接口文档补齐 |
| 是否需要 Declare | 待补 | 待补 | 需合规口径确认 |
| 是否需要白名单 | 待补 | 待补 | 需区分路径确认 |
| 是否存在 on-hold / risk rejected | 待补 | 待补 | 需风控 / DTC 口径确认 |
| 入金成功状态 | 待补 | 待补 | 需与 Wallet `state` 映射 |
| 入金失败状态 | 待补 | 待补 | 需与错误码 / 状态枚举映射 |
| 用户通知 | 待补 | 待补 | 需 Notification PRD |
| 用户资金可见时点 | 待补 | 待补 | 需产品 / 后端确认 |

## 9. 与 Card Transaction Flow 的边界

Card balance 自动归集到 Wallet 不是 Wallet Deposit 主流程。

| 项目 | 处理 |
|---|---|
| Card refund / reversal / deposit 触发查卡余额 | 属于 Card Transaction Flow |
| `Transfer Balance to Wallet(cardId, amount=balance)` | 属于 Card Transaction Flow |
| DTC transfer 成功响应无业务流水 | 已在 Card Transaction Flow 记录 |
| Wallet 是否生成对应交易 `id` | Wallet 交易 `id` 已确认存在，但与 Card 归集的关联仍 deferred |
| Wallet `relatedId` 在 Card balance 转 Wallet 场景下取值 | deferred gap，不在 Deposit 补写 |

## 10. 待补字段清单

| 待补项 | 建议来源 | 当前处理 |
|---|---|---|
| GTR Deposit 完整流程 | GTR PRD / 接口文档 / 截图 | 待补 |
| WalletConnect Deposit 完整流程 | WC PRD / 接口文档 / 截图 | 待补 |
| GTR / WC 支持国家、币种、链 | PRD / 合规确认 | 待补 |
| GTR / WC 入金交易 ID 字段 | DTC / AIX 接口文档 | 待补 |
| GTR / WC 入金状态映射 | PRD / DTC Wallet OpenAPI | 待补 |
| GTR / WC 风控拦截规则 | 风控 / DTC 文档 / PRD | 待补 |
| GTR / WC on-hold 规则 | 风控 / 合规文档 | 待补 |
| GTR / WC Declare / Travel Rule 规则 | 合规 PRD | 待补 |
| Deposit 通知规则 | Notification PRD | 待补 |
| Deposit 客服 / 人工处理边界 | 运营 / 后台 PRD | 待补 |

## 11. 不写入事实的内容

以下内容当前不得写成事实：

1. 所有 Deposit 子路径都未上线。
2. 所有 Deposit 子路径都已上线。
3. GTR 与 WalletConnect 使用同一套字段、状态或风控规则。
4. 所有 Deposit 都需要白名单。
5. 所有 Deposit 都需要 Declare。
6. Deposit 成功一定等同于 Wallet balance 立即可用。
7. Deposit 状态完全等同于 Wallet `state` 枚举中的某几个值。
8. Deposit 风控拦截规则。
9. Deposit 成功 / 失败通知文案。
10. Card balance 自动归集属于 Wallet Deposit。

## 12. 阶段影响

Deposit 恢复为 Wallet 阶段 active 能力，但当前仍是基础版。

下一步应优先补齐 GTR 和 WalletConnect 两条子路径的 PRD / 接口字段 / 状态 / 风控 / 通知规则，再判断 Deposit 是否具备完整 Stage Review 条件。

## 13. 来源引用

- (Ref: 用户确认结论 / 2026-05-01 / Deposit 包含 GTR 和 WalletConnect)
- (Ref: DTC Wallet OpenAPI Documentation / Wallet 通用交易记录与状态)
- (Ref: knowledge-base/wallet/_index.md / Wallet 模块边界)
- (Ref: knowledge-base/wallet/balance.md / Wallet Balance v1.0)
- (Ref: knowledge-base/wallet/transaction-history.md / Wallet Transaction History v1.0)
- (Ref: knowledge-base/changelog/knowledge-gaps.md / Card Transaction Flow deferred gaps)
