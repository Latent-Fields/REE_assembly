# Failure Autopsy (cluster) -- V3-EXQ-695 + V3-EXQ-696 (F-dominance conversion ceiling)

- **Generated:** 2026-06-21T12:45:21Z
- **Status:** `confirmed` (user-adjudicated in the interactive /governance walk, 2026-06-21T12:15Z)
- **Scope:** cluster (2 members, one structural property)
- **Members:**
  - V3-EXQ-695 `arc062_mech309_modulatory_bias_monomodal_retest` -- MECH-309, ARC-062 (supersedes 654g); `non_contributory`, `non_degenerate:true`
  - V3-EXQ-696 `sd033b_mech263_ofc_outcome_prediction_ceiling_retest` -- SD-033b, MECH-263; self-stamped **`weakens`** (OVERTURNED), `non_degenerate:true`

## Verdict

Both are the **F-dominance conversion ceiling** (V3-EXQ-571: the primary harm/goal score **F monopolises ~88-89% of committed-selection variance**). A secondary channel -- rule-apprehension / modulatory-bias (695) or OFC outcome-value devaluation (696) -- reaches the E3 score accumulator but **cannot move the F-dominated committed argmin**. This is one structural property tested by two structurally-different claims, **not** two independent falsifications.

- **695** self-routed correctly (`non_contributory`); keep.
- **696** self-stamped `weakens` -- **OVERTURN to `non_contributory`.** Its shape is C3 (controls) clean / C1+C2 (discrimination) fail = the substrate-ceiling fingerprint, identical to V3-EXQ-485h. A `weakens` would inflate SD-033b's conflict ratio against a substrate limitation (illusory-conflict-resolution rule).

## Cluster pattern

| Run | Claim | Negative control / silent arm | Discrimination criteria | Read |
|---|---|---|---|---|
| 695 | MECH-309 / ARC-062 | matched-noise / proposer (clean) | committed-action diversity does not strict-beat controls | conversion ceiling |
| 696 | SD-033b / MECH-263 | C3 OFF/control silent (3/3 PASS) | C1 devaluation 1/3, C2 discrimination 0/3 (FAIL) | conversion ceiling (mis-stamped weakens) |

**Structural property:** the E3 selector treats F as the *decider* rather than as *eligibility*; every secondary channel is subdominant and drowns at commit. The fix is **constitutional, not per-claim**.

## Response (already built / queued -- no new diagnosis)

- **MECH-448** rank-preserving F→eligibility demotion (the ARC-107 selector-constitution lead lever) landed 2026-06-20; V3-EXQ-689d PASS promoted it candidate→provisional.
- **V3-EXQ-654h** (MECH-448 demotion-enabled GAP-B retest) owns the 695 retest -- queued.
- **V3-EXQ-485i** (MECH-448 demotion-enabled trained-OFC-head behavioural falsifier) owns the 696 retest -- queued.

## Biological-reference triage

Closest mechanism: basal-ganglia hyperdirect conflict-grade selection / divisive normalisation of value (Frank 2006; Carandini & Heeger 2012). Not a formal-definition import. The rank-preserving F→eligibility demotion **exceeds** canonical order-preserving DN -- a load-bearing divergence tracked in the MECH-448/ARC-107 ledger. Mechanisms (rule-apprehension, OFC devaluation) are sound; the failure is the selector locus.

## Routing

`implement-substrate` (response built) → governance amends the `f_dominance_conversion_ceiling` substrate_queue entry with both failure records; the queued falsifiers (654h, 485i) carry the retests. No claim status changes. **696 reclassification clears the SD-033b `hold_candidate_resolve_conflict` pending_user agenda item.**

Evidence-quality notes to apply (verbatim) are in the companion JSON `recommended_evidence_quality_note` / `recommended_evidence_direction_note`.
