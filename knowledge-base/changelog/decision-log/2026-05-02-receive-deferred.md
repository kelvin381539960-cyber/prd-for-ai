---
decision_id: 2026-05-02-receive-deferred
module: wallet
decision_date: 2026-05-02
status: active
source_type: pm-fix
---

# 2026-05-02 Receive 状态降级决策

## 决策

Wallet Receive 当前不作为独立 active 功能事实源，状态降级为 deferred / placeholder。

## 原因

现有来源中，“Receive Crypto”主要出现在 GTR / Exchange 地址充值路径中，不能直接证明存在独立上线的 Receive 产品能力。

## 影响范围

- `knowledge-base/wallet/receive.md` 仅保留为占位与核验清单。
- 查询当前 Deposit 地址充值能力时，应读取 `knowledge-base/wallet/deposit.md`。
- 任何 Receive 独立入口、页面、地址字段、支持币种 / 链、memo/tag、状态、通知，都必须通过新来源确认后才能升为 active 事实。

## 后续升级条件

Receive 如需恢复 active，必须满足：

1. 有明确 PRD 或实现文档证明 Receive 独立上线。
2. 明确 Receive 与 Deposit 的关系。
3. 明确地址来源、币种 / 网络、memo/tag、交易记录、余额和通知规则。
4. 更新 ALL-GAP-059 / 060 / 061 / 062。