# AIX Pay 1.0.0_10 APK 前端事实源

## 1. 事实源定位

本目录用于管理 `AIX Pay_1.0.0_10.apk` 的静态拆解结果，作为后续补充 PRD 的客户端事实依据。

> 定位：现网客户端事实源。  
> 用途：补强 PRD、发现历史 PRD 与现网客户端冲突、沉淀页面/接口/前端逻辑索引。  
> 限制：不能替代服务端接口文档、风控规则、后台配置、供应商规则。

## 2. 当前文档

| 文档 | 用途 | 状态 |
| --- | --- | --- |
| [source-summary.md](./source-summary.md) | APK 来源、版本、技术栈、事实优先级说明 | 已建立 |
| [task-ledger.md](./task-ledger.md) | 分模块拆解任务台账 | 已建立 |
| [page-map.md](./page-map.md) | 页面路由清单与模块归属索引 | 初版待复核 |
| [screenshot-handoff.md](./screenshot-handoff.md) | 页面截图采集说明 | 已建立 |

## 3. 后续建议产物

```text
knowledge-base/apk-reverse/aix-pay-1.0.0_10/
├── _index.md
├── source-summary.md
├── task-ledger.md
├── page-map.md
├── api-map.md
├── common-frontend-patterns.md
├── account/
├── kyc/
├── wallet/
├── convert/
├── card/
├── transaction/
├── message/
├── user/
└── review/
```

## 4. PRD 引用建议

PRD 中引用 APK 事实时，建议统一使用以下表达：

```text
当前上线客户端表现为：……
来源：AIX Pay_1.0.0_10.apk 静态分析
事实等级：A/B/C
是否需产品确认：是/否
```

若 APK 与历史 PRD 冲突，默认先记录为：

```text
冲突项：历史 PRD 与现网客户端不一致。
处理建议：以现网客户端为当前事实源，除非产品/服务端确认该表现为 bug 或已计划调整。
```
