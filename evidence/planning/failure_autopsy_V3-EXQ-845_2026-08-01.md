# Failure Autopsy: V3-EXQ-845 (MECH-180 ecological end-to-end)

Generated: 2026-08-01T10:37:54Z
Status: confirmed (interactive gate completed with user)
Scope: single

## 1. Facts

- **run_id**: `v3_exq_845_mech180_ecological_novelty_sleep_consolidation_dose_response_20260731T235634Z_v3`
- **queue_id**: V3-EXQ-845
- **claim_ids**: MECH-180
- **outcome**: FAIL, self-routed `evidence_direction: non_contributory`, label `mel_control_degenerate`
- **Not a dry run**: confirmed clean via `check_dry_run_citations.py` (0 dry cited / 5 clean across this session's targets).
- This is the FIRST run to test MECH-180's two links (novelty->MEL, MEL->consolidation) TOGETHER, ecologically, using SD-MEL-PRODUCER (world_rule_shift) as the novelty knob through the live SleepLoopManager. Prior runs in this lineage (677, 718, 718a) all failed on link (i) -- the novelty->MEL producer gap -- which is why the re-derive brake fired and the claim was re-parked 2026-07-08, then un-parked 2026-07-21 once SD-MEL-PRODUCER was built and validated (V3-EXQ-798a, PASS, 2026-07-30).

### Readiness (both preconditions MET, 100%)
- R1 (world-model trained, frozen-probe conv_rel_drop >= 0.667 floor): measured 1.0. MET.
- R2 (ecological novelty->MEL link holds in this run's full config): measured 1.0. MET.
- **This is new**: for the first time in the lineage, the novelty->MEL link (link i) is confirmed live under the run's own full agent config (z_goal/benefit machinery + live sleep loop), not just as an isolated test-bed property (798a).

### C1 (load-bearing, conjunctive over 3 sub-DVs, 4 ON arms sorted by measured MEL)
| DV | seed 42 | seed 123 | seed 456 | pass frac |
|---|---|---|---|---|
| C1a sws_power (cumulative_sws_writes) | monotone, pass | non-monotone, fail | monotone, pass | 2/3 |
| C1b spindle_density (mean_sws_slot_diversity) | monotone-DECREASING, fail | flat/near-ceiling, fail | monotone-DECREASING, fail | 0/3 |
| C1c replay_rate (cumulative_rem_rollouts) | monotone, pass | non-monotone, fail | monotone, pass | 2/3 |

Seed 123 is an outlier across all three DVs: its measured-MEL rank order swaps ARM_1_LOW and ARM_2_MED, and its slot-diversity values sit near-ceiling (~1.00-1.01) rather than following the clear decreasing pattern seeds 42/456 show.

### C2 (control: ARM_3_HIGH_ON must exceed ARM_4_HIGH_OFF on ALL 3 DVs)
Per-seed, per-DV ON vs OFF (all 3 seeds):
| DV | seed 42 | seed 123 | seed 456 |
|---|---|---|---|
| cumulative_sws_writes | 51 > 30 | 60 > 30 | 72 > 30 |
| cumulative_rem_rollouts | 102 > 60 | 117 > 60 | 142 > 60 |
| mean_sws_slot_diversity | 0.159 < 0.288 | 1.0071 < 1.0072 | 0.104 < 0.441 |

The two "amount" DVs cleanly pass ON>OFF in **all 3 seeds**. The one DV that fails C2 -- in all 3 seeds, and it alone -- is slot_diversity. Because C2 requires all three DVs to pass, this single DV's inversion fails the entire control gate, which routes the self-label straight to `mel_control_degenerate` (non_contributory) per the driver's own interpretation grid, before C1's more nuanced "1-2/3 pass -> mixed" branch is ever reached.

### Mechanistic root cause of the slot_diversity inversion (code-verified)
`sws_slot_diversity` is computed in `run_sws_schema_pass` (ree-v3 `ree_core/agent.py:10194-10209`) as the mean pairwise cosine distance across ALL of `ContextMemory.memory` -- a FIXED 16-slot bank (`ree_core/predictors/e1_deep.py:39`, `num_slots=16`), not a per-cycle or per-write-batch statistic. Each write is an EMA blend into the slot with lowest attention score to the query (`ContextMemory.write`, `e1_deep.py:74-80`: `0.9*old + 0.1*new`). Higher MEL -> higher `mean_duration_factor` -> more `sws_consolidation_steps` -> more writes per cycle into the SAME fixed 16 slots (measured: ARM_3_HIGH_ON writes ~51-72 times over 6 cycles vs ARM_4_HIGH_OFF's pinned 30). A fresh `REEAgent` (and fresh ContextMemory) is created per (seed, arm) cell (`_run_cell`, "ONE agent per cell" -- driver line ~594), so this is NOT cross-arm carryover contamination; it is a within-cell effect of write COUNT into a small, EMA-blended, fixed-capacity bank.

## 2. Claim-layer map

**MECH-180** (candidate, v3_pending, epistemic_category=substrate_ceiling from the PRIOR lineage's producer-gap finding, ceiling_decision=deferred). depends_on: INV-050, MECH-121, MECH-122, MECH-120. Predicts SWS power, spindle density, AND replay rate all increase together with novelty/PE load during preceding wake.

This run tests the claim under conditions where it CAN express itself for the first time (readiness both met). The claim's own three predicted DVs are not treated as a monolithic pass/fail by the driver -- C1 is conjunctive but the interpretation grid has a dedicated "mixed" branch for 1-2/3 partial support, which never gets reached here because C2's blanket AND-gate collapses first.

## 3. Biological-reference triage

Closest mammalian reference: Wilson & McNaughton 1994 (novel-maze place-cell replay in subsequent SWS), Tononi & Cirelli 2003 (SWA increases after high-learning wake), Louie & Wilson 2001 (REM replay of novel sequences). All three predict SWS depth/power, spindle density, AND replay rate move TOGETHER as a coupled bundle reflecting increased consolidation *volume* -- biology does not predict a capacity-driven anti-correlation between "how much is being consolidated" and "how differentiated the memory store looks" at the specific timescale/capacity this experiment operates at (16 slots, 6 measurement cycles).

The observed inversion is best read as an ARTIFACT OF THE V3 PROXY'S CONSTRUCTION, not a biological or claim-level finding: `sws_slot_diversity`'s own docstring says it estimates "context differentiation quality," but as computed (whole-bank cosine diversity, no normalization for write count) it structurally entangles the manipulated variable (MEL -> write count) with the DV in a way the other two DVs do not share. This is a measurement-adequacy gap, not a biology-divergence gap -- the substrate's real content-differentiation mechanism (an explicit `compute_diversification_loss` orthogonality-pushing auxiliary term already exists elsewhere in `ContextMemory`, SD-016 Path 1) is not what `sws_slot_diversity` as currently read is actually isolating here.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **strengthened (partial)** | For the first time end-to-end, 2/3 predicted DVs track measured MEL correctly in 2/3 seeds. Genuine partial support, not "not tested." |
| Biological reference | clear | Strong, multi-citation grounding (Wilson & McNaughton 1994, Tononi & Cirelli 2003, Louie & Wilson 2001); the predicted co-increase of all three DVs is a standard consolidation-neuroscience result. |
| Developmental / dependency prerequisites | present | SD-MEL-PRODUCER (novelty->MEL, VALIDATED 798a) and SD-MEL-CONSUMER (MEL->cadence, VALIDATED via injection 718a) both landed and functioning; this run is their first genuine end-to-end coupling. |
| Implementation completeness | complete for amount DVs, confounded for diversity DV | sws_n_writes / rem_n_rollouts cleanly reflect the MEL-scaled duration factor. sws_slot_diversity's whole-bank, write-count-unnormalized construction is the specific implementation gap. |
| Environment adequacy | adequate | SD-MEL-PRODUCER's world_rule_shift is validated as genuinely learnable, graded novelty (798a). |
| Measurement adequacy | **under-instrumented for C1b/C2 specifically** | sws_slot_diversity confounds consolidation AMOUNT with an EMA/small-fixed-capacity write-count artifact; not free of the manipulated variable. |
| Integration adequacy | coupled, working | MEL consumer engages correctly via the real SleepLoopManager/force_cycle path (per DEAD_Z_GOAL_STREAM_EXEMPT note, the z_goal stream is intentionally inert and arm-symmetric here, reviewed, not a gap). |
| Scale / capacity | **likely insufficient** for the diversity DV specifically | 16 fixed slots, up to ~72 EMA writes per HIGH arm over 6 cycles -- plausibly capacity-saturating for a whole-bank diversity readout, though this reads as a DV-construction problem more than a substrate-scale problem (the amount DVs at the same n_buf=1000 buffer show no such saturation). |

## 5. Cluster pattern

N/A -- single target.

## 6. Learning extracted

1. **The novelty->MEL->consolidation causal chain now works end-to-end for the first time in this lineage.** Both "amount" DVs (SWS writes, REM rollouts) show clean, correctly-signed, monotone dose-response to ecologically-measured MEL in 2/3 seeds -- the first positive end-to-end signal MECH-180 has produced after four prior attempts (677, 718, 718a all failed on link i; this run's readiness confirms link i now holds).
2. **The self-route's binary C2 gate (ALL 3 DVs must show ON>OFF) causes a single confounded DV to mask 2/3 genuine positive support.** `mel_control_degenerate` reads as "the whole comparison is untrustworthy," but 2 of 3 DVs are trustworthy and positive; only the third is confounded.
3. **`sws_slot_diversity`, as currently computed, is a poor dose-response instrument**: mean pairwise cosine distance over a FIXED 16-slot EMA-blended bank mechanically anti-correlates with total write count -- exactly the variable MEL manipulates. This is a measurement-construction defect, traced to specific code (`ree_core/agent.py:10194-10209`, `ree_core/predictors/e1_deep.py:74-80`), not a biological or mechanism-level failure.
4. **This is NOT a repeat of 718a's `mel_control_degenerate` self-route** (same label string, different cause). 718a's C2 failed because the ecological novelty itself was ungraded (noise-level MEL, scrambled vs novelty level). This run's R2 precondition confirms the novelty->MEL gradient DOES hold; the C2 failure here is entirely attributable to one DV's construction, not to a repeat of the environment-producer gap.

## 7. Recommended routing

**Recommended `epistemic_category`**: `measurement_test_design_defect` (NOT `substrate_ceiling` -- the substrate demonstrably CAN sustain the predicted coupling; 2/3 DVs prove it).

**Recommended `evidence_direction`**: `mixed` (not `non_contributory`). Per this skill's own rule ("state the interpretable signal explicitly before ever recommending non_contributory"), there is a clear, specific, positive interpretable signal here that a blanket non_contributory label would discard.

**Recommended `evidence_quality_note`** (draft text for governance):
> V3-EXQ-845 (confirmed failure_autopsy_V3-EXQ-845_2026-08-01): the first ecological end-to-end test of MECH-180 (novelty->MEL, SD-MEL-PRODUCER, VALIDATED 798a; MEL->consolidation, SD-MEL-CONSUMER, VALIDATED via injection 718a) run TOGETHER for the first time in this lineage. Readiness fully met (both R1/R2 preconditions pass at 100%) -- the novelty->MEL link now holds live under this run's full agent config, closing the producer gap that blocked 677/718/718a. Two of three predicted DVs (sws_n_writes, rem_n_rollouts) show clean, correctly-signed, monotone dose-response to measured MEL in 2/3 seeds and ON>OFF in 3/3 seeds -- genuine partial support, the first positive end-to-end signal this claim has produced. The third DV (sws_slot_diversity, the "spindle density" proxy) inverts in all 3 seeds, traced to a specific measurement-construction defect: it is computed as whole-bank cosine diversity over a fixed 16-slot EMA-blended ContextMemory, which mechanically anti-correlates with total write count -- exactly the variable MEL manipulates (ree_core/agent.py:10194-10209). Because the driver's C2 control gate requires ALL THREE DVs to show ON>OFF, this single DV's inversion collapses the self-route to non_contributory (`mel_control_degenerate`) despite 2/3 DVs being clean and positive. NOT weakened (partial support is real), NOT cleared (C1 conjunctive full-pass not reached; one DV needs redesign). mixed, not non_contributory. v3_pending STAYS; route: /queue-experiment same-question letter (V3-EXQ-845a) to redesign sws_slot_diversity -- e.g. normalize by write count, or restrict the diversity readout to the newly-targeted slots this cycle rather than the whole bank. PROMOTES/DEMOTES NOTHING pending that redesign.

**routing**: `queue-experiment` (same-question letter, V3-EXQ-845a, redesigning the spindle-density DV only).

User-confirmed at the interactive gate (2026-08-01): "Mixed + redesign the DV."
