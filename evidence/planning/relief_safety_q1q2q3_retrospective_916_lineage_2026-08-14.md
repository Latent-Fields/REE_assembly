# Relief / Safety Retrospective — V3-EXQ-916 & V3-EXQ-916a (Q1 / Q2 / Q3)

**Date:** 2026-08-14
**Session:** `metaworker-chip-20260812-relief-safety-q1q2q3-retrospective` (headless dispatch chip)
**Chip:** `chip-20260812-relief-safety-q1q2q3-retrospective`
**Status:** retrospective DATA analysis. **This is NOT a `/failure-autopsy`.** No REE /
mechanism / measure / environment failure localization verdict is issued here, and nothing
below adjudicates the two runs' outstanding `relief_safety_showcase_channels_live`
self-route. Both runs remain awaiting a CONFIRMED autopsy on `/governance`'s own worklist.
This document is intended as *input* to that autopsy, not a substitute for it.

**Sources (all read at `origin/master`; nothing re-executed):**

| Artifact | Path |
|---|---|
| 916 manifest | `evidence/experiments/v3_exq_916_relief_safety_fishtank_showcase_20260811T064913Z_v3.json` |
| 916 episode log | `evidence/experiments/v3_exq_916_relief_safety_fishtank_showcase/v3_exq_916_relief_safety_fishtank_showcase_20260811T064913Z_episode_log.json` |
| 916a manifest | `evidence/experiments/v3_exq_916a_relief_safety_fishtank_showcase_20260811T194142Z_v3.json` |
| 916a episode log | `evidence/experiments/v3_exq_916a_relief_safety_fishtank_showcase/v3_exq_916a_relief_safety_fishtank_showcase_20260811T194142Z_episode_log.json` |
| drivers | `ree-v3/experiments/v3_exq_916{,a}_relief_safety_fishtank_showcase.py` (`origin/main`) |
| MECH-302 | `ree-v3/ree_core/comparator/suffering_derivative_comparator.py` |
| MECH-304 | `ree-v3/ree_core/safety/conditioned_safety_store.py` |
| gates | `ree-v3/ree_core/agent.py` ~5120, ~6286-6367 |

---

## 0. Headline

| Question | Answer | Strength |
|---|---|---|
| **Q1** — was relief computationally sensible? | **YES**, with two structural caveats (no refractory period; the `min_initial_norm` guard is inert in this config) | Strong for the 6 independent events observed; the effective n is **6**, not 60 |
| **Q2** — did the world become less harmful afterwards? | **YES for realized harm events and health; NO for hazard geometry** | Moderate — a large episode-selection confound is only partly removed by matching |
| **Q3** — did REE infer *safety*, and was it justified? | **The inference is NOT justified as an inference**, even though its value happened to be locally accurate about hazards | Strong and mechanistic — the signal is a two-valued irreversible latch, not a state read |

The combination the chip anticipated is what the data shows: **relief detection is valid; the
safety inference built on top of it is structurally incapable of being an inference.** Q1's
answer is not weakened by Q3's, and Q3's failure is not a defect in MECH-302.

One finding beyond the chip's framing: the Q3 failure mode here is **not** "felt safe while
next to a hazard" (that never happened — 0/465 high-cue steps were within 2 cells of a
hazard). It is **"felt maximally and irreversibly safe while starving to death"** — 2 of the
4 episodes in which the safety cue latched high ended in death with the cue still pinned at
its maximum.

---

## 1. Data inventory and what is actually logged

Both runs log **1013 eval steps** across **15 episodes** (3 seeds x 5 episodes; episodes
terminate early on death, so lengths are 9-200). Per-step channels present:

`t, pos, action, harm_signal, z_harm_norm, z_harm_s, z_harm_un, z_harm_a, z_world_norm,
z_beta_val, world_change_norm, drive, z_goal, vigor, override, z_block, freeze, excite,
dread, surprise, residue_wanting, liking, relief_event, safety_cue_signal,
safety_terrain_read, mode, transition_type, health, energy, harm_event, n_cands, hazards,
resources, in_reef`

**Channels the chip asked for that ARE present:** current `z_harm_a` (and therefore its
recent history and derivative, reconstructable exactly), `harm_event`, `health` (and slope),
hazard positions + agent position (so hazard distance/exposure is exact), reef/context
identity (`in_reef`, `reef_cells`, `mode`, `transition_type`), current action, full
trajectory, safety cue (MECH-304 `safety_cue_signal`), contextual safety (MECH-303
`safety_terrain_read`), subsequent behaviour, and later-realized harm at arbitrary lags.

**Channels the chip asked for that are NOT present — stated rather than proxied:**

1. **No predicted-harm / threat-prediction variable.** There is no E1/E2/E3 predictive
   readout, no trajectory-evaluation score, no expected-harm scalar, and no per-candidate
   value in either episode log. `n_cands` is a count (constant 32 throughout), not an
   evaluation. `dread` (MECH-307 split-surprise, negative pole) is the *closest* thing and
   is reported below **as an affect channel, explicitly not as a harm prediction** — it is a
   surprise decomposition, not a forward model output. **Nothing in this document treats
   `dread` as a predicted-harm proxy.**
2. **No per-step energy/health *decrement* accounting**, so "why did health fall" must be
   inferred from `harm_event` + `energy` rather than read directly.
3. **`liking` is logged but is the unbounded VALENCE_LIKING accumulator** flagged by
   SD-RESIDUE-VALENCE-BOUND; the drivers' own KNOWN LIMITATION block says so. It is not used
   as a measure anywhere below.

### 1a. 916 vs 916a are the SAME trajectory

Step-by-step comparison of all 1013 steps: `pos`, `action`, `z_harm_a`, `relief_event`,
`health`, `energy`, `harm_event`, `mode`, `hazards`, `resources`, `in_reef` are
**bit-identical** between the two runs. Only readout channels differ, at these counts:
`residue_wanting` 1013, `dread` 838, `excite` 781, `world_change_norm` 772,
`surprise` 757, `safety_cue_signal` 462, `z_world_norm` 167, `z_goal` 97.

So 916a's `residue_wanting` writer fix and `tonic_5ht_enabled=True` **did not change
behaviour at all** in this configuration. Q1 and Q2 below are therefore *identical* for the
two runs and are reported once. Q3 was recomputed separately for each; the `safety_cue_signal`
differences are in the 3rd-4th decimal and change no conclusion (both runs give the same
histogram, the same latch structure, and the same implied cosine range).

---

## 2. Q1 — was relief computationally sensible?

### 2a. What MECH-302 is *supposed* to detect (read from the implementation, not the name)

`SufferingDerivativeComparator.tick()` (`ree_core/comparator/suffering_derivative_comparator.py`)
is 20 lines of pure arithmetic. It keeps a rolling buffer of the **`z_harm_a` norm** of
length `window_length`, and fires iff:

```
len(buffer) == window_length
AND buffer[0] >= min_initial_norm
AND (buffer[0] - buffer[-1]) >= drop_threshold
```

The 916 drivers leave all three at `REEConfig` defaults: `suffering_window_length=5`,
`suffering_drop_threshold=0.10`, `suffering_min_initial_norm=0.05`. There is **no refractory
period** and the buffer slides by one each tick.

So the substrate's intent is: *"the chronic affective-harm accumulator has sustained a
downward crossing of 0.10 over the last 5 waking ticks, from a starting level that was not
already quiet."*

### 2b. Replay verification — the logged channel IS the comparator input

Recomputing the predicate above directly from the logged `z_harm_a` series, with the buffer
reset at each episode boundary:

```
tp 60   fp 0   fn 0   tn 953
```

Exact agreement on all 1013 steps, both runs. (Without the per-episode reset: `fp 8` —
confirming the agent *does* reset the comparator between episodes, as `agent.reset()` does.)
This is the load-bearing check for everything that follows: the analysis is operating on the
same scalar the mechanism operates on, and the config defaults are confirmed empirically
rather than assumed.

### 2c. The drop is small relative to the channel — but it is NOT noise

| quantity | value |
|---|---|
| `z_harm_a` over all 1013 eval steps | mean 7.396, sd 1.403, range 5.216 – 9.955 |
| all eligible 5-step drops `z[t-4]-z[t]` | mean 0.0061, sd 0.0864 |
| fraction of ALL 5-step windows meeting `drop >= 0.10` | 60/953 = **6.3%** |
| relief-event drops (n=60) | mean 0.1468, sd 0.0403, range 0.1011 – 0.2565 |
| ... in `z_harm_a` SD units | mean **0.105 SD**, min 0.072 SD |
| ... as a fraction of the level at window start | mean **1.65%** |

A 0.10 threshold against a channel with mean ~7.4 is a **1.3% relative change**. Taken alone
that looks like a threshold set for a channel that does not exist here, and it is the single
most legitimate reason to suspect noise-firing.

Three tests say it is not noise:

**(i) Persistence — the improvement never reverts.** For every relief event, comparing the
level at window start (`z_pre`) to the level at forward lags:

| lag | n | mean `z_lag` | mean (`z_pre` - `z_lag`) | fraction still below `z_pre` |
|---|---|---|---|---|
| +1 | 60 | 8.731 | 0.182 | **1.000** |
| +2 | 60 | 8.697 | 0.215 | **1.000** |
| +5 | 60 | 8.599 | 0.313 | **1.000** |
| +10 | 60 | 8.450 | 0.462 | **1.000** |
| +20 | 60 | 8.186 | **0.727** | **1.000** |

Zero reversion at any lag, and the gap **widens monotonically** to 5x the firing threshold by
+20 steps. A noise-triggered detector on a mean-reverting channel would show partial return;
this shows none in 60/60 cases.

**(ii) Idle decay alone is insufficient.** On quiescent steps (no `harm_event` at t or t-1)
the mean per-step change in `z_harm_a` is **-0.0049**, i.e. **-0.0243 over 5 steps** — only
about **one quarter** of the 0.10 threshold. Sitting still does not fire the comparator; a
fire requires roughly 4x the background decay rate. (`z_harm_a` decreases on 63.6% of all
step transitions, 69.2% of no-harm-event transitions, so descent is common but slow.)

**(iii) Fires follow real harm, in the right context.** All 6 burst onsets occurred with
`in_reef=True`, `mode='shelter'`, and 1-7 `harm_event`s in the preceding 10 steps:

| seed | ep | t | burst len | `z_pre` | `z_now` | drop | health | min haz dist | in_reef | harm events in prior 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 4 | 15 | 9.955 | 9.782 | 0.174 | 0.605 | 4 | True | 4 |
| 0 | 0 | 21 | 29 | 9.334 | 9.211 | 0.123 | 0.537 | 4 | True | 1 |
| 0 | 2 | 100 | 6 | 9.252 | 9.140 | 0.111 | 0.036 | 5 | True | 2 |
| 0 | 3 | 29 | 2 | 9.051 | 8.943 | 0.108 | 0.501 | 5 | True | 2 |
| 0 | 3 | 47 | 6 | 8.691 | 8.584 | 0.107 | 0.439 | 6 | True | 1 |
| 2 | 2 | 21 | 2 | 5.676 | 5.572 | 0.104 | 0.294 | 5 | True | 7 |

Context contrast at fire steps vs all other steps: `harm_event` rate **0.033 vs 0.158**,
`in_reef` **1.000 vs 0.707**, health **0.460 vs 0.373**, `dread` **0.408 vs 1.075**.

This is exactly the intended semantics — the agent has been hurt, has reached shelter, and
the chronic accumulator is coming down.

### 2d. Two structural caveats that DO weaken the number 60

**(1) No refractory period: 60 fires are 6 events.** The 60 relief-event steps occur in **6
contiguous bursts**, of lengths **29, 15, 6, 6, 2, 2**. Because the window slides one tick at
a time with no lockout, a single sustained descent re-fires on every tick it remains
qualifying. **44 of the 60 fires are 2 bursts.** Any statistic quoting `total_relief_fires:
60` (as both manifests and both summaries do) is quoting a **duration measure dressed as a
count**, inflated roughly 10x relative to independent events. The 6 events are also
distributed 5 in seed 0 and 1 in seed 2, with seed 1 contributing none — consistent with the
manifest's own per-seed table (58 / 0 / 2).

**(2) The `min_initial_norm` guard is inert.** Its purpose per the docstring is to "prevent
spurious fires on a stream that is already quiet". Its default is 0.05; the observed
`z_harm_a` floor across the whole run is **5.216**, i.e. **104x higher**. The guard can never
fire in this config and is effectively dead code here. This is the *mirror image* of the
MECH-303 threshold-unreachability the drivers already document (`contextual_safety_harm_threshold=0.05`
against the same channel, where the gate can never *open*): the same 0.05 default, on the
same scale mismatch, disables one guard and permanently satisfies another. Worth surfacing to
whoever eventually owns the MECH-303 threshold reachability work as a shared root cause
(SD-011 `z_harm_a` scale), not two separate config bugs.

### 2e. Q1 verdict

**Relief was computationally sensible.** It fired on a real, sustained, never-reverting
decline in the exact scalar the mechanism is specified to monitor, following actual recent
harm, at a rate (6.3% of eligible windows) well above what idle decay produces and well below
"always on". It is not firing on noise and it is not firing on trivial decay.

Caveats to carry forward: **n_effective = 6, not 60**; 5 of the 6 events are in one seed; the
threshold is a small fraction of the channel's range so the margin is thin; and one of the
comparator's two guards is inoperative in this configuration.

---

## 3. Q2 — did the world subsequently become less harmful?

This section is deliberately **ecological only**: it reads realized outcomes from the
environment side and says nothing about what REE believed.

### 3a. Forward outcome windows after relief steps

| metric | window | after relief | after all other steps | diff |
|---|---|---|---|---|
| `harm_event` rate | +1..+1 | 0.0167 | 0.1471 | **-0.131** |
| | +1..+5 | 0.0300 | 0.1430 | **-0.113** |
| | +1..+10 | 0.0317 | 0.1349 | **-0.103** |
| | +1..+20 | 0.0317 | 0.1301 | **-0.098** |
| `harm_signal` | +1..+10 | -0.0021 | -0.0140 | +0.012 |
| min hazard dist | +1..+5 | 4.347 | 4.177 | +0.170 |
| | +1..+20 | 4.295 | 4.263 | +0.032 |
| `health` | +1..+10 | 0.4485 | 0.3307 | +0.118 |
| | +1..+20 | 0.4369 | 0.3165 | +0.120 |

### 3b. `z_harm_a`-matched control

Comparing relief steps against non-relief steps whose `z_harm_a` is within +/-0.25 (n=646),
to remove the "relief only happens at particular accumulator levels" confound:

| metric | window | relief (n=60) | matched (n=646) | diff |
|---|---|---|---|---|
| `harm_event` rate | +1..+5 | 0.0300 | 0.1260 | **-0.096** |
| | +1..+20 | 0.0317 | 0.1150 | **-0.083** |
| min hazard dist | +1..+5 | 4.347 | 4.335 | **+0.012** |
| | +1..+20 | 4.295 | 4.399 | **-0.104** |
| health | +1..+20 | 0.4369 | 0.3179 | +0.119 |

**The harm-event reduction survives matching; the hazard-distance effect does not.** After
relief, the agent is not further from hazards than a level-matched control — at +20 it is
marginally *closer*. What changes is the rate at which harm is actually incurred, not the
geometry of exposure. That dissociation matters for Q3: the world did not become
*structurally* safer, the agent stopped being hit.

### 3c. The dominant confound, stated rather than adjusted away

Relief fired in **4 of 15 episodes**. Those 4 are the long ones:

| group | n | mean length | survived to the 200-step cap | mean `harm_event` rate |
|---|---|---|---|---|
| episodes with >=1 relief | 4 | **154.8** | **2** | 0.114 |
| episodes with no relief | 11 | **35.8** | **0** | 0.557 |

Both surviving episodes in the entire run are relief episodes. So a substantial part of
"after relief, harm is lower" is **"relief happened in the episodes that were going well"** —
the arrow of that association is not identified by this data. Two partial mitigations:

- The `z_harm_a`-matched control above still shows a ~4x gap.
- Restricting the comparison to *within relief-containing episodes only* (§4d) still shows
  0.123 vs 0.026.

Neither is a causal identification. **Q2's honest form is: after relief fires, realized harm
is 3-5x lower and health is materially higher over the next 1-20 steps, and this is not
fully explained by the accumulator level; but it is substantially entangled with episode
quality, and the mechanism visible in the trajectories is "the agent is parked in the reef",
not "relief made the world safer".**

### 3d. Episode-level table

| seed | ep | len | relief fires | final health | ended in death |
|---|---|---|---|---|---|
| 0 | 0 | 200 | 44 | 0.471 | no (cap) |
| 0 | 1 | 10 | 0 | 0.000 | yes |
| 0 | 2 | 175 | 6 | 0.000 | **yes** |
| 0 | 3 | 200 | 8 | 0.439 | no (cap) |
| 0 | 4 | 10 | 0 | 0.000 | yes |
| 1 | 0-4 | 9-140 | 0 | 0.000 | yes (all 5) |
| 2 | 0 | 10 | 0 | 0.000 | yes |
| 2 | 1 | 74 | 0 | 0.000 | yes |
| 2 | 2 | 44 | 2 | 0.000 | **yes** |
| 2 | 3 | 22 | 0 | 0.000 | yes |
| 2 | 4 | 36 | 0 | 0.000 | yes |

13 of 15 episodes end in death. **2 of the 4 relief episodes also end in death** — relief is
not a marker of eventual survival.

### 3e. Q2 verdict

**Partly yes.** Realized harm events fall sharply and durably after relief; health is higher
and stays higher. But hazard exposure is unchanged, half the relief episodes still end in
death, and the effect is entangled with a strong episode-selection confound that this data
cannot resolve. **Q2 does not license "the world became safe".**

---

## 4. Q3 — did REE infer SAFETY, and was that inference justified?

### 4a. MECH-303 (contextual safety terrain) contributed nothing

`safety_terrain_read` takes **exactly one distinct value, 0.0, across all 1013 steps** in both
runs. The manifests record this as `chan_nondegen_safety_terrain_read: 0.0`.

This is already explained and already owned. The 916 drivers carry a KNOWN LIMITATION block
attributing it to `contextual_safety_harm_threshold=0.05` being ~100x below the live
`z_harm_a` norm, so `accumulate_safety()` is never invoked; the full investigation is
`evidence/planning/mech303_contextual_safety_threshold_reachability.md`. **This retrospective
neither re-investigates nor re-litigates that**, and it does not touch the separate
chance-level-AUC question that `chip-20260812-mech303-sourcing-mode-reconciliation` owns.

**Cross-evidence offered to that chip, not duplicating its work:** the failure observed here
is *upstream* of any AUC — the channel is not near-chance, it is **identically zero and never
computed**. So this run is not usable as an instance of the chance-level-AUC phenomenon; it
is the reachability failure, in a live agent-path driver, with the numeric threshold ratio
measured directly (`z_harm_a` floor 5.216 vs threshold 0.05 = **104x**). If that chip needs a
live-driver datapoint for the reachability half, this is one.

**Consequence for Q3:** the *contextual* safety inference did not occur at all. Everything
below concerns MECH-304 only.

### 4b. MECH-304's `safety_cue_signal` is a two-valued irreversible latch

Histogram over all 1013 steps, both runs (10 equal bins on [0,1]):

```
[0.0,0.1)  548        [0.1,0.2) 0   [0.2,0.3) 0   [0.3,0.4) 0   [0.4,0.5) 0
[0.5,0.6)  0          [0.6,0.7) 0   [0.7,0.8) 0   [0.8,0.9) 0   [0.9,1.0) 465
```

Nonzero values: n=465, **mean 0.9818, sd 0.0007, range 0.9775 – 0.9820**. There is not a
single value between 0.0 and 0.9775.

**Latch test — once high, never low again.** In all 4 episodes where the cue exceeded 0.5, the
number of subsequent steps at or below 0.5 is **0**:

| seed | ep | len | first >0.5 at | steps latched | value range after latch | final health | died while latched |
|---|---|---|---|---|---|---|---|
| 0 | 0 | 200 | i=4 | 196 | 0.9806 – 0.9820 | 0.471 | no |
| 0 | 2 | 175 | i=100 | 75 | 0.9817 – 0.9820 | 0.000 | **yes** |
| 0 | 3 | 200 | i=29 | 171 | 0.9800 – 0.9820 | 0.439 | no |
| 2 | 2 | 44 | i=21 | 23 | 0.9775 – 0.9820 | 0.000 | **yes** |

The cue goes high on the **first relief event of the episode** in all 4 cases (0 steps of
nonzero cue precede the first relief fire in any episode), and never returns.

### 4c. Why — the readout is saturated, and it is measurable

`ConditionedSafetyStore._query()` returns `sigmoid(gain * cos_sim)` with `gain=4.0`
(`ree_core/safety/conditioned_safety_store.py`). Inverting that on the observed values:

```
implied cos(z_world, prototype)  range 0.9423 .. 1.0000,  mean 0.9974
```

**The cosine between the current world latent and the stored prototype is pinned at ~1.0 at
every step of every latched episode.** The store is therefore not discriminating world
states; it is reporting "a prototype exists". The mechanism has a designed fix for exactly
this — SD-066 `safety_store_centered=True`, which subtracts a running common-mode baseline so
the cue-carrying residual can dominate the raw cosine, with the docstring naming SD-008
`z_world` under-differentiation as the reason it is needed. The 916 drivers leave
`safety_store_centered` at its default **False**.

**And the gate consequence is not cosmetic.** `agent.py` ~6317 releases the avoidance
commitment when `_conditioned_safety_signal > safety_store_threshold` (default **0.5**) and
`beta_gate.is_elevated`. Observed value 0.982 is permanently above 0.5. So from the first
relief event onward, **the MECH-304 IL->CeA expression pathway fires on every tick with an
elevated beta gate, for the rest of the episode**, and writes VALENCE_LIKING each time. The
"expression pathway" is effectively wired open rather than gated.

### 4d. Was the inference justified by outcome?

Two answers, and they differ, which is the point.

**Locally about hazards: yes, and strikingly so.**

| group | n | fwd(+1..+10) `harm_event` rate | fwd min hazard dist | mean health |
|---|---|---|---|---|
| cue == 0 | 537 | 0.2172 | 3.851 | — |
| cue > 0.5 | 461 | **0.0256** | 4.644 | — |
| in_reef & cue == 0 | 265 | 0.1493 | 4.354 | 0.188 |
| in_reef & cue > 0.5 | 461 | 0.0256 | 4.644 | 0.387 |
| not in_reef & cue == 0 | 272 | 0.2832 | 3.361 | 0.567 |
| not in_reef & cue > 0.5 | **0** | — | — | — |

- `spearman(cue, forward harm_event rate) = -0.441`; `spearman(cue, forward min hazard dist) = +0.296`.
- **cue > 0.5 AND min hazard dist <= 2: 0 / 465.** The agent was never within 2 cells of a
  hazard while the cue was high.
- cue > 0.5 AND `harm_event` this step: 8/465 = 0.017.
- Restricted to relief-containing episodes only (removing the episode-selection confound):
  cue==0 gives 0.123, cue>0.5 gives 0.026 — the gap survives.

**As an inference: no.** Three reasons, in increasing order of severity:

1. **`cue > 0.5` is a strict subset of `in_reef`** (461/461, and `not in_reef & cue > 0.5` is
   empty). The conditional row above is not a clean test of incremental information, because
   the `in_reef & cue==0` group is dominated by *pre-latch* steps early in episodes and has
   very different health (0.188 vs 0.387). The cue adds nothing observable over "the agent is
   in the reef and has been there a while".
2. **A signal with two values that never decreases cannot be tracking the current world.**
   Its correlation with outcome is fully accounted for by the fact that it is a one-way
   function of "has relief ever fired in this episode", which is itself a function of "did the
   agent reach the reef" — the same variable that produces the low harm rate. The predictive
   validity is inherited, not earned.
3. **It is blind to the mortality channel that actually killed the organism.**
   **77/465 = 16.6% of high-cue steps had health < 0.2**, and 2 of the 4 latched episodes
   ended in death with the cue still at maximum. The trajectories are unambiguous:

```
seed 0 ep 2:  t=163..173  pos=[1,1]  cue=0.982  health=0.036  energy=0.000  minhaz=5-6  in_reef=True  mode=shelter
              t=174       pos=[1,1]  cue=0.982  health=0.000  energy=0.000  harm_event=True   <- death
seed 2 ep 2:  t=32..41    pos=[1,10] cue=0.978  health=0.224  energy=0.71->0.62  minhaz=5  mode=freeze
              t=42        health=0.154  harm_event=True
              t=43        health=0.000  cue=0.982                                          <- death
```

The safety signal is at its maximum for the eleven consecutive steps in which the organism
sits motionless at zero energy and then dies. **This is the Q3 failure mode the chip
anticipated, in its concrete form: relief detection valid (Q1), the world genuinely not safe
in the way that mattered (Q2's hazard-geometry null and the death outcomes), and the safety
inference nonetheless pinned at maximum and irreversible.**

### 4e. Behaviour after relief — reported, with a negative control that blocks the obvious causal reading

Post-relief behaviour is extremely narrow. In the +1..+10 window after a burst onset the mode
distribution is **shelter 0.983 / freeze 0.017**, against a global **shelter 0.610 / avoid
0.215 / freeze 0.174 / explore 0.001**. Every one of the 60 relief steps is `mode='shelter'`
and `in_reef=True`. Movement essentially ceases after the latch:

| seed | ep | latch at | movement rate pre-latch | movement rate post-latch |
|---|---|---|---|---|
| 0 | 0 | i=4 | 3/3 = 1.000 | **2/195 = 0.010** |
| 0 | 2 | i=100 | 11/99 = 0.111 | **0/74 = 0.000** |
| 0 | 3 | i=29 | 5/28 = 0.179 | **1/170 = 0.006** |
| 2 | 2 | i=21 | 9/20 = 0.450 | **0/22 = 0.000** |

Energy falls to 0.000 by episode end in 3 of those 4. Mean energy is **0.310 in-reef vs 0.791
out-of-reef**: reef occupancy is energetically costly, and the agent stops leaving.

**Do not read this as "the safety latch caused the parking."** Two things block that:

- **Negative control:** `seed 2 ep 1` has **no relief, no latch, and a movement rate of
  0/73 = 0.000** — total immobility with the safety pathway never engaged. `seed 1 ep 2`
  is 8/139 = 0.058. Immobility is a pre-existing property of this driver/config, not
  something the latch introduces.
- **Phase confound:** the pre-latch windows are short and early-episode, when the agent is
  still travelling toward the reef, so a pre/post movement comparison is partly a
  travelling/arrived comparison.
- **Direction:** mechanistically, MECH-304's gate *releases* the avoidance commitment, which
  should if anything *increase* mobility. A causal story that ends in reduced mobility does
  not follow from the gate's own semantics and would need its own test.

What can be said without overreach: **the safety signal endorses, at maximum and
irreversibly, a behavioural state that ends in death half the time**, whether or not it
caused that state.

### 4f. Q3 verdict

**REE did infer safety — via MECH-304 only, MECH-303 never engaged — and the inference is not
justified as an inference.** Its value happened to be locally accurate about hazard proximity
(0/465 high-cue steps within 2 cells of a hazard), but the signal is a two-valued,
never-decreasing latch whose implied cosine is saturated at ~1.0, whose correlation with
outcome is inherited from "the agent reached the reef", and which remained at maximum through
16.6% of steps with health < 0.2 and through two deaths.

**The Q1/Q3 combination is real and is the reportable finding:** relief is valid, safety is
premature. Q3's failure does not retroactively invalidate Q1.

---

## 5. Confounds and non-degeneracy — consolidated

| # | Confound / limitation | Effect | Handled how |
|---|---|---|---|
| C1 | **Pseudo-replication.** 60 relief fires = 6 contiguous bursts (29/15/6/6/2/2), no refractory period | Any per-fire statistic is ~10x over-weighted; the manifest's `total_relief_fires: 60` is a duration, not a count | Reported throughout; n_effective stated as **6** |
| C2 | **Seed concentration.** 5 of 6 bursts in seed 0; seed 1 has none | Cross-seed generality of every Q1/Q2 result is untested | Stated; not adjusted |
| C3 | **Episode selection.** Relief occurs only in the 4 long episodes (mean 154.8 vs 35.8 steps), including both survivors | Inflates every "after relief the world is better" contrast | Partly addressed by the `z_harm_a`-matched control and the within-relief-episode restriction; **not** resolved |
| C4 | **`cue > 0.5` is a strict subset of `in_reef`** (461/461) | MECH-304's apparent predictive validity is not separable from reef occupancy | Stated; conditional table given but explicitly labelled not-clean |
| C5 | **MECH-303 channel identically zero** (`chan_nondegen_safety_terrain_read: 0.0`) | Contextual safety contributes nothing; Q3 is a MECH-304-only result | Cross-referenced to the existing reachability investigation; not re-derived |
| C6 | **`vigor` and `z_block` also flat** (`chan_nondegen_*: 0.0` in both manifests) | Two more channels the run cannot speak to | Not used anywhere above |
| C7 | **No predicted-harm channel exists in the logs** | The chip's "predicted-harm / threat-prediction variable" alignment could not be done | Stated in §1; `dread` explicitly NOT substituted |
| C8 | **Diagnostic showcase, not a designed test.** `experiment_purpose: diagnostic`, `claim_ids: []`, `evidence_direction: non_contributory`; PASS criteria are channel non-degeneracy only | Nothing here is claim-scoring evidence | This document scores no claim |
| C9 | **Descriptive statistics only.** No significance testing, no CIs | With n_eff=6 events, formal inference would be misleading | Deliberate; all comparisons are point estimates with n shown |
| C10 | **916 and 916a share one trajectory** | The two runs are one behavioural sample, not two | Established in §1a |

**Non-degeneracy of the channels this analysis actually relies on** (max std across seeds,
from the manifests): `z_harm_a` 0.665, `safety_cue_signal` 0.429, `dread` 0.762, `drive`
0.365, `override` 0.242 — all non-degenerate. `z_goal` 0.000 in 916 / 0.078 in 916a; `vigor`,
`z_block`, `safety_terrain_read` all 0.000 and unused here.

---

## 6. What this document does NOT establish

- It does **not** localize failure (REE / mechanism / measure / environment). That is the
  pending `/failure-autopsy`'s job for both runs.
- It does **not** establish that relief *causes* lower subsequent harm (C3).
- It does **not** establish that the safety latch *causes* immobility or death (§4e negative
  control).
- It does **not** re-open, re-derive, or contradict the MECH-303 threshold-reachability
  investigation, and it makes no claim about the MECH-303 chance-level-AUC question owned by
  `chip-20260812-mech303-sourcing-mode-reconciliation`.
- It does **not** score any claim. Both runs are `non_contributory` diagnostics.
- It draws **nothing** from the Fishtank visualisation; every number above is computed from
  the episode-log JSON.

---

## 7. Observations a future autopsy or governance cycle may want (offered, not actioned)

Listed as observations only; this chip did not act on any of them and did not spawn chips for
them, since the two runs' disposition sits with `/failure-autopsy` and `/governance`.

1. **`total_relief_fires` is a duration, not a count.** Both manifests and both
   `summary_markdown` blocks report 60; the independent-event count is 6. Any downstream
   reader comparing "relief fires" across runs is comparing burst durations.
2. **The 0.05 default appears twice against the same `z_harm_a` scale with opposite
   effects** — `suffering_min_initial_norm` (guard permanently satisfied, inert) and
   `contextual_safety_harm_threshold` (gate permanently shut). One SD-011 scale mismatch,
   two symptoms.
3. **`safety_store_centered` (SD-066) is the named fix for exactly the saturation measured in
   §4c** and is off in this driver. A re-run of 916a with `safety_store_centered=True` would
   be a direct test of whether `safety_cue_signal` can be made state-discriminative at all in
   the Fishtank config — and would answer whether the latch is a config artifact or a
   substrate property.
4. **The MECH-304 release gate is effectively unconditional once seeded** (0.982 vs threshold
   0.5, permanently). Whether the expression pathway should have a decay, a refractory, or a
   re-arming condition is a substrate design question, not a driver question.
5. **The organism-review Section 6 concern is instantiated here in a specific form** worth
   naming precisely: not "safe belief next to a hazard", but "maximal safe belief while
   energy-starved and immobile". A safety signal keyed only on the aversive-harm derivative
   is structurally blind to the non-hazard mortality channel.

---

## 8. Reproduction

```
git -C REE_assembly show origin/master:evidence/experiments/v3_exq_916_relief_safety_fishtank_showcase/v3_exq_916_relief_safety_fishtank_showcase_20260811T064913Z_episode_log.json
git -C REE_assembly show origin/master:evidence/experiments/v3_exq_916a_relief_safety_fishtank_showcase/v3_exq_916a_relief_safety_fishtank_showcase_20260811T194142Z_episode_log.json
```

Every figure above is derived from those two files plus the four source files listed in the
header. The comparator replay in §2b is the reproducible check that anchors the rest: recompute
`buffer[0] - buffer[-1] >= 0.10` over a 5-long sliding window of the logged `z_harm_a`, reset
per episode, and it reproduces `relief_event` exactly (60 tp, 0 fp, 0 fn, 953 tn).

## Decision log

- **Kept Q1, Q2, Q3 answers independent, as instructed.** Q1 is answered from the comparator's
  own specification and the `z_harm_a` series alone; Q2 from environment-side outcomes alone;
  Q3 from the safety channels and their gates. Q2's partial failure and Q3's failure are not
  propagated backwards into Q1.
- **Did not substitute `dread` for the missing predicted-harm channel.** The chip explicitly
  asked for the gap to be named rather than proxied. `dread` is reported only as an affect
  contrast in §2c.
- **Did not run `/failure-autopsy`** and issued no failure-localization verdict, per the chip
  and per CLAUDE.md's chip-vs-report-inline rule.
- **Did not investigate the MECH-303 chance-level-AUC question**, which belongs to
  `chip-20260812-mech303-sourcing-mode-reconciliation`; offered §4a as cross-evidence for the
  distinct reachability half instead.
- **Reported the movement/immobility association with its negative control rather than
  omitting it.** Omitting it would hide the most behaviourally striking pattern in the run;
  reporting it without `seed 2 ep 1` would have licensed a causal claim the data does not
  support.
