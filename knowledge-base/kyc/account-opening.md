---
module: kyc
feature: account-opening
version: "2.6"
status: active
source_doc: archive/legacy-prd/kyc/wallet-opening/README.md；archive/legacy-prd/app/home/README.md；archive/legacy-prd/card/application/README.md；archive/legacy-prd/security/identity-verification/README.md
source_section: KYC / 国家线、状态机、开户页面逻辑、外部接口、错误码；Home / 钱包区域展示；Card Application / 申卡前置
last_updated: 2026-05-09
owner: 吴忆锋
readers: [product, ui, dev, qa, business, ai]
depends_on:
  - kyc/_index
  - integrations/aai
  - integrations/dtc
  - common/notification
  - wallet/deposit
  - wallet/balance
  - changelog/knowledge-gaps
  - _system-boundary
---

# Account Opening / KYC 开户与身份认证准入 PRD

> Source alignment note: 本文件已按 `archive/legacy-prd/kyc/wallet-opening/README.md` 做双向覆盖校验，并同步核对 Home 钱包面板、Card Application 申卡前置和 Security 身份认证支撑证据。


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

> 页面图：截图已复制到 `_assets/account-opening/`，阅读页面规则时可直接看到页面样式。
> 功能结构与账户结构图。

![KYC function structure - image1.jpeg](_assets/account-opening/image1.jpeg)

![KYC function structure - image2.jpeg](_assets/account-opening/image2.jpeg)


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

> 页面图：截图已复制到 `_assets/account-opening/`，阅读页面规则时可直接看到页面样式。
> 开户业务流程总图。

![KYC business flow - image4.jpeg](_assets/account-opening/image4.jpeg)


### 3.1 业务主流程说明

KYC 主流程按业务阶段可归纳为：

```text
手机号绑定判断
→ 准入状态判断
→ 居住国家与协议确认
→ 证件认证
→ 人脸验证
→ 地址证明上传
→ 提交审核
→ 结果通知 / 入口状态感知
```

页面路径为：

```text
手机号绑定判断 / 绑定流程
→ KYC Loading
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

> 本图只把第三章业务流程图时序化表达，参与方保持流程图泳道：AIX 客户端、AIX 中后台、DTCPay 服务端、AAI 服务。页面弹窗、waitlist、异常页等未在该流程图主干展示的细节，不在本图补充，见第 4 章与 3.5。

```mermaid
sequenceDiagram
    autonumber
    participant APP as AIX 客户端
    participant BE as AIX 中后台
    participant DTC as DTCPay 服务端
    participant AAI as AAI 服务

    APP->>APP: KYC Start Page（状态：未绑定手机）
    APP->>APP: 引导用户绑定手机

    alt 未绑定手机
        APP->>APP: 提示用户绑定手机流程
    else 已绑定手机
        APP->>BE: 查询 KYC 认证结果
        BE->>DTC: GET /openapi/v1/ekyc/verification-result/{externalId}
        DTC-->>BE: 返回认证结果（clientStatus、Passport、Face、POA result）
        BE->>BE: 更新 KYC 状态机

        alt KYC 状态为 Under review / Rejected / Approved
            BE-->>APP: 返回不可继续状态
            APP->>APP: 展示 Verification unavailable
        else KYC 状态为 pending / failed
            BE-->>APP: 返回可继续状态
            APP->>APP: KYC Start Page（状态：已绑定手机）
            APP->>APP: 用户填写居住国家，点击下一步
        end
    end

    APP->>BE: 请求 Passport 扫描 URL（verifyType = 1）
    BE->>DTC: POST /openapi/v1/ekyc/get-verification-url
    DTC-->>BE: 返回 Passport H5 URL
    BE-->>APP: 返回 Passport H5 URL
    APP->>APP: 客户端打开 H5 扫描页，进行扫描

    APP->>AAI: H5 内完成 Passport OCR
    AAI-->>DTC: 返回 OCR 信息 / Passport 信息
    DTC-->>BE: 返回 OCR 信息 / Passport 信息

    alt OCR 失败
        BE-->>APP: 返回 OCR 失败结果
        APP->>APP: 回到业务场景，由后续规则处理
    else OCR 完成
        BE->>BE: 按 Passport / Face 状态判断后续流程
    end

    alt passport = SUCCESS 且 face = UNVERIFIED / FAILURE
        BE-->>APP: 进入 Face Guide Page
        APP->>BE: 请求活体 URL（verifyType = 4）
        BE->>DTC: POST /openapi/v1/ekyc/get-verification-url
        DTC-->>BE: 返回活体 URL
        BE-->>APP: 返回活体 URL
        APP->>APP: 客户端打开活体 URL，进入活体识别页
        APP->>AAI: 进行活体识别 / 人脸比对
        AAI-->>DTC: 返回 Face result
        DTC-->>BE: 返回 Face result / webhook 结果
    else passport = VERIFYING 且 face = SUCCESS / FAILURE / VERIFYING
        BE-->>APP: 进入 Loading Page
    else passport = SUCCESS 且 face = VERIFYING
        BE-->>APP: 进入 Loading Page
    else Face 比对失败
        BE-->>APP: 进入人脸比对失败页
        APP->>APP: 展示失败信息
    end

    APP->>BE: Loading 中主动查询验证结果
    BE->>DTC: GET /openapi/v1/ekyc/verification-result/{externalId}
    DTC-->>BE: 返回 Passport / Face 验证结果
    BE-->>APP: 返回查询结果

    alt passport result = VERIFY_SUCCESS 且 face result = VERIFY_SUCCESS
        APP->>APP: 进入 Address Upload Page
        APP->>APP: 上传 POA 文件
    else face = UNVERIFIED / 其他 result / VERIFY_FAILURE
        BE-->>APP: 返回失败或未完成结果
        APP->>APP: 按失败结果处理
    end

    APP->>BE: POST /openapi/v1/ekyc/upload 上传 POA 文件
    BE->>DTC: 提交 POA 文件与居住地信息
    DTC->>AAI: 处理 POA 文件 / POA OCR
    AAI-->>DTC: 返回 POA OCR 结果
    DTC-->>BE: 返回 POA 处理结果
    BE-->>APP: 返回提交结果
    APP->>APP: 进入 Under review Page

    APP->>BE: 定时查询 KYC 结果
    BE->>DTC: GET /openapi/v1/ekyc/verification-result/{externalId}
    DTC-->>BE: 返回 KYC 审核结果

    alt clientStatus = ACTIVATED
        BE->>BE: KYC 状态变更为 approved
        BE-->>APP: 返回 Approved
        BE-->>APP: SMS / 邮件通知用户
    else clientStatus = REJECTED
        BE->>BE: KYC 状态变更为 rejected
        BE-->>APP: 返回 Rejected
        BE-->>APP: SMS / 邮件通知用户
    else passportVerifyStatus = VERIFY_FAILURE 或 faceIdVerifyStatus = VERIFY_FAILURE 或 proofOfAddressVerifyStatus = VERIFY_FAILURE
        BE->>BE: KYC 状态变更为 failed
        BE->>DTC: GET /openapi/v1/ekyc/passport-info/{externalId} 查询护照 OCR 信息
        BE->>DTC: GET /openapi/v1/ekyc/poa-info/{externalId} 查询 POA OCR 信息
        DTC-->>BE: 返回护照 OCR 信息 / POA OCR 信息
        BE-->>APP: 返回 failed
    end
```

### 3.3 流程步骤与业务规则

| 步骤 | 场景 / 规则 | 触发条件 | 责任方 | 系统处理 | 成功结果 | 失败 / 分支结果 | 来源 |
|---|---|---|---|---|---|---|---|
| 1 | 手机号绑定判断 | 用户发起 KYC / 开户流程 | App / Account | 判断是否已绑定手机号 | 已绑定：继续 KYC 状态判断；KYC Start 不展示额外绑定成功 toast | 未绑定：进入手机号绑定流程；绑定完成后继续 KYC 状态判断；未绑定流程细节见 `GAP-KYC-PHONE-001` | AIX KYC PRD 7.1 / 7.2.3 |
| 2 | KYC Loading 状态判断 | 用户进入 KYC | App / Backend | 查询 KYC 状态和 waitlist 状态 | KYC 状态为 Pending / failed 时进入 KYC Start 或后续未完成节点 | KYC 状态为 Under review / Rejected / Approved 时展示状态2；用户在 waitlist 中且来源渠道是 APP 时展示状态2；网络异常进入 Network Error Page；系统异常进入 Server Error Page；30 秒无结果进入 Loading Failed Page | AIX KYC PRD 7.2.2 |
| 3 | KYC Start | 状态允许继续 KYC | App | 展示标题、副标题、居住国家、协议、认证按钮 | 用户可选择国家和勾选协议 | 手机号未绑定处理待确认 | AIX KYC PRD 7.2.3 |
| 4 | 国家选择 | 用户点击居住国家 | App / Backend / 配置 | 展示国家列表、搜索、排序、Type 判断 | Phase 1 国家可继续 | phase 2-waitlist 进入 waitlist；Forbiden 隐藏 | AIX KYC PRD 7.2.3.1 |
| 5 | 协议确认 | 用户勾选协议 | App / Backend | 保存同意时间、Declaration 内容和快照 | 按钮可点击，继续 Identity Verify | 获取协议失败 toast；Reverse Solicitation 缺失可触发 DTC 50013 | AIX KYC PRD 7.2.3；Master sub account |
| 6 | Waitlist | 国家 Type = phase 2-waitlist，或 KYC Loading 判断用户在 waitlist 中且来源渠道是 APP | App / Backend | 校验 email；提交成功后按 userId 加入 waitlist，记录邮箱、国家、来源、提交时间、设备指纹 ID，并推送数仓 | 用户加入 waitlist，无法继续申请 KYC；历史原文返回业务流程入口页 | email 为空、格式错误、长度超过 103 字符时不提交；网络异常 Toast：Please check your internet connection and try again.；后端服务器错误 Toast：Something went wrong. Please try again later | AIX KYC PRD 7.2.3.2 |
| 7 | Identity Verify | 用户点击相机 | App / Backend / DTC | 判断相机权限，生成 Passport H5 URL | 进入 Identity Scan H5 | 未授权 / 永久拒绝 / DTC 01009 / 01005 | AIX KYC PRD 7.2.4；Master sub account |
| 8 | Identity Scan | 用户扫描护照 | AAI / DTC | AAI H5 完成 Passport OCR，DTC 接收结果 | 成功进入 Face Guide | 失败返回 Identity Verify | AIX KYC PRD 7.2.5 |
| 9 | Face Guide | 用户点击 Continue | App / Backend | 判断 face 锁定规则，获取 passport country，生成 selfie H5 URL | 未锁定进入 Face Scan | 锁定弹窗；网络 / 服务器错误 toast | AIX KYC PRD 7.2.6 |
| 10 | Face Scan | 用户完成活体采集 | AAI / DTC | 外部 H5 完成 Liveness / Face capture | 进入 Face Loading | AAI signatureId 3 次后需重新生成 URL | AIX KYC PRD 7.2.7 |
| 11 | Face Loading | 活体采集结束 | App / Backend / DTC / AAI | 轮询或接收验证结果 | 成功进入 Address Upload | 失败进入 Face Failed；30 秒超时进入 Loading Failed；网络 / 系统错误页 | AIX KYC PRD 7.2.8 |
| 12 | Loading Failed | Face Loading 超过 30 秒无结果 | App | 展示超时失败页 | Retry 后进入 Face Loading 重新提交 | Leave 返回入口 | AIX KYC PRD 7.2.9 |
| 13 | Face Failed | Face result 为 FAIL / EXPIRED / incomplete，或 Passport / Document Verification 失败，或 POA 失败 | App / Backend | Face 失败展示 Face Comparison 错误码映射文案；Passport 失败展示 Passport / Document Verification 错误码映射文案；POA 失败展示 POA error code 映射文案；Passport 与 Face 均失败时优先展示 Passport 原因 | Try again 且未锁定时重新触发 KYC 流程 | Try again 但已锁定时展示 Too many attempts，不允许重试 | AIX KYC PRD 7.2.10 / 9 |
| 14 | Address Upload / POA | Face 成功 | App / Backend / DTC / AAI | 上传 POA 文件；二次判断居住国家；AAI 机审提取 POA 国家并核验与用户填报居住国是否匹配，同时校验申请国家是否属于白名单 | POA 文件和国家信息提交成功后进入 Submission Success | 非 JPG/JPEG/PNG/PDF 阻止上传并展示格式 toast；单文件超过 16MB 阻止上传并展示大小 toast；上传服务器报错展示 Server busy toast；国家不支持进入 waitlist 拦截；POA OCR 国家不匹配或 POA 审核失败时按 POA error code 映射展示文案 | AIX KYC PRD 7.2.11；Master sub account |
| 15 | KYC Submission Success | POA 提交成功 | App / Backend | 展示提交成功状态 | 用户返回入口，等待审核 | 后续状态通过通知或入口感知 | AIX KYC PRD 7.2.12 |

### 3.4 状态规则

> 页面图：截图已复制到 `_assets/account-opening/`，阅读页面规则时可直接看到页面样式。
> KYC 状态机图。

![KYC status machine - image3.jpeg](_assets/account-opening/image3.jpeg)


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
| KYC Loading 状态2：KYC 状态命中 | 后端返回 KYC 状态机为 Under review / Rejected / Approved | Backend | KYC 状态 | KYC Loading Page 展示状态2 / Verification unavailable | 阻止继续提交 | 否 | 保持当前状态 |
| KYC Loading 状态2：APP 来源 waitlist 命中 | 用户在 waitlist 中，且来源渠道是 APP | Backend | waitlist | KYC Loading Page 展示状态2 / Verification unavailable | 阻止继续 KYC | 否 | waitlist |
| KYC Loading 网络异常 | 查询状态网络异常 | App / Network | 网络异常 | Network Error Page | 停留错误页 | 是 | 未变更 |
| KYC Loading 系统异常 | 后端系统异常 | Backend | 系统异常 | Server Error Page | 停留错误页 | 是 | 未变更 |
| KYC Loading 超时 | 30 秒无结果 | Backend / Network | Timeout | Loading Failed Page | 用户可 Retry | 是 | 未变更 |
| 协议获取失败 | 后端无法获取协议 | Backend | 获取协议失败 | Toast | 阻止继续 | 是 | 未变更 |
| Reverse Solicitation 缺失 | 国家要求反向招揽声明但未传 `reverseSolicitation=T` | DTC | 50013 | DTC 返回 `Reverse solicitation not declared by end user`；前端提示文案源文档未明确 | 阻止生成验证 URL；需补 Declaration 声明后再继续 | 是 | 未变更 |
| Passport URL 生成失败 | DTC get-verification-url 返回错误 | DTC | 01009 / 01005 / 其他 get-verification-url 错误码 | 01009 Toast：`Mobile number already exists.`；01005 Toast：`The email address is in use.`；其他错误码含义见 5.2，未明确前端文案的错误码需后端 / 产品确认 | 阻止进入 H5 | 01009 / 01005 可由用户更换信息后重试；其他错误码是否可重试需按 5.2 / 后端确认 | 未变更 |
| Passport OCR 失败 | AAI / DTC 返回 Passport OCR 失败 | AAI / DTC | passport error code | 源文档 7.2.5 明确扫描失败跳转至 Identity Verify Page；如后端返回 Passport / Document Verification 错误原因，文案见 5.3 | 记录失败原因和 error code | 是 | failed / 待映射 |
| Face 失败 | DTC 返回 face result=fail | DTC / AAI | face error code | Face Failed Page | 计入 face 失败次数 | 是，未锁定时 | failed |
| Face 失败 5 次 | 24 小时内 face fail 5 次 | Backend / DTC | 安全限制 | Too many attempts | 锁 20 分钟 | 否，锁定期不可重试 | lock |
| Face 失败 10 次 | 24 小时内 face fail 10 次 | Backend / DTC | 安全限制 | Too many attempts | 锁 24 小时 | 否，锁定期不可重试 | lock |
| Face 接口连续发起 20 次 | 24 小时内接口层连续发起 20 次 | Backend | 风控限制 | Too many attempts | 锁 20 分钟 | 否，锁定期不可重试 | lock |
| Face Loading 超时 | 30 秒无结果 | Backend / DTC / AAI | Timeout | Loading Failed Page | Retry 后重新提交 | 是 | 未变更 |
| POA 文件格式错误 | 上传非 JPG/JPEG/PNG/PDF | App | 文件格式 | Toast | 阻止上传 | 是 | 未变更 |
| POA 文件过大 | 单文件超 16MB | App | 文件大小 | Toast | 阻止上传 | 是 | 未变更 |
| POA 上传失败 | 服务器或 DTC 上传失败 | Backend / DTC | 14004 / 14005 / Server error | Toast | 阻止继续 | 是 | 未变更 |
| POA 国家不匹配 | POA OCR 国家与用户填报居住国家不匹配 | DTC / AAI | POA error code | 按 POA error code 映射展示前端提示文案 | 记录失败原因 | 是 | failed |
| POA 国家不支持 | 申请国家不属于支持国家 / 白名单 | Backend / DTC / AAI | 国家线 / POA error code | Address Upload Page 内 Waitlist 拦截；Join waitlist 进入 Waitlist Page | 阻止当前国家继续提交 POA | 是，用户可选择其他国家或加入 waitlist | waitlist / failed |
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

进入 KYC 时先做状态判断。该页只负责分流，不承载资料填写。

<table>
  <tr>
    <th width="48%">页面</th>
    <th width="52%">说明</th>
  </tr>
  <tr>
    <td valign="top">
      <img src="_assets/account-opening/image6.jpeg" width="480" />
    </td>
    <td valign="top">
      <p><strong>Loading 状态</strong></p>
      <ul>
        <li><strong>进入前提</strong>：用户从业务入口发起 KYC。</li>
        <li><strong>展示内容</strong>：展示 <code>loading...</code>。</li>
        <li><strong>系统处理</strong>：查询 KYC 状态和 waitlist 状态。
          <ul>
            <li>KYC 状态为 Pending / failed：进入 KYC Start 或后续未完成节点。</li>
            <li>KYC 状态为 Under review / Rejected / Approved：进入本页的 Verification unavailable 状态。</li>
            <li>用户在 waitlist 中，且来源渠道为 APP：进入本页的 Verification unavailable 状态，阻止继续 KYC。</li>
          </ul>
        </li>
      </ul>

      <p><strong>Verification unavailable 状态</strong></p>
      <ul>
        <li><strong>触发前提</strong>：后端返回 KYC 状态机为 Under review / Rejected / Approved，或用户在 waitlist 中且来源渠道是 APP。</li>
        <li><strong>展示内容</strong>：展示不可继续认证说明和 <code>Back</code> 按钮。</li>
        <li><strong>用户操作</strong>：
          <ul>
            <li>点击 Back：返回业务入口。</li>
            <li>点击关闭：关闭当前 KYC 流程。</li>
          </ul>
        </li>
      </ul>

      <p><strong>Loading 异常</strong></p>
      <ul>
        <li>网络异常：进入 Network Error Page。</li>
        <li>服务异常：进入 Server Error Page。</li>
        <li>30 秒无结果：进入 Loading Failed Page；细则见 <a href="#49-loading-failed-page">4.9 Loading Failed Page</a>。</li>
      </ul>
    </td>
  </tr>
</table>

关联：`KYC-LOADING-001 ~ KYC-LOADING-010`；Source：AIX KYC PRD 7.2.2。

---

### 4.3 KYC Start Page

用户在本页选择居住国家、确认协议，并通过底部认证按钮进入身份认证流程。

<table>
  <tr>
    <th width="48%">页面</th>
    <th width="52%">说明</th>
  </tr>
  <tr>
    <td valign="top">
      <img src="_assets/account-opening/image7.png" width="480" />
    </td>
    <td valign="top">
      <p><strong>居住国家 / 地区</strong></p>
      <ul>
        <li><strong>默认展示</strong>：默认值来自 IP 检测；检测不到时默认 SG。</li>
        <li><strong>点击国家区域</strong>：进入 Select Residence Country Page；国家选择细则见 <a href="#44-select-residence-country-page">4.4 Select Residence Country Page</a>。
          <ul>
            <li><strong>选择结果按国家 Type 判断</strong>：</li>
            <li>Type = Phase 1：返回本页；协议完成后可继续 KYC。</li>
            <li>Type = phase 2 - waitlist：返回本页；点击底部认证按钮后触发本页 Waitlist 拦截；拦截展示见 <a href="#432-拦截waitlist">4.3.2 拦截：Waitlist</a>，提交页细则见 <a href="#45-waitlist-page">4.5 Waitlist Page</a>。</li>
            <li>Type = Forbiden：国家列表隐藏，不可选择。</li>
          </ul>
        </li>
      </ul>
      <p>国家线存在版本口径冲突，见 <code>GAP-KYC-COUNTRY-001</code>。</p>

      <p><strong>协议区</strong></p>
      <ul>
        <li>Terms / Privacy：可直接勾选，无需强制阅读；需保存用户同意并提交的时间。</li>
        <li>Declaration：点击后打开 Declaration 弹窗 / 阅读页；完成规则见 <a href="#431-弹窗declaration-of-reverse-solicitation">4.3.1 弹窗：Declaration of Reverse Solicitation</a>。</li>
        <li>任一必选协议未完成：底部认证按钮灰色，不可点击。</li>
        <li>所有必选协议完成：底部认证按钮高亮，可点击。</li>
        <li>无法获取协议：Toast <code>Something went wrong. Please try again later</code>，不允许继续。</li>
      </ul>

      <p><strong>底部认证按钮</strong></p>
      <p>原 PRD 中称 <code>立即认证 / Continue / Verify</code>，具体文案以 UI 为准。</p>
      <ul>
        <li><strong>点击前提</strong>：所有必选协议完成。</li>
        <li><strong>点击后处理</strong>：
          <ul>
            <li>协议完成 + 国家 Type = Phase 1：保存协议相关信息，进入 Identity Verify；后续细则见 <a href="#46-identity-verify-page">4.6 Identity Verify Page</a>。</li>
            <li>协议完成 + 国家 Type = phase 2 - waitlist：不进入 Identity Verify，触发 waitlist 拦截；见 <a href="#432-拦截waitlist">4.3.2 拦截：Waitlist</a>。</li>
            <li>协议保存失败：不推进流程，应阻止继续；源文档未明确“勾选即保存”还是“点击底部认证按钮统一保存”，实现时需以后端接口约定为准。</li>
          </ul>
        </li>
      </ul>

      <p><strong>入口边界</strong></p>
      <ul>
        <li>手机号已绑定：直接进入 Start Page，不展示额外绑定成功 toast。</li>
        <li>手机号未绑定：本页流程未确认，见 <code>GAP-KYC-PHONE-001</code>。</li>
      </ul>
    </td>
  </tr>
</table>

#### 4.3.1 弹窗：Declaration of Reverse Solicitation

<table>
  <tr>
    <th width="48%">页面</th>
    <th width="52%">说明</th>
  </tr>
  <tr>
    <td valign="top">
      <img src="_assets/account-opening/image9.png" width="480" />
    </td>
    <td valign="top">
      <p><strong>触发方式</strong></p>
      <p>用户在 KYC Start Page 点击 Declaration 协议项后展示。</p>

      <p><strong>弹窗内操作</strong></p>
      <ul>
        <li>点击 <code>I agree</code>：关闭弹窗，Declaration 变为已完成。</li>
        <li>关闭 / 返回：关闭弹窗，Declaration 不算完成，底部认证按钮仍按协议未完成处理。</li>
      </ul>

      <p><strong>保存要求与边界</strong></p>
      <ul>
        <li>保存 Declaration 内容。</li>
        <li>保存用户同意时间。</li>
        <li>影响 DTC <code>reverseSolicitation</code> 入参。</li>
        <li>需要反向招揽声明的国家，应传 <code>reverseSolicitation=T</code>；缺失时 DTC 可能返回 <code>50013</code>。</li>
        <li>Reverse Solicitation 缺失：阻止生成验证 URL，需补声明后再继续；错误码细则见 <a href="#52-get-verification-url-错误码">5.2 get-verification-url 错误码</a>。</li>
      </ul>
    </td>
  </tr>
</table>

#### 4.3.2 拦截：Waitlist

<table>
  <tr>
    <th width="48%">页面</th>
    <th width="52%">说明</th>
  </tr>
  <tr>
    <td valign="top">
      <img src="_assets/account-opening/image10.png" width="480" />
    </td>
    <td valign="top">
      <p><strong>触发方式</strong></p>
      <p>用户在 KYC Start Page 点击底部认证按钮后，后端判断所选国家不支持继续 KYC。</p>

      <p><strong>拦截状态</strong></p>
      <ul>
        <li><strong>处理结果</strong>：不允许进入 Identity Verify。</li>
        <li><strong>用户操作</strong>：
          <ul>
            <li>点击 Join waitlist：进入 Waitlist Page；提交细则见 <a href="#45-waitlist-page">4.5 Waitlist Page</a>。</li>
            <li>返回：源文档未明确返回目标。当前仅确认用户不能进入 Identity Verify；返回 KYC Start 还是业务流程入口需以最新 UI / 产品确认为准。</li>
          </ul>
        </li>
      </ul>

      <p><strong>展示边界</strong></p>
      <p>源文档同时出现“弹窗拦截”描述和“waitlist 调整为页面级拦截”的变更记录。当前文档只确认结果：用户不能继续 KYC，并可进入 Waitlist Page；具体展示形态以最新 UI 为准。</p>
    </td>
  </tr>
</table>

协议快照需在提交成功后生成并与用户账户绑定。关联：`KYC-START-001 ~ KYC-START-010`；Source：AIX KYC PRD 7.2.3、Master sub account。

---

### 4.4 Select Residence Country Page

用于选择或修改居住国家。来源可能是 KYC Start，也可能是 Address Upload。

<table>
  <tr>
    <th width="48%">页面</th>
    <th width="52%">说明</th>
  </tr>
  <tr>
    <td valign="top">
      <img src="_assets/account-opening/image11.png" width="480" />
      <br><br>
      <img src="_assets/account-opening/image12.png" width="480" />
    </td>
    <td valign="top">
      <p><strong>默认国家列表状态</strong></p>
      <ul>
        <li><strong>进入前提</strong>：用户从 KYC Start 或 Address Upload 点击国家 / Residence 区域进入本页。</li>
        <li><strong>默认展示</strong>：
          <ul>
            <li>IP 可识别国家：默认展示 IP 国家。</li>
            <li>IP 不可识别国家：默认展示 SG。</li>
          </ul>
        </li>
        <li><strong>列表规则</strong>：
          <ul>
            <li>国家 / 地区按首字母排序。</li>
            <li>Type = Phase 1：展示，可选择。</li>
            <li>Type = phase 2 - waitlist：展示，可选择；后续进入 waitlist 判断。</li>
            <li>Type = Forbiden：隐藏。</li>
          </ul>
        </li>
      </ul>

      <p><strong>搜索状态</strong></p>
      <ul>
        <li><strong>触发方式</strong>：用户输入关键词。</li>
        <li><strong>展示结果</strong>：展示匹配国家。</li>
        <li><strong>清空关键词</strong>：恢复默认国家列表。</li>
      </ul>

      <p><strong>选择返回</strong></p>
      <ul>
        <li>从 KYC Start 进入：点击国家项后返回 KYC Start，并带回选择结果。</li>
        <li>从 Address Upload 进入：点击国家项后返回 Address Upload，并带回选择结果。</li>
        <li>点击关闭 / 返回：返回来源页面，不推进流程。</li>
      </ul>

      <p>国家线冲突见 <code>GAP-KYC-COUNTRY-001</code>。</p>
    </td>
  </tr>
</table>

关联：`KYC-COUNTRY-001 ~ KYC-COUNTRY-009`；Source：AIX KYC PRD 7.2.3.1。

---

### 4.5 Waitlist Page

国家暂不支持开户时进入本页。用户不能继续 KYC，只能提交 waitlist 或返回。

<table>
  <tr>
    <th width="48%">页面</th>
    <th width="52%">说明</th>
  </tr>
  <tr>
    <td valign="top">
      <img src="_assets/account-opening/image13.png" width="480" />
    </td>
    <td valign="top">
      <p><strong>Email 输入区域</strong></p>
      <ul>
        <li><strong>输入校验</strong>：
          <ul>
            <li>邮箱为空：展示校验提示，不提交。</li>
            <li>邮箱格式错误：展示校验提示，不提交。</li>
            <li>邮箱长度超过 103 字符：展示校验提示，不提交。</li>
            <li>邮箱格式正确：可提交。</li>
          </ul>
        </li>
      </ul>

      <p><strong>提交按钮</strong></p>
      <ul>
        <li><strong>点击前提</strong>：邮箱格式正确。</li>
        <li><strong>提交成功</strong>：按 userId 加入 waitlist，记录邮箱、国家、来源、提交时间、设备指纹，并推送数仓。</li>
        <li><strong>提交失败</strong>：
          <ul>
            <li>网络异常：Toast <code>Please check your internet connection and try again.</code></li>
            <li>后端服务器错误：Toast <code>Something went wrong. Please try again later</code></li>
          </ul>
        </li>
      </ul>

      <p><strong>退出</strong></p>
      <ul>
        <li>点击关闭 / 返回：历史原文为“返回到业务流程入口页”。若用户从 KYC Start 的 waitlist 拦截进入本页，是否返回 KYC Start 还是业务流程入口，需以最新 UI / 产品确认为准。</li>
      </ul>

      <p>设备指纹获取失败策略源文档未确认，见 waitlist 数据边界。</p>
    </td>
  </tr>
</table>

关联：`KYC-WAITLIST-001 ~ KYC-WAITLIST-010`；Source：AIX KYC PRD 7.2.3.2。

---

### 4.6 Identity Verify Page

证件认证入口页。App 负责引导和权限处理，外部 H5 负责护照扫描和 OCR。

<table>
  <tr>
    <th width="48%">页面</th>
    <th width="52%">说明</th>
  </tr>
  <tr>
    <td valign="top">
      <img src="_assets/account-opening/image14.png" width="480" />
      <br><br>
      <img src="_assets/account-opening/image15.png" width="480" />
    </td>
    <td valign="top">
      <p><strong>证件扫描入口</strong></p>
      <ul>
        <li><strong>点击相机 / 开始扫描</strong>：
          <ul>
            <li>有权限：请求 Passport H5 URL。</li>
            <li>相机未授权 / 永久拒绝：展示权限提示或引导开启权限。</li>
          </ul>
        </li>
        <li><strong>请求 H5 URL 失败</strong>：
          <ul>
            <li>DTC 返回 <code>01009</code>：Toast <code>Mobile number already exists.</code>，不进入 H5。</li>
            <li>DTC 返回 <code>01005</code>：Toast <code>The email address is in use.</code>，不进入 H5。</li>
            <li>DTC 返回其他 get-verification-url 错误：不进入 H5；错误码含义和已确认前端表现见 <a href="#52-get-verification-url-错误码">5.2 get-verification-url 错误码</a>，未明确前端文案的错误码需后端 / 产品确认。</li>
          </ul>
        </li>
      </ul>

      <p><strong>后续流转</strong></p>
      <ul>
        <li>成功获取 H5 URL：进入 Identity Scan H5；细则见 <a href="#461-h5identity-scan-page">4.6.1 H5：Identity Scan Page</a>。</li>
        <li>Passport OCR 成功：进入 Face Guide Page；细则见 <a href="#47-face-guide-page">4.7 Face Guide Page</a>。</li>
        <li>Passport OCR 失败：源文档 7.2.5 明确“扫描失败：跳转至 Identity Verify Page”；如后端同时返回 Passport / Document Verification 错误原因，前端文案映射见 <a href="#53-错误码与前端文案映射">5.3 错误码与前端文案映射</a>。</li>
      </ul>
    </td>
  </tr>
</table>

#### 4.6.1 H5：Identity Scan Page

<table>
  <tr>
    <th width="48%">页面</th>
    <th width="52%">说明</th>
  </tr>
  <tr>
    <td valign="top">
      <img src="_assets/account-opening/image16.png" width="480" />
    </td>
    <td valign="top">
      <p><strong>H5 扫描状态</strong></p>
      <ul>
        <li><strong>进入前提</strong>：Identity Verify Page 成功获取 Passport H5 URL。</li>
        <li><strong>用户操作</strong>：在外部 H5 完成护照扫描和 Passport OCR。</li>
        <li><strong>处理结果</strong>：
          <ul>
            <li>用户完成护照扫描：等待 AAI / DTC 返回 OCR 结果。</li>
            <li>用户取消或返回 H5：返回 Identity Verify Page。</li>
            <li>Passport OCR 成功：进入 Face Guide Page；细则见 <a href="#47-face-guide-page">4.7 Face Guide Page</a>。</li>
            <li>Passport OCR 失败：返回 Identity Verify Page；如后端返回 Passport / Document Verification 错误原因，前端文案映射见 <a href="#53-错误码与前端文案映射">5.3 错误码与前端文案映射</a>。</li>
            <li>H5 URL 过期或不可用：源文档未明确自动重试策略。当前仅确认不能继续使用该 URL；是否重新请求 <code>get-verification-url</code> 或展示接口错误，需要以后端接口约定为准。</li>
          </ul>
        </li>
      </ul>
    </td>
  </tr>
</table>

关联：`get-verification-url(PASSPORT)`、`passportVerifyStatus`、`requestId`、`url`、`expireTime`；Source：AIX KYC PRD 7.2.4、7.2.5。

---

### 4.7 Face Guide Page

Passport OCR 成功后进入本页，用户从这里发起人脸活体认证。

<table>
  <tr>
    <th width="48%">页面</th>
    <th width="52%">说明</th>
  </tr>
  <tr>
    <td valign="top">
      <img src="_assets/account-opening/image17.png" width="480" />
      <br><br>
      <img src="_assets/account-opening/image18.png" width="480" />
    </td>
    <td valign="top">
      <p><strong>Continue 按钮</strong></p>
      <ul>
        <li><strong>点击前提</strong>：用户在 Face Guide Page 点击 Continue。</li>
        <li><strong>点击后判断</strong>：
          <ul>
            <li>未锁定：获取 passport country，请求 selfie / liveness H5 URL，并进入 Face Scan H5；细则见 <a href="#471-h5face-scan-page">4.7.1 H5：Face Scan Page</a>。</li>
            <li>已锁定：展示 Too many attempts，不进入 H5。</li>
          </ul>
        </li>
        <li><strong>异常</strong>：
          <ul>
            <li>网络异常：Toast <code>Please check your internet connection and try again.</code></li>
            <li>后端服务器错误：Toast <code>Something went wrong. Please try again later</code></li>
          </ul>
        </li>
      </ul>

      <p><strong>锁定规则</strong></p>
      <ul>
        <li>24 小时内 face fail 5 次：锁 20 分钟。</li>
        <li>24 小时内 face fail 10 次：锁 24 小时。</li>
        <li>24 小时内接口层连续发起 20 次：锁 20 分钟。</li>
        <li>Face 验证成功：清零重新计算。</li>
      </ul>
    </td>
  </tr>
</table>

#### 4.7.1 H5：Face Scan Page

<table>
  <tr>
    <th width="48%">页面</th>
    <th width="52%">说明</th>
  </tr>
  <tr>
    <td valign="top">
      <img src="_assets/account-opening/image19.png" width="480" />
    </td>
    <td valign="top">
      <p><strong>H5 活体采集状态</strong></p>
      <ul>
        <li><strong>进入前提</strong>：Face Guide Page 成功获取 selfie / liveness H5 URL。</li>
        <li><strong>用户操作</strong>：在外部 H5 完成活体采集。</li>
        <li><strong>处理结果</strong>：
          <ul>
            <li>用户完成活体采集：返回 App，进入 Face Loading Page；细则见 <a href="#48-face-loading-page">4.8 Face Loading Page</a>。</li>
            <li>用户中断或返回 H5：源文档未明确 App 侧目标页。当前仅确认未完成活体采集时不能进入 Face Loading Page；返回 Face Guide Page、停留 H5 还是关闭流程，需以 AAI H5 返回协议和最新 UI 为准。</li>
            <li>AAI 同一 <code>signatureId</code> 重试 3 次后失效：重新 generate-url，生成新的 <code>signatureId</code>。</li>
            <li>网络 / 服务异常：源文档未明确 Face Scan H5 内异常的 App 展示形态。当前不能写死为错误页或 toast；需以 AAI H5 返回协议和 App 统一错误处理为准。</li>
          </ul>
        </li>
      </ul>
    </td>
  </tr>
</table>

关联：`get-verification-url(SELFIE / LIVENESS)`、face fail count、lock 状态；Source：AIX KYC PRD 7.2.6、7.2.7。

---

### 4.8 Face Loading Page

活体采集结束后进入本页，等待 face verification / face compare 结果。

<table>
  <tr>
    <th width="48%">页面</th>
    <th width="52%">说明</th>
  </tr>
  <tr>
    <td valign="top">
      <img src="_assets/account-opening/image6.jpeg" width="480" />
    </td>
    <td valign="top">
      <p><strong>等待状态</strong></p>
      <ul>
        <li><strong>进入前提</strong>：Face Scan H5 完成活体采集并返回 App。</li>
        <li><strong>系统处理</strong>：等待 face verification / face compare 结果。</li>
        <li><strong>结果返回后</strong>：
          <ul>
            <li>Face 成功：进入 Address Upload Page；细则见 <a href="#411-address-upload-page">4.11 Address Upload Page</a>。</li>
            <li>Face 失败：进入 Face Failed Page；细则见 <a href="#410-face-failed-page">4.10 Face Failed Page</a>。</li>
            <li>30 秒无结果：进入 Loading Failed Page；细则见 <a href="#49-loading-failed-page">4.9 Loading Failed Page</a>。</li>
            <li>网络异常：进入 Network Error Page。</li>
            <li>系统异常：进入 Server Error Page。</li>
          </ul>
        </li>
      </ul>
    </td>
  </tr>
</table>

关联：`faceIdVerifyStatus`；Source：AIX KYC PRD 7.2.8。

---

### 4.9 Loading Failed Page

Face Loading 超过 30 秒仍无结果时展示。

<table>
  <tr>
    <th width="48%">页面</th>
    <th width="52%">说明</th>
  </tr>
  <tr>
    <td valign="top">
      <img src="_assets/account-opening/image20.png" width="480" />
    </td>
    <td valign="top">
      <p><strong>超时状态</strong></p>
      <ul>
        <li><strong>进入前提</strong>：Face Loading Page 超过 30 秒仍未收到结果。</li>
        <li><strong>展示内容</strong>：展示 Loading Failed 状态，并提供 Retry / Leave 操作。</li>
        <li><strong>用户操作</strong>：
          <ul>
            <li>点击 Retry：重新提交或重新查询 Face 结果，进入 Face Loading Page；细则见 <a href="#48-face-loading-page">4.8 Face Loading Page</a>。</li>
            <li>点击 Leave：返回业务入口，不继续等待。</li>
          </ul>
        </li>
        <li><strong>重试后结果</strong>：
          <ul>
            <li>重试后仍无结果：继续展示 Loading Failed。</li>
            <li>查询返回 Face 失败：进入 Face Failed Page；细则见 <a href="#410-face-failed-page">4.10 Face Failed Page</a>。</li>
            <li>查询返回网络 / 系统异常：源文档未明确 Loading Failed Retry 后的异常展示形态；需按 App 统一网络 / 系统错误处理确认。</li>
          </ul>
        </li>
      </ul>
    </td>
  </tr>
</table>

关联：`KYC-LOADING-FAILED-001 ~ KYC-LOADING-FAILED-010`；Source：AIX KYC PRD 7.2.9。

---

### 4.10 Face Failed Page

认证失败后的说明页，覆盖 Passport、Face、POA 的失败展示和重试限制。

<table>
  <tr>
    <th width="48%">页面</th>
    <th width="52%">说明</th>
  </tr>
  <tr>
    <td valign="top">
      <img src="_assets/account-opening/image21.png" width="480" />
    </td>
    <td valign="top">
      <p><strong>失败展示状态</strong></p>
      <ul>
        <li><strong>进入前提</strong>：Face / Passport / POA 返回失败结果。</li>
        <li><strong>展示规则</strong>：
          <ul>
            <li>Face result 为 FAIL / EXPIRED / incomplete：展示 Face Comparison 错误码映射中的前端提示文案；映射见 <a href="#face-comparison">5.3 Face Comparison</a>。</li>
            <li>POA 失败：展示 POA error code 映射中的前端提示文案；映射见 <a href="#poa">5.3 POA</a>。</li>
            <li>Passport / Document Verification 失败：展示 Passport / Document Verification 错误码映射中的前端提示文案；映射见 <a href="#passport--document-verification">5.3 Passport / Document Verification</a>。</li>
            <li>Passport 与 Face 均失败：验收标准要求优先展示 Passport 原因。</li>
            <li>多个失败原因同时存在但不属于上述明确优先级：优先级源文档未完全明确，需产品 / 后端确认。</li>
          </ul>
        </li>
      </ul>

      <p><strong>用户操作</strong></p>
      <ul>
        <li>点击 Try again 且未锁定：重新触发 KYC 流程；当前流程图为 FaceFailed → Loading。</li>
        <li>点击 Try again 但已锁定：展示锁定提示，不允许重试。</li>
        <li>点击返回 / 关闭：历史原文为“返回到业务流程入口页”。是否存在返回上一流程节点的其他入口，源文档未明确。</li>
      </ul>

      <p><strong>锁定说明</strong></p>
      <ul>
        <li>命中 5 次限制：展示 Too many attempts / 安全锁提示。</li>
        <li>命中 10 次限制：展示 Too many attempts / 安全锁提示。</li>
        <li>命中接口层 20 次限制：展示锁定提示。</li>
      </ul>
    </td>
  </tr>
</table>

关联：错误码映射见 5.3；`KYC-FACE-FAILED-001 ~ KYC-FACE-FAILED-010`；Source：AIX KYC PRD 7.2.10 / 9。

---

### 4.11 Address Upload Page

Face 成功后进入本页，用户确认居住国家并上传地址证明。

<table>
  <tr>
    <th width="48%">页面</th>
    <th width="52%">说明</th>
  </tr>
  <tr>
    <td valign="top">
      <img src="_assets/account-opening/image22.png" width="480" />
      <br><br>
      <img src="_assets/account-opening/image23.jpeg" width="480" />
      <br><br>
      <img src="_assets/account-opening/image24.png" width="320" />
      <br><br>
      <img src="_assets/account-opening/image25.png" width="480" />
    </td>
    <td valign="top">
      <p><strong>Residence</strong></p>
      <ul>
        <li><strong>默认展示</strong>：回填 KYC 流程中已选择的居住国家。</li>
        <li><strong>点击 Residence</strong>：进入 Select Residence Country Page；选择国家后返回本页。</li>
        <li><strong>国家二次判断</strong>：
          <ul>
            <li>所选国家属于支持国家：继续 POA 提交流程。</li>
            <li>所选国家属于 phase 2 - waitlist / 不支持国家：展示本页 waitlist 拦截；见 <a href="#4111-拦截waitlist">4.11.1 拦截：Waitlist</a>。</li>
            <li>POA OCR 国家与用户填报居住国家不匹配：按 POA error code 映射展示文案；映射见 <a href="#poa">5.3 POA</a>。</li>
          </ul>
        </li>
      </ul>

      <p><strong>文件上传区域</strong></p>
      <ul>
        <li><strong>选择文件</strong>：支持 JPG / JPEG / PNG / PDF，单文件不超过 16MB。</li>
        <li><strong>本地校验失败</strong>：
          <ul>
            <li>文件格式错误：Toast <code>Unsupported file type. Please upload a JPG, JPEG, PNG, or PDF file.</code></li>
            <li>文件超过 16MB：Toast <code>File size exceeds the 16MB limit. Please choose a smaller file.</code></li>
          </ul>
        </li>
        <li><strong>上传结果</strong>：
          <ul>
            <li>上传成功：文件进入待提交状态。</li>
            <li>上传服务器报错：Toast <code>Server busy. Upload failed. Please try again.</code></li>
          </ul>
        </li>
        <li>当前验收标准要求只能上传一份，上传中可取消，已上传可删除和预览。</li>
      </ul>

      <p><strong>POA 提交</strong></p>
      <ul>
        <li><strong>点击提交前提</strong>：已上传合法 POA 文件，并完成居住国家确认。</li>
        <li><strong>提交成功</strong>：POA 文件和国家信息提交成功后，进入 KYC Submission Success Page；细则见 <a href="#412-kyc-submission-success-page">4.12 KYC Submission Success Page</a>。</li>
        <li><strong>提交失败 / 不可继续</strong>：
          <ul>
            <li>POA OCR 国家与用户填报居住国家不匹配：按 POA error code 映射展示文案；映射见 <a href="#poa">5.3 POA</a>。</li>
            <li>申请国家不属于支持国家 / 白名单：展示 waitlist 拦截；见 <a href="#4111-拦截waitlist">4.11.1 拦截：Waitlist</a>。</li>
            <li>POA 审核失败：记录失败原因，并按 POA error code 映射展示前端提示文案；映射见 <a href="#poa">5.3 POA</a>。</li>
            <li>POA 上传服务器报错：Toast <code>Server busy. Upload failed. Please try again.</code>，不进入 Success。</li>
            <li>POA 提交阶段网络 / 服务器异常：源文档未给出独立文案；需按 App 统一网络 / 系统错误处理确认。</li>
          </ul>
        </li>
      </ul>

      <p>POA 机审会 OCR 提取 POA 国家信息，核验其与用户填报居住国是否匹配，并校验申请国家是否属于白名单。</p>
    </td>
  </tr>
</table>

#### 4.11.1 拦截：Waitlist

<table>
  <tr>
    <th width="48%">页面</th>
    <th width="52%">说明</th>
  </tr>
  <tr>
    <td valign="top">
      <img src="_assets/account-opening/image26.png" width="360" />
    </td>
    <td valign="top">
      <p><strong>触发方式</strong></p>
      <p>Address Upload 阶段二次判断国家不支持时展示。</p>

      <p><strong>拦截状态</strong></p>
      <ul>
        <li><strong>处理结果</strong>：用户不能继续提交当前国家的 POA。</li>
        <li><strong>用户操作</strong>：
          <ul>
            <li>点击 Join waitlist：进入 Waitlist Page；提交细则见 <a href="#45-waitlist-page">4.5 Waitlist Page</a>。</li>
            <li>点击 Select other country：进入 Select Residence Country Page；细则见 <a href="#44-select-residence-country-page">4.4 Select Residence Country Page</a>。</li>
          </ul>
        </li>
      </ul>
    </td>
  </tr>
</table>

关联：POA upload token、POA 文件上传、`proofOfAddressVerifyStatus`；文件限制：JPG / JPEG / PNG / PDF，单文件 16MB；Source：AIX KYC PRD 7.2.11。

---

### 4.12 KYC Submission Success Page

POA 提交成功后的完成页，只表示资料已提交，不代表 KYC 已审核通过。

<table>
  <tr>
    <th width="48%">页面</th>
    <th width="52%">说明</th>
  </tr>
  <tr>
    <td valign="top">
      <img src="_assets/account-opening/image27.png" width="480" />
    </td>
    <td valign="top">
      <p><strong>提交成功状态</strong></p>
      <ul>
        <li><strong>进入前提</strong>：Address Upload Page 的 POA 文件和国家信息提交成功。</li>
        <li><strong>展示内容</strong>：告知用户资料已提交，等待审核结果。</li>
        <li><strong>用户操作</strong>：
          <ul>
            <li>点击完成 / 返回入口：关闭 KYC 流程并返回业务入口。</li>
            <li>关闭页面：返回入口，等待审核结果。</li>
          </ul>
        </li>
      </ul>

      <p><strong>状态边界</strong></p>
      <ul>
        <li>成功页不等同于 KYC Approved。</li>
        <li>成功页不代表 Wallet 能力全部可用。</li>
        <li>后续审核状态通过通知或业务入口状态感知；通知模板和触达规则当前未明确，见 <code>GAP-KYC-NOTIFICATION-001</code>。</li>
      </ul>
    </td>
  </tr>
</table>

关联：Under review、Approved、Rejected、failed；`KYC-SUCCESS-001 ~ KYC-SUCCESS-009`；Source：AIX KYC PRD 7.2.12。

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
| Waitlist | email 为空、格式错误、长度超过 103 字符时不提交并展示校验提示；提交成功后按 userId 加入 waitlist，记录 email、国家、来源（外部投放 / APP）、提交时间、设备指纹 ID，并推送数仓。 |
| 相机权限 | 已授权进入 AAI H5；未授权弹窗；永久拒绝可 open settings。 |
| Passport OCR | 扫描成功进入 Face Guide；扫描失败返回 Identity Verify；DTC 01009 / 01005 显示对应 toast。 |
| Face Guide | 5 次失败锁 20 分钟，10 次失败锁 24 小时，接口连续 20 次锁 20 分钟；人脸通过后清零。 |
| Face country 参数 | Continue 时后端获取 passport country；存在则使用，不存在默认 `sg`；前端调用 AAI H5 时传入 country。 |
| Face Scan | 同一 `signatureId` 最多重试 3 次；需要重来时重新 generate-url。 |
| Face Loading | Face 成功进入 Address Upload；Face result 为 FAIL / EXPIRED / incomplete 时进入 Face Failed；30 秒无结果进入 Loading Failed；网络异常进入 Network Error Page；系统异常进入 Server Error Page。 |
| Loading Failed | Retry 后进入 Face Loading 重新提交；Leave 返回业务入口。 |
| Face Failed | 按 passport、face、POA 错误码映射展示文案；passport 与 face 均失败时优先展示 passport 原因。 |
| Address Upload | 支持 JPG/JPEG/PNG/PDF，单文件 16MB，只能上传一份；上传中可取消；已上传可删除和预览。 |
| POA 提交 | POA 文件和国家信息提交成功后进入 Submission Success；申请国家不属于支持国家 / 白名单时展示 Address Upload Page 内 Waitlist 拦截；POA OCR 国家与填报居住国家不匹配或 POA 审核失败时按 POA error code 映射展示文案；POA 上传服务器报错展示 Toast：`Server busy. Upload failed. Please try again.`；POA 提交阶段网络 / 服务器异常的独立文案源文档未明确。 |
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
| Reverse Solicitation 50013 | 国家要求反向招揽但未传 `reverseSolicitation=T` | 点击认证 | 不生成验证 URL；前端提示文案源文档未明确 | DTC 返回 50013；用户需补 Declaration 声明后再继续 | 是 |
| Waitlist email 空 | Waitlist Page | 不输入 email | 提示空值 / 按钮禁用 | 不提交 | 是 |
| Waitlist email 格式错误 | Waitlist Page | 输入错误 email | 提示格式错误 | 不提交 | 是 |
| 相机未授权 | Identity Verify | 点击相机 | 权限弹窗 | 不进入 H5 | 是 |
| 相机永久拒绝 | OS 权限永久拒绝 | 点击 Allow access | 引导 open settings | 不进入 H5 | 是 |
| DTC 01009 | DTC 返回手机号重复 | 点击相机 | Toast：Mobile number already exists. | 不进入 H5 | 是 |
| Passport 失败 | AAI / DTC 返回 passport fail | 扫描护照 | 返回 Identity Verify Page；如后端返回 Passport / Document Verification 错误原因，展示 5.3 映射文案 | 记录失败 code | 是 |
| Face 成功 | Passport 成功且 face 通过 | 完成活体 | 进入 Address Upload | face 失败计数清零 | 是 |
| Face 失败 5 次 | 24 小时内 face fail 4 次 | 再次失败 | 锁 20 分钟 | 记录 lock | 是 |
| Face 失败 10 次 | 24 小时内 face fail 9 次 | 再次失败 | 锁 24 小时 | 记录 lock | 是 |
| Face 接口连续 20 次 | 24 小时内连续发起 19 次 | 再发起一次 | 锁 20 分钟 | 拦截后续发起 | 是 |
| Face Loading 超时 | Face 采集完成后无结果 | 等待 30 秒 | Loading Failed | 可 Retry | 是 |
| Loading Failed Retry | Loading Failed Page | 点击 Retry | 进入 Face Loading | 重新提交 | 是 |
| passport 与 face 均失败 | 后端返回两者失败 | 进入 Face Failed | 优先展示 passport 原因 | 展示映射文案 | 是 |
| POA 格式错误 | 上传非支持格式 | 选择文件 | Toast Unsupported file type | 不上传 | 是 |
| POA 超 16MB | 上传大文件 | 选择文件 | Toast File size exceeds | 不上传 | 是 |
| POA 上传失败 | DTC upload-file 返回 14004 / 14005，或上传服务器报错 | 点击 Continue | 上传服务器报错时 Toast：`Server busy. Upload failed. Please try again.`；14004 / 14005 的独立前端文案源文档未明确 | 不进入 Success | 是 |
| POA 国家不支持 | countryOfResidence 不属于支持国家 / 白名单 | 点击 Continue | Address Upload Page 内 Waitlist 拦截；Join waitlist 进入 Waitlist Page | 不提交成功 | 是 |
| POA 成功 | 文件合法且国家支持 | 点击 Continue | Submission Success | DTC 返回 requestId | 是 |
| webhook 延迟 | 外部 webhook 未及时返回 | 等待结果 | 停留 Loading；Face Loading 超过 30 秒进入 Loading Failed Page | query 兜底 / 轮询；Face Loading Retry 后重新提交或重新查询 | 是 |
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

## Source alignment additions

### A. KYC source rules confirmed

| 规则 | 结论 | 来源 |
|---|---|---|
| Waitlist | Waitlist 场景由弹窗提示调整为页面级拦截；被识别为 Waitlist 时停留在 Waitlist Page，不允许继续后续流程 | KYC changelog / Waitlist 处理方式 |
| Face Loading 超时 | Face Loading Page 等待超过 30 秒仍未收到检测结果，自动跳转 Face Loading Failed / Loading Failed Page | KYC changelog / 7.2.8 / 7.2.9 |
| Loading Failed Retry | 点击 Retry 后进入 Face Loading Page 重新提交，不返回 Face Scan | KYC / 7.2.9 |
| 申请单长期有效 | 申请单自创建后即长期有效；OCR、Face 等核心认证通过后，在 DTC 侧认证结果永久有效，不因时间推移失效 | KYC / 6.2 KYC状态机 |
| Passport / Face 成功不回退 | 只要 passport、face 认证通过，不会再变为失败状态 | KYC / 6.2 KYC状态机 |
| Face 失败锁定 | 24 小时内累计失败 5 次锁 20 分钟；累计失败 10 次锁 24 小时；接口层面连续发起 20 次锁 20 分钟，验证成功后清零 | KYC / 7.2.6 |
| Face 失败计数口径 | DTC 返回 face result=fail 才算失败，其他结果不算失败 | KYC / 7.2.6 |
| Face Failed 原因优先级 | passport 与 face 均失败时优先展示 passport 失败原因；POA 失败展示 POA error code 映射 | KYC / 7.2.10 |
| POA | AAI 机审提取 POA 资料，验证真实性、有效期，并校验 POA 国家与用户填报居住国是否匹配、申请国家是否白名单 | KYC / 7.2.11 |

### B. Home wallet panel mapping

| KYC 状态 | Home 钱包区域展示 | 行为 | 来源 |
|---|---|---|---|
| 无开户记录 / Pending | 显示未申请开通钱包面板；KYC 为空无 Tips，Pending 显示剩余步骤 | 点击 Activate wallet 进入钱包开通页面 | Home / 钱包区域 |
| Under Review | 显示审核中面板，Tips title 为 Verification is under reviewing，进度为 3 Steps Finished | 首页进入时局部静默刷新 | Home / 钱包区域 |
| Failed | 显示审核失败面板，后端 passport / face / POA 失败按对应错误码映射展示；任一验证项失败可重新开户 | 点击 Reactivate Now 进入钱包开通页面 | Home / 钱包区域 |
| Rejected | 显示审核拒绝面板；因风险被 DTC 拒绝的用户会被拦截开户且隐藏激活钱包入口 | 不允许再次提交 | Home / 钱包区域 |
| Approved | 显示审核通过 / 资产面板，后端获取全量钱包余额并展示稳定币资产 | 进入 Wallet 资产页 | Home / 钱包区域 |

### C. Card prerequisite mapping

| 规则 | 结论 | 来源 |
|---|---|---|
| 申卡前置 | 仅完成钱包开通、DTC 渠道开户、KYC 验证通过、刷脸 Token 有效、申卡 5 张以内的用户才能申请卡 | Card Application / 2.1 |
| KYC 与 Card 边界 | KYC 只维护开户 / 身份认证事实；卡申请、制卡费、卡类型和结果页由 card/application.md 维护 | Card Application |

### D. Source boundaries

- Security 身份认证 PRD 是 KYC 的支撑证据，但 KYC 钱包开户流程中的 Passport / Face / POA 页面和错误码以 KYC 主 PRD 为准。
- 删除线内容不沉淀为 confirmed fact，例如部分旧 Face 空值文案和锁定弹窗历史文案。

## 12. 来源引用

- (Ref: archive/legacy-prd/kyc/wallet-opening/README.md / 需求变更日志 / 国家线 / 6.2 KYC 状态机 / 7.2 开户页面逻辑 / 8 外部接口依赖 / 9 接口错误码映射 / 10 待确认事项)
- (Ref: archive/legacy-prd/app/home/README.md / Home 钱包区域展示逻辑)
- (Ref: archive/legacy-prd/card/application/README.md / 申卡前置条件)
- (Ref: archive/legacy-prd/security/identity-verification/README.md / 身份认证支撑能力)
- (Ref: external-docs/dtc/Master sub account 设计方案 (2).docx / KYC 流程 / DTC API / Master Account / Sub Account / D-SUB-ACCOUNT-ID / POA 文件上传流程 / 失败原因)
- (Ref: DTC Wallet OpenAPI Document20260126 / WalletConnect Token / D-SUB-ACCOUNT-ID / WalletAccount：本轮未上传，相关内容仅保留历史来源提示，不作为本轮核验事实)
- (Ref: prd-template/standard-prd-template.md / 标准 PRD 模板)
- (Ref: knowledge-base/integrations/aai/_index.md)
- (Ref: knowledge-base/integrations/dtc/_index.md)
- (Ref: knowledge-base/common/notification.md：Notification 规则待核验)
- (Ref: knowledge-base/changelog/knowledge-gaps.md / ALL-GAP-030 ~ ALL-GAP-035 / ALL-GAP-045 / ALL-GAP-046)
- (Ref: 用户确认结论 / 2026-05-02 / KYC 文件名不应带 wallet；新主事实源改为 account-opening.md)
