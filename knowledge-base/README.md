---
project: AIX Card
type: prd-knowledge-base
created: 2025-10-21
last_updated: 2026-05-01
maintainer: 吴忆锋
plan: ../IMPLEMENTATION_PLAN.md
status: active
---

# AIX Card PRD Knowledge Base

本目录是 AIX 的 AI-readable PRD 知识库。

它不是原始 PRD 归档，也不是临时需求草稿。它用于沉淀可追溯、可复用、可检索的产品事实，服务后续 PRD 编写、需求评审、UI 设计、研发实现、测试验收、业务对齐与 AI 复用。

## 事实源关系

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
└──────────────┬─────────────┘
               │ 复用
               ▼
┌────────────────────────────┐
│  prd-template/              │
│  后续新 PRD 写作模板          │
└────────────────────────────┘
```

## 目录结构

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
│   └── walletconnect/
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

## app-common 迁移口径

原规划中的 `app-common` 统一迁移为 `common`。

后续不再新增 `app-common` 目录。FAQ、通用错误页、通用弹窗、通知内容等统一归入 `common/`。

## 模块依赖关系

```text
_meta                      全局事实与规范
integrations               外部系统事实源
security                   公共身份认证能力
common                     通用页面、弹窗、FAQ、通知能力

account / wallet / card / transaction / growth / website / platform
    ↑
    业务模块按需依赖 _meta、integrations、security、common
```

## 文档规范

### 文件命名

- 全小写。
- 单词用 `-` 连接。
- 每个模块目录必须有 `_index.md`。
- 一个核心业务能力一个 Markdown 文件。
- 不按原始 PRD 文件机械拆分。
- 不拆成页面级小文件，避免维护成本过高。

### Frontmatter 字段

| 字段 | 说明 | 示例 |
|------|------|------|
| module | 所属模块 | `wallet` |
| feature | 功能名 | `deposit-walletconnect` |
| version | 版本号 | `1.0` |
| status | 状态 | `draft / in_review / active / released / deprecated` |
| source_doc | 来源文档 | `历史prd/AIX Wallet V1.0【Deposit & Send & Swap 】.docx` |
| source_section | 来源章节 | `5.4 钱包链接充值Deposit（WalletConnect）` |
| last_updated | 最后更新日期 | `2026-05-01` |
| owner | 负责人 | `吴忆锋` |
| depends_on | 依赖知识文件 | `[security/face-authentication, integrations/dtc]` |
| readers | 阅读对象 | `[product, ui, dev, qa, business, ai]` |

### 功能文件结构

每个核心功能文件应包含：

1. 功能定位
2. 适用范围
3. 前置条件
4. 标准流程
5. 页面与交互规则
6. 状态机
7. 字段与接口依赖
8. 异常与失败处理
9. 风控 / 合规边界
10. 多角色阅读视角
11. 待确认事项
12. 来源引用

## 来源与引用原则

来源优先级：

1. `历史prd/` 原始 PRD
2. `DTC接口文档/` 接口文档
3. 已确认的项目规则 / 评审结论
4. 外部公开资料，仅用于行业、政策、竞品，不作为 AIX 内部规则来源

禁止：

- 无来源推测。
- 把未确认事项写成已确认规则。
- 私自补全接口字段。
- 私自改变状态机。
- 私自改变资金路径。
- 私自改变风控 / 合规边界。

## 当前转译状态

| 模块 | 状态 | 说明 |
|------|------|------|
| _meta | 待建设 | 全局事实与规范待补齐 |
| integrations | 待建设 | DTC、AAI、WalletConnect 外部事实层待结构化 |
| common | 待建设 | FAQ、通用错误页、通用弹窗、通知内容待结构化 |
| account | 已有内容，需重构校准 | 注册、登录、忘记密码已转译 |
| security | 已有内容，需重构校准 | 身份认证公共能力已建立骨架 |
| wallet | 待转译 | 原始 PRD 已归档 |
| card | 待转译 | 原始 PRD 已归档 |
| transaction | 待转译 | 原始 PRD 已归档 |
| growth | 待转译 | 原始 PRD 已归档 |
| website | 待转译 | 原始 PRD 已归档 |
| platform | 待转译 | 原始 PRD 已归档 |

## 执行规则

跨对话继续执行时，必须先读取：

1. `IMPLEMENTATION_PLAN.md`
2. `knowledge-base/README.md`
3. `knowledge-base/changelog/implementation-log.md`
4. 当前目标模块 `_index.md`
5. 相关原始 PRD 或接口文档
