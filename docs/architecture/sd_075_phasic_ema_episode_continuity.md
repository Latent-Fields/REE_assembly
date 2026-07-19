---
status: candidate
status_asof: 2026-07-19
status_claim: SD-075
---

# SD-075: phasic.ema_episode_continuity

**Claim ID:** SD-075
**Subject:** phasic.ema_episode_continuity
**Registered:** 2026-07-19
**Status:** IMPLEMENTED 2026-07-19
**Depends on:** SD-069 `phasic_surprise_burst` (IMPLEMENTED -- capability present; this is a
baseline-continuity defect layered on top of it, not a missing capability)
**Blocks:** MECH-063 sub-claim (ii), which is `pending_retest_after_substrate` against this build
**Routed by:** `evidence/planning/failure_autopsy_V3-EXQ-779b_2026-07-19.json`
(`targets[0].recommended_substrate_queue_entry`, action `create`, priority 1)

## Problem

`PhasicSurpriseBurst.reset()` cleared the surprise-EMA cold at every episode boundary, and
the first waking tick of an episode can never fire an event -- it *seeds* the baseline
(`event_fired` requires `_ema_initialized`). With `surprise_ema_decay = 0.1` the baseline
has a ~10-tick time constant.

The consequence: **a seed whose episodes are shorter than that time constant never runs
against a converged baseline, so `n_event_ticks` becomes a function of episode LENGTH
rather than of surprise.**

V3-EXQ-779b (`v3_exq_779b_mech063_tonic_phasic_dissociation_20260718T233554Z_v3`) makes this
concrete:

| quantity | value |
|---|---|
| seed 23 mean episode length | ~6.9 steps |
| seeds 29 / 37 mean episode length | 300 steps |
| spread | **43x** |
| `phasic_fires_real_events` (MIN `n_event_ticks` across PHASIC-ON cells) | **6** vs threshold 10 |
| seed 23 budget raised | 835 -> 2400 env steps |
| what the extra budget bought | **345 episodes of ~7**, not longer episodes |
| precondition movement | **none** |

**No step-budget increase can reach this.** The one-parameter budget fix took effect and was
verified (`rollout_stop_reason` `episode_cap -> step_cap`, `rollout_episode_cap_can_bind`
False in all 20 cells), the targeted cell responded (`n_event_ticks` 6 -> 13), and the MIN
simply *migrated* to another short-episode cell (T0P1/seed23, 10 -> 6 despite ~2.85x
exposure). The binding axis is episode length.

**Capability was RULED OUT, not merely unproven.** `burst_level_max = 1.00` in every
PHASIC-ON cell including both seed-23 cells. SD-069 fires at full amplitude; what fails is
the *baseline the event detector compares against*, and the *accounting* that reports the
result.

### Why this is a measurement defect with a governance consequence

The failing gate is a `MIN`-across-cells precondition. A cell that structurally cannot fire
returns a near-zero count that is **indistinguishable from a real low-surprise measurement**,
and the MIN then propagates that starved cell's number as the family's verdict. The autopsy
records the gate as load-bearing and correct to have fired (leave-one-out: the verdict
depends on seed 23) -- so the repair is not to relax the gate but to make the cell able to
report honestly, or to declare itself uninformative.

### Biological divergence

The autopsy's `biological_reference` is explicit: LC-NE baseline adaptation is **continuous
across behavioural episodes**. A baseline that resets at every episode boundary has **no
biological counterpart** and is the proximate defect. The shipped default was the divergence.

## Solution

Two legs, both no-op by default, on `ree-v3/ree_core/regulators/phasic_surprise_burst.py`.

### Leg (a) -- `baseline_continuity`

`PhasicSurpriseBurstConfig.baseline_continuity: str = "reset"`, surfaced as
`REEConfig.phasic_burst_baseline_continuity`.

| value | behaviour |
|---|---|
| `"reset"` (default) | Clear the surprise-EMA at every episode boundary. SD-069 shipping behaviour, retained **bit-identically**. |
| `"carry"` | Preserve `_surprise_ema` and `_ema_initialized` across `reset()`. The envelope, cached temperature delta, and per-episode diagnostics are **still** cleared, so no in-flight burst leaks across a boundary; only the slow baseline persists. |

`"carry"` is the biologically faithful setting. `"reset"` remains the default **only** for
backward compatibility with every run already recorded against SD-069 -- not because it is
the better model. New work should declare `"carry"` deliberately.

A partial-decay `"warm"` mode is **deliberately not built**: a second knob with no question
that needs it. `"carry"` satisfies the autopsy's requirement.

### Leg (b) -- `warmup_ticks`

`PhasicSurpriseBurstConfig.warmup_ticks: int = 0`, surfaced as
`REEConfig.phasic_burst_warmup_ticks`.

| value | meaning |
|---|---|
| `0` (default) | OFF -- no gating, no-op. |
| `-1` | DERIVE as `ceil(3 / surprise_ema_decay)` = three EMA time constants (30 ticks at the default decay 0.1). The sentinel rather than a literal 30 so a future author who retunes the decay gets a correct warmup for free. |
| positive | verbatim tick count. |

Anything below `-1` raises: it is a typo for `-1` and must not silently mean OFF.

Lifetime tick/episode counters survive `reset()` in **both** continuity modes, because
convergence is a question about the regulator's whole history, not the current episode.

**ACCOUNTING ONLY -- it does not suppress the burst.** During warmup the regulator still
fires, still sets the envelope, and still perturbs the softmax temperature exactly as
before. Only the reporting splits.

This was an explicit design decision (user, 2026-07-19). Suppressing the burst during
warmup would change agent **behaviour** in the first ticks of a lifetime, layering a second
mechanism change on top of the continuity fix -- and the MECH-063 (ii) retest would then
confound the two. The defect being repaired is a *measurement* defect, so the gate is a
*measurement* instrument. `tests/contracts/test_sd075_phasic_ema_episode_continuity.py::test_d5_warmup_does_not_suppress_the_burst`
pins this.

### New `get_state()` fields

Config echo (so a manifest reader can tell which regime ran without re-deriving it):
`baseline_continuity`, `warmup_ticks`, `warmup_ticks_derived`.

Lifetime accounting: `lifetime_ticks`, `lifetime_episodes`, `baseline_converged`,
`n_converged_ticks`, `n_prewarmup_ticks`, `n_events_converged`, `n_events_prewarmup`.

`n_events` is retained unchanged for SD-069 continuity but is **per-episode** (cleared by
`reset()`); the lifetime split is the one a consumer should read.

## What a consumer must do

1. Read **`n_events_converged`** as the event count, not `n_events`.
2. Use **`n_converged_ticks`** as its denominator.
3. When `n_converged_ticks` is too small to support the read, declare the cell
   **UNINFORMATIVE** rather than emitting a near-zero count. A `MIN`-across-cells
   precondition otherwise treats a starved cell as a real measurement -- precisely how
   779b was withheld.

## Blast radius

Both fields are no-op by default, so **every existing consumer of `phasic_surprise_burst` is
bit-identical**. Guarded by `tests/test_flag_inertness.py` (SD-069 case) and by SD-075 D1 /
D5b.

Two blast-radius items from the routing brief, both resolved as *no action needed*:

- **`experiments/_lib/probe_warmup.py` `WarmupRecipe` (`probe_max_episodes` 40 vs
  `probe_max_env_steps` 4000), consumed by V3-EXQ-784.** This was **already fixed** by the
  RolloutBudget audit (ree-v3 `6ac2a0d`): `probe_max_episodes = 0` now means DERIVE
  (= `probe_max_env_steps`), the step-denominated form in which the episode cap can never
  bind first. No further change.
- **The warmup cache-key question ("every `WarmupRecipe` field is part of the cache key, so
  changing it invalidates cached warmups -- decide that explicitly").** SD-075 changes **no**
  `WarmupRecipe` field, so the question does not arise in the form posed. Note separately
  that `_warmup_key()` hashes `compute_substrate_hash(scope=None)` -- **the whole
  substrate** -- so *any* `ree_core/` edit busts every cached warmup regardless. That is
  deliberate there ("a false HIT corrupts a conclusion, a false MISS only wastes compute")
  and the resulting bust is benign and unavoidable.

## Live-agent smoke (2026-07-19) -- and a finding the retest author must not miss

25 episodes x 7 steps on seed 23 (the V3-EXQ-779b shape), `instantaneous_pe` source,
untrained agent:

| mode | lifetime ticks | `n_events_converged` | `n_events_prewarmup` |
|---|---|---|---|
| `reset`, `warmup_ticks=0` | 173 | **6** | 0 |
| `carry`, `warmup_ticks=0` | 173 | **12** | 0 |
| `reset`, `warmup_ticks=-1` (30) | 173 | **0** | 6 |
| `carry`, `warmup_ticks=-1` (30) | 173 | **0** | 12 |

Row 1 reproduces the failed precondition **exactly**: 6 events, the same 6 that 779b
reported against a threshold of 10. That is independent confirmation that the diagnosed
mechanism is the one that actually bit.

Row 2 is leg (a) working: identical exposure, 6 -> 12, clearing MIN_EVENT_TICKS = 10.

**Rows 3-4 are the finding.** With the convergence gate on, `n_events_converged` is **0** in
BOTH continuity modes -- every event this cell recorded happened inside the first 30 ticks
of the lifetime. It is not that the gate discards good events; it is that on an untrained
agent the instantaneous-PE stream produces its relative excesses early and then settles, so
by the time the baseline has converged there is nothing left to fire on.

So the two legs **disagree about this cell, and the disagreement is the point**:

- leg (a) alone says *"12 events, passes the threshold"*;
- leg (a) + leg (b) says *"0 events measured against a converged baseline -- UNINFORMATIVE"*.

The autopsy's own target sentence admits both outcomes ("must let a short-episode seed reach
MIN_EVENT_TICKS = 10 on a converged baseline, **or** declare the cell uninformative rather
than reporting a near-zero count"). This build supplies both readings and does not choose
between them, because choosing is a scientific decision for the retest design, not a
substrate default. **A retest that turns on `"carry"` and reads the raw count would be
reporting 12 events that the gate says are all warmup-era.** Turn the gate on, read
`n_events_converged`, and expect that an untrained short-episode cell may honestly have
nothing to report -- which is a different and much more useful failure than "6 vs 10".

### Warmup-rescue spike (2026-07-19) -- the hypothesis above, TESTED

The paragraph that stood here recorded an UNTESTED hypothesis: that the SD-074
`probe_warmup` path might keep the surprise stream producing genuine excesses past tick 30
where the untrained agent does not. **It was tested and it holds.** Diagnostic spike, not an
experiment -- no EXQ, no queue entry; driver `ree-v3/experiments/_scratch/sd075_warmup_rescue_spike.py`.

Method: SD-074 `warm_agent` over `WarmupRecipe.num_episodes` in {0, 10, 40} x seeds
{11, 23, 29}, then a 1200-env-step read with `baseline_continuity="carry"`,
`warmup_ticks=-1` (30), `instantaneous_pe`, 779b env and phasic constants. A FRESH
`PhasicSurpriseBurst` is installed after warmup so the measured lifetime is exactly the read
rollout -- the regulator contributes no `state_dict` keys, so without this a cache-HIT and a
cache-MISS agent would enter the read with different lifetime counters and the read would be
a function of cache state.

| warmup eps | seed | `n_events_converged` | `n_converged_ticks` | event rate | read episodes | mean ep len | `burst_level_max` |
|---|---|---|---|---|---|---|---|
| 0 | 11 | **3** | 116 | 2.6% | 4 | 300.0 | 1.00 |
| 0 | 23 | **1** | 105 | 1.0% | 4 | 300.0 | 1.00 |
| 0 | 29 | **110** | 435 | 25.3% | 52 | 23.1 | 1.00 |
| 10 | 11 | **44** | 305 | 14.4% | 13 | 92.3 | 1.00 |
| 10 | 23 | **65** | 323 | 20.1% | 24 | 50.0 | 1.00 |
| 10 | 29 | **14** | 124 | 11.3% | 4 | 300.0 | 1.00 |
| 40 | 11 | **25** | 194 | 12.9% | 11 | 109.1 | 1.00 |
| 40 | 23 | **87** | 343 | 25.4% | 23 | 52.2 | 1.00 |
| 40 | 29 | **16** | 131 | 12.2% | 6 | 200.0 | 1.00 |

**Both answers the retest author needs:**

1. `n_events_converged` becomes non-zero for a warmed agent -- in every warmed cell.
2. **MIN over the six warmed cells is 14, clearing MIN_EVENT_TICKS = 10.** MIN over the three
   untrained cells is 1. A MIN-across-cells precondition therefore passes on warmed cells and
   fails on untrained ones, which is exactly the axis 779b was blocked on.

**The load-bearing detail is the decoupling, not the raw counts.** Untrained, the converged
count tracks episode COUNT: seeds 11/23 ran 4 x 300-step episodes and yielded 3 and 1, while
seed 29 died in ~23 steps, ran 52 episodes and yielded 110 at 2.1 events per episode. Under
`"carry"` the baseline survives the boundary, so a fresh episode's first ticks compare new-env
surprise against a carried baseline and reliably clear the trigger -- i.e. the untrained
seed-29 count is plausibly BOUNDARY-LOCKED rather than surprise-locked, and should not be read
as the untrained agent doing well. Warmed, that dependence breaks: seed 29 at `num_episodes=10`
ran 4 x 300-step episodes -- the same long-episode shape that gave untrained seeds 1 and 3
events -- and still recorded 14. Per-converged-tick event rate is 1.0-2.6% on untrained
long-episode cells versus 11.3-25.4% across all six warmed cells.

`n_events_prewarmup` falls with training (17/18/16 untrained -> 5/7/3 at 10 episodes), which is
the same finding from the other side: a trained agent no longer dumps its whole surprise excess
into the first 30 ticks.

**Caveats, and they are real.** 3 seeds, one arm, no tonic axis, no fingerprinting -- this is a
spike sized to answer one yes/no question, not evidence for any claim. `num_episodes=40` is not
better than 10 (25 vs 44 on seed 11; 16 vs 14 on seed 29), so there is no monotone
training-dose effect here and 10 episodes suffices for the read; do not read a dose-response
into these numbers. The untrained cells also show that the smoke's `n_events_converged = 0` was
specific to its 25 x 7-step shape rather than a general property of untrained agents -- a longer
read recovers 1-3 events even with no warmup. So the rescue is a genuine training effect on the
event RATE, not merely a longer read.

**Consequence for the retest.** A retest that declares `"carry"` + the convergence gate should
also warm its agents via SD-074 `probe_warmup` (`num_episodes >= 10`), and should install a
fresh regulator post-warmup for the reason given above. Without warmup, a long-episode seed
will honestly report an uninformative cell.

## MECH-094

`simulation_mode=True` continues to advance nothing -- now explicitly including the SD-075
lifetime counters. Replay / DMN content must not accrue toward waking baseline convergence.
Pinned by D7.

## Contracts

`ree-v3/tests/contracts/test_sd075_phasic_ema_episode_continuity.py` (22 tests, D1-D9):

| id | contract |
|---|---|
| D1 | defaults are a no-op; SD-069 `reset()` semantics survive verbatim |
| D2 | `"carry"` preserves the baseline while still clearing the envelope, delta, and per-episode diagnostics |
| D2b | under `"reset"` the first tick of an episode can never fire; `"carry"` removes that |
| D3 | **the defect itself** -- identical exposure, `"reset"` recovers 0 events where `"carry"` recovers many |
| D3b | 779b in miniature: tripling the budget as more short episodes does not change the per-episode yield, on both an early-spike (yield 0) and a late-spike (yield capped at 1/episode) shape |
| D4 | `warmup_ticks` resolution: `-1` derives from the decay, positive verbatim, `0` off |
| D4b | convergence flips exactly at the boundary tick |
| D5 | the gate is accounting-only -- `burst_level` and `temperature_delta` identical tick-by-tick with and without it |
| D5b | agent-level: the action stream is unchanged by `warmup_ticks` |
| D6 | the split partitions the totals (parametrised over both modes x 4 warmup values) |
| D7 | MECH-094 -- simulation mode advances no lifetime counter |
| D8 | input validation on both fields |
| D9 | agent-level wiring; `agent.reset()` respects `"carry"` |

Regression: SD-069's own 8 contracts and `tests/test_flag_inertness.py` pass unchanged.

## Retest

MECH-063 sub-claim (ii) is `pending_retest_after_substrate` against this build.

**The re-derive brake fired both halves on this claim** (3rd MECH-063 autopsy) and explicitly
refuses another lettered iteration of the tonic/phasic probe against the current regulator.
**Do NOT queue a V3-EXQ-779c.** A redesign of a *different* mechanism under a new EXQ number
remains permitted. Any retest must declare `phasic_burst_baseline_continuity="carry"` and a
convergence gate, and must consume `n_events_converged` with an uninformative-cell path
rather than feeding a raw MIN.
