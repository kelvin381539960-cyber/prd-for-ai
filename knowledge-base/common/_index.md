---
module: common
feature: common-index
version: "3.0"
status: active
source_doc: knowledge-base/integrations/dtc/_index.md；knowledge-base/integrations/aai/_index.md；knowledge-base/integrations/walletconnect/_index.md；knowledge-base/common/errors.md；knowledge-base/common/notification.md；knowledge-base/common/faq.md；knowledge-base/changelog/knowledge-gaps.md；knowledge-base/_system-boundary.md
source_section: runtime common integration boundary；external dependency boundary；ALL-GAP usage
last_updated: 2026-05-02
owner: 吴忆锋
depends_on:
  - integrations/dtc
  - integrations/aai
  - integrations/walletconnect
  - common/errors
  - common/notification
  - common/faq
  - changelog/knowledge-gaps
  - _system-boundary
---

# Common 公共能力索引

## 1. 模块定位

Common 用于沉淀跨模块复用的公共运行态能力，包括错误处理、通知、FAQ、通用弹窗等。DTC、AAI、WalletConnect 等外部依赖边界统一在 `integrations/` 中维护。

本模块不是业务流程的再次归档，也不是供应商系统说明书。Account、Security、Card、Wallet、Transaction 中已经确认的业务事实，不在 Common 中重复定义。

Common 只沉淀：

1. AIX 侧实际使用到的公共能力。
2. AIX 依赖的错误、通知、FAQ 和通用交互规则。
3. AIX 侧已确认或待确认的公共处理边界。

## 2. 当前文件

| 文件 | 状态 | 目标 | 备注 |
|---|---|---|---|
| `common/_index.md` | active | 建立公共能力索引与边界 | 当前文件 |
| `common/errors.md` | active | 汇总错误码、失败处理、告警、用户提示边界 | 不自行补完整错误码表 |
| `common/notification.md` | active | 汇总 push / 站内信通知规则边界 | 不把通知写成必然到账 |
| `common/faq.md` | active | 汇总 APP 通用 FAQ 与场景 FAQ | 只使用原文或已确认口径 |

## 3. Common 与 Integrations 分工

| 能力域 | 主维护位置 | 不在 Common 中维护 |
|---|---|---|
| DTC | `integrations/dtc/_index.md` | DTC 内部系统逻辑、DTC 完整产品说明、DTC 未提供字段 |
| AAI | `integrations/aai/_index.md` | AAI 内部审核逻辑、AAI 完整系统说明、AAI 未提供字段 |
| WalletConnect | `integrations/walletconnect/_index.md` | GTR / Card 自动归集 / Send |
| Error | `common/errors.md` | 单业务特有错误流程 |
| Notification | `common/notification.md` | 业务流程正文 |
| FAQ | `common/faq.md` | 单页面业务文案 |

## 4. 已确认可引用事实

| 事实 | 来源 | Common 处理 |
|---|---|---|
| Card Transaction Notify 已明确 | Card Transaction Flow | 可在 `integrations/dtc/_index.md` 中作为 DTC Webhook 依赖引用 |
| `D-REQUEST-ID` 是 DTC API 请求唯一标识 Header | DTC Card Issuing / Card Transaction Flow | 可在 `integrations/dtc/_index.md` 中记录；不得写成幂等键 |
| Transfer Balance to Wallet 请求字段为 `cardId` / `amount` | DTC Card Issuing / Card Transaction Flow | 仅作为 AIX 依赖的 DTC Card 能力，不重写业务流程 |
| Wallet 交易 `id`、`transactionId`、`state` 已确认 | DTC Wallet OpenAPI / Transaction History | 可作为 AIX 依赖的 DTC Wallet 字段 |
| Deposit 包含 GTR / WalletConnect | Wallet Deposit | 可在 `integrations/walletconnect/_index.md` 中聚焦 WC 边界 |

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

## 6. 使用规则

1. 查询 Common 公共能力时，先读本索引，再读对应 common 事实文件。
2. 查询外部依赖责任边界时，必须读 `knowledge-base/_system-boundary.md`。
3. 查询未确认项时，只读 `knowledge-base/changelog/knowledge-gaps.md`。
4. 不默认读取建设期 stage-review、checklist 或 migrated-reference 文件。
5. 不在 Common 模块新增 checklist / TODO / gaps 表。

## 7. 来源引用

- (Ref: knowledge-base/integrations/dtc/_index.md)
- (Ref: knowledge-base/integrations/aai/_index.md)
- (Ref: knowledge-base/integrations/walletconnect/_index.md)
- (Ref: knowledge-base/common/errors.md)
- (Ref: knowledge-base/common/notification.md)
- (Ref: knowledge-base/common/faq.md)
- (Ref: knowledge-base/changelog/knowledge-gaps.md / ALL-GAP 总表)
- (Ref: knowledge-base/_system-boundary.md)
