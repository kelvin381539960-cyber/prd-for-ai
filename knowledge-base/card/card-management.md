---
module: card
feature: card-management
version: "1.0"
status: active
source_doc: 历史prd/AIX Card manage模块需求V1.0.docx；历史prd/AIX Card V1.0【Application】.pdf；历史prd/AIX APP V1.0【Home】.pdf
source_section: Manage 6.4 卡片状态与操作限制对照表；Manage 7.4 Lock Card；Manage 7.5 Unlock Card；Manage 8.1 外部接口清单；Application 5.2 卡片首页；Home 6.1 APP主页
last_updated: 2026-05-01
owner: 吴忆锋
depends_on:
  - card/_index
  - card/card-status-and-fields
  - card/card-home
  - security/biometric-verification
  - security/face-authentication
  - _meta/writing-standard
  - changelog/knowledge-gaps
---

# Card Management 卡管理

## 1. 功能定位

Card Management 用于沉淀 Card Home 中卡管理操作的业务规则，当前已确认范围包括 Lock Card、Unlock Card，以及操作限制表中出现但缺少独立流程的注销卡能力。

本文只写卡管理操作流程、状态边界、接口依赖与失败处理。卡状态引用 `card-status-and-fields.md`，交易关联流程不在本文展开。

## 2. 适用范围

| 维度 | 规则 | 来源 | 备注 |
|---|---|---|---|
| Lock Card | Card Home 点击 Lock Card 后二次确认并调用 Freeze Card | Manage / 7.4；Manage / 8.1 | 已有明确页面逻辑 |
| Unlock Card | 通过身份验证后自动提交 Unfreeze Card | Manage / 7.5；Manage / 8.1 | 已有明确页面逻辑 |
| 注销卡 | 操作限制表中出现，但无独立流程章节 | Manage / 6.4 | 仅记录为能力缺口，不补流程 |
| 状态来源 | 引用 `card-status-and-fields.md` | Card Status & Fields | 不重新定义卡状态 |
| 认证来源 | Unlock 提到指纹、面部识别或设备密码 | Manage / 7.5 | 认证机制引用 Security 模块 |

## 3. 前置条件

| 条件 | 说明 | 来源 |
|---|---|---|
| 用户已持有卡 | 从 Card Home 的卡片操作区进入 | Card Home / 6.6 |
| 卡状态允许对应操作 | Lock / Unlock 受卡状态限制 | Manage / 6.4；Card Status & Fields |
| Lock 需二次确认 | 用户点击 Lock Card 后弹出确认弹窗 | Manage / 7.4 |
| Unlock 需身份验证 | 用户通过身份验证后系统自动提交解锁请求 | Manage / 7.5 |
| Freeze / Unfreeze 接口可用 | 调用 DTC 卡冻结 / 解冻接口 | Manage / 8.1 |

## 4. 业务流程

### 4.1 主链路

```text
Card Home → Card Management Entry → Status Check → Lock / Unlock Flow → DTC Freeze / Unfreeze → Result Handling
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

    User->>Home: 点击 Lock / Unlock
    Home->>Client: 进入卡管理操作
    Client->>Status: 校验卡状态与操作限制
    alt Operation not allowed
        Client-->>User: 隐藏、禁用或阻止操作
    else Lock Card
        Client-->>User: 展示 Lock Card 确认弹窗
        alt User clicks NO
            Client-->>User: 关闭弹窗，返回原页面
        else User clicks YES
            Client->>DTC: POST /openapi/v1/card/freeze
            alt Freeze success
                DTC-->>Card: 返回成功
                Client-->>User: 关闭弹窗并展示锁定成功提示
            else Freeze failed
                DTC-->>Card: 返回失败
                Client-->>User: 展示网络错误或后端错误提示
            end
        end
    else Unlock Card
        Client->>Security: 发起身份验证
        alt Verification failed
            Security-->>Client: 返回失败
            Client-->>User: 按 Security 规则处理
        else Verification success
            Client->>DTC: POST /openapi/v1/card/unfreeze
            Client-->>User: 按钮显示 Loading，并禁止重复提交
            alt Unfreeze success
                DTC-->>Card: 返回成功
                Client-->>User: 更新为可用展示并提示解锁成功
            else Unfreeze failed
                DTC-->>Card: 返回失败
                Client-->>User: 保留当前锁定展示并提示失败
            end
        end
    end
```

### 4.3 业务逻辑矩阵

| 阶段 | 触发条件 | 系统动作 | 成功结果 | 失败 / 拦截结果 |
|---|---|---|---|---|
| 入口判断 | 用户点击 Lock / Unlock | 校验卡状态与操作限制 | 进入对应流程 | 状态不允许则隐藏、禁用或阻止 |
| Lock 二次确认 | 用户点击 Lock Card | 展示 Lock Card Popup | 用户确认或取消 | 取消则不执行接口 |
| Lock 提交 | 用户点击 YES | 调用 Freeze Card | 关闭弹窗并提示锁定成功 | 网络异常或后端错误提示 |
| Unlock 验证 | 用户点击 Unlock | 发起身份验证 | 通过后进入提交 | 失败按 Security 处理 |
| Unlock 提交 | 身份验证通过 | 调用 Unfreeze Card；按钮 Loading，禁止重复提交 | 更新为可用展示并提示解锁成功 | 保留当前锁定展示，允许重试 |
| 注销卡 | 操作限制表出现注销卡 | 无独立流程 | 不执行正文流程 | 记录为缺口 |

## 5. 页面关系总览

```mermaid
flowchart LR
    Home[Card Home]
    Status[Card Status & Fields]
    LockEntry[Lock Card]
    LockPopup[Lock Card Popup]
    Freeze[Freeze Card API]
    UnlockEntry[Unlock Card]
    Verify[Identity Verification]
    Unfreeze[Unfreeze Card API]
    Success[Success Toast]
    Failed[Failed / Error]
    Gaps[Knowledge Gaps]

    Home -->|Lock| LockEntry
    Home -->|Unlock| UnlockEntry
    LockEntry --> Status
    UnlockEntry --> Status
    LockEntry -->|Allowed| LockPopup
    LockPopup -->|NO| Home
    LockPopup -->|YES| Freeze
    Freeze -->|Success| Success
    Freeze -.->|Failed| Failed
    UnlockEntry -->|Allowed| Verify
    Verify -->|Success| Unfreeze
    Verify -.->|Failed| Failed
    Unfreeze -->|Success| Success
    Unfreeze -.->|Failed| Failed
    Status -.->|Cancel card flow missing| Gaps
```

## 6. 页面卡片与交互规则

### 6.1 Lock Card Popup

| 元素 / 行为 | 规则 | 来源 |
|---|---|---|
| 触发条件 | 用户在 Card Home Page 点击 Lock Card | Manage / 7.4 |
| 目的 | 二次确认锁定操作，防止误触 | Manage / 7.4 |
| 标题 | `Do you want to lock card **** 9282?` | Manage / 7.4 |
| 文案 | `Once locked, this card cannot be used to make payments. You can unlock the card anytime in the app later.` | Manage / 7.4 |
| NO | 关闭弹窗，返回原页面，不执行任何操作 | Manage / 7.4 |
| YES | 触发锁定流程，调用 Freeze Card 接口 | Manage / 7.4 |
| 成功提示 | `Your physical card has been locked.` | Manage / 7.4 |

### 6.2 Lock Card 失败处理

| 场景 | 规则 | 来源 |
|---|---|---|
| 超时 / 无网络 | 提示 `No internet connection, please check the connection or try again later.` | Manage / 7.4 |
| 其他后端错误 | Toast 提示后端返回错误文案；提示：`Freeze failed` | Manage / 7.4 |

### 6.3 Unlock Card

| 元素 / 行为 | 规则 | 来源 |
|---|---|---|
| 触发条件 | 用户点击 Unlock Card | Manage / 7.5；Card Home / 6.6 |
| 身份验证 | 用户通过指纹、面部识别或设备密码后提交 | Manage / 7.5 |
| 提交机制 | 自动发起卡片解锁请求 | Manage / 7.5 |
| 接口 | 调用 Unfreeze Card 接口 | Manage / 7.5 / 8.1 |
| 提交中 | 按钮显示 `Loading...`，禁止重复提交 | Manage / 7.5 |
| 成功提示 | `Your physical card has been unlocked.` | Manage / 7.5 |
| 成功状态 | 原文写状态更新为 `Activate`，当前按缺口处理，不直接改写为 `Active` | Manage / 7.5；Card Status & Fields |

### 6.4 Unlock Card 失败处理

| 场景 | 规则 | 来源 |
|---|---|---|
| 网络异常或请求失败 | 弹出 `Sorry, we cannot unlock your card at this time. Please try again later.` | Manage / 7.5 |
| 失败后状态 | 保留当前 Locked 状态，允许用户重试 | Manage / 7.5 |
| 其他后端错误 | Toast 提示后端返回错误文案；提示：`Unfreeze failed` | Manage / 7.5 |

### 6.5 注销卡

| 项 | 当前处理 | 来源 |
|---|---|---|
| 是否出现 | 操作限制表中出现“注销卡”列 | Manage / 6.4 |
| 是否有独立流程 | 原文未提供独立流程章节 | Manage / 6.4 |
| 当前处理 | 不补流程、不补接口、不补文案，记录缺口 | Knowledge Gaps |

## 7. 字段与接口依赖

| 字段 / 接口 / 能力 | 用途 | 来源 | 备注 |
|---|---|---|---|
| `cardStatus` | 判断 Lock / Unlock 是否可用 | Card Status & Fields | 不在本文重新定义状态 |
| `Freeze Card` | 临时锁定卡片，防止交易 | Manage / 8.1 | `POST /openapi/v1/card/freeze` |
| `Unfreeze Card` | 解除卡片冻结状态，恢复使用 | Manage / 8.1 | `POST /openapi/v1/card/unfreeze` |
| `Identity Verification` | Unlock 前身份验证 | Manage / 7.5；Security | 具体规则引用 Security |
| `Card Home Operation Entry` | Lock / Unlock 入口 | Application / 5.2；Home / 6.1 | Home 只提供入口 |

## 8. 异常与失败处理

| 场景 | 触发条件 | 用户提示 / 系统动作 | 最终状态 | 来源 |
|---|---|---|---|---|
| 状态不允许操作 | 卡状态不支持 Lock / Unlock | 隐藏、禁用或阻止 | 留在原页面 | Manage / 6.4；Card Status & Fields |
| Lock 用户取消 | 用户点击 NO | 关闭弹窗，不执行接口 | 原状态不变 | Manage / 7.4 |
| Lock 网络异常 | Freeze 请求超时或无网络 | 展示网络异常提示 | 原状态待确认 | Manage / 7.4 |
| Lock 后端失败 | Freeze 后端返回错误 | Toast 后端错误文案或 `Freeze failed` | 原状态待确认 | Manage / 7.4 |
| Unlock 认证失败 | 身份验证失败 | 按 Security 规则处理 | 保留当前状态 | Manage / 7.5；Security |
| Unlock 请求失败 | Unfreeze 网络异常或请求失败 | 弹出失败提示，允许重试 | 保留 Locked 状态 | Manage / 7.5 |
| Unlock 后端失败 | Unfreeze 后端返回错误 | Toast 后端错误文案或 `Unfreeze failed` | 保留当前状态 | Manage / 7.5 |
| 注销卡缺流程 | 原文仅在操作表出现 | 不执行流程，进入缺口 | 待确认 | Manage / 6.4 |

## 9. 风控 / 合规边界

| 边界 | 规则 | 影响 | 来源 |
|---|---|---|---|
| 二次确认 | Lock Card 需二次确认 | 防止误触锁卡 | Manage / 7.4 |
| 交易限制 | 卡锁定后不能用于支付 | 降低被盗刷风险 | Manage / 7.4 |
| 身份验证 | Unlock 前需身份验证 | 防止非本人解锁 | Manage / 7.5 |
| 重复提交控制 | Unlock 提交中按钮 Loading 并禁止重复提交 | 防止重复请求 | Manage / 7.5 |
| 状态来源单一 | 状态判断引用 `card-status-and-fields.md` | 防止状态重复定义 | IMPLEMENTATION_PLAN.md / v2.7 |
| 交易边界 | 本文不处理交易关联流程 | 防止资金流程混入卡管理 | IMPLEMENTATION_PLAN.md / v2.7 |

## 10. 来源引用

- (Ref: 历史prd/AIX Card manage模块需求V1.0.docx / 6.4 卡片状态与操作限制对照表 / V1.0)
- (Ref: 历史prd/AIX Card manage模块需求V1.0.docx / 7.4 Lock Card / V1.0)
- (Ref: 历史prd/AIX Card manage模块需求V1.0.docx / 7.5 Unlock Card / V1.0)
- (Ref: 历史prd/AIX Card manage模块需求V1.0.docx / 8.1 外部接口清单 / V1.0)
- (Ref: 历史prd/AIX Card V1.0【Application】.pdf / 5.2 卡片首页 / V1.0)
- (Ref: 历史prd/AIX APP V1.0【Home】.pdf / 6.1 APP主页 / V1.0)
- (Ref: knowledge-base/card/card-status-and-fields.md)
- (Ref: knowledge-base/card/card-home.md)
- (Ref: knowledge-base/security/biometric-verification.md)
- (Ref: knowledge-base/security/face-authentication.md)
