---
module: common
feature: common-stage-review
version: "1.2"
status: active
source_doc: IMPLEMENTATION_PLAN.md；knowledge-base/common/_index.md；knowledge-base/common/dtc.md；knowledge-base/common/notification.md；knowledge-base/common/walletconnect.md；knowledge-base/common/errors.md；knowledge-base/common/aai.md；knowledge-base/common/faq.md；knowledge-base/kyc/wallet-kyc.md；knowledge-base/transaction/reconciliation.md；knowledge-base/changelog/knowledge-gaps.md；用户确认结论 2026-05-02
source_section: Common / Integration 阶段回扫；IMPLEMENTATION_PLAN v4.6；外部依赖收窄；KYC 独立；Transaction Reconciliation；ALL-GAP 唯一总表
last_updated: 2026-05-02
owner: 吴忆锋
depends_on:
  - common/_index
  - common/dtc
  - common/notification
  - common/walletconnect
  - common/errors
  - common/aai
  - common/faq
  - kyc/wallet-kyc
  - transaction/reconciliation
  - changelog/knowledge-gaps
---

# Common / Integration 阶段回扫记录

## 1. 回扫结论

Common / Integration 阶段已完成基础版知识库沉淀，并已根据补材料阶段收窄外部依赖边界。

本次 Stage Review 结果为：`PARTIAL PASS`。

含义：

- 已建立 DTC、Notification、WalletConnect、Errors、AAI、FAQ 的公共能力边界。
- Common 不重复业务流程，只沉淀公共集成、公共规则和外部依赖边界。
- DTC / AAI 只保留影响 AIX 页面、状态、按钮、准入、通知、错误处理、人工处理、资金追踪、对账的内容。
- AAI 仍保留在 `common/aai.md`，KYC 主事实在 `kyc/wallet-kyc.md`。
- 资金追踪 / 对账边界由 `transaction/reconciliation.md` 承接。
- Send / Swap 继续保持 `deferred`。
- 所有不确定项统一引用 ALL-GAP，不在 Common 模块维护独立 checklist / gaps。

## 2. 回扫范围

| 文件 | 状态 | 回扫结果 |
|---|---|---|
| `common/_index.md` | active | 公共能力索引与边界已建立 |
| `common/dtc.md` | active | DTC 外部依赖边界已收窄，只保留 AIX 系统设计相关内容 |
| `common/notification.md` | active | Push / 站内信通知边界已建立，Deposit 通知已阶段性回填 |
| `common/walletconnect.md` | active | WalletConnect token、WebSocket、create_payment_intent、自动加白、send_payment、payment_info 已阶段性回填 |
| `common/errors.md` | active | WalletConnect 异常分流、Card 归集失败告警、Risk Withheld 边界已阶段性回填 |
| `common/aai.md` | active | AAI 作为外部依赖公共边界保留，不迁移 |
| `common/faq.md` | active | FAQ 已按原文落库，不自行编造新增 |

## 3. 已通过项

| 检查项 | 结果 | 说明 |
|---|---|---|
| Common 模块边界 | 通过 | Common 只承载公共能力和外部依赖，不重写业务流程 |
| 外部依赖收窄 | 通过 | DTC / AAI 不作为供应商说明书维护 |
| Notification 边界 | 部分通过 | Deposit success / under review 已回填；完整触发覆盖仍见 ALL-GAP |
| WalletConnect 边界 | 部分通过 | WC 主流程、自动加白、异常事件已回填；状态映射仍见 ALL-GAP |
| Errors 边界 | 部分通过 | WC 异常分流、归集失败告警已回填；人工补偿和告警覆盖仍见 ALL-GAP |
| AAI 边界 | 部分通过 | AAI 作为外部依赖边界；KYC 主事实已独立到 KYC 模块 |
| FAQ 边界 | 通过 | FAQ 答案来自原文，不脑补客服口径 |
| ALL-GAP 唯一源 | 通过 | 不再维护 Common 模块级 gap 编号 |
| 未上线能力隔离 | 通过 | Send / Swap 未被写成 active 能力 |

## 4. 当前 ALL-GAP 引用

Common 阶段不维护独立 gap。相关不确定项统一引用：

| 编号 | 主题 |
|---|---|
| ALL-GAP-010 | GTR / WalletConnect 是否复用 Deposit success / under review 通知 |
| ALL-GAP-012 | WalletConnect payment_info false / Transaction not found 后续处理 |
| ALL-GAP-013 | WalletConnect 失败是否需要告警 |
| ALL-GAP-021 | D-REQUEST-ID 是否仅是请求唯一标识，还是也承担幂等 / 去重 |
| ALL-GAP-022 | DTC Webhook 原始报文是否完整落库 |
| ALL-GAP-026 | Transfer Balance to Wallet 失败后是否存在后台人工补偿入口 |
| ALL-GAP-027 | DTC transfer 成功但 Wallet 未入账是否有系统对账 / 告警机制 |
| ALL-GAP-034 | KYC 结果是否触发通知 |
| ALL-GAP-035 | AIX 实际依赖哪些 AAI 结果 |
| ALL-GAP-036 | Webhook 原始报文落库规则 |
| ALL-GAP-038 | 通用错误页文案与错误码映射 |
| ALL-GAP-039 | 告警规则、监控群、责任分派 |
| ALL-GAP-040 | FAQ Row 14 无答案 |
| ALL-GAP-043 | DTC 通用响应结构和通用错误码边界 |
| ALL-GAP-044 | WalletConnect Declare / Travel Rule / 白名单规则边界 |
| ALL-GAP-045 | 通知失败重试 / 补发策略 |
| ALL-GAP-046 | AAI OCR / Liveness / KYC 状态和失败原因边界 |
| ALL-GAP-047 | FAQ 原文和客服口径完整性 |

## 5. 旧 COMMON-GAP 映射说明

原 Common Stage Review 中的 COMMON-GAP-001 到 COMMON-GAP-010 已迁入 ALL-GAP 总表，不再作为模块级 checklist 维护。

| 原范围 | 当前处理 |
|---|---|
| COMMON-GAP-001 ~ 002 | 已纳入 ALL-GAP-043、ALL-GAP-021 |
| COMMON-GAP-003 ~ 005 | 已阶段性回填，剩余引用 ALL-GAP-007、008、010、012、044 |
| COMMON-GAP-006 ~ 010 | 已纳入 ALL-GAP-038、039、040、045、046、047 |

## 6. 阶段判断

| 判断项 | 结论 |
|---|---|
| Common 模块边界 | PASS |
| DTC Integration | PARTIAL PASS |
| Notification | PARTIAL PASS |
| WalletConnect | PARTIAL PASS |
| Errors | PARTIAL PASS |
| AAI | PARTIAL PASS |
| FAQ | PARTIAL PASS |
| 外部依赖收窄 | PASS |
| ALL-GAP 唯一源 | PASS |
| 是否允许继续全仓库回扫 | 允许，带 ALL-GAP 继续 |
| 是否允许把 ALL-GAP 写成事实 | 不允许 |

## 7. 后续要求

1. 全仓库回扫阶段可引用 Common 已确认边界。
2. 不得把 Common 未确认项写成事实。
3. 不得把 Send / Swap 写成 active 能力。
4. 不得把 D-REQUEST-ID 写成幂等键。
5. 不得把 Wallet transactionId、Wallet id、Wallet relatedId 与 Card data.id 强行关联。
6. DTC / AAI 不维护完整供应商说明书，只保留 AIX 系统设计相关边界。
7. 所有不确定项只进入 `knowledge-base/changelog/knowledge-gaps.md` 的 ALL-GAP 总表。

## 8. 来源引用

- (Ref: IMPLEMENTATION_PLAN.md / v4.6)
- (Ref: knowledge-base/common/_index.md)
- (Ref: knowledge-base/common/dtc.md / v1.4)
- (Ref: knowledge-base/common/notification.md)
- (Ref: knowledge-base/common/walletconnect.md / v1.3)
- (Ref: knowledge-base/common/errors.md / v1.3)
- (Ref: knowledge-base/common/aai.md / v1.2)
- (Ref: knowledge-base/common/faq.md)
- (Ref: knowledge-base/kyc/wallet-kyc.md / v1.0)
- (Ref: knowledge-base/transaction/reconciliation.md / v1.0)
- (Ref: knowledge-base/changelog/knowledge-gaps.md / ALL-GAP 总表)
- (Ref: 用户确认结论 / 2026-05-02 / 外部依赖只保留 AIX 系统设计相关内容)
