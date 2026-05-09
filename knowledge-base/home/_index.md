---
module: home
feature: index
version: "1.1"
status: active
source_doc: archive/converted-prd/app/home/README.md；archive/converted-prd/app/faq/README.md
source_section: App Home；Home FAQ；runtime routing
last_updated: 2026-05-09
owner: 吴忆锋
readers: [product, ui, dev, qa, business, ai]
---

# Home 模块索引

## 1. 模块定位

Home 模块用于沉淀 AIX App 首页的运行态事实，包括首页整体结构、模块入口、首页钱包区域、申卡入口、首页卡片、FAQ 展示、核心交易入口和跨模块跳转边界。

Home 不是官网、Web 或 Marketing 站点模块；它只承接 App 内首页。

## 2. 当前文件

| 文件 | 状态 | 定位 |
|---|---|---|
| `home/_index.md` | active | Home 模块索引 |
| `home/app-home.md` | active | AIX App 首页运行态事实源 |

## 3. 与其他模块的边界

| 模块 | Home 可以记录 | 不在 Home 维护 |
|---|---|---|
| Card | 首页申卡入口、首页卡片展示和跳转 | Card 申请全流程、卡管理、PIN、敏感信息、卡交易详情 |
| Wallet | 钱包区域展示条件、资产入口、核心交易快捷入口 | Deposit / Send / Swap 完整流程、余额字段全量定义 |
| KYC | Home 依据 KYC 状态展示钱包区域 | KYC 开户流程和错误码映射 |
| Transaction | 首页 Transaction 入口 | 交易历史、交易详情、状态模型 |
| FAQ | 首页 FAQ 展示和 `more>` 边界 | FAQ 原文全集、Zendesk 内容维护 |
| Operation / Popup / Banner | 首页承接位 | 运营配置系统、投放规则、MGM 页面 |

## 4. 查询入口规则

| 查询问题 | 首读文件 |
|---|---|
| App 首页整体结构 / 首页入口 | `home/app-home.md` |
| 首页钱包区域 / 钱包状态面板 | `home/app-home.md`，必要时读 `wallet/`、`kyc/` |
| 首页申卡入口是否展示 / 是否可点 | `home/app-home.md`，必要时读 `card/application.md` |
| 首页卡片展示 / 点击跳转 | `home/app-home.md`，必要时读 `card/card-home.md`、`card/manage/` |
| 首页 FAQ 展示 / more 入口 | `home/app-home.md`，FAQ 原文读 `common/faq.md` |
| 首页 Deposit / Swap / Send / Transaction 快捷入口 | `home/app-home.md`，具体流程读 `wallet/`、`transaction/` |
| 首页 Popup / Banner / MGM 运营配置 | Home 只记录承接位；完整规则等 common popup-banner 审计 |

## 5. 不写入事实的内容

1. 不把官网 Home 写入本模块。
2. 不把 Website / Marketing 页面写入本模块。
3. 不把 Popup / Banner / MGM 运营配置能力写入 Home。
4. 不把 Card 模块内页规则写入 Home。
5. 不把 Wallet Deposit / Send / Swap 详情和交易状态写入 Home。
6. 不把删除线或待定事项当作 confirmed fact。

## 6. 来源引用

- (Ref: archive/converted-prd/app/home/README.md)
- (Ref: archive/converted-prd/app/faq/README.md)
- (Ref: archive/converted-prd/common/popup-banner/README.md，待 common 审计)
