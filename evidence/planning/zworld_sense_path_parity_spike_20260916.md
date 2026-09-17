# SD-ZWORLD-SENSE-PATH-PARITY -- discriminating probe (scoping spike)

- **Spike for:** `substrate_queue.json` entry `SD-ZWORLD-SENSE-PATH-PARITY` (status `pending_implementation`), minted by `governance-20260916` from the confirmed `failure_autopsy_V3-EXQ-1030_2026-09-14`.
- **Chip:** `chip-20260916-zworld-sense-path-parity-probe-spike`
- **Session:** `zworld-probe-20260917` (Opus subagent of `orchestrate-20260917-1138`; user per-launch decision 2026-09-17T11:44Z)
- **Run:** 2026-09-17, laptop `DLAPTOP`, `/opt/local/bin/python3`, torch 2.10.0
- **Probe:** `ree-v3/experiments/_probes/zworld_sense_path_parity_probe.py` (+ `summarise_parity_probe.py`)
- **Raw results:** `ree-v3/experiments/_probes/results_field_off.json`, `results_field_on.json`
- **NOT an experiment.** No manifest, no `evidence/experiments/` write, no queue entry, no `ree_core/` change. The train-through variant is a probe-local subclass of `ZWorldP0Trainer`.

---

## 1. The question

V3-EXQ-1030 measured the `agent.sense()`-path `z_world` ~0.10 absolute LOWER in held-out
linear-probe decodability of the 5-way oracle waypoint direction than
`split_encoder.world_encoder(raw world_state)` -- the path SD-070's P0a recipe actually
trains (arm means 0.3832 vs 0.4838 `field_off`, 0.4023 vs 0.5086 `field_on`;
majority-adjusted gap +0.1015, direct winning 8 of 10 cells).

The 2026-09-16 cross-model red-team (F3) marked the ATTRIBUTION unmeasured, between:

- **Cause A -- train/inference divergence.** `world_encoder` was optimised on raw `world_state`
  and evaluated on `world_obs_encoder(world_state)`. Fix: train P0a THROUGH the pre-projection.
- **Cause B -- intrinsic loss in the random ReLU projection.** A random `Linear + ReLU` destroys
  linear separability by itself. Fix: bypass it at inference.

The entry mandates running the discriminating probe before choosing.

## 2. Verdict

**Neither. The effect the two causes were competing to explain is not reliably present, and
the ~0.10 figure is an artifact of the measurement rather than a property of the pathway.**

Three findings, each independently sufficient:

1. **The 0.10 gap does not reproduce.** Measured as a PAIRED per-(seed, split) difference on
   1030's own data-collection code, seeds, and probe budget: **+0.007 +/- 0.082 (`field_off`)**
   and **+0.019 +/- 0.083 (`field_on`)**, with the direct path ahead in **46% / 62%** of 50
   cells -- against 1030's +0.1015 and 8 of 10.
2. **Under a CONVERGED probe the gap vanishes.** Same unnormalised features, 10x the gradient
   budget: **-0.018 (`field_off`) / +0.002 (`field_on`)**. Train-split standardisation:
   **-0.028 / -0.023** -- the sense path is then marginally AHEAD.
3. **Cause B is refuted directly, at matched width.** A fresh random `Linear(275,275) + ReLU`
   applied to `world_state` and probed against unprojected `world_state`, encoder-free, costs
   **-0.011 / -0.010 / +0.002 (`field_off`)** and **+0.007 / -0.012 / +0.003 (`field_on`)** --
   i.e. nothing. A full-rank random ReLU projection does not destroy the linear decodability
   of this label.

**Therefore the held build `chip-igw-217-substrate-ready-sd-zworld-sense` should implement
NEITHER fix as a decodability repair: there is no measured decodability deficit to repair.**
What remains is a real but cheap code-hygiene divergence -- see section 6.

## 3. Why 1030 saw 0.10: probe under-convergence, not representation

`agent.world_obs_encoder` is `Linear(275,275) + ReLU` at default init. The `z_world` it
yields is about **5x smaller in magnitude** than the direct path's (`mean_abs` 0.043 vs
0.234). 1030's probe is a single `nn.Linear` trained with Adam at a FIXED `lr = 5e-3` for a
FIXED 150 steps. On features 5x smaller that budget leaves the probe **under-converged** --
and the shortfall lands in test accuracy looking exactly like lost information.

The signature is in **train** accuracy, and it is already present in 1030's OWN manifest:

| | direct-path train acc | sense-path train acc |
|---|---|---|
| V3-EXQ-1030 manifest, all 10 cells | 0.539 - 0.692 | 0.487 - 0.576 |
| this probe, `field_off`, unnormalised | 0.592 | 0.521 |
| this probe, `field_off`, standardised | 0.608 | 0.592 |
| this probe, `field_on`, unnormalised | 0.626 | 0.538 |
| this probe, `field_on`, standardised | 0.662 | 0.635 |

The sense path's TRAIN accuracy is below the direct path's in **all 10 of 1030's own cells**,
and the deficit closes the moment feature scale or gradient budget is fixed -- while test
accuracy closes with it. A representation that had genuinely shed the label would not
recover on standardisation alone.

## 4. Why 1030's gap looked robust: split noise, and a split confound

- **Between-split spread within a single arm and seed reaches 0.42 absolute accuracy**
  (`field_off` unnormalised; 0.39 `field_on`; 0.30-0.36 standardised). Under a random policy
  episodes terminate early, so n is 957-1140 samples per cell, not 6000, and an 80/20
  EPISODE split leaves only 184-283 held-out samples. A 0.10 difference sits well inside that.
- 1030 fitted each arm under a **different** episode-split seed (`seed`, `seed+1`, `seed+2`,
  `seed+3`), so its sense-vs-direct contrast varied the held-out EPISODE PARTITION as well as
  the feature set. The autopsy's F2 correction records this and applies a majority-class
  adjustment; that corrects the label-balance component of the partition difference but not
  the rest. **Pairing within one split, as here, removes it exactly** -- and makes the
  majority adjustment identically zero, since both members of a pair are scored on the same
  held-out set.

## 5. Arm-by-arm results

Five seeds (42-46, 1030's own), ten episode-split seeds per arm, three probe conditions:
`unnorm` is 1030-identical; `long` is the same features at 10x gradient budget; `std`
z-scores on train-split statistics only. Contrasts are PAIRED per (seed, split), n = 50.
Arms are compared only within a matched-width family (32-dim `z_world`, 275-dim
`world_obs`, 50-dim raw slice).

### 5.1 What each contrast licenses

| contrast | what it isolates | `field_off` unnorm / long / std | `field_on` unnorm / long / std |
|---|---|---|---|
| `1030_gap_direct_minus_sense` | the 1030 headline | +0.007 / -0.018 / -0.028 | +0.019 / +0.002 / -0.023 |
| `preprojection_only` | the pre-projection ALONE (no top-down, reafference or EMA) | +0.014 / -0.018 / -0.030 | +0.024 / +0.005 / -0.018 |
| `sense_beyond_preprojection` | top-down + reafference + EMA, i.e. everything else `sense()` does | -0.006 / +0.000 / +0.002 | -0.005 / -0.003 / -0.004 |
| `fresh_random_only` | the arm the chip mandated: a FRESH random projection in the same slot | +0.039 / +0.012 / -0.000 | +0.060 / +0.045 / +0.020 |
| `ema_only` | the `alpha_world = 0.9` temporal EMA alone | -0.001 / +0.001 / +0.001 | -0.004 / -0.001 / -0.002 |
| `train_through_recovery` | does training P0a THROUGH the pre-projection recover anything? (Cause A's fix) | +0.029 / -0.002 / -0.004 | +0.018 / -0.007 / -0.015 |
| `random_relu_intrinsic_loss` | **Cause B**, encoder-free, matched 275-dim width | -0.011 / -0.010 / +0.002 | +0.007 / -0.012 / +0.003 |
| `untrained_wobs_intrinsic_loss` | the agent's OWN untrained pre-projection, encoder-free | -0.006 / -0.001 / +0.029 | +0.011 / +0.010 / +0.037 |

**Scale reference for "distinguishable from zero".** `ema_only` is a contrast that should be
null and is measured at **+/-0.004 with sd 0.009-0.012** -- so the instrument resolves a true
zero tightly when the two feature sets are near-identical. Every cross-feature-set contrast
above carries **sd 0.05-0.08**, which is the genuine between-split variance of comparing two
different 32-dim feature sets on ~200 held-out samples. None of them separates from zero at
that spread.

**One honest wrinkle, reported rather than smoothed:** `fresh_random_only` is the one contrast
that stays positive across conditions in `field_on` (+0.060 / +0.045 / +0.020, direct ahead in
74-76% of cells). It is NOT evidence for Cause B: the encoder-free matched-width control
(`random_relu_intrinsic_loss`) is zero, so whatever this is happens at the 32-dim bottleneck,
not in the projection. And the arm has only **five independent projection draws** (one per
seed), so its effective n for projection-draw variance is 5, not 50; the agent's own
pre-projection -- the path that actually ships -- measures at +0.005 / -0.018 under the same
conditions. Read it as draw-to-draw variance in an off-distribution input to a raw-trained
encoder, not as a property of the production path.

### 5.2 Positive controls (the pipeline is working)

- `ctrl_raw_slice` (1030's raw 25/50-dim waypoint-channel positive control): **0.340
  `field_off` -> 0.651 `field_on`** unnormalised (0.341 -> 0.704 standardised), a +0.31 field
  lift against 1030's own `RAW_LIFT_FLOOR = 0.15`. The manipulation reaches the raw feature
  space as designed.
- **Data-collection fidelity is exact.** Per-seed sample counts reproduce 1030's manifest
  byte-for-byte: 1140 / 957 / 1071 / 1044 / 1107 for seeds 42-46.
- **P0a trained in both variants.** `zworld_encoder_trained: true`, 4 of 4 `world_encoder`
  tensors moved, `world_encoder_max_abs_delta` 0.23-0.39 on every seed, in BOTH the
  raw-trained and the train-through variant. P0a's own held-out grounding lift is ~0.58 in
  both, so **training through the pre-projection costs the P0a objective nothing.**
- **The mechanism the autopsy asserted is confirmed as a code fact.** The `world_obs_encoder`
  state-dict delta after raw P0a is **exactly 0.0** on every seed -- the SD-070 recipe never
  touches it. Under the train-through variant the same delta is ~13.5. The training/inference
  divergence is real; it simply costs no measurable decodability.

## 6. Recommended disposition of the substrate_queue entry (NOT applied by this spike)

`REE_assembly/evidence/planning/substrate_queue.json` was held by another live session
(`bold-swanson-1789a0-land`) throughout this spike, so no edit was made to it. For whoever
holds it next:

1. Add `spike_result_2026_09_17`: **attribution resolved as NEITHER cause. The ~0.10
   decodability gap does not reproduce; it is attributable to linear-probe under-convergence
   on 5x-smaller features plus episode-split noise. Both candidate fixes measure at zero
   within a +/-0.05 noise band, so the choice between them is moot on decodability grounds.**
2. **Do not schedule the 34-driver `run_zworld_p0` migration on decodability grounds.** The
   migration cost the 1030 driver's own red-team F5a flagged now buys a measured ~0.00.
3. **Do not simply close the entry as invalid either.** What survives is a genuine, confirmed
   CODE-level divergence -- the training path and the inference path differ and nothing
   reconciles them -- which is a real hygiene defect and a latent hazard if the pre-projection
   ever stops being a full-rank, near-identity-scale random map (e.g. if it is ever narrowed,
   trained by a `agent.parameters()` optimiser in one lineage but not another, or given a
   different init). Suggested: keep the entry, demote `severity` from `degrading` to a
   hygiene/latent class, and re-scope the title from "repair a ~0.10 decodability loss" to
   "make the two paths agree". If it is kept as a build, **train P0a THROUGH
   `world_obs_encoder`** is the better of the two -- measured here it costs nothing in P0a's
   own objective, nothing in decodability, and removes the divergence -- but it is not urgent
   and should not gate anything.
4. **A finding for V3-EXQ-1030a** (already routed by the autopsy to `queue-experiment`): its
   probe must standardise features or verify convergence before comparing two paths whose
   feature scales differ, must fit both paths on ONE split, and must report train accuracy
   alongside test accuracy so under-convergence is visible. Comparing unnormalised features
   at a fixed lr/step budget is what produced the 0.10 in the first place. This sits
   alongside, not instead of, the autopsy's required change 5.
5. `INV-086` / `MECH-428` claim fields are untouched by this spike. `pending_retest_after_substrate`
   on MECH-428 was set for reasons this spike does not adjudicate.

## 7. Adjacent check: is z_world a frozen random projection in this regime?

The `validated` entry `sd_zworld_warmup_optimizer_group` records that the x734/737 driver
family's P0/P1 warmup had no optimizer group covering `latent_stack`, making z_world a frozen
random projection (0 of 61 latent_stack tensors changed at `p0_episodes = 200`, four
independent strikes). **That defect does NOT apply to the regime probed here.** This driver
family calls `run_zworld_p0` explicitly and guards it with `assert_world_encoder_trained`;
measured here, 4 of 4 `world_encoder` tensors move on every seed and in both variants. The
entry's `validated` status (fix landed `b523b9c`, 2026-07-20) is consistent. No new finding.

## 8. Method notes and self-red-team

- **RNG contract.** `reset_all_rng(seed)` normally lives in `arm_cell.__enter__`; this probe
  calls its cell function directly, so it calls `reset_all_rng(seed)` EXPLICITLY at cell
  entry. Both P0a variants run under `_rng_neutral()` and start from a byte-identical agent
  snapshot; probe weight init is seeded from a saved-and-restored global state. No arm
  inherits another's stream offset.
- **Why the chip's mandated arm alone could not have answered this.** Within the SD-070
  lineage `world_obs_encoder` is itself untrained random, so a fresh random projection and
  the agent's own projection are the same KIND of object, differing only by draw; both feed a
  raw-trained encoder an off-distribution input, so comparing them separates neither cause.
  The arms that do are (a) the **train-through** variant and (b) the **encoder-free,
  matched-width** control. Both were added; the mandated arm was run as well and is reported.
- **Confounds ruled out rather than assumed away.** `agent.sense()` differs from the direct
  path in four ways, not one (pre-projection, top-down conditioning, SD-007 reafference, the
  `alpha_world` EMA); `preprojection_only` isolates the first, `ema_only` the last, and
  `sense_beyond_preprojection` shows the remaining two contribute ~0. Probe capacity: arms
  compared only within matched input width. Normalisation: applied to neither path in the
  1030-identical condition, to both in the standardised one, never to one only.
- **Known limits.** One env-config family (`CausalGridWorldV2` as 1030 configures it), 5 seeds,
  n ~ 1000 samples per cell -- the same statistical power 1030 had, deliberately, because the
  question is whether 1030's own result holds. This spike does NOT claim the two paths are
  identical; it claims the ~0.10 gap is unsupported and that both candidate causes measure at
  zero within about +/-0.05. A real effect below ~0.05 would not be detected here and would
  need more collection episodes. The `fresh_random_only` wrinkle in section 5.1 is the one
  place where more projection draws would be worth having.
