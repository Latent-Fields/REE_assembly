# Dispatch Messages

Generated: `2026-02-13`
Source shortlist: `evidence/planning/DISPATCH_SHORTLIST.md`

Use these as copy/paste prompts in the target Codex threads.

## 1) Dispatch to `ree-experiments-lab`

```md
You are Codex operating in the `ree-experiments-lab` repository.

Goal: execute high-priority conflict-adjudication experiments and emit Experiment Packs that are ingestible by REE_assembly.

Context:
- Dispatch IDs: `EXP-0003`, `EXP-0005`
- Claims under test: `MECH-056`, `Q-011`
- Suggested experiment type: `trajectory_integrity`
- Required acceptance checks:
  1) At least 2 additional runs with distinct seeds per claim.
  2) Experiment Pack validates against v1 schema.
  3) Result links to `claim_ids_tested` and can update direction counts in REE_assembly.

Contract to satisfy exactly:
- Follow REE_assembly Experiment Pack contract in:
  `/Users/dgolden/Documents/GitHub/REE_assembly/evidence/experiments/INTERFACE_CONTRACT.md`
- Required pack files per run:
  - `manifest.json`
  - `metrics.json`
  - `summary.md`
  - optional `traces/`, `media/`
- Required manifest fields include:
  - `claim_ids_tested` (must include either `MECH-056` or `Q-011`)
  - `evidence_class`
  - `evidence_direction` (`supports|weakens|mixed|unknown`)

Requested implementation:
1. Add/adjust experiment runner config so runs emit compliant packs.
2. Execute minimum runs:
   - `MECH-056`: 2 seeds
   - `Q-011`: 2 seeds
3. Add emitter-side schema validation in CI (fail build on invalid pack).
4. Produce a concise run report including:
   - run IDs
   - seed values
   - PASS/FAIL
   - key metric values
   - assigned `evidence_direction` per run
5. Commit changes and summarize exactly what REE_assembly should ingest.

Constraints:
- Use standard-library-first dependencies where possible.
- Do not refactor unrelated code.
- Keep metric keys stable and numeric only.
```

## 2) Dispatch to `REE_assembly` (literature lane)

```md
You are Codex operating in the `REE_assembly` repository.

Goal: execute literature-side conflict adjudication for two claims and feed structured evidence into ingestion.

Context:
- Dispatch IDs: `LIT-0004`, `LIT-0006`
- Claims: `MECH-056`, `Q-011`
- Suggested literature types:
  - `targeted_review_mech_056`
  - `targeted_review_q_011`
- Acceptance checks:
  1) At least 1 structured literature entry per claim linked via `claim_ids_tested`.
  2) Confidence explicitly justified in `confidence_rationale`.
  3) Direction is `supports|weakens|mixed|unknown` and reflected in matrix/index outputs.

Contract to satisfy:
- Follow literature contract:
  `/Users/dgolden/Documents/GitHub/REE_assembly/evidence/literature/INTERFACE_CONTRACT.md`
- Add entries under:
  - `evidence/literature/targeted_review_mech_056/entries/<entry_id>/`
  - `evidence/literature/targeted_review_q_011/entries/<entry_id>/`
- Required files:
  - `record.json`
  - `summary.md`

Required `record.json` fields:
- `claim_ids_tested`
- `evidence_class`
- `evidence_direction`
- `confidence`
- `confidence_rationale`

Requested implementation:
1. Add one structured literature entry for `MECH-056`.
2. Add one structured literature entry for `Q-011`.
3. Run ingestion:
   - `python3 evidence/experiments/scripts/build_experiment_indexes.py`
   - `python3 evidence/planning/scripts/run_governance_cycle.py`
4. Summarize impact:
   - updated direction counts/conflict ratio for both claims
   - any changes to recommendation queue
   - any new TODOs/failure signatures surfaced

Constraints:
- Prefer primary sources and clear caveats.
- Keep evidence direction assignment explicit and auditable in summaries.
- Do not modify unrelated architecture docs in this pass.
```
