---
type: prd-writing-workflow
version: "1.0"
status: active
source_doc: AGENTS.md；prd-template/standard-prd-template.md；requirements/_index.md；knowledge-base/_ai-query-router.md；knowledge-base/_system-boundary.md；knowledge-base/changelog/knowledge-gaps.md；用户确认结论 2026-05-05
source_section: AI PRD 写作流程；标准 PRD 模板；requirements 使用规则；知识库路由；系统边界；ALL-GAP 使用规则
last_updated: 2026-05-05
owner: 吴忆锋
readers: [product, ui, dev, qa, business, ai]
---

# PRD 写作工作流

本文定义 AI Agent、定制 GPT、Cursor、Claude Code 等工具在本仓库中写 PRD 时应遵守的流程。

本文是工作流说明，不是 PRD 模板，也不是业务事实来源。PRD 正文仍必须使用 `prd-template/standard-prd-template.md`。

## 1. 适用范围

当用户提出以下请求时，使用本文流程：

- 写一个新的 PRD；
- 修改已有 PRD；
- 将一个原始需求拆成多个 PRD；
- 将原始需求整理成 PRD 结构；
- 检查某个 PRD 是否符合本仓库规则。

如果用户只是查询事实，且没有要求写入或修改 PRD，不要使用本文流程。

## 2. 必读顺序

写 PRD 前，按以下顺序读取文件：

```text
1. AGENTS.md
2. prd-template/prd-writing-workflow.md
3. prd-template/standard-prd-template.md
4. requirements/_index.md
5. knowledge-base/_ai-query-router.md
6. 与需求主题相关的 knowledge-base 模块索引和事实文件
7. knowledge-base/changelog/knowledge-gaps.md
8. 如涉及责任归属、外部依赖或系统边界，再读 knowledge-base/_system-boundary.md
```

只有在需要核验来源时，才读取 `reference-data/` 或 `external-docs/`。

不要默认读取 `archive/`。只有当用户明确要求参考历史 PRD 时，才读取历史材料。

## 3. 输出路径

新 PRD 必须写入月份和模块目录：

```text
requirements/YYYY-MM/<module>/<feature>.md
```

建议的配套文件：

```text
requirements/YYYY-MM/<module>/_brief-<feature>.md
requirements/YYYY-MM/<module>/_review-<feature>.md
```

如果一个用户请求包含多个独立功能，应拆成多个 PRD 文件，并新增或更新模块 `_index.md`：

```text
requirements/YYYY-MM/<module>/_index.md
requirements/YYYY-MM/<module>/<feature-a>.md
requirements/YYYY-MM/<module>/<feature-b>.md
```

模块 `_index.md` 只描述 PRD 边界、文件映射和相互引用关系，不得写成一个合并版 PRD。

## 4. 工作流阶段

### Phase 1 — 需求接收与来源路由

先判断并记录：

- 本次任务是新 PRD、修改、拆分还是评审；
- 目标模块；
- 目标功能；
- 预计输出路径；
- 相关来源文件；
- 是否需要读取系统边界或外部依赖文件。

如果需求存在歧义但仍可推进，使用最安全、最合理的假设继续，并在 brief 中标记不确定项。

### Phase 2 — 先写 Brief

写 PRD 正文前，必须先创建或提出 brief。

Brief 路径：

```text
requirements/YYYY-MM/<module>/_brief-<feature>.md
```

Brief front matter：

```yaml
---
type: prd-brief
feature: <feature>
module: <module>
brief_status: draft
target_prd: requirements/YYYY-MM/<module>/<feature>.md
source_files:
  - knowledge-base/...
open_gap_refs: []
last_updated: YYYY-MM-DD
---
```

Brief 正文应包含：

1. 用户原始请求摘要。
2. 需求目标。
3. 已确认事实。
4. 未确认边界。
5. 建议的功能拆分结论。
6. 目标 PRD 路径。
7. 需要用户确认的问题。

用户确认 brief 后，更新为：

```yaml
brief_status: confirmed
```

如果用户明确要求跳过问题并继续推进，使用：

```yaml
brief_status: skipped_questions_confirmed
```

同时必须在 brief 和 PRD 中记录采用的假设。

### Phase 3 — 功能粒度检查

使用 `prd-template/standard-prd-template.md` 第 0 章判断：当前请求是一个独立功能，还是多个独立功能。

当目标、触发条件、用户、页面、业务结果、责任方、状态模型或验收标准不同时，应拆成多个 PRD。

不得因为多个功能来自同一份原始文档或同一模块，就强行合并进同一个 PRD。

### Phase 4 — 写 PRD 正文

PRD 路径：

```text
requirements/YYYY-MM/<module>/<feature>.md
```

必备 front matter：

```yaml
---
type: prd
feature: <feature>
module: <module>
status: draft
version: "0.1"
brief_path: requirements/YYYY-MM/<module>/_brief-<feature>.md
brief_status: confirmed
source_files:
  - knowledge-base/...
open_gap_refs: []
last_updated: YYYY-MM-DD
owner: TBD
readers: [product, ui, dev, qa, business, ai]
---
```

PRD 正文必须遵循 `prd-template/standard-prd-template.md`，并保留第 0–10 章，除非用户明确要求只写局部草稿。

PRD 写作规则：

- 只有来源文件支持或用户明确确认的内容，才能写成事实。
- 不确定内容必须标记为待确认。
- 对 open 或 deferred 项，使用 `knowledge-base/changelog/knowledge-gaps.md`。
- 对 AIX 与外部系统责任边界，使用 `knowledge-base/_system-boundary.md`。
- 不要把接口字段、Header、参数、返回码、幂等细节写进业务主流程；这些内容应放在字段、接口与数据章节。
- 不要在当前 PRD 中展开另一个独立功能；应引用它或拆分它。

### Phase 5 — 生成评审记录

在 PRD 同级目录创建或更新评审记录：

```text
requirements/YYYY-MM/<module>/_review-<feature>.md
```

评审记录应检查：

1. 模板完整性。
2. 功能粒度和拆分是否正确。
3. 来源引用是否覆盖关键内容。
4. 是否与知识库事实一致。
5. ALL-GAP 是否处理正确。
6. 系统边界是否处理正确。
7. 是否误把外部系统内部行为写成 AIX 需求。
8. PRD 是否已准备好给用户评审。

评审结论必须是以下之一：

```text
pass
needs_revision
blocked_by_confirmation
```

### Phase 6 — 修订与确认

当用户修改范围、成功标准、业务规则、合规边界或功能拆分时，应先回到 brief 或拆分判断，再重写 PRD。

当用户只要求修改措辞、格式或轻量澄清时，可以直接更新 PRD，并保持来源引用不变。

允许的 PRD 状态值：

```text
draft
review
approved
deprecated
```

## 5. 来源与边界规则

除非有来源文件支持或用户明确确认，PRD 不得把以下内容写成确认事实：

- 外部系统内部行为；
- 推断出来的字段或状态；
- 来源材料中不存在的 UI 文案；
- 将通知成功等同于业务成功；
- open 或 deferred 的 gap 项；
- 未明确确认的钱包、卡、交易、KYC、DTC、AAI、WalletConnect 映射关系。

如果某项缺失或不确定，写成：

```text
当前未确认，见 ALL-GAP-XXX。
```

或放入 PRD 的待确认事项章节。

## 6. 写入后的最小回复

创建或更新文件后，最终回复只摘要说明：

- 创建或更新了哪些文件路径；
- 当前 PRD 状态；
- 仍需用户确认的事项；
- 哪些文件未能更新。

如果完整 PRD 正文已经写入仓库，不要再把全文粘贴到聊天中。
