# Failure Autopsy -- V3-EXQ-700 (+ sibling 700a): ARC-108 sec-7 learned-gating cluster

- **Generated (UTC):** 2026-06-23T16:58:45Z
- **Scope:** cluster (V3-EXQ-700 C1/C2 + V3-EXQ-700a C3 ablation)
- **Status:** confirmed (user-adjudicated 2026-06-23)
- **Claims tagged:** MECH-439 (F-dominance conversion ceiling; candidate / substrate_ceiling), ARC-108 (dopamine-gated learned selection; candidate / substrate_conditional), MECH-450 (recurrent settling step; candidate / substrate_conditional)
- **Outcome (both):** FAIL -- self-route `substrate_not_ready_requeue` -- evidence_direction `non_contributory` (all 3 claims)
- **Machine:** ree-cloud-3

---

## 1. Facts -- reconstruction (no interpretation)

Both runs: 3 seeds (42/43/44) x 5 arms, phased P0/P1/P2 = 100/50/100 ep x 200 steps, on the reef-bipartite foraging env (size 12, hazard_food_attraction 0.7). The **arithmetic envelope is a matched constant on all arms** (use_f_eligibility_demotion + adaptive_floor 689e + go_nogo_constitution 689g + modulatory-authority/top_k shortlist 569i); the only toggled flags are the learned levers.

### V3-EXQ-700 -- C1 conversion + C2 learning-load-bearing 2x2
`use_learned_channel_gating` {OFF,ON} x `use_learned_settling_step` {OFF,ON}; ARM_NOISE = verified-lifting matched-noise temperature control. PRIMARY DV = committed-action-class entropy.

Preconditions: 4 of 5 MET.

| precondition | measured | threshold | met |
|---|---|---|---|
| candidate_pool_divergent_all_arms | 0.0279 (seed-43 value) | 0.05 | True (2/3 majority) |
| committed_class_axis_exercisable | 1.0 | 0.3 | True |
| delta_t_carries_variance (armed arms) | 5.06e-4 | 1e-4 | True |
| learned_weights_moved (armed arms) | 1.3e-3 | 1e-4 | True |
| **matched_noise_control_verified_lifting** | **1.0 (=1/3 seeds)** | **2.0 (=2/3)** | **False** |

C1 (conversion) = false; C2 (learning grows) = false. The self-route is driven by the single unmet precondition (the noise bar).

Per-arm mean committed-class entropy: A0 0.935 / A1 (w_chan) 0.963 / A2 (settling) 1.029 / A3 (both) 1.033 / NOISE 0.986.

Per-seed (the load-bearing detail):
- **seed 42 (divergent):** A0 1.10, A1 1.17 (+0.07), **A2 1.35 (+0.25), A3 1.36 (+0.26)**, NOISE 1.25. Settling beats noise; w_chan below noise.
- **seed 44 (divergent, flat):** A0 1.03, A1/A2/A3 ~1.04-1.05 (+0.01-0.02 < 0.05 margin), NOISE 1.03. No arm converts.
- **seed 43 (DEGENERATE):** pool dist 0.028 < 0.05 (gapa_divergence=False); committed entropy 0.6799 **byte-identical** across A0/A1/NOISE (2-class lock); ran ~9x more ticks (n_p0 18705 vs ~2000). Learning has nothing to convert.

### V3-EXQ-700a -- C3 signed-vs-unsigned-RPE ablation (new `learned_channel_rpe_mode` flag)
Arms A0 / A1_SIGNED / C3_A1_UNSIGNED / ARM_NOISE. **Two** preconditions unmet: `candidate_pool_divergent_all_arms` (0.020 < 0.05; pool collapsed on the majority) AND `matched_noise_control_verified_lifting` (**0/3 lifts**). C3b (unsigned arm fails to convert) passed=True; C3a (signed converts) unscoreable on the unverified bar. The unsigned ARC-016-variance signal moved w_chan range **0.66** vs the signed RPE **0.0013** (one-directional, ~500x harder).

---

## 2. Claim-layer mapping

The experiment did **not** test the claims under conditions where they could express themselves -- the conversion DV was gated behind a non-vacuity precondition (verified noise bar) that failed, and one/most seeds had a collapsed (non-divergent) candidate pool. So no claim is weakened. `claim_ids` are correct (MECH-439 = the conversion ceiling under attack; ARC-108/MECH-450 = the learned levers being tested as the lift).

---

## 3. Biological-reference triage

- **ARC-108** -- faithful translation of basal-ganglia **three-factor dopaminergic plasticity** (cortico-striatal eligibility x signed RPE, D1-LTP/D2-LTD asymmetry). Not a formal import. Lit present (`targeted_review_connectome_mech_439`).
- **MECH-450** -- faithful translation of **BG/pallidal recurrent winner-take-most settling** (Mink surround inhibition). Not a formal import.
- **Missing-dependency signature?** Yes, latent: biological BG action selection runs over **multiple parallel cortico-BG-thalamic loops** (loop segregation). A single-arena foraging test cannot exercise loop-segregated diversity. *If* conversion genuinely fails to lift on a VERIFIED bar, that single collapsed arena is the binding constraint -> the grid's own `FAIL_no_lift...escalate_v4_full_loop` branch, not a falsification. We are not there yet (the bar was unverified).

---

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | conversion could not express (unverified bar + degenerate seed) |
| Biological reference | clear | faithful three-factor DA plasticity + recurrent settling; lit present |
| Prerequisites | present | ARC-108/MECH-450 built + engaged; divergent pool present on non-degenerate seeds |
| Implementation | complete-and-engaged | w_chan + W_lat move; delta_t variance; settling moves the field (round-delta 0.15-0.58) -- NOT symbol-only |
| Environment | adequate-but-brittle / latent suspect | reef-bipartite collapses to non-divergent 2-class lock on degenerate seeds; single arena is the latent V4 binding constraint |
| Measurement | **misleading / under-instrumented (dominant)** | noise control alpha=1.0 does not verify-lift (700 1/3, 700a 0/3); no per-seed-divergent gating -> one degenerate cell drags every >=2/3 criterion |
| Integration | coupled | learning composes inside the F-bounded MECH-448/449 eligible set |
| Scale | adequate | 3 seeds x 5 arms x 100/50/100 ep; gap is seed-screening + noise tuning, not budget |

**Dominant diagnosis:** measurement / test-design ceiling on the harness. Recommended `epistemic_category`: **NO CHANGE** (MECH-439 stays substrate_ceiling; ARC-108/MECH-450 stay substrate_conditional). Recommended `evidence_direction`: `non_contributory` (matches the self-route).

---

## 5. Cluster pattern

| Experiment | Claims | Negative-control / readiness | Discrimination criteria | Read |
|---|---|---|---|---|
| V3-EXQ-700 (C1/C2) | MECH-439/ARC-108/MECH-450 | noise bar 1/3 lift (UNVERIFIED); seed-43 pool collapsed | C1/C2 false | substrate_not_ready_requeue |
| V3-EXQ-700a (C3) | MECH-439/ARC-108/MECH-450 | noise bar 0/3 lift; pool collapsed on majority | C3a unscoreable / C3b passed | substrate_not_ready_requeue |

**One structural property, not two bugs:** a brittle test harness on a single foraging arena -- (1) the matched-noise control does not verify-lift (the recurring 569g/684 unverified-bar defect), and (2) the candidate pool collapses to a non-divergent monostrategy on degenerate seeds while the all-3-seeds-must-clear >=2/3 design has no per-seed-divergent gating. This is a measurement ceiling on the harness, **not** a substrate ceiling on the claims and **not (yet)** a confirmed no-lift.

---

## 6. Re-derive brake

MECH-439 has **3** prior `non_contributory`/`substrate_ceiling` autopsies (689, 689a, f-dominance-cluster); this is the **4th** (threshold 2) -- mechanically tripped. **Brake EXEMPT (user-adjudicated 2026-06-23), `fired: false`**, because:
1. The substrate was **genuinely enriched** between the prior autopsies and this run -- ARC-108 + MECH-450 are new builds (2026-06-20/22). (The explicit "substrate genuinely being enriched between letters" exemption.)
2. 700 tests a **different mechanism** (learned w_chan/W_lat) under a **new EXQ number**. (The explicit "redesign of a different mechanism" exemption.)
3. The re-queue (700b) is a **test-design/measurement fix**, not another iteration of the same lever circling the same ceiling.
4. The learning machinery engaged and produced a single-seed conversion signal.

**HARD STOP / decisive-or-escalate:** 700b is decisive. If it shows **no conversion with a VERIFIED noise bar + per-seed-divergent gating**, the `no_lift -> escalate_v4_full_loop` branch fires and the campaign moves to V4 loop-segregation -- **NOT another V3 letter**. The brake's intent is honoured at that point. ARC-108=1, MECH-450=0 (below threshold).

---

## 7. Learning extracted + routing

- ARC-108 (w_chan) + MECH-450 (W_lat) are implemented-and-engaged end-to-end -- positive readiness confirmation.
- **On the one clean divergent seed (42), the learned SETTLING (MECH-450 W_lat) is the lever that converts** (+0.25 over A0, beats noise), not channel re-weighting (ARC-108 w_chan +0.07, below noise). Focus the retest on settling.
- The matched-noise control alpha=1.0 does not verify-lift on this env -- the C1 bar must be made verified before a conversion FAIL can be trusted.
- The all-3-seeds-must-clear >=2/3 design is brittle to a single degenerate non-divergent cell -- per-seed-divergent gating (interpret only divergent-pool seeds, the 701a per-seed-gate pattern) is required.
- The unsigned-RPE C3b observation (unsigned moves w_chan ~500x harder, one-directional) is consistent with the B5 prediction but unscoreable here; fold C3 into 700b.

**Routing:** `/queue-experiment` (700b) -- a test-design fix (user-confirmed scope = **full harness fix + focus settling**): (a) re-tune the matched-noise alpha so it verify-lifts; (b) per-seed-divergent gating (interpret C1/C2/C3 only on seeds where the pool is divergent); (c) more seeds (5-6) for a robust divergent-seed count; (d) narrow toward the settling arm (A2/A3) and drop/down-weight the w_chan-only arm (A1, lifted below noise); (e) fold the C3 signed-vs-unsigned ablation into the same retest. `recommended_substrate_queue_entry.action = none` (no substrate build; the substrate is built + engaged). MECH-439 stays substrate_ceiling; ARC-108/MECH-450 stay substrate_conditional; `pending_retest_after_substrate`. **PROMOTES NOTHING, WEAKENS NOTHING.**

---

## 8. Draft `evidence_quality_note` (for governance to write -- do not write here)

See the two `recommended_evidence_quality_note` fields in `failure_autopsy_V3-EXQ-700-cluster_2026-06-23.json` (one per run); both record non_contributory + substrate_not_ready_requeue + the 700b decisive-or-escalate plan.
