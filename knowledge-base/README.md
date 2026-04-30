---
project: AIX Card
type: prd-knowledge-base
created: 2025-10-21
last_updated: 2026-04-30
maintainer: 吴忆锋
---

# AIX Card PRD Knowledge Base

AI 可读的全量 PRD 知识库，服务于：
1. AI 自动生成 UI 代码（读 PRD → 生成前端组件/页面）
2. AI 辅助撰写新 PRD（参考已有标准和模板）
3. 人类阅读和管理（模块化目录、统一格式）

---

## 目录结构

```
prd-knowledge-base/
├── _meta/                 全局配置（术语表、设计规范、字段定义）
├── security/              🔒 安全/身份认证（公共能力层）
├── account/               👤 账户模块（注册、登录、忘记密码）
├── card/                  💳 卡模块（申请、管理、ME模块）
├── transaction/           💰 交易模块（卡交易、交易记录&历史）
├── wallet/                👛 钱包模块（KYC、资产、充值、转账、兑换）
├── growth/                📈 增长/运营（MGM、推送、Banner、Waitlist、系统邮件）
├── website/               🌐 官网（一期、二期）
├── platform/              ⚙️  平台能力（OBOSS、多语言）
├── app-common/            📱 APP通用（FAQ）
├── assets/                🖼️  图片资源（按模块分目录）
└── changelog/             📝 迭代变更记录
```

## 模块依赖关系

```
security (公共能力层)
    ↑
    ├── account (注册/登录/重置密码)
    ├── card (敏感操作验证)
    ├── wallet (敏感操作验证)
    └── transaction (交易确认)
```

## 文档规范

### 文件命名
- 全小写，单词用 `-` 连接
- 每个模块目录下必须有 `_index.md`（模块总览）

### Frontmatter 字段

| 字段 | 说明 | 示例 |
|------|------|------|
| module | 所属模块 | `account` |
| feature | 功能名 | `registration` |
| version | 版本号 | `1.0` |
| last_updated | 最后更新日期 | `2025-11-11` |
| authors | 作者列表 | `[吴忆锋]` |
| status | 状态 | `draft / in_review / released` |
| depends_on | 依赖的其他文档 | `[security/otp-verification]` |

### 页面需求描述结构

每个页面按以下结构描述：
1. 页面截图（引用 assets 目录图片）
2. 页面元素表（元素名、类型、规则、必填）
3. 交互逻辑（分元素详细描述）
4. 异常处理（错误场景 + 提示文案）
5. 频控/安全规则（如适用）

---

## 转译进度

| 模块 | 状态 | 文件数 |
|------|------|--------|
| security | ✅ 已完成骨架 | 4 |
| account | ✅ 已完成 | 4 |
| card | ⏳ 待转译 | - |
| transaction | ⏳ 待转译 | - |
| wallet | ⏳ 待转译 | - |
| growth | ⏳ 待转译 | - |
| website | ⏳ 待转译 | - |
| platform | ⏳ 待转译 | - |
| app-common | ⏳ 待转译 | - |
| _meta | ⏳ 待转译 | - |
