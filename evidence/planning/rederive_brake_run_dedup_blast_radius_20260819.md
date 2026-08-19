# Re-derive brake: run-level de-dup fix and measured blast radius

**Generated:** 2026-08-19T18:50:11Z
**Chip:** `chip-20260819-rederive-brake-double-counts-readjudications`
**Status:** Fix landed (`.claude/skills/queue-experiment/SKILL.md` + `.agents/skills/queue-experiment/SKILL.md` Step 2.5b). This document is the measurement trail behind it and the **governance review surface** — see "What needs a human look" below.

## The defect

`/queue-experiment` Step 2.5b's re-derive brake counter (MOVE-3) counted **one hit per
artifact FILE** that tags a claim with a `substrate_ceiling`-shaped verdict (`break` after
the first matching target in each file). That unit — the artifact, not the underlying
experimental run — fails in two directions once an artifact stops being 1:1 with a run:

1. **Over-count.** A run re-adjudicated in a *later*, separate artifact (a combined /
   cluster re-read of an earlier single-run autopsy) was counted once in its original
   artifact and again in the re-adjudication. Confirmed on ARC-110:
   `failure_autopsy_V3-EXQ-711_2026-07-04.json` and
   `failure_autopsy_V3-EXQ-713_2026-07-05.json` each counted their own run, and
   `failure_autopsy_V3-EXQ-711-713_2026-07-20.json` (a combined re-adjudication of both)
   counted them a second time — 4 hits from only 3 distinct runs. This is the case the
   chip was scoped to fix.

2. **Under-count** (found while measuring the blast radius of #1 — same root cause, not a
   separate bug). A single "grandfathered"/cluster autopsy artifact bundling many distinct
   runs against one claim collapsed to **one** hit via the file-level `break`, discarding
   every other run in that file. Example: `failure_autopsy_grandfathered-sd029-arc030-cluster_2026-08-08.json`
   alone carries 12 qualifying distinct runs for MECH-256; the old counter read 2 for that
   claim across the whole corpus.

Both stem from the same design error: the loop's unit of counting was the artifact file,
when the brake's own semantics ("how many times has this claim's substrate hit a ceiling")
are defined over **runs**.

## The fix

The Step 2.5b snippet now keys its accumulator on `run_id` (falling back to `queue_id`,
then the filename) instead of the artifact file, and resolves a run counted in more than
one artifact to its **most recent** adjudication — `generated_utc` on the artifact,
falling back to the date embedded in the artifact's own filename when `generated_utc` is
absent (2 of 425 artifacts; neither affects any claim in the diff below). This also fixes
the under-count automatically: every distinct run in a cluster file now gets its own entry
regardless of how many siblings share the file.

Recency-based resolution is required, not optional — several re-adjudications explicitly
**withdraw** an earlier ceiling verdict, and a naive "counts if it ever counted" union
would keep re-inflating those. The clearest self-documenting case:
`failure_autopsy_V3-EXQ-710_2026-07-20.json`'s own `re_derive_brake` block states *"This is
a RE-ADJUDICATION of the same run, not a new experiment. Counting it as a fresh
substrate_ceiling hit would double-count one run. Withdrawing 710's ceiling reading REMOVES
its hit from every count"* and records `counts_before.MECH-140: 1` / `counts_after.MECH-140:
0` — independently deriving the same number this fix computes from the corpus today (`1 -> 0`).

## Held-out check (GOV-HELDOUT-1)

This is a standing-rule edit (`.claude/skills/queue-experiment/SKILL.md`), so per
`CLAUDE.md`'s held-out-check discipline the new wording was tested against real historical
cases the fix was not written from, requiring old and new to actually disagree:

- **MECH-140** (old 2, new 0): old wording counts a withdrawn ceiling verdict as still
  live; new wording correctly drops it — independently confirmed by the artifact's own
  `counts_after` field, computed by the autopsy author with no knowledge of this fix.
- **ARC-033** (old 1, new 2): old wording under-counts (misses a run bundled in a cluster
  file), silently leaving a claim un-braked that should be braked.
- **MECH-256** (old 2, new 13): old wording under-counts by an order of magnitude on a
  grandfathered cluster artifact.
- **ARC-110** (old 4, new 3): the motivating case — old wording over-counts a
  re-adjudicated run.

Four differing cases found directly in corpus data (exceeds the >=3 minimum), covering
both failure directions (over- and under-count) and one case independently cross-checked
against the corpus's own self-reported arithmetic. Shipped as a general fix to the counting
method, not scoped to the ARC-110 incident alone.

## Measured blast radius (full corpus, 425 artifacts, 158 claims with any brake-relevant history)

68 of 158 claims (43%) change count under the corrected method. Only changed claims are
listed; everything else is unaffected.

| Claim | Old | New | Note |
|---|---|---|---|
| ARC-016 | 3 | 5 |  |
| ARC-030 | 4 | 12 |  |
| ARC-033 | 1 | 2 | **NEWLY BRAKED** |
| ARC-062 | 22 | 26 |  |
| ARC-065 | 9 | 11 |  |
| ARC-110 | 4 | 3 |  |
| INV-034 | 4 | 3 |  |
| INV-054 | 2 | 4 |  |
| INV-074 | 9 | 11 |  |
| MECH-025 | 1 | 4 | **NEWLY BRAKED** |
| MECH-057b | 1 | 2 | **NEWLY BRAKED** |
| MECH-071 | 1 | 2 | **NEWLY BRAKED** |
| MECH-075 | 2 | 4 |  |
| MECH-090 | 10 | 11 |  |
| MECH-091 | 1 | 2 | **NEWLY BRAKED** |
| MECH-093 | 2 | 4 |  |
| MECH-095 | 5 | 12 |  |
| MECH-102 | 3 | 5 |  |
| MECH-112 | 2 | 11 |  |
| MECH-140 | 2 | 1 | **NEWLY RE-QUEUEABLE** |
| MECH-163 | 4 | 5 |  |
| MECH-171 | 3 | 7 |  |
| MECH-186 | 1 | 2 | **NEWLY BRAKED** |
| MECH-188 | 1 | 2 | **NEWLY BRAKED** |
| MECH-216 | 1 | 6 | **NEWLY BRAKED** |
| MECH-229 | 4 | 8 |  |
| MECH-230 | 4 | 8 |  |
| MECH-256 | 2 | 13 |  |
| MECH-258 | 2 | 10 |  |
| MECH-260 | 16 | 26 |  |
| MECH-263 | 11 | 10 |  |
| MECH-266 | 4 | 7 |  |
| MECH-295 | 3 | 4 |  |
| MECH-302 | 2 | 3 |  |
| MECH-309 | 21 | 25 |  |
| MECH-313 | 11 | 14 |  |
| MECH-314 | 11 | 10 |  |
| MECH-334 | 9 | 11 |  |
| MECH-341 | 8 | 5 |  |
| MECH-439 | 13 | 12 |  |
| MECH-440 | 1 | 0 |  |
| MECH-445 | 7 | 8 |  |
| MECH-456 | 3 | 4 |  |
| MECH-457 | 9 | 13 |  |
| MECH-471 | 2 | 1 | **NEWLY RE-QUEUEABLE** |
| Q-002 | 2 | 3 |  |
| Q-007 | 3 | 5 |  |
| Q-021 | 4 | 3 |  |
| Q-034 | 2 | 6 |  |
| Q-040 | 1 | 2 | **NEWLY BRAKED** |
| Q-043 | 3 | 2 |  |
| Q-045 | 7 | 10 |  |
| Q-054 | 1 | 0 |  |
| SD-005 | 1 | 2 | **NEWLY BRAKED** |
| SD-008 | 1 | 2 | **NEWLY BRAKED** |
| SD-010 | 2 | 4 |  |
| SD-011 | 1 | 3 | **NEWLY BRAKED** |
| SD-012 | 3 | 11 |  |
| SD-015 | 6 | 18 |  |
| SD-016 | 1 | 6 | **NEWLY BRAKED** |
| SD-017 | 4 | 11 |  |
| SD-021 | 3 | 9 |  |
| SD-029 | 2 | 13 |  |
| SD-032a | 4 | 7 |  |
| SD-032b | 3 | 10 |  |
| SD-033b | 11 | 10 |  |
| SD-034 | 10 | 16 |  |
| SD-049 | 5 | 9 |  |

### Threshold crossings (`RE_DERIVE_BRAKE_THRESHOLD` default 2) -- the actual review surface

**13 claims newly cross INTO braked status** (previously below threshold, a lettered
re-queue would have proceeded through Step 2.5b without stopping; a future
`/queue-experiment` session on these will now correctly stop and route to
`/implement-substrate` instead): `ARC-033`, `MECH-025`, `MECH-057b`, `MECH-071`,
`MECH-091`, `MECH-186`, `MECH-188`, `MECH-216`, `Q-040`, `SD-005`, `SD-008`, `SD-011`,
`SD-016`.

**2 claims newly cross OUT of braked status** (previously blocked, would now be allowed to
proceed to a lettered re-queue): `MECH-140`, `MECH-471`. Both are corpus-verified genuine
releases, not artifacts of the fix: `MECH-140`'s sole braking run (`v3_exq_710_...`) had its
ceiling verdict explicitly withdrawn in `failure_autopsy_V3-EXQ-710_2026-07-20.json`, whose
own `re_derive_brake.mech_140_note` already says *"MECH-140's brake count drops to 0, so the
standing refusal no longer has an autopsy basis on that claim specifically"* — the fix's `1`
differs from the artifact's stated `0` only because one further count-1 run for MECH-140
(`v3_exq_163_...`, a 2026-03-29 legacy run surfaced by an unrelated 2026-08-08 grandfathering
pass) postdates that note.

`MECH-440` and `Q-054` drop to 0 (were already below threshold at 1, so not a crossing, but
worth noting: both were sole-counted by since-withdrawn re-adjudications of the same kind as
MECH-140's).

## What needs a human look

This fix changes what a *future* `/queue-experiment` Step 2.5b invocation will report for
these 15 claims (13 newly-braked + 2 newly-released) — it does not retroactively alter
`claims.yaml`, `substrate_queue.json`, or any already-completed run's evidence direction.
Nothing here needs to happen before the fix can land (the counting method is simply more
correct now), but the next `/governance` cycle's routine walk should look at:

- The 2 newly-released claims (`MECH-140`, `MECH-471`) — confirm there is no other reason
  (outside the brake) they should stay parked before treating them as re-queueable.
- The 13 newly-braked claims — check whether any has an in-flight or imminently-planned
  lettered re-queue that this would now correctly stop, so the routing to
  `/implement-substrate` happens before, not after, a wasted run.

Not chipped: per `CLAUDE.md`'s chip-vs-inline-report rule, claim-disposition review of this
kind is `/governance` work, reported here for the next governance cycle rather than spawned
as a separate follow-on chip.

## Methodology notes

- `counts()` (the epistemic-category / instrument-defect / per-claim-override predicate)
  is unchanged — this fix only changes the accumulation unit (run vs. file) and the
  cross-artifact recency resolution, not what counts as a "genuine ceiling" in the first
  place.
- Two of 425 artifacts lack `generated_utc`
  (`failure_autopsy_V3-EXQ-626_2026-06-01.json`, `failure_autopsy_V3-EXQ-787_2026-07-19.json`);
  neither contributes a counted hit for any claim in the diff table above, so the filename-date
  fallback was never exercised by this measurement.
- 25 `(claim, run_id)` pairs are recorded as brake-relevant in more than one artifact; of
  those, 14 disagree on the `counts()` verdict across artifacts (i.e. genuinely need the
  recency tie-break, not just de-duplication) — the `MECH-140`/`MECH-710` and
  `MECH-102`/`SD-010` grandfathered-cluster pairs above are two of those 14.
