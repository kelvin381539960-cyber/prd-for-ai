---
module: common
feature: faq
version: "1.0"
status: active
source_doc: IMPLEMENTATION_PLAN.md；knowledge-base/common/_index.md；knowledge-base/card/card-home.md；knowledge-base/card/card-transaction-flow.md；knowledge-base/wallet/stage-review.md；knowledge-base/transaction/stage-review.md
source_section: IMPLEMENTATION_PLAN v4.0 / Common Integration；Common Index v2.0；Card Home FAQ；Card Transaction Flow；Wallet / Transaction Stage Review
last_updated: 2026-05-01
owner: 吴忆锋
depends_on:
  - common/_index
  - card/card-home
  - card/card-transaction-flow
  - wallet/stage-review
  - transaction/stage-review
---

# FAQ 公共问答边界

## 1. 功能定位

FAQ 用于沉淀 AIX 中跨模块或通用场景的问答边界，包括 Card FAQ、Wallet FAQ、交易 FAQ、错误 FAQ、合规 FAQ 等。

本文不直接编写具体 FAQ 答案。具体问答必须来自 PRD、截图、FAQ 原文、客服口径或已确认结论。

## 2. FAQ 分类边界

| 分类 | 当前处理 | 备注 |
|---|---|---|
| Card FAQ | 可引用 Card Home / Card Transaction Flow 已确认内容 | 不补写未确认资金追踪口径 |
| Wallet FAQ | 待补 | Deposit active，但 GTR / WalletConnect 细节待补 |
| Transaction FAQ | 可引用 Transaction 状态 / History / Detail 边界 | 不做状态等价推导 |
| Error FAQ | 待补 | 需引用 common/errors.md |
| Notification FAQ | 待补 | 需引用 common/notification.md |
| WalletConnect FAQ | 待补 | 需引用 common/walletconnect.md |
| KYC / AAI FAQ | 待补 | 需引用 common/aai.md |

## 3. 可引用事实

| 事实 | 来源 | FAQ 处理 |
|---|---|---|
| Card Home 有 FAQ 入口 / 内容基础 | Card Home | 可在 Card FAQ 中引用 |
| Card 退款 / 卡交易通知跳转交易详情 | Card Transaction Flow / Notification | 可用于通知类 FAQ |
| Card 资金归集存在极端异常 | Card Transaction Flow | 只能按已确认口径写，不得扩展 |
| Deposit 包含 GTR / WalletConnect | Wallet Deposit | 可用于 Deposit FAQ 边界 |
| Send / Swap deferred | Wallet Stage Review | 不写成用户可用 FAQ |
| Card / Wallet 状态不强行等价 | Transaction Stage Review | 可用于状态说明边界 |

## 4. 不写入事实的内容

以下内容不得写成 FAQ 答案：

1. 未确认的钱包入金成功 / 失败解释。
2. 未确认的 WalletConnect Declare / Travel Rule 规则。
3. 未确认的 GTR / WalletConnect 白名单规则。
4. 未确认的 Card balance 转 Wallet 对账字段。
5. Send / Swap 当前可用。
6. Card `SUCCESS` 等同 Wallet `COMPLETED`。
7. 通知必然代表 Wallet 已到账。
8. 未来源确认的客服口径。

## 5. 待补项

| 编号 | 待补项 | 来源建议 | 当前处理 |
|---|---|---|---|
| FAQ-GAP-001 | Card FAQ 原文完整整理 | Card PRD / 截图 | 待补 |
| FAQ-GAP-002 | Wallet FAQ 原文完整整理 | Wallet PRD / 截图 | 待补 |
| FAQ-GAP-003 | WalletConnect FAQ | WC PRD / 客服口径 | 待补 |
| FAQ-GAP-004 | Deposit GTR / WalletConnect FAQ | GTR / WC PRD | 待补 |
| FAQ-GAP-005 | Error FAQ | common/errors.md / 客服口径 | 待补 |
| FAQ-GAP-006 | Notification FAQ | common/notification.md / PRD | 待补 |
| FAQ-GAP-007 | KYC / AAI FAQ | common/aai.md / KYC PRD | 待补 |

## 6. 来源引用

- (Ref: IMPLEMENTATION_PLAN.md / v4.0 / Common Integration)
- (Ref: knowledge-base/common/_index.md / v2.0)
- (Ref: knowledge-base/card/card-home.md)
- (Ref: knowledge-base/card/card-transaction-flow.md / v1.2)
- (Ref: knowledge-base/wallet/stage-review.md / v1.0)
- (Ref: knowledge-base/transaction/stage-review.md / v1.0)
