# Failure Autopsy — V3-EXQ-603f (scaffolded_sd054_onboarding substrate-readiness)

**Generated:** 2026-06-07T05:48:39Z
**Scope:** single
**Target:** `v3_exq_603f_scaffolded_sd054_substrate_readiness_20260607T053934Z_v3`
**Queue:** V3-EXQ-603f · `experiment_purpose=diagnostic` · `claim_ids=[]`
**Outcome:** FAIL · `evidence_direction=non_contributory` · self-route `substrate_not_engaged / foraging_competence_open`
**Closure node:** goal_pipeline:GAP-2 (stays `blocked_pending_substrate`)
**Status:** confirmed (user scientific judgment applied at Step 8)

---

## 1. Facts (no interpretation)

Substrate-readiness gate for the `scaffolded_sd054_onboarding` curriculum at restored
budget (Stage-0 20 / Stage-0b 10 / P0 100 / P1 50 / P2 15 ep, 200 steps), with the
2026-06-05 foraging-competence residual levers engaged (`p1_reef_spawn_hold_fraction=0.4`,
`p1_anneal_hold_fraction=0.3`, `auto_reconcile_gating_to_seeding=true`,
`cue_recall_bridge_enabled=true`, `stage0_bind_incentive_token=true`,
`seeding_gain=1.5 / benefit_threshold=0.02 / drive_floor=0.9`,
`developmental_window_enabled=true`, `contact_gated_goal_updates=true`).

Three load-bearing gates, min_fraction 2/3:

| seed | G0 forced-feed→z_goal (≥0.4) | G1 P1 survival (median last-10 len, gate ≥75) | G2 P2 contact | P2 z_goal@contact (canonical G3, >0.4) |
|---|---|---|---|---|
| 42 | ✓ 0.493 | ✗ **38.0** | ✗ contact_rate 0.0 / 0 events | 0.0 |
| 43 | ✗ 0.397 | ✗ **12.5** | ✗ contact_rate 0.0 / 0 events | 0.0 |
| 44 | ✓ 0.437 | ✗ **28.5** | ✓ **contact_rate 0.393 / 85 events** | **0.450** |

Gate tally: **G0 2/3 PASS · G1 0/3 FAIL · G2 1/3 FAIL · overall FAIL**.
P0 (reef-refuge, hfa=0, goal frozen) mean episode length 96.6–100.9 (seeds 42/44);
collapses to median 12.5–38.0 in P1 wean-to-wild. Stage-0b retention gate passes 3/3
(0.93–0.97). Cue-recall fires heavily (892 / 198 / 298) without lifting contact on the
dying seeds. Self-route precondition `stage0_forced_feed_lights_zgoal` **met** (2/3);
`criteria_non_degenerate` all true → the self-route is a trustworthy hypothesis, not a
vacuous fail (V3-EXQ-642 check applied).

## 2. Claim-layer map

`claim_ids=[]` — substrate-readiness diagnostic, weights no claim. It gates the GAP-2
cohort (SD-049, SD-015, MECH-229, MECH-230, MECH-117, MECH-216, ARC-030, ARC-032,
Q-030), which stay `pending_retest_after_substrate`. No claim is at risk of demotion
from this FAIL; the question is purely which substrate work unblocks GAP-2 next.

## 3. Biological-reference triage

Closest reference: **altricial-species developmental provisioning** — a juvenile is
provisioned in a nursery and weaned *gradually*, acquiring survival skill
(hazard/predator avoidance) through a *protected exploration* period before it must
forage under hazard. Not a formal-definition import → **no lit-pull commission**; the
developmental-provisioning literature already grounds the nursery design, and the gap
is curriculum *structure*, not concept.

**Failure signature matches "weaned too early / both competencies loaded at once."**
The agent survives the safe refuge (P0 len ~97–101) and collapses the moment P1
unfreezes the goal pipeline *and* weans into the hazard band simultaneously
(median 12–38). It dies before survival competence develops.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | N/A (claim-free diagnostic) | gates GAP-2 cohort; no claim tested |
| Biological reference | clear | developmental provisioning; not a formal import; no lit-pull |
| Prerequisites | **missing** | hazard-avoidance / survival competence is never trained as its own stage; P1 loads goal-unfreeze + wean-to-hazard at once |
| Implementation completeness | partial | 2026-06-05 residual levers fire (reef-spawn 20 ep, auto-reconcile threshold computed, cue fires) but are necessary-not-sufficient for survival |
| Environment adequacy | wrong pressures (staging) | P1 hazard pressure arrives before the policy is survival-competent; `hfa=0.3` makes foraging actively dangerous |
| Measurement adequacy | adequate | gate non-degenerate; positive control met; seed-44 ecological G3 confirms the chain |
| Integration adequacy | coupled (proven) | seed 44: contact → seed → z_goal@contact 0.45 end-to-end |
| Scale / capacity | adequate | budget restored vs 603e; the budget confound is ruled out |

**Dominant diagnosis: prerequisites — a missing, separately-trained hazard-avoidance
competence stage.** Recommended epistemic_category for the gated cohort claims:
`substrate_conditional` (unchanged); the diagnostic itself is claim-free.

## 5. The disambiguator (why this overrides the script's pre-registered route)

The script's interpretation grid (lines 81–85) pre-registered, for this exact
G0-pass/G1-G2-fail outcome: *"the cue-to-action selection-authority thread
(modulatory-bias-selection-authority; V3-EXQ-643a/643b → 640b) is the next blocker,
NOT more developmental scaffold levers."*

**Seed 44 falsifies that as the dominant route.** Seed 44 foraged well (contact 0.393,
85 events) *and* its contact cleanly seeded z_goal ecologically (0.450 > 0.4 gate) — and
it **still failed survival** (median 28.5 < 75). Cue→food selection-authority (what 640b
tests) cannot rescue an agent that dies to hazards, and approaching food under `hfa=0.3`
(hazards drift toward food) plausibly *raises* exposure. The survival leg is upstream of,
and orthogonal to, the cue-authority question. 640b remains valid for the GAP-7
cue-authority claim, but it does **not** address the GAP-2 survival ceiling.

## 6. Learning extracted

1. **The goal-formation + ecological-seeding chain is proven end-to-end** (seed 44):
   the 2026-06-05 residual moved the substrate from 603e's z_goal=0-on-all-cells to one
   seed achieving a clean ecological seed. Positive progress; do not rebuild the goal
   stream.
2. **GAP-2's single load-bearing blocker is now P1 survival / hazard-avoidance**
   (0/3, even the foraging seed died), not goal-formation, not cue-recall, not contact
   wiring.
3. **The curriculum couples two competencies in P1** (goal-pipeline unfreeze + wean to
   hazard) and the agent cannot acquire both at once. Strengthening the existing holds
   is unlikely to suffice; the competencies need to be **decomposed and trained
   separately** (user judgment, Step 8).

## 7. Repair pathway (user-directed, Step 8)

**Route: `/implement-substrate` (amend `scaffolded_sd054_onboarding`).** Decompose the
wean-to-wild curriculum into separately-trained competency stages, per the user's
design:

1. **Safe goal-attainment stage** — a hazard-free (or near-free) curriculum stage,
   extended if needed, until goal-attainment / foraging is reliable on its own.
2. **Separate hazard-avoidance training stage** — hazards present, foraging pressure
   minimal, so the policy learns avoidance *in isolation* before it must do both.
3. **Wean into combined foraging + hazard** (the existing P1/P2), now entered by a
   policy that is already survival- *and* goal-competent.

Optional structured variant the user raised: a **forced-choice micro-environment** where
each adjacent grid cell carries a distinct affordance (goal / hazard / free), so the
agent learns the discrimination under controlled, balanced pressure.

This is a curriculum-*structure* amend (new stage between P0 and P1), not a re-run of the
603 lineage with stronger holds and not a goal-stream change. The substrate code exists;
the amend adds a separately-trained hazard-avoidance stage. Validation is a re-issued
substrate-readiness run (V3-EXQ-603g or successor) against the same G0/G1/G2/G3 gate.

GAP-2 stays `blocked_pending_substrate` until that re-run clears G1 survival ≥2/3
AND G2 contact ≥2/3 AND ecological G3 ≥2/3.

## 8. Routing summary

- **routing:** implement-substrate (amend)
- **substrate_queue:** amend `scaffolded_sd054_onboarding` (queue[90], ready=False) with
  the 603f failure record + the curriculum-decomposition implementation hint.
- **no** claims.yaml / manifest / review_tracker / substrate_queue writes from this
  skill — governance applies the recommendation.
- **640b** (running) is complementary (GAP-7 cue-authority), not a GAP-2 fix; the
  script's pre-registered "selection-authority is the next blocker" routing is
  superseded for GAP-2 by the seed-44 disambiguator.
