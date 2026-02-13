# JEPA Follow-On Dispatch Bundle (MECH-058/059/060)

Generated: `2026-02-13`
Scope: first evidence pass for newly added JEPA follow-on claim stubs.

## Dispatch Matrix

| Claim | Core question | `ree-v1-minimal` role | `ree-experiments-lab` role |
|---|---|---|---|
| `MECH-058` | Does slow target anchoring preserve E1/E2 timescale separation and reduce drift? | Controlled EMA ablation in stable harness. | Stress EMA ablation under non-stationary/adversarial shifts. |
| `MECH-059` | Should latent uncertainty remain distinct from residual error for precision routing? | Deterministic dispersion vs explicit uncertainty-head comparison. | Calibration stress tests, OOD shifts, and metric-gaming checks. |
| `MECH-060` | Are pre-commit and post-commit error channels functionally distinct and necessary? | Implement clean channel split and attribution traces. | Adversarial leakage tests + replication under alternate harness seeds/environments. |

---

## Prompt 1: Dispatch to `ree-v1-minimal` (Qualification Lane)

```md
You are Codex operating in the `ree-v1-minimal` repository.

Goal: run first-pass qualification experiments for `MECH-058`, `MECH-059`, and `MECH-060` and emit contract-compliant Experiment Packs for REE_assembly ingestion.

Contract references:
- `/Users/dgolden/Documents/GitHub/REE_assembly/evidence/experiments/INTERFACE_CONTRACT.md`
- `/Users/dgolden/Documents/GitHub/REE_assembly/evidence/experiments/schemas/v1/manifest.schema.json`
- `/Users/dgolden/Documents/GitHub/REE_assembly/evidence/experiments/schemas/v1/metrics.schema.json`
- `/Users/dgolden/Documents/GitHub/REE_assembly/evidence/experiments/schemas/v1/jepa_adapter_signals.v1.json`

Required run groups:

1) `MECH-058` (experiment_type: `jepa_anchor_ablation`)
- Compare: `ema_anchor_on` vs `ema_anchor_off`
- Minimum: 3 seeds per condition
- Include stable numeric metrics (at least):
  - `latent_prediction_error_mean`
  - `latent_prediction_error_p95`
  - `latent_rollout_consistency_rate`
  - `e1_e2_timescale_separation_ratio`
  - `representation_drift_rate`

2) `MECH-059` (experiment_type: `jepa_uncertainty_channels`)
- Compare: `deterministic_plus_dispersion` vs `explicit_uncertainty_head`
- Minimum: 3 seeds per condition
- Include stable numeric metrics (at least):
  - `latent_prediction_error_mean`
  - `latent_uncertainty_calibration_error`
  - `precision_input_completeness_rate`
  - `uncertainty_coverage_rate`

3) `MECH-060` (experiment_type: `commit_dual_error_channels`)
- Compare: `single_error_stream` vs `pre_post_split_streams`
- Minimum: 3 seeds per condition
- Include stable numeric metrics (at least):
  - `pre_commit_error_signal_to_noise`
  - `post_commit_error_attribution_gain`
  - `cross_channel_leakage_rate`
  - `commitment_reversal_rate`

Pack requirements per run:
- `manifest.json` must include `claim_ids_tested` with one of:
  - `MECH-058`, `MECH-059`, `MECH-060`
- `evidence_class` and `evidence_direction` set explicitly.
- For JEPA-backed runs, emit `jepa_adapter_signals.v1.json` and set `artifacts.adapter_signals_path`.

Acceptance checks:
- Distinct seeds documented in summary.
- Pack schema validation passes in CI.
- One concise comparative report per claim with:
  - run IDs
  - condition
  - key metric deltas
  - proposed evidence_direction per run.

Constraints:
- Keep dependencies boring (stdlib-first).
- Do not refactor unrelated modules.
```

---

## Prompt 2: Dispatch to `ree-experiments-lab` (Stress Lane)

```md
You are Codex operating in the `ree-experiments-lab` repository.

Goal: stress-test `MECH-058`, `MECH-059`, and `MECH-060` with adversarial and replication-focused runs, emitting Experiment Packs ingestible by REE_assembly.

Contract references:
- `/Users/dgolden/Documents/GitHub/REE_assembly/evidence/experiments/INTERFACE_CONTRACT.md`
- `/Users/dgolden/Documents/GitHub/REE_assembly/evidence/experiments/schemas/v1/jepa_adapter_signals.v1.json`

Dispatch focus:

1) `MECH-058` (`jepa_anchor_ablation`)
- Non-stationary environment shifts + replay stress.
- Test whether EMA anchor continues to preserve separation under shift.
- Add failure signatures for collapse/drift patterns.

2) `MECH-059` (`jepa_uncertainty_channels`)
- OOD perturbations and ambiguity-heavy settings.
- Compare calibration degradation slopes across uncertainty strategies.
- Add adversarial checks for uncertainty metric gaming.

3) `MECH-060` (`commit_dual_error_channels`)
- Adversarial leakage tests to force contamination between pre/post channels.
- Verify split channel still holds attribution reliability.
- Include independent replication harness variant if available.

Minimum acceptance:
- At least 2 adversarial scenarios per claim, 2 seeds each.
- Pack contract passes (`manifest`, `metrics`, `summary`, optional adapter signals as required).
- Explicit failure signatures when stress breaks assumptions.
- Summary table per claim with:
  - scenario
  - condition
  - PASS/FAIL
  - key metric outcomes
  - evidence_direction.

Constraints:
- Keep patch focused on experiments and emitter.
- Do not refactor unrelated architecture code.
```

---

## Prompt 3: Dispatch to `REE_assembly` (Literature Lane for Same Claims)

```md
You are Codex operating in `REE_assembly`.

Goal: add targeted literature entries for `MECH-058`, `MECH-059`, and `MECH-060` to triangulate experimental results.

Create literature types:
- `evidence/literature/targeted_review_mech_058/`
- `evidence/literature/targeted_review_mech_059/`
- `evidence/literature/targeted_review_mech_060/`

Minimum:
- 1 structured entry per claim (`record.json` + `summary.md`)
- Required fields: `claim_ids_tested`, `evidence_class`, `evidence_direction`, `confidence`, `confidence_rationale`
- Prefer primary sources; include caveats explicitly.

After adding entries:
- Run `python3 evidence/experiments/scripts/build_experiment_indexes.py`
- Summarize direction/confidence changes for MECH-058/059/060.
```

---

## Ingestion Checklist After Dispatches Land

1. Pull producer repos and copy/ingest new run packs under `evidence/experiments/<type>/runs/<run_id>/`.
2. Run:
   - `python3 evidence/experiments/scripts/build_experiment_indexes.py`
   - `python3 evidence/planning/scripts/run_governance_cycle.py`
3. Review:
   - `evidence/experiments/claim_evidence.v1.json`
   - `evidence/experiments/conflicts.md`
   - `evidence/experiments/promotion_demotion_recommendations.md`
4. Decide candidate -> provisional readiness for `MECH-058/059/060` with human-in-the-loop approval.
