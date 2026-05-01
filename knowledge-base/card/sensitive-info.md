---
module: card
feature: sensitive-info
version: "1.0"
status: active
source_doc: 历史prd/AIX Card manage模块需求V1.0.docx；历史prd/AIX Card V1.0【Application】.pdf；历史prd/AIX APP V1.0【Home】.pdf
source_section: Manage 7.1 查看卡信息；Manage 8.1 外部接口清单；Application 2.2 接口范围；Application 5.2 卡片首页；Home 6.1 APP主页
last_updated: 2026-05-01
owner: 吴忆锋
depends_on:
  - card/_index
  - card/card-status-and-fields
  - card/card-home
  - security/face-authentication
  - _meta/writing-standard
  - changelog/knowledge-gaps
---

# Card Sensitive Info 卡敏感信息查看

## 1. 功能定位

Card Sensitive Info 用于用户从 Card Home / Card Detail 入口查看卡片敏感信息。

本文只沉淀敏感信息查看流程、认证边界、展示规则、接口依赖与失败处理。卡状态和字段来源引用 `card-status-and-fields.md`，Face Authentication 引用 Security 模块，Lock / Unlock 与交易流程不在本文展开。

## 2. 适用范围

| 维度 | 规则 | 来源 | 备注 |
|---|---|---|---|
| 卡类型 | Virtual Card / Physical Card | Manage / 7.1；Application / 5.2 | 两类卡均可进入 Card Detail |
| 入口 | Card Home 的 `Card detail` / `>` | Application / 5.2；Home / 6.1 | Home 只展示脱敏信息 |
| 认证方式 | Face Authentication | Security / 7.2；Manage / 7.1 | 不在本文重复定义认证规则 |
| 敏感字段 | 由 Card Status & Fields 统一维护 | Card Status & Fields / 7.3 | 本文不重新定义字段集合 |
| 展示边界 | 仅认证通过后展示 | Manage / 7.1；Security / 7.2 | 未通过认证不得展示 |

## 3. 前置条件

| 条件 | 说明 | 来源 |
|---|---|---|
| 用户已持有卡 | 从已激活 / 已冻结卡片或卡详情入口进入 | Card Home / 6.5 / 6.6 |
| 卡状态允许查看 | 状态允许范围引用 `card-status-and-fields.md` | Card Status & Fields |
| 需完成 Face Authentication | 查看敏感信息属于高强度认证场景 | Security / 7.2；Manage / 7.1 |
| Sensitive Info 接口可用 | 需调用 DTC 敏感信息查询接口 | Manage / 8.1；Application / 2.2 |

## 4. 业务流程

### 4.1 主链路

```text
Card Home → Card Detail Entry → Face Authentication → Query Sensitive Info → Display Sensitive Info / Failed
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

    User->>Home: 点击 Card detail / >
    Home->>Client: 进入卡详情查看流程
    Client->>Status: 校验卡类型、卡状态、敏感字段来源
    alt Status not allowed
        Client-->>User: 阻止查看敏感信息
    else Status allowed
        Client->>Security: 发起 Face Authentication
        alt Face Authentication failed / locked
            Security-->>Client: 返回失败或锁定
            Client-->>User: 按 Security 规则处理
        else Face Authentication success
            Client->>DTC: Query Card Sensitive Info
            alt Query success
                DTC-->>Card: 返回敏感信息结果
                Card-->>Client: 展示卡详情敏感信息
            else Query failed
                DTC-->>Card: 返回失败
                Client-->>User: 展示失败承接或错误提示
            end
        end
    end
```

### 4.3 业务逻辑矩阵

| 阶段 | 触发条件 | 系统动作 | 成功结果 | 失败 / 拦截结果 |
|---|---|---|---|---|
| 入口 | 用户点击 Card detail / `>` | 进入卡详情查看流程 | 校验卡状态与类型 | 状态不允许时阻止 |
| 认证 | 状态允许查看 | 发起 Face Authentication | 进入接口查询 | 认证失败或锁定按 Security 处理 |
| 查询 | 认证通过 | 调用敏感信息查询接口 | 返回并展示卡详情敏感信息 | 接口失败则展示失败承接 |
| 退出 | 用户离开页面 | 关闭敏感信息展示 | 返回 Card Home | 无 |

## 5. 页面关系总览

```mermaid
flowchart LR
    Home[Card Home]
    DetailEntry[Card Detail Entry]
    Status[Card Status & Fields]
    FaceAuth[Face Authentication]
    Query[Query Sensitive Info]
    Display[Display Sensitive Info]
    Failed[Failed / Blocked]

    Home -->|Card detail / >| DetailEntry
    DetailEntry -->|Check status and fields| Status
    Status -->|Allowed| FaceAuth
    Status -.->|Not allowed| Failed
    FaceAuth -->|Success| Query
    FaceAuth -.->|Failed / locked| Failed
    Query -->|Success| Display
    Query -.->|Failed| Failed
```

## 6. 页面卡片与交互规则

### 6.1 Card Home 脱敏展示

| 元素 | 规则 | 来源 |
|---|---|---|
| 卡号展示 | Card Home 默认只展示截断卡号 | Home / 6.1 |
| `Card detail` | 点击进入卡详情查看流程 | Application / 5.2；Home / 6.1 |
| `>` | 点击进入卡详情查看流程 | Home / 6.1 |
| Sensitive Info | 不在 Card Home 直接展示 | Home / 6.1；Card Status & Fields |

### 6.2 Card Detail 查看规则

| 元素 / 能力 | 规则 | 来源 |
|---|---|---|
| 认证前 | 不展示敏感信息 | Manage / 7.1；Security / 7.2 |
| 认证方式 | Face Authentication | Security / 7.2；Manage / 7.1 |
| 认证通过 | 调用敏感信息查询接口 | Manage / 8.1；Application / 2.2 |
| 认证失败 | 按 Security Face Authentication 失败规则承接 | Security / Face Authentication |
| 接口失败 | 展示失败承接或错误提示 | Manage / 8.1 |

### 6.3 字段展示边界

| 字段类别 | 规则 | 来源 |
|---|---|---|
| 脱敏字段 | 可在 Card Home / Basic Info 中展示 | Card Status & Fields / 7.2 |
| 敏感字段 | 仅认证通过后展示 | Card Status & Fields / 7.3；Manage / 7.1 |
| 字段集合 | 统一引用 `card-status-and-fields.md` | Card Status & Fields |
| 展示样例 | 不在知识库中写真实样例值 | Writing Standard |

## 7. 字段与接口依赖

| 字段 / 接口 / 能力 | 用途 | 来源 | 备注 |
|---|---|---|---|
| `cardStatus` | 判断是否允许查看 | Card Status & Fields | 不在本文重新定义状态 |
| `cardType` | 判断卡类型 | Card Status & Fields | Virtual / Physical |
| `Card Basic Info` | Card Home / Detail 脱敏展示 | Card Status & Fields / 7.2 | 路径冲突待确认 |
| `Card Sensitive Info` | 认证通过后查询敏感信息 | Card Status & Fields / 7.3 / 7.6 | 路径冲突待确认 |
| `Face Authentication` | 查看前认证 | Security / 7.2 | 具体规则见 Security |
| `requestId / token` | 认证结果查询与回跳 | Security API Reference | 不在本文重复定义 |

## 8. 异常与失败处理

| 场景 | 触发条件 | 用户提示 / 系统动作 | 最终状态 | 来源 |
|---|---|---|---|---|
| 状态不允许查看 | cardStatus 不允许查看 | 阻止进入查看流程 | 留在原流程 | Card Status & Fields |
| Face Authentication 失败 | 活体认证失败或锁定 | 按 Security 规则处理 | 阻止查看 | Security / Face Authentication |
| Face Authentication 过期 | 认证结果失效 | 重新发起认证 | 阻止查看直到认证通过 | Security / Global Rules |
| Sensitive Info 查询失败 | DTC 查询接口失败 | 展示失败承接或错误提示 | 不展示敏感信息 | Manage / 8.1 |
| 接口路径冲突 | Application 与 Manage 路径不一致 | 保留缺口，不强行统一 | 待确认 | Card Status & Fields / KG-CARD-STATUS-009 |
| 页面停留超时 | 原文未明确 | 不补规则，记录缺口 | 待确认 | 文档缺口 |

## 9. 风控 / 合规边界

| 边界 | 规则 | 影响 | 来源 |
|---|---|---|---|
| 最小展示 | Card Home 只展示脱敏字段 | 降低敏感信息泄露风险 | Home / 6.1 |
| 高强度认证 | 查看敏感信息前必须 Face Authentication | 防止非本人查看 | Security / 7.2；Manage / 7.1 |
| 不缓存明文 | 原文未给缓存策略，知识库不得补缓存规则 | 需后续确认 | 文档缺口 |
| 接口失败不展示 | 查询失败时不得展示敏感信息 | 防止错误展示 | Manage / 8.1 |
| 字段来源单一 | 敏感字段集合引用 `card-status-and-fields.md` | 防止字段重复定义 | IMPLEMENTATION_PLAN.md / v2.6 |
| 功能边界 | Lock / Unlock、交易流程不在本文处理 | 防止功能混写 | IMPLEMENTATION_PLAN.md / v2.6 |

## 10. 来源引用

- (Ref: 历史prd/AIX Card manage模块需求V1.0.docx / 7.1 查看卡信息 / V1.0)
- (Ref: 历史prd/AIX Card manage模块需求V1.0.docx / 8.1 外部接口清单 / V1.0)
- (Ref: 历史prd/AIX Card V1.0【Application】.pdf / 2.2 接口范围 / V1.0)
- (Ref: 历史prd/AIX Card V1.0【Application】.pdf / 5.2 卡片首页 / V1.0)
- (Ref: 历史prd/AIX APP V1.0【Home】.pdf / 6.1 APP主页 / V1.0)
- (Ref: knowledge-base/card/card-status-and-fields.md)
- (Ref: knowledge-base/card/card-home.md)
- (Ref: knowledge-base/security/face-authentication.md)
