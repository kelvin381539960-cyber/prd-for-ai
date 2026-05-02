---
module: changelog
feature: refinement-stage-review
version: "1.0"
status: active
source_doc: IMPLEMENTATION_PLAN.md；DTC接口文档/DTC Wallet OpenAPI Document20260126 (1).docx；[2025-11-25] AIX+Notification（push及站内信）.docx；knowledge-base/wallet/deposit.md；knowledge-base/wallet/transaction-history.md；knowledge-base/wallet/balance.md；knowledge-base/transaction/status-model.md；knowledge-base/transaction/history.md；knowledge-base/transaction/detail.md；knowledge-base/common/dtc.md；knowledge-base/common/walletconnect.md；knowledge-base/common/notification.md；knowledge-base/common/errors.md
source_section: 补材料与精修阶段阶段性回扫；Deposit / Wallet History / ActivityType / Risk Withheld
last_updated: 2026-05-01
owner: 吴忆锋
---

# 补材料与精修阶段阶段性回扫

## 1. 回扫结论

本轮补材料与精修阶段已完成 P0 中一部分高价值回填，阶段性结果为：`PARTIAL PASS`。

已完成内容：

1. 回填 DTC Crypto Deposit 外部依赖边界。
2. 回填 Deposit success / Risk Withheld 通知事实。
3. 回填 Search Balance History 基础接口与字段边界。
4. 回填 ActivityType 已确认枚举。
5. 将 Deposit / Wallet History / Transaction 统一层 / DTC 外部依赖边界同步。

仍不能标记为 PASS，原因是 GTR / WalletConnect 的完整产品流程、前端页面、Declare / Travel Rule、relatedId 映射、余额可见时点、人工处理仍未闭环。

## 2. 已确认事实

| 事实 | 来源 | 已同步文件 |
|---|---|---|
| Crypto business includes whitelisting, deposit, and withdrawal | DTC Wallet OpenAPI / 3.4 Crypto Deposit | wallet/deposit、common/dtc、common/walletconnect、common/errors |
| Crypto 充值涉及 senderAddress / destinationAddress | DTC Wallet OpenAPI / 3.4 Crypto Deposit | wallet/deposit、common/walletconnect |
| destinationAddress 由 DTC 自动分配 | DTC Wallet OpenAPI / 3.4 Crypto Deposit | wallet/deposit、common/dtc、common/walletconnect |
| senderAddress 需要 whitelist 并 enable | DTC Wallet OpenAPI / 3.4 Crypto Deposit | wallet/deposit、common/walletconnect、common/errors |
| 未加白进入 `status=102 Risk Withheld` | DTC Wallet OpenAPI / 3.4 Crypto Deposit | wallet/deposit、wallet/transaction-history、transaction/status-model、common/errors |
| 加白成功后自动变为 success | DTC Wallet OpenAPI / 3.4 Crypto Deposit | wallet/deposit、common/errors、transaction/status-model |
| Search Balance History endpoint 为 `[GET] /openapi/v1/wallet/balance/history/search` | DTC Wallet OpenAPI / 4.2.4 | wallet/transaction-history、wallet/balance、transaction/history、common/dtc |
| `FIAT_DEPOSIT=6` | DTC Wallet OpenAPI / Appendix ActivityType | wallet/transaction-history、wallet/balance、transaction/status-model、transaction/history、transaction/detail、common/dtc |
| `CRYPTO_DEPOSIT=10` | DTC Wallet OpenAPI / Appendix ActivityType | wallet/transaction-history、wallet/balance、transaction/status-model、transaction/history、transaction/detail、common/dtc |
| `DTC_WALLET=13` | DTC Wallet OpenAPI / Appendix ActivityType | wallet/transaction-history、wallet/balance、transaction/status-model、transaction/history、transaction/detail、common/dtc |
| `CARD_PAYMENT_REFUND=20` | DTC Wallet OpenAPI / Appendix ActivityType | wallet/transaction-history、wallet/balance、transaction/status-model、transaction/history、transaction/detail、common/dtc |
| Deposit success 通知：`event=CRYPTO_TXN`、`type=DEPOSIT`、`state=success` | Notification PRD / Deposit row | common/notification、wallet/deposit、transaction/history、transaction/detail |
| Deposit under review 通知：`event=CRYPTO_TXN`、`type=DEPOSIT`、`state=RISK_WITHHELD` | Notification PRD / Deposit row | common/notification、common/errors、wallet/deposit、transaction/history、transaction/detail |

## 3. 已更新文件

| 文件 | 最新版本 | 本轮结果 |
|---|---|---|
| `wallet/deposit.md` | v1.4 | 已补 DTC Crypto Deposit、Risk Withheld、Deposit 通知边界 |
| `common/walletconnect.md` | v1.2 | 已补 WalletConnect 可引用的 DTC Crypto Deposit 外部依赖 |
| `common/notification.md` | v1.2 | 已补 Deposit success / under review 通知事实与模板参数 |
| `common/errors.md` | v1.2 | 已补 Risk Withheld 错误 / on-hold 边界 |
| `common/dtc.md` | v1.3 | 已补 DTC Wallet / Crypto Deposit / ActivityType / Wallet History 依赖边界 |
| `wallet/transaction-history.md` | v1.1 | 已补 Search Balance History 与 ActivityType |
| `wallet/balance.md` | v1.1 | 已补 Balance History 与 ActivityType 边界 |
| `transaction/status-model.md` | v1.1 | 已补 Deposit `Risk Withheld` / `success` 与 Wallet state 的边界 |
| `transaction/history.md` | v1.1 | 已补 Wallet History / Deposit History / ActivityType 边界 |
| `transaction/detail.md` | v1.1 | 已补 Deposit Detail / Wallet Detail / ActivityType 边界 |

## 4. 一致性检查

| 检查项 | 结果 | 说明 |
|---|---|---|
| Deposit 是否仍为 active | 通过 | 仍限定 GTR / WalletConnect |
| Send / Swap 是否仍为 deferred | 通过 | 未写成 active |
| DTC 是否仍为外部依赖 | 通过 | 未写成供应商系统说明书 |
| `FIAT_DEPOSIT` 是否被写死为 GTR | 通过 | 仅写作候选 / 分类来源 |
| `CRYPTO_DEPOSIT` 是否被写死为 WalletConnect | 通过 | 仅写作候选 / 分类来源 |
| Deposit success 是否被写死为 Wallet `COMPLETED` | 通过 | 明确禁止等同 |
| Risk Withheld 是否被写死为 Wallet `REJECTED` / `PENDING` / `PROCESSING` | 通过 | 明确禁止等同 |
| `relatedId` 是否被写死关联 Card / GTR / WC | 通过 | 继续 deferred |
| Deposit 通知是否被写成覆盖所有 GTR / WC 场景 | 通过 | 已保留“是否覆盖各子路径待确认” |

## 5. 仍需保留的待确认项

| 编号 | 待确认项 | 影响 |
|---|---|---|
| REFINE-GAP-001 | GTR 是否使用 `FIAT_DEPOSIT=6` | GTR 历史分类未闭环 |
| REFINE-GAP-002 | WalletConnect 是否使用 `CRYPTO_DEPOSIT=10` | WC 历史分类未闭环 |
| REFINE-GAP-003 | GTR / WC 是否都适用 senderAddress whitelist 规则 | 白名单产品规则未闭环 |
| REFINE-GAP-004 | WalletConnect senderAddress 获取方式 | WC 加白路径未闭环 |
| REFINE-GAP-005 | Declare / Travel Rule 触发条件 | 合规流程未闭环 |
| REFINE-GAP-006 | `relatedId` 在 GTR / WC / Card 归集场景下的具体取值 | 对账链路未闭环 |
| REFINE-GAP-007 | Deposit success 与 Wallet `state=COMPLETED` 的关系 | 状态机未闭环 |
| REFINE-GAP-008 | Risk Withheld 与 Wallet `state` 的关系 | 状态机未闭环 |
| REFINE-GAP-009 | Deposit success 后余额何时可见 / 可用 | 余额展示未闭环 |
| REFINE-GAP-010 | Risk Withheld 时是否展示冻结余额 | 余额展示未闭环 |
| REFINE-GAP-011 | GTR / WC 人工处理、客服口径、告警规则 | 异常闭环未完成 |

## 6. 阶段性判断

当前补材料与精修阶段可继续推进。下一步建议进入：

1. Wallet / Transaction 前端展示字段回填。
2. GTR / WalletConnect 页面流程、截图、入口、按钮、状态展示回填。
3. KYC / AAI 外部依赖材料回填。

当前不得进入最终 PASS，除非上述关键待确认项有真实来源或用户明确允许继续保留为 deferred gaps。

## 7. 来源引用

- (Ref: DTC Wallet OpenAPI Document20260126 / 3.4 Crypto Deposit)
- (Ref: DTC Wallet OpenAPI Document20260126 / 4.2.4 Search Balance History)
- (Ref: DTC Wallet OpenAPI Document20260126 / Appendix ActivityType)
- (Ref: [2025-11-25] AIX+Notification / Deposit rows)
- (Ref: knowledge-base/wallet/deposit.md / v1.4)
- (Ref: knowledge-base/wallet/transaction-history.md / v1.1)
- (Ref: knowledge-base/wallet/balance.md / v1.1)
- (Ref: knowledge-base/transaction/status-model.md / v1.1)
- (Ref: knowledge-base/transaction/history.md / v1.1)
- (Ref: knowledge-base/transaction/detail.md / v1.1)
- (Ref: knowledge-base/common/dtc.md / v1.3)
