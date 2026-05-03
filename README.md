# prd-for-ai

AIX AI-readable PRD and product knowledge repository.

This repository is used to maintain structured, source-based product facts for AIX Wallet, Card, KYC, Deposit, GTR, WalletConnect, and related external dependencies.

## Runtime entry points

| Purpose | File |
|---|---|
| AI query entry and reading route | `knowledge-base/_ai-query-router.md` |
| PRD and knowledge-base fact writing rules | `knowledge-base/_kb-ingestion-process.md` |
| System responsibility boundaries | `knowledge-base/_system-boundary.md` |
| Global confirmation gap table | `knowledge-base/changelog/knowledge-gaps.md` |
| Standard PRD template | `prd-template/standard-prd-template.md` |

## Operating rules

- Do not treat README files as business fact sources.
- Do not write inferred fields, states, UI text, flows, or external-system behavior as facts.
- Unconfirmed items must go through `knowledge-base/changelog/knowledge-gaps.md`.
- Knowledge-base updates must follow `knowledge-base/_kb-ingestion-process.md`.
- AI and human readers should start from `knowledge-base/_ai-query-router.md`.
