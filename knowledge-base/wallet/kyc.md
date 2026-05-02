---
module: wallet
feature: kyc
version: "1.2"
status: moved
source_doc: knowledge-base/kyc/wallet-kyc.md；IMPLEMENTATION_PLAN.md；用户确认结论 2026-05-02
source_section: KYC 独立目录结构调整
last_updated: 2026-05-02
owner: 吴忆锋
depends_on:
  - kyc/wallet-kyc
  - changelog/knowledge-gaps
---

# Wallet KYC 已迁移

本文档已迁移为兼容入口，不再维护 Wallet KYC 主事实。

主事实源：

`knowledge-base/kyc/wallet-kyc.md`

迁移原因：

1. KYC 不是 Wallet 独占能力。
2. KYC 会影响 Account / Card / Wallet / Deposit / Notification / Errors。
3. Wallet 目录只保留钱包产品能力，KYC 统一由 `knowledge-base/kyc/` 承接。

相关 ALL-GAP：

| 编号 | 主题 |
|---|---|
| ALL-GAP-030 | Wallet KYC 与 Card KYC 关系 |
| ALL-GAP-031 | Wallet KYC 是否为 GTR / WalletConnect Deposit 前置 |
| ALL-GAP-032 | Wallet 开户触发时机 |
| ALL-GAP-033 | KYC 失败 / 重试 / 人工处理规则 |
| ALL-GAP-034 | KYC 结果是否触发通知 |
| ALL-GAP-035 | AIX 实际依赖哪些 AAI 结果 |

使用规则：

- 新内容写入 `kyc/wallet-kyc.md`。
- 不确定项写入 `knowledge-base/changelog/knowledge-gaps.md`。
- 本文件不再新增 KYC 事实或 checklist。

来源引用：

- (Ref: knowledge-base/kyc/wallet-kyc.md / v1.0)
- (Ref: IMPLEMENTATION_PLAN.md / v4.5)
- (Ref: 用户确认结论 / 2026-05-02 / KYC 独立，common/aai.md 不迁移)
