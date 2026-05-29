# Scaffolded SD-054 onboarding -- substrate design memo

**Date:** 2026-05-29
**Author session:** `sd054-scaffolded-onboarding-memo-20260529T172125Z`
**Status:** plan-of-record for the goal-pipeline training-regime fix (substrate prereq #2 from the 591 autopsy)
**Lever chosen:** (A2) scaffolded SD-054 reef + bipartite-horizontal as the start-state distribution for P0+P1 training, with hazard_food_attraction and goal-pipeline writes annealed in across P1
**Successor session:** `/implement-substrate` on a new scheduler (sibling to `experiments/infant_curriculum.py`) AND a small spawn-relaxation extension on CausalGridWorldV2 (separate)

---

## Origin

Commissioned after the [2026-05-29 V3-EXQ-490g cohort autopsy](failure_autopsy_V3-EXQ-490g-cohort_2026-05-29.md) (commit `12f0dda773`) and user-confirmed sub-lever choice (A2). The autopsy's Fork B disposition for V3-EXQ-603c routes to `/implement-substrate` with `recommended_substrate_queue_entry.action=create` for a new SD-XXX scaffolded-SD-054-onboarding substrate. This memo is the canonical-shape sibling of the 2026-05-28 [E2 action-conditional divergence memo](e2_action_divergence_substrate_design.md): a substrate-design plan-of-record that a follow-on `/implement-substrate` session will execute against. It does not edit code.

The autopsy split a five-experiment cohort into two structurally distinct clusters. Cluster A (V3-EXQ-483c, 524a) is a GAP-4 Tier-1 library measurement gap that routes to `/queue-experiment` (Tier-1 library rebuild) -- **not in scope here**. Cluster B (V3-EXQ-603c) cluster-absorbs into the [2026-05-27 V3-EXQ-591 autopsy](failure_autopsy_V3-EXQ-591_2026-05-27.md) substrate-uniform z_goal-zero family. This memo addresses Cluster B at the substrate-design level by specifying the new SD-XXX-scaffolded-sd054-onboarding substrate that prereq #2 of the 591 autopsy ("goal-pipeline training regime produces non-trivial z_goal in default config") requires.

---

## What is broken

The goal-pipeline substrate is wired correctly in isolation. V3-EXQ-493 (2026-04-27/28) confirmed MECH-295 cue-side bias produces monotone-negative `score_bias` with the severed-bridge falsifier collapsing to zero (UC1-UC6 PASS). The downstream cascade `drive -> liking-stream -> approach cue` is inert under realistic policy state across V3-EXQ-540 series, 590a, 591, 603/603b/603c -- the substrate-uniform z_goal-zero family enumerated in the 591 autopsy §6.

V3-EXQ-603c (2026-05-27) was the predecessor 603-chain extension that added P0+P1 phased training (Fix C from the [2026-05-25 V3-EXQ-603b autopsy](failure_autopsy_V3-EXQ-603b_2026-05-25.md)) and a Fix D pre-measurement seed-stability gate (median episode length at end of P1 >= `FIFO_WARMUP_STEPS=75`). It FAILed. Manifest `metrics.json: values = {}` with `status: FAIL` and `outcome: None`. The script's `_evidence_direction_per_claim` correctly routed all three claims (Q-045, MECH-313, MECH-260) to `non_contributory` because `n_p2_cells < total_cells / 2` -- the structurally-underpowered branch the script was designed to detect.

The root reading: most (arm, seed) cells aborted at P0 (running_variance not converging in [`P0_BUDGET=100`](../../../ree-v3/experiments/v3_exq_603c_q045_mech313_mech260_phased_training.py) episodes) or failed the Fix D survival gate (`median episode length < 75` over the last 10 P1 episodes). The target env -- SD-054 reef + bipartite-horizontal + `hazard_food_attraction=0.7` + `proximity_harm_scale=0.1` + `num_hazards=4` + `num_resources=5` -- is structurally hostile to a random-init agent. The agent dies before z_goal can develop.

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

Suggested module surface: `ree-v3/experiments/scaffolded_sd054_onboarding.py` containing `ScaffoldedSD054OnboardingScheduler` + the new env-kwarg passthrough. The scheduler exposes `run_p0()`, `run_p1()`, `run_p2()`, and `clone_trained_agent()` helpers in the [committed_mode_curriculum.py](../../../ree-v3/experiments/committed_mode_curriculum.py) pattern landed for GAP-11.

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

*Author session: sd054-scaffolded-onboarding-memo-20260529T172125Z. Commissioned 2026-05-29T17:21:25Z. References: [failure_autopsy_V3-EXQ-490g-cohort_2026-05-29.md](failure_autopsy_V3-EXQ-490g-cohort_2026-05-29.md), [failure_autopsy_V3-EXQ-591_2026-05-27.md](failure_autopsy_V3-EXQ-591_2026-05-27.md), [failure_autopsy_V3-EXQ-603b_2026-05-25.md](failure_autopsy_V3-EXQ-603b_2026-05-25.md), [e2_action_divergence_substrate_design.md](e2_action_divergence_substrate_design.md), [goal_pipeline_plan.md](goal_pipeline_plan.md).*
