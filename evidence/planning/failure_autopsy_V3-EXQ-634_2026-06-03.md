# Failure Autopsy -- V3-EXQ-634 (scaffolded_sd054_onboarding nursery substrate-readiness)

- **generated_utc:** 2026-06-03T16:53:10Z
- **scope:** single (convergent with the 632 / 514l / 603e-626a-622 foraging-competence cluster)
- **status:** confirmed (user-approved 2026-06-03 via AskUserQuestion)
- **run_id:** v3_exq_634_scaffolded_nursery_substrate_readiness_20260603T163357Z_v3
- **queue_id:** V3-EXQ-634
- **claim_ids:** [] (diagnostic; weights no governance score)
- **experiment_purpose:** diagnostic (substrate-readiness validation)
- **machine:** see manifest

V3-EXQ-634 is the full-scale runtime-readiness validation of the freshly-landed
`scaffolded_sd054_onboarding` nursery/feeding amend (ree-v3 e718bf4 + the
developmental-window/consolidation amend, substrate_queue status
`amend_developmental_window_implemented_pending_validation`, ready=false). It is NOT
603f and tags no claim -- its job is to decide whether the substrate's own runtime
gates pass, which would flip `ready=true` and unblock V3-EXQ-603f.

---

## 1. Facts -- reconstruction (no interpretation)

Developmental sequence on one strengthened scaffold config x 3 seeds (42/43/44).
Curriculum budgets: Stage-0 nursery = 20 ep, P0 = 100 ep, P1 = 50 ep, P2 = 15 ep,
200 steps/ep; P1 hold_fraction = 0.3, P0 hazards = 1, P2 hazard_food_attraction
guard = 0.3.

**Outcome: FAIL. evidence_direction: non_contributory.
interpretation_branch = `substrate_not_engaged`. substrate_gate_passed = false.**

### Pre-registered substrate gates (each requires >= 2/3 seeds)

| Gate | Type | Threshold | Seed 42 | Seed 43 | Seed 44 | Seeds pass | Result |
|---|---|---|---|---|---|---|---|
| G0 Stage-0 forced-feed z_goal_norm_peak | **positive control** | > 0.4 | 0.4540 | 0.4543 | 0.4026 | **3/3** | **PASS** |
| G1 P1 survival/foraging | prerequisite | survive window | FAIL (med ep len 12.5) | PASS (200) | FAIL (med ep len 14.5) | 1/3 | **FAIL** |
| G2 P2 ecological contact rate | prerequisite | > 0 | 0.0 | 0.0 | 0.510 | 1/3 | **FAIL** |
| G3 P2 mature-test z_goal_norm_peak | discrimination | > 0.4 | 0.0038 | ~0 (5.7e-12) | 0.0057 | 0/3 | **FAIL** |

`stage0_benefit_exposure` = 1.0 on all three seeds (forced feed delivered as designed);
`stage0_z_goal_formed` = true on all three.

### Two load-bearing facts

1. **The forced-feed nursery (G0) passes on every seed.** When supra-threshold benefit
   is delivered in the hazard-free reef nursery -- decoupled from survival/foraging --
   the z_goal stream lights above the 0.4 threshold (0.40-0.45) on all 3 seeds. The
   Stage-0 positive control is satisfied: the goal-formation wiring is sound.
2. **The wean-to-wild half collapses.** Once the agent must forage on its own (P1/P2),
   only 1/3 seeds survives P1 (43; 42 and 44 die at ~12-15 step median episode length),
   only 1/3 makes any ecological resource contact in P2 (44 at 0.51; 42 and 43 at 0.0),
   and mature-test z_goal collapses to ~0 on all 3 seeds (G3 0/3). The seed that
   survives (43) makes zero contact; the seed that makes contact (44) does not survive
   P1. No single seed clears the whole chain.

**Positive/negative control passes; every behavioural-prerequisite and discrimination
gate fails because the agent does not reach self-sustaining foraging in the wild.**
This is the substrate-ceiling fingerprint, measured here at the substrate level.

---

## 2. Claim-layer map

Not applicable in the usual sense: `claim_ids = []`. 634 is a substrate-readiness
diagnostic and weights no claim's confidence or conflict ratio. Its disposition governs
the `scaffolded_sd054_onboarding` substrate_queue entry (which gates V3-EXQ-603f and,
through it, the retest of Q-045 / MECH-313 / MECH-260 / MECH-295 / SD-049 Phase-2 and
the rest of that entry's `unblocks_claims`).

---

## 3. Biological-reference triage

The mechanism under scaffold is goal-representation formation from reward contact
(vmPFC/OFC goal-value learning; Berridge incentive-salience). The biology requires
consummatory contact for a goal/value representation to form and persist. 634's split
is exactly the biological signature: **a hand-fed infant forms the goal representation
(nursery G0 passes), but a juvenile that cannot yet forage competently in the wild
loses it** -- the representation is not maintained without ongoing reward contact.

This is the **discovered/confirmed prerequisite** reading (parallel to SD-010/SD-011),
not falsification. Biology is clear and already lit-covered for this family
(SD-049 lit_conf 0.898; Berridge 2018, Smith & Berridge 2007) -- **no lit-pull is
warranted.** The gap is a behavioural-substrate (foraging-competence) gap, not a
biological-translation gap.

---

## 4. Multi-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | n/a | claim_ids=[]; diagnostic. Weights no governance score. |
| Biological reference | **clear, faithful** | vmPFC/OFC + Berridge; G0/G3 split = fed-infant forms goal, non-foraging juvenile loses it. |
| Prerequisites | **partially met** | Nursery/forced-feed prerequisite IMPLEMENTED + PROVEN (G0 3/3). Foraging-competence + survival prerequisite NOT met (G1 1/3, G2 1/3). |
| Implementation | **necessary-but-insufficient** | The amend's nursery half (run_stage0_nursery forced-feed) works exactly as designed. The P0/P1 survival-foraging scaffold half does not reliably carry >= 2/3 seeds to self-sustaining contact. |
| Environment | **guarded as designed** | P2 hfa guard = 0.3 applied on all seeds; P0 hazards = 1. The environment is not the confound -- the policy does not forage competently within it. |
| Measurement | **adequate** | Gates fire and read cleanly; per-seed instrumentation complete; positive control isolates formation from maintenance. One near-threshold signal (seed 43 reaches 200-step P1 survival) suggests the scaffold is close but not reliable across seeds. |
| Integration | **partially coupled** | Stage-0 -> P0 -> P1 -> P2 chain runs end-to-end; the failure is competence within the chain, not a wiring break. |
| Scale / capacity | **possible contributing factor** | P0=100 / P1=50 may be near the edge (seed 43 survives); strengthening AND/OR lengthening the survival-foraging scaffold are both live levers. |

**Recommended epistemic_category: `substrate_ceiling`** (recommendation only; governance
applies). **Recommended evidence_direction: `non_contributory`** (diagnostic, no claim
weighted).

---

## 5. Cluster context

634 is the substrate-level confirmation of the same structural property diagnosed per-run
in 632 (MECH-230 z_goal, seed-42 clean positive + 2/3 seeds zero contact), 514l (MECH-229
wanting/liking, ~0.2% consumption rate), and the 603e/626a/622 cluster. **One structural
property, not N bugs:** REE-v3's goal-pipeline FAILs across structurally-different claims
are dominated by an ecological foraging-competence / reward-contact ceiling, not by
representational absence. 634 adds the decisive within-substrate evidence: when contact is
*forced* (nursery), the goal representation forms (G0 3/3); the limiting factor is
getting the juvenile to self-sustaining contact in the wild.

---

## 6. Learning extracted + repair pathway

- The `scaffolded_sd054_onboarding` nursery/forced-feed amend is **validated as
  necessary** (G0 proves goal formation under forced feed) but **insufficient** (G1/G2/G3
  fail -- juveniles do not wean to competent foraging).
- The substrate is **NOT ready**: do not flip `substrate_queue.ready = true`; do not queue
  V3-EXQ-603f. The entry already carries `ready=false` and 0 failure_records.
- Repair: strengthen and/or lengthen the **P0/P1 survival-foraging scaffold** so >= 2/3
  seeds reach self-sustaining ecological contact, then re-validate. Seed 43's 200-step P1
  survival shows the target is reachable; the scaffold is not yet reliable across seeds.

**Routing (user-confirmed): `implement-substrate`, action = `amend` on
`scaffolded_sd054_onboarding`.** Add a 634 validation `failure_record` and refine the
`implementation_hint` to target the survival-foraging-competence half of the curriculum
(nursery/G0 proven; wean-to-wild insufficient). Keep `ready=false`. No claim edits.

### Draft note governance should record on the substrate_queue entry (do not write here)

> V3-EXQ-634 (2026-06-03) full-scale readiness validation FAILED the substrate gate
> (substrate_gate_passed=false, branch=substrate_not_engaged). Stage-0 forced-feed
> positive control PASSES 3/3 (z_goal_norm_peak 0.40-0.45 > 0.4) -- the nursery half of
> the amend is validated; the goal-formation wiring is sound. But P1 survival passes only
> 1/3 (seed 43), P2 ecological contact passes only 1/3 (seed 44), and P2 mature-test
> z_goal is ~0 on all 3 seeds (0/3). The seed that survives makes no contact; the seed
> that contacts does not survive. The amend is necessary-but-insufficient: forced-feed
> goal formation works, but the P0/P1 survival-foraging scaffold does not reliably carry
> >= 2/3 seeds to self-sustaining contact, so the goal representation is not maintained in
> the wild. Substrate stays NOT ready (ready=false); do not queue 603f. Repair: strengthen
> and/or lengthen the survival-foraging scaffold, then re-validate.

---

## 7. Routing summary

| Field | Value |
|---|---|
| failed gate | G1 P1-survival (1/3) + G2 P2-contact (1/3) + G3 P2-z_goal (0/3); G0 positive control PASSES 3/3 |
| dominant diagnosis layer | implementation: necessary-but-insufficient (foraging-competence half of the scaffold) |
| biological-reference verdict | clear + faithful; G0/G3 split = fed-infant-forms / non-foraging-juvenile-loses; discovered prerequisite, not falsification |
| recommended epistemic_category | substrate_ceiling |
| recommended evidence_direction | non_contributory (diagnostic, claim_ids=[]) |
| routing | implement-substrate, action=amend on scaffolded_sd054_onboarding |
| lit-pull | none (biology clear + already covered) |
| substrate ready? | NO -- keep ready=false; do NOT queue 603f |
