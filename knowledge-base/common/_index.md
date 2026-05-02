---
module: common
feature: common-index
version: "2.0"
status: active
source_doc: IMPLEMENTATION_PLAN.md；knowledge-base/transaction/stage-review.md；knowledge-base/wallet/stage-review.md；knowledge-base/card/stage-review.md；knowledge-base/changelog/knowledge-gaps.md
source_section: IMPLEMENTATION_PLAN v4.0 / Common Integration；Transaction Stage Review v1.0；Wallet Stage Review v1.0；Card Stage Review v1.3
last_updated: 2026-05-01
owner: 吴忆锋
depends_on:
  - transaction/stage-review
  - wallet/stage-review
  - card/stage-review
  - changelog/knowledge-gaps
  - _meta/writing-standard
---

# Common / Integration 公共能力索引

## 1. 模块定位

Common / Integration 用于沉淀跨模块复用的公共能力和集成边界，包括 DTC、AAI、WalletConnect、错误处理、通知、FAQ、通用弹窗等。

本模块不是业务流程的再次归档。Account、Security、Card、Wallet、Transaction 中已经确认的业务事实，不在 Common 中重复定义；Common 只沉淀可复用能力、公共接口边界、错误处理和通知规则。

## 2. 当前阶段任务

| 文件 | 状态 | 目标 | 备注 |
|---|---|---|---|
| `common/_index.md` | active | 建立公共能力索引与边界 | 当前文件 |
| `common/dtc.md` | Todo | 汇总 DTC 接口、状态、错误码、请求头、Webhook 边界 | 后续执行 |
| `common/aai.md` | Todo | 汇总 AAI / KYC / 身份认证相关公共能力边界 | 后续执行 |
| `common/walletconnect.md` | Todo | 汇总 WalletConnect 入金相关公共能力边界 | 后续执行 |
| `common/errors.md` | Todo | 汇总错误码、失败处理、告警、用户提示边界 | 后续执行 |
| `common/notification.md` | Todo | 汇总 push / 站内信通知规则边界 | 后续执行 |
| `common/faq.md` | Todo | 汇总 APP 通用 FAQ 与场景 FAQ | 后续执行 |
| `common/stage-review.md` | Todo | Common / Integration 阶段完成后执行 Stage Review | 后续执行 |

## 3. 公共能力边界

| 能力域 | Common 中沉淀 | 不在 Common 中重复定义 |
|---|---|---|
| DTC | 请求头、签名、Webhook、通用响应码、接口分组、跨模块字段边界 | Card / Wallet 具体业务流程 |
| AAI | KYC / OCR / Liveness / Face Auth 等公共集成边界 | Card 申卡或 Wallet KYC 的业务规则 |
| WalletConnect | WC 入金、连接、失败原因、第三方钱包交互边界 | GTR / Card 自动归集 / Send |
| Error | 通用错误码、系统失败、网络失败、告警、人工处理边界 | 单业务特有错误流程 |
| Notification | Push、站内信、通知触发源、模板参数、跳转目标 | 业务流程正文 |
| FAQ | 通用 FAQ 与跨模块 FAQ | 单页面业务文案 |

## 4. 已确认可引用事实

| 事实 | 来源 | Common 处理 |
|---|---|---|
| Card Transaction Notify 已明确 | Card Transaction Flow | 可在 `common/dtc.md` 中作为 DTC Webhook 示例引用 |
| `D-REQUEST-ID` 是 DTC API 请求唯一标识 Header | Card Transaction Flow / DTC Card Issuing | 可在 `common/dtc.md` 中记录；不得写成幂等键 |
| Transfer Balance to Wallet 请求字段为 `cardId` / `amount` | Card Transaction Flow | 仅作为 DTC Card 接口示例，不重写业务流程 |
| Wallet 交易 `id`、`transactionId`、`state` 已确认 | Wallet Transaction History | 可作为 DTC Wallet 公共字段示例 |
| Deposit 包含 GTR / WalletConnect | Wallet Deposit | 可在 `common/walletconnect.md` 中聚焦 WC 边界 |
| Send / Swap deferred | Wallet Stage Review | Common 中不得把其写成 active 能力 |
| Card / Wallet / Transaction 阶段均为 PARTIAL PASS | 各 Stage Review | Common 只能引用已确认部分 |

## 5. Deferred gaps 隔离

以下内容不得在 Common 中补写为事实：

| Deferred gap | 当前处理 |
|---|---|
| AIX 内部交易处理 ID | 保留在 `knowledge-gaps.md` |
| AIX 归集请求 ID | 保留在 `knowledge-gaps.md` |
| Wallet `relatedId` 在 Card balance 转 Wallet 场景下取值 | 保留在 `knowledge-gaps.md` |
| Wallet 交易 `id` 与 Card `data.id` / AIX 归集请求 / `D-REQUEST-ID` 的关联 | 保留在 `knowledge-gaps.md` |
| DTC `D-REQUEST-ID` 是否具备幂等语义 | 未确认，不写成事实 |
| GTR / WalletConnect 完整状态机 | 待补，不写成事实 |
| Receive 是否独立上线 | 待补，不写成事实 |
| Wallet KYC 完整流程 | 待补，不写成事实 |
| Send / Swap 当前上线能力 | deferred，不写成事实 |

## 6. 旧 Common 内容迁移口径

原 Common 旧索引中包含：

- 通用错误页
- 通用弹窗
- FAQ
- 通知内容

这些能力继续保留在 Common 范围内，但需按当前知识库标准重写：必须记录来源、适用场景、触发条件和边界，不得只写泛泛说明。

## 7. 转译顺序建议

| 顺序 | 文件 | 原因 |
|---|---|---|
| 1 | `common/dtc.md` | DTC 是 Card / Wallet / Transaction 的核心接口来源，应优先统一请求头、Webhook、错误码边界 |
| 2 | `common/notification.md` | Notification 已在 Card 交易通知中出现，需统一 push / 站内信边界 |
| 3 | `common/walletconnect.md` | Deposit 包含 WalletConnect，需拆出 WC 入金边界 |
| 4 | `common/errors.md` | 统一错误码、失败处理、告警、用户提示边界 |
| 5 | `common/aai.md` | 汇总身份认证 / KYC 公共集成边界 |
| 6 | `common/faq.md` | 汇总通用 FAQ 与跨模块 FAQ |
| 7 | `common/stage-review.md` | 执行 Common 阶段回扫 |

## 8. Stage Review 关注点

Common / Integration 阶段完成后必须检查：

1. Common 是否只承载公共能力，没有重复业务流程。
2. DTC / AAI / WalletConnect / Error / Notification 的边界是否清楚。
3. 是否把 deferred gaps 写成事实。
4. 是否把 Send / Swap 写成 active 能力。
5. 是否把 `D-REQUEST-ID` 写成幂等键。
6. 是否把 Card / Wallet ID 关联规则脑补完整。
7. 是否保留旧 Common 能力并按新标准重写。

## 9. 来源引用

- (Ref: IMPLEMENTATION_PLAN.md / v4.0 / Common Integration 当前执行)
- (Ref: knowledge-base/transaction/stage-review.md / v1.0)
- (Ref: knowledge-base/wallet/stage-review.md / v1.0)
- (Ref: knowledge-base/card/stage-review.md / v1.3)
- (Ref: knowledge-base/changelog/knowledge-gaps.md / deferred gaps)
