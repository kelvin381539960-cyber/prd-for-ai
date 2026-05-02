---
module: wallet
feature: transaction-history
version: "1.2"
status: moved
source_doc: knowledge-base/transaction/history.md；IMPLEMENTATION_PLAN.md；用户确认结论 2026-05-02
source_section: Wallet Transaction History 合并至 Transaction History
last_updated: 2026-05-02
owner: 吴忆锋
depends_on:
  - transaction/history
  - changelog/knowledge-gaps
---

# Wallet Transaction History 已迁移

本文档已迁移为兼容入口，不再维护 Wallet Transaction History 主事实。

主事实源：

`knowledge-base/transaction/history.md`

迁移原因：

1. Transaction History 不是 Wallet 独占能力。
2. 交易历史同时覆盖 Card History、Wallet History、Deposit History、Card refund / reversal / 资金归集等跨模块场景。
3. Wallet 目录只保留钱包产品能力，交易历史统一由 `knowledge-base/transaction/` 承接。

相关 ALL-GAP：

| 编号 | 主题 |
|---|---|
| ALL-GAP-001 | GTR 是否使用 `FIAT_DEPOSIT=6` |
| ALL-GAP-002 | WalletConnect 是否使用 `CRYPTO_DEPOSIT=10` |
| ALL-GAP-007 | `relatedId / transactionId / id` 如何串联 GTR / WalletConnect 入金 |
| ALL-GAP-014 | Wallet `relatedId` 在 Card / GTR / WC 场景取值 |
| ALL-GAP-015 | Wallet `transactionId` 与 Wallet `id` 的关系 |
| ALL-GAP-016 | Deposit success 与 Wallet `state=COMPLETED` 的映射 |
| ALL-GAP-037 | ActivityType 到 AIX 前端交易类型的映射 |

使用规则：

- 新内容写入 `transaction/history.md`。
- 不确定项写入 `knowledge-base/changelog/knowledge-gaps.md`。
- 本文件不再新增交易历史事实或 checklist。

来源引用：

- (Ref: knowledge-base/transaction/history.md / v1.2)
- (Ref: IMPLEMENTATION_PLAN.md / v4.5)
- (Ref: 用户确认结论 / 2026-05-02 / Wallet Transaction History 合并进 Transaction History)
