# Residue consumer reach at world_dim=32: does the GFLAG-0441 integrate() fix reach its native consumer?

- Session: bt0924-residue-reach (Worker B, breakthrough integration pass `orchestrate-20260924-breakthrough`)
- chip_ref: chip-20260924-residue-consumer-reach
- Written: 2026-09-24T17:43Z (probes 17:15Z-18:45Z local Mac CPU, 2 threads)
- Code under test: ree-v3 origin/main `00210b5` + `.scratch/breakthrough-20260924/residue_gflag0441_full.patch`
  (the GFLAG-0441 fix, adds `ResidueConfig.use_dim_scaled_integrate_sampling`), applied with `git apply --3way` in a
  private detached worktree. The fix was NOT on origin at probe time; a separate worker owns landing it.
  All file:line citations below are against that worktree (`00210b5` + patch).
- Probes: `evidence/planning/probes/residue/residue_reach_probe.py`, tabulated by `probes/residue/summarize.py`;
  raw per-cell outputs in `probes/residue/results/*.json`.
- Evidence domain reached: **D2** for the fix's effect on the two native consumers. The effect is **non-specific**
  (matched exactly by a permuted-target control) and **points toward more harm**. Closed-loop behaviour (D3) was
  not run, per the brief's stop rule.

## Verdict in one paragraph

With the fix ON, integrate() does distil the harm field, as the D1 contract C10 says it should. The native
consumers do not read it there. Both consumers score candidate E2 rollouts, and those rollouts spend almost their
whole 30-step horizon far outside the ~1-bandwidth shell integrate() now trains on: the median query is 12-18
kernel widths from the nearest harm location at the deployed bandwidth 1.0, and 80-120 at 0.15. The
neural_field's ReLU extrapolation there is large and anti-correlated with the RBF core (r = -0.13 to -0.42). The
consumer DOES respond strongly: at the native per-cycle budget, the CEM elite set is replaced in 100% of iterations
and 0-15% of E3 argmins flip. But the response is reproduced to two decimals by the permuted-target control (SCR)
in every one of seven cells, and it cuts or reverses the CEM stage's existing residue avoidance (retained
avoidance -0.97 to +0.35 of baseline). So the fix is D1, and its D2 reach is non-specific and in the wrong
direction. The alternative (sampling from the z_world points the consumer actually queried) does reach the
consumer faithfully (r = 0.997-1.000 with the RBF core at 300 steps). But it only reproduces a ~1.1x rescaling of the RBF
core, which leaves the CEM elite set and its residue avoidance essentially unchanged. That confirms GFLAG-0442's
arithmetic empirically: the current objective carries no information the consumer lacks. **Neither variant gives
the consumer new harm-specific information.** A larger upstream finding came out of the per-step profile (below):
the E2 world rollout is geometrically divergent (z_world norm x1.2 per step). Residue can only discriminate
candidates on the first ~2 rollout steps, whatever integrate() does.

## Premises re-measured (and one corrected)

| Premise (source) | Re-measured | Status |
|---|---|---|
| GFLAG-0441 fix not on origin (brief) | `git log origin/main` at 17:12Z: HEAD `00210b5`, no `use_dim_scaled_integrate_sampling` | holds |
| Fix gives mean target/peak ~0.61 at world_dim=32 (patch comment) | sample-shell radius measured: ON p50 0.99 bw, OFF p50 5.61 bw (`_sample_shell_*` in every results JSON) | holds (D1) |
| "Sampling from visited z_world needs new plumbing, no visited pool exists" (patch field comment) | True for a VISITED pool. But a CONSUMER-QUERIED pool is trivially available: every E3 query goes through `ResidueField.evaluate_trajectory` (field.py:650), so recording its (detached) input is a one-line hook. The probe's ALT arm does exactly this. | **partly stale**: the option is cheap, but see Q4. It does not help |
| Integration only happens in sleep WRITEBACK, 10 steps (chip, config) | Native forced cycle fired in all 8 cells: `mech018_residue_integration_fired=1, trains=1, steps=10`, rbf delta exactly 0.0 | holds |
| No production driver turns the flags on (orchestrator) | `use_offline_integration_gradient_step` / `use_sleep_residue_integration`: only `experiments/v3_exq_1072_*.py` (already ran 2026-09-22); `harm_field_bandwidth`: 0 scripts; new flag: 0 scripts; origin queue (4 items): none | holds |

## Q1: who reads the residue (worktree `00210b5`+patch)

`evaluate()` = `rbf + 0.1*neural` (field.py:648); `evaluate_trajectory()` = sum over horizon of the same
(field.py:662). Only these two reads see `neural_field`; everything else reads RBF buffers only.

| Consumer | Call site | Component | Query points | Trained? |
|---|---|---|---|---|
| E3 trajectory score, residue term | `e3_selector.py:1394` (`compute_residue_cost`), weighted `rho_residue=0.5` at `:1700`; argmin at `:2915` (committed; committed_frac 1.00 in every cell) | rbf + 0.1*neural | 32 candidates x 31 E2-rollout z_world states per select | E3 selection is native |
| Hippocampal CEM elite selection | `hippocampal/module.py:1775` (`_score_trajectory`), fallback `:1868`; elite = 6 lowest of 32, 3 iterations | rbf + 0.1*neural | same kind of E2-rollout states (CEM samples) | native ranking |
| Hippocampal terrain prior | `hippocampal/module.py:581` -> `terrain_prior` MLP | rbf + 0.1*neural | the CURRENT z_world only | **terrain_prior has no loss anywhere in ree_core** (grep: only its constructor and forward), so this read feeds a random projection. It is not a meaningful consumer |
| Structured curiosity (MECH-314a) | `policy/structured_curiosity.py:860` | rbf centres only | candidate summaries | neural_field unread |
| Valence / priority / MECH-295 | `evaluate_valence` (field.py:969, rbf `valence_vecs`), `get_valence_priority`, `mech295_liking_bridge.py:382` | rbf only | various | neural_field unread |
| Closure discharge | `discharge_domain` (field.py:1064), via `ClosureOperator(residue=...)` `agent.py:2460` | rbf weights only | closure location | neural_field unread |

Producers of `_harm_history` (the pool integrate() samples around): `agent.py:11369` (`update_residue`, every
harm tick) and `e3_selector.py:4695` (`post_action_update`, committed + harm). Both write per harm tick, which is
why harm_history is about 2x the harm-tick count in the results. `agent.offline_integration()` (`agent.py:12980`,
which calls `integrate()` at `:13001`) is called by no experiment. The only integrate() path is sleep WRITEBACK
(`sleep/phase_manager.py:695`).

**Flags ON in production:** none. Every current driver runs the consumer with an untrained neural head (the ~0.064
pedestal at 0.1 scale). That pedestal barely moves the consumer: NONE vs OFF_10 gives 0-1 E3 flips and CEM Jaccard
0.58-0.995.

## Q2: where the consumer queries vs where integrate() trains

Distances from consumer query points to the nearest location in integrate()'s own pool (`_harm_history[-100:]`),
in harm-kernel bandwidth units. W1 = 400 waking steps after a 600-step E1+E2 warmup; 3 seeds x 2 bandwidths.

| Cell | current-state (terrain) p50 | E3 / CEM rollout p50 | p95 | E3 queries <=1.25 bw | ON shell | OFF shell |
|---|---|---|---|---|---|---|
| bw 1.0 (deployed), s42/43/44 | 0.03 / 0.02 / 0.01 | 12.0 / 18.2 / 14.3 | 144 / 271 / 189 | 13% / 13% / 10% | 0.99 | 5.61 |
| bw 0.15 (58ac5de knob), s42/43/44 | 0.22 / 0.12 / 0.07 | 81 / 121 / 96 | 962 / 1806 / 1261 | 3% / 3% / 3% | 0.99 | 5.61 |

Per-step profile (`results/prof_w600_bwNone_s43.json`, `_e3_by_step`): the median distance to harm and the z_world
norm at rollout step t are

| t | 0 | 1 | 2 | 3 | 5 | 10 | 20 | 30 |
|---|---|---|---|---|---|---|---|---|
| dist (bw) | 0.02 | 0.39 | 0.78 | 1.21 | 2.19 | 6.66 | 48.7 | 327 |
| z_world norm | 0.49 | 0.68 | 1.02 | 1.41 | 2.37 | 6.80 | 48.8 | 327 |

(The visited-state norm p50 is 0.49.) The p95 equals the p50 at each step to three significant figures, so all 32
candidates are carried outward along the same growing mode. So: **the ON training shell (~1 bw) covers rollout
steps ~1-3 only. Steps 0-2 are the only steps where the RBF core itself discriminates. Steps ~4-30 are pure
neural_field extrapolation.** The fix is a D1 fix with no D2 reach where it matters. The answer to "sqrt(world_dim)
vs sample-from-queried" is decided by evidence, not preference: queried-point sampling is the only variant that
covers the consumer's support (see Q4).

## Q3: consumer response (matched counterfactual on the SAME candidate sets)

Design: fork the pre-sleep ResidueField. Train neural_field per arm with matched RNG and the same Adam lr 0.01 and
batch. Then, over a 200-step post-cycle waking phase on the live agent, re-score every recorded E3 select and every
CEM iteration under each arm's field. Arms: NONE (untrained); OFF (fix off); ON (fix on); SCR (ON geometry, targets
permuted within each step); SCRL (ON targets, trained at mirrored locations -h+noise); ALT (samples drawn from the
recorded E3-queried z_world, targets rbf); each at 10 steps (= one native cycle) and 300 steps (saturated).
Reference = OFF_10. "Avoidance retained" = (elite mean RBF-core terrain minus pool mean) / (the same for OFF_10):
1 = the CEM stage avoids residue as much as the production field does; <=0 = the avoidance is gone or reversed.

| Cell | Metric | NONE | ON_10 | SCR_10 | SCRL_10 | ALT_10 | ON_300 | SCR_300 | ALT_300 |
|---|---|---|---|---|---|---|---|---|---|
| bw1.0 s42 | CEM avoidance retained | 1.00 | 0.35 | 0.36 | 0.71 | 1.00 | 0.41 | 0.33 | 1.00 |
| | CEM elite Jaccard | 0.99 | 0.17 | 0.17 | 0.27 | 0.87 | 0.16 | 0.14 | 0.85 |
| | E3 argmin flips | 0/151 | 23 | 23 | 15 | 2 | 15 | 30 | 2 |
| bw1.0 s43 | avoidance / Jaccard / flips | 1.00 / 0.95 / 0 | -0.49 / 0.01 / 0 | -0.49 / 0.01 / 0 | -0.48 / 0.02 / 0 | 1.00 / 0.91 / 0 | 1.00 / 0.96 / 0 | -0.43 / 0.02 / 0 | 1.00 / 0.92 / 0 |
| bw1.0 s44 | avoidance / Jaccard / flips | 0.99 / 0.89 / 0 | -0.55 / 0.01 / 7 | -0.53 / 0.01 / 6 | 0.38 / 0.17 / 9 | 0.95 / 0.73 / 0 | 0.28 / 0.23 / 1 | 0.26 / 0.14 / 3 | 0.99 / 0.82 / 0 |
| bw0.15 s42 | avoidance / Jaccard / flips | 1.00 / 0.98 / 1 | 0.30 / 0.17 / 14 | 0.28 / 0.17 / 15 | 0.57 / 0.25 / 11 | 1.00 / 0.98 / 2 | -0.23 / 0.08 / 74 | -0.00 / 0.11 / 43 | 1.00 / 1.00 / 0 |
| bw0.15 s43 | avoidance / Jaccard / flips | 0.84 / 0.69 / 0 | -0.23 / 0.03 / 0 | -0.23 / 0.03 / 0 | -0.20 / 0.03 / 0 | 1.01 / 0.91 / 0 | -0.13 / 0.05 / 0 | -0.19 / 0.03 / 0 | 1.01 / 0.95 / 0 |
| bw0.15 s44 | avoidance / Jaccard / flips | 0.36 / 0.58 / 0 | -0.97 / 0.09 / 6 | -0.98 / 0.08 / 6 | 0.90 / 0.09 / 7 | 0.98 / 0.92 / 0 | -0.51 / 0.29 / 1 | 0.50 / 0.06 / 5 | 0.99 / 0.99 / 0 |
| bw1.0 s42, no warmup | avoidance / Jaccard / flips | 0.99 / 0.97 / 0 | 0.19 / 0.11 / 20 | 0.21 / 0.11 / 21 | 0.42 / 0.16 / 20 | 0.86 / 0.68 / 1 | 0.80 / 0.60 / 2 | 0.37 / 0.15 / 10 | 0.96 / 0.78 / 2 |

(E3 denominators: s43 30, s44 36/31, bw0.15 s42 132, no-warmup 143.) RBF_ONLY (neural zeroed) vs OFF_10: avoidance
retained 0.99-1.00, Jaccard 0.99-1.00, 0 flips. The production neural head contributes nothing either way.

Readings:
1. **The consumer is sensitive**, so this is not "consumer insensitive in all arms". The CEM elite stage reads the
   residue RBF core in the harm-avoiding direction: OFF_10 elites sit 0.005-1.9 below the pool mean in residue
   terrain. E3's rho=0.5 residue term is a minority of the score spread (rho*phi spread p50 0.004-0.73 vs total
   4.8-14.5), and the argmin it selects does not systematically avoid residue.
2. **ON_10 equals SCR_10 in all 7 cells** on all three metrics, to about +/-0.02 avoidance, +/-0.01 Jaccard and
   +/-1 flip. The consumer's response to the fix is therefore carried by the target LEVEL, not by harm geometry. The
   mechanism: the net learns a level near 0.61x peak on the shell, and its ReLU extrapolation at the rollout's
   distant states is large (0.1*neural at E3 queries 1.3-6.3, vs RBF-core mean 0.08-9.3) and anti-correlated with
   the RBF core.
3. **The direction is wrong.** ON at the native budget cuts the CEM stage's residue avoidance to 0.19-0.35 in 3 of 7
   cells and reverses it (-0.23 to -0.97) in the other 4. SCRL (right targets, wrong place) behaves the same way in 5 of 7 cells.
   Turning the fix ON in a production driver would make candidate generation LESS harm-avoiding.
4. **ALT reaches the consumer but adds nothing.** Correlation with the RBF core is 0.44-0.96 at 10 steps and
   0.997-1.000 at 300. Avoidance is retained (0.86-1.01) and flips stay at 0-2. It converges to about 0.1 x the RBF
   core, a ~1.1x rescale of what the consumer already reads. The small Jaccard drop (0.68-0.98 at 10 steps) is rescale-induced
   reordering in a term mixed with a modulatory component, not new information. This is GFLAG-0442's arithmetic,
   now measured at the native consumer.

D3 (closed-loop behaviour) was not measured, and this record does not claim it. By the brief's stop rule it is not
needed: no variant supplies harm-specific information for behaviour to act on.

## Q4: the alternative, prototyped in the throwaway worktree only

ALT above is the prototype. Each step draws `n = len(harm_locations)` points from the detached pool of E3-queried
z_world recorded during waking; targets are `rbf_field(points)` under `no_grad`; the Adam budget matches. Detach
discipline: the pool entries are `.detach().clone()` copies of the `evaluate_trajectory` input, the same convention
as `_harm_history` (field.py:706). No graph links across ticks. It is the only variant whose training support covers
where the consumer reads, and it reaches the consumer faithfully. **It does not deliver D2 in the claim's sense**:
distilling rbf targets reproduces rbf. Anything more needs the unauthorised `mech018-contextualisation-objective`
row (a harmless-context signal plus a signed or gating combination), and this record does not design that.

## What this means for the landing and for MECH-018

- Landing the GFLAG-0441 patch **default-OFF is safe** (bit-identical; contract C11). Its correct domain label is
  **D1 only**: "integrate() distils a non-zero target at world_dim=32". It must NOT be recorded as unblocking any
  consumer-level MECH-018 readout, and no driver should turn it ON as "the working residue integration". At the
  production budget, ON degrades CEM harm avoidance non-specifically.
- `residue-integrate-sampling-collapse-world-dim-32` can close as built (D1). `mech018-contextualisation-objective`
  gains a measured design constraint: its training support must be the consumer-queried z_world (rollout states),
  not a harm-centred shell. And while the rollout diverges (below), its effective support is rollout steps 0-3.

## Unexpected, larger finding: the E2 world rollout is divergent (upstream of residue)

At this probe's config (from_dims defaults, 600 warmup steps of `compute_prediction_loss + compute_e2_loss`,
warmup loss 1.7e-3 -> 4.0e-4), every candidate's z_world norm grows about 1.2x per rollout step: from 0.49 to 327
over the 30-step `rollout_horizon`, with p95 = p50 across candidates at each step. It is the same in the
no-warmup cell (E3 query distance p50 12.1 bw) and at both bandwidths. Consequences, beyond residue:

- any z_world-geometric scorer (residue, benefit terrain, harm_eval_head on z_world) sees informative input only on
  the first ~2-3 steps, and whatever its extrapolation does over the other ~27;
- the CEM "lowest-residue" elite ranking is dominated by rollout-norm growth, not place.

This is D1 at a small warmup budget. It needs re-measuring on a production-trained agent (a real EXQ checkpoint)
before anyone treats it as the earliest broken edge. If it holds, it sits upstream of every residue fix and is the
edge the breakthrough pass is looking for: "prediction of alternatives" leaves the manifold that evaluation is
defined on.

## Limitations (stated plainly)

- Mac CPU, 3 seeds per bandwidth, small warmup (600 steps), W1 400 / W2 200 steps, CausalGridWorldV2 8x8, 2 hazards,
  3 resources, EXQ-1072's config slice (world_dim=32 = deployed). Seeds 43/44 had few harm events (59/199 history
  entries), and their E3 select counts are small (30-36).
- The counterfactual re-scores recorded candidate sets. It does not regenerate CEM proposals under each arm, so it
  understates downstream divergence. That makes it conservative for "ON changes the consumer" and neutral for the
  ON = SCR equality.
- "Avoidance retained" uses the RBF core as the harm-proximity yardstick. That is the field's own definition of
  harm location, not an environment ground truth. Harm-proximity behaviour (D3) was not run.

## Run log

```
worktree: git -C ree-v3 worktree add --detach .scratch/breakthrough-20260924/residue/ree-v3-wt origin/main  (00210b5)
          git apply --3way .scratch/breakthrough-20260924/residue_gflag0441_full.patch
cells:    residue_reach_probe.py --seed {42,43,44} --warm 600 [--harm-bw 0.15]   -> results/w600_*.json
          residue_reach_probe.py --seed 42 --warm 0                              -> results/w0_bwNone_s42.json
          residue_reach_probe.py --seed 43 --warm 600 (with per-step profile)    -> results/prof_w600_bwNone_s43.json
wall:     282-717 s per cell, torch.set_num_threads(2)
```
