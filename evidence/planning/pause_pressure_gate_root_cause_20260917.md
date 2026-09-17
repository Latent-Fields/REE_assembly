# Pause-pressure gate: root cause of the ten-generation recurrence

**Date:** 2026-09-17
**Session:** pausepressure-g10-rootcause-20260917
**Chip:** `chip-20260917-pausepressure-g10-rootcause` (resolving `chip-pausepressure-dlaptop-g10`)
**Skill:** `/metaworker-learning`, root-cause mode -- ratified by the user 2026-09-17 via the
Orchestrator decision lane (`orchestrate-20260917-1532`) explicitly INSTEAD of another instance fix
or a curated pause window.
**Subject:** `scripts/pause_pressure.py`, and the shared episodic-chip machinery it rides
(`scripts/hygiene_routine_tick.py::_record_episodic_finding` / `_standing_generation`).

---

## Verdict, up front

The gate has never once read NO PRESSURE, and could not have. Its dominant arm
(`recorded_7d_authored > 150`) was above threshold in **43 of 43** daily rolling windows across the
entire recorded chip history -- 2026-07-29 to 2026-09-17, which is a month longer than the gate has
existed. The quietest window in all of that history reads 169; over the gate's own lifetime the
minimum is 235, which is 1.6x the ceiling. There is no observed negative.

A binary gate with no observed negative is not a gate. It carries zero bits, and the ten
"generations" are not ten failed fixes -- they are ten occasions on which somebody answered a
constant.

The recommendation is therefore **RETIRE the PRESSURE verdict in its current form** (section 6),
keeping the two things that demonstrably discriminate and demoting the rest to report-only. The
highest-leverage single change is not in this gate at all: it is in the shared generation counter,
which counts resolutions rather than recurrences and does the same thing to nine other chip classes.

---

## 1. Method and sources

- Gate implementation and its full git history: `scripts/pause_pressure.py` (6 commits,
  2026-08-29..2026-09-16), `scripts/hygiene_routine_tick.py`.
- **All ten generations read live from the coordinator** via `coordinator_transport.list_chips()`
  (3,794 chips), not from the `TASK_CHIPS.json` git render, which lags. Every generation chip
  carries its metric snapshot in `episodes[]`, giving **15 readings** (some generations have
  several episodes).
- Prior root-cause artifacts, read in full rather than re-derived:
  `evidence/planning/pause_pressure_recurrence_rootcause_staged_20260902.md` (generation 3, with a
  generation-5 addendum) and
  `evidence/planning/pausepressure_g9_claimrate_learning_staged_20260916.md` (generation 9).
- Mint/resolve rates recomputed independently from the chip ledger over 7 weekly windows.
- One live read-only run of the gate (2026-09-17T19:15Z), no `--chip`.

Nothing was built, no chip was closed to move a count, and no threshold was changed. Per the chip's
hard constraints this pass diagnoses only.

---

## 2. The per-generation table

This is the deliverable the chip asked for: for each generation, what was diagnosed, what was
changed, and what the metric did afterwards.

| Gen | Fired | Diagnosed as | What actually changed | What the targeted metric did next |
|-----|-------|--------------|------------------------|-----------------------------------|
| g1 | 08-29 13:32 | -- (no resolution note) | Nothing | `recorded_7d` 716 -> 721 (2nd episode, same generation) |
| g2 | 08-30 15:50 | -- (no note); a curation cycle ran against ~46 authored chips | Nothing in code | Aggregate 704 -> 930 by g3 |
| g3 | 09-02 05:49 | **Un-attributed aggregate**: gate counts every chip with no `origin` filter, so a backlog remedy is handed to a generator problem. Root-cause doc written. | Fix A: `proposal_routine_tick` mint cap. Fix B (`097c5b8cd`): signal 1 split into BACKLOG / GENERATOR arms | Generator side **worked**: aggregate `recorded_7d` 1016 -> 400 by g7, `proposal_tick` share fell below dominance. Authored side **unmoved**: 333 -> 291 -> 300 |
| g4 | 09-02 17:10 | -- (no note) | Nothing. Minted **14 minutes** after g3 was resolved, before Fix B had landed | n/a -- no fix existed to evaluate |
| g5 | 09-03 06:52 | **Hold lane invisible**: chips deliberately parked by a plan of record with a review date still counted as backlog | `7df1f4bdc` hold-lane predicate; generator drivers closed at source (HK-A gate, W5a hysteresis). Resolved "ROOT-CAUSED, no further respec... do not re-fire a generation 6" | Split 93 authored -> 54 actionable + 39 held. Then **decayed**: held count 39 -> 31 -> 26 -> **0** by g8; actionable back to 68-71 |
| g6 | 09-09 01:51 | Backlog genuinely due | User approved "run the curated pause now"; action chip `chip-20260910-curated-pause-window-g6` spawned. No code change | Remedy chip sat **open and unclaimed for ~27h** |
| g7 | 09-11 14:04 | **Duplicate of g6** -- "the remedy was never executed, not that a new decision was needed" | Nothing at the time. Later `e6dff8abd` added a CAPACITY arm (`claim_rate`, stock ratio, new threshold 0.10); `9356d8fe0` redefined `wedge_repairs_7d` from successes to attempts, **deliberately leaving the threshold at 2** | Both changes **added** trips. Wedge went from a structural 0 to 93 against an unchanged ceiling of 2 |
| g8 | 09-14 23:38 | Prior deliverables (g3 doc, g6 agenda) never actioned | Nothing. User asked for a read-only summary into the next cycle | Docs still unreviewed at g10 |
| g9 | 09-16 13:12 | **`claim_rate` is a stock ratio over a 0.3h-turnover pool** -- reads 0-3% even in the healthiest fortnight on record, so it can never go quiet | `57a556395` retyped CAPACITY to a matured 72h claim FLOW, policy-aware, class-split; `421fad278` added inert-slice reading | Held for **one reading**: NOT tripped at g10 (dispatch STOP in force), tripping again 65 minutes later once the lease expired |
| g10 | 09-17 18:13 | Recurrence itself | This pass | -- |

**Read the last column.** Exactly one intervention moved its target and held: the g3 generator fix,
which took the aggregate mint from ~1,000/week to ~400/week. Every other change either moved nothing,
decayed within days, or **added a new permanently-true trip**.

And the arm that has fired on all 15 readings -- `recorded_7d_authored` -- has never been the target
of any of the nine fixes.

### Signal firing frequency across the 15 readings

| Signal | Fired | Share |
|--------|-------|-------|
| S1 rate (`recorded_7d_authored > 150`) | 15/15 | **100%** |
| S1 open (`open_chips_authored > 40`) | 12/15 | 80% |
| S2 episodic (any class at generation >= 2) | 12/15 | 80% |
| S4 enablement (`findings > 0`) | 10/15 | 67% |
| S1 generator (dominant automated origin) | 5/15 | 33% |
| S3 wedge (`wedge_repairs_7d > 2`) | 3/15 | 20% (100% of readings since its 09-14 redefinition) |
| S1c capacity (claim rate / flow) | 2/15 | 13% |

---

## 3. Root cause

Three findings. R1 is why the gate fires; R2 is why it fires *again*; R3 is why nine passes never
reached R1.

### R1 -- The dominant arm measures gross authoring volume against a threshold whose stated premise is net accumulation. It is unconditionally true.

The module docstring says signal 1 is "accumulation outpacing digestion -- the W5b curator's
net-chip-sink metric". The code (`pause_pressure.py:491`) is:

```python
recorded_7d = [c for c in chips if (c.get("spawned_at") or "") >= week_ago]
```

There is no resolution term anywhere. It is gross mint. A system that authors 280 chips a week and
discharges 280 chips a week reads 280, and trips a ceiling of 150, forever.

That is exactly the system's state, and it has been for as long as there is data:

| Week ending | Authored mint | Authored resolve | **Net** |
|---|---|---|---|
| 2026-08-05 | 246 | 245 | **+1** |
| 2026-08-12 | 221 | 219 | **+2** |
| 2026-08-19 | 362 | 308 | **+54** |
| 2026-08-26 | 270 | 291 | **-21** |
| 2026-09-02 | 307 | 312 | **-5** |
| 2026-09-09 | 287 | 263 | **+24** |
| 2026-09-16 | 240 | 221 | **+19** |

Mean net accumulation is **+10.6 chips/week against ~276/week of throughput -- 3.8%**. The most
recent week is +19, and the 7-day window at the time of writing is **-10**. This fleet is in
balance. It has been in balance the whole time. The gate has been reporting a balanced system as an
"accumulation outpacing digestion" excursion for nineteen days.

The threshold cannot be reached. Over 43 daily rolling windows covering all recorded history:

- `recorded_7d_authored`: min **169**, median 287, max 401. Ceiling 150. Windows at or below
  ceiling: **0 of 43**.
- Over the gate's own lifetime only: min **235** (1.6x ceiling), 0 of 19 windows quiet.
- Windows where BOTH signal-1 arms would be quiet: **0 of 43**.

The 150 was set on 2026-08-29 in the gate's birth commit `02163bd0b`, whose own message records that
the very first live reading was PRESSURE at `recorded_7d=715`. The gate fired at birth and was never
silent afterwards.

**This is candidate (a) and candidate (b), and the data separates them.** (b) is false as stated --
the generator does not outrun the fixes; authored mint and authored resolve track each other to
within 4%, and the open authored pool is flat at 50-99 across all ten generations rather than
growing. (a) is true, but not because the denominator is wrong: the 123 unattributed `spawn_task`
chips in the current window are all genuinely distinct substantive work items, spot-checked by title.
The denominator is real. The **ceiling** is the artifact -- it encodes ~21 authored chips/day for a
fleet whose observed floor is ~32/day and whose median is ~41/day.

### R2 -- The generation counter counts resolutions, not recurrences. It is the escalation trigger, and it carries no information about whether any fix worked.

`hygiene_routine_tick._record_episodic_finding` (line 5877) has exactly two branches: if the standing
chip is **open**, append an episode; if it is **resolved**, mint generation N+1. There is no
hysteresis on the metric, no requirement that anything changed, and no minimum interval.

So generation N+1 is created by the act of resolving generation N. Measured, from resolution of gen N
to spawn of gen N+1:

| | g1->g2 | g2->g3 | g3->g4 | g4->g5 | g5->g6 | g6->g7 | g7->g8 | g8->g9 | g9->g10 |
|---|---|---|---|---|---|---|---|---|---|
| Hours | 7.6 | 14.3 | **0.23** | 13.0 | 10.0 | 16.3 | 72.3 | 35.2 | 23.2 |

Median 14.3h; the gate re-fires on the next read after resolution, ten times out of ten. **g4 was
minted 14 minutes after g3 was resolved** -- before the fix g3 commissioned had been written, let
alone landed. g4 was open for 42 minutes. No fix of any kind was evaluated in that interval, and none
could have been.

The consequence is perverse and is the actual engine of this whole episode: **the more promptly and
conscientiously the fleet answers this chip, the higher its generation count climbs -- and the
generation count is what the chip cites as proof that the answers are not working.** A team that
ignored the chip entirely would still be on generation 1.

The chip's generation-10 text reads "That recurrence count says the SYMPTOM fixes are not holding."
It would have read exactly the same if every fix had been perfect.

**This is candidate (c), confirmed, and it is not local to this gate.** `_EPISODIC_PREFIXES` covers
four chip families over 278 standing subjects and **321 generations burned**. Ten subjects have
reached generation >= 2, and `chip-queuefloor-fleet` shows the identical signature independently --
11 generations, with gen 4 resolved 18:47Z and gen 5 minted 18:55Z (8 minutes), gen 5 resolved 03:05Z
and gen 6 minted 03:10Z (5 minutes). Whatever is wrong here is wrong for `refwedge`, `queuefloor` and
`daemondrift` too.

There is also a literal self-latch. `_EPISODIC_PREFIXES` includes `"chip-pausepressure-"` with **no
self-exclusion**, so signal 2 counts the pause-pressure chip itself. This is visible in the data: at
generation 5, four consecutive episodes list `chip-pausepressure-dlaptop-g5` in their own `tripped`
array. Once the gate fires and its chip stays open, it is guaranteed to keep firing on its own
existence. Signal 2's other contributor, `chip-queuefloor-fleet`, has been at generation >= 2
continuously since 2026-08-30, making signal 2 permanently true by a second independent route.

### R3 -- Every learning pass shipped a better measurement; none re-examined the original thresholds. The correct diagnosis was written down at generation 3 and never built.

Six commits to `pause_pressure.py` in nineteen days. Four added arms or reading paths (generator
split, hold lane, capacity arm, inert slices) and two redefined a metric. `git log -S` on each of the
three original threshold constants returns **exactly one commit each -- the birth commit**:

```
OPEN_CHIPS_MAX = 40          02163bd0b (2026-08-29)   never changed
RECORDED_7D_MAX = 150        02163bd0b (2026-08-29)   never changed
WEDGE_REPAIRS_7D_MAX = 2     02163bd0b (2026-08-29)   never changed
```

All three were declared TRIAL values in that commit, with an explicit retune trigger: "expected to be
retuned from the recorded outcomes of the first ~3 governance cycles". Ten generations later the
retune has never happened, and every *new* arm was also declared TRIAL, so the stock of
un-recalibrated trial thresholds has grown monotonically.

The generation-3 root-cause document already named this. Under "Consequences, in order" it lists:

1. "A mint-and-withdraw event inflates the metric for a full 7 days at zero real backlog" -- the
   gross-vs-net defect, R1, stated on 2026-09-02.
2. "The thresholds (40 open, 150/7d) were calibrated before `proposal_tick`, before W5a, and before
   the detector suite reached its current breadth" -- the staleness, R1 again, same day.
3. The un-attributed aggregate.

Only (3) was built. (1) and (2) were written down at generation 3 and are still true at generation
10. That same document also flagged the cost of the route it chose: *"every new arm is another thing
to calibrate."* Four arms later, none calibrated, that is precisely the bill.

The mechanism is structural rather than anyone's oversight. Each generation routes to a learning
pass; a learning pass is scoped to the arm that fired *this time*; its natural output is a
better-specified arm; the better-specified arm is added to a gate whose oldest arm is
unconditionally true, so the next reading is still PRESSURE. The one thing never in scope is the
arm nobody is currently arguing about. **The gate's response loop is structurally incapable of
reaching its own dominant signal.**

The single precedent where this was escaped is instructive and should be the template: at generation
9 the `claim_rate` arm was found to be *structurally unable to go quiet* and was demoted to
report-only. That is the correct treatment. It has simply never been applied to
`recorded_7d_authored`, which fails the identical test far more severely -- `claim_rate` at least
varied.

### R4 -- The wedge arm is a fossil threshold on a duplicated alarm. It does not belong in this gate.

Candidate (d), confirmed on both halves.

**Fossil threshold.** `WEDGE_REPAIRS_7D_MAX = 2` was set for a counter that measured *successful*
repairs -- and `wedge_repairs_7d()`'s own docstring records that of 91, then 121 recorded attempts,
**zero ever succeeded**, because every one is refused by the auto-repair allowlist. The metric was
structurally pinned at 0, which is why the arm read 0 for its first 12 readings. On 2026-09-14 it was
redefined to count attempts, and the docstring states the threshold was left at 2 deliberately
because "a threshold change is a separate decision and would confound the next reading". That
separate decision was never taken. The metric's scale changed by roughly 45x; the ceiling did not
move. It has fired on every reading since (93, 90, 61) and always will.

Note also what the metric now counts: attempts by an auto-repairer that is designed to refuse
essentially all of them. It varies with tick frequency and wedge presence, not with whether wedges
are being fixed. "61 unrepaired" of 61 attempts is the allowlist working as specified, not a
thirty-fold breach of anything.

**Duplicated alarm.** The wedge problem already has a dedicated chip class: `chip-refwedge-*`, 46
chips, 9 generations on `ree-assembly-master` alone, with its own escalation path and its own
learning pass already commissioned (`chip-20260916-refwedge-class-learning-pass`). The same problem
additionally enters this gate through signal 2, since `chip-refwedge-...-g4` and `-g7` appear in the
episodic-generation lists. So one underlying problem is counted **three times** -- its own class,
signal 2, and signal 3 -- and only the first of those has an owner who can act on it.

---

## 4. Verdict on the four candidate causes

| | Candidate | Verdict |
|---|---|---|
| (a) | Ceilings mis-calibrated; gate reports steady state as excursion | **CONFIRMED, primary.** 0 of 43 windows below ceiling. But not via the denominator: the "38 other" authored chips are real distinct work. The ceiling is the artifact, and the metric is gross where its premise is net. |
| (b) | Generator outruns any discharge rate a fix can buy | **REFUTED.** Mint and resolve track within 3.8%; the open authored pool is flat at 50-99 across all ten generations. The one generator fix that was built (g3) worked and held -- aggregate mint fell ~1,000 -> ~400/week. |
| (c) | Resolution semantics guarantee re-firing; "generation" measures elapsed time | **CONFIRMED, and stronger than stated.** It measures *responsiveness*, not elapsed time: generation N+1 is minted by the act of resolving N (median 14.3h, minimum 14 minutes). Defect is in shared machinery affecting 4 chip families / 321 generations, plus a literal self-latch via the missing self-exclusion in `_EPISODIC_PREFIXES`. |
| (d) | Wedge arm is an independent, larger problem wearing this gate's clothing | **CONFIRMED.** Fossil threshold (set for a metric that could only read 0), and triple-counted against a dedicated chip class that already owns it. Does not belong in this gate. |

---

## 5. What this says about the ten generations

There was never a structural pause window due, on the gate's own stated premise. Had signal 1 been
built as the net-accumulation metric its docstring describes, with any reasonable threshold, it would
have fired at most once in seven weeks (week ending 2026-08-19, net +54) and never twice
consecutively.

The nine fixes did not fail. Seven of them were not fixes at all -- they were answers to a question,
correctly given. Two were real engineering (the g3 generator cap, the g9 capacity retype) and both
did what they claimed. What failed is the gate, which asked an unanswerable question ten times, and
the generation counter, which converted each answer into evidence that answering was not working.

---

## 6. Recommendation

**Retire the PRESSURE verdict in its present form.** Concretely, four changes, in priority order.
None is built here; all are consent-gated.

**REC-1 (highest leverage, and not in this gate) -- fix the generation counter.**
In `hygiene_routine_tick._record_episodic_finding`, do not mint generation N+1 on the next reading
after a resolution. Require *either* that the finding's payload materially changed, *or* a minimum
quiet interval (a re-fire inside ~24h of a resolution is an episode on the resolved chip, or a
re-open, not a new generation). Add `"chip-pausepressure-"` self-exclusion to signal 2's scan, or
better, exclude the evaluating chip's own base ref generically. This benefits `queuefloor`,
`refwedge` and `daemondrift` identically and is the only change here that stops the escalation
engine rather than one of its inputs.

**REC-2 -- demote signals 1-open, 1-rate, 2 and 4 to REPORT-ONLY.**
This is exactly the treatment generation 9 gave `claim_rate`, on exactly the same finding, and it is
the only remedy in this history that has held. All four are structurally-always-true against their
current thresholds; all four are genuinely useful as *dashboard* numbers. Keep printing them; stop
tripping on them. Signal 4 additionally has an unfixed measurement defect flagged at g3 (an ssh
error string split across three rows and counted as three findings) sitting behind a zero-tolerance
`> 0` threshold.

**REC-3 -- if a backlog trip is wanted at all, re-specify it as NET and replace the gross arm.**
Do not add it alongside; the whole finding of R3 is that adding arms is the failure mode. Net
authored accumulation over a trailing window, tripping only on sustained positive drift (illustrative:
net > +50/week for two consecutive weeks -- zero firings in the last seven weeks, one non-consecutive
+54). This restores the docstring's actual stated premise. A calibration-only change to
`RECORDED_7D_MAX` is **not** recommended as the primary route: it would buy one quiet week and then
drift, because the metric would still be gross.

**REC-4 -- remove signal 3 (wedge) from this gate entirely.**
Route it to the `chip-refwedge-*` class that already owns the problem and already has a learning pass
commissioned. If a wedge signal is wanted here at all it must first get a threshold matched to the
post-2026-09-14 definition, but the duplication argument stands on its own regardless.

**What is left tripping:** the capacity arm (`claim_flow_72h`), which is the only signal in this gate
with demonstrated two-regime discrimination (healthy 77-92%, collapsed 39-59%, nine and six samples
respectively) and a replay table behind it. It is worth noting that it tripped at the live reading
taken for this pass -- 57% with the dispatch STOP expired -- and that the gate's own verdict line for
it already says *"a pause window is NOT indicated for this arm"*. Even the one working signal is not
asking for the thing this gate was built to recommend.

If the user prefers the shortest route: **REC-1 plus REC-2 alone** would have left this gate silent
for its entire nineteen-day life while preserving every number it reports, and would end the
recurrence for the other nine standing subjects as well.

---

## 7. GOV-HELDOUT-1

This artifact changes no standing rule, skill or `CLAUDE.md` text, so the held-out check is not owed
*by this document*. It will be owed by whichever recommendation is ratified, and REC-1 in particular
touches shared fleet machinery.

The replay evidence is nonetheless already assembled and is recorded here so the check is cheap when
it comes: the 15-reading table in section 2, the 43-window distribution in R1, and the nine
resolution-to-re-fire intervals in R2 are all cases the recommendations were not written from in the
sense that matters -- they are the gate's own history, and for each one the old wording (PRESSURE,
new generation) and the proposed wording (report-only / no new generation) give **different**
answers. Non-degeneracy is satisfied on all 15 readings for REC-2 and on 9 of 9 intervals for REC-1.

A negative control worth preserving for that check: the generation-3 generator fix. Under both old
and proposed wording that intervention is correct and still recommended -- the generator arm keeps
its trip, because it is the one signal-1 arm that has actually decayed as the problem was fixed.

---

## 8. What was NOT done here, deliberately

- **No backlog curation, no chips closed, no ceilings changed.** The chip forbade all three and they
  are the instance fix this pass exists to avoid.
- **Nothing built.** All four recommendations touch shared fleet machinery under `scripts/`;
  `/metaworker-learning` Step 4 admits no obviously-safe carve-out for that.
- **`chip-queuefloor-fleet-g11` left open.** It is at generation 11 with the same signature and is
  the second-strongest evidence for REC-1, but it is a separate subject with its own owner.
- **The g3 doc's signal-4 measurement defect not chased.** Still unfixed, still inflating signal 4,
  still a separate and smaller problem. Named again here so the next reader does not re-diagnose it
  a third time.
- **The g6 curated agenda and the g3 root-cause doc remain unreviewed**, which is what generation 8
  was resolved pending. That is a live thread this pass does not close.
