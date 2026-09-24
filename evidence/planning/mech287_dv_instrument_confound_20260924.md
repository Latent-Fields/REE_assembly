# MECH-287's pre-registered DV is confounded with episode count -- V3-EXQ-1097 REFUSED

**Status: AWAITING USER REVIEW. No experiment was queued. EXQ id V3-EXQ-1097 was
reserved and RELEASED. Nothing was written to `claims.yaml`.**

- Session: `metaworker-science-20260924-orchb-mech287-invalidation-factorial`
- Campaign: `science-20260924-orchb-mech287-invalidation-factorial` (orchestrate-20260924-b)
- Chip: `chip-proposal-exp-0371` (EXP-0371 / MECH-287)
- Refused at: `/queue-experiment` Step 4.5, red-team verdict **BLOCKING** (model: fable)
- Written: 2026-09-24
- Source refs: `ree-v3` `351f0364`+ (this session's driver commit), `REE_assembly` `origin/master`

## 1. What happened

The user ruled **Option A** on this item's first decision chip
(`chip-20260924-mech287-readside-flag`): arm `use_vs_commit_release` ON and identical in
all four arms, leave the ratified manipulation untouched. That ruling was applied in full
and it works -- the read-side hook fires (`vs_commit_release_count = 1` in `D_BOTH_ON` at
toy scale), which is exactly what the first analysis said was missing.

The design was then authored, validated clean, smoke-tested green, and put through the
mandatory Step 4.5 adversarial red-team. The red-team returned **BLOCKING**, and four of
its findings were verified at source by this session. The decisive one is **not a defect in
the driver**: it is that MECH-287's pre-registered DV has no faithful instrument in the
current substrate, and the claim's own non-degeneracy precondition quotes the artifact.

Per the standing rule -- a red-team refusal is a result to record, not to design around --
this session stopped rather than re-operationalising the DV on its own authority.

## 2. F1, the decisive finding (CONFIRMED at source)

MECH-287's DV is *"Freeze re-commit count per PAG release"*. The only instrument is
`PAGFreezeGate.diagnostics` (`n_commits`, `n_releases`, `n_ticks`).

`PAGFreezeGate.reset()` (`ree-v3/ree_core/pag/freeze_gate.py:145-150`) clears
`_freeze_active`, `_duration_above_threshold`, `_ticks_in_freeze` and `_last_output` --
**but not `_n_commits`, `_n_releases` or `_n_ticks`**. `REEAgent.reset()` calls it once per
episode (`ree-v3/ree_core/agent.py:4016-4018`). The counters are therefore **cumulative
across every warmup and eval episode of the run**.

Freeze entry increments only from the inactive state and release only from the active
state, and `reset()` clears the freeze *without* incrementing `_n_releases`. So an episode
that ends while frozen consumes a commit with no matching release, giving

```
n_commits - n_releases  <=  n_episodes
recommits_per_release - 1  ~=  (episodes ending still frozen) / (PAG releases)
```

**The quantity is dominated by EPISODE COUNT, not by re-commit behaviour after a release.**

### The lineage numbers fit this exactly

V3-EXQ-475 ran 60 warmup + 5 eval = **65** episodes per seed and recorded:

| seed | `pag_n_commits` | `pag_n_releases` | difference | `recommits_per_release` |
|---|---|---|---|---|
| 0 | 71 | 6 | **65** | 11.8333 |
| 1 | 70 | 5 | **65** | 14.0000 |
| 2 | 64 | 5 | 59 | 12.8000 |

Two of three seeds hit the episode count exactly; the third is 59 <= 65. `pag_n_ticks` is
2629 / 2124 / 1993, all far above the 1000 eval steps -- independent confirmation that the
counters span warmup.

### Why this reaches the CLAIM, not just this driver

MECH-287's `functional_restatement` describes V3-EXQ-475's phenotype as *"~12x re-commits
per release"*, and its `what_would_answer` makes *"freeze re-commit count well above
floor"* the **non-degeneracy precondition** for any successor. Both statements are about
this confounded quantity. Every threshold this session derived from it inherits the
confound:

- `LOCK_REGIME_FLOOR = 8.0` (from 475's 11.83-14.00 range),
- `EFFECT_FLOOR_ABS = 4.0` (one third of the 11.878 elevation over the DV floor),
- `MODE_FLIP_RECOMMIT_BUDGET = 13` (round of the 12.878 mean).

A run built on them would have produced a PASS or FAIL attributable to warmup-phase
freeze-versus-episode-truncation dynamics, not to online anchor invalidation during eval.

## 3. The other verified findings

**F3 -- the mechanism instruments are per-episode; the post-loop read sees only the last
episode (CONFIRMED empirically, from this driver's own dry-run manifest).**
`agent.reset()` calls `reset_invalidation_trigger()` and `reset_staleness_accumulator()`,
which zero `_n_broadcast` and clear the staleness map. Reading `get_stats()` after the eval
loop therefore reads one episode. Direct evidence, `D_BOTH_ON` seed 1 in
`_dry_v3_exq_1097_..._20260924T133736Z_v3.json`: `mean_staleness_peak = 0.432491` (the
per-episode tracker this driver added) against `staleness_max = 0.000000` and
`staleness_n_integrations = 0` from the post-loop read. The accumulator demonstrably
integrated and the evidence was erased before the criterion read it. C3 as written would
fail whenever the final episode happens to be quiet.

**F4 -- C2 and C4 cannot fail under any outcome (CONFIRMED at source).** With
`use_invalidation_trigger=False`, `HippocampalModule.invalidation_trigger` is never
constructed (`ree_core/hippocampal/module.py:367-376`), so `n_broadcast` is 0 **by
construction** in arms A and C. With the segmenter off, `InvalidationTrigger.step` returns
before any increment on an empty boundary list (`invalidation_trigger.py:187-188`), so
arm E is silent by construction. Both were declared `load_bearing: true`, inflating the
PASS conjunction with two wiring checks. (The module's own comment at :364-366 describes
the segmenter-off case as the intended dissociation test -- so C4 is a *wiring* assertion,
which is legitimate to record but must not be load-bearing.)

**F5 -- the per-step freeze-commit poll over-counts (CONFIRMED empirically).**
`select_action` returns early on non-E3 ticks, so the `freeze_commit` edge flag persists
and is counted once per tick until the next E3 tick. Dry run, same cell:
`freeze_commit_count = 18` against `pag_n_commits = 5`. C5's re-commit budget was
denominated on a third quantity again.

**F6 -- reported by the red-team, not independently re-verified by this session.**
Broadcasts mark anchors inactive directly via the per-region T3 shortcut
(`module.py:4031-4053`), armed in every arm through `use_per_region_vs`, so `B_TRIG_ONLY`
may already carry a complete broadcast -> anchor-reset -> commit-release path with MECH-284
absent; and arm A is not "no invalidation" because anchors still go inactive through the
internal tick-delta staleness proxy. If it holds, A vs D is a change of staleness *source*,
not presence/absence -- which would bear on what the factorial can attribute to MECH-284.
**Flagged for verification, not relied on here.**

## 4. What this session verified vs took on report

Verified at source or from its own run: F1 (both the `reset()` omission and the 65-episode
arithmetic), F3 (from the dry-run manifest), F4 (both construction paths), F5 (from the
dry-run manifest). Taken on report, explicitly not re-verified: F6.

Also verified earlier this session and still standing: all five arms construct; every
instrument is present and correctly differentiated per arm; `use_vs_commit_release` fires
(`vs_commit_release_count = 1` in `D_BOTH_ON`); the driver passes
`validate_experiments.py --strict` (1 OK, 0 non-conforming, 0 warnings across 40 checks);
the `--dry-run` smoke exits 0, relocates its manifest, writes its sentinel, reports no
z_goal writer defect, and self-routes `substrate_not_ready_requeue` at toy scale rather
than emitting a false null.

## 5. The decision (why this session stopped a second time)

This is the **second** unspecified choice on this one item, which per the dispatch brief is
itself the finding: **the item's premises are stale and neither the proposal nor the
pre-flight caught it.** The pre-flight's AMBER named change was correct as far as it went --
build the comparator on 475, not 478 -- but both 475 and 478 measure the same confounded
counter, so "use 475's config" could not have fixed the DV.

Options, which measure different things:

- **A. Build the instrument first.** Add a phase-scoped PAG re-commit readout (either reset
  the counters at eval entry, or expose per-episode deltas) plus per-episode broadcast /
  staleness snapshots, then re-run this design against the repaired instrument. Route:
  `/implement-substrate`. This is the only option that lets MECH-287's DV mean what its text
  says. Cost: one substrate build before any science runs.
- **B. Re-operationalise the DV on existing instruments.** Define the DV as a within-eval
  per-episode quantity computed from the per-step polls this driver already collects
  (it records `release_steps`, `recommit_steps` and a mode timeline), and amend MECH-287's
  `what_would_answer` to match. Cheaper, but it changes the claim's registered falsifier and
  invalidates the comparison to V3-EXQ-475's recorded numbers.
- **C. Queue as designed.** Produces a verdict attributable to episode-truncation dynamics.
  Not recommended under any reading.

**Recommendation: A**, with the amendment in B's second half applied regardless -- MECH-287's
`functional_restatement` and non-degeneracy precondition both currently quote a confounded
number and should say so even if the instrument is repaired. C2/C4 should also be demoted
from `load_bearing` to recorded wiring assertions, and F6 verified, before this design runs.

## 6. Disposition of the artifacts

- Driver retained UNRUN at `ree-v3/experiments/v3_exq_1097_mech287_invalidation_trigger_accumulator_factorial.py`
  with a `DO NOT QUEUE` banner carrying all five findings.
- EXQ id **V3-EXQ-1097 reserved and RELEASED**; no queue entry exists.
- `EXP-0371` left for the registry write-back described in this session's closing note.
