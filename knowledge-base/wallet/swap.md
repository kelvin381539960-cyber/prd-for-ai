---
module: wallet
feature: swap
version: "1.0"
status: active
source_doc: archive/converted-prd/wallet/deposit-send-swap/README.md；archive/converted-prd/app/transaction-history/README.md
source_section: Wallet Deposit/Send/Swap / 6.2 钱包兑换 Swap Crypto；7.5 Get OTC Rate；7.6 OTC Exchange；Transaction Details
last_updated: 2026-05-09
owner: 吴忆锋
readers: [product, ui, dev, qa, business, ai]
depends_on:
  - wallet/_index
  - wallet/assets
  - transaction/detail
---

# Wallet Swap Crypto 钱包兑换

## 1. 功能定位

Swap Crypto 用于同一用户不同稳定币之间的兑换，例如 USDT、USDC 等。

## 2. Source alignment status

本文件用于收口原 `wallet/deposit.md` 的 SOURCE_GAP。规则来自 `archive/converted-prd/wallet/deposit-send-swap/README.md` 的 6.2 钱包兑换 Swap Crypto、7.5 Get OTC Rate、7.6 OTC Exchange，并同步引用 Transaction Details 作为交易详情支撑证据。

## 3. Swap 页面

| 项目 | 规则 |
|---|---|
| 标题 | “Swap” |
| FAQ | 根据关键场景 “Transactions” 及类型 “Crypto Swap” 筛选 FAQ，并按创建时间降序展示，滑动加载更多，不翻页 |
| Sell crypto | 卖出币种必选；默认包括 USDT、USDC、WUSD、FDUSD，后端可配置展示币种；需要过滤当前 Buy crypto 已选择币种 |
| Buy crypto | 买入币种必选；默认包括 USDT、USDC、WUSD、FDUSD，后端可配置展示币种；需要过滤当前 Sell crypto 已选择币种 |
| Available Balance | 用户选择 Sell crypto 后，调用 `[GET] /openapi/v1/wallet/balance/{currency}` 查询并展示当前币种可用余额 |
| Sell amount | 卖出金额必填 |
| Buy amount | 系统按当前汇率计算：Buy amount = Sell amount × Rate |
| Rate | 展示当前汇率，例如 `1 USDT = 0.78759 USDC` |
| Continue | 点击后跳转 Swap Order |

## 4. Swap Order 确认页

| 项目 | 规则 |
|---|---|
| 标题 | “Swap Order” |
| Rate | 与兑换选择页一致，例如 `1 USDT = 0.78759 USDC` |
| Confirm | 点击后进行汇率有效期和余额等校验 |
| Exchange rate expired | 若当前 Rate 已过报价有效期，提示 “Exchange rate expired” / “The exchange rate has expired. Please refresh to get the latest rate before continuing.” |
| Update rate | 点击后跳转回 Swap 页面，页面恢复初始加载状态，不保留历史操作数据 |
| Insufficient balance | 若余额不足，提示 “Insufficient balance” / “Your available balance is not enough to complete this exchange.Please add funds or adjust the exchange amount and try again.” |

## 5. OTC Rate / Quote

| 项目 | 规则 |
|---|---|
| Get OTC Rate | 通过 `POST /openapi/v1/otc/get-otc-rate` 获取兑换汇率 |
| OTC Exchange | 用于当前账户不同币种之间兑换 |
| dtcQuoteId | 一次性报价标识符，使用后失效，不能重复使用 |
| 重新获取 quote | 如需新的 dtcQuoteId，必须重新调用 `POST /openapi/v1/otc/get-otc-rate` |

## 6. 结果页

| 结果 | 文案 / 行为 |
|---|---|
| Swap completed | 状态说明：Swap completed；状态描述：Your asset conversion was completed successfully. The converted funds are now available in your balance.；点击 View Order Details 跳转 Transaction Details |
| Swap processing | 状态说明：Swap processing；状态描述：The asset conversion is currently in progress. Your balance will be updated once it’s completed. |
| Swap failed | 状态说明：Swap failed |

## 7. 交易详情边界

Swap Detail 的 exchange rate 由后端返回什么显示什么，不做位数处理。交易详情字段由 `transaction/detail.md` 维护。

## 8. 不得推导

1. 不得写成支持非稳定币兑换。
2. 不得自行扩展汇率有效期时长；源 PRD 只明确存在报价有效期校验和过期处理。
3. 不得复用 Card Detail 的 exchange rate 小数 6 位向上取整规则；Swap Detail 明确由后端给什么显示什么。
4. 不得把 dtcQuoteId 写成可重复使用。

## 9. Sources

- (Ref: archive/converted-prd/wallet/deposit-send-swap/README.md / 6.2 钱包兑换 Swap Crypto)
- (Ref: archive/converted-prd/wallet/deposit-send-swap/README.md / 7.5 Get OTC Rate)
- (Ref: archive/converted-prd/wallet/deposit-send-swap/README.md / 7.6 OTC Exchange)
- (Ref: archive/converted-prd/app/transaction-history/README.md / Swap Details)
