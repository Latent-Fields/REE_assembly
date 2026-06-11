# Failure Autopsy -- V3-EXQ-666a (ARC-063 CRF availability-maintenance substrate-readiness diagnostic)

- **Generated (UTC):** 2026-06-11T20:40:12Z
- **Scope:** single
- **Status:** confirmed (user-adjudicated at Step 8)
- **Run:** `v3_exq_666a_arc063_crf_availability_maintenance_readiness_20260611T154034Z_v3` (machine ree-cloud-4)
- **Outcome:** FAIL / `evidence_direction: non_contributory` / `experiment_purpose: diagnostic` / `claim_ids: []` / supersedes `v3_exq_666_arc063_crf_mature_pool_readiness`
- **Self-route flag:** `criteria_non_degenerate.maintained_pool_gate_discriminates_vs_arm1_no_maintenance = false` -> the readiness PASS is unattributable to the maintenance mechanism (discrimination FAIL)
- **Validates:** the 2026-06-11 `crf-availability-maintenance` amend (activity-silent maintenance trace + maintained-pool readout) routed by `failure_autopsy_V3-EXQ-666_2026-06-11` + the `targeted_review_arc_063_crf_rule_cell_persistence` B-leaning lit verdict

This skill is analysis + hand-off only. It does NOT edit claims.yaml, manifests, review_tracker, substrate_queue, or evidence_direction. Governance applies the recommendations interactively.

---

## 1. Scope

Single-target autopsy of a claim-free substrate-readiness diagnostic, flagged by the indexer's `criteria_non_degenerate` block (a `vacuous_pass`-style flag: the load-bearing PASS cleared but the discrimination control did not separate). 666a tests whether the activity-silent maintenance mechanism (built 2026-06-11) holds a differentiated, reactivatable >=2-rule pool at behavioural runtime. It does NOT validate or weaken MECH-309 / ARC-062 / ARC-063 (all stay candidate / substrate_ceiling / v3_pending / pending_retest_after_substrate). It gates the 654c GAP-B behavioural re-run (MECH-309 / ARC-062 committed-class entropy falsifier), which stays blocked until a CRF-readiness PASS lands.

---

## 2. Facts (reconstruction, no interpretation)

Three arms x 3 seeds (42/43/44), all on the matched 654b/666 stack (CRF + lateral-PFC head + e2 SD-056 online). The swept variables are three flags. The readiness gate is RE-STATED on the maintained pool per the lit verdict:

> `gate_cleared = crf_maintained_pairwise_dist > 0.1 AND crf_n_maintained_reactivatable >= 2`

(the retired 666 gate was `crf_max_pairwise_rule_dist > 0.1 AND crf_frac_active >= 0.30`).

| Arm | `frac_active` | `n_maintained` (42/43/44) | **`frac_maintained`** (42/43/44) | `maint_dist` | gate cleared |
|---|---|---|---|---|---|
| ARM_0_OFF (legacy, no mature/e2ctx/maint) | ~0.125 | 0 / 0 / 0 | **0.0 / 0.0 / 0.0** | 0.0 | 0/3 -- 654b churn reproduced |
| ARM_1_MATURE_E2CTX (no maintenance) | ~0.016 | 3 / 2 / 7 | **0.188 / 0.125 / 0.438** | ~1.4 | **3/3 -- cleared** |
| ARM_2_MATURE_E2CTX_MAINTENANCE (the fix) | ~0.028 | 16 / 10 / 15 | **1.0 / 0.625 / 0.938** | ~1.71 | 3/3 -- cleared |

- `non_vacuity_met = true` (every cell minted >=2; `min_n_minted_all_cells = 10`).
- `differentiation_met_e2ctx_arms = true` (`min_max_pairwise_dist 1.70 > floor`).
- `readiness_met_arm2_maintenance = true`.
- `discrimination_met_arm1_no_maintenance_does_not_hold = FALSE` <- the FAIL.
- Manifest criteria: `ARM_2_MAINTENANCE_clears_maintained_pool_gate` (load_bearing) PASSED; `ARM_1_NO_MAINTENANCE_does_not_hold_maintained_pool` (non-load-bearing) FAILED.

**Which criterion failed:** the discrimination control. ARM_1 (no maintenance) also clears the `n_maintained >= 2` count floor, so the experiment cannot attribute the readiness PASS to the maintenance mechanism.

---

## 3. The load-bearing finding: the mechanism works; the GATE used the wrong statistic

Two positive results and one test-design defect:

1. **The lit-prescribed readout redefinition is validated.** `crf_frac_active` is ~0.016-0.031 in BOTH e2ctx arms -- it would fail the retired 0.30 gate -- yet the differentiated pool is plainly maintained. This is exactly the Lundqvist/Stokes prediction the lit-pull adopted ("averaged activity hides sparse-but-maintained coding"; an instantaneous active-fraction misreads a maintained-but-silent rule as absent). The maintained-pool readout is the correct persistence instrument.

2. **The maintenance mechanism works and strictly dominates.** Read on `crf_frac_maintained` (maintained/minted, already in the manifest), the separation is clean and monotone across all 3 seeds: ARM_0 = 0.0, ARM_1 = 0.125-0.438, ARM_2 = 0.625-1.0. Activity-silent maintenance holds 62.5-100% of the differentiated pool where differentiation-alone holds only 12.5-43.75%.

3. **The pre-registered gate used the wrong statistic.** It gated on the COUNT floor `crf_n_maintained_reactivatable >= 2`. At behavioural-runtime context-absent gap density (100 ep x 40 steps -- shorter/denser than the implement-substrate unit smoke's 3000 idle ticks, where ARM_1-equivalent fully eroded to 0), differentiation + retirement keeps 2-7 rules reactivatable in ARM_1, so it clears the n>=2 floor. The FRACTION statistic that ISOLATES the maintenance contribution was computed but not used as the gate.

**Conclusion:** this is a measurement / test-design defect (the readiness gate's count-floor is gap-density-sensitive and does not isolate maintenance), NOT a substrate failure and NOT a claim falsification. The substrate maintenance mechanism is confirmed functional; the diagnostic just gated on the wrong (count) statistic instead of the right (fraction) one.

---

## 4. Biological-reference triage

- **Closest mechanism:** PFC rule/task-set cell maintenance across input-absent epochs. The CRF is a faithful biological-mechanism translation, NOT a formal-definition import.
- **Existence proof for the class:** brains maintain multiple concurrently-differentiated task rules; default reading of any shortfall is a calibration/measurement gap, not a falsification.
- **Divergence:** none load-bearing. The activity-silent maintenance FORM was adopted from the B-leaning lit verdict (`targeted_review_arc_063_crf_rule_cell_persistence`: Mongillo 2008 synaptic facilitation, Stokes 2015 activity-silent, Lundqvist 2018). 666a confirms the verdict: `crf_frac_active` is the wrong (averaged, instantaneous) readout; maintained-and-reactivatable is right. The directive set was deliberately robust to the live Constantinidis 2018 persistent-firing rebuttal, and the operative conclusion (instantaneous active-fraction is the wrong readout) survives either way.
- **Lit status:** present (`targeted_review_arc_063_crf_rule_cell_persistence`, DONE 2026-06-11).

---

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | n/a (claim-free) | MECH-309 / ARC-062 / ARC-063 stay candidate / substrate_ceiling / v3_pending / pending_retest_after_substrate. Unchanged by this non_contributory run. |
| Biological reference | clear | PFC rule-cell activity-silent maintenance; faithful translation; readout redefinition validated. Default reading = calibration/measurement gap. |
| Developmental / dependency prerequisites | strengthened | e2_world_forward context confirmed necessary for differentiation (carried from 666). |
| Implementation completeness | substantially advanced | Maintenance mechanism works (frac_maintained 0.625-1.0 vs 0.125-0.438) + readout redefinition validated. |
| Environment adequacy | adequate | ARM_0 reproduces churn; non-vacuity met. |
| Measurement adequacy | under-instrumented GATE (the defect) | Gate stated on count-floor (n>=2, gap-density-sensitive) which differentiation-alone clears; the isolating statistic crf_frac_maintained was collected but not gated on. |
| Integration adequacy | coupled | Maintenance trace integrates with the e2ctx source and retire/decay path; maintained-pool readout reads cleanly. |
| Scale / capacity | adequate | Minting and maintenance both clearly happen; budget not the limiter; gap density (not budget) is why the count-floor failed to discriminate. |

**Recommended `epistemic_category`:** `measurement_test_design_defect` (same family as V3-EXQ-514m / 660a / 642). Diagnostic stays `non_contributory`; weights nothing in governance.

---

## 6. Learning extracted

1. **The lit-prescribed readout redefinition is validated** -- `crf_frac_active` (instantaneous active fraction) is the wrong persistence readout for a sparsely-matched differentiated pool; maintained-and-reactivatable is right.
2. **The activity-silent maintenance mechanism works and strictly dominates** -- holds 62.5-100% of the differentiated pool vs 12.5-43.75% for differentiation-alone, clean monotone separation 3/3 seeds.
3. **The 666a readiness gate used the wrong statistic** -- a count floor (n_maintained>=2) is gap-density-sensitive and differentiation-alone clears it at behavioural-runtime gaps; the fraction statistic (crf_frac_maintained, already collected) isolates maintenance and should be the pre-registered gate.
4. **Recurrence is convergent iteration, not granularity debt** -- 3rd autopsy on the ARC-063 CRF-readiness target (654b -> 666 -> 666a), but each step advanced (no-differentiation -> differentiation-works/persistence-collapses -> maintenance-works/gate-mis-stated). The substrate_ceiling claims were never weakened. NO /claim-synthesis routing (user-confirmed at Step 8).

---

## 7. Repair pathway (user-confirmed at Step 8)

**Primary route: `/queue-experiment` V3-EXQ-666b.** Re-state the readiness gate on `crf_frac_maintained` (the isolating statistic, already collected by 666a: ARM_1 < ~0.5 fails, ARM_2 >= 0.625 clears) and/or run a longer context-absent gap regime so differentiation-alone erodes below the floor. Keep the same-statistic non-vacuity discipline (the gate statistic asserted as a readiness precondition) and ARM_2 maintenance-ON as the adopted differentiation+maintenance default. This is the disciplined path consistent with how the project handles wrong-statistic gates (514m -> 514n, 660a -> 660b: never silently re-read a pre-registered gate on a different post-hoc statistic).

**Substrate hand-off: `/governance` AMENDs the existing `crf-availability-maintenance` entry** (action=amend, do NOT create a new entry) with the 666a failure record: the maintenance mechanism is confirmed functional on the fraction readout, but `ready` stays `false` because the count-floor gate did not isolate it. On the 666b PASS, governance adopts maintenance-ON as the mature-regime default, flips `ready=true`, and unblocks the 654c GAP-B behavioural re-run.

**Not recommended:** demotion (claim-free; biology supports the class), requeue of 666a as-is (it self-routes the same discrimination FAIL), `/claim-synthesis` (convergent substrate iteration, not claim-granularity debt -- user-confirmed). The 654c GAP-B behavioural re-run STAYS gated/blocked until a discriminating CRF-readiness PASS lands.

**Draft `evidence_quality_note` for governance to write** (against the substrate entry's failure record; the claims stay untouched):

> V3-EXQ-666a (claim-free CRF availability-maintenance readiness diagnostic, non_contributory) self-routed FAIL on its discrimination criterion (ARM_1 no-maintenance also cleared the maintained-pool gate), but the FAIL is a measurement/test-design defect, not a substrate failure. The gate was pre-registered on the COUNT floor crf_n_maintained_reactivatable>=2, which differentiation-alone clears at behavioural-runtime gap density (ARM_1 holds 2/3/7 reactivatable rules). Read on the isolating statistic crf_frac_maintained (in-manifest), the maintenance mechanism works and strictly dominates with clean monotone separation 3/3 seeds: ARM_0 0.0, ARM_1 0.125/0.188/0.438, ARM_2 1.0/0.625/0.938. The lit-prescribed readout redefinition is VALIDATED (crf_frac_active ~0.016-0.031 in both e2ctx arms -- the averaged-activity artefact -- while the differentiated pool is plainly maintained). Substrate maintenance mechanism confirmed functional; the readiness gate just used the wrong (count, gap-density-sensitive) statistic. Routed: /queue-experiment V3-EXQ-666b re-stating the gate on crf_frac_maintained and/or a longer-gap regime. crf-availability-maintenance substrate entry stays ready=false pending the 666b PASS; 654c GAP-B stays gated. MECH-309/ARC-062/ARC-063 unchanged.

---

## 8. Hand-off summary

- **Failed criterion:** discrimination (ARM_1 no-maintenance also cleared the maintained-pool count gate = the discrimination control did not separate).
- **Dominant diagnosis layer:** measurement / test-design defect (count-floor gate is gap-density-sensitive and does not isolate maintenance) + substantially-advanced implementation (maintenance mechanism + readout redefinition both validated).
- **Biological-reference verdict:** clear existence proof; mechanism translation, not formal import; calibration/measurement gap, not falsification.
- **Routing:** /queue-experiment V3-EXQ-666b (re-gate on crf_frac_maintained / longer-gap) -> /governance amend crf-availability-maintenance substrate entry (ready stays false). No demotion, no requeue-as-is, no /claim-synthesis.
- **Gated downstream:** 654c GAP-B behavioural re-run (MECH-309 / ARC-062) stays blocked until a discriminating CRF-readiness PASS.
