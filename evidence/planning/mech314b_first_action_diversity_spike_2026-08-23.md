# Spike: is candidate-pool first-action diversity raisable? (MECH-314b ceiling)

**Date:** 2026-08-23T05:42:01Z
**Chip:** chip-20260823-firstaction-diversity-spike
**Type:** `complex (probe-gated)` diagnostic spike, not a build.
**Verdict up front: YES, trivially. Diversity is governed by one config knob
(`support_preserving_min_first_action_classes`), hardcoded to its own floor
value (2) at every one of 261 call sites in the repo. Raising it to
`action_dim` lifts measured diversity from ~2.16 to ~4.98 out of a possible
5, on real rollouts, on the current codebase, with no code change.**

---

## 1. Motivation

`REE_assembly/evidence/planning/sd063_online_head_training_keystone_2026-08-22.md`
section 5 (ree-v3 `88287f11c6`) measured, on real `CausalGridWorldV2` rollouts
(seeds 71/101/202, 4 episodes x 80 steps, `world_dim=32`), that the candidate
pool carries only **~2.0-2.4 distinct first-actions out of K=32 candidates**,
identical trained vs untrained head -- a **proposer** property, independent of
the newly-trained `E2WorldUncertaintyHead`. Since the head reads exactly those
first actions, it can express at most a 2-valued vector across 32 candidates
regardless of how well it is trained. That session flagged this as the
binding constraint on MECH-314b and asked, as follow-on 2 of its section 7:
"a spike measuring whether first-action diversity can be raised at all in
this substrate, not a build."

A second data point made this worth checking rather than assuming
architectural: `substrate_queue.json`'s `v3_exq_543e_arc062_spcem_falsifier`
entry (`evidence/planning/failure_autopsy_EXQ-543e_2026-05-17.md`) recorded,
on a **different, richer** agent build, `candidate_unique_first_action_classes:
mean 4.95 (min 4, max 5)` -- essentially full 5-class coverage
(`CausalGridWorldV2.action_dim == 5`). If that figure is real and
reproducible, first-action diversity is configuration-dependent, not fixed --
which is exactly what this spike was asked to determine.

## 2. Method

All four measurements below drive a real agent against real
`CausalGridWorldV2` rollouts (`env.action_dim == 5`), calling
`agent.generate_trajectories(...)` every tick (same driving pattern as
`tests/contracts/test_sd063_online_head_training.py::_drive_agent`, and as
the 543e failure-autopsy's own diagnostic harness), and recording
`len({agent.hippocampal._trajectory_first_action_class(c) for c in
candidates})` per tick. Run on the current codebase (ree-v3 `2cb7f730`,
fast-forwarded from a 7-commits-behind local checkout at session start --
0 ahead, so no local work was at risk; see WORKSPACE_STATE note below).
Reduced from the keystone's 4 episodes x 80 steps to 2 episodes x 40 steps x
3 seeds (240 ticks per config) to keep the spike fast; the reduction changes
sample size, not the qualitative answer (SP-CEM's per-tick behaviour does not
depend on episode length).

Two throwaway scripts (`ree-v3/_diversity_spike_scratch{,2}.py`), written and
deleted in-session, not committed, not queued as experiments -- this is a
diagnostic spike per the parent chip's own framing, not new experiment
infrastructure.

## 3. Results

### 3a. Config-richness comparison (does a richer build alone explain 543e's 4.95?)

| Build | `min_first_action_classes` | mean unique / 5 | min | max |
|---|---:|---:|---:|---:|
| A: SD-063-style minimal (`REEConfig.from_dims` bare) | 2 (default) | **2.163** | 2 | 4 |
| B: A + SP-CEM knobs pinned explicitly (rules out default drift) | 2 | **2.163** | 2 | 4 |
| C: 543e-style richer build (harm/goal/benefit/resource streams, same knobs 543e used) | 2 | **3.083** | 2 | 5 |

B == A exactly -- the SD-063 keystone's 2.0-2.4 figure is not a stale-default
artifact; `use_support_preserving_cem=True`, `stratified_elites=True`,
`ao_std_floor=0.2`, `min_first_action_classes=2` are genuinely today's
defaults and genuinely produce ~2.16. A richer build (C) raises the natural
ceiling somewhat (2.16 -> 3.08 -- extra heads shift the raw CEM proposal
distribution before support-preservation ever engages) but does **not**
reach 543e's historical 4.95 on its own. That residual gap (3.08 vs 4.95) is
not chased further here -- it is orthogonal to the actionable finding below,
which does not depend on config richness at all. Plausible candidates:
single-run vs 3-seed-averaged sampling noise, or incidental substrate drift
across the ~600 commits between 2026-05-17 and now in an unrelated code path
-- worth a follow-up only if the 543 lineage is revisited, not for MECH-314b.

### 3b. Direct lever sweep (raising the floor knob)

All on the SD-063-style **minimal** build (config A above), varying only the
floor:

| Build | Mechanism | mean unique / 5 | min | max |
|---|---|---:|---:|---:|
| D: `min_first_action_classes=3` | production SP-CEM injection + stratified elites | 2.987 | 2 | 4 |
| E: `min_first_action_classes=5` (`=action_dim`) | same | **4.979** | 4 | 5 |
| F: E + `per_class_quota=2` | same, plus a per-class elite quota | 4.979 | 4 | 5 |
| G: `use_action_class_scaffold_candidates=True` | diagnostic-only full one-hot scaffold (`ree_core/hippocampal/module.py:1208`), replaces lowest-scored candidates with one per class **every tick, unconditionally** | **5.000** | 5 | 5 |

E alone -- one integer config change, already-shipped production code path,
zero new architecture -- reaches **4.979**, matching 543e's historical 4.95
almost exactly. F shows the quota knob adds nothing once the floor itself is
at `action_dim` (there is no room left to quota within). G is the ceiling:
literal 5/5 every tick, because it forces one real (E2-rollout-scored)
candidate per action class unconditionally rather than only when the
existing pool falls short.

**So: the ~2.0-2.4 ceiling in the SD-063 keystone measurement is not an
intrinsic proposer/CEM-sampling limitation. It is a floor value
(`support_preserving_min_first_action_classes: int = 2`,
`ree_core/utils/config.py:2161`) chosen once, on 2026-05-17, to be "at least
2" and never revisited upward. Every one of 261 experiment-driver call sites
that sets this knob sets it to exactly `2`; `grep` finds no experiment or
behavioral test that has ever tried a higher value (the one `=3` hit in the
whole tree is a pure config-wiring unit test,
`tests/contracts/test_hippocampal_candidate_support.py:76`, asserting only
that the field round-trips).**

## 4. What the injected candidates actually are (why this is a cheap lever, not a hack)

`_inject_support_preserving_candidates` (module.py:1423) and
`_build_action_class_scaffold_candidates` (module.py:1208) do not manufacture
placeholder or random candidates. A missing-class candidate is built by
running the SAME `e2.rollout_with_world(...)` the ordinary CEM candidates go
through, constrained only to the required first action -- it is a real,
E2-scored trajectory for that class, not noise. `_support_preserving_elite_indices`
with `stratified_elites=True` then keeps the **best-scoring** candidate per
present class, so raising the floor does not inject arbitrary low-quality
options into the elite set at the expense of good ones -- it guarantees the
*best available* candidate for each action class is representable, in
addition to whatever the unconstrained CEM search already found.

**Cost, stated honestly and not fully measured here (out of spike scope):**
raising the floor from 2 to 5 means up to 3 more `e2.rollout_with_world`
calls per tick, only on the ticks where the pool doesn't already cover all 5
classes naturally -- a bounded, modest compute increase (observed: 240-tick
sweep of configs D/E/F/G together completed in ~500s wall-clock on this
box, no errors, no assertion failures). **What this spike does NOT measure**
is any *behavioural* cost -- whether forcing full first-action representability
changes `select_action`'s committed-action distribution, task reward, or
existing claim-relevant DVs on any of the many experiments that currently run
at the floor=2 default. That is exactly what follow-on 3 (below) should
cover before anyone proposes changing the production default.

## 5. Consequence for MECH-314b and the staged validation experiment

The staged design doc
(`mech314bc_percandidate_extension_staged_2026-08-08.md`) follow-on item 3 --
an ON-vs-OFF validation experiment for 314b's live per-candidate path -- was
deliberately left unqueued because a proposer-diversity floor of ~2 risked
reading a proposer null as a 314b null. **That risk is resolved: diversity is
not stuck at ~2, it is a one-line config change away from ~5 (saturating
`action_dim`).** The validation experiment can now proceed, but should be
designed as a **2x2** (314b ON/OFF x diversity floor default/raised) rather
than the original single-factor ON/OFF, with distinct-first-action count
recorded as a covariate on every arm (as the keystone doc already required)
so the raised-floor arms can be read against their own measured diversity
rather than assumed.

**This spike does not recommend changing the production default itself.**
`support_preserving_min_first_action_classes=2` is depended on by 261
existing driver call sites and is the substrate every landed claim in the
543/567 lineage was evaluated against; raising it fleet-wide is a substrate
change requiring its own behavioural validation (section 4's open cost
question), not a spike-scope decision.

## 6. Scope held

This session did not: touch `ree_core/utils/config.py` or
`ree_core/hippocampal/module.py` (read-only diagnostic); queue or build the
314b validation experiment (spawned as a follow-on chip instead, per
CLAUDE.md's default-to-chip housekeeping rule -- this is `/queue-experiment`
work, not `/governance` or `/failure-autopsy` work); resolve the 3.08-vs-4.95
config-richness residual (section 3a, noted as out-of-scope); or run the
`ree-v3` contract suite (no `ree_core`/`config.py` edit was made, so nothing
here requires a green gate run).

## 7. Follow-on

1. **Queue the 314b 2x2 validation experiment** (ON/OFF x floor
   default/raised, distinct-first-action-count covariate mandatory on every
   arm) via `/queue-experiment`. Chipped, not built here.
2. The 3.08-vs-4.95 config-richness gap (section 3a) is recorded but not
   investigated -- only worth chasing if the 543/567/543e-546 lineage is
   revisited on its own terms.
