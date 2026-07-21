---
title: "SD-077: common-mode-invariant (centered) super-ordinal goal-anchor cue key"
nav_exclude: true
status: candidate/v3_pending
status_asof: 2026-07-21
status_claim: SD-077
---

# SD-077: goal.common_mode_invariant_super_ordinal_cue_key

**Claim ID:** SD-077
**Subject:** goal.common_mode_invariant_super_ordinal_cue_key
**Registered:** 2026-07-21
**Status:** IMPLEMENTED (2026-07-21)
**Depends on:** MECH-189 substrate (`SuperOrdinalGoalMemory`, ree-v3 `ree_core/goal.py`), SD-008 (z_world differentiation -- the deficit this works around), SD-066 (the same fix, previously validated on the SD-051 conditioned-safety readout)
**Blocks:** MECH-329 (wanting-before-liking goal seeding), MECH-189 (super-ordinal goal anchors); the V3-EXQ-669c re-issue of the 669b ordering test

## Problem

`V3-EXQ-669b` (run 2026-06-13, manifest
`v3_exq_669b_mech329_wanting_first_goal_seeding_20260613T123433Z_v3.json`, outcome
FAIL / `non_contributory`) self-routed on its own pre-registered readiness gate
**R3**: *max `anchor_count` across all arms/seeds >= 2*. Observed `anchor_count = 1`
everywhere, so the two load-bearing criteria -- C1 (`anchor_count` delta) and C3
(p01 complexity delta) -- had zero cross-arm range and could not differentiate.
This was correctly adjudicated as a substrate-readiness limit, **not** a
falsification of MECH-329 / MECH-189.

The manifest note and the script docstring both attribute this to
`super_ordinal_merge_similarity` collapsing the nursery `z_world` contexts into a
single anchor, and propose "a more context-diverse nursery / lower
merge_similarity". **The diagnosis is right about the collapse and wrong about
both proposed remedies.** Measured 2026-07-21 (session
`scientific-dashboard-status-7d2d08`) by driving the actual 669b Stage-0
forced-feed nursery (`CausalGridWorldV2(size=8, num_hazards=0, num_resources=6,
use_proxy_fields=True)`, 155 contexts, seed 101, `alpha_world=0.9`):

| signal | pairwise cosine min / mean / max | fraction of pairs < 0.8 |
|---|---|---|
| raw `world_obs` (250-d) | 0.2164 / 0.6084 / 1.0000 | **90.7%** |
| `z_world` (32-d -- what the store keys on) | **0.9641** / 0.9898 / 1.0000 | **0.0%** |
| `z_world` minus its running mean | -0.7595 / -0.0054 / 1.0000 | **97.7%** |

with `||mean(z_world)|| / mean||z_world|| = 0.9949` -- every context points in
essentially the same direction.

**The nursery is not context-poor. It is richly diverse in the observation, and
the untrained `z_world` encoder buries that diversity under a dominant common-mode
offset.** This is the identical signature already diagnosed and fixed once, for a
different consumer, in SD-066 (measured there as `cos(two different contexts) =
0.9950`); it is a consequence of the SD-008 / SD-070 z_world under-differentiation,
which SD-070 records is *not* repairable by the prescribed P0 training recipe
(that recipe collapses z_world to participation ratio ~1).

### Why threshold tuning cannot fix it

This is provable, not merely observed. `contextual_complexity = 1 - best_cosine`,
and `best_cosine >= 0.9641` for every context in the nursery, so complexity
`<= 0.036` for every non-bootstrap write under **any** threshold setting --
strictly below 669b's pre-registered `COMPLEXITY_MARGIN` of 0.05. Measured mean
complexity over the 160 fired writes is **0.0077**. The C3 criterion is
**unsatisfiable by construction** on a raw-`z_world` key. Only changing the key
space helps.

Both suggested directions fail, in different ways:

- **Lowering `merge_similarity` is the wrong sign.** It moves *more* contexts into
  the REINFORCE branch (`ree_core/goal.py`, the `best_sim >= merge_similarity`
  test), making saturation strictly worse.
- **Raising it** to 0.99 does yield ~4 anchors, but only by slicing the untrained
  encoder's numerical residue; the complexity statistic still cannot exceed 0.036,
  so C3 remains unreachable and the anchors index nothing meaningful.

Note also that the 669b script ran `complexity_threshold=0.2` with
`merge_similarity=0.8`, so there was no reinforce/allocate dead zone -- every
contact *did* write. `anchor_count = 1` is 1 allocation and 159 reinforcements into
slot 0, not a suppressed write path.

## Solution

Apply the **SD-066 pattern** to `SuperOrdinalGoalMemory`: maintain a slow EMA
**common-mode baseline** of presented `z_world` contexts and take every cue cosine
on the **centered residual** `z_world - baseline`. Entirely internal to
`ree_core/goal.py` -- **no `agent.py` wiring change**.

- **Baseline** (`_baseline`): EMA at `super_ordinal_cue_baseline_alpha` (default
  0.02, matching SD-066). **Lazily seeded** from the first waking context, so there
  is no zero-init cold-start transient. Advanced by `observe()`, which is called
  from both `write()` and `retrieve()`.
- **Advanced before the `write_enabled` gate**, deliberately: the baseline is cue
  *geometry*, not anchor *content*, so it must keep tracking the context
  distribution through the adult (write-frozen) phase that reads from the store.
  `retrieve()` also advances it, because once writes are frozen the retrieval
  contexts are often the only contexts presented.
- **MECH-094:** `simulation_mode` contexts never advance the baseline. Replay/DMN
  must not shape the waking cue geometry. (The existing anchor-write path was
  already `simulation_mode`-gated.)
- **Keys are stored RAW and centered at comparison time** -- deliberately, rather
  than storing pre-centered keys. A drifting baseline then moves query and stored
  keys together and can never leave the store internally inconsistent, which
  storing pre-centered keys would.
- `contextual_complexity` and `retrieve` inherit the change automatically; both
  route through `_best_match`.

### Config

| Param | Type | Default | Purpose |
|---|---|---|---|
| `super_ordinal_cue_centering` | bool | `False` | master switch; OFF allocates no baseline and runs no baseline arithmetic |
| `super_ordinal_cue_baseline_alpha` | float | `0.02` | common-mode EMA rate (SD-066's validated default) |

**Backward compatible.** With `super_ordinal_cue_centering=False` the OFF path is
bit-identical: `observe()` returns immediately, `_centered()` is the identity, and
no baseline tensor is allocated. Verified by contract (C1) and by end-to-end
smoke test reproducing the exact 669b failure signature (`anchors=1`, `alloc=1`,
`reinforce=159`, mean complexity 0.0077).

**Phased training: not required.** `SuperOrdinalGoalMemory` is a pure stateful
tensor store -- no `nn.Module`, no trainable parameters, no gradient flow. SD-077
adds one more non-trainable tensor. No encoder head is introduced, so the
P0/P1/P2 protocol does not apply.

## Measured effect

End-to-end on the real 669b nursery (seed 101, 4 episodes x 40 steps, forced
supra-threshold benefit each step, 160 writes):

| configuration | anchors | allocate | reinforce | mean complexity |
|---|---|---|---|---|
| centering OFF (= pre-SD-077, the 669b run) | **1** | 1 | 159 | **0.0077** |
| ON, `n_slots=16`, merge 0.8, cthr 0.2 | 16 (slot-capped) | 28 | 132 | 0.080 |
| **ON, `n_slots=64`, merge 0.8, cthr 0.2** | **26** | 26 | 134 | **0.076** |
| ON, `n_slots=64`, merge 0.5, cthr 0.5 | 9 | 9 | 151 | 0.104 |

R3 (`anchor_count >= 2`) clears, and mean complexity clears the 0.05
`COMPLEXITY_MARGIN` that was unreachable by construction before.

**Consequence for the V3-EXQ-669c re-issue:** 669b's `super_ordinal_n_slots=16`
**caps** the bank (28 allocations into 16 slots), which would re-flatten C1 by
saturating every arm at the same ceiling. 669c should raise `n_slots` to 64 so
`anchor_count` is free to vary between arms. Recommended 669c config:
`super_ordinal_cue_centering=True`, `super_ordinal_n_slots=64`, thresholds
otherwise unchanged from 669b (merge 0.8, cthr 0.2) -- 26 anchors with headroom.

## Architecture Context

SD-077 is the third instance of one recurring pattern: **a cosine readout over
`z_world` is dominated by the common mode, not by the context**, because SD-008
z_world under-differentiation is unresolved and SD-070 shows the prescribed
training recipe makes it worse rather than better.

- **SD-066** fixed it for the SD-051 `ConditionedSafetyStore` release gate.
- **SD-077** fixes it for the MECH-189 `SuperOrdinalGoalMemory` cue key.

Both are opt-in, non-parametric workarounds at the *consumer*, not repairs of the
encoder. The encoder-level repair remains the SD-008 / SD-070 open problem. That
this pattern has now recurred twice is itself evidence about where the real debt
sits: any future consumer keying an absolute cosine on `z_world` should be assumed
to need centering until SD-008 is resolved.

## What This SD Enables

- **MECH-329** (`development.wanting_before_liking_goal_seeding_sequence`) --
  currently `candidate/substrate_ceiling`, confidence 0.0,
  `pending_retest_after_substrate: true`. The 669c re-issue can now score C1/C3.
- **MECH-189** (`development.super_ordinal_goal_formation`) -- same status. The
  write+read substrate fires either way; SD-077 is what makes the *hierarchy*
  (more than one anchor) observable.
- Releases the `/queue-experiment` Step 2.5b re-derive brake, which trips at count
  2 for MECH-189 (`failure_autopsy_V3-EXQ-588_2026-05-19`,
  `failure_autopsy_V3-EXQ-669a_2026-06-13`) and refuses further lettered
  iterations until the substrate moves.

## Related Claims

MECH-189, MECH-329, SD-066, SD-008, SD-070, SD-051, SD-057, DEV-NEED-006,
DEV-NEED-024, goal_pipeline:GAP-2.
