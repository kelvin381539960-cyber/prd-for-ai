---
module: _meta
feature: glossary
version: "2.0"
status: active
source_doc: archive/legacy-prd/**/README.md；knowledge-base/* 已校准模块
source_section: converted PRD corpus / glossary
last_updated: 2026-05-09
owner: 吴忆锋
readers: [product, ui, dev, qa, business, ai]
---

# Glossary 术语表

## 1. 任务 / 证据术语

| 术语 | 定义 |
|---|---|
| converted-prd | 由历史 Word PRD 转换得到的 Markdown 证据层，位于 archive/legacy-prd |
| knowledge-base | 当前整理后的 runtime 产品事实库 |
| ALIGNED | 知识库文件已完成 KB→Evidence 与 Evidence→KB 双向覆盖校验 |
| SOURCE_GAP | converted-prd 中有关键规则，但知识库尚未完整结构化覆盖 |
| NEED_CONFIRMATION | 源 PRD 删除线、待定或证据不足，需产品确认 |
| CONFLICT | 多份 converted-prd 对同一事实存在冲突，不能自行裁决 |
| OUT_OF_SCOPE | 不纳入 runtime knowledge-base 范围 |

## 2. 产品 / 系统术语

| 术语 | 定义 |
|---|---|
| AIX Pay | AIX App 内钱包 / 卡 / 交易等用户产品能力 |
| DTC / DTCPay | 卡、钱包、KYC 等外部渠道或服务依赖方，具体接口以模块 PRD 为准 |
| OBoss | 运营配置、通知、Popup、Banner 等能力相关平台 |
| MoEngage | Notification / System Email 相关发送或模板能力依赖 |
| message-center | Notification 中对上游消息进行过滤、push、存储的服务 |
| message-push-system | Notification 中负责向 App Client 发送 push 的系统 |
| WalletConnect | 钱包充值中通过私有钱包连接和授权的能力 |
| GTR | Wallet Deposit 中自动交易报备路径 |
| OTC | Swap / exchange 相关场景，用于稳定币兑换 |
| IVS | Identity Verification Service，身份认证相关能力 |
| BIO / BIOMETRICS | 设备生物识别能力，如 Face ID / Touch ID / Fingerprint |
| Face Auth | 活体识别认证 |
| POA | Proof of Address，地址证明 |
| AIX Tag / X-Tag | Wallet Send 收款人标识之一 |

## 3. Sources

- (Ref: knowledge-base/changelog/prd-source-alignment.md)
- (Ref: knowledge-base/* 已校准模块)
