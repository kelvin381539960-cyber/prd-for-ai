---
module: changelog
feature: knowledge-gaps
version: "1.0"
status: active
source_doc: IMPLEMENTATION_PLAN.md
source_section: source-policy
last_updated: 2026-05-01
owner: 吴忆锋
readers: [product, ai]
---

# Knowledge Gaps 知识缺口与冲突记录

## 1. 文档定位

本文档用于集中记录知识库转译过程中发现的文档缺口、原文疑似异常、口径冲突和需要后续确认的信息。

功能正文应优先承载稳定事实；不确定事项集中放在本文档，避免污染事实来源正文。

## 2. Account / Login

| 编号 | 问题 | 影响范围 | 来源 | 当前处理 | 状态 |
|------|------|----------|------|----------|------|
| KG-LOGIN-001 | Login Page 原始 PRD Description 列从第 4 项开始，1-3 项仅存在于 UX 截图，缺少可结构化文字规则 | Login Page / 页面元素 | AIX Card 注册登录需求V1.0 / 7.2.4 Login Page | 正文保留截图与已知结构化规则；缺失项不脑补 | open |
| KG-LOGIN-002 | 账号不存在 / 未注册提示为中文原文：`您输入的账号信息有误，请检查或注册新账号。`，英文最终文案缺失 | Login Page / 文案 | AIX Card 注册登录需求V1.0 / 7.2.4 Login Page | 正文保留中文原文，不替换为英文推测 | open |
| KG-LOGIN-003 | `Phone number must be at least 6 digits` 来自当前知识库旧内容，需确认是否为最终翻译文案 | Login Page / Phone 校验 | 当前知识库旧版 login.md | 正文保留该提示并标注来源为当前知识库旧内容 | open |
| KG-LOGIN-004 | 中国和中国台湾选项隐藏规则需确认由后端过滤还是前端过滤 | Select Country Page | AIX Card 注册登录需求V1.0 / 7.2.4.1 Select Country Page | 正文仅写“隐藏”，不判断前后端责任 | open |
| KG-LOGIN-005 | Android 指纹原文出现“若协议已全部勾选”，疑似串入注册协议逻辑 | Biometric Login / Android Fingerprint | AIX Card 注册登录需求V1.0 / 7.2.5 Biometric 登录 | 正文不采纳该疑似串文；保留为缺口记录 | open |
| KG-LOGIN-006 | Enable BIO 的系统授权差异、权限弹窗样式、跳转设置页方式需结合 iOS / Android 实现确认 | Enable BIO Page | AIX Card 注册登录需求V1.0 / 7.2.7 Enable BIO Page | 正文只保留“已授权 / 未授权”业务规则 | open |

## 3. Account / Registration

| 编号 | 问题 | 影响范围 | 来源 | 当前处理 | 状态 |
|------|------|----------|------|----------|------|
| KG-REG-001 | Registration Page 协议复选框默认状态存在口径差异：原始 PRD 有“默认为勾选状态（待合规确定）”，当前知识库旧内容写“默认为不勾选状态” | Registration Page / 合规 | AIX Card 注册登录需求V1.0 / 7.1.4 Registration Page | 功能正文暂按“必选协议需同意后才可继续”表达，不写默认勾选口径 | open |
| KG-REG-002 | Email 已注册提示文案需确认是否统一为 `This email has been used`，还是只要求明确提示并引导登录 | Registration Page / 文案 | AIX Card 注册登录需求V1.0 / 7.1.4 Registration Page；旧知识库 | 正文保留已知文案并标注来源差异 | open |
| KG-REG-003 | AIX Tag 错误提示存在两套文案 | Set AIX Tag Page / 文案 | AIX Card 注册登录需求V1.0 / 7.1.7 Set Tag Page；旧知识库 | 正文保留两套文案来源，不做统一替换 | open |
| KG-REG-004 | 注册频控的设备指纹、IP、接口总限流规则需确认后端实现口径 | Registration Page / 风控 | 旧知识库 / 注册 PRD | 正文标注需与后端限流策略确认 | open |
| KG-REG-005 | Set Password 是否仍存在 Re-enter Password Page 作为确认密码页，需结合最新 UX 确认 | Set Password / Registration | AIX Card 注册登录需求V1.0 / 7.1.6-7.1.7；2025-11-18 变更 | 正文采用“创建密码即注册成功”口径；保留缺口 | open |

## 4. Account / Password Reset

| 编号 | 问题 | 影响范围 | 来源 | 当前处理 | 状态 |
|------|------|----------|------|----------|------|
| KG-PWD-001 | Reset Password Page 的 Phone 格式校验是否完全复用 Login Page，需确认最终口径 | Password Reset / Login | AIX Card 注册登录需求V1.0 / 7.3.3 Reset Password Page | 正文标注复用登录输入能力，但不扩展未确认规则 | open |
| KG-PWD-002 | Reset Password Page 的账号不存在提示文案缺少英文最终口径 | Password Reset / 文案 | AIX Card 注册登录需求V1.0 / 7.3.3 Reset Password Page | 正文不推断英文文案 | open |
| KG-PWD-003 | 密码重置成功后是否需要展示成功页 / Toast，当前文档只明确强制登出和重新登录 | Password Reset Result | AIX Card 注册登录需求V1.0 / 7.3.5 设置密码页 | 正文只保留强制登出和关闭 BIO | open |
| KG-PWD-004 | 关闭 BIO 的系统动作需确认：仅清除本地凭证，还是同时后端关闭该设备 BIO 开关 | Password Reset / Biometric | AIX Card 注册登录需求V1.0 / 7.3.1 功能说明 | 正文写“清除 BIO / 自动关闭 BIO”，不判断系统层实现 | open |
| KG-PWD-005 | Set Password 是否仍存在确认密码页，需结合最新 UX 确认 | Password Reset / Registration | AIX Card 注册登录需求V1.0 / 7.3.5 设置密码页 | 正文复用 Registration 密码规则 | open |
