# Failure Autopsy -- V3-EXQ-651 (ARC-060 blocked-goal recovery)

- **Generated:** 2026-06-07T14:20:26Z
- **Scope:** single (ARC-060)
- **Status:** confirmed (user-adjudicated via AskUserQuestion, 2026-06-07)
- **Routed from:** governance cycle `governance-cycle-20260607T1346Z` (commit 80c8335256).
- **Sibling autopsy:** `failure_autopsy_gapA-cluster-604b-648a-649_2026-06-07` (independent cluster).

## TL;DR

The discrete ghost-goal bank genuinely engaged, but the **FIELD_ONLY negative control
never abandoned the goal** -- Phase-C goal-proximity stayed ~0.98 in BOTH arms. ARC-060
predicts the bank rescues a goal the field-alone agent *loses*; that loss never happened,
so the bank had nothing to rescue. This is a **degenerate negative control / test-design
ceiling**, NOT evidence against ARC-060. `non_contributory`; **do NOT weaken ARC-060**;
re-queue 651a with a non-degeneracy gate.

---

## Facts (no interpretation)

- Ran **2026-06-07T13:19Z** on ree-cloud-3. Arms: FIELD_ONLY (bank off) vs FIELD_PLUS_BANK (bank on), seeds 42/43/44.
- **C1 precondition (bank engaged) met 3/3**: ghost candidates admitted 130/146/... ; goal_active_frac=1.0; bank populated in the ON arm.
- **C2 off-arm clean 3/3.**
- **C3 recovery margin met 0/3.** Phase-C mean goal-proximity:
  - FIELD_ONLY: 0.981 / 0.991 / ... ; seed 42 early 0.990 -> late 0.972.
  - FIELD+BANK: 0.989 / 0.990 / ...
  - `goal_prox_delta_on_minus_off` = +0.0079 / -0.0008 / ... vs required margin 0.01.
- z_goal seeded modestly in Phase A: `goal_norm_after_phase_a` = 0.30.
- Design: Phase A forced-seed z_goal; Phase B remove resource + stop re-seeding (intended gradient collapse); Phase C measure `GoalState.goal_proximity` of current z_world to the persisted z_goal (high = persistence, low = abandonment).

---

## Claim-layer map

| Claim | Type | Status | v3_pending | Reading |
|---|---|---|---|---|
| ARC-060 | architecture_hypothesis | candidate | yes | **intact** -- not tested under conditions where it could express itself (negative control never abandoned) |

Sub-mechanism validations explicitly defer the recovery prediction to ARC-060:
SD-039 (V3-EXQ-494), MECH-292 (V3-EXQ-496), MECH-293 (V3-EXQ-497) all PASS. The bank
machinery is confirmed firing; only the architectural behavioural prediction is untested.

---

## Biological-reference triage

- **Closest mechanism:** deferred-goal maintenance -- a continuous wanting field (vmPFC/striatal value landscape) PLUS a discrete reinstatable ghost-goal trace (hippocampal episodic goal snapshot). Well-evidenced class of mechanism (working-memory maintenance + episodic reinstatement of an interrupted goal; cf. Zeigarnik / interrupted-task resumption).
- **Dependency the test failed to supply:** a goal whose **local gradient genuinely collapses** so the field alone loses it -- and a **behavioural readout** of abandonment vs recovery (re-approach), not a saturating latent-proximity scalar.
- **Not a biology divergence.** This is a test-design / environment ceiling, not a formal-import mismatch.
- Does the failure resemble a biological missing-dependency signature? No -- it resembles "the experiment never created the lesion condition," i.e. the negative control was healthy.

## Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | ARC-060 could not express itself; field-alone never abandoned |
| Biological reference | clear | deferred-goal maintenance; failure = lesion condition never induced |
| Prerequisites | present | SD-039/MECH-292/MECH-293 PASS; bank engaged (C1 3/3) |
| Implementation | complete | both arms behaved as configured |
| Environment | too sparse / wrong pressure | Phase-B invalidation did not force FIELD_ONLY drift; agent stays near old goal scene |
| Measurement | misleading | latent goal_proximity saturates ~0.98 both arms; doesn't read behavioural abandonment |
| Integration | coupled | -- |
| Scale | adequate-ish | modest seeded z_goal (norm 0.30); secondary, not decisive |

---

## Learning extracted

1. An OFF-vs-ON recovery test is only interpretable if the OFF arm first exhibits the failure mode the ON arm is meant to rescue. 651 had **no non-degeneracy gate**, so a saturated negative control produced a spurious 0/3.
2. Latent `goal_proximity`-to-persisted-z_goal saturates near-ceiling and cannot discriminate abandonment from persistence in a small grid; ARC-060 needs a **behavioural abandonment / re-approach** readout.
3. ARC-060's substrate is landed and the bank engages; the open question is **test design**, not substrate.
4. Plausible secondary contributor: the modest seeded z_goal (norm 0.30) -- a stronger / SD-057 object-bound goal gradient may sharpen the field-alone abandonment the redesign needs.

---

## Routing (user-confirmed)

| evidence_direction | epistemic_category | routing | substrate action |
|---|---|---|---|
| non_contributory | measurement_test_design_defect | queue-experiment (651a redesign); **do NOT weaken ARC-060** | none (SD-039/MECH-292/293 landed) |

**651a redesign spec:**
- (a) Phase-B invalidation strong enough to force FIELD_ONLY drift (physically displace the agent far from the goal cell, and/or harden the invalidation).
- (b) A **non-degeneracy gate**: the FIELD_ONLY arm must show abandonment (late << early goal-proximity, or a behavioural drop in re-approach) BEFORE the bank comparison is scored.
- (c) A **behavioural re-approach** readout alongside the latent metric.

Draft `evidence_quality_note` text is in the companion JSON (`recommended_evidence_quality_note`).
This skill does NOT write claims.yaml, manifests, review_tracker, or substrate_queue --
/governance applies the note; /queue-experiment authors 651a.
