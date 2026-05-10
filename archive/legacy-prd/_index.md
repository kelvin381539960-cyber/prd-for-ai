# Legacy PRD Index

This directory contains historical PRD documents converted from old Word files.

These documents are historical references only. Do not treat them as current product facts unless the facts have been extracted into `knowledge-base/` or confirmed by approved current PRDs, current reference data, external official documents, or explicit user decisions.

## How AI should use this directory

1. Use `knowledge-base/` as the source of current product truth.
2. Use this directory only for historical reference, source verification, or old requirement comparison.
3. If a legacy PRD conflicts with `knowledge-base/`, follow `knowledge-base/`.
4. If a legacy requirement is not confirmed in `knowledge-base/`, mark it as pending confirmation.
5. Do not infer current product scope, active features, field definitions, or page behavior directly from legacy PRDs.

## Recommended reading order

When working on new PRDs or product decisions:

1. Start with `knowledge-base/_ai-query-router.md`.
2. Read the relevant `knowledge-base/` module index and fact files.
3. Check `knowledge-base/changelog/knowledge-gaps.md` for unresolved questions.
4. Use this legacy archive only when source verification or historical comparison is needed.

## Index files

- `_module-map.md`: maps product modules to related legacy PRD files.
- `_source-map.md`: maps legacy PRD files to confirmed or pending knowledge-base files.
- `_legacy-summary.md`: provides a high-level summary of historical PRD usage rules and known risks.

## Status rule

Legacy PRDs may contain outdated, removed, incomplete, or conflicting requirements. Current product truth must come from confirmed knowledge-base content or other approved current sources.
