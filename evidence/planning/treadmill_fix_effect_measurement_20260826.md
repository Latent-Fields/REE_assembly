# Treadmill fix effect measurement -- 2026-08-26

**Status: measurement complete, verdict is INSUFFICIENT ELAPSED TIME, not a refutation or confirmation.**

Chip: `chip-20260826-treadmill-fix-effect-measurement`, spawned 2026-08-26T20:28:37Z by
`mech-152-measurement-redesign-d5bf26`. Written 2026-08-26T21:19:50Z (UTC, `date -u`).

## Why this report says "too early" up front

The chip's own tldr states the intent explicitly: *"In ~7 days, re-run the August work-mix
measurement to test whether capping housekeeping's session share actually lowered housekeeping
chip CREATION."* The three fix commits it is testing landed the SAME DAY it was dispatched, not
seven days earlier:

| commit | time (UTC) | what |
|---|---|---|
| `672c6037` | 2026-08-26T19:53:43Z | `dispatch_budget_gate.py` housekeeping-share cap (fix 1) + `check_experiment_queue_floor.py` alarm (fix 3, part A) |
| `a00be1ba` | 2026-08-26T19:53:43Z | wires both gates into metaworker-dispatch Step 4c (fix 3, part B) |
| `109d9708` | 2026-08-26T20:27:06Z | host-qualifies the queue-floor chip_ref (dedup fix for fix 3's own alarm chip) |

This report was written at 21:19:50Z -- **83 to 87 minutes after the fixes landed.** That is the
entire post-fix data window available right now. Every number below that is described as
"post-fix" should be read with that in mind: it is a sample of one partial hour, not the ~7 days
the diagnosis called for. Rather than force a verdict out of a window this thin, this report
does two things: (1) reproduces the historical diagnosis cleanly, since that data is not
time-limited, and (2) checks whether the fixes' MECHANISMS are even engaging yet, which is a
question the 87-minute window CAN answer, per Step 5's own instruction to distinguish "no effect"
from "never engaged." A full creation-rate verdict needs the re-run this chip's own tldr asked
for, at fix+~7d (~2026-09-02).

## 1. Housekeeping share of chips SPAWNED per day (creation, not resolution)

Classification is origin-first, matching `dispatch_candidate_order.py`'s own rule, applied to
every entry in `TASK_CHIPS.json` (1,714 chips, all with a `spawned_at` timestamp, none dropped):

```
origin == "hygiene_tick"                              -> housekeeping
origin in ("igw_tick", "proposal_tick")               -> science
title matches (MECH|ARC|SD|INV|GAP|Q|EXQ|EXP)-<alnum> -> science
everything else                                       -> other
```

| date | housekeeping | science | other | total | hk share |
|---|---|---|---|---|---|
| 2026-07-29 | 0 | 15 | 10 | 25 | 0.0% |
| 2026-07-30 | 0 | 13 | 40 | 53 | 0.0% |
| 2026-07-31 | 0 | 19 | 4 | 23 | 0.0% |
| 2026-08-01 | 0 | 31 | 17 | 48 | 0.0% |
| 2026-08-02 | 3 | 30 | 26 | 59 | 5.1% |
| 2026-08-03 | 4 | 24 | 31 | 59 | 6.8% |
| 2026-08-04 | 0 | 4 | 0 | 4 | 0.0% |
| 2026-08-05 | 0 | 3 | 0 | 3 | 0.0% |
| 2026-08-06 | 0 | 1 | 0 | 1 | 0.0% |
| 2026-08-07 | 2 | 25 | 14 | 41 | 4.9% |
| 2026-08-08 | 3 | 41 | 28 | 72 | 4.2% |
| 2026-08-09 | 3 | 24 | 48 | 75 | 4.0% |
| 2026-08-10 | 0 | 11 | 20 | 31 | 0.0% |
| 2026-08-11 | 0 | 13 | 13 | 26 | 0.0% |
| 2026-08-12 | 0 | 18 | 30 | 48 | 0.0% |
| 2026-08-13 | 2 | 14 | 11 | 27 | 7.4% |
| **2026-08-14** | 16 | 10 | 48 | 74 | **21.6%** |
| 2026-08-15 | 26 | 7 | 49 | 82 | 31.7% |
| 2026-08-16 | 27 | 21 | 46 | 94 | 28.7% |
| 2026-08-17 | 9 | 5 | 25 | 39 | 23.1% |
| 2026-08-18 | 74 | 13 | 80 | 167 | 44.3% |
| 2026-08-19 | 91 | 2 | 65 | 158 | 57.6% |
| 2026-08-20 | 78 | 4 | 35 | 117 | 66.7% |
| 2026-08-21 | 25 | 9 | 29 | 63 | 39.7% |
| 2026-08-22 | 70 | 10 | 41 | 121 | 57.9% |
| 2026-08-23 | 34 | 11 | 17 | 62 | 54.8% |
| 2026-08-24 | 0 | 1 | 4 | 5 | 0.0% |
| 2026-08-25 | 16 | 21 | 30 | 67 | 23.9% |
| **2026-08-26 (all day, pre+post-fix mixed)** | 21 | 8 | 41 | 70 | 30.0% |

Period aggregates (chips, not per-day average of percentages):
- **1-13 Aug**: 17 housekeeping / 494 total = **3.4%**
- **14-26 Aug**: 487 housekeeping / 1,119 total = **43.5%**

This reproduces the diagnosis's direction cleanly (near-zero pre-14-Aug, a step change upward
starting exactly 14 Aug) though not its exact magnitude -- the diagnosis cited "75-90% from 14
Aug" where this reproduction peaks at 66.7% (2026-08-20) on a spawned-chip basis; the diagnosis's
number may have been measured on RESOLVED chips or a different window, which this report did not
attempt to reproduce exactly since Step 1 of the task explicitly asks for the CREATION series.
The qualitative finding -- a large, sudden, sustained inversion starting 14 Aug -- holds under
this independent reproduction.

### 2026-08-26 broken into pre-fix / post-fix (the only slice that bears on the actual test)

Fixes landed at 19:53:43Z (fix 1 + fix 3A) and 20:27:06Z (fix 3's dedup patch). Splitting today's
70 chips at 19:53:43Z:

| window | housekeeping | science | other | total | hk share |
|---|---|---|---|---|---|
| pre-fix (00:00-19:53Z, ~20h) | 17 | 6 | 35 | 58 | 29.3% |
| post-fix (19:53-21:14Z, ~80min) | 4 | 2 | 6 | 12 | 33.3% |

**Do not read the post-fix row as "the fix made it worse."** Of the 4 post-fix "housekeeping"
chips, 3 are `chip-queuefloor-*` -- the alarm chip fix 3 ITSELF creates every time it fires (see
Section 5). It is a hygiene_tick-origin chip by the classification rule, but it is the fix's own
output announcing "housekeeping is being withheld," not the pre-existing treadmill class the
diagnosis was about. Netting those out: 1 genuine non-alarm housekeeping chip
(`chip-staleclaim-insights-...`) in 12 total post-fix chips = 8.3%. Twelve chips in eighty
minutes is not a sample that supports any conclusion either way; it is reported for completeness
per the task brief, not as evidence.

## 2. Experiment result manifests landed per day

`git -C REE_assembly log --diff-filter=A --name-only`, top-level `evidence/experiments/*.json`
only (paths containing `/runs/` excluded, per the task brief):

| date | manifests | date | manifests |
|---|---|---|---|
| 2026-07-29 | 1 | 2026-08-13 | 4 |
| 2026-07-30 | 10 | **2026-08-14** | **14** |
| 2026-07-31 | 2 | 2026-08-15 | 3 |
| 2026-08-01 | 25 | 2026-08-16 | 1 |
| 2026-08-02 | 34 | 2026-08-17 | 3 |
| 2026-08-03 | 8 | 2026-08-18 | 5 |
| 2026-08-04 | 8 | 2026-08-19 | 5 |
| 2026-08-05 | 1 | 2026-08-20 | 3 |
| 2026-08-06 | 1 | 2026-08-21 | 0 |
| 2026-08-07 | 2 | 2026-08-22 | 6 |
| 2026-08-08 | 23 | 2026-08-23 | 2 |
| 2026-08-09 | 20 | 2026-08-24 | 2 |
| 2026-08-10 | 11 | 2026-08-25 | 5 |
| 2026-08-11 | 17 | 2026-08-26 | 2 (as of 21:19Z) |
| 2026-08-12 | 8 | | |

Period averages:
- **1-13 Aug**: 162 manifests / 13 days = **12.5/day** (diagnosis cited 10.9/day -- same
  direction, methodology not identical; not re-derived further since Step 3 only asked for the
  raw series, not a reconciliation with the prior figure)
- **14-26 Aug**: 51 manifests / 13 days = **3.9/day** -- matches the diagnosis's figure almost
  exactly.

No post-fix-only manifest figure is meaningful: manifests land on a timescale of hours per
experiment run, and only ~80 minutes have elapsed. 2026-08-26's count (2, both landed before the
fix) is not evidence of anything about the fix.

## 3. Experiment queue depth (`ree-v3/experiment_queue.json`)

One sample per day (latest commit touching the file that day), `git cat-file -p <sha>:experiment_queue.json`, `len(items)`:

| date | depth | date | depth |
|---|---|---|---|
| 2026-07-29 | 4 | 2026-08-13 | 0 |
| 2026-07-30 | 1 | 2026-08-14 | 3 (see Section 4 -- other samples read 1) |
| 2026-07-31 | 16 | 2026-08-15 | 0 |
| 2026-08-01 | 8 | 2026-08-16 | 1 |
| 2026-08-02 | 8 | 2026-08-17 | 0 |
| 2026-08-03 | 9 | 2026-08-18 | 0 |
| 2026-08-04 | 1 | 2026-08-19 | 0 |
| 2026-08-05 | 1 | 2026-08-20 | 1 |
| 2026-08-06 | 0 | 2026-08-21 | 2 |
| 2026-08-07 | 1 | 2026-08-22 | 1 |
| 2026-08-08 | 6 | 2026-08-23 | 0 |
| 2026-08-09 | 3 | 2026-08-24 | (no commit that day) |
| 2026-08-10 | 0 | 2026-08-25 | 0 |
| 2026-08-11 | 1 | **2026-08-26 (as of last commit before this report)** | **1** |
| 2026-08-12 | 2 | | |

Confirms the diagnosis's "depth 0-1 on every sampled day from 12 Aug" claim: every day from
2026-08-12 onward reads 0, 1, 2, or 3, with the floor of 3 breached (depth < 3) on 10 of the 14
days sampled since 12 Aug. **Right now** (2026-08-26T21:19Z), `check_experiment_queue_floor.py
--json` reports `depth: 1, floor: 3, starved: true` -- the queue is starved at the moment this
report is being written, which is directly relevant to Section 5.

## 4. Note on the 2026-08-14 discrepancy (this IS the residual the floor docstring already flags)

`check_experiment_queue_floor.py`'s own "WHY A FLOOR OF 3" section states 2026-08-14 sat at
depth 1 while landing 14 manifests that day, sampled at a specific intraday point. This report's
end-of-day sampling read depth 3 for the same date. Both are correct reads of the same file at
different times of day -- the queue was filled and drained multiple times on 2026-08-14. This is
exactly the residual the floor's own docstring names: **a single daily snapshot cannot
distinguish "starved" from "being consumed faster than it is filled,"** because depth measures
forward supply only. This report's own Section 3 sampling methodology reproduces that residual
rather than resolving it -- treat the docstring's intraday figures (depth 1 for both 08-11 and
08-14) as the more informative read, and this report's coarser one-sample-per-day series as
supporting context only.

## 5. Mechanism check: did the fixes actually engage?

**Fix 3 (queue-floor preemption): CONFIRMED ENGAGED, live, right now.**

```
$ python3 scripts/dispatch_budget_gate.py check --category housekeeping
BUDGET comfortable -- ticks 24/900 (0.03), workers 27/240 (0.11). HOUSEKEEPING WITHHELD: the
experiment queue is below its floor, so a housekeeping session is the wrong use of this slot.
SKIP THIS CHIP AND TAKE THE NEXT CANDIDATE -- ...

$ python3 scripts/check_experiment_queue_floor.py --json
{"depth": 1, "floor": 3, "starved": true, "queue_ids": ["V3-EXQ-603v"], ...}
```

The queue is starved right now, and the gate is actively returning WITHHOLD for housekeeping
category regardless of share. This is direct, live confirmation that fix 3's wiring works
end-to-end -- not an inference from chip counts.

**Fix 1 (25% housekeeping-share cap): NOT YET TESTABLE, and this is a wiring/timing finding, not
a refutation.** The share cap reads `category` fields on ledger events written by
`dispatch_budget_gate.py record --kind worker --category ...`. Inspecting
`metaworker_dispatch_budget_log.json` directly:

- 58 total events in the ledger; only **3** carry a `category` field at all, and all 3 were
  written AFTER the fix landed (21:12:54Z, 21:14:05Z, 21:15:30Z -- the earliest is 79 minutes
  post-fix). Every event before that predates the category-tagging wiring and is legacy
  (`category` absent).
- Of those 3 categorized events: 1 `science`, 2 `default`, **0 `housekeeping`.**
- `housekeeping_share()`'s denominator is the total WORKER count in the 24h window (27, per the
  `check` output above), of which only 3 carry a real category and the rest count in the
  denominator as legacy/unknown (never in the housekeeping numerator, per the module's own
  fail-open design). Current computed share is therefore 0/27 -- nowhere near the 25% trigger,
  and cannot meaningfully be otherwise until categorized events accumulate.
- **Because fix 3 is currently ALSO in force (queue starved) and ORs with fix 1 at the gate**,
  every housekeeping dispatch right now is being withheld by the floor check regardless of what
  the share cap would say. The two mechanisms are not separable in the current window: fix 3 is
  doing 100% of the observed suppression, and fix 1 has had no opportunity to bind on its own
  merits yet, categorization apart.

**Per Step 5's instruction to distinguish "no effect" from "never had a chance to fire": this
is the second case for fix 1, not the first.** It is a sample-size/timing fact (79-87 minutes of
categorized history against a mechanism designed to read a 24-hour window), not evidence the
share cap is broken or ineffective. It has simply not yet been given a window in which it could
bind independently of the (also-true-right-now) queue starvation.

## 6. Verdict

**INSUFFICIENT ELAPSED TIME -- neither "model supported" nor "model wrong" can be claimed
honestly from an 87-minute post-fix window against a mechanism whose own budget window is 24
hours and whose own recommended re-check interval (stated in this chip's tldr) is ~7 days.**

What CAN be said now:
- The historical diagnosis reproduces cleanly on an independent re-derivation: housekeeping
  chip-creation share went from 3.4% (1-13 Aug) to 43.5% (14-26 Aug); manifests/day fell from
  ~12.5 to ~3.9; queue depth sat at 0-3 on nearly every day from 12 Aug, breaching the floor of 3
  on 10 of 14 sampled days. The diagnosis's premise is not in doubt.
- Fix 3 (queue-floor preemption) is confirmed engaged and is the sole mechanism currently
  suppressing housekeeping dispatch, verified live against the running scripts, not inferred.
- Fix 1 (housekeeping-share cap) has not yet had an independent test window: too little
  categorized dispatch history exists (3 events, 0 of them housekeeping-categorized), and fix
  3's blanket withhold currently masks whatever fix 1 would otherwise decide. This is a
  timing/wiring observation, not a defect.
- No governance flag is being raised. The task brief's flag trigger is "verdict is 'model wrong'
  or 'fix never engaged'" -- neither holds here. Fix 3 demonstrably engaged; fix 1's status is
  "not yet observable," which is a distinct, milder finding that a flag would overstate.

**Recommendation, matching the chip's own stated intent:** re-run this exact measurement at
fix+~7 days (~2026-09-02), by which point (a) `metaworker_dispatch_budget_log.json` will hold a
full day or more of categorized worker events, letting fix 1's share cap be evaluated
independently of fix 3, and (b) several full days of post-fix chip-creation and manifest-landing
data will exist to compare against the 3.4%/43.5% and 12.5/3.9 baselines above. Re-dispatching
this same chip again immediately (as happened today) will reproduce this same "too early" result
-- the ~7-day gap in the original tldr was load-bearing and should be preserved by whatever
re-queues it.

## Raw data

Daily chip classification: `/tmp/daily_chip_classification.json` (ephemeral, worktree-local --
regenerable from `TASK_CHIPS.json` with the classification rule in Section 1). Manifest and
queue-depth series are reproduced in full in Sections 2-3 above; no separate raw file is needed
since the git commands that produced them are given inline and are cheap to re-run.
