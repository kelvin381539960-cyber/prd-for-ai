---
type: visibility-rules
status: draft
language: zh-CN
last_updated: 2026-05-10
---

# 可见性规则

本文件定义智能客服知识库中哪些内容可以对 C 端用户展示，哪些内容只能内部使用。

## 用户可见内容

以下内容可以用于生成用户回答：

- 功能入口说明
- 用户操作步骤
- 常见问题解释
- 通用排查建议
- 用户需要准备或提供的信息
- 建议联系人工客服的条件
- 以 App 页面提示为准的说明

用户可见内容应放在：

```text
customer-support-kb/user-facing/
customer-support-kb/faq/
```

## 内部可见内容

以下内容只能供内部客服或内部 agent 使用，不得直接输出给用户：

- PRD、archive、legacy、来源文档路径
- 后台字段
- 内部状态机
- 内部审核逻辑
- 风控或合规判断规则
- 供应商处理逻辑
- 未发布功能
- 运营配置
- 内部处理 SLA，除非已确认为用户可见口径
- 内部排查步骤中不适合用户知道的部分

内部内容应放在：

```text
customer-support-kb/agent-internal/
```

## 待确认内容

不确定是否可以对用户展示的内容，应先放在：

```text
customer-support-kb/unresolved/pending-confirmation.md
```

## 不可回答内容

明确不适合智能客服回答的问题，应放在：

```text
customer-support-kb/unresolved/do-not-answer.md
```

## 输出规则

当生成用户回答时：

1. 只能使用 `user-facing/` 和 `faq/` 中的用户可见内容。
2. 不得向用户展示来源路径、PRD 名称或内部文档名称。
3. 如果需要用到 `agent-internal/` 内容，只能转换为安全、简洁的用户口径。
4. 如果无法安全转换，必须转人工。
