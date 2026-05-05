---
module: knowledge-base
feature: runtime-readme
version: "2.1"
status: active
source_doc: knowledge-base/_ai-query-router.md；knowledge-base/_system-boundary.md；knowledge-base/changelog/knowledge-gaps.md；用户确认结论 2026-05-03
source_section: runtime entry；system boundary；ALL-GAP
last_updated: 2026-05-05
owner: 吴忆锋
---

# Knowledge Base Runtime Entry

This directory is the runtime knowledge base for AIX product facts.

It is not a build-phase plan, not a draft area, and not the place to maintain temporary implementation notes, review comments, correction plans, or implementation logs.

## Primary entry points

| Purpose | File |
|---|---|
| AI daily query route | `_ai-query-router.md` |
| System responsibility boundary | `_system-boundary.md` |
| Global confirmation gap table | `changelog/knowledge-gaps.md` |

## Usage rules

1. For AI or human queries, start from `_ai-query-router.md`.
2. For module facts, read the corresponding module `_index.md`, then read the main fact file.
3. For AIX / DTC / AAI / KUN / WalletConnect responsibility questions, read `_system-boundary.md`.
4. For unresolved or conflicting items, use `changelog/knowledge-gaps.md`.
5. Do not add module-level TODO, checklist, review notes, correction plans, local gap tables, or implementation logs.
6. Do not treat README files as business fact sources.

## Current module directories

| Directory | Purpose |
|---|---|
| `account/` | Account and login-related facts |
| `home/` | App Home runtime facts and cross-module entry boundaries |
| `wallet/` | Wallet, balance, deposit, and related wallet facts |
| `card/` | Card application, Card Home, and Card Management runtime facts |
| `transaction/` | Transaction history, detail, status, and reconciliation facts |
| `kyc/` | Account Opening / KYC and related access facts |
| `common/` | Common runtime facts such as notification, errors, and FAQ |
| `integrations/` | External dependency boundaries such as DTC, AAI, and WalletConnect |
| `changelog/` | Global knowledge gaps only |

## Current scope exclusions

Website / Web / Marketing site PRDs are not included in this runtime knowledge base for now.

Non-existent wallet capabilities are not maintained in this runtime knowledge base.

## Deprecated usage

Do not use this README as:

- an implementation plan;
- a directory construction plan;
- a source of business rules;
- a replacement for `_ai-query-router.md`.
