# AGENTS.md

This repository stores AIX PRDs and AI-readable product knowledge.

This file is the repository-level operating guide for AI agents, custom GPTs, Cursor, Claude Code, and similar tools. It is not a PRD template and is not a business fact source.

## Default entry for PRD work

When the user asks to write, modify, split, review, or organize a PRD:

1. Read `prd-template/prd-writing-workflow.md` first.
2. Read `prd-template/standard-prd-template.md`.
3. Read `requirements/_index.md`.
4. Read `knowledge-base/_ai-query-router.md`.
5. Read relevant `knowledge-base/` module files based on the PRD topic.
6. Read `knowledge-base/changelog/knowledge-gaps.md` when facts, states, mappings, or boundaries may be uncertain.
7. Read `knowledge-base/_system-boundary.md` when system responsibility, external dependency, or AIX ownership is involved.

## Write locations

- New and in-progress PRDs go under `requirements/YYYY-MM/<module>/`.
- PRD briefs and review notes for a PRD should stay next to that PRD, using `_brief-<feature>.md` and `_review-<feature>.md`.
- Confirmed reusable product facts go under `knowledge-base/` only after review or release.
- Current reusable configuration and mapping sources go under `reference-data/`.
- Original external dependency documents go under `external-docs/`.
- Historical or deprecated materials go under `archive/`.

## Safety and source rules

- Do not treat `archive/` as current product facts unless the user explicitly asks to reference historical PRDs.
- Do not treat README files as business fact sources.
- Do not turn `open` or `deferred` gap items into confirmed facts.
- Do not invent fields, states, UI text, flows, APIs, error codes, notifications, permissions, or external-system behavior.
- Do not write external-system internal behavior as AIX requirements.
- Use `reference-data/` and `external-docs/` only when source verification is needed.
- If required facts are missing or uncertain, record them as pending confirmation instead of inventing them.

## Output expectation

For PRD writing, first produce a brief and get the brief confirmed before creating or rewriting the PRD body. Use the standard PRD template and preserve source references in the PRD.
