# Failure autopsy -- V3-EXQ-1027 + V3-EXQ-1029 (SD-082 fan-out portfolio, legs 1 and 3)

- **Generated:** 2026-09-14T22:01:33Z
- **Status:** confirmed (user-gated at 2026-09-14T22:32:04Z, interactive, Mac DLAPTOP: 1027 leg `eliminated`; successor attached to H1 after 1028, no ledger growth; routing confirmed as drafted)
- **Scope:** cluster (two legs of one GOV-FANOUT-1 portfolio)
- **Runs:**
  - `v3_exq_1027_sd082_replay_own_rule_state_credit_assignment_20260914T135320Z_v3` -- FAIL, diagnostic, `H_replay_rule_state_mismatch_not_supported`
  - `v3_exq_1029_sd082_selection_authority_readout_consequence_20260914T191118Z_v3` -- PASS, diagnostic, `H_selection_authority_bounded_supported_magnitude_test_underpowered`
- **Claims:** SD-082 (both). Registry question `sd082_candidate_discriminating_readout_locus` (co-registered SD-078).
- **Fan-out source:** confirmed `failure_autopsy_V3-EXQ-1020_2026-09-11` (REE_assembly 92751187b1), ratified gov-20260911-1612; queued as ree-v3 d76b57c4c3 (chip chip-20260911-sd082-fanout-portfolio-v2). Sibling V3-EXQ-1028 (`v3_exq_1028_sd082_learning_signal_extended_budget`, legs 2 + 4) was still running on DLAPTOP at draft time and is NOT adjudicated here.
- **Dry-run gate (Step 2a):** `check_dry_run_citations.py V3-EXQ-1027 V3-EXQ-1029 V3-EXQ-1037` -> 0 dry cited, 0 dry in named families. Both manifests `dry_run: false`, non-dry run_id shape. `validate_experiments.py --checks dry_run_unreachable_criterion` silent on both drivers. `excluded_dry_run_ids: []`.
- **Recording provenance:** `validate_recording.py` -> 2 complete, 0 always-core gaps. 1027: ree-v3 42c03b1485, substrate_hash 0c2fcc38f0ce..., ree-cloud-2, 4960.7 s. 1029: ree-v3 64d9ee07c8, substrate_hash 14ff4a2a0074..., ree-cloud-2, 19074.5 s. The two legs ran on different main commits; `git diff --name-only 42c03b1485 64d9ee07c8` touches only `experiment_queue.json` and three new drivers (1012a, 1037, 1038), no `ree_core/` file, so cross-leg inference is safe (red-team attack (d), failed).
- **Routing (confirmed):** 1027 `governance-note-only`; 1029 `queue-experiment` (one successor run attached to the alive registry leg H1, queued only after 1028). Substrate queue: `amend` SD-082 (chain extension + two failure records + disposition of the open 1020 record's C2 clause; severity/paths unchanged). No build owed. No lit-pull owed.
- **Step 7c red team:** CONTESTED (claude-opus-5, cross-model), seven findings, all independently verified and folded in -- section 11.

---

## 1. Why these runs existed

`failure_autopsy_V3-EXQ-1020_2026-09-11` closed 822f's blind-instrument ambiguity (the in-run positive control learned and persisted) but settled neither pre-registered learning-signal leg, and its own driver named an unexcluded rival: the REINFORCE replay scores every buffered sample at ONE shared end-of-episode `rule_state`. Its Step 7c red team added a second observation: with `use_modulatory_selection_authority` False, a +/-0.1 tanh-bounded bias added to primary scores whose range is much larger should not be able to change the argmin. The user selected a four-leg portfolio at that gate:

| Leg | Hypothesis | Axis (family) | Run |
|---|---|---|---|
| 1 | H-replay-rule-state-mismatch | credit-assignment (process) | **V3-EXQ-1027** (this artifact) |
| 2 + 4 | H-learning-signal-sign + H-learning-signal-noisy | learning-signal (constitution) | V3-EXQ-1028 (running) |
| 3 | H-selection-authority-bounded | intrinsic-architecture (constitution) | **V3-EXQ-1029** (this artifact) |

Both drivers were red-teamed at queue time (fable, CONTESTED, findings fixed) and carry `interpretation.criteria_aggregation` (the 1020 autopsy's forward-only fix).

## 2. Facts

### 2.1 V3-EXQ-1027 (FAIL, informative null)

Two replay arms, everything else byte-identical to 1020's ARM_ON: `REPLAY_FAITHFUL` (index 4 = None, every sample scored at the live end-of-episode rule_state) vs `REPLAY_OWN_RULE_STATE` (each sample scored at the rule_state snapshot taken immediately after its own `select_action`; live state saved/restored around every update). Seeds 611/622/633/644/655, P0 60 / P1 70 / 48 steps. DV: pooled step-direction persistence of `rule_bias_head` over the P1 updates, bracketed per cell by the in-run pure-noise Adam floor (0.449) and dense-synthetic-credit ceiling (0.723-0.757).

**Readiness (all met):**

| Gate | measured | threshold | note |
|---|---|---|---|
| R1 synth_credit_control_ready | 1.0 | >= 0.8 | control learned (+0.0024..+0.0036 gain) and persisted (0.723-0.757) in 10/10 cells |
| R2 own_rule_state_manipulation_non_vacuous | 0.5006 (worst seed 622) | >= 0.10 | buffer-mean DIRECTION mismatch mean(1-cos), per seed 0.50-0.70; norm-inclusive 0.97-1.18 |
| R3 persistence_headroom_eligible_seeds | 5 | >= 3 | worst headroom-minus-margin +0.009 (seed 611); P1 buffers byte-identical (SHA-256) 5/5; trajectories identical 5/5. C1 is reachable without the marginal seed: 622/633/644 carry 2.6x-4.6x margin headroom |

**Criteria:**

| Seed | pers FAITHFUL | pers OWN | lift | margin | summary-col lift | rule-col delta | clears C1 | below 1020 C2 midpoint (both arms) |
|---|---|---|---|---|---|---|---|---|
| 611 | 0.652 | 0.622 | -0.031 | 0.071 | -0.004 | -0.071 | no | no |
| 622 | 0.406 | 0.475 | +0.070 | 0.070 | +0.003 | +0.173 | no (by 0.0006) | yes |
| 633 | 0.558 | 0.559 | +0.001 | 0.077 | -0.012 | +0.072 | no | yes |
| 644 | 0.481 | 0.537 | +0.055 | 0.069 | +0.048 | +0.078 | no | yes |
| 655 | 0.620 | 0.613 | -0.007 | 0.072 | -0.007 | +0.074 | no | no |

C1 (load-bearing) 0/5 against 3 required; C2 (lift <= -margin) 0/5. Independently recomputed: mean lift +0.0178, SD 0.043, SE 0.019, t(4) = 0.93 against zero; the mean sits **2.8 SE below the margin** (paired per-seed t(4) = -2.73, one-sided p = 0.026). Rule-input-column persistence rises on 4/5 seeds by +0.07 to +0.17; summary-input columns are flat. `live_rule_state_zero_frac` 0.0-0.014 (the trivial-lift path is closed). The label is the driver's pre-registered informative-null branch.

**Two further facts the cells carry** (surfaced by the red team): (i) against 1020's C2 midpoint `(floor + ceiling)/2` = 0.586-0.603, seeds 622/633/644 sit below in BOTH arms and 611/655 above in both -- a bit-for-bit reproduction of 1020's 3-of-5 on the identical seeds, now with the replay mismatch controlled; (ii) the two arms' TRAINED heads diverge measurably (fresh-select flips 84/373 vs 70/373 on seed 644, 19/186 vs 13/186 on 622, 6/200 vs 9/200 on 611) across 70 online P1 episodes while per-episode returns are bit-identical on 5/5 seeds.

### 2.2 V3-EXQ-1029 (PASS)

One yoked group of 8 runners per seed on private RNG streams, every runner stepped on the reference runner's observation each tick: AUTH_OFF x {intact, rule-ablated}, AUTH_ON x {intact, ablated} (`use_modulatory_selection_authority=True`, gain 0.5, basis range), MAG x {intact, ablated} (authority OFF, lateral_pfc bias x50 applied AFTER its tanh bound), two self-yokes. Head at init (untrained) -- stated scope. 60 warm-up + 60 scored episodes. DV per pair: fraction of raw-identical co-fresh ticks on which `argmin(last_scores)` differs. E3 never commits in this configuration (committed_fraction 0.0 on all 40 runners), so the argmin is E3's top preference; the multinomially sampled action is recorded as secondary.

**Readiness 5/5 seeds** (self-yokes 0 divergent ticks of 2624-2836; head-level rule-ablation flip fraction 0.16-0.41 over intact runners, gate min 0.162 >= 0.01; authority active 100 percent; raw-identical co-fresh ticks 283-414 per pair >= 50; authority_only argmin divergence 0.34-0.81 >= 0.02). The raw-identical filter retained 100 percent of co-fresh ticks in all 35 pair-seed cells: state echo was prevented by the observation-yoking, not by the filter.

| Seed | raw E3 range | \|lpfc bias\| | bias/range | headroom to 0.1 bound | OFF pair | ON pair | MAG x50 pair | x50 vs native (both OFF) | authority ON-vs-OFF | sampled-action div (ON pair) | authority scale factor |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 611 | 5.59 | 0.022 | 0.0040 | 4.5x | 0/283 | 74/283 = 0.261 | 0/283 | 1/283 | 0.809 | 0.053 | 755 |
| 622 | 66.6 | 0.025 | 0.0004 | 4.0x | 0/295 | 8/295 = 0.027 | 0/295 | 3/295 | 0.342 | 0.010 | 6543 |
| 633 | 2.85 | 0.0037 | 0.0013 | 27x | 0/347 | 5/347 = 0.014 | 6/347 = 0.017 | 24/347 | 0.597 | 0.000 | 72 |
| 644 | 25.4 | 0.040 | 0.0016 | 2.5x | 0/414 | 34/414 = 0.082 | 0/414 | 2/414 | 0.391 | 0.075 | 2976 |
| 655 | 17.2 | 0.030 | 0.0017 | 3.4x | 0/355 | 41/355 = 0.115 | 0/355 | 1/355 | 0.631 | 0.056 | 2040 |

C1 (ON pair >= 0.02) 4/5; C2 (OFF pair <= 0.005) 5/5 -- 0 of 1694 pooled ticks, and 0 of 13857 sampled actions over all ticks; C3 interaction 4/5; C4 (MAG pair >= 0.02) 0/5, 6/1694 pooled. Median authority scale factor 2040 > MAG_GAIN 50 -> the driver's own rule suffixes the PASS `magnitude_test_underpowered`. All independently recomputed from `arm_results[].pairs`.

**Adjudication of C4 (red-team F1).** The substrate bounds |bias| < `bias_scale` = 0.1 (`lateral_pfc_analog.py:154`, tanh at `:479-481`), so a realisable SD-082 head has 2.5x-27x headroom over native; MAG x50 already tested 1.8x-20x BEYOND the bound and the rule-attributable part still moved the argmin on only 6/1694 (the whole readout on 31/1694). The magnitude sub-question is **closed from above by the substrate**: within the bound, readout magnitude alone cannot move E3's ranking -- which is the hypothesis's content. The driver's suffix is correct relative to authority's realised factor (72-6543) and should be read as "under-set vs authority, over-powered vs the substrate". No measurement-debt is owed.

## 3. Claim layer

SD-082 (`design_decision`, `candidate_substrate_landed`, `epistemic_category: standard`, `pending_retest_after_substrate: false`, `diagnostic_evidence_adjudicated: true`, `live_status.evidence.from = failure_autopsy_V3-EXQ-1020_2026-09-11`) asserts a common-mode-invariant, gradient-trainable readout mapping the SD-078 rule_state to the SD-033a per-candidate action bias. **Neither run tests that content.** 1027 tests a rival explanation of the lineage's low training-signal persistence; 1029 tests, with an untrained head, whether the readout's output can reach E3's ranking at all. Both are `non_contributory` to SD-082 and the claim can neither be supported nor weakened by them. `claim_ids` are accurate (SD-082 only; SD-078 is co-registered on the question but not tagged, correctly). Nothing stored moves; SD-082's `standard` carries no stale re-check condition.

## 4. Biological triage

- **1027.** The eligibility-trace analogue (bind credit to the state active at action time) was tested exactly as the 1020 triage named it, and returned a null. Three-factor corticostriatal plasticity binds outcome-credit to synapses that PARTICIPATED in the selected action; this readout's output was empirically inert at selection throughout the lineage (1029: 0/1694 argmin, 0/13857 sampled actions at native magnitude; 1027: diverging trained heads, bit-identical returns). The dependency the biology names was absent to measurement precision -- the missing-dependency signature the skill's Step 4 asks about, and a positive-negative result for the dependency ("selection without a trained read-out to action is inert", sd_082 design doc).
- **1029.** The biological reference is a graded, gated influence of prefrontal rule signals on selection, with the gate regulating the rule signal's authority relative to the primary drive. The substrate's device is a divisive-normalisation-style rescale of the whole modulatory composite to gain x raw range by one scalar (`e3_selector.py` authority block) -- formal, channel-blind, scale-free. Literature analogue present (`targeted_review_sd_082`: Carandini 2012, Louie 2011). Divergence is load-bearing for successor DESIGN, not for SD-082's truth.
- **The formal import that matters most (cluster):** the P1 optimiser's surrogate is `log_softmax(-bias / T)` over the head's OWN output with the action chosen by E3 and one per-episode scalar advantage for every sample (`x1020._reinforce_step`, driver:656-658; the substrate exposes only `bias_head_parameters()` and no substrate-side caller exists -- the loop is driver-owned). With the readout inert at selection to measurement precision, the return is independent of the head's output and the gradient is advantage-weighted imitation of E3. This is a MAGNITUDE fact, not a structural one: with authority OFF the bias is applied as-is (`e3_selector.py:3390`), and at x50 it does move the argmin (31/1694). Biology's credit binding requires participation; the import does not and therefore cannot detect its absence.

`targeted_review_sd_082` exists (8 entries) -> **no `/lit-pull` owed.**

## 5. Four-layer diagnosis

### 5.1 V3-EXQ-1027

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear | SD-082's content not tested; rival explanation of an optimisation reading |
| Biological reference | partial | eligibility-trace analogue tested; null explained by the absent participation dependency |
| Prerequisites | **missing** | the readout's participation in selection (authority OFF) -- the prerequisite the HYPOTHESIS presupposed; measured by 1029 and by 1027's own bit-identical returns |
| Implementation | complete | manipulation reached the DV (direction mismatch 0.50-0.70); buffers/trajectories identical across arms |
| Environment | adequate | matched budget by the leg's own terms; return variance 0.16-0.34 |
| Measurement | adequate | per-seed bracket, headroom on 5/5, per-tensor and per-column splits |
| Integration | isolated | head trains but is decoupled from selection |
| Scale | adequate | mean lift 2.8 SE below the margin (t(4) = -2.73, p = 0.026); a ~0.7x-margin effect is not excluded; the disposition rests on the 0/5 per-seed count |

**Failure-location (GOV-FAILLOC-1): HYPOTHESIS ELIMINATED.** Implementation, Measurement and Environment each adequate, so the null is chargeable to the hypothesis. The `missing` prerequisite is the one the hypothesis presupposed, which is what makes the null informative rather than vacuous. Not REE FAILED.

### 5.2 V3-EXQ-1029

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear | init head, ranking consequence; establishes a NECESSARY CONDITION for SD-082's consequence to be observable |
| Biological reference | partial | gated graded influence vs channel-blind scalar rescale |
| Prerequisites | present | authority block engaged 100 percent; CRF matured |
| Implementation | complete | yoked 8-runner design, self-yokes bit-identical whole-run |
| Environment | adequate | raw E3 range varies 23x across seeds (2.85-66.6) -- a finding, not a defect |
| Measurement | adequate | C1/C2 clean; the magnitude question is closed from above by the 0.1 bound (MAG x50 over-powers it); under-set only vs authority's factor. Recording gap: per-channel modulatory composition |
| Integration | partially coupled | couples to selection only under authority, as one component of a rescaled composite |
| Scale | adequate | 283-414 raw-identical ticks per pair, 5/5 seeds |

**Failure-location: PASS, none.** No MEASURES debt remains after F1.

### 5.3 Epistemic category

Both targets: `standard` (in the `VALID_EPISTEMIC_CATEGORIES` enum). 1027's failure mode is "rival eliminated"; 1029 establishes a configuration precondition. Neither asserts suppression. Per-claim: SD-082 `standard` (unchanged). `recommended_diagnostic_evidence_adjudicated: true` (already true on SD-082).

## 6. Cluster pattern

| Experiment | Hypothesis | Negative-control / absolute | Discrimination | Read |
|---|---|---|---|---|
| V3-EXQ-1027 | H-replay-rule-state-mismatch | R1-R3 all green; noise floor / synth ceiling bracket valid 10/10 | C1 0/5 (lift vs 0.25 x bracket) | **eliminated** on the pre-registered bar; residual is the input-structure signature |
| V3-EXQ-1029 | H-selection-authority-bounded | self-yokes 0/2624-2836; OFF pair 0/1694 | C1 4/5, C2 5/5; C4 0/5 (closed from above) | **confirmed**; magnitude alone cannot suffice within the bound |

**Not two independent results -- one structural property.** The credit-assignment leg nulls and the intrinsic-architecture leg confirms; together they put the binding constraint UPSTREAM of both credit assignment and the learning-signal legs: in the lineage's configuration the readout's output is empirically inert at selection (a magnitude fact), so the REINFORCE signal every P1 run in 822f/1020/1027/1028 trained on is, to measurement precision, advantage-weighted imitation of E3, not reinforcement of the readout's consequences. 1027's fix could not matter because there was no measurable consequence-credit to mis-assign. This is a training-regime property of the whole lineage -- not a substrate ceiling, not a defect in any one driver.

Two readings, both live: `training_regime_causally_inert` (design implication: P1 under authority ON with co-summed channels controlled) and `authority_channel_confound` (authority amplifies the whole modulatory composite -- authority ON vs OFF alone moves the argmin on 34-81 percent of ticks, of which the rule-attributable share is 1.4-26 percent, and 0-7.5 percent of sampled actions).

## 7. Learning extracted

1. **H-replay-rule-state-mismatch eliminated at matched budget on the pre-registered bar.** +0.018 +/- 0.019 against margins of 0.069-0.077; 2.8 SE below the margin (p = 0.026); a by-construction randomisation would have recovered a large fraction of the 0.27-0.31 bracket, it recovered ~6 percent. Seeds 622/644 carry small positive lifts (+0.070, +0.055), three seeds are null or negative; a sub-margin residual (~0.7x) is not excluded.
2. **The residual is input structure, not credit.** Rule-column persistence +0.07 to +0.17 on 4/5 seeds with summary columns flat is the driver's own pre-registered non-credit route (one shared rule_state makes rule-column gradients collinear within an update; per-sample rule_state breaks that). The queue-time red-team F3 fix is what kept this from reading as support.
3. **1027 reproduces 1020's C2 majority on the identical seeds** (622/633/644, both arms, below the 0.586-0.603 midpoints) with the credit path controlled: the persistence-low reading is robust to the replay path, and SEED IDENTITY is now the candidate explanatory variable -- a confound any successor must pre-register against.
4. **Within-1027 proof of behavioural inertness with TRAINED heads:** the arms' heads diverge (fresh flips 84/373 vs 70/373 on seed 644) across 70 online P1 episodes while per-episode returns stay bit-identical on 5/5 seeds -- independent of 1029's init-head measurement, and covering the trained-head magnitude regime 1029 did not run.
5. **H-selection-authority-bounded confirmed quantitatively.** Native inertness is a magnitude fact (bias/range 0.0004-0.0040 -> 0/1694 argmin, 0/13857 sampled actions; the bias is applied as-is with authority OFF and moves the argmin on 31/1694 at x50), not a tanh fact (|bias| at 4-40 percent of the 0.1 bound, linear region). The raw E3 range varies 23x across seeds, so a fixed-magnitude readout's inertness is seed-dependent -- which is what authority's range-normalisation is for.
6. **The magnitude sub-question is closed from above by the substrate.** Realisable headroom is 2.5x-27x; MAG x50 exceeded it by 1.8x-20x and returned 6/1694. Within the bound, magnitude alone cannot suffice. No measurement-debt; a successor magnitude arm at authority's factor (|bias| 0.27-262) could not bear on SD-082.
7. **Authority is a blunt instrument.** One scalar rescales the whole modulatory composite (realised factor 72-6543); the random-init gated_policy bias rides along. Any successor reading behaviour under authority must ablate or record co-summed channels, or its "readout effect" is mostly gated_policy. **Recording gap for successors:** per-channel modulatory composition per tick (the scale factor is recorded).
8. **Training-regime finding (cluster).** Every P1 run in the lineage trained the head as an advantage-weighted imitator of E3. SD-082's design names the intended regime ("(b) reinforcement-style gradient from E3 action outcomes"; "selection without a trained read-out to action is inert"); **no run with the SD-082 consumer engaged** (`rule_readout_consumer=True`) has yet trained the readout in it. About 50 ARC-062/GAP-B-lineage drivers (654a-j, 695, 699*, 700*, 704*, 707*, 708*, 709-714, 719*, 722-724, 728*, 736, 847*, 851, 858, 863, 955, 959) train the pre-SD-082 hard-clamp head under authority gain 2.0 (654a-c at 0.5) -- the successor's GOV-REUSE-1 prior art.
9. **Read-across for V3-EXQ-1028 (not adjudicated here) -- confirming, not correcting.** 1028's driver pre-registers (lines 90-93, 110-112) that with authority OFF the head's bias never changes a committed action, names 1029 as the run that measures it, labels flips with the frozen init head on that basis, and declares its C3 "Correlational by construction at authority OFF ... which is what the hypothesis asserts". 1029 supplies that measurement, so 1028's C3 scoping is licensed. H-learning-signal-noisy remains well-posed (does the imitation gradient accumulate at T=500) and is strengthened by 1027's elimination of its rival.
10. **E3 never commits here** (committed_fraction 0.0, 40 runners). The behavioural consequence of the readout under authority is a change in a multinomial draw's distribution; expect it to stay small unless commitment is engaged.

## 8. Lineage checks

- **Granularity-debt trigger: does NOT fire.** `granularity_debt_cluster.py SD-082`: 6 tagging targets, alignment `unclear=6`, zero `weakened`; both targets here read unclear. Measurement/implementation/configuration debt.
- **Re-derive brake (R1-R3): count 3** (822b / 822c / 822d) against threshold 2, released on their own records by 822f and 1020. Both targets here read `non_contributory` / `standard` with **no build owed**, stamped `re_derive_brake.fired: false, literal_count_meets_threshold: true` (explicit producer release, R3 step 3), so neither adds a hit. **REFUSED:** V3-EXQ-1027a / 1029a same-design letters, a standalone MAG_GAIN re-sweep (the magnitude question is closed from above), any further lettered iteration of 822/1020. **LICENSED:** the running 1028; the successor run below.
- **Stale conditional category:** none on SD-082.

## 9. Repair pathway and routing (CONFIRMED at the Step 8 gate)

Work-graph token: `complex (probe-gated) / puzzle (known rules)` -- the frame (the question's `decision_question`: does the TRAINED readout deliver a candidate-discriminating, argmin-consequential bias beyond init -- registry leg H1, alive) is well-posed, and the missing fact is now precisely located: no run with the SD-082 consumer has trained the readout under a regime where its output reaches selection.

| Target | Routing | Substrate queue | Note |
|---|---|---|---|
| 1027 | `governance-note-only` | `amend` SD-082 (chain + failure record + 1020 record C2-clause disposition) | rival eliminated; nothing to build or re-run |
| 1029 | `queue-experiment` (conditional) | `amend` SD-082 (chain + failure record + training-regime note) | one successor run attached to H1, queue AFTER 1028 lands |

**Successor (CONFIRMED: attach to H1, after 1028; no growth).** Per red-team F2 the drafted "H-consequence-trained-readout" restates the alive registry leg `H1-trained-discriminating-readout` (same argmax-consequential assertion, same trained-minus-init contrast, same inside-init-spread null); the training regime is a MANIPULATION, so the recommended form is a **new adjudicating run for H1** (no denominator growth; `initial_frozen_count` stays 9), with growth to a 10th leg kept only as the user's alternative. Design: 1029's yoked instrument with P1 REINFORCE under authority ON and the gated_policy channel disabled/ablated (or its share recorded), TRAINED head intact-vs-ablated against a FROZEN-INIT copy intact-vs-ablated, DV = trained-pair minus init-pair argmin divergence per seed, null pre-registered from an init-only pilot's spread, the five lineage seeds plus fresh ones with seed pre-registered as a factor, NO magnitude arm at authority's factor (x50 already brackets the substrate bound), per-channel composition recorded every tick, GOV-REUSE-1 disposition against the ARC-062/GAP-B authority-ON family (gain 2.0). New EXQ number; queue only after 1028's confirmed autopsy sets the P1 budget.

**Substrate queue `amend` (SD-082, `implemented_pending_validation`, ready false):** extend `validation_experiment` to name 1027 and 1029 with the cluster read; append both failure_record entries (JSON); disposition the open 1020 record's C2 clause as discharged by 1027 (C3 clause stays open pending 1028; record stays `open`); `severity: corrupting` / `substrate_paths: []` **unchanged** (governance emptied the paths 2026-09-09 on purpose).

**Draft `evidence_quality_note`:** exact text in the JSON `recommended_evidence_quality_note`. NOTE-ONLY, both directions `non_contributory`; nothing stored moves; `live_status.evidence.from` re-pointed at this artifact.

## 10. Frozen ledger (Step 9b) -- applied

- **Mode B resolve** `H-replay-rule-state-mismatch` -> `eliminated` (resolving_runs V3-EXQ-1027, control_passed true, non_degenerate true, met_elimination_bar true, resolved_utc 2026-09-14T13:53:20Z). The gate alternative (leave `alive` as budget-limited) was presented and declined.
- **Mode B resolve** `H-selection-authority-bounded` -> `confirmed` (resolving_runs V3-EXQ-1029, control_passed true, non_degenerate true, met_elimination_bar false, resolved_utc 2026-09-14T19:11:18Z).
- **No Mode A growth** (user-confirmed): the successor attaches to H1's `adjudicating_runs` when /queue-experiment assigns its id. Alternative if the user prefers growth: `H-consequence-trained-readout`, axis learning-signal (constitution), delta 1, 9 -> 10; `growth_restriction` is empty so nothing mechanical stops it.
- Then `build_hypothesis_space.py` + `check_hypothesis_space_integrity.py`; commit registry + three derive-only siblings with the artifact pair.

## 11. Step 7b / 7c

- **Step 7b:** 3 fires (2 entries: C1 carries two queue_ids; C7 one), 0 inapplicable. C1 -- `v3_exq_1028_sd082_learning_signal_extended_budget` (V3-EXQ-1028, the portfolio's legs 2+4) is on disk and unscored: ACTED ON -- it was already the condition on the successor; now named explicitly. C7 -- `live_rule_state_zero_frac` bit-identical across 1027's arms: DISMISSED -- it is a property of the shared episode stream, cited only to close the trivial-lift path, never as an arm discriminator.
- **Step 7c: CONTESTED**, run on **claude-opus-5 (cross-model; drafter claude-fable-5-1)**, reading order JSON -> raw evidence (every headline number recomputed and matched) -> markdown. Seven findings, every citation independently re-verified by the drafter and all accepted:
  - F1 (severe, routing): MAG x50 is applied after the substrate's 0.1 tanh bound (`lateral_pfc_analog.py:154, :479-481`), so it over-powers, not under-powers, the magnitude question; the drafted "gain from authority's factor" successor arm would exceed the bound by 3x-2600x. **Fixed:** C4 re-adjudicated as closed from above; arm dropped.
  - F2 (severe, routing): the proposed new leg restated the alive H1. **Fixed:** successor attached to H1 as an adjudicating run; growth demoted to a gate alternative.
  - F3 (severe, read-across): 1028's driver pre-registers the correlational reading verbatim and names 1029 as its measurement. **Fixed:** read-across rewritten as confirming.
  - F4 (assertion): "no causal loop / never / by construction" was false as stated -- the bias is applied as-is with authority OFF and x50 moves the argmin on 31/1694. **Fixed:** every absolute replaced with the measured statement.
  - F5 (assertion): "3.7 SE" was margin-over-zero; margin-over-mean is 2.8 SE, paired t(4) = -2.73, p = 0.026. **Fixed.**
  - F6 (assertion + routing): "no run has yet trained the readout in it" is false fleet-wide (~50 authority-ON drivers train the pre-SD-082 head). **Fixed:** scoped to the SD-082 consumer; family named as GOV-REUSE-1 prior art.
  - F7 (routing): 1027 reproduces 1020's C2 3-of-5 on the identical seeds with the mismatch controlled -- the C2 clause of the open 1020 failure record. **Fixed:** extracted; amend dispositions it; seed-as-factor added to the successor.
  - In the draft's favour, unused: the within-1027 trained-head inertness proof (now learning 4). Nine hygiene items applied.
  - Attacks that failed: cross-leg substrate provenance; C1 reachability; amend non-duplication; claims.yaml field match; driver-owned training loop.

## 12. Concurrency note

Written from a throwaway worktree off `origin/master` (the shared REE_assembly checkout was diverged: 4 bot-authored IGW regen commits ahead, 14 behind). The registry claim was opened with `--allow-overlap` against `metaworker-chip-20260914-waypoint-consumer-reach-h1`, which holds `hypothesis_space_registry.v1.json` for a DIFFERENT question (`waypoint_field_consumer_reach`); this session's edit is a narrow structural update to `sd082_candidate_discriminating_readout_locus` only, read fresh from origin immediately before writing.
