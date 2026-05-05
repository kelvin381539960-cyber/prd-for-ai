---
type: prd-writing-workflow
version: "1.0"
status: active
source_doc: AGENTS.md；prd-template/standard-prd-template.md；requirements/_index.md；knowledge-base/_ai-query-router.md；knowledge-base/_system-boundary.md；knowledge-base/changelog/knowledge-gaps.md；用户确认结论 2026-05-05
source_section: AI PRD writing workflow；standard PRD template；requirements usage；knowledge-base routing；system boundary；ALL-GAP usage
last_updated: 2026-05-05
owner: 吴忆锋
readers: [product, ui, dev, qa, business, ai]
---

# PRD Writing Workflow

This workflow defines how AI agents and custom GPTs should write PRDs in this repository.

It is a workflow guide, not a PRD template and not a business fact source. The PRD body must still use `prd-template/standard-prd-template.md`.

## 1. Scope

Use this workflow when the user asks to:

- write a new PRD;
- modify an existing PRD;
- split one requirement into multiple PRDs;
- organize raw requirements into PRD structure;
- review whether a PRD follows repository rules.

Do not use this workflow for ordinary fact lookup unless the user is asking to write or change a PRD.

## 2. Required reading order

Before writing a PRD, read these files in order:

```text
1. AGENTS.md
2. prd-template/prd-writing-workflow.md
3. prd-template/standard-prd-template.md
4. requirements/_index.md
5. knowledge-base/_ai-query-router.md
6. Relevant knowledge-base module index and fact files
7. knowledge-base/changelog/knowledge-gaps.md
8. knowledge-base/_system-boundary.md, if responsibility or external dependency boundaries are involved
```

Use `reference-data/` or `external-docs/` only when source verification is needed.

Do not default to `archive/` unless the user explicitly asks to reference historical PRDs.

## 3. Output paths

New PRDs must be created under a month and module path:

```text
requirements/YYYY-MM/<module>/<feature>.md
```

Recommended companion files:

```text
requirements/YYYY-MM/<module>/_brief-<feature>.md
requirements/YYYY-MM/<module>/_review-<feature>.md
```

If one user request contains multiple independent features, split them into multiple PRD files and add or update a module `_index.md`:

```text
requirements/YYYY-MM/<module>/_index.md
requirements/YYYY-MM/<module>/<feature-a>.md
requirements/YYYY-MM/<module>/<feature-b>.md
```

The module `_index.md` should only describe PRD boundaries, file mapping, and cross-references. It should not become a combined PRD.

## 4. Workflow phases

### Phase 1 — Intake and source routing

Determine:

- whether this is a new PRD, modification, split, or review;
- target module;
- target feature;
- expected output path;
- relevant source files;
- whether system boundary or external dependency files are needed.

If the request is ambiguous but still actionable, proceed with the safest reasonable assumption and mark uncertain items in the brief.

### Phase 2 — Brief first

Before writing the PRD body, create or propose a brief.

Brief path:

```text
requirements/YYYY-MM/<module>/_brief-<feature>.md
```

Brief front matter:

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

Brief body should include:

1. User request summary.
2. Requirement goal.
3. Confirmed facts.
4. Unconfirmed boundaries.
5. Suggested feature split.
6. Target PRD path.
7. Questions that need user confirmation.

After user confirmation, update:

```yaml
brief_status: confirmed
```

If the user explicitly asks to skip questions and proceed, use:

```yaml
brief_status: skipped_questions_confirmed
```

and record assumptions in the brief and PRD.

### Phase 3 — Feature granularity check

Use Section 0 of `prd-template/standard-prd-template.md` to judge whether the request is one independent feature or multiple independent features.

Split into separate PRDs when goals, triggers, users, pages, business results, owners, state models, or acceptance criteria are different.

Do not combine multiple independent features only because they come from the same raw document or module.

### Phase 4 — PRD body writing

PRD path:

```text
requirements/YYYY-MM/<module>/<feature>.md
```

Required front matter:

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

The PRD body must follow `prd-template/standard-prd-template.md` and preserve Sections 0–10 unless the user explicitly asks for a partial draft.

PRD writing rules:

- Write only source-backed or user-confirmed facts as facts.
- Mark uncertain items as pending confirmation.
- Use `knowledge-base/changelog/knowledge-gaps.md` for open or deferred items.
- Use `knowledge-base/_system-boundary.md` for AIX versus external responsibility boundaries.
- Do not write interface fields, headers, parameters, return codes, or idempotency details inside the business main flow; put them in the fields, interface, and data section.
- Do not expand another independent feature inside the current PRD; reference it or split it.

### Phase 5 — Review note

Create or update a review note next to the PRD:

```text
requirements/YYYY-MM/<module>/_review-<feature>.md
```

Review note should check:

1. Template completeness.
2. Feature granularity and split correctness.
3. Source reference coverage.
4. Knowledge-base fact consistency.
5. ALL-GAP handling.
6. System boundary handling.
7. Whether external-system internal behavior was accidentally written as AIX requirements.
8. Whether the PRD is ready for user review.

Review conclusion must be one of:

```text
pass
needs_revision
blocked_by_confirmation
```

### Phase 6 — Revision and confirmation

When the user changes scope, success criteria, business rules, compliance boundary, or feature split, return to the brief or split decision before rewriting the PRD.

When the user only requests wording, formatting, or minor clarification changes, update the PRD directly and keep the source references intact.

Allowed PRD status values:

```text
draft
review
approved
deprecated
```

## 5. Source and boundary rules

A PRD must not present the following as confirmed facts unless supported by source files or explicit user confirmation:

- external-system internal behavior;
- inferred fields or states;
- UI copy not present in source materials;
- notification success implying business success;
- open or deferred gap items;
- wallet, card, transaction, KYC, DTC, AAI, or WalletConnect mappings that are not explicitly confirmed.

If an item is missing or uncertain, write:

```text
当前未确认，见 ALL-GAP-XXX。
```

or record it in the PRD pending-confirmation section.

## 6. Minimal final response after writing

After creating or updating files, summarize only:

- created or updated file paths;
- current PRD status;
- items still needing user confirmation;
- any files that could not be updated.

Do not paste the full PRD body into chat if it has already been written to the repository.
