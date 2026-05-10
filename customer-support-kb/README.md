---
type: customer-support-kb-index
status: draft
language: zh-CN
last_updated: 2026-05-10
---

# Customer Support KB

本目录用于构建面向 C 端用户的中文智能客服知识库。

当前版本为 draft，后续需要业务审核后才能作为正式客服口径使用。

## 使用范围

本知识库支持智能客服回答以下问题：

1. 注册 / 登录
2. KYC / 身份验证 / 钱包开户
3. 钱包资产 / 充值 / 发送 / 兑换
4. 卡申请 / 卡管理 / 卡交易
5. 通知 / 系统邮件
6. 官网 / FAQ

## 目录说明

| 目录 / 文件 | 作用 |
|---|---|
| `_answer-policy.md` | 智能客服回答规则 |
| `_visibility-rules.md` | 用户可见与内部可见内容边界 |
| `_verification-status.md` | 确认状态定义 |
| `_handoff-rules.md` | 转人工规则 |
| `user-facing/` | 可用于生成用户回答的知识内容 |
| `agent-internal/` | 仅供内部客服或内部 agent 使用的排查手册 |
| `faq/` | FAQ 问答知识 |
| `unresolved/` | 待确认和不可回答内容 |

## 重要规则

- 默认使用中文回答用户。
- 不向用户暴露 PRD、archive、legacy、来源路径或内部文档名称。
- 不把历史 PRD 内容直接当作当前产品事实。
- 不确定的内容必须标记为 `draft_pending_review` 或放入 `unresolved/pending-confirmation.md`。
- 不适合由智能客服回答的问题必须放入 `unresolved/do-not-answer.md`。
- 用户可见回答只能基于 `user-facing/` 和 `faq/` 生成。
- `agent-internal/` 内容只能供内部客服或内部 agent 使用，不得直接输出给用户。

## 当前状态

- status: draft
- verification: pending business review
- language: zh-CN
