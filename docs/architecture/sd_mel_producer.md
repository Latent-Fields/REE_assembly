---
title: "SD-MEL-PRODUCER: environment.non_converging_world_rule_shift"
parent: "Sleep & Offline Integration"
grandparent: Architecture
nav_order: 12
---

# SD-MEL-PRODUCER: environment.non_converging_world_rule_shift

**Claim ID:** SD-MEL-PRODUCER
**Subject:** environment.non_converging_world_rule_shift
**Status:** VALIDATED (V3-EXQ-798a, 2026-07-29; confirmed failure_autopsy_V3-EXQ-798a_2026-07-30)
**Registered:** 2026-07-21
**Depends on:** (none unresolved)
**Blocks:** MECH-180 link (i), INV-050 ecological end-to-end demonstration

## Problem

MECH-180 / INV-050 split into two links:

- **link (i)** real graded novelty -> graded above-reference waking MEL
- **link (ii)** MEL -> graded offline-phase duration

Link (ii) is **owned by SD-MEL-CONSUMER and is BUILT + PROVEN**: V3-EXQ-718a's
injection positive control shows graded injected MEL producing exact-monotone graded
offline duration (`[9,13,18,24,30,38]` tracking `[0.6..2.5]`, all seeds).

Link (i) has never been demonstrated, and three runs establish that it cannot be
demonstrated in the current environment:

| Run | Readout |
|---|---|
| V3-EXQ-677 | C1 manipulation check: high- vs low-novelty mean E1 prediction error differed by **8.8e-07** against a 0.01 threshold. `env_drift_interval` 3 vs 999 plus context switching produced **no measurable novelty gradient**. Sleep counts identical across arms (SWS 80.0/80.0, REM 60.0/60.0). |
| V3-EXQ-718 | Consumer functional (C2 PASS 3/3) but C1 novelty-label monotonicity 0/3 -- the test-bed did not produce graded MEL (factor ordering LOW < NONE < MED ~ HIGH). |
| V3-EXQ-718a | Ecological measured MEL **~1e-5, noise-level and scrambled vs novelty level**; ecological HIGH DV 72/74 **below** the OFF baseline 90. `conv_rel_drop ~0.98`. |

The autopsies (`failure_autopsy_V3-EXQ-718_2026-07-07`,
`failure_autopsy_V3-EXQ-718a_2026-07-08`) both classify this as
`measurement_gap (environment / test-bed producer gap)` -- **not** a substrate ceiling
at the consumer and **not** a falsification of the claim.

### Root cause

`_drift_hazards()` (`causal_grid_world.py`, fired by `env_drift_interval`) only
**moves hazards**. The optimal prediction of a random walk is its mean; the
world-forward model learns that quickly and prediction error floors at the
irreducible noise level. Turning the drift knob up adds *sampling noise*, not
*learning load*. Hence a fully converged world model (`conv_rel_drop ~0.98`) and a
residual ecological MEL indistinguishable from noise.

## Solution

Periodically **re-permute the action -> displacement map**.

`E2.world_forward(z_world, a) -> z_world_next` takes the action as an input. When the
map changes, the learned forward model becomes systematically wrong and stays wrong
until re-learned. Between shifts the world is deterministic and therefore
**learnable**; each shift invalidates learned structure. That is genuine re-learning
load, graded by shift **rate**.

Config (env kwargs on `CausalGridWorld` / `CausalGridWorldV2`):

| Param | Type | Default | Purpose |
|---|---|---|---|
| `world_rule_shift_enabled` | bool | `False` | master switch |
| `world_rule_shift_interval` | int | `0` | world-steps between rule re-draws (0 = never) |
| `world_rule_shift_depth` | int | `0` | action-pair transpositions applied per shift |
| `world_rule_shift_scope` | str | `"action_map"` | reserved for a later structural-statistics variant |

Emitted in `info`: `world_rule_shift_occurred`, `world_rule_shift_count`,
`steps_since_world_rule_shift`.

### Why noise is not a substitute (the design's central constraint)

Grading **observation noise** would also produce a monotone MEL gradient -- but by
construction, on any substrate, whether or not MECH-180 is true. That is the
DV-symmetry artifact class (`failure_autopsy_V3-EXQ-604c`; the same defect that held
V3-EXQ-683 on 2026-07-21), where the delta is fixed before the run.

Elevated prediction error only counts as **learning load** if it is *reducible*.
The operational discriminator: genuine load **decays within a stationary window**
(the model re-learns the new rule), noise does not. `steps_since_world_rule_shift`
exists so a consumer can bin per-step PE by time-since-shift and measure exactly
that. The validation experiment carries a matched-PE noise arm as a negative
control for this reason.

### Design decisions that are load-bearing (do not "simplify" these)

1. **The class-level `ACTIONS` dict is never mutated.** The effective map is a
   per-instance `self._action_map`; mutating the class attribute would leak the
   permutation into every other env instance in the process.

2. **The shift schedule keys off a cumulative `_world_steps_total`, not
   `self.steps`.** `self.steps` is episode-local. Because episode length *itself*
   collapses as the world becomes less predictable, an episode-relative schedule
   makes the nominal interval stop controlling the actual shift rate. Measured on
   the first implementation probe (2026-07-21): intervals 60/30/15/8/5 produced
   **2/2/3/20/21** shifts -- non-monotone, and the resulting MEL ladder was
   non-monotone with it. Fixed by keying off world time.

3. **`_action_map`, the shift counters and `_world_steps_total` are NOT reset by
   `reset()` / `reset_to()`.** The action map is the world's causal structure, not
   episode state; resetting it to identity each episode would hand the forward
   model a fixed anchor to re-converge on and defeat the point.

4. **Every RNG draw sits inside the enabled guard**, so a disabled env consumes no
   randomness and is bit-identical to a pre-SD-MEL-PRODUCER env at the same seed.
   Every existing experiment depends on this.

5. **Episode length is a confound, not a nuisance.** Shift rate shortens episodes
   (measured 69.0 -> 13.5 steps across the ladder). Measurement must use a fixed
   **step** budget, not a fixed episode count, and report mean episode length per
   arm so the confound stays visible.

## Architecture Context

Producer half of the MECH-180 pair. `SD-MEL-CONSUMER`
(`ree_core/sleep/mel_consumer.py`) owns link (ii) and is already validated; this SD
owns link (i). The two are deliberately independent: the validation experiment for
this SD runs **with the consumer absent**, because 718a's `learning_extracted[1]`
records that the consumer's DV is a deterministic function of MEL, making
DV-monotone-in-measured-MEL near-tautological and unable to validate a producer.

No `LatentState` field, no encoder, no new module -> **no phased-training
requirement**. **MECH-094 does not apply**: nothing is written to memory during
non-waking states.

## What This SD Enables

- The ecological end-to-end MECH-180 / INV-050 demonstration (novelty -> graded MEL
  -> graded offline duration), which is currently environment-blocked. That run is
  **separate and still gated** on this test-bed validating first.
- Any future work needing a non-converging world: continual-learning /
  task-switching studies, world-model staleness, `V_s` invalidation under genuine
  structural change.

## Related Claims

MECH-180, INV-050, SD-MEL-CONSUMER, INV-049 (sleep as mathematical necessity for
model-building agents), SD-056 (contrastive auxiliary -- a confirmed P0
world-forward destabiliser; the validation base is recon-only for that reason).
