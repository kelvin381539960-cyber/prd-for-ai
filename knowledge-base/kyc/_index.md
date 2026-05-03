---
module: kyc
feature: kyc-index
version: "2.1"
status: active
source_doc: knowledge-base/kyc/account-opening.md；knowledge-base/common/aai.md；knowledge-base/changelog/knowledge-gaps.md；knowledge-base/_system-boundary.md；用户确认结论 2026-05-02；用户确认结论 2026-05-03
source_section: KYC 使用态目录结构；Account Opening / KYC；AAI Dependency；ALL-GAP 总表；system-boundary；KYC deprecated path cleanup
last_updated: 2026-05-03
owner: 吴忆锋
depends_on:
  - kyc/account-opening
  - common/aai
  - changelog/knowledge-gaps
  - _system-boundary
---

# KYC 模块索引

## 1. 模块定位

KYC 模块用于沉淀 AIX 中与身份认证、开户、账户准入、业务准入相关的事实和边界。

KYC 不归属于单一 Wallet 模块。它可能影响 Account、Card、Wallet、Deposit、Notification、Errors、人工处理和外部账户系统。

AAI 保留在 `common/aai.md`，作为外部供应商依赖边界；KYC 模块只引用 AIX 业务准入所需的 AAI 结果边界，不维护 AAI 内部逻辑。

DTC Master / Sub Account、`D-SUB-ACCOUNT-ID`、Wallet Account 与开户流程有关的运行时事实，主事实源为 `kyc/account-opening.md`。

## 2. 当前文件

| 文件 | 状态 | 定位 |
|---|---|---|
| `kyc/_index.md` | active | KYC 模块索引 |
| `kyc/account-opening.md` | active | Account Opening / KYC 开户与身份认证准入事实源 |
| `kyc/wallet-kyc.md` | removed / deprecated path | 历史 Wallet KYC 路径；当前 main 上不存在，不作为运行时主事实源 |

已迁出旧路径：

| 旧路径 | 当前处理 |
|---|---|
| `wallet/kyc.md` | 不作为运行时事实源；主事实源改为 `kyc/account-opening.md` |
| `kyc/wallet-kyc.md` | 历史路径；当前 main 上不存在，不作为运行时事实源 |

## 3. 与其他模块的边界

| 模块 | 关系 | 当前处理 |
|---|---|---|
| Account | KYC / 开户可能依赖账户基础信息、手机号绑定、用户身份 | 不补 Account 字段，缺口进入 ALL-GAP |
| Security | OTP、Face Auth、Passcode、设备权限等安全能力可能被 KYC 流程引用 | 引用 Security，不重复定义 |
| Card | Card 申卡可能依赖 KYC；是否复用 Account Opening / KYC 结果仍需确认 | 不默认等同，见 ALL-GAP-030 |
| Wallet | Wallet Balance / Deposit / WalletConnect / Receive 可能依赖开户、Sub Account 或 KYC 结果 | 主事实源为 `kyc/account-opening.md`；Wallet 目录不维护 KYC 主事实 |
| Common / AAI | AAI 是外部身份认证依赖 | 保留 `common/aai.md`，KYC 侧只引用 AIX 依赖结果 |
| Common / DTC | DTC 是 Master / Sub Account 与 Wallet Account 外部账户系统 | 保留 `common/dtc.md`，KYC 侧只记录开户相关边界 |
| Notification | KYC Approved / Rejected / Failed 通知已在开户事实源中记录；模板细节仍以 Notification 为准 | 见 `common/notification.md` 与 ALL-GAP-045 |

## 4. 待确认唯一来源

KYC 相关不确定项统一记录在：

`knowledge-base/changelog/knowledge-gaps.md`

当前核心引用：

| 编号 | 主题 | 当前处理 |
|---|---|---|
| ALL-GAP-030 | Wallet KYC 与 Card KYC 关系 | 仍保留，未确认复用 / 独立 / 部分复用 |
| ALL-GAP-031 | Wallet KYC 是否为 GTR / WalletConnect Deposit 前置 | 应拆分为产品入口前置、技术依赖、Sub Account 前置等 |
| ALL-GAP-032 | Wallet 开户触发时机 | Account Opening PRD 已可回填部分事实，剩余只保留“入口触发场景是否覆盖所有路径” |
| ALL-GAP-033 | KYC 失败 / 重试 / 人工处理规则 | 页面失败、Face 锁定可回填；只保留人工处理、原始错误码、补偿机制 |
| ALL-GAP-034 | KYC 结果是否触发通知 | 已有 PRD 依据，建议后续改为 resolved-by-source 并回填 Notification |
| ALL-GAP-035 | AIX 实际依赖哪些 AAI 结果 | 已可回填 Passport OCR、Liveness + Face Comparison、POA 等类别；字段映射仍待确认 |
| ALL-GAP-046 | AAI OCR / Liveness / KYC 状态和失败原因边界 | 页面级处理已确认；AAI 原始错误码仍待确认 |

## 5. 不写入事实的内容

以下内容不得写成事实：

1. Account Opening / KYC 与 Card KYC 完全相同。
2. Account Opening / KYC 与 AAI 内部 KYC 完全相同。
3. AIX user 与 DTC Sub Account 一定一一对应。
4. `D-SUB-ACCOUNT-ID` 与 WalletAccount.clientId 一定完全等价。
5. KYC Approved 一定立即创建 DTC Sub Account。
6. KYC Approved 一定代表 Wallet / Deposit / WalletConnect / Receive 全部可用。
7. AAI 内部审核逻辑、完整字段、完整错误码。
8. DTC Master / Sub Account 内部实现。

## 6. 使用规则

1. 查询开户、KYC、Sub Account、`D-SUB-ACCOUNT-ID`、Wallet Account 准入时，读 `kyc/account-opening.md`。
2. 查询 AAI 外部依赖时，读 `common/aai.md`。
3. 查询 DTC 外部账户边界时，读 `common/dtc.md`。
4. 查询未确认项时，读 `knowledge-base/changelog/knowledge-gaps.md`。
5. 查询责任边界时，读 `knowledge-base/_system-boundary.md`。
6. 不默认读取 `kyc/wallet-kyc.md`、moved notice、stage-review 或历史 checklist 文件；`kyc/wallet-kyc.md` 当前 main 上不存在，不作为运行时事实源。

## 7. 来源引用

- (Ref: knowledge-base/kyc/account-opening.md)
- (Ref: knowledge-base/common/aai.md)
- (Ref: knowledge-base/common/dtc.md)
- (Ref: knowledge-base/changelog/knowledge-gaps.md / ALL-GAP-030 ~ ALL-GAP-035 / ALL-GAP-046)
- (Ref: knowledge-base/_system-boundary.md)
- (Ref: 用户确认结论 / 2026-05-02 / KYC 文件名不应带 wallet；新主事实源改为 account-opening.md)
- (Ref: 用户确认结论 / 2026-05-03 / `kyc/wallet-kyc.md` 当前 main 上不存在，不作为运行时事实源)
