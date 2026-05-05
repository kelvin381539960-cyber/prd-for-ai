---
module: card
feature: card-manage-index
version: "1.0"
status: active
source_doc: archive/historical-prd/card/AIX Card 【manage】模块需求V1.0 .docx；external-docs/dtc/DTC Card Issuing API Document_20260310 (1).docx；knowledge-base/changelog/knowledge-gaps.md
source_section: Card Manage module；Manage 6.4 / 7.1 / 7.2 / 7.3 / 7.4 / 7.5 / 8.1
last_updated: 2026-05-05
owner: 吴忆锋
readers: [product, ui, dev, qa, business, ai]
---

# Card Manage 模块索引

## 1. 模块定位

`card/manage/` 承接原始 PRD `AIX Card 【manage】模块需求V1.0 .docx` 中的卡管理能力。

Card Manage 只维护卡管理相关事实，不承接申卡、Card Home、Card Transaction 或全局 Transaction & History。

## 2. 当前文件

| 文件 | 状态 | 定位 | 主要来源 |
|---|---|---|---|
| `card/manage/_index.md` | active | Card Manage 索引 | Manage 模块整体 |
| `card/manage/status-and-operations.md` | active | 卡状态、操作限制矩阵、Lock / Unlock / Terminate 边界 | Manage 6.4 / 7.4 / 7.5 |
| `card/manage/activation.md` | active | 实体卡激活、后四位校验、激活后续流转 | Manage 7.2 / DTC Activation |
| `card/manage/sensitive-info.md` | active | Card detail、敏感信息查看、PAN / EXP / CVV / CVC | Manage 7.1 / DTC Sensitive Info |
| `card/manage/pin.md` | active | Set PIN、Change PIN、Reset PIN、OTP 与 PIN 公钥 | Manage 7.3 / DTC PIN APIs |

## 3. 与 Card 其他文件的边界

| 文件 | 关系 | 边界 |
|---|---|---|
| `card/application.md` | 申卡和卡计划 | Manage 不维护申卡流程 |
| `card/card-home.md` | Card 模块首页 | Manage 只维护从 Card Home 进入的管理动作 |
| `card/transaction.md` | Card 交易 | Manage 不维护 Card Transaction Notify 或交易归集 |
| `transaction/*` | 全局交易历史、详情、状态、对账 | Manage 不维护统一交易模块 |

## 4. 查询入口规则

| 查询主题 | 优先读取 |
|---|---|
| 卡状态 / 操作权限 / Lock / Unlock / Terminate 边界 | `card/manage/status-and-operations.md` |
| 实体卡激活 / 后四位校验 | `card/manage/activation.md` |
| PAN / EXP / CVV / CVC / Card detail | `card/manage/sensitive-info.md` |
| Set PIN / Change PIN / Reset PIN / PIN OTP | `card/manage/pin.md` |
| Card 交易通知 / Card 交易展示 | `card/transaction.md` |

## 5. 不写入事实的内容

1. 不把 Card Transaction 写进 Manage。
2. 不把全局 Transaction & History 写进 Manage。
3. 不把 Terminate Card 写成独立 PRD 文件；只作为操作矩阵和待确认边界维护。
4. 不把旧 Card Manage 合并文件 当作运行态入口。

## 6. 来源引用

- (Ref: archive/historical-prd/card/AIX Card 【manage】模块需求V1.0 .docx)
- (Ref: external-docs/dtc/DTC Card Issuing API Document_20260310 (1).docx)
- (Ref: knowledge-base/card/manage/status-and-operations.md)
- (Ref: knowledge-base/card/manage/activation.md)
- (Ref: knowledge-base/card/manage/sensitive-info.md)
- (Ref: knowledge-base/card/manage/pin.md)
- (Ref: knowledge-base/changelog/knowledge-gaps.md)
