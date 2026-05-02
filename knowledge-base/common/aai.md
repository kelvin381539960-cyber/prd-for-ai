---
module: common
feature: aai-dependency
version: "1.3"
status: active
source_doc: knowledge-base/common/_index.md；knowledge-base/kyc/account-opening.md；knowledge-base/changelog/knowledge-gaps.md；knowledge-base/_system-boundary.md；用户确认结论 2026-05-02
source_section: AAI Dependency；Account Opening / KYC；Passport OCR；Liveness + Face Comparison；POA；KYC 状态与失败边界；ALL-GAP-035 / ALL-GAP-046
last_updated: 2026-05-02
owner: 吴忆锋
depends_on:
  - common/_index
  - kyc/account-opening
  - changelog/knowledge-gaps
  - _system-boundary
---

# AAI Dependency 外部依赖边界

## 1. 功能定位

AAI 是 AIX 的外部身份认证 / KYC 供应商能力，不是 AIX 内部系统，也不是本知识库需要维护的供应商系统说明书。

本文只记录 AIX 在 Account Opening / KYC 等流程中实际需要感知和承接的 AAI 依赖边界，包括：Passport OCR、Liveness、Face Comparison、POA、KYC 结果类别、失败 / 重试 / 页面处理边界。

本文不维护：

1. AAI 内部审核逻辑。
2. AAI 完整接口字段。
3. AAI 完整错误码表。
4. AAI 算法、OCR、Liveness、Face Match 的供应商侧细节。
5. 未被 AIX 产品 / 后端 / 前端使用的供应商字段。
6. AAI 内部状态机。

Account Opening / KYC 的用户流程、页面状态、Sub Account、DTC Wallet Account、能力准入主事实源为：

`knowledge-base/kyc/account-opening.md`

## 2. 当前已确认边界

| 项目 | 当前结论 | AIX 侧处理 | 主事实源 |
|---|---|---|---|
| AAI 是外部依赖 | AAI 不是 AIX 内部系统 | AIX 只承接结果、状态和失败边界，不维护 AAI 内部实现 | `_system-boundary.md` |
| Passport OCR | Account Opening / KYC 流程中通过外部 H5 完成护照扫描 | AIX 处理页面跳转、权限、失败返回；不维护 OCR 内部识别逻辑 | `kyc/account-opening.md` |
| Liveness / Face capture | Face Scan Page 通过外部 H5 完成活体采集 | AIX 根据采集成功 / 失败进入 Face Loading 或 Face Failed | `kyc/account-opening.md` |
| Face Comparison | Face Loading Page 等待后端验证结果 | AIX 轮询 / 等待结果，并按成功 / 失败 / 超时分流 | `kyc/account-opening.md` |
| POA / Address Upload | Account Opening / KYC 流程包含 Address Upload / POA | AIX 承接页面与提交结果，AAI / KUN 侧识别和审核细节不在本文维护 | `kyc/account-opening.md` |
| KYC 结果通知 | KYC Approved / Rejected / Failed 会触发 Email / in-app notification / push | 通知模板、跳转和重试策略以 Notification 文件与 ALL-GAP 为准 | `kyc/account-opening.md`、`common/notification.md` |
| Face 失败锁定 | 24 小时内 Face 失败 5 次锁 20 分钟，10 次锁 24 小时；只统计 Face 失败，不含 passport 失败；人脸通过后清零 | AIX 可引用为页面级重试 / 锁定规则 | `kyc/account-opening.md` |

## 3. AIX 需要关心的 AAI 结果类别

以下不是 AAI 完整状态机，只是 AIX 侧需要承接的结果类别。

| 结果类别 | AIX 需要关心的原因 | 当前处理 |
|---|---|---|
| Passport OCR 成功 | 影响是否进入 Face Guide / 后续验证 | 可作为页面流转事实引用 |
| Passport OCR 失败 | 影响是否回到 Identity Verify | 可作为页面失败处理引用 |
| Face capture 成功 | 影响是否进入 Face Loading | 可作为页面流转事实引用 |
| Face capture 失败 | 影响是否进入 Face Failed | 可作为页面失败处理引用 |
| Face Comparison 成功 | 影响是否进入 Address Upload / POA | 可作为页面流转事实引用 |
| Face Comparison 失败 | 影响是否进入 Face Failed | 可作为页面失败处理引用 |
| Face 验证超时 | 30 秒无结果进入 Loading Failed | 可作为页面超时处理引用 |
| KYC Approved | 影响用户 KYC 结果、通知和后续能力准入判断 | 可引用，但不得推导所有 Wallet 能力必然可用 |
| KYC Rejected | 影响用户结果展示、通知和后续处理 | 可引用，但失败原因和人工处理仍需确认 |
| KYC Failed | 影响用户结果展示、通知、失败 / 重试处理 | 可引用，但 AAI 原始失败原因仍需确认 |
| Under review | 影响 Verification unavailable 和等待状态 | 可作为 AIX 页面分流状态引用 |

## 4. 与 AIX 业务模块的关系

| 模块 | 关系 | 当前处理 |
|---|---|---|
| KYC / Account Opening | AAI 支撑 Passport OCR、Liveness、Face Comparison、POA 等外部能力 | 主事实源为 `kyc/account-opening.md` |
| Account | KYC 可能依赖账户基础信息、手机号绑定、用户身份 | 不在 AAI 中补 Account 字段 |
| Security | 相机权限、OTP、Face Auth、Passcode 等属于 AIX 安全层能力 | 引用 Security，不在 AAI 重写 |
| Card | Card 申卡可能依赖 KYC / 身份认证 | 不默认复用为 Account Opening / KYC，见 ALL-GAP-030 |
| Wallet | Wallet Balance / Deposit / WalletConnect / Receive 可能依赖开户、Sub Account 或 KYC 结果 | 主事实源为 `kyc/account-opening.md`；不在 AAI 中补 Wallet 准入规则 |
| Deposit | GTR / WalletConnect 是否在产品入口强制 KYC / Account Opening 仍需确认 | 见 ALL-GAP-031 |
| Notification | KYC Approved / Rejected / Failed 有通知规则 | 模板、跳转、补发策略以 Notification 文件和 ALL-GAP-045 为准 |
| Errors | 页面级失败已在 `account-opening.md` 回填；AAI 原始错误码仍未完整确认 | 见 ALL-GAP-046 |

## 5. 不写入事实的内容

以下内容不得写成事实：

1. Account Opening / KYC 与 Card KYC 完全相同。
2. Account Opening / KYC 与 AAI 内部 KYC 完全相同。
3. AAI KYC 内部状态枚举已完整确认。
4. AAI OCR / Liveness / Face Match 的原始字段和错误码已完整确认。
5. KYC Approved 一定立即创建 DTC Sub Account。
6. KYC Approved 一定代表 Wallet / Deposit / WalletConnect / Receive 全部可用。
7. AAI 内部审核逻辑。
8. AAI 未提供但由 AIX 推测的字段、状态或错误码。
9. 与 AIX 系统设计无关的供应商字段。
10. Face Authentication 规则在 Common / AAI 中重新定义。

## 6. ALL-GAP 映射

本文不维护本地 `AAI-GAP-*` 表。所有未确认项统一进入 `knowledge-base/changelog/knowledge-gaps.md`。

| ALL-GAP | 主题 | 当前处理 |
|---|---|---|
| ALL-GAP-030 | Account Opening / KYC 与 Card KYC 关系 | 仍未确认复用 / 独立 / 部分复用 |
| ALL-GAP-031 | Account Opening / KYC 是否为 GTR / WalletConnect Deposit 前置 | 应拆分产品入口前置、技术依赖、Sub Account 前置等 |
| ALL-GAP-033 | KYC 失败 / 重试 / 人工处理规则 | 页面级失败与 Face 锁定已回填；人工处理、外部错误码仍需确认 |
| ALL-GAP-035 | AIX 实际依赖哪些 AAI 结果 | 已回填结果类别；字段、状态、失败原因映射仍需确认 |
| ALL-GAP-046 | AAI OCR / Liveness / KYC 状态和失败原因边界 | 页面级处理已回填；AAI 原始状态 / 错误码仍需确认 |

## 7. 使用规则

1. 查询 AAI 外部依赖边界时，读本文。
2. 查询开户、KYC、页面状态、Sub Account、能力准入时，读 `kyc/account-opening.md`。
3. 查询 AAI / AIX / DTC / KUN 责任边界时，读 `knowledge-base/_system-boundary.md`。
4. 查询未确认项时，读 `knowledge-base/changelog/knowledge-gaps.md`。
5. 不默认读取旧 `wallet/kyc.md`、`kyc/wallet-kyc.md`、stage-review 或本地 AAI-GAP 表。

## 8. 来源引用

- (Ref: knowledge-base/kyc/account-opening.md / Account Opening / KYC / Passport OCR / Face / POA / 通知 / 错误处理)
- (Ref: knowledge-base/common/_index.md)
- (Ref: knowledge-base/changelog/knowledge-gaps.md / ALL-GAP-030 / ALL-GAP-031 / ALL-GAP-033 / ALL-GAP-035 / ALL-GAP-046)
- (Ref: knowledge-base/_system-boundary.md)
- (Ref: 用户确认结论 / 2026-05-02 / KYC 文件名不应带 wallet；AAI 只保留 AIX 设计相关外部依赖边界)
