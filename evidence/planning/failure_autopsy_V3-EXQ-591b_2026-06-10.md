# Failure Autopsy -- V3-EXQ-591b (curriculum Phase 0->1 gate reachability)

**Date:** 2026-06-10T14:40:35Z
**Scope:** single
**Status:** confirmed (user-adjudicated 2026-06-10)
**Routing:** governance (record finding + mark reviewed); residual tracked upstream -- NO new gate work, NO new substrate_queue entry this cycle
**Run:** `v3_exq_591b_isef005_curriculum_phase_advance_readiness_20260610T090813Z_v3`
**Queue:** V3-EXQ-591b | `experiment_purpose: diagnostic` | `claim_ids: []`

---

## Summary

V3-EXQ-591b is a claim-free substrate-readiness diagnostic: does the
InfantCurriculumScheduler **Phase 0->1** advancement gate fire under the landed
`H_POS_FRAC_OF_MAX=0.20` recalibration (down from the structurally-unreachable 0.70,
recalibrated 2026-05-31)? It is GAP-14 **prereq (c)** reachability only (prereq (b),
the goal-pipeline non-trivial z_goal, is owned separately by goal_pipeline:GAP-4 /
behavioral_diversity_isolation:GAP-C; Phase 1->2 is deliberately not evaluated here).

**Result:** C1 (every seed reaches Phase 1) FAIL -- **4/5 seeds** advanced
(seeds 42/43/44/45 at episodes 104/114/100/142); **seed 46 stuck at Phase 0**.

The self-routed label `phase01_gate_unreliable_needs_strengthening` is **adjudicated**:
the user accepts it as a **real gate-calibration finding** (the gate is genuinely
brittle for the low-exploration seed tail -- not fully exonerated as "working as
designed"), but routes **no gate change this cycle**; the residual is tracked upstream.

---

## Facts (no interpretation)

Single-crossing telemetry gate (`infant_curriculum.py:_try_phase_0_to_1`): once
`episode >= PHASE_EP_MIN[1]`, advance Phase 0->1 the first episode whose per-episode
`h_pos` (Shannon positional entropy, nats) clears `H_POS_FRAC_OF_MAX * ln(grid_cells)`
= `0.20 * ln(144)` = **0.9940**.

| Seed | final_phase | adv. ep | h_pos mean | h_pos max | n_eps >= thr (of 60) |
|------|-------------|---------|-----------|-----------|----------------------|
| 42 | 1 | 104 | 0.562 | 1.838 | 7 |
| 43 | 1 | 114 | 0.323 | 1.312 | 6 |
| 44 | 1 | 100 | 0.842 | 2.485 | 36 |
| 45 | 1 | 142 | 0.140 | 1.453 | 2 |
| **46** | **0** | **null** | **0.0375** | **0.690** | **0** |

- Precondition `early_policy_produces_nontrivial_h_pos` MET (max h_pos 2.485 > floor 0.2)
  -- the C1 verdict is real, not a degenerate non-mover artifact.
- `criteria_non_degenerate.C1_all_reach_phase1 = true`; `C1` is `load_bearing` and FAILED.
- Seed 46 is a stark outlier: `h_pos_max = 0.690` over the FULL 160-episode budget --
  it **never** reached the 0.994 threshold on any single episode; mean 0.0375 = a
  near-stationary policy. Seed 45 barely cleared (2 of 60 eligible episodes; advanced
  late at ep 142).

Failed criterion: **discrimination** (C1, all-seeds reachability). Negative-control /
precondition (agent-moves) PASSED.

---

## Claim-layer map

`claim_ids: []` -- 591b tests **no claim**. It is a reachability probe for GAP-14
prereq (c), lineage ARC-046 / behavioral_diversity_isolation:GAP-C / infant_substrate.
**No claim is weakened or demoted by this FAIL.** `evidence_direction: does_not_support`
refers to the gate-reachability hypothesis ("all seeds reach Phase 1"), not to any claim.

---

## Biological-reference triage

The mechanism class is a **staged developmental-curriculum competency gate** (ARC-019):
a stage transition is licensed only once the prior-stage competency is acquired. This is
a faithful translation, **not** a formal-definition import -- in real development a stage
gate withholds advancement from an organism that has not acquired the prior competency.
Seed 46's policy collapsed to near-stationarity (it never acquired Phase-0 exploration),
so the gate **correctly withheld** its advancement. The failure does **not** resemble a
missing-dependency signature of the gate; it resembles a missing-dependency signature
**upstream of the gate** -- the exploration drive that should pull a collapsed policy out
of stationarity.

---

## Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | N/A | claim_ids=[]; tests no claim; nothing to weaken |
| Biological reference | clear | staged-curriculum competency gate (ARC-019); faithfully withholds a non-explorer; not a formal import |
| Prerequisites | present | scheduler + H_POS recalib (0.70->0.20) landed 2026-05-31 |
| Implementation | **partial (gate-calibration brittle)** | the single-crossing 0.994 gate advances 4/5 typical seeds but is brittle for the low-exploration seed tail (seed 46). Recorded as a REAL calibration finding per user adjudication -- NOT fully exonerated as "working as designed". The self-route "needs strengthening" is legitimate; the fix is deferred. |
| Environment | adequate | no env defect; precondition met |
| Measurement | adequate | h_pos is the right axis; per-seed reachability measured cleanly |
| Integration | N/A | single-module scheduler gate |
| Scale | adequate for 4/5 | seed 46 had the FULL 160-ep budget and never cleared -- not a budget shortfall; an exploration collapse |

**Recommended epistemic_category:** N/A (claim_ids=[]; no claim to categorise). The
finding is an implementation/calibration record on the InfantCurriculumScheduler gate
plus an upstream exploration-diversity pointer.

---

## Learning extracted

1. The 2026-05-31 H_POS recalibration (0.70->0.20) **substantially fixed** the Phase 0->1
   gate: it advances 4/5 seeds (vs the pre-recalib state where the 0.70 threshold was
   structurally unreachable for ALL seeds). Prereq-(c) reachability is **established for
   typical seeds**.
2. The residual 1/5 miss (seed 46) is a genuine **early monostrategy / exploration
   collapse** (h_pos mean 0.0375, max 0.690 -- near-stationary policy), the SAME failure
   mode the behavioral_diversity_isolation programme (ARC-065 SP-CEM main-path + the
   2026-06-10 modulatory-bias route-range amend) targets. It is an **upstream
   exploration-diversity gap**, surfaced by the gate -- not, primarily, a gate defect.
3. The gate ALSO has a real calibration brittleness for the low-exploration tail
   (user-adjudicated): a single-episode 0.994 crossing is sensitive to seed-level
   exploration variance (seed 45 cleared on only 2 of 60 episodes). A future strengthening
   (e.g. rolling-window or adaptive criterion, or a Phase-0 stage that actively shapes
   exploration rather than passively gating) is a legitimate enhancement -- **deferred**,
   not queued this cycle.
4. Adjudication value: the autopsy prevents the naive "loosen the gate" reading of the
   self-route. Loosening the single-crossing threshold to admit seed-46-class policies
   would advance an agent past a Phase-0 competency it never acquired.

---

## Repair pathway (user-confirmed)

- **No new gate work this cycle.** No `/implement-substrate` gate change, no new
  `substrate_queue.json` entry. The gate-calibration brittleness is recorded as a
  deferred finding.
- **Track the residual upstream.** Seed-46-class exploration collapse is covered by the
  in-flight behavioral_diversity_isolation / ARC-065 exploration-diversity programme
  (SP-CEM main-path default + the modulatory-bias-selection-authority route-range amend
  validated by V3-EXQ-662 the same day). When that stack matures, the Phase-0->1
  reachability probe can be re-run and the gate threshold re-evaluated together.
- **Prereq-(c) disposition:** reachability is **established for typical seeds (4/5)**;
  the residual is an upstream-diversity concern tracked by behavioral_diversity_isolation:GAP-C,
  not a blocker that needs a gate fix before GAP-14 work proceeds (GAP-14 full closure
  still independently waits on prereq (b), the goal-pipeline z_goal, per the manifest note).
- `claim_ids: []` -> **no claims.yaml action**; no `pending_retest_after_substrate` flag
  (no claim to flag). 591b marked reviewed with this autopsy as the adjudication.

---

## Hand-off

- `/governance` (or this autopsy-completion session): mark 591b reviewed citing this
  artifact; no claim edit, no substrate_queue entry. pending_review -> 0.
- The InfantCurriculumScheduler Phase-0->1 gate-strengthening enhancement remains an
  OPEN, DEFERRED option (rolling-window / adaptive criterion / active Phase-0 exploration
  shaping) for a future cycle if the upstream diversity stack does not resolve the
  seed-tail collapse on a re-run.
