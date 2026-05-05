---
type: prd-brief
module: account
feature: change-email
status: reviewed-awaiting-prd-confirmation
created: 2026-05-05
last_updated: 2026-05-05
owner: TBD
target_prd: requirements/2026-05/account/change-email.md
source_doc: 用户需求 2026-05-05；用户补充确认 2026-05-05；Atome SG Help - How do I change the email address for my account；Atome MY Help - How do I change the email address for my account；Atome SG Help - How do I change the mobile number for my account；Atome PH Help - How do I update my account details；prd-template/prd-writing-workflow.md；prd-template/standard-prd-template.md；requirements/_index.md；knowledge-base/_ai-query-router.md；knowledge-base/account/_index.md；knowledge-base/security/_index.md；knowledge-base/security/global-rules.md；knowledge-base/security/email-otp-verification.md；knowledge-base/_system-boundary.md；knowledge-base/changelog/knowledge-gaps.md；OWASP Email Validation and Verification Cheat Sheet；OWASP Changing A User's Registered Email Address；OWASP API Security API2:2023 Broken Authentication；OWASP Multifactor Authentication Cheat Sheet
---

# 更换邮箱 PRD Brief

## 1. 需求背景

用户希望增加“更换邮箱”功能，使已注册用户可以在 AIX 内将账户邮箱更新为新的邮箱地址。

当前 Account 知识库已沉淀注册、登录、密码重置、账户状态、邮箱唯一性、手机号唯一性和设备绑定规则；Security 知识库已沉淀 AIX 自有认证能力、认证优先级、Email OTP 页面规则、锁定规则和验证码规则。

本 brief 用于确认功能边界、用户补充结论、Atome 调研结论和产品建议。确认后，再按标准 PRD 模板生成正式 PRD：`requirements/2026-05/account/change-email.md`。

## 2. 功能归属与粒度判断

| 项目 | 判断 |
|---|---|
| 主模块 | Account |
| 依赖模块 | Security / Email OTP Verification / Notification |
| 功能粒度 | 独立功能 |
| 原因 | 更换邮箱有独立入口、独立安全校验、独立数据更新结果和独立异常处理，不应混入注册、登录或密码重置 PRD。Security 作为认证公共能力被引用，不在本 PRD 重复定义认证失败次数、锁定规则、验证码有效期等公共规则。 |

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

## 4. Atome 调研结论

| 对象 | 公开说明 | 对 AIX 的启发 |
|---|---|---|
| Atome SG - 更换邮箱 | 用户可在 Atome App 内从 `Me` 进入右上角箭头，点击邮箱地址编辑并保存；变更会立即反映在 App 内。公开文档未提到旧邮箱 OTP 或新邮箱 OTP。 | 入口形态可以参考：个人中心 / Me 页已有邮箱展示位置进入编辑。AIX 不能直接照搬“无验证即保存”，因为 AIX 邮箱同时涉及登录、找回密码和 Email OTP 接收。 |
| Atome MY - 更换邮箱 | 用户从 `Me` tab 进入右上角箭头，点击邮箱编辑图标，保存后更新邮箱；更新后的邮箱会立即在 App 内反映。公开文档未提到 OTP 校验。 | 支持“邮箱展示行 / 编辑图标”作为入口参考。 |
| Atome SG - 更换手机号 | 如果用户仍可访问已注册手机号，可在 `Me` → `Account & Security` → `Update Mobile Number` 发起，并验证是否仍可访问旧手机号；如果已登出或不能访问旧手机号，走 `No longer using this number?` 旁的 `Update now`，验证当前号码后选择 recovery option。 | 对敏感联系方式变更，Atome 手机号流程区分“仍可访问旧联系方式”和“不可访问旧联系方式”。AIX 更换邮箱 V1 可沿用更安全思路：旧邮箱可访问则验证旧邮箱；旧邮箱不可访问则不自助绕过，转客服 / 人工处理。 |
| Atome PH - 账户资料更新 | Atome PH 对部分申请资料出于安全原因不允许直接修改；手机号更新可在 App 修改，或联系客户支持并提供手机号所有权证明等材料。 | 旧邮箱不可用时，客服 / 人工处理路径是合理兜底，不建议 V1 做无验证自助绕过。 |

## 5. 安全参考结论

1. OWASP 将邮箱视为身份标识和账号恢复链路的一部分，提示邮箱变更流程可能被攻击者用于账号接管。
2. OWASP API Security 建议对敏感操作进行重新认证，其中示例包括更换账户 owner email / 2FA phone number。
3. OWASP 注册邮箱变更建议中，若没有更强 MFA，推荐同时确认当前邮箱与新邮箱；若当前注册邮箱不可访问，建议走系统管理员 / Help Desk 等站外人工路径。
4. 因 AIX 目前 Email OTP 已是账号注册、忘记密码等链路的重要能力，AIX 不建议采用 Atome 公开邮箱流程中“编辑后保存、立即生效、无公开验证”的轻量方案。

## 6. 用户补充确认与产品建议

| 编号 | 事项 | 结论 / 建议 | 状态 |
|---|---|---|---|
| CE-DECISION-001 | 更换邮箱入口 | 推荐放在个人中心已有邮箱地址展示位置。当前邮箱展示行增加可点击区域、右箭头或 Change 入口；点击后进入 Change Email 流程。 | 用户认可方向 + Atome 参考 |
| CE-DECISION-002 | 是否验证旧邮箱 | 需要验证旧邮箱。 | 用户确认 |
| CE-DECISION-003 | 旧邮箱验证方式 | 建议在当前账户身份验证通过后，向旧邮箱发送 Email OTP；用户输入旧邮箱 OTP 通过后，才允许进入新邮箱验证。若旧邮箱不可用，V1 不提供“跳过旧邮箱验证”的自助入口，页面提示用户联系客服 / 人工处理。 | 产品建议 |
| CE-DECISION-004 | 当前账户身份验证 | 建议新增 Security 业务场景 `Change Email`。更换邮箱属于敏感操作，需先完成当前账户身份验证，再进行旧邮箱 / 新邮箱 OTP。认证方式建议复用 AIX 自有认证能力；Email OTP 不应作为唯一当前账户身份验证，因为旧邮箱已作为单独控制权验证。 | 产品建议 |
| CE-DECISION-005 | 新邮箱验证 | 需要向新邮箱发送 Email OTP，确认用户可接收新邮箱邮件；只有新邮箱 OTP 验证成功后才更新账户邮箱。 | 产品建议 |
| CE-DECISION-006 | 成功后是否强制登出 | 建议不强制登出当前设备；成功后刷新当前登录态中的 email 信息。因 AIX 已有单账户单设备在线规则，V1 可不单独处理“踢出其他设备”。 | 产品建议 |
| CE-DECISION-007 | 成功后是否清除 BIO | 建议不清除 BIO。邮箱更换不等同于密码重置，不改变本地生物识别凭证；只需确保后续 Email OTP 接收邮箱切换为新邮箱。 | 产品建议 |
| CE-DECISION-008 | 验证码失效规则 | 不新增“更换邮箱 challenge 失效”规则；正式 PRD 直接引用现有 Email OTP 规则：验证码 5 分钟有效、重新发送后旧验证码立即失效、仅最新一次验证码有效、验证码仅限发起请求设备使用。 | 已检查知识库 |
| CE-DECISION-009 | 成功通知 | 建议向旧邮箱发送安全通知，告知账户邮箱已被更换；向新邮箱发送确认通知，告知该邮箱已绑定为账户邮箱。如 Notification 支持站内信 / Push 安全事件，可同步发送站内信或 Push；若模板未就绪，不阻塞 V1。 | 产品建议 |
| CE-DECISION-010 | 外部账户上下文 | 不影响 DTC / AAI / KUN 等外部账户上下文。 | 用户确认 |

## 7. 本期范围

| 功能点 | 是否纳入 | 说明 | 当前状态 |
|---|---:|---|---|
| 更换邮箱入口 | 是 | 放在个人中心已有邮箱地址展示位置，邮箱展示行可点击进入更换邮箱流程。 | 用户认可方向 |
| 当前邮箱展示 | 是 | 个人中心按当前展示策略展示；更换邮箱流程内建议展示当前邮箱掩码。 | 待正式 PRD 固化 |
| 当前账户身份验证 | 是 | 更换邮箱前先完成当前账户身份验证；建议新增 Security `Change Email` 场景。 | 产品建议 |
| 旧邮箱 Email OTP 验证 | 是 | 当前账户身份验证后，向旧邮箱发送 Email OTP，验证旧邮箱控制权。 | 用户确认 + 产品建议 |
| 旧邮箱不可用处理 | 是 | 不提供自助跳过旧邮箱验证；提示用户联系客服 / 人工处理。 | 产品建议 |
| 新邮箱输入 | 是 | 用户输入新邮箱地址；校验格式、不可与当前邮箱相同、不可与已存在邮箱冲突。 | 产品建议 |
| 邮箱唯一性校验 | 是 | 邮箱全局唯一为已确认事实；建议在发送新邮箱 OTP 前完成唯一性校验，避免向不可用邮箱发送验证码。 | 产品建议 |
| 新邮箱 Email OTP 验证 | 是 | 向新邮箱发送 Email OTP，验证新邮箱可接收邮件。 | 产品建议 |
| 更新账户邮箱 | 是 | 旧邮箱 OTP 与新邮箱 OTP 均通过后，更新账户邮箱。 | 产品建议 |
| 成功结果页 / 成功提示 | 是 | 更换成功后展示成功提示，并返回个人中心或账户安全设置页。 | 产品建议 |
| 成功后安全处理 | 是 | 不强制登出、不清除 BIO；刷新当前登录态 email。 | 产品建议 |
| 验证码失效 | 是 | 直接引用 Email OTP 既有失效规则，不在 Change Email PRD 中重复定义。 | 已检查知识库 |
| 通知 | 是 | 旧邮箱和新邮箱发送安全通知；站内信 / Push 视 Notification 模板支持情况纳入。 | 产品建议 |
| 外部系统同步 | 否 | 用户确认不影响 DTC / AAI / KUN 等外部账户上下文。 | 用户确认 |

## 8. 建议主流程

```text
用户进入个人中心邮箱展示行
→ 用户点击邮箱行 / Change 入口
→ AIX 展示当前邮箱与更换说明
→ 用户发起更换邮箱
→ AIX 调用 Security 完成当前账户身份验证
→ AIX 向旧邮箱发送 Email OTP
→ 用户输入旧邮箱 4 位 Email OTP
→ Security 校验旧邮箱 Email OTP
→ 用户输入新邮箱
→ AIX 校验新邮箱格式、非当前邮箱、全局唯一性
→ AIX 向新邮箱发送 Email OTP
→ 用户输入新邮箱 4 位 Email OTP
→ Security 校验新邮箱 Email OTP
→ 校验成功后 AIX 更新账户邮箱
→ AIX 刷新当前登录态 email
→ AIX 向旧邮箱和新邮箱发送安全通知
→ AIX 展示更换成功结果
```

验证码相关规则：本流程不新增独立验证码失效规则，直接引用 `knowledge-base/security/email-otp-verification.md` 中的 Email OTP 规则。

## 9. 建议页面 / 节点

| 页面 / 节点 | 目的 | 关键规则 |
|---|---|---|
| Personal Center Email Row | 承载入口和当前邮箱信息 | 复用当前个人中心邮箱展示位置；增加可点击区域、右箭头或 Change 入口 |
| Change Email Intro | 告知用户将进行邮箱更换 | 展示当前邮箱，建议掩码；说明需完成当前身份验证、旧邮箱验证和新邮箱验证 |
| Current Account Verification | 验证当前账户操作者身份 | 引用 Security；建议新增 `Change Email` 场景，不重复定义认证公共规则 |
| Old Email OTP Verify Page | 验证旧邮箱控制权 | 复用 Email OTP 4 位验证码、5 分钟有效、自动提交、重发与锁定规则；接收邮箱为当前账户旧邮箱 |
| New Email Input | 输入新邮箱地址 | 校验邮箱格式、不可与当前邮箱相同、不可与已存在邮箱冲突；建议发送 OTP 前完成唯一性校验 |
| New Email OTP Verify Page | 验证新邮箱可接收邮件 | 复用 Email OTP 规则；接收邮箱为用户输入的新邮箱 |
| Change Email Success | 告知用户邮箱已更换 | 成功后返回个人中心或账户安全设置页；不强制登出当前设备；不清除 BIO |
| Security Notification | 告知邮箱已变更 | 旧邮箱和新邮箱发送安全通知；站内信 / Push 视模板支持情况纳入 |
| Failure / Locked / Expired | 处理失败、锁定、过期 | 复用 Security 对应失败、锁定、过期规则；业务失败文案在正式 PRD 中补充 |

## 10. 初版验收标准建议

1. 用户可以从个人中心已有邮箱地址展示位置发起更换邮箱流程。
2. 用户在完成当前账户身份验证前，不能进入旧邮箱 OTP 或最终邮箱更新动作。
3. 系统向旧邮箱发送 Email OTP，并按 Email OTP 规则完成验证。
4. 旧邮箱 OTP 未验证通过时，用户不能继续更新新邮箱。
5. 用户无法接收旧邮箱验证码时，V1 不提供自助跳过旧邮箱验证入口，页面提示联系客服 / 人工处理。
6. 新邮箱必须满足邮箱格式要求。
7. 新邮箱不能与当前账户邮箱相同。
8. 新邮箱不能与其他账户已注册 / 已绑定邮箱冲突。
9. 系统在发送新邮箱 OTP 前完成新邮箱可用性校验。
10. 系统向新邮箱发送 Email OTP，并按 Email OTP 规则完成验证。
11. 旧邮箱 OTP 与新邮箱 OTP 均验证成功后，账户邮箱更新为新邮箱。
12. 更换成功后，当前会话中的 email 信息刷新为新邮箱。
13. 更换成功后，不强制登出当前设备，不清除 BIO。
14. 更换成功后，后续登录账号、找回密码邮箱、Email OTP 接收邮箱使用新邮箱。
15. 更换成功后，系统向旧邮箱和新邮箱发送安全通知；站内信 / Push 视 Notification 模板支持情况执行。
16. 更换失败、取消、OTP 失败、锁定、过期、重发超限时，不得更新账户邮箱。
17. Email OTP 失效规则直接引用现有 Email OTP 规则：5 分钟有效、重新发送后旧验证码立即失效、仅最新一次验证码有效、验证码仅限发起请求设备使用。
18. 更换邮箱不影响 DTC / AAI / KUN 等外部账户上下文。

## 11. 仍待正式 PRD 固化的问题

| 编号 | 问题 | 建议确认对象 | 影响 | 当前建议 |
|---|---|---|---|---|
| CE-GAP-001 | 个人中心邮箱展示行具体交互形态：整行可点、右箭头、Change 文案按钮，还是进入二级安全设置页？ | 产品 / UX | 页面结构与导航路径 | 推荐整行可点 + 右箭头；如页面已有编辑样式，则跟随当前个人中心规范 |
| CE-GAP-002 | Security 场景矩阵如何正式新增 `Change Email`？认证方式具体枚举如何写入 Security？ | 产品 / Security / 后端 | 当前身份验证规则 | 推荐新增敏感操作场景，先完成当前账户身份验证，再进行旧邮箱 / 新邮箱 OTP |
| CE-GAP-003 | 旧邮箱不可用时客服 / 人工处理入口如何展示？ | 产品 / Security / 客服 | 用户无法接收旧邮箱时的闭环 | 推荐 V1 不开放自助绕过，只提示联系客服 |
| CE-GAP-004 | 新邮箱已被使用时，是否复用注册文案 `This email has been used`？ | 产品 / UX / Security | 文案一致性与防枚举 | 推荐在已完成当前账户身份验证后可复用；若风控要求更强防枚举，可改为 `This email is unavailable` |
| CE-GAP-005 | 站内信 / Push 安全通知模板是否已存在？ | 产品 / Notification | 通知渠道完整性 | 推荐 Email 通知必做；站内信 / Push 有模板则纳入，无模板不阻塞 V1 |
| CE-GAP-006 | 操作日志 / 审计日志字段是否需要在正式 PRD 中要求？ | 后端 / Security / 风控 | 排障与风险追踪 | 推荐记录 UID、旧邮箱、新邮箱、设备、IP、时间、结果、失败原因 |

> 以上待确认项暂写入本 brief，不写入知识库 `knowledge-base/changelog/knowledge-gaps.md`。如正式 PRD 需要长期保留缺口，再按知识库规则统一登记到 ALL-GAP。

## 12. 正式 PRD 写作建议

确认 brief 后，正式 PRD 建议按以下结构展开：

1. 文档信息
2. 背景、目标与范围
3. 竞品参考与安全参考
4. 业务流程与规则
5. 页面与交互规则
6. 字段、接口与数据需求
7. 通知与安全边界
8. 异常与失败处理
9. 权限、合规与风控边界
10. 待确认项
11. 验收标准与测试要点
12. 来源引用

## 13. 来源引用

- (Ref: 用户需求 / 2026-05-05 / “我希望增加一个更换邮箱的功能”)
- (Ref: 用户补充确认 / 2026-05-05 / 入口放在个人中心邮箱展示位置；需要验证旧邮箱；外部账户上下文不影响)
- (Ref: Atome SG Help / How do I change the email address for my account)
- (Ref: Atome MY Help / How do I change the email address for my account)
- (Ref: Atome SG Help / How do I change the mobile number for my account)
- (Ref: Atome PH Help / How do I update my account details)
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
- (Ref: OWASP Email Validation and Verification Cheat Sheet / Email Change Workflows)
- (Ref: OWASP Changing A User's Registered Email Address)
- (Ref: OWASP API Security API2:2023 Broken Authentication)
- (Ref: OWASP Multifactor Authentication Cheat Sheet / Changing MFA Factors)
