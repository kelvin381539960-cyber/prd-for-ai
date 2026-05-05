---
module: card
feature: card-management
version: "2.0"
status: active
source_doc: 历史prd/AIX Card 【manage】模块需求V1.0 .docx；历史prd/AIX Card V1.0【Application】.docx；历史prd/AIX Card交易【transaction】.docx；历史prd/AIX APP V1.0【Transaction & History】 (1).docx；DTC Card Issuing API Document_20260310；DTC Wallet OpenAPI Documentation；knowledge-base/changelog/knowledge-gaps.md
source_section: Card Manage 6.4 / 7.1 / 7.2 / 7.3 / 7.4 / 7.5 / 8.1；Card Status；Card Sensitive Info；Card Activation；Card PIN；Card Transaction Notify；Transfer Balance to Wallet
last_updated: 2026-05-05
owner: 吴忆锋
readers: [product, ui, dev, qa, business, ai]
---

# Card Management 卡管理

## 1. 文档定位

本文是 Card 模块的管理类运行态事实源，统一承接以下内容：

| 能力 | 是否在本文维护 | 说明 |
|---|---|---|
| 卡状态与操作矩阵 | 是 | 原 `card-status-and-fields.md` 已并入本文 |
| 实体卡激活 | 是 | 原 `activation.md` 已并入本文 |
| PIN 设置 / 修改 / 重置 | 是 | 原 `pin.md` 已并入本文 |
| 敏感信息查看 | 是 | 原 `sensitive-info.md` 已并入本文 |
| Lock / Unlock / Terminate | 是 | 原 `card-management.md` 主体能力 |
| 卡交易通知 / 归集 / 展示边界 | 是 | 原 `card-transaction-flow.md` 已并入本文 |

Card 目录不再为每个管理子动作单独建文件。查询卡状态、激活、PIN、敏感信息、锁卡、解锁、注销、卡交易归集时，默认读取本文。

---

## 2. Card 状态与操作矩阵

### 2.1 状态清单

| 状态 | 含义 | 用户可见表现 | 主要允许操作 | 是否终态 | 来源 |
|---|---|---|---|---|---|
| `Pending` / `Processing` | 申卡审核中 | Under review | 禁止重复申请；不允许卡管理操作 | 否 | Application |
| `Pending activation` / `Inactive` | 实体卡待激活 | 展示物流、Tracking、Activate card | 仅允许激活 | 否 | Application / Home / Manage |
| `Active` / `ACTIVE` | 已激活 / 可用 | 展示卡面、可用操作、交易 | 敏感信息、PIN、Lock、交易、注销 | 否 | Manage 6.4 |
| `Suspended` / `SUSPENDED` | 已冻结 | 展示冻结状态、Unlock | Unlock、注销；不允许交易 | 否 | Manage 6.4 |
| `BLOCKED` | 阻断 / 风控状态 | 仅允许查看部分卡信息 | 不允许敏感信息、交易、Lock / Unlock | 否 | Manage 6.4 |
| `CANCELLED` | 取消 / 终止 | 不允许操作 | 无 | 是 | Manage 6.4 |
| `Terminated` | 终止 | 与 Cancelled / BLOCKED 关系待确认 | 无 | 待确认 | Application |
| `Activate` | 原文疑似 Active 拼写 | 不作为独立状态 | 需归一为 Active | 否 | Manage 7.5 |

### 2.2 Manage 6.4 操作限制矩阵

| 卡状态 | 查看卡信息 | 查看敏感信息 | 卡激活 | Set PIN | Change PIN | Lock Card | Unlock Card | 注销卡 | 交易功能 |
|---|---|---|---|---|---|---|---|---|---|
| 待激活 | 否 | 否 | 是 | 否 | 否 | 否 | 否 | 否 | 否 |
| `ACTIVE` | 是 | 是 | 否 | 是，仅限首次 | 是 | 是 | 否 | 是 | 是 |
| `SUSPENDED` | 否 | 否 | 否 | 否 | 否 | 否 | 是 | 是 | 否 |
| `CANCELLED` | 否 | 否 | 否 | 否 | 否 | 否 | 否 | 否 | 否 |
| `BLOCKED` | 是 | 否 | 否 | 否 | 否 | 否 | 否 | 否 | 否 |
| `PENDING` | 否 | 否 | 否 | 否 | 否 | 否 | 否 | 否 | 否 |

规则：任何 Card Home、Application、Management、PIN、Sensitive Info、Transaction 展示或操作，都必须先引用本状态矩阵。未知状态或冲突状态进入 `knowledge-gaps.md`，不得自行推断。

---

## 3. 实体卡激活

### 3.1 主流程

用户从 Card Home 点击待激活实体卡的 `Activate card`，进入 Active Card Page 输入实体卡后四位。输入满 4 位后，系统调用 Inquiry Card Basic Info，并用返回的 `truncatedCardNumber` 与用户输入比对。比对成功后进入身份验证、Card Activation API 和 Set PIN 流程；具体顺序仍待确认。

```text
Card Home
→ Activate card
→ 输入实体卡后四位
→ Inquiry Card Basic Info
→ 比对 truncatedCardNumber
→ 身份验证 / Card Activation / Set PIN
```

### 3.2 激活规则

| 规则 | 结论 |
|---|---|
| 入口状态 | 仅待激活实体卡可进入激活 |
| 后四位校验 | 输入满 4 位后查询 Basic Info，读取 `truncatedCardNumber` 比对 |
| 校验失败文案 | `The last 4 digits entered are invalid` |
| 网络 / 服务异常 | 展示 Network Error / Server Error，关闭后回本页并清空输入 |
| 激活接口 | `POST /openapi/v1/card/activate` |
| autoDebit | 激活可能携带 `autoDebit`，与 Application `autoDebitEnabled` 关系待确认 |
| OTP for activation | DTC 存在 `Sent OTP For Card Activation`，AIX 是否使用待确认 |
| Set PIN 联动 | 激活成功后是否强制 Set PIN、是否可跳过待确认 |

---

## 4. PIN 设置 / 修改 / 重置

### 4.1 主流程

系统根据卡状态和 PIN 设置状态决定展示 `Set PIN` 或 `Change PIN`。

```text
ACTIVE + 未设置 PIN → Set PIN → Generate Public Pin Key → Set Card PIN(encryptedPin)
ACTIVE + 已设置 PIN → Change PIN → OTP For Reset PIN → Generate Public Pin Key → Reset Card PIN(encryptedPin)
```

### 4.2 PIN 规则

| 规则 | 结论 |
|---|---|
| Set PIN 入口 | `ACTIVE` 实体卡且未设置 PIN |
| Change PIN 入口 | `ACTIVE` 实体卡且已设置 PIN |
| 非 ACTIVE 状态 | 不展示或禁用 PIN 入口，不调用 PIN 接口 |
| PIN 格式 | 4 位数字 |
| 加密规则 | 获取 Public Pin Key 后提交 `encryptedPin`；不得使用旧字段 `encryptPin` |
| Set 接口 | Set Card PIN |
| Change / Reset 接口 | 前端显示 Change PIN，接口命名为 Reset Card PIN |
| OTP | Change PIN 前需 `OTP For Reset PIN`，具体失败锁定按 Security 规则 |
| 通知 | PIN 设置 / 重置不触发用户 Push / In-app 通知 |

---

## 5. 敏感信息查看

### 5.1 主流程

用户从 Card Home 点击 `Card detail`。系统先判断卡状态，再发起 Face Authentication。认证通过后，调用 Card Basic Info 和 Card Sensitive Info。任一接口失败时，不展示敏感信息。

```text
Card Home
→ Card detail
→ 状态判断
→ Face Authentication
→ Get Card Basic Info + Get Card Sensitive Info
→ Card detail popup
```

### 5.2 敏感信息规则

| 规则 | 结论 |
|---|---|
| 可查看状态 | `ACTIVE` 可查看完整卡信息和敏感信息 |
| `BLOCKED` | 仅可查看卡信息，不允许查看敏感信息；具体可见字段待确认 |
| 其他状态 | 不展示或禁用敏感信息入口 |
| 认证方式 | 查看敏感信息前必须 Face Authentication |
| Basic Info | 优先 `[POST] /openapi/v1/card/inquiry-card-info` |
| Sensitive Info | 优先 `[POST] /openapi/v1/card/inquiry-card-sensitive-info` |
| 展示字段 | Card type、Default currency、Name on card、Card number、EXP、CVV / CVC |
| 可复制字段 | Name on card、Card number、EXP、CVV / CVC |
| 复制成功文案 | `The information has been copied.` |
| 查询失败文案 | `Failed to get card info. Please try again later` |
| 安全边界 | Card Home 不展示完整 PAN / CVC / EXP；关闭 popup 后不得继续展示敏感信息 |

---

## 6. Lock / Unlock / Terminate

### 6.1 Lock / Unlock 主流程

`Lock Card` 适用于 `ACTIVE` 卡，用户确认后调用 Freeze Card。`Unlock Card` 适用于 `SUSPENDED` 卡，用户通过身份验证后调用 Unfreeze Card。

```text
ACTIVE → Lock Card → Lock Confirm Popup → Freeze Card → SUSPENDED
SUSPENDED → Unlock Card → Face Authentication → Unfreeze Card → Active
```

### 6.2 Lock / Unlock / Terminate 规则

| 能力 | 状态限制 | 认证 / 确认 | 接口 | 成功结果 | 失败结果 |
|---|---|---|---|---|---|
| Lock Card | `ACTIVE` | Lock 确认弹窗 | `POST /openapi/v1/card/freeze` | 卡进入 `SUSPENDED` | 保持 `ACTIVE` |
| Unlock Card | `SUSPENDED` | Face Authentication | `POST /openapi/v1/card/unfreeze` | 卡恢复 `Active` | 保持 `SUSPENDED` |
| Terminate Card | `ACTIVE` / `SUSPENDED` 理论可用 | AIX 页面流程待确认 | DTC Terminate Card | 待确认 | 不直接落实现 |

Lock 成功 Toast：`Your physical card has been locked.`  
Unlock 成功 Toast：`Your physical card has been unlocked.`

边界：上述文案写的是 physical card，是否同样适用于 virtual card 待确认。

---

## 7. Card Transaction Flow / 卡交易归集与展示边界

### 7.1 后端归集流程

DTC 通过 Card Transaction Notify 通知 AIX。AIX 接收通知后按 `event + data.id` 去重，再判断交易类型是否为 `refund / reversal / deposit`。若命中目标类型，AIX 查询当前卡 `balance`；`balance=0` 时终止，`balance>0` 时调用 Transfer Balance to Wallet，`amount=balance`。归集失败不自动重试，需要告警和人工处理。

```text
Card Transaction Notify
→ event + data.id 去重
→ type 判断：refund / reversal / deposit
→ Inquiry Card Basic Info 查询 balance
→ balance > 0 时 Transfer Balance to Wallet(amount=balance)
→ 成功结束 / 失败告警人工处理
```

### 7.2 交易展示规则

| 场景 | 规则 |
|---|---|
| Card Home Recent Transactions | 展示最近 3 条卡交易 |
| Card History | 查看最近 1 年内卡交易数据；默认当前月份最新 10 条；单次最多查询 6 个月 |
| Card Transaction Details | 上送 Transaction ID 获取最新记录 |
| 无数据 | 展示 `No transaction data` |
| 交易状态机 | 不在 Card Home 中维护，状态映射由 Transaction 模块和 ALL-GAP 承接 |
| 对账字段 | Card `data.id`、`D-REQUEST-ID`、Wallet `transactionId`、Wallet `relatedId` 的关联规则待确认 |

### 7.3 归集边界

| 边界 | 结论 |
|---|---|
| 触发类型 | 仅 `refund / reversal / deposit` 触发自动归集 |
| 金额来源 | 归集金额只取查询得到的 card balance，不按通知金额直接归集 |
| 失败处理 | Transfer 失败不自动重试，需告警和人工介入 |
| 用户展示 | AIX 对外主要展示 Wallet 资金；卡内资金不可见边界需谨慎处理 |
| 对账 | 资金追踪和最终对账由 `transaction/reconciliation.md` 承接 |

---

## 8. 字段、接口与数据

| 类型 | 名称 | 所属系统 | 用途 | 当前规则 / 边界 |
|---|---|---|---|---|
| 字段 | `cardStatus` | AIX / DTC | 判断展示组和操作权限 | 必须引用本文状态表和操作矩阵 |
| 字段 | `cardHolderName` | DTC | Name on card | Virtual / Physical 均展示 |
| 字段 | `truncatedCardNumber` | DTC | 激活时校验后四位 | 来自 Inquiry Card Basic Info |
| 字段 | `autoDebitEnabled` | AIX / DTC | 自动扣款 | 产品 `2/ON` 与 DTC `1/ON` 冲突，待确认 |
| 字段 | `encryptedPin` | DTC | 提交加密 PIN | Set / Reset PIN 均使用该字段 |
| 接口 | Inquiry Card Basic Info | DTC | 卡基础信息、余额、物流、后四位 | 优先 POST 路径 |
| 接口 | Inquiry Card Sensitive Info | DTC | PAN / EXP / CVC | 优先 POST 路径 |
| 接口 | Card Activation | DTC | 实体卡激活 | 入参和 autoDebit 关系待确认 |
| 接口 | Generate Public Pin Key | DTC | 获取 PIN 加密公钥 | 进入 PIN 设置 / 重置前调用 |
| 接口 | Set Card PIN | DTC | 首次设置 PIN | 提交 `encryptedPin` |
| 接口 | OTP For Reset PIN | DTC / Security | Change PIN 前认证 | 按 Security 规则处理 |
| 接口 | Reset Card PIN | DTC | 修改 / 重置 PIN | 前端显示 Change PIN |
| 接口 | Freeze Card | DTC | Lock Card | 失败保持 ACTIVE |
| 接口 | Unfreeze Card | DTC | Unlock Card | 失败保持 SUSPENDED |
| 接口 | Terminate Card | DTC | 注销卡 | AIX 页面流程待确认 |
| 接口 | Card Transaction Notify | DTC | 卡交易通知 | `event + data.id` 可作为去重候选 |
| 接口 | Transfer Balance to Wallet | DTC | 卡余额归集到 Wallet | amount = 查询得到的 balance |
| Header | `D-REQUEST-ID` | DTC | 请求唯一标识 | 是否承担幂等语义待确认 |
| Header | `D-SUB-ACCOUNT-ID` | DTC | DTC 子账户上下文 | 与 WalletAccount.clientId 不得写死等价 |

---

## 9. 通知规则

| 场景 | 当前处理 |
|---|---|
| Lock / Unlock 成功 | 页面 Toast，不定义 Push / In-app 通知 |
| Terminate 成功 | 待确认 |
| PIN 设置 / 重置 | 不适用，当前事实未定义通知 |
| 敏感信息查看 | 不适用，不触发通知 |
| 卡交易成功 / 退款成功 | 用户通知由 `common/notification.md` 维护 |
| 自动归集失败 | 内部 Monitor / 告警，告警模板、群、字段和责任人待确认 |

---

## 10. 待确认事项

| 问题 | 影响范围 | 是否阻塞 | 建议确认人 |
|---|---|---|---|
| 实体卡激活完整顺序：Last4 → Face Auth → Activation → Set PIN，还是 Last4 → Set PIN → Activation | Activation / PIN / Security | 是 | PM / BE / Security |
| 激活成功后 Set PIN 是否强制，用户是否可跳过 | Activation / PIN / Home | 是 | PM / Design / BE |
| `autoDebitEnabled` 产品 `2/ON` 与 DTC `1/ON` 如何映射 | Application / Activation / Home | 是 | PM / BE / DTC |
| Public Pin Key 响应字段、加密算法、`encryptedPin` 结构 | PIN / Security / DTC | 是 | BE / DTC / Security |
| Basic Info / Sensitive Info 旧 GET 路径是否废弃 | Home / Sensitive Info | 是 | BE / DTC |
| Terminate Card 的 AIX 入口、确认弹窗、认证方式、请求字段、成功失败文案、注销后状态 | Management / DTC | 是 | PM / Design / BE |
| `Activate` 是否为 `Active` 拼写问题 | Management / Home | 否 | PM / BE |
| `BLOCKED` 状态仅可查看卡信息时具体可见字段 | Status / Sensitive Info | 否 | PM / BE |
| PIN 失败提示文案、尝试次数、锁定规则 | PIN / Security | 否 | PM / Security |
| Card Transaction Notify 原始报文落库、去重、重放规则 | Transaction / Audit | 是 | BE / Audit |
| 自动归集失败告警监控群、告警字段、责任分派和人工补偿入口 | Ops / Finance / BE | 是 | PM / Ops / BE |
| Card `data.id`、`D-REQUEST-ID`、Wallet `transactionId`、Wallet `relatedId` 的最终关联规则 | Reconciliation | 是 | BE / Finance |

---

## 11. 不得推导的内容

1. 不得把未知 cardStatus 自动归一为 Active。
2. 不得把 `Activate` 写成独立卡状态。
3. 不得把 `autoDebitEnabled=2/ON` 与 DTC `1/ON` 写成已确认映射。
4. 不得把 Card `data.id`、`D-REQUEST-ID`、Wallet `transactionId`、Wallet `relatedId` 写死为同一 ID。
5. 不得把 Transfer Balance to Wallet 成功写成 Wallet 余额一定立即可见。
6. 不得在 Card Home 内维护交易状态机主事实。
7. 不得把敏感信息查询失败时的部分返回字段展示给用户。
8. 不得把 Terminate Card 直接落为 AIX 当前页面能力。

---

## 12. 来源引用

- (Ref: 历史prd/AIX Card 【manage】模块需求V1.0 .docx / 6.4 / 7.1 / 7.2 / 7.3 / 7.4 / 7.5 / 8.1 / V1.0)
- (Ref: 历史prd/AIX Card V1.0【Application】.docx / 2.1 / 2.2 / 3-4 / 5.1 / 5.2 / V1.0)
- (Ref: 历史prd/AIX Card交易【transaction】.docx / 7 / 8.1 / V1.0)
- (Ref: 历史prd/AIX APP V1.0【Transaction & History】 (1).docx / 5.2 / 5.3 / V1.1)
- (Ref: DTC Card Issuing API Document_20260310 / Card Basic Info / Card Sensitive Info / Freeze / Unfreeze / Terminate / PIN APIs / Card Transaction Notify)
- (Ref: DTC Wallet OpenAPI Documentation / Transfer Balance to Wallet / Wallet 关联字段：来源未完整核验)
- (Ref: knowledge-base/transaction/reconciliation.md)
- (Ref: knowledge-base/changelog/knowledge-gaps.md)
