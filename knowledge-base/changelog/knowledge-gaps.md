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

## 3. Account / Registration

| 编号 | 问题 | 影响范围 | 来源 | 当前处理 | 状态 |
|---|---|---|---|---|---|
| KG-REG-001 | Registration Email 最长 103 字符，但 Login Email 最长 254 字符，二者口径不一致 | Registration / Login / Email 字段 | AIX Card 注册登录需求V1.0 / 7.1.4；7.2.4 | 正文分别保留原文，不统一改写 | open |
| KG-REG-002 | 协议默认勾选状态存在“待合规确定”口径，需确认最终是否默认勾选 | Registration / 协议同意 / 合规 | AIX Card 注册登录需求V1.0 / 7.1.4 | 正文按最新结构写必选协议，默认状态不扩展解释 | open |
| KG-REG-003 | `Privacy Policy test` 疑似原文笔误，需确认最终页面文案是否为 `Privacy Policy` | Registration / 协议链接 | AIX Card 注册登录需求V1.0 / 7.1.4 | 正文保留原文字段并标注来源 | open |
| KG-REG-004 | Set Password / Re-enter Password 的中文标题是否需要最终英文文案，原文存在中文“设置密码” | Registration / 密码设置页 | AIX Card 注册登录需求V1.0 / 7.1.6 / 7.1.7 | 正文保留原文，不自行翻译 | open |

## 4. Account / Password Reset

| 编号 | 问题 | 影响范围 | 来源 | 当前处理 | 状态 |
|---|---|---|---|---|---|
| KG-PWD-001 | Reset Password Page 的输入字段类型、字段名和格式规则原文未明确 | Password Reset / Reset Password Page | AIX Card 注册登录需求V1.0 / 7.3.3 | 正文使用 `resetInput` 作为占位能力名，并明确原文未定义字段类型 | open |
| KG-PWD-002 | Reset Password Page 输入不合法或为空时的具体错误文案原文未明确 | Password Reset / 异常文案 | AIX Card 注册登录需求V1.0 / 7.3.3 | 正文仅写 Next 不可点击或阻止继续，不补具体文案 | open |
| KG-PWD-003 | 身份验证流程在 Password Reset 中具体采用 OTP、Email OTP 或其他方式，原文仅指向 Security 文档 | Password Reset / Identity Verification | AIX Card 注册登录需求V1.0 / 7.3.4；AIX Security 身份认证需求V1.0 | 正文引用 Security，不在 Account 中重复定义 | open |
| KG-PWD-004 | 密码重置成功后的成功提示、跳转页或登录页落点原文未明确，只明确强制登出并需新密码重新登录 | Password Reset / 成功结果 | AIX Card 注册登录需求V1.0 / 7.3.5 | 正文只写强制登出和新密码重新登录 | open |

## 5. Security / API Reference

| 编号 | 问题 | 影响范围 | 来源 | 当前处理 | 状态 |
|---|---|---|---|---|---|
| KG-SEC-API-001 | `tokenAuthType` 为必填字段，但原文未说明枚举值、含义和与业务场景的映射关系 | Security API / Generate Verification URL | AIX Security 身份认证需求V1.0 / 9.1.1 | 正文保留字段，并标注“原文未给出说明” | open |
| KG-SEC-API-002 | Generate Verification URL 接口未列出失败响应、错误码、重试规则和幂等要求 | Security API / Generate Verification URL | AIX Security 身份认证需求V1.0 / 9.1.1 | 正文不补失败处理，仅记录缺口 | open |
| KG-SEC-API-003 | Query Auth Result 接口未列出 HTTP 失败、系统异常、网络异常、超时等响应字段 | Security API / Query Auth Result | AIX Security 身份认证需求V1.0 / 9.1.2 | 正文仅保留 status = INCOMPLETE / PASS / FAIL | open |
| KG-SEC-API-004 | `INCOMPLETE` 同时包含未验证和验证中，原文未拆分具体状态 | Security API / Query Auth Result / 状态映射 | AIX Security 身份认证需求V1.0 / 9.1.2 | 正文按原文保留，不拆分新状态 | open |
| KG-SEC-API-005 | 原文 `10.1 passport error code` 标题与错误码内容存在口径疑问，错误码多为活体 / 人脸相关错误 | Security API / Error Code Mapping | AIX Security 身份认证需求V1.0 / 10.1 | 正文说明原文标题与内容，不自行重命名事实来源 | open |
| KG-SEC-API-006 | 原文 `9.2 外部接口地址` 仅写“Master sub account 设计方案”，没有可结构化接口地址或字段 | Security API / External API Address | AIX Security 身份认证需求V1.0 / 9.2 | 正文保留缺口，不补接口地址 | open |
| KG-SEC-API-007 | 旧版 api-reference 中“验证处理规则需要列出10次，以及验证错误4、5次提示语优化”属于待定事项，需确认是否仍有效 | Security API / 错误提示规则 | 旧版 knowledge-base/security/api-reference.md / 11 待定事项 | 迁移至 gaps，不放入功能正文 | open |

## 6. Card / Application

| 编号 | 问题 | 影响范围 | 来源 | 当前处理 | 状态 |
|---|---|---|---|---|---|
| KG-CARD-APP-001 | 申卡数量限制写“可配置”，但未给出配置来源、配置项名称或后台位置 | Card Application / 申卡入口 | AIX Card V1.0【Application】 / 5.1.4 | 正文按 5 张规则保留，并标注来源 | open |
| KG-CARD-APP-002 | “仅可一张在途”注明 DTC 可配置是否限制，但未给出最终配置口径 | Card Application / 在途卡限制 | AIX Card V1.0【Application】 / 2.1 | 正文保留单在途规则，不扩展配置实现 | open |
| KG-CARD-APP-003 | Card Application 接口请求 / 响应表在 PDF 抽取中不可读，字段级定义需后续从接口原文或截图补齐 | Card Application / DTC 接口字段 | AIX Card V1.0【Application】 / 6.1.4 / 6.1.5 | 接口路径已统一为 `/openapi/v1/card/request-card`；字段级定义仍保留缺口 | open |
| KG-CARD-APP-004 | DTC 错误码表在 PDF 抽取中不可读，无法结构化列出错误码 | Card Application / 错误码 | AIX Card V1.0【Application】 / 6.1.6 | 正文只写未知错误码报警，不补错误码表 | open |
| KG-CARD-APP-005 | Add to Google Wallet 绑卡方案待定，原文不确定是仅唤起 App 还是 API 一键绑卡 | Card Application Result / Google Wallet | AIX Card V1.0【Application】 / 5.1.4 | 正文保留待定口径，不作为已确认方案 | open |
| KG-CARD-APP-006 | 高风险及制裁地区过滤规则只在修订记录中出现，未给出具体国家/地区名单与过滤责任方 | Card Application / 地区选择 / 合规 | AIX Card V1.0【Application】 / 1.2 | 正文只写边界，不补国家名单 | open |
| KG-CARD-APP-007 | FAQ 配置来源、OBoss 可视化 Dashboard 未完成，当前为数据库预设口径 | Card Application / FAQ | AIX Card V1.0【Application】 / 5.1.4 | 正文保留预设数据库口径，不补 OBoss 配置能力 | open |
| KG-CARD-APP-008 | 减免费来源写 MGM 提供减免传参，但未给出具体字段名、接口或回调机制 | Card Application / Discount / MGM | AIX Card V1.0【Application】 / 5.1.4 | 正文只写业务动作，不补接口字段 | open |
| KG-CARD-APP-009 | 申卡支付链路缺少可追溯字段闭环，未明确 Apply Order、referenceNo、钱包扣减流水、DTC 扣费流水、退款流水、MGM discount id 之间的关联 | Card Application / 支付 / 退款 / 对账 | AIX Card V1.0【Application】 / 5.1.4 / 6.1 / 6.3 | 不补字段；后续应在 `card-status-and-fields.md` 或接口事实源中统一收口 | open |
| KG-CARD-APP-010 | Application Result 使用 Processing / Pending / Active / Pending activation / Terminated / Cancelled 等状态，但 Card 统一状态字典尚未建立 | Card Application / Card Status | AIX Card V1.0【Application】 / 5.1.4；AIX Card manage模块需求V1.0 / 6.4 | 已在 `card-status-and-fields.md` 建立已知状态分组；状态映射表仍需确认 | open |
| KG-CARD-APP-011 | Card Application 原文接口清单早期摘要处出现 `/requestcard`，6.1 正式接口处出现 `/request-card`；当前按 6.1 正式接口路径统一为 `/request-card` | Card Application / API Path | AIX Card V1.0【Application】 / 2.2 / 6.1 | `_index.md` 已统一；如 DTC 最终接口与 6.1 不一致，需重新确认 | open |

## 7. Card / Status & Fields

| 编号 | 问题 | 影响范围 | 来源 | 当前处理 | 状态 |
|---|---|---|---|---|---|
| KG-CARD-STATUS-001 | Application 3.1 卡状态映射、3.2 虚拟卡状态机、3.3 实体卡状态机均为外链，PDF 正文未给出结构化状态表 | Card Status / 状态映射 | AIX Card V1.0【Application】 / 3.1-3.3 | `card-status-and-fields.md` 仅保留正文中出现的状态 | open |
| KG-CARD-STATUS-002 | Application 4.3 cardStatus 卡状态在 PDF 中无可读表格内容 | Card Status / 数据字典 | AIX Card V1.0【Application】 / 4.3 | 不补 cardStatus 枚举 ID | open |
| KG-CARD-STATUS-003 | Manage 6.1-6.4 状态映射、虚拟卡状态机、实体卡状态机、操作限制表在 DOCX 中为图片/同步块，无法结构化读取 | Card Status / 操作限制 | AIX Card manage模块需求V1.0 / 6.1-6.4 | 不补完整操作限制矩阵 | open |
| KG-CARD-STATUS-004 | Home 3.5 卡状态映射为外链，无法结构化读取 | Card Home / 状态映射 | AIX APP V1.0【Home】 / 3.5 | 使用 Home 6.1 正文出现状态做展示分组 | open |
| KG-CARD-STATUS-005 | `Pending` 与 `Processing` 是否为同一审核中状态未明确 | Card Status / Application Result / Home | Application / 6.10；Home / 6.1 | 当前归入“审核中”展示组，但不强行统一为一个系统状态 | open |
| KG-CARD-STATUS-006 | `Pending activation` 与 `Inactive` 是否为同一待激活状态未明确 | Card Status / Application Result / Home | Application / 6.10；Home / 6.1 | 当前归入“待激活”展示组，但不强行统一为一个系统状态 | open |
| KG-CARD-STATUS-007 | Manage Unlock 成功后写“状态更新为 Activate”，与其他文档 `Active` 口径不一致 | Card Management / Unlock | AIX Card manage模块需求V1.0 / 7.5 | 正文标记为疑似 `Active`，不直接替换 | open |
| KG-CARD-STATUS-008 | Get Card Basic Info 接口在 Application 与 Manage 中路径不一致 | Card API / Basic Info | Application / 2.2；Manage / 8.1 | `card-status-and-fields.md` 并列保留，待接口最终确认 | open |
| KG-CARD-STATUS-009 | Get Card Sensitive Info 接口在 Application 与 Manage 中路径不一致 | Card API / Sensitive Info | Application / 2.2；Manage / 8.1 | `card-status-and-fields.md` 并列保留，待接口最终确认 | open |

## 8. Card / Activation

| 编号 | 问题 | 影响范围 | 来源 | 当前处理 | 状态 |
|---|---|---|---|---|---|
| KG-CARD-ACT-001 | 卡号后四位不匹配时的最终英文提示文案未明确 | Card Activation / Last 4 Digits | AIX Card manage模块需求V1.0 / 7.2 | 正文只写阻止继续，不补具体文案 | open |
| KG-CARD-ACT-002 | Card Activation 接口失败错误码、失败响应字段和失败页文案未明确 | Card Activation / API Error | AIX Card manage模块需求V1.0 / 7.2 / 8.1 | 正文只写失败承接，不补错误码 | open |
| KG-CARD-ACT-003 | 激活成功后卡状态如何从待激活更新为 Active，依赖接口响应还是状态通知，原文未明确 | Card Activation / Status Update | AIX Card manage模块需求V1.0 / 7.2；Card Status & Fields | 正文写归入已激活展示组，状态回写机制待确认 | open |
| KG-CARD-ACT-004 | 激活成功页是否必须强制进入 Set PIN，还是只提供入口，原文未明确 | Card Activation / Set PIN Entry | AIX Card manage模块需求V1.0 / 7.2 / 7.3 | 正文按“提供 Set PIN 入口”处理，不写强制 | open |

## 9. Card / PIN

| 编号 | 问题 | 影响范围 | 来源 | 当前处理 | 状态 |
|---|---|---|---|---|---|
| KG-CARD-PIN-001 | Set PIN / Change PIN / Reset PIN 的页面文案、成功页和失败页文案未明确 | Card PIN / Page Copy | AIX Card manage模块需求V1.0 / 7.3 | 正文只写流程和接口，不补文案 | open |
| KG-CARD-PIN-002 | PIN 可尝试次数、错误锁定规则、冷却时间未明确 | Card PIN / Risk Control | AIX Card manage模块需求V1.0 / 7.3 | 正文不补失败次数，只记录缺口 | open |
| KG-CARD-PIN-003 | Change PIN 与 Reset PIN 的产品关系未明确：页面入口写 Change PIN，接口清单写 Reset Card PIN | Card PIN / Change vs Reset | AIX Card V1.0【Application】 / 5.2；AIX Card manage模块需求V1.0 / 8.1 | 正文合并为 Change / Reset PIN，并标注待确认 | open |
| KG-CARD-PIN-004 | `pinSetStatus` 字段名为产品占位，原文未给出判断是否已设置 PIN 的真实字段 | Card PIN / Field | AIX Card V1.0【Application】 / 5.2 | 正文标注为占位字段，不作为接口字段 | open |
| KG-CARD-PIN-005 | PIN 公钥加密算法、请求字段、响应字段未明确 | Card PIN / Encryption | AIX Card manage模块需求V1.0 / 8.1 | 正文只写需调用 Public Pin Key，不补加密细节 | open |
| KG-CARD-PIN-006 | Set Card PIN / Reset Card PIN 的请求响应字段与错误码未明确 | Card PIN / API | AIX Card manage模块需求V1.0 / 8.1 | 正文只写接口路径和业务用途，不补字段 | open |

## 10. Card / Sensitive Info

| 编号 | 问题 | 影响范围 | 来源 | 当前处理 | 状态 |
|---|---|---|---|---|---|
| KG-CARD-SENS-001 | Card Sensitive Info 查询接口在 Application 与 Manage 中路径不一致 | Card Sensitive Info / API Path | AIX Card V1.0【Application】 / 2.2；AIX Card manage模块需求V1.0 / 8.1 | 正文引用 `card-status-and-fields.md` 中的并列路径，不强行统一 | open |
| KG-CARD-SENS-002 | 查看敏感信息失败页、失败文案和错误码未明确 | Card Sensitive Info / Error Handling | AIX Card manage模块需求V1.0 / 7.1 / 8.1 | 正文只写失败承接，不补错误码和文案 | open |
| KG-CARD-SENS-003 | 敏感信息页面停留时长、自动隐藏、切后台隐藏、截图限制等安全策略未明确 | Card Sensitive Info / Security UX | AIX Card manage模块需求V1.0 / 7.1 | 正文不补策略，只记录缺口 | open |
| KG-CARD-SENS-004 | 敏感信息是否允许复制、复制哪些字段、复制后是否提示未明确 | Card Sensitive Info / Copy Rule | AIX Card manage模块需求V1.0 / 7.1 | 正文不补复制规则 | open |
| KG-CARD-SENS-005 | Face Authentication 成功后的有效期与 Sensitive Info 是否复用 Security Token 仍需最终确认 | Card Sensitive Info / Authentication Validity | AIX Security 身份认证需求V1.0 / 7.4；AIX Card manage模块需求V1.0 / 7.1 | 正文按 Security 规则引用，不单独定义有效期 | open |
