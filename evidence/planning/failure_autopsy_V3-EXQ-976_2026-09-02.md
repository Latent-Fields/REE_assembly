# Diagnostic-PASS adjudication: V3-EXQ-976 (SD-e1 ITEM 2 candidate-1 rollout-consistency validation) -- 2026-09-02

**Run:** `v3_exq_976_sd_e1_item2_rollout_consistency_validation_20260902T114700Z_v3` - PASS - diagnostic - `claim_ids: []` (deliberate) - seeds [42,123,7,2024] - arms [ARM_single_step (routed OFF, depth-0), ARM_single_step_stateful (968's incumbent verbatim, non-routing anchor), ARM_rc_flat (H=5, decay 1.0), ARM_rc_decay (H=5, decay 0.5)] - ree-cloud-2 - 659 s - substrate commit ree-v3 `77dcc1dd` (dirty:false) - self-route `rollout_consistency_mixed_across_seeds` - manifest `evidence_direction: non_contributory` - manifest qid stamp `inv088_evaluator_degeneracy_cause` is a STALE template inheritance (that question is closed); the live question is `sd_e1_residual_crush_locus`.
**Status:** **confirmed** (2026-09-02, user answered all five questions "yes / agree with recommendation" via parent session sd018-directional-field-amend-ba5834ed; Q5 substrate_queue amend APPLIED, Q1 contrastive build + Q2 H-c probe chipped, Q3 ledger growth left for /governance, Q4 note only). Original drafting note: awaiting_human_confirmation -- drafted by a subagent of session `sd018-directional-field-amend-ba5834ed` that could not hold the Step 8 gate. The five questions the user must answer are at the end. Nothing here is applied. Red-team (Fable) CONTESTED the first draft's routing premise; contest accepted, artifact revised (Step 7c section).
**Dry-run check:** clean -- `check_dry_run_citations.py` exit 0 on the manifest; no `dry_run` key; the driver is not named by the `dry_run_unreachable_criterion` lint. The 2-seed smoke in the queue note wrote to scratch and is cited only as author intent.
**Recording:** `validate_recording.py` complete, 0 always-core gaps. `substrate_hash` present; `substrate_stable_across_run: false` is a fingerprint-scope artifact, not a code change (see Facts).

**Verdict in one line: the self-route label is ACCURATE and the run is a genuine, non-vacuous test; under the DRIVER's pre-registered relative rule it is MIXED (licenses nothing); under the SUBSTRATE ENTRY's own absolute-leaning licence text it is the NULL -- no absolute progress on the bars at h=1, where the evaluator runs the trained map -- and at depth the accuracy objective DAMPS per-action divergence growth on 8/8 ON cells, the mechanism the entry's `why_not_contrastive` named as the reason a divergence-preserving objective would be needed.**

## Facts (no interpretation)

**Provenance.** ITEM 2 substrate `ree-v3 6447b45` (11:14Z; rollout_consistency_loss + four default-off knobs, 24 contracts) is an ancestor of the run commit `77dcc1dd` (11:36Z; `git merge-base --is-ancestor` holds; dirty:false; no ree_core commit between 11:36 and 11:47Z). The manifest's two `substrate_hash` values (`201efa59...` on the four ARM_single_step cells, `a55fa9cf...` on the other twelve) are NOT a mid-run code change: the OFF arm is minted with `include_driver_script_in_hash=False` (driver:1180, the lineage-first-experiment cross-driver-reuse convention), the other arms with `True` -- 203 vs 204 fingerprinted files, same commit, identical `driver_script_hash`, resolved 11:36:38Z vs 11:38:53Z. The stability check compares unlike scopes and trips on that.

**Readiness (all 9 met, every cell).** encoder_trained; real_zworld_nondegenerate_h1 (n=40, floor 10); no_missing_action_calls (0); direct_action_supply_fraction 1.0; cr_ratio_h1_finite; e1_grad_steps_matched (gap 0 on every seed; 2614-2701 steps); rc_objective_non_vacuous (per ON cell mean gradient cosine with the incumbent objective: flat 0.711-0.748, decay 0.918-0.933, ceiling 0.95; depth-0 OFF diagnostic 0.381-0.620; stateful anchor 0.724-0.741 -- the gate certifies the objective PAIR disagrees at the current weights, it would pass on every arm); at_least_one_on_arm_non_vacuous (2); trained_calls_at_depth0 (1.0 on every routed cell; stateful anchor 0.037 = once per episode, by design). `non_degenerate: true`. That the ON objective was actually TRAINED rests on the code path (driver:618-629, `weighted = RC_WEIGHT * trained; weighted.backward()`) and on the per-arm fingerprints and profiles differing, not on the gate.

**Primary DV, cr_ratio(h=1) per cell** (recomputed from `cell_*_cr_ratio_by_h`):

| arm | s42 | s123 | s7 | s2024 |
|---|---|---|---|---|
| ARM_single_step (routed OFF, depth-0) | 1.38e-03 | 5.90e-04 | 2.63e-03 | 6.73e-03 |
| ARM_single_step_stateful (anchor) | 2.56e-03 | 4.33e-03 | 5.91e-03 | **2.98e-05** |
| ARM_rc_flat | 1.22e-03 | 3.39e-03 | 8.78e-03 | 1.26e-02 |
| ARM_rc_decay | 1.62e-03 | 1.64e-03 | 1.09e-02 | 2.03e-03 |

**Relative lift vs the routed OFF arm, fixed bar 3.0, majority 3 of 4** (`per_seed_lift`, recomputed; the sign-test p is the autopsy's own >=k-of-4 computation -- the driver records only the all-positive case, null here):

| contrast | h | per-seed lift | geo-mean | >=3.0 | <=1/3 | positive | sign p | driver verdict |
|---|---|---|---|---|---|---|---|---|
| rc_flat / single_step | 1 | 0.884 / 5.754 / 3.345 / 1.873 | 2.38 | 2 | 0 | 3 | 0.31 | mixed |
| rc_decay / single_step | 1 | 1.174 / 2.773 / 4.135 / 0.301 | 1.42 | 1 | 1 | 3 | 0.31 | mixed |
| rc_flat / single_step | 5 (trained H) | 0.337 / 2.662 / 1.828 / 0.773 | 1.06 | 0 | 0 | 2 | 0.69 | null |
| rc_decay / single_step | 5 | 0.449 / 1.269 / 1.598 / 0.055 | 0.47 | 0 | 1 | 2 | 0.69 | mixed |
| rc_flat / single_step | 30 (not a verdict horizon) | 0.293 / 2.402 / 1.830 / 0.694 | 0.97 | 0 | 1 | 2 | 0.69 | (would read mixed) |

No lift at h=5, so the `lift_at_trained_horizon_only` override did not fire; label composes to `rollout_consistency_mixed_across_seeds`. The numerator check the driver asks for passes: `cr_rollout_spread` ratios (0.887 / 6.037 / 3.283 / 1.847 for flat at h=1) track the cr_ratio lifts to within 5%, centroid norms within 3% -- the movement is per-action spread, not a denominator artifact.

**Depth growth, cr_ratio(h) / cr_ratio(1) per cell** (the table the first draft did not compute; red-team F1):

| arm | s42 h5, h30 | s123 | s7 | s2024 |
|---|---|---|---|---|
| ARM_single_step (routed OFF) | 3.23, 3.64 | 3.78, 4.48 | 3.10, 3.09 | 2.63, 2.44 |
| ARM_rc_flat | 1.23, 1.20 | 1.75, 1.87 | 1.69, 1.69 | 1.08, 0.91 |
| ARM_rc_decay | 1.23, 1.20 | 1.73, 1.70 | 1.20, 1.20 | 0.48, 0.31 |
| ARM_single_step_stateful (anchor) | 0.98, 0.34 | 0.09, 0.03 | 0.07, 0.04 | 0.69, 0.35 |

ON grows less than OFF on 4/4 seeds for each ON arm at both h=5 and h=30 (8/8 ON cells). The ON arms' absolute level is flat-to-mildly-rising with h (rc_flat s123: 3.4e-03 -> 5.9e-03 -> 6.4e-03); it is the OFF arm that rises ~3x. Every depth-0-trained arm except rc_decay s2024 (3.3x fall) holds or rises with h; the stateful anchor FALLS 3-30x on its three healthy seeds.

**Against the stateful anchor (recorded, never routed)**, h=1: rc_flat 0.476 / 0.784 / 1.487 / **422.5**; rc_decay 0.633 / 0.378 / 1.838 / **67.9** -- 1 exceeds, 0 below, 2 positive on each arm. The 422x/68x are the anchor's seed-2024 cell: cr_ratio 1.0e-05..3.0e-05 at EVERY h, e1coe var 4.7e-14, direct one-step action-probe pairwise mean 1.56e-05 vs 1.57e-03 on seed 42 -- ~100x action-insensitive at every readout after an unremarkable training (2705 steps, loss ratio 0.53, grad-cos 0.74). Either a statistical outlier or a fourth-seed instance of the stateful regime's own collapse mode; excluding it is post hoc at n=4 and is labelled as such. Routed OFF / stateful anchor at h=1 = 0.54 / 0.14 / 0.44 / 225.6: the B1 depth-0 symmetrisation lowered the routed incumbent 2-7x below the stateful one on the three healthy seeds (the trailing-window schedule cannot explain it: driver:570 gates every arm identically, anchor included). At h=5 the routed OFF arm is 1.8 / 6.0 / 18.7x ABOVE the anchor and at h=30 5.7 / 18.3 / 31.3x (healthy seeds). The anchor's seeds 42/123 (2.56e-03 / 4.33e-03) sit in 965/968's band (2.67e-03..3.96e-03 / 2.67e-03, 2.72e-03) -- commensurability holds.

**Absolute level (C2, recorded; both bars read at h=1).** `evaluator_bar_reached_cells = []`. Best ON cr_ratio(h=1) 1.26e-02 (rc_flat s2024) is 7.9x short of 0.1; worst ON 1.22e-03 is 82x short. Best ON e1coe_score_var(h=1) 6.1e-06 (rc_decay s7) is 2.5 orders short of 0.002. The highest cr_ratio anywhere in the run is the depth-0 OFF arm at h=5, s2024: 1.77e-02.

**Convergence proxy.** `trained_loss_last_over_first_fifth` 0.49-0.73 on every routed cell: still falling at 100 episodes. The ON arms receive H=5 supervision targets per optimiser step vs the incumbent's 1 (`e1_grad_steps_matched` calls that asymmetry "the manipulation").

**Recomputation scripts:** scratchpad `exq976/derived_numbers.md` and the red-team's `exq976/redteam_976.md` (every number above regenerates from the manifest's per-cell fields).

## The adjudication question: null, weak positive, or under-powered?

1. **By the DRIVER's pre-registered rule: MIXED.** `null` = "neither direction fires on ANY seed" (`_arm_verdict_at`: `n_exceeds == 0 and n_below == 0`; the manifest's `what_a_null_licenses` words it as "against the fixed bar 3.0 on >= MAJORITY_SEEDS seeds" -- 976 is not a relative null under either wording). Two seeds clear 3.0 on rc_flat, so not null; three are needed for `lifts`. `what_a_null_licenses` says only `rollout_consistency_null` licenses the withheld rollout-endpoint contrastive. **On the driver's terms the run does not license it**, and the label must not be rewritten post hoc.
2. **But the licence is written TWICE, and the texts disagree on 976 (red-team F3).** The substrate entry (`implementation_hint`: "If candidate 1 returns a null, THAT is what licenses the rollout-endpoint contrastive"; item-2 `validation_status`: "reading cr_ratio(h=1) and e1coe_score_var against the 0.1 / 0.002 evaluator bars"; `why_not_contrastive` and design doc ~line 325: "a null on it narrows ITEM 2's real target and buys the departure to a contrastive with evidence rather than intuition") never defines null relatively; its readout is the absolute bars. **Against those bars 976 IS a null**: no cell within 7.9x of 0.1, var 2.5 orders short -- and the bars are read at h=1, the one horizon at which the evaluator's hybrid rollout and the trained rollout are literally the same operation, so nothing about the readout blunts that result.
3. **Substantively: a weak h=1 positive, damping at depth.** Geometric-mean 2.4x for the flat form at h=1 with per-seed lifts spanning 0.88-5.75 (3/4 positive, p=0.31); 1.4x for the discounted form (sign-inconsistent); within 0.4-1.8x of the lineage's stateful incumbent at h=1 on its healthy seeds. At h>=2 the ON arms grow LESS than the OFF arm on 8/8 cells: the h=5 "null" is the OFF arm's compounding growth catching a damped ON arm. A trajectory-accuracy objective over H=5 works AGAINST per-action divergence at depth -- the signature the entry predicted for an accuracy objective and recorded as unmeasured ("INTUITION, not measurement").
4. **Power.** n=4 cannot separate a real ~2-3x paired h=1 effect from heavy-tailed paired noise; settling it is `complicated (buildable)` (add seeds) but of low decision value, since a settled 2.4x still leaves the bars 8-80x away. For the SD's decision -- does candidate 1 close or materially narrow the gap at this horizon and budget? -- the run IS adequately powered: no, on every cell.

**Recommendation (Q1):** read 976 as the entry's licensing null. Two independent lines point the same way: no absolute progress at h=1 on the trained map, and depth damping on 8/8 ON cells. The first draft of this artifact recommended holding the contrastive behind a readout-regime probe; that reason does not survive the red-team (below) and is withdrawn.

## Claim layer

`claim_ids: []` by deliberate and correct design; MECH-135 and INV-088 (both `candidate`, `epistemic_category: standard`, `pending_retest_after_substrate: true`, `diagnostic_evidence_adjudicated: true`) are untouched. Nothing here makes them retestable: the bars are still missed by wide margins. No `per_claim_recommendation`; GOV-APPLY-1 has nothing to apply.

## Biological-reference triage

Multi-step latent consistency is TD-MPC's ML form -- a formal import, ranked strongest of five in the commissioned lit-pull (`targeted_review_e1_forward_model_rollout_consistency`, 2026-08-03), which also found **no long-horizon biological anchor** for any candidate. Biological forward models (cerebellar/cortical efference-copy predictors) learn online from prediction error at the timescale of the loop they close -- nearer the single-step incumbent than a 5-step teacher-forced window; nothing in the biology predicts that a deeper accuracy window per se restores per-action discriminability, and this run's damping is consistent with the opposite. The divergence is already recorded in the synthesis; **no new lit-pull is commissioned**. The synthesis's #5 objection ("no long-horizon anchor") applies to the sequence contrastive with more force, as the entry says -- and the entry's own resolution was to proceed on evidence from candidate 1 rather than on literature; that evidence now exists.

## Four-layer diagnosis

| Layer | Status | Note |
|---|---|---|
| Claim alignment | n/a | claim-free by design |
| Biological reference | partial | formal import; divergence already in the synthesis; no long-horizon anchor |
| Prerequisites | present | ITEM 1 validated (965); ITEM 2 substrate an ancestor of the run commit; all 9 readiness met |
| Implementation | complete | objective genuinely trained (driver:618-629; per-arm fingerprints/profiles differ); matched steps; depth-0 symmetrised. The grad-cos gate is a pair-level certificate (anchor also 0.72-0.74). rc_decay is a small perturbation by construction: decay 0.5 over H=5 puts 51.6% of the weight on the incumbent's own step |
| Environment | adequate | CR_real 0.17-0.26, n=40 at every checkpoint |
| Measurement | adequate but under-powered at h=1; informative but on an untrained map at h>=2 | The Phase-4 evaluator is a HYBRID rollout (driver:791-830: E1 at horizon=1 per step with hidden state carried; z_self re-primed from E2 at :822; E1's context/prior re-computed per call, e1_deep.py:911-928) while `rollout_consistency_loss` trains E1's OWN map (`predict_long_horizon`, e1_deep.py:947-960: prior once, own total fed back). They coincide exactly at h=1 -- where the bars are read -- and differ from h=2 in the z_self source and per-step prior re-projection. **Withdrawn (red-team F1):** "the h=5 null shows the evaluator cannot see an E1-side change beyond h=1" -- the hybrid map reads E1's LSTM+output_proj at every step and the cells show it registers the objective (damping). What is missing is an E1-alone rollout readout for the MECH-135 30-step consumer question (108b's C3 is the same hybrid scorer, v3_exq_108b:451-463) -- a measurement gap, not a recording gap, and not one that bears on the h=1 bars |
| Integration | coupled | real pipeline; the hybrid evaluator is the 108-lineage C3 consumer, and at h=1 it runs the trained map |
| Scale | likely insufficient for the objective, adequate for the comparison | 100x200 kept for commensurability; loss still falling (0.49-0.73); H=5 is the substrate default, chosen without evidence; the supervision-volume asymmetry (5 targets vs 1 per step) is inside the h=1 lift |

**Failure-location (GOV-FAILLOC-1): MEASURES-partial on a diagnostic PASS; REE bucket not engaged.** Mechanism established, environment established, measures partial (n=4 at h=1; no E1-alone readout for the deeper consumer). No observation is described as REE failing.

## Learning extracted

1. A `mixed` under a majority rule is not a null wearing a modest coat -- do not rewrite the driver's label to reach the licence. But check whether the ENTRY that commissioned the run wrote the same licence: here it did not (relative in the driver, absolute in the entry), and they disagree on this run.
2. A null at the trained horizon can be damping, not absence. Compare depth GROWTH per arm before reading a flat ON/OFF ratio at depth as "no effect": OFF grew x3 from h=1 to h=5, ON x1.4, so the ratio's collapse toward 1 IS the objective's (negative) effect. First-draft argument withdrawn on this evidence: "different map" is not "blind".
3. Symmetrising a confound can move the incumbent. B1's depth-0 symmetrisation (correct) lowered the routed OFF arm below the stateful incumbent at h=1 on 3 of 4 seeds, so a lift over it partly measures the incumbent's drop -- at h=1 only; at h>=5 the depth-0 arms are 2-30x ABOVE the anchor. The non-routing anchor (N1) is what made both halves visible.
4. Know which horizon the bars are read at before arguing about readout regimes: the SD's bars are at h=1, where the hybrid evaluator and the trained rollout are the same operation, so a readout-regime hypothesis cannot gate the SD-level decision.
5. A gradient-cosine non-vacuity gate certifies the objective PAIR disagrees, not that the ON weights were trained on the ON objective (the untrained stateful anchor read 0.72-0.74, rc_flat's band). Keep the gate; cite the code path for "the manipulation landed".
6. A minted OFF arm fingerprinted with `include_driver_script_in_hash=False` beside ON arms fingerprinted with `True` yields two substrate hashes in one run and trips `substrate_stable_across_run: false` -- indistinguishable, as a flag, from a real mid-run code change. Compare like scopes, or say which it was.
7. A decay-0.5 discounted objective over H=5 is 51.6% the incumbent's own step; its near-ceiling gradient cosine and noisier read follow.
8. (Observation) The stateful incumbent's cr_ratio collapses 3-30x with depth on its healthy seeds and its fourth seed is ~100x action-insensitive at every readout; depth-0-trained arms (bar rc_decay s2024) hold or rise. The hidden-state training regime, not the objective, separates the depth profiles in this run.

## Step 7b (mechanical pre-routing checks)

`autopsy_pre_routing_checks.py`: fire_count 0. C1/C2/C3 INAPPLICABLE (claim-free target -- structurally blind, not a clean bill); C5 looked once the `.md` existed and did not fire; C6-narrow did not fire. Step 7c carried the load, and found the routing defect the checks cannot see.

## Step 7c (adversarial red-team -- Fable, `claude-fable-5-1`, cross-model)

**CONTESTED; contest accepted; artifact revised.** Every stated number was reproduced (lifts, geometric means, sign p 0.3125, spread ratios, vs-anchor lifts, 7.93x / 82.0x / 2.52 orders, 51.6%, grad-cos ranges, fingerprint scope split, git window, ancestry). Contested and accepted:

- **F1** -- the first draft's H-c mechanism ("the hybrid evaluator is blind to an E1-side change beyond h=1") is contradicted by the manifest's own cells: ON arms grow less with depth than OFF on 8/8 ON cells (OFF x2.6-3.8 h1->h5; rc_flat x1.1-1.75; rc_decay x0.5-1.7). The h=5 null is damping -- H-f's predicted signature, now measured. Confirmer: the depth-growth table above.
- **F2** -- the SD's bars are read at h=1 (`C2` reads `cr_ratio_by_h[1]`, `var[1]`; 965 failure record; entry `validation_status`), where the hybrid and trained maps coincide exactly; H-c cannot gate the licence question. Confirmer: `grep -n "cr_ratio_by_h\].get(1" driver`.
- **F3** -- the substrate entry / design doc write the licence in absolute-leaning terms and never define null relatively; only the driver does. Q1 must present both texts.
- Also accepted: F5 (post-hoc anchor exclusion labelled), F6 ("restores the level" scoped to h=1), F8 (H-c is a retrain; H-e needs a supervision-matched OFF cell), F9 (grad-cos gate is pair-level), hygiene 1-9 (rc_decay s2024 depth fall; h=30 rc_flat "mixed"; no bare "null at the trained horizon" in durable entry text; stale qid stamp flagged; sign test labelled as the autopsy's; new-EXQ justification for H-c; `aleatoric` token corrected to `complicated (buildable)`).

**Net effect on routing:** first draft "queue-experiment, H-c first as the gate on the contrastive" -> this revision "implement-substrate on the contrastive conditional on Q1; H-c a queue-experiment sibling, never a gate". The withdrawn argument is recorded (learning 2, measurement row), not deleted.

## Routing (DRAFT -- awaiting the user)

- **Adjudication:** self-route `rollout_consistency_mixed_across_seeds` ACCURATE and retained. `evidence_direction: non_contributory`, `epistemic_category: standard`, no per-claim change. MECH-135 / INV-088 stay `pending_retest_after_substrate`.
- **Routing: `implement-substrate`, conditional on Q1** -- amend `SD-e1-rollout-consistency-training` per `recommended_substrate_queue_entry` (candidate 1 validated-as-mixed with damping; 976 failure record appended; the withheld rollout-endpoint contrastive `e1_rollout_sequence_divergence_*` put forward as the next build item, H-f, licensed by the entry's own null text and supported by the damping). Validation of that build: contrastive ON arm vs a depth-0-symmetrised single-step OFF arm AND 968's stateful anchor, same DVs, n>=6 seeds, fixed 3.0 paired bar, bars at h=1; declared null: within the 3.0 band at h=1 and depth growth no larger than the incumbent's.
- **If the user holds the DRIVER's rule instead (Q1-b):** no contrastive yet; fall back to `queue-experiment` -- H-c first, H-e on idle compute.
- **Fan-out siblings (GOV-FANOUT-1, `sd_e1_residual_crush_locus`), in both cases:** **H-c readout-regime** (eval-dynamics): 976's driver re-run (a RETRAIN, ~11 min; 976's agents were never saved) with an added E1-alone rollout readout (`predict_long_horizon(total_0, 30, actions=seq)` on the identical 40 sequences) beside the hybrid readout; new EXQ number because the question is different (does the consumer's regime suppress divergence the objective produced?) although the manipulation is identical; declared null: same damping contrast under both readouts. **H-e horizon/budget** (learning-signal, LOW; weakened a priori by the damping): rc_flat, H in {5,30} x budget {100,400}, plus a supervision-matched OFF cell, n>=6.
- **Explicitly NOT:** a same-question lettered power-up of 976 alone (`complicated (buildable)` but low decision value); `/lit-pull`.
- **Re-derive brake:** not applicable (claim-free; `standard`). **Granularity trigger:** not applicable. **Step 9b:** drafted only -- Mode B leave-alive on `H-training-objective` (resolving run 976; basis narrowed and weakened) and a three-leg labelled fan-out growth on `sd_e1_residual_crush_locus` (3 -> 6: H-objective-class-divergence, H-readout-regime, H-objective-horizon-budget), in `hypothesis_space_ledger_pending` for the confirming session.
- **Substrate-queue amend (Q5, applied by the parent session, which holds the claim):** status -> `item2_candidate1_validated_mixed_contrastive_decision_owed`; item-2 `validation_status` -> the 976 result text (says "damping", never a bare "null at the trained horizon"); append the 976 `failure_record` entry; `implementation_hint` -> the two-licence-texts statement and the next-action text. `severity` / `substrate_paths` untouched. The 965 record stays open.
- **`action_cond_unzero_self_slot`:** unchanged; every 976 arm ran with it True and the run adds no evidence either way. Successors keep it fixed; the default flip remains a user decision.
- **Nothing spawned** (2026-07-30 rule): governance chips the routing once ratified.

## Read-across (verified, NOT adjudicated here)

1. `sd_e1_residual_crush_locus / H-training-objective` stays alive, narrowed and weakened (see ledger-pending block).
2. `inv088_evaluator_degeneracy_cause / H-horizon-compounding` (eliminated by 954 on the action-blind substrate): the stateful anchor on the ITEM-1-ON substrate shows the depth-collapse profile 954 did not see. Not a re-adjudication -- 954 eliminated compounding as the DOMINANT cause of the 108b collapse, which stands. Q4 asks whether to register it (recommendation: note only).
3. MECH-135's 30-step endpoint consumer is the same hybrid scorer (108b:451-463); 976's damping says an accuracy E1 objective moves its endpoint divergence the wrong way at depth; H-c asks whether the consumer's regime would suppress a divergence-preserving objective's effect too.
4. IGW-20260831-222: the ITEM 2 build session's ledger row already names 976 as its validation; nothing further owed.

## Questions for the user (Step 8 gate, not held)

1. **Q1 (load-bearing):** two licence texts disagree on 976 -- the DRIVER's relative rule ("mixed", not licensed) vs the SUBSTRATE ENTRY's absolute-leaning text (976 is the null, licensed). The draft recommends the entry's reading (no absolute progress at h=1 on the trained map + depth damping on 8/8 ON cells). (a) Sanction the rollout-endpoint contrastive build now (H-f -> `/implement-substrate`; H-c as a sibling), or (b) hold the driver's rule -- no contrastive yet; `queue-experiment` H-c first?
2. **Q2:** run H-c (the E1-alone readout retrain) alongside either answer? (Recommend yes, as a sibling -- it settles what the MECH-135 30-step consumer can see, which the contrastive's validation will need.)
3. **Q3:** confirm the three-leg fan-out growth on `sd_e1_residual_crush_locus` (3 -> 6), or fold H-e into H-training-objective's basis and register only H-f and H-c?
4. **Q4:** register the stateful-anchor depth-collapse observation as a Mode-C discovery on `inv088_evaluator_degeneracy_cause`, or note only? (Recommend note only.)
5. **Q5:** approve the substrate_queue amend as drafted for the parent session to apply.
