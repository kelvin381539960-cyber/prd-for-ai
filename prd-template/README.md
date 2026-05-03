---
type: prd-template-index
version: "2.0"
status: active
source_doc: prd-template/standard-prd-template.md；knowledge-base/_kb-ingestion-process.md；用户确认结论 2026-05-03
source_section: standard PRD template；PRD fact rules
last_updated: 2026-05-03
owner: 吴忆锋
readers: [product, ui, dev, qa, business, ai]
---

# PRD Template Index

This directory contains the active PRD writing template for AIX.

## Active template

| Template | File | Status | Purpose |
|---|---|---|---|
| Standard PRD Template | `standard-prd-template.md` | active | Write new AIX iteration PRDs using the page-first, business-rule-first, and source-based structure |

## Usage rules

1. Use `standard-prd-template.md` as the PRD structure template.
2. Use `knowledge-base/_kb-ingestion-process.md` to decide what can be written as confirmed facts.
3. Before writing a PRD, check relevant knowledge-base modules through `knowledge-base/_ai-query-router.md`.
4. Do not write inferred fields, states, UI copy, external-system behavior, or open / deferred items as confirmed PRD facts.
5. Unconfirmed PRD content must reference `knowledge-base/changelog/knowledge-gaps.md`.

## Deprecated usage

Do not treat this README as:

- a PRD template;
- a source of business facts;
- a list of planned templates;
- a replacement for `standard-prd-template.md`.
