# Failure Autopsy: V3-EXQ-919 (MECH-321)

**Generated:** 2026-08-13T05:24:45Z
**Scope:** single
**Status:** confirmed
**Dry-run check:** clean

## 1. Facts

- **Run:** `v3_exq_919_mech321_harm_aware_selection_unconditional_wholeepisode_20260811T225107Z_v3`, queue_id V3-EXQ-919, claim_ids `["MECH-321"]` (`bears_on`: ARC-070, ARC-071, SD-hazard-aware-policy-decomposition — context only, not claim-weighted).
- **Outcome:** FAIL, `evidence_direction: weakens`, `non_degenerate: true`. `interpretation.label`: `harm_aware_selection_does_not_reduce_task_harm_unconditional` — a genuine negative-result self-route, not a precondition-failure branch.
- **Criteria:** C1 (load-bearing, `harm_delta_mean_unconditional > 0`) — **FAIL**, measured -0.0037281. C2 (mechanistic PE corroboration, non-load-bearing) — **FAIL**, measured -0.0000422.
- **Preconditions:** all green (`per_arm_gate.all_green: true`, `red_arms: []`). OFF-arm harm-bias inertness met, ON-arm engagement robust (150+ min fires/cell), 4/4 A-A null-control replicate pairs bit-identical (`aa_control.ok: true`, `max_abs_delta: 0.0`).
- **Power:** n=40 seeds (`enough_seeds: true`), SE 0.02292. `engagement_outcome_spearman_rho = -0.28563` — more engagement of the harm bias weakly correlates with a *worse*, not better, outcome. Recording provenance clean.
- **Substrate note:** `substrate_stable_across_run: false` internally — but `per_cell_hashes_disagree: false` (every measurement cell used the same hash throughout); the repo simply advanced on disk after the run finished (`lag_seconds ≈ 16134`, matching wall-clock). Not a threat to internal validity.

## 2. Lineage

This is the 5th generation of the same behavioural-effect question: V3-EXQ-844 (structural gap: no harm signal reached the redecomposition step) → 867 (bias never engaged) → 867a (n=2, underpowered) → 867b (pool-exhausted, screen-soundness confound — later traced to an RNG-reset asymmetry between screen cells and measurement cells, an instrumentation artifact, not evidence the manipulation perturbs decomposition) → **919**, which took a **new EXQ number** (not `867c`) because it changes three design axes at once: no screen (every seed enters via `arm_cell`), unconditional whole-episode DV (no divergence-tick windowing/conditioning), n=40 pre-registered hard floor with an A-A null control discharging the matching-validity precondition by construction.

**919 is the first run in this lineage to reach a clean, non-degenerate, fully-powered reading** — no precondition failures, no pool exhaustion, no screen-soundness question (no screen exists in this design).

## 3. Claim-layer mapping — MECH-321

Policy decomposition via event segmenter — first child mechanism for ARC-070. `status: candidate`, `epistemic_category`: unset (this run is the opportunity to set it), `v3_pending: true`, `pending_retest_after_substrate: true`. `depends_on`: ARC-070, MECH-288, MECH-269, MECH-094 — all confirmed built. The harm-bias/selection substrate itself was built 2026-08-01, closing the structural gap V3-EXQ-844 identified. **919 is the first test of a substrate now structurally complete for this question** — earlier FAILs were readiness/measurement-instrument failures on top of that same substrate, not tests of an incomplete one.

## 4. Biological-reference triage

Closest reference: Fanselow's Predatory Imminence Continuum + threat-modulated defensive-path-selection literature (Mobbs, Evans, Cooper, Blanchard & Blanchard). A dedicated 9-entry lit-pull exists (`targeted_review_threat_modulated_defensive_path_selection`, pulled 2026-08-01, commissioned directly by V3-EXQ-844's autopsy). That review's Form B ("two-stage regime-sensitive": continuously-graded harm-bias + threshold-gated categorical override) is what got built — a genuine, literature-grounded translation, not a bare formal import. **But two literature-identified co-determinants are explicitly deferred, not built:** escapability (distance-to-refuge/relative-speed/path-angle — Cooper 2016) and threat-cue predictability/certainty (Fanselow 2022, Blanchard & Blanchard 1989). Both are named in the lit-pull's own "deferred refinement, not blocking a first buildable version" section. This is a real, literature-grounded candidate explanation for the null result — magnitude alone is not, per the reference literature, what drives adaptive defensive selection; escapability and imminence/rate-of-change are co-determinants.

## 5. Four-layer diagnosis

| Layer | Status | Note |
|---|---|---|
| Claim alignment | weakened | Cleanest, best-powered test yet; C1 fails negative, C2 fails to corroborate |
| Biological reference | partial | Well-grounded lit-pull; two co-determinants explicitly deferred |
| Prerequisites | present | All 4 depends_on landed |
| Implementation completeness | complete | Both selection stages built, wired, confirmed non-inert |
| Environment adequacy | adequate | Robust engagement, no environment-side precondition failed |
| Measurement adequacy | adequate | The explicit fix-point of this lineage — first genuinely decisive measurement |
| Integration adequacy | coupled but unstable | Genuinely integrated; net effect inconsistent in sign across seeds |
| Scale/capacity | adequate | n=40 meets pre-registered power floor |

**Failure-location (GOV-FAILLOC-1):** MECHANISM FAILED only (Implementation = complete). MEASURES and ENVIRONMENT are both adequate but that alone doesn't establish REE FAILED — this is a clean negative result on a structurally complete but biologically partial (magnitude-only) implementation, not a REE-wide or infrastructure failure.

## 6. Re-derive brake & granularity-debt checks

- **Re-derive brake:** 0 prior confirmed `substrate_ceiling` hits across all 6 confirmed MECH-321 targets (categories used: `standard` x2, `competence_implementation_gap`, `environment_adequacy_defect`, `measurement_test_design_defect` x2). Does **not** fire.
- **Granularity-debt:** 6 prior targets, 1 `weakened` (V3-EXQ-844 — partial, mechanistically-corroborated). 919's signature (both C1 and C2 fail, engagement now anti-correlates) is **structurally different** from 844's — a broader, more decisive negative on a now-structurally-complete substrate, not a repetition. Does **not** fire `/claim-synthesis` routing.

## 7. Hypothesis-space ledger

This run resolves a **pre-registered question**: `mech321_harm_aware_selection_task_effect` (qid), single hypothesis `H-harm-aware-reduces-task-harm`, previously `alive` with `adjudicating_runs: [844, 867, 867a, 867b]`. The question's own `decision.live_gate` explicitly named the redesign V3-EXQ-919 implements ("unconditional whole-episode harm-rate DV... n=40... assign a NEW EXQ number"). **Resolved to `eliminated`** — control_passed (A-A bit-identical), non_degenerate=true, met_elimination_bar=true. `growth_restriction`: none present, no STOP triggered. Ledger update applied in Step 9b (see `hypothesis_space_registry.v1.json` diff in this session's commit).

## 8. Recommended epistemic_category

`standard`. Ordinary mechanism-hypothesis test with a clean negative result — no substrate-gate assertion warranted.

## 9. Learning extracted

- First structurally decisive test in a 5-generation lineage is a clean negative for magnitude-only harm-aware selection.
- The built substrate is a partial, not full, translation of its own grounding literature review — escapability and threat-predictability were explicitly deferred, not omitted through oversight.
- Engagement anti-correlating (not merely failing to correlate) with outcome is a real, if modest, signal worth carrying forward.

## 10. Routing — CONFIRMED

**`/implement-substrate`, amend** (user confirmed the recommended option at the Step 8 gate, 2026-08-13). Amend `SD-hazard-aware-policy-decomposition` to add the escapability and/or threat-predictability input channel the lit-pull already specified. **Do not re-queue the magnitude-only design under a new letter.**

Draft `evidence_quality_note`: see JSON companion `failure_autopsy_V3-EXQ-919_2026-08-13.json`.

## 11. Governance apply checklist

- [ ] Append `evidence_quality_note` to MECH-321 in `claims.yaml`; set `epistemic_category: standard`
- [ ] Amend `substrate_queue.json` SD entry `SD-hazard-aware-policy-decomposition` per `recommended_substrate_queue_entry`
- [ ] Ledger already updated this session (Step 9b) — confirm `mech321_harm_aware_selection_task_effect` shows `H-harm-aware-reduces-task-harm: eliminated` with V3-EXQ-919 in `resolving_runs`
