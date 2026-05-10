---
module: account
feature: password-reset
version: "2.0"
status: deleted_out_of_scope
source_doc: archive/legacy-prd/app/registration-login/README.md；archive/legacy-prd/security/identity-verification/README.md
source_section: Registration Login / 7.3 Password Reset 删除线内容
last_updated: 2026-05-09
owner: 吴忆锋
readers: [product, ui, dev, qa, business, ai]
---

# Password Reset 忘记密码流程

## 1. 当前结论

Password Reset / Forgot Password 相关内容在 `archive/legacy-prd/app/registration-login/README.md` 中属于删除线内容。

用户已确认：删除线内容等同已删除，不再作为待确认逻辑，也不纳入当前 App runtime knowledge-base。

## 2. Runtime 处理

| 项目 | 处理 |
|---|---|
| Forgot Password 入口 | 不作为当前 Login confirmed 入口 |
| Reset Password Page | 不作为当前 active 页面 |
| 重置密码后清除 BIO / 关闭 BIO | 不作为当前 confirmed runtime fact |
| OTP / Face Auth / Password Policy | 仍由 Security 模块维护，但不代表 Password Reset 流程存在 |

## 3. 使用规则

1. 回答当前 App 是否支持 Forgot Password / Password Reset 时，应说明：当前 runtime KB 不纳入该能力，因为源 PRD 对应内容为删除线。
2. 不得根据删除线中的页面、接口、BIO 清理逻辑推导当前能力。
3. 若后续产品重新启用该能力，需要新的 active PRD 作为证据，再重建本文件。

## 4. Sources

- (Ref: archive/legacy-prd/app/registration-login/README.md / 7.3 Password Reset 删除线)
- (Ref: archive/legacy-prd/security/identity-verification/README.md / OTP / Password / BIO 支撑能力，不代表 Password Reset active)
