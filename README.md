# prd-for-ai

AIX AI-readable PRD and product knowledge repository.

This repository is used to maintain structured, source-based product facts, new iteration PRDs, reference data, historical PRDs, and external dependency documents for AIX Wallet, Card, KYC, Deposit, GTR, WalletConnect, and related product areas.

## Directory map

| Directory | Purpose |
|---|---|
| `prd-template/` | Active PRD writing templates |
| `requirements/` | New and in-progress iteration PRDs |
| `knowledge-base/` | Confirmed AI-readable runtime product facts |
| `reference-data/` | Current reusable configuration, mapping, dictionary, FAQ, country/region, and notification source tables |
| `external-docs/` | Original external dependency documents such as DTC documents |
| `archive/` | Historical or deprecated source materials, including historical PRDs |
| `tools/` | Helper scripts for maintaining this repository |

## Runtime entry points

| Purpose | File |
|---|---|
| AI query entry and reading route | `knowledge-base/_ai-query-router.md` |
| PRD and knowledge-base fact writing rules | `knowledge-base/_kb-ingestion-process.md` |
| System responsibility boundaries | `knowledge-base/_system-boundary.md` |
| Global confirmation gap table | `knowledge-base/changelog/knowledge-gaps.md` |
| Standard PRD template | `prd-template/standard-prd-template.md` |

## Operating rules

- New PRDs go to `requirements/`.
- Confirmed reusable product facts go to `knowledge-base/`.
- Current configuration and mapping source tables go to `reference-data/`.
- External supplier source documents go to `external-docs/`.
- Historical PRDs and deprecated materials go to `archive/`.
- Helper scripts go to `tools/`.
- Do not treat README files as business fact sources.
- Do not write inferred fields, states, UI text, flows, or external-system behavior as facts.
- Unconfirmed items must go through `knowledge-base/changelog/knowledge-gaps.md`.
- Knowledge-base updates must follow `knowledge-base/_kb-ingestion-process.md`.
- AI and human readers should start from `knowledge-base/_ai-query-router.md`.
