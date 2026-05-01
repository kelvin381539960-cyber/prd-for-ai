---
module: card
feature: card-stage-review
version: "1.0"
status: active
source_doc: IMPLEMENTATION_PLAN.md；knowledge-base/card/_index.md；knowledge-base/card/card-transaction-flow.md；knowledge-base/changelog/knowledge-gaps.md
source_section: Card 阶段回扫
last_updated: 2026-05-01
owner: 吴忆锋
depends_on:
  - card/_index
  - card/application
  - card/card-status-and-fields
  - card/card-home
  - card/activation
  - card/pin
  - card/sensitive-info
  - card/card-management
  - card/card-transaction-flow
  - changelog/knowledge-gaps
---

# Card 阶段回扫记录

## 1. 回扫结论

Card 模块主文件已完成，但当前不建议直接进入 Wallet 批量推进。

阻塞原因是 `card-transaction-flow.md` 涉及资金归集，当前仍缺少完整可追溯字段闭环。资金路径缺少通知原始交易 ID、归集流水、钱包入账流水、幂等字段和重试字段，不能判断是否满足资金链路可追溯要求。

## 2. 回扫范围

| 文件 | 状态 | 回扫结果 |
|---|---|---|
| `_index.md` | active | 功能清单已收口 |
| `application.md` | active | 申卡流程已完成，资金字段缺口已记录 |
| `card-status-and-fields.md` | active | 状态与字段事实源已建立 |
| `card-home.md` | active | 首页展示与入口已完成 |
| `activation.md` | active | 实体卡激活已完成 |
| `pin.md` | active | PIN 能力已完成 |
| `sensitive-info.md` | active | 卡信息安全查看已完成 |
| `card-management.md` | active | 卡管理能力已完成 |
| `card-transaction-flow.md` | active | 卡交易关联流程已完成，但资金可追溯缺口阻塞阶段完成 |

## 3. 已通过项

| 检查项 | 结果 | 说明 |
|---|---|---|
| 模块边界 | 通过 | Card 与 Security、Wallet、Transaction 边界基本清晰 |
| 状态引用 | 通过 | 后续文件均要求引用 `card-status-and-fields.md` |
| 页面入口 | 通过 | Card Home、Activation、PIN、Sensitive Info、Management 入口已拆分 |
| Security 复用 | 通过 | Face Authentication、OTP、设备认证均引用 Security，不重复定义 |
| 无来源补写 | 基本通过 | 不可读状态表、接口字段、错误码均以缺口处理 |

## 4. 阻塞问题

### 4.1 资金路径不可追溯

| 问题 | 影响 | 当前处理 |
|---|---|---|
| Card Transaction Notification 原始交易 ID 未明确 | 无法关联 DTC 通知和后续处理 | 记录缺口 |
| Transfer Balance to Wallet 返回字段未明确 | 无法确认归集结果流水 | 记录缺口 |
| 钱包入账流水 ID 未明确 | 无法关联钱包到账 | 记录缺口 |
| 幂等字段 / 重试字段未明确 | 无法防止重复归集或漏归集 | 记录缺口 |
| 查询余额失败处理未明确 | 无法闭环异常分支 | 记录缺口 |

### 4.2 接口路径与字段缺口

| 问题 | 影响 | 当前处理 |
|---|---|---|
| Card Transaction Notification 接口地址未完整呈现 | 研发对接不完整 | 记录缺口 |
| Retrieve Basic Card Info 实际接口路径待确认 | 查询余额实现不确定 | 记录缺口 |
| Card Transaction Detail Inquiry 路径格式待确认 | 交易详情接口实现不确定 | 记录缺口 |

## 5. 需要补充的信息

| 编号 | 需补充信息 | 建议来源 |
|---|---|---|
| CARD-REVIEW-001 | DTC Card Transaction Notification 完整字段表 | DTC 接口文档 |
| CARD-REVIEW-002 | 通知原始交易 ID 与 AIX 内部交易 ID 映射规则 | 后端 / DTC |
| CARD-REVIEW-003 | Transfer Balance to Wallet 请求、响应、失败码 | DTC 接口文档 |
| CARD-REVIEW-004 | 钱包入账流水 ID 与归集请求 ID 关联规则 | Wallet / 后端 |
| CARD-REVIEW-005 | 幂等键、重试策略、重复通知处理规则 | 后端 / DTC |
| CARD-REVIEW-006 | 查询卡余额失败后的重试与告警策略 | 后端 / 运维 |

## 6. 阶段判断

| 判断项 | 结论 |
|---|---|
| Card 页面类能力 | 可作为阶段完成 |
| Card 状态与字段事实源 | 可作为阶段完成 |
| Card 资金归集链路 | 暂不闭环 |
| 是否进入 Wallet 批量推进 | 暂缓 |

## 7. 后续建议

先补齐 Card Transaction Flow 的资金追踪字段和接口缺口。

补齐后再执行一次 Card 阶段回扫。只有资金链路可追溯、状态闭环、接口路径明确后，再进入 Wallet 批量推进。

## 8. 来源引用

- (Ref: IMPLEMENTATION_PLAN.md / v2.9 / Card 阶段回扫)
- (Ref: knowledge-base/card/_index.md / Card 功能清单 / 2026-05-01)
- (Ref: knowledge-base/card/card-transaction-flow.md / 6.3 可追溯性当前状态 / 2026-05-01)
- (Ref: knowledge-base/card/card-transaction-flow.md / 8 字段与接口依赖 / 2026-05-01)
- (Ref: knowledge-base/card/card-transaction-flow.md / 9 异常与失败处理 / 2026-05-01)
