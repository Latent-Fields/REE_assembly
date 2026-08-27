# Morning-digest scheduler misfire: ROOT CAUSE FOUND (account/org profile outage)

**Status: AWAITING USER REVIEW. Nothing in this file has been written to claims.yaml or any
other registry. One live action is recommended in section 8 and has NOT been taken.**

Chip: `chip-20260823-morning-digest-scheduler-misfire`
Session: `metaworker-chip-20260823-morning-digest-scheduler-misfire`
Measured: 2026-08-27T07:24Z - 07:34Z, DLAPTOP.
Reproduce:
```bash
/opt/local/bin/python3 /Users/dgolden/REE_Working/scripts/audit_scheduled_task_fires.py \
  --task ree-morning-digest --scheduler-log --profiles
```

---

## 1. Summary

The morning digest's repeated silent misses are **not** caused by the Mac sleeping (already
refuted twice by `pmset`), nor by a late fire alone, nor by a held lock. The cause is:

> **The Claude DESKTOP APP's scheduled-task subsystem is scoped to a single
> `(accountId, orgId)` profile. While the app is signed in under any other profile, the
> scheduler dispatches nothing at all and writes no log line at all -- a completely silent
> outage. `ree-morning-digest` is owned by one profile; the app is regularly switched away
> from it and left there for days.**

This is confirmed on **three separate occurrences**, one of which is **live right now**.

A second, independent mechanism compounds it: the scheduler is an **app** component, not a
system cron, and a fire missed while it is not dispatching is re-issued at the next
opportunity as a `missed:` **catch-up**, typically many hours late -- which the digest's own
Check-1 stale-skip guard then correctly kills. Every guard behaves exactly as designed and
the net result is still no agenda.

## 2. The measurement that was missing (again)

Both prior investigations recorded that no scheduler-side record exists:

* `chip-20260809-morning-digest-gap-detection` and the morning-digest SKILL.md:
  *"No run log is kept for scheduled tasks (`~/.claude/scheduled-tasks/<name>/` holds only
  `SKILL.md`), so scheduler-side causes are not currently establishable after the fact."*
* `morning_digest_firing_diagnosis_20260818.md` S2 built the transcript-based fire log
  instead, and closed with the honest limit that a day with **no transcript at all** is
  unexplainable.

Both are wrong about the record's existence. **The Claude desktop app logs its own dispatch
decisions** to `~/Library/Logs/Claude/main*.log`, tagged `[CCDScheduledTasks]`:

```
2026-08-18 05:07:17 [info] [CCDScheduledTasks] Delaying dispatch for ree-morning-digest by 583s (jitter)
2026-08-18 05:17:00 [info] [CCDScheduledTasks] Spawning new session for scheduled task ree-morning-digest
                          { cronExpression: '7 5 * * 1-5', fireAt: undefined,
                            lastRunAt: '2026-08-17T04:17:40.227Z', missed: undefined }
2026-08-18 05:17:01 [info] [CCDScheduledTasks] Confirmed task run for: ree-morning-digest
```

It records the jitter delay, on-time vs `missed:` catch-up dispatch, `Skipping dispatch ... :
<reason>` (with `global_limit` / `per_task_limit`), `Deferring check: <reason>` (post-wake
delay, `net.isOnline() is false`), and -- the load-bearing one -- the `accountId`/`orgId` the
scheduler was initialised under.

This is the **complement** of the transcript source, not a replacement: transcripts show what
a fire *did*; this shows whether a fire was *issued at all*, and why not. Retention is ~2-3
weeks across the rotated `main*.log` set, so like `pmset` it adjudicates only recent gaps.

Landed with this document: `REE_Working/scripts/audit_scheduled_task_fires.py --scheduler-log`
(extends the existing transcript auditor rather than duplicating it).

## 3. The discriminator: 40 of 40 dispatches under one profile

Over the full retained log window (2026-08-06 20:26 -> 2026-08-27, 1307 `[CCDScheduledTasks]`
lines, deduped and time-sorted across `main.log` .. `main4.log`), every dispatch of every
scheduled task occurred under exactly one profile:

| accountId | orgId | initialisations | dispatches |
|---|---|---:|---:|
| `e6c369d5` | `327a6a20` | 8 | **40** |
| `5879f72b` | `eceb62e1` | 10 | 0 |
| `06c66487` | `96721d82` | 5 | 0 |
| `5879f72b` | `327a6a20` | 3 | 0 |
| `06c66487` | `327a6a20` | 2 | 0 |
| `e6c369d5` | `eceb62e1` | 2 | 0 |
| `e6c369d5` | `96721d82` | 1 | 0 |

**Six non-owning profiles, 23 initialisations between them, zero dispatches** -- and zero
skips, zero deferrals, zero lines of any kind naming a task. The outage is not merely silent
to the user; it is silent in the log too. Only the `Initialized { accountId, orgId }` line
marks the transition.

Note also that **both** `accountId` and `orgId` must match: `e6c369d5` paired with `eceb62e1`
or `96721d82` dispatches nothing, and so does `5879f72b` paired with the correct org
`327a6a20`.

## 4. The 2026-08-19..21 gap (the chip's motivating incident)

Prior agenda `2026-08-18T22:04Z`; next agenda a manual out-of-slot run on 2026-08-23.

| date | day | scheduled? | what the scheduler log shows | outcome |
|---|---|---|---|---|
| 08-18 | Tue | yes | jitter 583s -> dispatch 05:17 on-time -> confirmed | **RAN** (last good run) |
| 08-18 23:30 | -- | -- | `Initialized` -> `5879f72b`/`eceb62e1` | **profile switched away** |
| 08-19 | Wed | yes | *nothing at all* (app initialised 22:38 under `5879f72b`/`eceb62e1`) | lost silently |
| 08-20 | Thu | yes | *nothing at all* (app initialised 19:46 under `5879f72b`/`eceb62e1`) | lost silently |
| 08-21 | Fri | yes | *nothing at 05:07* | lost at the slot |
| 08-21 18:58 | -- | -- | `Initialized` -> `e6c369d5`/`327a6a20`; within 5s three catch-ups dispatched | see below |
| 08-22 | Sat | **NO** | cron is `7 5 * * 1-5` | **never due** |
| 08-23 | Sun | **NO** | cron is `7 5 * * 1-5` | **never due** |
| 08-24 | Mon | yes | catch-up dispatch 05:11, 4 min late | **RAN** |

The 08-21 18:58 catch-up, verbatim:

```
2026-08-21 18:58:04 Spawning new session for scheduled task ree-morning-digest
   { cronExpression: '7 5 * * 1-5', lastRunAt: '2026-08-21T17:58:04.094Z',
     missed: '2026-08-21T04:07:00.000Z' }
```

**831 minutes late.** Check-1 computes `delta = 1138 - 307 = 831 > 60` and emits `STALE_SKIP`.
The guard was correct -- overwriting a fresh agenda with a 14-hour-late one is exactly what it
exists to prevent -- and the day still produced nothing.

Two further details worth keeping:

* The catch-up queue carries only the **most recent** missed slot per task, not one per missed
  day. 08-19 and 08-20 were never re-issued in any form.
* Alongside the digest, `ree-lit-pull-am` (missed 08-21T06:00Z) and `ree-evening-sync` (missed
  08-20T16:47Z) were dispatched in the same 5-second burst, and
  `nightly-documentation-update` was **`Skipping dispatch ... global_limit (active=3,
  limit=3)`** -- a concurrency cap of 3 that the catch-up burst saturates. It re-dispatched a
  minute later, so nothing was lost here, but a larger burst could drop work.

## 5. Independent confirmation on the earlier gap -- and a correction to the record

The 2026-08-10..14 gap (5 days, the one the 2026-08-15 digest used to refute the sleep
hypothesis) has the **identical signature**:

| when | event |
|---|---|
| 2026-08-09 18:21 | `Initialized` -> `06c66487`/`96721d82` -- switched away |
| 08-10 .. 08-13 05:07 | *nothing at all* |
| 2026-08-13 22:02 | `Initialized` -> `e6c369d5`/`327a6a20`; catch-up dispatched, **1015 min late** -> `STALE_SKIP` |
| 2026-08-14 00:53 | `Initialized` -> `5879f72b`/`eceb62e1` -- switched away again |
| 08-14 05:07 | *nothing at all* |
| 2026-08-15 05:35 | `Initialized` -> `e6c369d5`/`327a6a20`; catch-up, **28 min late** -> `TIME_OK` -> **RAN** |

Confirmed independently in the session transcripts: `2026-08-15T04:35:54Z TIME_OK: delta=28min`
and `2026-08-24T04:11:47Z TIME_OK: delta=4min`, matching the two catch-up dispatches that
landed inside the window.

**This resolves two things previously left open:**

1. `morning_digest_firing_diagnosis_20260818.md` S1 flagged as an unresolved caveat that the
   digest fired on **Saturday 2026-08-15**, which a weekday-only cron should not do, and
   guessed *"the most likely reading is that the harness deferred a missed weekday fire into
   Saturday morning ... This was not conclusively established."* **That guess was correct and
   is now established**: it is the `missed: 2026-08-14T04:07:00.000Z` catch-up dispatched at
   05:35 when the profile was switched back.
2. That same document attributed the 08-10..14 misses to *"the Mac was asleep 08-10..08-14"*
   and recorded that a `pmset` RTC wake fix was *"applied and still in force"*. **The sleep
   attribution is refuted** -- consistent with what the morning-digest SKILL.md already said
   for that exact window from `pmset` evidence, and now with a positive cause in its place.
   The RTC wake remains harmless insurance for genuine battery/clamshell sleeps; it is not
   the fix and never was.

## 6. THERE IS A LIVE GAP RIGHT NOW (2026-08-25, 08-26, 08-27)

Last agenda commit: `REE_assembly 1b3dac56a7`, **2026-08-24T05:39+01:00**. Today is Thursday
2026-08-27. **Three weekday slots have been missed and the third was this morning.**

The scheduler log's final entry of any kind is:

```
2026-08-24 22:23:44 [info] [CCDScheduledTasks] Initialized
    { accountId: '5879f72b-b3ba-4218-a22c-0d7bb47cd3b7', orgId: 'eceb62e1-8bcc-4d4f-9e98-5836f4bb0a22' }
```

-- a **zero-dispatch profile**. Since that moment there has been no dispatch, no skip, no
deferral, no tick.

This is not an app that was closed. `ps -p 98261 -o lstart=` gives **`Sun Aug 23 20:04:42
2026`, elapsed `03-12:28:43`** -- the desktop app has been running **continuously for over
three days**, straight through all three missed slots. `main1.log` rotated to `main.log` at
2026-08-27 01:55 purely on size (10 MB), not on a restart, and `main.log` contains **zero**
`[CCDScheduledTasks]` lines.

**This refutes candidate (a) as the chip stated it** ("the Claude app was not running at the
fire time"). The app running is not sufficient. The condition is that the app's **active
account/org profile** is the one that owns the task.

## 7. Corrections to the chip brief's premises

* **"08-19, 08-20, 08-21 and 08-22 all fired and produced nothing."** 08-22 was a **Saturday**
  and the cron is `7 5 * * 1-5`; no fire was due and none was issued. Only three weekday slots
  were missed, not four. (This is the second time a weekend day has been miscounted as a
  missed fire -- `chip-20260816-morningdigest-missed-firing-window` falsified the same premise
  for Sunday 2026-08-16. Check the day of week before counting a gap.)
* **"there is NO run log"** -- there is; see section 2.
* **Candidate (a) "the Claude app was not running"** -- refuted as stated; see section 6.
* **Candidate (b) "fired late and Check-1 aborted it"** -- **confirmed**, for 08-21 and 08-13,
  as the downstream half of the profile outage rather than as an independent cause.
* **Candidate (c) "Check-2 lock held"** -- no `CONCURRENT_SKIP` appears in any transcript or
  scheduler-log line across the whole retained window. Not implicated.
* **Candidate (d) "the scheduler did not fire at all"** -- **confirmed**, and now explained.

## 8. Recommended action (NOT taken -- needs the user)

**Switch the Claude desktop app back to the account/org that owns the scheduled tasks**
(`accountId 5879f72b...` -> `e6c369d5-ce3c-4248-ab6d-080542d56734`, `orgId eceb62e1...` ->
`327a6a20-b9fa-4854-944e-e27d8ac20069`) and confirm a `[CCDScheduledTasks] Initialized` line
with that pair appears. This is a live UI action on the user's own accounts and was
deliberately left for the user rather than guessed at.

Expect a catch-up burst on the switch, and expect the digest's share of it to `STALE_SKIP` --
that is correct behaviour, not a second fault. A same-day agenda then needs a manual
`/morning-digest` run.

**Not recommended: widening the Check-1 window** (chip suggested-work item 3). The evidence is
against it. Of the seven digest dispatches in the retained window, only two were on-time; the
five catch-ups were +4, +28, +286, +831 and +1015 minutes. A +60 ceiling admits the two useful
ones and rejects three that are 5-17 hours stale, which is precisely the discrimination
wanted. Widening far enough to catch an 831-minute catch-up would mean accepting an evening
"morning" agenda. The one genuinely marginal case in the whole record remains
**2026-07-28 at +67 min** (7 minutes past the boundary), already flagged for the user by
`morning_digest_firing_diagnosis_20260818.md` and still unresolved; note the standing jitter
is up to 583s (~10 min), so the effective ceiling is ~50 min of real lateness.

**Also not recommended: a self-written run log in the scheduled task's SKILL.md** (chip
suggested-work item 1). It cannot observe any of the three confirmed causes. A profile outage
means the session never starts, so nothing it could write ever executes; the same is true of
the usage-limit refusals that `morning_digest_firing_diagnosis_20260818.md` measured at 40% of
fires, which kill the session before its first Bash call. The scheduler log already records
the dispatch side, and the transcript auditor already records the execution side. A third
log would add cost and cover nothing the other two miss.

## 9. What this does not establish

* `pmset` and the app log both retain ~1-3 weeks. The 11-day (2026-08-09), 8-day
  (2026-07-29) and 6-day (2026-07-08, 2026-06-16) gaps are **outside both horizons** and
  remain unadjudicated. The profile mechanism is a plausible explanation for them and is
  explicitly **not** asserted for them here.
* Why the profile gets switched, and whether it is a deliberate user action or the app
  re-selecting a profile on its own, is not established. The log shows only the transition.
* The `global_limit (active=3, limit=3)` cap is documented above as observed; it has not been
  shown to have dropped any digest run.
