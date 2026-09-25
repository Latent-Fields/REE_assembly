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

## RESULTS (written 2026-09-25T20:35Z)

**Runs.** 3 seeds (11/12/13) x 2 configs (baseline, nonsat), EVAL only, 1100 steps each (100 burn-in), `probes/ceacal2/ceacal2_record.py`. Mac wall 89-202s/recording (6 recordings, ~14.3 min total). No shrink needed.
- **Analysis:** offline, `ceacal2_analyze.py`, pooled per config in `ceacal2_pool.py`. Raw per-seed JSON in `results/ana2_<config>_<seed>.json`, pooled in `results/pooled2_<config>.json`.
- **Sample.** Baseline: 106 onsets pooled (34/37/35), 1645 pool steps (560/525/560) -- matches probe1's baseline counts exactly (same seeds, same config, independent re-recording -- a reproducibility check in itself). Nonsat: 81 onsets pooled (20/28/33), 1800 pool steps (631/665/504).
- **Instrument check passed** for both encoders: recomputed `s_t` (z_harm_a and z_harm_s) matches the agent's own `_cea_last_output.low_freq_magnitude` / `mean|agent._current_latent.z_harm|` to <= 6e-8 on all 6 x 1100 steps.
- **Config check.** Scored-region `hazard_at_agent` mean/min: baseline 0.847-0.870 / 0.467-0.548 (matches the field-check floor of ~0.50 and probe1's prior reading); nonsat 0.112-0.140 / 0.037-0.040 -- the chosen config is measured non-saturated on the actual trajectories, not just at `reset()`.

### R1. Pooled readout, N=5 primary window, pre-registered thresholds, regime A (untrained)

d' = z(H) - z(Fw), log-linear corrected (chance = 0). Bold = best stream per config per variant family; best cell overall in **iii_rate**.

| config | stream | i_fixed | ii_zscore | **iii_rate** | iv_ratio |
|---|---|---|---|---|---|
| baseline | z_harm_a (current CeA input) | H 0/106 d'=0.31 (never fires) | H 0/106 d'=-0.82 | H 6/106 (5.7%) F 1.5% **d'=-0.18** | H 7/106 d'=-0.88 |
| baseline | z_harm_s (candidate a) | 0.31 (never fires) | H 8/106 d'=0.10 | H 25/106 (23.6%) F 1.0% **d'=0.83** | H 8/106 d'=-0.51 |
| baseline | preema_hz (candidate b) | H 105/106 d'=-3.80 (always fires) | H 7/106 d'=0.58 | H 35/106 (33.0%) F 1.3% **d'=1.00** | H 3/106 d'=0.15 |
| baseline | fastema alpha=0.3 (candidate c) | H 105/106 d'=-3.80 (always) | H 3/106 d'=0.30 | H 24/106 (22.6%) F 1.0% **d'=0.82** | H 7/106 d'=-0.95 |
| baseline | raw_a (probe1 control v) | H 106/106 d'=-3.40 (always) | H 0/106 d'=0.31 | H 5/106 (4.7%) **d'=0.43** | H 10/106 d'=-1.16 |
| nonsat | z_harm_a | H 0/81 d'=0.43 (never fires) | H 3/81 d'=-0.29 | H 8/81 (9.9%) **d'=-0.24** | H 5/81 d'=-0.80 |
| nonsat | z_harm_s | 0.43 (never fires) | H 5/81 d'=-0.22 | H 11/81 (13.6%) **d'=0.29** | H 6/81 d'=-0.27 |
| nonsat | **preema_hz** | H 2/81 d'=1.06 (2.5% -- correction-floor artefact, not selective) | H 18/81 d'=0.15 | H 23/81 (28.4%) F 1.7% **d'=0.73** | H 37/81 (45.7%) F 22.7% d'=-0.90 |
| nonsat | fastema alpha=0.3 | H 1/81 (silent) | H 14/81 d'=-0.10 | H 22/81 (27.2%) **d'=0.47** | H 34/81 (42.0%) F 23.7% d'=-1.05 |
| nonsat | raw_a | 0.43 (never fires) | H 6/81 d'=-0.15 | H 16/81 (19.8%) **d'=0.10** | H 30/81 (37.0%) F 22.8% d'=-1.13 |

**N=10 secondary window** (same thresholds): the ranking is unchanged and no stream crosses H>=0.5 at N=10 either. `iii_rate` pooled d': baseline z_harm_a -0.36, z_harm_s 0.62, preema_hz 0.90, fastema 0.80, raw_a 0.36; nonsat z_harm_a -0.61, z_harm_s 0.16, preema_hz 0.82, fastema 0.50, raw_a 0.09. `preema_hz` stays best in both configs at both windows.

**Post-hoc threshold sweep** (40 quantiles/seed, labelled exploratory): `preema_hz` `iii_rate` reaches per-seed d' 1.15-1.42 in baseline and 0.37-1.44 in nonsat (seed 13's nonsat sweep is 0.37 -- inconsistent, a sweep-over-noise symptom like probe1's). This is a ceiling on what threshold-only re-tuning could buy, not evidence the pre-registered operating point works.

### R2. Decision (pre-registered rule)

**ENV SATURATION: REFUTED for z_harm_a.** De-saturating the field does not restore `z_harm_a`'s onset-selectivity. Every relative gate on `z_harm_a` is negative in the nonsat config (ii -0.29, iii -0.24, iv -0.80) -- **below its own "always-silent" correction floor of +0.43** -- vs baseline's already-poor -0.18 to -0.88. z_harm_a is not merely unhelped by de-saturation, its relative gates get *worse*: with only one sparse hazard, the agent's incidental movement through empty terrain produces more spurious rate-of-change/z-score fires per onset than the smoother multi-hazard baseline field did, at no compensating gain in real hits (H stays 6-10%).

**STREAM CHOICE: the dominant factor, but no stream reaches the pre-registered qualifying bar (d'>=1.0 AND H>=0.5) in either config.** `preema_hz` -- **candidate (b), the raw un-encoded, un-smoothed `hazard_at_agent` scalar** -- is the best stream in both configs under `iii_rate` (baseline d'=1.00 H=33%, nonsat d'=0.73 H=28%), clearly separated from `z_harm_a` in both (delta ~1.0-1.2 d' at baseline, ~1.0 at nonsat). `z_harm_s` (candidate a) and `fastema` (candidate c) are both intermediate: better than `z_harm_a`, worse than raw `preema_hz`, in both configs. So the ordering **less-processed beats more-processed, at both saturation levels**: `preema_hz` > `{z_harm_s, fastema}` > `raw_a` > `z_harm_a` (baseline); `preema_hz` > `fastema` > `{z_harm_s, raw_a}` > `z_harm_a` (nonsat). No decision-rule "both" case applies either -- z_harm_a does not improve enough in nonsat for that branch.

**Verdict: neither config alone explains the loss; it is chiefly a STREAM-CHOICE problem, and among the tested candidates the LEAST-processed stream (raw hazard-at-agent proximity) is consistently best, better than the two more elaborate candidates the first probe proposed (z_harm_s, a fast EMA) -- but even that best stream does not reach the pre-registered working bar (H stays <=33% at either window).** The practical ceiling for `iii_rate` on `preema_hz` is real (best of all 20 cells tested) but modest; a build on this input alone would still miss roughly 2 of 3 onsets at the tested false-alarm budget.

**New prerequisite this reprobe surfaces, not in R2's original candidate list.** `preema_hz` (the raw `hazard_at_agent` scalar, `causal_grid_world.py:3035`) is **not currently exposed to the agent at all** -- `harm_obs` normalises it into a per-step-relative 5x5 view (`:4129-4132`) and `harm_obs_a` EMAs it at alpha=0.05 (`:3036-3037`); neither is the raw scalar. A build sourcing CeA from this candidate needs a NEW `obs_dict` field (e.g. `hazard_proximity_raw`), not a rewire of an existing one.

### R3. Salience arithmetic reconfirmed (D0), independent of stream/gate choice

`cea.py:336` (`cap=mode_prior_log_odds_max=0.8`), `cea.py:348-361` (`mode_prior`/`fast_prime` clip), `agent.py:2573-2577` (`salience_weights["cea_fast_prime"]=0.5`, `affinity_weights["cea_mode_prior"]={"external_task":1.0}`), `salience_coordinator.py:311/664-694` (`switch_threshold=1.0`) are all unchanged at `2ea0e3c8` (same lines probe1 cited at `aa14769`). The R4 conclusion from probe1 is stream/gate-independent by construction (it bounds `over`'s contribution after the clip, not before) and is reconfirmed here by code-read: **CeA alone still caps at 0.4 < 1.0 regardless of which input or gate feeds it**, so even a fully onset-selective `preema_hz`-style gate could not alone trip MECH-259's switch; it would still need >=0.6 co-triggering salience from another source (dACC) on the same tick.

### Domain reached

- **D1:** gate readouts on newly-recorded native trajectories (both configs), input-information/field-floor checks.
- **D0:** salience arithmetic (reconfirmed, unchanged).
- **No D2.** No gate or stream was wired into a native consumer.

### What a ree_core build would need (routed to the SD-035/MECH-046 owner; NOT built)

This reprobe sharpens GFLAG-0556's routing rather than reversing it:

1. **Source CeA's fast route from a new raw hazard-proximity `obs_dict` field** (`hazard_at_agent`, pre-EMA, pre-normalisation -- currently computed at `causal_grid_world.py:3035` but not exposed), not from `z_harm_s` or a fast EMA -- both measured worse than the raw scalar in both saturation regimes. Default-OFF knob, e.g. `cea_fast_route_input = {"z_harm_a"(default), "hazard_proximity_raw"}`.
2. **A relative gate on that input**, rate-of-change form (`iii_rate`'s formula), `complicated (buildable)` once (1) exists.
3. **Even (1)+(2) is not proven sufficient at the pre-registered bar** -- best measured H is 33% (baseline) / 28% (nonsat) at N=5, 39%/38% at N=10. A build attempt should expect to also need either a wider integration window, a second onset feature (e.g. combine with `iv_ratio`'s slow-baseline signal, which had the highest H in nonsat, 42-46%, but the worst FA), or accept a genuinely probabilistic (not deterministic-threshold) fast-route trigger. This is `complex (probe-gated)`: the next informative probe is a 2D gate (rate-of-change AND ratio jointly) or an FA-budget-matched ROC comparison across streams, offline on data already in hand.
4. **Env de-saturation is NOT a prerequisite.** Do not gate the build on choosing a non-saturated env config -- `z_harm_a` gained nothing from it, and `preema_hz`/`fastema` were if anything *slightly worse* in nonsat (H comparable, d' lower) than baseline. The saturated EXP-0787 config is not the obstacle.
5. **The emission ceiling and direction (R3)** remain a design decision for the MECH-039/046 claim holder, unchanged from probe1.

## Governance

I raised **GFLAG-0557** (stale_note, MECH-046 + MECH-039), refining GFLAG-0556. No other registry edits.

## Premises re-measured

- **"The env/CeA/encoder code probe1 read is current" (implicit in reusing probe1's file:line citations): confirmed.** `git diff --stat aa14769 2ea0e3c8` on the 4 files this probe depends on shows only `config.py` (+71 lines, additive MECH-039 fields) changed; `causal_grid_world.py`, `cea.py`, `latent/stack.py` are byte-identical to probe1's sha.
- **"z_harm_s / a fast EMA of hazard_at_agent are the strongest untested candidates" (probe1's R2 "What a build would need" list, its framing going in): partially refuted.** Both are real improvements over `z_harm_a`, but a candidate NOT on that list -- the completely raw, un-encoded `hazard_at_agent` scalar -- beat both in every (config, window) cell tested.
- **"Env saturation is a plausible confound worth testing" (probe1's own open question, and this brief's premise): tested and refuted for z_harm_a.** Measured, not assumed: the chosen nonsat config's on-trajectory `hazard_at_agent` mean is 0.11-0.14 (vs baseline 0.85-0.87), a genuine ~7x reduction, and z_harm_a's relative-gate d' still does not improve.

## Uncertainty

- **Regime A (untrained) only.** Probe1's P3 finding (scale-invariance of relative gates across training) is being extended here to a second env config on inference, not re-measured directly in this probe -- a direct check (retrain regime B in the nonsat config) was cut for budget. Low risk: P3's own mechanism (relative gates ignore encoder scale) does not depend on env config.
- **One nonsat config tested** (nh=1, decay=2.0), chosen for the widest measured floor/ceiling separation among 4 candidates. A different point in that space (e.g. nh=2, decay=1.0) was not tested; the qualitative pattern (z_harm_a does not improve, preema_hz stays best) is unlikely to reverse given the monotonic trend across the 4 field-check candidates, but this is inference, not measurement.
- **`iv_ratio`'s nonsat behaviour is notable and unexplained here**: it has the highest raw H of any variant in nonsat (42-46%) but an FA rate an order of magnitude worse (22-24% vs <3% for other variants), driving d' very negative. This looks like the slow baseline `b` (beta=0.01) failing to track the sparser, more volatile nonsat field rather than a genuine onset signal; not diagnosed further here (out of scope, see build item 3 above).
- **Untrained agent, short/variable lives** (18-100 episodes per 1100 steps, more variable in nonsat where survival depends heavily on the single hazard's random walk). Same caveat probe1 carried forward.
