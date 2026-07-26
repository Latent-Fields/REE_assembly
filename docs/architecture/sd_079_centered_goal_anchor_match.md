---
title: "SD-079: common-mode-invariant (centered) z_goal cue for goal-anchor match"
nav_exclude: true
status: provisional
status_asof: 2026-07-26
status_claim: SD-079
---

# SD-079: hippocampal.common_mode_invariant_goal_anchor_match

**Claim ID:** SD-079
**Subject:** hippocampal.common_mode_invariant_goal_anchor_match
**Registered:** 2026-07-22
**Status:** IMPLEMENTED (2026-07-22)
**Depends on:** SD-039 substrate (`Anchor.goal_match`, ree-v3 `ree_core/hippocampal/anchor_set.py`), MECH-292 (`GhostGoalBank`), SD-008 (root cause), SD-066 / SD-077 / SD-078 (the same fix on three other consumers)
**Blocks:** MECH-292 (ranked ghost-goal bank), MECH-339 (composite cue + outshining gate), MECH-293 (ghost-goal seeding), MECH-340 (persistence-efficacy gate, which reads the same ranked pool)

## Problem

`Anchor.goal_match` is a raw cosine between a stored `z_goal_snapshot` and the
current `z_goal`. **`z_goal` is not an independent stream** -- it is an EMA
attractor pulled toward `z_world`, so it inherits the SD-008 common-mode offset
and, being an integrator, concentrates it further.

Measured 2026-07-22 (session `sad-newton-00451d`) on the V3-EXQ-669b Stage-0
nursery, seed 101, `alpha_world=0.9`:

| signal | pairwise cosine min / mean | ‖mean‖/mean‖·‖ |
|---|---|---|
| raw `world_obs` (control) | 0.3000 / 0.6859 | -- |
| `z_world` | 0.9767 / 0.9928 | 0.9964 |
| **`z_goal`** | **0.9878** / 0.9969 | **0.9987** |

Consequence, measured by scoring a real 24-anchor pool with the real module:

| statistic | raw | centered |
|---|---|---|
| `goal_match` min / max | 0.9884 / 0.9995 | 0.0000 / 0.9709 |
| `goal_match` spread across the pool | **0.0111** | **0.9709** |
| MECH-292 `goal_match_floor` (0.05) excludes | **0 / 24** | 9 / 24 |
| MECH-339 outshining gate nonzero on | **0 / 24** | 9 / 24 |

Two distinct failures follow, and the second is the more serious:

1. **The ranking term is inert.** `goal_match_weight * goal_match` varies by 0.011
   across the pool, so the motivational-relevance channel contributes essentially
   nothing to `ghost_priority` ordering -- the bank ranks on wanting, staleness
   and recoverability alone while *appearing* to be a four-term composite.
2. **Both ABSOLUTE gates downstream are dead, unconditionally.** The
   `goal_match_floor` "rumination guard" excludes nothing it was built to exclude.
   And MECH-339's outshining gate,
   `clip_[0,1]((outshine_pivot - goal_match) / outshine_pivot)` with
   `outshine_pivot = 0.5`, evaluates to **exactly 0.0 for every anchor** whenever
   `goal_match >= 0.5` -- which is always. MECH-339's composite cue therefore
   contributes a context term of identically zero the moment it is switched on:
   the constraint would read as falsified by a mechanism that never ran.

## Solution

Apply the **SD-066 / SD-077 / SD-078 pattern**: a slow EMA common-mode baseline
over presented waking `z_goal` cues, with the match taken on the centered
residuals.

- **Baseline lives on `AnchorSet`** (`_goal_baseline`), the pool owner.
  `GhostGoalBank` reads it through its existing `anchor_set` reference, so both
  consumers share one baseline and cannot desynchronise.
- **`Anchor.goal_match(current_z_goal, baseline=None)`** -- the new argument
  defaults to `None`, which is the identity. The pre-SD-079 call form is
  bit-identical.
- **Snapshots are stored RAW and centered at comparison time** (the SD-077 trade).
- **Both the READ and the WRITE path advance the baseline.** This is not
  cosmetic: advancing on reads alone lets the baseline be lazily seeded *from the
  query itself*, which centers every snapshot against the query, drives every
  residual to ~0 and every match to 0.0. Measured -- the first ON arm scored
  0.0000 across all 20 anchors before the write-path advance was added. Pinned as
  contract C6.
- **MECH-094:** `simulation_mode` cues never advance the baseline. On the write
  path this holds by construction -- a `goal_payload` is only attached when the
  SD-039 flag is on AND the write is not simulation/replay, so a payload's
  presence certifies a waking cue.

### Config

| Param | Type | Default | Purpose |
|---|---|---|---|
| `AnchorSetConfig.goal_cue_centering` | bool | `False` | master switch; OFF allocates no baseline and passes `baseline=None` |
| `AnchorSetConfig.goal_cue_baseline_alpha` | float | **`0.05`** | common-mode EMA rate -- see below |
| `REEConfig.from_dims(goal_cue_centering=..., goal_cue_baseline_alpha=...)` | | | plumbed to the nested `AnchorSetConfig` |

### Why alpha is 0.05 here and 0.02 in SD-066 / SD-077 / SD-078

**Do not "harmonise" this back to 0.02.** Those three center a *per-tick encoding*
(`z_world`), whose common mode is near-stationary. `z_goal` is an **integrator**,
so its common mode **drifts**, and a baseline slow enough for a stationary cue lags
a drifting one -- the lag direction then becomes a new shared component and
re-pins the readout. Measured on the real agent across seeds 101 / 202 / 303
(`goal_match` spread across a 20-anchor pool; raw spread 0.0051-0.0144):

| alpha | seed 101 | seed 202 | seed 303 | anchors below floor |
|---|---|---|---|---|
| 0.02 | 0.1508 | 0.3319 | 0.0942 | 0/20 (still lagging) |
| **0.05** | **0.9999** | **0.9995** | **0.9999** | **2/20** |
| 0.10 | 0.9995 | 0.9975 | 0.9992 | 4/20 |
| 0.20 | -- | -- | -- | 14/20 (over-tracking) |
| 0.50 | -- | -- | -- | 18/20 (over-tracking) |

0.05 is the measured plateau; 0.2 and above is actively harmful, the baseline
chasing the cue and erasing genuine matches.

**Contract scope note.** Only the OVER-tracking bound is asserted in the contract
(C7). The lag half does **not** reproduce on a synthetic fixture, because the real
`z_goal` drift saturates (it is an EMA attractor) whereas a cheap fixture drifts
linearly -- and under linear drift a baseline seeded from an early cue sits far
from the query, manufacturing a wide spread at 0.02 and inverting the ordering.
Calibrating a fixture until it reproduced the ordering would be fitting the test
to the answer, so it was deliberately not done.

**Backward compatible.** With `goal_cue_centering=False` no baseline is allocated,
`goal_cue_baseline` returns `None`, and every `goal_match` call is the identity.
Verified by contract C1.

**Phased training: not required.** Pure stateful tensor state, no `nn.Module`.

## Architecture Context

Fourth instance of the same failure mode (SD-066, SD-077, SD-078), and the second
found by sweep rather than by a burned experiment. It is the instance that extends
the pattern **beyond `z_world` itself** to a *derived* latent: `z_goal` is
downstream of `z_world` and inherits the offset more strongly than its source.

The generalisation worth carrying forward is therefore not "audit `z_world`
consumers" but **"audit consumers of `z_world` and of anything integrated from
it, for ABSOLUTE thresholds"**. Rank-based and difference-based readouts remain
exempt -- but note failure (1) above: a *weighted additive term* in a ranking
formula is not automatically exempt, because a near-constant term contributes no
ordering information even though the readout is nominally rank-based.

## What This SD Enables

- MECH-292's `goal_match` channel becomes a real contributor to `ghost_priority`
  ordering rather than a near-constant additive offset.
- MECH-339's composite cue + outshining gate becomes testable at all; any prior
  or future measurement of it with `goal_cue_centering=False` is measuring a
  channel that is identically zero.
- The MECH-292 `goal_match_floor` rumination guard starts excluding anchors.
- MECH-293 / MECH-340 read the same ranked pool and inherit the repair.

## Related Claims

SD-039 (anchor goal payload), MECH-292 (ghost-goal bank), MECH-339 (composite cue
+ outshining), MECH-293, MECH-340, SD-008 (root cause), SD-070 (why the
encoder-level fix is unavailable), SD-066 + SD-077 + SD-078 (prior instances).
