---
module: knowledge-base
feature: kb-ingestion-process
version: "1.0"
status: active
last_updated: 2026-05-05
owner: 吴忆锋
---

# Knowledge Base Ingestion Process

This document defines how PRDs, reference data, external documents, and user-confirmed conclusions are converted into AI-readable product facts.

## 1. Source types

| Source type | Directory | Usage |
|---|---|---|
| New iteration PRD | `requirements/` | Used during drafting and review; not a confirmed fact source by default |
| Historical PRD | `archive/historical-prd/` | Used for source verification and traceability |
| Reference data | `reference-data/` | Used for current configuration, mapping, dictionary, FAQ, notification, and country/region source tables |
| External documents | `external-docs/` | Used to verify external dependency fields, events, and boundaries |
| Knowledge base | `knowledge-base/` | Stores confirmed runtime product facts |

## 2. Ingestion rule

Only write a statement into `knowledge-base/` when it is confirmed by at least one acceptable source:

1. Approved or reviewed PRD content.
2. Current reference data.
3. External document content that AIX needs to call, receive, display, notify, log, or handle.
4. Explicit user-confirmed conclusion.
5. Existing knowledge-base fact with compatible scope.

Do not write inferred fields, inferred states, inferred UI copy, external-system internal logic, or open questions as confirmed facts.

## 3. Unconfirmed items

If a rule is needed but not confirmed, write it into:

```text
knowledge-base/changelog/knowledge-gaps.md
```

Do not create module-level TODO lists, local gap tables, temporary review files, or implementation logs inside module directories.

## 4. Update path

```text
source document / reference data / external doc
        ↓ verify source and scope
knowledge-base/changelog/knowledge-gaps.md, if unresolved
        ↓ confirmed
corresponding knowledge-base module fact file
        ↓ if routing changes
knowledge-base/_ai-query-router.md
```

## 5. Boundary rule

When a fact involves AIX / DTC / AAI / KUN / WalletConnect / third-party wallet / GTR / blockchain responsibility, also check:

```text
knowledge-base/_system-boundary.md
```

AIX knowledge-base files should only maintain AIX-visible facts, responsibilities, fields, events, statuses, and handling boundaries. Do not maintain external-system internal logic.
