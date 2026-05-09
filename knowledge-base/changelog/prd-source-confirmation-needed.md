---
module: changelog
feature: prd-source-confirmation-needed
version: "1.0"
status: active
source_doc: archive/converted-prd/app/registration-login/README.md；archive/converted-prd/app/home/README.md；archive/converted-prd/card/application/README.md
source_section: final unresolved evidence after PRD source alignment
last_updated: 2026-05-09
owner: 吴忆锋
readers: [product, ui, dev, qa, business, ai]
---

# PRD Source Confirmation Needed 产品确认清单

## 1. 文档定位

本文记录本轮 `knowledge-base` 按新转换历史 PRD 对齐后，仍不能由 AI 自行裁决的事项。

这些事项不是遗漏，而是证据本身存在删除线、证据不足或多份 active PRD 冲突。除非产品给出明确裁决，否则不得把它们改写成 confirmed fact。

## 2. 总览

| 类型 | 数量 | 说明 |
|---|---:|---|
| NEED_CONFIRMATION | 3 | 源 PRD 删除线或证据不足 |
| CONFLICT | 1 | 两份 active converted-prd 对同一跳转规则冲突 |
| TODO | 0 | 无未执行任务 |
| SOURCE_GAP | 0 | 无证据规则遗漏 |

## 3. Account 待确认项

### 3.1 Account index / Account Status

| 项目 | 当前处理 | 原因 | 涉及文件 |
|---|---|---|---|
| Account Status 中的 Locked | 不作为 Account Status confirmed fact | `registration-login` 中 Locked 为删除线；OTP / Email OTP / Face Auth / Login Passcode 的 Locked 应作为 Security 场景锁定处理 | `knowledge-base/account/_index.md`；`knowledge-base/security/global-rules.md` |
| Account index 状态 | NEED_CONFIRMATION | Account index 依赖 Login / Password Reset，后两者仍有待确认 | `knowledge-base/account/_index.md` |

### 3.2 Login 输入范围 / Forgot Password 入口

| 项目 | 当前处理 | 原因 | 涉及文件 |
|---|---|---|---|
| Login 支持 Email / Phone 输入范围 | 保留风险说明，不作为完全确认事实 | `registration-login` 中登录输入和部分入口存在删除线 / 证据不完整 | `knowledge-base/account/login.md` |
| Forgot Password 入口 | 不作为 active confirmed fact | 相关 Reset Password 章节为删除线 | `knowledge-base/account/login.md`；`knowledge-base/account/password-reset.md` |

### 3.3 Password Reset

| 项目 | 当前处理 | 原因 | 涉及文件 |
|---|---|---|---|
| Reset Password Page | NEED_CONFIRMATION | `registration-login` 7.3.3 “Reset Password Page 重置密码页”为删除线 | `knowledge-base/account/password-reset.md` |
| 重置密码后清除 BIO / 关闭 BIO | 不作为 confirmed fact | 来源跟随 Password Reset 删除线，Security 仅登记为删除线边界 | `knowledge-base/account/password-reset.md`；`knowledge-base/security/biometric-verification.md` |

## 4. Card Home 冲突项

### 4.1 冲突来源

| 来源 | 相关段落 |
|---|---|
| `archive/converted-prd/app/home/README.md` | 首页当前卡片展示逻辑 |
| `archive/converted-prd/card/application/README.md` | Card Application / Card Home 展示逻辑 |

### 4.2 冲突矩阵

| 卡状态 / 场景 | Home PRD | Card Application PRD | 当前处理 |
|---|---|---|---|
| Processing / 审核中点击 | 跳转当前卡片（审核中）页面 `My Card` | 跳转当前卡片首页 `Card（审核中）` | CONFLICT，待产品确认 |
| Pending activation / 待激活点击 | 跳转当前卡片（待激活）页面 `My Card` | 跳转激活卡页面 `Activate Card` | CONFLICT，待产品确认 |
| Active 且未设置 PIN 点击 | 跳转当前卡片首页 `My Card` | 跳转设置 PIN 页面 `Set PIN` | CONFLICT，待产品确认 |
| Frozen / 已冻结点击 | 跳转当前卡片首页 `Card` | 跳转触发解冻卡的身份认证页面 | CONFLICT，待产品确认 |

## 5. 产品裁决建议

### 5.1 Account

请产品确认：

1. 当前版本是否支持 Forgot Password / Reset Password？
2. Login 当前是否同时支持 Email 与 Phone？
3. Account Status 是否只有 Active / Banned / Closed，Locked 是否仅作为 Security 场景锁定？
4. 重置密码后是否需要清除本地 BIO 并关闭后端 BIO 开关？

### 5.2 Card Home

请产品确认首页卡片点击跳转的最终优先级：

1. `Home PRD` 是否覆盖 `Card Application PRD` 的首页卡片跳转？
2. 还是 `Card Application PRD` 作为 Card 领域事实源覆盖 Home？
3. 对 Processing / Pending activation / Active 未设置 PIN / Frozen 四种状态，各自最终跳转是什么？

## 6. 使用规则

1. 在产品裁决前，AI 回答这些问题时必须说明“源 PRD 存在删除线 / 冲突”。
2. 不得为了让任务状态看起来完成而强行选择其中一份 PRD。
3. 产品确认后，应更新对应 KB 文件，并把任务表中的 NEED_CONFIRMATION / CONFLICT 改为 ALIGNED。

## 7. Sources

- (Ref: archive/converted-prd/app/registration-login/README.md / 7.3.3 Reset Password 删除线)
- (Ref: archive/converted-prd/app/home/README.md / 当前卡片展示逻辑)
- (Ref: archive/converted-prd/card/application/README.md / Card Home 展示逻辑)
- (Ref: archive/converted-prd/security/identity-verification/README.md / Security 场景锁定)
