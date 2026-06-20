# Failure Autopsy -- V3-EXQ-690 (Q-054 ARC-062 diversity-floor sweep)

- **Generated (UTC):** 2026-06-20T12:01:52Z
- **Scope:** single (a member of the f-dominance committed-action conversion cluster)
- **Status:** confirmed (interactive, user-ratified at the Step-8 gate 2026-06-20: "Confirm as recommended")
- **Target:** `v3_exq_690_q054_arc062_diversity_floor_sweep_20260620T105823Z_v3` (V3-EXQ-690)
- **Claim:** `ARC-062` (rule-apprehension architectural slot, weak reading; candidate / substrate_ceiling / v3_pending / pending_retest_after_substrate)
- **Self-route under adjudication:** `substrate_not_ready_requeue`, `non_contributory`, `non_degenerate=false`
- **Cross-ref:** `failure_autopsy_f-dominance-conversion-cluster_2026-06-20` (this 690 is the diversity-floor-sweep instance of the same convergent fingerprint); substrate entry `f_dominance_conversion_ceiling`

---

## 1. Facts (no interpretation)

The sweep graded the MECH-313 noise-floor `min_temperature` across 4 arms (`0.30 / 1.00 / 1.75 / 2.75`), `noise_floor_alpha` held at `0.0`, with the 569i top-k shortlist conversion stack armed **identically** on every arm. DV1 = ARC-062 reef-vs-forage discriminator balanced accuracy (gating_weight cut); DV2 = TV(P(a|s_reef), P(a|s_forage)); x-axis = MEASURED realised committed first-action entropy per arm. 3 seeds (42/43/44) x 4 arms = 12 cells, all completed.

**The decisive fact:** every arm is **byte-identical per seed**.

| seed | realised_first_action_entropy (all 4 arms) | disc balanced acc (all 4 arms) | TV (all 4 arms) | n reef ticks | context_scorable | r3 nondegenerate |
|---|---|---|---|---|---|---|
| 42 | 0.285896 | 0.823767 | 0.048978 | 271 | true | true |
| 43 | 0.652856 | 0.899025 | 0.807295 | 8909 | true | false (gw_range 0.00042) |
| 44 | 0.728731 | 0.500000 (chance) | 0.000000 | 0 | false | false |

A `0.30 -> 2.75` (>2.75x) change of `noise_floor_min_temperature` moved **nothing** in any metric on any seed.

**Readiness gates (the self-route drivers):**

- **R1** realised committed first-action entropy *RANGE across the 4 arms* = **0.0** (< 0.2 floor) -> **FAIL**.
- **R2** top-k shortlist engaged (shortlist active, mode `top_k`, mean size 3.0 on all 4 arms) -> **met**.
- **R3** discriminator non-degenerate (gating_weight cross-tick range AND both reef+forage contexts sampled, on a majority of arms) -> **0/4 arms** -> **FAIL**.

Per the script's pre-registered branch: R1/R3 unmet -> `substrate_not_ready_requeue` (explicitly NOT a floor verdict, NOT an ARC-062 falsification).

## 2. Why the lever was inert (code-confirmed)

`NoiseFloor.compute_effective_temperature`: `effective_T = max(baseline_T + alpha, min_temperature)`. With `alpha=0.0` and `base_select_temperature=1.0`:

- min_temp 0.30 -> `max(1.0, 0.30) = 1.0` (no lift)
- min_temp 1.00 -> `max(1.0, 1.00) = 1.0` (no lift)
- min_temp 1.75 -> `max(1.0, 1.75) = 1.75` (**lift applied**)
- min_temp 2.75 -> `max(1.0, 2.75) = 2.75` (**lift applied**)

So the temperature *was* lifted on ARM_T_MID and ARM_T_HIGH -- yet the committed metrics are byte-identical. The committed first action is selected by the MECH-090 committed-trajectory **argmin** over the F-dominated scores (`committed_trajectory.actions[:, 0, :]`), which is temperature-invariant; the noise-floor temperature only spreads the *uncommitted* multinomial. A selection-softmax temperature floor therefore **cannot move committed first-action entropy** -- the script's header assumption ("...so it directly raises REALISED committed first-action entropy (the committed / uncommitted multinomial)") is the design error.

The per-seed entropy that *does* exist (0.29 / 0.65 / 0.73 nats) comes from the seed's reef/forage environment trajectory (different reef-tick mix), **not** from the swept lever. So R1=0.0 is *between-arm lever inertness*, distinct from a *within-seed monostrategy collapse* (seed 42 commits 5 distinct first-action classes).

## 3. Claim-layer mapping -- ARC-062 is NOT weakened

ARC-062 is the gated-policy 3-stream context discriminator. The data shows the discriminator **works above chance where context is exposed**: balanced accuracy 0.74 mean, 0.82 (seed 42) and 0.90 (seed 43) on the two seeds that sampled reef. The R3 degeneracy is purely environmental sampling: seed 44 never visited a reef tick (`n_reef_ticks=0`, `context_scorable=false`, discriminator at chance), and seed 43 was reef-dominated with a tiny gating_weight range. Only seed 42 had a balanced split AND `gating_weight_range > 0.001`.

So the FAIL says nothing against ARC-062's mechanism. The experiment never delivered the upstream entropy variation its Q-054 floor verdict reads against, so the floor question was untestable -- a `substrate_not_ready_requeue`, exactly as self-routed.

## 4. Biological-reference triage

Same as the cluster: the closest reference is the BG action-selection bottleneck with the **hyperdirect (cortico-STN) conflict-graded hold** -- the mechanism that, in real brains, lets a non-dominant stream change the committed action at near-ties by widening the eligible set (Frank 2006; Cavanagh/Cohen/Frank 2011; grounded in `targeted_review_connectome_mech_439`). The MECH-313 noise floor is a faithful LC-NE tonic-temperature translation but the **wrong lever** for the committed-argmax question: it spreads the softmax sample, it does not bound the eligible set. The architecturally-correct lever (569i top-k / 689a conflict-graded width) bounds the set so F gates eligibility only.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **intact** | ARC-062 discriminator above chance where context sampled (0.74 mean); never got a fair floor-test. NOT weakened. |
| Biological reference | clear | BG bottleneck + missing hyperdirect conflict-graded hold (cluster reference). |
| Prerequisites / dependency | **missing (shared)** | conflict-graded committed-selection lever (689a, BUILT, in flight) + a committed-argmax-reaching lever in place of the temperature floor. |
| Implementation | complete but **lever-target-mismatched** | MECH-313 fully wired; it lifts the selection-softmax temperature (argmin-invariant for the committed first action) -> inert for the swept DV. |
| Environment | adequate -> wrong-pressures (conditional) | per-seed reef exposure uncontrolled (seed 44 = 0 reef ticks) -> R3 lost to sampling, not ARC-062. |
| Measurement | adequate | R1 range-across-arms correctly caught the inert lever; readiness self-routed instead of emitting a false floor verdict. |
| Integration | coupled, **ceiling at the argmax** | temperature reaches the softmax but cannot move the F-dominated committed argmin. |
| Scale | n/a | -- |

**Recommended `epistemic_category`:** `substrate_ceiling` (ARC-062 already carries it; UNCHANGED).

## 6. The two live readings (which planning decision they force)

Inherited from the cluster; 689a is the experiment that discriminates them:

- **Reading 1 -- substrate-enrichment.** The 689a conflict-graded shortlist lifts committed-action-class entropy strict-above the gap-blind controls; the ceiling lifts; 690a (re-armed with the committed-reaching lever) then reads a real Q-054 floor.
- **Reading 2 -- test-design ceiling.** Near-ties levers cap committed entropy below the proposer ceiling; the real target is direct rank-preserving F->eligibility demotion, and the floor question's lever must change accordingly.

690 does not force the choice -- it confirms the same E3-committed-argmax bottleneck under a 4th lever and remains gated on the SAME 689a keystone.

## 7. Routing (user-ratified 2026-06-20)

**non_contributory + pending_retest_after_substrate.** ARC-062 stays `candidate / substrate_ceiling / v3_pending / pending_retest_after_substrate`, **UNCHANGED**.

**implement-substrate -- substrate_queue `amend`.** Append V3-EXQ-690 as a failure_record on the existing `f_dominance_conversion_ceiling` entry (ARC-062 already in `unblocks_claims`; 689a remains the keystone). No new substrate entry.

**Requeue 690a, gated on V3-EXQ-689a, NOT on the current selector.** The 690a redesign must:
1. **Sweep a committed-argmax-reaching lever** (569i top-k `k` / 689a conflict-graded shortlist width) for the Q-054 floor question, instead of the MECH-313 selection-softmax temperature (re-running on the current lever reproduces R1=0.0).
2. **Control per-seed reef/forage exposure** (or gate the discriminator readout on `context_scorable`) so R3 is not lost to environmental sampling.

**689a is in flight -- do NOT touch it.** Coordinator DB (2026-06-20T12:01Z): `status=claimed`, `DLAPTOP-4.local`, claimed 2026-06-19T20:25Z, **no results row**. Per `feedback_heartbeat_stale_not_abandoned` and the 2026-06-20 morning assessment (running, ~4h left) this is a live local run, not abandoned. The 690a gate sequences behind whatever 689a yields; this autopsy makes no release/re-queue recommendation about 689a.

**Draft `evidence_quality_note`** (governance writes verbatim to the 690 manifest / for the substrate entry): see the JSON sibling `recommended_evidence_quality_note`.

## 8. Learning extracted

1. A selection-softmax TEMPERATURE floor (MECH-313) is architecturally incapable of moving a deterministic committed ARGMIN regardless of F-dominance -- the Q-054 sweep used a lever that cannot reach the committed first action it measures.
2. The F-dominance ceiling has two faces: within-seed monostrategy (625e `{0:4000}`) and between-arm lever-inertness (690 byte-identical arms). 690 is the latter -- committed entropy is non-zero per seed but invariant to the lever.
3. ARC-062's discriminator is intact and above-chance where context is sampled; R3 degeneracy is uncontrolled per-seed reef exposure, so 690a must guarantee balanced reef/forage exposure independent of the F-dominance gate.
4. 690 adds no independent root -- it is the diversity-floor-sweep member of the f-dominance cluster, confirming the same E3-committed-argmax bottleneck under a 4th lever, still blocked on the SAME 689a keystone.

## 9. Granularity-debt recurrence note

ARC-062 appears in many prior autopsy docs, but as a *channel claim gated behind a downstream ceiling it does not own* (the f-dominance cluster already adjudicated this as one structural property, not granularity debt; the MECH-439 decomposition discharges the divergent-signature debt). 690 reinforces that reading rather than opening new debt: it is a fourth lever drowning at the same F-dominated argmin. No `/claim-synthesis` escalation owed beyond the already-flagged MECH-439 decomposition (`claim_synthesis_MECH-439_2026-06-20`).
