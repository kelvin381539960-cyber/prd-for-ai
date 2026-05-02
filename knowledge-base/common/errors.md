---
module: common
feature: errors
version: "1.1"
status: active
source_doc: IMPLEMENTATION_PLAN.md；knowledge-base/common/_index.md；knowledge-base/common/dtc.md；knowledge-base/common/walletconnect.md；knowledge-base/common/notification.md；knowledge-base/wallet/deposit.md；knowledge-base/card/card-transaction-flow.md；knowledge-base/wallet/stage-review.md；knowledge-base/transaction/stage-review.md；knowledge-base/changelog/knowledge-gaps.md
source_section: IMPLEMENTATION_PLAN v4.1 / 全仓库回扫；Common Index v2.0；DTC Integration v1.0；WalletConnect v1.1；Notification v1.1；Wallet Deposit v1.3；Card Transaction Flow v1.2
last_updated: 2026-05-01
owner: 吴忆锋
depends_on:
  - common/_index
  - common/dtc
  - common/walletconnect
  - common/notification
  - wallet/deposit
  - card/card-transaction-flow
  - wallet/stage-review
  - transaction/stage-review
  - changelog/knowledge-gaps
---

# Common Errors 错误处理公共能力

## 1. 功能定位

Common Errors 用于沉淀 AIX 跨模块错误处理边界，包括 DTC 错误码、系统异常、网络异常、风控 / on-hold、告警、人工处理和用户提示。

本文只记录已确认的错误处理事实和边界，不补写未确认错误码、用户文案或自动补偿策略。

## 2. 已确认错误处理事实

| 场景 | 当前结论 | 来源 | 备注 |
|---|---|---|---|
| Card 归集失败 | 不自动重试，发送异常告警至监控群 | Card Transaction Flow | 已确认 |
| DTC transfer 成功但 Wallet 未到账 | 当前无法系统自动发现，主要依赖用户反馈 | Card Transaction Flow | 已确认 |
| Card balance 查询失败 | 处理规则未确认 | Card / knowledge-gaps | deferred |
| WalletConnect 风控 / on-hold / rejected | 规则未确认 | WalletConnect | 待补 |
| Deposit GTR / WalletConnect 失败原因 | 未补齐 | Wallet Deposit / Wallet Stage Review | 待补 |
| Send / Swap 错误处理 | 不归档 active | Wallet Stage Review | 功能 deferred |

## 3. Deposit 错误边界

Deposit 当前 active，包含 GTR 与 WalletConnect。错误处理必须按子路径拆开，不得默认共用。

| 错误 / 异常场景 | GTR | WalletConnect | 当前处理 |
|---|---|---|---|
| 入金发起失败 | 待补 | 待补 | 不写用户提示 |
| 入金处理中失败 | 待补 | 待补 | 不写状态映射 |
| on-hold | 待补 | 待补 | 不写处理路径 |
| risk rejected | 待补 | 待补 | 不写用户提示 |
| Declare / Travel Rule 异常 | 待补 | 待补 | 不写处理规则 |
| 白名单异常 | 待补 | 待补 | 不写处理规则 |
| Wallet balance 未更新 | 待补 | 待补 | 不写自动发现 / 自动补偿 |
| 通知失败 | 待补 | 待补 | 不写补发策略 |

## 4. WalletConnect 专属错误边界

| 错误 / 异常 | 当前处理 |
|---|---|
| 用户取消连接 | 待补，不写用户提示 |
| 用户拒绝授权 | 待补，不写用户提示 |
| 第三方钱包连接失败 | 待补，不写用户提示 |
| 第三方钱包支付成功但 AIX 未入账 | 待补，不写自动发现能力 |
| DTC risk 拦截 | 待补，不写状态与提示 |
| WalletConnect session 过期 | 待补，不写处理规则 |
| 链 / 币种不支持 | 待补，不写提示文案 |
| 网络异常 | 待补，不写重试策略 |

## 5. DTC 错误码边界

| 项目 | 当前处理 |
|---|---|
| DTC 通用错误码表 | 待补，不写成完整事实 |
| Transfer Balance to Wallet 错误码 | Card Transaction Flow 中已有部分错误码来源，可后续补表 |
| Wallet 错误码 | 待补 |
| GTR / WalletConnect 错误码 | 待补 |
| 错误码与用户提示映射 | 待补，不脑补文案 |

## 6. 告警与人工处理边界

| 场景 | 当前结论 | 未确认项 |
|---|---|---|
| Card 归集失败 | 告警至监控群，不自动重试 | 是否有后台人工补偿入口未确认 |
| DTC transfer 成功但 Wallet 未到账 | 依赖用户反馈发现 | 人工处理路径未确认 |
| 查询 balance 失败 | 待确认 | 是否告警 / 队列 / 人工介入未确认 |
| WalletConnect 入金异常 | 待确认 | on-hold / rejected / Declare 处理未确认 |
| GTR 入金异常 | 待确认 | 失败原因、通知、人工处理未确认 |
| Deposit 余额未更新 | 待确认 | 是否告警、是否自动对账、是否人工补偿未确认 |

## 7. 用户提示边界

| 场景 | 当前处理 |
|---|---|
| 通用网络错误 | 旧 Common 中有通用错误页方向，需后续按 PRD / 截图重写 |
| 通用服务器错误 | 旧 Common 中有通用错误页方向，需后续按 PRD / 截图重写 |
| Card 交易异常 | 不在 Common 中补文案，引用业务 PRD |
| WalletConnect 失败 | 待补，不写用户提示 |
| Deposit 风控拦截 | 待补，不写用户提示 |
| Deposit on-hold | 待补，不写用户提示 |
| KYC 失败 | 待补，不写用户提示 |

## 8. 不写入事实的内容

以下内容不得写成事实：

1. Card 归集失败会自动重试。
2. Card 归集失败一定有后台补偿入口。
3. DTC transfer 成功但 Wallet 未到账可被系统自动发现。
4. Deposit 余额未更新可被系统自动发现。
5. 所有 DTC 错误码都已完成映射。
6. WalletConnect risk rejected 的用户提示已确认。
7. GTR / WalletConnect on-hold 的处理路径已确认。
8. GTR 与 WalletConnect 使用同一套错误码和提示。
9. Send / Swap 的错误处理属于当前 active 范围。
10. 通用错误页文案已确认。
11. 未来源确认的错误码与用户提示映射。

## 9. 待补项

| 编号 | 待补项 | 来源建议 | 当前处理 |
|---|---|---|---|
| ERR-GAP-001 | DTC 通用错误码完整表 | DTC 接口文档 | 待补 |
| ERR-GAP-002 | Transfer Balance to Wallet 错误码映射 | DTC Card Issuing / Card PRD | 待补 |
| ERR-GAP-003 | WalletConnect 错误码与失败原因 | WC PRD / DTC Wallet OpenAPI | 待补 |
| ERR-GAP-004 | GTR Deposit 错误码与失败原因 | GTR PRD / DTC Wallet OpenAPI | 待补 |
| ERR-GAP-005 | 通用错误页文案和展示条件 | Common PRD / 截图 | 待补 |
| ERR-GAP-006 | 告警规则、监控群、责任分派 | 后端 / 运维 / 产品确认 | 待补 |
| ERR-GAP-007 | 人工补偿入口与操作边界 | 后台 PRD / 后端确认 | 待补 |
| ERR-GAP-008 | 用户提示与错误码映射 | PRD / UX / 客服口径 | 待补 |
| ERR-GAP-009 | Deposit 余额未更新发现机制 | 后端 / 账务 / 产品确认 | 待补 |
| ERR-GAP-010 | WalletConnect 用户拒绝授权 / 连接失败提示 | WC PRD / UX | 待补 |

## 10. 来源引用

- (Ref: IMPLEMENTATION_PLAN.md / v4.1 / 全仓库回扫)
- (Ref: knowledge-base/common/_index.md / v2.0)
- (Ref: knowledge-base/common/dtc.md / v1.0)
- (Ref: knowledge-base/common/walletconnect.md / v1.1)
- (Ref: knowledge-base/common/notification.md / v1.1)
- (Ref: knowledge-base/wallet/deposit.md / v1.3)
- (Ref: knowledge-base/card/card-transaction-flow.md / v1.2)
- (Ref: knowledge-base/wallet/stage-review.md / v1.0)
- (Ref: knowledge-base/transaction/stage-review.md / v1.0)
- (Ref: knowledge-base/changelog/knowledge-gaps.md / deferred gaps)
