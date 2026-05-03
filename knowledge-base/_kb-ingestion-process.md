---
module: knowledge-base
feature: kb-ingestion-process
version: "1.0"
status: active
source_doc: 用户确认结论 / PRD 模板 v1.1 / AI 查询路由表 / 系统边界文件 / ALL-GAP 总表
source_section: PRD fact rules；KB ingestion；write safety；confirmation gate
last_updated: 2026-05-03
owner: 吴忆锋
readers: [product, ui, dev, qa, ai]
---

# PRD 与知识库事实写入规范 / PRD & KB Fact Rules

## 0. 强制确认门禁

未完成用户确认，不得写入 Git。

所有 PRD 事实固化、知识库入库、文件创建、文件更新、开 PR、合并 PR，都必须经过用户确认。

强制流程：

```text
1. 输出骨架
2. 用户确认骨架
3. 输出全文草稿
4. 用户确认全文
5. 用户确认写入 Git
6. 才允许执行 Git 写入
```

禁止：

- 未确认直接创建文件
- 未确认直接更新文件
- 未确认直接开 PR
- 未确认直接合并 PR
- 自动入库
- 跳过确认步骤

最终入库必须以用户确认结果为准。

---

## 1. 文档定位

本文档规定 PRD 与知识库写作时：

```text
什么能写成事实
写到哪里
什么不能写，必须进入 ALL-GAP
```

核心关系：

```text
PRD 模板 = 规定 PRD 怎么写
本文档 = 规定什么能写成事实
```

本文档用于两类场景：

1. 写迭代 PRD 时，判断哪些内容可以写成 confirmed 需求、流程、页面、字段、状态、规则和验收标准。
2. 修改知识库时，判断 PRD、接口文档、截图、用户确认如何转成长期事实。

本文档不替代：

- `prd-template/standard-prd-template.md`
- `knowledge-base/_ai-query-router.md`
- `knowledge-base/_system-boundary.md`
- `knowledge-base/changelog/knowledge-gaps.md`

本文档不承载具体业务正文。

---

## 2. 事实来源规则

只允许以下来源写成 PRD 或知识库事实：

- 已确认 PRD
- 接口文档
- 页面截图
- 用户明确确认
- 已验证测试 / 线上现象

以下内容不得写成事实：

- AI 推测
- 合理推断
- 模糊会议记忆
- 工具摘要
- 截断内容
- open / deferred 项
- 未核验旧文档
- 外部系统内部逻辑

禁止使用以下表达包装不确定内容：

```text
应该
默认
可能
合理推测
通常会
后续会
系统应当
```

不确定内容不得伪装成事实。

---

## 3. 写 PRD 时的事实约束

写迭代 PRD 时，只能把有明确来源的内容写成 confirmed。

可以写成 confirmed 的内容包括：

- 已确认业务流程
- 已确认页面与交互
- 已确认字段 / 接口
- 已确认状态
- 已确认通知规则
- 已确认权限 / 合规 / 风控规则
- 已确认验收标准

不得写成 confirmed 的内容包括：

- 未确认流程
- 未确认页面
- 未确认字段
- 未确认状态
- 未确认页面文案
- 未确认外部系统行为
- open / deferred 项
- AI 自行补充的逻辑

PRD 中遇到未确认内容时，只能写：

```text
当前未确认，见 ALL-GAP-XXX。
```

PRD 的章节结构、页面表达、流程图、时序图、字段表、验收表格，以 `prd-template/standard-prd-template.md` 为准。

本文档只判断内容是否有资格写成事实，不规定 PRD 表达格式。

---

## 4. 知识库入库规则

知识库入库的默认原则：

```text
已有模块，优先修改原文件。
没有模块，才考虑新增文件。
新增文件必须经过用户确认。
迭代需求不得默认新建文档。
```

例如：

```text
KYC 迭代需求调整功能点
→ 修改 knowledge-base/kyc/account-opening.md
→ 不新建 kyc/account-opening-v2.md
→ 不新建 kyc/new-kyc-iteration.md
```

以下情况必须优先修改原文件：

- 原模块已存在
- 原功能已存在
- 只是规则变更
- 只是页面变更
- 只是字段变更
- 只是状态变更
- 只是流程分支变更
- 只是外部依赖结果变更

修改原文件时，必须写清：

- 新增了什么
- 修改了什么
- 替换了什么
- 哪些旧规则不再适用
- 来源是什么

只有以下情况才允许考虑新增文件：

1. 现有模块无法承载该内容。
2. 这是全新的功能域或长期独立模块。
3. 已明确文件定位。
4. 已确认不会与现有文件重复。
5. 用户已确认新增文件。

新增、改名、迁移文件时，必须同步对应模块 `_index.md`。

影响 AI 读取路径时，必须同步 `knowledge-base/_ai-query-router.md`。

涉及系统责任边界时，必须同步或核验 `knowledge-base/_system-boundary.md`。

---

## 5. 冲突与未确认项

以下情况必须进入：

```text
knowledge-base/changelog/knowledge-gaps.md
```

包括：

- 来源不足
- 规则冲突
- 页面截图缺失
- 字段含义不明确
- 状态映射不明确
- 外部系统行为不明确
- AIX 与外部系统责任不明确
- active / deferred 不明确
- 新旧知识库事实冲突

所有未确认项统一使用：

```text
ALL-GAP-XXX
```

要求：

- 全局唯一编号
- 不按模块单独编号
- 不在模块内另建待确认表
- 不在模块内写 TODO
- 不在模块内写 checklist
- 不在模块内写 local gap

模块正文中如必须引用未确认项，只能写：

```text
当前未确认，见 ALL-GAP-XXX。
```

不得写：

```text
系统默认会……
后续应该会……
合理推测……
```

---

## 6. 外部系统边界引用规则

涉及以下系统责任边界时，必须读取：

```text
knowledge-base/_system-boundary.md
```

适用对象包括：

- DTC
- AAI
- KUN
- WalletConnect
- GTR
- 第三方钱包
- 区块链网络

本文档不重新定义系统责任边界。

硬规则：

- 不得把外部系统内部逻辑写成 AIX 事实。
- 不得在 PRD 或知识库中自行补外部系统行为。
- 边界不清时，进入 ALL-GAP。
- 外部系统只记录 AIX 需要调用、接收、展示、判断、提示、记录或处理的部分。

---

## 7. PRD 模板引用规则

页面、流程、字段、通知、权限、风控、验收标准的表达格式，以以下文件为准：

```text
prd-template/standard-prd-template.md
```

本文档不规定：

- PRD 章节结构
- 页面流程图画法
- 业务时序图画法
- 外部页面样式
- 字段表格式
- 验收表格式

本文档只判断这些内容是否有事实来源，是否允许写成 confirmed，是否应进入知识库。

---

## 8. 写入安全底线

禁止将以下内容写回 Git：

```text
content truncated
truncated for brevity
(content truncated for brevity...)
tool summary
summary
partial result
```

只要读取结果出现截断提示，必须视为读取失败。

不得用以下内容覆盖原文件：

- 工具摘要
- 截断正文
- 局部片段
- 未核验复制内容
- AI 重写但未对照原文的内容

修改已有文件时，必须基于：

- 完整文件内容
- 完整 blob
- raw 文件
- 可靠 diff
- 原始 PRD / 接口文档 / 截图

Markdown 文件如果出现以下情况，必须阻断：

```text
大幅删除正文
只新增少量内容
没有明确原因
没有用户确认
```

尤其禁止把完整文件覆盖成：

```text
(content truncated for brevity...)
```

提交前必须检查 diff：

- 是否误删大段内容
- 是否出现截断提示
- 是否出现工具摘要
- 是否新增无来源事实
- 是否把未确认项写成事实
- 是否误写外部系统内部逻辑
- 是否遗漏 `_index.md`
- 是否遗漏 `_ai-query-router.md`
- 是否遗漏 `_system-boundary.md`
- 是否误提交临时文件

---

## 9. 一句话执行规则

```text
不确定的不写。
已有的优先改。
新增文件必须确认。
不能确认的进 ALL-GAP。
未确认不入库。
```
