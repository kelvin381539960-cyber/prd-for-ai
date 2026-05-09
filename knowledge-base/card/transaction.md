---
module: card
feature: card-transaction
version: "1.1"
status: active
source_doc: archive/converted-prd/card/transaction/README.md；archive/converted-prd/app/transaction-history/README.md
source_section: Card Transaction / 7.1 资金回退；Transaction & History / 7.2 Card History；7.3 Card Transaction Details
last_updated: 2026-05-09
owner: 吴忆锋
readers: [product, ui, dev, qa, business, ai]
---

# Card Transaction 卡交易资金回退

> Source alignment note: 本文件已按 Card Transaction PRD 与 App Transaction History PRD 做双向覆盖校验，补齐卡交易通知、退款/回退、REVERSAL type=19、卡交易展示范围和异常文案。


## 1. 文档信息

| 项目 | 内容 |
|---|---|
| 功能名称 | Card Transaction 卡交易资金回退 |
| 所属模块 | Card |
| Owner | 吴忆锋 |
| 版本 | 1.2 |
| 状态 | Review |
| 更新时间 | 2026-05-05 |
| 来源文档 | AIX Card交易【transaction】、DTC Card Issuing API、DTC Wallet OpenAPI、Standard PRD Template v1.3 |

---

## 2. 需求背景、目标与范围

### 2.1 需求背景

原始 PRD 的目标是：当卡收到特定类型资金时，AIX 自动将卡余额回退 / 归集到用户 Wallet 账户。

原文中的 DTC 知识点说明：退款交易会退回到卡余额；退款时会根据交易发生时汇率将 USD 金额转换为 USDT 等值金额后退回；退款仅退还净商品金额，不包含 FX 费用和 Transaction Fee；退款过程中不收取额外手续费。

### 2.2 用户问题 / 业务问题

如果卡收到退款、冲正、Top-up 或 deposit 后资金停留在卡余额中，用户在 AIX 对外展示的 Wallet 账户中可能无法看到对应资金。因此 AIX 需要在收到 DTC 卡交易通知后，按原文规则判断是否需要将卡余额回退到 Wallet。

### 2.3 需求目标

本文只定义 Card 侧资金回退流程，包括：DTC 卡交易通知、交易类型判断、主动查询卡余额、余额大于 0 时回退到 Wallet、回退结果校验、失败告警和人工介入。

本文不定义 Card History、Card Transaction Details、全量交易列表、交易状态展示、交易详情字段或对账规则；这些由 `card/transaction-detail.md` 与 `transaction/` 模块承接。

### 2.4 涉及功能清单

| 功能点 | 本期范围 | 优先级 | 状态 | 说明 |
|---|---|---|---|---|
| Card Transaction Notification | In Scope | P0 | Confirmed | DTC 检测发生交易后向 AIX 发送交易通知 |
| 交易类型判断 | In Scope | P0 | Confirmed | AIX 校验 type 是否为 refund / reversal / Top-up / deposit |
| 主动查询卡余额 | In Scope | P0 | Confirmed | 命中目标类型后调用 Inquiry Card Basic Info 查询当前卡 balance |
| 余额判断 | In Scope | P0 | Confirmed | balance > 0 时回退钱包；balance = 0 时终止流程 |
| Transfer Balance to Wallet | In Scope | P0 | Confirmed | 请求将卡内余额归集到用户 Wallet，amount = balance |
| 回退结果校验 | In Scope | P0 | Confirmed | 成功则资金已转入用户 Wallet；失败则告警并人工介入 |
| 异常告警 | In Scope | P0 | Confirmed | 失败发送异常告警至监控群，人工介入处理 |
| Card History / Transaction Details | Out of Scope | P1 | Confirmed | 由 `card/transaction-detail.md` 维护 |
| 全局交易历史 / 状态 / 对账 | Out of Scope | P1 | Confirmed | 由 `transaction/` 模块维护 |
| 幂等 / 去重机制 | Out of Scope | P1 | Open | 原文未说明，不写入主流程；如需实现，需技术方案确认 |

---

## 3. 业务流程与规则

### 3.1 业务主流程说明

DTC 检测发生卡交易后，通过 Card Transaction Notification 向 AIX 发送交易通知。AIX 收到交易通知后，校验交易类型是否为 refund / reversal / Top-up / deposit。

若不是目标类型，则终止流程。若命中目标类型，AIX 主动查询当前卡余额，DTC 返回最新卡 balance。若 balance = 0，则终止流程；若 balance > 0，则 AIX 调用 Transfer Balance to Wallet，请求将卡内余额归集到用户 Wallet，入参 amount = balance。

AIX 校验回退接口返回结果。若成功，资金已转入用户 Wallet，流程结束；若失败，则发送异常告警至监控群，人工介入处理。

### 3.2 业务时序图

```mermaid
sequenceDiagram
    autonumber
    participant DTC as DTC
    participant Card as AIX Card 服务
    participant Wallet as Wallet 服务
    participant Monitor as 监控群

    DTC-->>Card: 通知 AIX 发生卡交易
    Card->>Card: 判断交易类型是否需要回退到 Wallet
    alt 非目标交易类型
        Card->>Card: 终止流程
    else 目标交易类型
        Card->>DTC: 查询当前卡余额
        DTC-->>Card: 返回当前卡余额
        alt 卡余额为 0
            Card->>Card: 终止流程
        else 卡余额大于 0
            Card->>Wallet: 发起卡余额回退到用户 Wallet
            alt 回退成功
                Wallet-->>Card: 返回回退成功结果
                Card->>Card: 流程结束
            else 回退失败
                Card->>Monitor: 发送异常告警
                Monitor->>Card: 人工介入处理
            end
        end
    end
```

### 3.3 流程步骤与业务规则

| 步骤 | 场景 / 规则 | 触发条件 | 责任方 | 系统处理 | 成功结果 | 失败 / 分支结果 | 来源 |
|---|---|---|---|---|---|---|---|
| 1 | 触发通知 | DTC 检测发生卡交易 | DTC | 通过 Card Transaction Notification 向 AIX 发送交易通知 | AIX 收到交易通知 | 通知字段取值待 DTC 确认 | 原文 7.3 |
| 2 | 类型判断 | AIX 收到交易通知 | AIX Card | 校验 type 是否为 refund / reversal / Top-up / deposit | 命中则查询卡余额 | 未命中则终止流程 | 原文 7.3 |
| 3 | 主动查询卡余额 | 命中目标交易类型 | AIX Card / DTC | 调用 Inquiry Card Basic Info 主动查询当前卡余额 | DTC 返回最新 balance | 查询失败处理待确认 | 原文 7.3 |
| 4 | 余额判断 | 获取 balance | AIX Card | 判断 balance 是否大于 0 | balance > 0 时回退 Wallet | balance = 0 时终止流程 | 原文 7.3 |
| 5 | 请求资金回退 Wallet | balance > 0 | AIX Card / Wallet | 调用 Transfer Balance to Wallet，amount = balance | 回退请求成功提交 | 回退失败进入告警 | 原文 7.3 |
| 6 | 回退结果校验 | 回退接口返回 | AIX Card | 校验回退接口返回结果 | 成功则资金转入用户 Wallet，流程结束 | 失败则发送告警并人工介入 | 原文 7.3 |
| 7 | 失败人工处理 | 回退失败 | AIX / 监控群 / 人工处理人 | 发送异常告警至监控群 | 人工介入跟进 | 系统原因由开发跟进；交易金额大于卡余额由 PM 跟进 | 原文 7.3 |

### 3.4 状态规则

| 状态 | 含义 | 触发条件 | 用户可见表现 | 系统处理 | 可迁移到 | 是否终态 | 来源 |
|---|---|---|---|---|---|---|---|
| 已收到交易通知 | DTC 已通知 AIX 发生卡交易 | Card Transaction Notification | 用户不可见 | 进入交易类型判断 | 目标类型 / 非目标类型 | 否 | 原文 7.3 |
| 非目标交易类型 | type 不是 refund / reversal / Top-up / deposit | 交易类型判断 | 用户不可见 | 终止流程，不回退 Wallet | 不适用 | 是 | 原文 7.3 |
| 目标交易类型 | type 是 refund / reversal / Top-up / deposit | 交易类型判断 | 用户不可见 | 主动查询当前卡余额 | balance = 0 / balance > 0 | 否 | 原文 7.3 |
| balance = 0 | 当前卡余额为 0 | 查询卡余额后 | 用户不可见 | 终止流程，不回退 Wallet | 不适用 | 是 | 原文 7.3 |
| balance > 0 | 当前卡余额大于 0 | 查询卡余额后 | 用户不可见 | 发起资金回退 Wallet | 回退成功 / 回退失败 | 否 | 原文 7.3 |
| 回退成功 | Transfer Balance to Wallet 成功 | 回退接口成功返回 | 用户 Wallet 资金更新 | 流程结束 | 对账 | 是 | 原文 7.3 |
| 回退失败 | Transfer Balance to Wallet 失败 | 回退接口失败返回 | 用户可能不可见资金 | 告警并人工介入 | 人工处理 | 否 | 原文 7.3 |

### 3.5 业务级异常与失败处理

| 异常场景 | 触发条件 | 错误来源 | 错误码 / 原因 | 用户表现 | 系统处理 | 是否可重试 | 最终状态 |
|---|---|---|---|---|---|---|---|
| 非目标交易类型 | type 非 refund / reversal / Top-up / deposit | DTC | type 不匹配 | 用户不可见 | 终止流程，不回退 Wallet | 否 | 不回退 |
| 查询余额失败 | Inquiry Card Basic Info 失败 | DTC / Network | 接口失败 | 用户不可见 | 原文未说明，待确认 | 待确认 | 待处理 |
| balance = 0 | 查询卡余额为 0 | DTC | 余额为 0 | 用户不可见 | 终止流程，不回退 Wallet | 否 | 不回退 |
| 回退失败：系统原因 | Transfer Balance to Wallet 失败 | AIX / DTC / Wallet | 系统原因 | 用户可能不可见资金 | 发送告警，开发跟进处理 | 人工 | 待人工处理 |
| 回退失败：交易金额大于卡余额 | Transfer Balance to Wallet 失败 | AIX / DTC / Wallet | 金额大于卡余额 | 用户可能不可见资金 | 发送告警，由 PM 跟进处理 | 人工 | 待人工处理 |
| 回退成功但交易 / 对账不可见 | 回退成功后关联记录不可追踪 | Transaction / Reconciliation | 关联规则缺失 | 用户可能咨询 | 由 Transaction / Reconciliation 模块承接 | 待确认 | 待确认 |

---

## 4. 页面与交互说明

本功能为后台资金回退流程，原文没有定义独立用户页面。

| 区块 | 内容 |
|---|---|
| 页面类型 | 不适用 |
| 页面目标 | 不适用 |
| 入口 / 触发 | DTC Card Transaction Notification 触发 |
| 展示内容 | 不适用 |
| 用户动作 | 无用户主动操作 |
| 系统处理 / 责任方 | AIX 根据交易类型、卡余额和回退结果处理资金回退 |
| 元素 / 状态 / 提示规则 | 不适用 |
| 成功流转 | 资金转入用户 Wallet，流程结束 |
| 失败 / 异常流转 | 发送异常告警至监控群，人工介入处理 |
| 备注 / 边界 | Card History、Card Transaction Details 页面见 `card/transaction-detail.md` |

---

## 5. 字段、接口与数据

| 类型 | 名称 | 所属系统 | 来源 | 用途 | 规则 / 输入输出 | 异常处理 |
|---|---|---|---|---|---|---|
| 接口 | Card Transaction Notification | DTC | 原文 7.3 / 8.1 / 8.3 | DTC 通知 AIX 发生卡交易 | 通知字段、取值和落库规则待 DTC 确认 | 通知失败处理待确认 |
| 字段 | type | DTC | 原文 7.3 | 判断是否需要回退 Wallet | refund / reversal / Top-up / deposit 触发后续查询余额 | 非目标类型终止流程 |
| 接口 | Inquiry Card Basic Info | DTC | 原文 7.3 | 主动查询当前卡余额 | 返回最新卡 balance | 查询失败处理待确认 |
| 字段 | balance | DTC | 原文 7.3 | 判断是否需要回退 Wallet，也作为回退金额来源 | balance > 0 时回退；balance = 0 时终止；amount = balance | 缺失或异常待确认 |
| 接口 | Transfer Balance to Wallet | DTC / Wallet | 原文 7.3 / 8.1 | 将卡内余额回退到用户 Wallet | 入参 amount = balance | 失败发送异常告警并人工介入 |
| 接口 | Card Balance History Inquiry | DTC / Transaction | 原文 8.1 | 卡余额历史查询 | 与 Card History / Transaction 模块关系待确认 | 查询失败待确认 |

---

## 6. 通知规则（如适用）

| 触发事件 | 通知渠道 | 通知对象 | 文案 / 模板 | 跳转目标 | 失败 / 补发规则 |
|---|---|---|---|---|---|
| 回退失败告警 | Monitor / 内部群 | 内部运营 / 技术 / PM | 告警模板待确认 | 内部处理台 | 原文要求人工介入；补发规则待确认 |

本文不定义用户 Push / In-app 通知模板。卡交易成功、退款成功等用户通知由 `common/notification.md` 或 Transaction 相关模块承接。

---

## 7. 权限 / 合规 / 风控（如适用）

| 类型 | 规则 | 影响 | 来源 |
|---|---|---|---|
| 资金回退范围 | 仅 refund / reversal / Top-up / deposit 触发余额查询与 Wallet 回退 | 防止非目标交易误回退 | 原文 7.3 |
| 金额来源 | 回退金额取查询得到的卡 balance，amount = balance | 防止按通知金额错误回退 | 原文 7.3 |
| 失败可观测 | 回退失败必须发送异常告警并人工介入 | 防止资金悬挂 | 原文 7.3 |
| 退款费用规则 | 退款仅退还净商品金额，不含 FX 费用和 Transaction Fee；退款过程不额外收费 | 明确用户退款金额预期 | 原文 DTC 知识点 |

---

## 8. 待确认事项

| 问题 | 影响范围 | 当前处理 | 是否阻塞验收 | 建议确认人 |
|---|---|---|---|---|
| Card Transaction Notification 的完整字段、type 枚举和取值大小写 | BE / DTC / QA | 阻塞 | 是 | BE / DTC |
| 原文 `Top-up` 与 DTC 实际 type 枚举如何拼写和映射 | BE / DTC / QA | 阻塞 | 是 | BE / DTC / PM |
| Inquiry Card Basic Info 查询失败时是否告警、是否重试、是否人工介入 | BE / Ops | 阻塞 | 是 | BE / Ops / PM |
| 回退失败告警监控群、告警字段、责任分派和人工补偿入口 | Ops / Finance / BE | 阻塞 | 是 | PM / Ops / BE |
| 失败原因为系统原因和交易金额大于卡余额时的判断来源 | Ops / BE / PM | 阻塞 | 是 | BE / Ops / PM |
| Card Balance History Inquiry 与 Card History / Transaction 模块的关系 | FE / BE / QA / Transaction | 不阻塞 | 否 | PM / BE |
| Card 交易、Wallet 回退记录和全局 Transaction 记录之间的关联字段 | 对账 / 故障追踪 | 阻塞 | 是 | BE / Finance |
| Card Transaction Notification 是否需要幂等 / 去重机制，以及去重字段是什么 | BE / Audit | 不阻塞 / 技术方案待定 | 否 | BE / Audit |

---

## 9. 验收标准 / 测试场景

### 9.1 验收标准

| 验收场景 | 验收标准 |
|---|---|
| 正常流程 | DTC 通知目标交易类型且 balance > 0 时，AIX 发起 Transfer Balance to Wallet，amount = balance |
| 异常流程 | 非目标类型、balance = 0、查询余额失败、回退失败均有明确处理或待确认边界 |
| 页面展示 | 本功能无独立用户页面；Card History / Details 由 `card/transaction-detail.md` 维护 |
| 系统交互 | Card Transaction Notification、Inquiry Card Basic Info、Transfer Balance to Wallet 的边界明确 |
| 通知 | 回退失败走内部告警和人工介入 |
| 数据 / 埋点 | type、balance、回退结果、告警原因和交易关联字段可追踪或进入待确认 |

### 9.2 测试场景矩阵

| 场景 | 前置条件 | 用户操作 | 预期页面表现 | 预期系统结果 | 是否必测 |
|---|---|---|---|---|---|
| refund 回退成功 | 收到 refund，balance > 0 | 无用户操作 | 用户 Wallet 资金更新 | 调用 Transfer Balance to Wallet，amount = balance | 是 |
| reversal 回退成功 | 收到 reversal，balance > 0 | 无用户操作 | 用户 Wallet 资金更新 | 调用 Transfer Balance to Wallet，amount = balance | 是 |
| Top-up 回退成功 | 收到 Top-up，balance > 0 | 无用户操作 | 用户 Wallet 资金更新 | 调用 Transfer Balance to Wallet，amount = balance | 是 |
| deposit 回退成功 | 收到 deposit，balance > 0 | 无用户操作 | 用户 Wallet 资金更新 | 调用 Transfer Balance to Wallet，amount = balance | 是 |
| 非目标类型 | 收到非目标 type | 无用户操作 | 用户不可见 | 终止流程，不查询或不回退 | 是 |
| balance = 0 | 目标类型，卡余额为 0 | 无用户操作 | 用户不可见 | 终止流程，不调用 Transfer | 是 |
| 查询余额失败 | 目标类型，查询余额失败 | 无用户操作 | 用户不可见 | 处理方式待确认 | 是 |
| 回退失败 | 目标类型，balance > 0，Transfer 失败 | 无用户操作 | 用户可能不可见资金 | 发送异常告警，人工介入 | 是 |

---

## Source alignment additions

### A. Card transaction notification / funds rollback

| 规则 | 结论 | 来源 |
|---|---|---|
| DTC 通知 | DTC 检测发生交易后，通过 Card Transaction Notification 接口向 AIX 发送交易通知 | Card Transaction / 7.1 |
| AIX 校验类型 | AIX 收到交易通知后先校验 type 是否为 refund、reversal、deposit 等源 PRD 定义范围；Top-up 为删除线，不沉淀为 confirmed fact | Card Transaction / 7.1 |
| 余额回查 | 若匹配，AIX 调用 Inquiry Card Basic Info 主动查询当前卡余额，DTC 返回最新 card balance | Card Transaction / 7.1 |
| 回退结果 | AIX 校验回退接口返回结果；具体异常与渠道确认事项不自行扩展 | Card Transaction / 7.1 |

### B. Card History display range

| 规则 | 结论 | 来源 |
|---|---|---|
| 卡交易列表接口 | [POST] /openapi/v1/card/inquiry-card-transaction | Transaction & History / 7.2、8.1 |
| 搜索 | 全量交易及卡交易去掉搜索，后续再迭代 | Transaction & History changelog |
| 原始类型展示范围 | 仅展示 PURCHASE、CASH_WITHDRAWAL、REFUND、INCREMENTAL_AUTH | Transaction & History / 7.2 |
| REVERSAL | DTC 反馈部分退款会使用 REVERSAL，因此卡交易需展示该 type=19 单子 | Transaction & History changelog / 7.2 |
| REVERSAL 展示 | 前端与 REFUND 一样显示 refund-商户名称 | Transaction & History changelog / 7.2 |
| 无数据 | 如果没有数据，占位符显示 No transaction data | Transaction & History / 7.2 |
| 异常文案 | DTC / 服务端异常显示 Data error. Please refresh and try again.；网络异常显示 No internet connection. Please retry | Transaction & History / 7.1 |

## 10. 来源引用

- (Ref: archive/historical-prd/card/AIX Card交易【transaction】.docx / 7.1 / 7.2 / 7.3 / 8.1 / 9)
- (Ref: external-docs/dtc/DTC Card Issuing API Document_20260310 (1).docx / Card Transaction Notification / Inquiry Card Basic Info)
- (Ref: external-docs/dtc/DTC Wallet OpenAPI Document20260126 (1).docx / Transfer Balance to Wallet)
- (Ref: knowledge-base/changelog/knowledge-gaps.md)
- (Ref: prd-template/standard-prd-template.md / v1.3)
