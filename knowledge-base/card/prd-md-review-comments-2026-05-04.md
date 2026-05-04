# Card PRD MD 文档评审意见（仅评审，不修改源文档）

评审日期：2026-05-04  
评审人：YI助手  
评审范围：`knowledge-base/card/` 下全部 Markdown 文档  
评审性质：只评审、只记录问题与建议；未修改任何被评审 MD 文件。

## 0. 本次评审依据

### 0.1 事实文件

1. `AIX Card 【manage】模块需求V1.0 .docx`
2. `AIX Card V1.0【Application】.docx`
3. `DTC Card Issuing API Document_20260310 (1).pdf`

### 0.2 模板依据

- `prd-template/standard-prd-template.md`

### 0.3 被评审文件

| 文件 | 评审结论 |
|---|---|
| `knowledge-base/card/_index.md` | 结构可作为索引，但与标准 PRD 模板差异较大；部分来源不可用或不可验证。 |
| `knowledge-base/card/application.md` | 问题较多，尤其是 DTC API 字段、autoDebit 枚举、币种口径、页面字段校验与模板缺失。 |
| `knowledge-base/card/card-status-and-fields.md` | 高风险。状态和操作限制表的处理与事实文件不一致，且接口路径和字段口径存在多处冲突。 |
| `knowledge-base/card/card-home.md` | 页面信息较丰富，但依赖未随本次附件提供的 Home / Transaction 文档，部分内容本次无法验证；模板结构仍不达标。 |
| `knowledge-base/card/activation.md` | 高风险。激活流程与 Manage 7.2 的页面逻辑、接口校验、异常规则存在明显缺漏或顺序风险。 |
| `knowledge-base/card/pin.md` | 中高风险。PIN 业务范围正确，但 DTC PIN 接口字段、加密字段、状态限制和验收场景不足。 |
| `knowledge-base/card/sensitive-info.md` | 中高风险。敏感信息查看流程有框架，但缺少 Card detail popup 的关键页面字段、复制规则和失败提示。 |
| `knowledge-base/card/card-management.md` | 中高风险。Lock / Unlock 有主流程，但注销卡被不当处理为纯缺口，且状态限制未按事实表闭环。 |
| `knowledge-base/card/card-transaction-flow.md` | 内容完整度较高，但大量依赖本次未提供的交易、钱包、通知事实源；仅能对 DTC Card API 可核部分做有限评审。 |

---

## 1. 总体结论

当前 `knowledge-base/card` 下的 MD 更像“知识库事实归纳稿”，还不是严格符合 `standard-prd-template.md` 的标准 PRD。整体存在以下共性问题：

1. **模板结构不一致**：多数文件使用“功能定位 / 适用范围 / 前置条件 / 业务流程 / 页面卡片与交互规则”结构，但标准模板要求“文档信息、需求背景目标范围、业务流程与规则、页面与交互、字段接口与数据、通知规则、权限合规风控、待确认事项、验收标准、来源引用”。
2. **事实文件引用边界不清**：不少文件引用 `Home`、`Transaction & History`、`AIX Card交易`、`DTC Wallet OpenAPI`、`Notification`、`用户确认结论` 等来源，但本次附件没有提供这些文件。不能把这些内容作为本次评审可确认事实。
3. **状态与操作限制高风险**：`card-status-and-fields.md` 多次说明操作限制表不可读，但本次 Manage 附件中 6.4 操作限制表是可读取的，且给出了待激活、ACTIVE、SUSPENDED、CANCELLED、BLOCKED、PENDING 各状态下的操作权限。
4. **DTC API 契约缺失或冲突**：多个 MD 对接口路径、枚举值、字段长度、必填性、错误码、请求/响应结构没有按 DTC 官方 API 文档落地。最突出的冲突是 `autoDebitEnabled`：Application 事实文件写 `0/OFF`、`2/ON`，DTC API 写 `0/OFF`、`1/ON`，且默认值为 `0`。
5. **页面交互细节缺失**：Manage 事实文件中有大量明确页面文案、按钮行为、Loading 禁用、Network Error Popup、Server Error Popup、清空输入等规则，多个 MD 只写了抽象流程，没有落到页面交互规则。
6. **验收标准与测试场景普遍缺失**：标准模板要求验收标准/测试场景，当前绝大多数文件没有可以直接给 QA 使用的测试矩阵。

建议先按以下优先级处理：

1. 先修 `card-status-and-fields.md`：补齐状态映射和操作限制矩阵，解决 `autoDebitEnabled`、接口路径、敏感字段、`cardHolderName` 展示规则等基础事实。
2. 再修 `application.md`：对齐 DTC Card Application 请求/响应字段、费用和币种口径、姓名/手机号/地址字段校验。
3. 再修 `activation.md`、`pin.md`、`sensitive-info.md`、`card-management.md`：这些文件都依赖状态和字段事实源。
4. 最后统一改全部文件的模板结构和验收标准。

---

## 2. 全局问题

### GLOBAL-001：所有 MD 未严格使用标准 PRD 模板

严重级别：高  
影响范围：全部文件

标准模板要求至少包含以下结构：

- 文档信息
- 需求背景、目标与范围
- 业务流程与规则
- 页面与交互
- 字段、接口与数据
- 通知规则
- 权限 / 合规 / 风控
- 待确认事项
- 验收标准 / 测试场景
- 来源引用

当前文件普遍缺少：

1. `需求背景、目标与范围` 中的用户问题、业务目标、功能清单。
2. `通知规则` 独立章节。Card 状态通知、物流通知、交易通知均被散落在不同章节或仅作为接口字段出现。
3. `待确认事项` 独立章节。当前有些文件用 “gap” 表述，但没有按标准模板集中管理。
4. `验收标准 / 测试场景`。这会导致研发、测试无法直接按文档验收。
5. 标准化 `文档信息` 表。当前只有 YAML frontmatter，缺少模板内的正文文档信息。

建议：保留 YAML 作为知识库元数据，但正文必须补齐标准 PRD 模板章节。若该目录定位是“知识库事实文件”而非 PRD，也建议在 `_index.md` 明确说明“本目录不使用 PRD 模板”，否则本次用户要求对照标准模板时应视为结构不合格。

### GLOBAL-002：Frontmatter 与标准模板元信息不一致

严重级别：中  
影响范围：全部文件

当前 frontmatter 常见字段为：

- `module`
- `feature`
- `version`
- `status`
- `source_doc`
- `source_section`
- `last_updated`
- `owner`
- `depends_on`

标准模板还要求体现：

- 文档类型
- 文档状态：Draft / Review / Approved
- 目标读者
- 需求来源
- 最后更新时间

问题：

1. 当前 `status: active` 更像知识库状态，不等于 PRD 状态。
2. 未区分 `version` 是需求版本、知识库版本还是文档版本。
3. 未记录目标读者，例如 Product / Design / FE / BE / QA / Risk / Compliance。
4. `source_doc` 中引用了大量本次附件未提供的资料，导致可验证性不一致。

建议：新增正文“1. 文档信息”表，保留 frontmatter 但不要用 frontmatter 替代标准模板。

### GLOBAL-003：业务流程图混入接口实现细节，不符合模板边界

严重级别：中  
影响范围：多数文件

标准模板强调业务流程图应表达业务主体和职责，不应把接口字段、错误码、页面文案全部塞入时序图。

当前多个文件的 mermaid sequence diagram 同时包含：

- 具体接口路径
- 请求字段
- 状态字段
- 错误处理
- 页面展示行为

影响：

1. 图过重，不利于业务评审。
2. 接口变更时需要同时改图和字段表，维护成本高。
3. 研发可能误以为图中的接口顺序就是最终技术方案。

建议：

- `业务流程与系统交互时序图` 只保留业务节点。
- 接口路径、字段、错误码统一放入“字段、接口与数据”。
- 页面文案、按钮、弹窗统一放入“页面与交互”。

### GLOBAL-004：来源引用中存在本次附件无法验证的内容

严重级别：高  
影响范围：`_index.md`、`card-home.md`、`card-transaction-flow.md` 等

本次附件只有 Manage、Application、DTC Card Issuing API 三份事实文件。当前多个 MD 引用了：

- `AIX APP V1.0【Home】.pdf`
- `AIX APP V1.0【Transaction & History】.pdf`
- `AIX Card交易【transaction】.pdf`
- `DTC Wallet OpenAPI Documentation`
- `AIX+Notification`
- 用户确认结论
- 其他内部 knowledge-base 文件

这些来源在本次附件中没有提供，不能在本次评审中判断其真实性。若这些内容来自历史知识库，应在文档里明确“非本次附件可验证来源”。

建议：增加来源可信度分层：

| 来源类型 | 建议标记 |
|---|---|
| 本次附件事实 | `verified_by_current_review` |
| 仓库内其他知识库文件 | `internal_reference` |
| 历史 PRD 但本次未附 | `unverified_in_current_review` |
| 用户确认结论 | 需记录确认人、确认时间、上下文链接 |

### GLOBAL-005：全局异常组件没有被系统性复用

严重级别：高  
影响范围：`activation.md`、`pin.md`、`sensitive-info.md`、`card-management.md`、`application.md`

Manage 6.5 明确抽象了：

- Network Error Page
- Network Error Popup
- Server Error Page
- Server Error Popup

并给出了触发条件、按钮行为、返回规则、文案。当前文件里大多只写“网络异常 / 后端错误 / 失败承接”，没有统一映射到这四类组件。

影响：

1. 前端实现无法知道什么时候用 Page，什么时候用 Popup。
2. 文案可能不一致。
3. 用户关闭弹窗后的页面状态不明确。

建议：每个业务文件在异常章节增加统一表：

| 业务场景 | 异常类型 | 使用组件 | 用户关闭后的页面状态 | 是否清空输入 | 是否可重试 |
|---|---|---|---|---|---|

---

## 3. `card-status-and-fields.md` 评审意见

### STATUS-001：将 Manage 6.4 操作限制表标记为不可读，与附件事实不符

严重级别：阻塞  
影响范围：状态、激活、PIN、锁卡、解锁、注销卡、交易功能

当前文档多处写到：

- 操作限制表不可读
- 不补操作限制矩阵
- 状态允许范围待表补齐

但 Manage 附件中的 6.4 “卡片状态与操作限制对照表”是可读取的，且明确列出了：

| 状态 | 查看卡信息 | 查看敏感信息 | 卡激活 | Set PIN | Change PIN | Lock Card | Unlock Card | 注销卡 | 交易功能 |
|---|---|---|---|---|---|---|---|---|---|
| 待激活 | 否 | 否 | 是 | 否 | 否 | 否 | 否 | 否 | 否 |
| ACTIVE | 是 | 是 | 否 | 是，仅限首次 | 是 | 是 | 否 | 是 | 是 |
| SUSPENDED | 否 | 否 | 否 | 否 | 否 | 否 | 是 | 是 | 否 |
| CANCELLED | 否 | 否 | 否 | 否 | 否 | 否 | 否 | 否 | 否 |
| BLOCKED | 是 | 否 | 否 | 否 | 否 | 否 | 否 | 否 | 否 |
| PENDING | 否 | 否 | 否 | 否 | 否 | 否 | 否 | 否 | 否 |

建议：把该表作为 `card-status-and-fields.md` 的核心事实，并让 Activation / PIN / Sensitive Info / Card Management 统一引用。

### STATUS-002：状态集合与事实文件不完全一致

严重级别：高

当前状态列表包括：

- `Pending`
- `Processing`
- `Pending activation`
- `Inactive`
- `Active`
- `Suspended`
- `Terminated`
- `Cancelled`
- `Activate`

Manage 6.4 操作表则使用：

- 待激活
- ACTIVE
- SUSPENDED
- CANCELLED
- BLOCKED
- PENDING

问题：

1. `BLOCKED` 在当前 MD 中未被充分纳入操作规则，但 Manage 表明确存在。
2. `Terminated` 在 Application 里出现，但 Manage 表没有该状态，需要说明与 `BLOCKED` / `CANCELLED` / DTC status 的映射关系。
3. `Activate` 明显像 `Active` 的拼写或文案问题，不能作为独立状态直接使用。
4. `Pending activation` 与 `Inactive` 当前只标注待确认，但需要明确哪个来自 DTC、哪个来自产品展示。

建议：补一个“三层状态映射表”：

| DTC 原始状态 | AIX 后端归一状态 | 前端展示组 | 允许操作 | 来源 | 待确认项 |
|---|---|---|---|---|---|

### STATUS-003：`cardHolderName` 展示规则与 Manage 7.1 冲突

严重级别：高

当前 `card-status-and-fields.md` 在 Card Basic Info 字段中写：

- `cardHolderName`：Physical Card 展示，Virtual Card 隐藏

但 Manage 7.1 Card detail popup 明确写到：

- `Name on card`：无论物理卡还是虚拟卡，都展示该字段。
- 数据来源：`Get Card Basic Info.cardHolderName`

影响：

- Card Detail 展示会被错误实现。
- Sensitive Info 文档引用该字段集合后也会继承错误。

建议：改为“Physical Card / Virtual Card 均展示 `Name on card`，来源 `Get Card Basic Info.cardHolderName`”。

### STATUS-004：`autoDebitEnabled` 枚举与 DTC API 冲突

严重级别：阻塞

当前文档使用：

- `0 / OFF`
- `2 / ON`

Application 事实文件中确实出现 `0 OFF`、`2 ON`。但 DTC Card Issuing API 的 Card Application 请求字段 `autoDebitEnabled` 写明：

- `0 - OFF`
- `1 - ON`
- default is `0`

同时 Manage 7.2 还提到 Card Activation 接口入参 `autoDebit`，当值为 `ON` 时，激活同时开启自动扣款。

问题：

1. 产品字典值与 DTC API 值不一致。
2. Application 说申卡时上送 / 展示，Manage 说激活时入参 `autoDebit`。
3. DTC API 默认 OFF，而 Application 文档存在默认开启口径。

建议：必须新增待确认事项：

- AIX 内部 `autoDebitEnabled=2` 是否需要映射为 DTC `autoDebitEnabled=1`？
- 自动扣款到底在申卡时开启，还是实体卡激活时开启，还是两处都可能设置？
- 前端 Auto Debit Tag 的显示依据是 Application 入参、Activation 入参，还是 DTC 查询字段？

### STATUS-005：Basic Info / Sensitive Info 接口路径不应长期并列保留

严重级别：高

当前文件并列保留多套路径：

- Basic Info：`[POST] /openapi/v1/card/inquiry-card-info` / `GET /openapi/v1/card/basic-info`
- Sensitive Info：`[POST] /openapi/v1/card/inquiry-card-sensitive-info` / `GET /openapi/v1/card/sensitive-info`

本次 Application 事实文件和 DTC API 都支持以下路径作为主路径：

- Get Card Basic Info：`[POST] /openapi/v1/card/inquiry-card-info`
- Get Card Sensitive Info：`[POST] /openapi/v1/card/inquiry-card-sensitive-info`

建议：

1. 将 POST 路径标记为当前有效路径。
2. GET 路径若来自旧文档，移到“历史冲突 / 待废弃路径”。
3. 不要在字段依赖表中让研发二选一。

### STATUS-006：未纳入 DTC OpenAPI 通用安全 Header

严重级别：中

DTC API 2.4 要求关键请求包含：

- `Authorization`
- `D-REQUEST-ID`
- `D-TIMESTAMP`
- `D-SIGNATURE`
- `D-SUB-ACCOUNT-ID`
- `Content-Type`
- `DTC-MFA-Data`（可选）

当前状态和接口文档没有统一沉淀这些通用 Header，导致每个业务文件都只写路径，没有说明安全签名依赖。

建议：在 `card-status-and-fields.md` 或 `_index.md` 增加“Card OpenAPI 通用请求要求”，各业务文档引用即可。

---

## 4. `application.md` 评审意见

### APP-001：Card Application 请求字段未按 DTC API 完整落地

严重级别：阻塞

DTC Card Application 接口 `[POST] /openapi/v1/card/request-card` 明确包含以下关键字段：

- `referenceNo`
- `productCode`
- `cardMaterial`
- `currency`
- `firstName`
- `lastName`
- `preferredPrintedName`
- `email`
- `mobile.countryCode`
- `mobile.number`
- `deliveryAddress.country`
- `deliveryAddress.state`
- `deliveryAddress.city`
- `deliveryAddress.district`
- `deliveryAddress.address1`
- `deliveryAddress.address2`
- `deliveryAddress.address3`
- `deliveryAddress.postal`
- `deliveryAddress.fullName`
- `deliveryAddress.phoneNumber`
- `cardFeeDetails.type`
- `cardFeeDetails.amount`
- `cardFeeDetails.currency`
- `autoDebitEnabled`

当前 `application.md` 没有形成完整请求字段表、必填条件、长度限制、字段来源和 AIX 前端字段映射。

建议：补充一张字段映射表：

| AIX 页面字段 | AIX 内部字段 | DTC 字段 | Required | 长度 | 来源页面 | 校验规则 | 备注 |
|---|---|---|---|---|---|---|---|

### APP-002：`currency` 口径混淆，稳定币与 DTC National Currency Code 未拆开

严重级别：阻塞

Application 产品事实中，用户选择的是稳定币：

- USDT
- USDC
- FDUSD
- WUSD

DTC Card Application API 的 `currency` 字段说明为：

- National Currency Code (ISO 4217)
- 示例：SGD

问题：

1. 用户选择的 stablecoin 不应直接等同于 DTC Card Application 的 `currency`。
2. 卡默认消费币种、钱包扣费币种、DTC 卡币种、费用币种需要拆分。
3. 当前文档如果把 USDT/USDC 直接上送到 DTC `currency`，可能导致接口参数错误。

建议：明确以下字段：

| 业务口径 | 示例 | 是否上送 DTC | DTC 字段 |
|---|---|---|---|
| 用户选择稳定币 | USDT / USDC / WUSD / FDUSD | 待确认 | 不应默认等于 `currency` |
| DTC 卡币种 | SGD 等 ISO 4217 | 是 | `currency` |
| 费用扣款币种 | 用户选择稳定币 | 可能通过 AIX 支付链路处理 | 非 DTC Card Application `currency` |
| `cardFeeDetails.currency` | DTC 要求 ISO 4217 | 是 | `cardFeeDetails.currency` |

### APP-003：`autoDebitEnabled` 默认值和枚举未与 DTC API 对齐

严重级别：阻塞

同 STATUS-004。此问题在 `application.md` 中更关键，因为 Application 是申卡接口上送来源。必须明确：

- 前端/产品枚举是否 `0/2`
- DTC API 枚举是否 `0/1`
- 默认是否 ON 或 OFF
- 激活接口的 `autoDebit` 与申卡接口的 `autoDebitEnabled` 是否为同一能力

### APP-004：Billing information 页面标题写错

严重级别：高

Application 事实文件的账单信息页面标题为：

- `Billing information`

当前 `application.md` 中出现将页面命名为 `Mailing information` 或与邮寄信息混淆的风险。

影响：

- 页面标题错误。
- 账单信息与邮寄地址页面边界混乱。

建议：账单页面统一为 `Billing information`，邮寄地址页面统一为 `Mailing address`。

### APP-005：姓名输入校验与事实文件不一致

严重级别：高

Application 事实文件要求：

- First name / Last name 为必填。
- 长度 25 字节。
- 只能输入英文字母及空格。
- 不允许特殊字符。
- 校验不通过提示 `Text format error. `。
- 保存时用 `Last+First` 或 `First+Last` 与 KYC Full name 比对，大小写不敏感。

当前 MD 中如存在允许数字、特殊字符、只比较 `First+Last` 的描述，均应修正。

建议：明确输入规则、错误提示、KYC 比对算法和前端缓存规则。

### APP-006：手机号字段长度与 DTC API、产品事实不一致

严重级别：高

产品事实：

- CountryNo 长度 4 字节，至少填 1 位。
- 手机号长度 12 字节，至少填 4 位。

DTC API：

- `mobile.countryCode` 长度 3。
- `mobile.number` 长度 12。

当前 MD 若使用 20 字节或未区分国家码与手机号，会导致实现错误。

建议：

1. 前端展示字段按产品规则校验。
2. 上送 DTC 字段时转换为 `mobile.countryCode` 和 `mobile.number`。
3. 明确超过 DTC `countryCode=3` 的国家区号如何处理。

### APP-007：Mailing address 字段长度与 DTC API 冲突

严重级别：高

DTC API 对邮寄地址字段限制：

- `deliveryAddress.country`：3
- `state`：20
- `city`：20
- `district`：40
- `address1`：40
- `address2`：40
- `address3`：40
- `postal`：10
- `fullName`：60
- `phoneNumber`：16

当前 MD 如果使用：

- Postcode 40
- Recipient name 10
- Recipient mobile 20

则与 DTC API 不一致。

建议：补充“页面输入限制”和“DTC 上送限制”的差异处理。若前端允许更长，必须写清截断/禁止提交/后端校验策略。

### APP-008：卡面颜色命名需与事实文件统一

严重级别：中

Application 事实文件中卡面颜色为：

- Coral Orange 珊瑚橙
- Obsidian Black 黑曜石
- Clear blue sky 纯白

当前 MD 若使用 `Orange white`、`Orange black`、`Pure white` 等非事实名称，应统一。

建议：保留英文产品展示名和中文解释，不要自行改名。

### APP-009：缺少接口异常和错误码处理

严重级别：高

DTC Card Application 明确列出错误码，例如：

- `00006 Access denied`
- `31002 Card processor error`
- `31006 Parameters is invalid`
- `31007 have a pending card application`
- `31024 Failed to for virtual card`
- `31025 Failed to apply for physical card`
- `31028 have reached limit of application physical card`
- `31047 Virtual card holding limit`
- `31055 Insufficient wallet balance. Card application fee cannot be deducted`

当前 `application.md` 没有把错误码映射到页面提示、订单状态、失败页、是否可重试。

建议：新增错误码处理矩阵。

---

## 5. `activation.md` 评审意见

### ACT-001：卡号后四位校验逻辑与 Manage 7.2 不一致

严重级别：阻塞

Manage 7.2 明确：

- 用户完整输入 4 位卡号后四位后，系统自动调用 `Inquiry Card Basic Info` 接口验证。
- 若接口返回的 `truncatedCardNumber` 与用户输入不一致，显示错误：`The last 4 digits entered are invalid`。
- 若一致，自动进入下一流程 `7.3 Set PIN / Change PIN`。

当前 `activation.md` 更像是“读取本地 `truncatedCardNumber` 后本地比对”，没有明确“输入完成后调用 Inquiry Card Basic Info”。

建议：修正为：输入 4 位 -> 调用 Inquiry Card Basic Info -> 以接口返回 `truncatedCardNumber` 做校验。

### ACT-002：Active Card Page 页面细节缺失

严重级别：高

Manage 7.2 给出了清晰页面规则，当前文档缺少或不完整：

1. 返回按钮弹挽留弹窗：
   - Title：`Confirm Exit?`
   - Content：`Are you sure you want to leave before completing this step?`
   - Button：`Stay And Continue` / `Leave`
2. 主标题：`Enter last 4 digits`
3. 副标题：`Enter the last 4-digit of your physical AIX Card number`
4. 提交中显示 `Loading...`。
5. 提交中禁止重复输入或返回。
6. 网络异常使用 Network Error Popup。
7. 服务器异常使用 Server Error Popup。
8. 用户关闭异常弹窗返回本页面后自动清空输入框。

建议：按模板“页面与交互”章节补一张 Active Card Page 元素表。

### ACT-003：激活流程中 Face Authentication 与 Set PIN 顺序需要确认

严重级别：高

当前 MD 流程为：

`Last 4 matched -> Face Authentication -> Card Activation API -> Activation Success -> Set PIN`

Manage 7.2 页面逻辑片段写到：

- 卡号验证通过后，自动进入下一流程 `7.3 Set PIN / Change PIN`。

同一事实文件又描述激活流程包括身份验证、设置 PIN（可选）及状态确认。

问题：

1. 卡号验证后到底先进入 Set PIN，还是先 Face Authentication + Activation API？
2. PIN 是激活前设置、激活后设置，还是可选后置入口？
3. Card Activation API 与 Set PIN API 的调用顺序是否有强依赖？

建议：该点不能脑补，需要列为待确认；如果已有 UX 最新流程，应把完整步骤和接口顺序写清。

### ACT-004：遗漏激活接口入参 `autoDebit`

严重级别：高

Manage 7.2 知识点写明：

- 调用 Card Activation 接口时，入参：`autoDebit`。
- 当该参数值为 `ON` 时，系统将在卡片激活的同时开启自动扣款功能。
- 开启后用户消费时系统自动从关联钱包账户扣款。

当前 `activation.md` 未充分沉淀这一规则，也未与 Application 的 `autoDebitEnabled` 区分。

建议：在字段与接口章节增加：

| 字段 | 所属接口 | 取值 | 作用 | 与 Application `autoDebitEnabled` 的关系 |
|---|---|---|---|---|

### ACT-005：未评估 DTC `Sent OTP For Card Activation` 是否适用

严重级别：中

DTC API 目录中存在：

- `Sent OTP For Card Activation`
- `Card Activation`

当前产品文档强调 Face Authentication，但 DTC API 仍有激活 OTP 能力。当前 `activation.md` 没有说明 AIX 是否不用 OTP、还是由 Face Authentication 替代。

建议：新增待确认：AIX 实体卡激活是否调用 DTC OTP For Card Activation？若不用，应明确“不使用原因 / 替代认证方式”。

---

## 6. `pin.md` 评审意见

### PIN-001：PIN 状态限制必须引用 Manage 6.4 的真实操作表

严重级别：高

Manage 6.4 明确：

- 待激活：Set PIN 否，Change PIN 否。
- ACTIVE：Set PIN 是，仅限首次；Change PIN 是。
- SUSPENDED：Set PIN 否，Change PIN 否。
- CANCELLED / BLOCKED / PENDING：均不可 Set / Change PIN。

当前 `pin.md` 依赖 `card-status-and-fields.md` 的缺口状态，导致 PIN 可操作状态不闭环。

建议：补充 PIN 操作限制表，不要只写“状态允许范围引用”。

### PIN-002：缺少 DTC PIN 接口请求字段与加密字段

严重级别：高

DTC API 更新历史提到：

- `encryptPin` rename to `encryptedPin`

当前文档只写：

- Generate Public Pin Key
- Set Card PIN
- Reset Card PIN

但没有写清：

1. 获取公钥响应字段。
2. 前端如何加密 PIN。
3. `encryptedPin` 字段名称。
4. Set / Reset 请求字段。
5. 失败码和错误提示。

建议：补 DTC PIN 接口字段表，至少覆盖字段名、必填性、来源、加密方式、错误处理。

### PIN-003：Change PIN 与 Reset PIN 的产品/接口关系仍不清

严重级别：中

产品入口叫 `Change PIN`，DTC API 叫 `Reset Card PIN`，并需要 `OTP For Reset PIN`。当前文档虽然提到 Change / Reset，但仍把关系标为待确认。

建议：明确：

- 前端显示：`Change PIN`
- 后端接口：`OTP For Reset PIN` + `Reset Card PIN`
- 是否需要输入旧 PIN：当前事实未说明，不得补写。
- OTP 校验失败、锁定、重发规则引用 Security OTP 文档。

### PIN-004：缺少页面验收场景

严重级别：中

建议至少补充以下验收：

1. ACTIVE 且未设置 PIN，展示 Set PIN 和小红点。
2. ACTIVE 且已设置 PIN，展示 Change PIN，小红点消失。
3. SUSPENDED 不展示或禁用 Set / Change PIN。
4. 输入非 4 位数字，不能提交。
5. Public Key 获取失败，不能提交 PIN。
6. Set PIN 成功后状态刷新。
7. Reset PIN OTP 失败按安全规则处理。
8. Reset PIN 成功后仍为已设置状态。

---

## 7. `sensitive-info.md` 评审意见

### SENS-001：缺少 Card detail popup 的完整页面字段

严重级别：高

Manage 7.1 明确 Card detail popup 包含：

- 右上角关闭按钮：点击关闭 popup。
- Card type：显示卡类型，数据来源于 AIX 申卡时储存。
- Default currency：读取 `Get Card Basic Info.currency`。
- Name on card：物理卡和虚拟卡都展示，读取 `Get Card Basic Info.cardHolderName`。
- Card number：读取 `Get Card Sensitive Info.cardNumber`。
- EXP：读取 `Get Card Sensitive Info.expiryDate`。
- CVV：读取 `Get Card Sensitive Info.cvc`。

当前 `sensitive-info.md` 把字段集合下沉到 `card-status-and-fields.md`，但没有在页面章节写清 popup 展示规则。

建议：在“页面与交互”中补 Card detail popup 元素表。

### SENS-002：缺少复制规则和 Toast 文案

严重级别：高

Manage 7.1 明确：

- Name on card / Card number / EXP / CVV 点击复制完整信息。
- Toast：`The information has been copied.`

当前文档未完整沉淀这些交互细节。

建议：补充字段级复制规则表：

| 字段 | 是否可复制 | 复制内容 | 成功 Toast | 失败处理 |
|---|---|---|---|---|

### SENS-003：接口失败提示未按事实文件写明

严重级别：高

Manage 7.1 Card home page 写明：

- 点击 Card detail，若 `Get Card Basic Info` / `Get Card Sensitive Info` 返回失败，前端写死 toast：`Failed to get card info. Please try again later`

当前文档只写“展示失败承接或错误提示”，不够精确。

建议：明确该 toast，以及 Basic Info 失败和 Sensitive Info 失败是否都使用同一文案。

### SENS-004：Sensitive Info 接口路径应优先使用 DTC / Application 的 POST 路径

严重级别：中

见 STATUS-005。建议在 Sensitive Info 文件中明确当前有效路径为：

- `[POST] /openapi/v1/card/inquiry-card-sensitive-info`

旧 GET 路径若存在，应移至冲突记录。

---

## 8. `card-management.md` 评审意见

### MGMT-001：注销卡不应只记录为“无接口缺口”

严重级别：高

当前文档把“注销卡”处理为：

- 操作限制表中出现，但无独立流程章节。
- 不补流程、不补接口、不补文案，记录缺口。

但 Manage 6.4 明确：

- ACTIVE：注销卡允许。
- SUSPENDED：注销卡允许。

DTC API 目录也有：

- `Terminate Card`

所以“是否存在能力”并非纯缺口。缺口应该是：

1. AIX 页面入口是否展示。
2. 注销卡确认流程。
3. 是否需要身份验证。
4. 成功/失败文案。
5. 与 DTC `Terminate Card` 的接口字段和错误码。

建议：改为“能力已存在但 AIX 产品流程缺失”，不要写成完全未知能力。

### MGMT-002：Lock / Unlock 状态限制应按 Manage 6.4 明确写出

严重级别：高

Manage 6.4：

- ACTIVE：Lock Card 是，Unlock Card 否。
- SUSPENDED：Lock Card 否，Unlock Card 是。
- 其他状态均不可 Lock / Unlock。

当前文档写“状态允许范围引用”，但由于状态文件本身将操作表标为不可读，会导致实现不闭环。

建议：Card Management 自身也补一张最小状态限制表。

### MGMT-003：Lock / Unlock 是否仅限 Physical Card 需要确认

严重级别：中

当前文档部分成功提示写：

- `Your physical card has been locked.`
- `Your physical card has been unlocked.`

但操作限制表没有区分虚拟卡/实体卡。Card Home 文件里也给虚拟卡列了 Lock / Unlock。

建议：新增待确认：

- Lock / Unlock 是否支持 Virtual Card？
- 若支持，为什么文案写 physical card？
- 是否需要按卡类型分别配置文案？

### MGMT-004：Unlock 成功状态 `Activate` 需要归一

严重级别：中

Manage 7.5 原文写状态更新为 `Activate`，当前文档按缺口处理是合理的，但还需要明确：

- 研发不应将 `Activate` 作为枚举实现。
- 应确认它是否为 `Active` 的文案/拼写问题。

建议：在待确认事项中提高优先级，因为它会影响状态机。

### MGMT-005：Lock / Unlock 错误处理与全局异常组件未完全统一

严重级别：中

Manage 6.5 已抽象 Network Error Popup / Server Error Popup。Card Management 中仍写了单独错误文案，例如：

- `No internet connection, please check the connection or try again later.`
- `Freeze failed`
- `Unfreeze failed`

建议：明确哪些场景使用全局组件，哪些保留业务 Toast。

---

## 9. `card-home.md` 评审意见

### HOME-001：大量来源本次附件无法验证

严重级别：高

`card-home.md` 引用：

- `AIX APP V1.0【Home】.pdf`
- `AIX APP V1.0【Transaction & History】.pdf`

本次附件未提供上述文件。因此对于以下内容，本次只能标记“未验证”，不能判断事实正确：

- Home 6.1 主页面完整展示规则。
- Recent Transactions 详细展示规则。
- FAQ 筛选规则。
- Google Wallet 入口细节。
- 多卡排序、首页卡片滑动等细节。

建议：把本次可由 Application / Manage / DTC API 直接支撑的内容和未随附件提供来源的内容分层标记。

### HOME-002：默认申卡文案疑似拼写错误

严重级别：低

当前写：

- `Apply for a AlX card`

其中 `AlX` 看起来是字母 L，不是 `AIX`。且英文冠词也应考虑为 `an AIX card` 或产品事实文案原样。

建议：回查原始 Home 设计稿 / 文案表，避免误改品牌名。

### HOME-003：操作入口应受 Manage 6.4 操作限制表约束

严重级别：高

Card Home 展示 Card detail、Set PIN、Change PIN、Lock、Unlock、Activate card 等入口。当前文档依赖 `card-status-and-fields.md`，但该文件对操作表处理错误。

建议：在 Home 文件中至少引用经过修正后的操作矩阵，并明确：

- 不允许的操作是隐藏、置灰，还是点击拦截。
- ACTIVE / SUSPENDED / BLOCKED 下 Card detail 展示差异。
- 待激活实体卡是否允许查看基本信息：Manage 6.4 写不允许。

### HOME-004：Recent Transactions 接口需与 DTC API 对齐

严重级别：中

当前写：

- `/openapi/v1/card/inquiry-card-transaction`

DTC API 确实包含 Transaction History Of Card 相关接口，但当前 Home 文档没有写请求字段、分页、错误码和空态边界。

建议：如果 Home 只展示最近 3 条，应写清：

- 是否调用同一交易历史接口。
- page size 是否取 3 或后端截取。
- 查询失败时是否隐藏模块、展示空态，还是 Toast。

### HOME-005：Card Home 不应承担交易状态机事实源

严重级别：中

当前文件已写“交易状态只作为首页展示，不作为交易状态机事实源”，方向正确。但建议进一步：

- 将交易状态映射完全移到 `card-transaction-flow.md` 或交易模块。
- Home 只保留 UI 展示字段。

---

## 10. `activation.md` 与 `pin.md` 的联动问题

### FLOW-001：激活成功、Set PIN、Card Home 入口之间缺少闭环

严重级别：高

事实文件中存在以下口径：

1. 实体卡需用户手动激活。
2. 虚拟卡无需激活，也无需设置 PIN。
3. 激活流程包括身份验证、设置 PIN（可选）及状态确认等步骤。
4. Active Card Page 卡号校验通过后自动进入 7.3 Set PIN / Change PIN。
5. Card Home 对 ACTIVE 卡允许 Set PIN（仅首次）和 Change PIN。

当前文档将 Activation 和 PIN 拆开是合理的，但缺少一个明确联动表：

| 场景 | 下一步 | 是否强制 | 接口顺序 | 失败后回退 |
|---|---|---|---|---|
| 卡号后四位校验通过 | Face Auth / Set PIN / Activation API | 待确认 | 待确认 | 待确认 |
| 激活成功且未设置 PIN | Set PIN | 是否可跳过待确认 | 待确认 | Card Home 小红点 |
| 用户从 Card Home 点 Set PIN | Set PIN | 可选 | Public Key -> Set PIN | 保持未设置 |

建议：在 `activation.md` 和 `pin.md` 中明确谁负责“激活后进入 PIN”的导航规则，避免重复或漏写。

---

## 11. `card-transaction-flow.md` 评审意见

### TXN-001：大量来源本次附件无法验证，应标注来源等级

严重级别：高

该文件引用很多本次附件未提供的来源，例如：

- `AIX Card交易【transaction】.pdf`
- `Transaction & History`
- `DTC Wallet OpenAPI Documentation`
- `Notification`
- 用户确认结论
- `transaction/reconciliation.md`

本次只能核对 DTC Card Issuing API 中存在的部分：

- Request Signature
- Inquiry Card Basic Info
- Transaction History Of Card
- Detail Of Card Transaction
- Inquiry Card Balance History
- Card Transaction Notify
- Transfer to wallet 等目录项

建议：将非本次附件来源标记为 `unverified_in_current_review`。

### TXN-002：交易文档与标准 PRD 模板不一致

严重级别：中

该文件虽然比其他文件更完整，但仍不是标准模板结构：

- 缺少标准“文档信息”正文表。
- “通知规则”有，但不完全按模板独立沉淀。
- “验收标准 / 测试场景”缺少可执行 case。
- “待确认事项”使用 ALL-GAP 列表，但不是模板要求的待确认事项表。

建议：保留 ALL-GAP 引用，同时新增标准模板下的待确认表和验收表。

### TXN-003：资金归集逻辑需要谨慎标注为用户确认，而不是 DTC API 事实

严重级别：中

当前文件写：

- 仅 refund / reversal / deposit 触发归集。
- balance > 0 调用 Transfer Balance to Wallet。
- 失败不自动重试，告警监控群。

这些规则主要来自“用户确认结论 / AIX Card交易 PRD”，不是 DTC API 自身规定。DTC API 只提供接口能力与字段。

建议：在每条资金归集规则旁明确来源类型，避免研发误以为 DTC 自动保证该流程。

---

## 12. `_index.md` 评审意见

### INDEX-001：索引文件没有说明目录是“PRD”还是“知识库”

严重级别：中

`_index.md` 如果作为知识库索引，可以不完全等同于 PRD。但本次用户要求对照标准 PRD 模板评审，因此 `_index.md` 至少应说明：

- 该目录是 Card 模块知识库。
- 每个功能文件是否必须符合标准 PRD 模板。
- `_index.md` 是否也按 PRD 模板维护。

建议：在开头增加定位说明。

### INDEX-002：索引中引用的功能文件依赖链需要区分“事实源”和“派生引用”

严重级别：中

当前各文件互相依赖，例如：

- Home 依赖 Status。
- Activation 依赖 Status / PIN / Security。
- PIN 依赖 Activation / Status。

建议 `_index.md` 增加依赖关系说明：

| 类型 | 文件 | 作用 | 是否事实源 |
|---|---|---|---|
| 基础事实 | `card-status-and-fields.md` | 状态、字段、接口 | 是 |
| 页面事实 | `card-home.md` | 首页 UI | 否，引用状态事实 |
| 功能流程 | `activation.md` | 激活 | 否，引用状态事实 |

---

## 13. 建议新增的统一待确认清单

| 编号 | 问题 | 影响模块 | 优先级 |
|---|---|---|---|
| Q-001 | `autoDebitEnabled` 产品枚举 `2/ON` 与 DTC API `1/ON` 如何映射？ | Application / Activation / Status | P0 |
| Q-002 | 自动扣款是在申卡时开启，还是实体卡激活时开启，还是两处都支持？ | Application / Activation / Home | P0 |
| Q-003 | Card Application 的 `currency` 是否应为 ISO 4217 法币？用户选择的 USDT/USDC/WUSD/FDUSD 如何映射？ | Application | P0 |
| Q-004 | 实体卡激活的最终顺序：Last4 -> Face Auth -> Activation API -> Set PIN，还是 Last4 -> Set PIN -> Activation？ | Activation / PIN | P0 |
| Q-005 | AIX 是否使用 DTC `Sent OTP For Card Activation`？ | Activation / Security | P1 |
| Q-006 | `Pending activation`、`Inactive`、`待激活` 的后端状态映射关系是什么？ | Status / Home / Activation | P0 |
| Q-007 | `BLOCKED`、`Terminated`、`Cancelled` 的关系是什么？注销卡成功后归入哪个状态？ | Status / Management | P0 |
| Q-008 | Lock / Unlock 是否支持虚拟卡？若支持，为什么文案写 physical card？ | Management / Home | P1 |
| Q-009 | 注销卡的页面流程、认证方式、确认弹窗、成功失败文案是什么？ | Management | P0 |
| Q-010 | Card Detail 查询失败时 Basic Info 和 Sensitive Info 是否统一使用 `Failed to get card info. Please try again later`？ | Sensitive Info | P1 |
| Q-011 | `Get Card Basic Info` 和 `Get Card Sensitive Info` 是否正式废弃旧 GET 路径？ | Status / Sensitive / Home | P0 |
| Q-012 | PIN Set / Reset 的 `encryptedPin` 字段和 RSA 加密方式是否由 DTC API 完全决定？ | PIN | P1 |
| Q-013 | Wallet / Card transaction 关联 ID 的最终对账字段组合是什么？ | Transaction Flow | P1 |

---

## 14. 建议验收标准补充方向

每个功能文件建议至少补充以下验收维度：

### 14.1 Application

- 首次申卡 / 非首次申卡入口正确。
- 5 张卡上限和审核中卡限制正确。
- 钱包余额为 0 与大于 0 的按钮逻辑正确。
- 虚拟卡 / 实体卡字段必填差异正确。
- Billing 信息姓名校验、KYC 比对正确。
- Mailing address 字段长度与 DTC 限制正确。
- 免费申卡、付费申卡、扣费失败、申卡失败均可落状态。
- DTC 错误码映射正确。

### 14.2 Status & Fields

- 每个状态的展示组正确。
- 每个状态的操作权限正确。
- Basic / Sensitive 字段展示正确。
- BLOCKED / CANCELLED / PENDING 等不可操作状态正确。
- 接口路径唯一且可调用。

### 14.3 Activation

- 待激活实体卡可进入激活。
- 虚拟卡不可进入激活。
- 后四位输入不足 4 位不提交。
- 输入满 4 位自动调用 Inquiry Card Basic Info。
- 后四位不一致显示红色错误。
- 网络 / 服务器错误使用正确弹窗并清空输入。
- 返回按钮挽留弹窗正确。
- 激活成功后的 PIN 入口正确。

### 14.4 PIN

- ACTIVE 未设置 PIN 展示 Set PIN。
- ACTIVE 已设置 PIN 展示 Change PIN。
- SUSPENDED / PENDING / BLOCKED 不允许 PIN 操作。
- PIN 只允许 4 位数字。
- Public Key 获取失败不能提交。
- Set PIN / Reset PIN 成功和失败状态正确。
- OTP 失败按安全规则处理。

### 14.5 Sensitive Info

- 未认证不展示 PAN / EXP / CVV。
- 认证成功后展示 Card Detail popup。
- 每个字段来源正确。
- 复制后 Toast 正确。
- Basic / Sensitive 任一接口失败时提示正确。

### 14.6 Card Management

- ACTIVE 可 Lock，不可 Unlock。
- SUSPENDED 可 Unlock，不可 Lock。
- ACTIVE / SUSPENDED 可注销卡，但流程待补。
- Lock 二次确认正确。
- Unlock 身份验证正确。
- 请求中 Loading 和重复提交控制正确。
- Freeze / Unfreeze 失败提示正确。

---

## 15. 结论

当前文档的主要问题不是“完全缺内容”，而是：

1. 标准 PRD 模板没有统一执行。
2. 基础状态和接口事实源没有先闭环。
3. DTC API 契约没有被完整转化为字段表和错误处理。
4. 页面交互细节没有按事实文件完整沉淀。
5. 待确认事项分散，且部分本应可确认的事实被误标成 gap。

建议先以 `card-status-and-fields.md` 为主修入口，完成状态、操作、字段、接口路径统一后，再同步修正其他功能文档。否则后续 Activation、PIN、Sensitive Info、Card Management 都会继续继承状态和接口层错误。