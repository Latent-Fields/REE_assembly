# Failure Autopsy: V3-EXQ-603 followon chain (603a/b/c) + V3-EXQ-604/605

**Generated**: 2026-05-29T16:56:00Z
**Scope**: cluster (two sequenced clusters)
**Status**: confirmed
**Autopsy session**: failure-autopsy-603-followon-604-605-20260529T165600Z
**Calibration-debt lens**: MECH-320 / ARC-065 / goal-pipeline priority-1 per `memory/project_calibration_debt.md`

## Predecessor autopsies in scope

- `evidence/planning/failure_autopsy_V3-EXQ-603_2026-05-23.md` — predecessor for Cluster A; identified call-path bypass + temporal-horizon gap; routed `/queue-experiment` for 603a
- `evidence/planning/failure_autopsy_V3-EXQ-490g-cohort_2026-05-29.md` (commit `12f0dda773`) — analysed V3-EXQ-603c under substrate-uniform z_goal-zero lens; created `SD-XXX-scaffolded-sd054-onboarding` substrate_queue entry (action=create)
- `evidence/planning/failure_autopsy_V3-EXQ-591_2026-05-27.md` — named substrate prereq #2 (goal-pipeline z_goal under default V3 training regime)

---

## CLUSTER A — V3-EXQ-603a / 603b / 603c (Q-045 / MECH-313 / MECH-260)

### 1. Targets

| Target | Date | Outcome | manifest evidence_direction | Predecessor relation |
|---|---|---|---|---|
| V3-EXQ-603a | 2026-05-24 | FAIL | non_contributory (per-claim all non_contributory) | First fix-pass (Fix 1 call-path + Fix 2 FIFO warmup + Fix 3 per-claim direction) following V3-EXQ-603 predecessor autopsy |
| V3-EXQ-603b | 2026-05-25 / 2026-05-26 | FAIL | re-run mixed -> non_contributory after 2026-05-26 governance autopsy override | Fix A steps_per_episode 200 -> 500 + Fix B hazard_harm 0.05 -> 0.02 |
| V3-EXQ-603c | 2026-05-27 | FAIL | non_contributory | Fix C P0 100ep + P1 50ep phased training + Fix D P1 survival gate. ALREADY autopsied by 490g-cohort (commit 12f0dda773) under substrate-uniform z_goal-zero lens; this autopsy confirms that disposition under the Q-045/MECH-313/MECH-260 followon lens (no fork). |

### 2. Convergent table — four-run chain

| Run | mech260 operative | fifo gate ok | Surviving seeds | ARM_0 | ARM_1 (313 only) | ARM_2 (260 only) | ARM_3 (both) | Outcome |
|---|---|---|---|---|---|---|---|---|
| V3-EXQ-603 (x2) | false (call-path bypass) | n/a | 3/3 (no warmup) | 0.244 | 0.292 | 0.244 (== 0) | 0.292 (== 1) | FAIL, 6 d.p. degenerate |
| V3-EXQ-603a | true | false | 1/3 (seed 43) | 0.481 | 0.496 (+0.015) | 0.442 (-0.039) | 0.451 (-0.030) | FAIL non_contributory |
| V3-EXQ-603b | true | false | 1/3 (seed 43) | 0.449 | 0.460 (+0.011) | 0.490 (+0.041) | 0.494 (+0.045) | FAIL non_contributory (sub-margin) |
| V3-EXQ-603c | true (seed 43) | false (8/12 cells abort P1) | 1/3 (seed 43) | 0.484 | 0.484 (== ARM_0!) | 0.519 (+0.035) | 0.522 (+0.038) | FAIL non_contributory |

### 3. The shape

**Convergent single structural property across the four-run chain**: V3 substrate at default config under random / early policy produces a two-failure-mode lock:

1. **Seed-fragility on the target env.** Seeds 42 and 44 die before the FIFO warmup (or, in 603c, before the P1 survival gate) in every cell across all three followons. Only seed 43 survives. Effective N=1.
2. **MECH-313 noise-floor lift collapses post-phased-training** (603c ARM_1 == ARM_0 exactly), directionally consistent with the LC-NE-against-prior biology but anecdotal at N=1.

The four-run progression demonstrates that the predecessor autopsy's repair pathway (call-path → temporal gate → hazard tuning → phased training) was **chasing the wrong layer**. Each fix landed at its stated target; each successive fix made the next layer down the proximate constraint. The load-bearing constraint is goal-pipeline / training-regime substrate enrichment (591 autopsy substrate prereq #2; 490g-cohort autopsy Cluster B disposition).

### 4. Claim-layer map

| Claim | Type | Status | epistemic_category | Did the test let it express? |
|---|---|---|---|---|
| MECH-260 | mechanism_hypothesis | candidate, v3_pending, pending_retest_after_substrate | substrate_ceiling | NO — operative in all three followons but only seed 43 produces measurable data; N=1 cannot resolve C2/C3 |
| MECH-313 | mechanism_hypothesis | candidate_substrate_landed, v3_pending, pending_retest_after_substrate | substrate_ceiling | NO — pre-training sub-threshold lift (+0.011 to +0.015 at N=1); post-training zero lift (ARM_1 == ARM_0 in 603c) |
| Q-045 | open_question | open, v3_pending, pending_retest_after_substrate | substrate_ceiling | NO — coupling/independence question untestable when both mechanisms produce sub-threshold or zero deltas at N=1 |

All three claims already carry `pending_retest_after_substrate: true` and `epistemic_category: substrate_ceiling`. **This autopsy adds the followon record, not a re-classification.**

### 5. Biological-reference triage

- **MECH-313 (LC-NE tonic noise floor)** — clear (Aston-Jones & Cohen 2005; Haarnoja 2018 SAC). 603c post-training collapse (ARM_1 == ARM_0) is directionally consistent with LC-NE-against-prior biology — tonic noise weakens against a sharper behavioural prior. Anecdotal at N=1; worth re-checking once substrate-fixed retests deliver N>=2.
- **MECH-260 (dACC anti-recency)** — clear (Scholl & Kolling 2015; Kennerley 2006). FIFO + suppression both fire (dacc_history_len up to 8, max suppression 1.0, forward_calls up to 4791 across cells). Biology is intact.
- **Q-045 (LC-NE / dACC substrate independence)** — biology says COUPLED-NOT-COLLAPSED (Tervo 2014). Prediction requires a non-degenerate substrate.
- **Biology divergence: none**. This is a substrate-translation failure, not claim-falsification.

### 6. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | None of the three claims is under fair test — substrate cannot deliver discriminating signal |
| Biological reference | clear | All claims well-anchored; failure does not implicate biology |
| Prerequisites | **missing** | goal-pipeline z_goal does not develop under default V3 training; seeds 42/44 die at P1 survival gate even after P0(100ep)+P1(50ep) phased training |
| Implementation completeness | complete | MECH-260 module + MECH-313 noise floor wired and verifiably operative in surviving seed |
| Environment adequacy | inadequate for discrimination | SD-054 reef + bipartite + hazard_food_attraction=0.7 + proximity_harm_scale=0.1 hostile at random-init |
| Measurement adequacy | adequate | Per-claim direction logic, FIFO temporal gate, P1 survival gate all correctly emit underpowered branch |
| Integration adequacy | isolated | Modules work alone; default-config training does not engage goal-pipeline |
| Scale / capacity | likely insufficient | P0(100ep)+P1(50ep)+P2(500step) does not develop survival-competent policy in 2/3 seeds |

**Dominant diagnosis**: `substrate_ceiling` (goal-pipeline / training-regime substrate enrichment unmet)
**Recommended epistemic_category**: `substrate_ceiling` (already set on all three claims)

### 7. Learning extracted

1. The 603 predecessor autopsy's repair-pathway diagnosis was one layer too shallow. Call-path / temporal gate / hazard tuning / phased training are all measurement-layer fixes; the load-bearing constraint is goal-pipeline / training-regime substrate.
2. Three confirmation runs of the same convergent shape — the seed-fragility (only seed 43) is structurally identical across three different fix configurations. Not flaky data — substrate-uniform z_goal-zero fingerprint repeated.
3. MECH-313 noise-floor lift collapses with training (603c ARM_1 == ARM_0). Directionally consistent with LC-NE biology, requires substrate-fixed retest to be evidence rather than anecdote.
4. MECH-260 dACC suppression operative everywhere but behavioural effect unmeasurable at N=1. EXQ-445h (C3 3/3 seeds) remains the only valid MECH-260 support; nothing in the 603 chain weakens that record.
5. `pending_retest_after_substrate` already set across all three claims — this autopsy adds load-bearing 603a/603b failure_records to the parent SD-XXX-scaffolded-sd054-onboarding entry, not a re-classification.

### 8. Confirmed routing (user 2026-05-29 interactive gate)

- V3-EXQ-603a → **amend** SD-XXX-scaffolded-sd054-onboarding (failure_record_entry: 1/3 surviving seeds at FIFO temporal gate)
- V3-EXQ-603b → **amend** SD-XXX-scaffolded-sd054-onboarding (failure_record_entry: env-side reach extended via steps/ep=500 + hazard_harm=0.02 still 1/3 surviving)
- V3-EXQ-603c → **none** (parent 490g-cohort autopsy commit `12f0dda773` already created the entry with 603c failure_record; this autopsy confirms that disposition under the Q-045/MECH-313/MECH-260 followon lens)

### 9. Draft `evidence_quality_note` additions for `/governance`

**MECH-260** (append):
```
[2026-05-29 autopsy V3-EXQ-603a/b/c followon cluster]: Three-followon convergent confirmation
of the 591 substrate-uniform z_goal-zero family. 603a/b/c all 1/3 surviving seeds; MECH-260
operative every cell (dacc_forward_calls up to 4791 in surviving cells) but effective N=1
across the chain. Confirms 490g-cohort autopsy (commit 12f0dda773) Cluster B disposition
under the Q-045/MECH-313/MECH-260 lettered-followon lens (no fork). Adds 603a + 603b
failure_records to SD-XXX-scaffolded-sd054-onboarding substrate entry. EXQ-445h remains
the sole valid MECH-260 support; sub-margin 'weakens' or 'supports' appearances at N=1
across the 603 chain are not load-bearing.
```

**MECH-313** (append — covers 603 chain + 605):
```
[2026-05-29 autopsy V3-EXQ-603a/b/c followon + V3-EXQ-605 cluster]: Cumulative cross-substrate
sub-threshold directional signal. 603a (ARM_1 +0.015 vs ARM_0, N=1), 603b (ARM_1 +0.011,
ARM_2 +0.041, ARM_3 +0.045, N=1), 605 noise alpha sweep ({0.1, 0.5, 1.0} -> entropy
{0.259, 0.292, 0.305}, N=1 per cell). Three independent substrate designs now deliver
same-direction MECH-313 signal. 603c surprise: post-phased-training ARM_1 == ARM_0 exactly
-- directionally consistent with LC-NE-against-prior biology but anecdotal at N=1.
Re-evaluate once substrate-fixed retests (SD-XXX-scaffolded-sd054-onboarding land) deliver
N>=2 per cell.
```

**Q-045** (append):
```
[2026-05-29 autopsy V3-EXQ-603a/b/c followon cluster]: Independence/coupling question
untestable across the four-run chain (predecessor + three followons) -- effective N=1
in every iteration. Confirms substrate_ceiling category. Pending retest after
SD-XXX-scaffolded-sd054-onboarding lands and a P2 measurement window with >=2/3 seeds
becomes reachable. Lit-pull R5 design-gate (Kennerley temporal horizon) and R4
(8-cell extension) remain on hold behind the substrate fix.
```

---

## CLUSTER B — V3-EXQ-604 / 605 (Q-044/Q-043/ARC-065/MECH-313/MECH-314 + sub-flavours)

### 1. Targets

| Target | Date | Outcome | manifest evidence_direction | Existing evidence_quality |
|---|---|---|---|---|
| V3-EXQ-604 | 2026-05-21 | FAIL | non_contributory | substrate_ceiling (governance 2026-05-21) |
| V3-EXQ-605 | 2026-05-21 | FAIL | non_contributory | substrate_ceiling/measurement (governance 2026-05-21) |

### 2. Convergent table

| Run | Design | Surviving seeds | Key per-seed result | Discrimination criterion | Outcome |
|---|---|---|---|---|---|
| V3-EXQ-604 | 4-arm: ARM_0 all-on / ARM_1 novelty-off / ARM_2 uncertainty-off / ARM_3 lp-off | seeds 43, 44 partial; seed 42 dies (unique_actions=1) | **all 4 arms BIT-IDENTICAL per seed** (entropy 0.000 / 0.405813 / 0.326341; total_steps 5805 / 1495 / 2267) | C1 two-distinct-ablations: **false**; C2 ablations-not-identical: **false** | FAIL non_contributory |
| V3-EXQ-605 | 3×3: noise_alpha {0.1, 0.5, 1.0} × curiosity_scale {1.0, 5.0, 10.0} | seeds 43, 44 partial; seed 42 dies | **noise_alpha modulates** (0.259 → 0.292 → 0.305) but **curiosity_scale degenerate** (identical entropy/reef across {1×,5×,10×} per alpha row) | p1_any_calibration_zone: **false** | FAIL non_contributory |

### 3. The shape — two substrate gaps stacked

Cluster B is **convergent with Cluster A on seed-fragility** (seed 42 dies — total_steps 5805 = capped-out death; seeds 43/44 partial → same goal-pipeline-z_goal-zero fingerprint). **And** Cluster B surfaces a distinct, mechanistically separate substrate gap that Cluster A's 603 design (temperature-level mechanisms) could not surface:

**Gap 1 (shared with Cluster A): goal-pipeline / training-regime substrate** — agent survival pattern structurally identical to Cluster A.

**Gap 2 (Cluster B specific): per-candidate z_world variance substrate** — the curiosity / candidate-bonus pathway can't discriminate any ablation because all candidates carry ~uniform z_world. Fingerprint:
- **MECH-314b (uncertainty)** and **MECH-314c (learning progress)** are Phase 1 BROADCAST scalars by design (uniform across `[K]` candidates). Turning them off arithmetically cannot change selection ordering. ARM_2 == ARM_0 and ARM_3 == ARM_0 are *expected and structural*, the declared Phase 1 honest-scoping caveat surfacing under ablation.
- **MECH-314a (striatal novelty)** is supposed to be "genuinely per-candidate" via distance to ResidueField RBF centers. ARM_1 == ARM_0 to 6 d.p. in 604 means the novelty bonus is producing the same effective shift across all candidates — i.e. the candidate set is z_world-degenerate, distances are ~uniform, bonus is ~uniform, ablation undiscriminable.
- **605 curiosity_scale degeneracy at 1×/5×/10×** is the same fingerprint amplified: scaling a uniform-across-candidates bonus by 10× still doesn't change selection ordering.

This is the **per-candidate-z_world-variance gap** that SD-056 `e2_action_conditional_divergence_contrastive` is the proximal substrate fix for. SD-056 landed today (2026-05-29) on ree-v3 main (commit `041a974`); V3-EXQ-613 PASSed substrate-readiness; V3-EXQ-569a FP-2 falsifier queued today specifically tests whether SD-056 propagates per-candidate z_world variance through hippocampal scoring + E3 aggregation into observable action diversity.

**605 also delivers a partial positive read on the noise dimension**: MECH-313 modulates entropy (0.259 → 0.292 → 0.305) — same sub-threshold pattern as the 603 chain, surfacing on a different substrate. Three independent substrate designs, same-direction signal.

### 4. Claim-layer map

| Claim | Type | Status | Did the test let it express? |
|---|---|---|---|
| Q-044 | open_question | open, v3_pending | NO — sub-flavours undifferentiable because candidate set is z_world-degenerate |
| MECH-314 | mechanism_hypothesis | candidate_substrate_landed, v3_pending | NO — parent; sub-flavour ablations cannot discriminate without per-candidate z_world variance |
| MECH-314a (per-candidate novelty) | mechanism_hypothesis | candidate_substrate_landed, v3_pending | NO — per-candidate signal collapses to uniform on z_world-degenerate candidates |
| MECH-314b (broadcast uncertainty) | mechanism_hypothesis | candidate_substrate_landed, v3_pending | **Expected n/a** — Phase 1 broadcast scalar by design; cannot change selection ordering under its own ablation. 604 surfaces the declared Phase 1 honest-scoping caveat. |
| MECH-314c (broadcast learning progress) | mechanism_hypothesis | candidate_substrate_landed, v3_pending | **Expected n/a** — same as 314b |
| Q-043 | open_question | open, v3_pending | NO — curiosity dimension fully degenerate; noise dimension N=1-per-cell, governance can't read |
| ARC-065 | architectural_commitment | candidate, v3_pending | NO — neither child substrate can be load-bearing-tested while V3 substrate produces candidate-degenerate scoring AND seeds 42/44 die at random-init |
| MECH-313 | mechanism_hypothesis | candidate_substrate_landed, v3_pending | Partial — 605 alpha-row sweep produces real (sub-threshold) entropy lifts; consistent with 603 chain |

### 5. Biological-reference triage

- **MECH-314a** (ventral striatum novelty bonus): Wittmann 2008; Bellemare 2016; Burda 2018. Biology is per-state and per-candidate; the V3 implementation requires non-degenerate candidates to produce a per-candidate output. **Divergence: none.**
- **MECH-314b** (frontopolar uncertainty) and **MECH-314c** (learning progress / compression): Daw 2006; Friston 2010/2015; Schmidhuber 1991; Pathak 2017. Phase 1 broadcast-scalar implementation deliberately omits per-candidate refinement (Phase 2 follow-on). Surfacing ARM_2 == ARM_0 / ARM_3 == ARM_0 is the **declared Phase 1 honest-scoping caveat** in each claim's evidence_quality_note. Recording 604 as weakening evidence would over-state.
- **Q-043, MECH-313**: covered in Cluster A triage.
- **Biology divergence: none across the cluster.**

### 6. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact for Q-044/MECH-314a/Q-043/ARC-065; **test-design issue for MECH-314b/c** | 604 ablation cannot in principle weaken 314b/c — declared broadcast |
| Biological reference | clear | All claims well-anchored; no divergence |
| Prerequisites | **missing × 2** | (1) goal-pipeline substrate (Cluster A); (2) per-candidate z_world variance substrate (SD-056, in flight as V3-EXQ-569a) |
| Implementation completeness | partial (MECH-314b/c by design); complete (MECH-314a, MECH-313) | 314b/c Phase 2 (per-candidate refinement) is the missing implementation for them to be ablation-testable |
| Environment adequacy | inadequate for discrimination | Same as Cluster A |
| Measurement adequacy | misleading for MECH-314b/c; adequate for the others | 604 design conflates broadcast-by-design with non_contributory FAIL |
| Integration adequacy | isolated; **per-candidate variance does not propagate from E2 → hippocampal scoring → E3 aggregation** | SD-056 explicitly addresses this propagation gap |
| Scale / capacity | likely insufficient | Same as Cluster A |

**Dominant diagnoses (two stacked)**:
1. `substrate_ceiling` — goal-pipeline / training-regime (deep; shared with Cluster A)
2. `substrate_ceiling` — per-candidate z_world variance (proximal for 604 curiosity-cluster; SD-056 in flight)

**Recommended epistemic_category**: `substrate_ceiling`

### 7. Learning extracted

1. Cluster B's failure shape is two substrate gaps stacked, not one. Acknowledging only the goal-pipeline/scaffolded-SD-054 substrate would miss the per-candidate-z_world-variance gap that SD-056 + V3-EXQ-569a are specifically commissioned to close.
2. MECH-314b/c Phase 1 broadcast scalars cannot weaken under their own ablation. The 604 design tested a falsification that is structurally impossible on the Phase 1 substrate. Their `non_contributory` direction is correct but **not evidence of a substrate ceiling specific to those claims** — it's an experiment-design / Phase-scoping mismatch already declared on file.
3. MECH-313 noise-floor accumulates consistent sub-threshold directional support across three independent substrate designs now (603 chain target env + 605 curiosity-grid env). N=1 per cell prevents governance reading; the cumulative directional consistency is evidentially loaded — flag for governance.
4. MECH-314a (novelty) is the load-bearing per-candidate bonus in the structured-curiosity cluster; its untestability under 604/605 is the proximal evidence V3-EXQ-569a will read. PASS unlocks MECH-314a + Q-044 retest; FAIL means the per-candidate-variance gap is deeper than SD-056 and goal-pipeline substrate prereq dominates.
5. Two-substrate-prereq stack makes retest sequence explicit: V3-EXQ-569a (SD-056) first, then SD-XXX-scaffolded-sd054-onboarding lands, then Q-044 + Q-045 + Q-043 multi-substrate retest under a working policy. Until 569a PASSes, Q-044 cannot be tested even with scaffolded onboarding.

### 8. Confirmed routing (user 2026-05-29 interactive gate — Fork A)

- V3-EXQ-604 → **amend** SD-XXX-scaffolded-sd054-onboarding (failure_record_entry + flag SD-056 / V3-EXQ-569a as proximal retest in evidence_quality_note)
- V3-EXQ-605 → **amend** SD-XXX-scaffolded-sd054-onboarding (failure_record_entry + cumulative MECH-313 directional signal note)
- MECH-314b/c get a narrower Phase 1 honest-scoping evidence_quality_note (no substrate routing, no weakening tag)
- SD-056 does NOT get a separate substrate_queue entry (already tracked under `behavioral_diversity_isolation_plan.md` GAP-A with V3-EXQ-569a as the active falsifier)

### 9. Draft `evidence_quality_note` additions for `/governance`

**Q-044** (append):
```
[2026-05-29 autopsy V3-EXQ-604 + V3-EXQ-605 cluster]: untestable on V3 default substrate
due to candidate-uniform z_world (no per-candidate variance from E2 forward-model output).
MECH-314a per-candidate novelty bonus collapses to uniform across degenerate candidates
-> ARM_1 (novelty-off) == ARM_0 (all-on) bit-identical per seed. MECH-314b/c are
broadcast-by-design (Phase 1 honest-scoping caveat already on file). Two-substrate-prereq
stack: SD-056 e2_action_conditional_divergence_contrastive (proximal; landed 2026-05-29
ree-v3 main 041a974; V3-EXQ-613 PASS; V3-EXQ-569a falsifier queued) AND
SD-XXX-scaffolded-sd054-onboarding (deep; parent 490g-cohort autopsy commit 12f0dda773).
Both must close before Q-044 retest is meaningful; SD-056 first via V3-EXQ-569a.
```

**MECH-314** (append):
```
[2026-05-29 autopsy V3-EXQ-604 + V3-EXQ-605 cluster]: parent claim; sub-flavour ablations
cannot discriminate without per-candidate z_world variance. Same two-substrate-prereq
stack as Q-044.
```

**MECH-314a** (append):
```
[2026-05-29 autopsy V3-EXQ-604 + V3-EXQ-605 cluster]: per-candidate novelty bonus collapses
to uniform across z_world-degenerate candidate sets, making ARM_1 (novelty-off)
bit-identical to ARM_0 (all-on) per seed in 604. NOT a substrate ceiling specific to the
novelty mechanism -- it's the upstream per-candidate-variance gap. SD-056
substrate-readiness PASS (V3-EXQ-613) and behavioural validation (V3-EXQ-569a, queued
today) are the proximal retest path.
```

**MECH-314b** (append, narrow):
```
[2026-05-29 autopsy V3-EXQ-604 cluster]: ARM_2 (uncertainty-off) == ARM_0 (all-on)
bit-identical per seed in 604 is the declared Phase 1 broadcast-scalar honest-scoping
caveat surfacing under ablation, NOT a substrate ceiling specific to this claim.
Per-candidate refinement (Phase 2 follow-on) is the architectural work that makes 314b
independently ablation-testable. No demotion or supports tagging warranted from V3-EXQ-604.
```

**MECH-314c** (append, narrow):
```
[2026-05-29 autopsy V3-EXQ-604 cluster]: same as MECH-314b -- ARM_3 (lp-off) == ARM_0
(all-on) bit-identical per seed is the Phase 1 broadcast-scalar caveat surfacing under
ablation, NOT a substrate ceiling. Phase 2 per-candidate refinement is the prerequisite
for ablation-testability.
```

**Q-043** (append):
```
[2026-05-29 autopsy V3-EXQ-605 cluster]: calibration grid untestable on V3 default
substrate -- curiosity dimension fully degenerate (curiosity_scale {1x, 5x, 10x} produces
identical per-cell entropy + reef_fraction); noise dimension delivers sub-threshold
signal but N=1 per cell. p1_any_calibration_zone=false stays. Same two-substrate-prereq
stack as Q-044 (SD-056 proximal, SD-XXX-scaffolded-sd054-onboarding deep).
```

**ARC-065** (append):
```
[2026-05-29 autopsy V3-EXQ-605 + V3-EXQ-604 cluster]: foundational architectural slot;
neither child substrate (MECH-313 noise / MECH-314 curiosity) can be load-bearing-tested
while V3 substrate produces candidate-degenerate scoring AND seeds 42/44 die on the
target env at random-init. ARC-065 stays candidate pending the two-substrate-prereq close
(SD-056 via V3-EXQ-569a + SD-XXX-scaffolded-sd054-onboarding via implement-substrate
session). Priority-1 calibration debt per project_calibration_debt.md.
```

(MECH-313 note is recorded once under Cluster A Section 9; it covers both 603-chain and 605.)

---

## CROSS-CLUSTER OBSERVATIONS

1. Both clusters route to the same `SD-XXX-scaffolded-sd054-onboarding` substrate entry (created by parent 490g-cohort autopsy commit `12f0dda773`). This autopsy adds four new `failure_record_entries` (603a, 603b, 604, 605) and confirms the parent disposition for 603c.
2. MECH-313 cumulative sub-threshold directional signal attested across three substrate designs now (603 + 603a/b on the 4-arm target env, 605 on the 3×3 noise/curiosity grid env). N=1 per cell prevents governance reading individually; the cross-substrate convergence is evidentially loaded — re-evaluate once substrate-fixed retests deliver N>=2.
3. MECH-314b/c surfacing in 604 is a Phase 1 honest-scoping caveat under ablation, NOT a substrate ceiling specific to those claims. Recording it as weakening evidence would over-state.
4. Calibration-debt lens: ARC-065 priority-1 confirmed. The 591 autopsy substrate prereq #2 + 490g-cohort autopsy + this two-cluster autopsy + SD-056 substrate-readiness + V3-EXQ-569a falsifier together cover the goal-pipeline + per-candidate-variance gap. No new work items beyond the four failure_record_entries.

---

## ROUTING SUMMARY (for /governance)

| Run | Routing | Substrate action | New evidence_quality notes |
|---|---|---|---|
| V3-EXQ-603a | implement-substrate (parent) | amend SD-XXX-scaffolded-sd054-onboarding (failure_record) | MECH-260, MECH-313, Q-045 |
| V3-EXQ-603b | implement-substrate (parent) | amend SD-XXX-scaffolded-sd054-onboarding (failure_record) | (covered above) |
| V3-EXQ-603c | implement-substrate (parent) | none (490g-cohort autopsy commit 12f0dda773 already created the entry) | (covered above; confirmation only) |
| V3-EXQ-604 | implement-substrate (parent) + flag SD-056 / V3-EXQ-569a proximal | amend SD-XXX-scaffolded-sd054-onboarding (failure_record + proximal note) | Q-044, MECH-314, MECH-314a, MECH-314b, MECH-314c |
| V3-EXQ-605 | implement-substrate (parent) + cumulative MECH-313 signal flag | amend SD-XXX-scaffolded-sd054-onboarding (failure_record + cumulative-signal note) | Q-043, ARC-065 (MECH-313 covered) |

`/governance` applies these recommendations interactively. The five run_ids should be added to `reviewed_run_ids` once the application pass completes.
