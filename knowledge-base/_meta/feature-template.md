---
module: _meta
feature: feature-template
version: "1.0"
status: draft
source_doc: IMPLEMENTATION_PLAN.md
source_section: "6. 单个功能文件标准结构"
last_updated: 2026-05-01
owner: 吴忆锋
readers: [product, ui, dev, qa, business, ai]
---

# Feature Template 功能模板

复制本模板创建功能文件。

```markdown
---
module:
feature:
version: "1.0"
status: draft
source_doc:
source_section:
last_updated:
owner:
depends_on: []
readers: [product, ui, dev, qa, business, ai]
---

# 功能名称

## 1. 功能定位

说明该功能解决什么问题，只写事实，不写愿景。

## 2. 适用范围

| 维度 | 规则 | 来源 | 备注 |
|------|------|------|------|
| 国家 / 地区 | TBD | TBD | TBD |
| 用户状态 | TBD | TBD | TBD |
| 账户状态 | TBD | TBD | TBD |
| 钱包 / 卡状态 | TBD | TBD | TBD |

## 3. 前置条件

| 条件 | 说明 | 来源 |
|------|------|------|
| TBD | TBD | TBD |

## 4. 标准流程

```text
待补充
```

| 步骤 | 角色 | 动作 | 系统处理 | 下一步 |
|------|------|------|----------|--------|
| 1 | 用户 | TBD | TBD | TBD |

## 5. 页面与交互规则

| 页面 | 元素 | 规则 | 异常 | 来源 |
|------|------|------|------|------|
| TBD | TBD | TBD | TBD | TBD |

## 6. 状态机

如不适用，写：本功能无独立状态机。

| 状态 | 含义 | 是否终态 | 可迁移到 | 来源 |
|------|------|----------|----------|------|
| TBD | TBD | TBD | TBD | TBD |

## 7. 字段与接口依赖

| 接口 / 字段 | 读/写 | 用途 | 来源 | 备注 |
|-------------|------|------|------|------|
| TBD | TBD | TBD | TBD | TBD |

## 8. 异常与失败处理

| 场景 | 触发条件 | 用户提示 | 系统动作 | 最终状态 | 来源 |
|------|----------|----------|----------|----------|------|
| TBD | TBD | TBD | TBD | TBD | TBD |

## 9. 风控 / 合规边界

| 边界 | 规则 | 资金影响 | 来源 | 待确认 |
|------|------|----------|------|--------|
| TBD | TBD | TBD | TBD | TBD |

## 10. 多角色阅读视角

### UI 视角

- TBD

### 开发视角

- TBD

### 测试视角

- TBD

### 业务视角

- TBD

### AI 复用视角

- TBD

## 11. 待确认事项

| 问题 | 影响范围 | 建议确认人 | 状态 |
|------|----------|------------|------|
| TBD | TBD | TBD | open |

## 12. 来源引用

- (Ref: TBD)
```
