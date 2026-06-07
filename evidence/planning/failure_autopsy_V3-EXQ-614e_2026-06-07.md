# Failure Autopsy -- V3-EXQ-614e (MECH-341 within-class temperature, authority ON)

- **Generated (UTC):** 2026-06-07T07:55:01Z
- **Scope:** single
- **Status:** confirmed (user-adjudicated 2026-06-07)
- **Run ID:** `v3_exq_614e_mech341_within_class_temperature_authority_on_20260607T070701Z_v3`
- **Queue ID:** V3-EXQ-614e (supersedes V3-EXQ-614d)
- **Claims:** MECH-341 (`e3_scoring_preserves_trajectory_class_diversity`)
- **Routed from:** /governance 2026-06-07 (script self-emitted `weakens`; governance DEFERRED weakens -> non_contributory pending this autopsy)
- **Verdict:** non_contributory; `epistemic_category=substrate_ceiling`; `pending_retest_after_substrate=true` (gated on ARC-065/GAP-A). **MECH-341 not weakened.**

## 1. Facts (no interpretation)

| Criterion | Result | Detail |
|---|---|---|
| C1 substrate-operative (non-vacuity) | **True** | within-class branch fires + Site-2 across-class authority normalization fires (majority seeds); ARM_0_LEGACY committed_class_entropy mean = 1.035689 (non-degenerate, > 0.1 floor) |
| C2 (PRIMARY) within-class committed-class lift | **False** | per-arm paired-lift seed counts 0/0/0; committed_class_entropy **byte-identical 1.033608** at T=0.5, 1.0, 2.0 |
| C3 substrate-readiness | **True** | all 4 arms frac_pre_ge2 majority pass |

Config: `use_modulatory_selection_authority=True`, `modulatory_authority_gain=0.5`; 4 arms (legacy + T 0.5/1.0/2.0) x 3 seeds (42/43/44) x (P0 30ep + P1 60ep) x 200 steps. SD-056 amend ON; the ONLY swept axis is `stratified_within_class_temperature`. Self-route label: `FAIL_C1_holds_C2_fails_lever_operative_but_no_committed_class_lift`.

**Expected vs observed.** Expected: cranking within-class temperature 0.5 -> 2.0 raises committed_class_entropy (the scoring-layer diversity lever reaches committed-action selection). Observed: committed_class_entropy is byte-identical across the 4x temperature range AND shifted off legacy (1.035689 -> 1.033608). Failed criterion = **discrimination** (C2).

## 2. The load-bearing observation

The positive-temperature arms are byte-identical *to each other* (1.033608) but *different from legacy* (1.035689). Two facts follow:

1. **The lever reaches committed selection** -- turning on within-class temperature sampling moved committed entropy off the legacy argmin value. The 643a authority fix is operative; this is NOT a 614d-style zeroed-lever artifact.
2. **The committed-CLASS distribution is insensitive to which within-class representative wins** -- a 4x change in T produces zero change in committed_class_entropy. The across-class competition is decided by class-level structure that the representative shift never perturbs.

## 3. Claim-layer mapping

MECH-341 = "E3 scoring **preserves trajectory-class diversity**." Committed-class diversity is the **across-class** axis. Within-class temperature is a **within-class** sub-axis (which representative of a committed class executes). 614e tested the within-class lever against an across-class readout, under a candidate pool that is monostrategic at the class level. A committed-class lift is therefore **structurally impossible** here -- the experiment did not let MECH-341's preservation principle express itself. The FAIL falsifies neither the within-class sub-axis (wrong readout) nor the across-class principle (no diversity present to preserve).

## 4. Biological-reference triage

- Closest mechanism: basal-ganglia action selection over a diverse cortico-striatal candidate set; diversity preserved at the scoring/selection step.
- Not a formal-definition import -- the principle is biologically grounded. The gap is a **missing upstream substrate** (candidate-pool class diversity), which is exactly what would happen biologically if the proposal stage fed the selector a degenerate, single-class option set.
- Does the failure match a missing-dependency signature? **Yes** -- it is the discovered-prerequisite case (GAP-A candidate-pool collapse), not a falsification.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | claim could not express itself; wrong-axis readout + monostrategic pool |
| Biological reference | partial | mechanism class has existence proof; translation sound |
| Dependency prerequisites | **missing** | ARC-065 candidate-pool class diversity (GAP-A) not delivered; cand_world_pairwise_dist=0.0000 |
| Implementation completeness | complete | within-class branch + Site-2 authority both fire; 643a operative |
| Environment adequacy | adequate (for lever) | candidate-generation pathway upstream does not produce class diversity |
| Measurement adequacy | **under-instrumented** | committed_class_entropy (across-class) is byte-identical to T; matched metric is within-class-representative diversity |
| Integration adequacy | coupled but inert | lever + authority fire; committed-class outcome decided upstream |
| Scale / capacity | unknown | not dominant |

**Dominant diagnosis -> `epistemic_category=substrate_ceiling`** (upstream candidate-pool class collapse; GAP-A).

## 6. Lineage context (GAP-B)

4th convergent committed-action no-lift instance on `behavioral_diversity_isolation:GAP-B`: 604a (curiosity), 624a (vigor), 614d (within-class temp), **614e (within-class temp, authority ON)**. The first three predated an operative authority gate. 614e is the first AFTER the authority substrate was proven operative (643a PASS) -- so it cleanly relocates the bottleneck from the authority gate (GAP-B, resolved) to the **candidate pool (GAP-A, blocked_pending_substrate)**.

## 7. Learning extracted

- The authority gate (GAP-B) is no longer the limiter for committed-class diversity; GAP-A candidate-pool class collapse is.
- Committed-class entropy is the wrong matched readout for a within-class lever; need a within-class-representative-diversity metric.
- byte-identical-across-temperature is the substrate-ceiling fingerprint for the whole 614 lineage.
- MECH-341's within-class vs across-class sub-axes should be scored separately so an across-class ceiling cannot masquerade as a within-class-lever falsification.

## 8. Repair pathway (routing = implement-substrate, action = amend ARC-065/GAP-A)

Governance should append a `failure_record_entry` for 614e to the ARC-065 / GAP-A substrate work (E2-world-forward per-candidate signal preservation beyond GatedPolicy). The MECH-341 committed-class diversity re-test is `pending_retest_after_substrate` until class-level candidate diversity exists. **MECH-341 stays candidate / v3_pending=true; no confidence move; not weakened.**

### Draft evidence_quality_note (governance to write -- do not write here)

See `recommended_evidence_quality_note` in the JSON sibling.

## 9. Routing decision (user-confirmed)

`substrate_ceiling (GAP-A)` -- non_contributory + substrate_ceiling + pending_retest_after_substrate; amend ARC-065/GAP-A; MECH-341 not weakened. Confirmed via AskUserQuestion 2026-06-07.
