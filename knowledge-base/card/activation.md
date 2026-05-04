---
module: card
feature: activation
version: "1.1"
status: active
source_doc: 历史prd/AIX Card manage模块需求V1.0.docx；历史prd/AIX APP V1.0【Home】.pdf；历史prd/AIX Card V1.0【Application】.pdf
source_section: Manage 7.2 卡激活；Manage 8.1 外部接口清单；Home 6.1 APP主页；Application 5.2 卡片首页
last_updated: 2026-05-04
owner: 吴忆锋
depends_on:
  - card/_index
  - card/card-status-and-fields
  - card/card-home
  - card/pin
  - security/face-authentication
  - _meta/writing-standard
  - changelog/knowledge-gaps
---

# Card Activation 实体卡激活

## 0. 文档信息

| 项 | 内容 |
|---|---|
| 文档类型 | Card Activation 标准 PRD / 知识库事实文件 |
| 当前版本 | 1.1 |
| 文档状态 | active |
| 目标读者 | Product、Design、FE、BE、QA、Risk、Compliance |
| 本次修订 | 收拢评审意见：修正后四位校验为调用 Inquiry Card Basic Info、补充 Active Card Page 交互、标记 Set PIN 顺序与 DTC OTP 待确认、补充 autoDebit 入参和验收标准 |
| 维护原则 | 激活状态和操作限制引用 `card-status-and-fields.md`；PIN 规则引用 `pin.md`；认证规则引用 Security |

## 1. 功能定位

Card Activation 用于用户收到 Physical Card 后，在 AIX App 内完成实体卡激活。

本文件只沉淀实体卡激活入口、卡号后四位校验、Face Authentication、Card Activation 接口调用、激活结果和后续 Set PIN 入口。PIN 设置规则见 `pin.md`，锁卡 / 解锁见 `card-management.md`，卡状态归一见 `card-status-and-fields.md`。

## 2. 适用范围

| 维度 | 规则 | 来源 | 备注 |
|---|---|---|---|
| 卡类型 | Physical Card | Manage / 7.2；Home / 6.1 | Virtual Card 不走实体卡激活 |
| 激活入口 | 待激活实体卡片的 `Activate card` / `Activate now` | Home / 6.1；Application / 5.2 | Card Home 只提供入口 |
| 状态来源 | 待激活展示组 | card-status-and-fields.md | 包含 `Pending activation` / `Inactive` 展示组 |
| 认证方式 | Face Authentication | Security / 7.2；Manage / 7.2 | 不在本文重复定义活体规则 |
| 卡号校验 | 用户输入实体卡卡号后四位，与 `truncatedCardNumber` 比对 | Manage / 7.2；Card Status & Fields | 用于确认用户持有实体卡 |
| 后续入口 | 激活成功后可进入 Set PIN | Manage / 7.2 | PIN 具体规则见 `pin.md` |

## 3. 前置条件

| 条件 | 说明 | 来源 |
|---|---|---|
| 用户已有待激活实体卡 | Card Home 已展示待激活实体卡片 | Home / 6.1；Card Status & Fields |
| 用户收到实体卡 | 页面文案提示收到卡后激活 | Home / 6.1；Application / 5.2 |
| 可读取卡基本信息 | 需要 `truncatedCardNumber` 用于后四位比对 | Card Status & Fields / 7.2 |
| 需完成 Face Authentication | 激活卡属于 Security 场景矩阵中的 Face Authentication 场景 | Security / 7.2 |
| Card Activation 接口可用 | 调用 `POST /openapi/v1/card/activate` | Manage / 8.1 |

## 4. 业务流程

### 4.1 主链路

```text
Card Home → Activate Card → Input Last 4 Digits → Inquiry Card Basic Info 校验后四位 → Face Authentication / Activation API / Set PIN 顺序待确认 → Activation Success / Failed
```

### 4.2 业务流程与系统交互时序图

```mermaid
sequenceDiagram
    autonumber
    actor User as User
    participant Home as Card Home
    participant Client as AIX App / Client
    participant Status as Card Status & Fields
    participant Security as Security Module
    participant Card as Card Module
    participant DTC as DTC Card API

    User->>Home: 点击 Activate card / Activate now
    Home->>Client: 进入 Active Card Page
    Client->>Status: 读取卡类型、状态、truncatedCardNumber
    alt Not physical card or not pending activation group
        Client-->>User: 阻止进入激活流程
    else Physical card pending activation
        Client-->>User: 展示输入卡号后四位页面
        User->>Client: 输入实体卡卡号后四位
        Client->>DTC: POST /openapi/v1/card/inquiry-card-info
        DTC-->>Client: 返回 truncatedCardNumber
        Client->>Client: 与接口返回 truncatedCardNumber 比对
        alt Last 4 digits mismatch
            Client-->>User: 展示校验失败提示或保持当前页
        else Last 4 digits matched
            Client->>Security: 发起 Face Authentication
            alt Face Authentication failed / locked
                Security-->>Client: 返回失败或锁定
                Client-->>User: 按 Security Face Authentication 规则处理
            else Face Authentication success
                Client->>DTC: POST /openapi/v1/card/activate
                alt Activation success
                    DTC-->>Card: 返回激活成功
                    Card-->>Client: 更新卡片进入已激活展示组
                    Client-->>User: 展示激活成功结果，并提供 Set PIN 入口
                else Activation failed
                    DTC-->>Card: 返回激活失败
                    Client-->>User: 展示激活失败承接页或错误提示
                end
            end
        end
    end
```

### 4.3 业务逻辑矩阵

| 阶段 | 触发条件 | 系统动作 | 成功结果 | 失败 / 拦截结果 |
|---|---|---|---|---|
| 入口 | 用户点击待激活实体卡的激活入口 | 进入 Active Card Page | 展示激活页面 | 非实体卡或状态不符时阻止 |
| 卡号校验 | 用户输入卡号后四位 | 与 `truncatedCardNumber` 比对 | 进入 Face Authentication | 不一致则停留当前页或提示失败 |
| 活体认证 | 卡号后四位校验通过 | 调用 Security Face Authentication | 进入激活接口调用 | 失败 / 锁定按 Security 处理 |
| 激活提交 | Face Authentication 通过 | 调用 Card Activation 接口 | 激活成功，进入已激活展示组 | 激活失败，展示失败承接 |
| 后续引导 | 激活成功 | 提供 Set PIN 入口 | 用户可继续设置 PIN | PIN 规则由 `pin.md` 承接 |

## 5. 页面关系总览

```mermaid
flowchart LR
    Home[Card Home - Pending Activation]
    ActivePage[Active Card Page]
    Last4[Input Last 4 Digits]
    Inquiry[Inquiry Card Basic Info]
    FaceAuth[Face Authentication]
    API[Card Activation API]
    Success[Activation Success]
    Failed[Activation Failed]
    SetPIN[Set PIN]
    Status[Card Status & Fields]

    Home -->|Activate card / Activate now| ActivePage
    ActivePage -->|Read card status and fields| Status
    ActivePage -->|Input last 4 digits| Last4
    Last4 -->|Submit 4 digits| Inquiry
    Inquiry -->|Matched| FaceAuth
    Inquiry -.->|Mismatch / query failed| ActivePage
    FaceAuth -->|Success| API
    FaceAuth -.->|Failed / locked| ActivePage
    API -->|Success| Success
    API -.->|Failed| Failed
    Success -->|Set PIN| SetPIN
```

## 6. 页面卡片与交互规则

### 6.1 激活入口

| 入口 | 展示条件 | 点击结果 | 来源 |
|---|---|---|---|
| `Activate card` | 待激活实体卡片 | 跳转卡激活页面 | Application / 5.2；Home / 6.1 |
| `Activate now` | 用户收到实体卡后提示区域 | 跳转卡激活页面 | Home / 6.1 |

### 6.2 Active Card Page

| 元素 / 能力 | 规则 | 来源 |
|---|---|---|
| 页面目的 | 引导用户激活实体卡 | Manage / 7.2 |
| 页面标题 | `Enter last 4 digits` | Manage / 7.2 |
| 页面说明 | `Enter the last 4-digit of your physical AIX Card number` | Manage / 7.2 |
| 返回按钮 | 点击返回时弹出 `Confirm Exit?` 挽留弹窗 | Manage / 7.2 |
| 挽留弹窗文案 | `Are you sure you want to leave before completing this step?` | Manage / 7.2 |
| 挽留弹窗按钮 | `Stay And Continue` 留在当前页；`Leave` 离开流程 | Manage / 7.2 |
| 卡号后四位输入 | 用户输入实体卡卡号后四位，满 4 位后进入校验 | Manage / 7.2 |
| 校验方式 | 调用 `Inquiry Card Basic Info`，用接口返回 `truncatedCardNumber` 与用户输入比对 | Manage / 7.2；DTC Card Issuing / 3.2.15 |
| 校验失败提示 | `The last 4 digits entered are invalid` | Manage / 7.2 |
| 提交中 | 按钮或页面显示 `Loading...`，禁止重复提交和重复输入 | Manage / 7.2 |
| Face Authentication | 校验通过后是否先进行刷脸认证需结合完整激活流程确认；当前保留为待确认顺序 | Manage / 7.2；Security / 7.2 |
| Activation API | 调用 `POST /openapi/v1/card/activate`，顺序与 Set PIN 待确认 | Manage / 8.1 |

### 6.3 激活成功

| 元素 / 能力 | 规则 | 来源 |
|---|---|---|
| 状态变化 | 激活成功后归入已激活展示组 | Card Status & Fields |
| Card Home | 返回后展示已激活卡首页 | Home / 6.1 |
| Set PIN | 激活成功后可进入 Set PIN | Manage / 7.2 |

### 6.4 激活失败

| 场景 | 规则 | 来源 |
|---|---|---|
| 卡号后四位不一致 | 阻止继续激活 | Manage / 7.2 |
| Face Authentication 失败 | 按 Security Face Authentication 规则承接 | Security / Face Authentication |
| Card Activation 接口失败 | 展示激活失败承接页或错误提示 | Manage / 7.2 / 8.1 |

## 7. 字段与接口依赖

| 字段 / 接口 / 能力 | 用途 | 来源 | 备注 |
|---|---|---|---|
| `cardType` | 判断是否 Physical Card | Card Status & Fields | Virtual Card 不走实体卡激活 |
| `cardStatus` | 判断是否待激活展示组 | Card Status & Fields | 不在本文重复定义状态 |
| `truncatedCardNumber` | 与用户输入卡号后四位比对 | Manage / 7.2；Card Status & Fields；DTC Card Issuing / 3.2.15 | 输入满 4 位后调用 Inquiry Card Basic Info 返回该字段再校验 |
| `Face Authentication` | 激活前高强度认证 | Security / 7.2；Manage / 7.2 | 具体规则见 Security |
| `Card Activation` | 实体卡激活接口 | Manage / 8.1 | `POST /openapi/v1/card/activate` |
| `autoDebit` | Card Activation 入参 | Manage / 7.2 | 当值为 `ON` 时，激活同时开启自动扣款；与申卡 `autoDebitEnabled` 的关系待确认 |
| `Sent OTP For Card Activation` | DTC 激活 OTP 能力 | DTC Card Issuing API | AIX 是否使用待确认；当前产品流程以 Face Authentication 为认证事实 |
| `Set PIN` | 激活成功后的后续入口 | Manage / 7.2 / 7.3 | 具体规则见 `pin.md` |

## 8. 异常与失败处理

| 场景 | 触发条件 | 用户提示 / 系统动作 | 最终状态 | 来源 |
|---|---|---|---|---|
| 非实体卡进入激活 | cardType 不是 Physical Card | 阻止进入激活流程 | 留在原流程 | Card Status & Fields |
| 状态不属于待激活 | cardStatus 不属于待激活展示组 | 阻止进入激活流程 | 留在原流程 | Card Status & Fields |
| 卡号后四位不匹配 | 用户输入与 Inquiry Card Basic Info 返回的 `truncatedCardNumber` 不一致 | 展示 `The last 4 digits entered are invalid`，阻止继续提交 | 留在 Active Card Page | Manage / 7.2 |
| Face Authentication 失败 | 活体认证失败或锁定 | 按 Security 失败规则处理 | 阻止激活 | Security / Face Authentication |
| Card Activation 失败 | DTC 激活接口失败 | 展示失败承接页或错误提示 | 未激活 | Manage / 7.2 / 8.1 |
| Inquiry Card Basic Info 网络异常 | 后四位校验接口超时或无网络 | 使用 Network Error Popup，关闭后清空输入框并留在 Active Card Page | 待激活 | Manage / 6.5 / 7.2 |
| Inquiry Card Basic Info 后端异常 | 后四位校验接口返回后端错误 | 使用 Server Error Popup，关闭后清空输入框并留在 Active Card Page | 待激活 | Manage / 6.5 / 7.2 |
| 激活后状态不一致 | 接口成功但卡状态未进入已激活展示组 | 记录缺口，后续需状态通知或查询确认 | 待确认 | Card Status & Fields |

## 9. 风控 / 合规边界

| 边界 | 规则 | 影响 | 来源 |
|---|---|---|---|
| 实体卡限定 | 只有 Physical Card 执行激活 | 防止虚拟卡误入激活流程 | Manage / 7.2；Card Status & Fields |
| 持卡校验 | 输入卡号后四位并与系统字段比对 | 确认用户实际持有实体卡 | Manage / 7.2 |
| 高强度认证 | 激活前需 Face Authentication | 防止非本人激活卡片 | Security / 7.2；Manage / 7.2 |
| 状态引用 | 激活成功后的状态展示引用 `card-status-and-fields.md` | 防止状态重复定义 | IMPLEMENTATION_PLAN.md / v2.4 |
| PIN 边界 | 激活后可进入 Set PIN，但 PIN 规则不在本文展开 | 防止规则混写 | Manage / 7.2 / 7.3 |

## 10. 待确认事项

| 编号 | 问题 | 影响 | 优先级 |
|---|---|---|---|
| CARD-ACT-Q001 | 激活完整顺序：后四位校验后，是先 Face Authentication、先 Set PIN，还是先 Activation API？ | Activation、PIN、Security | P0 |
| CARD-ACT-Q002 | DTC `Sent OTP For Card Activation` 是否在 AIX 使用？若不用，是否由 Face Authentication 完全替代？ | Activation、Security、DTC 接入 | P1 |
| CARD-ACT-Q003 | Card Activation 入参 `autoDebit` 与 Application `autoDebitEnabled` 的关系 | 自动扣款、Home 标签、接口入参 | P0 |
| CARD-ACT-Q004 | 激活接口成功但状态未进入 ACTIVE 时，是否主动查询状态或等待通知？ | 状态回写、Home 展示 | P1 |

## 11. 验收标准 / 测试场景

| 场景 | 验收标准 |
|---|---|
| 入口限制 | 仅待激活实体卡可进入 Active Card Page；虚拟卡、ACTIVE、SUSPENDED、PENDING、BLOCKED、CANCELLED 均不可进入 |
| 页面展示 | Active Card Page 展示 `Enter last 4 digits` 标题、说明文案、返回挽留弹窗 |
| 后四位校验 | 输入满 4 位后调用 Inquiry Card Basic Info；用返回 `truncatedCardNumber` 比对用户输入 |
| 后四位错误 | 不一致时显示 `The last 4 digits entered are invalid`，停留当前页 |
| 异常处理 | 校验接口网络 / 后端异常时使用全局 Popup，关闭后清空输入 |
| 重复提交 | Loading 中禁止重复输入、重复提交和返回导致重复请求 |
| 认证与接口 | Face Authentication、Activation API、Set PIN 的顺序未确认前，研发不得自行改变流程 |
| 成功结果 | 激活成功后状态进入 ACTIVE / 已激活展示组，并按确认后的 PIN 规则提供后续入口 |

## 12. 来源引用

- (Ref: 历史prd/AIX Card manage模块需求V1.0.docx / 7.2 卡激活 / V1.0)
- (Ref: 历史prd/AIX Card manage模块需求V1.0.docx / 8.1 外部接口清单 / V1.0)
- (Ref: 历史prd/AIX APP V1.0【Home】.pdf / 6.1 APP主页 / V1.0)
- (Ref: 历史prd/AIX Card V1.0【Application】.pdf / 5.2 卡片首页 / V1.0)
- (Ref: knowledge-base/card/card-status-and-fields.md)
- (Ref: knowledge-base/card/card-home.md)
- (Ref: knowledge-base/security/face-authentication.md)
