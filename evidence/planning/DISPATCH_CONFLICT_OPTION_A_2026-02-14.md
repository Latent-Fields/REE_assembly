# Dispatch Bundle: Conflict Adjudication Option A (2026-02-14)

This is the approved execution order:
1. `MECH-060` -> `EXP-0017` (`commit_dual_error_channels`) in `ree-experiments-lab`
2. `MECH-059` -> `EXP-0015` (`jepa_uncertainty_channels`) in `ree-experiments-lab`
3. `MECH-058` -> `EXP-0013` (`jepa_anchor_ablation`) in `ree-experiments-lab`
4. `MECH-056` -> `EXP-0010` (`trajectory_integrity`) in `ree-v1-minimal`

## Claim meanings (plain language)

- `MECH-060` (dual error channels pre/post commit): use separate error-routing streams before commitment (planning/control) and after commitment (attribution/learning), instead of one merged stream.
- `MECH-059` (latent uncertainty stream separation): keep uncertainty/precision as an explicit stream, separate from generic prediction error.
- `MECH-058` (JEPA EMA target-anchor timescale separation): keep a slow stable target anchor and a faster predictor to stabilize learning under shift.
- `MECH-056` (trajectory-first residue placement): place mismatch pressure first in trajectory/decision space before representational distortion.

---

## Prompt 1: `ree-experiments-lab` (MECH-060 -> MECH-059 -> MECH-058)

```md
You are Codex operating in `ree-experiments-lab`.

Goal: execute approved conflict adjudication Option A in strict order and emit Experiment Packs ingestible by REE_assembly.

Execution order and meaning:
1) `MECH-060` (`commit_dual_error_channels`): pre-commit and post-commit error streams must remain functionally separate.
2) `MECH-059` (`jepa_uncertainty_channels`): uncertainty/precision stream must remain calibrated and non-gameable.
3) `MECH-058` (`jepa_anchor_ablation`): slow EMA anchor + fast predictor should remain stable under shift.

Dispatch IDs:
- `EXP-0017` -> `MECH-060` -> `commit_dual_error_channels`
- `EXP-0015` -> `MECH-059` -> `jepa_uncertainty_channels`
- `EXP-0013` -> `MECH-058` -> `jepa_anchor_ablation`

Contract:
- Match REE_assembly Experiment Pack contract exactly:
  `/Users/dgolden/Documents/GitHub/REE_assembly/evidence/experiments/INTERFACE_CONTRACT.md`
- Required per-run artifacts:
  - `manifest.json`
  - `metrics.json`
  - `summary.md`
  - optional `traces/`, `media/`
- Required manifest fields:
  - `claim_ids_tested`
  - `evidence_class`
  - `evidence_direction` (`supports|weakens|mixed|unknown`)

Required run minimum:
- For each experiment type above: at least 4 runs total
  - >=2 distinct seeds in nominal condition
  - >=2 adversarial/shift conditions

Targeted failure signatures to test explicitly:
- `MECH-060`: `precommit_channel_contamination`, `postcommit_channel_contamination`, `attribution_reliability_break`
- `MECH-059`: `calibration_slope_break`, `uncertainty_metric_gaming_detected`, `abstention_reliability_collapse`
- `MECH-058`: `ema_drift_under_shift`, `latent_cluster_collapse`, `anchor_separation_collapse`

After runs:
1. Validate pack shape in CI (schema check).
2. Provide a concise report table with: run_id, seed, scenario, PASS/FAIL, key metrics, evidence_direction.
3. Commit only focused changes.
```

---

## Prompt 2: `ree-v1-minimal` (MECH-056 qualification)

```md
You are Codex operating in `ree-v1-minimal`.

Goal: execute qualification runs for `MECH-056` (`trajectory_first_residue_placement`) via `trajectory_integrity` experiment and emit contract-compliant Experiment Packs.

Claim meaning:
- `MECH-056`: mismatch/residue should be applied first to trajectory/decision layer, before representational distortion.

Dispatch ID:
- `EXP-0010` -> `MECH-056` -> `trajectory_integrity`

Contract:
- Match REE_assembly Experiment Pack contract:
  `/Users/dgolden/Documents/GitHub/REE_assembly/evidence/experiments/INTERFACE_CONTRACT.md`
- Required artifacts per run:
  - `manifest.json`
  - `metrics.json`
  - `summary.md`

Run minimum:
- At least 4 runs total
  - >=2 distinct seeds for trajectory-first condition
  - >=2 comparator runs where trajectory-first placement is disabled/ablated

Stop-criteria focus (mirror REE_assembly thresholds):
- `ledger_edit_detected_count == 0`
- `explanation_policy_divergence_rate <= 0.05`
- `domination_lock_in_events == 0`

After runs:
1. Emit run report table: run_id, seed, condition, PASS/FAIL, key metrics, evidence_direction.
2. Keep metric keys numeric and stable.
3. Commit only focused changes.
```

---

## Prompt 3: `REE_assembly` ingestion after packs are pulled

```md
You are Codex in `REE_assembly`.

Goal: ingest new adjudication runs for `MECH-060`, `MECH-059`, `MECH-058`, `MECH-056` and report whether conflicts are reduced.

Claims (plain language):
- `MECH-060`: split pre-commit vs post-commit error-routing channels.
- `MECH-059`: keep uncertainty/precision stream separate from generic prediction error.
- `MECH-058`: maintain slow anchor + fast predictor timescale split.
- `MECH-056`: place residue in trajectory space first.

Steps:
1) Run ingestion/index build:
   - `python3 evidence/experiments/scripts/build_experiment_indexes.py`
2) Run governance cycle:
   - `python3 evidence/planning/scripts/run_governance_cycle.py`
3) Summarize by claim:
   - before/after direction counts
   - before/after conflict ratio
   - whether recurring failure signatures changed
   - recommendation change (hold/promote/demote)

Constraints:
- Do not refactor unrelated docs.
- Keep output as a decision-ready conflict summary.
```
