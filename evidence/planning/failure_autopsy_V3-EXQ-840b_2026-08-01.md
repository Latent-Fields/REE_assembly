# Failure Autopsy: V3-EXQ-840b (MECH-294 theta-packet binding, committed-action falsifier)

**Generated:** 2026-08-01T12:54:47Z
**Run:** `v3_exq_840b_mech294_theta_packet_binding_committed_action_falsifier_20260801T120516Z_v3`
**Queue ID:** V3-EXQ-840b
**Claim IDs:** MECH-294
**Status:** confirmed
**Supersedes:** V3-EXQ-840

## 1. Facts

**Design.** Joint vs alternation vs shuffled theta-burst binding, per-candidate co-binding coherence routed via `modulatory_channel_route_source='coherence'` through the modulatory-bias-selection-authority (landed 2026-06-10), read out on the E3 committed-action distribution. Fixes V3-EXQ-840's measurement-window starvation bug (seeds 45/49 self-contaminated their harm-free env design; fixed here by zeroing `contaminated_harm`).

**Outcome:** FAIL. `non_degenerate: true`. Label: `joint_indistinguishable_from_alternation`.

**Readiness — all 12 preconditions across 4 arms, ALL GREEN:**
- ARM_0_OFF, ARM_1_JOINT, ARM_2_ALT, ARM_3_SHUF: `routed_range_bounded` ✅ all
- ARM_1_JOINT: `joint_route_range_supra_floor` (0.063 vs 0.01) ✅, `adequate_fresh_selection_sample` (400 vs 180) ✅, `candidate_first_action_diversity_supra_floor` (2.00 vs 1.0) ✅, `adequate_committed_window_sample` (3600 vs 200) ✅
- ARM_2_ALT, ARM_3_SHUF: same diversity/window checks, all ✅

10 seeds run (42–51), well above the 7-seed minimum.

**Criteria:**
- C1 (JOINT ≠ ALTERNATION): mean TV **0.087** vs 0.1 floor, only **3/10** seeds above floor (7 required) — **FAIL**
- C2 (JOINT ≠ SHUFFLED): mean TV 0.193, 7/10 seeds above floor but `exceeds_baseline: false` — **FAIL** (moot given C1 already fails; label routes on C1 first per the driver's outcome map)

## 2. Claim-layer mapping

MECH-294 (candidate) is currently pinned `epistemic_category: substrate_ceiling`, `pending_retest_after_substrate: true` — from the 569f/661/654a E3-commit-readout substrate_ceiling cluster (shared with ARC-065/062/309). **This run is that pending retest.** V3-EXQ-840 (the first behavioural-evidence attempt) FAILed on a measurement-window bug (`measurement_test_design_defect`, not counted toward the ceiling cluster). This run fixes that bug and comes back fully clean.

## 3. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **weakened** | clean, well-powered test of the joint-binding claim's own criterion |
| Biological reference | Kay-2020 cited directly | parsimonious alternation account matches this null |
| Prerequisites | present | this IS the pending substrate retest |
| Implementation | complete | predecessor's measurement-window bug fixed cleanly |
| Environment | adequate | fishtank env exercises all three binding conditions as designed |
| Measurement | **all 12 preconditions green**, 10 seeds | as clean a non-degenerate FAIL as this corpus produces |
| Integration | coupled, correctly measured | routed coherence genuinely differentiates JOINT from OFF/SHUF/ALT |
| Scale | adequate | well above every stated floor |

## 4. Why this reads as genuine claim pressure, not a wiring gap

The driver's own `evidence_direction_note` explicitly frames the decision this autopsy needs to make: *"joint_indistinguishable_from_alternation -> weakens (C1 fail -- Kay-2020 parsimonious outcome; route /failure-autopsy to disambiguate residual wiring vs genuine over-specification; hold stands)."* With all 12 readiness preconditions green and 10 seeds run, there is no residual-wiring-gap candidate left to point to — the substrate is confirmed ready, the manipulation is confirmed to differentiate the arms (route range: JOINT 0.069, ALT 0.057, OFF/SHUF 0.0), and the committed-action readout still can't distinguish JOINT from ALTERNATION at the pre-registered threshold. This is the "genuine over-specification" branch: MECH-294's joint-binding claim, as currently worded, is not supported at the behavioral-committed-action level this substrate can measure — consistent with, though not a full test of, Kay (2020)'s more parsimonious cross-cycle/alternation account.

## 5. Learning extracted

1. This run resolves the `pending_retest_after_substrate` flag MECH-294's `substrate_ceiling` category was explicitly waiting on — it came back clean, so the category should graduate.
2. A clean, well-powered, all-green-readiness C1-fail with the driver's own pre-registered outcome map already naming the biological reading is about as unambiguous a `weakens` as this corpus produces.
3. The predecessor's measurement-window bug (V3-EXQ-840) was correctly diagnosed and fixed rather than conflated with a substrate ceiling — a useful contrast case for what "substrate not actually ready" looks like vs. this run's "substrate ready, claim doesn't hold."

## 6. Routing (user-confirmed)

**Evidence direction: `weakens`** (confirmed, matches the manifest's own clean reading).

**Recommend flipping `epistemic_category`: `substrate_ceiling` → `standard`** — user confirmed 2026-08-01. The retest this category was pending on has happened and came back fully clean; continuing to exclude this evidence as ceiling-pending would misrepresent the current state.

**No demotion** — per the driver's own note, "hold stands." One clean weakens against a candidate architectural claim with existing lit grounding is informative but not sufficient on its own for demotion. `pending_retest_after_substrate` → `false`.

**No further experiment/lit-pull/build needed from this autopsy** — routes directly to `/governance` for the category flip and evidence_quality_note application.

Re-derive brake: 0 prior `substrate_ceiling` autopsies scored against MECH-294 under this specific reading — n/a (this run is what resolves the pending ceiling, not another ceiling hit). Granularity-debt check: alignment distribution across the MECH-294 cluster (661 intact, 840 unclear, 840b **weakened**) — first `weakened` reading in the cluster; does not fire the recurrence trigger (needs a second weakened reading with a different failure signature).
