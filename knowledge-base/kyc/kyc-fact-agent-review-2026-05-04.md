# KYC 知识库 md 事实评审意见（Fact Agent）

> 评审日期：2026-05-04  
> 评审范围：`knowledge-base/kyc/_index.md`、`knowledge-base/kyc/account-opening.md`  
> 评审方式：只评审，不修改原 md 文档。  
> GitHub 目标目录：`knowledge-base/kyc`  
> 事实依据：用户上传的《AIX WALLET 钱包开户KYC需求V1.0 (1).docx》与《Master sub account 设计方案 (2).docx》。  
> 说明：用户消息中提到“对照以下模板”，但本轮消息未提供额外评审模板正文，因此本文件采用统一评论模板：严重级别 / 目标位置 / 当前问题 / 事实依据 / 建议评论。

---

## 0. 评审结论总览

本次评审发现：当前 `kyc/account-opening.md` 已经覆盖 KYC 主流程的大框架，但对事实文件中的页面细节、状态分流、国家线版本差异、协议与反向招揽、DTC/AAI 接口、错误码映射、POA 上传、Face 锁定规则等内容存在大量压缩、遗漏或降级为 Gap 的情况。

最需要优先处理的问题：

1. **国家支持范围写法不准确**：md 断言“只支持 AU / PH / VN”，但事实文件同时存在 VN/PH/AU 国家线、330 版本 PH+SG、3.6 内测 PH/AU/VN/SG 保持 Phase 1 等多个口径，应作为版本化事实或冲突 Gap，而不是简单写死 AU/PH/VN。
2. **KYC Loading Page 漏掉 waitlist 页面级拦截**：事实文件明确 waitlist 场景由弹窗调整为页面级拦截，且 KYC Loading 状态 2 包含“用户在 waitlist 中（仅限来源渠道 APP）”。md 没有体现。
3. **错误码与前端文案映射被错误降级为未确认**：事实文件已给出 passport、face comparison、POA 的错误码与 AIX 前端提示文案，md 仍写“AAI 原始错误码未完整转译 / 待确认”，容易误导后续使用。
4. **DTC / AAI 接口契约缺失**：`get-verification-url`、`verification-result`、webhook、passport-info、poa-info、POA upload token / upload-file、错误码、reverseSolicitation 等关键事实未沉淀。
5. **Face Guide 缺少接口层 20 次连续发起锁 20 分钟规则**：事实文件明确有三条锁定规则，md 只记录两条。
6. **DTC Sub Account 创建事实处理过保守**：Master sub account 方案的 POA 成功分支明确写到 create sub account / upload s3 / update status，当前 md 仍将“是否创建 Sub Account”整体作为不可推导，需要细化为“设计方案已写 POA 成功会创建，但实际落地、失败补偿、与 KYC Approved 的等价关系仍待确认”。
7. **协议与反向招揽事实缺失**：事实文件中协议保存、强制阅读、Declaration 文案、DTC reverseSolicitation 参数、50013 错误码均未完整记录。
8. **页面关闭 / 返回 / Retry / Toast / 文件上传状态等交互细节大量遗漏**：这些并非 UI 装饰，而是运行时事实，影响状态机、失败恢复、用户能否继续流程。

---

## 1. 严重级别定义

| 级别 | 含义 |
|---|---|
| P0 | 明显事实错误或会误导业务准入、状态机、账户模型的结论 |
| P1 | 关键事实遗漏，影响实现、评审、问答或后续知识库使用 |
| P2 | 重要细节缺失或表达过度概括，建议补齐 |
| P3 | 结构、溯源、表述或可维护性问题 |

---

## 2. 针对 `knowledge-base/kyc/_index.md` 的评审意见

### IDX-001｜P1｜`_index.md` 的 ALL-GAP 范围与事实文件不匹配

**目标位置**：`_index.md` / “待确认唯一来源” / ALL-GAP-033、ALL-GAP-035、ALL-GAP-046  
**当前问题**：文档称页面失败、Face 锁定可回填，但原始错误码、字段映射仍待确认。这个说法过于笼统。事实文件已经给出 passport error code、Face Comparison error code、POA error code 以及对应 AIX 前端提示文案；Master sub account 方案也给出了 DTC `get-verification-url`、`verification-result`、webhook、passport-info、poa-info、POA upload 的字段。  
**事实依据**：AIX KYC PRD 第 8、9 章；Master sub account 设计方案 DTC API、失败原因、POA 文件上传流程。  
**建议评论**：建议将 ALL-GAP 拆分为“已确认的 AIX 前端映射错误码 / DTC 接口字段”和“仍未确认的 AAI 原始内部错误码 / 供应商内部状态”。不要把已由 PRD 或 DTC 设计方案给出的错误码继续标为待确认。

### IDX-002｜P1｜`_index.md` 中“不得写入事实：KYC Approved 一定立即创建 DTC Sub Account”需要更细化

**目标位置**：`_index.md` / “不写入事实的内容”第 5 条  
**当前问题**：该条作为防误导原则可以保留，但现在容易压掉 Master sub account 设计方案中的明确流程事实。设计方案在 POA success 分支写明 DTC 执行 `create sub account [countryOfResidence] / upload s3 / update status`，并 webhook `poa success & verify success`。  
**事实依据**：Master sub account 设计方案 / kyc 流程 / upload poa 分支。  
**建议评论**：建议改成更准确的边界：`POA success 设计流程中包含 create sub account；但不能进一步推导 KYC Approved 通知一定等价于 Sub Account 创建成功，也不能推导创建失败时的 AIX 补偿机制。` 这样既保留防误导，又不遗漏已确认流程。

### IDX-003｜P1｜`_index.md` 没有提示国家线存在版本口径冲突

**目标位置**：`_index.md` / “待确认唯一来源”与模块边界  
**当前问题**：索引没有提示 `account-opening.md` 中国家支持范围存在版本化或冲突事实。事实文件同时出现：国家线 VN/PH/AU；KYC Start 里“330版本支持国家为 ph+sg”；Select Residence Country 里“3.6 内测版本生产验证，Phase 1 国家全部临时处理为 phase 2-waitlist，除了 PH、AU、VN、SG 保持 Phase 1”。  
**事实依据**：AIX KYC PRD / 国家线、KYC Start Page、Select Residence Country Page。  
**建议评论**：建议在 `_index.md` 的 ALL-GAP 或使用规则中新增“国家线 / Phase 版本口径”Gap，要求查询国家支持时必须读取 `account-opening.md` 的版本说明，不能只读单一 AU/PH/VN 结论。

### IDX-004｜P2｜`_index.md` 的来源引用包含“用户确认结论”，但本次事实文件无法验证

**目标位置**：`_index.md` / front matter `source_doc`、第 7 节来源引用  
**当前问题**：文档引用了“用户确认结论 / 2026-05-02 / 2026-05-03”。这些可能是有效来源，但不在本次附件事实文件中，Fact Agent 无法验证其内容。  
**事实依据**：本次用户仅提供两个事实 docx 附件。  
**建议评论**：建议把用户确认结论单独标为“外部确认来源”，并注明“不在当前事实附件内”。否则后续读者可能误以为所有结论都来自 PRD 或 DTC 设计方案。

### IDX-005｜P2｜`_index.md` 中“当前 main 上不存在”是时间敏感描述

**目标位置**：`_index.md` / 当前文件、已迁出旧路径、使用规则  
**当前问题**：文档在一个具体 commit 页面中写“当前 main 上不存在”，这类表述会随分支变化而失效。  
**事实依据**：GitHub 评审目标是具体 commit / tree；文档自身 last_updated 为 2026-05-03。  
**建议评论**：建议改为“截至 2026-05-03 的 main 快照中不存在”，或改为更稳定的“本模块 active 事实源不使用该路径”。

---

## 3. 针对 `knowledge-base/kyc/account-opening.md` 的总体评审意见

### ACC-001｜P0｜支持国家写死为 AU / PH / VN，遗漏 SG 与版本差异

**目标位置**：`account-opening.md` / 第 2 节事实摘要、第 3.2 节步骤 4、第 5.2 节 Select Residence Country  
**当前问题**：md 多处写“只支持 AU / PH / VN”或“支持国家 AU / PH / VN”。事实文件并不支持这样简单断言：

- “国家线”表写 VN / PH / AU 为支持；
- KYC Start Page 的特殊说明写“330版本支持国家为 ph+sg”；
- Select Residence Country Page 的特殊处理写“为了支持3.6内测版本生产验证，Phase 1 国家全部临时处理为 phase 2-waitlist，除了 PH、AU、VN、SG 保持 Phase 1”。

**事实依据**：AIX KYC PRD / 国家线、7.2.3 KYC Start Page、7.2.3.1 Select Residence Country Page。  
**建议评论**：建议不要写死“支持 AU / PH / VN”。应按版本和页面规则记录：`基础国家线：VN / PH / AU；330 版本特殊说明：PH + SG；3.6 内测特殊处理：PH / AU / VN / SG 保持 Phase 1，其余 Phase 1 临时转 phase 2-waitlist。最终线上口径需作为 Gap 确认。`

### ACC-002｜P0｜KYC Loading Page 漏掉 waitlist 状态 2 页面级拦截

**目标位置**：`account-opening.md` / 第 4.1 节状态机、第 5.1 节 KYC Loading Page、第 3.2 节步骤 1-2  
**当前问题**：md 只记录 `Under review` / `Rejected` / `Approved` 展示 Verification unavailable，`Pending` / `failed` 继续流程。事实文件明确：当后端返回 KYC 状态机为 `Under review / Rejected / Approved` **或用户在 waitlist 中（仅限来源渠道 APP）**，KYC Loading Page 展示状态 2 内容。变更日志还说明 waitlist 由弹窗提示调整为页面级拦截。  
**事实依据**：AIX KYC PRD / 需求变更日志 2026-1-15、7.2.2 KYC Loading Page。  
**建议评论**：建议补充 waitlist 页面级拦截规则：APP 来源用户一旦命中 waitlist，在 KYC Loading 即展示 Verification unavailable 或对应状态 2，不允许继续后续流程。

### ACC-003｜P1｜KYC Loading Page 缺少关闭按钮和挽留弹窗规则

**目标位置**：`account-opening.md` / 第 5.1 节 KYC Loading Page  
**当前问题**：事实文件要求 KYC Loading Page 的关闭按钮点击后弹出挽留弹窗，包含 Title、Content、Stay and continue、Leave 的行为。md 未记录。该行为影响用户能否中断流程以及返回入口。  
**事实依据**：AIX KYC PRD / 7.2.2 KYC Loading Page；变更日志 2026-1-20。  
**建议评论**：建议把所有带关闭 / 返回按钮的页面统一记录挽留弹窗规则，避免后续实现只在部分页面生效。

### ACC-004｜P1｜KYC Start Page 对未绑定手机号的描述超出事实文件

**目标位置**：`account-opening.md` / 第 3.2 节步骤 3  
**当前问题**：md 写“若手机号未绑定，先引导绑定手机号；已绑定则进入 Start”。事实文件当前只写：用户发起 KYC 流程时，若系统检测到手机号已绑定，则直接进入 KYC Start Page，不展示额外提示；同时变更日志写去掉绑定手机成功 toast。事实文件没有完整描述“未绑定时如何引导绑定手机号”的流程。  
**事实依据**：AIX KYC PRD / 7.2.3 KYC Start Page、变更日志 2026-1-20。  
**建议评论**：建议将“未绑定手机号如何处理”标为 Gap 或引用 Account / Security 事实源；不要在 KYC 文档中直接写成已确认流程。

### ACC-005｜P1｜协议规则被过度压缩，缺少快照、强制阅读、链接和保存内容

**目标位置**：`account-opening.md` / 第 3.2 步骤 5、第 5.2 节 Select Residence Country 中“协议勾选”  
**当前问题**：md 只写“协议默认不勾选；未勾选按钮不可点，勾选后可继续”。事实文件对协议有更细的运行时规则：

- Terms of Service and Privacy Policy：只需保存用户同意并提交的时间；单击可勾选；无需强制阅读；有第三方链接；
- Declaration of reverse solicitation：需要保存协议内容以及同意并提交时间；需要强制阅读；点击 I agree 后才能勾选；
- 本次提交成功后生成不可更改快照并绑定账户；
- 协议内容仅英文，无需多语言；
- 后端无法获取协议时 toast：`Something went wrong. Please try again later`。

**事实依据**：AIX KYC PRD / 7.2.3 KYC Start Page / 协议。  
**建议评论**：建议把协议拆成两个对象分别记录：ToS/Privacy 与 Reverse Solicitation Declaration，并记录保存字段、快照、强制阅读、链接、失败 toast。否则后续合规留痕和 DTC 参数传递会缺事实。

### ACC-006｜P1｜反向招揽 Declaration 与 DTC `reverseSolicitation` 参数未打通

**目标位置**：`account-opening.md` / 第 5.2 协议、第 6 节系统交互、第 11 节错误处理  
**当前问题**：事实文件中 KYC Start Page 有 Declaration of Reverse Solicitation 协议；Master sub account 设计方案中 `get-verification-url` 请求参数包含 `reverseSolicitation`，并说明若国家后台配置为需要提交反向招揽声明，该参数需填 `T`，否则为空或 `F`；错误码有 `50013 - Reverse solicitation not declared by end user`。md 没有记录这个合规事实链路。  
**事实依据**：AIX KYC PRD / 7.2.3 协议；Master sub account 设计方案 / get-verification-url API。  
**建议评论**：建议新增“Reverse Solicitation 合规链路”：前端强制阅读和同意 → AIX 保存内容与同意时间 → 后端调用 DTC get-verification-url 时按国家配置传 `reverseSolicitation=T` → 处理 50013 错误。

### ACC-007｜P1｜KYC Start Page 的立即认证按钮缺少 Phase 判断和 waitlist 弹窗细节

**目标位置**：`account-opening.md` / 第 3.2 步骤 5、第 5.2 节  
**当前问题**：md 没有记录点击立即认证后后端判断国家 Type 的规则：Phase 1 支持国家进入 Identity Verify；phase 2-waitlist 弹窗拦截，按钮包括 Join waitlist 和 Select other country；还遗漏了 330 版本支持国家 ph+sg 的特殊说明。  
**事实依据**：AIX KYC PRD / 7.2.3 KYC Start Page / 立即认证按钮。  
**建议评论**：建议记录按钮点击后的国家 Type 分流，而不是只写“勾选后进入 Identity Verify”。

### ACC-008｜P1｜Select Residence Country Page 缺少国家列表展示、排序、Forbidden 隐藏、Type 定义

**目标位置**：`account-opening.md` / 第 5.2 节 Select Residence Country  
**当前问题**：md 只记录默认国家和支持 / 非支持国家，没有记录：支持搜索和列表；展示全部国家；按首字母排序；支持国家 + 不支持国家展示；禁止国家隐藏；Type 列表 Phase 1 / phase 2-waitlist / Forbiden 的含义。  
**事实依据**：AIX KYC PRD / 7.2.3.1 Select Residence Country Page。  
**建议评论**：建议把国家列表作为配置事实单独记录，尤其 `Forbiden` 隐藏规则和 Type 分类，避免后续误把禁止国家也展示给用户。

### ACC-009｜P2｜Waitlist Page 缺少关闭按钮、按钮禁用、网络/服务器错误 toast

**目标位置**：`account-opening.md` / 第 5.3 节 Waitlist  
**当前问题**：md 已记录 email 长度、格式和后端记录，但缺少：关闭按钮返回上一级；email 为空时按钮灰色不可点击；网络异常 toast `Please check your internet connection and try again.`；后端服务器错误 toast `Something went wrong. Please try again later`。  
**事实依据**：AIX KYC PRD / 7.2.3.2 Waitlist Page。  
**建议评论**：建议补齐 Waitlist 的前端交互与异常处理，否则后续实现可能只保留入库逻辑，遗漏用户体验与失败路径。

### ACC-010｜P1｜Identity Verify Page 缺少 DTC 01009 / 01005 错误处理

**目标位置**：`account-opening.md` / 第 5.4 节 Identity Verify / Identity Scan、第 11 节错误处理  
**当前问题**：事实文件明确点击相机进入 AAI H5 之前，若 DTC 返回 `01009`，toast `Mobile number already exists.`；若返回 `01005`，toast `The email address is in use.`。md 未记录。  
**事实依据**：AIX KYC PRD / 7.2.4 Identity Verify Page；Master sub account 设计方案 / get-verification-url errCode。  
**建议评论**：建议在 Identity Verify / get-verification-url 错误处理中补充 01009、01005，以及 Master 设计方案列出的其他错误码，至少把 AIX 页面需要展示的错误先沉淀。

### ACC-011｜P2｜Identity Verify 授权弹窗细节不完整

**目标位置**：`account-opening.md` / 第 5.4 节  
**当前问题**：md 记录了未授权弹窗、永久拒绝 open settings，但没有记录授权弹窗新增点：进入 Identity / POA 流程前新增授权弹窗；用户点击 not now 停留当前页；点击 Allow access 后根据未授权 / 已拒绝 / 永久拒绝分别处理。  
**事实依据**：AIX KYC PRD / 需求变更日志 2026-1-15、7.2.4 Identity Verify Page。  
**建议评论**：建议补充授权弹窗的按钮和分支，尤其 `not now` 不进入系统授权、`Allow access` 后才触发系统弹窗或 settings。

### ACC-012｜P1｜Face Guide 缺少“接口层连续发起 20 次锁 20 分钟”规则

**目标位置**：`account-opening.md` / 第 5.5 Face Guide / Face Scan / Face Loading、第 11 节错误处理  
**当前问题**：md 记录了 5 次失败锁 20 分钟、10 次失败锁 24 小时，但遗漏事实文件中的规则三：24 小时内，接口层面连续发起 20 次则锁 20min，验证成功后清零重新计算。  
**事实依据**：AIX KYC PRD / 7.2.6 Face Guide Page / 安全限制规则。  
**建议评论**：建议补充第三条锁定规则，并区分“face result=fail 计数”与“接口连续发起计数”的统计口径。

### ACC-013｜P1｜Face Guide Continue 缺少 passport country 获取与 fallback SG 规则

**目标位置**：`account-opening.md` / 第 5.5 Face Guide、第 6.2 系统交互  
**当前问题**：事实文件明确用户点击 Continue 后，AIX 后端调用 passport get result 接口获取 country；若 country 存在直接使用；若为空，默认使用 `sg`；AIX 后端传给前端，前端调用 AAI 活体 H5 并传入 country。md 没有记录。  
**事实依据**：AIX KYC PRD / 7.2.6 Face Guide Page / Continue 按钮。  
**建议评论**：建议将 Face Guide Continue 的 country 参数链路补充为运行时事实。该规则影响 AAI 活体 H5 入参，不能只写“进入 Face Scan”。

### ACC-014｜P2｜Face Guide 锁定弹窗文案和剩余时间展示规则缺失

**目标位置**：`account-opening.md` / 第 5.5、第 11 节  
**当前问题**：md 仅写“锁定则展示限制”，缺少弹窗 title/content、`[time]` 单位规则（大于 1 小时按小时，小于 1 小时按分钟）、Try again Later 返回业务流程入口页。  
**事实依据**：AIX KYC PRD / 7.2.6 Face Guide Page。  
**建议评论**：建议补齐锁定弹窗内容和时间展示规则，否则前端会无法一致展示剩余锁定时长。

### ACC-015｜P1｜Face Scan 缺少 AAI signatureId 最多重试 3 次限制

**目标位置**：`account-opening.md` / 第 5.5 Face Scan  
**当前问题**：事实文件注明 AAI 同一个 `signatureId` 最多重试 3 次，3 次后终止采集；调用方需要重来时发起 `generate-url` 重新生成 `signatureId`。md 未记录。  
**事实依据**：AIX KYC PRD / 7.2.7 Face Scan Page 知识点。  
**建议评论**：建议新增 Face Scan 的 AAI 重试边界，避免 AIX 端误以为同一 URL / signatureId 可以无限重试。

### ACC-016｜P1｜Face Loading Page 缺少状态 2 分流规则

**目标位置**：`account-opening.md` / 第 5.5 Face Loading  
**当前问题**：md 记录了后台轮询、成功 / 失败 / 30 秒无结果，但事实文件还规定 Face Loading Page 的状态 2：当后端返回 KYC 状态机为 `Under review / Rejected / Approved`，展示状态 2 内容。  
**事实依据**：AIX KYC PRD / 7.2.8 Face Loading Page。  
**建议评论**：建议补充 Face Loading 的 `Under review / Rejected / Approved` 分流，以免只按 face compare 成功 / 失败处理。

### ACC-017｜P2｜Loading Failed Page 缺少 Retry 行为

**目标位置**：`account-opening.md` / 第 5.5 或第 11 节  
**当前问题**：md 只写 30 秒无结果进入 Loading Failed Page，没有记录 Retry 按钮点击后进入 Face Loading Page 并重新提交。  
**事实依据**：AIX KYC PRD / 7.2.9 Loading Failed Page。  
**建议评论**：建议补充 Loading Failed Page 的 Retry 行为，并明确它不是返回 Face Scan，而是进入 Face Loading Page 重新提交。

### ACC-018｜P1｜Face Failed Page 动态失败原因和优先级缺失

**目标位置**：`account-opening.md` / 第 11 节错误 / 失败 / 重试 / 锁定 / 人工处理  
**当前问题**：md 仅写失败进入 Face Failed Page，没有记录事实文件中的动态原因规则：

- face result 为空：`Liveness check failed. Please try again.`；
- passport 失败：展示 Document Verification 错误码映射文案；
- face result 为 `FAIL / EXPIRED / incomplete`：展示 Face Comparison API 错误码映射文案；
- passport 与 face 均失败：优先展示 passport 失败原因；
- POA 失败：展示 POA error code 映射文案；
- 兜底文案：`The verification was not successful. Please review your information and try again.`。

**事实依据**：AIX KYC PRD / 7.2.10 Face Failed Page、9 接口错误码映射。  
**建议评论**：建议新增 Face Failed Page 失败原因决策表，尤其记录 passport 优先级和 POA 失败也可能展示在 Face Failed Page 的事实。

### ACC-019｜P1｜Face Failed Page Try again 规则缺失

**目标位置**：`account-opening.md` / 第 11 节  
**当前问题**：事实文件规定 Try again 按钮正常状态会重新触发 KYC 流程，并根据用户当前最新认证结果状态自动判断跳转起始页；锁定状态点击按钮弹窗提示 `For your account security...`，确认后返回流程入口页。md 未记录。  
**事实依据**：AIX KYC PRD / 7.2.10 Face Failed Page。  
**建议评论**：建议补齐 Try again 的正常态和锁定态规则，否则失败恢复路径不完整。

### ACC-020｜P1｜Address Upload Page 缺少 AAI / DTC 对 POA 的审核职责边界

**目标位置**：`account-opening.md` / 第 3.2 步骤 12、第 6.1 系统角色、第 12 节责任边界  
**当前问题**：md 只写“采集或提交地址证明材料”，没有记录事实文件中 AAI 与 DTC 的 POA 审核职责：AAI 只有机审，提取 POA 资料、验证真实性/是否篡改、默认验证有效期；DTC 机审 + 人审，机审核验 POA 国家与用户填报居住国是否匹配、申请国家是否白名单；人审核对姓名一致性、文件真伪和复杂场景。  
**事实依据**：AIX KYC PRD / 7.2.11 Address Upload Page。  
**建议评论**：建议在系统责任边界中补充 POA 的 AAI / DTC 分工，避免把 POA 全部归为 AAI 或 AIX。

### ACC-021｜P1｜Address Upload Page 文件上传限制和状态缺失

**目标位置**：`account-opening.md` / 第 5 页面规则、第 11 错误处理  
**当前问题**：事实文件明确 POA 上传支持 JPG/JPEG/PNG/PDF，单个文件 16MB，只能上传一份；有未上传、上传中、已上传三个状态；上传中可删除取消；已上传可删除，可预览图片或 PDF；格式、大小、服务器报错有对应 toast。md 未记录。  
**事实依据**：AIX KYC PRD / 7.2.11 Address Upload Page。  
**建议评论**：建议补充 POA 文件上传状态机与校验文案，不能只写“上传地址证明”。

### ACC-022｜P1｜Address Upload Page 的 Residence 国家可改与提交时国家判断缺失

**目标位置**：`account-opening.md` / 第 3.2 步骤 12、第 5 页面规则  
**当前问题**：事实文件规定 Address Upload Page 中 Residence 回填 KYC 流程选择的居住国家，点击可进入 Select Residence Country Page 修改；continue 后后端还会判断国家是否属于支持国家，非支持国家弹窗进入 Waitlist 或选择其他国家。md 未记录。  
**事实依据**：AIX KYC PRD / 7.2.11 Address Upload Page。  
**建议评论**：建议记录 POA 阶段可变更居住国家，以及提交时二次国家判断。否则后续会误以为国家只在 KYC Start 阶段判断一次。

### ACC-023｜P1｜Address Upload Page 中“continue 后进入 Identity Verify Page”疑似源文档矛盾未标 Gap

**目标位置**：`account-opening.md` / 第 3.2 步骤 12  
**当前问题**：事实文件 7.2.11 中写“点击后，后端判断若属于支持国家，则进入下一级页面 Identity Verify Page”，但同段后面又写“后端返回提交成功，前端跳转至 KYC Submission Success Page”。从流程看，POA 后应进入 Submission Success，前一句可能是复制 KYC Start 的描述。md 直接写成功后进入 Submission Success，但没有记录源文档存在冲突。  
**事实依据**：AIX KYC PRD / 7.2.11 Address Upload Page。  
**建议评论**：建议将该处标为 PRD 文案疑似冲突 Gap：POA continue 支持国家时是否应进入 Submission Success，还是文档误写 Identity Verify Page。不能静默消除冲突。

### ACC-024｜P1｜外部接口依赖章节几乎未沉淀

**目标位置**：`account-opening.md` / 第 6、7、8、11、15 节  
**当前问题**：事实文件第 8 章和 Master 方案给出大量接口事实，但 md 只抽象描述“外部依赖”和“接收结果”，缺少可查询的接口契约。至少应记录：

- 查询 KYC 结果：`externalId`、`dtcId`、`clientStatus`、`passportVerifyStatus`、`faceIdVerifyStatus`、`proofOfAddressVerifyStatus`；
- webhook：`clientId`、`externalId`、`clientStatus`、`nationality`、`countryOfResidence`、各 verify status / code、`requestId`；
- `get-verification-url` 的 `successRedirectUrl`、`failureRedirectUrl`、`externalId`、`eKycVerifyType`、`country`、`language`、`email`、`mobile`、`reverseSolicitation`；
- `passport-info` 与 `poa-info` 查询字段；
- POA upload token 与 upload-file。

**事实依据**：AIX KYC PRD / 8 外部接口依赖；Master sub account 设计方案 / DTC 提供的 API。  
**建议评论**：建议新增“DTC / KYC 接口契约事实”章节，区分 AIX 页面事实与接口事实。否则知识库无法支撑后续 API 问答。

### ACC-025｜P0｜错误码映射表缺失，且被错误标为未确认

**目标位置**：`account-opening.md` / 第 11、14.1、14.2 节  
**当前问题**：AIX KYC PRD 第 9 章提供 passport、Face Comparison、POA 的错误码与 AIX 映射前端提示文案；Master sub account 设计方案也提供 DTC API 错误码和失败原因。md 没有沉淀这些表，反而写“AAI 原始错误码未完整转译 / 待确认”。  
**事实依据**：AIX KYC PRD / 9.1 passport error code、9.2 Face Comparison error code、9.3 POA error code；Master sub account 设计方案 / errCode、失败原因。  
**建议评论**：建议立即补齐 AIX 前端映射错误码表，并将 Gap 缩小为“AAI 原始内部错误码是否还有未暴露项”。已在事实文件出现的错误码不应标为未确认。

### ACC-026｜P1｜passport 错误码存在 PRD 与 Master 方案命名差异，md 未标识

**目标位置**：`account-opening.md` / 错误码相关章节  
**当前问题**：AIX PRD passport error code 中有 `Duplicated`；Master sub account 方案中 passport error code 有 `DUPLICATED_ID_NUMBER`、`DUPLICATED_USER`。两份事实文件存在命名差异。md 未记录错误码，因此也没有标出这个差异。  
**事实依据**：AIX KYC PRD / 9.1 passport error code；Master sub account 设计方案 / dtc 提供 passport 的 error code。  
**建议评论**：建议记录“PRD 前端映射码”和“DTC 原始码”两层，并建立映射 Gap，避免直接把 `Duplicated` 当成 DTC 原始码。

### ACC-027｜P1｜POA 有效期事实不一致，md 未标 Gap

**目标位置**：`account-opening.md` / Address Upload / POA 相关  
**当前问题**：AIX PRD 7.2.11 的 POA 知识点写 AAI 默认验证“仅接受过去三个月内签发的文档”；但 9.3 POA error code 中 `NOT_WITHIN_6_MONTHS` 的前端文案是 “issued within the last 6 months”。md 未记录 POA 有效期，也未将 3 个月 / 6 个月差异标为 Gap。  
**事实依据**：AIX KYC PRD / 7.2.11 Address Upload Page、9.3 POA error code。  
**建议评论**：建议新增 Gap：POA 文档有效期到底是 3 个月还是 6 个月；在确认前不要写死有效期。

### ACC-028｜P1｜KYC 结果通知规则来源不足或与事实文件不匹配

**目标位置**：`account-opening.md` / 第 2 节事实摘要、第 10 节通知规则  
**当前问题**：md 写 KYC Approved / Rejected / Failed 均有 Email / in-app notification / push 规则，但本次上传的 AIX KYC PRD 自动提取内容中没有看到完整 Notification 章节或模板细节。该结论可能来自其他知识库文件或未上传资料。  
**事实依据**：本次可见事实文件主要覆盖页面、接口、错误码；通知细节未完整出现在附件抽取内容中。  
**建议评论**：建议将 Notification 结论标明具体来源文件。如果来源不是本次附件，应写为“来自 common/notification 或其他来源”，不要伪装成 AIX KYC PRD 的已确认事实。

### ACC-029｜P1｜KYC 状态机未区分 AIX 页面状态与 DTC `clientStatus` / `EKycFileVerifyStatus`

**目标位置**：`account-opening.md` / 第 4 节 KYC 状态机、第 8 节字段边界  
**当前问题**：md 状态机只记录 `Pending`、`failed`、`Under review`、`Rejected`、`Approved` 的 AIX 页面语义，但事实文件还给出 DTC 查询结果的 `clientStatus` 数字枚举和 `passportVerifyStatus / faceIdVerifyStatus / proofOfAddressVerifyStatus` 的 `UNVERIFIED / VERIFYING / VERIFY_SUCCESS / VERIFY_FAILURE`。当前文档没有把 AIX 页面状态与 DTC 状态分层，容易混用。  
**事实依据**：AIX KYC PRD / 8.1 查询 KYC 结果接口；Master sub account 设计方案 / verification-result API。  
**建议评论**：建议新增三层状态模型：AIX 页面分流状态、DTC clientStatus、DTC EKycFileVerifyStatus，并明确映射待确认处。不要只维护一张页面状态表。

### ACC-030｜P1｜DTC `clientStatus` 枚举缺失

**目标位置**：`account-opening.md` / 第 8 节字段边界  
**当前问题**：Master sub account 设计方案给出 `clientStatus` 枚举，包括 `SUSPENDED=0`、`PENDING_KYC=1`、`REGISTERED=3`、`REJECTED=4`、`ACTIVATED=99` 等。md 没有记录，但又使用 Approved / Rejected 等状态进行能力判断。  
**事实依据**：Master sub account 设计方案 / verification-result API / ClientStatus。  
**建议评论**：建议补充 DTC clientStatus 枚举，并说明 AIX 页面上的 Approved / Rejected 是否与 DTC 枚举存在一一映射仍需确认。

### ACC-031｜P1｜KYC 过程中“护照未出结果也可做人脸比对”的异步异常场景缺失

**目标位置**：`account-opening.md` / 第 3.2、5.5、6.2、11 节  
**当前问题**：Master sub account 方案明确：DTC 支持在护照上传还没有验证结果但已有 OCR 信息时继续进行人脸比对；异常场景是人脸比对成功后，护照最终可能失败，因此如果护照还在处理中，需要根据护照最终结果更新人脸比对结果：护照通过则人脸通过，护照失败则人脸失败。md 没有记录该关键异步依赖。  
**事实依据**：Master sub account 设计方案 / 问题：dtc 是否支持上一步护照上传还没有验证结果就继续人脸比对。  
**建议评论**：建议在 Face Loading / 状态机中补充“passport pending + face success”的延迟判定规则，避免把 face compare success 当作最终通过。

### ACC-032｜P1｜AAI ProductLevel 缺失

**目标位置**：`account-opening.md` / AAI 外部依赖 / 系统交互  
**当前问题**：Master 方案写明 AAI 提供不同 ProductLevel：护照 `STANDARD`；活体验证和交易中的人脸验证 `PRO`。md 没有记录。  
**事实依据**：Master sub account 设计方案 / AAI 提供不同 ProductLevel。  
**建议评论**：建议补充 AAI ProductLevel 事实，尤其区分 KYC 护照 OCR 与 Liveness / Face Auth 的级别。

### ACC-033｜P1｜POA 文件上传 token 双步骤缺失

**目标位置**：`account-opening.md` / Address Upload / DTC API  
**当前问题**：Master 方案明确 POA 上传分两步：先 `Post /openapi/v1/file/get-upload-token`，该请求需要验签，token 只能使用一次且 5 分钟有效；再 `Post /openapi/v1/ekyc/upload-file`，携带 token 上传文件，此时不需要验签。md 没有记录。  
**事实依据**：Master sub account 设计方案 / POA 文件上传流程。  
**建议评论**：建议补充 POA 上传技术事实，包括 token 有效期、一次性、是否验签、documentType=3、externalId、fileContent、countryOfResidence、返回 requestId、错误码 14004 / 14005。

### ACC-034｜P1｜POA upload 的国家参数与 md 国家线没有对齐

**目标位置**：`account-opening.md` / 国家线、Address Upload、DTC API  
**当前问题**：Master 方案的 POA upload-file 示例中 `countryOfResidence` 说明为 `(PHL，AUS，VNM) 如果其他国家会 error`。而 PRD 又有 SG 相关特殊处理。md 只写 AU / PH / VN，没有把 DTC API 国家代码与前端国家线 / SG 特殊版本差异对齐。  
**事实依据**：Master sub account 设计方案 / upload-file API；AIX KYC PRD / KYC Start 与 Select Residence Country 特殊说明。  
**建议评论**：建议把国家线拆成“前端选择国家 / KYC Phase 配置 / DTC POA upload 支持国家代码”三层，并对 SG 是否可上传 POA 标 Gap。

### ACC-035｜P1｜`get-verification-url` 的 VerificationType 与 requestId 缺失

**目标位置**：`account-opening.md` / Identity Scan、Face Scan、DTC API  
**当前问题**：Master 方案给出 `eKycVerifyType`：`PASSPORT=1`、`SELFIE=4`，返回参数含 `url`、`urlExpiredTime`、`externalId`、`verificationType`、`requestId`。md 没有记录这些会话和结果查询关键字段。  
**事实依据**：Master sub account 设计方案 / passport/selfie verification url。  
**建议评论**：建议补充 H5 URL 生成接口字段，以便后续知道 Identity Scan 与 Face Scan 分别传什么类型、如何用 requestId 追踪。

### ACC-036｜P1｜webhook 事件 `KYC_VERIFICATION` 与数据结构缺失

**目标位置**：`account-opening.md` / 系统交互、接口依赖、状态机  
**当前问题**：Master 方案给出 webhook 事件为 `KYC_VERIFICATION`，data 中包含 `externalId`、`clientStatus`、`nationality`、`countryOfResidence`、passport / face / POA verify status 与 code、`requestId`。md 只笼统写“接收结果 / 通知”，没有记录 webhook 结构。  
**事实依据**：Master sub account 设计方案 / webhook 的接口。  
**建议评论**：建议新增 webhook 数据结构表，并说明 AIX 后端通过 webhook 与 query 双路径更新状态。

### ACC-037｜P1｜passport-info / poa-info OCR 反显接口缺失

**目标位置**：`account-opening.md` / 外部接口依赖、字段边界  
**当前问题**：Master 方案给出 `GET /openapi/v1/ekyc/passport-info/{externalId}` 返回 `fullName`、`idNumber`、`dateOfBirth`、`gender`、`nationality`；`GET /openapi/v1/ekyc/poa-info/{externalId}` 返回 address1/2/3、country、state、city、postal。md 没有记录。  
**事实依据**：Master sub account 设计方案 / 查询护照 ocr 信息、查询 POA ocr 信息。  
**建议评论**：建议补充 OCR 反显接口事实，并与 ALL-GAP 中“字段映射待确认”区分：接口字段已经有来源，是否展示 / 入库 / 与 AIX 字段映射才是 Gap。

### ACC-038｜P1｜POA success 创建 Sub Account 的流程事实没有正确落地

**目标位置**：`account-opening.md` / 第 6.2、7.2、8、14 节  
**当前问题**：md 反复写 KYC Approved 是否必然创建 DTC Sub Account 待确认。作为谨慎边界可以理解，但 Master 方案的 POA success 分支明确写 `create sub account [countryOfResidence] / upload s3 / update status`。md 未沉淀这一流程事实。  
**事实依据**：Master sub account 设计方案 / upload poa sequence。  
**建议评论**：建议写成：“设计流程：POA success 后 DTC 创建 Sub Account，并上传 S3、更新状态；仍待确认：该 create sub account 是否已上线、失败补偿、是否与 AIX 的 KYC Approved 通知完全同步。”

### ACC-039｜P2｜POA failed 分支中 `update passport verify failed status` 疑似设计文档笔误，md 未识别

**目标位置**：`account-opening.md` / 错误处理、DTC API  
**当前问题**：Master 方案 upload poa 的 failed 分支写 `update passport verify failed status`，上下文看可能应为 POA verify failed status。md 没有记录，也没有标出该源文档疑点。  
**事实依据**：Master sub account 设计方案 / upload poa sequence。  
**建议评论**：建议新增 Gap：POA failed 时 DTC 更新的是 proofOfAddressVerifyStatus 还是 passportVerifyStatus；需要 DTC 确认。

### ACC-040｜P1｜AAI / DTC / KUN 链路描述与事实文件角色不完全一致

**目标位置**：`account-opening.md` / 第 6.1、6.2  
**当前问题**：md 把 KUN 作为 AIX 与 AAI 的承接方，但本次上传的 Master sub account 设计方案 sequence 主要是 `customer(aix page) -> aix -> dtc -> aai`；AIX KYC PRD 中确有 AIX App / AIX Platform / KUN / AAI / DTC / AIX Ledger 等角色，但具体链路未完全展开。md 当前写法“通过 KUN / AAI 链路承接”可能混合了不同来源。  
**事实依据**：AIX KYC PRD / 账户结构说明；Master sub account 设计方案 / sequenceDiagram。  
**建议评论**：建议明确两种链路来源：PRD 角色边界包含 KUN；DTC 设计方案中的接口链路是 AIX -> DTC -> AAI。不要在没有映射说明时把 KUN 固定写入每个 DTC API 调用路径。

### ACC-041｜P2｜AIX WALLET PRD 的“申请单长期有效 / DTC 认证结果永久有效”未沉淀

**目标位置**：`account-opening.md` / KYC 状态机、失败重试  
**当前问题**：事实文件 6.2 KYC 状态机注释写：申请单自创建后长期有效；一旦用户 OCR、Face 等核心认证成功通过，其在 DTC 侧认证结果将永久有效，不会因时间推移失效。md 没有记录这个关键状态生命周期事实。  
**事实依据**：AIX KYC PRD / 6.2 KYC 状态机。  
**建议评论**：建议补充 KYC 申请单和 DTC 认证结果生命周期，尤其与重试、重复进入、审核失败后的状态复用有关。

### ACC-042｜P1｜passport / face 成功后不会再变失败的规则未完整记录

**目标位置**：`account-opening.md` / KYC 状态机、Face Failed、人工审核  
**当前问题**：事实文件知识点写：只要 passport、face 认证通过，不会再变为失败状态；KYC 人工审核如果 OCR name 等有问题，人工审核直接改，不影响状态；如果 id 有问题，直接 kyc reject；passport、face 认证状态也不会变。md 未记录这组关键状态不可逆规则。  
**事实依据**：AIX KYC PRD / 7 需求描述 / 知识点。  
**建议评论**：建议将 passport / face 状态不可逆和人工审核处理方式写入状态机边界，避免后续误以为人工审核会回写 passportVerifyStatus 或 faceIdVerifyStatus。

### ACC-043｜P2｜AAI 接口耗时事实未记录

**目标位置**：`account-opening.md` / KYC Loading、Face Loading、POA、系统交互  
**当前问题**：事实文件提供 AAI 接口耗时参考：Document Verification p90=20-25s、p95=25-35s、p99=35-40s；Face Comparison 226ms~348ms；POA 异步数分钟。md 没有记录。  
**事实依据**：AIX KYC PRD / 7 需求描述 / 知识点。  
**建议评论**：建议补充耗时参考，并说明 Face Loading 30 秒超时与 Document Verification p95/p99 的关系，POA 不应按短轮询即时结果处理。

### ACC-044｜P1｜KYC Start Page “绑定手机成功 toast 去掉”变更未记录

**目标位置**：`account-opening.md` / KYC Start / 变更日志相关  
**当前问题**：事实文件变更日志 2026-1-20 写 KYC start page 去掉绑定手机成功 toast 提示。md 只写已绑定进入 Start，没有记录这个变更。  
**事实依据**：AIX KYC PRD / 需求变更日志 2026-1-20。  
**建议评论**：如果 md 要沉淀页面运行时事实，建议记录“已绑定手机号进入 Start，不展示额外 toast / 绑定成功 toast 已移除”。

### ACC-045｜P1｜KYC Loading Page 和 KYC Start Page 增加挽留弹窗的变更未整体落地

**目标位置**：`account-opening.md` / KYC Loading、KYC Start、页面交互  
**当前问题**：事实文件变更日志明确 KYC loading page 和 KYC start page 增加弹出挽留弹窗。md 没有系统记录 KYC Start 的返回按钮挽留弹窗，KYC Loading 也缺。  
**事实依据**：AIX KYC PRD / 需求变更日志 2026-1-20、7.2.2、7.2.3。  
**建议评论**：建议新增“通用退出挽留弹窗”规则，并列出适用页面：KYC Loading、KYC Start、Identity Verify、Face Guide、Face Loading、Loading Failed、Address Upload 等。

### ACC-046｜P2｜KYC Submission Success Page 细节过少

**目标位置**：`account-opening.md` / 第 3.2 步骤 13  
**当前问题**：md 写“等待审核结果”，但事实文件还规定返回首页按钮：用户点击后关闭当前 KYC 流程，并返回业务流程入口页。  
**事实依据**：AIX KYC PRD / 7.2.12 KYC Submission Success Page。  
**建议评论**：建议补充返回首页按钮行为，尤其“关闭当前 KYC 流程”这一状态动作。

### ACC-047｜P1｜`source_doc` 引用未上传事实文件 `DTC Wallet OpenAPI Document20260126`，本次无法验证

**目标位置**：`account-opening.md` / front matter `source_doc`、第 2 节 WalletAccount 字段、第 8 节 Wallet Account 字段边界  
**当前问题**：md 的 WalletAccount 字段、WalletConnect token、Wallet OpenAPI 等部分可能来自 `DTC Wallet OpenAPI Document20260126 (1).docx`，但本次用户没有上传该文件。作为 Fact Agent，本次无法确认 WalletAccount 字段是否准确。  
**事实依据**：本次附件只有 AIX KYC PRD 和 Master sub account 设计方案。  
**建议评论**：建议在评审范围中标明：WalletAccount 字段与 Wallet OpenAPI 相关事实本次不可验证；若保留，需要补充对应附件或降低为“来源未核验”。

### ACC-048｜P2｜front matter `source_section` 过长且混合多个来源，不利于追溯

**目标位置**：`account-opening.md` / front matter  
**当前问题**：`source_section` 把 AIX KYC PRD、Master / Sub Account、D-SUB-ACCOUNT-ID、WalletAccount、Notification、ALL-GAP 等混在一个长字符串中。后续无法判断每个事实对应哪个文件和章节。  
**事实依据**：当前 md front matter。  
**建议评论**：建议按来源拆成结构化列表，例如 `sources: [{file, section, used_for}]`。这不是事实错误，但会影响审计和追溯。

---

## 4. 建议新增或调整的知识库结构

### 4.1 建议新增章节：国家线与 Phase 规则

建议在 `account-opening.md` 中新增独立章节，记录：

| 层级 | 建议记录内容 |
|---|---|
| PRD 国家线 | VN / PH / AU |
| 330 版本特殊说明 | PH + SG |
| 3.6 内测特殊处理 | PH / AU / VN / SG 保持 Phase 1；其他 Phase 1 临时转 phase 2-waitlist |
| Select Residence Country Type | Phase 1 / phase 2-waitlist / Forbiden |
| DTC POA upload country code | PHL / AUS / VNM；SG 是否支持待确认 |
| Gap | 最终线上版本国家线与 SG 支持范围待确认 |

### 4.2 建议新增章节：DTC KYC API 契约

建议至少记录：

1. `POST /openapi/v1/ekyc/get-verification-url`
2. `GET /openapi/v1/ekyc/verification-result/{externalId}`
3. `KYC_VERIFICATION` webhook
4. `GET /openapi/v1/ekyc/passport-info/{externalId}`
5. `GET /openapi/v1/ekyc/poa-info/{externalId}`
6. `POST /openapi/v1/file/get-upload-token`
7. `POST /openapi/v1/ekyc/upload-file`

并把字段分为：入参、返回、错误码、AIX 处理。

### 4.3 建议新增章节：错误码映射

建议把 PRD 第 9 章三张表完整沉淀为：

1. Passport / Document Verification 错误码映射；
2. Face Comparison 错误码映射；
3. POA 错误码映射；
4. PRD 映射码与 DTC 原始码命名差异；
5. Face Failed Page 展示优先级。

### 4.4 建议新增章节：页面退出 / 返回 / Retry 通用规则

事实文件中多个页面共用挽留弹窗，建议抽象为通用规则，再在页面表中引用，避免重复遗漏。

### 4.5 建议调整 ALL-GAP

| Gap | 建议调整 |
|---|---|
| ALL-GAP-033 | 从“失败 / 重试 / 人工处理规则待确认”缩小为“人工处理、补偿机制、PRD 与 DTC 源文档冲突项待确认”；页面失败、Face 锁定、Face Failed 文案已可回填 |
| ALL-GAP-035 | 从“实际依赖哪些 AAI 结果”缩小为“字段映射、原始状态、AIX 展示映射边界”；Passport OCR / Liveness / Face Comparison / POA 类别已确认 |
| ALL-GAP-046 | 区分“AAI 原始内部码未确认”和“PRD / DTC 已给出的错误码映射已确认” |
| 新增 Gap | 国家线 / Phase 版本口径冲突：VN/PH/AU、PH+SG、PH/AU/VN/SG 三种口径如何落地 |
| 新增 Gap | POA 有效期 3 个月 vs 6 个月冲突 |
| 新增 Gap | POA failed 更新 passportVerifyStatus 还是 proofOfAddressVerifyStatus |
| 新增 Gap | KUN 在 DTC -> AAI 链路中的实际位置 |
| 新增 Gap | SG 是否支持 DTC POA upload-file 的 countryOfResidence |

---

## 5. 可直接作为 GitHub Review Comment 的评论清单

以下评论可直接贴到 PR 或 issue 中：

1. `account-opening.md` 当前把支持国家写成 AU / PH / VN，但 PRD 中存在 VN/PH/AU、330 版本 PH+SG、3.6 内测 PH/AU/VN/SG 三种口径。建议改成版本化事实，并新增国家线 Gap，避免写死。
2. KYC Loading Page 缺少 waitlist 页面级拦截。PRD 明确 waitlist 场景从弹窗调整为页面拦截，且 APP 来源用户在 waitlist 时 Loading Page 展示状态 2。
3. 协议部分过度压缩。ToS/Privacy 与 Reverse Solicitation Declaration 的保存内容、同意时间、强制阅读、链接、快照、获取协议失败 toast 都应补齐。
4. Reverse Solicitation 前端协议与 DTC `reverseSolicitation` 入参、50013 错误码没有打通，建议补充合规链路。
5. Face Guide 漏了“24 小时内接口层连续发起 20 次锁 20min”的第三条安全限制规则。
6. Face Guide Continue 缺少 passport get result 获取 country、空值 fallback SG、传给 AAI 活体 H5 的入参规则。
7. Face Scan 缺少 AAI 同一 `signatureId` 最多重试 3 次，重来需重新 generate-url 的边界。
8. Face Failed Page 缺少动态失败原因、错误码映射和展示优先级，尤其 passport 与 face 均失败时优先展示 passport 原因。
9. Address Upload Page 缺少 POA 文件格式、16MB、单文件、上传中/已上传状态、删除/预览、toast 文案。
10. Address Upload Page 缺少 POA 阶段居住国家可修改，以及提交时二次国家判断和 waitlist 分流。
11. PRD 中 POA continue 同时出现“进入 Identity Verify Page”和“提交成功进入 KYC Submission Success Page”，疑似源文档冲突，建议标 Gap 而不是静默选择。
12. 错误码映射表不应继续标为未确认。PRD 已给出 passport、face、POA 三张前端提示映射表；Master 方案也给出 DTC 原始错误码。
13. DTC KYC API 契约缺失，包括 get-verification-url、verification-result、webhook、passport-info、poa-info、POA upload token、upload-file。
14. KYC 状态机应分层记录 AIX 页面状态、DTC clientStatus、DTC EKycFileVerifyStatus，避免混用 Pending / failed / Rejected 与 DTC 数字枚举。
15. Master 方案明确支持护照仍在处理中继续做人脸比对，并根据护照最终结果更新 face 结果；当前 md 未记录该异步异常场景。
16. Master 方案的 POA success 分支明确 create sub account，md 不应完全写成“是否创建 Sub Account 待确认”；应改为“设计流程已写，落地与失败补偿待确认”。
17. POA 有效期在 PRD 中存在 3 个月与 6 个月两种口径，应新增 Gap。
18. `source_doc` 中引用了本次未上传的 DTC Wallet OpenAPI 文档，WalletAccount 字段本次无法验证，建议标注来源未核验。
19. Notification 规则在本次附件中未看到完整来源，建议补充具体来源或降低为待核验。
20. `current main 上不存在` 等时间敏感描述建议改为带日期的快照描述，避免未来 main 变化导致事实失真。

---

## 6. 本次未修改内容声明

本次仅新增本评审意见文件，未修改以下原文件：

- `knowledge-base/kyc/_index.md`
- `knowledge-base/kyc/account-opening.md`

