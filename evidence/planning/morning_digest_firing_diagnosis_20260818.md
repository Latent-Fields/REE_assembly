# Morning-digest firing diagnosis (chip-20260816-morningdigest-missed-firing-window)

**Status: DIAGNOSIS COMPLETE. No change was made to the stale-skip window, and nothing
in this file has been applied to any registry, skill, or scheduled-task definition.**

Session: `metaworker-chip-20260816-morningdigest-missed-firing-window`
Measured: 2026-08-18T03:04Z - 04:40Z, DLAPTOP.
Tool (landed with this): `REE_Working/scripts/audit_scheduled_task_fires.py`
Reproduce: `/opt/local/bin/python3 scripts/audit_scheduled_task_fires.py --task ree-morning-digest`

---

## 1. The chip's premise is FALSIFIED: 2026-08-16 was a SUNDAY

The chip reported "no agenda for 2026-08-16" as a missed firing window. **2026-08-16 was a
Sunday**, and the task's own definition is `description: REE morning digest -- weekdays 5:07am`.
There is no fire record for 2026-08-16 because none was due. The next weekday, **Monday
2026-08-17, fired at 05:17 local (delta=+10 min, inside the window), ran, and committed an
agenda** (`REE_assembly` `5122bf373b`, generated 04:23:27Z).

The chip's supporting inference -- that the session alive at 09:16Z "was ~5h9m past the slot,
so the task fired ~5 hours late" -- does not hold either. That session was not a scheduled
fire; no `ree-morning-digest` scheduled fire exists on 2026-08-16 at all.

**Honest caveat, not papered over:** the digest DID fire on **Saturday 2026-08-15 at 05:35**,
which a strict weekday-only schedule would not do. The most likely reading is that the harness
deferred a missed weekday fire into Saturday morning (the Mac was asleep 08-10..08-14, see S4),
rather than that the schedule is 7-day. This was not conclusively established and does not
affect the 08-16 finding, which rests on the absence of any fire record.

## 2. The measurement that was missing: there IS a fire record, but not where anyone looked

The chip correctly noted there is no log under `~/.claude/scheduled-tasks/ree-morning-digest/`
(only SKILL.md), and `~/.claude.json`'s `routineFiredWatermark` is stale (2026-06-21) and
unrelated. But the fire record does exist: **every fire creates a session transcript** under
`~/.claude/projects/`, carrying a `<scheduled-task name="ree-morning-digest">` opening block.

That corpus is ~253 MB and a naive grep is actively misleading, which is why this is now a
script. **The task's SKILL.md text is delivered INTO the prompt**, so every guard string in it
(`STALE_SKIP: delta=`, `LOCK_ACQUIRED: fresh`, `Morning digest aborted: ...`) appears in the
transcript of every run, successful ones included. Measured: the naive grep matched 56-59
transcripts; **15 were genuine fires**. The discriminator is interpolation and emission -- a
real execution prints a NUMBER (`delta=10min`), and a real abort is an ASSISTANT MESSAGE, not
quoted instruction text. This trap was hit three separate times while building the auditor,
including one that mis-classified 2026-07-21 (a run that completed and wrote an agenda) as an
abort; each is pinned in the script's comments.

## 3. The fire log (2026-07-21 .. 2026-08-17; earlier transcripts rotated out)

| local time | outcome | detail |
|---|---|---|
| 2026-07-21 Tue 05:16 | RAN | guard passed (delta=+10) |
| 2026-07-22 Wed 05:17 | SKILL_ABORT | digest's own contention guard |
| 2026-07-23 Thu 05:17 | USAGE_LIMIT | refused before any guard ran |
| 2026-07-24 Fri 05:17 | USAGE_LIMIT | refused before any guard ran |
| 2026-07-27 Mon 05:17 | SKILL_ABORT | digest's own contention guard |
| 2026-07-28 Tue 06:14 | STALE_SKIP | +67 min (7 min past the boundary) |
| 2026-07-29 Wed 05:17 | RAN | guard passed (delta=+10) |
| 2026-07-30 Thu 07:08 | STALE_SKIP | +121 min |
| 2026-07-31 Fri 16:53 | USAGE_LIMIT | refused before any guard ran |
| 2026-08-03 Mon 09:07 | STALE_SKIP | +240 min |
| 2026-08-04 Tue 05:16 | USAGE_LIMIT | refused before any guard ran |
| 2026-08-07 Fri 18:30 | USAGE_LIMIT | refused before any guard ran |
| 2026-08-13 Thu 22:02 | USAGE_LIMIT | refused before any guard ran |
| 2026-08-15 Sat 05:35 | RAN | guard passed (delta=+28) |
| 2026-08-17 Mon 05:17 | RAN | guard passed (delta=+10) |

**USAGE_LIMIT 6 (40%) | RAN 4 (27%) | STALE_SKIP 3 (20%) | SKILL_ABORT 2 (13%)**

**Cross-validated against an independent source:** the `RAN` set
{07-21, 07-29, 08-15, 08-17} is EXACTLY the set of scheduled `morning_agenda.md` commits in
that window. The one other agenda commit (08-09 13:20) has no fire row and its own message
says "manual out-of-slot" -- consistent. So the classifier is not merely self-consistent.

## 4. Four independent causes, and the dominant one was not in the hypothesis set

**(1) Usage limit -- 6/15 fires (40%), the single largest cause, and NEW.**
The task fires exactly on time and the session is refused immediately:
`You've hit your weekly limit - resets ...`. It dies **before its first Bash call**, so Check 1
never executes. This is neither of the chip's candidate mechanisms (a: guards abort / stranded
lock; b: harness defers the fire). It is live and recurring on this account -- the umbrella's
own recent history carries `metaworker-dispatch: cycle 2712 -- usage-limit lockout still active`.

**This has a sharp consequence for the fix the chip proposed.** A fire-time breadcrumb written
by Check 1 "BEFORE the stale-skip decision" would **miss this entire 40% by construction** --
no bash in that session ever runs. That is why the deliverable here is a transcript auditor
rather than a breadcrumb: the transcript is the only artifact that survives a refused session.

**(2) The machine never fired at all -- ~6 weekdays.**
08-05, 08-06, 08-10, 08-11, 08-12, 08-14 have **no transcript at all**. This is the block the
2026-08-15 agenda attributed to the Mac being asleep, and that fix is applied and verified
still in force: `pmset -g sched` shows `wakepoweron at 5:00AM every day`. Note the failure
signature is *absence of a row*, which is why the auditor prints that caveat explicitly.

**(3) Late fire -> correct STALE_SKIP -- 3/15 (20%). The guard working as designed.**
Deltas +67, +121, +240. Per the chip's step 3, the window was **not** loosened. One case is
worth flagging for a human, though: **2026-07-28 fired at +67 min, i.e. 7 minutes past the
+60 boundary.** That is the only observed instance where a modest widening would have converted
a miss into a run; the other two (+121, +240) are far outside and SHOULD be skipped. Widening
is a judgement call about how stale an agenda may be before it stops being a morning brief --
left to the user, deliberately not taken here.

**(4) The digest's own contention guard -- 2/15, ALREADY FIXED.**
07-22 and 07-27 fired on time, passed both startup guards, then aborted inside the
`morning-digest` skill on "active sessions detected". This was the binary abort rule, replaced
by the three-tier (FULL / DEGRADED / ABORT) system **on 2026-07-27** -- by the very session
that aborted. No abort has occurred since; 08-17 correctly took Tier 2 and produced an agenda.
No action needed.

## 5. Mechanisms the evidence RULES OUT

- **Stranded lock (chip mechanism (a)).** Zero `CONCURRENT_SKIP` in all 15 fires, and no
  `/tmp/ree-morning-digest.lock` present at 2026-08-18T03:14Z. The one stale lock ever cleared
  (`stale_cleared age=357349s`) was handled correctly by Check 2's own stale-clear.
- **The firing window being systematically too narrow (chip mechanism (b)).** When the harness
  fires normally it lands at **+10 min, every time** (delta=10 on 07-21, 07-22, 07-23, 07-24,
  07-27, 07-29, 08-17). The window is not marginal for on-time fires; it has ~50 min of unused
  slack above the observed latency.

## 6. What is NOT recommended

- Do **not** loosen the stale-skip window as a general fix. It is doing its job in 3/3 cases,
  and 2 of those 3 were hours late. Only the +67 case is arguable (S4.3).
- Do **not** add a fire-time breadcrumb inside Check 1 expecting it to explain the misses --
  it cannot see the 40% usage-limit class (S4.1).
- The base-rate erosion the chip identified is **real and correctly identified**; it is just
  not one defect. It is (1)+(2) above, plus a (4) that is already fixed.

## 7. Deliverable

`REE_Working/scripts/audit_scheduled_task_fires.py` -- generic over any scheduled task
(`--list`, `--task`, `--since`, `--json`). Exit 0 even with findings. This makes the question
"did my scheduled task fire, and what happened" a one-command check instead of a 253 MB grep
with three known false-positive traps.
