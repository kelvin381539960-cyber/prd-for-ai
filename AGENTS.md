# AGENTS.md

本仓库存放 AIX PRD 与 AI 可读的产品知识库。

本文是给 AI Agent、定制 GPT、Cursor、Claude Code 等工具使用的仓库级操作说明。本文不是 PRD 模板，也不是业务事实来源。

## PRD 工作默认入口

当用户要求写 PRD、修改 PRD、拆分 PRD、评审 PRD 或整理 PRD 时，以 `prd-template/prd-writing-workflow.md` 作为唯一流程源。

默认执行顺序：

1. 先读 `prd-template/prd-writing-workflow.md`。
2. 再读 `prd-template/prd-writing-preferences.md`。
3. 再读 `prd-template/standard-prd-template.md`。
4. 再读 `requirements/_index.md`。
5. 再读 `knowledge-base/_ai-query-router.md`。
6. 根据 PRD 主题读取相关 `knowledge-base/` 模块文件。
7. 当事实、状态、映射或边界可能不确定时，读取 `knowledge-base/changelog/knowledge-gaps.md`。
8. 当涉及系统责任、外部依赖或 AIX 责任归属时，读取 `knowledge-base/_system-boundary.md`。

## Canvas 与 Git 写入

- PRD 流程默认先在 Canvas 中输出 brief / PRD / 评审草稿，方便用户快速反复修改。
- Canvas 是草稿协作区，不是正式产物，也不由 validator 校验。
- 用户明确确认草稿并授权写入 Git 后，才允许创建或更新仓库文件。
- 如果当前环境没有 Canvas 能力，AI 应明确说明，并使用当前环境中最接近的可编辑草稿方式；没有用户确认前仍不得写入 Git。

## 写入位置与文件最小化

- 新 PRD 和进行中的 PRD 写入 `requirements/YYYY-MM/<module>/`。
- 默认只写正式 PRD 正文：`requirements/YYYY-MM/<module>/<feature>.md`。
- PRD brief、research、评审记录和模块索引均为按需文件，不强制创建。
- 如需写入，PRD brief、research 和评审记录应与目标 PRD 放在同级目录，命名为 `_brief-<feature>.md`、`_research-<feature>.md` 和 `_review-<feature>.md`。
- 只有当一个需求拆成多个 PRD，或模块内 PRD 关系复杂时，才创建或更新模块 `_index.md`。
- 已确认、可复用的产品事实只有在评审或发布后，才写入 `knowledge-base/`。
- 当前可复用配置和映射来源写入 `reference-data/`。
- 外部依赖原始文档写入 `external-docs/`。
- 历史或废弃材料写入 `archive/`。

## 安全与来源规则

- 不要把 `archive/` 当成当前产品事实，除非用户明确要求参考历史 PRD。
- 不要把 README 文件当成业务事实来源。
- 不要把 `open` 或 `deferred` 的 gap 项写成确认事实。
- 不要自行编造字段、状态、UI 文案、流程、API、错误码、通知、权限或外部系统行为。
- 不要把外部系统内部行为写成 AIX 需求。
- 只有在需要核验来源时，才使用 `reference-data/` 和 `external-docs/`。
- 如果必要事实缺失或不确定，应记录为待确认，不要自行补全。

## 输出要求

- 写 PRD 时，先在 Canvas 中产出 brief / PRD 草稿，用户确认后再写入 Git。
- 每次 PRD 正文写完后，必须做一次落地评审，检查是否足够让前端、后端、测试、设计和产品进入实际落地。
- 评审默认在 Canvas / 聊天中完成，不强制新增 `_review` 文件。
- PRD 正文必须使用标准 PRD 模板，并保留来源引用。
