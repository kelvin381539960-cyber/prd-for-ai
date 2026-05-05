---
type: prd-writing-workflow
version: "1.6"
status: active
source_doc: AGENTS.md；prd-template/standard-prd-template.md；prd-template/prd-writing-preferences.md；requirements/_index.md；knowledge-base/_ai-query-router.md；knowledge-base/_system-boundary.md；knowledge-base/changelog/knowledge-gaps.md；用户确认结论 2026-05-05；用户补充确认 2026-05-05 Canvas 优先确认后再写入 Git；用户确认结论 2026-05-06 长期经验沉淀机制；用户确认结论 2026-05-06 Canvas 用于草稿协作而非 harness 强校验；用户确认结论 2026-05-06 文件最小化；用户确认结论 2026-05-06 PRD 写完必须做落地评审
source_section: AI PRD 写作流程；标准 PRD 模板；PRD 写作长期偏好；requirements 使用规则；知识库路由；系统边界；ALL-GAP 使用规则；Canvas 草稿协作规则；文件最小化规则；PRD 落地评审规则
last_updated: 2026-05-06
owner: 吴忆锋
readers: [product, ui, dev, qa, business, ai]
---

# PRD 写作工作流

本文定义 AI Agent、定制 GPT、Cursor、Claude Code 等工具在本仓库中写 PRD、改 PRD、拆分 PRD、评审 PRD 时应遵守的流程。

本文是工作流说明，不是 PRD 模板，也不是业务事实来源。PRD 正文仍应使用 `prd-template/standard-prd-template.md`，写作偏好应参考 `prd-template/prd-writing-preferences.md`。

## 0. 核心原则

### 0.1 Canvas 是草稿协作区，不是正式产物

PRD 流程默认使用 Canvas 作为草稿协作区。AI 必须先在 Canvas 中输出 brief / PRD / 评审草稿，方便用户快速反复修改；用户确认后，才允许写入 Git。

Canvas 的目的：

- 让用户快速看方向、改范围、改页面、改规则；
- 避免未确认内容过早写入 Git；
- 降低反复修改正式文件的成本。

Canvas 不作为 Git 正式产物，不要求在 Git 中记录 Canvas ID，也不由 `tools/validate_prd.py` 校验。validator 只校验已经写入 `requirements/` 的正式 PRD 文件。

如果当前环境没有 Canvas 能力，AI 应明确说明，并优先使用当前环境中最接近的可编辑草稿方式；没有用户确认前，仍不得写入 Git。

### 0.2 Git 只沉淀确认后的最小必要产物

默认只写正式 PRD 正文：

```text
requirements/YYYY-MM/<module>/<feature>.md
```

以下文件均为按需文件，不强制创建：

```text
requirements/YYYY-MM/<module>/_research-<feature>.md
requirements/YYYY-MM/<module>/_brief-<feature>.md
requirements/YYYY-MM/<module>/_review-<feature>.md
requirements/YYYY-MM/<module>/_index.md
```

创建条件：

| 文件 | 默认创建 | 创建条件 |
|---|---:|---|
| `_brief-<feature>.md` | 否 | 需求复杂、需要长期追溯、拆分多个 PRD、用户要求沉淀 |
| `_research-<feature>.md` | 否 | 调研量大、来源复杂、方案比较重要、后续要复用 |
| `_review-<feature>.md` | 否 | 用户明确要求保留评审记录，或 PRD 已进入正式 review / approved 阶段 |
| `_index.md` | 否 | 一个需求拆成多个 PRD，或模块内 PRD 关系复杂 |

不得为了流程完整而强制新增过程文件。

### 0.3 每次 PRD 写完后必须做落地评审

每次 PRD 正文写完后，必须先做一次 PRD 落地评审。评审目的不是挑文案，而是判断这份 PRD 是否足够让前端、后端、测试、设计和产品进入实际落地。

评审默认在 Canvas / 聊天中完成，不强制创建 `_review-<feature>.md`。评审通过且用户确认写入 Git 后，才更新正式 PRD 文件。

评审结论只能是：

```text
pass
needs_revision
blocked_by_confirmation
```

处理规则：

- `pass`：PRD 草稿可进入用户确认写 Git。
- `needs_revision`：AI 应回到 Canvas 修改 PRD 草稿。
- `blocked_by_confirmation`：AI 只列阻塞问题，不得自行补事实。

## 1. 适用范围

当用户提出以下请求时，使用本文流程：

- 写一个新的 PRD；
- 修改已有 PRD；
- 将一个原始需求拆成多个 PRD；
- 将原始需求整理成 PRD 结构；
- 检查或评审某个 PRD 是否符合本仓库规则。

如果用户只是查询事实，且没有要求写入、修改或评审 PRD，不使用本文流程。

## 2. 必读顺序

写 PRD 前，按以下顺序读取文件：

```text
1. AGENTS.md
2. prd-template/prd-writing-workflow.md
3. prd-template/prd-writing-preferences.md
4. prd-template/standard-prd-template.md
5. requirements/_index.md
6. knowledge-base/_ai-query-router.md
7. 与需求主题相关的 knowledge-base 模块索引和事实文件
8. knowledge-base/changelog/knowledge-gaps.md（当存在缺口、open/deferred 项或事实不确定时）
9. knowledge-base/_system-boundary.md（当涉及责任归属、外部依赖或系统边界时）
```

只有在需要核验来源时，才读取 `reference-data/` 或 `external-docs/`。

不要默认读取 `archive/`。只有当用户明确要求参考历史 PRD 时，才读取历史材料。

## 3. 工作流阶段

### Phase 1 — 需求接收与来源路由

先判断并记录：

- 本次任务是新 PRD、修改、拆分还是评审；
- 目标模块；
- 目标功能；
- 预计输出路径；
- 相关来源文件；
- 是否需要读取系统边界或外部依赖文件；
- 是否需要调研记录。

如果需求存在歧义但仍可推进，使用最安全、最合理的假设继续，并在 Canvas 草稿中标记不确定项。

### Phase 2 — 在 Canvas 先写 brief 草稿

写 PRD 正文前，先在 Canvas 中输出 brief 草稿，用于确认方向。brief 草稿建议包含：

1. 用户原始请求摘要。
2. 需求目标。
3. 已确认事实。
4. 未确认边界。
5. 调研摘要（如适用，不超过 5 条）。
6. 建议的功能拆分结论。
7. 核心主流程。
8. 主页面流程（低保真原型方向）。
9. 目标 PRD 路径。
10. 需要用户确认的问题。

brief 不默认写入 Git。只有在需求复杂、需要长期追溯、拆分多个 PRD 或用户要求沉淀时，才写入：

```text
requirements/YYYY-MM/<module>/_brief-<feature>.md
```

如写入 Git，建议 front matter：

```yaml
---
type: prd-brief
feature: <feature>
module: <module>
brief_status: confirmed
or_skipped_questions: false
target_prd: requirements/YYYY-MM/<module>/<feature>.md
source_files:
  - knowledge-base/...
open_gap_refs: []
last_updated: YYYY-MM-DD
---
```

### Phase 3 — 在 Canvas 写 PRD 正文草稿

用户确认 brief 方向后，AI 在 Canvas 中输出完整 PRD 草稿，供用户逐章修改。PRD 正文应遵循 `prd-template/standard-prd-template.md`，并参考 `prd-template/prd-writing-preferences.md`。

PRD 写作规则：

- 只有来源文件支持或用户明确确认的内容，才能写成事实。
- Research / 竞品 / 调研观察只能作为参考，不能单独写成确认事实。
- 不确定内容必须标记为待确认。
- 对 open 或 deferred 项，使用 `knowledge-base/changelog/knowledge-gaps.md`。
- 对 AIX 与外部系统责任边界，使用 `knowledge-base/_system-boundary.md`。
- 不要把接口字段、Header、参数、返回码、幂等细节写进业务主流程。
- 不要在当前 PRD 中展开另一个独立功能；应引用它或拆分它。
- 不要把内部技术实现细节、内部幂等方案、内部接口设计放入 PRD 待确认项。

### Phase 4 — 功能粒度检查

根据目标、触发条件、用户、页面、业务结果、责任方、状态模型或验收标准判断：当前请求是一个独立功能，还是多个独立功能。

当目标、触发条件、用户、页面、业务结果、责任方、状态模型或验收标准不同时，应拆成多个 PRD。

不得因为多个功能来自同一份原始文档或同一模块，就强行合并进同一个 PRD。

如拆成多个 PRD，才按需创建或更新模块 `_index.md`。

### Phase 5 — PRD 落地评审

PRD 正文草稿完成后，必须做落地评审。评审检查以下 11 项：

1. 范围是否清楚：本期做什么、不做什么是否明确；是否混入独立功能；是否需要拆分。
2. 主流程是否能跑通：用户从入口到成功结果的链路是否完整；成功、失败、取消、返回、重试是否有合理结果。
3. 页面与交互是否可落地：新增 / 改造页面是否有低保真原型或明确页面结构；页面规则是否只写开发测试需要判断的内容。
4. 用户体验是否顺畅：用户是否知道当前在哪一步、为什么要做这一步、下一步会发生什么；关键操作是否有反馈；失败后是否知道怎么继续；成功后是否知道结果已生效；是否存在不必要步骤、重复确认、绕路、信息过载或让用户困惑的页面。
5. 规则是否可开发、可测试：每条产品规则是否能被开发实现、被 QA 判断对错；是否存在不可验收空话。
6. 公共能力是否正确复用：OTP、密码、BIO、Notification、风控、权限等公共能力是否只引用，不重复定义；是否会让开发误以为要改造公共能力。
7. 数据、接口、外部系统边界是否清楚：是否只写产品验收需要的数据 / 外部影响；是否误把内部字段、内部接口、幂等、日志明细写进 PRD；是否误把外部系统内部行为写成 AIX 需求。
8. 异常与失败处理是否足够：关键失败场景是否有结果；失败后数据是否保持一致；是否存在半成功、重复提交、并发、状态回退风险。
9. 来源与事实是否可靠：关键事实是否来自知识库、用户确认或明确来源；调研、竞品、推测是否没有被写成确认事实； open / deferred / gap 是否没有被写成已确认范围。
10. 待确认项是否真正必要：是否只保留影响范围、开发、测试、风控、上线的事项；技术实现细节是否没有放进产品待确认；已能从仓库查明的问题是否没有继续保留。
11. 是否可以交给团队执行：前端知道页面和交互；后端知道业务规则和数据结果；QA 知道主要验收点；UI 知道设计范围；产品知道未决事项。

评审结论为 `needs_revision` 时，回到 Canvas 修改 PRD 草稿。评审结论为 `blocked_by_confirmation` 时，只列出阻塞问题。评审结论为 `pass` 且用户确认写入 Git 后，进入下一阶段。

### Phase 6 — 用户确认后写入 Git

只有在用户明确确认 PRD 草稿通过，并授权写入 Git 后，才允许创建或更新正式 PRD 文件：

```text
requirements/YYYY-MM/<module>/<feature>.md
```

以下表达可视为写入 Git 的确认：

```text
确认
通过
确认这个版本
按这个版本写入 Git
同步到 Git
可以更新仓库
生成正式 PRD 并写入 Git
```

以下表达不视为写入 Git 的确认：

```text
继续改
先看看
再调整一下
这个方向不错
帮我补一段
```

用户在 Canvas 中提出局部修改意见，只代表继续修改 Canvas 草稿，不代表授权写入 Git。

正式 PRD 建议 front matter：

```yaml
---
type: prd
feature: <feature>
module: <module>
status: draft
version: "0.1"
brief_path:
brief_status:
source_files:
  - knowledge-base/...
external_sources: []
user_confirmation_refs: []
open_gap_refs: []
last_updated: YYYY-MM-DD
owner: TBD
readers: [product, ui, dev, qa, business, ai]
---
```

说明：

- `brief_path` 可以为空，因为 brief 不一定写入 Git。
- `source_files` 用于仓库内来源路径，建议尽量结构化填写。
- 外部网页、竞品、安全参考放入 `external_sources` 或正文来源引用，不要伪装成仓库文件。
- 关键用户确认可放入 `user_confirmation_refs` 或正文来源引用。
- `source_doc` 可作为历史兼容字段，但新 PRD 优先使用 `source_files`。

允许的 PRD 状态值：

```text
draft
review
approved
deprecated
```

### Phase 7 — 可选调研记录

如果写 PRD 前进行了大量调研、竞品观察、资料核验或方案比较，且后续需要复用，才将 research 写入 Git：

```text
requirements/YYYY-MM/<module>/_research-<feature>.md
```

Research 是过程材料，不是确认后的需求方案，也不是 PRD 事实来源。PRD 读取应以 source_files、用户确认和知识库事实为准。

### Phase 8 — 修订与确认

当用户修改范围、成功标准、业务规则、合规边界或功能拆分时，应先回到 Canvas 中的 brief 或拆分判断，再重写 PRD 草稿。

当用户只要求修改措辞、格式或轻量澄清时，可以直接更新 Canvas 中的 PRD 草稿，并保持来源引用不变；同步到 Git 仍需用户明确确认。

### Phase 9 — 经验教训总结与长期偏好沉淀

每次 PRD 完成或一次明显评审闭环结束后，AI 应输出简短经验教训总结：

```text
经验教训总结

1. 本次新增或强化的写作偏好
- ...

2. 建议沉淀到长期偏好
- ...

3. 是否需要更新标准 PRD 模板
- 是 / 否
- 原因：...
```

长期沉淀规则：

- 明确、稳定、可复用的 PRD 写作偏好，可以写入 `prd-template/prd-writing-preferences.md`。
- 不确定是否长期适用的偏好，需要先询问用户。
- 单个业务需求结论只写入对应 PRD，不写入长期偏好文件。
- 如果经验教训总结出需要调整 PRD 模板，AI 必须主动询问用户是否修改 `prd-template/standard-prd-template.md`。
- 用户明确确认后，才允许修改 `prd-template/standard-prd-template.md`。

## 4. 来源与边界规则

除非有来源文件支持或用户明确确认，PRD 不得把以下内容写成确认事实：

- 外部系统内部行为；
- 推断出来的字段或状态；
- 来源材料中不存在的 UI 文案；
- 将通知成功等同于业务成功；
- open 或 deferred 的 gap 项；
- 未明确确认的钱包、卡、交易、KYC、DTC、AAI、WalletConnect 映射关系。

如果某项缺失或不确定，写成待确认项，或写成：

```text
当前未确认，见 ALL-GAP-XXX。
```

## 5. validator 使用边界

`tools/validate_prd.py` 只校验已经写入 Git 的正式 PRD 文件，不校验 Canvas，不强制 brief / research / review 文件存在。

默认校验应尽量轻量，重点检查：

- PRD 路径是否符合 `requirements/YYYY-MM/<module>/<feature>.md`；
- front matter 基本字段是否合法；
- 仓库来源路径是否存在；
- open gap 引用是否存在；
- 本地图片 / SVG 原型路径是否存在；
- 如存在 review 文件，review 结论是否合法。

严格校验可以通过 validator 的 strict 模式实现，但 strict 不应成为普通 PRD 草稿写作的阻塞条件。

## 6. 写入后的最小回复

创建或更新文件后，最终回复只摘要说明：

- 创建或更新了哪些文件路径；
- 当前 PRD 状态；
- 评审结论；
- 仍需用户确认的事项；
- 哪些文件未能更新。

如果完整 PRD 正文已经写入仓库，不要再把全文粘贴到聊天中。
