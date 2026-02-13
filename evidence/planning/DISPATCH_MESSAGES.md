# Dispatch Messages

Generated: `2026-02-13`
Source shortlist: `evidence/planning/DISPATCH_SHORTLIST.md`

Use these as copy/paste prompts in the target Codex threads.

## 1) Dispatch to `ree-experiments-lab` (`EXP-0001`, `MECH-056`)

```md
You are Codex operating in the `ree-experiments-lab` repository.

Goal: execute `EXP-0001` for `MECH-056` and emit Experiment Packs ingestible by REE_assembly.

Context:
- Dispatch ID: `EXP-0001`
- Claim under test: `MECH-056`
- Suggested experiment type: `trajectory_integrity`
- Routing note: this proposal was capability-gated away from `ree-v1-minimal` because required producer capabilities were not declared there.
- Required acceptance checks:
  1) At least 2 additional runs with distinct seeds.
  2) Experiment Pack validates against v1 schema.
  3) Result links to `claim_ids_tested` and updates direction counts in REE_assembly.
  4) `metrics.json` includes required keys for every run:
     - `trajectory_commit_channel_usage_count`
     - `perceptual_sampling_channel_usage_count`
     - `structural_consolidation_channel_usage_count`
     - `precommit_semantic_overwrite_events`
     - `structural_bias_magnitude`
     - `structural_bias_rate`
  5) `precommit_semantic_overwrite_events == 0` on PASS runs.
  6) `summary.md` states channel escalation order and rationale for any non-primary channel activation.
  7) `manifest.json` includes `producer_capabilities` with flags set true for:
     - `trajectory_integrity_channelized_bias`
     - `mech056_dispatch_metric_set`
     - `mech056_summary_escalation_trace`

Contract to satisfy exactly:
- Follow REE_assembly Experiment Pack contract:
  `/Users/dgolden/Documents/GitHub/REE_assembly/evidence/experiments/INTERFACE_CONTRACT.md`
- Required pack files per run:
  - `manifest.json`
  - `metrics.json`
  - `summary.md`
  - optional `traces/`, `media/`
- Required manifest fields include:
  - `claim_ids_tested` (must include `MECH-056`)
  - `evidence_class`
  - `evidence_direction` (`supports|weakens|mixed|unknown`)

Requested implementation:
1. Update emitter defaults so `MECH-056` runs always emit the required channel metrics and required producer capability flags.
2. Execute 2+ seeds and emit compliant packs.
3. Add/keep emitter-side schema validation in CI to block invalid packs.
4. Produce a concise run report: run IDs, seeds, PASS/FAIL, key metric values, evidence direction per run.
5. Commit changes and summarize exactly what REE_assembly should ingest.

Constraints:
- Use standard-library-first dependencies where possible.
- Do not refactor unrelated code.
- Keep metric keys stable and numeric only.
```

## 2) Dispatch to `ree-experiments-lab` (`EXP-0003`, `Q-011`)

```md
You are Codex operating in the `ree-experiments-lab` repository.

Goal: execute `EXP-0003` for `Q-011` and emit Experiment Packs ingestible by REE_assembly.

Context:
- Dispatch ID: `EXP-0003`
- Claim under test: `Q-011`
- Suggested experiment type: `trajectory_integrity`
- Required acceptance checks:
  1) At least 2 additional runs with distinct seeds.
  2) Experiment Pack validates against v1 schema.
  3) Result links to `claim_ids_tested` and updates direction counts in REE_assembly.

Contract to satisfy exactly:
- Follow REE_assembly Experiment Pack contract:
  `/Users/dgolden/Documents/GitHub/REE_assembly/evidence/experiments/INTERFACE_CONTRACT.md`
- Required pack files per run:
  - `manifest.json`
  - `metrics.json`
  - `summary.md`
  - optional `traces/`, `media/`
- Required manifest fields include:
  - `claim_ids_tested` (must include `Q-011`)
  - `evidence_class`
  - `evidence_direction` (`supports|weakens|mixed|unknown`)

Requested implementation:
1. Execute 2+ seeds and emit compliant packs.
2. Add/keep emitter-side schema validation in CI to block invalid packs.
3. Produce a concise run report: run IDs, seeds, PASS/FAIL, key metric values, evidence direction per run.
4. Commit changes and summarize exactly what REE_assembly should ingest.

Constraints:
- Use standard-library-first dependencies where possible.
- Do not refactor unrelated code.
- Keep metric keys stable and numeric only.
```

## 3) Dispatch to `REE_assembly` (literature lane: `LIT-0002`, `LIT-0004`)

```md
You are Codex operating in the `REE_assembly` repository.

Goal: execute literature-side conflict adjudication for two claims and feed structured evidence into ingestion.

Context:
- Dispatch IDs: `LIT-0002`, `LIT-0004`
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
   - `python3 evidence/planning/scripts/run_governance_cycle.py --skip-thought-sweep`
4. Summarize impact:
   - updated direction counts/conflict ratio for both claims
   - any changes to recommendation queue
   - any new TODOs/failure signatures surfaced

Constraints:
- Prefer primary sources and clear caveats.
- Keep evidence direction assignment explicit and auditable in summaries.
- Do not modify unrelated architecture docs in this pass.
```

## 4) Optional Requalification Dispatch to `ree-v1-minimal`

```md
You are Codex operating in the `ree-v1-minimal` repository.

Goal: requalify `ree-v1-minimal` for future `MECH-056` dispatches by declaring required producer capabilities.

Required manifest extension:
- Add `producer_capabilities` to emitted `manifest.json` for relevant runs.
- Set these flags truthfully based on implementation:
  - `trajectory_integrity_channelized_bias`
  - `mech056_dispatch_metric_set`
  - `mech056_summary_escalation_trace`

Required behavior:
1. Ensure trajectory-integrity runs can emit the MECH-056 required metric keys.
2. Ensure summary generation can emit escalation-order and trigger-rationale statements.
3. Validate manifests against REE_assembly contract and schema.
4. Run one smoke experiment pack with `claim_ids_tested` including `MECH-056` and commit it.

Outcome expected by REE_assembly:
- capability-gate can observe declared capabilities from recent `ree-v1-minimal` packs and may route future MECH-056 proposals back to `ree-v1-minimal`.
```
