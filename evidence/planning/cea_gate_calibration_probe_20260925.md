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

### PRE-REGISTRATION AMENDMENT 1 (2026-09-25T14:56Z, before any gate readout was computed; committed d0a405af486)

*Correction:* the header of this amendment originally said 15:05Z. The actual write/commit time was 14:56Z; I corrected it in the results commit.

A 60-step timing smoke (seed 11 EVAL) recorded only the ground-truth channels. It showed that the pre-registered ground truth is **degenerate**. `hazard_field[agent cell] >= 0.15` held on **60/60** steps; recorded values were 0.74-1.0.

- **Why.** The field is `sum over hazards of 1/(1 + 0.5 x ManhattanDist)` (`causal_grid_world.py:4746-4750`). On a 10x10 grid with 3 hazards, each hazard contributes >= 0.1 anywhere, so the field is >= ~0.3 everywhere and clips to 1.0 near any hazard. The `hazard_approach` transition (threshold 0.15, `:2720-2740`) therefore fires on almost every non-contact step.
- **Consequence for the input.** The same saturated scalar is what `harm_obs_a[:25]` EMAs (`:3035-3037`). The result section reports this as a finding about the input itself.
- **The smoke also showed** that `harm_obs_a_ema` starts at 0 on a fresh env and warms up over ~100 steps, so `s_t` is warm-up-dominated at first.

Amended, in place of the ground-truth bullets above. Everything else stands.

- **Hazard step:** Manhattan distance from the agent cell to the nearest `env.hazards` entry `d_min <= 1`, OR `transition_type == "env_caused_hazard"` (contact). **ONSET:** a hazard step whose previous 3 steps, all in the same episode, have `d_min >= 2`. Window N = 5 as before. FA pool: steps with `d_min >= 2` outside every onset window, excluding the first 3 steps of each episode.
- **Burn-in:** EVAL records 1100 steps. The first 100 run the gate statistics but are not scored.
- **Added control (v), input ceiling:** the same four gates applied to the raw input scalar `x_t = harm_obs_a[0]`, with no encoder. This bounds what any gate reading this input can do, and separates an encoder limit from an input limit. Its thresholds are the same as (i)-(iv), except that (i) on the raw input uses 0.5 as well, which is purely descriptive.
- P1-P4 and the decision rule are unchanged.

## RESULTS (written 2026-09-25T16:25Z)

**Runs.** 3 seeds (11/12/13). Each has a TRAIN recording (2000 steps, env seed s) and an EVAL recording (1100 steps, env seed s+1000, 100 burn-in), made with `probes/ceacal/ceacal_record.py`. The Mac wall per recording was 100-370 s.
- **Analysis:** offline in `ceacal_analyze.py`, pooled in `ceacal_pool.py`. Raw per-seed JSON is in `probes/ceacal/results/ana_<seed>_p<passes>.json`, pooled results in `pooled_p1.*` / `pooled_p3.*`.
- **Sample:** 106 onsets pooled (34/37/35) and 1645 non-hazard pool steps (560/525/560).
- **Instrument check passed.** My recomputed `s_t` matches the agent's own CeA `low_freq_magnitude` to <= 6e-8 on all 3 x 1100 steps.
- **Dims:** `world_dim = self_dim = 32` (deployed), `z_harm_a_dim = 16`.
- **Deviation 1.** The pre-registered ground truth was degenerate: Amendment 1, committed before any readout.
- **Deviation 2.** The analysis stage was 6 processes totalling ~18 s CPU, offline, with no env stepping. It ran **without** `mac_probe.lock`, single-threaded. I waited ~60 min on the lock and it was re-acquired back-to-back by another worker's job chain (bt0925-rt5), so my 30 s poll never won. All env-stepping recordings ran under the lock.

### R1. Pre-registered readout: no variant is onset-selective, in either regime (D1)

Pooled over 3 seeds, pre-registered thresholds, 1-pass regime B. `H` = onsets with >= 1 fire in [t_on, t_on+5]. `F` = per-step fire rate on the non-hazard pool. `d'` = z(H) - z(1-(1-F)^6).

| regime | (i) fixed 0.5 | (ii) running z > 2 | (iii) rate > 2 sd | (iv) ratio > 1.25 |
|---|---|---|---|---|
| A untrained | H 0/106, F 0 -> never fires | H 0/106, F 0.006; d' -0.82 | H 6/106, F 0.015; d' -0.18 | H 7/106, F 0.052; d' -0.88 |
| B harm_accum (w 0.1) | H 106/106, F 1.000 -> always fires; d' -3.40 | H 2/106, F 0.005; d' -0.12 | H 6/106, F 0.005; d' +0.32 | H 7/106, F 0.076; d' -1.17 |
| control (v): raw input `harm_obs_a[0]` | always fires | H 0/106 | H 5/106, F 0.003; d' +0.43 | H 10/106, F 0.094; d' -1.16 |

- **Correction floor.** d' = +0.31 is what a gate with **zero** fires and zero false alarms scores after the log-linear correction. d' values near +0.3 therefore mean "silent", not "selective".
- **Post-hoc threshold sweep** (best of 40 quantile thresholds per seed): the maximum per-seed d' was 0.85 (A, iii; seed 13) and 0.84 (raw, iii). Each of those is 0-1 hits at F ~ 0. That is a sweep over noise, not a working operating point.
- **The 3-pass regime B** (`pooled_p3.txt`) gives the same picture: best (iii) d' +0.26, H 7/106.

**P1 confirmed.** (i) is degenerate in both regimes: never fires untrained, always fires trained.

**P2 refuted.** (iii) has the best pooled d' in regime B, but it does not reach 1.0 in either regime (A -0.18, B +0.32). Its hit rate is ~6%.

**P3: vacuous.** The relative gates are scale-invariant (A and B within 0.5 d' for ii/iii/iv), but invariantly at chance. There is no onset information for training to preserve.

**P4: not informative.** The FA rates are near zero. For (iii) in A, FA on resource-adjacent pool steps is 0.02-0.04 vs 0.004-0.025 on other steps, a weak tilt on tiny counts.

**Decision rule outcome: no variant qualifies.** By the pre-registered rule, the answer is that **no harness-side re-reading of `mean|z_harm_a|` gives an onset-selective gate.** The nominal "best" (highest minimum-over-regimes pooled d') is (iii) rate-of-change, and it is at chance. I do not name it as a working variant.

### R2. Why: the onset information is destroyed upstream of the encoder, in the input EMA (D1, the main finding)

- **The pre-EMA env scalar carries adjacency** (`ceacal_hz_check.py`, `results/hz_check.json`). `hazard_at_agent = clip(hazard_field[agent], 0, 1)` (`causal_grid_world.py:3035`) is what `harm_obs_a[:25]` EMAs. It separates hazard-adjacent from non-adjacent steps well:
  - `corr(hazard_at_agent, d_min)` = -0.82 / -0.75 / -0.75;
  - mean 0.94 adjacent vs 0.82-0.84 far;
  - >= 0.99 on 68-80% of adjacent steps vs 15-23% of far steps.
- **After the EMA it is gone.** `harm_obs_a = EMA_{alpha=0.05}(hazard_at_agent)` (`:3037`). Mean `harm_obs_a[0]` is 0.876 vs 0.836 (seed 11), **0.869 vs 0.868** (seed 12), and 0.875 vs 0.849 (seed 13), adjacent vs far.
- **The per-step change at onset is 0.24 / 0.37 / 0.26 pool-SDs** above the pool mean change (raw input). In `s_t` (encoder A) it is 0.13 / 0.17 / 0.09 SDs. No gate can detect a 0.1-0.4 SD single-step shift at a useful false-alarm rate.
- **Two env properties compound.**
  1. **The hazard field is saturated.** `sum 1/(1 + 0.5 d)` over 3 hazards on a 10x10 grid (`:4746-4750`) is >= ~0.47 everywhere and clips to 1.0 near any hazard. So "hazard proximity" is a small modulation on a high floor. It is also why `hazard_approach` fires on almost every step.
  2. **A time constant of ~20 steps** against untrained-agent lives of 11-39 steps and approaches lasting a few steps. The ~20-step constant is deliberate: the SD-011 homeostatic accumulator, fixed for autocorrelation, `:3025-3032`.
- **A post-hoc check (not pre-registered)** ran the same four gates on the faster `harm_exposure` channel (`harm_obs[-1]`, which also enters the encoder via `harm_history`). It was not onset-selective either: best pooled d' +0.04 (iii) and -0.004 (ii). In this config proximity harm accrues on nearly every step, so that channel is tonic too.

So the CeA gate's problem is not only its threshold. **The input it was wired to (`z_harm_a`, the SD-011 affective/C-fibre accumulator stream) is by construction a slow homeostatic integral. In this environment configuration it carries almost no per-approach onset information.** Recalibrating the gate moves the saturation point and nothing else. This matches the biology the module cites: the fast amygdala route reads coarse *fast* thalamic input, not a slow affective integral. That is inference, not measured here.

### R3. Encoder regime B at the native weight (D1)

The encoder was trained online (batch 1, Adam 1e-3) at `0.1 x MSE(harm_accum_pred, harm_exposure)`, the 935a native target.
- **1 pass:** `s` on EVAL rises from 0.14-0.16 at init to **1.5-1.8** (range 1.09-2.06). It plateaus by 250 steps. Loss 0.0057 -> 3e-5.
- **3 passes (6000 steps):** 6.3-8.8 and still climbing, toward the trace's 12-17 (offline, batch 32, weight 1, target `accumulated_harm`).

The fixed gate is therefore not merely "always firing". **Its operating point drifts with training time**, 10x over 6000 steps. Any absolute threshold on this latent is unstable by construction. As pre-noted, weight 0.1 vs 1 is nearly irrelevant under Adam; the difference from the trace comes from the target, the batch and the step count.

### R4. Salience arithmetic: no variant can reach the switch threshold, and all push toward `external_task` (D0)

A gate variant changes only **when** CeA fires. It does not change what a fire emits.
- **Fire emission.** On fire, `mode_prior = clip(over x gain, +/-0.8)` (`cea.py:348-354`). `fast_prime = clip((over/0.8) x min(0.6, 0.8), +/-0.8)` (`cea.py:356-361`). Here `over = low_freq - thr` (`:346`), and `cap = mode_prior_log_odds_max = 0.8` (`:336`, `config.py:7146`).
- **Largest possible salience contribution:** `salience_weights["cea_fast_prime"] = 0.5` (`agent.py:2577`) x 0.8 = **0.4**.
- **Switch threshold:** `switch_threshold = 1.0` (`salience_coordinator.py:311`), x `(1 + stability_scaling x pcc_stability) >= 1` (`:668-670`).
- A relative gate would need `over` redefined, e.g. `z - k`. It is still clipped at 0.8. **So under every variant, CeA alone contributes <= 0.4 < 1.0 and cannot trip MECH-259** (`:687-691`). It could co-trigger only with >= 0.6 salience from another source (dACC) on the same tick.
- **Direction:** `affinity_weights["cea_mode_prior"] = {"external_task": 1.0}` (`agent.py:2574-2576`). Every variant pushes toward `external_task`, the default and post-reset mode (trace section 2a).

### Domain reached

- **D1:** gate readouts on recorded native inputs, plus the input-information check.
- **D0:** salience arithmetic.
- **No D2.** No gate was wired into a native consumer, and none should be until R2 is resolved.

### What a ree_core build would need (routed to the SD-035 / MECH-046 owner; NOT built)

The probe says the build is **not** "a scale-aware gate on `z_harm_a`". A build needs, in order:

1. **An onset-bearing input for the CeA fast route.** This is the missing prerequisite, and it is `complex (probe-gated)`. The candidates, none tested here, are:
   - (a) the sensory-discriminative stream `z_harm_s` / `harm_obs` (the 5x5 local hazard view, SD-010);
   - (b) a pre-EMA hazard-proximity scalar;
   - (c) a fast-alpha second EMA of `hazard_at_agent`.

   Behind default-OFF knobs, e.g. `cea_fast_route_input = {"z_harm_a" (default), "z_harm_s", "harm_prox_fast"}`. The **next probe** is this same harness with (a)-(c) recorded, cheap and offline once recorded. It must also be run in a config where the hazard field is not saturated (for example, fewer hazards or a larger `hazard_field_decay`), so the probe can tell env saturation apart from stream choice.
2. **Then a relative gate on that input**, `complicated (buildable)`. Only once an input passes (1). For example `cea_gate_mode = {"absolute" (default), "rate", "zscore"}` with `cea_gate_k` and `cea_gate_ema_beta`, default OFF. Rate-of-change is the natural form for an onset detector.
3. **The emission ceiling and direction** (R4). This is a design decision for the MECH-039/046 claim holder, not a calibration: `salience_weights["cea_fast_prime"]` and the `external_task` affinity at `agent.py:2573-2577`.

## Premises re-measured

- **"MECH-039 two-part veto readout is on main" (brief): false at `origin/main aa14769`.** Commits `ef83289` / `1b8422d` ("[WIP, parked: suite pending, not rebased]") are on `origin/bt0925-mech039` only (`git merge-base --is-ancestor` false for both). This probe did not need it.
- **"harm_accum training drives low_freq to 12-17" (trace, weight 1, offline):** at native weight 0.1 with the 935a target, online, the value is 1.5-1.8 after 2000 steps and 6.3-8.8 after 6000. Same direction; the magnitude depends on training length.
- **"A relative/onset gate (baseline-subtracted or derivative of z_harm_a)" as the Q2 fix (trace section 3, GFLAG-0554 routing): refuted for this input and config.** The information is not in `z_harm_a` (R2).
- **Trace numbers at init (low_freq 0.14-0.20, never fires): reproduced**, 0.11-0.17 on scored EVAL steps.

## Uncertainty

- **Untrained agent, short lives** (28-100 episodes per 1100 steps). A trained agent with longer, deliberate approaches from farther away could give the slow EMA more room. Hazard adjacency from distance >= 2 after 3 non-adjacent steps is a demanding onset definition. The input-level null (R2) still holds for this environment configuration.
- **Only one environment configuration** (3 hazards, 10x10, decay 0.5), the one EXP-0787 and the trace used. Field saturation is config-dependent.
- **Regime B is offline on the recorded trajectory**, not in-loop with an acting agent. This is justified because the gate has no behavioural consumer (trace section 1c), but it is not identical.
- **N = 5-step window.** A longer window would favour slow gates. With ~0.1-0.4 SD per-step onset shifts, I would not expect it to change the verdict. Not tested.
