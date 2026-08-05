# Failure Autopsy: 2026-08-05 pending_review.md batch (6 FAILs)

**Generated:** 2026-08-05T06:20:43Z
**Scope:** cluster (batch of 5 independent claim-lineages, N independent bugs -- see Cluster Read at the end)
**Status:** confirmed (user-gated at Step 8, all six targets)

Source: `REE_assembly/evidence/experiments/pending_review.md` regenerated 2026-08-05T06:04:58Z, 6 FAIL / 4 PASS (clean, no adjudication flags -- not autopsied) / 0 diagnostic self-routes. Dry-run gate (`check_dry_run_citations.py`) confirmed clean on all six run_ids before any metric was read.

Before scoping, `REE_assembly` and `ree-v3` were found in a genuinely dirty/diverged state (stray unmerged IGW-ledger conflict on 4 derive-only files in REE_assembly, no live process; `ree-v3` carries unrelated live uncommitted work from another session and was deliberately left untouched, not pulled). REE_assembly was repaired via a narrow reset+checkout of the 4 confirmed-derive-only paths, a clean merge with origin/master, and a full derive-chain regen (`sync_v3_results.py` -> `build_experiment_indexes.py` -> `generate_pending_review.py`) before scoping began.

---

## 1. V3-EXQ-875 / V3-EXQ-875a -- MECH-471 (competence provenance / local-update interference)

### Facts
- **875** (2026-08-03, ~20.5h, ree-worker-3): `outcome=FAIL`, `interpretation.label=substrate_not_ready_requeue`, `readiness.acquisition_ok=false`. Root cause (per a prior autopsy already on record, `failure_autopsy_V3-EXQ-875_2026-08-03`): all three `_train_all_on_agent` calls omitted `zworld_p0_episodes` (defaulted to 0) -- the documented SD-070 defect, z_world stayed a frozen random projection. Matches the pre-fix V3-EXQ-728 "seeds_failed=3/3" signature exactly.
- **875a** (2026-08-04, ~18.8h, ree-cloud-4, supersedes 875): fix applied -- `zworld_p0_episodes=60` added to competence-A acquisition, budget aligned to V3-EXQ-728's validated recipe (P0 120->200, P1 50->90, steps 150->200, eval 12->20, ~2.7x total training env-steps). z_world confirmed genuinely trained via a pre-queue probe (4/4 world_encoder tensors moved).
- **875a still fails the SAME readiness gate** (`acquisition_ok=false`), but the failure *shape* changed:

  | seed | a_baseline (survival ticks) | b_baseline | floor (0.6 x 200) |
  |---|---|---|---|
  | 42 | 15.95 | 23.75 | 120 |
  | 43 | **172.25** | **181.2** | 120 |
  | 45 | 51.25 | 50.45 | 120 |

  Seed 43 clears the floor strongly (near the 200-tick episode ceiling). Seeds 42 and 45 stay close to the random-walk anchor (~10-11 ticks) despite the identical, larger training budget.

### Claim mapping
MECH-471 (candidate, mechanism_hypothesis): "behavioural-competence updates require the same bounded/provenanced/rollback-capable discipline as consolidation." Neither run lets the claim express itself -- both are readiness-gate FAILs, `evidence_direction=unknown` by the driver's own acceptance schema (correctly self-routes "requeue," not a verdict; no V3-EXQ-642-style mislabeling here).

### Biological reference
Sequential local-update interference between two competences on a shared network is a well-grounded phenomenon in the retrograde/catastrophic-interference literature (Krakauer 2005, Walker 2003 -- currently only cited via sibling claim MECH-476's `targeted_review_mech_457_consolidation`). **No dedicated MECH-471 literature review exists.**

### Four-layer diagnosis (875a)
| Layer | Status | Notes |
|---|---|---|
| Claim alignment | not yet tested | readiness precondition unmet both times |
| Biological reference | partial | general interference literature exists; nothing MECH-471-specific |
| Prerequisites | present (SD-070 fix applied and confirmed) | necessary but not sufficient |
| Implementation | complete, exercised | z_world genuinely trains this run |
| Environment | adequate | reef/hazard survival task |
| Measurement | adequate | readiness metrics correctly capture acquisition |
| Integration | coupled, and demonstrably CAN work | seed 43 proves the pipeline is not broken |
| Scale | ~2.7x budget increase did not close the gap for 2/3 seeds | more of the SAME kind of budget did not fix it |

### Learning extracted
- The SD-070 zworld_p0 fix was necessary but not sufficient -- a second, distinct reliability problem sits underneath it.
- Seed 43's strong success rules out a representational ceiling: the substrate CAN acquire this competence end-to-end.
- A uniform budget increase across the board did not resolve the bimodality for the two failing seeds.
- Both runs executed the FULL expensive dose-response design (~19-20h each) to discover readiness-gate problems a much cheaper, narrower diagnostic could have surfaced.

### Routing -- confirmed at Step 8
**Cheap many-seed diagnostic probe** (user-confirmed, recommended option): queue a narrow probe running ONLY competence-A acquisition (skip the expensive Phase-2 targeted-update stage) across 10-20 seeds at modest budget, to characterize the seed-success-rate distribution and check for an early-death correlation, a hazard-layout-difficulty correlation, or neither. This is fact-finding, not a verdict, and is deliberately NOT a third full-budget same-design re-queue (875b) and NOT a blind route to `/implement-substrate` -- neither is warranted without first knowing which of three live hypotheses (exploration/init variance; hazard-layout difficulty variance; bias_head/OFC drive-arbitration interaction) explains the pattern. Pre-registered in the hypothesis-space ledger as `mech471_competence_acquisition_reliability` (3 hypotheses, unresolved, Mode A fan-out).

---

## 2. V3-EXQ-867b -- MECH-321 (harm-aware selection task effect)

### Facts
Fourth generation of the same question: **844** (2026-08-01, weakens for the harm-outcome prediction specifically -- C2 mechanistic PE-reduction supported) -> **867** (2026-08-02, non_contributory -- harm bias never engaged, no SD-029 hazard tuning) -> **867a** (2026-08-02, non_contributory -- hazard tuning added and bias engages, but the power guard was vacuous, `min(6, n_observed)` collapsed to the observed n=2) -> **867b** (2026-08-04, non_contributory again):

- Power guard fixed: hard floor `n_pairs >= 6`, the `min()` softening deleted.
- Screened a 48-candidate pool in-process on the measuring machine (ree-worker-1) -- still only **4** matched pairs with a measurable window; pool **exhausted** (only 7 of 48 candidates screen-matched at all).
- **New finding this cycle**: `screen_soundness_check` -- prefix-monotonicity predicts every screen-matched seed lands in `both_decompose` at full schedule. **5 of the 7** screen-matched seeds did NOT (`held: false`). Only seeds 8 and 103 actually held.

### Claim mapping
MECH-321 (candidate, v3_pending, `pending_retest_after_substrate=true`). All four attempts are inconclusive, each for a materially different reason.

### Biological reference
Well-grounded: `targeted_review_threat_modulated_defensive_path_selection` (9 entries, 2026-08-01) supports graded-threat-input / thresholded-regime / graded-output-within-regime as the correct model (Fanselow & Hoffman 2024, Mobbs 2007/2020, Evans 2018). The biology is not in question here.

### Four-layer diagnosis
| Layer | Status | Notes |
|---|---|---|
| Claim alignment | not yet tested at adequate power | 4th consecutive inconclusive attempt |
| Biological reference | adequate, well-cited | not the problem |
| Prerequisites | present | SD-hazard-aware-policy-decomposition + SD-029 tuning both engaged |
| Implementation | complete | both arms decompose, harm bias fires 1005x on-arm |
| Environment | adequate for engaging the mechanism | not adequate for reliable MATCHED comparison |
| Measurement | **under-instrumented for this design** | screen-to-full-schedule monotonicity assumption falsified |
| Integration | coupled but structurally unstable for measurement | the intervention itself appears to perturb whether/when decomposition fires |
| Scale | 48-candidate screen exhausted without reaching the floor | more screening of the SAME kind may not help |

The screen-soundness violation is the load-bearing finding: it is not "not enough seeds," it is "the short-screen result does not predict the full-schedule result for most of the seeds it selected." That is direct evidence the ON-arm manipulation changes decomposition timing/occurrence itself -- which is exactly what the matched-pair design needs to hold constant to isolate a harm-outcome effect.

### Learning extracted
- The matched-abort-pair screening premise is falsified on this run's own data, not merely under-sampled.
- This is a genuinely informative negative about the MEASUREMENT approach, even though it says nothing yet about the harm-outcome question itself.
- Four generations of fixing successive instrumentation defects (environment tuning -> power guard -> screen pool size) have each revealed a NEW defect rather than converging -- the recurrence itself is the signal that the design needs to change, not the sample size.

### Routing -- confirmed at Step 8
**Redesign the DV/matching strategy** (user-confirmed, recommended option). Refuse a same-design 867c (bigger pool, same screen-then-match methodology). Recommend a DV that does not require post-hoc divergence-tick matching -- e.g. an unconditional whole-episode harm-rate comparison across all measurement seeds. This is not a literal re-derive-brake firing (none of the four runs is stamped `substrate_ceiling`, so the strict R1-R3 counting convention doesn't count it), but the SAME spirit applies and is documented as such: don't re-queue the same design a fifth time. Registered in the hypothesis-space ledger as `mech321_harm_aware_selection_task_effect`, `resolution.state=alive`, `observation_bottleneck` naming the screen-soundness falsification.

---

## 3. V3-EXQ-887 -- SD-014 (node-valence representational separability)

### Facts
- SD-014's **first-ever genuine experimental evidence** (previously `lit_conf=0.868`, `experimental_confidence=0` across 4 prior non_contributory/measurement-gap runs going back to 2026-04-18).
- A live substrate defect was found by this experiment's own Step 2.5a probe and FIXED before the run: `ree_core/agent.py::_do_replay` built a 4-element `drive_state` against the `VALENCE_DIM=6` field (widened by MECH-307 on 2026-05-11) -- 12 weeks of silent breakage on the live replay-prioritization consumer path. Fixed ree-v3 `32edd553`; probe refreshed `46569178` the same day; the run's recorded `substrate_hash` matches the post-fix commit.
- **Readiness gate green**: all 4 R1-R4 preconditions met, including the instrument's own orthogonal synthetic control (tau=-0.011 vs a 0.5 ceiling) -- confirming the tau/rho statistics CAN detect separability when it's present.
- **Both load-bearing criteria fail on every one of 3 seeds:**
  - C1 (functional drive-gating): `mean_pairwise_tau_dissociated` = 0.867-0.889 vs `TAU_MAX=0.85` (drive vectors barely re-rank replay candidates -- tau near 1.0 means near-identical rankings).
  - C2 (representational separability): `max_abs_channel_spearman(wanting, liking)` = 0.93-0.97 vs `RHO_MAX=0.90` (the two channels are highly collinear in the actual stored representation).
  - C3 (replay-set selectivity) PASSES (jaccard 0.62-0.79 < 0.80 ceiling).
- `non_degenerate=true`.

### Root cause (read directly from source this session)
`ree_core/agent.py`:
- `update_liking()` (line 10287): writes `VALENCE_LIKING` from raw `benefit_exposure`, threshold-gated at `liking_threshold`.
- `update_benefit_salience()` (writes `VALENCE_WANTING`): uses `self.serotonin.benefit_salience(benefit_exposure)` -- a smoothed/EMA-calibrated transform of the **same underlying `benefit_exposure` signal**.

Both channels are mechanically derived from one shared input, just through different transforms (raw-threshold vs EMA-calibrated). That is a close-to-guaranteed source of collinearity, independent of environment richness or the presence/absence of a behavioral dissociation manipulation. This is unlike the biological system the claim is grounded in: Berridge's dopamine-mediated wanting and opioid-mediated liking are genuinely separate neurochemical pathways, which is precisely why sensitization/devaluation manipulations CAN pull them apart experimentally (Smith/Berridge/Aldridge 2011).

### Claim mapping
SD-014 (candidate, design_decision): "hippocampal map nodes must store an explicit 4-component valence vector... replay prioritisation weighted by drive-state-gated valence relevance." Literature strongly supports the general architecture (4 entries, all supports, `targeted_review_sd_014`). This run is the first fair test of whether the CURRENT implementation actually realizes it.

### Four-layer diagnosis
| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact -- a fair, well-instrumented test | mechanism given every chance to express itself |
| Biological reference | strong (4 lit entries, all supports) | LOAD-BEARING DIVERGENCE FOUND, see below |
| Prerequisites | present (SD-070/MECH-307 width fix landed same day) | confirmed via contract test |
| Implementation | complete, confirmed exercised | all four channels populate |
| Environment | single-arm, no active manipulation, but designed to probe stored representation directly | should not need behavioral manipulation IF write-paths were independent |
| Measurement | adequate, instrument-verified | orthogonal control confirms detection capability |
| Integration | coupled at the SOURCE | wanting and liking share one input signal |
| Scale | 3 seeds, fully consistent | not a power problem |

**Biological divergence (load-bearing, per the skill's core stance on formal-vs-biological translation):** the implementation computes wanting and liking from a shared input rather than genuinely independent pathways -- this is an implementation gap relative to the cited biology, not evidence the broader architectural claim (nodes should carry 4 separable components) is false.

### Learning extracted
- A clean, non-degenerate weakens with a concrete source-level mechanistic explanation -- not a measurement artifact, instrumentation gap, or underpowered test.
- Reading the substrate source directly (not just the manifest) was necessary to distinguish an implementation gap from an environment/design gap or a genuine claim falsification.

### Routing -- confirmed at Step 8
**Accept weakens + route to `/implement-substrate`** (user-confirmed, recommended option). `recommended_substrate_queue_entry.action=create`: decouple `VALENCE_WANTING`'s write-path from raw `benefit_exposure`, e.g. an incentive-sensitization term per Smith/Berridge/Aldridge 2011 so wanting can diverge from liking over repeated exposure/training. V3-EXQ-887's own instrument (validated, orthogonal-control-tested) can be reused to retest C1/C2 once the write-path changes. Registered in the hypothesis-space ledger as `sd014_wanting_liking_representational_separability`, `resolution.state=eliminated` (as-currently-implemented), `met_elimination_bar=true`.

---

## 4. V3-EXQ-848b -- ARC-005 (control-plane precision routing, finer ladder)

### Facts
Third generation: **848** (unweighted-channel bug, `dacc_goal_readout_weight` silently defaulted to 0.0) -> **848a** (calibration fixed, channel genuinely engaged -- 25,289 dACC bias calls -- but only 1/10 units cleared the bar on a 3-level ladder, with 7/10 units positive-signed and 6 piled at exactly rho=+0.5, the arithmetic signature of a 3-point Spearman-rho resolution ceiling) -> **848b** (pure measurement-resolution redesign, ladder 3-level -> 7-level, no substrate changes):

- Resolution ceiling now **broken**: `n_distinct_rho_values_observed=10` (all distinct), spanning -0.536 to 0.964.
- 4/10 units clear `|rho|>=0.6` (up from 1/10 on 848a), 2/10 additionally Mann-Kendall significant.
- `all_near_zero_null=false` -- not a clean negative either.
- True effect (~1e-3 log10-precision-units) is ~180x smaller than cross-seed SD (~0.18): a genuine underpowered-relative-to-noise problem, not resolution ambiguity anymore.
- `per_arm_gate.all_green=true` across all 14 arms/70 cells; build-time guard held.
- **No dedicated ARC-005 literature review exists anywhere in `evidence/literature/`.**

### Claim mapping
ARC-005 (active, architectural_commitment): "control plane routes precision and modes." Already satisfied via its own disjunctive test design (>=1 of 4 channels demonstrates causal authority) by the MODEPRIOR channel in V3-EXQ-846. This is a narrower, precision-specific sub-question about channels 1+2 specifically.

### Four-layer diagnosis
| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | ARC-005 itself already supported via a different channel |
| Biological reference | plausible, formal-import concern | dACC/NE precision-weighting (Yu & Dayan 2005) is real, but no dedicated lit-pull grounds it |
| Prerequisites | present | calibration confirmed engaged since 848a |
| Implementation | complete | all gates green |
| Environment | adequate | |
| Measurement | resolution bottleneck CLOSED this run | new bottleneck is statistical power, not resolution |
| Integration | coupled as designed | channel 2 architecturally expected null, channel 1 genuinely weighted |
| Scale | adequate cell count, inadequate power for a ~1e-3-unit effect against ~0.18 SD | |

### Learning extracted
- A finer measurement resolution converted an ambiguous "noise vs resolution artifact" result into a clear read: real but small, not a resolution ceiling and not a clean null.
- Breaking one bottleneck (resolution) revealed a different one (statistical power) -- worth recognizing before queuing yet another same-design iteration.
- ARC-005 rests on a real, citable mechanism (dACC/norepinephrine precision-weighting) with no literature review grounding it -- a gap that predates this specific sub-question.

### Routing -- confirmed at Step 8
**Accept mixed as final + commission `/lit-pull`** (user-confirmed, recommended option). No further same-design lettered iteration (resolution is no longer the bottleneck). Commission a targeted literature review for ARC-005's control-plane precision-routing claim. Registered in the hypothesis-space ledger by updating the existing `arc005_precision_channel_measurement_resolution` question (pre-registered 2026-08-03 off the 848a autopsy) -- `resolution.state` stays `alive`, `observation_bottleneck` updated from "3-point ladder ceiling" to "true effect ~180x smaller than cross-seed noise."

---

## 5. V3-EXQ-436d -- SD-017 / ARC-045 / MECH-166 (sleep-driven slot differentiation)

### Facts
Fourth generation: **436a** (SD-016 `cue_action_proj` consumer collapse, unrelated bug) -> **436b** (2026-08-02, recording gap -- `_ = agent.run_sleep_cycle()` discarded the write-counter return value entirely, `sws_n_writes`/`rem_n_rollouts` never captured) -> **436c** (2026-08-02, P0 recording fixed, but `ContextMemory.write()`'s `write_gate` acted as constant content -- sigmoid-midpoint 0.5·ones, not a modulator -- homogenizing whole-bank cosine toward 1.0 in 4/5 seeds, the OPPOSITE of the predicted direction) -> **436d** (2026-08-04, fixes the exact write_gate defect via `contextmemory_gated_content_write=True`, empirically pre-confirmed to break homogenization: legacy cosine 0.99993 -> 0.02487 with the flag on):

- P0 met: pooled `sws_n_writes=800`, `rem_n_rollouts=600`, both floor-clearing.
- `non_degenerate=true` (healthy waking-phase action-class entropy per the degeneracy self-check).
- **C1 fails**: 2/5 seeds pass (need 3/5). Per-seed direction is genuinely mixed (3 seeds show SWS >= WAKING cosine, i.e. sleep does NOT differentiate; 2 seeds show SWS < WAKING).
- **The WAKING_ONLY baseline itself is high-variance and doesn't match the claim's own prediction:**

  | seed | WAKING_ONLY cosine | SWS_THEN_REM cosine | direction |
  |---|---|---|---|
  | 42 | 0.391 | 0.432 | fails C1 |
  | 7 | 0.470 | 0.157 | passes C1 |
  | 13 | 0.00995 | 0.0854 | fails C1 |
  | 100 | 0.208 | 0.107 | passes C1 |
  | 200 | **0.00088** | 0.488 | fails C1, badly |

  ARC-045's own experimental_implication states "waking-only remains at cosine_sim -> 1.0 regardless of training duration." None of the WAKING_ONLY values are anywhere near 1.0 -- they range from 0.0009 to 0.47. Seed 200 shows sleep *increasing* similarity from near-zero to 0.488 -- the opposite of the predicted direction.

### Claim mapping
Three claims tested jointly: SD-017 (stable, design_decision), ARC-045 (candidate, architectural_commitment), MECH-166 (candidate, mechanism_hypothesis). All three still carry `pending_retest_after_substrate: true` and `live_status.evidence.from` pointing at the 436c autopsy -- none updated for 436d yet.

### Biological reference
Strong, well-cited on all three claims (10 lit entries total across `targeted_review_arc_045`, `targeted_review_mech_166`, `targeted_review_sd_017`, all supports, dated 2026-04-05: Diekelmann & Born 2010, Tse 2007, Born 2010, Tukker 2020, Aleman-Zapata 2022, Ego-Stengel/Wilson 2010, Girardeau 2009, Wikenheiser 2015).

### Four-layer diagnosis
| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear pending a check | first test with no KNOWN defect, but new anomaly |
| Biological reference | strong, well-cited | not the concern here |
| Prerequisites | present (write_gate fix confirmed) | pre-confirmed via a 200-write probe |
| Implementation | complete | P0 gate met |
| Environment | adequate | |
| Measurement | non-degenerate, but WAKING_ONLY baseline is anomalous | doesn't match the claim's own stated prediction |
| Integration | coupled | |
| Scale | 5 seeds, adequate for the pre-registered bar | not necessarily adequate given the baseline's own variance |

### Learning extracted
- 436d is the first test in this lineage to clear every known instrumentation/substrate defect, making it the most decision-relevant result so far -- but "most decision-relevant" is not the same as "decisive."
- A baseline that contradicts the claim's own stated prediction is itself diagnostic information, worth checking before treating the comparison arm's result as governance-ready.
- This is the skill's core stance in direct practice: the self-route (weakens) is a hypothesis about what the data means, not a verdict, even with `non_degenerate=true` and no known defect present.

### Routing -- confirmed at Step 8
**Quick methodological check before treating as decisive** (user-confirmed, recommended option). Do NOT yet discharge `pending_retest_after_substrate` on the three claims or feed this into a demotion discussion. Recommend a quick check of the `slot_cosine_sim` computation -- does it include empty/unwritten memory slots; is there a content-diversity confound driving WAKING_ONLY's own variance -- before finalizing. Registered in the hypothesis-space ledger as `sd017_arc045_mech166_slot_differentiation_sleep`, `resolution.state=alive`, `control_passed=false` (deliberately overriding the manifest's own P0-passed flag, since the concern is about what the baseline's behaviour implies, not about whether the write-counter gate cleared), `observation_bottleneck` naming the specific anomaly.

---

## Cluster read

**N independent bugs/questions, not one structural property.** Five unrelated claim-lineages (MECH-471, MECH-321, SD-014, ARC-005, SD-017/ARC-045/MECH-166) swept together in one governance cycle purely because they all landed in the same `pending_review.md` window -- there is no single underlying substrate defect connecting them.

That said, a shape recurs across four of the six targets worth naming explicitly: **875/875a, 867b, and 436d are all 3rd-or-4th-generation lettered iterations where fixing the PRIOR letter's diagnosed defect did not produce a decisive result -- it surfaced a genuinely NEW problem** (875a: readiness fix revealed seed-dependent bimodality; 867b: power-guard fix revealed a screening-methodology falsification; 436d: substrate fix revealed a baseline anomaly). In all three cases this session recommended against a further same-design lettered iteration, in favor of either a cheap targeted diagnostic (MECH-471) or an explicit redesign / methodological check (MECH-321, SD-017 lineage) -- the pattern itself, recurring across genuinely unrelated mechanisms, is evidence that iterative same-design re-queuing tends to peel back successive INSTRUMENTATION/DESIGN layers rather than reliably converging on a claim-level verdict.

The other two targets (887/SD-014, 848b/ARC-005) are the control case: both ARE lettered/staged iterations that DID reach a clean, decisive-enough reading once their prior instrumentation gap was closed -- 887 by finding the actual literature-divergent root cause in source code, 848b by resolving into a well-characterized (if still underpowered) real effect rather than an ambiguous artifact. The difference in both cases was reaching a point where the remaining uncertainty could be PRECISELY NAMED (a specific shared-input coupling; a specific noise/effect-size ratio) rather than staying diffuse.

## Governance follow-on (report only, not chipped -- per this autopsy's own routing not yet ratified by governance)

- MECH-471: queue the cheap many-seed acquisition-only diagnostic probe (`/queue-experiment`).
- MECH-321: design a redesigned DV/matching strategy for the harm-aware-selection task-effect test (`/queue-experiment`).
- SD-014: build the wanting/liking write-path decoupling (`/implement-substrate`), per `recommended_substrate_queue_entry` above.
- ARC-005: commission a targeted literature review (`/lit-pull`).
- SD-017/ARC-045/MECH-166: a quick methodological check of `slot_cosine_sim`'s computation (source read, not a new experiment) before 436d is treated as decisive.

Per CLAUDE.md Session Land Protocol step 6 and this skill's Step 8 rule (2026-07-30, user-instructed): these are NOT spawned as chips from this autopsy session -- `/governance` puts each recommendation in front of the user again before ratifying, and chips it once ratified.
