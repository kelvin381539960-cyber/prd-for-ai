# prd-for-ai 实施计划

版本：v1.3  
状态：执行中  
适用仓库：`prd-for-ai`  
更新时间：2026-05-01

## 1. 文档定位

本文件是 `prd-for-ai` 仓库的长期实施主控文件。

本项目会跨多个对话、多个时间段持续推进。后续每次开始执行前，必须先读取本文件，确认当前阶段、当前模块、待办任务和验收标准，再继续执行。

本文件优先级高于临时对话结论。若临时任务与本实施计划冲突，必须先更新本实施计划，再执行具体任务。

## 2. 强制执行原则

1. `IMPLEMENTATION_PLAN.md` 是唯一主控计划。
2. 每次开始任务前，必须先读取本文件。
3. 如果用户临时要求与本文件冲突，先更新本文件，再执行任务。
4. 不允许跳阶段。
5. 不允许用新的模块清单替代阶段计划。
6. 模块清单只能作为阶段内的执行子任务。
7. 若发现本实施计划不符合当前真实进度，必须先修正实施计划，再继续执行。
8. 所有内容必须来源于历史 PRD、接口文档、截图、已确认结论或已存在知识库。
9. 允许跨文档、跨模块引用已确认事实。
10. 禁止无来源补流程、补页面、补字段、补状态、补文案。

---

## 3. 项目目标

建设 AIX 的 AI-readable PRD 知识库，使其成为后续编写 PRD、评审需求、生成 UI、辅助开发和测试的事实来源。

核心目标：

1. 将历史 PRD 统一归档，作为不可随意修改的原始事实源。
2. 将 DTC、AAI、WalletConnect、OBOSS 等外部系统能力沉淀为独立事实层。
3. 将历史 PRD 与接口文档转译为结构化 Markdown，形成 AI 可读、可检索、可复用的知识库。
4. 将状态、字段、错误码、国家线、限额、合规边界沉淀为全局规则。
5. 支撑后续 AI 辅助编写新 PRD 时，能准确复用既有业务规则、接口、状态机、异常处理和验收标准。
6. 保证所有知识均可追溯到原始 PRD、接口文档或已确认的项目结论。

---

## 4. 仓库分层原则

`历史prd/`、`DTC接口文档/`、其他外部系统文档均属于原始事实源，不直接修改。

```text
┌────────────────────────────┐
│ 原始事实源                   │
│ - 历史prd/                   │
│ - DTC接口文档/               │
│ - 外部系统/接口/评审结论      │
└──────────────┬─────────────┘
               │ 提取 / 映射 / 转译
               ▼
┌────────────────────────────┐
│ knowledge-base/             │
│ AI-readable 事实知识库        │
│ 规则 / 流程 / 状态 / 字段      │
└──────────────┬─────────────┘
               │ 复用
               ▼
┌────────────────────────────┐
│ prd-template/               │
│ 后续新 PRD 写作模板           │
└────────────────────────────┘
```

### 4.1 原始事实源规则

- 原始 PRD、接口文档、截图、评审结论仅作为事实来源保留。
- 不直接修改原始文件内容。
- 不在原始目录内做结构化加工。
- 若原始事实源之间存在冲突，必须记录到 `knowledge-base/changelog/knowledge-gaps.md` 或相关冲突记录，不得自行拍板。

### 4.2 Knowledge Base 规则

目录：

```text
knowledge-base/
```

规则：

- 作为 AI、产品、UI、开发、测试、业务的主要读取对象。
- 只写可验证、可追溯的业务事实。
- 每个规则必须尽量关联来源文档、章节或接口文档。
- 不写推测，不写未确认方案。
- 功能正文不写评审型内容；不确定点集中进入 `knowledge-base/changelog/knowledge-gaps.md`。

### 4.3 PRD Template 规则

目录：

```text
prd-template/
```

用途：

- 沉淀新 PRD 的标准章节。
- 统一需求描述、状态机、字段、异常、验收、风控、合规边界写法。
- 未来写新 PRD 时，优先引用 `knowledge-base/` 中的既有事实。

---

## 5. 推荐目录结构

最终建议结构如下：

```text
knowledge-base/
├── _meta/                       # 全局事实与写作规范
│   ├── glossary.md
│   ├── countries-and-regions.md
│   ├── status-dictionary.md
│   ├── field-dictionary.md
│   ├── error-code-dictionary.md
│   ├── limits-and-rules.md
│   ├── compliance-boundaries.md
│   ├── source-policy.md
│   ├── writing-standard.md
│   ├── module-template.md
│   └── feature-template.md
│
├── integrations/                # 外部系统事实源
│   ├── _index.md
│   ├── dtc/
│   ├── aai/
│   ├── walletconnect/
│   └── oboss/
│
├── common/                      # APP 通用能力
│   ├── _index.md
│   ├── common-error-pages.md
│   ├── common-popups.md
│   ├── faq.md
│   └── notification-content.md
│
├── account/                     # 注册、登录、忘记密码
├── security/                    # OTP、Email OTP、Passcode、Bio、Face、IVS
├── wallet/                      # KYC、资产、充值、转账、兑换
├── card/                        # 申卡、激活、PIN、卡管、敏感信息
├── transaction/                 # 全量交易、卡交易、钱包交易、状态类型
├── growth/                      # MGM、Push、Message Center、Banner、Popup、Waitlist
├── website/                     # 官网一期、官网二期、外部投放
├── platform/                    # OBOSS、多语言、系统邮件等平台能力
├── assets/                      # 图片资源
└── changelog/                   # 实施日志、知识缺口、冲突记录
```

### 5.1 app-common 迁移口径

原 `knowledge-base/README.md` 中的 `app-common` 后续统一迁移为 `common`。

后续不再新增 `app-common` 目录。FAQ、通用错误页、通用弹窗、通知内容等统一归入 `common/`。

---

## 6. 模块拆分规则

采用“模块目录 + 功能文件”的结构。

原则：

- 一个业务模块一个目录。
- 一个核心能力一个 Markdown 文件。
- 复杂模块可拆出状态、字段、接口文件。
- 不按原始 PRD 文件机械拆分。
- 不拆成页面级小文件，避免维护成本过高。
- 资金、交易、KYC、卡、钱包相关模块必须单独沉淀状态机与字段规则。
- 公共规则不在各功能文件中重复维护，应沉淀到 `_meta/` 或对应公共模块。

推荐粒度示例：

```text
wallet/
├── _index.md
├── kyc.md
├── deposit-gtr.md
├── deposit-walletconnect.md
├── send.md
├── swap.md
├── receive.md
└── wallet-status-and-fields.md
```

```text
card/
├── _index.md
├── application.md
├── activation.md
├── card-management.md
├── pin.md
├── sensitive-info.md
└── card-status-and-fields.md
```

```text
transaction/
├── _index.md
├── transaction-history.md
├── card-transaction.md
├── crypto-transaction.md
├── otc-transaction.md
└── transaction-status-and-type.md
```

---

## 7. 单个功能文件标准结构

每个核心功能文件应使用统一结构。

```markdown
---
module:
feature:
version:
status:
source_doc:
source_section:
last_updated:
owner:
depends_on:
---

# 功能名称

## 1. 功能定位
说明该功能解决什么问题，只写事实，不写愿景。

## 2. 适用范围
说明适用国家、用户状态、账户状态、卡状态、钱包状态等。

## 3. 前置条件
说明用户必须满足什么条件。

## 4. 业务流程
包含主链路、Mermaid sequenceDiagram、业务逻辑矩阵。

## 5. 页面关系总览
使用 Mermaid flowchart 表达页面地图。只表达页面节点和跳转关系，不展开业务校验。

## 6. 页面卡片与交互规则
说明页面、按钮、输入框、校验、跳转、截图引用。

## 7. 字段与接口依赖
说明接口、字段、读写关系、系统动作、异步回调。

## 8. 异常与失败处理
说明失败场景、错误提示、重试、兜底动作、最终状态。

## 9. 风控 / 合规边界
涉及账户、资金、卡、交易、KYC 时必须说明。

## 10. 来源引用
列出原始 PRD、接口文档、章节、版本。
```

禁止在功能正文中固定保留：

- `readers` frontmatter。
- 多角色阅读视角。
- 待确认事项章节。
- 试验版 / 方案 A/B/C 等过程性内容。

不确定点统一记录到：

```text
knowledge-base/changelog/knowledge-gaps.md
```

---

## 8. 流程图与页面地图规则

### 8.1 业务流程与系统交互

核心业务流程统一使用 Mermaid `sequenceDiagram`。

定位：

- 表达产品业务流程和系统交互。
- 不替代页面概览图。
- 写法使用“时序图形式 + 职能泳道图表达 + 业务规则语言”。

写法要求：

- 参与方按职责分层，例如 User、Client / AIX App、Backend / AIX Backend、Security Module、Device OS、DTC / AAI / Third Party。
- 文案写业务动作，不写纯技术调用。
- 异常分支必须写清失败原因、系统动作、用户/状态落点。
- 使用 `alt / else / end` 表达分支。
- 复杂流程可按子链路拆分，但仍放在同一功能文件内。

### 8.2 页面关系总览

页面关系总览统一使用 Mermaid `flowchart` 表达页面地图。

定位：

- 只表达当前功能涉及的页面节点和页面跳转关系。
- 不表达业务流程、系统交互、字段规则、后端校验、风控判断、异常处理细节。

要求：

- 必须完整覆盖当前功能相关的页面、弹窗页、认证页、结果页、异常承接页。
- 不得为了追求简洁而删除页面节点。
- 不限制节点数量；复杂功能应通过 `subgraph` 分组控制可读性。
- 连线文案只写短动作或短入口，例如 Next、Submit、Confirm、Back、Close、Enable now。
- 复杂业务条件放在第 4 章业务流程或业务逻辑矩阵中。
- 实线表示正常页面跳转，虚线表示异常 / 拦截 / 失败承接。

推荐分组：

```text
入口层
主页面层
分支页面 / 能力页
结果页 / 异常承接
```

---

## 9. 图片与截图规则

图片继续保留，但不作为唯一事实表达。

规则：

1. 原 PRD 截图保留在 `knowledge-base/assets/`。
2. 页面截图可作为证据引用，但规则必须写成文字。
3. 原始 PRD 页面概览截图可以保留，但只能作为追溯证据，不作为主要规则表达。
4. 如果截图与文字规则冲突，以文字规则为准，并标记冲突点。
5. 不删除历史截图，除非确认重复或错误。

表达优先级：

```text
结构化 Markdown 规则 > Mermaid 图 > 页面截图
```

---

## 10. 来源与引用规则

所有知识必须有来源。

来源优先级：

1. `历史prd/` 原始 PRD
2. `DTC接口文档/` 接口文档
3. 已确认的项目规则 / 评审结论
4. 已存在知识库
5. 外部公开资料，仅用于行业、政策、竞品，不作为 AIX 内部规则来源

允许：

- 跨模块引用已确认事实。
- 跨文档引用已确认事实。
- 使用公共规则替代重复描述。

禁止：

- 无来源推测。
- 把未确认事项写成已确认规则。
- 私自补全接口字段。
- 私自改变状态机。
- 私自改变资金路径。
- 私自改变风控 / 合规边界。

如发现冲突，必须标记：

```markdown
## 冲突 / 待确认

- 冲突点：
- 涉及文件：
- 影响范围：
- 建议确认人：
- 当前处理：
```

---

## 11. 阶段实施路线表

| 阶段 | 名称 | 当前状态 | 目标 | 阶段产出 | 下一步 |
|---|---|---|---|---|---|
| 1 | Account 样板 | 基本完成 | 固化知识库写法 | Login / Registration / Forgot Password | 最终 Review |
| 2 | 基础规则沉淀 | 部分完成 | 建立长期规则 | Writing Standard / Source Rules | 抽 Security |
| 3 | Security 标准化 | 未开始 | 统一认证事实源 | OTP / Email OTP / Passcode / BIO / IVS | 当前优先执行 |
| 4 | Card 批量推进 | 未开始 | 转译卡模块 | Application / Manage / Transaction | Security 后执行 |
| 5 | Wallet 批量推进 | 未开始 | 转译钱包模块 | KYC / Send / Swap / Receive / Deposit | Security 后执行 |
| 6 | Transaction 统一层 | 未开始 | 统一交易状态 | Card / Wallet / Swap / History | Card / Wallet 后执行 |
| 7 | Common / Integration | 未开始 | 抽公共能力 | DTC / AAI / WC / Error / FAQ | Transaction 后执行 |
| 8 | 全仓库回扫 | 未开始 | 去重复、补引用 | 字段 / 状态 / 来源 / gaps | 最后执行 |

---

## 12. 阶段内任务拆解

### 12.1 阶段 1：Account 样板

| 子任务 | 状态 | 说明 |
|---|---|---|
| Login | 已完成 | 可作为样板 |
| Registration | 已完成 | 已按原 PRD 重构 |
| Forgot Password | 需复核 | 上一版可能仍有推导，需原文校验 |
| Account `_index.md` | 待执行 | 需按最终模块清单更新 |
| Account gaps | 待执行 | 需集中记录字段冲突与未确认项 |

### 12.2 阶段 2：基础规则沉淀

| 子任务 | 状态 | 说明 |
|---|---|---|
| writing-standard | 已完成 | 已加入流程图、页面地图、禁止编造、跨文档引用 |
| source rule | 已完成 | 已明确允许跨模块引用事实 |
| field dictionary | 待执行 | 需抽字段标准 |
| status dictionary | 待执行 | 需统一状态定义 |
| compliance boundaries | 待执行 | 需统一资金、KYC、卡、钱包边界 |

### 12.3 阶段 3：Security 标准化

| 子任务 | 状态 | 说明 |
|---|---|---|
| security/_index.md | 未开始 | 统一 Security 功能清单 |
| otp-verification.md | 未开始 | 短信 OTP 规则 |
| email-otp-verification.md | 未开始 | 邮箱 OTP 规则 |
| login-passcode-verification.md | 未开始 | 登录密码认证规则 |
| biometric-verification.md | 未开始 | BIO 登录与设备认证规则 |
| face-verification.md | 未开始 | DTC / AAI 活体认证规则 |
| authentication-rules.md | 未开始 | 场景认证方式、优先级、有效期 |

### 12.4 阶段 4：Card 批量推进

| 子任务 | 状态 | 说明 |
|---|---|---|
| card/_index.md | 未开始 | Card 模块功能清单 |
| application.md | 未开始 | 申卡流程 |
| card-home.md | 未开始 | 卡首页 |
| activation.md | 未开始 | 实体卡激活 |
| pin.md | 未开始 | Set / Change PIN |
| sensitive-info.md | 未开始 | 查看敏感卡信息 |
| card-management.md | 未开始 | Lock / Unlock / Cancel |
| card-status-and-fields.md | 未开始 | 卡状态与字段 |
| card-transaction-flow.md | 未开始 | 卡退款 / 回退钱包流程 |

### 12.5 阶段 5：Wallet 批量推进

| 子任务 | 状态 | 说明 |
|---|---|---|
| wallet/_index.md | 未开始 | Wallet 模块功能清单 |
| kyc.md | 未开始 | 钱包开户 KYC |
| wallet-home.md | 未开始 | 钱包首页 |
| send.md | 未开始 | 钱包转账 |
| swap.md | 未开始 | 钱包兑换 |
| receive.md | 未开始 | 地址充值 / GTR |
| deposit-walletconnect.md | 未开始 | WalletConnect 充值 |
| wallet-status-and-fields.md | 未开始 | 钱包状态、币种、网络、字段 |

### 12.6 阶段 6：Transaction 统一层

| 子任务 | 状态 | 说明 |
|---|---|---|
| transaction/_index.md | 未开始 | Transaction 功能清单 |
| transaction-history.md | 未开始 | 全量交易记录 |
| card-transaction.md | 未开始 | 卡交易列表与详情 |
| crypto-transaction.md | 未开始 | 加密币交易详情 |
| otc-transaction.md | 未开始 | Swap 交易详情 |
| transaction-status-and-type.md | 未开始 | 状态 / 类型统一映射 |

### 12.7 阶段 7：Common / Integration

| 子任务 | 状态 | 说明 |
|---|---|---|
| common-error-pages.md | 未开始 | Network / Server Error |
| common-popups.md | 未开始 | 通用弹窗 |
| faq.md | 未开始 | FAQ 来源与展示规则 |
| integrations/dtc | 未开始 | DTC 能力事实源 |
| integrations/aai | 未开始 | AAI 能力事实源 |
| integrations/walletconnect | 未开始 | WalletConnect 能力事实源 |
| integrations/oboss | 未开始 | OBOSS 能力事实源 |

### 12.8 阶段 8：全仓库回扫

| 子任务 | 状态 | 说明 |
|---|---|---|
| 去重复 | 未开始 | 公共规则改引用 |
| 补来源 | 未开始 | 所有规则补来源 |
| 补 gaps | 未开始 | 缺口集中化 |
| 状态统一 | 未开始 | 状态名与终态统一 |
| 字段统一 | 未开始 | 字段名与系统归属统一 |
| PRD template | 未开始 | 输出新 PRD 模板 |

---

## 13. 第一阶段完成标准

当前第一阶段指：Account 样板收口。

完成标准：

- `knowledge-base/account/login.md` 已作为 Login 样板，包含：
  - 标准 frontmatter。
  - 1–10 标准章节。
  - Mermaid `sequenceDiagram` 业务流程与系统交互图。
  - Mermaid `flowchart` 页面地图。
  - 页面截图与页面卡片。
  - 字段与接口依赖。
  - 异常与失败处理。
  - 风控 / 合规边界。
  - 来源引用。
- `knowledge-base/account/registration.md` 已按原 PRD 完整重构。
- `knowledge-base/account/forgot-password.md` 必须完成原文复核后，才可标记为完成。
- `knowledge-base/account/_index.md` 必须反映 Account 模块真实功能清单。
- `knowledge-base/changelog/knowledge-gaps.md` 已集中承接 Account 知识缺口。

---

## 14. 模块验收标准

每个模块必须满足：

- 有 `_index.md`。
- 有功能清单。
- 有适用范围。
- 有核心流程。
- 有状态机，或说明不适用。
- 有字段与接口依赖。
- 有异常处理。
- 有风控 / 合规边界。
- 有来源引用。
- 有知识缺口记录或明确无缺口。
- 有 Mermaid `sequenceDiagram` 表达业务流程与系统交互。
- 有 Mermaid `flowchart` 表达页面关系总览。
- 不把推测写成事实。

---

## 15. 单个功能验收标准

每个功能文件必须能回答：

1. 这个功能是什么？
2. 谁可以用？
3. 前置条件是什么？
4. 业务流程怎么走？
5. 系统交互怎么发生？
6. 页面关系是什么？
7. 失败怎么办？
8. 依赖哪些状态？
9. 依赖哪些接口和字段？
10. 涉及哪些风控 / 合规边界？
11. UI 能否据此画页面？
12. 开发能否据此理解接口与状态？
13. 测试能否据此写测试用例？
14. 业务能否据此判断支持 / 不支持范围？
15. AI 能否据此复用到新 PRD？
16. 来源文档是什么？
17. 还有哪些缺口或冲突？

---

## 16. 跨对话执行规则

由于本项目会跨多个对话、多个时间段执行，后续每次开始任务前必须先读取：

1. `IMPLEMENTATION_PLAN.md`
2. `knowledge-base/_meta/writing-standard.md`
3. 当前目标模块的 `_index.md`
4. 相关功能文件
5. `knowledge-base/changelog/knowledge-gaps.md`
6. 相关原始 PRD 或接口文档

每次执行必须遵守：

- 先确认当前阶段。
- 再确认当前模块。
- 再确认待办任务。
- 不直接跨阶段批量重构，除非本实施计划已允许，且用户明确开启代理模式并限定范围。
- 每次修改必须能回溯来源。
- 发现冲突必须先记录冲突，不得自行拍板。
- 当前阶段完成前，不启动下一阶段代理执行。
- 若本文件与真实进度不一致，必须先更新本文件。

---

## 17. 当前状态

| 模块 | 状态 | 说明 |
|---|---|---|
| IMPLEMENTATION_PLAN | 已更新 | v1.3，加入阶段计划与执行护栏 |
| writing-standard | 已更新 | 已包含时序图、页面地图、禁止编造、跨文档引用 |
| Account / Login | 已完成 | 可作为样板 |
| Account / Registration | 已完成 | 已按原 PRD 完整重构 |
| Account / Forgot Password | 需复核 | 必须回源文档校验，不能直接按当前版本视为完成 |
| Account / _index | 待执行 | 需更新 Account 功能清单 |
| Security | 当前优先 | 必须先标准化，再推进 Card / Wallet |
| Card | 未开始 | 已定位源文档，禁止先于 Security 批量推进 |
| Wallet | 未开始 | 已定位源文档，禁止先于 Security 批量推进 |
| Transaction | 未开始 | 需在 Card / Wallet 后统一状态与类型 |
| Common | 未开始 | 通用错误页、弹窗、FAQ 待结构化 |
| Integrations | 未开始 | DTC、AAI、WalletConnect、OBOSS 待结构化 |
| prd-template | 未开始 | 新 PRD 写作模板待建设 |

---

## 18. 下一步

当前立即任务：

1. 复核 `knowledge-base/account/forgot-password.md`，确认是否存在无来源推导。
2. 更新 `knowledge-base/account/_index.md`。
3. 更新 `knowledge-base/changelog/knowledge-gaps.md` 中 Account 相关缺口。
4. 进入阶段 3：Security 标准化。

当前禁止事项：

- 不得直接跳到 Card / Wallet 批量转译。
- 不得用 Card / Wallet 模块清单替代本阶段计划。
- 不得在 Security 未收口前重复写认证规则。

阶段 3 完成后，才允许进入 Card / Wallet 批量推进。
