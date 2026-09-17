# MECH-268 gradedness successor: the banked lever does not reproduce on a trained agent

**Status: AWAITING USER REVIEW. Nothing in this file has been written to claims.yaml (or whichever registry).**

Session: `metaworker-science-20260917-mech268-gradedness` (headless, campaign
`science-20260917-mech268-gradedness`), 2026-09-17. Chip
`chip-20260916-mech268-nonsaturating-harm-gradedness-queue`. No queue entry was added and no
experiment script was written; `ree-v3` is untouched.

## Why this file exists

The user ratified a design on 2026-09-17 (Option 1 + Option 3 readouts, 3 seeds x 4 rungs + OFF).
Its first step is: *pin `contextual_safety_harm_threshold` so realized `harm_class_fraction` lands
near ~0.5*, with a per-rung non-degeneracy gate `harm_class_fraction` inside `[0.3, 0.7]`.

That step rests on a single banked measurement carried forward by the AMBER pre-flight from
GFLAG-0299, listed under "BANKED AND REUSABLE ... do not rediscover":

> THE WORKING LEVER is `contextual_safety_harm_threshold`. Smoke sweep over {0.05, 0.55, 0.75}
> moved `harm_class_fraction` 1.000 / 0.625 / 0.450 (spread 0.45).

**Re-measured this session on a TRAINED agent, that lever is inert.** The pinning step is not
executable, and the ratified non-degeneracy gate would reject every achievable regime.

## Measurement 1 -- the lever is inert on a trained agent

P0 warmup 20 episodes x 100 steps (`run_p0_warmup`, converged, seed 42), one `state_dict`
snapshot shared across cells, eval 500 steps per threshold, `dacc_saturation_strength=0.3`,
window 8, grace 2, eval env `size=7 num_hazards=6`. `harm_class_fraction` is computed from the
**spy on `dacc.record_outcome`** -- i.e. the class stream that actually drives `n_rec` -- which is
the fix for GFLAG-0299 Finding 2 (its spy was installed outside the injection wrapper).

| `contextual_safety_harm_threshold` | `harm_class_fraction` | n_fresh | mean sat_factor | interior frac | n_rec values |
|---|---|---|---|---|---|
| 0.05 | 1.000 | 56 | 0.4092 | 0.946 | 0..8 |
| 0.35 | 0.982 | 56 | 0.4207 | 0.929 | 0..8 |
| 0.50 | 0.964 | 56 | 0.4322 | 0.911 | 0..8 |
| 0.60 | 0.964 | 56 | 0.4322 | 0.911 | 0..8 |
| 0.65 | 0.964 | 56 | 0.4322 | 0.911 | 0..8 |
| 0.70 | 0.946 | 56 | 0.4396 | 0.911 | 0..8 |
| 0.80 | 0.946 | 56 | 0.4396 | 0.911 | 0..8 |

Sweeping the threshold across its whole usable range moves `harm_class_fraction` by **0.054**
(1.000 -> 0.946), never approaching 0.5 and never entering the ratified `[0.3, 0.7]` gate. The
banked spread of 0.45 does not reproduce.

**Why the banked number differed:** it was almost certainly measured on an untrained or
barely-trained agent. An untrained-agent replication of the same sweep this session produced
1.000 / 0.956 / 0.240 / 0.900 / 0.000 at thresholds 0.05 / 0.55 / 0.65 / 0.75 / 0.85 -- large
movement, but **non-monotone and erratic**, because the harm class feeds `record_outcome` ->
`n_rec` -> `sat_factor` -> PE -> `control_required` -> selection. The threshold is inside a closed
behavioural loop, so it is not a clean exogenous dose on harm density at any training level: it is
chaotic when untrained and saturated when trained.

## Measurement 2 -- gradedness is nevertheless richly exercised, for a different reason

At **every** threshold above, `n_rec` spans the full `[0..8]` and interior occupancy (sat_factor
strictly between the 0.25 floor and 1.0) is **0.911-0.946**. The saturation function is exercised
across its whole range in the live loop.

The mechanism is **not** harm-class mixedness. It is SD-034 closure:
`ClosureOperator._fire()` calls `dacc.reset_outcome_history()`
(`ree_core/governance/closure_operator.py:727-730`, `closure_reset_outcome_history=True` by
default), clearing the saturation FIFO on rule completion. A trained agent completes rule-states
regularly, so `n_rec` repeatedly sweeps 0 -> 8 even when every recorded class is identical.

**This is the load-bearing reframe:** the ecological driver of graded dACC saturation in the live
loop is **closure cadence**, not harm-density mixedness. The ratified gate
(`harm_class_fraction in [0.3,0.7]`) is a proxy for non-degeneracy whose premise -- *one-class
stream implies pinned `n_rec`* -- is empirically false on a trained agent. It would reject the
regime in which gradedness is *maximally* exercised (threshold 0.05, interior 0.946).

It also explains V3-EXQ-729's degenerate `sat_factor = 0.25` in all 6x2 cells without appealing to
harm chronicity: whatever the harm stream did, 729's cells were not firing closure.

## Measurement 3 -- the strength ladder works, and its separations are as predicted

Confirmed at runtime that `dacc_saturation_strength` propagates into `DACCConfig` and moves
`sat_factor` at fixed history (`_outcome_history=[1,0,1,1,0,1,1,1]`, n_rec=6):

| strength | 0.0 | 0.15 | 0.3 | 0.5 |
|---|---|---|---|---|
| sat_factor | 1.0000 | 0.6250 | 0.4545 | 0.3333 |

These match the analytic predictions the ratified design was sized on. The dose ladder itself is
sound; only the harm-regime pinning step and its gate are broken.

## Measurement 4 -- the E3 latch, and the real sample-size denominator

`dacc.forward()` (and therefore `record_outcome`) runs **only on an E3 tick**. Measured realised
period: **8.57-8.93** env steps (60 env steps -> 7 fresh calls; 500 eval steps -> 56 fresh calls),
confirming and slightly refining GFLAG-0299 Finding 4 ("9, not the assumed 8").

`_last_saturation_factor` / `_last_pe_unsaturated` / `_last_outcome_recurrence` **latch** between
E3 ticks. V3-EXQ-729's driver reads them once per env step with no clear, so its `sat_factor`
series is pseudo-replicated ~8.6x and its effective n is ~1/9 of its reported step count. Any
successor must use the CLAUDE.md/`/queue-experiment` latch idiom, adapted to the dACC:

```python
agent.dacc._last_pe_unsaturated = None      # clear IMMEDIATELY before the call
agent.select_action(candidates, ticks)
if agent.dacc._last_pe_unsaturated is None:
    n_latched_ticks += 1                     # no fresh dACC forward; record NOTHING
else:
    ...                                      # one genuine observation
```

and must emit `n_latched_ticks` so the true denominator is auditable.

Cost measured: ~85 ms per eval step, ~266 s for a 20x100 P0 warmup (single cloud worker, cpu).

## What is now owed

The ratified design's criteria (i)/(ii)/(iii) are all still sound and all still answerable. Only
the harm-regime pinning step and the `harm_class_fraction in [0.3,0.7]` gate are broken. The
question put to the user in the decision chip is which non-degeneracy gate replaces them --
a criterion change, so not this session's to make.

## Provenance

Probes were run against `ree-v3` at the working-tree state of 2026-09-17, on `ree-cloud-5`
(`linux-x86_64`). Read-only: no substrate file was modified. Source paths cited:
`ree_core/cingulate/dacc.py:229-279`, `ree_core/agent.py:7544` (sole live `dacc(...)` call site,
passes no `current_outcome_class`), `ree_core/agent.py:10184-10198` (live `record_outcome` tail),
`ree_core/governance/closure_operator.py:727-730`.
