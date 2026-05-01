---
module: _meta
feature: module-template
version: "1.0"
status: draft
source_doc: IMPLEMENTATION_PLAN.md
source_section: "10. 实施阶段"
last_updated: 2026-05-01
owner: 吴忆锋
readers: [product, ui, dev, qa, business, ai]
---

# Module Template 模块模板

复制本模板创建模块 `_index.md`。

```markdown
---
module:
description:
version: "1.0"
status: draft
source_docs: []
last_updated:
owner:
depends_on: []
readers: [product, ui, dev, qa, business, ai]
---

# 模块名称

## 1. 模块定位

说明本模块承载的业务范围。

## 2. 功能清单

| 功能 | 文件 | 状态 | 说明 | 来源 |
|------|------|------|------|------|
| TBD | TBD | draft | TBD | TBD |

## 3. 适用范围

| 维度 | 范围 | 来源 | 备注 |
|------|------|------|------|
| 国家 / 地区 | TBD | TBD | TBD |
| 用户状态 | TBD | TBD | TBD |
| 账户状态 | TBD | TBD | TBD |
| 钱包 / 卡状态 | TBD | TBD | TBD |

## 4. 模块依赖

| 依赖对象 | 依赖内容 | 来源 | 备注 |
|----------|----------|------|------|
| _meta | 全局字段、状态、错误码、合规边界 | TBD | TBD |
| integrations | 外部接口与渠道规则 | TBD | TBD |
| security | 身份认证能力 | TBD | TBD |
| common | 通用页面、弹窗、FAQ | TBD | TBD |

## 5. 核心流程总览

```text
待补充
```

## 6. 状态机总览

如不适用，写：本模块无独立状态机。

## 7. 字段与接口总览

| 接口 / 字段 | 所属功能 | 来源 | 备注 |
|-------------|----------|------|------|
| TBD | TBD | TBD | TBD |

## 8. 风控 / 合规边界

| 边界 | 影响功能 | 来源 | 备注 |
|------|----------|------|------|
| TBD | TBD | TBD | TBD |

## 9. 待确认事项

| 问题 | 影响范围 | 建议确认人 | 状态 |
|------|----------|------------|------|
| TBD | TBD | TBD | open |

## 10. 来源引用

- (Ref: TBD)
```
