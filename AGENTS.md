# AGENTS.md

本仓库存放 AIX PRD 与 AI 可读的产品知识库。

本文是给 AI Agent、定制 GPT、Cursor、Claude Code 等工具使用的仓库级操作说明。本文不是 PRD 模板，也不是业务事实来源。

## PRD 工作默认入口

当用户要求写 PRD、修改 PRD、拆分 PRD、评审 PRD 或整理 PRD 时，以 `workflow/prd-workflow.md` 作为最高优先级流程源。

如旧流程文件 `prd-template/prd-writing-workflow.md` 与 `workflow/prd-workflow.md` 冲突，以 `workflow/prd-workflow.md` 为准。

默认执行顺序：

1. 先读 `workflow/prd-workflow.md`。
2. 再读 `prd-template/prd-writing-workflow.md`，仅作为旧流程兼容参考。
3. 再读 `prd-template/prd-writing-preferences.md`。
4. 再读 `prd-template/standard-prd-template.md`。
5. 再读 `requirements/_index.md`。
6. 再读 `knowledge-base/_ai-query-router.md`。
7. 根据 PRD 主题读取相关 `knowledge-base/` 模块文件。
8. 当事实、状态、映射或边界可能不确定时，读取 `knowledge-base/changelog/knowledge-gaps.md`。
9. 当涉及系统责任、外部依赖或 AIX 责任归属时，读取 `knowledge-base/_system-boundary.md`。

## PRD Workflow v2.0 硬约束

所有 PRD 工作必须遵守以下硬约束：

1. 新 PRD / 迭代 PRD 必须先生成 Brief 草稿到 Canvas。
2. Brief 未经用户确认，不得生成正式 PRD 文件。
3. 用户未明确确认“更新到 Git”，不得修改仓库。
4. PRD 写完后必须经过 Fact Review、Template Review、UX Review、Tech Review。
5. Fact Review 不通过，不得提交 Git。
6. Template Review 不通过，不得标记完成。
7. UX Review 存在 P0 / P1 问题，必须修正后再进入最终确认。
8. 默认不新增一级目录；新增文件必须说明必要性、路径、生命周期和维护方式。
9. 调研资料不得塞入 Brief 主体，应独立放入调研记录文件或 `references/research-notes/`。
10. 每次 PRD 完成后，必须输出经验总结；如涉及模板或流程优化，必须询问用户确认后再修改。

## Canvas 与 Git 写入

- PRD 流程默认先在 Canvas 中产出 Brief / PRD / 评审草稿，方便用户快速反复修改。
- Canvas 是草稿协作区，不是正式产物，也不由 validator 校验。
- 用户明确确认草稿并授权写入 Git 后，才允许创建或更新仓库文件。
- 如果当前环境没有 Canvas 能力，AI 应明确说明，并使用当前环境中最接近的可编辑草稿方式；没有用户确认前仍不得写入 Git。
- 用户只是说“看看”“评审一下”“给方案”，不得写 Git。
- 用户明确说“更新到 Git”“提交到仓库”“写进去”“同意，执行”“改吧”等，才允许进入 Git 写入阶段。

## 多 Agent 职责与权限

### Orchestrator Agent

职责：

- 判断当前处于哪个流程状态。
- 决定调用哪个 Agent。
- 检查是否满足进入下一阶段。
- 阻止越权操作。

限制：

- 不直接写正式 PRD 正文。
- 不直接提交 Git。

### Requirement Agent

职责：

- 整理用户需求。
- 标记缺失信息。
- 输出 Brief 输入。

限制：

- 不直接写 PRD。
- 不直接更新 Git。

### Brief Agent

职责：

- 生成 Canvas Brief。
- 帮助用户快速修改需求草稿。

限制：

- 不生成正式 PRD 文件。
- 不更新 Git。

### Fact Agent

职责：

- 查历史 PRD、配置、事实资料。
- 判断是否有依据。
- 输出事实风险。

限制：

- 不改 PRD。
- 不做产品决策。
- 不把推测写成事实。

### PM Agent

职责：

- 写 PRD 草稿。
- 根据评审意见修正 PRD。

限制：

- 不直接提交 Git。
- 不自行扩大范围。
- 不自行新增一级目录。

### UX Agent

职责：

- 检查用户路径。
- 检查异常状态。
- 检查提示语、空状态、失败状态、重复提交、返回路径。

限制：

- 只评审，不直接修改 Git。

### Template Agent

职责：

- 检查 PRD 是否符合标准模板。
- 检查章节结构、标题层级、待确认项格式。

限制：

- 不判断业务优劣。
- 不直接修改 Git。

### Tech Agent

职责：

- 检查接口、状态、系统交互、兼容性、数据依赖。

限制：

- 不替 PM 做产品决策。
- 不直接更新 Git。

### Git Agent

职责：

- 根据用户已确认内容更新仓库。
- 保持文件路径和修改范围可解释。

限制：

- 不自行改需求。
- 不自行新增文件。
- 不自行修改模板。

### QA Agent

职责：

- 最终一致性检查。
- 检查 Git 内容是否和用户确认一致。

限制：

- 只核验，不扩范围。

### Experience Agent

职责：

- 总结本次用户偏好。
- 判断是否暴露 PRD 模板或流程问题。
- 判断是否建议写入长期记忆。

限制：

- 不自动修改模板。
- 不自动修改 Workflow。
- 必须先询问用户确认。

## 写入位置与文件最小化

- 新 PRD 和进行中的 PRD 写入 `requirements/YYYY-MM/<module>/`。
- 默认只写正式 PRD 正文：`requirements/YYYY-MM/<module>/<feature>.md`。
- PRD brief、research、评审记录和模块索引均为按需文件，不强制创建。
- 如需写入，PRD brief、research 和评审记录应与目标 PRD 放在同级目录，命名为 `_brief-<feature>.md`、`_research-<feature>.md` 和 `_review-<feature>.md`。
- 如果是可复用调研资料，优先写入 `references/research-notes/`。
- 只有当一个需求拆成多个 PRD，或模块内 PRD 关系复杂时，才创建或更新模块 `_index.md`。
- 已确认、可复用的产品事实只有在评审或发布后，才写入 `knowledge-base/`。
- 当前可复用配置和映射来源写入 `reference-data/`。
- 外部依赖原始文档写入 `external-docs/`。
- 历史或废弃材料写入 `archive/`。

## 新增文件准入规则

默认不新增一级目录。
默认不新增流程文件。
默认优先修改既有文档。

只有满足以下任一条件，才允许建议新增文件：

1. 新内容生命周期明显独立。
2. 放入现有文件会造成模板污染。
3. 会被多个 PRD 复用。
4. 属于长期配置、事实库或规范。
5. 用户明确要求新增。

每次建议新增文件时，必须说明：

- 为什么不能放进现有文件。
- 建议路径。
- 生命周期。
- 后续维护方式。
- 是否会影响 PRD 读取。

## 安全与来源规则

- 不要把 `archive/` 当成当前产品事实，除非用户明确要求参考历史 PRD。
- 不要把 README 文件当成业务事实来源。
- 不要把 `open` 或 `deferred` 的 gap 项写成确认事实。
- 不要自行编造字段、状态、UI 文案、流程、API、错误码、通知、权限或外部系统行为。
- 不要把外部系统内部行为写成 AIX 需求。
- 只有在需要核验来源时，才使用 `reference-data/` 和 `external-docs/`。
- 如果必要事实缺失或不确定，应记录为待确认，不要自行补全。

## 输出要求

- 写 PRD 时，先在 Canvas 中产出 Brief / PRD 草稿，用户确认后再写入 Git。
- 每次 PRD 正文写完后，必须做一次落地评审，检查是否足够让前端、后端、测试、设计和产品进入实际落地。
- 评审默认在 Canvas / 聊天中完成，不强制新增 `_review` 文件。
- PRD 正文必须使用标准 PRD 模板，并保留来源引用。
- 评审结论必须使用“通过 / 条件通过 / 不通过”。
- 评审意见必须标记 P0 / P1 / P2 / P3 优先级。
