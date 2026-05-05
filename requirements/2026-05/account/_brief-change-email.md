---
type: prd-brief
module: account
feature: change-email
status: draft
created: 2026-05-05
last_updated: 2026-05-05
owner: TBD
target_prd: requirements/2026-05/account/change-email.md
source_doc: 用户需求 2026-05-05；prd-template/prd-writing-workflow.md；prd-template/standard-prd-template.md；requirements/_index.md；knowledge-base/_ai-query-router.md；knowledge-base/account/_index.md；knowledge-base/security/_index.md；knowledge-base/security/global-rules.md；knowledge-base/security/email-otp-verification.md；knowledge-base/_system-boundary.md；knowledge-base/changelog/knowledge-gaps.md
---

# 更换邮箱 PRD Brief

## 1. 需求背景

用户希望增加“更换邮箱”功能，使已注册用户可以在 AIX 内将账户邮箱更新为新的邮箱地址。

当前 Account 知识库已沉淀注册、登录、密码重置、账户状态、邮箱唯一性、手机号唯一性和设备绑定规则；Security 知识库已沉淀 AIX 自有认证能力、认证优先级、Email OTP 页面规则、锁定规则和验证码规则。

本 brief 先确认功能边界与待确认问题。经确认后，再按标准 PRD 模板生成正式 PRD：`requirements/2026-05/account/change-email.md`。

## 2. 功能归属与粒度判断

| 项目 | 判断 |
|---|---|
| 主模块 | Account |
| 依赖模块 | Security / Email OTP Verification |
| 功能粒度 | 独立功能 |
| 原因 | 更换邮箱有独立入口、独立安全校验、独立数据更新结果和独立异常处理，不应混入注册、登录或密码重置 PRD。Security 仅作为认证公共能力被引用，不在本 PRD 重复定义认证规则。 |

## 3. 已确认事实

1. Account 模块覆盖 AIX 用户账户体系事实，是 Wallet、Card、Transaction 等后续业务模块的账户前置基础。
2. 邮箱全局唯一，不允许重复注册或绑定。
3. Account 当前已沉淀 Registration、Login、Password Reset，但尚未沉淀 Change Email。
4. Security 是 AIX 身份认证公共能力层，业务模块不得重复定义认证方式、认证优先级、失败次数、锁定规则和有效期。
5. AIX 自有认证方式包括 OTP、Email OTP、Login Passcode、Biometric。
6. Email OTP 为 4 位数字验证码，有效期 5 分钟；进入 Email OTP Verify Page 后自动发送；输入满 4 位后自动提交。
7. 每次重新发送 Email OTP 会生成新的 OTP，旧 OTP 立即失效，仅最新一次 OTP 有效。
8. Email OTP 验证码仅限发起请求设备使用，更换设备验证无效。
9. Email OTP 失败与重发存在锁定 / 冷却规则：24 小时内失败 5 次锁定 20 分钟，10 次锁定 24 小时；24 小时内最多重发 3 次。
10. 当前 Security 场景矩阵已包含“首次绑定手机号 / 更换手机号”“修改密码”等场景，但未明确包含“更换邮箱”场景。

## 4. 建议本期范围

> 下表为 brief 建议范围。未在知识库中明确的规则均标记为待确认，正式 PRD 不会写成已确认事实。

| 功能点 | 是否纳入 | 说明 | 当前状态 |
|---|---:|---|---|
| 更换邮箱入口 | 是 | 用户从账户 / 安全设置等入口发起更换邮箱；具体入口位置待确认。 | 待确认 |
| 当前邮箱展示 | 是 | 展示当前账户邮箱，建议使用掩码；是否复用 Email OTP 掩码规则待确认。 | 待确认 |
| 当前身份验证 | 是 | 用户更换邮箱前需完成当前账户身份验证；认证方式需由 Security 场景矩阵补充确认。 | 待确认 |
| 新邮箱输入 | 是 | 用户输入新邮箱地址；需校验格式、不可与当前邮箱相同、不可与已存在邮箱冲突。 | 待确认 |
| 邮箱唯一性校验 | 是 | 邮箱全局唯一为已确认事实；更换邮箱场景的校验时机、错误文案和接口返回需确认。 | 待确认 |
| 新邮箱 Email OTP 验证 | 是 | 建议向新邮箱发送 Email OTP，以确认用户可接收新邮箱邮件；具体是否必须、是否还需要旧邮箱 OTP 待确认。 | 待确认 |
| 更新账户邮箱 | 是 | 验证通过后将账户邮箱更新为新邮箱；更新后登录、找回密码、Email OTP 接收邮箱的生效范围需确认。 | 待确认 |
| 成功结果页 / 成功提示 | 是 | 更换成功后展示成功状态并返回账户 / 安全设置页；页面形态和文案待确认。 | 待确认 |
| 成功后安全处理 | 是 | 是否强制登出、是否清除 BIO、是否踢出其他设备、是否刷新登录态待确认。 | 待确认 |
| 通知 | 待定 | 是否向旧邮箱 / 新邮箱 / 站内信 / Push 发送安全通知待确认。 | 待确认 |
| 外部系统同步 | 待定 | 如需同步 DTC / AAI / KUN 等外部账户上下文，只能写 AIX 调用 / 接收 / 记录 / 展示边界，不写外部系统内部逻辑。 | 待确认 |

## 5. 建议主流程

```text
用户进入更换邮箱入口
→ AIX 展示当前邮箱与更换入口
→ 用户发起更换邮箱
→ AIX 调用 Security 完成当前账户身份验证
→ 用户输入新邮箱
→ AIX 校验新邮箱格式与唯一性
→ AIX 向新邮箱发送 Email OTP
→ 用户输入 4 位 Email OTP
→ Security 校验 Email OTP
→ 校验成功后 AIX 更新账户邮箱
→ AIX 展示更换成功结果
```

## 6. 建议页面 / 节点

| 页面 / 节点 | 目的 | 关键规则 |
|---|---|---|
| Change Email Entry | 承载入口和当前邮箱信息 | 入口位置、当前邮箱掩码展示待确认 |
| Current Account Verification | 验证当前账户操作者身份 | 引用 Security；更换邮箱场景的认证方式待确认 |
| New Email Input | 输入新邮箱地址 | 格式校验、重复校验、与当前邮箱相同校验待确认 |
| Email OTP Verify Page | 验证新邮箱可接收邮件 | 复用 Email OTP 4 位验证码、5 分钟有效、自动提交、重发与锁定规则 |
| Change Email Success | 告知用户邮箱已更换 | 成功提示、返回路径、是否强制重新登录待确认 |
| Failure / Locked / Expired | 处理失败、锁定、过期 | 复用 Security 对应失败、锁定、过期规则；业务失败文案待确认 |

## 7. 初版验收标准建议

1. 用户可以从指定入口发起更换邮箱流程。
2. 用户在完成当前账户身份验证前，不能进入最终邮箱更新动作。
3. 新邮箱必须满足邮箱格式要求。
4. 新邮箱不能与当前账户邮箱相同。
5. 新邮箱不能与其他账户已注册 / 已绑定邮箱冲突。
6. 系统向新邮箱发送 Email OTP，并按 Email OTP 规则完成验证。
7. Email OTP 验证成功后，账户邮箱更新为新邮箱。
8. Email OTP 验证失败、锁定、过期、重发超限时，按 Security / Email OTP 既有规则处理。
9. 更换成功后，后续涉及账户邮箱展示和 Email OTP 接收的场景使用新邮箱；具体生效范围待确认后写入正式 PRD。
10. 更换失败时，不得更新账户邮箱。

## 8. 待确认问题

| 编号 | 问题 | 建议确认对象 | 影响 |
|---|---|---|---|
| CE-GAP-001 | 更换邮箱入口位于 Account、Profile、Security Settings 还是其他页面？ | 产品 / UX | 页面结构与导航路径 |
| CE-GAP-002 | Security 场景矩阵是否新增“更换邮箱”场景？认证方式使用 Login Passcode / Biometric / OTP / Email OTP 中的哪几种？ | 产品 / Security / 后端 | 当前身份验证规则 |
| CE-GAP-003 | 更换邮箱是否需要验证旧邮箱，还是只验证当前账户身份 + 新邮箱 OTP？ | 产品 / Security / 风控 | 安全等级与流程长度 |
| CE-GAP-004 | 新邮箱唯一性校验在输入后实时校验、提交后校验，还是发送 OTP 前校验？ | 产品 / 后端 / 前端 | 错误提示与接口时机 |
| CE-GAP-005 | 新邮箱已被使用时，是否复用注册文案 `This email has been used`？ | 产品 / UX | 文案一致性 |
| CE-GAP-006 | 更换成功后是否强制登出、是否清除 BIO、是否踢出其他设备？ | 产品 / Security / 后端 | 账户安全与会话管理 |
| CE-GAP-007 | 更换成功后，登录账号、找回密码邮箱、Email OTP 接收邮箱是否立即切换为新邮箱？ | 产品 / Account / 后端 | 账号标识与后续认证 |
| CE-GAP-008 | 是否需要向旧邮箱、新邮箱、站内信或 Push 发送安全通知？ | 产品 / Notification / Security | 用户感知与风险告知 |
| CE-GAP-009 | Banned / Closed / Locked 等账户状态下是否允许更换邮箱？ | 产品 / Security / 风控 | 入口拦截与状态规则 |
| CE-GAP-010 | 更换邮箱是否需要同步或影响外部账户上下文，例如 DTC / AAI / KUN？ | 后端 / 外部依赖负责人 | 系统边界与外部依赖 |

> 以上待确认项暂写入本 brief，不写入知识库 `knowledge-base/changelog/knowledge-gaps.md`。如正式 PRD 需要长期保留缺口，再按知识库规则统一登记到 ALL-GAP。

## 9. 正式 PRD 写作建议

确认 brief 后，正式 PRD 建议按以下结构展开：

1. 文档信息
2. 背景、目标与范围
3. 业务流程与规则
4. 页面与交互规则
5. 字段、接口与数据需求
6. 通知与安全边界
7. 异常与失败处理
8. 权限、合规与风控边界
9. 待确认项
10. 验收标准与测试要点
11. 来源引用

## 10. 来源引用

- (Ref: 用户需求 / 2026-05-05 / “我希望增加一个更换邮箱的功能”)
- (Ref: prd-template/prd-writing-workflow.md)
- (Ref: prd-template/standard-prd-template.md)
- (Ref: requirements/_index.md)
- (Ref: knowledge-base/_ai-query-router.md)
- (Ref: knowledge-base/account/_index.md)
- (Ref: knowledge-base/security/_index.md)
- (Ref: knowledge-base/security/global-rules.md)
- (Ref: knowledge-base/security/email-otp-verification.md)
- (Ref: knowledge-base/_system-boundary.md)
- (Ref: knowledge-base/changelog/knowledge-gaps.md)
