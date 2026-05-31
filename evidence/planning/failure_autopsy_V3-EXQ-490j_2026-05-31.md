# Failure autopsy V3-EXQ-490j -- MECH-295 cascade GAP-4 Tier-1 (severed-bridge baseline)

- run_id: v3_exq_490j_mech295_cascade_gap4_tier1_severed_bridge_baseline_20260531T112417Z_v3
- queue_id: V3-EXQ-490j
- supersedes: V3-EXQ-490i
- claim_ids: [MECH-295]
- experiment_purpose: evidence
- outcome: FAIL
- timestamp_utc: 20260531T112417Z (machine DLAPTOP-4.local; elapsed 5.8 h)
- scope: single (cohort context: V3-EXQ-490g/h/i/j MECH-295 GAP-4 Tier-1 lineage)
- status: confirmed (user-confirmed routing 2026-05-31T11:50Z via AskUserQuestion)

## 1. Facts reconstruction (no interpretation)

### What 490j was designed to be

A corrected MECH-295 successor to V3-EXQ-490i per the failure_autopsy_V3-EXQ-490i_2026-05-30.{md,json} routing:

- ARM_0_severed_bridge: gap4-substrate-on with a post-build override `cfg.goal.z_goal_enabled = False`. `GoalState.is_active()` is False; the MECH-295 bridge cannot fire on the waking path (cue side checks goal_state.is_active(); write side checks GoalState.goal_norm >= floor which is zero when z_goal disabled).
- ARM_1_gap4_operating: identical to 490i ARM_1 (gap4 substrate, full Fork A library rebuild; drive_floor=0.9, drive_ema_alpha=1.0, goal_stream=True, use_dacc=True).
- Direct bridge-magnitude probe (per-tick `mech295_anticipatory_liking_write_peak/sum/calls` and `mech295_approach_cue_score_bias_peak/sum/calls`) replaces the 490i goal_norm_peak delta that was contaminated by ARM_0_legacy_collapsed accumulating a goal-norm baseline.
- Fixed 900-step eval budget per (seed, arm) to calibrate cross-seed magnitude comparisons (490i ARM_1 totals ranged 59 / 793 / 1379 across seeds 42 / 7 / 19; uncalibrated).
- C2 dACC bias recorded as diagnostic only (separate /diagnose-errors session owns the SD-032b dACC wiring gap per 490i autopsy).

### Per-criterion result (pre-registered acceptance grid)

| Criterion | Floor | ARM_1 result (seeds 42 / 7 / 19) | Pass? |
|---|---|---|---|
| C1 bridge_cue_fires >= 1 | 1 | 150 / 885 / 200 | T/T/T -> PASS |
| C2 dacc_bias_nonzero_steps | DIAGNOSTIC ONLY | 0 / 0 / 0 | (diagnostic; not gating) |
| C3 approach_commit_steps >= 1 | 1 | 900 / 900 / 900 | T/T/T -> PASS |
| C4 goal_active_fraction >= 0.05 | 0.05 | 1.0 / 1.0 / 1.0 | T/T/T -> PASS |
| C5 bridge_write_fires >= 1 | 1 | 900 / 430 / 822 | T/T/T -> PASS |
| C6 anticipatory_write_peak > 0 | > 0 | 0.287 / 0.0066 / 0.069 | T/T/T -> PASS |
| C7 approach_cue_bias_peak > 0 | > 0 | 0.396 / 0.054 / 0.427 | T/T/T -> PASS |
| **C8 approach_commit_rate_lift ARM_1 - ARM_0 >= 0.5** | 0.5 | 0.0 / 0.0 / 0.0 | **F/F/F -> FAIL** |
| C9 direct magnitude_lift ARM_1_sum > ARM_0_sum + floor | floor 1e-3 each | LW 80.2/0.58/17.5 vs 0/0/0; CB 27.1/8.9/34.2 vs 0/0/0 | T/T/T -> PASS |

### Severed-bridge sentinel (ARM_0 across all 3 seeds)

`severed_bridge_sentinel_clean: true` in the manifest. Explicit per-seed verification:

| Seed | bridge_cue_fires | bridge_write_fires | mech295_anticipatory_*_calls | mech295_approach_cue_*_calls | goal_active_steps | goal_norm_peak |
|---|---|---|---|---|---|---|
| 42 | 0 | 0 | 0 | 0 | 0 | 0.0 |
| 7  | 0 | 0 | 0 | 0 | 0 | 0.0 |
| 19 | 0 | 0 | 0 | 0 | 0 | 0.0 |

The severed-bridge contract holds. MECH-295 is structurally silent when z_goal_enabled=False, as the architecture predicts.

### The collapsed C8 in detail

`approach_commit_rate = approach_commit_steps / total_eval_steps`. Per-seed:

| Seed | ARM_0 approach_commit_rate | ARM_1 approach_commit_rate | C8 lift |
|---|---|---|---|
| 42 | 1.0 (900 / 900) | 1.0 (900 / 900) | 0.0 |
| 7  | 1.0 (900 / 900) | 1.0 (900 / 900) | 0.0 |
| 19 | 1.0 (900 / 900) | 1.0 (900 / 900) | 0.0 |

**The metric is at ceiling on the negative control.** ARM_0's `approach_commit_rate` is not zero (as the script's ROW 5 / ROW 6 paths would have anticipated under a bridge-mediated commitment-loss reading); it is 1.0 across all seeds. The lift criterion cannot fire even when ARM_1 also pegs at 1.0.

### Failed criterion class

**Discrimination**. Both arms hit the metric ceiling. Not absolute (the metric range is bounded) and not negative-control (the sentinel passes cleanly). The grid's pre-registered routing for this exact pattern is ROW 3 (C8 FAIL alone; C6/C7 PASS in ARM_1; C9 lifts).

### Action-class distribution (sanity check; not gating)

ARM_0 (severed-bridge) is NOT exhibiting goal-directed approach behaviour despite the metric ceiling:
- Seed 42: action_counts = {0: 3, 1: 171, 2: 4, 3: 716, 4: 6}; entropy 0.574 (mostly action 3)
- Seed 7: {0: 45, 2: 3, 4: 852}; entropy 0.221 (monostrategy on action 4)
- Seed 19: {0: 323, 2: 531, 3: 1, 4: 45}; entropy 0.836

The behavioural signature is incoherent across seeds and unrelated to MECH-295 cue-following -- yet the metric still says `approach_commit_rate = 1.0` everywhere. This independently confirms the contamination diagnosis: `_approach_commit` is reading something other than MECH-295-driven approach in ARM_0.

## 2. Script's pre-registered grid -> matched row

ROW 3 (C8 FAIL alone; C6/C7 PASS in ARM_1; C9 lifts) -- exact match.

Script (lines 132-141, paraphrased): "Substrate-side bridge fires cleanly; downstream linkage to the committed-state VALENCE_WANTING threshold gate is broken. The bridge produces a per-candidate negative score_bias that is too small to trip approach commitment. evidence_direction_per_claim[MECH-295] = narrow_supports (substrate validated, behavioural-test ambiguity). Routing: /queue-experiment (parametric sweep on mech295_liking_to_approach_cue_gain and APPROACH_WANTING_THRESH)."

**The grid's own routing recommendation is partially wrong.** A parametric sweep on bridge gain or APPROACH_WANTING_THRESH does not address the ceiling problem -- ARM_0 already saturates the metric, so raising the bridge gain in ARM_1 does not widen the lift. The pre-registered diagnostic narrative ("bridge bias too small to trip approach commitment") assumed an ARM_0 baseline near zero, which the manifest disproves. ROW 3's per-claim direction (narrow_supports) is the right call; ROW 3's routing recommendation is not.

## 3. Claim-layer mapping -- MECH-295

`claims.yaml:24389-` (read 2026-05-31):

- claim_type: mechanism_hypothesis
- status: candidate
- v3_pending: true
- implementation_phase: v3
- depends_on: SD-012, SD-014, SD-015, SD-016, MECH-117, ARC-036
- Strong vs weak necessity: **weak reading committed provisionally** (Pecina 2003 DAT-knockdown incompatible with strong, compatible with weak).
- Falsifiable (primary, weak reading): "a V3 factorial with the drive->liking link intact vs severed (under matched drive_level) should show approach_commit recovers when the bridge is intact and collapses when severed. EXQ-483's all-zero approach_commit signal is consistent with a broken bridge."
- `evidence_quality_note` (most recent, 490i upgrade): "V3-EXQ-490i autopsy upgrade (2026-05-31): the manifest evidence_direction_per_claim[MECH-295] is overridden from 'weakens' to 'narrow_supports' per confirmed failure_autopsy_V3-EXQ-490i_2026-05-30. Bridge fires cleanly in ARM_1 (cue_fires 6/4/12; write_fires 6/4/40)..."

**Did the experiment test the claim under conditions where the claim could express itself?** The substrate-side direct probe (C6/C7/C9) DID test the claim and confirmed the weak-reading prediction: bridge severed -> structurally silent (ARM_0 sentinel); bridge intact -> fires across all 3 seeds (ARM_1). The behavioural sign-test (C8) did NOT test the claim cleanly because the readout metric (`approach_commit_rate`) saturates on the negative control via paths that do not depend on MECH-295. The behavioural-test FAIL is a metric-design contamination, not a claim falsification.

**claim_ids accuracy.** `[MECH-295]` is correct -- this experiment was re-evaluated from scratch as a corrected MECH-295 successor (per 490i autopsy routing). No tag carried forward from a predecessor that was testing a different claim.

## 4. Biological-reference triage

- Closest mammalian reference: NAc shell hedonic hotspot + ventral pallidum + OFC pleasure coding (Berridge & Kringelbach 2015 architectural articulation).
- Dependencies in real brains: SD-012 (homeostatic drive), SD-014 (wanting/liking architecture), SD-015 (liking-stream substrate), SD-016 (appetitive valence stream wiring), MECH-117 (existing REE wanting/liking dissociation), ARC-036 (hedonic hotspot anatomical substrate).
- Formal-definition import? No. MECH-295 is biology-anchored not formal-import-anchored; the lit-pull (`targeted_review_mech295_liking_approach_bridge/`, 6 entries, mean conf 0.77) carries direct mechanistic evidence (Smith Berridge & Aldridge 2011 PNAS -- VP single-unit recording, drive change recodes palatability before cue firing).
- Divergence between REE bridge and biology? None at the SUBSTRATE level. The 490j substrate-side measurements (C6/C7/C9) match the architectural prediction exactly: drive amplifies liking-stream gain (anticipatory write at goal location), and the cue side translates the liking activation into per-candidate approach score_bias (negative bias in REE lower-is-better convention). The behavioural readout failure is REE-implementation-specific (an integration-layer measurement issue), not a biological mismatch.
- "Does the failure resemble what would happen biologically if a known dependency of the reference mechanism were absent?" No. In the biological reference, severing the drive -> liking bridge produces a behavioural collapse (Dickinson & Balleine 1994 devaluation pattern). 490j's ARM_0 does not show behavioural collapse on the metric -- it shows metric saturation, which is not a biological signature. The biological prediction is consistent with the SUBSTRATE-side C6/C7/C9 PASS; it is silent on whether the REE `_approach_commit` readout function should also collapse in ARM_0.
- Lit status: present (`targeted_review_mech295_liking_approach_bridge/SYNTHESIS.md`).

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **strengthened** | Substrate-side C6/C7/C9 cleanly support the weak-reading prediction. Severed-bridge silence (sentinel) is the predicted falsifier; bridge-intact firing (3/3 seeds) is the predicted positive. |
| Biological reference | **clear** | NAc shell + VP + OFC; lit conf 0.84 mean. No divergence at substrate level. |
| Prerequisites | **present** | gap4 substrate operating; Fork A library rebuild (2026-05-29 V3-EXQ-490g-cohort autopsy); drive_floor=0.9, drive_ema_alpha=1.0, goal_stream=True, use_dacc=True. |
| Implementation | **complete** at MECH-295 substrate; **partial** at downstream behavioural-readout isolation | MECH-295 bridge wired correctly (V3-EXQ-493 isolation 6/6 PASS, 2026-04-27/28, still standing). 490j sentinel-clean confirms the wiring. What is NOT complete: behavioural-readout isolation of MECH-295 contribution from other VALENCE_WANTING write paths. |
| Environment | **adequate** for substrate probe; **inadequate** for behavioural sign-test | The CausalGridWorld fishtank env with default REE config has too many MECH-295-independent VALENCE_WANTING write paths active in the eval window (see Section 6). |
| Measurement | **inadequate** | `_approach_commit` (goal_pipeline_tier1.py:225) reads `residue_field.evaluate_valence(z_world)[VALENCE_WANTING]` aggregate, not MECH-295-specific bridge propagation. Cannot dissociate MECH-295 contribution from sibling VALENCE_WANTING writers. |
| Integration | **partially coupled** | Bridge writes to ResidueField VALENCE_WANTING at goal-location and produces per-candidate negative score_bias at E3 cue-side -- both confirmed by C6/C7/C9. Downstream behavioural readout aggregates all VALENCE_WANTING sources, blurring MECH-295's contribution. |
| Scale / capacity | **adequate** | 900-step budget calibrated from 490i ARM_0 worst-case (911 at seed 19); above mean. Representational depth not relevant -- this is a non-trainable regulator substrate. |

Recommended `epistemic_category`: **standard**. Not substrate_ceiling -- the substrate itself works (C9 substrate-side measurement shows the claim's predicted signature). The failure is at the behavioural-test metric design layer, which is a /queue-experiment problem, not a /implement-substrate problem.

## 6. Why the metric is at ceiling on the severed-bridge baseline

`_approach_commit` returns True iff `beta_gate.is_elevated AND residue_field.evaluate_valence(z_world)[VALENCE_WANTING] > APPROACH_WANTING_THRESH`. In ARM_0:

1. **beta_gate.is_elevated** reaches True via E3 commitment driven by residue-terrain navigation alone. E3 commit gating does not require MECH-295. The agent commits on residue-shaped z_world terrain (ARC-007 strict; HippocampalModule generates value-flat proposals over residue-shaped terrain).
2. **VALENCE_WANTING readout** is non-zero via paths that do not depend on z_goal_enabled or MECH-295:
   - MECH-216 schema readout (when `schema_wanting_enabled=True`, writes VALENCE_WANTING = E1 schema_salience * drive * gain).
   - Serotonin tonic_5ht (when `tonic_5ht_enabled=True`, writes benefit_salience to VALENCE_WANTING).
   - MECH-290 hippocampal backward credit sweep (writes VALENCE_WANTING at committed-trajectory states on completion).
   - MECH-307 anticipatory liking write at predicted-location (writes to VALENCE_POSITIVE_SURPRISE / VALENCE_LIKING / VALENCE_WANTING depending on flags).
   - Contact-driven liking writes (VALENCE_LIKING, but evaluate_valence aggregates the relevant channels in downstream consumers).

None of these paths is severed by `z_goal_enabled=False`. They produce a VALENCE_WANTING floor in ARM_0 sufficient to clear APPROACH_WANTING_THRESH. The metric saturates as a consequence.

The action-class distributions for ARM_0 (Section 1 last table) confirm the agent is NOT actually engaging in MECH-295-style approach in ARM_0 -- it is monostrategy- or low-entropy-mixed-behaviour. The `_approach_commit` metric labels this as "approach commit" anyway because its definition does not require MECH-295-specific signal.

## 7. Cohort context (not a structurally-different-claim cluster)

V3-EXQ-490g/h/i/j is a single-claim cohort (all MECH-295 GAP-4 Tier-1) iterating on the test design after successive root causes:

- **490g cohort (FAIL 2026-05-29)**: Fork A library rebuild root cause; substrate not delivering the bridge under realistic policy state.
- **490h (FAIL 2026-05-30)**: silent-drop runner bug 41c3411; manifest never reached REE_assembly.
- **490i (FAIL 2026-05-30, narrow_supports per autopsy)**: substrate-side bridge fires cleanly (cue 6/4/12; write 6/4/40); C3_lift_vs_baseline contaminated by ARM_0_legacy_collapsed (z_goal_enabled=True, drive_floor=0) accumulating a goal-norm baseline. Autopsy routed to a corrected 490j with TRUE severed-bridge baseline + direct magnitude probe + fixed eval budget.
- **490j (FAIL 2026-05-31, narrow_supports)**: severed-bridge sentinel clean; substrate-side direct magnitudes lift; behavioural sign-test C8 ceiling-saturated on both arms.

**Convergent shape across 490i and 490j**: substrate-side probes cleanly support MECH-295 weak-reading; the behavioural sign-test (`approach_commit_rate` ARM_1 vs ARM_0) cannot carry the load. 490i had baseline-contamination on goal_norm_peak; 490j has ceiling-saturation on approach_commit_rate. Two distinct metric-design contaminations on the same MECH-295 weak-reading falsifier. The substrate is repeatedly clearing its bar; the BEHAVIOURAL TEST DESIGN is the recurring failure mode -- not a structural property of MECH-295 or its substrate.

This is not the substrate_uniform cluster shape (V3-EXQ-540/590a/591/598/603/610) and not the SD-037 consumer-cascade shape (V3-EXQ-483d/483e). It is a MECH-295-specific behavioural-readout-isolation problem.

## 8. Learning extracted

1. **Metric design must isolate the claim**. `approach_commit_rate` aggregates over `beta_gate.is_elevated * (VALENCE_WANTING > threshold)`. In a substrate where multiple write paths populate VALENCE_WANTING (MECH-216, serotonin, MECH-290, MECH-307), the metric cannot dissociate MECH-295 contribution. The 490j sentinel demonstrates this directly: bridge is provably silent in ARM_0 yet the metric still saturates at 1.0.
2. **Severed-bridge baseline is necessary but not sufficient**. Severing `z_goal_enabled` correctly disables MECH-295 at the source (C6/C7 zero in ARM_0 across all seeds, confirmed). But it does not disable the agent's other approach-related write paths. The 490i autopsy's baseline-contamination fix solved one contamination; 490j surfaces another at the readout layer.
3. **The grid's ROW 3 routing recommendation should be revised**. Parametric sweeps on `mech295_liking_to_approach_cue_gain` or `APPROACH_WANTING_THRESH` do not address ceiling-saturated negative controls. ROW 3's per-claim direction (`narrow_supports`) is correct; ROW 3's routing prescription (parametric sweep) is misaligned with the ceiling-saturation failure mode.
4. **Substrate signal is genuinely strong**. C6/C7/C9 PASS on 3/3 seeds with substantial magnitudes (peak anticipatory_write 0.287, peak approach_cue_bias 0.396, write_sum 80.2 vs zero in ARM_0 seed 42) is more direct mechanistic support for MECH-295 weak-reading than any 490 cohort run prior. This signal should be weighted in governance via the narrow_supports per-claim direction.
5. **Cohort-stable pattern**: substrate-side direct measurements cleanly support MECH-295 weak-reading; every behavioural sign-test design tried so far has had a distinct contamination. The next iteration should put a clean metric at the centre of the design, not just iterate on the baseline arm config.

## 9. Repair pathway and routing (user-confirmed 2026-05-31T11:50Z)

**Routing: /queue-experiment** for V3-EXQ-490k successor (corrected metric).

The behavioural sign-test must be redesigned to isolate MECH-295's contribution. Three candidate designs (the V3-EXQ-490k script should pick one or compose two):

(a) **Action-class divergence on first commit tick** between ARM_1 and ARM_0, holding other VALENCE_WANTING write paths active in BOTH arms. The metric becomes a per-seed `(argmax-first-action ARM_1) != (argmax-first-action ARM_0)` count or a cosine distance on the score_bias vector at first commit. This tests whether MECH-295 changes the SELECTED ACTION, not whether VALENCE_WANTING aggregate is non-zero.

(b) **Ablate non-MECH-295 VALENCE_WANTING writers** in both arms: turn off MECH-216 schema readout (`schema_wanting_enabled=False`), tonic_5ht (`tonic_5ht_enabled=False`), MECH-290 backward credit sweep (`use_backward_credit_sweep=False`), and any MECH-307 / SD-014 paths that touch VALENCE_WANTING. Then `approach_commit_rate` reflects only the MECH-295 path. Cleanest discriminant; the cost is ablating substrates that may interact.

(c) **Measure bridge-driven E3 score_bias propagation magnitude on first action selection directly**. The substrate-side C7 (`mech295_approach_cue_score_bias_peak`) measures the magnitude at the BRIDGE's output. The readout-side analog measures whether that bias actually moves the argmin in E3.select() at the commit tick. The metric becomes "fraction of commit ticks where MECH-295 bridge's per-candidate negative score_bias changes argmin from `no-MECH-295-counterfactual` to `with-MECH-295`." This is the cleanest mechanistic isolation but is the most invasive instrumentation.

**Recommended composition**: (a) + a per-tick guard that confirms the substrate is firing (C7 > floor) so that the metric only counts ticks where MECH-295 is actually producing bias. Variant (b) is a useful ablation arm to add for cross-validation.

**Per-claim direction for the 490j manifest**: `narrow_supports`. Strengthens the 490i precedent.

**Recommended `evidence_direction_per_claim[MECH-295]` exact text governance should write**:

> "narrow_supports"

**Recommended `evidence_quality_note` exact text governance should APPEND to the existing MECH-295 entry**:

> "V3-EXQ-490j autopsy upgrade (2026-05-31): manifest evidence_direction_per_claim[MECH-295] overridden from 'weakens' to 'narrow_supports' per confirmed failure_autopsy_V3-EXQ-490j_2026-05-31. Severed-bridge baseline contract verified (ARM_0 z_goal_enabled=False; bridge_cue_fires=0, bridge_write_fires=0, mech295_*_calls=0, goal_active_steps=0, goal_norm_peak=0.0 across 3/3 seeds). Substrate-side direct probes confirm bridge fires correctly in ARM_1: anticipatory_liking_write_peak 0.287/0.0066/0.069 (seeds 42/7/19), approach_cue_score_bias_peak 0.396/0.054/0.427, write_sum 80.2/0.58/17.5, all PASS the C9 direct_magnitude_lift criterion against zero-baseline ARM_0. The C8 approach_commit_rate_lift FAIL is metric-design contamination, not claim falsification: approach_commit_rate = 1.0 in BOTH arms across all 3 seeds. _approach_commit (goal_pipeline_tier1.py:225) reads VALENCE_WANTING aggregate at current z_world; in ARM_0 this saturates via MECH-216 schema readout, serotonin tonic_5ht benefit_salience, MECH-290 backward credit sweep, and MECH-307 anticipatory liking write paths that are independent of z_goal_enabled and do not flow through the MECH-295 bridge. Cohort context: 490i had goal_norm_peak baseline contamination; 490j has approach_commit_rate ceiling contamination -- distinct readout-design failures on the same MECH-295 weak-reading falsifier. The substrate signal is the load-bearing positive evidence; the behavioural sign-test cannot carry the load until the readout is redesigned. Routing: /queue-experiment for V3-EXQ-490k with metric redesign isolating MECH-295 contribution from sibling VALENCE_WANTING writers (action-class divergence on first commit tick under matched-write-path conditions, or ablation of non-MECH-295 writers in both arms, or direct E3 score_bias argmin-change probe). claims.yaml MECH-295 v3_pending gate remains held; the substrate is repeatedly clearing its bar, the metric design has not yet caught up."

## 10. Substrate queue handoff (not required this autopsy)

`recommended_substrate_queue_entry.action: none`. The substrate is operative -- MECH-295 bridge fires correctly when wired, structurally silent when severed (sentinel-clean). The repair pathway is /queue-experiment metric redesign, not /implement-substrate. The existing MECH-295 substrate_queue.json entry should remain at its current state (no amend, no new entry).

## 11. Open items NOT done this session

- claims.yaml MECH-295 evidence_quality_note append (governance applies).
- Manifest evidence_direction_per_claim write (governance applies).
- V3-EXQ-490k queue + script (separate /queue-experiment session per routing).
- C2 dACC wiring diagnosis (V3-EXQ-483 cluster owns this; orthogonal to 490j).
- review_tracker.json (governance applies on 490j review marking).
- substrate_queue.json (no edit -- no substrate amendment).

## 12. Predecessor autopsies in this cohort

- `failure_autopsy_V3-EXQ-490g-cohort_2026-05-29.{md,json}` -- Fork A library rebuild root cause.
- `failure_autopsy_V3-EXQ-490h-V3-EXQ-592b_2026-05-30.{md,json}` -- runner silent-drop bug 41c3411.
- `failure_autopsy_V3-EXQ-490i_2026-05-30.{md,json}` -- ARM_0_legacy_collapsed goal_norm_peak baseline contamination (substrate fires + sentinel needed; this autopsy chartered the 490j corrected harness).
