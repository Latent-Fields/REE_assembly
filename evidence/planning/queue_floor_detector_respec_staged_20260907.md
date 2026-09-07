# Queue-floor detector: root-cause respec (generation 9)

**Status: AWAITING USER REVIEW**

Session `objective-hamilton-1d00ce` | `/metaworker-learning` | 2026-09-07T23:1xZ
Chip: `chip-20260907-queuefloor-detector-respec` (routed from `chip-queuefloor-fleet-g8`)

---

## Summary

The queue-floor detector is **correct and should not be re-specified**. The floor of 3 is
right, the alarm is TRUE, and the condition it reports is real and worsening.

The defect is one level up, in the episodic-chip machinery that CARRIES the finding:
**`_hygiene_resolution` reads absence-of-observation as absence-of-condition.** Six of the
seven queue-floor generation resolutions closed a standing chip as "quiet" while the queue
was continuously below its floor -- one of them while the queue sat at depth **0** for the
entire "quiet" window. The generation counter is therefore measuring gaps in the hygiene
tick's own observation record, not recurrence of a fault, and the `g3` escalation to
`/metaworker-learning` has fired seven times on a class that never recurred because it never
left.

This is the same error class as the standing memory `feedback_heartbeat_stale_not_abandoned`
("absence is not abandonment"), in a different subsystem.

The chip's own proposed root cause -- that the floor is an over-tight stock threshold whose
preemption has been throttling housekeeping dispatch -- is **REFUTED on four independent
grounds** below, and one of its supporting statistics is a measurement artifact that
understates the real condition by 6.5x.

---

## 1. What was re-measured (independently, not trusting the chip's numbers)

Walked all 253 revisions of `ree-v3/experiment_queue.json` on `origin/main`,
2026-08-20T06:34Z -> 2026-09-07T17:13Z (442.7h / 18.44 days), scoring each with
`check_experiment_queue_floor.queue_state()`'s own predicate.

| quantity | chip g8 said | re-measured | verdict |
|---|---|---|---|
| below floor 3 | 88% (356.8h) | **88.9%** (393.7h of 442.7h) | CONFIRMED |
| median depth | 2 | 2 (sample), 1 (time-weighted) | CONFIRMED |
| max depth | 8 | 8 | CONFIRMED |
| authoring rate | ~4.3 new queue_ids/day | **4.34/day** (80 ids / 18.44d) | CONFIRMED |
| at depth 0 | "17/242 samples (7%)" | 7.1% of samples, **46.3% of wall-clock** | **CORRECTED** |

### 1a. The depth-0 statistic is a sample-weighting artifact

Revisions of the queue file are not a uniform time sample. The queue file is committed when
it CHANGES -- claims, completions, appends. When the queue is empty nothing changes it, so
an empty queue generates almost no commits while consuming large amounts of wall-clock.
Sample-weighting therefore systematically under-counts exactly the state that costs the most.

Time-weighted depth histogram over the 442.7h window:

```
depth  0 : 205.1h (46.3%)      depth  4 :  10.0h ( 2.2%)
depth  1 : 157.9h (35.7%)      depth  5 :  13.6h ( 3.1%)
depth  2 :  30.7h ( 6.9%)      depth  6 :   3.8h ( 0.9%)
depth  3 :  16.9h ( 3.8%)      depth  7 :   3.8h ( 0.9%)
                               depth  8 :   0.9h ( 0.2%)
```

**The experiment queue was completely empty for 46.3% of the last 18 days**, not 7%. The
chip's argument for re-specifying the detector against worker idleness rests on depth-0 being
"12x rarer than the floor breach"; it is roughly half as common, not a twelfth. That premise
does not survive correct weighting, and it points the opposite way: the floor is not
over-tight, it is detecting a genuinely severe condition.

### 1b. Corroborating outcome measure

Experiment result manifests newly added to `REE_assembly/evidence/experiments`:

- 2026-08-01..08-19 (pre-window): 341 manifests over 19 active days = **17.9/day**
- 2026-08-20..09-07 (window):     166 manifests over 18 active days = **9.2/day**

Scientific output roughly halved across the window in which the queue was starved 88.9% of
the time. Stated as co-occurrence, not proven causation -- but it is the direction that makes
silencing the alarm the wrong move.

---

## 2. REFUTATION of the chip's causal claim

The chip asked to confirm or refute: *"the detector that fires 88% of the time is also the
switch that stops the housekeeping backlog being worked."* **Refuted.** Four independent
grounds, any one of which is sufficient.

**(a) Scope.** `dispatch_budget_gate.budget_verdict()` withholds only chips whose
`dispatch_candidate_order.budget_category()` is `housekeeping`, which by that function's own
rule requires a positive `origin == hygiene_tick` classification AND not being
`is_critical_housekeeping` (those ride in the `default` band, uncapped). Run over the live
open ledger: of **104 open chips**, `housekeeping` = **4**, `science` = 48, `default` = 52.
The preemption's maximum possible blast radius is 4 chips. It cannot gate a large backlog
because almost nothing is in its scope.

**(b) No observed withhold.** The dispatch budget log (`metaworker_dispatch_budget_log.json`,
314 events, 2026-08-25 -> 2026-09-02) records exactly 8 `housekeeping`-category worker
dispatches, all on 2026-09-02. Cross-referencing each against the reconstructed queue depth
at that instant: they occurred at depth **6, 6, 6, 4, 3, 3, 3, 3** -- every one at or ABOVE
the floor. There is no observed instance of the preemption withholding anything.

**(c) The backlog drained.** Over the same 18-day window, `hygiene_tick`-origin chips were
spawned 706 and resolved 718 -- a **net drain of 12**. Of 966 such chips ever minted, **5**
are open. Housekeeping was not accumulating while the floor alarm stood.

**(d) The number "~280" is a mis-citation.** Traced through `WORKSPACE_STATE.md`: "~280"
first appears 2026-09-03 as the TOTAL open-chip count, used as the corpus size `n` for a
duplicate-detection `df_cap`, with no housekeeping filtering. The same log re-uses it as a
raw shrinkage figure ("the backlog shrank 280 -> 108"). Only in g8's resolution note is it
relabelled "the ~280-chip housekeeping backlog". There has been no such backlog; the
housekeeping-specific open count is 4.

**(e) Additional, decisive for the recent period.** All three dispatchers have carried
`requested_state: "stop"` since 2026-09-03T01:03Z (`local` since 2026-08-30T06:33Z), and the
last dispatch event of any kind is 2026-09-02T23:45Z. For the last five days nothing was
dispatched by any mechanism, preemption or otherwise.

The preemption is not harmful. It is very nearly inert. **No change is recommended to it on
the grounds the chip proposed**, and the claim in the chip prompt template that "non-critical
housekeeping dispatch is preempted until this clears" overstates a 4-chip effect and should
be corrected, since it is what made this chip's premise wrong.

---

## 3. ROOT CAUSE: resolution reads silence as remedy

`_hygiene_resolution` (`scripts/hygiene_routine_tick.py`) resolves a standing episodic chip
when its class has been "quiet for `_EPISODIC_HYSTERESIS_HOURS` (6.0) past its last episode".
**Quiet means no episode was recorded. It does not mean the condition was observed to be
absent.** When the hygiene tick does not run -- or runs and its episode write is dropped (the
episode verb is coordinator-only by design, with no git fallback) -- the class reads as quiet
and the standing chip resolves itself.

For each queue-floor generation, the queue depth over the 6h window it resolved on:

| gen | resolved_at | queue depth min/max in window | hours at/above floor | tick events in window |
|---|---|---|---|---|
| g1 | 2026-08-30T09:54:33Z | 2 / 3 | 0.21 of 6 | 4 |
| g3 | 2026-09-03T03:30:40Z | 3 / 8 | **6.00 of 6** | 6 |
| g4 | 2026-09-03T18:47:07Z | 0 / 2 | 0.00 of 6 | 3 |
| g5 | 2026-09-04T03:05:37Z | 1 / 3 | 0.30 of 6 | 3 |
| g6 | 2026-09-04T09:23:06Z | 0 / 3 | 0.04 of 6 | 2 |
| g7 | 2026-09-04T19:19:11Z | **0 / 0** | 0.00 of 6 | **0** |
| g8 | 2026-09-07T22:23:16Z | 1 / 2 | 0.00 | 0.8h span |

**g3 is the only legitimate resolution in the series.** g7 resolved with the note "episodic
class quiet for 9.8h" while the experiment queue was at depth ZERO for that entire window and
the tick recorded no observations at all.

This explains every symptom the previous eight generations chased:

- the 233 auto-notes read "finding no longer **REPORTED** by its audit -- remedied"; the note
  says exactly what happened, and "remedied" is the unwarranted inference;
- the median gap between one generation resolving and the next spawning is **7.2 minutes** --
  the tick resumes, immediately re-observes the same standing condition, and mints `gN+1`;
- nothing was ever fixed because nothing was ever broken-then-repaired;
- the `g3` escalation to `/metaworker-learning` fired seven times while counting observation
  gaps rather than failed fixes -- it has now consumed two full root-cause sessions (g8 and
  this one).

### 3a. The separation is clean and measurable

Median refire gap (spawn of `gN+1` minus resolve of `gN`), by episodic class:

| class | n | median refire gap | min | max |
|---|---|---|---|---|
| **chip-queuefloor-** | 8 | **7.2 min** | 2.5 min | 546 min |
| chip-daemondrift- | 3 | 5,471 min (91h) | 1,439 min | 7,228 min |
| chip-checkoutdiverged- | 2 | 6,097 min (102h) | 1,037 min | 11,157 min |
| chip-refwedge- | 2 | 21,403 min (357h) | 16,792 min | 26,015 min |

Three orders of magnitude, with **no overlap**: queuefloor's maximum (546 min) sits below
every other class's minimum (1,037 min). CONTINUATION and RECURRENCE are empirically
separable in this data, and the machinery currently cannot tell them apart.

---

## 4. Proposed fix (narrow)

**Resolve a standing episodic chip on a POSITIVE observation that the condition is absent,
never on the absence of an episode.**

Concretely, in `scripts/hygiene_routine_tick.py`:

1. `_hygiene_resolution`'s hysteresis clock counts **clean observations**, not elapsed
   wall-clock. A class is "quiet" only across ticks in which its source actually RAN and
   positively reported no finding.
2. The signal already exists and needs no new plumbing: the tick's `sources[<name>]` meta
   dict already carries `scan_ok`, and `_experiment_queue_floor_findings` already returns
   `{"scan_ok": True, "starved": False, ...}` -- which is precisely "I looked, and it is
   fine", distinct from "I did not look".
3. A class that cannot supply such a signal keeps today's behaviour (fail-open, unchanged).

Deliberately NOT proposed: changing the floor value, retiring the detector, re-specifying it
against worker idleness, or severing it from `dispatch_budget_gate`. Sections 1 and 2 refute
the grounds for each.

Expected effect: `chip-queuefloor-fleet` becomes ONE standing chip that stays open while the
condition holds, instead of `g10, g11, g12...`; the `/metaworker-learning` escalation returns
to meaning "this was fixed and broke again N times".

---

## 5. Held-out check (GOV-HELDOUT-1)

Tested against historical cases from the OTHER three episodic classes -- the rule was written
from queuefloor and none of these. Non-degenerate (old and new give DIFFERENT answers):

**HO-1 -- `chip-refwedge-dlaptop-ree-assembly-master`**, resolved 2026-09-01T03:03:46Z, note
"episodic class quiet for 7.8h", **0 tick observations in the prior 6h**. OLD: resolves. NEW:
does not resolve (no clean observation). Right call: the wedge was never verified cleared.

**HO-2 -- `chip-daemondrift-ree-cloud-1-ree-explorer`**, resolved 2026-09-02T16:37:33Z, note
"episodic class quiet for 7.7h", **0 tick observations in the prior 6h**. OLD: resolves, then
mints g2 (2026-09-04, also on a silence-resolution) and g3, which is OPEN now and has reached
the `/metaworker-learning` escalation threshold. NEW: stays as one open standing chip; no g2,
no g3, no escalation. Right call, and it shows daemondrift is on the same trajectory as
queuefloor, just slower -- this fix pre-empts generation 9 of a second class.

**HO-3 -- `chip-checkoutdiverged-dlaptop-ree-working-master-g2`**, resolved 2026-09-06T20:49:10Z,
note "episodic class quiet for 6.3h", 2 tick observations in the prior 6h. OLD: resolves on
elapsed time. NEW: resolves only if those 2 observations were positively clean -- a weaker
but non-vacuous gate. Borderline by design; it is the case that shows the rule is a gate on
evidence, not a blanket refusal to resolve.

**Non-misfire confirmation.** Every resolution in the corpus carrying a substantive human
verification note -- "Cleared via chip-20260826-cloud4-refwedge-authorise-adopt: user-author...",
"REPAIRED (user-authorized, session elated-nobel-914234). 14.7h wedge...", "Wedge confirmed
CLEARED. Independently verified via 'ref_convergence.py'..." -- had 2 to 47 tick observations
in its window and an explicit positive check. The new rule leaves all of them untouched. The
failure mode GOV-HELDOUT-1 exists to catch (a rule derived from one incident that misfires on
others) does not occur here across 20+ examined resolutions.

**Honest counterweight.** (i) This check cost roughly an hour of measurement, and the
tick-liveness proxy (counting `hygiene_tick`-origin chip spawns in a window) is a proxy: it
establishes the tick was minting chips, not that this specific source ran and evaluated
cleanly. That is precisely the signal the fix would start recording, so the fix improves the
evidence available to its own future audits. (ii) Making resolution stricter means standing
chips stay open longer, and a chip that never closes is its own kind of noise -- the mitigation
is that it stays ONE chip rather than a generation series, but this is a real trade and the
user should weigh it. (iii) Sections 1-3 are strongly evidenced; the fix in section 4 is a
design proposal that has not been built or tested.

---

## 6. The finding that is not a tooling fix

Authoring throughput is the real problem, and it is the one thing eight generations never
addressed. 4.34 new queue entries/day, consumed at the same rate, zero buffer, empty queue for
46.3% of wall-clock, manifests down from 17.9/day to 9.2/day. No change to a detector alters
any of that.

This is reported, deliberately NOT chipped. A chip saying "author more experiments" would be
generation 10 in a different costume: the queue-floor chip already says exactly that, has said
it 246 times, and the saying is not the constraint. What would have to change for option (d)
to be real is a decision about research direction and cadence, which belongs to the user, not
to the metaworker machinery.

---

## 7. Decision required

Nothing has been landed. Per `/metaworker-learning` Step 4 this cannot be self-approved.
Options, in the decision chip:

- **A (recommended)** -- build the section 4 fix: observation-gated resolution for episodic
  standing chips. Narrow, held-out-checked, fixes queuefloor and daemondrift together.
- **B** -- correct the false "housekeeping dispatch is preempted" claim in the queue-floor
  chip prompt and g8-style notes, and stop there. Cheapest; leaves the generation churn.
- **C** -- A + B.
- **D** -- hold: do nothing to the machinery, accept the churn, and treat section 6 as the
  only real item.

Explicitly NOT offered, because the evidence refutes them: lowering or retiring the floor,
re-specifying it against worker idleness, or severing it from `dispatch_budget_gate`.
