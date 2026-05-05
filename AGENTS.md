# AGENTS.md

本仓库存放 AIX PRD 与 AI 可读的产品知识库。

本文是给 AI Agent、定制 GPT、Cursor、Claude Code 等工具使用的仓库级操作说明。本文不是 PRD 模板，也不是业务事实来源。

## PRD 工作默认入口

当用户要求写 PRD、修改 PRD、拆分 PRD、评审 PRD 或整理 PRD 时：

1. 先读 `prd-template/prd-writing-workflow.md`。
2. 再读 `prd-template/standard-prd-template.md`。
3. 再读 `requirements/_index.md`。
4. 再读 `knowledge-base/_ai-query-router.md`。
5. 根据 PRD 主题读取相关 `knowledge-base/` 模块文件。
6. 当事实、状态、映射或边界可能不确定时，读取 `knowledge-base/changelog/knowledge-gaps.md`。
7. 当涉及系统责任、外部依赖或 AIX 责任归属时，读取 `knowledge-base/_system-boundary.md`。

## 写入位置

- 新 PRD 和进行中的 PRD 写入 `requirements/YYYY-MM/<module>/`。
- PRD brief 和评审记录应与目标 PRD 放在同级目录，命名为 `_brief-<feature>.md` 和 `_review-<feature>.md`。
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

写 PRD 时，先产出 brief，并在 brief 确认后再创建或重写 PRD 正文。PRD 正文必须使用标准 PRD 模板，并保留来源引用。
