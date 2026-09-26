# Failure autopsy -- V3-EXQ-1109 (DCD2 probe F: freeze / veto earliest edge) -- CONFIRMED

- **Status:** `confirmed` 2026-09-26T18:01:31Z. The user answered the Step 8 gate live (AskUserQuestion via orchestrator `orchestrate-20260924-breakthrough-c2`): **route B** was confirmed and the category was accepted as proposed (sec 11). The artifact was first staged at `498d4c094a`. No registry, `claims.yaml` or `substrate_queue.json` write was made by this skill; `/governance` applies the amend and chips the follow-on.
- **Generated:** 2026-09-26T17:35:48Z by `bt0926-ap1109` (chip `chip-20260926-autopsy-v3-exq-1109`).
- **Target:** `v3_exq_1109_pag_freeze_veto_earliest_edge_20260926T161927Z_v3`. Outcome FAIL, `experiment_purpose: diagnostic`, `claim_ids: []`, `evidence_direction: non_contributory`, ree-cloud-2, 4406 s, seeds 47/48/49.
- **Code read:** driver `experiments/v3_exq_1109_pag_freeze_veto_earliest_edge.py` (queued at ree-v3 `89976eb7ec`, byte-identical at the run's substrate commit `22aadc0c9d`). Every `file:line` below is against a detached worktree at `22aadc0c9d`.
- **Context read:**
  - `dynamic_control_discrimination_plan_20260926.md`, sec 1-6;
  - the V3-EXQ-1107, 1106 and 1090 autopsies;
  - the `substrate_queue.json` rows for MECH-279 and `f_dominance_conversion_ceiling`;
  - `Q086-zharma-calibration-vs-ecological`;
  - `docs/architecture/harm_to_threat_causal_credit.md`, relayed as input by the orchestrator.
- **Probes (Mac, small).** All three are under `.scratch/breakthrough-20260924/ap1109/probes/`, each with a `.out.txt`. They use the driver's own `_build_dual_cue_env`, `_make_scaffold_cfg(False)` and `_env_seeds` at the deployed env dims (12x12, 4 hazards, P2 config).
  - `ap1109_life_budget_probe.py`: env-only, scripted policies, final eval env seeds.
  - `ap1109_candidate_contrast_probe.py`: env-only, oracle one-step harm per candidate.
  - `ap1109_zharms_vs_zharma_probe.py`: an UNTRAINED agent built from the driver's `_make_config`, on the driver's final walk env seeds and walker RNG. It reproduces the run's final `R2_in` exactly (0.07532 / 0.1883 / 0.3184).

## 1. Facts (no interpretation)

**Dry-run gate.** `check_dry_run_citations.py` was run over the run_id and over V3-EXQ-1109/1107/1106/1090: 0 dry. `validate_recording.py` reports OK.

**Pre-registered verdicts:**
- F0 `F0_INDETERMINATE` (seed classes HOLDS / INDETERMINATE / INDETERMINATE).
- F1 `F1_BOTH_COLLAPSE_F0_INDETERMINATE` (BOTH on 3/3).
- F3 `F3_H3_LIVE` (NO_ORGANISM_EFFECT x2, VETO_NO_CANDIDATE_CONTRAST x1).
- Outcome FAIL, because F0 was not decisive.

| readout (ARM_WALK unless noted) | seed 47 | seed 48 | seed 49 | mean |
|---|---|---|---|---|
| R2_dist init / p0 / final | 0.459 / 0.328 / 0.066 | 0.310 / 0.325 / 0.139 | 0.253 / 0.322 / 0.213 | 0.341 / 0.325 / 0.139 |
| R2_in (input ceiling) init / p0 / final | 0.451 / 0.311 / 0.075 | 0.295 / 0.301 / 0.188 | 0.261 / 0.327 / 0.318 | 0.336 / 0.313 / 0.194 |
| R2_hf final (z / input) | 0.336 / 0.340 | -0.009 / 0.022 | 0.142 / 0.257 | |
| R2_fid final | 0.997 | 0.998 | 0.981 | 0.992 |
| R2_norm_dist init / p0 / final | -0.036 / -0.160 / -0.040 | -0.008 / 0.062 / -0.039 | -0.013 / -0.087 / 0.021 | ~0 |
| dead encoder units init / final | 0.375 / 0.422 | 0.484 / 0.500 | 0.516 / 0.500 | 0.458 / 0.474 |
| walk mean \|\|z_harm_a\|\| init / p0 / final | 0.284 / 4.189 / 3.815 | 0.344 / 4.259 / 4.029 | 0.309 / 3.105 / 2.596 | |
| min walk norm / theta (0.8), final | 4.60 | 4.96 | 2.68 | |
| within-life rel SD of norm, final | 0.0096 | 0.0092 | 0.049 | |
| walk life, final | 11.7 | 12.1 | 13.1 | 12.3 |
| FZ_ON life / freeze_active, final | 5.917 / 1.0 | 5.917 / 1.0 | 5.917 / 1.0 | |
| FZ_OFF life init / p0 / final | 68.0 / 30.0 / 15.0 | 74.7 / 10.7 / 11.75 | 6.0 / 7.7 / 8.17 | |
| FZ_OFF blocked-move fraction init / final | 0.87 / 0.34 | 0.86 / 0.33 | 0.00 / 0.07 | |
| FZ_OFF true-hazard / contamination / resource contacts, final | 0 / 7 / 0 | 6 / 0 / 3 | 0 / 17 / 0 | |
| freeze-OFF arms: beta_elevated = e3_committed fraction, init / p0 / final | 0 / 1.0 / 1.0 | 0 / 1.0 / 1.0 | 0 / 1.0 / 1.0 | |
| VETO_OFF entropy (bits) | 1.59 | 1.55 | 1.22 | 1.45 |
| veto fire rate (per CANDIDATE, ~32/tick) | 0.063 | 0.007 | 0.038 | 0.036 |
| safety No-Go applied / episodes diverged (of 12); divergence steps | 222 / 3; steps 1,0,2 | 24 / 0 | 83 / 1; step 1 | |
| producer within-tick harm spread p50 | 0.033 | 0.025 | 0.0039 | |
| VETO_OFF true-hazard contacts | 0 | 1 | 0 | |

**Env-only life probe** (driver's final eval env seeds, 12 episodes per seed). The wall-press row is from the red-team's probe.

| scripted policy | mean life (s47 / s48 / s49) | health-loss share from `hazard_approach` |
|---|---|---|
| STAY-only | 5.92 / 5.92 / 5.92 | 0.38-0.42 (the rest is self-contamination) |
| uniform random over 4 moves | 11.5 / 10.8 / 11.0 | 0.88-0.89 |
| oracle min-field (forced to move) | 15.9 / 15.1 / 16.0 | 0.96-0.97 |
| oracle forager (forced to move) | 16.5 / 15.5 / 13.8 | 0.95-0.97 |
| wall-press | 200 (cap) / 200 / 183.8 | ~0; a blocked move skips the movement block (causal_grid_world.py:2563-2564) |

- The hazard field is 0.44-2.33 on every cell, against an approach threshold of 0.15. Every successful move costs `0.1 x field` of health (causal_grid_world.py:2718-2743).
- Oracle within-tick one-step harm spread between candidates: p50 0.021-0.024. A contact-harm candidate exists on 3.4-4.6% of ticks.

**Stream-choice probe** (untrained agent; ridge on the final walk; held-out split by episode parity):

| quantity | R^2 -> distance | R^2 -> hazard field | NORM R^2 -> distance | NORM relSD |
|---|---|---|---|---|
| `harm_obs` (z_harm_s input: hazard/resource field views) | 0.69-0.80 | 0.54-0.75 | 0.50-0.66 | 0.22-0.24 |
| `z_harm_s` (32-d; `LatentState.z_harm`) | 0.57-0.76 | 0.61-0.78 | 0.42-0.66 | 0.15-0.19 |
| `harm_obs_a` (7-d SD-022 body damage) | 0.07-0.32 | 0.02-0.34 | ~0 | 0.58-0.62 |
| `z_harm_a` (16-d; what the PAG gate reads as a norm) | 0.07-0.32 | 0.02-0.35 | ~0 | 0.004-0.010 |

Trained `z_harm_s` is unmeasured: the run did not save weights.

## 2. Claim layer

The target is claim-free, so there is no claims.yaml row to move. `bears_on` carries:
- `GFLAG-0508`, `substrate_queue:MECH-279` and `substrate_queue:f_dominance_conversion_ceiling`, reused verbatim from the 1107 and 1090 autopsies;
- `dynamic_control_discrimination_plan_20260926:family_F` (new).

The read-across to ARC-155, ARC-156, Q-111, MECH-279, MECH-280, MECH-598/599/Q-113 and Q086 is in sec 7 and in the JSON `read_across_not_adjudicated`. It is not adjudicated here.

## 3. What each pre-registered verdict can and cannot say

1. **F0 INDETERMINATE is bounded by its own rule.**
   - The HOLDS bar (0.25) is not normalised by the input ceiling. Seed 48's best input R^2 is 0.188, so HOLDS was unreachable there even for a perfect encoder.
   - init, p0 and final use different walk env seeds and walker RNG (driver:941-943). The init-vs-trained comparison is therefore unpaired.
2. **F1 BOTH is a valid readout.**
   - LOCK was reachable: the rule exempts wall-pressing from collapse (driver:114-116, 1027-1031), and wall-pressing lives to the cap tax-free.
   - *Withdrawn claim, kept for the record:* the first draft asserted "BOTH forced by construction". Its oracle policies were forced to move every tick and omitted the tax-free wall-press policy that the untrained agent actually used. The Step 7c red-team found this.
3. **F3 H3_LIVE is fall-through.**
   - EFFECTIVE needs >= 5 OFF true-hazard contacts; the run had 0 / 1 / 0.
   - The per-candidate veto readouts also do not record the commit latch, which decides whether a No-Go can reach execution (sec 4).

## 4. The headline readouts, explained

- **R2_dist 0.139 trained vs 0.341 untrained.** About 70% of the 0.20 drop is the input ceiling falling over the same unpaired samples (0.336 -> 0.194).
  - The z-minus-input gap is +0.005 at init, +0.012 at p0 and -0.055 at final.
  - So there is a modest real transmission loss at final. "Training destroyed the hazard information" is not supported.
  - The confirmer is a paired walk.
- **Fidelity 0.992.** The encoder follows its input everywhere. At final it transmits 67-87% of the input's distance R^2.
- **Input R^2 0.194.** The affective stream is the weak link. Body damage accrues only on moves that take harm, and heals every step (causal_grid_world.py:2901-2921), so it tracks proximity only through history.
- **47% dead units.** Already 46% at the untrained init, so this is not a training effect. The likely cause is input scale (damage entries ~0-0.05); that is a D1 inference and was not probed.
- **Resting norm 2.68x theta.**
  - During P0, `||z_harm_a||` inflates ~13x as an offset.
  - Its within-life relative SD is 0.4-5%, and R^2(norm -> distance) is ~0 at *every* checkpoint, the untrained one included.
  - The PAG gate reads exactly this norm (agent.py:11478-11479), so it is input-independent (manifest `gate_input_independent: true`).
  - No theta can make that gate proximity-contingent.
  - The sensory stream `z_harm_s` carries what `z_harm_a` lacks: R^2 0.57-0.76, and its norm 0.42-0.66, at init. So the information exists one stream over, and **this is a stream-choice defect at the consumer**. It is also the SD-011 / SD-020 / MECH-258 contract named in the harm-to-threat page.
- **What kills trained freeze-OFF lives.**
  - The cause is the ambient hazard-field tax on successful moves, plus self-contamination when standing still. It is not hazards and not the freeze.
    - FZ_OFF true-hazard contacts are 0/6/0.
    - For moving policies, hazard_approach is 88-97% of health loss.
    - Seed 49's policy STAYs 79% of the time, and about half of its loss is self-contamination.
  - FZ_OFF life (11.6) equals the random-walk life (12.3 in-run; 11 scripted).
  - The untrained freeze-OFF agent lived 68.0 and 74.7 steps on seeds 47 and 48 by wall-pressing. **Training reduced freeze-OFF life on 2 of 3 seeds**: blocked moves fell from 0.87 to 0.34 and 0.33, as the policy moved into taxed cells.
  - FZ_ON life is 5.917 on all three seeds, equal to the STAY-only life of 5.92. The freeze-ON arm *is* a STAY-only policy.
- **Training-time lock: NOT established.** The freeze is ON in the training config (driver:428) and locked in EVAL by p0. But training-time freeze counts were not recorded, and the MECH-357 scaffold suppresses the freeze during Stage-H by design (red-team R2). This is a recording gap.
- **F3: weak producer or composition? First, the commit latch.**
  - In every freeze-OFF own-policy arm at p0 and final, `beta_elevated_fraction = e3_committed_fraction = 1.0`; at init both are 0.
  - With beta elevated, the executed action is `traj.actions[:, committed_step_idx]` of the latched committed trajectory (agent.py:11444-11455). A per-candidate No-Go therefore reaches execution only when a new commitment forms.
  - All four divergences sit at episode steps 0-2.
  - This is the plan's own third F3 row: the veto starved by Family C, repair order C then F. The rule's entropy test could not see it, because diversity stayed at 1.2-1.6 bits.
  - Secondary legs:
    - composition proper (seed 48: 24 No-Go applications, 0 divergence);
    - producer signal validity (seed 49: spread 0.0039 vs oracle ~0.021, and 5/5 fired ticks all-fired, which hits the fallback at e3_selector.py:2439-2447);
    - environment-limited contrast.
  - Where the veto did change behaviour, life was equal or shorter (17=17, 13->12, 21->17, 9->8).
  - *Withdrawn claim:* the first draft's "first-action aliasing" leg assumed the executed action is the selector's first action. It is not, on latched ticks.

## 5. Four-layer table

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | n/a | claim-free diagnostic |
| Biological reference | partial | vlPAG freeze is graded by threat imminence (CeA -> vlPAG). The gate here reads the norm of a tissue-damage encoding. This is a stream mismatch, and it is load-bearing |
| Prerequisites | immature / unmeasured | the training-time lock was not recorded; trained policies are commitment-latched |
| Implementation | partial (inert by DEFECT) | the freeze input is a content-free norm; z_harm_s carries the signal. Missing link: neutralising input |
| Environment | wrong pressures for moving policies | ambient field tax; moving-policy life ~16 at best; wall-press is tax-free; true contact rare |
| Measurement | partly misleading | F0 bar above the input ceiling (1/3 seeds) and unpaired; F3 EFFECTIVE unreachable; commit latch unrecorded. F1 is valid |
| Integration | coupled but inert | freeze: input-independent; veto -> action: most likely starved by the commit latch |
| Scale | adequate | budget is not the limit |

**Failure-location (GOV-FAILLOC-1): MIXED (MECHANISM partial + MEASURES + ENVIRONMENT). Not chargeable to REE.**

## 6. Biological triage

- In the reference circuit, freezing is graded by threat imminence along the predatory-imminence continuum, with CeA -> vlPAG as the drive. It is released as imminence changes.
- Tissue-damage, nociceptive input drives recuperative quiescence, which is a different behaviour class.
- REE already separates these two streams (SD-011: z_harm_s for proximity and intensity, z_harm_a for accumulated deviation). The freeze consumer is simply wired to the wrong one.
- So this is a translation (wiring) gap, not evidence against the freeze mechanism. No `/lit-pull` is needed to act on it.

## 7. Learning and repair pathway

The learning list is in the JSON `learning_extracted`. The main items:
- test the statistic a consumer actually reads;
- choose the stream by what it carries;
- life-ceiling probes must include the degenerate policies the agent actually uses;
- pair representation comparisons and normalise them by the input ceiling;
- a dead-unit fraction is only a training finding if it moved from init;
- veto tests must record the commit latch;
- recording gaps: training-time freeze counts, trained z_harm_s, and latch state.

**Node classification:**
- **Freeze edge: `complicated (buildable)`.** It is a consumer-rewiring test, and an existing wiring may already cover it.
- **Veto edge: `complex (probe-gated) / puzzle (known rules)`.** Four legs, with H-commit read against probe C first.

**Routing options (the orchestrator puts these to the user; `routing` is staged as `implement-substrate`):**
- **B (recommended first): a consumer-rewiring TEST under MECH-279.** This amends the input, not theta.
  - Enable the existing `use_lpb_interoceptive_routing` input (`external_magnitude`, derived from proximity `harm_obs`; agent.py:11473-11477). Failing that, use a flag-gated z_harm_s-norm or E3-predicted-harm entry input.
  - `z_harm_a` stays for recuperation, guarding and valence.
  - Score freeze_active against proximity under a moving policy, plus paired FZ_ON / FZ_OFF life.
  - Keep the freeze OFF in training curricula meanwhile.
  - This is also the near-term route that would unblock the parked MECH-280, and it is what makes ARC-155/ARC-156 PAG designs meaningful: an own-scale denomination of a content-free norm would be content-blind.
- **A: V3-EXQ-1109a (same question, recording-extended), ~75 min on a cloud worker.**
  - paired init/final walks and a ceiling-normalised F0;
  - trained z_harm_s readouts;
  - F3 commit-latch recording (beta state, step_idx, committed-trajectory identity, executed step);
  - producer-vs-oracle candidate harm;
  - an optional low-tax env arm;
  - training-time freeze and suppression counts.
  - Run it scoped to F3 + trained z_harm_s, after probe C reports.
- **MECH-598/599: not indicated by this data.**
  - This run supports Q-113's answer 2 at the PAG ("semantic split: injury and threat need separate consumer contracts").
  - Name the MECH-598/599 build route only if a z_harm_s-fed freeze still cannot act before harm recurs, or if 1109a shows the veto producer's candidate harm fails to track oracle harm.
- **Literature context** (lit-pull REE_assembly `3f354b10ec`, GFLAG-0563; relayed by the orchestrator; supportive, not decisive):
  - Roelofs & Dayan 2022 and Moscarello & Penzo 2022: defensive consumers read PREDICTED threat. That is the direction of option B.
  - If the MECH-598/599 conditional fires, MECH-599 alone is the smaller first build. Whether it depends on MECH-598 is a `/governance` call.
  - Design constraints for any follow-on arm: log orienting separately from learning rate; a threat store must subtract its own prediction from its teaching signal (Ozawa 2017).
- **Severity: unchanged at `degrading`.** The first draft's `corrupting` upgrade was withdrawn: the rec-20260926 user decision already declined it.

**Draft `evidence_quality_note`:** see JSON `recommended_evidence_quality_note`.

**Granularity-debt trigger:** does not fire (claim-free).

**Re-derive brake:** not applicable (claim-free).

**GOV-DIAG-1:** this is hit 1 on `GFLAG-0508` / `substrate_queue:MECH-279`. The predecessors were claim-tagged.

**Step 9b:** drafted only, in `hypothesis_space_ledger_pending`. It proposes a new question, `q111_leg1_veto_inertness_locus`, with legs H-commit, H-comp, H-sv and H-env. Apply it only if option A is confirmed.

## 8. Hand-off

No chip was spawned. After the gate, `/governance` or the orchestrator chips B, A, or both.

## 9. Step 7b pre-routing checks

`fire_count: 0`. C1, C2 and C3 were inapplicable (claim-keyed; `claim_ids: []`); C6 and C7 were inapplicable (no arm-array manifest shape). The checks could not look, so Step 7c carried the load.

## 10. Step 7c red-team

The pass ran on **fable** (Claude Fable 5.1), a different model from the drafter (Opus 5.5). **Verdict: CONTESTED.** Every verdict-moving finding was accepted and applied above.

- **F1.** "BOTH forced by construction" is contradicted by init FZ_OFF lives of 68.0 and 74.7, and by a wall-press probe that reaches the 200-step cap.
  - Confirmer: the manifest's `checkpoints[0].arms.ARM_FZ_OFF.per_episode`, plus the wall-skip branch at causal_grid_world.py:2563-2564.
  - Applied: the claim is withdrawn, and "training reduced freeze-OFF life" is added as a finding.
- **F2.** The F3 fan-out omitted the plan's commitment row; `e3_committed = beta_elevated = 1.0`.
  - Confirmer: agent.py:11444-11455 and the per-seed `collapse_target`.
  - Applied: H-commit is added as the lead leg, and the aliasing leg is withdrawn.
- **R1.** The severity upgrade re-litigated the rec-20260926 user decision. Applied: withdrawn.
- **R2.** "Trained STAY-locked since P0" is unmeasured, and the MECH-357 Stage-H suppression contradicts it. Applied: softened to a recording gap.
- **R3.** The norm defect may instead be owned by the P0 harm training (the Q086 calibration pathology). Noted; option B stands.
- **Hygiene.** Applied: "moving policies" (not "every policy"), "successful move".
- **Verified correct by the red-team:**
  - the 70% input-ceiling arithmetic;
  - R^2(norm) ~0 at every checkpoint;
  - dead units already present at init;
  - FZ_OFF contact counts;
  - the per-candidate unit of the veto fire rate;
  - the seed-49 all-fired ticks;
  - the seed-47 application split, and the veto-ON lives;
  - that LPB `external_magnitude` exists, is wired, and derives from proximity `harm_obs`.

Findings file: `.scratch/breakthrough-20260924/ap1109/redteam/redteam_findings.md` (not committed).

## 11. Confirmed routing (Step 8, user decision)

- **Decision source:** the user, via a live AskUserQuestion put by orchestrator `orchestrate-20260924-breakthrough-c2` on 2026-09-26.
- **Route: B, a MECH-279 consumer-rewiring test.**
  - Rewire the freeze ENTRY input to `z_harm_s`, LPB interoceptive routing (`use_lpb_interoceptive_routing` -> `external_magnitude`), or E3 predicted harm.
  - `z_harm_a` is kept for recuperation and valence.
  - The freeze stays OFF in training curricula meanwhile.
  - This unblocks MECH-280.
  - Hand-off: `recommended_substrate_queue_entry` (action `amend`, target MECH-279, severity unchanged at `degrading`).
- **Category: accepted as proposed.** `standard`; `non_contributory`; failure location MIXED; severity `degrading`.
- **Not chosen:**
  - option A (V3-EXQ-1109a);
  - the MECH-598/599 build route.
- **Step 9b:** not applied. The ledger blocks were conditional on option A, so this autopsy owes no hypothesis-space registration.
- **`per_claim_recommendation`:** empty. The target is claim-free.
- **Follow-on:** not spawned here. `/governance` chips the MECH-279 rewiring build once it applies the amend.
