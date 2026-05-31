# Failure Autopsy: V3-EXQ-483e

- **Scope:** single (references EXQ-483 cohort; does not re-open closed superseded manifests)
- **Status:** confirmed
- **Generated:** 2026-05-31T10:58:34Z
- **Manifest:** `evidence/experiments/v3_exq_483e_sd037_consumer_cascade_4arm/v3_exq_483e_sd037_consumer_cascade_4arm_20260530T195925Z_v3.json`
- **Run id:** `v3_exq_483e_sd037_consumer_cascade_4arm_20260530T195925Z_v3`
- **Queue id:** `V3-EXQ-483e` (supersedes `V3-EXQ-483d`)
- **Machine:** `ree-cloud-2`
- **Claims tagged:** SD-037, MECH-280, MECH-281
- **Outcome:** FAIL
- **Failed criteria:** discrimination (`C2_cascade_engagement`, `C3_lift_vs_baseline`, `C4_action_divergence`)
- **Routing:** implement-substrate (amend SD-037 entry in `substrate_queue.json`)

## 1. Facts reconstruction

Four-arm 2x2 factorial (broadcast_override master x consumer-cascade-gains-active) on PAG-engaging env via SD-036+MECH-279 substrate (`use_gabaergic_decay=True` + `use_pag_freeze_gate=True` in all four arms), 3 seeds (42, 7, 19). Arms:

- `OFF_OFF`: `use_broadcast_override=True` + 4 cascade gains set BUT `override_recruitment_threshold=10.0` pins `override_signal=0` structurally inert.
- `ON_OFF`: `use_broadcast_override=False` (master OFF) -> regulator dormant; cascade flags master-ON but inert.
- `OFF_ON`: `use_broadcast_override=True` default recruitment_threshold so override_signal lifts; but all 4 cascade gains = 0.0 (wired-but-inert baseline).
- `ON_ON`: `use_broadcast_override=True` + all 4 cascade gains > 0 (pfc_eta=1.0, bla_encoding=1.0, cea_amplitude=1.0, beta_interrupt=0.5). The "consumer cascade engaged" arm.

Tier-1 acceptance requires the `ON_ON` arm to clear C1 (cue_fires) + C2_override_signal + C3_approach_commit + C4_goal_active substrate gates AND C2_cascade_engagement (ARM_3/ARM_2 ratios >=1.5x lateral_pfc / >=1.3x bla / >=1.3x cea on >=2/3 seeds) AND C3_lift_vs_baseline (ARM_3 goal_norm_peak > ARM_0 + 0.01 in 3/3 seeds) AND C4_action_divergence (TV(ARM_3, ARM_2) >= 0.05 per seed).

Result: `pass=false`. C1 / C2_override / C3_approach_commit / C4_goal_active PASS. The three discrimination criteria FAIL:

- **C2_cascade_engagement**: 0/3 seeds clear. Per-seed sub-checks:
  - lateral_pfc_ratio: seed 42 = 1.16, seed 7 = 1.08, seed 19 = 1.18 (all below 1.5 threshold)
  - **bla_ratio: 0.0 / 0.0 / 0.0** (BLA module never fires in ANY arm)
  - **cea_ratio: 0.0 / 0.0 / 0.0** (CeA module never fires in ANY arm)
- **C3_lift_vs_baseline**: `C3_lift_count = 0` (zero seeds lifted; previously 1/3 on 483d).
- **C4_action_divergence**: TV(ARM_3, ARM_2) = 0.0 / 0.0 / 0.0 across seeds. No action-distribution divergence at all.

### The load-bearing observation: bit-identical actions

Across every seed, `action_counts` is bit-identical between all four arms:

| Seed | total_steps | action_counts (identical in OFF_OFF / ON_OFF / OFF_ON / ON_ON) |
|---|---|---|
| 42 | 1514 | {0:6, 1:683, 2:4, 3:813, 4:8} |
| 7  | 76   | {0:5, 2:2, 3:9, 4:60} |
| 19 | 1349 | {0:397, 2:912, 4:40} |

Goal_norm_peak shows the same near-bit-identical pattern:

| Seed | OFF_OFF | ON_OFF | OFF_ON | ON_ON |
|---|---|---|---|---|
| 42 | 0.18358927 | 0.18358927 | 0.18989914 | 0.18989914 |
| 7  | 0.21524085 | 0.21524085 | 0.21524085 | 0.21524085 |
| 19 | 0.23919561 | 0.23919561 | 0.23919561 | 0.23919561 |

The OFF_OFF vs ON_OFF pair (broadcast_override toggled, all cascade gains held) and OFF_ON vs ON_ON pair (cascade gains toggled, broadcast_override held) BOTH produce bit-identical action distributions and near-bit-identical goal_norm_peak within each seed. The slight goal_norm_peak lift in seed 42 between OFF_ON (0.18989) and OFF_OFF (0.18358) is the only signal of the override path doing anything to `effective_drive` -- and it does NOT survive the cascade gain toggle (OFF_ON == ON_ON exactly).

### Consumer-module silence

In every single one of the 12 runs (including the four ON_ON runs where SD-037 broadcast saturates AND all 4 consumer cascade gains are > 0):

- `bla_encoding_gain_peak = 0.0`
- `cea_mode_prior_peak = 0.0`
- `cea_fast_prime_peak = 0.0`
- `dacc_bias_nonzero_steps = 0`
- `pag_release_count_end = 0`
- `beta_release_count = 0`

`override_signal_nonzero_steps` is exactly `total_eval_steps` in every `OFF_ON` and `ON_ON` seed (1514, 76, 1349 -- 100% saturation). SD-037 itself fires correctly. What does not fire is anything downstream: BLA, CeA, dACC, PAG freeze, urgency-interrupt are all silent at their own input thresholds.

`lateral_pfc_rule_state_norm_peak` is the only consumer that moves at all: seed 42 0.339 -> 0.398 (1.17x), seed 7 0.125 -> 0.135 (1.08x), seed 19 0.372 -> 0.445 (1.20x). The override path through `eff_eta = update_eta * (1 + override_pfc_eta_gain * override_signal)` does deliver a marginal EMA acceleration on rule_state -- but at this magnitude it doesn't change any selected actions (TV=0.0).

## 2. Claim-layer map

- **SD-037** `regulators.broadcast_override`. status: candidate. v3_pending. pending_retest_after_substrate=true (carried from 483d). Substrate implemented 2026-04-25; consumer-cascade amend landed 2026-05-30 (the very work this experiment validates). The broadcast itself fires correctly at saturation. What fails is the cascade's ability to express itself behaviourally because each consumer has its own input-side gating that the env baseline does not clear.
- **MECH-280** `pag.lh_override_projection`. status: candidate. v3_pending. PAG `alpha_override` is wired AND the env config now includes `use_pag_freeze_gate=True` + `use_gabaergic_decay=True` (the 483d autopsy's recommended PAG-engaging substrate). `pag_release_count_end = 0` everywhere -- PAG freeze-gate is enabled but never enters a freeze state. The product `z_harm_a * duration_above_threshold` never crosses theta_freeze=2.0 because z_harm_a does not climb high enough for long enough in fishtank under default agent behaviour. Claim cannot express itself.
- **MECH-281** `orexin.drive_arousal_coupling` (motor-coupling axis). status: candidate. v3_pending. All four MECH-281 consumer sites are now wired (PFC eta gain, BLA encoding gain, CeA amplitude gain, beta-interrupt gain) per the 2026-05-30 amend. BLA/CeA/dACC consumer-output peaks are 0.0 across all arms; beta_release_count is 0. The motor-coupling gains amplify `(1 + gain * override_signal)` multiplied by consumer-module outputs that remain at zero baseline. Amplifying zero = zero. action_counts bit-identical across the cascade-engaged axis confirms zero behavioural effect.

Did the experiment test the claims under conditions where they could express themselves? **No -- one layer deeper than 483d.** The 483d autopsy diagnosed "consumers unwired"; 483e wires them per that recommendation, but each consumer module has its own INPUT-side gating that the validation env does not clear at baseline:

- BLA `arousal_threshold_on = 0.4` (Roozendaal inverted-U on-threshold on z_harm_a norm). Below threshold -> encoding_gain stays at 1.0 (or 0.0 in the peak measurement; the module zero-pegs).
- CeA `fast_route_threshold = 0.5` (Mendez-Bertolo fast subcortical route). Below threshold -> mode_prior + fast_prime stay at 0.0.
- dACC pe-driven bundle composition requires `pe = ||z_harm_a - E2_harm_a(z_harm_a_prev, a_prev)||` magnitude. Fishtank baseline produces near-zero pe.
- PAG freeze-gate requires `z_harm_a * duration_above_threshold > theta_freeze = 2.0`. Fishtank baseline z_harm_a is too low for too short.
- MECH-091 urgency-interrupt threshold attenuation works only when z_harm_a magnitude is high enough to fire the urgency block in the first place.

SD-037 broadcast amplifies multipliers on whatever the consumers produce. With consumers at zero baseline, `output * (1 + gain * override_signal) = 0 * anything = 0`. The override has nowhere to land EVEN WITH the cascade fully wired.

## 3. Biological-reference triage

Closest mammalian reference: orexin / hypocretin multi-target broadcast. Lit-pull `targeted_review_orexin_kinetics/synthesis.md` already supports the multi-target architectural commitment (Mileykovskiy 2005, Lee 2005, Karnani 2020, Johnson 2012, Carter 2009). The biology says: orexin gain modulates downstream targets THAT ARE ALREADY RESPONDING TO THEIR OWN INPUTS. BLA / NAc / mPFC / LC don't generate behavioural output from orexin alone -- orexin sets their gain on signals they receive from their own afferents. If their afferents are silent, orexin can rise without behavioural consequence.

The translation is faithful. What is missing is the upstream prerequisite: the env must drive z_harm_a / pe / sustained-threat z_world signatures into the regimes that recruit the consumer-module input gating. The 483d autopsy named this as "wrong pressures." 483e clears the PAG-engaging substrate flags but does NOT clear the actual signal magnitudes the substrates need to act on.

This is the load-bearing finding: the failure resembles what would happen biologically if you injected orexin while the rest of the brain was at rest -- arousal-modulator output would rise, BLA / CeA / dACC / PAG would remain silent because their own input afferents are quiet, and behaviour would not change. The biology predicts NO behavioural divergence under these conditions. 483e is consistent with the biology; it does not falsify it.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear -- test cannot express the claim | wiring fully landed but consumers' own input thresholds not cleared; broadcast amplifies zero |
| Biological reference | clear | orexin multi-target broadcast; literature predicts no behavioural divergence when target afferents are quiet |
| Prerequisites | partially missing | BLA arousal_threshold + CeA fast_route_threshold + dACC pe magnitudes + PAG theta_freeze sustained-z_harm_a duration -- none cleared at fishtank env baseline |
| Implementation completeness | complete | SD-037 broadcast + 4-channel cascade + PAG alpha_override + SalienceCoordinator slot all wired per 2026-05-30 amend |
| Environment adequacy | wrong pressures | fishtank baseline z_harm_a / pe / sustained-threat profile sits below the input gates of every wired consumer |
| Measurement | adequate | C2_cascade ratios + C3_lift + C4 TV are the right discrimination criteria; they correctly read zero behavioural divergence |
| Integration | partially coupled but inert | cascade wired AND broadcast saturated AND env nominally PAG-engaging, yet downstream is silent end-to-end |
| Scale / capacity | adequate | not a model-capacity issue; lateral_pfc EMA does respond (1.17x growth) but at sub-discrimination magnitude |

**Recommended `epistemic_category`:** `substrate_ceiling`. Same shape as 483d but one architectural layer deeper. The substrate is V3-tractable in principle -- BLA / CeA / dACC / PAG threshold defaults are config knobs (e.g. `bla_arousal_threshold_on`, `cea_fast_route_threshold`, `pag_theta_freeze`); the env can carry a sustained-threat curriculum (analog to SD-029 `scheduled_external_hazard`). What is missing is the calibration that makes the consumer input gates loadable from fishtank baseline signal magnitudes, OR an env enrichment that lifts z_harm_a into the regimes the consumers expect.

## 5. Cluster context (single-scope reference only)

The EXQ-483 chain is a six-iteration thread on the same architectural surface (483 / 483a / 483b / 483c / 483d / 483e). 483d's autopsy classified the FAIL as substrate_ceiling and routed to implement-substrate amend SD-037 with the recommendation to wire the deferred PFC / BLA / beta-gate consumers per MECH-281 implementation_note. The 2026-05-30 amend landed exactly that consumer-cascade wiring. 483e is the validation pass on the amended substrate, and it now exposes a fresh substrate-ceiling shape ONE LAYER DEEPER:

- 483d FAIL shape: "regulator fires + consumers unwired" -> amplifying nothing.
- 483e FAIL shape: "regulator fires + consumers wired + consumer input gates not cleared" -> amplifying zero.

Both are substrate_ceiling and both route to implement-substrate, but the next substrate step is at the consumer-input threshold layer + env-pressure layer, NOT at the cascade-wiring layer (that work is done).

Per user direction (confirm option 1 via AskUserQuestion 2026-05-31T10:58Z), do not re-open closed superseded manifests; this autopsy applies to 483e only and the 483 cluster is referenced for context.

Note on the broader substrate_uniform cluster (540/590a/591/598/603/610): 483e is NOT the same cluster shape. That cluster shows "negative-control-passes-discrimination-fails" on goal-pipeline / z_goal-zero substrates and is rooted in the goal-pipeline training-regime substrate. 483e is a distinct shape -- "broadcast saturates + consumer cascade silent at input thresholds" -- and belongs in the SD-037-specific substrate-ceiling thread, not folded into the substrate_uniform cluster.

## 6. Learning extracted

- The wired-but-inert pattern is now confirmed ONE LAYER DEEPER at the SD-037 validation surface. 483d's recommended substrate work (consumer-cascade wiring) landed correctly. 483e shows that wiring alone is not sufficient: each consumer has its own input-side gating that the validation env does not clear.
- BLA / CeA / dACC / PAG modules are all on, all listening for their own input signals, and all silent in fishtank baseline. The SD-037 multiplicative gain pattern `output * (1 + gain * override_signal)` makes this architecturally inevitable: if `output = 0` at baseline, the broadcast cannot generate behavioural lever no matter how saturated it is.
- The 483d substrate_queue prediction ("consumer-cascade work would deliver the lever") is now closed and falsified. The next prediction must name the consumer-input threshold layer + env-pressure layer.
- The `lateral_pfc_rule_state_norm_peak` 1.08-1.18x growth across the cascade axis is the only signal that the override path delivers ANYTHING downstream. It is below the C2 discrimination threshold (1.5x) but it is non-zero and consistent across seeds. This is the only consumer site that does not require an input threshold crossing -- the rule_state EMA accelerates under any non-zero source. It also indicates the wiring is sound: when a consumer's input gate is open, the broadcast does land. The other three consumer-output peaks reading 0.0 is the input-threshold story, not a wiring story.
- 483e is structurally consistent with the 483d substrate_ceiling reading at the architectural level. It is not the substrate_uniform cluster (540/590a/591/598/603/610 cluster has a different shape on a different substrate).

## 7. Recommended `evidence_quality_note` (governance to write -- do not write here)

> EXQ-483e (supersedes 483d). Substrate broadcast fires correctly: override_signal_nonzero_steps saturates at total step count in every OFF_ON / ON_ON seed (C2_substrate cleanly PASS). The 2026-05-30 MECH-281 consumer-cascade amend (four new gain knobs landed: pfc_eta / bla_encoding / cea_amplitude / beta_interrupt) is fully wired in ARM_3 ON_ON but produces zero behavioural divergence: bla_encoding_gain_peak = 0.0 / cea_mode_prior_peak = 0.0 / cea_fast_prime_peak = 0.0 / dacc_bias_nonzero_steps = 0 / pag_release_count_end = 0 / beta_release_count = 0 across ALL 12 runs (including ARM_3 ON_ON arms in every seed). action_counts BIT-IDENTICAL across all four arms within each seed and goal_norm_peak near-bit-identical (OFF_OFF vs ON_OFF identical, OFF_ON vs ON_ON identical). The only consumer that responds at all is lateral_pfc rule_state EMA (1.08-1.18x growth, below the 1.5x C2 discrimination threshold). Diagnosis: SD-037 multiplicative gain pattern requires consumer-module input gates to be crossed first; with consumer-output baselines at zero, broadcast saturation cannot generate behavioural lever. Substrate-ceiling at the consumer-input-threshold layer + env-pressure layer (one architectural layer deeper than 483d). Closes the SD-037 substrate_queue 483d prediction ("consumer-cascade work would deliver the lever") -- falsified. Hold pending consumer-input-threshold recalibration AND env enrichment that drives z_harm_a / pe above BLA arousal_threshold_on=0.4 + CeA fast_route_threshold=0.5 + PAG theta_freeze sustained-product=2.0 + dACC pe-magnitude thresholds. Pair with pending_retest_after_substrate. Apply per-claim: SD-037 evidence_direction non_contributory; MECH-280 / MECH-281 evidence_direction non_contributory (claims could not express themselves -- their targets remained silent at the consumer-input layer). Set pending_retest_after_substrate: true on all three. epistemic_category: substrate_ceiling. Routing: implement-substrate (amend SD-037 substrate_queue entry with new failure_record naming the consumer-input-threshold shape; deferred follow-on: consumer-module threshold default recalibration AND/OR SD-029-style sustained-threat env curriculum). Artifact: evidence/planning/failure_autopsy_V3-EXQ-483e_2026-05-31.{md,json}.

## 8. Recommended routing -- implement-substrate (amend SD-037 entry)

The SD-037 substrate_queue entry already exists and is `implementation_status: implemented` (consumer-cascade amend landed 2026-05-30). The autopsy emits a `failure_record_entry` for governance to append to its `metric_trajectory.observations`, plus an updated `current_blocker` / `prediction` capturing the consumer-input-threshold + env-pressure layer.

The amend specifically does NOT propose new SD-037 substrate code changes. It identifies that the next substrate work is at:

- **Consumer-input thresholds** (config-knob recalibration on BLA / CeA / PAG / dACC modules):
  - `BLAConfig.arousal_threshold_on` (default 0.4; Roozendaal-anchored, may be too high for fishtank baseline)
  - `CeAConfig.fast_route_threshold` (default 0.5; Mendez-Bertolo-anchored)
  - `PAGFreezeGateConfig.theta_freeze` (default 2.0) + `duration_input_threshold` (default 0.4)
  - dACC pe scaling / threshold defaults
- **Env enrichment** -- a sustained-threat curriculum analogous to SD-029 `scheduled_external_hazard` but for z_harm_a magnitude (rather than hazard-event relocation), driving the affective stream above arousal / fast-route / freeze thresholds during scheduled windows. Could also be co-instantiated with SD-022 scheduled-injection extension (limb damage path already lands directly on harm_obs).

These are two orthogonal substrate axes; the next behavioural EXQ (`V3-EXQ-483f` reserved) should be queued only after at least one of them is empirically substrate-readiness-validated (consumer thresholds raise BLA/CeA peak > 0 under env baseline, OR env curriculum lifts z_harm_a above current thresholds without recalibrating them).

Deferred behavioural-validation note: 483f cannot be a simple re-run of 483e. It requires either (a) a consumer-threshold-recalibrated agent on the same env, with substrate-readiness diagnostics proving BLA/CeA actually fire, OR (b) a curriculum-engaged env where sustained-threat windows are scheduled, with diagnostic confirmation that z_harm_a clears the consumer-input thresholds during those windows. The current `483e` lineage of "wire one more consumer level and re-run on fishtank" cannot succeed without one of these architectural changes.

## 9. recommended_substrate_queue_entry payload

Action: `amend`. Target SD-037 (already in substrate_queue). Governance applies the `failure_record_entry` and updates `current_blocker` / `prediction`. See the JSON artifact's `recommended_substrate_queue_entry` block for the exact payload to apply.

## 10. Note on the broader review queue

Per user direction (single scope on 483e), other unreviewed items on `pending_review.md` are NOT actioned in this autopsy. Flagged in the session report; routed separately.
