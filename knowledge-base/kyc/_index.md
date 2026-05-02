---
module: kyc
feature: kyc-index
version: "1.0"
status: active
source_doc: IMPLEMENTATION_PLAN.md；knowledge-base/wallet/kyc.md；knowledge-base/common/aai.md；knowledge-base/changelog/knowledge-gaps.md；用户确认结论 2026-05-02
source_section: KYC 独立目录结构调整；Wallet KYC v1.1；AAI Dependency v1.2；ALL-GAP 总表
last_updated: 2026-05-02
owner: 吴忆锋
depends_on:
  - kyc/wallet-kyc
  - common/aai
  - changelog/knowledge-gaps
---

# KYC 模块索引

## 1. 模块定位

KYC 模块用于沉淀 AIX 中与身份认证、钱包开户、业务准入相关的 KYC 事实和边界。

KYC 不归属于单一 Wallet 模块。它可能影响 Account、Card、Wallet、Deposit、通知、错误处理和人工处理。

AAI 仍保留在 `common/aai.md`，作为外部供应商依赖边界；KYC 模块只引用 AIX 业务准入所需的 AAI 结果边界，不维护 AAI 内部逻辑。

## 2. 当前文件

| 文件 | 状态 | 定位 |
|---|---|---|
| `kyc/_index.md` | active | KYC 模块索引 |
| `kyc/wallet-kyc.md` | active | Wallet KYC / 钱包开户准入边界 |

兼容入口：

| 旧路径 | 当前处理 |
|---|---|
| `wallet/kyc.md` | 已迁移为兼容入口，主事实源改为 `kyc/wallet-kyc.md` |

## 3. 与其他模块的边界

| 模块 | 关系 | 当前处理 |
|---|---|---|
| Account | KYC 可能依赖账户基础信息 | 不补字段，缺口进入 ALL-GAP |
| Security | OTP、Face Auth、Passcode 等安全能力可被 KYC 流程引用 | 引用 Security，不重复定义 |
| Card | Card 申卡可能依赖 KYC | 不默认等同 Wallet KYC |
| Wallet | Wallet 开户 / Deposit 准入可能依赖 KYC | 事实源为 `kyc/wallet-kyc.md` |
| Common / AAI | AAI 是外部供应商依赖 | 保留 `common/aai.md`，KYC 侧引用 |
| Notification | KYC 结果是否通知未确认 | 见 ALL-GAP-034 |

## 4. 待确认唯一来源

KYC 相关不确定项统一记录在：

`knowledge-base/changelog/knowledge-gaps.md`

当前核心引用：

| 编号 | 主题 |
|---|---|
| ALL-GAP-030 | Wallet KYC 与 Card KYC 关系 |
| ALL-GAP-031 | Wallet KYC 是否为 GTR / WalletConnect Deposit 前置 |
| ALL-GAP-032 | Wallet 开户触发时机 |
| ALL-GAP-033 | KYC 失败 / 重试 / 人工处理规则 |
| ALL-GAP-034 | KYC 结果是否触发通知 |
| ALL-GAP-035 | AIX 实际依赖哪些 AAI 结果 |

## 5. 不写入事实的内容

以下内容不得写成事实：

1. Wallet KYC 与 Card KYC 完全相同。
2. Wallet KYC 与 AAI KYC 完全相同。
3. Wallet 开户一定在注册时自动完成。
4. Wallet KYC 一定是 GTR / WalletConnect Deposit 前置。
5. AAI 内部审核逻辑、完整字段、完整错误码。

## 6. 来源引用

- (Ref: IMPLEMENTATION_PLAN.md / v4.5)
- (Ref: knowledge-base/wallet/kyc.md / v1.1)
- (Ref: knowledge-base/common/aai.md / v1.2)
- (Ref: knowledge-base/changelog/knowledge-gaps.md / ALL-GAP-030 ~ ALL-GAP-035)
- (Ref: 用户确认结论 / 2026-05-02 / KYC 独立，common/aai.md 不迁移)
