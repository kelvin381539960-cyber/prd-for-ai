---
decision_id: 2026-05-02-deposit-active
module: wallet
decision_date: 2026-05-02
status: active
source_type: user-confirmed
---

# 2026-05-02 Wallet Deposit active 决策

## 决策

Wallet Deposit 当前为 active 能力，包含两条已确认入金路径：

1. GTR / Exchange 地址充值。
2. WalletConnect / Self-custodial Wallet 充值。

## 影响范围

- `knowledge-base/wallet/deposit.md` 作为 Wallet Deposit 主事实源。
- Deposit 不受 Send / Withdraw deferred 状态传导影响。
- Deposit 应按 GTR 与 WalletConnect 两条产品路径分别维护页面、接口、白名单、状态、异常和结果页边界。

## 关键边界

- GTR 与 WalletConnect 不得默认共用字段、状态、白名单或结果页规则。
- GTR / WalletConnect 与 Wallet `state`、ActivityType、`relatedId` / `transactionId` / `id` 的映射，未确认项继续进入 ALL-GAP。
- WalletConnect 对客授权有效期按 1 天；DTC 7 天免连接仅为内部逻辑，不作为 AIX 对客有效期。