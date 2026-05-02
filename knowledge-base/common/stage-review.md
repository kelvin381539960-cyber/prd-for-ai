---
module: common
feature: common-stage-review
version: "1.0"
status: active
source_doc: IMPLEMENTATION_PLAN.md；knowledge-base/common/_index.md；knowledge-base/common/dtc.md；knowledge-base/common/notification.md；knowledge-base/common/walletconnect.md；knowledge-base/common/errors.md；knowledge-base/common/aai.md；knowledge-base/common/faq.md；knowledge-base/changelog/knowledge-gaps.md
source_section: Common / Integration 阶段回扫；IMPLEMENTATION_PLAN v4.0；Common Index v2.0；DTC v1.0；Notification v1.0；WalletConnect v1.0；Errors v1.0；AAI v1.0；FAQ v1.0
last_updated: 2026-05-01
owner: 吴忆锋
depends_on:
  - common/_index
  - common/dtc
  - common/notification
  - common/walletconnect
  - common/errors
  - common/aai
  - common/faq
  - changelog/knowledge-gaps
---

# Common / Integration 阶段回扫记录

## 1. 回扫结论

Common / Integration 阶段已完成基础版知识库沉淀，阶段结果为：`PARTIAL PASS`。

含义：

- 已建立 DTC、Notification、WalletConnect、Errors、AAI、FAQ 的公共能力边界。
- 已明确 Common 不重复业务流程，只沉淀公共集成与公共规则边界。
- 已隔离 Send / Swap deferred 能力。
- 已明确不得把 `D-REQUEST-ID` 写成幂等键。
- 已明确不得把 Card / Wallet ID 关联、Wallet `relatedId`、AIX 内部归集字段补写成事实。
- 可以进入全仓库回扫阶段。

## 2. 回扫范围

| 文件 | 状态 | 回扫结果 |
|---|---|---|
| `common/_index.md` | active | 公共能力索引与边界已建立 |
| `common/dtc.md` | active | DTC 请求头、Webhook、Card / Wallet 接口边界已建立 |
| `common/notification.md` | active | Push / 站内信通知边界已建立 |
| `common/walletconnect.md` | active | WalletConnect 入金公共边界已建立 |
| `common/errors.md` | active | 错误处理、告警、人工处理边界已建立 |
| `common/aai.md` | active | AAI / KYC / OCR / Liveness / Face Auth 公共边界已建立 |
| `common/faq.md` | active | FAQ 分类与答复来源边界已建立 |

## 3. 已通过项

| 检查项 | 结果 | 说明 |
|---|---|---|
| Common 模块边界 | 通过 | Common 只承载公共能力，不重写业务流程 |
| DTC 边界 | 部分通过 | 已记录 `D-REQUEST-ID`、Card Notify、Wallet 基础字段；完整错误码和 Wallet 字段待补 |
| Notification 边界 | 部分通过 | 已记录卡交易 / 卡退款通知；Deposit / WC 通知待补 |
| WalletConnect 边界 | 部分通过 | 已确认 WC 属于 Deposit 子路径；完整流程、Declare、白名单、风控待补 |
| Errors 边界 | 部分通过 | 已记录 Card 归集失败不重试、告警监控群；完整错误码和人工补偿待补 |
| AAI 边界 | 部分通过 | 已隔离 Wallet KYC / Card KYC / AAI KYC；完整接口和状态待补 |
| FAQ 边界 | 通过 | 已明确 FAQ 答案必须来自事实源，不脑补客服口径 |
| Deferred gaps 隔离 | 通过 | 未把 Card / Wallet 资金追踪遗留项写成事实 |
| 未上线能力隔离 | 通过 | Send / Swap 未被写成 active 能力 |

## 4. 当前待补问题

| 编号 | 问题 | 影响 | 当前处理 |
|---|---|---|---|
| COMMON-GAP-001 | DTC 通用响应结构和错误码表未补齐 | 错误处理和接口统一层不完整 | 待补 |
| COMMON-GAP-002 | `D-REQUEST-ID` 是否具备幂等语义未确认 | 请求重试 / 去重策略不完整 | deferred |
| COMMON-GAP-003 | WalletConnect 完整入金流程、字段、状态未补齐 | WC 入金公共能力不完整 | 待补 |
| COMMON-GAP-004 | WalletConnect Declare / Travel Rule / 白名单规则未确认 | 合规边界不完整 | 待补 |
| COMMON-GAP-005 | Deposit GTR / WalletConnect 通知规则未补齐 | 通知边界不完整 | 待补 |
| COMMON-GAP-006 | 通知失败重试 / 补发策略未确认 | 通知可靠性不完整 | 待补 |
| COMMON-GAP-007 | 通用错误页、通用弹窗文案和展示条件未补齐 | 用户体验公共层不完整 | 待补 |
| COMMON-GAP-008 | 告警规则、监控群、责任分派、人工补偿入口未补齐 | 运营处理闭环不完整 | 待补 |
| COMMON-GAP-009 | AAI OCR / Liveness / KYC 状态和失败原因未补齐 | 身份认证公共层不完整 | 待补 |
| COMMON-GAP-010 | FAQ 原文和客服口径未补齐 | FAQ 知识库不完整 | 待补 |

## 5. 阶段判断

| 判断项 | 结论 |
|---|---|
| Common 模块边界 | PASS |
| DTC Integration | PARTIAL PASS |
| Notification | PARTIAL PASS |
| WalletConnect | PARTIAL PASS |
| Errors | PARTIAL PASS |
| AAI | PARTIAL PASS |
| FAQ | PARTIAL PASS |
| Deferred gaps 隔离 | PASS |
| 是否允许进入全仓库回扫 | 允许，带待补项继续 |
| 是否允许把待补项写成事实 | 不允许 |

## 6. 后续要求

1. 全仓库回扫阶段可引用 Common 已确认边界。
2. 不得把 Common 待补项写成事实。
3. 不得把 Send / Swap 写成 active 能力。
4. 不得把 `D-REQUEST-ID` 写成幂等键。
5. 不得把 Wallet `transactionId`、Wallet `id`、Wallet `relatedId` 与 Card `data.id` 强行关联。
6. 后续如获得补充材料，应优先回填：
   - DTC 通用错误码与响应结构
   - WalletConnect 入金完整流程
   - Deposit / WC 通知规则
   - AAI OCR / Liveness / KYC 状态
   - 通用错误页 / 弹窗 / FAQ 原文

## 7. 来源引用

- (Ref: IMPLEMENTATION_PLAN.md / v4.0 / Common Integration)
- (Ref: knowledge-base/common/_index.md / v2.0)
- (Ref: knowledge-base/common/dtc.md / v1.0)
- (Ref: knowledge-base/common/notification.md / v1.0)
- (Ref: knowledge-base/common/walletconnect.md / v1.0)
- (Ref: knowledge-base/common/errors.md / v1.0)
- (Ref: knowledge-base/common/aai.md / v1.0)
- (Ref: knowledge-base/common/faq.md / v1.0)
- (Ref: knowledge-base/changelog/knowledge-gaps.md / deferred gaps)
