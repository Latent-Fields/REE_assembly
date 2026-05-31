# Failure autopsy V3-EXQ-490j -- MECH-295 cascade GAP-4 Tier-1 (severed-bridge baseline)

- run_id: v3_exq_490j_mech295_cascade_gap4_tier1_severed_bridge_baseline_20260531T112417Z_v3
- queue_id: V3-EXQ-490j
- supersedes: V3-EXQ-490i
- claim_ids: [MECH-295]
- experiment_purpose: evidence
- outcome: FAIL
- timestamp_utc: 20260531T112417Z (machine DLAPTOP-4.local; elapsed 5.8 h)
- scope: single (cohort context: V3-EXQ-490g/h/i/j MECH-295 GAP-4 Tier-1 lineage)
- status: confirmed (initial routing user-confirmed 2026-05-31T11:50Z; **revised 2026-05-31T11:58Z** per user follow-up question — see Section 13 necessity-vs-substrate reckoning. The revision changes the per-claim direction reading from `narrow_supports` to a split reading: **`weakens`** at the behavioural-necessity layer + **`supports`** at the substrate-firing layer. Sections 5, 9, and the recommended_evidence_quality_note are revised accordingly. The original narrow_supports framing is preserved verbatim within Section 13 for audit.)

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

**The grid's own routing recommendation is partially wrong.** A parametric sweep on bridge gain or APPROACH_WANTING_THRESH does not address the ceiling problem -- ARM_0 already saturates the metric, so raising the bridge gain in ARM_1 does not widen the lift. The pre-registered diagnostic narrative ("bridge bias too small to trip approach commitment") assumed an ARM_0 baseline near zero, which the manifest disproves. ROW 3's routing recommendation is misaligned with the failure mode. (Note: the grid's `narrow_supports` per-claim direction was endorsed in the initial autopsy but is superseded by the 11:58Z revision -- the parallel pathways that saturate ARM_0's metric are themselves architecturally first-class REE drive→approach pathways, so ARM_0's continued approach commitment is substantive falsifying evidence against the weak-reading necessity claim, not a metric-only artefact. See Section 13.)

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
| Claim alignment | **split: strengthened-at-substrate, weakened-at-behavioural-necessity** (revised 2026-05-31T11:58Z) | Substrate-side C6/C7/C9 cleanly support the architectural prediction that the bridge fires when wired and is silent when severed (strengthened). BUT the weak-reading necessity claim asserts "if the link is severed, drive amplification produces no approach regardless of drive magnitude" — ARM_0 (link severed, drive amplification active) **still produces approach commitment** (approach_commit_rate=1.0 in 3/3 seeds). Substrate-firing PASS does not entail behavioural necessity; the experiment provides falsifying evidence against the weak-reading at the behavioural layer via parallel pathways (MECH-216 drive→wanting, MECH-290 backward credit, MECH-307 anticipatory liking, serotonin tonic_5ht benefit_salience). See Section 13. |
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
- **490i (FAIL 2026-05-30, per-claim direction `narrow_supports` per the 490i autopsy as registered in claims.yaml; that direction was set on 2026-05-30 before the 490j parallel-pathways reckoning and may itself warrant a revisit in light of Section 13)**: substrate-side bridge fires cleanly (cue 6/4/12; write 6/4/40); C3_lift_vs_baseline contaminated by ARM_0_legacy_collapsed (z_goal_enabled=True, drive_floor=0) accumulating a goal-norm baseline. Autopsy routed to a corrected 490j with TRUE severed-bridge baseline + direct magnitude probe + fixed eval budget.
- **490j (FAIL 2026-05-31, per-claim direction revised 11:58Z to `weakens` at behavioural-necessity layer + `supports` at substrate-firing layer; indexer single assignment `weakens`)**: severed-bridge sentinel clean; substrate-side direct magnitudes lift; behavioural sign-test C8 ceiling-saturated on both arms; ARM_0's continued approach commitment via parallel pathways is substantive falsifying evidence against the weak-reading necessity claim, not a metric-only artefact.

**Convergent shape across 490i and 490j (revised 11:58Z)**: at the **substrate-firing layer**, both runs show the MECH-295 bridge fires correctly when wired and is silent when severed — that part of the architecture is validated. At the **behavioural-necessity layer**, both runs fail to demonstrate the weak-reading prediction that severing the bridge collapses approach behaviour; 490i failed via goal_norm_peak baseline contamination (the chosen substrate-side proxy was contaminated by a non-severed baseline), and 490j fails via approach_commit_rate ceiling-saturation (the chosen behavioural sign-test cannot distinguish MECH-295's contribution from architecturally parallel drive→approach pathways). The cohort-stable pattern is that **the substrate fires correctly, but no behavioural test in this cohort has cleared the weak-reading necessity prediction** — neither narrowly (490i contaminated metric) nor in the actual multi-pathway substrate (490j shows approach persists when MECH-295 is severed). The right governance response is to narrow MECH-295 from necessity to modulation (Section 9 primary route) and to design V3-EXQ-490k around the narrowed claim (Section 9 secondary route).

This is not the substrate_uniform cluster shape (V3-EXQ-540/590a/591/598/603/610) and not the SD-037 consumer-cascade shape (V3-EXQ-483d/483e). It is a **claim-scope** problem: MECH-295's weak-reading is over-specified for the actual REE substrate where multiple drive→approach pathways exist.

## 8. Learning extracted

1. **Metric design must isolate the claim, but isolating the metric does not rescue an over-specified claim**. `approach_commit_rate` aggregates over `beta_gate.is_elevated * (VALENCE_WANTING > threshold)`. In a substrate where multiple write paths populate VALENCE_WANTING (MECH-216, serotonin, MECH-290, MECH-307), the metric cannot dissociate MECH-295 contribution — but that is not the only problem. The deeper problem is that the parallel write paths are themselves **architecturally first-class REE drive→approach pathways**, so even a perfectly isolated metric would face a substrate in which approach can occur without MECH-295. Metric redesign is the route to test the *narrowed-modulatory* claim; it does not save the original *necessity* claim.
2. **Severed-bridge baseline is necessary but not sufficient**. Severing `z_goal_enabled` correctly disables MECH-295 at the source (C6/C7 zero in ARM_0 across all seeds, confirmed). But it does not disable the agent's other approach-related write paths. The 490i autopsy's baseline-contamination fix solved one metric contamination; 490j shows another at the readout layer — and the revision shows the cohort's underlying issue is claim scope, not just measurement.
3. **The grid's ROW 3 routing recommendation should be revised on both prongs**. Parametric sweeps on `mech295_liking_to_approach_cue_gain` or `APPROACH_WANTING_THRESH` do not address ceiling-saturated negative controls (the grid's routing prescription is misaligned), AND ROW 3's `narrow_supports` per-claim direction is also wrong for this run (revised 11:58Z to `weakens` — see Section 13). Future grids should explicitly distinguish "C8 FAIL with ARM_0 near zero" (potentially `narrow_supports`) from "C8 FAIL with ARM_0 at ceiling via parallel pathways" (necessity falsification at behavioural layer).
4. **Substrate signal is genuinely strong — at the substrate layer**. C6/C7/C9 PASS on 3/3 seeds with substantial magnitudes (peak anticipatory_write 0.287, peak approach_cue_bias 0.396, write_sum 80.2 vs zero in ARM_0 seed 42) is more direct mechanistic support for the **substrate implementation** than any 490 cohort run prior. It is NOT support for the **weak-reading necessity claim**, which makes a behavioural prediction the substrate-side measurement does not test. The signal should be weighted in governance as evidence FOR a narrowed-modulatory MECH-295 claim, not for the original necessity-framed claim.
5. **Cohort-stable pattern (revised)**: at the substrate-firing layer, direct measurements cleanly confirm the MECH-295 bridge fires when wired and is silent when severed across the entire 490g/h/i/j lineage. At the behavioural-necessity layer, no run in the cohort has produced behavioural collapse under severed-bridge — 490i via metric contamination, 490j via ceiling-saturation reflecting the actual multi-pathway substrate. Future iterations should be designed around the narrowed-modulatory claim, not the necessity claim, unless governance explicitly retains necessity and routes to a full-ablation test.

## 9. Repair pathway and routing (revised 2026-05-31T11:58Z; original 2026-05-31T11:50Z preserved in Section 13)

**Dual routing: /governance (claim narrowing) + /queue-experiment (substrate-isolating retest)**

The original autopsy routed only to /queue-experiment metric redesign on the framing that the metric was contaminated. The revision adds /governance as the load-bearing primary route because the load-bearing problem is **claim scope**, not metric design: in a substrate where parallel drive→approach pathways exist (MECH-216 drive-modulated wanting, MECH-290 backward credit, MECH-307 anticipatory liking, tonic_5ht benefit_salience), MECH-295's weak-reading necessity claim ("liking-stream activation is necessary; severing the bridge eliminates approach regardless of drive magnitude") is falsifiable as stated, and 490j provides falsifying behavioural evidence. The substrate IS implemented correctly (C6/C7/C9 PASS); what's mis-scoped is the claim, not the implementation.

### Primary route: /governance for claim narrowing

Propose to governance that MECH-295 be **narrowed from "necessity" to "modulation"**, with explicit text along the lines of:

> "MECH-295 modulatory reading: the drive → liking-stream → approach-cue gain pathway biases approach scoring via a liking-specific per-candidate score_bias; it is not the sole or necessary pathway by which drive amplification reaches approach action selection (MECH-216 drive-modulated wanting writes, MECH-290 backward credit, MECH-307 anticipatory liking, and tonic_5ht benefit_salience are parallel drive→approach pathways operating independently of the SD-014/SD-015 liking-stream substrate that MECH-295 names). MECH-295 specifies how liking-stream gain affects approach selection when active; it does not assert that severing the liking-bridge collapses behavioural approach in a multi-pathway substrate."

This preserves the V3-EXQ-493 isolation 6/6 PASS (substrate-side mechanism check) and the 490j C6/C7/C9 PASS (substrate fires correctly when wired) as evidence FOR the narrowed claim, and reclassifies the 490j C8 behavioural result as evidence AGAINST the original weak-reading-necessity scoping. The strong-reading falsifier (mu-opioid antagonist in NAc shell hotspot + hunger + cue-approach; lit-pull-flagged experimental gap) remains open under the narrowed claim.

The narrowing is biology-faithful: Pecina 2003 DAT-knockdown (more wanting, unchanged liking) is already incompatible with the strong reading and uneasily reconciled with the weak reading; the modulatory reading drops the necessity assertion entirely and treats liking as one substrate within a multi-pathway architecture (Berridge & Robinson 2003 wanting/liking dissociation; Berridge & Kringelbach 2015 hedonic architecture as one pathway among several).

### Secondary route: /queue-experiment for substrate-isolating retest

Even with the narrowed claim, a behavioural test that isolates MECH-295's modulatory contribution remains useful for landing the narrowed claim as confirmed_established. The three candidate designs from the original autopsy still apply, now reframed as "test the modulatory contribution, not the necessity":

(a) **Action-class divergence on first commit tick** between ARM_1 and ARM_0, with all other VALENCE_WANTING writers matched. Per-seed argmax-first-action ARM_1 ≠ ARM_0 count, or cosine distance on score_bias vector at first commit. Tests whether MECH-295 changes the selected action (modulatory contribution), not whether VALENCE_WANTING aggregate is non-zero (which it is in both arms via parallel writers).

(b) **Full-pathway ablation in both arms**: turn off MECH-216 schema readout (`schema_wanting_enabled=False`), tonic_5ht (`tonic_5ht_enabled=False`), MECH-290 backward credit sweep (`use_backward_credit_sweep=False`), and MECH-307 paths touching VALENCE_WANTING. The arm contrast then reflects only MECH-295's pathway contribution. Useful for landing whether MECH-295 is non-trivial in isolation, but does NOT recover the necessity claim — even if approach collapses in the all-off ARM_0, that only shows MECH-295 is necessary GIVEN the other writers are off, not that MECH-295 is necessary in the full multi-pathway substrate. This is the cleanest contributory test for the narrowed-modulatory claim.

(c) **Direct E3 score_bias argmin-change probe**: fraction of commit ticks where MECH-295 bridge's per-candidate negative score_bias changes argmin from no-MECH-295-counterfactual to with-MECH-295. This is the cleanest mechanistic isolation of MECH-295's modulatory contribution and is most directly what the narrowed claim asserts.

**Recommended composition for V3-EXQ-490k**: (c) as the primary metric (directly probes whether MECH-295's bias is load-bearing for the argmin) + (a) as a behavioural sanity check + (b) as a sensitivity-analysis ablation arm.

**Per-claim direction for the 490j manifest** (revised): `weakens` at the behavioural-necessity layer + `supports` at the substrate-firing layer. The indexer vocabulary does not have a native "split direction by interpretive layer" value; the cleanest single-value assignment is **`weakens`** on the manifest evidence_direction_per_claim[MECH-295] with the evidence_direction_note pointing to the substrate-firing PASS as a counterweight. Governance applies the split nuance via the evidence_quality_note text on the claim entry.

**Recommended `evidence_direction_per_claim[MECH-295]` exact text governance should write** (revised):

> "weakens"

**Recommended `evidence_quality_note` exact text governance should APPEND to the existing MECH-295 entry** (revised):

> "V3-EXQ-490j autopsy upgrade (2026-05-31, revised 11:58Z): manifest evidence_direction_per_claim[MECH-295] = 'weakens' at the behavioural-necessity layer. Severed-bridge baseline contract verified at the substrate layer (ARM_0 z_goal_enabled=False; bridge_cue_fires=0, bridge_write_fires=0, mech295_*_calls=0, goal_active_steps=0, goal_norm_peak=0.0 across 3/3 seeds; substrate-side C6 anticipatory_write_peak 0.287/0.0066/0.069 + C7 approach_cue_bias_peak 0.396/0.054/0.427 + C9 write_sum 80.2/0.58/17.5 ALL PASS in ARM_1 vs zero baseline). The C8 approach_commit_rate_lift FAIL is **not** purely metric contamination -- approach_commit_rate = 1.0 in BOTH arms across all 3 seeds reflects the substantive fact that ARM_0 (link severed, drive amplification active per gap4 substrate) still produces approach commitment via parallel pathways: MECH-216 schema readout (drive-modulated wanting write, W_m = κ(drive_level)·V_hat(schema_salience)), MECH-290 backward credit sweep (VALENCE_WANTING at completion), MECH-307 anticipatory liking write at predicted location, and serotonin tonic_5ht benefit_salience -- all drive→approach pathways operating independently of the SD-014/SD-015 liking-stream substrate that MECH-295 names. This falsifies the weak-reading necessity claim ('if the link is severed, drive amplification produces no approach regardless of drive magnitude') at the behavioural layer. The substrate IS implemented correctly (V3-EXQ-493 6/6 PASS isolation + 490j C6/C7/C9 PASS); what is mis-scoped is the claim. Governance recommendation: narrow MECH-295 from a necessity claim to a **modulation** claim -- 'the drive → liking-stream → approach-cue gain pathway biases approach scoring via a liking-specific per-candidate score_bias; it is not the sole or necessary pathway by which drive amplification reaches approach action selection in a multi-pathway substrate'. This is biology-faithful (Berridge & Robinson 2003 wanting/liking dissociation; Berridge & Kringelbach 2015 hedonic architecture as one pathway among several) and resolves the long-standing Pecina 2003 DAT-knockdown tension that troubled the weak-reading. The strong-reading falsifier (mu-opioid antagonist in NAc shell + hunger + cue-approach) remains the experimental gap for the narrowed claim. Cohort context: 490g (Fork A library rebuild root cause), 490h (runner silent-drop bug), 490i (goal_norm_peak baseline contamination -- corrected by 490j), 490j (substrate fires correctly, behavioural-necessity reading reframed). v3_pending gate stays held until either (i) the narrowed claim is registered + tested with substrate-isolating metric per the routing below, or (ii) governance retains the necessity framing and routes to a substrate-isolating test that suppresses MECH-216/MECH-290/MECH-307/tonic_5ht in the severed-bridge arm. Routing: PRIMARY /governance for claim narrowing (see autopsy Section 9 revised); SECONDARY /queue-experiment V3-EXQ-490k with direct E3 score_bias argmin-change probe (autopsy Section 9 option c)."

### Original (2026-05-31T11:50Z) Section 9 text — superseded by the revision above

The full text of the original Section 9 (recommended composition, per-claim direction `narrow_supports`, exact `evidence_direction_per_claim` and `evidence_quality_note` strings as initially landed at REE_assembly master `7715d75e8d`) is preserved verbatim in **Section 13** under "Original (2026-05-31T11:50Z) routing preserved verbatim for audit". The duplicate that previously lived here has been removed in the 11:58Z revision to avoid the appearance of two conflicting current recommendations within the same section. **Use the revised routing + revised `evidence_direction_per_claim` + revised `evidence_quality_note` above; the original is preserved only for audit.**

## 10. Substrate queue handoff (not required this autopsy)

`recommended_substrate_queue_entry.action: none`. The substrate is operative -- MECH-295 bridge fires correctly when wired, structurally silent when severed (sentinel-clean). The revised repair pathway is **/governance for claim narrowing (primary)** + **/queue-experiment metric redesign for the narrowed-modulatory claim (secondary)** — neither requires substrate enrichment. The existing MECH-295 substrate_queue.json entry should remain at its current state (no amend, no new entry).

## 11. Open items NOT done this session

- claims.yaml MECH-295 evidence_quality_note append (governance applies, using revised text from Section 9).
- claims.yaml MECH-295 **claim narrowing from necessity to modulation** (PRIMARY governance action per the revision; revised functional_restatement + falsifiable_predictions text per Section 9).
- Manifest evidence_direction_per_claim write (`weakens` per the revision; governance applies).
- V3-EXQ-490k queue + script for the substrate-isolating retest of the narrowed-modulatory claim (separate /queue-experiment session; SECONDARY routing per Section 9; option (c) direct E3 score_bias argmin-change probe recommended as primary metric).
- 490i autopsy direction may itself warrant a revisit in light of the parallel-pathways reckoning (Section 13) — its `narrow_supports` direction predates this revision and was set on the same conflation the revision tears apart. Flag to governance for a separate look.
- C2 dACC wiring diagnosis (V3-EXQ-483 cluster owns this; orthogonal to 490j).
- review_tracker.json (governance applies on 490j review marking).
- substrate_queue.json (no edit -- no substrate amendment).

## 12. Predecessor autopsies in this cohort

- `failure_autopsy_V3-EXQ-490g-cohort_2026-05-29.{md,json}` -- Fork A library rebuild root cause.
- `failure_autopsy_V3-EXQ-490h-V3-EXQ-592b_2026-05-30.{md,json}` -- runner silent-drop bug 41c3411.
- `failure_autopsy_V3-EXQ-490i_2026-05-30.{md,json}` -- ARM_0_legacy_collapsed goal_norm_peak baseline contamination (substrate fires + sentinel needed; this autopsy chartered the 490j corrected harness).

## 13. Necessity-vs-substrate reckoning (revision 2026-05-31T11:58Z)

### The gap the original autopsy missed

The original autopsy (Sections 1-12 as initially landed at REE_assembly master `7715d75e8d`, 2026-05-31T11:55Z) treated ARM_0's `approach_commit_rate = 1.0` as a **measurement contamination** -- the metric was reading non-MECH-295 VALENCE_WANTING writers, so the C8 FAIL did not carry information about MECH-295 itself. That framing recommended `narrow_supports` per-claim direction and /queue-experiment metric redesign as the sole routing.

The user follow-up question (paraphrased): "does this diagnosis take into account the idea that perhaps drive → liking bridge is an active modulatory pathway that can bias approach-cue scoring, but its necessity is not established while alternate approach pathways remain active?"

That question identifies a substantive gap in the original reading.

### What the original framing smuggled in

The original "metric contamination" framing implicitly assumed the parallel VALENCE_WANTING writers (MECH-216, MECH-290, MECH-307, tonic_5ht) are **confounds the test failed to control**, not **substantive evidence that approach behaviour has multiple drive-coupled pathways**. That assumption is not justified by the evidence; it begs the question against the modulatory reading.

### What the weak-reading necessity claim actually predicts

`claims.yaml` MECH-295 weak-reading falsifiable text:
> "if the link is severed, drive amplification produces no approach regardless of drive magnitude."

In V3-EXQ-490j ARM_0:
- Link severed: confirmed (C6/C7 = 0 across 3/3 seeds; severed-bridge sentinel clean).
- Drive amplification active: confirmed (gap4 substrate on: drive_floor=0.9, drive_ema_alpha=1.0).
- Approach is **still produced**: confirmed (approach_commit_rate = 1.0 across 3/3 seeds; agent commits in all eval windows).

On the face of it, this is **falsifying evidence against the weak-reading necessity claim's behavioural prediction**. The original autopsy reframed this as "the metric is reading non-MECH-295 paths" -- which is true at the level of mechanism, but the weak-reading claim is **about behaviour**, not about which substrate is driving it. The weak-reading says "no approach when severed"; 490j shows "approach when severed." That is the canonical pattern of necessity falsification, modulo the question of whether the parallel pathways are themselves substantive.

### The parallel pathways are substantive, not confounds

- **MECH-216 schema readout**: writes VALENCE_WANTING with `W_m = κ(drive_level)·V_hat(schema_salience)`. This IS a drive→wanting→approach pathway. It writes to VALENCE_WANTING (Berridge wanting), NOT to the SD-014/SD-015 liking-stream substrate that MECH-295 names. Wanting and liking are dissociable in REE (MECH-117 wanting/liking dissociation; Berridge & Robinson 2003).
- **MECH-290 backward credit sweep**: writes VALENCE_WANTING at committed-trajectory states on hippocampal completion (outcome_quality * gamma^(T-1-t)). Independent of MECH-295 bridge state.
- **MECH-307 anticipatory liking write at predicted location**: writes to VALENCE_POSITIVE_SURPRISE / VALENCE_LIKING / VALENCE_WANTING depending on flags, gated on MECH-205 PE > threshold. Independent of z_goal_enabled.
- **Serotonin tonic_5ht benefit_salience (MECH-203)**: writes VALENCE_WANTING = tonic_5ht * benefit_exposure. Independent of MECH-295.

These are not implementation artifacts to be ablated; they are **architecturally registered REE pathways**, each with its own claim and substrate landing. The existence of multiple drive-coupled wanting/approach pathways in REE is not a metric bug; it is the substrate's actual architecture.

### What the substrate-side PASS actually does and doesn't show

C6/C7/C9 PASS shows: **the MECH-295 bridge fires as architecturally specified and produces a substantial per-candidate approach_cue_score_bias when wired** (peak 0.396 / 0.054 / 0.427 across seeds 42 / 7 / 19). That is substrate-level validation of the IMPLEMENTATION.

C6/C7/C9 PASS does NOT show:
- That the bridge's score_bias is **load-bearing** for the argmin at E3 action selection (the score_bias is additive, and at peak 0.4 magnitude may be additive on top of other already-decisive score components).
- That the bridge is the **necessary** pathway through which drive amplification reaches approach commitment.
- That severing the bridge produces a behavioural collapse (490j actively shows it does not, in this multi-pathway substrate).

The original autopsy conflated "the bridge fires correctly when wired" with "the bridge is the necessary behavioural pathway." Those are different claims, and the 490j evidence supports the first and weakens the second.

### Revised reading (user-confirmed 2026-05-31T11:58Z via AskUserQuestion)

Per-claim direction MECH-295 = **`weakens`** at the behavioural-necessity layer + **`supports`** at the substrate-firing layer. The indexer vocabulary cannot natively express the split, so the single manifest assignment is `weakens` with the substrate-firing PASS recorded in evidence_direction_note as a counterweight. Governance applies the nuanced reading via the evidence_quality_note text on the MECH-295 claim entry.

The recommended governance action is to **narrow MECH-295 from a necessity claim to a modulation claim**. The narrowing is biology-faithful (resolves the Pecina 2003 DAT-knockdown tension, aligns with Berridge & Robinson 2003 wanting/liking dissociation and Berridge & Kringelbach 2015 hedonic architecture as one pathway among several) and preserves all substrate-side evidence (V3-EXQ-493 6/6 isolation + 490j C6/C7/C9 PASS) as evidence FOR the narrowed claim.

### Why "narrow_supports" was the wrong call originally

`narrow_supports` is the right reading when (i) the substrate fires correctly, (ii) the behavioural test is contaminated by an isolable measurement issue, and (iii) the claim's behavioural prediction is preserved pending a cleaner test. The original autopsy stopped at (i) and (ii); (iii) is the part that the revision pulls apart. In a multi-pathway substrate where parallel drive→approach writers exist (and are themselves architecturally first-class REE claims, not confounds), the behavioural prediction of the weak-reading necessity is NOT preserved pending a cleaner test -- it is **actively falsified** by ARM_0's continued approach commitment via parallel writers. The right call is to narrow the claim, not to preserve it.

### Substrate-queue implications

`recommended_substrate_queue_entry.action: none` is unchanged. The substrate is operative at the implementation layer; the claim-scope question is a /governance issue, not a /implement-substrate issue. No SD amendment is warranted by the revision.

### Original (2026-05-31T11:50Z) routing preserved verbatim for audit

Original Section 9 routing (replaced by the 11:58Z revision above):
> "Routing: /queue-experiment for V3-EXQ-490k successor (corrected metric). The behavioural sign-test must be redesigned to isolate MECH-295's contribution. [Three candidate designs (a)/(b)/(c)...] Recommended composition: (a) + per-tick guard that confirms substrate is firing (C7 > floor) so the metric only counts ticks where MECH-295 is actually producing bias. Variant (b) is a useful ablation arm to add for cross-validation. Per-claim direction for the 490j manifest: narrow_supports. Strengthens the 490i precedent."

The candidate experimental designs (a)/(b)/(c) survive the revision unchanged -- the cleanest test for the narrowed-modulatory claim is (c) the direct E3 score_bias argmin-change probe -- but the routing is dual now (/governance primary, /queue-experiment secondary) and the per-claim direction is `weakens` not `narrow_supports`.

### Methodological note for future autopsies in this cohort

When the substrate-side direct probe PASSes and the behavioural sign-test FAILs, the autopsy should explicitly check whether:

1. The behavioural test failure is metric contamination (alternative pathways inflate the readout aggregate).
2. The behavioural test failure is substantive falsification of a necessity claim (alternative pathways themselves carry the behaviour, demonstrating that the claimed pathway is not necessary).

These are not mutually exclusive but they have different routings: (1) → /queue-experiment metric redesign; (2) → /governance claim narrowing. Defaulting to (1) without checking (2) under-weights the falsifying signal and over-defends the claim. The original 490j autopsy made this mistake; the revision corrects it.
