# prd-for-ai 实施计划

版本：v1.1  
状态：待执行  
适用仓库：`prd-for-ai`

## 1. 文档定位

本文件是 `prd-for-ai` 仓库的长期实施主控文件。

本项目会跨多个对话、多个时间段持续推进。后续每次开始执行前，必须先读取本文件，确认当前阶段、当前模块、待办任务和验收标准，再继续执行。

本文件优先级高于临时对话结论。若临时任务与本实施计划冲突，必须先更新本实施计划，再执行具体任务。

---

## 2. 项目目标

建设 AIX 的 AI-readable PRD 知识库，使其成为后续编写 PRD、评审需求、生成 UI、辅助开发和测试的事实来源。

核心目标：

1. 将历史 PRD 统一归档，作为不可随意修改的原始事实源。
2. 将 DTC、AAI、WalletConnect、OBOSS 等外部系统能力沉淀为独立事实层。
3. 将历史 PRD 与接口文档转译为结构化 Markdown，形成 AI 可读、可检索、可复用的知识库。
4. 将状态、字段、错误码、国家线、限额、合规边界沉淀为全局规则。
5. 支撑后续 AI 辅助编写新 PRD 时，能准确复用既有业务规则、接口、状态机、异常处理和验收标准。
6. 保证所有知识均可追溯到原始 PRD、接口文档或已确认的项目结论，禁止无来源推测。

---

## 3. 仓库分层原则

`历史prd/` 与 `DTC接口文档/` 是并列的原始事实源，不是上下游关系。

```text
┌────────────────────────────┐
│  原始事实源                  │
│  - 历史prd/                  │
│  - DTC接口文档/              │
└──────────────┬─────────────┘
               │ 提取 / 映射 / 转译
               ▼
┌────────────────────────────┐
│  knowledge-base/            │
│  AI-readable 事实知识库       │
│  规则 / 流程 / 状态 / 字段     │
└──────────────┬─────────────┘
               │ 复用
               ▼
┌────────────────────────────┐
│  prd-template/              │
│  后续新 PRD 写作模板          │
└────────────────────────────┘
```

### 3.1 历史 PRD

目录：

```text
历史prd/
```

规则：

- 作为原始 PRD 事实源保留。
- 不直接修改原始文件内容。
- 不在该目录内做结构化加工。
- 如发现历史 PRD 与当前知识库冲突，应在知识库中标记“冲突 / 待确认”，不得直接篡改原始文档。

### 3.2 DTC 接口文档

目录：

```text
DTC接口文档/
```

规则：

- 作为外部接口、字段、状态、回调、资金路径的原始事实源。
- 不直接修改原始文件内容。
- 与业务 PRD 冲突时，必须标记冲突，并明确需要产品、技术或 DTC 确认。

### 3.3 Knowledge Base

目录：

```text
knowledge-base/
```

规则：

- 作为 AI、产品、UI、开发、测试、业务的主要读取对象。
- 只写可验证、可追溯的业务事实。
- 每个规则必须尽量关联来源文档、章节或接口文档。
- 不写推测，不写未确认方案。
- 如存在文档缺口，必须显式标记为“待确认事项”。

### 3.4 PRD Template

目录：

```text
prd-template/
```

用途：

- 沉淀新 PRD 的标准章节。
- 统一需求描述、状态机、字段、异常、验收、风控、合规边界写法。
- 未来写新 PRD 时，优先引用 `knowledge-base/` 中的既有事实。

---

## 4. 推荐目录结构

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
│   │   ├── _index.md
│   │   ├── wallet-api.md
│   │   ├── card-api.md
│   │   ├── transaction-notification.md
│   │   └── status-and-fields.md
│   ├── aai/
│   │   ├── _index.md
│   │   └── kyc-and-face.md
│   └── walletconnect/
│       ├── _index.md
│       └── deposit-flow.md
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
└── changelog/                   # 实施日志与知识库变更记录
```

### 4.1 app-common 迁移口径

原 `knowledge-base/README.md` 中的 `app-common` 后续统一迁移为 `common`。

后续不再新增 `app-common` 目录。FAQ、通用错误页、通用弹窗、通知内容等统一归入 `common/`。

---

## 5. 模块拆分规则

采用“模块目录 + 功能文件”的结构。

原则：

- 一个业务模块一个目录。
- 一个核心能力一个 Markdown 文件。
- 复杂模块可拆出状态、字段、接口文件。
- 不按原始 PRD 文件机械拆分。
- 不拆成页面级小文件，避免维护成本过高。
- 资金、交易、KYC、卡、钱包相关模块必须单独沉淀状态机与字段规则。

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

## 6. 单个功能文件标准结构

每个功能文件必须使用统一结构。

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
readers: [product, ui, dev, qa, business, ai]
---

# 功能名称

## 1. 功能定位
说明该功能解决什么问题，只写事实，不写愿景。

## 2. 适用范围
说明适用国家、用户状态、账户状态、卡状态、钱包状态等。

## 3. 前置条件
说明用户必须满足什么条件。

## 4. 标准流程
使用步骤表 + Mermaid / ASCII 流程图描述主流程。

## 5. 页面与交互规则
说明页面、按钮、输入框、校验、跳转、截图引用。

## 6. 状态机
如适用，必须列状态、含义、可迁移路径、终态。

## 7. 字段与接口依赖
说明接口、字段、读写关系、系统动作、异步回调。

## 8. 异常与失败处理
说明失败场景、错误提示、重试、兜底动作。

## 9. 风控 / 合规边界
涉及账户、资金、卡、交易、KYC 时必须说明。

## 10. 多角色阅读视角
- UI 视角
- 开发视角
- 测试视角
- 业务视角
- AI 复用视角

## 11. 待确认事项
只放真实缺口，不脑补。

## 12. 来源引用
列出原始 PRD、接口文档、章节、版本。
```

---

## 7. 多角色阅读视角要求

每个核心功能文件必须能服务以下阅读对象。

### 7.1 UI 视角

需要回答：

- 页面有哪些。
- 每个页面有哪些组件。
- 按钮、输入框、状态、文案如何展示。
- 是否有截图、状态变体、弹窗。
- 用户每一步看到什么。

### 7.2 开发视角

需要回答：

- 依赖哪些接口。
- 读取哪些字段。
- 写入哪些字段。
- 状态如何迁移。
- 回调如何处理。
- 幂等、重试、超时、异常如何处理。

### 7.3 测试视角

需要回答：

- 主流程如何验收。
- 异常流如何验收。
- 边界条件是什么。
- 状态迁移是否闭环。
- 失败后是否有可验证结果。

### 7.4 业务视角

需要回答：

- 用户能做什么。
- 哪些用户不能做。
- 哪些国家 / 地区支持。
- 哪些场景不支持。
- 是否影响 CS、运营、合规、风控。

### 7.5 AI 复用视角

需要回答：

- 未来写类似 PRD 时应复用哪些规则。
- 哪些状态、字段、接口、错误提示不能改。
- 哪些内容是可配置项。
- 哪些内容需要重新确认。

---

## 8. 图片与流程图规则

图片继续保留，但不作为唯一事实表达。

规则：

1. 原 PRD 截图保留在 `knowledge-base/assets/`。
2. 关键流程必须转成 Mermaid 或 ASCII，方便 AI 读取。
3. 页面截图可作为证据引用，但规则必须写成文字。
4. 如果截图与文字规则冲突，以文字规则为准，并标记冲突点。
5. 不删除历史截图，除非确认重复或错误。

表达优先级：

```text
结构化 Markdown 规则 > Mermaid / ASCII 流程图 > 页面截图
```

---

## 9. 来源与引用规则

所有知识必须有来源。

来源优先级：

1. `历史prd/` 原始 PRD
2. `DTC接口文档/` 接口文档
3. 已确认的项目规则 / 评审结论
4. 外部公开资料，仅用于行业、政策、竞品，不作为 AIX 内部规则来源

禁止：

- 无来源推测
- 把未确认事项写成已确认规则
- 私自补全接口字段
- 私自改变状态机
- 私自改变资金路径
- 私自改变风控 / 合规边界

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

## 10. 实施阶段

### Phase 1：建立工程规范与事实层骨架

目标：先统一怎么写，避免后续越转越乱。

产出：

- `IMPLEMENTATION_PLAN.md`
- 更新 `knowledge-base/README.md`，使目录结构与本实施计划一致
- `knowledge-base/_meta/glossary.md`
- `knowledge-base/_meta/countries-and-regions.md`
- `knowledge-base/_meta/status-dictionary.md`
- `knowledge-base/_meta/field-dictionary.md`
- `knowledge-base/_meta/error-code-dictionary.md`
- `knowledge-base/_meta/limits-and-rules.md`
- `knowledge-base/_meta/compliance-boundaries.md`
- `knowledge-base/_meta/source-policy.md`
- `knowledge-base/_meta/writing-standard.md`
- `knowledge-base/_meta/module-template.md`
- `knowledge-base/_meta/feature-template.md`
- `knowledge-base/integrations/_index.md`
- `knowledge-base/common/_index.md`
- `knowledge-base/changelog/implementation-log.md`
- `prd-template/`

验收标准：

- 仓库目录规则清晰。
- 文件命名规则清晰。
- 功能文件结构统一。
- 来源引用规则清晰。
- 多角色阅读视角明确。
- `knowledge-base/README.md` 与本实施计划目录一致。
- `implementation-log.md` 已创建，后续执行可持续记录。
- 后续任何对话都可以按本计划继续执行。

状态：待执行。

### Phase 2：重构 Account + Security

目标：将已有 Account 和 Security 作为标准样板。

范围：

- `knowledge-base/account/`
- `knowledge-base/security/`

动作：

- 统一 frontmatter。
- 统一章节结构。
- 补齐来源引用。
- 检查状态、字段、流程是否冲突。
- 保留已有有效内容，不做无意义重写。
- 将公共认证事实沉淀到 `_meta` 或 `security`，供 Card / Wallet / Transaction 复用。

验收标准：

- Account 模块可作为后续业务模块样板。
- Security 模块可作为公共认证能力事实源。
- 所有认证规则可以被 Card / Wallet / Transaction 复用。

状态：待执行。

### Phase 3：转译核心业务模块

优先级：

1. Wallet
2. Card
3. Transaction

优先原因：

- 涉及资金路径。
- 涉及 KYC、卡、交易、钱包状态。
- 依赖 DTC、AAI、WalletConnect 外部系统事实。
- 后续新 PRD 最容易复用这些规则。
- 错误成本最高，必须优先结构化。

状态：待执行。

### Phase 4：转译增长、平台、官网与通用能力

范围：

1. Growth
2. Platform
3. Website
4. Common

目标：

- 补齐运营、通知、MGM、Banner、Popup、Waitlist、官网、多语言、系统邮件、FAQ 等模块。
- 将通用能力沉淀到 `common/`。
- 将平台能力沉淀到 `platform/`。

状态：待执行。

### Phase 5：建立长期维护机制

目标：让仓库可长期维护，而不是一次性整理。

产出：

- 模块验收清单
- 新 PRD 入库流程
- 冲突处理流程
- 待确认事项追踪规则
- 知识库版本管理规则

状态：待执行。

---

## 11. 模块验收标准

每个模块必须满足：

- 有 `_index.md`
- 有功能清单
- 有适用范围
- 有核心流程
- 有状态机，或说明不适用
- 有字段与接口依赖
- 有异常处理
- 有风控 / 合规边界
- 有来源引用
- 有待确认事项
- 有 Mermaid / ASCII 流程表达
- 有 UI / 开发 / 测试 / 业务 / AI 复用视角
- 不把推测写成事实

---

## 12. 单个功能验收标准

每个功能文件必须能回答：

1. 这个功能是什么？
2. 谁可以用？
3. 前置条件是什么？
4. 标准流程怎么走？
5. 失败怎么办？
6. 依赖哪些状态？
7. 依赖哪些接口和字段？
8. 涉及哪些风控 / 合规边界？
9. UI 能否据此画页面？
10. 开发能否据此理解接口与状态？
11. 测试能否据此写测试用例？
12. 业务能否据此判断支持 / 不支持范围？
13. AI 能否据此复用到新 PRD？
14. 来源文档是什么？
15. 还有哪些待确认？

---

## 13. 跨对话执行规则

由于本项目会跨多个对话、多个时间段执行，后续每次开始任务前必须先读取：

1. `IMPLEMENTATION_PLAN.md`
2. 当前目标模块的 `_index.md`
3. 相关功能文件
4. `knowledge-base/changelog/implementation-log.md`
5. 相关原始 PRD 或接口文档

每次执行必须遵守：

- 先确认当前阶段。
- 再确认当前模块。
- 再确认待办任务。
- 不跳阶段。
- 不直接改业务内容，除非当前阶段允许。
- 每次修改必须更新执行日志。
- 发现冲突必须先记录冲突，不得自行拍板。

---

## 14. 当前状态

当前已知状态：

| 模块 | 状态 | 说明 |
|------|------|------|
| Account | 已有内容，需重构校准 | 注册、登录、忘记密码已转译 |
| Security | 已有内容，需重构校准 | 身份认证公共能力已建立骨架 |
| Wallet | 待转译 | 原始 PRD 已归档 |
| Card | 待转译 | 原始 PRD 已归档 |
| Transaction | 待转译 | 原始 PRD 已归档 |
| Growth | 待转译 | 原始 PRD 已归档 |
| Website | 待转译 | 原始 PRD 已归档 |
| Platform | 待转译 | 原始 PRD 已归档 |
| Common | 待建设 | FAQ、通用错误页、通用弹窗、通知内容待结构化 |
| Integrations | 待建设 | DTC、AAI、WalletConnect 外部事实层待结构化 |
| _meta | 待建设 | 工程规范、术语、字段、状态、错误码、合规边界待补齐 |
| prd-template | 待建设 | 新 PRD 写作模板待建设 |

---

## 15. 下一步

下一步执行 Phase 1。

具体任务：

1. 创建或更新 `IMPLEMENTATION_PLAN.md`
2. 更新 `knowledge-base/README.md`
3. 创建 `knowledge-base/_meta/`
4. 创建 `knowledge-base/integrations/`
5. 创建 `knowledge-base/common/`
6. 创建 `knowledge-base/changelog/implementation-log.md`
7. 创建 `prd-template/`
8. 创建知识库写作规范
9. 创建来源引用规范
10. 创建模块模板
11. 创建功能模板

Phase 1 完成后，再进入 Account + Security 重构。
