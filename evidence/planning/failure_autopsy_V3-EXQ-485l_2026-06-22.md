# Failure Autopsy -- V3-EXQ-485l (SD-033b/MECH-263 MECH-449-engaging OFC devaluation behavioural)

- **generated_utc:** 2026-06-22T06:47:06Z
- **status:** confirmed (user-adjudicated 2026-06-22 -- routing: implement-substrate, re-derive brake FIRED)
- **scope:** single
- **run_id:** v3_exq_485l_sd033b_devaluation_nogo_behavioural_20260622T063547Z_v3
- **queue_id:** V3-EXQ-485l (machine ree-cloud-2; supersedes 485k)
- **claim_ids (manifest):** SD-033b, MECH-263
- **manifest self-route:** FAIL / evidence_direction=non_contributory / interpretation.label=`substrate_not_ready_requeue` -- **CONFIRMED as a FAIL but re-localised** (see below). The behavioural test never ran; the failure is a readiness/non-vacuity floor breach on the devalued path, not a fair discrimination falsification.

---

## 1. One-line verdict

MECH-449 (Go/No-Go eligibility constitution) is **built and independently correct** (selection-face falsifier 689g PASS 3/3; promoted candidate->provisional 2026-06-22), so the 485k->485l transition was a *legitimate* re-derive-brake override -- real substrate was added between letters. But 485l shows the residual is now **structural scale**, not a tunable gain: the single shared OFC head under the **+/-0.5 `ofc_bias_scale` clamp** cannot carry a devalued re-ranking magnitude that is simultaneously (a) above the 0.05 readout floor and (b) above the No-Go viability trigger, while *also* carrying the C2 high-threat discrimination range. 485k's gain 4.0 **saturated** the clamp (range 0.0); 485l's gain 1.5 **undershot** it (range 0.031). The bias *vector* inverts cleanly (l2 1.83, cosine -0.716; C1b PASS 2/3) -- the head has the right re-ranking **direction** -- but the clamp compresses the **magnitude** below floor, so the viability No-Go that MECH-449 reads is starved (engaged 1/3) and the behavioural DV cannot register. **There is no feasible gain band on the shared +/-0.5 clamped head.** Route: implement-substrate (decouple the devaluation head / rescale the OFC clamp); refuse a plain 485m gain letter.

---

## 2. Facts -- reconstruction (no interpretation)

### Acceptance (pre-registered, per seed then >= MIN_PASS_SEEDS=2 of 3)

| Criterion | load-bearing | verdict | n_seeds |
|---|---|---|---|
| C1_devaluation_behavioural_shift | yes | **FAIL** | 1/3 |
| C1b_devaluation_bias_vector_inversion | yes (scored) | **PASS** | 2/3 |
| C2_discrimination_behavioural_separation | yes | FAIL (test short-circuited) | 1/3 |
| C3_silence_control | yes | PASS | 3/3 |

`pass=false`. The behavioural battery short-circuited under the readiness gate (`substrate_not_ready_requeue`), so the C1/C2 behavioural counts are partial, not a fair test result.

### Readiness preconditions (per-seed pass counts -- the 485k aggregate-max mask is fixed)

| precondition | measured | threshold | met |
|---|---|---|---|
| `ofc_bias_range_supra_floor_seed_count_HIGH_THREAT` (C2 control) | 3.0 | 2.0 | **True** |
| `ofc_bias_range_supra_floor_seed_count_DEVALUED_STATE` (the C1 statistic) | **0.0** | 2.0 | **False** |
| `ofc_head_trained_seed_count` | 3.0 | 2.0 | True |
| `mech448_f_eligibility_excluded_seed_count` | 3.0 | 2.0 | True |
| `mech449_go_nogo_withdrawal_engaged_seed_count` | **1.0** | 2.0 | **False** |

### Key range / engagement metrics

| metric | value | floor / note |
|---|---|---|
| `max_test_bias_range` (high-threat) | 0.3819 | >> 0.05 -- discrimination substrate present |
| `max_test_bias_range_devalued` | **0.0311** | < 0.05 readout floor -- the binding miss |
| `max_test_deval_bias_l2_shift` | 1.8308 | vector inverts (direction correct) |
| `min_test_deval_bias_cosine` | **-0.7156** | strong anti-alignment -- correct re-ranking direction |
| `nogo_engaged_seeds` | **1** | of 3; No-Go viability input starved by the flat range |

### Script parameters (code-confirmed, `experiments/v3_exq_485l_sd033b_devaluation_nogo_behavioural.py`)

- `DEVALUED_RERANK_GAIN = 1.5` (485k 4.0 -> 1.5, in-band), `DEVALUED_RERANK_WEIGHT = 0.3` (485k 0.5 -> 0.3).
- `ofc_bias_scale = 0.5` -- the +/-0.5 clamp, **KEPT from 485j/k** ("do NOT change").
- `GNG_VIABILITY_FLOOR = 0.1` -- per-candidate viability < 0.1 -> No-Go withdrawal. The viability is derived from the devalued bias (`_build_viability_nogo(bias_low)`).
- `BIAS_RANGE_FLOOR = DEVAL_SHIFT_MARGIN = 0.05`; `MIN_PASS_SEEDS = 2`.
- Pre-registered (line 147): a persistent FAIL despite MECH-449 self-routes `conversion-ceiling-persists-despite-go-nogo -> V4` for the autopsy to adjudicate.

**Causal chain:** gain 1.5 -> devalued range 0.031 (sub-floor) -> per-candidate viability nearly flat -> few/no candidates cross `GNG_VIABILITY_FLOOR=0.1` -> No-Go engages 1/3 -> withdrawal silent -> committed selection unchanged -> behavioural DV vacuous. The two readiness misses (devalued range, No-Go engagement) are **one root**, not two bugs.

**Which criterion failed:** readiness / non-vacuity floor on the devalued path (`ofc_bias_range_supra_floor_DEVALUED` + `mech449_go_nogo_withdrawal_engaged`), i.e. an absolute / non-vacuity breach -- the same shape as 485j/485k, NOT a fair discrimination falsification.

---

## 3. Claim-layer mapping

| claim | status / category | tested fairly? |
|---|---|---|
| **SD-033b** (OFC substrate) | candidate / substrate_ceiling / impl_phase v3 | devaluation half **not** tested under conditions where it could express itself (devalued range clamp-starved below the same-statistic floor). Non_contributory; **UNWEAKENED**. |
| **MECH-263** (OFC task-role discrimination + devaluation sensitivity) | candidate / substrate_ceiling / v3_pending | sig-b discrimination substrate present (high-threat range 3/3); sig-a devaluation half non_contributory pending the clamp/head substrate fix. **UNWEAKENED**. |
| **MECH-448** (rank-preserving F->eligibility demotion) | provisional / standard | not tagged; envelope fired (excluded 3/3). Not weakened. |
| **MECH-449** (Go/No-Go eligibility constitution) | provisional / standard | built + validated by 689g (3/3). 485l shows it is **correct but non-engaging** here because its viability input is clamp-starved -- positive evidence that the constitution needs a supra-floor valuation input, NOT a weakens. |

The self-route `substrate_not_ready_requeue` is CONFIRMED as a real FAIL (behavioural test did not run) but its *cause* is re-localised from "demotion-alone insufficient -> build MECH-449" (485k's correct diagnosis, now discharged) to "MECH-449 present but starved by the +/-0.5 shared-head clamp."

---

## 4. Biological-reference triage

Inherited and unchanged from the 485j/485k autopsies: OFC outcome-devaluation is a faithful biological target (Rudebeck & Murray 2014; Dickinson & Balleine; Mink 1996 focal-Go + surround-No-Go; Maia & Frank 2011), **not** a formal-definition import; `lit_status: present`. No `/lit-pull` commission needed. The mammalian devaluation signature is an active No-Go *withdrawal* of the previously-preferred action -- which is exactly what MECH-449 implements and 485l wires in. The failure resembles a known-dependency-present-but-input-starved signature: the withdrawal pathway exists and is correct, but the upstream valuation it reads is compressed below the trigger -- a discovered scale prerequisite (the devalued valuation must reach the No-Go in supra-floor magnitude), not a falsification.

---

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact (unweakened) | devalued half never tested fairly -- readiness floor breach |
| Biological reference | clear, load-bearing | OFC devaluation = active No-Go withdrawal; lit present |
| Developmental / dependency prerequisites | **present but non-engaging** | MECH-449 built (689g 3/3) but starved of a supra-floor viability input; MECH-448 envelope fired 3/3; trained head 3/3 |
| Implementation completeness | partial | single shared OFC head couples C2 magnitude + devalued range under one +/-0.5 clamp |
| Environment adequacy | adequate | OFC-isolated SD-054 bipartite reef/forage candidate bank |
| Measurement adequacy | adequate (fixed) | per-seed pass counts replace 485k aggregate-max mask; C1b vector readout catches the (correct) direction |
| Integration adequacy | coupled but unstable | one OFC head must do both devaluation re-ranking AND task-role discrimination |
| Scale / capacity | **clamp-bound (binding ceiling)** | +/-0.5 clamp + shared head -> no feasible gain band: 4.0 saturates, 1.5 undershoots |

**Dominant diagnosis -> recommended epistemic_category: `substrate_conditional`** (the devaluation half is conditional on a not-yet-built OFC-head clamp/decoupling substrate; the discrimination half remains substrate_ceiling under the existing tag).

---

## 6. Re-derive brake (MOVE-3) -- FIRED

This is the **10th** `non_contributory` / `substrate_ceiling` autopsy tagging SD-033b and MECH-263 (485e/g/h/i/j/k + three cluster docs, plus this one) -- far past `RE_DERIVE_BRAKE_THRESHOLD` (default 2). The 485k->485l override was legitimate (MECH-449 was genuinely built between letters), but 485l's residual is **structural scale**, not a tunable gain on the same substrate. The brake therefore FIRES:

- **Routing MUST be implement-substrate** on a named upstream substrate (the OFC devaluation-head clamp rescale / head decoupling).
- **REFUSE a same-claim test re-queue.** A plain 485m gain-tweak (gain between 1.5 and 4.0, lower `GNG_VIABILITY_FLOOR`) is **explicitly refused** -- it is exactly the lettered-iteration loop the brake exists to stop, and the autopsy shows there is no feasible gain band on the shared +/-0.5 clamped head. A redesign testing a *different* mechanism (new EXQ, different claim_ids) or a commitment-free read remains allowed; another letter circling this clamp ceiling is not.
- Stamped `re_derive_brake.fired: true` on the target.

---

## 7. Learning extracted + repair pathway

**Learning:**
1. MECH-449 demotion->withdrawal is correct but **input-gated**: it can only withdraw a candidate whose devalued viability crosses the No-Go floor, which requires a supra-floor devalued bias *range* -- a magnitude the +/-0.5 shared-head clamp does not deliver.
2. The 485k saturation and 485l undershoot bracket an (empty-or-near-empty) feasible band: on a single shared OFC head under +/-0.5, a differentiated-but-unsaturated devalued range that also preserves C2 is not reachable by gain alone. The shared head couples the two signatures destructively.
3. The correct *direction* (vector inversion, cosine -0.716, C1b 2/3) confirms the valuation is right; only the readable magnitude is clamp-limited -- this is a clean scale/integration diagnosis, not a claim pressure.

**Repair pathway: implement-substrate.** Amend the existing `f_dominance_conversion_ceiling` substrate entry (the same lineage 485k routed MECH-449 through) with a fresh failure record for the OFC-head clamp/decoupling gap. The build options for `/implement-substrate` to weigh: (a) **decouple** the devaluation head from the discrimination head (two heads, so the devalued re-ranking magnitude is not traded against C2); and/or (b) **rescale** the OFC bias clamp at the devalued state (or make `ofc_bias_scale` state-conditional) so a supra-floor differentiated devalued range fits without saturating; with (c) the No-Go viability mapping re-derived from the rescaled range. The behavioural retest is gated behind that build.

**Draft `evidence_quality_note` (governance to write, verbatim):**

> V3-EXQ-485l (2026-06-22, ree-cloud-2): supersedes 485k; FAIL/non_contributory/non_degenerate:false (no governance weight), self-route substrate_not_ready_requeue CONFIRMED + re-localised by failure_autopsy_V3-EXQ-485l_2026-06-22. MECH-449 (Go/No-Go constitution) is BUILT + validated (689g PASS 3/3, promoted candidate->provisional) so the 485k "build MECH-449" route is DISCHARGED, but 485l shows the residual is structural scale: the single shared OFC head under the +/-0.5 ofc_bias_scale clamp cannot carry a devalued re-ranking magnitude above the 0.05 readout floor AND the No-Go viability trigger while preserving C2. 485k gain 4.0 saturated (devalued range 0.0); 485l gain 1.5 undershot (0.031 < 0.05). The bias VECTOR inverts (l2 1.83, cosine -0.716, C1b PASS 2/3) -- correct direction -- but the clamp compresses the magnitude, starving the viability No-Go (engaged 1/3, < 2/3 gate). MECH-449 correct-but-non-engaging here = positive evidence the constitution needs a supra-floor valuation input, NOT a weakens. SD-033b / MECH-263 devaluation half: non_contributory / substrate_conditional / pending_retest_after_substrate, blocked on a NEW substrate -- OFC devaluation-head clamp rescale / head decoupling (amend f_dominance_conversion_ceiling). RE-DERIVE BRAKE FIRED (10th non_contributory autopsy on SD-033b/MECH-263): a plain 485m gain-tweak is REFUSED -- no feasible gain band on the shared +/-0.5 clamped head. MECH-448/MECH-449 NOT weakened (both engaged correctly within their scope). PROMOTES NOTHING.

---

## 8. Routing decision (user-confirmed 2026-06-22)

**implement-substrate** -- decouple the OFC devaluation head and/or rescale the +/-0.5 clamp so the re-ranking magnitude clears the readout + No-Go floors. Re-derive brake FIRED: a plain 485m gain letter is refused. Substrate entry: amend `f_dominance_conversion_ceiling`.
