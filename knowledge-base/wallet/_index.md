---
module: wallet
feature: wallet-index
version: "3.0"
status: active
source_doc: knowledge-base/wallet/deposit.md；knowledge-base/wallet/assets.md；knowledge-base/transaction/history.md；knowledge-base/kyc/account-opening.md；knowledge-base/changelog/knowledge-gaps.md；knowledge-base/_system-boundary.md
source_section: Wallet runtime structure；Assets；Deposit；Transaction；KYC boundary；ALL-GAP
last_updated: 2026-05-05
owner: 吴忆锋
depends_on:
  - wallet/assets
  - wallet/deposit
  - transaction/history
  - kyc/account-opening
  - changelog/knowledge-gaps
  - _system-boundary
---

# Wallet 模块索引

## 1. 模块定位

Wallet 模块用于沉淀 AIX 钱包运行态事实，目前只保留资产展示和入金能力。

## 2. 当前文件

| 文件 | 状态 | 目标 |
|---|---|---|
| `wallet/_index.md` | active | Wallet 模块边界、能力清单与依赖关系 |
| `wallet/assets.md` | active | 钱包首页 My Assets、总资产、稳定币资产、快捷入口与最近交易 |
| `wallet/deposit.md` | active | GTR / Exchange 地址充值与 WalletConnect 入金能力 |

## 3. 使用规则

1. 查询钱包资产页时，读 `wallet/assets.md`
2. 查询入金时，读 `wallet/deposit.md`
3. 查询交易历史时，读 `transaction/history.md`
