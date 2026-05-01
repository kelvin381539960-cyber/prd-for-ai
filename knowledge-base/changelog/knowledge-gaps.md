---
module: changelog
feature: knowledge-gaps
version: "1.0"
status: active
source_doc: IMPLEMENTATION_PLAN.md
source_section: source-policy
last_updated: 2026-05-01
owner: 吴忆锋
---

# Knowledge Gaps 知识缺口与冲突记录

## 1. 文档定位

本文档用于集中记录知识库转译过程中发现的文档缺口、原文疑似异常、口径冲突和需要后续确认的信息。

功能正文应优先承载稳定事实；不确定事项集中放在本文档，避免污染事实来源正文。

## 2. Account / Login

| 编号 | 问题 | 影响范围 | 来源 | 当前处理 | 状态 |
|---|---|---|---|---|---|
| KG-LOGIN-001 | Login Page 原始 PRD Description 列从第 4 项开始，1-3 项仅存在于 UX 截图，缺少可结构化文字规则 | Login Page / 页面元素 | AIX Card 注册登录需求V1.0 / 7.2.4 Login Page | 正文保留截图与已知结构化规则；缺失项不脑补 | open |
| KG-LOGIN-002 | 账号不存在 / 未注册提示为中文原文：`您输入的账号信息有误，请检查或注册新账号。`，英文最终文案缺失 | Login Page / 文案 | AIX Card 注册登录需求V1.0 / 7.2.4 Login Page | 正文保留中文原文，不替换为英文推测 | open |
| KG-LOGIN-003 | `Phone number must be at least 6 digits` 来自当前知识库旧内容，需确认是否为最终翻译文案 | Login Page / Phone 校验 | 当前知识库旧版 login.md | 正文保留该提示并标注来源为当前知识库旧内容 | open |
| KG-LOGIN-004 | 中国和中国台湾选项隐藏规则需确认由后端过滤还是前端过滤 | Select Country Page | AIX Card 注册登录需求V1.0 / 7.2.4.1 Select Country Page | 正文仅写“隐藏”，不判断前后端责任 | open |
| KG-LOGIN-005 | Android 指纹原文出现“若协议已全部勾选”，疑似串入注册协议逻辑 | Biometric Login / Android Fingerprint | AIX Card 注册登录需求V1.0 / 7.2.5 Biometric 登录 | 正文不采纳该疑似串文；保留为缺口记录 | open |
| KG-LOGIN-006 | Enable BIO 的系统授权差异、权限弹窗样式、跳转设置页方式需结合 iOS / Android 实现确认 | Enable BIO Page | AIX Card 注册登录需求V1.0 / 7.2.7 Enable BIO Page | 正文只保留“已授权 / 未授权”业务规则 | open |
