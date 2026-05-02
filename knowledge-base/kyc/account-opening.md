---
module: kyc
feature: account-opening
version: "1.0"
status: active
source_doc: 历史prd/AIX WALLET 钱包开户KYC需求V1.0 (1).docx；DTC接口文档/Master sub account 设计方案 (2).docx；DTC接口文档/DTC Wallet OpenAPI Document20260126 (1).docx；knowledge-base/common/aai.md；knowledge-base/common/dtc.md；knowledge-base/changelog/knowledge-gaps.md；用户确认结论 2026-05-02
source_section: AIX Wallet Account Opening & KYC；KYC 状态机；开户页面逻辑；Master / Sub Account；D-SUB-ACCOUNT-ID；WalletAccount；Notification；ALL-GAP-030 ~ ALL-GAP-035 / ALL-GAP-046
last_updated: 2026-05-02
owner: 吴忆锋
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

# Account Opening / KYC 开户与身份认证准入

## 1. 文档定位

本文是 AIX Account Opening / KYC 的运行时事实源，用于沉淀：

1. AIX 钱包开户与 KYC 的用户流程。
2. KYC 页面、状态、失败、重试和提交规则。
3. AIX App / AIX Platform / KUN / AAI / DTC / AIX Ledger 的系统交互边界。
4. DTC Master / Sub Account、`D-SUB-ACCOUNT-ID`、Wallet Account 的账户模型边界。
5. KYC / 开户结果对 Wallet、Deposit、WalletConnect、Balance、Receive 等能力的准入影响。
6. 仍未确认的问题与 ALL-GAP 的关系。

本文替代原 `knowledge-base/kyc/wallet-kyc.md` 的主事实源定位。旧文件名中的 `wallet-kyc` 容易误导 AI 将该能力理解为 Wallet 模块子能力；实际范围应是 KYC 目录下的开户、身份认证和业务准入边界。

本文不维护 AAI / DTC / KUN 的完整供应商说明书；只记录 AIX 需要感知、展示、调用、接收、判断和处理的事实。

## 2. 已确认事实摘要

| 事实 | 当前结论 | 来源 |
|---|---|---|
| AIX 存在 Account Opening & KYC 流程 | 流程涉及 AIX App、AIX Platform、AIX Ledger、KUN、AAI 等角色 | AIX WALLET 钱包开户 KYC PRD |
| KYC 不是单一页面 | 覆盖 KYC Loading、Start、Select Residence Country、Waitlist、Identity Verify、Identity Scan、Face Guide、Face Scan、Face Loading、Loading Failed、Face Failed、Address Upload、KYC Submission Success 等页面 | AIX WALLET 钱包开户 KYC PRD / 开户页面逻辑 |
| KYC 状态影响页面分流 | `Under review` / `Rejected` / `Approved` 展示 Verification unavailable；`Pending` / `failed` 继续 KYC 流程 | AIX WALLET 钱包开户 KYC PRD / KYC Loading Page |
| 支持居住国家有限 | 支持 AU / PH / VN；其他国家进入 waitlist | AIX WALLET 钱包开户 KYC PRD / Select Residence Country / Waitlist |
| KYC 依赖外部身份验证能力 | Passport OCR、Liveness + Face Comparison、POA 等结果由 AIX 通过 KUN / AAI 链路承接 | AIX WALLET 钱包开户 KYC PRD / AAI 相关流程 |
| Face 失败有锁定规则 | 24 小时内 face 失败 5 次锁 20 分钟，10 次锁 24 小时；只统计 face 失败，不含 passport 失败；人脸通过后清零 | AIX WALLET 钱包开户 KYC PRD / Face Guide Page |
| KYC 结果会触发通知 | Approved、Rejected、Failed 均有 Email / in-app notification / push 相关规则 | AIX WALLET 钱包开户 KYC PRD / Notification 相关描述 |
| DTC Sub Account 是后续 Wallet 能力的重要账户上下文 | DTC API 中存在 `D-SUB-ACCOUNT-ID`，定义为 master account 下注册的 sub account id；WalletConnect token 也依赖该 header | Master sub account 方案 / DTC Wallet OpenAPI |
| WalletAccount 有明确字段 | 包含 `id`、`clientId`、`status`、`currency`、`balance`、`label`、`createdDate`、`lastUpdatedDate` 等 | DTC Wallet OpenAPI / WalletAccount |

## 3. 用户侧开户 / KYC 流程

### 3.1 主流程

```text
进入 KYC Loading
→ 判断当前 KYC / 开户状态
→ 进入 KYC Start
→ 选择居住国家
→ 勾选协议
→ 进入 Identity Verify
→ Passport OCR / Identity Scan
→ Face Guide
→ Face Scan / Liveness
→ Face Loading / 后台轮询验证结果
→ Address Upload / POA
→ KYC Submission Success
→ 等待审核 / 结果通知
```

### 3.2 页面流程表

| 步骤 | 页面 / 场景 | 用户动作 | AIX 侧处理 | 外部依赖 | 结果 |
|---|---|---|---|---|---|
| 1 | KYC Loading Page | 进入 KYC 流程 | 查询用户当前 KYC / 开户状态 | AIX Backend / KYC 状态服务 | 按状态分流 |
| 2 | Verification unavailable | 无继续验证动作 | 若状态为 `Under review` / `Rejected` / `Approved`，展示不可继续验证 | AIX Backend | 用户无法重复提交当前流程 |
| 3 | KYC Start Page | 点击开始验证 | 若手机号未绑定，先引导绑定手机号；已绑定则进入 Start | AIX Account / Security | 进入国家选择 |
| 4 | Select Residence Country | 选择居住国家 | 默认使用 IP 检测国家；检测不到默认 SG；只支持 AU / PH / VN | AIX App / 配置 | 支持国家继续；非支持国家进入 waitlist |
| 5 | Agreement | 勾选协议 | 协议默认不勾选；未勾选按钮不可点，勾选后可继续 | AIX App | 进入 Identity Verify |
| 6 | Waitlist Page | 提交 email | 校验 email 非空、格式、长度；按 userId 加入 waitlist，并记录国家、来源、提交时间、设备指纹等 | AIX Backend | 用户无法继续申请 KYC |
| 7 | Identity Verify Page | 点击相机 | 判断相机权限；无权限弹窗；永久拒绝引导 open settings | AIX App / OS 权限 | 授权后进入 AAI H5 护照扫描 |
| 8 | Identity Scan Page | 扫描护照 | 通过外部 H5 完成 Passport OCR | AAI / KUN | 成功进入 Face Guide；失败回 Identity Verify |
| 9 | Face Guide Page | 点击开始人脸验证 | 判断 face 失败次数与锁定规则 | AIX App / AIX Backend | 未锁定进入 Face Scan；锁定则展示限制 |
| 10 | Face Scan Page | 完成活体采集 | 通过外部 H5 完成 Liveness / Face capture | AAI / KUN | 成功进入 Face Loading；失败进入 Face Failed |
| 11 | Face Loading Page | 等待结果 | 后台轮询验证结果；30 秒无结果进入 Loading Failed | AIX Backend / AAI / KUN | 成功进入 Address Upload；失败进入 Face Failed |
| 12 | Address Upload Page | 上传地址证明 / POA | 采集或提交地址证明材料 | AIX / KUN / AAI | 成功后进入 Submission Success |
| 13 | KYC Submission Success | 等待审核结果 | AIX 记录提交结果，并等待后续审核状态 | AIX Backend / KYC 服务 | 后续通过通知或入口状态感知结果 |

## 4. KYC 状态机

### 4.1 当前已知状态

| 状态 | 当前含义 | 页面处理 | 是否可继续 KYC |
|---|---|---|---|
| `Pending` | 用户仍可继续或重新进入 KYC 流程 | KYC Loading 后进入后续流程 | 是 |
| `failed` | 上次流程失败，但仍允许按规则继续 | KYC Loading 后进入后续流程 | 是 |
| `Under review` | 已提交，等待审核 | Verification unavailable | 否 |
| `Rejected` | 审核被拒绝 | Verification unavailable | 否 |
| `Approved` | 审核通过 | Verification unavailable | 否 |

### 4.2 状态使用边界

1. 上表是 AIX 页面分流语义，不等同于 AAI / DTC / KUN 的完整内部状态机。
2. 状态字段名、后端存储位置、状态转换触发点仍需以后端实现或接口文档确认。
3. `Rejected` 与 `failed` 不应混用：当前页面规则显示两者在 KYC Loading 分流上不同。
4. `Approved` 代表 KYC 已通过，但不自动推导所有 Wallet / Deposit / Card 能力全部可用。

## 5. 页面与交互规则

### 5.1 KYC Loading Page

| 规则 | 当前结论 |
|---|---|
| 默认展示 | 用户进入 KYC 默认为 loading |
| 状态分流 | `Under review` / `Rejected` / `Approved` → Verification unavailable；`Pending` / `failed` → 继续 KYC 流程 |
| 网络异常 | 进入 Network Error |
| 系统异常 | 进入 Server Error |
| 超时 | 等待超过 30 秒进入 Loading Failed Page |

### 5.2 Select Residence Country

| 规则 | 当前结论 |
|---|---|
| 默认国家 | 使用 IP 检测国家；检测不到默认 SG |
| 支持国家 | AU / PH / VN |
| 非支持国家 | 进入 waitlist 流程 |
| 协议勾选 | 默认不勾选；未勾选按钮不可点；勾选后可继续 |

### 5.3 Waitlist

| 规则 | 当前结论 |
|---|---|
| email 长度 | 最长 103 字符 |
| email 校验 | 非空、格式校验 |
| 提交后处理 | 用户无法继续申请 KYC |
| 后端记录 | userId、email、国家、来源、提交时间、设备指纹等 |

### 5.4 Identity Verify / Identity Scan

| 规则 | 当前结论 |
|---|---|
| 相机权限 | 点击相机前判断权限 |
| 未授权 | 弹窗提示 |
| 永久拒绝 | 引导 open settings |
| 扫描方式 | 外部 H5 护照扫描 |
| 扫描成功 | 进入 Face Guide |
| 扫描失败 | 回到 Identity Verify |

### 5.5 Face Guide / Face Scan / Face Loading

| 规则 | 当前结论 |
|---|---|
| 失败次数统计 | 只统计 face 失败，不含 passport 失败 |
| 5 次失败 | 24 小时内 face 失败 5 次，锁 20 分钟 |
| 10 次失败 | 24 小时内 face 失败 10 次，锁 24 小时 |
| 计数清零 | 人脸通过后清零 |
| 活体采集成功 | 进入 Face Loading |
| 活体采集失败 | 进入 Face Failed |
| Face Loading | 后台轮询验证结果 |
| 30 秒无结果 | 进入 Loading Failed Page |
| 验证成功 | 进入 Address Upload Page |
| 验证失败 | 进入 Face Failed Page |

## 6. AIX / KUN / AAI 系统交互

### 6.1 系统角色

| 系统 / 角色 | 当前定位 | 不维护内容 |
|---|---|---|
| AIX App | 承载用户页面、权限、交互、状态展示、跳转 | 不判断 AAI 内部识别逻辑 |
| AIX Platform / Backend | 初始化流程、接收结果、轮询状态、控制页面分流、记录用户状态 | 不维护供应商内部状态机 |
| KUN | KYC 会话或供应商链路承接方 | 不维护 KUN 内部实现 |
| AAI | Passport OCR、Liveness、Face Comparison、POA 等外部能力 | 不维护 AAI 完整字段、错误码、算法 |
| AIX Ledger | 与开户 / 账户 / 钱包能力相关的内部账务或账户承接角色 | 具体字段和实现待确认 |
| DTC | Master / Sub Account、Wallet Account、后续 Wallet 能力的外部账户系统 | 不维护 DTC 内部系统逻辑 |

### 6.2 系统交互边界

```text
AIX App
→ AIX Platform / Backend
→ KUN / AAI 初始化或承接 KYC 能力
→ AAI H5 完成 Passport OCR / Liveness / Face Comparison / POA
→ AIX Backend 接收或轮询结果
→ AIX 根据结果展示状态、控制准入、触发通知
→ 后续如需 Wallet 能力，依赖 DTC Sub Account / Wallet Account 上下文
```

当前不能推导：

1. AIX 是否直接调用 AAI，还是全部经 KUN 中转。
2. KUN 与 DTC Master / Sub Account 创建的准确调用顺序。
3. KYC Approved 是否必然立即创建 DTC Sub Account。
4. DTC Sub Account 创建失败时 AIX 的补偿机制。

以上内容若源文档未明确，应保留为 ALL-GAP。

## 7. DTC Master / Sub Account 模型

### 7.1 当前已确认边界

| 对象 | 当前理解 | 来源 / 备注 |
|---|---|---|
| Master Account | DTC 账户体系中的主账户；Sub Account 注册在 Master Account 下 | Master sub account 方案 / DTC header 定义 |
| Sub Account | 注册在 Master Account 下的子账户 | `D-SUB-ACCOUNT-ID` 定义 |
| `D-SUB-ACCOUNT-ID` | DTC 请求头，表示 master account 下注册的 sub account id | DTC API / WalletConnect token |
| clientId | DTC Wallet 相关客户标识；WalletConnect token 文档将 `D-SUB-ACCOUNT-ID` 描述为 dtcpay wallet 下注册的 client_id | DTC Wallet OpenAPI |
| Wallet Account | DTC 钱包账户对象，包含 id、clientId、status、currency、balance 等 | DTC WalletAccount |

### 7.2 与 AIX 的关系

```text
AIX User
→ Account Opening / KYC
→ 外部 KYC 结果 Approved / Failed / Rejected / Under review
→ DTC Sub Account / Wallet Account 上下文
→ Wallet Balance / Deposit / WalletConnect / History 等能力
```

注意：以上是账户模型边界，不代表所有箭头的创建顺序均已确认。创建时机、失败补偿、重试机制和字段映射仍需逐项确认。

## 8. Wallet Account / ClientId / D-SUB-ACCOUNT-ID 字段边界

| 字段 / 对象 | 所属系统 | 当前含义 | 关系与边界 | 状态 |
|---|---|---|---|---|
| AIX userId | AIX | AIX 用户标识 | Waitlist 等逻辑按 userId 处理；与 DTC sub account 映射字段待确认 | 部分确认 |
| KYC session | AIX / KUN / AAI | KYC 流程会话 | 是否由 KUN 创建、字段名是什么仍需确认 | 待确认 |
| AAI result | AAI / KUN | OCR / Face / POA / KYC 结果 | AIX 只承接结果，不维护内部逻辑 | 部分确认 |
| DTC Master Account | DTC | 主账户 | AIX 是否作为 master、或由 DTC 为 AIX 配置 master，需确认 | 待确认 |
| DTC Sub Account | DTC | master 下子账户 | 与 AIX user 是否一一对应需确认 | 待确认 |
| `D-SUB-ACCOUNT-ID` | DTC Header | sub account id / client_id 语义 | 后续 DTC Wallet / WalletConnect 请求依赖该 header | 部分确认 |
| WalletAccount.id | DTC | Wallet Account ID | 与 clientId / sub account 的关系需确认 | 部分确认 |
| WalletAccount.clientId | DTC | Wallet Account 的 clientId | 与 `D-SUB-ACCOUNT-ID` 的等价关系不能直接写死 | 部分确认 |
| WalletAccount.status | DTC | Wallet Account 状态 | 具体枚举和 AIX 展示映射需确认 | 待确认 |
| WalletAccount.currency | DTC | 钱包币种 | 可作为 Wallet Account 字段引用 | 确认 |
| WalletAccount.balance | DTC | 当前余额 | 可作为 Wallet Account 字段引用；余额可用性规则另见 Wallet Balance | 确认 |
| WalletAccount.createdDate | DTC | 创建时间 | 可引用字段 | 确认 |
| WalletAccount.lastUpdatedDate | DTC | 更新时间 | 可引用字段 | 确认 |

## 9. KYC 结果与能力准入

| 能力 | 与 KYC / 开户的关系 | 当前处理 |
|---|---|---|
| Wallet 首页 / Balance | 可能依赖 Wallet Account / Sub Account 是否已创建、状态是否可用 | 字段和准入细节见 Wallet Balance；不在本文补余额规则 |
| GTR / Exchange Deposit | 是否要求 KYC Approved / Sub Account 已创建，需按产品入口和后端规则确认 | 见 ALL-GAP-031 拆分项 |
| WalletConnect Deposit | 技术链路依赖 `D-SUB-ACCOUNT-ID`；是否作为 App 入口前置拦截需确认 | 见 ALL-GAP-031 拆分项 |
| Receive | 是否要求 KYC Approved / Sub Account 已创建未确认 | 见 Receive 相关 ALL-GAP |
| Send / Swap | 当前 deferred | 不纳入 active KYC 准入范围 |
| Card | Card KYC 与 Wallet / Account Opening KYC 是否复用未确认 | 见 ALL-GAP-030 |
| Notification | KYC Approved / Rejected / Failed 有通知规则 | 可回填到 Notification 事实源 |

## 10. 通知规则

当前可确认：KYC 结果会触发通知，至少覆盖以下结果：

| 结果 | 通知渠道 | 说明 |
|---|---|---|
| KYC Approved | Email / in-app notification / push | 开户成功 / KYC 状态变更为 Approved |
| KYC Rejected | Email / in-app notification / push | 开户被拒绝 / 状态为 Rejected |
| KYC Failed | Email / in-app notification / push | 开户失败 / 状态为 Failed |

边界：

1. 通知模板、参数、跳转目标应以 `common/notification.md` 或 Notification 原文为准。
2. KYC 通知不等同于 DTC Sub Account 一定已创建成功。
3. KYC Approved 通知不自动代表所有 Wallet 能力均可用。
4. 通知失败重试 / 补发策略仍见 ALL-GAP-045。

## 11. 错误 / 失败 / 重试 / 锁定 / 人工处理

| 场景 | 当前规则 | 是否确认 |
|---|---|---|
| KYC Loading 网络异常 | 进入 Network Error | 确认 |
| KYC Loading 系统异常 | 进入 Server Error | 确认 |
| KYC Loading 超过 30 秒 | 进入 Loading Failed Page | 确认 |
| Passport OCR 扫描失败 | 回到 Identity Verify Page | 确认 |
| Face Scan 采集失败 | 进入 Face Failed Page | 确认 |
| Face Loading 验证失败 | 进入 Face Failed Page | 确认 |
| Face Loading 超过 30 秒 | 进入 Loading Failed Page | 确认 |
| 24 小时内 Face 失败 5 次 | 锁定 20 分钟 | 确认 |
| 24 小时内 Face 失败 10 次 | 锁定 24 小时 | 确认 |
| 人脸通过 | face 失败计数清零 | 确认 |
| AAI 原始错误码 | 未完整转译 | 待确认 / ALL-GAP-046 |
| DTC Sub Account 创建失败 | 当前未确认 | 待确认 |
| KYC 人工审核 / 人工处理规则 | 当前未完全确认 | 待确认 / ALL-GAP-033 |

## 12. 系统责任边界

| 范围 | AIX 责任 | 外部系统责任 |
|---|---|---|
| 页面展示 | 展示 KYC 页面、状态、失败、重试、锁定、waitlist、通知跳转 | 无 |
| 权限处理 | 相机权限判断、弹窗、open settings 引导 | OS 权限系统实际授权 |
| KYC 初始化 | 发起流程、承接会话、展示结果 | KUN / AAI 执行具体 OCR / Face / POA 能力 |
| 身份识别 | 接收并处理外部结果 | AAI / KUN 执行识别、比对、审核相关能力 |
| 账户模型 | 保存 AIX user 与外部账户上下文的关系 | DTC Master / Sub Account / Wallet Account 外部账户体系 |
| 能力准入 | 根据已确认状态控制 AIX 页面和入口 | 外部系统提供状态、账户、结果 |
| 通知 | 触发和展示 AIX 通知 | Notification 服务投递，外部渠道实际到达可能另有失败策略 |
| 错误处理 | 展示错误页、限制重试、引导用户 | AAI / DTC / KUN 返回失败结果或异常 |

## 13. 不得推导的内容

以下内容不得在没有来源时写成事实：

1. Wallet KYC 与 Card KYC 完全相同。
2. Wallet KYC 与 AAI KYC 完全相同。
3. AIX user 与 DTC Sub Account 一定一一对应。
4. `D-SUB-ACCOUNT-ID` 与 WalletAccount.clientId 一定完全等价。
5. KYC Approved 一定立即创建 DTC Sub Account。
6. KYC Approved 一定代表 Wallet / Deposit / WalletConnect / Receive 全部可用。
7. DTC Sub Account 创建失败时 AIX 一定有自动补偿。
8. KYC Failed / Rejected 的所有失败原因已完整枚举。
9. AAI OCR / Face / POA 原始错误码已完整转译。
10. WalletConnect / GTR Deposit 的产品入口一定以 KYC Approved 为前置。
11. Notification 成功代表用户一定收到消息。
12. Send / Swap 是当前 active 能力。

## 14. 未确认项 / ALL-GAP

### 14.1 仍保留的 ALL-GAP

| 编号 | 主题 | 当前处理 |
|---|---|---|
| ALL-GAP-030 | Wallet KYC 与 Card KYC 关系 | 保留，仍未从当前材料确认复用 / 独立 / 部分复用 |
| ALL-GAP-031 | Wallet KYC 是否为 GTR / WalletConnect Deposit 前置 | 需要拆分为产品准入与技术依赖；WalletConnect 技术链路依赖 `D-SUB-ACCOUNT-ID`，但入口拦截规则仍需确认 |
| ALL-GAP-033 | KYC 失败 / 重试 / 人工处理规则 | 页面级失败与 face 锁定已确认；人工处理、DTC / AAI 原始错误码仍需确认 |
| ALL-GAP-035 | AIX 实际依赖哪些 AAI 结果 | 已确认 Passport OCR、Liveness + Face Comparison、POA 等类别；字段与错误码边界仍需确认 |
| ALL-GAP-046 | AAI OCR / Liveness / KYC 状态和失败原因边界 | 页面级处理已确认；AAI 原始状态 / 失败原因仍需确认 |

### 14.2 建议调整的 ALL-GAP

| 编号 | 建议 |
|---|---|
| ALL-GAP-031 | 拆分为：Deposit 产品入口前置、WalletConnect 技术依赖 `D-SUB-ACCOUNT-ID`、GTR 前置、DTC Sub Account 前置 |
| ALL-GAP-032 | Wallet 开户触发时机已有 PRD 页面流程支撑，应部分改为 resolved-by-source；剩余只保留“入口触发场景是否覆盖所有路径” |
| ALL-GAP-033 | 将已确认的失败 / 重试 / lock 规则回填；只保留人工处理、原始错误码、补偿机制 |
| ALL-GAP-034 | KYC 结果通知已确认，应改为 resolved-by-source，并同步回填 Notification |
| ALL-GAP-035 | 已确认结果类别后，应缩小为“字段、状态、失败原因和映射边界” |

## 15. 来源引用

- (Ref: 历史prd/AIX WALLET 钱包开户KYC需求V1.0 (1).docx / 6.1 账户结构说明 / 6.2 KYC 状态机 / 7.1 开户业务流程 / 7.2 开户页面逻辑 / 8 外部接口依赖 / 9 接口错误码映射 / 10 待确认事项)
- (Ref: DTC接口文档/Master sub account 设计方案 (2).docx / Master Account / Sub Account / D-SUB-ACCOUNT-ID)
- (Ref: DTC接口文档/DTC Wallet OpenAPI Document20260126 (1).docx / WalletConnect Token / D-SUB-ACCOUNT-ID / WalletAccount)
- (Ref: knowledge-base/common/aai.md)
- (Ref: knowledge-base/common/dtc.md)
- (Ref: knowledge-base/common/notification.md)
- (Ref: knowledge-base/changelog/knowledge-gaps.md / ALL-GAP-030 ~ ALL-GAP-035 / ALL-GAP-045 / ALL-GAP-046)
- (Ref: 用户确认结论 / 2026-05-02 / KYC 文件名不应带 wallet；新主事实源改为 account-opening.md)
