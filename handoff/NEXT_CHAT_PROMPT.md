# Next Chat Handoff Prompt

## 当前任务状态

当前仓库：`kelvin381539960-cyber/prd-for-ai`  
当前分支：`phase2/account-feature-files-clean`  
当前主控文件：`IMPLEMENTATION_PLAN.md`  
当前版本：v3.2  
当前状态：Card 阶段回扫阻塞

## 必须先读取的文件

新会话开始后，必须先读取以下文件，再继续任何任务：

1. `IMPLEMENTATION_PLAN.md`
2. `knowledge-base/card/stage-review.md`
3. `knowledge-base/card/transaction-flow-traceability-checklist.md`
4. `knowledge-base/card/card-transaction-flow.md`
5. `knowledge-base/changelog/knowledge-gaps.md`

## 已完成范围

### Account

- `knowledge-base/account/login.md`
- `knowledge-base/account/registration.md`
- `knowledge-base/account/password-reset.md`
- `knowledge-base/account/_index.md`

Gate：PASS

### Security

- `knowledge-base/security/_index.md`
- `knowledge-base/security/global-rules.md`
- `knowledge-base/security/otp-verification.md`
- `knowledge-base/security/email-otp-verification.md`
- `knowledge-base/security/login-passcode-verification.md`
- `knowledge-base/security/biometric-verification.md`
- `knowledge-base/security/face-authentication.md`
- `knowledge-base/security/api-reference.md`

Gate：PASS

### Card

已完成文件：

- `knowledge-base/card/_index.md`
- `knowledge-base/card/application.md`
- `knowledge-base/card/card-status-and-fields.md`
- `knowledge-base/card/card-home.md`
- `knowledge-base/card/activation.md`
- `knowledge-base/card/pin.md`
- `knowledge-base/card/sensitive-info.md`
- `knowledge-base/card/card-management.md`
- `knowledge-base/card/card-transaction-flow.md`
- `knowledge-base/card/stage-review.md`
- `knowledge-base/card/transaction-flow-traceability-checklist.md`

Gate：BLOCK

阻塞原因：Card Transaction Flow 涉及资金归集，但可追溯字段未闭环。

## 当前阻塞点

必须确认以下字段或规则后，才允许解除 Card 阻塞：

- DTC Card Transaction Notification 完整字段表
- DTC 通知唯一 ID
- DTC 原始交易 ID
- AIX 内部交易 ID
- 归集请求 ID
- DTC 归集结果 ID
- 钱包入账流水 ID
- 幂等键
- 重复通知处理
- 查询余额失败处理
- 归集失败重试策略
- 告警与人工处理责任分派

确认清单已写入：

`knowledge-base/card/transaction-flow-traceability-checklist.md`

## 当前禁止事项

- 不得直接进入 Wallet 批量推进。
- 不得把未确认流水字段写成事实。
- 不得新增无来源状态、字段或接口。
- 不得把 Transaction 统一层提前混入 Card 阶段正文。
- 不得绕过 Stage Review Gate。

## Gate Review 机制

`IMPLEMENTATION_PLAN.md` v3.2 已新增 Stage Review Gate 机制：

- 每个阶段完成后必须执行 Stage Review。
- Gate 结果只能是 `PASS` / `PARTIAL PASS` / `BLOCK`。
- 未执行 Stage Review，或 Stage Review 未达到 `PASS`，不得进入下一阶段。
- 涉及资金处理时，缺少通知 ID、业务 ID、请求 ID、结果流水、入账流水、幂等键、重试策略、异常责任分派任一关键项，阶段结果不得为 `PASS`。

## 新会话推荐启动 Prompt

请复制以下内容到新会话：

```text
你现在接手 AIX 项目 prd-for-ai 知识库转译任务。

请先读取 GitHub 仓库：kelvin381539960-cyber/prd-for-ai
分支：phase2/account-feature-files-clean

必须先读取：
1. IMPLEMENTATION_PLAN.md
2. knowledge-base/card/stage-review.md
3. knowledge-base/card/transaction-flow-traceability-checklist.md
4. knowledge-base/card/card-transaction-flow.md
5. knowledge-base/changelog/knowledge-gaps.md

当前状态：IMPLEMENTATION_PLAN.md 已升级到 v3.2，Card 阶段 Gate Review 为 BLOCK，不允许进入 Wallet。

阻塞原因：Card Transaction Flow 涉及资金归集，但 DTC 通知 ID、AIX 内部交易 ID、归集请求 ID、DTC 归集结果 ID、钱包入账流水 ID、幂等键、重试策略等可追溯字段未确认。

请严格遵守：
- 先读 IMPLEMENTATION_PLAN.md，再执行任何任务。
- 不得直接进入 Wallet。
- 不得把未确认字段写成事实。
- 所有新增内容必须来自历史 PRD、接口文档、截图、已确认结论或现有知识库。
- 每完成阶段必须执行 Stage Review Gate。

下一步任务：把 knowledge-base/card/transaction-flow-traceability-checklist.md 改写成一版可以直接发给 DTC / 后端 / Wallet 负责人确认的精简沟通稿，要求短、清楚、能推动对方回复字段和规则。
```

## 建议下一步

将 `transaction-flow-traceability-checklist.md` 改写为对外沟通版，目标是发给 DTC / 后端 / Wallet 负责人确认字段。

确认后再更新：

- `knowledge-base/card/card-transaction-flow.md`
- `knowledge-base/changelog/knowledge-gaps.md`
- `knowledge-base/card/stage-review.md`
- `IMPLEMENTATION_PLAN.md`
