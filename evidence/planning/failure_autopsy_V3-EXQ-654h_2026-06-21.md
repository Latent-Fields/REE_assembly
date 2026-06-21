# Failure Autopsy -- V3-EXQ-654h (MECH-309 / ARC-062, arc_062:GAP-B)

- **Generated (UTC):** 2026-06-21T18:27:19Z
- **Target run_id:** `v3_exq_654h_arc062_gapb_rule_apprehension_behavioural_falsifier_20260621T175704Z_v3`
- **Queue id:** V3-EXQ-654h (supersedes V3-EXQ-654g)
- **Claims:** MECH-309 (rule-state abstraction propagation), ARC-062 (rule-apprehension architectural slot, weak reading)
- **Outcome:** FAIL -> `non_contributory`, self-route `substrate_not_ready_requeue`
- **Scope:** single
- **Routing:** `queue-experiment` (re-queue as V3-EXQ-654i) + `amend` `f_dominance_conversion_ceiling` substrate entry
- **Status:** confirmed (interactive)

---

## 1. Facts (no interpretation)

The behavioural falsifier ran to completion. Its self-route decision tree evaluated six gates; **five passed, one failed**:

| Gate | Measured | Threshold | Met |
|---|---|---|---|
| committed_class_axis_exercisable_both_arms | 1.0 | 0.3 | yes |
| gapa_consumed_summary_divergence_both_arms | 0.022601 | 0.05* | yes |
| gapa_consumed_summary_bounded | 0.121628 | 1e6 | yes |
| arm_on_rule_field_differentiated_and_matured | 0.871716 | 0.3 | yes |
| propagation_non_vacuity_arm_on_bias_differs_from_arm_off | 0.0194828 | 0.001 | yes |
| **mech448_demotion_lever_live_and_excluding_both_arms** | **0.0** | **>0** | **no** |

*(the divergence gate is a >= floor on the per-candidate spread; 0.0226 cleared its own per-seed majority test.)*

Load-bearing criterion `C2_committed_class_entropy_lift` = **not passed**, but only because the precondition `C1e_mech448_demotion_live_and_excluding` failed first. The manifest self-routed `substrate_not_ready_requeue` (`non_contributory`), not a weakens. This is the gate working as designed.

**Failing mechanism:** `f_eligibility_excluded_count == 0`. With `merit[i] = max(F) - F[i]` and `elig[i] = merit[i] / (dn_sigma + sum(merit))`, the arc_062 rule-apprehension candidate bank's **spread / non-divergent** F pool gives no candidate a merit-share >= the absolute `f_eligibility_envelope_floor = 0.30`. The envelope admits nobody -> all-admit fallback -> ARM_ON == ARM_OFF -> the F->eligibility demotion is a **structural no-op**, and the rule channel never arbitrated a genuinely-F-demoted committed selection.

This is the **identical signature** to V3-EXQ-485i (same MECH-448 lever, OFC bank). 654h is its arc_062-bank twin.

## 2. Claim-layer mapping

- **MECH-309 / ARC-062 alignment: intact.** The rule-apprehension propagation path is healthy (rule-field matured 0.872; propagation non-vacuity 0.0195). The claims were never tested through a genuinely-demoting selector. **Not a weakens.**
- The experiment tagged the right claims (MECH-309, ARC-062); no inherited-tag drift.

## 3. Biological-reference triage

- **Closest mechanism:** basal-ganglia hyperdirect conflict-grade selection / divisive normalisation of value (Frank 2006; Carandini & Heeger 2012). `lit_status: present` (`targeted_review_connectome_mech_439`).
- **Formal import?** No -- MECH-448 is a biologically-motivated rank-preserving demotion (it *exceeds* canonical order-preserving DN by removing F from the commit argmin; load-bearing divergence tracked in the MECH-448/ARC-107 ledger). Not implicated here -- the lever did not engage at all.
- The failure resembles a known-dependency-absent signature: the envelope needs a **divergent (peaked)** competing field to discriminate; the arc_062 bank does not supply one. Discovered prerequisite, not a falsification.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | claims never reached a demoting selector; not a weakens |
| Biological reference | clear | BG hyperdirect / DN; envelope mis-engagement is tuning, not divergence |
| Prerequisites | missing | divergent-pool non-vacuity (689d precondition) not armed on the arc_062 bank |
| Implementation | complete but mis-calibrated | floor=0.30 tuned to 689d's peaked pool, not the arc_062 spread bank |
| Environment | wrong pressures for this lever | arc_062 rule-apprehension bank yields a spread F pool |
| Measurement | adequate | C1e non-degeneracy gate caught the no-op and self-routed correctly |
| Integration | -- | MECH-448 x arc_062 harness surfaced the same bank-dependence as 485i (OFC) |
| Scale | adequate | structural no-op, not under-training |

**Recommended `epistemic_category`:** `substrate_ceiling`. **Recommended `evidence_direction`:** `non_contributory`.

## 5. The re-queue gate -- CLEARED

> Gate: re-queue 654i only if `failure_autopsy_V3-EXQ-485j` does NOT conclude the BG demotion lever fails to generalise off the GAP-A foraging substrate.

`failure_autopsy_V3-EXQ-485j` (committed this session, HEAD `32c2518c1d`) concluded:

- **MECH-448 demotion GENERALISES off GAP-A** for the discrimination / committed-separation signature family -- first cross-substrate corroboration, via a clean 3-arm dissociation (ARM_2 between-context committed TV 1.0 on 2/3 seeds vs ARM_1 F-dominance control 0.0 on all seeds). `claim_alignment: strengthened on C2`.
- The one signature that did **not** convert (C1 OFC devaluation) was pinned to a **devalued-head / test-design gap** (the devalued-state head trains flat / anti-range rather than re-ranking; the C1 readiness precondition keyed the high-threat state, not the devalued state) -- explicitly **not** the lever, **not** the envelope, **not** MECH-448. Routed to a 485k re-design.

654's load-bearing DV (`committed_class_entropy_lift` -- does the rule field arbitrate committed-action diversity after F-demotion) is in the **same discrimination / diversity family** that 485j showed converts off GAP-A, **not** the devaluation/value family that failed. The gate's hold trigger (a clean "does not generalise off GAP-A") is therefore **not met**. Independent of the formal 485j autopsy, the per-criterion read agrees: 485j C2 PASS 2/3 (relevant family) vs C1 FAIL 0/3 (orthogonal value family).

**Safeguard built into 654i:** keep `C1e` (`excluded_count>0`) as a HARD pre-DV readiness gate AND score a *fired-but-non-converting* outcome as a genuine MECH-309/ARC-062 **weakens** -- so if 654i lands where 485j's C1 did, that becomes the real escalation-worthy evidence rather than another silent no-op requeue.

## 6. Learning extracted

1. 654h is the arc_062 twin of 485i's MECH-448 no-op: the absolute share floor engages the lever only on a PEAKED pool; a SPREAD bank -> all-admit fallback -> structural no-op. The 689d config is not portable to a new candidate-bank construction without re-establishing the divergent-pool non-vacuity precondition.
2. The C1e non-degeneracy gate did its job (caught the no-op, self-routed, no false weakens). The autopsy confirms it.
3. Gate cleared: 485j proved MECH-448 demotion generalises off GAP-A for 654's signature family; the non-converting devaluation signature is orthogonal and test-design-bound.
4. Recurrence audit: 7th autopsy in the MECH-309/ARC-062 series (654/b/c/d/f/g/h). **No `/claim-synthesis`** -- the shared selector locus is already decomposed by the ARC-107 BG-selector constitution (MECH-448 demotion; MECH-449 Go/No-Go). Logged for the audit trail only.

## 7. Repair pathway

- **`queue-experiment`** -> V3-EXQ-654i (new letter, supersedes 654h): port the 485j per-(arm,seed) envelope-floor calibration onto the arc_062 bank (measure the bank's max per-candidate merit-share, set `f_eligibility_envelope_floor` below it so the envelope keeps F-best top-k in [2,4] and excludes a non-empty tail; keep `f_eligibility_dn_sigma=0.0`; keep an ABSOLUTE share floor). Keep `use_f_eligibility_demotion=True` as a matched-stack constant on BOTH arms (f_demotion overrides 569i top_k); keep `use_candidate_rule_field` as the swept variable. `claim_ids=[MECH-309, ARC-062]`. Add `supersedes: V3-EXQ-654h`.
- **`amend`** `f_dominance_conversion_ceiling`: append the 654h failure_record + arc_062 calibration hint (for governance tracking; the calibration itself lives in the 654i harness).

### Draft `evidence_quality_note` (governance writes; do not write here)

> V3-EXQ-654h (MECH-309/ARC-062 arc_062:GAP-B rule-apprehension behavioural falsifier on the MECH-448 demotion-enabled E3 selector; supersedes V3-EXQ-654g) self-routed substrate_not_ready_requeue (non_contributory; NO governance weight). All readiness/non-vacuity gates PASSED except the MECH-448 non-degeneracy gate: f_eligibility_excluded_count==0 on the arc_062 bank -- the 689d-validated config (floor=0.30, dn_sigma=0.0) admitted every candidate (spread/non-divergent F -> all-admit fallback) -> demotion no-op (ARM_ON==ARM_OFF) -> the C2 committed-class-entropy-lift DV never ran through a demoted selector. Identical no-op-envelope signature to V3-EXQ-485i (same lever, different bank). NOT a MECH-309/ARC-062 weakens. Re-queued as V3-EXQ-654i with 485j-style per-(arm,seed) envelope-floor calibration. Gate cleared by failure_autopsy_V3-EXQ-485j (MECH-448 demotion generalises off GAP-A for the discrimination/committed-diversity family 654 tests). pending_retest_after_substrate.
