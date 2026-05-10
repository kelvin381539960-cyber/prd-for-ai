---
module: common
feature: errors
version: "2.0"
status: active
source_doc: archive/legacy-prd/**/README.md；knowledge-base/* 已校准模块
source_section: converted PRD corpus / error messages, toast, popup, failed pages, API errors
last_updated: 2026-05-09
owner: 吴忆锋
readers: [product, ui, dev, qa, business, ai]
depends_on:
  - account/_index
  - security/_index
  - kyc/account-opening
  - card/application
  - card/manage/_index
  - card/transaction-detail
  - wallet/assets
  - wallet/deposit
  - wallet/send
  - wallet/swap
  - transaction/_index
  - common/notification
---

# Common Errors 错误处理公共能力

## 1. 文档定位

本文沉淀已从 converted-prd 和已校准知识库中确认的跨模块错误文案、toast、popup、failed page、异常边界和处理原则。

本文不是后端错误码全集，也不替代模块内具体错误规则。回答具体模块错误时，优先读取对应模块文件；本文用于统一查找高频用户侧文案和跨模块异常处理边界。

## 2. Source alignment status

本文件已按本轮已校准模块进行重写，原 `SOURCE_GAP` 已收口为 `ALIGNED`。

已覆盖来源包括 Account、Security、KYC、Card Application、Card Manage、Card Transaction、Wallet、Transaction、Notification、FAQ。若后续新增 PRD 或后端接口新增错误码，需要继续维护本文。

## 3. 全局错误处理原则

| 原则 | 说明 |
|---|---|
| 不自行编造错误文案 | 未在 converted-prd 或已校准 KB 中出现的错误文案，不得直接输出为 confirmed fact |
| 优先模块来源 | 模块文档中有明确文案时，以模块文档为准 |
| 后端透传文案 | 源 PRD 明确“后端返回错误文案”时，不在本文伪造具体 copy |
| 删除线隔离 | 源 PRD 删除线中的错误文案或弹窗，不作为 confirmed fact |
| 未知 DTC 错误 | 源 PRD 要求 Lark 报警 / 产品与渠道确认的，不自行归类 |
| Failed Page 与 Toast 区分 | Page / Popup / Toast / Inline error 应按源文档形态区分，不能互相替代 |

## 4. Account 错误 / 提示

| 文案 / 规则 | 场景 | 来源 |
|---|---|---|
| `Account locked. Please contact customer support.` | Banned 登录拦截 | account/login.md；registration-login |
| `This email has been used. Please try another one.` | 注册邮箱重复 | account/registration.md；registration-login |
| `Passwords do not match. Please try again.` | 两次密码不一致 | account/registration.md；security/password-policy.md |
| Password Reset | 忘记密码章节整体为删除线；相关错误和 BIO 清理不能作为 active runtime fact | account/password-reset.md |

## 5. Security 错误 / 提示

| 文案 / 规则 | 场景 | 来源 |
|---|---|---|
| `Too Many Attempts` | OTP / Email OTP / Login Passcode / Face Auth 达到锁定阈值 | security/global-rules.md |
| `Invalid OTP` | OTP / Email OTP 输入错误 | security/otp-verification.md；security/email-otp-verification.md |
| `Verification Expired` | 身份验证挑战或凭证过期 | security/global-rules.md |
| OTP 失败 5 次 | 24 小时内失败 5 次，锁定 20 分钟 | security/global-rules.md |
| OTP 失败 10 次 | 24 小时内失败 10 次，锁定 24 小时 | security/global-rules.md |
| Resend 限制 | 24 小时内最多 3 次 resend，达到上限后 20 分钟冷却 | security/otp-verification.md；security/email-otp-verification.md |
| 验证码设备绑定 | 验证码仅限发起请求的设备使用，更换设备无效 | security/otp-verification.md；security/email-otp-verification.md |
| BIO 后端验证失败 | 清除本地 Bio，后端关闭账户 Bio 开关，并引导回登录 | security/biometric-verification.md |
| Face Auth Failed Page | FAIL / EXPIRED / incomplete / 空值进入失败页 | security/face-authentication.md |

## 6. KYC 错误 / 提示

| 文案 / 规则 | 场景 | 来源 |
|---|---|---|
| Face Loading 超时 | Face Loading 超过 30 秒未收到结果，进入 Loading Failed | kyc/account-opening.md |
| Loading Failed Retry | 点击 Retry 重新进入 Face Loading，不返回 Face Scan | kyc/account-opening.md |
| Face 失败锁定 | 24 小时内 5 次锁 20 分钟；10 次锁 24 小时；接口连续 20 次锁 20 分钟 | kyc/account-opening.md |
| Face 失败原因优先级 | passport 与 face 均失败时优先展示 passport 失败原因 | kyc/account-opening.md |
| POA 失败 | POA 失败按 POA error code 映射展示 | kyc/account-opening.md |
| Waitlist 拦截 | Waitlist 为页面级拦截，不允许继续后续 KYC | kyc/account-opening.md |
| Rejected | 因风险被 DTC 拒绝时，Home 隐藏激活钱包入口 | kyc/account-opening.md；home/app-home.md |

## 7. Card Application 错误 / 提示

| 文案 / 规则 | 场景 | 来源 |
|---|---|---|
| `The exchange rate has not been updated in real time. Please try again.` | 申卡 Checkout 切换支付币种汇率失败 | card/application.md |
| `Top up & Get started` | 钱包余额为 0 时展示 | card/application.md |
| `Address selection isnot completed.` | 实体卡地址选择未完成返回 | card/application.md |
| Face Token 无效提示 | `To ensure the security and rights of your application card, please complete the facial recognition verification as per the instructions.` | card/application.md |
| `Verify Now` | Face Token 无效时跳转身份认证刷脸页 | card/application.md |
| Application unsuccessful | 申卡 response success=false | card/application.md |
| MGM Fee waiver | 响应失败不通知；审核中冻结；审核通过核销；审核失败 Terminated / Cancelled 解冻 | card/application.md |

## 8. Card Manage 错误 / 提示

| 文案 / 规则 | 场景 | 来源 |
|---|---|---|
| `The last 4 digits entered are invalid` | 实体卡激活后四位校验失败 | card/manage/activation.md |
| `Your card has been activated` | 实体卡激活成功 toast | card/manage/activation.md |
| Active fail Page | Card Activation 失败 | card/manage/activation.md |
| Set fail Page | 激活成功但 Set PIN 失败 | card/manage/activation.md |
| `Please re-entered the same PIN.` | 两次 PIN 不一致 | card/manage/pin.md |
| `PIN setup failed` | PIN 设置默认失败页标题 | card/manage/pin.md |
| `We could not complete your PIN setup right now. Please try again later.` | PIN 设置默认失败内容 | card/manage/pin.md |
| error_code = 31031 | 使用后端返回文案覆盖默认失败文案 | card/manage/pin.md |
| PIN 简单规则 | 任一数字出现超过 3 次会被 DTC 拒绝 | card/manage/pin.md |
| `Failed to get card info. Please try again later` | Get Card Basic Info / Sensitive Info 返回失败 | card/manage/sensitive-info.md |
| `The information has been copied.` | 复制卡信息 / 钱包地址 | card/manage/sensitive-info.md；wallet/deposit.md |
| `Freeze failed` | Lock Card / Freeze 后端错误 | card/manage/status-and-operations.md |
| `Unfreeze failed` | Unlock / Unfreeze 后端错误 | card/manage/status-and-operations.md |
| `Your physical card has been unlocked.` | Unlock 成功 | card/manage/status-and-operations.md |
| `No internet connection, please check the connection or try again later.` | Unlock 网络异常 | card/manage/status-and-operations.md |
| Network Error Page | 页面级网络异常 | card/manage/status-and-operations.md |
| Server Error Page | 页面级服务端异常 | card/manage/status-and-operations.md |
| Network Error Popup | 操作时网络异常但无需中断整体流程 | card/manage/status-and-operations.md |
| Server Error Popup | 操作时服务端异常但无需中断整体流程 | card/manage/status-and-operations.md |

## 9. Card Transaction / Transaction 错误 / 提示

| 文案 / 规则 | 场景 | 来源 |
|---|---|---|
| `Data error. Please refresh and try again.` | DTC / 服务端异常 | transaction/history.md；card/transaction.md |
| `No internet connection. Please retry` | 网络异常 | transaction/history.md；card/transaction.md |
| `No transaction data` | Card History / Recent transaction 空态 | transaction/history.md；wallet/assets.md |
| DTC 未知错误码 | 直接 Lark 报警通知，以便产品和渠道确认错误处理 | card/transaction-detail.md |
| Merchant city / MCC 缺失 | 非必填；没有则不显示 item | card/transaction-detail.md；transaction/detail.md |
| Deposit Gas fee | Deposit 详情隐藏 Gas fee，不作为当前展示项 | transaction/detail.md |

## 10. Wallet 错误 / 提示

| 文案 / 规则 | 场景 | 来源 |
|---|---|---|
| `Network abnormality. Please try again later.` | My Assets 汇率异常 | wallet/assets.md |
| `No transaction data` | Recent transaction 空态 | wallet/assets.md |
| `The information has been copied.` | Receive Crypto 复制地址 | wallet/deposit.md |
| `The QR code has expired` | WalletConnect QR 过期 | wallet/deposit.md |
| `If you have not completed the deposit, please resubmit.` | WalletConnect QR 过期说明 | wallet/deposit.md |
| `Come back Wallet` | QR 过期后返回钱包首页 | wallet/deposit.md |
| `Insufficient balance` | Send / Swap / Checkout 余额不足类场景 | wallet/send.md；wallet/swap.md；card/application.md |
| `Your available balance is not enough to complete this send.` | Send 余额不足 | wallet/send.md |
| `Your available balance is not enough to complete this exchange.Please add funds or adjust the exchange amount and try again.` | Swap 余额不足 | wallet/swap.md |
| `Exchange rate expired` | Swap Order 报价过期 | wallet/swap.md |
| `The exchange rate has expired. Please refresh to get the latest rate before continuing.` | Swap Order 报价过期说明 | wallet/swap.md |
| `Send successful!` | Send 成功结果页 | wallet/send.md |
| `Send processing!` | Send 处理中结果页 | wallet/send.md |
| `Send failure!` | Send 失败结果页 | wallet/send.md |
| `Swap completed` | Swap 成功结果页 | wallet/swap.md |
| `Swap processing` | Swap 处理中结果页 | wallet/swap.md |
| `Swap failed` | Swap 失败结果页 | wallet/swap.md |

## 11. Notification 错误 / 提示

| 文案 / 规则 | 场景 | 来源 |
|---|---|---|
| `全部已读` | Notification Center 一键已读 toast | common/notification.md |
| 未读数字 `99+` | Me tab 未读消息超过 100 条 | common/notification.md |
| inactive / Closed / banned | 停止全部消息推送 | common/notification.md |
| MoEngage subscribe sync | 删除线内容，不作为 confirmed fact | common/notification.md |

## 12. FAQ / 用户解释边界

FAQ 中的用户解释文案可以作为帮助中心内容，但不能反推业务规则。比如 FAQ 中出现 Google Pay、Apple Pay、Samsung Pay 时，实际产品支持范围必须以 Card Manage / Card Application 当前 confirmed fact 为准。

## 13. 仍需模块内维护的内容

| 类型 | 处理 |
|---|---|
| KYC 全量 error code | 维护在 `kyc/account-opening.md` 或后续 `_meta/error-code-dictionary.md` |
| Security 认证错误码 | 维护在 `security/*` |
| DTC 未知错误 | 按模块 PRD 要求 Lark 报警，不在本文自行分类 |
| 后端透传错误文案 | 模块中写明透传时，以后端返回为准 |
| 删除线错误文案 | 不沉淀为 confirmed fact |

## 14. Sources

- (Ref: archive/legacy-prd/app/registration-login/README.md)
- (Ref: archive/legacy-prd/security/identity-verification/README.md)
- (Ref: archive/legacy-prd/kyc/wallet-opening/README.md)
- (Ref: archive/legacy-prd/card/application/README.md)
- (Ref: archive/legacy-prd/card/manage/README.md)
- (Ref: archive/legacy-prd/card/transaction/README.md)
- (Ref: archive/legacy-prd/app/transaction-history/README.md)
- (Ref: archive/legacy-prd/wallet/asset/README.md)
- (Ref: archive/legacy-prd/wallet/deposit-send-swap/README.md)
- (Ref: archive/legacy-prd/notification/push-inbox/README.md)
- (Ref: knowledge-base/* 已校准模块)
