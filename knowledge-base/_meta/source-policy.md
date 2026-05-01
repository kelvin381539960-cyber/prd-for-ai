---
module: _meta
feature: source-policy
version: "1.0"
status: draft
source_doc: IMPLEMENTATION_PLAN.md
source_section: "9. 来源与引用规则"
last_updated: 2026-05-01
owner: 吴忆锋
readers: [product, dev, qa, business, ai]
---

# Source Policy 来源与引用规则

## 1. 来源优先级

1. `历史prd/` 原始 PRD
2. `DTC接口文档/` 接口文档
3. 已确认的项目规则 / 评审结论
4. 外部公开资料，仅用于行业、政策、竞品，不作为 AIX 内部规则来源

## 2. 禁止事项

- 禁止无来源推测。
- 禁止把未确认事项写成已确认规则。
- 禁止私自补全接口字段。
- 禁止私自改变状态机。
- 禁止私自改变资金路径。
- 禁止私自改变风控 / 合规边界。

## 3. 来源引用格式

```text
(Ref: 来源文件名 / 章节 / 版本或日期)
```

示例：

```text
(Ref: AIX Security 身份认证需求V1.0 / 7.4 活体有效期说明 / 2025-11-28)
```

## 4. 冲突处理模板

```markdown
## 冲突 / 待确认

- 冲突点：
- 涉及文件：
- 影响范围：
- 建议确认人：
- 当前处理：
```

## 5. 待补充

- 补齐历史 PRD 文件与知识库模块的映射表。
- 补齐 DTC 接口文档与 integrations 模块的映射表。
