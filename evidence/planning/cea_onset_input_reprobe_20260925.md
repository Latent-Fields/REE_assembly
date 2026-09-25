# CeA onset-input re-probe: env saturation vs stream choice (2026-09-25)

- **Session:** `bt0925-ceacal2` (breakthrough integration pass `orchestrate-20260924-breakthrough`), chip_ref `chip-20260925-cea-onset-input-reprobe`.
- **Scope:** probe only. No ree_core edits, no queue entries, no claims.yaml edits, no chips.
- **Code under test:** ree-v3 `origin/main` @ **`2ea0e3c863db61af9ad39195457d75cbff95b2a5`** (private detached worktree). Every `file:line` is against that sha. `git diff --stat aa14769 2ea0e3c8 -- ree_core/environment/causal_grid_world.py ree_core/amygdala/cea.py ree_core/latent/stack.py ree_core/utils/config.py` shows only `config.py` changed (+71 lines, additive MECH-039 veto-readout fields) since the first probe's sha; the env/CeA/encoder code this probe reads is unchanged.
- **Context:** `cea_gate_calibration_probe_20260925.md` (origin/master `dfe73c29b7d`) R2 -- the onset info is destroyed upstream, the hazard field saturates and `z_harm_a` is an EMA of it; section "What a ree_core build would need" names candidates (a) `z_harm_s`, (b) a pre-EMA hazard-proximity scalar, (c) a fast-alpha second EMA of `hazard_at_agent`, and calls for this exact harness re-run, plus a non-saturated config. GFLAG-0556 (raised by that probe). `mode_switch_cea_mechanism_trace_20260925.md` Q2.

## PRE-REGISTRATION (written and committed before any onset-probe readout was computed)

Written 2026-09-25T20:09Z.

### Question

Is the CeA fast route's missing onset information an **env-saturation** artefact (a non-saturated hazard-field config restores onset selectivity in `z_harm_a` itself), a **stream-choice** artefact (only a different input stream carries it, in both configs), or **both**? And, among the candidates, which (config, stream, gate) combination is closest to a working operating point, with its evidence domain?

### Env-config selection (measured, not assumed)

`ceacal2_field_check.py` (this probe's dir) instantiated `CausalGridWorldV2(size=10, num_resources=3, harm_history_len=10)` with 4 candidate `(num_hazards, hazard_field_decay)` pairs, 5 seeds each (21-25), and read `hazard_field` (`causal_grid_world.py:4741-4750`, `sum over hazards of 1/(1+dist*decay)`) directly after `reset()` -- no agent, no stepping. Results (`field_check.json`, mean over 5 seeds):

| config | floor | ceiling | frac cells >= 0.15 | frac cells >= 0.5 | mean at hazard-adjacent (d<=1) | mean far (d>=2) | adj/far ratio |
|---|---|---|---|---|---|---|---|
| baseline nh=3, decay=0.5 (EXP-0787) | 0.497 | 1.681 | 1.000 | 0.988 | 1.337 | 0.821 | 1.6x |
| nh=3, decay=2.0 | 0.143 | 1.239 | 0.972 | 0.120 | 0.678 | 0.271 | 2.5x |
| nh=1, decay=0.5 | 0.147 | 1.000 | 0.978 | 0.126 | 0.733 | 0.282 | 2.6x |
| **nh=1, decay=2.0** | **0.041** | **1.000** | **0.126** | **0.010** | **0.467** | **0.093** | **5.0x** |

**Chosen non-saturated config: `num_hazards=1, hazard_field_decay=2.0`.** It has by far the widest adjacent/far separation (5.0x vs baseline's 1.6x), and unlike the other two alternatives it also breaks the *approach-threshold* saturation the first probe's Amendment 1 flagged (`proximity_approach_threshold=0.15`, `causal_grid_world.py:346`): only 12.6% of cells reach 0.15 at all, vs 100% at baseline and ~97% for the other two candidates. This is the config where "hazard proximity" is a genuinely rare, spatially localised state rather than a near-constant floor. Both env configs otherwise match EXP-0787: `size=10, num_resources=3, harm_history_len=10`.

### Design

- **2 x K.** Env config in {**baseline** nh=3/decay=0.5, **nonsat** nh=1/decay=2.0} x input stream in {**z_harm_a** (baseline stream, `AffectiveHarmEncoder` on `harm_obs_a`+`harm_history`), **z_harm_s** (candidate a, `HarmEncoder` on `harm_obs` = `hazard_field_view[25]+resource_field_view[25]+harm_exposure[1]`, `causal_grid_world.py:4129-4132`, `latent/stack.py:119-172`), **preema_hz** (candidate b, raw `hazard_at_agent = clip(hazard_field[agent],0,1)`, `causal_grid_world.py:3035`, zero smoothing), **fastema** (candidate c, post-hoc EMA of `hazard_at_agent` at alpha=0.3, the same recurrence the env itself runs for `_safety_proximity_ema` at its default alpha=0.05, `causal_grid_world.py:3049-3052`/`:1615`, init 0.0 -- alpha=0.3 implies a ~3-step time constant against the deployed 0.05's ~20-step constant, and N_WIN=5 is the discriminating comparison), **raw_a** (probe1's control v: `harm_obs_a[0]`, the post-default-EMA scalar, kept for cross-probe continuity)}.
- **Regime: A (untrained) only, this round.** Probe1 (`cea_gate_calibration_probe_20260925.md` P3/R2) found the relative gates scale-invariant across encoder training and the missing information upstream of the encoder -- an input-level property. Retraining regime B a second time would not bear on the env-saturation-vs-stream-choice question and is dropped to fit budget; this is a deliberate scope reduction, stated per the Stop rules in COMMON.md point 10.
- **Agent/env.** `world_dim=self_dim=32` (deployed). Untrained agent, `StepHarness(train_mode=False)`. External hazard injected at `t % 30 == 15` via `env._inject_external_hazard()` (unchanged code, works with `num_hazards=1`: moves the existing hazard adjacent to the agent). Seeds 11/12/13 (env seed = seed+1000, EVAL convention). `torch.set_num_threads(2)`. EVAL-only recording, 1100 steps, 100-step burn-in (unscored).
- **Instrument checks.** Both encoders' weights are the agent's own (`state_dict()` saved at record time); `z_harm_a`/`z_harm_s` recomputed offline must match the agent's own per-step `_cea_last_output.low_freq_magnitude` / `mean|agent._current_latent.z_harm|` to float precision -- reported per (config, seed).
- **Ground truth, onset, pool, window.** Identical to probe1 Amendment 1: hazard step = nearest-hazard Manhattan distance `d_min<=1` OR `transition_type=="env_caused_hazard"`; onset = a hazard step whose previous 3 steps (same episode) all have `d_min>=2`; **primary window N=5**; **secondary window N=10** (brief requirement); FA pool = non-onset-window non-hazard steps outside the first 3 steps of each episode.
- **Gates.** The same four causal, online variants as probe1: (i) fixed `s_t>0.5`; (ii) running z-score (beta 0.05) `>2.0`; (iii) rate-of-change (beta 0.05) `>2.0 sd`; (iv) ratio to a slow baseline (beta 0.01) `>1.25`. Same pre-registered thresholds, same 20-step warmup, same causal ordering (stats updated after the gate is evaluated at t).
- **Readouts.** Per (config, stream, variant): hit rate H (>=1 fire in the onset window), per-step FA rate F on the pool, window-matched FA `Fw=1-(1-F)^(N+1)`, `d'=z(H)-z(Fw)` with log-linear correction (chance = 0), both at N=5 and N=10, plus a post-hoc best-threshold sweep (40 quantiles) as in probe1, labelled post hoc.
- **Salience arithmetic (R4 redo).** `cea.py:336` (`cap=mode_prior_log_odds_max`), `cea.py:348-361` (`mode_prior`/`fast_prime` clip), `agent.py:2573-2577` (`salience_weights["cea_fast_prime"]=0.5`, `affinity_weights["cea_mode_prior"]={"external_task":1.0}`), `salience_coordinator.py:311/664-694` (`switch_threshold=1.0`) are confirmed **unchanged** at this sha (same line numbers as probe1 cited). This arithmetic is independent of which input stream or gate variant feeds `over = low_freq - thr`: the clip at `mode_prior_log_odds_max=0.8` and the weight 0.5 cap CeA's own contribution at 0.4 regardless of what makes `low_freq` cross `thr`. So the R4 conclusion (CeA alone cannot reach `switch_threshold=1.0`; every fire pushes `external_task`) is reconfirmed by code-read (D0) for whichever (stream, gate) this probe finds best, not re-derived per variant.

### Pre-registered decision rule

- **Env saturation** is confirmed if, for **z_harm_a** specifically, some relative gate reaches pooled d' >= 1.0 with H >= 0.5 in the **nonsat** config but not in **baseline**.
- **Stream choice** is confirmed if a *different* stream (z_harm_s / preema_hz / fastema) reaches pooled d' >= 1.0 with H >= 0.5 in **both** configs while z_harm_a does not reach it in either.
- **Both** if z_harm_a improves substantially in nonsat (>= 0.5 d' gain) AND a different stream still outperforms it there.
- **Neither / open** if no stream in either config reaches d' >= 1.0 at H >= 0.5 -- report the best available (config, stream, gate) by the same highest-minimum-over-what-was-tested rule probe1 used, and say so plainly.
- The best variant, if any qualifies, is named with its (config, stream, gate, N-window) and the minimal default-OFF knob set for a build, routed to the SD-035/MECH-046 owner. No build.

### Budget and shrink rule

~90 min Mac wall (per brief). Field-check (no-agent, no-lock-required-strictly but run under lock per rule) took under a minute once the lock freed. 6 EVAL recordings (3 seeds x 2 configs) budgeted at up to ~370s each (probe1's per-recording range) = worst case ~37 min; analysis is offline and cheap (~18s CPU total per probe1's Deviation 2). If a recording seed exceeds 10 min, steps shrink to 600 for the remaining seeds of that config and this is stated in RESULTS.

Mac CPU lock (`mac_probe.lock`) held for each record process individually, released between them.
