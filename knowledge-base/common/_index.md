---
module: common
description: APP 通用能力，沉淀 FAQ、通用错误页、通用弹窗、通知内容等跨模块能力
version: "1.0"
status: draft
source_docs: [历史prd]
last_updated: 2026-05-01
owner: 吴忆锋
depends_on: [_meta]
readers: [product, ui, dev, qa, business, ai]
---

# Common APP 通用能力

## 1. 模块定位

本模块用于沉淀跨业务模块复用的 APP 通用能力，包括通用错误页、通用弹窗、FAQ、通知内容等。

原 `app-common` 后续统一迁移为 `common`。

## 2. 功能清单

| 功能 | 文件 | 状态 | 说明 |
|------|------|------|------|
| 通用错误页 | common-error-pages.md | 待创建 | Network Error / Server Error 等页面级异常 |
| 通用弹窗 | common-popups.md | 待创建 | 网络异常、服务器异常、确认离开等弹窗 |
| FAQ | faq.md | 待创建 | APP 通用 FAQ 与场景 FAQ |
| 通知内容 | notification-content.md | 待创建 | Push、站内信、系统通知内容 |

## 3. 维护规则

- 通用能力应优先放在 common，业务模块引用 common。
- 若某弹窗只属于单个业务功能，可放在对应功能文件中。
- FAQ 需记录适用场景和来源。
- 通知内容需记录触发条件、接收对象、展示渠道。
