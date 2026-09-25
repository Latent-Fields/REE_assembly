# CeA gate calibration probe: does a scale-aware gate fire at hazard ONSET? (2026-09-25)

- **Session:** `bt0925-ceacal` (breakthrough integration pass `orchestrate-20260924-breakthrough`), chip_ref `chip-20260925-cea-gate-calibration-probe`.
- **Scope:** probe only. No ree_core edits, no queue entries, no claims.yaml edits, no chips.
- **Code under test:** ree-v3 `origin/main` @ **`aa14769`** (private detached worktree). Every `file:line` is against that sha.
- **Context:** `mode_switch_cea_mechanism_trace_20260925.md` Q2 (`e2bbd2a98e`); GFLAG-0554. The CeA gate (`ree_core/amygdala/cea.py:309-337`) is `low_freq = ||z_harm_a||_1 / dim > 0.5`. On an uncalibrated encoder that is 0.14-0.20 untrained (never fires) and 12-17 after SD-011 harm_accum training (always fires).

## PRE-REGISTRATION (written and committed before any readout was computed)

Written 2026-09-25T14:53Z.

### Question

Does a gate that reads `s_t = mean|z_harm_a|` (the CeA `low_freq` input, unchanged) **relative to its own recent history** fire selectively at hazard ONSET, under both encoder regimes, where the fixed absolute threshold does not? The gate variants are computed harness-side from `s_t`. ree_core is not edited.

### Design

- **Environment and agent.** EXP-0787 probe config, as in the modetrace probe. Changes: `harm_history_len=10`, so the SD-011 `harm_accum_head` exists and regime B can train, and no salience/dACC changes. `CausalGridWorldV2(size=10, num_hazards=3, num_resources=3, harm_history_len=10)`. `world_dim = self_dim = 32` (deployed). The agent is untrained and driven through `experiments/_harness.StepHarness` (`train_mode=False`). An external hazard is injected every 30 steps (t % 30 == 15), as in the trace. Seeds 11/12/13. `torch.set_num_threads(2)`.
- **Two recorded trajectories per seed:** TRAIN, 2000 env steps, and EVAL, 1000 env steps. EVAL is a separate env/agent instance with seed + 1000. At each step I record `harm_obs_a`, `harm_history`, `harm_obs[-1]` (harm_exposure), the env's `hazard_field` at the agent cell, `transition_type`, and the episode index. For regime A only, I also record the agent's own `_cea_last_output.low_freq_magnitude` as an instrument check: my recomputed `s_t` must match it.
- **Why offline on recorded inputs.** Both regimes are scored on the **identical** EVAL input sequence, a matched comparison. The gate variants are pure functions of `s_t`. The recorded trajectory does not depend on the gate, because the CeA output has no behavioural consumer in this config (trace section 1c: A4/A5 episode counts identical). Encoder weights could in principle perturb actions through other z_harm_a consumers. I accept that, and the uncertainty section states it.
- **Encoder regimes.**
  - **A (untrained):** the agent's encoder at init.
  - **B (harm_accum-trained, native weight):** a deep copy of the same encoder, trained **online, one Adam step per TRAIN step, in time order, batch 1**. Loss = `0.1 x MSE(harm_accum_pred, target)`. This is exactly `agent.compute_harm_accum_loss` (`agent.py:12690-12753`, weight `z_harm_a_aux_loss_weight = 0.1`, `config.py:323`). The target is the 935a native target, `harm_obs[-1]` = harm_exposure (`experiments/scaffolded_sd054_onboarding.py:1293-1301`). Adam lr 1e-3. One pass over the 2000 TRAIN steps is the primary regime B. Checkpoints at 0/250/500/1000/2000 steps are recorded for the scale trajectory. A 3-pass version (6000 steps) is secondary.
  - **Honest note, stated before running.** Adam is invariant to the loss scale on a parameter group that receives no other gradient. So weight 0.1 vs 1 changes almost nothing about the trajectory. Online batch-1 training at the native target differs from the trace's offline batch-32 run at weight 1.
- **Ground truth (EVAL).** `h_t` = `hazard_field[agent cell]` after step t (clipped to [0,1]).
  - **Hazard step:** `h_t >= 0.15` (`proximity_approach_threshold`, `causal_grid_world.py:348`) OR `transition_type == "env_caused_hazard"`.
  - **ONSET:** a hazard step whose previous 3 steps, all in the same episode, were non-hazard.
  - **Onset window:** steps `[t_on, t_on + N]`, **N = 5**.
  - **Non-hazard pool (FA pool):** non-hazard steps that lie outside every onset window and are not among the first 3 steps of an episode.
  - **Alignment.** `s_t` is computed from the obs after step t (the obs CeA reads on the next `sense()`), and it is scored against `h_t` on the same index.
- **Gate variants** on `s_t`. All are causal and online. Running statistics update AFTER the gate is evaluated at t. A variant cannot fire in the first 20 EVAL steps (warmup), except (i), which has no state. Pre-registered thresholds:
  - **(i) fixed:** fire iff `s_t > 0.5` (current `cea.py:337`).
  - **(ii) running z-score:** `mu`, `var` are EMA with beta = 0.05. Fire iff `(s_t - mu)/sd > 2.0`, with `sd = max(sqrt(var), 1e-3*|mu| + 1e-8)`.
  - **(iii) rate-of-change (onset detector):** `d_t = s_t - s_{t-1}`, `sd_d` = sqrt of an EMA (beta 0.05) of `d^2`. Fire iff `d_t > 2.0 x sd_d` and `d_t > 0`.
  - **(iv) ratio to a slow baseline:** `b` = EMA of `s` (beta 0.01), initialised to `s_0`. Fire iff `s_t / b > 1.25`.
- **Readouts** per (seed, regime, variant):
  - hit rate `H` = fraction of onsets with >= 1 fire in the onset window;
  - per-step FA rate `F` over the non-hazard pool;
  - window-matched FA `F_w = 1 - (1 - F)^(N+1)`, i.e. the chance that a gate firing at rate F lands in a 6-step window;
  - **d' = z(H) - z(F_w)**, with log-linear correction `H = (hits+0.5)/(n_on+1)` and `F = (fa+0.5)/(n_pool+1)`, so chance = 0;
  - fire rate on sustained hazard steps (hazard steps outside onset windows), descriptive;
  - median latency from onset to first fire.
- **Secondary (labelled post hoc when reported):** a threshold sweep per variant, giving the best d' over a grid. This separates "variant family can work" from "my threshold was wrong".
- **Arithmetic readout (D0):** can the salience contribution reach the switch threshold under each variant, and which mode does it push toward? Taken from `cea.py:335-365`, `agent.py:2573-2577` and `salience_coordinator.py:311,664-694`.

### Pre-registered predictions and decision rules

- **P1.** (i) is degenerate in both regimes. In A, F = 0 and H = 0 (never fires). In B, F ~ 1 and H ~ 1 (always fires). |d'| < 0.5.
- **P2.** (iii) rate-of-change has the highest pooled d' of the four in BOTH regimes, because `harm_obs_a` is an EMA of hazard-at-agent (alpha 0.05, `causal_grid_world.py:3033-3038`), so its first difference is proportional to `(h_t - ema)`, a step-onset signal. Prediction: pooled d' >= 1.0 in A.
- **P3.** Scale invariance. For (ii)-(iv), `|d'(A) - d'(B)| < 0.5` if training preserves the hazard ordering of `s`. If B's d' collapses (< 0.5) while A's does not, the harm_accum objective destroyed the onset information, not only the scale.
- **P4 (confound check).** `harm_obs_a` also carries the resource EMA (`[25:]`). A variant whose false alarms concentrate on resource approach is reading approach-in-general, not threat. I report FA split by resource-approach vs other steps (`resource_field` at agent >= 0.15).
- **Decision.** The best variant = highest pooled d' (3 seeds pooled onsets/pool) in the regime where it is lower (min over A, B), provided H >= 0.5. If no variant reaches pooled d' >= 1.0 in both regimes, the answer is "no harness-side re-reading of `mean|z_harm_a|` gives an onset-selective gate". The fix is then in the encoder or the input, not the gate. Either way it routes to the SD-035 / MECH-046 owner. I do not build.

### Budget and shrink rule

~75 min Mac wall. Mac CPU lock (`mac_probe.lock`) per process; one process at a time. If one seed takes > 10 min, TRAIN shrinks to 1000 and EVAL to 600, and I say so.

### PRE-REGISTRATION AMENDMENT 1 (2026-09-25T15:05Z, before any gate readout was computed)

A 60-step timing smoke (seed 11 EVAL) recorded only the ground-truth channels. It showed that the pre-registered ground truth is **degenerate**. `hazard_field[agent cell] >= 0.15` held on **60/60** steps; recorded values were 0.74-1.0.

- **Why.** The field is `sum over hazards of 1/(1 + 0.5 x ManhattanDist)` (`causal_grid_world.py:4746-4750`). On a 10x10 grid with 3 hazards, each hazard contributes >= 0.1 anywhere, so the field is >= ~0.3 everywhere and clips to 1.0 near any hazard. The `hazard_approach` transition (threshold 0.15, `:2720-2740`) therefore fires on almost every non-contact step.
- **Consequence for the input.** The same saturated scalar is what `harm_obs_a[:25]` EMAs (`:3035-3037`). The result section reports this as a finding about the input itself.
- **The smoke also showed** that `harm_obs_a_ema` starts at 0 on a fresh env and warms up over ~100 steps, so `s_t` is warm-up-dominated at first.

Amended, in place of the ground-truth bullets above. Everything else stands.

- **Hazard step:** Manhattan distance from the agent cell to the nearest `env.hazards` entry `d_min <= 1`, OR `transition_type == "env_caused_hazard"` (contact). **ONSET:** a hazard step whose previous 3 steps, all in the same episode, have `d_min >= 2`. Window N = 5 as before. FA pool: steps with `d_min >= 2` outside every onset window, excluding the first 3 steps of each episode.
- **Burn-in:** EVAL records 1100 steps. The first 100 run the gate statistics but are not scored.
- **Added control (v), input ceiling:** the same four gates applied to the raw input scalar `x_t = harm_obs_a[0]`, with no encoder. This bounds what any gate reading this input can do, and separates an encoder limit from an input limit. Its thresholds are the same as (i)-(iv), except that (i) on the raw input uses 0.5 as well, which is purely descriptive.
- P1-P4 and the decision rule are unchanged.

## RESULTS

(pending -- filled after the runs)
