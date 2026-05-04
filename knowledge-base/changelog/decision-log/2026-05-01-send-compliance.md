---
decision_id: 2026-05-01-send-compliance
module: wallet
decision_date: 2026-05-01
status: active
source_type: user-confirmed
---

# 2026-05-01 Send / Withdraw 合规上线决策

## 决策

Wallet Send / Withdraw 因合规原因未上线，当前不得作为 AIX Wallet active 功能事实源。

## 影响范围

- `knowledge-base/wallet/send.md` 仅作为 deferred 占位文件。
- 旧 Send / Withdraw PRD、流程、字段、状态、风控、通知，不得直接写入当前正式事实层。
- 如后续重新上线 Send / Withdraw，必须基于新的 PRD、接口文档、合规结论和用户确认重新转译。

## 不影响范围

- Wallet Balance 作为钱包余额基础能力继续保留。
- Wallet Deposit 作为当前 active 入金能力继续保留。
- Transaction History 作为统一交易历史主事实源继续保留。