---
module: card
feature: card-index
version: "1.1"
status: active
source_doc: 历史prd/AIX Card V1.0【Application】.pdf；历史prd/AIX Card manage模块需求V1.0.docx；历史prd/AIX Card交易【transaction】.pdf；历史prd/AIX APP V1.0【Home】.pdf；历史prd/AIX APP V1.0【Transaction & History】.pdf
source_section: Card Application / Card Manage / Card Transaction / Home Card / Transaction & History
last_updated: 2026-05-04
owner: 吴忆锋
depends_on:
  - security/_index
  - security/face-authentication
  - wallet/_index
  - transaction/_index
  - integrations/dtc
  - _meta/status-dictionary
  - _meta/field-dictionary
  - _meta/limits-and-rules
  - _meta/writing-standard
---

# Card 卡模块

## 0. 文档信息

| 项 | 内容 |
|---|---|
| 文档类型 | Card 模块知识库索引 / PRD 汇总入口 |
| 当前版本 | 1.1 |
| 文档状态 | active |
| 目标读者 | Product、Design、FE、BE、QA、Risk、Compliance |
| 本次修订 | 收拢 `prd-md-review-comments-2026-05-04.md` 的共性问题：明确事实源分层、补充模板化信息、统一状态与接口事实源引用边界 |
| 维护原则 | 各功能文件按标准 PRD 模板补齐“文档信息、业务流程、页面交互、字段接口、待确认项、验收标准、来源引用”；本索引只维护模块定位、功能清单和依赖关系 |

## 1. 模块定位

Card 模块沉淀 AIX Card 的申请、卡首页、实体卡激活、PIN、卡信息安全查看、卡管理、卡状态、卡字段和卡交易关联流程。

本模块依赖 Account、Wallet、Security、Transaction 和 DTC 能力。Card 模块不得重复定义 Security 已完成的认证规则，敏感操作统一引用 Security 事实源。

## 2. 功能清单

| 功能 | 文件 | 状态 | 说明 | 来源 |
|---|---|---|---|---|
| Card Application | [application.md](./application.md) | active | 申卡流程、资格、卡类型、费用、币种、地区、自动扣款 | AIX Card V1.0【Application】 / 2.1 / 5.1 |
| Card Status & Fields | [card-status-and-fields.md](./card-status-and-fields.md) | active | 卡状态、字段、接口路径和操作限制统一事实源 | AIX Card V1.0【Application】 / 3-4；AIX Card manage模块需求V1.0 / 6.1-6.4 |
| Card Home | [card-home.md](./card-home.md) | active | 卡首页、卡片展示、操作入口、Recent Transactions、物流信息、FAQ | AIX Card V1.0【Application】 / 5.2；AIX APP V1.0【Home】 / 6.1 |
| Card Activation | [activation.md](./activation.md) | active | 实体卡激活、后四位校验、认证、激活接口、Set PIN 入口 | AIX Card manage模块需求V1.0 / 7.2 |
| PIN | [pin.md](./pin.md) | active | Set PIN / Change PIN / Reset PIN、PIN 公钥、OTP For Reset PIN、Reset Card PIN | AIX Card manage模块需求V1.0 / 7.3 |
| Sensitive Info | [sensitive-info.md](./sensitive-info.md) | active | 卡信息安全查看流程、认证边界、展示规则、接口依赖与失败处理 | AIX Card manage模块需求V1.0 / 7.1 |
| Card Management | [card-management.md](./card-management.md) | active | 卡管理操作、状态边界、接口依赖与失败处理 | AIX Card manage模块需求V1.0 / 7.4 / 7.5 / 6.4 |
| Card Transaction Flow | [card-transaction-flow.md](./card-transaction-flow.md) | active | DTC 卡交易通知、目标类型判断、余额查询、归集处理、交易展示边界 | AIX Card交易【transaction】 / 7；Transaction & History / 5.1-5.3 |

## 3. 适用范围

| 维度 | 规则 | 来源 | 备注 |
|---|---|---|---|
| 国家线 | VN / PH / AU | AIX Card V1.0【Application】 / 2.1；AIX Card交易【transaction】 / 5 | 一期国家线 |
| 申卡地区 | Philippines / Vietnam / Australia | AIX Card V1.0【Application】 / 2.1 | 后续可配置 |
| 支持币种 | USDT / USDC / WUSD / FDUSD | AIX Card V1.0【Application】 / 2.1 | 后续可配置 |
| 卡类型 | Virtual Card / Physical Card | AIX Card V1.0【Application】 / 5.1 | 实体卡需单独激活 |
| 品牌 | VISA / MASTER | AIX Card V1.0【Application】 / 4.1 | AIX Card 对应 Brand |
| 费用类型 | application fee / delivery fee | AIX Card V1.0【Application】 / 4.4 | 申请费 / 邮寄费 |
| 自动扣款 | OFF / ON | AIX Card V1.0【Application】 / 4.5；DTC Card Issuing / Card Application | 产品枚举与 DTC 枚举存在差异，统一在 `card-status-and-fields.md` 与 `application.md` 标记为待确认映射 |

## 4. 前置条件

| 条件 | 说明 | 来源 |
|---|---|---|
| 钱包已开通 | 用户必须完成 DTC 渠道开户和 KYC 验证通过 | AIX Card V1.0【Application】 / 2.1 |
| 刷脸 Token 有效 | Card Application 需完成刷脸 Token 验证 | AIX Card V1.0【Application】 / 2.1 / 2.2 |
| 申卡数量未达上限 | 用户申卡数量限制为 5 张，统计待激活、已激活、审核中、已冻结之和 | AIX Card V1.0【Application】 / 5.1.4 |
| 单在途限制 | 一个用户可申请多张卡，但仅可一张在途 | AIX Card V1.0【Application】 / 2.1 |
| 费用处理完成 | 有减免费时直接开卡；无减免费时需余额足够覆盖制卡费 | AIX Card V1.0【Application】 / 2.1 |
| 卡状态允许操作 | 卡相关操作均受卡状态限制 | AIX Card manage模块需求V1.0 / 6.4 |
| 交易通知可接收 | DTC 可通过 Card Transaction Notification 通知 AIX | AIX Card交易【transaction】 / 7.3 |

## 5. 业务流程

```text
Wallet Opened + KYC Passed → Face Authentication → Card Application → Card Status & Fields → Card Home → Card Manage / Card Transaction Flow
```

## 6. 页面关系总览

```mermaid
flowchart LR
    Entry[Card Entry]
    Application[Card Application]
    Status[Card Status & Fields]
    Home[Card Home]
    Activation[Activation]
    PIN[PIN]
    Sensitive[Sensitive Info]
    Management[Card Management]
    Txn[Card Transaction Flow]

    Entry --> Application
    Application --> Status
    Status --> Home
    Home --> Activation
    Home --> PIN
    Home --> Sensitive
    Home --> Management
    Home --> Txn
```

## 7. 事实源分层与依赖关系

| 类型 | 文件 / 来源 | 用途 | 处理规则 |
|---|---|---|---|
| 本次已验证事实 | AIX Card Application、AIX Card Manage、DTC Card Issuing API | 申卡、卡管理、状态操作、DTC 接口字段 | 可写入正文事实；若与旧知识库冲突，以本次事实源为准并记录差异 |
| 内部事实源 | `card-status-and-fields.md` | 状态、字段、接口路径、操作限制 | 其他 Card 文件不得重复定义卡状态和核心接口路径 |
| 页面派生文件 | `card-home.md`、`activation.md`、`pin.md`、`sensitive-info.md`、`card-management.md` | 页面与功能流程 | 必须引用 Status & Fields 中的状态、字段和操作权限 |
| 本次未提供附件 | Home、Transaction & History、Card Transaction、Wallet、Notification 等历史资料 | 首页、交易展示、通知与钱包联动 | 保留原有引用，但在对应文件中标记为“本次评审未验证来源” |

## 8. 待确认事项

| 编号 | 问题 | 影响文件 | 优先级 |
|---|---|---|---|
| CARD-IDX-Q001 | `autoDebitEnabled` 产品枚举 `2/ON` 与 DTC API `1/ON` 的映射关系 | application、activation、card-status-and-fields | P0 |
| CARD-IDX-Q002 | Application 选择的稳定币与 DTC `currency` / `cardFeeDetails.currency` 的映射关系 | application | P0 |
| CARD-IDX-Q003 | 激活后 Set PIN 的强制性与接口顺序 | activation、pin | P0 |
| CARD-IDX-Q004 | 注销卡能力的 AIX 页面流程与 DTC `Terminate Card` 接入 | card-management、card-status-and-fields | P0 |
| CARD-IDX-Q005 | 未随本次附件提供的 Home / Transaction / Wallet / Notification 事实源是否为最新版本 | card-home、card-transaction-flow | P1 |

## 9. 模块级验收标准

| 验收项 | 标准 |
|---|---|
| 模板一致性 | Card 目录下功能文件均包含文档信息、业务流程、页面交互、字段接口、异常处理、风控边界、待确认项、验收标准、来源引用 |
| 状态一致性 | 所有卡操作均引用 `card-status-and-fields.md` 的状态与操作限制，不在单独文件重复解释状态 |
| 接口一致性 | DTC 接口路径、关键字段、枚举差异在状态与业务文件中保持一致 |
| Gap 管理 | 未确认项必须集中记录，不能写成已确认事实 |

## 10. 来源引用

- (Ref: 历史prd/AIX Card V1.0【Application】.pdf / 2.1 / 2.2 / 5.1 / 5.2 / V1.0)
- (Ref: 历史prd/AIX Card manage模块需求V1.0.docx / 6.4 / 7.1-7.5 / 8.1 / V1.0)
- (Ref: 历史prd/AIX Card交易【transaction】.pdf / 7 / 8.1 / 9 / V1.0)
- (Ref: 历史prd/AIX APP V1.0【Home】.pdf / 6.1 / V1.0)
- (Ref: 历史prd/AIX APP V1.0【Transaction & History】.pdf / 5.1-5.3 / V1.1)
