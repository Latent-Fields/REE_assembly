# REE Typed-Claims Documentation

This repository is the canonical, typed-claims documentation system for the Reflective Ethical Engine (REE). It preserves all prior REE documentation in a quarantined legacy area while maintaining a clean, current canonical layer.

**Start here:** `docs/README.md`

## Structure

- `docs/` — Canonical REE documentation and operating procedure
- `evidence/experiments/` — Experiment Pack ingestion boundary, generated indexes, and failure-driven TODO queue
- `evidence/literature/` — Structured academic-literature evidence linked to claims with explicit confidence
- `evidence/decisions/` — Persistent human decision log for promotion/demotion governance
- `evidence/planning/` — Generated evidence backlog and experiment proposals that drive implementation repos
- `docs/claims/` — Claim registry (`claims.yaml`) and human index (`claim_index.md`)
- `docs/processed/legacy_tree/` — Verbatim preserved legacy sources (immutable)
- `docs/conflicts/` — Documented conflicts and forks (no silent resolution)
- `docs/thoughts/` — Unprocessed thought intake (raw inputs)

## Intent

This repo is documentation‑only. It is designed to:
- preserve historical formulations without deletion,
- promote new understanding into typed claims,
- and surface conflicts explicitly rather than resolving them silently.

For the full workflow and required prompts, see `docs/README.md`.

License: Apache License 2.0
