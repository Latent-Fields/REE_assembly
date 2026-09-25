# MECH-287 PAG re-commit readout: built, landed, then REFUSED by red-team

**Status: AWAITING USER REVIEW. Nothing in this file has been written to claims.yaml. The
MECH-287 experiment was NOT queued. EXP-0371 was NOT released.**

- Session: `metaworker-science-20260925-orchc-mech287-readout-build`
- Campaign: `science-20260925-orchc-mech287-readout-build` (orchestrate-20260924-1707)
- Chip: `chip-20260924-mech287-pag-recommit-readout-build` (/implement-substrate)
- Decision chip raised: `chip-20260925-mech287-dv-choice`
- Landed: `ree-v3` `7181ac2d6c` (build) + the annotation commit that follows it
- Written: 2026-09-25

## 1. What was built, and what happened

The chip applied the user's OPTION A ruling (2026-09-24, rec-20260924-115a750f): build the
instrument before re-running the MECH-287 design. The defect it targets was re-verified at
source by this session before any code was written --
`PAGFreezeGate.reset()` (`ree_core/pag/freeze_gate.py:145-150` pre-change) clears the
per-episode freeze state but not `_n_ticks` / `_n_commits` / `_n_releases`, and
`REEAgent.reset()` calls it every episode, so the counters span warmup+eval; an episode
ending frozen consumes a commit with no matching release.

The build landed green (5601 contract tests passed; the 2 reds were isolated to other
sessions' untracked scripts in the shared checkout -- 44/44 in a clean throwaway worktree
at the base commit and 44/44 with only these changes).

It was then put through the mandatory adversarial red-team, which returned **BLOCKING**.
**Four findings were independently re-measured by this session before being accepted.** Per
the standing rule -- a red-team refusal is a result to record, not to design around -- the
session stopped rather than re-defining the DV on its own authority.

## 2. F1 (BLOCKING, re-measured): the headline DV is bounded at 1.0 and PINNED at 1.0 in the comparator regime

A commit fires only from the inactive state and a release only from the active state, so
within an episode **every re-commit is preceded by exactly one release**. Therefore
`recommits <= releases` always and `recommits_per_release` is bounded in **[0, 1]**. It
reduces algebraically to

```
recommits_per_release = 1 - (episodes with >=1 release that ended NOT frozen) / (total releases)
```

Measured by this session (11 episodes each, every episode ending frozen -- V3-EXQ-475's
phenotype is 1000/1000 freeze-active steps):

| re-commit cycles per episode | commits | releases | recommits | DV |
|---|---|---|---|---|
| 1 | 22 | 11 | 11 | **1.0000** |
| 2 | 33 | 22 | 22 | **1.0000** |
| 5 | 66 | 55 | 55 | **1.0000** |
| 10 | 121 | 110 | 110 | **1.0000** |

**Zero variance, whatever the re-commit behaviour is.** A brute-force sweep over 400 random
freeze/release shapes never exceeded 1.0000.

Where episodes end RELEASED the DV instead moves with **episode LENGTH**, not episode count:

| cycles per episode | 1 | 2 | 4 | 8 | 20 |
|---|---|---|---|---|---|
| DV | 0.0000 | 0.5000 | 0.7500 | 0.8750 | 0.9500 |

exactly `1 - 1/cycles`. So the episode-boundary artifact was **re-parameterised, not
removed**: from `+episodes_ending_frozen/releases` to `-episodes_ending_released/releases`.

Consequences:
- MECH-287's non-degeneracy precondition ("freeze re-commit count well above floor") cannot
  be satisfied by any "per release" ratio -- the ceiling is 1.0.
- Every threshold derived from V3-EXQ-475 (`LOCK_REGIME_FLOOR = 8.0`, `EFFECT_FLOOR_ABS =
  4.0`, `MODE_FLIP_RECOMMIT_BUDGET = 13`) is above that ceiling, so unreachable rather than
  merely confounded. A reader comparing the new number to "12.9" misreads by an order of
  magnitude.
- The field is a deterministic recoding of `releases_per_episode` and
  `frac_episodes_ending_frozen`, both already in the same dict.

## 3. F2 (BLOCKING, re-measured): the staleness "peak" fields recover <1% of the peak

`staleness_peak_over_episodes` / `mean_staleness_peak` are the max ACROSS episodes of each
episode's **end-of-episode** value, not a within-episode peak.
`StalenessAccumulator.tick_leak()` multiplies every region by `leak_factor` (default
**0.995**) on every tick and deletes rows below `drop_epsilon=1e-6`.

Decay of the exact 0.432491 peak the V3-EXQ-1097 dry run recorded:

| ticks | value | % of peak |
|---|---|---|
| 100 | 0.261990 | 60.58% |
| 500 | 0.035279 | 8.16% |
| **1000** (V3-EXQ-475's eval length) | **0.002878** | **0.67%** |

After ~2589 quiet ticks the map is empty and `max_staleness` is exactly 0.0. So the field
reproduces the `0.000` that motivated the build, not the `0.432`. The capture-before-erase
ordering repair is correct but saves a number that leak has already destroyed.

**Asymmetric:** `n_broadcast`, `n_suppressed`, `n_integrations` are monotone counters and DO
survive. Only the staleness MAGNITUDE fields are broken.

## 4. F3 (MAJOR, re-measured): phase labels misattribute one episode per boundary

The label is stamped at finalize time, so under a RESET-AT-START driver the last episode of
the old phase is finalised under the new label. Measured on a 60-warmup / 5-eval shape:

```
warmup  n_episodes=59 (expected 60)
eval    n_episodes= 6 (expected 5)  ending_frozen=1 (expected 0)
```

At V3-EXQ-475's 5 eval episodes that is a **20% contamination of the eval denominator**, and
the contaminating episode is an ends-frozen one -- the worst kind for this DV. The contract
tests cannot see it because their helper always resets after the last episode, which is the
one convention under which the label is correct (a guard that supplies the thing it asserts).

## 5. Other findings accepted on the red-team's report (not independently re-measured)

- **F4 (MAJOR)** the `episode_*` ride-along keys on `diagnostics` are ALL-PHASE aggregates
  (no `phase=` argument), so the advertised zero-driver-change route hands back a
  warmup-dominated pool. They also omit `dv_measurable`.
- **F5 (MAJOR)** three different quantities are called `n_episodes`:
  `episode_diagnostics()` folds the in-progress episode, `episode_records()` does not, and
  the agent readout never does. The gate's denominator counts **E3 ticks**, the agent's
  counts environment steps.
- **F6 (MAJOR)** the agent readout aggregates FROM its `deque(maxlen=8192)`, so past 8192
  episodes every total is silently truncated with no dropped-row count (the gate keeps exact
  aggregates separately and is fine).
- **F7 (MAJOR)** the C4 blind-spot test's "naive read" divisor comes from the test's own
  `max(n_releases, 1)` helper on a 0/0 case; C4b's naive ratio does not in fact move.
- **F8-F15 (MINOR/NIT)** `reset_diagnostics()` does not clear `_freeze_active`;
  `max_freeze_duration` cap-forced releases count as genuine releases; `include_current`
  makes `episodes_ending_frozen` transiently wrong mid-episode; `episode_records(phase=)`
  evicts the earliest phase first; nothing in the repo consumes the instrument yet.

## 6. What the red-team confirmed is SOUND

- Purely additive / bit-identical: integer bookkeeping, no RNG, no new branch affecting output.
- The cumulative counters keep their exact prior semantics; every consumer
  (`v3_exq_483/483a/603i/603p/603r/603t`) reads selectively via `.get()`, nothing asserts the
  key set, and the 11 pre-existing MECH-279 tests pass.
- An episode ending frozen contributes no release.
- The capture-before-erase ORDERING is correct, and is what makes the monotone count fields work.
- ASCII-clean; no hot-path cost.

## 7. Blind-spot measurement (the new contract is real on the gate side)

Required by `/implement-substrate`. With the readout re-wired to the cumulative counters AND
the agent capture moved below the resets, **9 of the new tests FAIL** (C2, C4, C4b, C5b, C6,
C7, C10, C10b, C11) while **all 11 pre-existing MECH-279 tests still PASS**. The old guard is
blind to both defects. (Caveat: F7 above -- C4's specific construction is weaker than intended.)

## 8. F6-from-the-chip: the red-team's earlier unverified finding (d) -- CONFIRMED

The chip asked this session to verify whether broadcasts mark anchors inactive directly via
the per-region T3 shortcut. **They do.**

`HippocampalModule.apply_invalidation_broadcasts_to_regions()`
(`ree_core/hippocampal/module.py:4005-4054`) pops the `per_region_vs` entry for the
broadcast-targeted region and then calls `self.anchor_set.mark_inactive(...)` for every
active anchor matching `(source_scale, source_segment_id_old)`. Its only gate is
`use_per_region_vs` (`:4032`). The call site, `ree_core/agent.py:6095`, is likewise gated
only on `use_per_region_vs` -- **`use_staleness_accumulator` (MECH-284) appears nowhere in
either gate.**

So `B_TRIG_ONLY` DOES already carry a complete broadcast -> anchor-reset -> commit-release
path with MECH-284 absent, given `use_per_region_vs` and `use_anchor_sets` are on (they are,
in every arm, via `use_per_region_vs`). The prior analysis' F6 is confirmed, and its
consequence stands: **A vs D would be a change of staleness SOURCE, not presence/absence.**
Recorded here only -- per the chip, the experiment was NOT redesigned.

## 9. The decision owed (chip-20260925-mech287-dv-choice)

MECH-287's registered DV text ("freeze re-commit count per PAG release") is not measurable as
written: any faithful "per release" ratio is bounded at 1.0 and pinned at 1.0 in the regime the
claim's own non-degeneracy precondition demands. Options, which measure different things:

- **A. Re-point the DV to `recommits_per_episode`** (unbounded, does not saturate) and amend
  MECH-287's `functional_restatement` / `what_would_answer` to match. Breaks commensurability
  with V3-EXQ-475's recorded numbers -- but those are the artifact, so that is arguably
  correct rather than a cost.
- **B. Keep a per-release DV and add the missing headroom** by excluding ends-frozen episodes
  from the denominator, reporting them as a separate censoring rate. Preserves the claim's
  wording; introduces a censoring model the claim does not currently have.
- **C. Re-scope MECH-287 away from a ratio entirely** -- e.g. to the freeze-duration /
  lock-persistence phenotype 475 actually exhibited (1000/1000 freeze-active steps).
- Independently: whether to build a true within-episode staleness peak (a hippocampal-module
  running max, per F2) or to rename the fields to honest end-of-episode names.

**Recommendation: A for the DV, plus the honest rename now and the within-episode peak as a
separate substrate entry.** A is the only option that yields an unbounded quantity the
manipulation can move, and the claim text needs amending regardless (GFLAG-0477 already owes
an amendment to the same two fields for the original confound).

All of F3-F8 are ordinary defects with unambiguous fixes; they were left unfixed only because
they are cheaper to land in one pass with whichever DV the decision picks.
