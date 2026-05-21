# Failure autopsy: V3-EXQ-597 (MECH-258)

**Generated:** 2026-05-21T12:59:23Z  
**Status:** confirmed (governance walk 2026-05-21)

## Target

- **run_id:** `v3_exq_597_mech258_pe_vs_raw_post_spcem_20260520T063328Z_v3`
- **queue_id:** V3-EXQ-597
- **claim_ids:** MECH-258
- **Outcome:** FAIL (C2 only; C0/C1 pass on PE_FORWARD)

## Facts

| Criterion | Result |
|-----------|--------|
| C0 policy entropy >= 0.10 (2/3 seeds) | PASS |
| C1 harm_a forward_r2 >= 0.3 (2/3 seeds, PE_FORWARD) | PASS |
| C2 corr(|bias|, model_pe) > corr(|bias|, raw_norm) + 0.05 (2/3 seeds) | FAIL (0/3; all correlations null) |

**Observed:** `mean_score_bias_abs == 2.0` on every seed and both conditions. All `corr_bias_model_pe`, `corr_bias_raw_norm`, `corr_delta_pe_minus_raw` are null.

**Root cause in script:** `_make_agent` sets `dacc_bias_max_abs=2.0` with `dacc_weight=0.5`, `dacc_interaction_weight=0.3`, `dacc_suppression_weight=4.0` -- the scaled bias saturates the clip, so |bias| has no variance and Pearson r is undefined.

## Diagnosis

- **Epistemic category:** measurement_gap (not substrate_ceiling, not claim falsification)
- **Biology:** precision-weighted affective PE vs raw norm in dACC-like control is plausible; failure does not contradict the mechanism class
- **Routing:** `/queue-experiment` -- 597b (or letter suffix) with non-saturating bias telemetry for C2

## Governance apply

- Manifest: `evidence_direction: non_contributory` for MECH-258
- Do not weaken MECH-258 from this run
- `review_tracker`: add run_id + dir_name
