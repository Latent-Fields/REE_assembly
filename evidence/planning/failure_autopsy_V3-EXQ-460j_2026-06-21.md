# Failure Autopsy -- V3-EXQ-460j (natural-commit-occupancy-release de-commit falsifier)

- **Generated:** 2026-06-21T12:45:21Z
- **Status:** `confirmed` (user-adjudicated, interactive /governance walk 2026-06-21T12:15Z)
- **Run:** `v3_exq_460j_natural_commit_occupancy_release_decommit_falsifier_20260621T115511Z_v3` (supersedes V3-EXQ-460i)
- **Claims:** MECH-445 (closure→beta coupling engagement) + MECH-446 (de-commit-authority magnitude) — both candidate / standard / v3_pending / pending_retest
- **Outcome:** FAIL, `non_contributory`, `substrate_not_ready_requeue`, `route_reason: off_baseline_not_sustained`

## Verdict

Clean substrate-readiness self-route — **not a weakens.** The 460j gate-3 sustained-hold redesign + the 2026-06-21 natural-commit **LATCH-HOLD amend** were both armed, and the redesign correctly detected that the **OFF (lever-disabled) baseline does not sustain** a natural-commit beta-latch occupancy (`sustained_hold` 0/3). Because there is no sustained occupancy, the rung-6 RELEASE lever has nothing to shorten (`lever_shortened_occupancy` 0/3) and the de-commit DV never runs (`coupling_nonvacuity` 0/3, `co_occurrence` 0/3).

## Readiness gates

| gate | result |
|---|---|
| contact_non_vacuity | 3/3 ✓ |
| rule_bias_trained | 2/3 ✓ |
| closure_trigger_available | 3/3 ✓ |
| **sustained_hold** | **0/3 ✗** ← the blocker |
| lever_shortened_occupancy | 0/3 ✗ (consequent) |
| coupling_nonvacuity | 0/3 ✗ (consequent) |
| co_occurrence | 0/3 ✗ (consequent) |

## Root cause

The latch-hold amend re-asserts the beta latch each tick to make the OFF baseline sustain — **but it yields to the SD-034 closure de-commit by design.** On the closure-active foraging substrate the closure control plane de-commits ~every tick (the 460i fragmentation, ~35 re-commits/episode), so the hold yields immediately and never establishes a sustained occupancy. The latch-hold is *necessary-but-insufficient*: the binding constraint is the **latch-hold ↔ closure-de-commit interaction**, not the absence of a hold lever.

The gate-3 redesign is itself a measurement-instrument *improvement* — it caught what 460i's `mean_beta_elevated` proxy missed.

## Four-layer (abridged)

- **Claim alignment:** intact — MECH-445/446 never tested (DV didn't run). Correctly non_contributory.
- **Prerequisites:** missing — a sustained natural-commit occupancy on the OFF baseline.
- **Implementation:** the latch-hold is built/armed; the gap is its yield-to-closure clause vs the churny closure plane.
- **Biological reference:** BG committed-motor-program maintenance + graded urgency release (Thura & Cisek 2022; Jin 2014); mechanism not implicated.

## Routing → implement-substrate (yield-clause fix)

Amend the `f_dominance_conversion_ceiling` rung-6 substrate entry with the 460j failure record. Next substrate step: **narrow the latch-hold yield clause** so it yields only to a *genuine* closure fire (not the per-tick re-toggle), OR test the rung-6 release on a regime where the closure de-commit is quieter so a sustained natural-commit occupancy can form. MECH-445/446 stay candidate/v3_pending/pending_retest — no status change.

## Granularity-debt flag (8th iteration)

460d→460j; **three consecutive autopsies (460h/i/j)** on the same lever with an **evolving** failure shape (disjoint-certifier → off-baseline-fragmentation → latch-hold-yields-to-closure). Surfacing for a **design-rethink at the human gate**: is the rung-6 natural-commit-occupancy-release lever fundamentally testable on a closure-de-commit-active substrate, or does MECH-445/446 need a substrate where natural commit and closure de-commit are dissociable? Not auto-routed — this autopsy's own routing is the yield-clause substrate fix.
