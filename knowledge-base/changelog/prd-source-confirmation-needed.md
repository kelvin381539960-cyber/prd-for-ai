---
module: changelog
feature: prd-source-confirmation-needed
version: "2.0"
status: active
source_doc: archive/legacy-prd/app/registration-login/README.md；archive/legacy-prd/app/home/README.md；archive/legacy-prd/card/application/README.md
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
| NEED_CONFIRMATION | 0 | 删除线内容已按用户确认视为删除，不再待确认 |
| CONFLICT | 1 | 两份 active converted-prd 对同一跳转规则冲突 |
| TODO | 0 | 无未执行任务 |
| SOURCE_GAP | 0 | 无证据规则遗漏 |

## 3. Account 删除线处理结论

用户已确认：删除线内容等同已删除。Account 相关 Forgot Password / Password Reset 逻辑不再进入待确认清单，而是从 runtime logic 中排除。

| 项目 | 最终处理 |
|---|---|
| Forgot Password 入口 | 删除线来源，不纳入 current runtime |
| Reset Password Page | 删除线来源，不纳入 current runtime |
| 重置密码后清除 BIO / 关闭 BIO | 跟随 Password Reset 删除线，不纳入 confirmed fact |
| Account Locked | 不作为 Account Status；Security 场景锁定继续由 security/global-rules.md 维护 |

## 4. Card Home 冲突项

### 4.1 冲突来源

| 来源 | 相关段落 |
|---|---|
| `archive/legacy-prd/app/home/README.md` | 首页当前卡片展示逻辑 |
| `archive/legacy-prd/card/application/README.md` | Card Application / Card Home 展示逻辑 |

### 4.2 冲突矩阵

| 卡状态 / 场景 | Home PRD | Card Application PRD | 当前处理 |
|---|---|---|---|
| Processing / 审核中点击 | 跳转当前卡片（审核中）页面 `My Card` | 跳转当前卡片首页 `Card（审核中）` | CONFLICT，待产品确认 |
| Pending activation / 待激活点击 | 跳转当前卡片（待激活）页面 `My Card` | 跳转激活卡页面 `Activate Card` | CONFLICT，待产品确认 |
| Active 且未设置 PIN 点击 | 跳转当前卡片首页 `My Card` | 跳转设置 PIN 页面 `Set PIN` | CONFLICT，待产品确认 |
| Frozen / 已冻结点击 | 跳转当前卡片首页 `Card` | 跳转触发解冻卡的身份认证页面 | CONFLICT，待产品确认 |

## 5. 产品裁决建议

### 5.1 Card Home

请产品确认首页卡片点击跳转的最终优先级：

1. `Home PRD` 是否覆盖 `Card Application PRD` 的首页卡片跳转？
2. 还是 `Card Application PRD` 作为 Card 领域事实源覆盖 Home？
3. 对 Processing / Pending activation / Active 未设置 PIN / Frozen 四种状态，各自最终跳转是什么？

## 6. 使用规则

1. 在产品裁决前，AI 回答这些问题时必须说明“源 PRD 存在删除线 / 冲突”。
2. 不得为了让任务状态看起来完成而强行选择其中一份 PRD。
3. 产品确认后，应更新对应 KB 文件，并把任务表中的 CONFLICT 改为 ALIGNED。

## 7. Sources

- (Ref: archive/legacy-prd/app/registration-login/README.md / 7.3.3 Reset Password 删除线)
- (Ref: archive/legacy-prd/app/home/README.md / 当前卡片展示逻辑)
- (Ref: archive/legacy-prd/card/application/README.md / Card Home 展示逻辑)
- (Ref: archive/legacy-prd/security/identity-verification/README.md / Security 场景锁定)
