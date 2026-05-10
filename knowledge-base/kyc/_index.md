---
module: kyc
feature: kyc-index
version: "3.1"
status: active
source_doc: archive/legacy-prd/kyc/wallet-opening/README.md；archive/legacy-prd/app/home/README.md；archive/legacy-prd/card/application/README.md；archive/legacy-prd/security/identity-verification/README.md
source_section: KYC wallet opening；Home wallet panel；Card application prerequisite；Security identity verification
last_updated: 2026-05-09
owner: 吴忆锋
depends_on:
  - kyc/account-opening
  - integrations/aai
  - integrations/dtc
  - changelog/knowledge-gaps
  - _system-boundary
---

# KYC 模块索引

> Source alignment note: 本模块已按 converted-prd 做双向覆盖校验。主证据为 KYC 钱包开户 PRD，支撑证据包括 Home 钱包面板、Card 申卡前置条件和 Security 身份认证能力。


## 1. 模块定位

KYC 模块用于沉淀 AIX Account Opening / KYC 的运行态产品事实，包括开户准入、身份认证、国家线、协议、Passport OCR、Face、POA、DTC Master / Sub Account、AAI / DTC 外部依赖和业务准入边界。

KYC 不归属于单一 Wallet 模块。Wallet、Card、Deposit、WalletConnect、Receive 等能力可能依赖 KYC 结果，但这些能力的业务流程不在 KYC 目录内维护。

## 2. 当前文件

| 文件 | 状态 | 定位 |
|---|---|---|
| `kyc/_index.md` | active | KYC 模块索引 |
| `kyc/account-opening.md` | active | Account Opening / KYC 主事实源 |

## 3. 已清理文件原则

KYC 目录不保留 review、correction plan、stage review、临时 checklist、过程说明或迁移说明文件。

如果评审或修正方案中存在正式事实，必须迁移进 `kyc/account-opening.md` 或 `changelog/knowledge-gaps.md`；迁移后删除过程文件。

## 4. 与其他模块的边界

| 模块 | 关系 | 当前处理 |
|---|---|---|
| Account | KYC 可能依赖账户基础信息、手机号、邮箱、用户身份 | Account 主事实不在 KYC 内补写 |
| Security | OTP、Face Auth、Passcode、设备权限等安全能力可能被 KYC 流程引用 | 安全能力主事实在 `security/` |
| Card | Card Application 明确要求完成钱包开通、DTC 渠道开户和 KYC 验证通过后才能申卡 | 申卡资格见 card/application；KYC 不维护申卡流程 |
| Wallet | Home 钱包区域和 Wallet 能力依赖 KYC 状态；KYC Approved 后 Home 展示资产面板 | Wallet 主事实仍在 `wallet/`，Home 展示见 home/app-home |
| Integrations / AAI | AAI 是外部身份认证依赖 | AAI 内部逻辑在 `integrations/aai/_index.md` 维护边界 |
| Integrations / DTC | DTC 是 Master / Sub Account、KYC API、Wallet Account 外部依赖 | DTC 依赖边界在 `integrations/dtc/_index.md` |
| Notification | KYC Approved / Rejected / Failed 通知规则需引用 Notification 事实源 | KYC 不补通知模板 |

## 5. 查询入口规则

| 查询主题 | 优先读取 |
|---|---|
| 开户 / KYC 主流程 | `kyc/account-opening.md` |
| 国家线 / Phase / waitlist | `kyc/account-opening.md` 的国家线、Gap 与页面规则章节 |
| KYC Loading / Start / Identity / Face / POA 页面规则 | `kyc/account-opening.md` |
| AIX 页面状态、DTC clientStatus、EKycFileVerifyStatus | `kyc/account-opening.md` 的状态模型章节 |
| DTC KYC API / webhook / POA upload | `kyc/account-opening.md`，必要时联动 `integrations/dtc/_index.md` |
| AAI OCR / Liveness / Face / POA 外部依赖 | `kyc/account-opening.md`，必要时联动 `integrations/aai/_index.md` |
| DTC Master / Sub Account / D-SUB-ACCOUNT-ID | `kyc/account-opening.md`、`integrations/dtc/_index.md` |
| 未确认项 / 冲突项 | `changelog/knowledge-gaps.md` |
| 系统责任边界 | `_system-boundary.md` |

## 6. 不写入事实的内容

以下内容不得在 KYC 模块中写成事实：

1. Account Opening / KYC 与 Card KYC 完全相同。
2. Account Opening / KYC 与 AAI 内部 KYC 完全相同。
3. AIX user 与 DTC Sub Account 一定一一对应。
4. `D-SUB-ACCOUNT-ID` 与 WalletAccount.clientId 一定完全等价。
5. KYC Approved 通知一定代表 DTC Sub Account 创建成功。
6. KYC Approved 一定代表 Wallet / Deposit / WalletConnect / Receive 全部可用。
7. DTC Sub Account 创建失败时 AIX 一定有自动补偿。
8. AAI OCR / Face / POA 原始内部错误码已完整转译。
9. 未上传或未核验来源中的 WalletAccount / WalletConnect 细节。
10. Send / Swap 是当前 active 能力。

## Source alignment additions

| 证据 | 已覆盖内容 | 处理 |
|---|---|---|
| KYC 主 PRD | 国家线、KYC 状态机、开户页面、Passport、Face、POA、错误码、DTC 接口 | 已在 account-opening.md 覆盖 |
| Home PRD | Pending / Under Review / Failed / Rejected / Approved 钱包面板展示和 Reactivate Now / Activate wallet 入口 | 已补充到 account-opening.md 的 Home 映射 |
| Card Application PRD | 申卡前置依赖：完成钱包开通、DTC 开户、KYC 通过 | 已登记为跨模块依赖，不在 KYC 维护申卡流程 |
| Security PRD | 身份认证能力、Face Auth、OTP 等支撑 | 仅作为支撑证据；KYC 主流程 Face / OCR 仍以 KYC PRD 为准 |

## 7. 来源引用

- (Ref: archive/legacy-prd/kyc/wallet-opening/README.md；knowledge-base/kyc/account-opening.md)
- (Ref: knowledge-base/integrations/aai/_index.md)
- (Ref: knowledge-base/integrations/dtc/_index.md)
- (Ref: knowledge-base/changelog/knowledge-gaps.md)
- (Ref: knowledge-base/_system-boundary.md)
