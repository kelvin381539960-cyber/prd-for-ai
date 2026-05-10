---
type: verification-status-definition
status: draft
language: zh-CN
last_updated: 2026-05-10
---

# 确认状态定义

每个主要知识块都必须标记确认状态。

## 状态列表

| Status | 含义 | 是否可直接用于用户回答 |
|---|---|---|
| `draft_pending_review` | 初稿，基于历史资料或初步整理，待业务审核 | 可以用于测试，不建议作为正式口径 |
| `confirmed` | 已由业务或当前知识库确认 | 可以作为正式客服口径 |
| `partial_confirmed` | 部分已确认，部分仍待确认 | 仅可回答已确认部分，其他部分需保守处理 |
| `deprecated` | 已废弃或确认不再适用 | 不可用于回答 |
| `internal_only` | 仅供内部使用 | 不可直接对用户输出 |
| `do_not_answer` | 不应由智能客服回答 | 不可回答，需拒答或转人工 |

## 默认状态

从历史资料抽取的新内容，默认状态必须是：

```text
draft_pending_review
```

除非已有明确确认，否则不得标记为 `confirmed`。

## 文件 frontmatter 要求

每个知识文件应包含：

```yaml
verification_status: draft_pending_review
```

如果同一文件内不同内容的确认状态不同，应在对应小节中单独标记。

## 使用规则

- `confirmed`：可以直接作为用户可见答案。
- `partial_confirmed`：只回答已确认部分，不确定部分引导用户以页面提示为准或联系人工客服。
- `draft_pending_review`：仅作为 draft 或测试口径，正式上线前必须审核。
- `deprecated`：不得被智能客服召回。
- `internal_only`：只能内部使用。
- `do_not_answer`：必须转人工或拒答。
