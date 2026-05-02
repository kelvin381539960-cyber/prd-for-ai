---
module: common
feature: common-index
version: "3.0"
status: active
source_doc: knowledge-base/common/dtc.md；knowledge-base/common/aai.md；knowledge-base/common/walletconnect.md；knowledge-base/common/errors.md；knowledge-base/common/notification.md；knowledge-base/common/faq.md；knowledge-base/changelog/knowledge-gaps.md；knowledge-base/_system-boundary.md
source_section: runtime common integration boundary；external dependency boundary；ALL-GAP usage
last_updated: 2026-05-02
owner: 吴忆锋
depends_on:
  - common/dtc
  - common/aai
  - common/walletconnect
  - common/errors
  - common/notification
  - common/faq
  - changelog/knowledge-gaps
  - _system-boundary
---

# Common / Integration 公共能力索引

## 1. 模块定位

Common / Integration 用于沉淀跨模块复用的公共能力和外部依赖边界，包括 DTC、AAI、WalletConnect、错误处理、通知、FAQ、通用弹窗等。

本模块不是业务流程的再次归档，也不是供应商系统说明书。Account、Security、Card、Wallet、Transaction 中已经确认的业务事实，不在 Common 中重复定义。

Common 只沉淀：

1. AIX 侧实际使用到的公共能力。
2. AIX 对外部供应商的依赖边界。
3. AIX 依赖的外部字段、状态、回调、错误和通知规则。
4. AIX 侧已确认或待确认的处理边界。

## 2. 当前文件

| 文件 | 状态 | 目标 | 备注 |
|---|---|---|---|
| `common/_index.md` | active | 建立公共能力索引与边界 | 当前文件 |
| `common/dtc.md` | active | 记录 AIX 对 DTC 的外部依赖边界 | DTC 是供应商系统，不维护其内部逻辑 |
| `common/aai.md` | active | 记录 AIX 对 AAI 的外部依赖边界 | AAI 是供应商能力，不维护其内部逻辑 |
| `common/walletconnect.md` | active | 汇总 WalletConnect 入金相关公共能力边界 | 与 Wallet Deposit 配合读取 |
| `common/errors.md` | active | 汇总错误码、失败处理、告警、用户提示边界 | 不自行补完整错误码表 |
| `common/notification.md` | active | 汇总 push / 站内信通知规则边界 | 不把通知写成必然到账 |
| `common/faq.md` | active | 汇总 APP 通用 FAQ 与场景 FAQ | 只使用原文或已确认口径 |

## 3. 公共能力与外部依赖边界

| 能力域 | Common 中沉淀 | 不在 Common 中维护 |
|---|---|---|
| DTC | AIX 调用的 DTC 能力、AIX 依赖的 DTC 字段 / 状态 / Webhook / 响应边界 | DTC 内部系统逻辑、DTC 完整产品说明、DTC 未提供字段 |
| AAI | AIX 使用的 AAI OCR / Liveness / KYC / Face Auth 外部依赖边界 | AAI 内部审核逻辑、AAI 完整系统说明、AAI 未提供字段 |
| WalletConnect | WC 入金、连接、失败原因、第三方钱包交互边界 | GTR / Card 自动归集 / Send |
| Error | 通用错误码、系统失败、网络失败、告警、人工处理边界 | 单业务特有错误流程 |
| Notification | Push、站内信、通知触发源、模板参数、跳转目标 | 业务流程正文 |
| FAQ | 通用 FAQ 与跨模块 FAQ | 单页面业务文案 |

## 4. 已确认可引用事实

| 事实 | 来源 | Common 处理 |
|---|---|---|
| Card Transaction Notify 已明确 | Card Transaction Flow | 可在 `common/dtc.md` 中作为 DTC Webhook 依赖引用 |
| `D-REQUEST-ID` 是 DTC API 请求唯一标识 Header | DTC Card Issuing / Card Transaction Flow | 可在 `common/dtc.md` 中记录；不得写成幂等键 |
| Transfer Balance to Wallet 请求字段为 `cardId` / `amount` | DTC Card Issuing / Card Transaction Flow | 仅作为 AIX 依赖的 DTC Card 能力，不重写业务流程 |
| Wallet 交易 `id`、`transactionId`、`state` 已确认 | DTC Wallet OpenAPI / Transaction History | 可作为 AIX 依赖的 DTC Wallet 字段 |
| Deposit 包含 GTR / WalletConnect | Wallet Deposit | 可在 `common/walletconnect.md` 中聚焦 WC 边界 |
| Send / Swap deferred | Wallet / Transaction 模块事实 | Common 中不得把其写成 active 能力 |

## 5. Deferred gaps 隔离

以下内容不得在 Common 中补写为事实：

| Deferred gap | 当前处理 |
|---|---|
| AIX 内部交易处理 ID | 保留在 `knowledge-gaps.md` |
| AIX 归集请求 ID | 保留在 `knowledge-gaps.md` |
| Wallet `relatedId` 在 Card balance 转 Wallet 场景下取值 | 保留在 `knowledge-gaps.md` |
| Wallet 交易 `id` 与 Card `data.id` / AIX 归集请求 / `D-REQUEST-ID` 的关联 | 保留在 `knowledge-gaps.md` |
| DTC `D-REQUEST-ID` 是否具备幂等语义 | 未确认，不写成事实 |
| GTR / WalletConnect 完整状态机 | 待确认，不写成事实 |
| Receive 是否独立上线 | 待确认，不写成事实 |
| Wallet KYC 完整流程 | 待确认，不写成事实 |
| Send / Swap 当前上线能力 | deferred，不写成事实 |

## 6. 使用规则

1. 查询 Common 公共能力时，先读本索引，再读对应 common 事实文件。
2. 查询外部依赖责任边界时，必须读 `knowledge-base/_system-boundary.md`。
3. 查询未确认项时，只读 `knowledge-base/changelog/knowledge-gaps.md`。
4. 不默认读取建设期 stage-review、checklist 或 migrated-reference 文件。
5. 不在 Common 模块新增 checklist / TODO / gaps 表。

## 7. 来源引用

- (Ref: knowledge-base/common/dtc.md)
- (Ref: knowledge-base/common/aai.md)
- (Ref: knowledge-base/common/walletconnect.md)
- (Ref: knowledge-base/common/errors.md)
- (Ref: knowledge-base/common/notification.md)
- (Ref: knowledge-base/common/faq.md)
- (Ref: knowledge-base/changelog/knowledge-gaps.md / ALL-GAP 总表)
- (Ref: knowledge-base/_system-boundary.md)
