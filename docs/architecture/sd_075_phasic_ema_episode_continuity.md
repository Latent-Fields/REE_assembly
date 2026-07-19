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

This also means the SD-074 `probe_warmup` path (train the agent before measuring) is
plausibly complementary rather than redundant here: a trained agent's surprise stream may
keep producing genuine excesses past tick 30, where this untrained one does not. That is a
hypothesis, not a finding -- it is untested and must not be cited as evidence.

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
