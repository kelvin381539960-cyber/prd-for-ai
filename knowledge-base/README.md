---
module: knowledge-base
feature: runtime-readme
version: "2.0"
status: active
source_doc: knowledge-base/_ai-query-router.md；knowledge-base/_kb-ingestion-process.md；knowledge-base/_system-boundary.md；knowledge-base/changelog/knowledge-gaps.md；用户确认结论 2026-05-03
source_section: runtime entry；fact writing rules；system boundary；ALL-GAP
last_updated: 2026-05-03
owner: 吴忆锋
---

# Knowledge Base Runtime Entry

This directory is the runtime knowledge base for AIX product facts.

It is not a build-phase plan, not a draft area, and not the place to maintain temporary implementation notes.

## Primary entry points

| Purpose | File |
|---|---|
| AI daily query route | `_ai-query-router.md` |
| PRD and knowledge-base fact writing rules | `_kb-ingestion-process.md` |
| System responsibility boundary | `_system-boundary.md` |
| Global confirmation gap table | `changelog/knowledge-gaps.md` |

## Usage rules

1. For AI or human queries, start from `_ai-query-router.md`.
2. For PRD writing or knowledge-base changes, follow `_kb-ingestion-process.md`.
3. For AIX / DTC / AAI / KUN / WalletConnect responsibility questions, read `_system-boundary.md`.
4. For unresolved or conflicting items, use `changelog/knowledge-gaps.md`.
5. Do not add module-level TODO, checklist, or local gap tables.
6. Do not treat README files as business fact sources.

## Current module directories

| Directory | Purpose |
|---|---|
| `account/` | Account and login-related facts |
| `wallet/` | Wallet, balance, deposit, receive, and related wallet facts |
| `card/` | Card application, activation, management, and card transaction facts |
| `transaction/` | Transaction history, detail, status, and reconciliation facts |
| `kyc/` | Account Opening / KYC and related access facts |
| `common/` | Common dependencies such as DTC, AAI, WalletConnect, notification, errors, and FAQ |
| `changelog/` | Global knowledge gaps and change records |

## Deprecated usage

Do not use this README as:

- an implementation plan;
- a directory construction plan;
- a source of business rules;
- a replacement for `_ai-query-router.md`;
- a replacement for `_kb-ingestion-process.md`.
