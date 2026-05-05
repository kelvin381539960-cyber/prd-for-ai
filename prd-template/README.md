---
type: prd-template-index
version: "2.2"
status: active
source_doc: prd-template/standard-prd-template.md；prd-template/prd-writing-workflow.md；knowledge-base/_kb-ingestion-process.md；用户确认结论 2026-05-05
source_section: standard PRD template；PRD writing workflow；PRD fact rules；research companion files
last_updated: 2026-05-05
owner: 吴忆锋
readers: [product, ui, dev, qa, business, ai]
---

# PRD Template Index

This directory contains the active PRD writing template and AI writing workflow for AIX.

## Active files

| File | Status | Purpose |
|---|---|---|
| `standard-prd-template.md` | active | Write new AIX iteration PRDs using the page-first, business-rule-first, and source-based structure |
| `prd-writing-workflow.md` | active | Guide AI agents and custom GPTs through brief-first, source-based PRD writing in this repository |

## Usage rules

1. For AI-assisted PRD writing, read `prd-writing-workflow.md` first.
2. Use `standard-prd-template.md` as the PRD structure template.
3. Use `knowledge-base/_kb-ingestion-process.md` to decide what can be written as confirmed facts.
4. Before writing a PRD, check relevant knowledge-base modules through `knowledge-base/_ai-query-router.md`.
5. Do not write inferred fields, states, UI copy, external-system behavior, or open / deferred items as confirmed PRD facts.
6. Unconfirmed PRD content must reference `knowledge-base/changelog/knowledge-gaps.md`.
7. New PRDs should be written under `requirements/YYYY-MM/<module>/`.
8. If AI research, competitive observation, source verification, or option comparison is performed, store the full process in `requirements/YYYY-MM/<module>/_research-<feature>.md` after user confirmation.
9. Do not put full research notes in brief or PRD. Brief may reference `research_path` and include only a short research summary.

## Deprecated usage

Do not treat this README as:

- a PRD template;
- a workflow specification;
- a source of business facts;
- a list of planned templates;
- a replacement for `standard-prd-template.md` or `prd-writing-workflow.md`.
