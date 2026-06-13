# Failure Autopsy -- V3-EXQ-655 (INV-074 crystallization necessity, TASK-SHIFT redesign)

- **Generated (UTC):** 2026-06-13T10:02:38Z
- **Scope:** single
- **Status:** confirmed (user adjudicated 2026-06-13: route = STOP cascade / accept substrate_ceiling)
- **Run:** v3_exq_655_inv074_crystallization_necessity_taskshift_20260613T070430Z_v3
- **Queue:** V3-EXQ-655 (supersedes V3-EXQ-610f, and transitively the 610a-f noise-only lineage); backlog EVB-0270
- **Outcome:** FAIL; manifest evidence_direction=unknown (all 5 claims) -> non-standard, routed to autopsy by the 2026-06-13 AM governance cycle
- **Claims tagged:** INV-074, MECH-333, MECH-334, MECH-341, MECH-313
- **Purpose:** evidence
- **Lineage:** 543h/i/k/l + 610a-d (harness no-op, RESOLVED) -> 610e (first behaviourally-live; ARM_0 confound) -> 610f (ARM_0 stripped to a true negative; D2 FAIL under NOISE) -> **655 (the pre-registered route-(a) redesign: noise-only phase-3 replaced with a genuine TASK-DISTRIBUTION SHIFT)**

## Thesis

655 is the **decisive substrate-incapacity experiment** the 610f autopsy set up. 610f re-FAILed D2 (the
stripped REINFORCE control did not collapse) under an IGW-023 *noise* phase-3, leaving two live readings:
(a) noise simply was not the right destabilising pressure, or (b) the V3 REINFORCE-on-grid substrate cannot
exhibit catastrophic plasticity collapse at all. The user routed **one task-shift redesign, decisive either
way** (2026-06-08). 655 implements exactly that -- phases 0-2 unchanged, only the phase-3 environment swapped
to a genuine conflicting-task shift (SD-054 `reef_bipartite_layout` + `hazard_food_attraction=0.8`: foraging
the top half becomes lethal, the only viable policy is flee-to-reef, a single dominant first-action class that
*conflicts* with the phase-0-2 forage-diverse optimum).

**The stripped control STILL did not collapse** (D2 delta 0.0654 < 0.10; threshold map 0.065-0.080 across all
phase-3 entropy weights, no floor load-bearing). Per 655's own interpretation-grid **branch (ii)** and the
610f pre-registration, this **confirms reading (b)**: INV-074's V3-applicability is genuinely blocked. This is
NOT a falsification of a universal invariant grounded in a working biological existence proof -- it is the
decisive-with-evidence confirmation that the V3 substrate is too coarse to instantiate the necessity premise.

## Adjudicating the three candidate readings (degenerate / bug / genuine-null)

The three symptoms flagged at intake resolve as follows:

1. **"All five arms identical at 0.7940 at phase 2 -> zero cross-arm differentiation" -> BY DESIGN, not degeneracy.**
   The crystallize-vs-control manipulation fires only at Phase-3 entry (`_on_phase3_entry_closure`). Phases 0-2
   are bit-identical across all five arms (same seed, `entropy_bonus_train=0.02` everywhere), so per-seed
   phase-2 endpoints MUST be identical across arms. This is precisely what the **D3 non-vacuity sanity gate
   checks**, and D3 PASSed (`d3_sanity_both_show_diversity_at_phase2=true`). The discriminative axis is phase
   **3**, not phase 2.

2. **"Aggregate 0.794 vs per-seed 0.233 -> aggregation/normalisation mismatch" -> REFUTED, mean-vs-single-seed.**
   `arm_N_end_phase_2_entropy=0.79396` is the **seed-mean** (`_arm_mean` averages seeds 42/43/44 =
   (0.23336 + 1.04046 + 1.10805)/3 = 0.79396). The 0.23336 is seed-42 alone. No bug. Checked on the substantive
   axis too: per-seed **D1** (ARM_1 crystallize - ARM_0 control at phase 3) = {42: -0.0211, 43: -0.0077,
   44: +0.0268}, mean -0.00065 -- sign-inconsistent and ~0 even **paired per-seed**, so the seed-mean is not
   masking a real effect. The crystallization effect on action entropy is genuinely zero.

3. **The real result.** The crystallization machinery DID fire (`ewc_penalty_last` 1938/315/563 across seeds,
   `n_ewc_terms_phase3=499`, `n_expansion_steps_phase3=499`, 1249 expansion params) yet produced D1 = -0.00065.
   The precondition **D2 (control collapses) FAILED** (delta 0.0654 < 0.10). D4 (MECH-341/313 floor) = **0.0
   exactly** -- ARM_4 (floors-on control) is bit-identical to ARM_0, so the diversity floor was also inert.

**Verdict: (a) non-discriminative test -> substrate-ceiling.** NOT (b) a measurement/aggregation bug (the
phase-2 cross-arm identity is by design; the aggregate is the correct seed-mean). NOT (c) a genuine null /
falsification (the test could not instantiate INV-074's necessity premise even under a genuine task-shift).

## Facts (no interpretation)

`fix_verification`: fix1_policy_trained=true (init_entropy 0.9166 -> trained 0.9443; below the untrained band
1.04), fix2_expansion_stepped=true (1249 params), fix3_ewc_penalty_in_loss=true (penalty 0.2227, residue grad
0.891). NOT the harness-no-op lineage.

| Criterion | Rule | Result | Read |
|---|---|---|---|
| **D2** true-negative control collapses | ARM_0.end_p2 - end_p3 >= +0.10 | **FAIL** delta **0.0654** | per-seed {42: 0.108, 43: 0.093, 44: -0.004}; seed-44 never collapsed, mean below floor |
| **D1** crystallization preserves diversity | ARM_1.end_p3 - ARM_0.end_p3 >= +0.10 | FAIL delta **-0.00065** | per-seed {42: -0.021, 43: -0.008, 44: +0.027}; ~0, sign-inconsistent -> nothing preserved |
| **D3** both diverse at phase-2 peak | ARM_0.end_p2 > 0.4 AND ARM_1.end_p2 > 0.4 | **PASS** | non-vacuous; mean phase-2 entropy 0.794 |
| **D4** MECH-341/313 floor preserves diversity | ARM_4.end_p3 - ARM_0.end_p3 >= +0.10 | FAIL delta **0.0** | ARM_4 bit-identical to ARM_0; floor inert; only interpretable when D2 PASS |

Threshold map (control collapse delta end_p2 - end_p3): ARM_0 (eb=0.0) 0.0654; ARM_2 (eb=0.005) 0.0796;
ARM_3 (eb=0.02) 0.0695. **No entropy floor is load-bearing** under the task-shift -- the same convergent
finding as 610f under noise.

Per-seed phase-2 entropy spans 0.233 / 1.040 / 1.108 (std 0.40), so the cross-arm/cross-condition deltas (all
< 0.08) sit well inside the seed-to-seed variance -- the seed-mean aggregation is statistically weak, but the
underlying per-seed deltas confirm the same null, so aggregation is not the cause of the FAIL.

## Claim-layer mapping

| Claim | Type | Status | epistemic_category | Read |
|---|---|---|---|---|
| INV-074 | invariant (universal) | candidate | **substrate_ceiling** | plasticity crystallization necessity; OD critical-period existence proof; lit_conf 0.82. NOT weakened (test could not let it express). |
| MECH-333 | mechanism (v3, v3_pending) | candidate | substrate_conditional | plasticity-injection open-phase channel. unknown -> non_contributory. |
| MECH-334 | mechanism (v3, v3_pending) | candidate | **substrate_ceiling** | EWC residue write-protect. EWC fired (penalty 1938) but D1~0; necessity premise never instantiated -> unknown, NOT weakens. |
| MECH-341 | mechanism (v3, v3_pending) | candidate | (inferred) | E3 score-diversity floor (D4). D4=0 only because D2 failed -> unknown. |
| MECH-313 | mechanism (v3_pending) | candidate_substrate_landed | **substrate_ceiling** | LC-NE noise floor (D4). unknown. |

INV-074, MECH-334, MECH-313 already carry `epistemic_category: substrate_ceiling`. A FAIL here does NOT and
must NOT weaken a universal invariant with a working biological existence proof. Per grid (ii):
{INV-074, MECH-333, MECH-334} = unknown; per grid (v) (D4 FAIL with D2 FAIL): {MECH-341, MECH-313} = unknown.
All five non_contributory.

## Biological-reference triage

Closest mechanism: ocular-dominance critical-period crystallization (Hensch 2005) + plasticity injection
(Nikishin 2023 NeurIPS, MECH-333) + EWC write-protect (Kirkpatrick 2017, MECH-334). Biology CLEARLY supports
the mechanism CLASS -- crystallization of plasticity is a real, necessary property of developing cortex. This
is NOT a formal-definition import; a biology lit entry exists (lit_conf 0.82). The failure resembles "the
destabilising pressure was never strong enough to force catastrophic forgetting" -- a missing
environmental-pressure capacity, not a wrong mechanism. By the autopsy core principle, demotion is off the
table: tested-fairly is NOT satisfied because the V3 substrate cannot instantiate the collapse premise even
under a genuine conflicting-task shift.

## Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | test could not let INV-074 express (D2 precondition unmet, now under a genuine task-shift) |
| Biological reference | clear | OD critical period; plasticity injection; EWC; lit_conf 0.82 |
| Prerequisites | missing | a V3 phase-3 regime that actually induces collapse-without-crystallization (now shown unreachable by task-shift) |
| Implementation | complete | fix_verification: policy trained, expansion stepped, EWC penalty 0.2227 in loss |
| Environment | **substrate ceiling** | conflicting-task shift (reef-bipartite + food-attracted hazards) does NOT force collapse in stripped REINFORCE-on-grid; threshold map shows no floor load-bearing |
| Measurement | adequate but weak | selected_action_entropy non-degenerate, D3 PASS; but seed variance (std 0.40) dwarfs cross-arm deltas, and D2/D4 are 3-seed means |
| Integration | fine | arms isolate cleanly; EWC anchors residue basins, expansion MLP trains freely (designed: plasticity-injection channel) |
| Scale / capacity | insufficient at test-design level | stripped REINFORCE-on-grid does not collapse catastrophically under any phase-3 pressure tried (noise OR conflicting task) |

Dominant locus: **environment / substrate ceiling**. Recommended experiment-level
`recommended_epistemic_category: substrate_ceiling` (consistent with the claims' existing tags).

## The load-bearing signal

This is the **7th iteration** of the necessity test. Across 610a-f (noise) and now 655 (genuine task-shift),
the convergent finding is invariant: **the stripped REINFORCE-on-grid control does not catastrophically
collapse, so the crystallization-necessity discrimination (D1) is structurally unreadable.** The 610f autopsy
named two readings; 655 was the decisive disambiguator and it landed on the substrate-incapacity reading (b)
WITH EVIDENCE, not by assumption: a conflicting-task phase-3 whose optimum is incompatible with phases 0-2
*also* failed to collapse the control.

**Same failure signature, not divergent signatures** -- this is one structural substrate property repeatedly
confirmed, NOT a coarse claim hiding several finer claims. Therefore this is **NOT a `/claim-synthesis`
granularity-debt trigger** despite being a multi-autopsy recurrence; the correct disposition is to STOP the
cascade and rest INV-074 on its biological grounding + existing substrate_ceiling status.

## Learning extracted

1. A genuine task-distribution SHIFT (reef-bipartite + food-attracted hazards, conflicting optimum) is NOT
   sufficient to force catastrophic plasticity collapse in the stripped V3 REINFORCE-on-grid control. This is
   the decisive disambiguator the 610f autopsy queued, and it confirms the substrate-incapacity reading.
2. The crystallization machinery is verified-live (EWC penalty 1938; expansion stepped 1249 params) yet has
   zero effect on policy action entropy -- consistent with there being no collapse to resist, AND with the
   architectural fact that EWC protects residue-field z_world basins while the policy expansion MLP (the
   MECH-333 plasticity-injection channel) trains freely, so "crystallization preserves policy action entropy"
   may be the wrong observable for MECH-334 even if a collapse were induced.
3. Seed variance (std 0.40 at phase 2) dwarfs all cross-arm deltas; per-seed paired D1 confirms ~0, so the
   FAIL is not a seed-mean aggregation artefact.
4. INV-074 as a universal invariant with a working biological existence proof cannot be weakened by a test the
   substrate cannot instantiate. non_contributory is correct for all five claims.

## Instrumentation notes (for the record; only actionable if the cascade is ever re-opened)

- The landed manifest carries **no** `non_degenerate` / `degeneracy_reason` top-level field -- the run executed
  on a script state predating the `check_degeneracy` block, which is why the indexer saw an un-adjudicated
  `evidence_direction: unknown` and routed it to autopsy.
- The `check_degeneracy` block now in the script keys on `cross_arm_phase2_entropy`. Phase-2 cross-arm variance
  is **zero by design** (manipulation is phase-3-only), so that check would emit a **false** degeneracy flag.
  If the 610/655 line is ever revisited, the non-degeneracy axis should be phase-**3** cross-condition (or the
  within-seed phase2->phase3 collapse), not cross-arm phase-2.

## Routing decision (user-confirmed 2026-06-13)

**STOP the 610 necessity-test cascade. Accept INV-074 substrate_ceiling.** No re-queue -- the task-shift was
the decisive disambiguator and it confirmed substrate-incapacity. Governance applies: all five claims
`non_contributory` (NOT weakens), `non_degenerate: false`, `pending_retest_after_substrate`, with the
recommended note below. INV-074 rests on its OD-critical-period biological grounding + existing
substrate_ceiling status. A future retest is unblocked only by a V3 substrate enrichment that can exhibit
catastrophic plasticity collapse (not on any current roadmap item; no substrate_queue entry created).

## Draft evidence_quality_note (governance applies; do not write here)

- **INV-074 / MECH-333 / MECH-334 (655):** "V3-EXQ-655 (7th necessity-test iteration; the pre-registered
  route-(a) redesign replacing the 610f noise-only phase-3 with a genuine TASK-DISTRIBUTION SHIFT -- SD-054
  reef-bipartite + hazard_food_attraction=0.8) re-FAILed D2: the stripped REINFORCE control did NOT collapse
  its action entropy even under a conflicting-task phase-3 (delta 0.0654; threshold map 0.065-0.080, no entropy
  floor load-bearing), so the necessity premise (collapse-without-crystallization) was never instantiated and
  D1 (crystallization preserves) is unreadable (delta -0.00065, sign-inconsistent per seed). Wiring
  verified-live (policy trained, expansion stepped 1249 params, EWC penalty 1938 / 0.2227-in-loss) and D3
  sanity PASS, so this is a genuine substrate-incapacity finding, not a harness no-op or a measurement bug
  (cross-arm phase-2 identity is by design; the aggregate is the correct seed-mean). DECISIVE per the 610f
  pre-registration: a genuine conflicting-task shift also failing to collapse the control confirms reading (b)
  -- the V3 REINFORCE-on-grid substrate cannot exhibit catastrophic plasticity collapse. INV-074 NOT weakened
  (universal invariant; OD critical-period existence proof; lit_conf 0.82); ACCEPT substrate_ceiling and STOP
  the 610 necessity-test cascade. non_contributory; non_degenerate:false; pending_retest_after_substrate (a
  future V3 substrate enrichment that can exhibit catastrophic collapse). User adjudication 2026-06-13."
- **MECH-341 / MECH-313 (655, D4 floor-contrast):** "V3-EXQ-655 D4 (floor preserves diversity) is
  uninterpretable because D2 (control collapse) FAILed -- D4 is only readable when ARM_0 actually collapses,
  and ARM_4 (floors-on) was bit-identical to ARM_0 (delta 0.0). non_contributory; not weakened; carried under
  the same substrate_ceiling disposition; no further re-queue in the 610 cascade."
