# Scaffolded SD-054 onboarding -- substrate design memo

**Date:** 2026-05-29
**Author session:** `sd054-scaffolded-onboarding-memo-20260529T172125Z`
**Status:** IMPLEMENTED 2026-05-31 (ree-v3/main commit `28ebd3d`; substrate landed via `experiments/scaffolded_sd054_onboarding.py` + `reef_bipartite_agent_spawn_in_reef_half` env kwarg on `CausalGridWorldV2`; implementation surface (a) NEW scheduler taken per "Implementation surface choice" section; 14 phase-config knobs match the Config Surface table; 17 contracts in `tests/contracts/test_scaffolded_sd054_onboarding.py` PASS; 645/645 full regression PASS; closes IGW-20260531-029. Behavioural validation V3-EXQ-621 queued separately per the Sequencing table step 4).
**Amend 2026-06-02 (update_z_goal wiring):** the as-landed scheduler never called `agent.update_z_goal`, so `GoalState.update` was never reached and z_goal stayed zero-init across every arm (V3-EXQ-603d C4 FAIL; 626-class harness/wiring artifact in the substrate module, not a ceiling). Wired `agent.update_z_goal(benefit, drive)` into `_train_episode` (P1 only, via a `seed_goal` kwarg) and `_eval_episode` (P2), mirroring the `goal_stream_stages_sd054.py` reference runner; P0 left goal-frozen by design (user-confirmed P1+P2-only scope). Added Stage-0 positive-control contracts so a z_goal=0 scheduler is unshippable. **Two-part fix:** the validation config must ALSO set `z_goal_enabled=True` + `drive_weight=2.0` (603d's config omitted it -> `goal_state` was None -> `update_z_goal` early-returns); the working reference V3-EXQ-622 sets it. V3-EXQ-603e re-issue (restored P0/P1=100/50 budget + z_goal_enabled=True) is the validation. Folds the V3-EXQ-625b monostrategy failure record (plausibly downstream of the same inert goal pipeline). Session `implement-substrate-scaffolded-sd054-zgoal-wiring-20260602T062215Z`; autopsies `failure_autopsy_V3-EXQ-603d_2026-06-01` + `failure_autopsy_V3-EXQ-625b_2026-06-02`.
**Amend 2026-06-03 (foraging-competence + forced-benefit Stage-0) -- PENDING:** the update_z_goal wiring amend (deb24cc) is now validated **necessary-but-insufficient** by V3-EXQ-603e + V3-EXQ-626a: z_goal forms under the forced-input Stage-0 contract yet stays **0.0 ecologically** (603e: 0.0 on all 15 cells incl. the 5 surviving seed-43 cells, restored budget P0/P1=100/50; 626a P0 positive control forms z_goal on only 1/3 seeds). The 2026-06-03 cluster autopsy ([failure_autopsy_V3-EXQ-603e-626a-622_2026-06-03](failure_autopsy_V3-EXQ-603e-626a-622_2026-06-03.md)) ruled the cluster `non_contributory` / `substrate_ceiling` / `pending_retest_after_substrate`: the gap is **upstream of the wiring** -- (1) survival/foraging competence (2/3 seeds never reach a foraging-competent policy) and (2) benefit-input starvation (hard P2 `hazard_food_attraction=0.7` keeps `benefit_exposure` sub-threshold even for survivors). The foraging-competence amend is now **IMPLEMENTED 2026-06-03** (ree-v3 commit `e718bf4`; nursery/forced-benefit Stage-0 + survival lever + P2 guard + contact-rate + gate/branch helpers + 12 contracts; 731 contracts + 7/7 preflight PASS; forced-feed smoke lights z_goal). **Full-scale runtime readiness is still PENDING** a substrate-readiness run, so substrate_queue `ready` stays `false` and the re-issue **V3-EXQ-603f** is NOT yet queued. See the "## Amend 2026-06-03" section below.
**Lever chosen:** (A2) scaffolded SD-054 reef + bipartite-horizontal as the start-state distribution for P0+P1 training, with hazard_food_attraction and goal-pipeline writes annealed in across P1
**Successor session:** `/implement-substrate` on a new scheduler (sibling to `experiments/infant_curriculum.py`) AND a small spawn-relaxation extension on CausalGridWorldV2 (separate) -- DONE 2026-05-31 via session `implement-substrate-scaffolded-sd054-onboarding-20260531T174200Z`

---

## Origin

Commissioned after the [2026-05-29 V3-EXQ-490g cohort autopsy](failure_autopsy_V3-EXQ-490g-cohort_2026-05-29.md) (commit `12f0dda773`) and user-confirmed sub-lever choice (A2). The autopsy's Fork B disposition for V3-EXQ-603c routes to `/implement-substrate` with `recommended_substrate_queue_entry.action=create` for a new SD-XXX scaffolded-SD-054-onboarding substrate. This memo is the canonical-shape sibling of the 2026-05-28 [E2 action-conditional divergence memo](e2_action_divergence_substrate_design.md): a substrate-design plan-of-record that a follow-on `/implement-substrate` session will execute against. It does not edit code.

The autopsy split a five-experiment cohort into two structurally distinct clusters. Cluster A (V3-EXQ-483c, 524a) is a GAP-4 Tier-1 library measurement gap that routes to `/queue-experiment` (Tier-1 library rebuild) -- **not in scope here**. Cluster B (V3-EXQ-603c) cluster-absorbs into the [2026-05-27 V3-EXQ-591 autopsy](failure_autopsy_V3-EXQ-591_2026-05-27.md) substrate-uniform z_goal-zero family. This memo addresses Cluster B at the substrate-design level by specifying the new SD-XXX-scaffolded-sd054-onboarding substrate that prereq #2 of the 591 autopsy ("goal-pipeline training regime produces non-trivial z_goal in default config") requires.

---

## What is broken

The goal-pipeline substrate is wired correctly in isolation. V3-EXQ-493 (2026-04-27/28) confirmed MECH-295 cue-side bias produces monotone-negative `score_bias` with the severed-bridge falsifier collapsing to zero (UC1-UC6 PASS). The downstream cascade `drive -> liking-stream -> approach cue` is inert under realistic policy state across V3-EXQ-540 series, 590a, 591, 603/603b/603c -- the substrate-uniform z_goal-zero family enumerated in the 591 autopsy §6.

V3-EXQ-603c (2026-05-27) was the predecessor 603-chain extension that added P0+P1 phased training (Fix C from the [2026-05-25 V3-EXQ-603b autopsy](failure_autopsy_V3-EXQ-603b_2026-05-25.md)) and a Fix D pre-measurement seed-stability gate (median episode length at end of P1 >= `FIFO_WARMUP_STEPS=75`). It FAILed. Manifest `metrics.json: values = {}` with `status: FAIL` and `outcome: None`. The script's `_evidence_direction_per_claim` correctly routed all three claims (Q-045, MECH-313, MECH-260) to `non_contributory` because `n_p2_cells < total_cells / 2` -- the structurally-underpowered branch the script was designed to detect.

The root reading: most (arm, seed) cells aborted at P0 (running_variance not converging in [`P0_BUDGET=100`](https://github.com/Latent-Fields/ree-v3/blob/main/experiments/v3_exq_603c_q045_mech313_mech260_phased_training.py) episodes) or failed the Fix D survival gate (`median episode length < 75` over the last 10 P1 episodes). The target env -- SD-054 reef + bipartite-horizontal + `hazard_food_attraction=0.7` + `proximity_harm_scale=0.1` + `num_hazards=4` + `num_resources=5` -- is structurally hostile to a random-init agent. The agent dies before z_goal can develop.

603c's "easy" P0 env disables `reef_bipartite_layout` and sets `hazard_food_attraction=0.0`, but keeps `reef_enabled=True` so the encoder shape matches via the +25 `reef_field_view` channel. The autopsy diagnosis confirms 603c's design does NOT exploit SD-054 as a *spatially-scaffolded* refuge during P0; it just relaxes hazard density. The agent still spawns at a uniformly-random empty cell across the whole grid and faces the random-walk hazards anywhere it lands. **Phased training alone is insufficient**: the agent needs both phased training AND a scaffolded *start-state distribution* that exploits SD-054's spatial structure as developmental safety scaffolding.

The 591 autopsy enumerated three substrate prerequisites:
1. RV convergence below `commit_threshold` reliably reached during warmup.
2. The goal-pipeline training regime produces non-trivial z_goal under default config.
3. InfantCurriculumScheduler exit-gate tuning (ARC-046; out of scope here -- ARC-046 has its own pending prereqs).

This memo addresses **prereq #2** at the substrate-design level. Prereq #1 is partially co-addressed (the scaffolded P0 env will let RV converge more reliably). Prereq #3 is unaffected.

---

## The substrate change

A new substrate, provisionally named `SD-XXX-scaffolded-sd054-onboarding` (governance picks the real ID via the autopsy's `recommended_substrate_queue_entry.action=create`). Three coordinated changes, all behind a single master switch.

### Phase structure

Three phases per (arm, seed) cell, matching the 603c three-phase shape but with different env config + spawn discipline per phase.

#### P0 -- encoder + E2 + E3 warmup on scaffolded SD-054, goal pipeline FROZEN (suggested 30-50 episodes)

- Env config: `reef_enabled=True`, `reef_bipartite_layout=True`, `reef_bipartite_axis="horizontal"`, `reef_bipartite_agent_band_radius=1`. `hazard_food_attraction=0.0` (legacy random-walk hazards). `proximity_harm_scale=0.05` (sub-target value, easier survival). `num_hazards=2`, `num_resources=3` (sub-target density, easier learning).
- Spawn discipline: the agent spawns **inside the reef refuge band**, NOT in the SD-054 default agent band on the midline. This is the load-bearing scaffolding change: SD-054 bipartite-horizontal currently places agent in `[midline - radius, midline + radius]` (rows 5-7 at `size=12, radius=1`) with reef cells in `[midline + radius + 1, size - 2]` (rows 8-10). The new substrate widens spawn admissibility to also cover the reef-half rows during the P0 window. Concretely: a new boolean kwarg on the env's bipartite path, suggested `reef_bipartite_agent_spawn_in_reef_half=False` default (preserves all existing SD-054 behaviour), set `True` during P0. When True, agent draws spawn from the union of the agent-band rows AND the reef rows. Hazards and resources still draw from the forage half only.
- Goal pipeline writes FROZEN: `use_mech307_conjunction=False`, `use_mech295_liking_bridge=False`. The encoder + E2 + E3 learn the SD-054 spatial structure (reef-field-view channel + bipartite topology + hazard substrate) without the goal pipeline gating its own training data.
- Convergence target: running_variance below `commit_threshold` reliably reached. Equivalent to 603c's P0 RV-convergence probe at `P0_PROBE_INTERVAL=20`. Per the autopsy's bound on P0 episode count (50-100 in 603c, lowered here because the scaffolded env is easier).

#### P1 -- annealed unfreeze of goal pipeline + annealed hazard_food_attraction (suggested 30-50 episodes)

- Env config: anneal `hazard_food_attraction` from `0.0 -> 0.7` linearly across the P1 window. Anneal `proximity_harm_scale` from `0.05 -> 0.1` in parallel. `num_hazards` and `num_resources` step up to the target-env values at the start of P1.
- Spawn discipline: spawn admissibility narrows back to the SD-054 default agent band (`reef_bipartite_agent_spawn_in_reef_half=False`) at the start of P1. The agent now spawns in the midline band and must navigate to find food in the forage half OR retreat to the reef for safety. This is the curriculum-style commitment moment: the scaffolded survival from P0 has trained an encoder that knows where the reef is; P1 lets the goal pipeline grow against a slowly-increasing reward landscape.
- Goal pipeline writes UNFREEZE with annealed gates: anneal `mech295_min_drive_to_fire` from `1.0 -> 0.01` linearly across the P1 window (the existing default landed 2026-05-12 is `0.01`; anneal from above-threshold-impossible at the start to default at the end so the bridge ramps up gradually). Anneal `mech307_conjunction_z_beta_threshold` from `0.6 -> 0.3` in parallel (default `0.3` landed 2026-05-12; anneal from the pre-fix legacy value). Other goal-pipeline flags (`use_mech307_conjunction=True`, `use_mech295_liking_bridge=True`) hard-on for the duration of P1.
- Survival gate: at the end of P1, check `median episode length over the last P1_STABILITY_WINDOW=10 episodes >= P1_SURVIVAL_GATE_STEPS=75` (Fix D from 603c, retained as-is). Cells that fail the gate route to `non_contributory` per the 603c pattern.

#### P2 -- frozen policy, full target-env config, measurement (suggested 30 episodes)

- Env config: full target env, identical to V3-EXQ-603b's target config and the eventual GAP-4 Tier-1 measurement env. `reef_enabled=True, reef_bipartite_layout=True, reef_bipartite_axis="horizontal", reef_bipartite_agent_band_radius=1, hazard_food_attraction=0.7, proximity_harm_scale=0.1, num_hazards=4, num_resources=5`. Spawn discipline at SD-054 default (`reef_bipartite_agent_spawn_in_reef_half=False`).
- Policy frozen, goal-pipeline writes hard-on at the defaults annealed-to at end of P1.
- Measurement: `z_goal_norm_peak` per cell + cascade behavioural metrics (`approach_commit_rate`, `bridge_cue_fires`, `dacc_bias_nonzero_steps`, `selected_action_entropy`). The C1-C3 acceptance criteria (below) read these metrics.

### Config surface

All new knobs gated by a single master switch. Suggested names (final naming is the `/implement-substrate` session's responsibility; these are the substrate-design memo's pre-registration):

| Flag | Type | Default | Role |
|---|---|---|---|
| `use_scaffolded_sd054_onboarding_scheduler` | bool | `False` | Master switch. Default OFF preserves all current behaviour. |
| `scaffold_p0_episode_budget` | int | `30` | P0 window length. |
| `scaffold_p1_episode_budget` | int | `30` | P1 window length. |
| `scaffold_p2_episode_budget` | int | `30` | P2 measurement budget. |
| `scaffold_p0_proximity_harm_scale` | float | `0.05` | Sub-target value during P0. |
| `scaffold_p1_anneal_hazard_food_attraction_min` | float | `0.0` | Start of P1 anneal. |
| `scaffold_p1_anneal_hazard_food_attraction_max` | float | `0.7` | End of P1 anneal (= target env value). |
| `scaffold_p1_anneal_proximity_harm_scale_min` | float | `0.05` | Start of P1 anneal. |
| `scaffold_p1_anneal_proximity_harm_scale_max` | float | `0.1` | End of P1 anneal (= target env value). |
| `scaffold_p1_anneal_mech295_min_drive_to_fire_max` | float | `1.0` | Start of P1 anneal (high = bridge silent). |
| `scaffold_p1_anneal_mech295_min_drive_to_fire_min` | float | `0.01` | End of P1 anneal (= 2026-05-12 default). |
| `scaffold_p1_anneal_mech307_conjunction_z_beta_threshold_max` | float | `0.6` | Start of P1 anneal (legacy pre-fix value). |
| `scaffold_p1_anneal_mech307_conjunction_z_beta_threshold_min` | float | `0.3` | End of P1 anneal (= 2026-05-12 default). |
| `scaffold_p1_survival_gate_steps` | int | `75` | Fix D from 603c, retained as-is. |
| `reef_bipartite_agent_spawn_in_reef_half` | bool | `False` | Env-side kwarg on CausalGridWorldV2's bipartite spawn path. Master scheduler sets this `True` for P0 only. |

Per the implement-substrate skill rule, no defaults of existing parameters change. `reef_bipartite_agent_spawn_in_reef_half` is a new env-side kwarg that defaults `False` (preserving all SD-054 / SD-054-bipartite behaviour). The annealing schedule flags are scheduler-side and only consulted when the master switch is on.

### Implementation surface choice

The autopsy named two options without arbitrating: (a) a new `InfantCurriculumScheduler`-style scheduler dedicated to this curriculum, or (b) an extension to the existing `ree-v3/experiments/infant_curriculum.py` `InfantCurriculumScheduler`.

**This memo commits to option (a): a new scheduler.** Two grounds.

First, ARC-046's `InfantCurriculumScheduler` is itself in the substrate-prereq #3 lane (H_POS_FRAC unreachable; see the 591 autopsy and the 2026-05-29 IGW-033 deferred-close session). Coupling the goal-pipeline substrate fix to ARC-046's pending repair creates a dependency cycle. The two curricula address structurally different gaps (ARC-046 is about Phase 0->1 advancement signal; this scheduler is about P0/P1/P2 env transition + flag annealing for goal pipeline). Keep them decoupled.

Second, the canonical-shape precedent for this kind of phased-training memo (the 2026-05-28 SD-056 contrastive-loss memo) created new module surfaces rather than extending existing ones. Cleaner ablation, smaller blast radius, no ABI risk to existing curricula.

Suggested module surface: `ree-v3/experiments/scaffolded_sd054_onboarding.py` containing `ScaffoldedSD054OnboardingScheduler` + the new env-kwarg passthrough. The scheduler exposes `run_p0()`, `run_p1()`, `run_p2()`, and `clone_trained_agent()` helpers in the [committed_mode_curriculum.py](https://github.com/Latent-Fields/ree-v3/blob/main/experiments/committed_mode_curriculum.py) pattern landed for GAP-11.

### What does NOT change

- `ree_core/` is untouched. The substrate change is entirely env-side (one new kwarg on CausalGridWorldV2's bipartite spawn path) + an experiment-harness scheduler. No agent / encoder / E2 / E3 / hippocampal / residue / regulator changes.
- ARC-046 InfantCurriculumScheduler is untouched. ARC-046 has its own pending prereqs (substrate_queue.json) and is not coupled to this work.
- SD-054 substrate semantics unchanged. `reef_bipartite_layout=True` continues to spawn agent in the midline band by default. The new `reef_bipartite_agent_spawn_in_reef_half` kwarg widens spawn admissibility ONLY when set, ONLY during P0.
- `mech295_liking_bridge` and `mech307_conjunction` substrate-side defaults unchanged. The annealing curriculum operates on the experiment-side flags consumed by the scheduler; the bridge / conjunction modules themselves are not edited.

---

## Why this should work (the falsifiable bet)

The 603c failure mode is structural: at random-init in the target env, episode length is short enough that the agent dies before drive_level rises high enough to trigger `mech295_liking_bridge` writes against a goal location it has visited often enough for `mech307_conjunction` to fire. The phased-training scaffold (Fix C) cannot fix this because P0 trained the encoder in a stripped-down env where the goal pipeline was disabled -- when P1 turns the goal pipeline on, the agent re-encounters the hostile target env at the same random-init survival floor.

The scaffolded SD-054 onboarding inverts the order. P0 trains the encoder in an env where the agent literally starts inside a refuge band that SD-054's spatial structure provides. Surviving long enough to develop a coherent encoder is structurally guaranteed (the agent can stand still inside the reef and not die). P1 then introduces the survival pressure gradually: spawn moves back to the midline, hazards become food-attracted, the goal-pipeline gates open. By the time P2 measurement starts, the agent has been trained against the target env's reward landscape for at least ~30 episodes with a working encoder and a goal pipeline that has had time to develop a non-trivial z_goal.

This is the V3-EXQ-540e-anchored argument: the 540-series probe data showed `goal_norm_peak` values in the `0.05+` range under partial-substrate firing. The C2 acceptance criterion below pre-registers `goal_norm_peak >= 0.1` per cell -- modestly above the 540-series floor, leaving headroom for the substrate fix to demonstrate real effect rather than measurement-floor crossing.

The honest disclaimer: if C1 fails (most cells still don't complete P2), the substrate-uniform z_goal-zero family is the wrong reading. Most likely upstream culprit then becomes ARC-046 H_POS_FRAC unreachable + InfantCurriculumScheduler -- but that's a different chain of substrate work, not this memo's scope.

---

## Acceptance criteria

Pre-registered for the V3-EXQ-603c successor (next letter -- pick at `/queue-experiment` write time; tentative `V3-EXQ-603d`).

- **C1 substrate-readiness (cells complete).** P0+P1+P2 completes on `>= total_cells / 2` (arm, seed) cells without hitting the Fix D survival gate. This is the structurally-underpowered-branch guard 603c's script already implements. PASS = the scaffolded onboarding lets the agent survive the target env after the curriculum, FAIL = the scaffold is insufficient and the substrate-uniform reading holds.

- **C2 z_goal materially nonzero.** `z_goal_norm_peak` in P2 measurement cells achieves `>= 0.1` on at least `2 of 3 seeds in at least one arm`. The threshold is anchored on the V3-EXQ-540e probe data (`goal_norm_peak` in the `0.05+` range under partial firing); 0.1 leaves a 2x floor above measurement noise. PASS = the goal pipeline is no longer collapsed to zero by the training regime, FAIL = the substrate change does not lift z_goal above the 540-series floor.

- **C3 goal pipeline behaviourally consequential.** One of the following measurably differs between the scaffolded-curriculum arms and a from-scratch-no-scaffolding control arm (3 seeds each):
  - `approach_commit_rate` lift `>= 0.10` (scaffolded > control).
  - `bridge_cue_fires` mean per episode `>= 2` (scaffolded; control expected near zero per 603/603b/603c).
  - `dacc_bias_nonzero_steps` `>= 1` per episode mean (scaffolded; control expected zero per 603c).
  PASS = goal pipeline becomes behaviourally consequential at P2 measurement, FAIL = z_goal develops but does not feed downstream cascade effects.

Overall PASS = C1 AND (C2 OR C3). C2 OR C3 captures the two routes the substrate fix could succeed: either z_goal_norm itself crosses the floor (the 540e-anchored direct probe) OR the cascade fires behaviourally even at modest z_goal_norm (the 493-anchored isolation result extending to cascade). Joint pass would be ideal but is not required.

The C3 control arm matters: a from-scratch-no-scaffolding arm uses the existing 603c P0+P1 phased training (Fix C) without the scaffolded SD-054 onboarding scheduler. This pins the substrate effect to the new scheduler rather than to any incidental P0/P1 budget tuning the successor adopts.

---

## Sequencing

| Step | Skill / session | Output | Status |
|---|---|---|---|
| 0 | this memo | `sd_054_scaffolded_onboarding_substrate_design.md` | DONE 2026-05-29 |
| 1 | governance applies the autopsy's `recommended_substrate_queue_entry.action=create` | new `SD-XXX-scaffolded-sd054-onboarding` entry in `substrate_queue.json` (governance assigns the real SD ID) | NEXT |
| 2 | `/inter-governance-brief` surfaces the new substrate-queue entry as `Implement substrate: SD-XXX (unblocks Q-045)` IGW item; prereq-detection symmetric extension (2026-05-29 commit `d8d1aa2707`) ensures human-visible review before auto-spawn | IGW item routed | after step 1 |
| 3 | `/implement-substrate` on SD-XXX | new scheduler module + env-kwarg passthrough + contract tests + bit-identical-OFF regression | after step 2 |
| 4 | `/queue-experiment` | V3-EXQ-603c successor (next letter) queued: 4-arm design ALL_OFF_baseline / SCAFFOLD_ONLY / SCAFFOLD_AND_ANNEAL / SCAFFOLD_AND_ANNEAL_CONTROL_FROM_SCRATCH; phased training matches 603c budgets so per-arm comparisons are calibrated; acceptance criteria C1/C2/C3 pre-registered per this memo | after step 3 |
| 5 | runner | V3-EXQ-603c-successor manifest landed | after step 4 |
| 6 | governance | Apply per-claim direction overrides per C1/C2/C3 outcomes; update `goal_pipeline_plan.md` GAP-4 status; clear `pending_retest_after_substrate` on Q-045 / MECH-313 / MECH-260 if PASS | after step 5 |

Each step is a separate session to keep blast radii small and concurrency clean.

---

## What this memo does NOT do

- **Does not pick the budget magnitudes empirically.** P0 / P1 / P2 episode budgets, the anneal start/end values, and the C2 threshold are starting points. The validation experiment calibrates them; the `/implement-substrate` session may adjust the defaults if the canonical-shape precedent or contract-suite outcomes warrant.
- **Does not commit to the spawn-relaxation kwarg name `reef_bipartite_agent_spawn_in_reef_half`.** Final naming is the `/implement-substrate` session's responsibility; the substrate-design pre-registration is the kwarg's *role* (widen P0 spawn admissibility to the reef half) and its default (`False`, bit-identical OFF).
- **Does not pre-commit to a new SD ID.** Governance assigns the real ID via the autopsy's `recommended_substrate_queue_entry.action=create`. `SD-XXX-scaffolded-sd054-onboarding` is a placeholder; the next available SD slot after the current registry max is the natural pick.
- **Does not modify SD-054, SD-012, MECH-295, MECH-307, ARC-030, or any other existing substrate.** SD-054's existing semantics (reef + bipartite-horizontal + agent-band) are preserved exactly; the new kwarg only widens spawn admissibility under explicit opt-in. The annealing schedule operates on experiment-side flag values consumed by the new scheduler, not on the existing substrate defaults.
- **Does not touch ARC-046 / `infant_curriculum.py`.** ARC-046 has its own pending prereqs and is structurally distinct from this work (Phase 0->1 advancement-signal substrate gap vs P0/P1/P2 env+flag annealing for the goal pipeline).
- **Does not queue V3-EXQ-603c-successor.** Separate `/queue-experiment` session per the skill discipline.
- **Does not address Fork A (Tier-1 library rebuild + 483d cohort).** That work is the autopsy's Cluster A routing and is a separate chip.

---

## What the substrate fix is NOT promising

Three honest disclaimers, mirroring the SD-056 memo's tone.

- **The scaffolded curriculum surviving P2 does not by itself imply MECH-295 cascade promotion.** C1 is necessary (the 603c family showed it being absent and the cascade collapsing); C2/C3 are what test cascade-state response. A cell-completion PASS with zero cascade movement (C1 PASS, C2/C3 FAIL) is a substrate finding that warrants its own autopsy.

- **(A2) may not be the load-bearing lever** if the substrate-uniform z_goal-zero family has a deeper cause we have not noticed. (A1) full-policy-replay-onto-reward-rich-trajectories and (A3) hand-coded heuristic-pretrained agents are valid fallbacks if the validation experiment FAILs. If V3-EXQ-603c-successor fails on the scaffolded SD-054 onboarding objective, that is itself a substrate finding worth its own autopsy before re-trying a different lever.

- **The MECH-307 4-arm discriminative pair remains separately pending** (GAP-4 plan-of-record row 1). This memo addresses the upstream substrate gap that has been blocking *every* GAP-4 retest cohort from running through to measurement; it does not by itself constitute the MECH-307 acceptance evidence. The cascade behavioural validation that MECH-295 needs is still the Phase 4 Tier-1 cohort's responsibility, gated on this substrate landing first.

---

## Amend 2026-06-03: foraging-competence + forced-benefit Stage-0 z_goal warmup (603e -> 603f path)

**Status: IMPLEMENTED 2026-06-03 (ree-v3 `e718bf4`); full-scale runtime readiness PENDING.**
The nursery/feeding scaffold landed in `experiments/scaffolded_sd054_onboarding.py`
(additive -- no existing config default changed; master-OFF bit-identical;
731 contracts + 7/7 preflight PASS; 603e --dry-run unchanged). Activation smoke
(real REEAgent, z_goal_enabled=True + drive_weight=2.0, Stage-0 2 ep x 25 steps):
forced feed lights z_goal (`z_goal_norm_peak=0.234 > 0`; the `>0.4` acceptance is
a full-scale gate, not a dry-scale one), P2 guard `hfa=0.3` applied, contact-rate
readout wired. What lands: `run_stage0_nursery` (forced supra-threshold benefit,
decoupled from survival) + `Stage0NurseryResult`; `scaffold_p1_anneal_hold_fraction`
staged-withdrawal lever; `STAGE_PLAN`/`stage_plan()`; P2 `scaffold_p2_hazard_food_attraction_guard`
+ `contact_steps`/`contact_rate`/`hazard_food_attraction_used`; `evaluate_substrate_gate`
+ `classify_interpretation_branch`. **What remains before 603f:** a full-budget
substrate-readiness run must confirm the runtime gates (Stage-0 z_goal>0.4 on
>=2/3 seeds, P1 survival >=2/3, P2 contact>0 on >=2/3) -- the mechanism is proven
but the strengthened scaffold's ability to get 2/3 seeds to competence at scale
is not yet demonstrated. substrate_queue `ready` stays `false` until then.

Routed by the 2026-06-03 cluster autopsy
[failure_autopsy_V3-EXQ-603e-626a-622_2026-06-03](failure_autopsy_V3-EXQ-603e-626a-622_2026-06-03.md)
(`recommended_substrate_queue_entry.action=amend`). Tracked in
`substrate_queue.json :: scaffolded_sd054_onboarding.current_pending_amend`
(`ready:false`, `status: amend_foraging_competence_pending_implementation`).

### What 603e/626a established

The 2026-06-02 update_z_goal wiring amend (`deb24cc`) closed the harness/wiring
layer and is **necessary** -- the Stage-0 positive-control contract proves z_goal
forms under forced supra-threshold benefit+drive. But it is **not sufficient**:

- **V3-EXQ-603e** (restored budget P0/P1=100/50, z_goal_enabled=True, ruling out
  the 603d budget confound) FAILed with `z_goal_norm_peak = 0.0` on **all 15 cells**,
  including the 5 surviving seed-43 cells; P1 survival passed on **1/3** seeds.
- **V3-EXQ-626a** P0 positive control formed z_goal on only **1/3** seeds (seed 44 = 0.19;
  42/43 = 0.0); dACC consumer readout = 0 on all seeds.

Terminal diagnosis (cluster autopsy): z_goal=0 is downstream of **two coupled
prerequisites upstream of the wiring** -- (1) survival/foraging competence (2/3 seeds
never reach a survival-competent foraging policy even on easy P0 at restored budget)
and (2) benefit-input starvation (the hard P2 env `hazard_food_attraction=0.7` keeps
`benefit_exposure` sub-threshold even for survivors). Biologically a **discovered
prerequisite** (goal representations require reward-contact history; Berridge), NOT a
falsification -- Q-045/MECH-313/MECH-260 were never under fair test (z_goal=0 -> no
goal-directed behaviour to diversify; effective N=1).

### Required repairs (the pending amend)

1. **(a) Strengthen the P0/P1 survival-foraging scaffold** so **>=2/3 seeds** reach a
   foraging-competent policy. 603e shows the current scaffold gets 1/3.
2. **(b) Forced-benefit Stage-0 z_goal warmup** that seeds z_goal **independent of
   foraging competence**, so Q-045/MECH-313/MECH-260 discrimination is testable at N>1
   even while ecological foraging is still developing. This **decouples goal FORMATION
   from survival** -- the key architectural move (the existing Stage-0 contract proves
   formation is possible under forced input; this makes it a training stage, not just a
   test assertion).
3. **(c) P2 measurement guard:** lower the P2 `hazard_food_attraction` (currently
   hardcoded 0.7 at `scaffolded_sd054_onboarding.py:133`, knob
   `scaffold_p2_hazard_food_attraction`) and/or add a **foraging-contact-rate guard** so
   a z_goal=0 read is **interpretable** (distinguishes "substrate not engaged" from
   "goal mechanism absent").
4. **(d) Foraging-contact-rate readout** recorded per seed in the manifest so z_goal=0 is
   never confounded with benefit starvation.

**Acceptance target (substrate-readiness for 603f):** `z_goal_norm_peak > 0.4` on
**>=2/3 seeds** in P2 **AND** P1 survival/foraging gate passed on **>=2/3 seeds**
**AND** non-zero benefit/contact exposure on **>=2/3 seeds**. The forced-benefit Stage-0
warmup must produce direction-stable z_goal independent of survival.

### V3-EXQ-603f (the post-substrate re-issue) -- BLOCKED, not queued

Proposal `EXP-603F-POSTSUBSTRATE` (`experiment_proposals.v1.json`,
`status: blocked_substrate`, `supersedes: V3-EXQ-603e`, `claim_ids: Q-045 / MECH-313 /
MECH-260`). **This is NOT a same-substrate retest** -- it runs only after the foraging
amend lands and its survival/Stage-0 smoke + contracts pass. 603f re-runs the 603e 4-arm
Q-045 ablation (ARM_0 both-off / ARM_1 313-only / ARM_2 260-only / ARM_3 both-on) on the
repaired scaffold, evaluating the **substrate gate first** (G1 survival >=2/3, G2 non-zero
benefit contact, G3 z_goal>0.4 on >=2/3) and interpreting Q-045 discrimination **only if
the gate passes**.

**Pre-registered four-way interpretation grid:**

| Branch | Signature | Disposition |
|---|---|---|
| (1) substrate NOT engaged | G1/G2/G3 fail | `non_contributory`; re-route `/implement-substrate` (not a MECH-313/260 falsification). |
| (2) goal formed, diversity INERT | gate passes; all ARM deltas sub-margin | `does_not_support`/`weakens` MECH-313/260; **next blocker = modulatory-bias-selection-authority** (BG-like E3.select authority), not reward-contact. |
| (3) goal formed, mechanisms LOAD-BEARING | gate passes; ARM deltas resolve >0.05 at N>=2 | `supports`. |
| (4) goal formed, behaviour RANDOM/HARMFUL | gate passes; harm_rate up / churn up / entropy never narrows | arbitration-failure signature -> `/failure-autopsy`; do NOT treat as MECH-313/260 falsification. |

### Interpretation framing (why 603f matters)

REE-v3's dominant goal-pipeline failure **may not be representational absence but failure
of ecological reward-contact plus basal-ganglia-like action-selection / commitment loops.**
603f isolates the first half: whether repairing developmental foraging/contact makes goal
representations behaviourally **available**. Outcome (2) is the diagnostic hinge -- if
z_goal forms but the diversity mechanisms stay inert, the locus shifts to the **BG-like
selection-authority** gap captured by the `modulatory-bias-selection-authority`
substrate_queue entry (the 2026-06-03 governance CREATE from the 604a/624a autopsy:
modulatory score-bias fires but has zero E3.select authority). 603f (reward-contact side)
and that substrate (selection-authority side) are **complementary** tests, not duplicates.

**Avoid overclaiming:** a passing 603f on Q-045 does not by itself promote MECH-313/MECH-260
(v3_pending + answer_state gating); it removes the substrate-ceiling confound so the
diversity claims can be **fairly tested** for the first time.

---

## Amend 2026-06-03b (developmental-window / protected-goal consolidation)

**Status:** IMPLEMENTED 2026-06-03 (harness layer; no `ree_core`/`goal.py`/`claims.yaml` change). Validation experiment **V3-EXQ-634b** queued; claim-free (substrate diagnostic). Session `scaffolded-sd054-developmental-window-amend-20260603T1520Z`.

**Problem (substrate design error surfaced by the V3-EXQ-634 review, not tuning).** `GoalState.update()` (`ree_core/goal.py:173`) *always* decays the persistent z_goal attractor (`z_goal *= 1 - decay_goal`) before the benefit-gated pull, and `REEAgent.reset()` never calls `goal_state.reset()` (z_goal persists across episodes/phases). The as-landed scaffold called `update_z_goal` **every step** in P1 (`seed_goal=True`) and P2 (`_eval_episode`), so every *unfed* step is a pure decay-only washout. Stage-0 lights z_goal and P0 preserves it (goal pipeline frozen -> `update_z_goal` not called), but P1/P2 then erode the trace before ecological contact — and because the 603e cluster shows 2/3 seeds never reach foraging competence, P1 is mostly unfed, so the Stage-0 trace is washed out before the P2 measurement. 634 thus tests "can the infant stay goal-active while fed-then-starved under decay-only updates?" rather than "form -> consolidate -> learn guided/autonomous contact." `_set_goal_pipeline_frozen` only short-circuits the MECH-295/MECH-307 *consumer* pathway; it does not protect the attractor — a separate developmental window was required.

**Fix (all behind no-op-default flags; bit-identical when off).**
- **Stage-0b protected consolidation:** `run_stage0b_consolidation()` runs a short window in the safe nursery env with E1/E2 training open but `update_z_goal` not called -> z_goal cannot be washed out by decay-only updating. Records `z_goal_norm_start/end`, `retention_ratio`, `retention_gate_passed` (acceptance `>= scaffold_stage0b_retention_gate`, default 0.75 of the Stage-0 baseline).
- **Contact-gated P1/P2:** with `scaffold_contact_gated_goal_updates` (under master `scaffold_developmental_window_enabled`), P1/P2 only call `update_z_goal` on a *validated contact* step (`benefit > scaffold_p2_contact_benefit_threshold`); unfed steps are skipped (no decay-only washout). Stage-0 forced-feed is unaffected. `decay_only` is reserved for mature/autonomous tests, NOT the nursery gate.
- **Goal-write-mode constants + diagnostics:** `GOAL_WRITE_{FORCED_FEED_OPEN,CONSOLIDATE_PROTECTED,ECOLOGICAL_CONTACT_OPEN,DECAY_ONLY_ALLOWED,MEASUREMENT_READONLY}`; per-phase `n_contact_refresh_updates` / `n_decay_only_updates` / `n_skipped_protected_updates` on `P1OnboardingResult` + `P2OnboardingMetrics`, so a manifest distinguishes goal loss due to no-contact vs decay-only washout vs failed-formation-despite-contact.

**Validation.** 739 contracts (C7 group: persistence-across-Stage-0b; decay-only blockable in protected window (ON-vs-OFF contrast); ecological contact still refreshes; flags-off bit-identical) + 7/7 preflight PASS; `v3_exq_634` dry-run unchanged. Smoke: Stage-0b retention 1.000; under contact-gating the Stage-0 trace survives to P2 vs decaying to ~0 on the legacy path.

**Governance.** V3-EXQ-634b (developmental-window flags ON) is the corrected nursery readiness gate. **V3-EXQ-603f stays blocked** until 634b passes. V3-EXQ-634 was left running for diagnostic value; if it fails Stage-0-lights / P1-P2-contact-absent / z_goal-collapses, that is `substrate_not_engaged` (developmental-window missing), NOT evidence against the goal stream.

---

*Author session: sd054-scaffolded-onboarding-memo-20260529T172125Z. Commissioned 2026-05-29T17:21:25Z. References: [failure_autopsy_V3-EXQ-490g-cohort_2026-05-29.md](failure_autopsy_V3-EXQ-490g-cohort_2026-05-29.md), [failure_autopsy_V3-EXQ-591_2026-05-27.md](failure_autopsy_V3-EXQ-591_2026-05-27.md), [failure_autopsy_V3-EXQ-603b_2026-05-25.md](failure_autopsy_V3-EXQ-603b_2026-05-25.md), [e2_action_divergence_substrate_design.md](e2_action_divergence_substrate_design.md), [goal_pipeline_plan.md](goal_pipeline_plan.md).*

---

## Amend 2026-06-03c (seeding-calibration + consumption-gated G3)

**Status:** IMPLEMENTED 2026-06-03 (harness layer; no `ree_core`/`goal.py`/`claims.yaml` change). Validation experiment **V3-EXQ-634c** queued; claim-free (substrate diagnostic). Session `implement-substrate-scaffolded-sd054-634b-amend-20260603T2122Z`. Routed by [failure_autopsy_V3-EXQ-634b_2026-06-03](failure_autopsy_V3-EXQ-634b_2026-06-03.md).

**What 634b proved (do not re-litigate).** The 2026-06-03b developmental-window amend works: G0 Stage-0 forced-feed PASS 3/3, **G0b Stage-0b retention PASS 3/3 (0.98-0.99) with `n_decay_only_updates=0` everywhere** — the protected window + contact-gating eliminate the decay-only washout. G2 contact improved 1/3 -> 2/3.

**The new sub-gap 634b exposed.** Contact-gating skipped only `benefit <= scaffold_p2_contact_benefit_threshold` (1e-6), but `GoalState.update` (`goal.py:209-224`) seeds z_goal only when `effective_benefit = benefit * z_goal_seeding_gain(1.0) * (1 + drive_weight(2.0)*drive_trace) > benefit_threshold(0.1)`. Natural wild benefit (`obs_body[11]` ~0.03) stays sub-threshold, so the band `(1e-6, ~0.1-effective)` was **not** skipped yet did **not** seed — it only applied the 0.5%/step decay, eroding the consolidated trace during real foraging. The result is an anti-correlation: seed 43 (forages best, 475 P2 contact-refresh calls) collapsed z_goal to ~4.5e-05; seed 42 (zero contact) "passed" G3 by carrying the untouched forced-feed nursery trace (0.4398, byte-identical to Stage-0b-end). G3-at-frozen-peak is anti-correlated with foraging.

**Fix (all behind no-op-default flags/sentinels; bit-identical when off).**
- **Decoupled contact-gating threshold.** The skip/update decision keys off a separate gating floor `scaffold_contact_gating_benefit_threshold` (sentinel `-1.0` -> fall back to the readout threshold). When set >= 0, sub-seeding whiffs in `(readout_floor, seeding_floor)` are **protected** (skipped, not decay-only updated) while the contact-RATE readout (g2 "was the infant fed at all") keeps using `scaffold_p2_contact_benefit_threshold`. Wired through `_train_episode` (P1) + `_eval_episode` (P2) via a `gating_threshold` kwarg and `Scheduler._gating_threshold()`.
- **Goal-seeding magnitude propagation.** New `scaffold_z_goal_seeding_gain` / `scaffold_benefit_threshold` / `scaffold_drive_floor` (all `Optional`, default `None` = no-op) are written onto the agent's live `GoalConfig` at the top of each seeding-capable `run_*` stage via `Scheduler._apply_goal_seeding_calibration(agent)`, so genuine wild contact can clear the GoalState firing threshold (e.g. gain 1.5 + benefit_threshold 0.02 + drive_floor 0.9 -> wild benefit 0.03 yields effective 0.126 > 0.02). GoalConfig owns the magnitudes (MECH-186/187/188 / SD-012 precedent); the scaffold propagates them so 634c can sweep them through the scaffold's own config surface.
- **Consumption-event-gated G3 readout.** `P2OnboardingMetrics` gains `z_goal_norm_at_contact_peak` (max goal-norm read AT a genuine seeding event, 632-style) + `num_contact_events`. `_eval_episode` captures the goal-norm only on a seeding step; it stays 0.0 when wild contact never clears the seeding floor, so a z_goal=0-at-contact read is interpretable rather than masked by the carried nursery trace. 634c feeds this consumption-gated peak as the G3 input.

**Division of labor.** The substrate amend owns the gating-threshold decoupling, the GoalConfig propagation surface, and the consumption-gated readout. The seeding-magnitude **values** (gain / benefit_threshold / drive_floor) + the strengthened P0/P1 foraging-competence budgets are swept per-arm by **V3-EXQ-634c** (the autopsy: "one or a combination, pick via a small sweep"), with `scaffold_contact_gating_benefit_threshold` matched to the chosen seeding floor.

**Validation.** 42/42 scaffolded contracts (incl. 6 new C8) + 7/7 preflight PASS; `v3_exq_634b` dry-run unchanged (decay_only=0, contact-gating behaviour identical). C8 covers: config no-op defaults; gating fallback-then-decouple; calibration no-op + applies (direct + via `run_p1`); the core decoupling (same 0.05 benefit PROTECTED under gating 0.1 but SEEDS under the sentinel); the G3 redesign (frozen peak > 0 from the carried trace while the consumption-gated peak == 0 + `num_contact_events` == 0 when no genuine seeding).

**Governance.** Substrate stays **NOT ready** (`ready=false`); **V3-EXQ-603f stays blocked** until V3-EXQ-634c clears a consumption-event-gated gate on >= 2/3 seeds. Claim-free diagnostic; weights no claim.

---

## Amend 2026-06-05 (foraging-competence / reach-contact residual -- GAP-2 ceiling)

**Status:** IMPLEMENTED 2026-06-05 (harness layer; no `ree_core`/`goal.py`/`claims.yaml` change). Session `implement-substrate-scaffolded-sd054-foraging-competence-20260605T2015Z`. The residual the substrate_queue `scaffolded_sd054_onboarding` title names after the 634c split: **(1) reconcile the contact-gating `contact_threshold` with the z_goal seeding firing threshold so genuine WILD contact seeds z_goal; (2) strengthen/lengthen the P0/P1 foraging-competence scaffold; (3) redefine the mature-test z_goal readout to consumption-event-gated.**

**What was already done vs this residual.** 634c (governance 2026-06-05) confirmed the z_goal **seeding half** is validated -- seeded arms reach `g3_zgoal ~0.44` at contact and the 634b contact-vs-zgoal anti-correlation is resolved. The remaining substrate-gate failure is purely **foraging-competence (reach-contact + survival)** -- the same GAP-2 ceiling tracked by 632/634/634b. The 634c dry-run shows the live signature directly: P1 `survival_gate=pass` but `contact_rate=0.0` / `contact_events=0` -- the agent survives yet never reaches food, so z_goal is never ecologically seeded.

**Three coupled, no-op-default fixes (all bit-identical OFF; the master switch + every new knob defaults inert).**

- **(1) Auto-reconcile the gating floor to the GoalState seeding firing threshold.** 634c decoupled the gating floor (`scaffold_contact_gating_benefit_threshold`) from the contact-rate readout, but it still had to be **hand-matched** to the GoalState seeding magnitudes as a magic number -- a mismatch *is* the 634b anti-correlation (the scaffold counts a step as "seeded" while `GoalState.update` only decay-updated it). New flag `scaffold_auto_reconcile_gating_to_seeding` (default `False`): when on, `Scheduler._reconciled_gating_threshold(agent)` derives the raw-benefit gating floor from the agent's **live** `GoalConfig` each stage --
  `benefit_threshold / (z_goal_seeding_gain * (1 + drive_weight * drive_floor))`
  (the steady-state lower bound, since `drive_trace >= drive_floor` per the SD-012 insatiability floor `goal.py:369`). `Scheduler._effective_gating_threshold(agent)` returns this when the flag is on, else the static `_gating_threshold()`. So the scaffold's `seeds` boolean tracks `GoalState.update`'s **actual** firing decision -- genuine wild contact that clears the floor seeds, sub-seeding whiffs stay protected -- without the experiment having to keep the two knobs in sync. The reconciled floor is recorded on `P1OnboardingResult.reconciled_gating_threshold` + `P2OnboardingMetrics.reconciled_gating_threshold`.

- **(2) Graded P1 reef-spawn weaning (foraging-competence / survival lever).** P0 spawns the agent inside the reef refuge band (safe); the legacy P1 abruptly moves spawn to the midline for **every** P1 episode, so a not-yet-competent agent faces the hazard band before its first wild contact (603e: P1 survival 1/3). New knob `scaffold_p1_reef_spawn_hold_fraction` (default `0.0`): keeps `reef_bipartite_agent_spawn_in_reef_half=True` for the first `fraction` of P1 episodes (then switches to midline), extending the developmental safety window. `_build_env` gains a `p1_spawn_in_reef_half` parameter; `run_p1` records `n_reef_spawn_episodes`. Complements `scaffold_p1_anneal_hold_fraction` (which holds the *hazard/food-attraction anneal* low) -- this holds the *spawn* safe. Paired with the SD-057 cue-recall bridge (the contact lever), so the agent both survives long enough AND has a path to approach perceived food.

- **(3) Consumption-event-gated G3 as the canonical mature-test readout.** The 634c `z_goal_norm_at_contact_peak` field (z_goal read AT a genuine 632-style seeding event) is now the **default** G3 input via new module helper `substrate_readiness_from_results(stage0_results, p1_results, p2_metrics, *, use_consumption_gated_g3=True)`. A seed carrying an untouched Stage-0 nursery trace through a zero-contact P2 (the seed-42 artifact) reads `g3=0` here -- G3 cannot be passed by a non-foraging seed. `use_consumption_gated_g3=False` falls back to the frozen `z_goal_norm_peak_max` for side-by-side comparison only; the returned dict carries a `g3_source` field.

**Acceptance target (unchanged, per the 603f gate).** `z_goal_norm_at_contact_peak > 0.4` on **>=2/3 seeds** in P2 **AND** P1 survival/foraging gate passed on **>=2/3 seeds** **AND** non-zero benefit/contact exposure on **>=2/3 seeds** -- evaluated by `substrate_readiness_from_results` (consumption-gated G3).

**Validation -- contracts + local readiness check (2026-06-05).** 79/79 scaffold contracts (9 new C11) + 7/7 preflight PASS; `v3_exq_634c --dry-run` runs unchanged (new flags off -> bit-identical). A **local readiness check** (all levers on: cue-recall bridge + reef-spawn weaning 0.4 + auto-reconcile + 634c seeding calibration drive_floor=0.9/gain=1.5/thr=0.02; moderate budget Stage0=10/P0=28/P1=40/P2=14, 3 seeds) confirms **the mechanisms work end-to-end** and the consumption-gated gate behaves correctly:
- The auto-reconcile derived the gating floor **exactly** from the live GoalConfig on every seed: `gate_floor = 0.02 / (1.5 * (1 + 2.0*0.9)) = 0.00476`.
- **seed 44 is a clean positive**: 9 genuine P2 contact events -> `z_goal_norm_at_contact_peak = 0.4456 > 0.4`. The full chain (reconciled gating -> wild contact seeds z_goal -> consumption-gated readout captures it) fires when ecological contact occurs.
- The consumption-gated G3 correctly **exposes the seed-42 artifact**: seed 42/43 carried a frozen Stage-0 trace (`z_frozen` 0.41/0.55) yet read `z_at_contact = 0.0` (zero contact) -- G3 is no longer masked by the carried trace.

**Result: `substrate_gate_passed = False`** (`stage0_positive_control` 2/3 pass; **g1_survival 1/3, g2_contact 1/3, g3_zgoal 1/3** -- each needs 2/3). The residual mechanisms are landed + validated; the gate fails on **foraging-competence** (survival + reach-contact), the same 634 split (the seed that survives makes no contact; the seed that contacts dies). Notably the cue-recall bridge fired **thousands of times** (P1: 2221/1917/711) while contact stayed ~0 on 2/3 seeds -- the cue moves z_goal but z_goal->approach->contact does not follow. That is the **cue-to-action selection-authority** ceiling (the V3-EXQ-640 autopsy finding; `modulatory-bias-selection-authority` substrate + the V3-EXQ-640a cue-authority gain sweep), which is **downstream of this scaffold** and not fixable by the developmental levers alone.

**Governance.** `ready` STAYS **false** (the readiness gate fails 1/3 on the foraging axes). The residual amend is complete: the three mechanism pieces are landed, contract-validated, and demonstrated end-to-end on the contact-positive seed. The full-scale substrate-readiness re-run is queued via `/queue-experiment` (tests whether a full P0/P1 budget lifts survival+contact to 2/3). **V3-EXQ-603f stays blocked** until the gate clears >=2/3. The persistent zero-contact on the non-foraging seeds routes to the **cue-to-action authority** thread (V3-EXQ-640a / `modulatory-bias-selection-authority`), NOT to further scaffold levers.

## Amend 2026-06-07 (curriculum decomposition -- isolated hazard-avoidance stage)

**Status: IMPLEMENTED 2026-06-07** (ree-v3 harness layer; no `ree_core` / `goal.py` / `claims.yaml` change). Routed by [failure_autopsy_V3-EXQ-603f_2026-06-07](failure_autopsy_V3-EXQ-603f_2026-06-07.md) (substrate-readiness FAIL, self-route `substrate_not_engaged / foraging_competence_open`, confirmed at Step 8).

**What 603f changed vs the 2026-06-05 prediction.** The 2026-06-05 residual entry above predicted that the persistent zero-contact routes to the cue-to-action *authority* thread. **The full-budget 603f run (P0/P1 = 100/50) superseded that routing for GAP-2.** 603f PROVED the goal-formation + ecological-seeding chain is **sound**: seed 44 foraged (P2 `contact_rate` 0.393, 85 events) **and** its contact cleanly seeded z_goal ecologically (`z_goal_norm_at_contact_peak` 0.450 > 0.4 gate) -- and it **still died** (median 28.5 < 75 survival gate). The single load-bearing GAP-2 blocker is therefore the **P1 survival / hazard-avoidance leg** (G1 **0/3**; median episode len 12.5/38.0/28.5), not goal-formation, cue-recall, or contact wiring. The seed-44 disambiguator falsifies the cue-authority route for GAP-2: cue->food selection-authority (what 640b tests) cannot rescue an agent that dies to hazards, and approaching food under `hfa=0.3` plausibly *raises* exposure. **640b remains valid for the GAP-7 cue-authority claim but does not address the GAP-2 survival ceiling.**

**Root cause.** P1 couples **two competencies at once** -- goal-pipeline unfreeze **and** wean into the hazard band -- and the agent cannot acquire both simultaneously. P0 trains only in the safe reef refuge (mean episode len 96.6-100.9), so the agent never learns hazard navigation before P1 throws it at the midline hazard band (collapse to median 12-38).

**The fix (user-directed, AskUserQuestion 2026-06-07 "Stage-H only").** A **separately-trained isolated hazard-avoidance stage (Stage-H)** inserted between P0 and P1, so the competencies are trained in isolation: survival/avoidance alone in Stage-H, then the existing goal-unfreeze + final-hazard-ramp in P1, now entered by an already-survival-AND-goal-competent policy.
- New `ScaffoldedSD054OnboardingScheduler.run_hazard_avoidance(agent, device)` + `HazardAvoidanceResult`. Goal pipeline **FROZEN** (`_set_goal_pipeline_frozen(frozen=True)`, `seed_goal=False` -> `update_z_goal` never called, z_goal untouched -- the isolation); trains E1+E2 (+E3 running-variance) exactly like `run_p0`; reports a median-episode-length survival readout (**G_H**, diagnostic only -- does NOT change the canonical G0/G1/G2/G3 gate).
- New `_build_env` phase `"hazard"`: hazards present (`num_hazards` 4), foraging minimal (`num_resources` 2), `hazard_food_attraction=0.0` (hazards drift randomly so foraging does NOT raise hazard exposure -- clean avoidance signal), `proximity_harm_scale=0.1` (target level), **midline spawn** (so the agent must navigate the hazard band; the reef refuge stays available as the flee-to-safety attractor). Same structural kwargs as every other phase -> `world_obs_dim` matches the single shared agent.
- Config (all no-op default, bit-identical OFF): `scaffold_hazard_stage_enabled` (False) + `_episode_budget` (40) + `_num_hazards` (4) + `_num_resources` (2) + `_hazard_food_attraction` (0.0) + `_proximity_harm_scale` (0.1) + `_spawn_in_reef_half` (False) + `_survival_gate_steps` (75) + `_stability_window` (10).

**Curriculum becomes:** Stage-0 (forced feed) -> Stage-0b (consolidate) -> P0 (encoder warm-up, goal frozen) -> **Stage-H (isolated hazard avoidance, goal frozen)** -> P1 (combined wean) -> P2 (measure). Legs (1) safe goal-attainment and (3) combined wean are covered by the existing Stage-0 / P0 / early-P1 levers (extendable via budgets + anneal/reef-spawn holds in the 603g config). The optional **forced-choice micro-env** variant (each adjacent cell a distinct goal/hazard/free affordance) is **deferred** -- it needs a new `CausalGridWorldV2` env mode (a `ree_core` change), orthogonal to this curriculum-structure fix.

**Backward compatible.** Master switch + every new knob default inert; `run_hazard_avoidance` aborts when disabled; existing scripts never call it; `STAGE_PLAN` + its 5-stage contract untouched. **85/85** scaffold contracts (79 prior + 6 new **C12**) + 7/7 preflight PASS; `v3_exq_603f --dry-run` runs unchanged. Phased training N/A (an additional goal-frozen E1/E2/E3 warm-up phase; no new encoder head / latent target / collapse risk). MECH-094 N/A (waking onboarding; no simulation/replay write surface). Evidence-staleness NOT triggered (no-op-default curriculum-structure amend; every existing experiment uses the default disabled stage -> no dependent claim's measured mechanism changed; KEEP all evidence).

**Governance.** `ready` STAYS **false**. Validation is the re-issued substrate-readiness run **V3-EXQ-603g** (copy of 603f with Stage-H inserted ON + a G_H survival diagnostic) against the **same G0/G1/G2/G3 gate**. **GAP-2 stays `blocked_pending_substrate` until 603g clears G1>=2/3 AND G2>=2/3 AND ecological G3>=2/3.** Session `implement-substrate-scaffolded-sd054-curriculum-decomp-20260607T0612Z`.


## Amend 2026-06-09 (Stage-H harm-pathway training -- the 603i nav/survival-competence fix)

**Status: IMPLEMENTED 2026-06-09** (ree-v3 harness layer; no `ree_core` / `goal.py` / `claims.yaml` change -- the block calls EXISTING ree_core harm heads). Routed by [failure_autopsy_V3-EXQ-603i_2026-06-08](failure_autopsy_V3-EXQ-603i_2026-06-08.md) (PRIMARY: nav/survival-competence ceiling -- `ARM_NAV_CONTROL` spawn-in-reef `G_H=0.0`) + the [603g/624c/651a cluster autopsy](failure_autopsy_V3-EXQ-603g-624c-651a_2026-06-07.md) ("deeper than budget", user-adjudicated) + lit verdict `targeted_review_hazard_avoidance_learning`.

**Root cause -- diagnosed first (code trace + empirical probe), NOT assumed.** The Stage-H curriculum-decomposition amend (above) isolated the survival leg but it still did not train (603g/603h/603i G_H 0/3). A code trace of `_train_episode` shows why: across the **entire** curriculum (Stage-0/0b/P0/Stage-H/P1/P2) the only optimized parameters are **E1** (`compute_prediction_loss`, the LSTM MSE) and **E2.world_transition/world_action_encoder**. The hazard-avoidance **VALUATION** pathway is never in any optimizer:
- `E3.harm_eval_head(z_world)` -- the harm cost that scores **every candidate trajectory** in `E3.select` (`e3_selector.py:419/564`) -- is a **near-constant ~0.523** (random init).
- `HarmEncoder` (z_harm), `AffectiveHarmEncoder` (z_harm_a), `E3.harm_eval_z_harm_head`, `E2_harm_s` (ARC-033): all random-init / untrained.
- `env.step`'s realized `_harm_signal` (the natural supervision target) is **discarded** at the call site.

An instrumented probe (2026-06-09, ARM_NAV_CONTROL spawn-in-reef, reduced budget) confirmed the consequence with data: `harm_eval_head(z_world)` output range **[0.522, 0.524]** across 300 states (a flat constant -- the agent cannot distinguish a refuge cell from a hazard-adjacent cell); `||z_harm||` vs true proximity correlation **NaN** (zero variance); Stage-H survival slope **-0.94 steps/ep** (no learning, gets *worse*); **24/25** episodes die early even handed the reef refuge; median last-window **23** vs the **75** gate. **More budget cannot train a head that is not in the loss** -- this is a missing-mechanism / training-coverage gap, confirming the cluster autopsy's "deeper than budget" adjudication. It also explains why SD-058/MECH-357 (IA gate) and SD-059/MECH-358 (escape bridge) were "engaged but insufficient": they bias action selection within whatever harm landscape E3 hands them, and that landscape is noise.

**The fix (user-confirmed FULL scope + encoder co-train, AskUserQuestion 2026-06-09).** Train the existing-but-untrained harm pathway during **P0 + Stage-H**, supervised by the env hazard-proximity label (`harm_obs` centre; SD-010/SD-018) + accumulated-harm scalar (SD-011). Four independently-toggleable terms (Q-044 / MECH-314a-style ablatability):
1. **harm_eval(z_world)** -- `E3.harm_eval_head` **+ the z_world encoder**. The proximity MSE backprops **into** `latent_stack` (SD-018 semantics) so z_world becomes hazard-discriminative -- head-only training fails on the flat z_world the probe measured. **Load-bearing**: makes the trajectory-rollout harm landscape (`E2.world_forward` -> `harm_eval_head`) predictive.
2. **z_harm sensory** -- `HarmEncoder` + `E3.harm_eval_z_harm_head` (SD-010) on the same label.
3. **z_harm_a affective** -- `AffectiveHarmEncoder` via `compute_harm_accum_loss` (SD-011) -- trains the threat signal MECH-279 PAG + SD-058 IA gate + SD-059 bridge key on.
4. **E2_harm_s forward** -- `E2HarmSForward` (ARC-033) on FROZEN (detached) z_harm_s for multi-step harm lookahead.

**Config (all no-op default, bit-identical OFF):** `scaffold_train_harm_pathway` (False, master) + `scaffold_train_harm_eval_head` / `_z_harm_sensory` / `_z_harm_affective` / `_e2_harm_s_forward` (True; consulted only when master on) + `scaffold_harm_pathway_lr` (1e-3) + `scaffold_harm_pathway_in_p0` (True) + `scaffold_harm_s_buf_max` (2000). New module helpers `_hazard_proximity_target` / `_accumulated_harm_target` / `_harm_pathway_params` / `_harm_pathway_step` / `_measure_harm_discriminativeness`; `Scheduler._make_harm_pathway` builds the optimizer/buffer/diag; `run_p0` (when `in_p0`) + `run_hazard_avoidance` thread the training through `_train_episode`. Terms 2+4 require the agent built with `use_harm_stream=True` (sensory z_harm) + `use_e2_harm_s_forward=True`; inert no-op (correctly skipped) when absent -- the 603k config enables both so all four terms engage.

**Backward compatible.** Master OFF -> `train_harm` False, `harm_opt` None, the harm block + the Stage-H discriminativeness probe skipped -> bit-identical. **97/97** scaffold contracts (91 prior + 6 new **C15**) + 7/7 preflight PASS. **Activation smoke 2026-06-09** (ARM_NAV_CONTROL spawn-in-reef, harm pathway ON, reduced budget): `survival_gate_passed=True`, **median_last_window=80.0** (vs OFF probe 23.0, gate 75); survival slope **+0.19** (vs OFF -0.94); early deaths **9/25** (vs OFF 24/25); `harm_eval` loss trains (n_train_steps 586 P0 + 1511 Stage-H). The headline -- **G_H 0 -> survival_passed=True** -- validates both the diagnosis and the fix at smoke scale. Phased training: the proximity heads co-train with their encoder (SD-010/SD-018 single regression, no collapse risk); E2_harm_s on detached z_harm_s (ARC-033 P1 phasing). MECH-094 N/A (waking training; no simulation/replay write). Evidence-staleness NOT triggered (no-op-default flag; KEEP all evidence).

**Governance.** `ready` STAYS **false**. Validation: **V3-EXQ-603k** substrate-readiness diagnostic (`claim_ids=[]`; HARM_OFF vs HARM_ON ablation on the 603i-INTACT base + nav-competence reef spawn; `use_harm_stream=True` + `use_e2_harm_s_forward=True`). Acceptance per the 603i failure-record target: Stage-H **G_H >= 2/3** (median last-window >= 75) with nav-to-safety handed AND a **non-vacuity gate** (harm_eval discriminativeness lifts above the flat baseline) AND the HARM_OFF arm reproduces `G_H ~ 0`. **PASS unblocks the escape-affordance-bridge retest** (the bridge can finally be scored once survival clears) + the GAP-2 survival-leg cohort. Session `implement-substrate-stageh-harm-pathway-20260609T0456Z`.

## Amend 2026-06-16 (harm-pathway training STABILIZATION -- the 603p seed-fragility fix)

**Status:** IMPLEMENTED 2026-06-16. behavioral_diversity_isolation:GAP-C; ISOLATED harm-valuation subsystem (no GAP-A overlap). Routed by the confirmed `failure_autopsy_V3-EXQ-603p_2026-06-15` (Branch B, user-confirmed).

**Problem (603p, claim-free Stage-H base-harm-landscape diagnostic).** The 2026-06-09 harm-pathway training (above) is in the optimizer but **seed-fragile**: the base harm landscape `E3.harm_eval_head(z_world)` clears `harm_eval_range >= 0.02` on only **1/3 seeds** at the EASIEST regime (proximity_harm=0.10; per-seed [0.166 PASS, 0.0057, 0.0]), and tripling the global harm-pathway LR to 3e-3 **COLLAPSES** it to ~1e-23 on all three seeds. Root cause (code-confirmed): `_make_harm_pathway` builds a **single** `Adam` group at `scaffold_harm_pathway_lr` (1e-3) that co-trains the `latent_stack` ENCODER (the SD-018 proximity MSE backprops into it) AND the harm HEADS. Raising that one LR drives the encoder to the trivial constant-z_world solution (range -> 0 = the 3x-LR collapse); 1e-3 leaves most seeds under-converged. The mechanism is RIGHT (where it forms, prox_corr 0.44-0.83); convergence/seed-robustness is the gap. NOT a budget tweak; **NOT a global-LR raise** (it collapses the landscape).

**The substrate change (two no-op-default levers; bit-identical OFF; stabilize WITHOUT raising the global LR):**

1. `scaffold_harm_pathway_encoder_lr` (Optional[float], default **None**). When set, the `latent_stack` ENCODER params get their own Adam param group at this (typically LOWER) LR while the harm heads + E2_harm_s keep `scaffold_harm_pathway_lr` -- the encoder moves gently (escaping the collapse-to-constant basin) while the heads still extract the proximity mapping at the base rate. None -> single Adam group at `scaffold_harm_pathway_lr` (bit-identical legacy optimizer). New helper `_harm_pathway_param_groups` builds the two disjoint groups (shared encoder-first dedup -> no param in two groups).
2. `scaffold_harm_pathway_warmup_steps` (int, default **0**). Linear LR warmup over the first N harm-pathway steps -- scales every param group's LR from base/N up to base, then holds at base, easing the early-training basin where the encoder is most prone to collapse (gradient stabilization). 0 -> no scaling (bit-identical). Applied per param group in `_harm_pathway_step` right before the existing grad-clip + step; the per-group base LRs are stashed on `harm_opt._harm_base_lrs` at construction.

These cover the autopsy's primary prescriptions (lower [encoder] LR with the heads still at base + gradient stabilization); the "more training steps" candidate stays available via the existing budget knobs. (Seed-robust head re-init is a deferred fourth lever -- the encoder-LR decoupling already removes the encoder-collapse instability that makes success seed-dependent.)

**Backward compatible.** Both levers default OFF -> single-group Adam at base LR, no LR scaling -> bit-identical to the 2026-06-09 harm-pathway optimizer. **102/102** scaffold contracts (97 prior + 5 new **C16**) + 7/7 preflight PASS. Phased training: N/A (changes only the harm-pathway optimizer param-group LRs + a warmup schedule; no new encoder head / latent target). MECH-094 N/A (waking onboarding; no simulation/replay write). Evidence-staleness NOT triggered (no-op-default levers; KEEP all evidence).

**In-session validation (proof-of-fix probe; `ree-v3/scripts/_validate_603q_harm_amend.py` replicates the 603p positive-control cell via 603p's own config builders):** the levers run END-TO-END in the real 603p pipeline and the harm head learns the correct proximity mapping (prox_corr positive even at reduced budget). The full-scale `>=2/3`-seed seed-robustness confirmation at proximity_harm=0.10 is carried as **V3-EXQ-603q's FIRST self-routing non-vacuity precondition** (the cloud establishes it; 603q self-routes `substrate_not_ready_requeue` if the base does not clear `>=2/3`, never a false bridge verdict) -- per the GAP-C durable 603q spec.

**Governance.** `ready` STAYS **false** until V3-EXQ-603q's base-discriminativeness precondition clears `>=2/3`. SD-059 / MECH-358 / MECH-313 / MECH-260 / Q-045 stay at current status (NOT weakened). The harm-pathway leg's "VALIDATED 2026-06-09 (V3-EXQ-603k PASS)" status was a NARROW probe -- this amend bakes a `>=2/3`-seed gate on the DIRECT `harm_eval_range` statistic into the readiness criterion. Validation: **V3-EXQ-603q** (the corrected SD-059/MECH-358 escape-affordance-bridge EVIDENCE re-run, bridge ON vs base) runs on the now-stabilized base with the two levers ON + the base-harm-landscape `>=2/3` discriminativeness as a self-routing precondition. Session `implement-substrate-harm-pathway-leg-603q-20260616T0717Z`.
