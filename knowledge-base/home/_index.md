---
module: home
feature: home-index
version: "1.0"
status: active
source_doc: knowledge-base/home/app-home.md；knowledge-base/card/card-home.md；knowledge-base/wallet/_index.md；knowledge-base/changelog/knowledge-gaps.md
source_section: App Home；Card entry；Wallet entry；runtime routing
last_updated: 2026-05-05
owner: 吴忆锋
---

# Home 模块索引

## 1. 模块定位

Home 模块用于沉淀 AIX App 首页的运行态事实，包括首页整体结构、模块入口、首页卡片、首页区块和跨模块跳转边界。

Home 不是官网、Web 或 Marketing 站点模块；它只承接 App 内首页。

## 2. 当前文件

| 文件 | 状态 | 定位 |
|---|---|---|
| `home/_index.md` | active | Home 模块索引 |
| `home/app-home.md` | active | AIX App 首页运行态事实源 |

## 3. 与其他模块的边界

| 模块 | 关系 | 边界 |
|---|---|---|
| Card | Home 可展示 Card 区块和入口 | Card 模块首页、卡状态和操作入口在 `card/card-home.md` |
| Wallet | Home 可展示 Wallet 入口或资产入口 | Wallet 余额、Deposit 等事实在 `wallet/` |
| Account | Home 可能依赖登录态和账户状态 | Account 主事实在 `account/` |
| Common | Home 可能使用 Notification、FAQ、Errors | Common 主事实在 `common/` |
| Operation / Popup / Banner | 首页弹窗 Banner 能力暂未入库 | 不在 Home 中补写运营配置系统 |

## 4. 查询入口规则

| 查询主题 | 优先读取 |
|---|---|
| App 首页整体结构 / 首页入口 | `home/app-home.md` |
| 首页 Card 区块跳转 Card 页面 | `home/app-home.md`，必要时读 `card/card-home.md` |
| Card 模块首页详情 | `card/card-home.md` |
| 首页 Wallet 入口或资产入口 | `home/app-home.md`，必要时读 `wallet/_index.md`、`wallet/balance.md` |
| 首页弹窗 / Banner / MGM 运营配置 | 暂不入库，不从 Home 推导 |

## 5. 不写入事实的内容

1. 不把官网 Home 写入本模块。
2. 不把 Marketing 落地页写入本模块。
3. 不把 Popup / Banner / MGM 运营配置能力写入本模块。
4. 不把 Card 模块内页规则写入 Home。
5. 不把 Wallet 余额、Deposit、交易状态写入 Home。

## 6. 来源引用

- (Ref: 历史prd/AIX APP V1.0【Home】.docx)
- (Ref: knowledge-base/home/app-home.md)
- (Ref: knowledge-base/card/card-home.md)
- (Ref: knowledge-base/wallet/_index.md)
- (Ref: knowledge-base/changelog/knowledge-gaps.md)
