# Failure Autopsy — V3-EXQ-485e (trained-OFC-head behavioural; SD-033b / MECH-263)

- **Generated (UTC):** 2026-06-11T14:19:16Z
- **Run:** `v3_exq_485e_sd033b_trained_ofc_head_behavioural_20260611T135223Z_v3`
- **Outcome:** FAIL · `evidence_direction: non_contributory` (both SD-033b and MECH-263)
- **Self-route:** `substrate_not_ready_requeue` — **CONFIRMED**
- **Scope:** single
- **Status:** confirmed (interactive gate answered 2026-06-11; routing = both-axis requeue)

---

## 1. Facts (no interpretation)

The experiment advances the MECH-263 functional signatures (devaluation sensitivity = signature a; perceptually-matched task-role discrimination = signature b) from the representation level (485b/485c, frozen head) to the **behaviour** level on the **trained** OFC head. Behaviour = the candidate-selection distribution the OFC bias induces in isolation, `softmax(-compute_bias(bank) / T)` over a fixed bank of real candidate first-step z_world summaries. OFC is the sole bias channel (gated_policy / dACC / lateral_pfc / modulatory-bias-selection-authority all OFF).

Acceptance (per seed, then ≥2/3): **READINESS** (trained-head bias cross-candidate RANGE > `BIAS_RANGE_FLOOR=0.001` AND head weight-delta > `HEAD_DELTA_MIN=1e-3`); **C1** devaluation_selection_shift > 0.05 beyond the frozen control; **C2** discrimination separation_ratio ≥ 3.0; **C3** frozen-head silent.

Result: `readiness_met=false` (ready_seeds **1/3**) → outcome FAIL, route `substrate_not_ready_requeue`, direction `non_contributory`.

**Per-seed (ARM_1_trainable_head):**

| seed | head Δ | grad≠0 | p1 \|bias\| | clamp | bias range | READY | deval_shift | between_tv | within_jitter | sep_ratio |
|------|--------|--------|-------------|-------|------------|-------|-------------|------------|---------------|-----------|
| 0 | 0.2537 | 60 | 0.00552 | unsat | 0.003497 | **yes** | 8.06e-05 | 3.22e-04 | 4.84e-08 | 322.3 |
| 1 | 0.0753 | 1 | 0.09981 | **@rail** | 0.000491 | no | 1.43e-05 | 2.69e-04 | 0 | 268.5 |
| 2 | 0.1341 | 60 | 0.09508 | **@rail** | 0.000685 | no | 5.01e-05 | 0 | 0 | 0.0 |

Thresholds: `ofc_bias_scale` clamp = ±0.1 · `DEVAL_SHIFT_MARGIN=0.05` · `SEPARATION_RATIO_MIN=3.0` · `MIN_PASS_SEEDS=2`.

**Expected vs observed.** Expected: a trained, devaluation-sensitive / task-role-discriminative OFC head shifts/separates its candidate selection. Observed: the head trained on all three seeds (head Δ 0.075–0.25, the second precondition `met:true`), but the cross-candidate bias *range* — the statistic every selection DV routes on — fell below floor on 2/3 seeds.

**Which criterion failed:** the **readiness / non-vacuity precondition** (a same-statistic gate), not C1/C2/C3 directly. C1 failed substantively (n_c1_seeds=0); C2 "passed" (n_c2_seeds=2) but `criteria_non_degenerate.C2=false`.

> Note on the manifest preconditions: both `interpretation.preconditions[].met` report `true`, because they are **max-over-seeds** (max bias range 0.0035 > 0.001; max head Δ 0.25 > 1e-3). The load-bearing gate is the **per-seed count** (`ready_seeds >= 2`), which only seed 0 clears. The self-route reads `readiness_met`, not the max-over-seeds preconditions — so it routes correctly.

## 2. Claim-layer mapping

- **SD-033b** (`design_decision`, candidate, `v3_pending=false`, depends_on SD-033/MECH-263/MECH-261). The behavioural validation that would take it candidate→provisional is precisely this experiment; the predecessors 485b/485c PASSed only as representation-level diagnostics.
- **MECH-263** (`mechanism_hypothesis`, candidate, `v3_pending=true`). Behavioural signatures still deferred per its own evidence note.

**Did the test let the claims express?** No. With near-zero cross-candidate bias range, the softmax over `-bias` is ~uniform regardless of devaluation or task-role context, so the DVs are vacuously ~0 by construction. The FAIL carries no information *against* either claim. `claim_ids` are accurate (the experiment does test these two; not inherited-tag contamination).

## 3. Biological-reference triage

Closest mechanism: OFC outcome-value / state-value coding driving candidate-differentiated action bias (Rudebeck & Murray 2018; Stalnaker 2021; Wilson-Niv 2014 cognitive map; SD-033b lit_conf 0.863). This is a **faithful translation**, not a formal-definition import (not the SD-003 class). The dependency the mechanism needs — candidate-*differentiated* value inputs and a bias-output range competitive with the selection softmax — is exactly what is absent. The failure matches "what happens biologically if a known dependency is absent," so it is a **discovered prerequisite**, not a falsification. Demotion threshold (tested fairly + biology supports + still fails) is **not** reached.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **intact** | Test never let SD-033b/MECH-263 express; non_contributory, not weakens. |
| Biological reference | **clear** | OFC value coding; faithful translation; failure = missing dependency. |
| Prerequisites | **missing/immature** | Candidate-bank cross-candidate z_world spread (ARC-065 GAP-A / SD-056) absent under reconstruction-trained e2.world_forward. |
| Implementation | **partial** | Trained-head substrate wired (485d), but the behavioural readout starves range on two axes (clamp + bank). |
| Environment | adequate | SD-054 bipartite reef/forage supplies the pressure. |
| Measurement | **under-instrumented** | C2 separation_ratio degenerate (tiny/tiny → 322 or 0); `criteria_non_degenerate.C2=false` caught it. |
| Integration | isolated (by design) | OFC is deliberately the sole bias channel. |
| Scale / capacity | adequate | Head trained fine at P1=60 ep; range collapse is structural, not under-training. |

**Recommended `epistemic_category`: `substrate_ceiling`** (V3-tractable in principle, but the current substrate readout — clamp regime + candidate bank — cannot deliver the cross-candidate range the distinctions require). The actionable response is the two-axis requeue below, not a demotion.

## 5. The two layers of the FAIL

**Layer 1 — OFC clamp-saturation (the readiness FAIL).** Seeds 1 & 2 saturate at the ±0.1 `ofc_bias_scale` rail (|bias| ≈ 0.095–0.10), collapsing range to ~0.0005. This is the calibration risk the GAP-8 landing pre-registered verbatim ("compute_bias clamps to ±ofc_bias_scale… can push the pre-clamp output past the rail for ~all candidates, zeroing grad… consider a larger ofc_bias_scale or a pre-clamp training signal if saturation stalls C2").

**Layer 2 — candidate-bank z_world collapse (why even the READY seed is vacuous).** Seed 0 is unsaturated and clears readiness, yet deval_shift = 8e-05 (margin 0.05; three orders too small) and its C2 separation is a near-zero-denominator artifact. The bank is the proposer's `world_states[1]` = reconstruction-trained `e2.world_forward` predictions, which fit the action contribution toward zero (V3-EXQ-571 / ARC-065 GAP-A / SD-056). So even an unsaturated head reads near-identical per-candidate inputs → no range to express. The 485e config does **not** enable SD-056 `e2_action_contrastive` in P0.

This is the OFC-head instance of the standing **candidate-differentiated affective gradients** pattern (V3-EXQ-643 cluster): a modulatory channel with magnitude but ~zero cross-candidate range gives E3 no gradient to carve behaviour.

## 6. Cluster shape

| Run | Channel | What carried range in the representation | What reached selection | Read |
|---|---|---|---|---|
| 569f / 661 / 654a | world-summary / rule_state / coherence | yes | nothing (flattened by the consuming head) | ARC-065 GAP-A route-range |
| 643 / 614e | curiosity / committed-class | (collapsed cand pool) | nothing | candidate-pool collapse |
| **485e** | **OFC trained head** | head trained (Δ 0.075–0.25) | near-zero range (clamp + collapsed bank) | **this autopsy** |

**Structural property, not N independent bugs:** the candidate-pool z_world collapse (ARC-065 GAP-A / SD-056) starves every per-candidate bias channel that reads it. 485e adds an OFC-specific compounding cause (compute_bias clamp-saturation). Two live readings, both addressed by the requeue: candidate-bank enrichment (SD-056 / GAP-A) **and** OFC clamp calibration (experiment-side).

## 7. Learning extracted

1. The GAP-8 clamp-saturation risk materialised on 2/3 seeds.
2. Clamp-saturation is necessary but **not sufficient** — the unsaturated READY seed still produced a vacuous DV, proving the candidate-bank collapse reaches this OFC channel.
3. 485e is the OFC-head instance of the V3-EXQ-643 candidate-differentiated-affective-gradients pattern.
4. The C2 separation_ratio metric is degenerate; it needs an absolute floor on `between_context_tv` before a PASS can count.
5. The same-statistic non-vacuity readiness gate worked exactly as designed: it converted a would-be false weakens into a correct `substrate_not_ready_requeue`.

## 8. Routing (user-confirmed: both axes)

**Route: `/queue-experiment` → V3-EXQ-485f** (alphabetic suffix; same scientific question, implementation/calibration fix). Apply **both** axes:

- **(a) Defeat OFC clamp-saturation** — raise `ofc_bias_scale` and/or add a pre-clamp training signal, and/or adopt the SD-033a 598b REINFORCE-over-candidates seeding the GAP-8 note cites as handling saturation, so per-candidate variation lands some candidates in-band.
- **(b) Restore candidate-bank spread** — enable SD-056 `e2_action_contrastive` in P0 so `e2.world_forward` preserves action divergence and the proposer's `world_states[1]` bank carries cross-candidate z_world range.
- **(c) Harden the metric** — add an absolute floor on `between_context_tv` so the C2 separation ratio cannot pass vacuously on a near-zero denominator.

**Substrate hand-off:** `action=amend` on the `modulatory-bias-selection-authority` / ARC-065 GAP-A substrate_queue entry — record 485e as a **corroborating** failure record of the candidate-pool-collapse cross-claim pattern. No *new* substrate is needed (candidate_summary_source / SD-056 already landed; V3-EXQ-649 validation pending). The OFC clamp axis is experiment-side, not a substrate gap.

**Governance posture:** SD-033b and MECH-263 stay **candidate / v3_pending**. `evidence_direction` stays `non_contributory`; `pending_retest_after_substrate=true`. No weakens, no demotion. The draft `evidence_quality_note` for governance to write is in the companion JSON.

## 9. Draft `evidence_quality_note` (for `/governance` to apply — not written here)

> See `recommended_evidence_quality_note` in `failure_autopsy_V3-EXQ-485e_2026-06-11.json`.
