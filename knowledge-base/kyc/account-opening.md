---
module: kyc
feature: account-opening
version: "1.2"
status: active
source_doc: 历史prd/AIX WALLET 钱包开户KYC需求V1.0 (1).docx；DTC接口文档/Master sub account 设计方案 (2).docx；DTC Wallet OpenAPI Document20260126（本轮未核验，仅保留历史来源提示）；knowledge-base/common/aai.md；knowledge-base/common/dtc.md；knowledge-base/changelog/knowledge-gaps.md；用户确认结论 2026-05-02
source_section: AIX Wallet Account Opening & KYC；KYC 状态机；开户页面逻辑；DTC KYC API；Master / Sub Account；D-SUB-ACCOUNT-ID；POA Upload；错误码映射；标准 PRD 模板
last_updated: 2026-05-04
owner: 吴忆锋
readers: [product, ui, dev, qa, business, ai]
depends_on:
  - kyc/_index
  - common/aai
  - common/dtc
  - common/notification
  - wallet/deposit
  - wallet/balance
  - changelog/knowledge-gaps
  - _system-boundary
---

# Account Opening / KYC 开户与身份认证准入 PRD

## 1. 文档信息

| 项目 | 内容 |
|---|---|
| 功能名称 | Account Opening / KYC 开户与身份认证准入 |
| 所属模块 | KYC |
| Owner | 吴忆锋 |
| 版本 | 1.2 |
| 状态 | Review |
| 更新时间 | 2026-05-04 |
| 来源文档 | AIX WALLET 钱包开户KYC需求V1.0；Master sub account 设计方案；DTC Wallet OpenAPI Document20260126（本轮未核验）；KYC 知识库评审意见；标准 PRD 模板 |
| 适用读者 | Product / UI / Dev / QA / Business / AI |
| 文档定位 | 本文既作为 KYC 运行时事实源，也按标准 PRD 模板沉淀产品范围、流程、页面、接口、异常、待确认事项、验收标准与测试场景。 |

---

## 2. 需求背景、目标与范围

### 2.1 需求背景

AIX 钱包开户需要完成用户身份认证、居住国家判断、协议确认、证件识别、人脸验证、地址证明上传及后续审核，以满足合规准入、账户创建和后续钱包能力开通的基础要求。

KYC 能力不是单一 Wallet 页面能力，而是影响 Account、Wallet、Deposit、WalletConnect、Receive、Notification、外部 DTC 账户体系以及 AAI 身份验证链路的基础准入能力。

### 2.2 用户问题 / 业务问题

| 问题类型 | 当前问题 |
|---|---|
| 用户问题 | 用户需要知道是否可以开户、如何完成身份认证、失败后如何重试、被 waitlist 或锁定时如何处理。 |
| 业务问题 | AIX 需要基于国家线、KYC 状态、外部身份认证结果控制用户能否继续开户及后续钱包能力。 |
| 合规问题 | KYC 需要保存协议同意时间、Reverse Solicitation Declaration 内容与快照，并根据国家配置传递 DTC 反向招揽参数。 |
| 系统问题 | KYC 依赖 AIX App / Backend、DTC、AAI、KUN 等多方系统，需要明确状态、接口、webhook、错误码和责任边界。 |
| QA 问题 | KYC 涉及多页面、多状态、多异常、多外部依赖，必须提供验收标准和测试场景矩阵。 |

### 2.3 需求目标

1. 建立 AIX 钱包开户 / KYC 的标准产品流程。
2. 明确 KYC 主流程、分支、异常、锁定、waitlist、POA 和提交审核规则。
3. 明确 AIX 页面状态、DTC `clientStatus`、DTC `EKycFileVerifyStatus` 的边界。
4. 明确 DTC / AAI 相关接口、webhook、字段和错误码映射。
5. 明确权限、合规、风控、通知、数据保存和待确认事项。
6. 提供 QA 可验收的验收标准和测试场景矩阵。
7. 防止 AI 或后续文档错误推导 Wallet / Card / Sub Account / Notification 等跨模块事实。

### 2.4 涉及功能清单

| 功能点 | 本期范围 | 优先级 | 状态 | 说明 |
|---|---|---|---|---|
| KYC Loading 状态分流 | In Scope | P0 | Confirmed | 根据 KYC 状态、waitlist、异常和超时分流。 |
| KYC Start | In Scope | P0 | Confirmed | 展示认证入口、居住国家、协议和立即认证按钮。 |
| Select Residence Country | In Scope | P0 | Confirmed / Open | 国家线存在版本口径冲突，见 GAP-KYC-COUNTRY-001。 |
| Waitlist | In Scope | P0 | Confirmed | waitlist 为页面级拦截，提交后用户无法继续 KYC。 |
| 协议与 Reverse Solicitation | In Scope | P0 | Confirmed | 保存同意时间、协议内容、快照，并影响 DTC 入参。 |
| Identity Verify / Passport OCR | In Scope | P0 | Confirmed | 调用外部 H5 完成护照扫描。 |
| Face Guide / Face Scan / Face Loading | In Scope | P0 | Confirmed | 包含活体采集、人脸比对、锁定、超时和失败处理。 |
| Address Upload / POA | In Scope | P0 | Confirmed / Open | 文件上传、国家二次判断、POA 审核；有效期和跳转冲突见 Gap。 |
| KYC Submission Success | In Scope | P1 | Confirmed | 提交成功后关闭当前 KYC 流程并返回入口。 |
| DTC KYC API / webhook | In Scope | P0 | Confirmed | 包含 URL、结果查询、webhook、OCR info、POA upload。 |
| 错误码映射 | In Scope | P0 | Confirmed / Open | PRD 已有映射；部分 DTC 原始码差异见 Gap。 |
| DTC Sub Account 创建边界 | In Scope | P1 | Confirmed / Open | 设计流程包含 POA success 后 create sub account；等价关系待确认。 |
| KYC 通知 | Deferred | P1 | Open | 历史记录存在通知规则，本轮附件未完整核验模板。 |
| Wallet / Deposit / WalletConnect 准入 | Deferred | P1 | Open | 只记录依赖边界，不在本文补完整钱包规则。 |
| Card KYC 复用关系 | Out of Scope | P2 | Open | 是否复用 Wallet / Account Opening KYC 未确认。 |
| Send / Swap | Out of Scope | P2 | Deferred | 当前不纳入 active KYC 准入范围。 |

---

## 3. 业务流程与规则

### 3.1 业务主流程说明

KYC 主流程按业务阶段可归纳为：

```text
准入状态判断
→ 居住国家与协议确认
→ 证件认证
→ 人脸验证
→ 地址证明上传
→ 提交审核
→ 结果通知 / 入口状态感知
```

页面路径为：

```text
KYC Loading
→ KYC Start
→ Select Residence Country
→ Agreement
→ Identity Verify
→ Identity Scan
→ Face Guide
→ Face Scan
→ Face Loading
→ Address Upload
→ KYC Submission Success
```

关键分支包括：waitlist、Verification unavailable、Network Error、Server Error、Loading Failed、Face Failed、POA 错误、DTC API 错误、国家线冲突和外部状态延迟。

### 3.2 业务时序图

```mermaid
sequenceDiagram
    autonumber
    actor User as 用户
    participant App as AIX App
    participant Backend as AIX Backend / KYC 服务
    participant DTC as DTC
    participant AAI as AAI H5 / 身份验证能力

    Note over User,AAI: A. 准入判断
    User->>App: 发起 KYC / 开户流程
    App->>Backend: 查询 KYC 状态 / waitlist 状态
    Backend-->>App: 返回 Pending / failed / Under review / Rejected / Approved / waitlist

    alt 不可继续验证
        App-->>User: 展示 Verification unavailable 或 waitlist 拦截
    else 可继续验证
        App-->>User: 展示 KYC Start
    end

    Note over User,AAI: B. 国家与协议确认
    User->>App: 选择居住国家并勾选协议
    App->>Backend: 保存协议同意时间 / 快照 / reverse solicitation 信息
    Backend-->>App: 返回可继续或错误

    alt 国家不支持 / waitlist
        App-->>User: 进入 Waitlist Page 或 waitlist 拦截
    else 国家支持
        App-->>User: 进入 Identity Verify
    end

    Note over User,AAI: C. Passport OCR
    User->>App: 点击相机开始证件认证
    App->>Backend: 请求护照 H5 URL
    Backend->>DTC: get-verification-url(PASSPORT)
    DTC->>AAI: 获取护照扫描 H5 URL
    AAI-->>DTC: 返回 url / expireTime
    DTC-->>Backend: 返回 url / requestId
    Backend-->>App: 返回 H5 URL
    App-->>User: 打开 AAI H5 扫描护照
    AAI-->>DTC: webhook 返回 passport 结果
    DTC-->>Backend: webhook / query 同步 passport 结果

    Note over User,AAI: D. Face verification
    User->>App: 在 Face Guide 点击 Continue
    App->>Backend: 判断锁定规则并获取 passport country
    Backend->>DTC: 获取 selfie / liveness H5 URL
    DTC->>AAI: 获取活体 H5 URL
    AAI-->>DTC: 返回 url / expireTime
    DTC-->>Backend: 返回 url / requestId
    Backend-->>App: 返回 H5 URL
    App-->>User: 打开 AAI H5 完成活体采集
    AAI-->>DTC: webhook 返回 liveness / face compare 结果
    DTC-->>Backend: webhook / query 同步 face 结果
    Backend-->>App: 返回验证结果

    alt Face 成功
        App-->>User: 进入 Address Upload
    else Face 失败 / 锁定 / 超时
        App-->>User: 展示 Face Failed / Loading Failed / lock 提示
    end

    Note over User,AAI: E. POA 与提交审核
    User->>App: 上传地址证明文件
    App->>Backend: 提交 POA 文件和居住国家
    Backend->>DTC: 获取 upload token 并上传文件
    DTC->>AAI: 上传 / 验证 POA
    AAI-->>DTC: webhook 返回 POA 结果
    DTC-->>Backend: webhook / query 同步 POA 结果

    alt POA 提交成功
        Backend-->>App: 返回提交成功
        App-->>User: 展示 KYC Submission Success
    else POA 失败 / 国家不支持
        Backend-->>App: 返回失败原因或 waitlist 分支
        App-->>User: 展示错误 / waitlist / 重试入口
    end
```

### 3.3 流程步骤与业务规则

| 步骤 | 场景 / 规则 | 触发条件 | 责任方 | 系统处理 | 成功结果 | 失败 / 分支结果 | 来源 |
|---|---|---|---|---|---|---|---|
| 1 | KYC Loading 状态判断 | 用户进入 KYC | App / Backend | 查询 KYC 状态和 waitlist 状态 | Pending / failed 进入后续流程 | Under review / Rejected / Approved / APP 来源 waitlist 展示状态 2；网络 / 系统 / 超时走错误页 | AIX KYC PRD 7.2.2 |
| 2 | KYC Start | 状态允许继续 KYC | App | 展示标题、副标题、居住国家、协议、认证按钮 | 用户可选择国家和勾选协议 | 手机号未绑定处理待确认 | AIX KYC PRD 7.2.3 |
| 3 | 国家选择 | 用户点击居住国家 | App / Backend / 配置 | 展示国家列表、搜索、排序、Type 判断 | Phase 1 国家可继续 | phase 2-waitlist 进入 waitlist；Forbiden 隐藏 | AIX KYC PRD 7.2.3.1 |
| 4 | 协议确认 | 用户勾选协议 | App / Backend | 保存同意时间、Declaration 内容和快照 | 按钮可点击，继续 Identity Verify | 获取协议失败 toast；Reverse Solicitation 缺失可触发 DTC 50013 | AIX KYC PRD 7.2.3；Master sub account |
| 5 | Waitlist | 国家不支持或用户被识别为 waitlist | App / Backend | 校验 email，按 userId 加入 waitlist，记录邮箱、国家、来源、设备指纹等 | 返回流程入口，用户无法继续申请 KYC | email 非空 / 格式 / 网络 / 服务器错误 | AIX KYC PRD 7.2.3.2 |
| 6 | Identity Verify | 用户点击相机 | App / Backend / DTC | 判断相机权限，生成 Passport H5 URL | 进入 Identity Scan H5 | 未授权 / 永久拒绝 / DTC 01009 / 01005 | AIX KYC PRD 7.2.4；Master sub account |
| 7 | Identity Scan | 用户扫描护照 | AAI / DTC | AAI H5 完成 Passport OCR，DTC 接收结果 | 成功进入 Face Guide | 失败返回 Identity Verify | AIX KYC PRD 7.2.5 |
| 8 | Face Guide | 用户点击 Continue | App / Backend | 判断 face 锁定规则，获取 passport country，生成 selfie H5 URL | 未锁定进入 Face Scan | 锁定弹窗；网络 / 服务器错误 toast | AIX KYC PRD 7.2.6 |
| 9 | Face Scan | 用户完成活体采集 | AAI / DTC | 外部 H5 完成 Liveness / Face capture | 进入 Face Loading | AAI signatureId 3 次后需重新生成 URL | AIX KYC PRD 7.2.7 |
| 10 | Face Loading | 活体采集结束 | App / Backend / DTC / AAI | 轮询或接收验证结果 | 成功进入 Address Upload | 失败进入 Face Failed；30 秒超时进入 Loading Failed；网络 / 系统错误页 | AIX KYC PRD 7.2.8 |
| 11 | Loading Failed | Face Loading 超过 30 秒无结果 | App | 展示超时失败页 | Retry 后进入 Face Loading 重新提交 | Leave 返回入口 | AIX KYC PRD 7.2.9 |
| 12 | Face Failed | Face / passport / POA 失败 | App / Backend | 按失败原因优先级展示文案 | Try again 重新触发 KYC 流程 | 锁定态展示安全锁弹窗 | AIX KYC PRD 7.2.10 / 9 |
| 13 | Address Upload / POA | Face 成功 | App / Backend / DTC / AAI | 上传 POA 文件，二次判断国家，提交审核 | 成功进入 Submission Success | 文件格式 / 大小 / 服务器 / 国家不支持 / POA 失败 | AIX KYC PRD 7.2.11；Master sub account |
| 14 | KYC Submission Success | POA 提交成功 | App / Backend | 展示提交成功状态 | 用户返回入口，等待审核 | 后续状态通过通知或入口感知 | AIX KYC PRD 7.2.12 |

### 3.4 状态规则

#### 3.4.1 AIX 页面状态

| 状态 | 含义 | 触发条件 | 用户可见表现 | 系统处理 | 可迁移到 | 是否终态 | 来源 |
|---|---|---|---|---|---|---|---|
| `Pending` | 用户仍可继续或重新进入 KYC | 后端返回可继续状态 | Loading 后进入后续流程 | 继续 KYC 流程 | failed / Under review / Approved / Rejected | 否 | AIX KYC PRD |
| `failed` | 上次流程失败，但允许按规则继续 | 上次 KYC 流程失败 | Loading 后进入后续流程 | 根据最新认证结果判断起始页 | Pending / Under review / Approved / Rejected | 否 | AIX KYC PRD |
| `Under review` | 已提交，等待审核 | 用户提交 KYC 成功 | Verification unavailable | 不允许重复提交当前流程 | Approved / Rejected / failed（具体映射待确认） | 否 | AIX KYC PRD |
| `Rejected` | 审核被拒绝 | KYC 审核拒绝 | Verification unavailable | 不允许继续当前 KYC 流程 | 待确认 | 是 / 待确认 | AIX KYC PRD |
| `Approved` | KYC 审核通过 | KYC 审核通过 | Verification unavailable | 不允许重复提交 KYC | 后续 Wallet 能力准入需另行判断 | 是 | AIX KYC PRD |
| `waitlist` | 用户被加入 waitlist | 国家不支持或来源渠道 APP 命中 waitlist | KYC Loading 状态 2 / Waitlist Page | 用户无法继续申请 KYC | 待国家线或运营策略变化 | 否 | AIX KYC PRD |

#### 3.4.2 DTC clientStatus

| Name | ID | Descriptor | AIX 映射边界 |
|---|---:|---|---|
| SUSPENDED | 0 | Suspended | 具体页面映射待确认 |
| PENDING_KYC | 1 | Pending KYC | 可能对应 KYC 未完成或审核中，需后端映射确认 |
| DORMANT | 2 | Dormant | 待确认 |
| REGISTERED | 3 | Self Registered | 待确认 |
| REJECTED | 4 | Rejected | 可能对应 AIX `Rejected`，需确认 |
| OFF_BOARD | 5 | Off Board | 待确认 |
| REFERRER | 8 | Referrer | 待确认 |
| TERMINATED | 9 | Terminated | 待确认 |
| DEACTIVATED | 10 | Deactivated | 待确认 |
| RESTRICTED | 11 | Restricted | 待确认 |
| DELETED | 12 | Deleted | 待确认 |
| FROZEN | 13 | Frozen | 待确认 |
| DROP | 14 | Drop | 待确认 |
| ACTIVATED | 99 | Activated | 可能对应开户完成 / 激活，不能自动等同所有 Wallet 能力可用 |

#### 3.4.3 DTC EKycFileVerifyStatus

适用于 `passportVerifyStatus`、`faceIdVerifyStatus`、`proofOfAddressVerifyStatus`。

| Name | ID | Descriptor | AIX 使用边界 |
|---|---:|---|---|
| UNVERIFIED | 1 | Document verification is not completed | 可作为未完成状态引用 |
| VERIFYING | 2 | Document verification is in progress | 可作为处理中状态引用 |
| VERIFY_SUCCESS | 3 | Document verification succeeded | 表示对应文件 / 认证项成功 |
| VERIFY_FAILURE | 4 | Document verification failed | 表示对应文件 / 认证项失败，失败文案按错误码映射 |

#### 3.4.4 状态生命周期规则

1. 申请单自创建后长期有效。
2. 一旦 OCR、Face 等核心认证在 DTC 侧成功通过，其认证结果长期有效，不因时间推移失效。
3. 只要 passport、face 认证通过，不会再变为失败状态。
4. KYC 人工审核如果 OCR 的 name 等有问题，人工审核可直接修改，不影响 passport / face 状态。
5. 如果 ID 有问题，可直接 KYC reject；passport、face 认证状态也不会变。
6. AIX 页面状态不等同于 DTC clientStatus 或 EKycFileVerifyStatus；映射关系需由后端实现或接口确认。

#### 3.4.5 异步依赖规则

DTC 支持在护照上传还没有验证结果但已有 OCR 信息时继续进行人脸比对。

| 护照最终结果 | 人脸结果处理 |
|---|---|
| 护照通过 | 人脸通过 |
| 护照失败 | 人脸失败 |

### 3.5 业务级异常与失败处理

| 异常场景 | 触发条件 | 错误来源 | 错误码 / 原因 | 用户表现 | 系统处理 | 是否可重试 | 最终状态 |
|---|---|---|---|---|---|---|---|
| KYC 状态不可继续 | 状态为 Under review / Rejected / Approved | Backend | KYC 状态 | Verification unavailable | 阻止继续提交 | 否 | 保持当前状态 |
| APP 来源 waitlist 拦截 | 用户在 waitlist 中 | Backend | waitlist | Verification unavailable / Waitlist Page | 阻止继续 KYC | 否 | waitlist |
| KYC Loading 网络异常 | 查询状态网络异常 | App / Network | 网络异常 | Network Error Page | 停留错误页 | 是 | 未变更 |
| KYC Loading 系统异常 | 后端系统异常 | Backend | 系统异常 | Server Error Page | 停留错误页 | 是 | 未变更 |
| KYC Loading 超时 | 30 秒无结果 | Backend / Network | Timeout | Loading Failed Page | 用户可 Retry | 是 | 未变更 |
| 协议获取失败 | 后端无法获取协议 | Backend | 获取协议失败 | Toast | 阻止继续 | 是 | 未变更 |
| Reverse Solicitation 缺失 | 国家要求反向招揽声明但未传 | DTC | 50013 | 按接口错误处理 | 阻止生成验证 URL | 是 | 未变更 |
| Passport URL 生成失败 | DTC 返回错误 | DTC | 01009 / 01005 / 其他 | Toast 或错误提示 | 阻止进入 H5 | 是 / 视错误而定 | 未变更 |
| Passport OCR 失败 | AAI / DTC 返回失败 | AAI / DTC | passport error code | 回 Identity Verify 或 Face Failed 原因 | 记录失败原因 | 是 | failed / 待映射 |
| Face 失败 | DTC 返回 face result=fail | DTC / AAI | face error code | Face Failed Page | 计入 face 失败次数 | 是，未锁定时 | failed |
| Face 失败 5 次 | 24 小时内 face fail 5 次 | Backend / DTC | 安全限制 | Too many attempts | 锁 20 分钟 | 否，锁定期不可重试 | lock |
| Face 失败 10 次 | 24 小时内 face fail 10 次 | Backend / DTC | 安全限制 | Too many attempts | 锁 24 小时 | 否，锁定期不可重试 | lock |
| Face 接口连续发起 20 次 | 24 小时内接口层连续发起 20 次 | Backend | 风控限制 | Too many attempts | 锁 20 分钟 | 否，锁定期不可重试 | lock |
| Face Loading 超时 | 30 秒无结果 | Backend / DTC / AAI | Timeout | Loading Failed Page | Retry 后重新提交 | 是 | 未变更 |
| POA 文件格式错误 | 上传非 JPG/JPEG/PNG/PDF | App | 文件格式 | Toast | 阻止上传 | 是 | 未变更 |
| POA 文件过大 | 单文件超 16MB | App | 文件大小 | Toast | 阻止上传 | 是 | 未变更 |
| POA 上传失败 | 服务器或 DTC 上传失败 | Backend / DTC | 14004 / 14005 / Server error | Toast | 阻止继续 | 是 | 未变更 |
| POA 国家不匹配 / 不支持 | POA 国家或居住国家不符合规则 | DTC / AAI | POA error code | Face Failed / POA 错误文案 | 记录失败原因 | 是 / 视状态 | failed |
| webhook 延迟或未返回 | 外部验证结果未及时到达 | DTC / AAI | 异步延迟 | Loading 或超时页 | query 兜底 / 轮询 | 是 | 未变更 |

---

## 4. 页面与交互说明

### 4.1 页面关系总览图

```mermaid
flowchart LR
  Loading[KYC Loading Page]
  Unavailable[Verification unavailable]
  Start[KYC Start Page]
  Country[Select Residence Country Page]
  Waitlist[Waitlist Page]
  IdentityVerify[Identity Verify Page]
  IdentityScan[Identity Scan H5]
  FaceGuide[Face Guide Page]
  FaceScan[Face Scan H5]
  FaceLoading[Face Loading Page]
  LoadingFailed[Loading Failed Page]
  FaceFailed[Face Failed Page]
  AddressUpload[Address Upload Page]
  Success[KYC Submission Success Page]
  NetworkError[Network Error Page]
  ServerError[Server Error Page]
  Entry[业务流程入口页]

  Loading -->|Pending / failed| Start
  Loading -->|Under review / Rejected / Approved / APP waitlist| Unavailable
  Loading -->|Network error| NetworkError
  Loading -->|Server error| ServerError
  Loading -->|30s timeout| LoadingFailed

  Start -->|Select country| Country
  Country -->|Selected| Start
  Start -->|Unsupported country| Waitlist
  Start -->|Agreement checked + supported country| IdentityVerify

  Waitlist -->|Submit success| Entry
  IdentityVerify -->|Camera allowed| IdentityScan
  IdentityScan -->|Success| FaceGuide
  IdentityScan -->|Failure| IdentityVerify

  FaceGuide -->|Continue / not locked| FaceScan
  FaceGuide -->|Locked| Entry
  FaceScan -->|Capture completed| FaceLoading
  FaceLoading -->|Success| AddressUpload
  FaceLoading -->|Failure| FaceFailed
  FaceLoading -->|30s timeout| LoadingFailed
  FaceLoading -->|Network error| NetworkError
  FaceLoading -->|Server error| ServerError

  LoadingFailed -->|Retry| FaceLoading
  LoadingFailed -->|Leave| Entry
  FaceFailed -->|Try again| Loading
  FaceFailed -->|Close| Entry
  AddressUpload -->|Country unsupported| Waitlist
  AddressUpload -->|Submit success| Success
  Success -->|Back home| Entry
```

### 4.2 KYC Loading Page

截图暂缺，视觉以 Figma 为准。

| 区块 | 内容 |
|---|---|
| 页面类型 | 状态页 |
| 页面目标 | 在进入 KYC 时判断用户是否可继续流程。 |
| 入口 / 触发 | 用户从业务入口发起 KYC。 |
| 展示内容 | 状态 1：`loading...`；状态 2：`Verification unavailable` 及说明文案。 |
| 用户动作 | 可点击关闭按钮；状态 2 可点击 Back。 |
| 系统处理 / 责任方 | AIX Backend 查询 KYC 状态与 waitlist 状态；AIX App 展示分流结果。 |
| 元素 / 状态 / 提示规则 | Under review / Rejected / Approved 或 APP 来源 waitlist 展示状态 2；Pending / failed 进入后续流程。 |
| 成功流转 | 可继续时进入 KYC Start 或后续流程。 |
| 失败 / 异常流转 | Network Error、Server Error、Loading Failed。 |
| 备注 / 边界 | waitlist 是页面级拦截，不是弹窗继续。 |

### 4.3 KYC Start Page

截图暂缺，视觉以 Figma 为准。

| 区块 | 内容 |
|---|---|
| 页面类型 | 主页面 |
| 页面目标 | 让用户确认开始身份验证、选择居住国家并同意协议。 |
| 入口 / 触发 | KYC Loading 判断可继续后进入。 |
| 展示内容 | title、subtitle、居住国家、协议、立即认证按钮。 |
| 用户动作 | 选择国家、勾选协议、点击立即认证、返回。 |
| 系统处理 / 责任方 | App 展示国家和协议；Backend 保存协议同意、快照、Reverse Solicitation 信息。 |
| 元素 / 状态 / 提示规则 | 协议未勾选按钮禁用；已勾选按钮可点；已绑定手机号不展示额外 toast。 |
| 成功流转 | 支持国家进入 Identity Verify。 |
| 失败 / 异常流转 | 不支持国家进入 waitlist；协议获取失败 toast。 |
| 备注 / 边界 | 手机号未绑定处理见 GAP-KYC-PHONE-001。 |

#### 4.3.1 协议元素明细

| 元素 / 状态 / 提示 | 类型 | 触发 / 展示条件 | 交互 / 校验规则 | 成功结果 | 失败 / 提示 | 后续流转 | 文案来源 |
|---|---|---|---|---|---|---|---|
| Terms of service | Link / Checkbox | 页面展示 | 单击可勾选，无需强制阅读；链接至 DTC Terms | 保存同意时间 | 获取协议失败 toast | 可继续 | PRD / DTC 链接 |
| Privacy Policy | Link / Checkbox | 页面展示 | 单击可勾选，无需强制阅读；链接至 DTC Privacy | 保存同意时间 | 获取协议失败 toast | 可继续 | PRD / DTC 链接 |
| Declaration of Reverse Solicitation | Popup / Checkbox | 用户点击协议 | 需强制阅读；点击 `I agree` 后勾选；关闭则不同意 | 保存协议内容和同意时间 | 未同意不可继续 | 影响 DTC reverseSolicitation 入参 | PRD / Master sub account |
| 立即认证按钮 | Button | 协议状态变化 | 未勾选禁用；勾选后启用 | 进入国家判断 | 不支持国家 waitlist | Identity Verify / Waitlist | PRD |

### 4.4 Select Residence Country Page

截图暂缺，视觉以 Figma 为准。

| 区块 | 内容 |
|---|---|
| 页面类型 | 选择页 |
| 页面目标 | 让用户选择居住国家 / 地区。 |
| 入口 / 触发 | KYC Start 或 Address Upload 点击 Residence。 |
| 展示内容 | 国家列表、搜索、支持国家和不可支持国家。 |
| 用户动作 | 搜索、选择国家、关闭返回。 |
| 系统处理 / 责任方 | App 根据配置展示国家；禁止国家隐藏。 |
| 元素 / 状态 / 提示规则 | 默认 IP 检测国家；检测不到默认 SG；按首字母排序。 |
| 成功流转 | 选择国家后返回上一级页面。 |
| 失败 / 异常流转 | 不适用。 |
| 备注 / 边界 | 国家线存在版本口径冲突，见 GAP-KYC-COUNTRY-001。 |

### 4.5 Waitlist Page

截图暂缺，视觉以 Figma 为准。

| 区块 | 内容 |
|---|---|
| 页面类型 | 拦截 / 提交页 |
| 页面目标 | 对不支持国家或 waitlist 用户收集邮箱，并阻止继续 KYC。 |
| 入口 / 触发 | 国家为 phase 2-waitlist，或 KYC Loading 命中 waitlist。 |
| 展示内容 | email 输入框、Join waitlist 按钮、关闭按钮。 |
| 用户动作 | 输入 email、提交、关闭。 |
| 系统处理 / 责任方 | Backend 按 userId 加入 waitlist，记录 email、国家、来源、提交时间、设备指纹，并推送数仓。 |
| 元素 / 状态 / 提示规则 | email 最长 103 字符；空值和格式校验；按钮根据输入状态禁用 / 启用。 |
| 成功流转 | 提交成功后返回业务入口页，用户无法继续申请 KYC。 |
| 失败 / 异常流转 | 网络异常 / 后端服务器错误 toast。 |
| 备注 / 边界 | waitlist 是页面级拦截。 |

### 4.6 Identity Verify Page / Identity Scan H5

截图暂缺，视觉以 Figma / AAI H5 为准。

| 区块 | 内容 |
|---|---|
| 页面类型 | 主页面 + 外部 H5 |
| 页面目标 | 引导用户上传 / 扫描护照完成 Passport OCR。 |
| 入口 / 触发 | KYC Start 支持国家且协议已同意。 |
| 展示内容 | 标题、副标题、上传 / 相机按钮、权限弹窗。 |
| 用户动作 | 点击相机、授权、进入 H5 扫描护照。 |
| 系统处理 / 责任方 | App 判断相机权限；Backend / DTC 生成 Passport H5 URL；AAI 完成 OCR。 |
| 元素 / 状态 / 提示规则 | 未授权弹窗；永久拒绝 open settings；DTC 01009 / 01005 toast。 |
| 成功流转 | Identity Scan 成功进入 Face Guide。 |
| 失败 / 异常流转 | Identity Scan 失败返回 Identity Verify。 |
| 备注 / 边界 | App 不判断 AAI 内部识别逻辑。 |

### 4.7 Face Guide / Face Scan / Face Loading

截图暂缺，视觉以 Figma / AAI H5 为准。

| 区块 | 内容 |
|---|---|
| 页面类型 | 主页面 + 外部 H5 + 状态页 |
| 页面目标 | 完成活体采集和人脸比对。 |
| 入口 / 触发 | Passport OCR 成功后进入。 |
| 展示内容 | Face Guide 说明、Continue 按钮、锁定弹窗、Face Loading。 |
| 用户动作 | 点击 Continue、完成 H5 活体采集、等待结果。 |
| 系统处理 / 责任方 | Backend 判断锁定、获取 passport country、生成 selfie H5 URL、轮询或接收结果。 |
| 元素 / 状态 / 提示规则 | 5 次锁 20 分钟；10 次锁 24 小时；接口连续 20 次锁 20 分钟；30 秒超时进入 Loading Failed。 |
| 成功流转 | Face 成功进入 Address Upload。 |
| 失败 / 异常流转 | Face Failed、Loading Failed、Network Error、Server Error。 |
| 备注 / 边界 | 同一 signatureId 最多重试 3 次，重来需重新 generate-url。 |

### 4.8 Loading Failed Page

截图暂缺，视觉以 Figma 为准。

| 区块 | 内容 |
|---|---|
| 页面类型 | 错误页 |
| 页面目标 | 处理 Face Loading 超过 30 秒无结果。 |
| 入口 / 触发 | Face Loading 等待超过 30 秒。 |
| 展示内容 | 加载失败提示、Retry、返回。 |
| 用户动作 | Retry 或 Leave。 |
| 系统处理 / 责任方 | App 重新进入 Face Loading 并重新提交。 |
| 元素 / 状态 / 提示规则 | 返回按钮使用通用挽留弹窗。 |
| 成功流转 | Retry 进入 Face Loading。 |
| 失败 / 异常流转 | Leave 返回入口。 |
| 备注 / 边界 | Retry 不是返回 Face Scan。 |

### 4.9 Face Failed Page

截图暂缺，视觉以 Figma 为准。

| 区块 | 内容 |
|---|---|
| 页面类型 | 失败页 |
| 页面目标 | 展示人脸 / 护照 / POA 失败原因，并提供重试入口。 |
| 入口 / 触发 | Face Loading 验证失败、Face Scan 失败、POA 失败等。 |
| 展示内容 | 固定主文案、动态原因文案、Try again、关闭按钮。 |
| 用户动作 | Try again 或关闭。 |
| 系统处理 / 责任方 | Backend 返回失败原因；App 按优先级展示映射文案。 |
| 元素 / 状态 / 提示规则 | passport 与 face 均失败时优先 passport；锁定态展示安全弹窗。 |
| 成功流转 | 正常态 Try again 重新触发 KYC 流程。 |
| 失败 / 异常流转 | 锁定态确认后返回入口。 |
| 备注 / 边界 | 错误文案来源为 PRD 第 9 章映射表。 |

### 4.10 Address Upload Page

截图暂缺，视觉以 Figma 为准。

| 区块 | 内容 |
|---|---|
| 页面类型 | 主页面 |
| 页面目标 | 收集用户地址证明文件并提交 POA 审核。 |
| 入口 / 触发 | Face 验证成功。 |
| 展示内容 | Residence、文件上传区、Continue 按钮、文件状态。 |
| 用户动作 | 修改 Residence、上传 / 删除 / 预览文件、点击 Continue。 |
| 系统处理 / 责任方 | App 校验文件；Backend 获取 DTC upload token 并上传 POA；DTC / AAI 审核。 |
| 元素 / 状态 / 提示规则 | JPG/JPEG/PNG/PDF；16MB；只能上传一份；上传中 / 已上传状态。 |
| 成功流转 | 提交成功进入 KYC Submission Success。 |
| 失败 / 异常流转 | 文件错误、上传失败、国家不支持、服务器错误、POA 失败。 |
| 备注 / 边界 | POA continue 后跳转存在源文档冲突，见 GAP-KYC-POA-002。 |

### 4.11 KYC Submission Success Page

截图暂缺，视觉以 Figma 为准。

| 区块 | 内容 |
|---|---|
| 页面类型 | 成功页 |
| 页面目标 | 告知用户 KYC 资料已提交，等待审核结果。 |
| 入口 / 触发 | POA 提交成功。 |
| 展示内容 | 固定成功文案、返回首页按钮。 |
| 用户动作 | 点击返回首页。 |
| 系统处理 / 责任方 | App 关闭当前 KYC 流程。 |
| 元素 / 状态 / 提示规则 | 返回首页按钮返回业务流程入口页。 |
| 成功流转 | 返回入口，后续通过状态或通知感知结果。 |
| 失败 / 异常流转 | 不适用。 |
| 备注 / 边界 | 通知规则待 Notification 来源核验。 |

---

## 5. 字段、接口与数据

### 5.1 字段 / 接口 / 数据总表

| 类型 | 名称 | 所属系统 | 来源 | 用途 | 规则 / 输入输出 | 异常处理 |
|---|---|---|---|---|---|---|
| 字段 | `externalId` | AIX / DTC | AIX 生成 / DTC 接口 | 关联用户 KYC 结果 | URL 生成、结果查询、OCR info、POA upload 均使用 | 格式错误返回 DTC `50004` |
| 字段 | `requestId` | DTC | DTC 返回 | 追踪单次认证请求 | URL 生成、webhook、POA upload 返回 | 缺失时无法定位请求，需后端处理 |
| 字段 | `clientStatus` | DTC | 查询结果 / webhook | 表示 DTC 客户状态 | 枚举见 3.4.2 | 与 AIX 页面状态映射待确认 |
| 字段 | `passportVerifyStatus` | DTC | 查询结果 / webhook | 表示护照认证状态 | 使用 EKycFileVerifyStatus | 失败时看 `passportVerifyCode` |
| 字段 | `faceIdVerifyStatus` | DTC | 查询结果 / webhook | 表示人脸认证状态 | 使用 EKycFileVerifyStatus | 失败时看 `faceIdVerifyCode` |
| 字段 | `proofOfAddressVerifyStatus` | DTC | 查询结果 / webhook | 表示 POA 审核状态 | 使用 EKycFileVerifyStatus | 失败时看 `proofOfAddressVerifyCode` |
| 字段 | `reverseSolicitation` | AIX / DTC | 协议确认 / DTC 接口 | 标记反向招揽声明 | 需要时传 `T`，否则空或 `F` | 缺失可能返回 `50013` |
| 数据 | 协议同意时间 | AIX | 用户勾选协议 | 合规留痕 | ToS / Privacy / Declaration 均需保存同意并提交时间 | 保存失败应阻止继续 |
| 数据 | Declaration 协议内容 | AIX | 用户强制阅读并同意 | 合规留痕 | 需要保存协议内容和同意时间 | 保存失败应阻止继续 |
| 数据 | 协议快照 | AIX | 提交成功 | 合规留痕 | 生成不可更改快照并与用户账户绑定 | 保存失败待后端确认 |
| 数据 | waitlist email | AIX | 用户输入 | waitlist 运营与通知 | 最长 103 字符，格式校验 | 空 / 格式错误提示 |
| 数据 | 设备指纹 ID | AIX | App / 设备 | waitlist 落库和数仓分析 | 与 userId、email、国家、来源、提交时间一并记录 | 获取失败策略待确认 |
| 接口 | `POST /openapi/v1/ekyc/get-verification-url` | DTC | Master sub account | 获取 Passport / Selfie H5 URL | 入参含 redirectUrl、externalId、type、country、language、email、mobile、reverseSolicitation | 错误码见 5.2 |
| 接口 | `GET /openapi/v1/ekyc/verification-result/{externalId}` | DTC | Master sub account | 查询 KYC 结果 | 返回 clientStatus、nationality、country、三类 verifyStatus/code | 查询失败按系统异常处理 |
| 接口 | `KYC_VERIFICATION` webhook | DTC | Master sub account | 异步同步 KYC 结果 | 返回 externalId、clientStatus、三类状态和 code、requestId | webhook 延迟时 query 兜底 |
| 接口 | `GET /openapi/v1/ekyc/passport-info/{externalId}` | DTC | Master sub account | 查询护照 OCR 信息 | 返回 fullName、idNumber、DOB、gender、nationality | 查询失败待后端处理 |
| 接口 | `GET /openapi/v1/ekyc/poa-info/{externalId}` | DTC | Master sub account | 查询 POA OCR 信息 | 返回 address、country、state、city、postal | 查询失败待后端处理 |
| 接口 | `POST /openapi/v1/file/get-upload-token` | DTC | Master sub account | 获取 POA 上传 token | documentType=3，externalId，需要签名 | token 5 分钟有效，只能用一次 |
| 接口 | `POST /openapi/v1/ekyc/upload-file` | DTC | Master sub account | 上传 POA 文件 | token、fileContent、countryOfResidence | 14004 / 14005 |
| 日志 / 埋点 | KYC 页面曝光与错误 | AIX | 当前文档未明确 | QA / 运营 / 风控分析 | 待确认是否需要埋点 | GAP 待补 |

### 5.2 `get-verification-url` 错误码

| errCode | 含义 | 处理建议 |
|---|---|---|
| `00010` | Invalid parameters | 参数错误，阻止继续 |
| `00025` | Services unavailable in country or region | 国家 / 地区不可用，进入 waitlist 或提示 |
| `01009` | Mobile number already exists | Toast：`Mobile number already exists.` |
| `01005` | The email address is in use | Toast：`The email address is in use.` |
| `01049` | Account is invalid | 展示账户不可用提示，具体页面待确认 |
| `50001` | Mobile number format invalid | 参数错误 |
| `50002` | Email format invalid | 参数错误 |
| `50003` | Country of residence format invalid | 参数错误 |
| `50004` | externalId format invalid | 参数错误 |
| `50005` | targetKycLevel format invalid | 参数错误 |
| `50006` | Mobile number exists | 参数 / 账户冲突 |
| `50007` | Applicant currently undergoing verification | 用户正在认证中，应进入不可重复提交或状态页 |
| `50008` | Email exists | 邮箱冲突 |
| `50013` | Reverse solicitation not declared by end user | 反向招揽未声明，应阻止继续并要求补声明 |
| `59999` | Internal error | 系统错误 |

### 5.3 错误码与前端文案映射

#### Passport / Document Verification

| code | AIX 前端提示文案 |
|---|---|
| `ID_FORGERY_DETECTED` | We couldn't verify this document. Please upload a valid document. |
| `NO_SUPPORTED_CARD` | This document type isn't supported. Please upload a valid document. |
| `CARD_TYPE_MISMATCH` | Document type doesn't match your selection. Please upload a valid document. |
| `CARD_LOW_QUALITY_IMAGE` | Image is too blurry or dark. Please upload a well-lit, clear photo. |
| `INCOMPLETED_CARD` | Document appears incomplete. Please ensure the full document is visible. |
| `CARD_INFO_MISMATCH` | Document doesn't match your submitted details. Please upload a valid document. |
| `TOO_MANY_CARDS` | Multiple documents detected. Please upload one at a time. |
| `CARD_NOT_FOUND` | No document detected. Please upload a clear image of your document. |
| `OCR_NO_RESULT` | Couldn't read your document. Please upload a clear image of your document. |
| `PARAMETER_ERROR` | Something went wrong. Please try again. |
| `USER_TIMEOUT` | Your session timed out. Please try again. |
| `ERROR` | Something went wrong. Please try again. |
| `NO_SUPPORTED_CARD_CUSTOMIZED` | This document type isn't supported. Please upload a valid document. |
| `NO_FACE_DETECTED` | No face detected on document. Please upload a clear image of your document. |
| `Duplicated` | This ID number has already been used. Please upload a different document. |
| `DEFAULT` | We couldn't verify this document. Please upload a clear image of your document. |

#### Face Comparison

| code | AIX 前端提示文案 |
|---|---|
| `NO_FACE_DETECTED_FROM_PASSPORT` | No face was detected in the passport image. Please upload a clear passport photo. |
| `NO_FACE_DETECTED_FROM_LIVENESS_DETECTION` | No face was detected during facial verification. Please ensure your face is clearly visible and try again. |
| `LOW_QUALITY_FACE_FROM_PASSPORT` | The face in the passport image is unclear. Please upload a clearer photo. |
| `LOW_QUALITY_FACE_FROM_LIVENESS_DETECTION` | The facial image quality is low. Please ensure good lighting and avoid movement. |
| `FACE_NOT_MATCH` | The facial scan does not match the passport photo. Please try again. |
| `ERROR` | The facial verification could not be completed at this time. Please try again later. |
| `DEFAULT` | The facial verification could not be completed. Please try again. |

#### POA

| code | AIX 前端提示文案 |
|---|---|
| `The identity document could not be verified` | The name on your proof of address does not match your submitted details. Please review and upload again. |
| `NOT_WITHIN_6_MONTHS` | Your proof of address must be issued within the last 6 months. Please upload a valid document. |
| `WRONG_DOCUMENT_TYPE` | This proof of address type is not accepted. Please upload a valid proof of address. |
| `OTHERS` | Your proof of address could not be verified. Please review and upload again. |
| `NOT_REQUIRED_NOT_RELEVANT` | The uploaded document is not a valid proof of address. Please upload an acceptable document. |
| `DUPLICATED` | A duplicate proof of address was detected. Please upload a different document. |
| `NOT_ACCEPTED` | Your proof of address was not accepted. Please upload a valid document. |
| `EXPIRED` | Your proof of address has expired. Please upload a valid and recent document. |
| `COUNTRY_OF_RESIDENCE_MISMATCH` | The country on your proof of address does not match your submitted details. Please review and upload again. |
| `DOCUMENT_UNCLEAR` | Your proof of address image is unclear. Please upload a clearer copy. |
| `EDITED_SCREENSHOT_NOT_ACCEPTED` | Edited or altered proof of address documents are not accepted. Please upload the original document. |
| `NOT_SUPPORTED_COUNTRY` | Proof of address documents from this country are not supported. Please upload a valid document. |
| `DUPLICATED_ID_NUMBER` | The identification number on your proof of address has already been used. Please review and upload a valid document. |
| `FRAUD_RISK` | Your proof of address could not be verified. Please ensure the information is accurate and upload again. |
| `PROOF_DOCUMENT_MATCHING_FAILED` | The information on your proof of address could not be matched. Please review and upload again. |
| `DATA_VERIFICATION_FAILED` | The details on your proof of address could not be verified. Please review and try again. |
| `DOCUMENT_INCOMPLETE` | Your proof of address is incomplete. Please ensure the full document is visible and upload again. |
| `POOR_IMAGE_QUALITY` | The image quality of your proof of address is too low. Please upload a clearer photo. |
| `DOCUMENT_EXPIRED` | Your proof of address has expired. Please upload a valid and recent document. |
| `DOCUMENT_UNSUPPORTED_OR_INVALID` | This proof of address document is not supported. Please upload a valid document. |
| `USER_SUBMISSION_FAILED` | Your proof of address submission could not be completed. Please try again. |
| `PROCESS_INCOMPLETE` | The proof of address verification process was not completed. Please try again. |
| `ADDRESS_NOT_FOUND` | The address on your proof of address could not be verified. Please upload a valid document. |
| `DEFAULT` | Your proof of address could not be verified. Please ensure it is clear and valid, then try again. |

---

## 6. 通知规则

历史文档中记录 KYC Approved / Rejected / Failed 可能触发 Email / in-app notification / push，但本轮附件未完整提供 Notification 模板、参数、跳转目标和失败补发策略。

| 触发事件 | 通知渠道 | 通知对象 | 文案 / 模板 | 跳转目标 | 失败 / 补发规则 |
|---|---|---|---|---|---|
| KYC Approved | Email / Push / In-app | KYC 用户 | 待 `common/notification.md` 或 Notification 原文确认 | 待确认 | ALL-GAP-045 / GAP-KYC-NOTIFICATION-001 |
| KYC Rejected | Email / Push / In-app | KYC 用户 | 待 `common/notification.md` 或 Notification 原文确认 | 待确认 | ALL-GAP-045 / GAP-KYC-NOTIFICATION-001 |
| KYC Failed | Email / Push / In-app | KYC 用户 | 待 `common/notification.md` 或 Notification 原文确认 | 待确认 | ALL-GAP-045 / GAP-KYC-NOTIFICATION-001 |

边界：KYC Approved 通知不等同于 DTC Sub Account 一定已创建成功，也不自动代表所有 Wallet 能力均可用。

---

## 7. 权限 / 合规 / 风控

| 类型 | 规则 | 影响 | 来源 |
|---|---|---|---|
| 系统权限 | Identity Verify 点击相机前判断相机权限；未授权弹窗；永久拒绝 open settings | 影响是否进入 AAI H5 护照扫描 | AIX KYC PRD 7.2.4 |
| 合规 | ToS / Privacy 保存用户同意并提交时间 | 合规留痕 | AIX KYC PRD 7.2.3 |
| 合规 | Reverse Solicitation Declaration 需强制阅读，保存协议内容和同意时间 | 合规留痕，并影响 DTC `reverseSolicitation` 入参 | AIX KYC PRD 7.2.3；Master sub account |
| 合规 | 提交成功后生成不可更改协议快照并绑定账户 | 合规留痕 | AIX KYC PRD 7.2.3 |
| 国家合规 | Phase 1 / phase 2-waitlist / Forbiden 控制国家展示和流程准入 | 决定是否允许 KYC 或进入 waitlist | AIX KYC PRD 7.2.3.1 |
| 风控 | 24 小时内 face 失败 5 次锁 20 分钟 | 限制频繁失败重试 | AIX KYC PRD 7.2.6 |
| 风控 | 24 小时内 face 失败 10 次锁 24 小时 | 限制高风险重试 | AIX KYC PRD 7.2.6 |
| 风控 | 24 小时内接口层连续发起 20 次锁 20 分钟 | 限制接口滥用 | AIX KYC PRD 7.2.6 |
| 风控 | AAI 同一 `signatureId` 最多重试 3 次 | 控制活体 H5 重试 | AIX KYC PRD 7.2.7 |
| 合规 / 风控 | POA 文件真实性、篡改、有效期、国家白名单、姓名一致性审核 | 决定 POA 是否通过 | AIX KYC PRD 7.2.11 |
| 隐私 / 数据 | waitlist 记录 userId、email、国家、来源、提交时间、设备指纹并推送数仓 | 运营分析与后续准入 | AIX KYC PRD 7.2.3.2 |
| 账户边界 | POA success 设计流程包含 create sub account | 影响后续 DTC Sub Account 上下文 | Master sub account |

---

## 8. 待确认事项

| 问题 | 影响范围 | 当前处理 | 是否阻塞验收 | 建议确认人 |
|---|---|---|---|---|
| GAP-KYC-COUNTRY-001：VN/PH/AU、PH+SG、PH/AU/VN/SG 三种国家线口径如何对应最终线上版本 | 国家选择、waitlist、POA、验收测试 | 带版本上下文记录，不写死单一口径 | 是 | 产品 Owner / 合规 / 后端 |
| GAP-KYC-SG-001：SG 是否支持 DTC POA upload-file 的 `countryOfResidence` | SG 用户 POA 提交 | 前端版本口径包含 SG，DTC 示例未包含 SGP | 是 | DTC / 后端 / 产品 |
| GAP-KYC-PHONE-001：手机号未绑定时完整处理流程 | KYC Start 入口 | 当前只确认已绑定直接进入 Start，未绑定流程引用 Account / Security 待确认 | 是 | Account / Security PM / 后端 |
| GAP-KYC-POA-001：POA 有效期是 3 个月还是 6 个月 | POA 审核、QA 验收、错误文案 | PRD POA 知识点写 3 个月，错误文案写 6 个月 | 是 | 合规 / DTC / 产品 |
| GAP-KYC-POA-002：POA continue 后支持国家是进入 Submission Success 还是 Identity Verify | Address Upload 流转 | 当前按提交成功进入 Submission Success，保留源文档冲突 | 是 | 产品 Owner / UI / QA |
| GAP-KYC-POA-003：POA failed 时 DTC 更新 passportVerifyStatus 还是 proofOfAddressVerifyStatus | 状态更新、失败展示 | Master 方案文本疑似笔误 | 是 | DTC / 后端 |
| GAP-KYC-ERROR-001：PRD `Duplicated` 与 DTC `DUPLICATED_ID_NUMBER` / `DUPLICATED_USER` 的映射关系 | 错误码映射 | 保留 PRD 映射，原始码映射待确认 | 否 | 后端 / DTC |
| GAP-KYC-KUN-001：KUN 在 AIX → DTC → AAI 链路中的实际位置 | 系统责任边界 | PRD 提到 KUN，Master 方案主要为 AIX → DTC → AAI | 否 | 架构 / 后端 |
| GAP-KYC-NOTIFICATION-001：KYC 通知规则来源与模板细节 | 通知验收 | 保留历史提示，模板待 Notification 模块确认 | 否 | Notification PM / QA |
| GAP-KYC-WALLET-001：WalletAccount / WalletConnect 相关字段与准入 | Wallet 能力准入 | 依赖本轮未上传 DTC Wallet OpenAPI 文档，暂不扩写 | 否 | Wallet PM / DTC / 后端 |
| GAP-KYC-TRACKING-001：是否需要 KYC 埋点、日志、审计事件 | QA / 运营 / 风控分析 | 当前 PRD 未明确 | 否 | 数据 / 风控 / 产品 |

---

## 9. 验收标准 / 测试场景

### 9.1 验收标准

| 验收场景 | 验收标准 |
|---|---|
| 正常流程 | 支持国家用户可从 KYC Loading 进入 Start，选择国家、勾选协议，完成 Passport、Face、POA，并进入 Submission Success。 |
| KYC Loading 状态分流 | Pending / failed 可继续；Under review / Rejected / Approved 展示 Verification unavailable；APP 来源 waitlist 命中时不可继续。 |
| 国家选择 | IP 检测默认国家；检测不到默认 SG；国家可搜索、排序；Forbiden 国家隐藏；phase 2-waitlist 进入 waitlist。 |
| 协议 | 未勾选协议按钮禁用；ToS / Privacy 保存同意时间；Declaration 强制阅读并保存内容与同意时间；提交成功生成快照。 |
| Reverse Solicitation | 需要反向招揽声明的国家，DTC URL 生成入参应传 `reverseSolicitation=T`；缺失时能处理 `50013`。 |
| Waitlist | email 空 / 格式错误 / 超长均按规则处理；提交成功后 userId 加入 waitlist，记录 email、国家、来源、提交时间、设备指纹。 |
| 相机权限 | 已授权进入 AAI H5；未授权弹窗；永久拒绝可 open settings。 |
| Passport OCR | 扫描成功进入 Face Guide；扫描失败返回 Identity Verify；DTC 01009 / 01005 显示对应 toast。 |
| Face Guide | 5 次失败锁 20 分钟，10 次失败锁 24 小时，接口连续 20 次锁 20 分钟；人脸通过后清零。 |
| Face country 参数 | Continue 时后端获取 passport country；存在则使用，不存在默认 `sg`；前端调用 AAI H5 时传入 country。 |
| Face Scan | 同一 `signatureId` 最多重试 3 次；需要重来时重新 generate-url。 |
| Face Loading | 成功进入 Address Upload；失败进入 Face Failed；30 秒无结果进入 Loading Failed；网络 / 系统异常进入对应错误页。 |
| Loading Failed | Retry 后进入 Face Loading 重新提交；Leave 返回业务入口。 |
| Face Failed | 按 passport、face、POA 错误码映射展示文案；passport 与 face 均失败时优先展示 passport 原因。 |
| Address Upload | 支持 JPG/JPEG/PNG/PDF，单文件 16MB，只能上传一份；上传中可取消；已上传可删除和预览。 |
| POA 提交 | 支持国家提交成功后进入 Submission Success；不支持国家进入 waitlist；网络 / 服务器异常展示对应 toast。 |
| KYC Submission Success | 点击返回首页后关闭当前 KYC 流程并返回业务入口。 |
| DTC API | get-verification-url、verification-result、webhook、passport-info、poa-info、POA upload token / upload-file 字段与错误处理符合文档。 |
| 状态模型 | AIX 页面状态、DTC clientStatus、EKycFileVerifyStatus 不混用；未确认映射不写死。 |
| 通知 | 若启用通知，Approved / Rejected / Failed 的渠道、模板、跳转和补发规则需以 Notification 模块确认。 |
| 数据 / 埋点 | 协议、waitlist、requestId、externalId、verifyStatus / verifyCode 保存和使用规则需可测试；埋点待确认。 |

### 9.2 测试场景矩阵

| 场景 | 前置条件 | 用户操作 | 预期页面表现 | 预期系统结果 | 是否必测 |
|---|---|---|---|---|---|
| 支持国家完整 KYC 成功 | 用户状态 Pending，国家为支持国家 | 完成 Start、Passport、Face、POA | 进入 Submission Success | 产生 KYC 结果，等待审核 | 是 |
| Under review 不可继续 | 用户状态 Under review | 进入 KYC | Verification unavailable | 不发起新 KYC | 是 |
| Rejected 不可继续 | 用户状态 Rejected | 进入 KYC | Verification unavailable | 不发起新 KYC | 是 |
| Approved 不可继续 | 用户状态 Approved | 进入 KYC | Verification unavailable | 不发起新 KYC | 是 |
| APP waitlist 拦截 | 用户在 waitlist 且来源 APP | 进入 KYC | Loading 状态 2 / 不可继续 | 不进入 Start | 是 |
| 国家 phase 2-waitlist | 用户选择不支持国家 | 点击立即认证 | waitlist 拦截 | 可进入 Waitlist Page | 是 |
| Forbidden 国家 | 国家配置为 Forbiden | 打开国家列表 | 不展示该国家 | 用户不可选择 | 是 |
| 协议未勾选 | Start Page | 不勾选协议 | 按钮禁用 | 不可继续 | 是 |
| Declaration 未强制阅读 | Start Page | 尝试直接勾选 Declaration | 弹出强制阅读 | 不保存同意 | 是 |
| Reverse Solicitation 50013 | 国家要求反向招揽但未传 T | 点击认证 | 错误提示 / 阻止继续 | DTC 返回 50013 被处理 | 是 |
| Waitlist email 空 | Waitlist Page | 不输入 email | 提示空值 / 按钮禁用 | 不提交 | 是 |
| Waitlist email 格式错误 | Waitlist Page | 输入错误 email | 提示格式错误 | 不提交 | 是 |
| 相机未授权 | Identity Verify | 点击相机 | 权限弹窗 | 不进入 H5 | 是 |
| 相机永久拒绝 | OS 权限永久拒绝 | 点击 Allow access | 引导 open settings | 不进入 H5 | 是 |
| DTC 01009 | DTC 返回手机号重复 | 点击相机 | Toast：Mobile number already exists. | 不进入 H5 | 是 |
| Passport 失败 | AAI / DTC 返回 passport fail | 扫描护照 | 返回 Identity Verify 或展示失败原因 | 记录失败 code | 是 |
| Face 成功 | Passport 成功且 face 通过 | 完成活体 | 进入 Address Upload | face 失败计数清零 | 是 |
| Face 失败 5 次 | 24 小时内 face fail 4 次 | 再次失败 | 锁 20 分钟 | 记录 lock | 是 |
| Face 失败 10 次 | 24 小时内 face fail 9 次 | 再次失败 | 锁 24 小时 | 记录 lock | 是 |
| Face 接口连续 20 次 | 24 小时内连续发起 19 次 | 再发起一次 | 锁 20 分钟 | 拦截后续发起 | 是 |
| Face Loading 超时 | Face 采集完成后无结果 | 等待 30 秒 | Loading Failed | 可 Retry | 是 |
| Loading Failed Retry | Loading Failed Page | 点击 Retry | 进入 Face Loading | 重新提交 | 是 |
| passport 与 face 均失败 | 后端返回两者失败 | 进入 Face Failed | 优先展示 passport 原因 | 展示映射文案 | 是 |
| POA 格式错误 | 上传非支持格式 | 选择文件 | Toast Unsupported file type | 不上传 | 是 |
| POA 超 16MB | 上传大文件 | 选择文件 | Toast File size exceeds | 不上传 | 是 |
| POA 上传失败 | DTC 返回 14004 | 点击 Continue | 上传失败 Toast | 不进入 Success | 是 |
| POA 国家不支持 | countryOfResidence 不支持 | 点击 Continue | waitlist 或错误 | 不提交成功 | 是 |
| POA 成功 | 文件合法且国家支持 | 点击 Continue | Submission Success | DTC 返回 requestId | 是 |
| webhook 延迟 | 外部 webhook 未及时返回 | 等待结果 | 按 Loading / 超时处理 | query 或轮询兜底 | 是 |
| 通知触发 | KYC 结果 Approved / Rejected / Failed | 后端状态变化 | 待 Notification 规则确认 | 触发对应渠道 | 否，待确认 |
| 数据保存 | 用户提交协议 / waitlist / POA | 完成对应动作 | 页面正常流转 | 保存同意时间、快照、waitlist 信息、requestId | 是 |

---

## 10. DTC Master / Sub Account / Wallet 能力边界

### 10.1 DTC 账户对象

| 对象 | 当前理解 | 来源 / 备注 |
|---|---|---|
| Master Account | DTC 账户体系中的主账户；Sub Account 注册在 Master Account 下 | Master sub account 方案 |
| Sub Account | 注册在 Master Account 下的子账户 | Master sub account 方案 |
| `D-SUB-ACCOUNT-ID` | DTC 请求头，表示 master account 下注册的 sub account id | DTC API / WalletConnect token 历史来源 |
| clientId | DTC 客户标识；与 sub account / WalletAccount 字段关系需确认 | Master sub account 方案 / 历史 DTC Wallet OpenAPI 来源 |
| Wallet Account | DTC 钱包账户对象；字段来自历史 DTC Wallet OpenAPI，当前附件未核验 | GAP-KYC-WALLET-001 |

### 10.2 POA success 与 Sub Account 创建

Master sub account 方案的 POA success 分支写明：

```text
poa success
→ create sub account [countryOfResidence]
→ upload s3
→ update status
→ webhook poa success & verify success
```

当前处理：

1. 可以记录“设计流程中 POA success 包含 create sub account”。
2. 不能推导 “KYC Approved 通知一定代表 Sub Account 创建成功”。
3. 不能推导 “AIX user 与 DTC Sub Account 一定一一对应”。
4. 不能推导 “Sub Account 创建失败时 AIX 一定有自动补偿”。

### 10.3 Wallet 能力准入边界

| 能力 | 与 KYC / 开户的关系 | 当前处理 |
|---|---|---|
| Wallet 首页 / Balance | 可能依赖 Wallet Account / Sub Account 是否已创建、状态是否可用 | 字段和准入细节见 Wallet Balance；本文不补余额规则 |
| GTR / Exchange Deposit | 是否要求 KYC Approved / Sub Account 已创建，需按产品入口和后端规则确认 | 见 ALL-GAP-031 |
| WalletConnect Deposit | 技术链路可能依赖 `D-SUB-ACCOUNT-ID`；是否作为 App 入口前置拦截需确认 | 见 ALL-GAP-031 / GAP-KYC-WALLET-001 |
| Receive | 是否要求 KYC Approved / Sub Account 已创建未确认 | 见 Receive 相关 ALL-GAP |
| Send / Swap | 当前 deferred | 不纳入 active KYC 准入范围 |
| Card | Card KYC 与 Wallet / Account Opening KYC 是否复用未确认 | 见 ALL-GAP-030 |

---

## 11. 不得推导的内容

以下内容不得在没有来源时写成事实：

1. Wallet KYC 与 Card KYC 完全相同。
2. Account Opening / KYC 与 AAI 内部 KYC 完全相同。
3. AIX user 与 DTC Sub Account 一定一一对应。
4. `D-SUB-ACCOUNT-ID` 与 WalletAccount.clientId 一定完全等价。
5. KYC Approved 通知一定代表 DTC Sub Account 创建成功。
6. KYC Approved 一定代表 Wallet / Deposit / WalletConnect / Receive 全部可用。
7. DTC Sub Account 创建失败时 AIX 一定有自动补偿。
8. KYC Failed / Rejected 的所有失败原因已完整覆盖供应商内部全部可能性。
9. AAI OCR / Face / POA 原始内部错误码已完整转译。
10. WalletConnect / GTR Deposit 的产品入口一定以 KYC Approved 为前置。
11. Notification 成功代表用户一定收到消息。
12. Send / Swap 是当前 active 能力。
13. 未上传的 DTC Wallet OpenAPI 文档中的 WalletAccount / WalletConnect 细节。

---

## 12. 来源引用

- (Ref: 历史prd/AIX WALLET 钱包开户KYC需求V1.0 (1).docx / 需求变更日志 / 国家线 / 6.2 KYC 状态机 / 7.2 开户页面逻辑 / 8 外部接口依赖 / 9 接口错误码映射 / 10 待确认事项)
- (Ref: DTC接口文档/Master sub account 设计方案 (2).docx / KYC 流程 / DTC API / Master Account / Sub Account / D-SUB-ACCOUNT-ID / POA 文件上传流程 / 失败原因)
- (Ref: DTC Wallet OpenAPI Document20260126 / WalletConnect Token / D-SUB-ACCOUNT-ID / WalletAccount：本轮未上传，相关内容仅保留历史来源提示，不作为本轮核验事实)
- (Ref: prd-template/standard-prd-template.md / 标准 PRD 模板)
- (Ref: knowledge-base/common/aai.md)
- (Ref: knowledge-base/common/dtc.md)
- (Ref: knowledge-base/common/notification.md：Notification 规则待核验)
- (Ref: knowledge-base/changelog/knowledge-gaps.md / ALL-GAP-030 ~ ALL-GAP-035 / ALL-GAP-045 / ALL-GAP-046)
- (Ref: 用户确认结论 / 2026-05-02 / KYC 文件名不应带 wallet；新主事实源改为 account-opening.md)
