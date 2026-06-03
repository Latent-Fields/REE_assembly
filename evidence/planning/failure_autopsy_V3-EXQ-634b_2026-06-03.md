# Failure Autopsy -- V3-EXQ-634b (scaffolded_sd054_onboarding developmental-window / Stage-0b consolidation readiness)

- **generated_utc:** 2026-06-03T19:29:05Z
- **scope:** single (convergent with the 632 / 514l / 603e-626a-622 / 634 goal-pipeline contact-seeding cluster)
- **status:** confirmed (user-approved 2026-06-03 via AskUserQuestion)
- **run_id:** v3_exq_634b_scaffolded_nursery_consolidation_readiness_20260603T183754Z_v3
- **queue_id:** V3-EXQ-634b
- **claim_ids:** [] (diagnostic; weights no governance score)
- **experiment_purpose:** diagnostic (substrate-readiness validation of the 2026-06-03b developmental-window / consolidation amend)
- **machine:** ree-cloud-3

V3-EXQ-634b is the developmental-window-ON validation that the `scaffolded_sd054_onboarding`
substrate_queue entry was explicitly `ready_blocked_by` (`validation_experiment = V3-EXQ-634b`).
It turns ON the two flags the 634 design-error review identified as missing
(`scaffold_stage0b_enabled` + `scaffold_contact_gated_goal_updates`) and re-runs the full
developmental sequence. It tags no claim; its disposition governs the substrate entry
(which gates V3-EXQ-603f and, through it, Q-045 / MECH-313 / MECH-260 / MECH-295 / MECH-307 /
MECH-117 / SD-049 Phase-2 behavioural / ARC-030 / Q-040 / MECH-230).

---

## 1. Facts -- reconstruction (no interpretation)

Developmental sequence on one strengthened scaffold config x 3 seeds (42/43/44).
Curriculum: Stage-0 nursery = 20 ep, Stage-0b consolidation = 10 ep, P0 = 100 ep, P1 = 50 ep,
P2 = 15 ep, 200 steps/ep; P1 hold_fraction = 0.3, P0 hazards = 1, P2 hazard_food_attraction
guard = 0.3. Amend flags ON: `developmental_window_enabled`, `stage0b_enabled`,
`contact_gated_goal_updates`.

**Outcome: FAIL. evidence_direction: non_contributory.
interpretation_branch = `substrate_not_engaged`. substrate_gate_passed = false.**

### Pre-registered substrate gates (each requires >= 2/3 seeds)

| Gate | Type | Threshold | Seed 42 | Seed 43 | Seed 44 | Seeds pass | Result |
|---|---|---|---|---|---|---|---|
| G0 Stage-0 forced-feed z_goal_norm_peak | positive control | > 0.4 | 0.4424 | 0.4567 | 0.4008 | **3/3** | **PASS** |
| G0b Stage-0b retention_ratio | **NEW** consolidation | >= 0.75 | 0.9942 | 0.9856 | 0.9831 | **3/3** | **PASS** |
| G1 P1 survival/foraging | prerequisite | survive window | FAIL (med 20) | PASS (132) | FAIL (med 12) | 1/3 | **FAIL** |
| G2 P2 ecological contact rate | prerequisite | > 0 | 0.0 | 0.3482 | 0.1118 | **2/3** | **PASS** |
| G3 P2 mature-test z_goal_norm_peak | discrimination | > 0.4 | 0.4398 | 4.5e-05 | 0.1036 | 1/3 | **FAIL** |

Decay-only-update instrumentation (the amend's whole point): `n_decay_only_updates = 0` on
all three seeds in BOTH P1 and P2. Contact-gating eliminated the every-step decay-only washout
the 634 design review diagnosed. Per-seed contact-refresh / skipped-protected counts:
- s42: P1 refresh 0 / skipped 1208 ; P2 refresh 0 / skipped 250  (never contacts)
- s43: P1 refresh 1870 / skipped 3885 ; P2 refresh 475 / skipped 889  (forages richly)
- s44: P1 refresh 405 / skipped 479 ; P2 refresh 18 / skipped 143  (partial)

### Three load-bearing facts

1. **The consolidation fix works -- decisively.** G0b retention passes 3/3 (0.983-0.994), and
   `n_decay_only_updates = 0` everywhere. The Stage-0b protected window + contact-gating do
   exactly what they were designed to do: a non-contacting infant retains its forced-feed
   z_goal across P0/P1/P2 instead of having it eroded by per-step decay-only calls. This is a
   **positive result for the mechanism**, and G2 contact improved 1/3 (634) -> 2/3 (634b).

2. **G3 is anti-correlated with foraging.** The seed that *passes* G3 (s42, z_goal 0.4398) made
   **zero** wild contact: its P2 peak is byte-identical to its Stage-0b-end value
   (0.4398159682750702), i.e. it is the protected forced-feed nursery trace carried through
   untouched (every P1/P2 step skipped). The seed that forages best (s43: survives P1,
   contact_rate 0.348, **475** P2 contact-refresh calls) collapsed to z_goal ~ **4.5e-05** -- its
   consolidated trace was decayed to zero by the very foraging meant to maintain it.

3. **Root cause (verified in code): a benefit-magnitude / seeding-threshold mismatch.** The
   contact-gating skips updates only when `benefit <= contact_threshold` (`1e-6`,
   `scaffold_p2_contact_benefit_threshold`). But `GoalState.update` (goal.py:209-224) only pulls
   z_goal toward z_world when `effective_benefit = benefit * z_goal_seeding_gain(1.0) *
   (1 + drive_weight(2.0) * drive_trace) > benefit_threshold (0.1)`. Natural wild contact
   (`obs_body[11]`, documented ~0.03 regime, goal.py:77-78) yields effective_benefit <= ~0.09
   < 0.1 at full drive, so the seeding pull **essentially never fires during real foraging**.
   Steps in the band `(1e-6, ~0.1-effective)` count as "contact" (so they are NOT skipped) yet
   are too weak to seed -- they only apply the unconditional 0.5%/step decay (goal.py:173). For
   the foraging seed (s43), 475+ such weak-contact updates decayed the consolidated attractor
   toward zero. The forced nursery (benefit=1.0) is the **only** input above the 0.1 firing
   threshold -- which is exactly why G0 (forced) passes and G3-via-wild-contact cannot.

---

## 2. Claim-layer map

Not applicable in the usual sense: `claim_ids = []`. 634b is a substrate-readiness diagnostic
and weights no claim's confidence or conflict ratio. Its disposition governs the
`scaffolded_sd054_onboarding` substrate_queue entry (ready=false; `ready_blocked_by` =
V3-EXQ-634b; gates V3-EXQ-603f).

---

## 3. Biological-reference triage

The mechanism under scaffold is goal-representation formation/maintenance from reward contact
(vmPFC/OFC goal-value learning; Berridge incentive salience). Two biological facts are relevant
and both are satisfied/clear:
- Incentive-salience / goal-value magnitude **scales with reward magnitude**, so a regime where
  sub-threshold ecological reward fails to maintain a goal representation is biologically
  plausible -- a fed infant forms it (G0/G0b 3/3); a juvenile receiving only weak/intermittent
  wild reward loses it.
- The *consolidation* reading (Stage-0b protected window) is biologically faithful and is the
  thing 634b decisively confirms: a just-formed goal trace, protected from erosion, persists.

The specific numeric mismatch (contact detected at 1e-6 while seeding fires at 0.1-effective) is
an **implementation / calibration artifact, not a biological claim**. Biology is clear and
already lit-covered for this family (SD-049 lit_conf 0.898; Berridge 2018; Smith & Berridge 2007)
-- **no lit-pull warranted.** The gap is substrate calibration + foraging competence, not a
biological-translation gap. This is the discovered/strengthened-prerequisite reading
(parallel SD-010/SD-011), not falsification.

---

## 4. Multi-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | n/a | claim_ids=[]; diagnostic. Weights no governance score. |
| Biological reference | **clear, faithful** | vmPFC/OFC + Berridge; magnitude-scaled incentive salience + consolidation both supported. |
| Prerequisites | **partially met (advanced)** | Nursery/forced-feed PROVEN (G0 3/3). **Consolidation/protected-window now PROVEN (G0b 3/3)** -- a 634->634b advance. Foraging-competence (G1 1/3) + contact-seeding-magnitude (the new gap) NOT met. |
| Implementation | **necessary-but-insufficient; new sub-gap isolated** | Stage-0b + contact-gating work as designed (decay_only=0). The remaining blocker: the contact-gating `contact_threshold` (1e-6) is decoupled from the goal-seeding firing threshold (`benefit_threshold` 0.1-effective), so genuine wild contact decays rather than seeds z_goal. |
| Environment | **guarded as designed** | P2 hfa guard 0.3; P0 hazards 1. Not the confound. |
| Measurement | **test-design defect on G3** | G3 (z_goal>0.4) is forced-feed-calibrated and is anti-correlated with foraging: passed by the non-contacting seed, failed by the forager. G2 contact threshold (1e-6) and G3 (0.4-via-forced-feed) measure at incompatible benefit scales. |
| Integration | **coupled, runs end-to-end** | Stage-0 -> 0b -> P0 -> P1 -> P2 chain runs; failure is calibration + competence within the chain, not a wiring break. |
| Scale / capacity | possible contributing factor | P0=100/P1=50 near edge (only s43 survives P1). |

**Recommended epistemic_category: `substrate_ceiling`** (with a `measurement_test_design_defect`
component on G3). **Recommended evidence_direction: `non_contributory`** (diagnostic, no claim
weighted). Recommendations only; governance applies.

---

## 5. Cluster context

634b belongs to the same goal-pipeline contact/seeding ceiling family diagnosed in 632
(MECH-230 z_goal, seed-42 clean positive at genuine consumption + 2/3 seeds zero consumption),
514l (MECH-229 wanting/liking, ~0.2% consumption rate), 626a, and 603e/622, and confirmed at
substrate level by 634. **One structural property, not N bugs.** 634b *sub-divides* that ceiling
into two separable gaps:
1. **Reach contact** -- foraging competence (G1 1/3 survival; still open from 634).
2. **Contact strong enough to fire seeding** -- benefit-magnitude / threshold calibration
   (effective_benefit < benefit_threshold for natural reward; new this run).

The 632 seed-42 clean positive (z_goal_norm 3.0115 at 6 genuine consumption events) is the
existence proof that when the pull fires the representation is correct -- so the limiter is
getting effective_benefit above the firing threshold during natural foraging, not representational
absence. A concurrent session (goal_pipeline:GAP-7 L1, V3-EXQ-626b forced-seed positive control)
is directly convergent.

---

## 6. Learning extracted + repair pathway

- The `scaffolded_sd054_onboarding` developmental-window / Stage-0b consolidation amend is
  **validated** (G0b retention 3/3; decay_only=0): the protected-window + contact-gating fix the
  decay-only washout 634 flagged. This is a genuine 634->634b advance and should be recorded as a
  *positive* mechanism result, not just another FAIL.
- The substrate is **still NOT ready** because two coupled gaps remain: (a) a contact->seed
  benefit-magnitude/threshold mismatch that prevents natural foraging from seeding z_goal, and
  (b) the still-open foraging-competence half (G1 1/3). Keep `ready=false`; do **not** queue
  V3-EXQ-603f.
- The G3 acceptance gate is mis-specified: at 0.4 it is reachable only by the protected nursery
  trace and is anti-correlated with the foraging it is meant to certify. A future re-validation
  must read mature-test z_goal **at genuine consumption events** (632-style `num_contact_events`),
  not the forced-feed-calibrated frozen-peak, or it remains uninterpretable.

**Routing (user-confirmed): `implement-substrate`, action = `amend` on
`scaffolded_sd054_onboarding`.** Add a 634b `failure_record`; refine the `implementation_hint` to
target BOTH (a) reconciling the contact-gating `contact_threshold` with the goal-seeding firing
threshold so genuine wild contact seeds z_goal (candidate levers: raise `z_goal_seeding_gain`
above 1.0, lower `benefit_threshold` below 0.1, apply `drive_floor`~0.9 as the EXQ-582a first-PASS
arm did, and/or raise `contact_threshold` so sub-seeding whiffs are *protected* rather than
decaying the trace) AND (b) the still-open foraging-competence half (strengthen/lengthen P0/P1 so
>=2/3 seeds reach self-sustaining consumption). Keep `ready=false`. No claim edits.

### Draft note governance should record on the substrate_queue entry (do not write here)

> V3-EXQ-634b (2026-06-03) developmental-window/Stage-0b consolidation validation FAILED the
> substrate gate (substrate_gate_passed=false, branch=substrate_not_engaged), BUT validated the
> consolidation half: G0 Stage-0 forced-feed PASS 3/3 (0.40-0.46) and **G0b Stage-0b retention
> PASS 3/3 (0.98-0.99) with n_decay_only_updates=0 everywhere** -- the protected-window +
> contact-gating amend fixes the decay-only washout 634 flagged. The remaining blockers are two
> coupled gaps: (1) a contact->seed benefit-magnitude/threshold mismatch -- contact-gating skips
> only benefit<=1e-6, but GoalState.update seeds only when effective_benefit (benefit *
> gain(1.0) * (1 + drive_weight(2.0)*drive_trace)) > benefit_threshold(0.1); natural wild benefit
> ~0.03 stays below the firing threshold, so the foraging seed (43: 475 P2 contact-refresh calls,
> contact_rate 0.348) DECAYED its consolidated trace to ~0 while the non-foraging seed (42)
> "passed" G3 by retaining the untouched forced-feed nursery value (0.4398, byte-identical to
> Stage-0b-end). G3 is thus anti-correlated with foraging and is mis-specified at 0.4
> (forced-feed-calibrated); a re-validation must read z_goal at genuine consumption events
> (632-style), not the frozen-peak. (2) The still-open foraging-competence half (G1 P1-survival
> 1/3). Substrate stays NOT ready (ready=false); do not queue 603f. Repair: reconcile
> contact_threshold with the seeding firing threshold (raise z_goal_seeding_gain / lower
> benefit_threshold / drive_floor / raise contact_threshold) AND strengthen/lengthen the P0/P1
> survival-foraging scaffold, then re-validate with a consumption-event-gated mature-test readout.

---

## 7. Routing summary

| Field | Value |
|---|---|
| failed gate | G1 P1-survival (1/3) + G3 P2-z_goal (1/3); G0 positive control PASS 3/3; **G0b consolidation PASS 3/3 (NEW, validates the amend)**; G2 contact PASS 2/3 |
| dominant diagnosis layer | implementation: contact->seed benefit-magnitude/threshold mismatch (new) + still-open foraging-competence; consolidation half proven |
| biological-reference verdict | clear + faithful; magnitude-scaled incentive salience + consolidation both supported; calibration artifact, not falsification |
| recommended epistemic_category | substrate_ceiling (+ measurement_test_design_defect on G3) |
| recommended evidence_direction | non_contributory (diagnostic, claim_ids=[]) |
| routing | implement-substrate, action=amend on scaffolded_sd054_onboarding (both seeding-calibration + foraging-competence; + G3 redesign to consumption-event-gated readout) |
| lit-pull | none (biology clear + already covered) |
| substrate ready? | NO -- keep ready=false; do NOT queue 603f |
