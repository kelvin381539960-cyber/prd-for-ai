# KYC 知识库 PM 收敛修正方案

> 日期：2026-05-04  
> 角色：PM Agent  
> 输入：`knowledge-base/kyc/kyc-fact-agent-review-2026-05-04.md`、AIX KYC PRD、Master sub account 设计方案  
> 输出：评审意见收敛后的修正方案  
> 当前动作：只新增本修正方案文档，不直接修改原事实文件  
> 待修正目标文件：`knowledge-base/kyc/account-opening.md`、`knowledge-base/kyc/_index.md`

---

## 1. PM 收敛结论

Fact Agent 的评审意见数量较多，但问题本质可以收敛为 10 个修正主题：

| 编号 | 修正主题 | 影响级别 | PM 结论 |
|---|---|---|---|
| T1 | 国家线 / Phase / 版本口径 | P0 | 必须修正，不能继续写死 AU / PH / VN |
| T2 | KYC Loading 与 waitlist 页面级拦截 | P0 | 必须修正，当前遗漏关键分流 |
| T3 | 错误码与前端文案映射 | P0 | 必须修正，已确认内容不应继续标为待确认 |
| T4 | 协议 / Reverse Solicitation 合规链路 | P1 | 必须修正，影响合规留痕和 DTC 入参 |
| T5 | Face 流程 / 锁定 / 重试 / 失败展示 | P1 | 必须修正，当前缺多条运行时规则 |
| T6 | Address Upload / POA 流程 | P1 | 必须修正，当前 POA 审核、上传、国家校验不完整 |
| T7 | DTC / AAI 接口契约 | P1 | 必须修正，当前知识库无法支撑接口问答 |
| T8 | AIX 页面状态、DTC clientStatus、EKycFileVerifyStatus 分层 | P1 | 必须修正，避免状态混用 |
| T9 | DTC Sub Account 创建边界 | P1 | 需要修正，既不能过度推导，也不能忽略设计方案事实 |
| T10 | 来源、Gap 与 `_index.md` 索引治理 | P2 | 建议同步修正，提高可维护性 |

---

## 2. 修正目标

本次修正不是扩大 PRD 范围，而是把现有事实文件中的内容准确沉淀到知识库。

修正目标：

1. `account-opening.md` 从“流程摘要型文档”升级为“可查询、可追溯、可用于 AI 问答的 KYC 运行时事实源”。
2. `_index.md` 保持索引定位，但补充关键边界提示，避免错误引用。
3. 已由附件明确的事实，不再保留为 Gap。
4. 源文件存在冲突或未明确的内容，必须显式标为 Gap，不静默选择。
5. 不把外部系统内部逻辑写成 AIX 已确认事实。

---

## 3. 修正范围

### 3.1 本轮应修正

| 文件 | 修正范围 |
|---|---|
| `knowledge-base/kyc/account-opening.md` | 国家线、页面规则、状态机、DTC API、错误码、POA、Face、协议、Sub Account、Gap |
| `knowledge-base/kyc/_index.md` | 索引提示、Gap 口径、来源边界、不得推导规则 |

### 3.2 本轮不修正

| 内容 | 处理方式 |
|---|---|
| `common/aai.md` | 只引用，不在本轮展开 AAI 供应商完整说明 |
| `common/dtc.md` | 如需沉淀通用 DTC 模型，另起 DTC 通用修正任务 |
| `common/notification.md` | 本轮只在 KYC 文档标注通知来源待核验，不直接改通知模块 |
| 代码 / 接口实现 | 不涉及 |
| 未上传的 DTC Wallet OpenAPI 文档 | 本轮只能标记为“来源未核验”，不能补事实 |

---

## 4. PM 收敛后的修正原则

### 4.1 已确认事实优先写入

以下内容已在事实文件中出现，应写入事实源：

1. KYC 页面完整路径。
2. waitlist 页面级拦截。
3. 协议勾选、强制阅读、快照、保存内容。
4. Reverse Solicitation Declaration 与 DTC `reverseSolicitation` 参数。
5. Face 三类锁定规则。
6. Face Failed 动态失败原因展示优先级。
7. POA 上传限制、上传状态、审核职责。
8. DTC KYC API、webhook、passport-info、poa-info、POA upload token / upload-file。
9. Passport / Face / POA 错误码映射。
10. DTC clientStatus 与 EKycFileVerifyStatus 枚举。

### 4.2 冲突事实必须显式标 Gap

以下内容不要静默处理，应进入 Gap：

| Gap | 冲突 / 不确定点 |
|---|---|
| GAP-KYC-COUNTRY-001 | 国家线存在 VN/PH/AU、PH+SG、PH/AU/VN/SG 多个版本口径 |
| GAP-KYC-POA-001 | POA 有效期存在 3 个月与 6 个月两种口径 |
| GAP-KYC-POA-002 | POA continue 后“进入 Identity Verify”疑似 PRD 复制错误，与 Submission Success 冲突 |
| GAP-KYC-POA-003 | POA failed 时 DTC 更新 passportVerifyStatus 还是 proofOfAddressVerifyStatus |
| GAP-KYC-SG-001 | SG 是否支持 DTC POA upload-file 的 `countryOfResidence` |
| GAP-KYC-KUN-001 | KUN 在 AIX -> DTC -> AAI 链路中的实际位置 |
| GAP-KYC-NOTIFICATION-001 | KYC 通知规则本次附件来源不足，需要补 Notification 原文或模块来源 |
| GAP-KYC-WALLET-001 | WalletAccount / WalletConnect 相关事实依赖未上传的 DTC Wallet OpenAPI 文档，本轮不可验证 |

### 4.3 不得推导的内容继续保留

以下边界仍应保留：

1. 不推导 Wallet KYC 与 Card KYC 完全相同。
2. 不推导 AIX user 与 DTC Sub Account 一定一一对应。
3. 不推导 `D-SUB-ACCOUNT-ID` 与 WalletAccount.clientId 完全等价。
4. 不推导 KYC Approved 通知一定代表 Sub Account 已创建成功。
5. 不推导 KYC Approved 一定代表所有 Wallet / Deposit / WalletConnect / Receive 能力可用。
6. 不推导 DTC Sub Account 创建失败时 AIX 一定有自动补偿。

---

## 5. `account-opening.md` 修正方案

### 5.1 建议重构后的章节结构

建议将 `account-opening.md` 调整为以下结构：

```md
# Account Opening / KYC 开户与身份认证准入

## 1. 文档定位
## 2. 已确认事实摘要
## 3. 国家线 / Phase / 版本口径
## 4. 用户侧开户 / KYC 主流程
## 5. 页面与交互规则
  ### 5.1 通用退出挽留弹窗
  ### 5.2 KYC Loading Page
  ### 5.3 KYC Start Page
  ### 5.4 Select Residence Country Page
  ### 5.5 Waitlist Page
  ### 5.6 Identity Verify / Identity Scan
  ### 5.7 Face Guide / Face Scan / Face Loading
  ### 5.8 Loading Failed / Face Failed
  ### 5.9 Address Upload / POA
  ### 5.10 KYC Submission Success
## 6. KYC 状态模型
  ### 6.1 AIX 页面状态
  ### 6.2 DTC clientStatus
  ### 6.3 DTC EKycFileVerifyStatus
  ### 6.4 状态映射边界 / Gap
## 7. DTC / AAI 接口契约
## 8. 错误码与前端文案映射
## 9. DTC Master / Sub Account / Wallet Account 边界
## 10. KYC 结果与能力准入
## 11. 通知规则
## 12. 系统责任边界
## 13. 不得推导的内容
## 14. 未确认项 / Gap
## 15. 来源引用
```

---

## 6. 分主题修正明细

### T1｜国家线 / Phase / 版本口径

**当前问题**：md 写死“支持 AU / PH / VN”，与事实文件多个版本口径不一致。

**修正动作**：

1. 删除“只支持 AU / PH / VN”的绝对表达。
2. 新增“国家线 / Phase / 版本口径”章节。
3. 分层记录：

| 层级 | 修正后记录 |
|---|---|
| PRD 国家线 | VN / PH / AU |
| KYC Start 330 版本特殊说明 | PH + SG |
| Select Residence Country 3.6 内测特殊处理 | PH / AU / VN / SG 保持 Phase 1；其他 Phase 1 临时转 phase 2-waitlist |
| Type 定义 | Phase 1 = 支持国家；phase 2-waitlist = 不支持国家；Forbiden = 禁止国家 |
| 列表展示 | 支持国家 + 不支持国家展示；禁止国家隐藏；国家按首字母排序；支持搜索 |
| DTC POA upload | PHL / AUS / VNM；SG 是否支持待确认 |

**PM 结论**：必须改。最终文案应承认版本口径差异，并新增 Gap。

---

### T2｜KYC Loading 与 waitlist 页面级拦截

**当前问题**：md 漏掉 waitlist 状态 2 页面级拦截。

**修正动作**：

1. 在 KYC Loading Page 中补充：
   - 用户进入默认为 loading。
   - 当后端返回 KYC 状态为 `Under review / Rejected / Approved`，展示状态 2。
   - 当用户在 waitlist 中，且来源渠道为 APP，展示状态 2。
2. 在 waitlist 章节中补充：
   - waitlist 由弹窗提示调整为页面级拦截。
   - 命中 waitlist 后用户不能继续后续 KYC 流程。

**PM 结论**：必须改。这是流程分流错误，不是 UI 细节。

---

### T3｜错误码与前端文案映射

**当前问题**：md 未沉淀 PRD 第 9 章错误码映射，还将错误码继续标为待确认。

**修正动作**：

1. 新增“错误码与前端文案映射”章节。
2. 完整记录三张映射表：
   - passport / Document Verification error code；
   - Face Comparison error code；
   - POA error code。
3. 区分两类错误码：
   - PRD 已确认的 AIX 前端映射码；
   - DTC / AAI 原始码命名差异。
4. 对命名差异单独标 Gap，例如：
   - PRD 中 `Duplicated`；
   - Master 方案中 `DUPLICATED_ID_NUMBER` / `DUPLICATED_USER`。

**PM 结论**：必须改。已在事实文件中的映射不能继续标为未确认。

---

### T4｜协议 / Reverse Solicitation 合规链路

**当前问题**：协议规则过度压缩，Reverse Solicitation 没有和 DTC 入参连接。

**修正动作**：

1. KYC Start Page 中补充协议规则：
   - 默认不勾选；
   - 未勾选按钮不可点击；
   - ToS / Privacy Policy 单击可勾选，无需强制阅读；
   - Declaration of Reverse Solicitation 需要强制阅读，同意后才能勾选；
   - 提交成功后生成不可更改快照并绑定用户账户；
   - 协议内容仅英文，无需多语言；
   - 获取协议失败 toast：`Something went wrong. Please try again later`。
2. 新增 Reverse Solicitation 链路：
   - 前端强制阅读并同意；
   - AIX 保存协议内容、同意时间；
   - DTC `get-verification-url` 根据国家配置传 `reverseSolicitation=T`；
   - DTC `50013` 表示用户未声明 reverse solicitation。

**PM 结论**：必须改。该问题影响合规和接口入参。

---

### T5｜Face 流程 / 锁定 / 重试 / 失败展示

**当前问题**：Face 流程缺多条运行时规则。

**修正动作**：

1. Face Guide 中补三条安全限制：
   - 24 小时内 face 失败 5 次，锁 20 分钟；
   - 24 小时内 face 失败 10 次，锁 24 小时；
   - 24 小时内接口层连续发起 20 次，锁 20 分钟；验证成功后清零。
2. 补充计数口径：
   - 失败计数只统计 DTC 返回 `face result=fail`；
   - passport 失败不计入 face 失败；
   - 人脸通过后清零。
3. Face Guide Continue 补充：
   - AIX 后端调用 passport get result 获取 country；
   - country 存在则使用；为空则默认 `sg`；
   - AIX 后端传给前端，前端调用 AAI 活体 H5 并传 country。
4. Face Scan 补充：
   - AAI 同一 `signatureId` 最多重试 3 次；
   - 3 次后终止采集；
   - 需要重来时重新 generate-url。
5. Face Loading 补充：
   - `Under review / Rejected / Approved` 也会展示状态 2；
   - 30 秒无结果进入 Loading Failed。
6. Loading Failed 补充：
   - Retry 后进入 Face Loading Page 重新提交。
7. Face Failed 补充：
   - 主文案固定 `Verification failed.`；
   - face result 为空展示 liveness 失败文案；
   - passport 失败展示 Document Verification 映射文案；
   - face result 为 `FAIL / EXPIRED / incomplete` 展示 Face Comparison 映射文案；
   - passport 与 face 均失败，passport 优先；
   - POA 失败展示 POA 映射文案；
   - 兜底文案。

**PM 结论**：必须改。Face 是 KYC 主链路，不能只保留高层流程。

---

### T6｜Address Upload / POA 流程

**当前问题**：POA 审核职责、上传规则、提交分流缺失。

**修正动作**：

1. 补充 AAI / DTC POA 分工：
   - AAI：机审、提取 POA 信息、验证真实性、篡改、有效期；
   - DTC：机审 + 人审；机审核验居住国匹配、白名单；人审核姓名一致性、文件真伪、复杂场景。
2. 补充上传限制：
   - JPG / JPEG / PNG / PDF；
   - 单文件 16MB；
   - 只能上传一份文件。
3. 补充上传状态：
   - 未上传；
   - 上传中，可删除取消；
   - 已上传，可删除，可预览图片或 PDF。
4. 补充 toast：
   - 格式不支持；
   - 文件超 16MB；
   - 上传服务器报错。
5. 补充 Residence 可改：
   - 回填 KYC 流程中选择的居住国家；
   - 点击可进入 Select Residence Country Page 修改。
6. 补充 continue 后二次国家判断：
   - 支持国家继续；
   - 不支持国家进入 waitlist 弹窗；
   - 支持国家后到底进入 Submission Success 还是 Identity Verify，按 Gap 处理。

**PM 结论**：必须改。POA 是提交审核前的关键页面，当前事实不够支撑实现和问答。

---

### T7｜DTC / AAI 接口契约

**当前问题**：接口事实几乎没有沉淀。

**修正动作**：

新增“DTC / AAI 接口契约”章节，至少包含：

| 接口 / 事件 | 必须记录内容 |
|---|---|
| `POST /openapi/v1/ekyc/get-verification-url` | 入参、VerificationType、reverseSolicitation、返回 url / expireTime / requestId、错误码 |
| `GET /openapi/v1/ekyc/verification-result/{externalId}` | externalId、dtcId、clientStatus、nationality、countryOfResidence、三类 verifyStatus / code |
| `KYC_VERIFICATION` webhook | event、clientId、data 字段、requestId |
| `GET /openapi/v1/ekyc/passport-info/{externalId}` | fullName、idNumber、dateOfBirth、gender、nationality |
| `GET /openapi/v1/ekyc/poa-info/{externalId}` | address1/2/3、country、state、city、postal |
| `POST /openapi/v1/file/get-upload-token` | documentType=3、externalId、签名、token |
| `POST /openapi/v1/ekyc/upload-file` | token、fileContent、countryOfResidence、requestId、错误码 |

**PM 结论**：必须改。否则知识库无法回答接口字段、状态来源、错误码来源。

---

### T8｜状态模型分层

**当前问题**：AIX 页面状态、DTC clientStatus、DTC 文件审核状态混在一起，容易误用。

**修正动作**：

新增三层状态模型：

#### AIX 页面状态

| 状态 | 页面语义 |
|---|---|
| `Pending` | 可继续或重新进入 KYC 流程 |
| `failed` | 上次流程失败，可按规则继续 |
| `Under review` | 已提交，等待审核 |
| `Rejected` | 审核被拒绝 |
| `Approved` | 审核通过 |

#### DTC clientStatus

记录 Master 方案枚举，例如：

| Name | ID | Descriptor |
|---|---:|---|
| SUSPENDED | 0 | Suspended |
| PENDING_KYC | 1 | Pending KYC |
| REGISTERED | 3 | Self Registered |
| REJECTED | 4 | Rejected |
| ACTIVATED | 99 | Activated |

其他枚举按事实文件补齐。

#### DTC EKycFileVerifyStatus

| Name | ID | Descriptor |
|---|---:|---|
| UNVERIFIED | 1 | Document verification is not completed |
| VERIFYING | 2 | Document verification is in progress |
| VERIFY_SUCCESS | 3 | Document verification succeeded |
| VERIFY_FAILURE | 4 | Document verification failed |

**PM 结论**：必须改。状态模型是后续所有准入判断的基础。

---

### T9｜DTC Sub Account 创建边界

**当前问题**：md 过度保守，把 Sub Account 创建全部写成待确认，但 Master 方案已有 POA success 创建分支。

**修正动作**：

1. 在 DTC Sub Account 章节记录：
   - Master 方案的 POA success 分支包含 `create sub account [countryOfResidence] / upload s3 / update status`；
   - webhook 返回 `poa success & verify success`。
2. 继续保留以下 Gap：
   - 该流程是否已上线；
   - 创建失败时 AIX 如何补偿；
   - KYC Approved 通知是否严格等价于 Sub Account 创建成功；
   - AIX user 与 DTC Sub Account 是否一一对应；
   - `D-SUB-ACCOUNT-ID` 与 WalletAccount.clientId 是否完全等价。

**PM 结论**：需要修正为“设计事实已确认，落地和等价关系待确认”。

---

### T10｜来源、Gap 与 `_index.md` 治理

**当前问题**：索引没有提示核心冲突，部分来源不可验证，部分时间敏感描述不稳定。

**修正动作**：

1. `_index.md` 新增提示：国家线 / Phase 存在版本口径冲突，查询国家支持必须读取 `account-opening.md`。
2. `_index.md` 中 ALL-GAP-033 / 035 / 046 改为更细：
   - 已确认页面级失败、Face 锁定、PRD 错误码；
   - 未确认 AAI 原始内部码、补偿机制、字段映射边界。
3. `当前 main 上不存在` 改为带日期快照描述或改为“active 事实源不使用该路径”。
4. 对“用户确认结论”标注为外部确认来源，不与本次附件混为一类。
5. 对未上传的 DTC Wallet OpenAPI 文档标注“本轮未核验”。

**PM 结论**：建议同步改，避免索引继续引导错误引用。

---

## 7. 优先级与执行顺序

### Phase 1：必须立即修正

| 顺序 | 内容 | 文件 |
|---:|---|---|
| 1 | 国家线 / Phase / 版本口径 | `account-opening.md` |
| 2 | KYC Loading + waitlist 页面级拦截 | `account-opening.md` |
| 3 | 错误码与前端文案映射 | `account-opening.md` |
| 4 | 状态模型分层 | `account-opening.md` |
| 5 | Face 锁定 / 重试 / 失败展示 | `account-opening.md` |
| 6 | 协议 / Reverse Solicitation | `account-opening.md` |

### Phase 2：关键补全

| 顺序 | 内容 | 文件 |
|---:|---|---|
| 7 | Address Upload / POA 完整规则 | `account-opening.md` |
| 8 | DTC / AAI 接口契约 | `account-opening.md` |
| 9 | DTC Sub Account 创建边界 | `account-opening.md` |
| 10 | 申请单长期有效、passport / face 成功不回退 | `account-opening.md` |

### Phase 3：治理与索引同步

| 顺序 | 内容 | 文件 |
|---:|---|---|
| 11 | Gap 收敛与新增冲突 Gap | `account-opening.md` |
| 12 | 索引边界、来源、时间敏感描述 | `_index.md` |
| 13 | Notification / Wallet OpenAPI 来源待核验标注 | `account-opening.md`、`_index.md` |

---

## 8. 建议最终交付物

如果进入实际修正阶段，建议形成以下交付：

1. 更新后的 `knowledge-base/kyc/account-opening.md`。
2. 更新后的 `knowledge-base/kyc/_index.md`。
3. 简短变更说明，记录：
   - 已从 Fact Review 回填的事实；
   - 新增 Gap；
   - 明确仍不可推导的边界；
   - 本轮未核验来源。

不建议创建更多过程文件，避免知识库文件膨胀。

---

## 9. PM 决策记录

| 决策项 | 结论 |
|---|---|
| 是否直接采用 Fact Agent 的 48 条评论逐条修改 | 否，先收敛为 10 个主题再修正 |
| 是否把所有 Gap 都保留 | 否，已由事实文件确认的内容应回填，不继续保留为 Gap |
| 是否把国家线写死为 AU / PH / VN | 否，改为版本化事实 + Gap |
| 是否把错误码继续标为未确认 | 否，PRD 和 Master 方案已有的错误码应写入 |
| 是否确认 KYC Approved 一定创建 Sub Account | 否，只记录 POA success 设计流程包含 create sub account，等价关系仍待确认 |
| 是否修改原 md | 本文件不直接修改；后续执行修正时再改原 md |

---

## 10. 建议后续执行指令

后续若要进入实际修正文档，可按以下方式执行：

```text
请根据 knowledge-base/kyc/kyc-pm-correction-plan-2026-05-04.md，修改 knowledge-base/kyc/account-opening.md 和 knowledge-base/kyc/_index.md。
```

执行时应遵守：

1. 只改上述两个目标文件。
2. 不新增无关过程文件。
3. 不补写未上传事实文件中的内容。
4. 所有冲突事实显式写入 Gap。
5. 修改完成后回报 commitSha 和变更摘要。

---

## 11. 本次文件变更声明

本次仅新增 PM 修正方案文件：

- `knowledge-base/kyc/kyc-pm-correction-plan-2026-05-04.md`

本次未修改：

- `knowledge-base/kyc/_index.md`
- `knowledge-base/kyc/account-opening.md`
- `knowledge-base/kyc/kyc-fact-agent-review-2026-05-04.md`
