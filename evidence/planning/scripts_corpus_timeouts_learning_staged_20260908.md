# Scripts-corpus daily-run timeouts: root cause and durable fix (staged design)

**Status: AWAITING USER REVIEW**

Produced by a `/metaworker-learning` pass (session `wizardly-meninsky-e6c09c`, 2026-09-08,
chip `chip-20260908-scripts-corpus-timeouts-learning`, user decision of 2026-09-08 in
campaign-w5-20260908). Decision chip: `chip-20260908-scriptscorpus-qos-decision`.
Nothing in this document has been landed. Build only after the decision chip is answered.

## 0. One-paragraph summary

The daily `com.ree.scriptscorpus` run has never been green since the timer was installed on
2026-08-20. Every red set it has produced passes when re-run by hand, and the recurrence has
been resolved by hand or auto-resolved 15 times (section 2). The chip that routed this here
carried the hypothesis "coordinator-bound tests hang under 7-job parallel load". That
hypothesis is **refuted by measurement** (section 4): the same 22 files pass at 7 jobs in the
foreground in 295 s even with the box at load 22. What reproduces this morning's signature
exactly -- same failing files, timeouts, ~6x elapsed -- is running the corpus under
`PRIO_DARWIN_BG`, which is what the plist's `ProcessType Background` gives it. On this Apple M2
(4 performance + 4 efficiency cores) a Darwin-background process is confined to the 4
efficiency cores with throttled I/O, and 7 git-heavy pytest processes plus their self-spawned
lock contenders are squeezed onto those 4 cores. The fix is a scheduling-posture change to the
plist, pinned by a test, plus the doc corrections that follow from it. It is not a change to
`run_scripts_tests.sh`'s execution model, the cross-run mutex, or the per-file isolation rule.

## 1. The problem class, and why the recurrence is genuine (Step 1)

Same root cause, not merely same symptom: every occurrence is the DAILY run reporting a red
set whose members pass alone, on the same box, under the same plist. Occurrences counted from
resolution notes, not chip existence:

| date | chip_ref | N red | response applied |
|---|---|---|---|
| 2026-08-23 | `chip-scriptscorpus-dlaptop-test-task-claim-amend-renew-orphan-guard` (+7 per-file siblings, 08-25) | 1 (8) | absence-resolved by next run |
| 2026-08-25 | `chip-scriptscorpus-dlaptop-sweep-8-19be6ae80bda6f51` | 8 | absence-resolved |
| 2026-08-26 | `chip-scriptscorpus-dlaptop-sweep-8-632ae879e5aeb0f2` | 8 | absence-resolved |
| 2026-08-27 | `chip-scriptscorpus-dlaptop-sweep-14-8220a4d6ba1cc18e` | 14 | re-run by hand under a 1800 s budget: 6 artifacts, 8 genuine (pre-transport-pin) |
| 2026-08-28 | `chip-20260828-scriptscorpus-amendrenew-over-budget` | 1 (815 s) | withdrawn: 15 s by hand after the transport pin |
| 2026-08-29 | `chip-scriptscorpus-dlaptop-sweep-62-43416a3b563fbc3f` | 62 | absence-resolved |
| 2026-08-30 | `chip-scriptscorpus-dlaptop-sweep-15-7dd468d0f65ccfa0` | 15 | absence-resolved |
| 2026-08-30 | `chip-scriptscorpus-dlaptop-sweep-11-bef2d63bffd9ac92` | 11 | Healer: 5 self-cleared, 1 batch-flaky, 3 env-dependent, 1 pin fix |
| 2026-08-31 | `chip-scriptscorpus-dlaptop-sweep-7-0486195d1ed83375` | 7 | Healer: 6 green on recheck, 1 genuine `pin_scripts_dir` (44edf5221) |
| 2026-09-01 | `chip-scriptscorpus-dlaptop-sweep-5-5b2bb1a848dba173` | 5 | absence-resolved |
| 2026-09-02 | `chip-scriptscorpus-dlaptop-sweep-8-2766959498437125` | 8 | absence-resolved |
| 2026-09-04 | `chip-scriptscorpus-dlaptop-sweep-12-1b245ba6309fc0b3` | 12 | absence-resolved (contained one genuine red, `test_corpus_run_lock.py`, fixed f87f3ec37) |
| 2026-09-08 | `chip-scriptscorpus-dlaptop-sweep-8-5d5b89a73a9d681c` | 8 (+14 timeouts) | W5-HK-G: all pass alone; routed here |

Two ledger mechanics make the "absence-resolved" rows meaningless as fixes:
`hygiene_routine_tick.py` source 18 keys a sweep chip on the sha1 of the sorted red set
(`_scripts_corpus_sweep_chip_ref`, ~L7169), so any change in membership -- one transient file
dropping out -- absence-resolves the old chip and mints a new one; and source 18 deliberately
does not chip `timeouts` at all (~L7050-7078), so the 14 timeouts in today's run were invisible
to the ledger. The 8-of-15 "remedied" resolutions are therefore 8 unexamined recurrences.

Threshold: the skill's default of 2 confirmed occurrences is met many times over. This is a
`complicated (buildable)` node, not a `complex (probe-gated)` one, once section 4 is in hand.

## 2. What the prior responses were, and why none was durable

- **Absence-resolution, no diagnosis** -- 8 times. Not a response at all.
- **Re-run alone, declare artifact** -- 3 times (08-27, 08-30, 09-08). Correct each time,
  changes nothing.
- **Genuine one-off defects the daily run happened to surface** -- 3 (`pin_scripts_dir` x2,
  `corpus_run_lock` dead-holder reclaim). Real fixes, unrelated to the class.
- **Structural mitigations to the runner** -- 2: the cross-run mutex + TIMEOUT/FAIL split
  (9432f948, 2026-08-28) and the coordinator-transport pin in three layers (75b4ffde). Both
  fixed a REAL adjacent cause (three concurrent runs; tests reaching the production hub) and
  both left the daily run red, because neither touched the scheduling posture.

Each mitigation was written from a by-hand reproduction. Nobody had reproduced the daily run's
own conditions, which is why the class survived two correct fixes.

## 3. Mechanism (Step 2 research, two subagents + local checks)

**Ruled out, by construction or measurement:**

- *Shared coordination lock between test processes.* Every chip_ledger / task_claim test file
  patches `ROOT` to its tempdir before any lock is taken and passes `REE_WORKING_ROOT` to its
  subprocess contenders; lock paths are `<tempdir>/.git/ree_chip_ledger.lock` and
  `<tempdir>/checkout/.git/ree_task_claims.lock`. Nothing is shared between sibling files.
- *Coordinator network.* `TASK_CLAIM_COORDINATION_MODE=git` is pinned in three layers
  (run_scripts_tests.sh:200-221, scripts/conftest.py:47, _test_provenance.py:98); the transport
  timeout is 5 s anyway.
- *Mac asleep during the run.* `pmset -g log`: no sleep entry after 2026-09-07 13:42; a
  `caffeinate -i` (pid 78077) has held the box awake since 2026-09-07 13:51. Today's run began
  05:15 local and wrote its result at 07:18 (elapsed 7348 s).
- *Parallelism per se.* Section 4, P2.

**What is actually shared:** the box's 8 cores and, for four files, live Mac state.

- Three files spawn their own real contender processes (`test_chip_ledger_mutation_lock.py:626`
  6 procs; `test_taskclaims_writer_lock.py:724` 5 procs; `test_task_claim_mutation_lock.py:453`)
  and carry wall-clock assertions (`assertLess(elapsed, 1.0)`, `<5.0`, `<30`, `<60`).
- Four files read live state -- real `git status`/`index.lock`, `git worktree list` (36
  worktrees), system-wide `lsof`, real `.claude/skills/*.md` -- and run the real script under
  short embedded subprocess timeouts sized for an idle box: `test_audit_stashes.py:868`
  `timeout=15`; `test_dev_doctor_worktrees.py:622` `timeout=60`;
  `test_session_startup_checklist.py:215-237` `timeout=180`. These are what turn starvation
  into FAIL rather than TIMEOUT.
- The remaining 14 are simply git-subprocess-heavy (hundreds to >2000 git processes per file)
  and starve.

**The scheduling posture.** `scripts/com.ree.scriptscorpus.plist` (unchanged since c50b28c49,
2026-08-20) sets `ProcessType Background`, `Nice 10`, `LowPriorityIO true`. `launchd.plist(5)`:
Background jobs get "resource limits ... intended to prevent them from disrupting the user
experience" -- on Darwin that is the `PRIO_DARWIN_BG` policy, which on Apple Silicon schedules
the process only on efficiency cores and throttles its I/O. `sysctl`: `hw.perflevel0` =
Performance x4, `hw.perflevel1` = Efficiency x4. The "~8 min at --jobs 7" baseline in
CLAUDE.md was measured on 2026-08-18 (98ee28068), interactively, two days before the plist
existed. The daily run has never run under the conditions its baseline was measured in.

The plist installed in `~/Library/LaunchAgents/` matches the repo copy apart from a comment
(`launchctl print`: nice = 10, low priority i/o).

## 4. Measurement (2026-09-08, DLAPTOP, main checkout, all 22 red/timeout files)

All phases with `TASK_CLAIM_COORDINATION_MODE=git`; P2-P5 through the real runner with the
cross-run lock held; live sessions were running throughout (baseline load 6-7).

| phase | posture | jobs | elapsed | result |
|---|---|---|---|---|
| P1 | foreground, nice 10, sequential | 1 | 847 s total, max 95 s (`test_ref_convergence.py`) | 22/22 pass |
| P2 | foreground, nice 10 | 7 | 295 s (load peaked 22) | 22/22 pass |
| P3 | foreground, nice 10 | 3 | 417 s | 22/22 pass |
| P4 | `taskpolicy -b` (PRIO_DARWIN_BG) | 7 | 1831 s | 12 pass, **5 FAIL, 5 TIMEOUT** |
| P5 | `taskpolicy -b` | 3 | 2159 s | 19 pass, **2 FAIL** (`test_dev_doctor_worktrees`, `test_taskclaims_writer_lock`), **1 TIMEOUT** (`test_ref_convergence`) |

P4's failures -- `test_audit_shared_checkout_conflicts`, `test_chip_ledger_mutation_lock`,
`test_dev_doctor_worktrees`, `test_task_claim_mutation_lock`, `test_taskclaims_writer_lock` --
are five of this morning's eight; its five timeouts are all in this morning's fourteen. That is
the daily run's signature, reproduced in the afternoon on demand, by changing nothing but the
scheduling policy. P2 at the same job count and higher ambient load is green in a sixth of the
time. Raw logs: scratchpad `measure.out`, `measure_p4.out` (session-local; the JSON summaries
are reproduced above in full).

Residual uncertainty, stated: `taskpolicy -b` sets `PRIO_DARWIN_BG` via `setpriority(2)`;
launchd's `ProcessType Background` is documented only at the "resource limits" level. The two
are widely treated as the same policy but I have not read launchd's source. The acceptance
criterion in section 6 is what closes that gap.

## 5. Candidate fixes

The chip named (a), (b), (c). The measurement adds (d), and (e) is the observability gap that
let the class hide.

- **(a) Hermetic coordinator stub.** Solves a mechanism that is not operating (section 3). For
  the four live-state files it would also delete the point of their end-to-end smoke classes.
  Rejected.
- **(b) Serial lane for tagged files in `run_scripts_tests.sh`.** Would remove the
  self-spawning amplifier and the live-state races. P2 shows it is not needed for correctness:
  those files pass at 7 jobs in the foreground. Held in reserve as the second step if the daily
  run is still red after (d). Not proposed now.
- **(c) Lower `--jobs` for the daily run.** P5 measures this directly (Background posture at 3
  jobs): still 2 FAIL + 1 TIMEOUT, and slower than at 7 jobs (2159 s vs 1831 s), because the
  binding constraint is the efficiency-core confinement and I/O throttle, not the job count.
  Refuted as a fix on its own. As an add-on to (d) it is unnecessary (P2/P3 both green) and
  costs wall-clock.
- **(d) Change the plist's scheduling posture -- RECOMMENDED.** `ProcessType Background` ->
  `Interactive` (launchd's "no resource limits", i.e. the posture P2 was measured under), drop
  `LowPriorityIO`, keep `Nice 10`. Nice is the knob that protects the user's live sessions --
  P2 ran at nice 10 alongside live sessions and was green -- and it does not restrict core
  placement. `Standard` is also documented as applying "light" CPU and I/O throttling; only
  `Interactive` reproduces the measured-green posture, so that is the proposal rather than the
  softer-looking choice. Pin it with a new corpus test `scripts/test_scriptscorpus_plist_qos.py`
  that parses the plist and asserts `ProcessType != Background` and no `LowPriorityIO`, carrying
  this document's WHY, so a future "let's be gentler on the box" edit cannot silently re-arm the
  class. Re-run `scripts/install_scriptscorpus_timer.sh` (bootout + bootstrap; launchd caches
  the loaded plist) -- on the Mac, by the landing session.
- **(e) Make the class visible next time.** Today's 14 timeouts reached nobody because source
  18 does not chip timeouts (a deliberate 2026-08-28 decision, kept) and the sweep chip
  absence-resolves on any membership change. Proposed narrow addition, NOT in the first
  landing: a single tick-side warning finding when `elapsed_seconds` in the results file
  exceeds a fixed ceiling (say 1800 s, 6x the interactive baseline, 4x P2), keyed on the run
  date so it cannot flap. Listed so the decision can constrain or exclude it; the default
  recommendation is to land (d) alone first and judge (e) against three clean daily runs.

Out of scope, noted for the record: five other `com.ree.*` plists also use `ProcessType
Background` (hygienetick, coordinatorbackup, gitsyncrepair, indexlockwatch,
workspacestaterotate). They are short sampling jobs and the posture is right for them; but
`chip-hookgating-dlaptop-*` of 2026-08-28 ("audit_hook_gating --json did not finish within
its 90 s outer bound", attributed to a load spike) is the same shape under the hygiene tick's
Background posture, and is worth remembering if it recurs. Not touched here.

## 6. Files the recommended fix touches, and the acceptance test

- `scripts/com.ree.scriptscorpus.plist` -- `ProcessType` Background -> Interactive; remove
  `LowPriorityIO`; rewrite the "WHY NICE'D" comment to say why Background is wrong here.
- `scripts/test_scriptscorpus_plist_qos.py` -- new, pins the posture.
- `docs/reference/scripts-test-corpus.md` -- a short subsection under "Results wiring": the
  daily run is a trunk verdict only at the interactive posture; this document as the record.
- `CLAUDE.md` "Running the umbrella `scripts/` test corpus" -- no rule change; the "~8 min at
  --jobs 7" figure stands (P2: 295 s for the 22 heaviest files).
- Re-install the timer on DLAPTOP.
- Then run the corpus from the main checkout (`run_scripts_tests.sh --changed` at minimum, full
  run preferred) before landing, per the standing rule.

**Acceptance:** three consecutive daily runs (05:15 local) with `elapsed_seconds` under 900
and every red, if any, reproducible by hand. A red that survives a by-hand foreground run is a
genuine defect and gets its own chip, exactly as before. If the first post-change daily run is
still red with the P4 signature, the `taskpolicy`/`ProcessType` equivalence assumption was
wrong and (b) is the next step -- not a return to lowering `--jobs`.

## 7. GOV-HELDOUT-1 check

The standing change is "the daily run's scheduling posture is Interactive + nice 10, and a
daily red is read as genuine only if it reproduces at that posture". Cases below were NOT used
to derive it (it was derived from today's run and P1-P5) and the OLD and NEW readings give
different calls:

1. **2026-08-28, `chip-20260828-scriptscorpus-amendrenew-over-budget` (815 s in the daily
   run).** Old reading: the 815 s was entirely the coordinator transport, fixed by 75b4ffde,
   chip withdrawn. New reading: the transport fix was real but the file would still overrun
   under the Background posture -- and it did: it is in today's 14 timeouts (P1 today: 75 s
   alone; P4: TIMEOUT). Different call; the new one is confirmed.
2. **2026-08-31, `chip-scriptscorpus-dlaptop-sweep-7-0486195d1ed83375`.** Old: a 7-file chip,
   6 of them noise, one genuine (`pin_scripts_dir` on `test_dispatch_budget_gate.py`). New: at
   the Interactive posture the 6 noise members do not appear (five of the six are in today's
   22 and pass in P2 at 7 jobs; the sixth, `test_test_provenance.py`, was not in today's set
   and is unmeasured) and the genuine defect surfaces alone. Different call: a 1-file chip
   instead of 7. Prediction, supported by P2, closed by acceptance.
3. **2026-08-30, `chip-scriptscorpus-dlaptop-sweep-11-bef2d63bffd9ac92`.** The Healer found 3
   reds that were NOT load: `test_ree_metaworker_heartbeat_health.py` reading a live
   account-wide cooldown window. Today's routing note on sweep-8-5d5b89 says "a later daily RED
   of the same shape is the same class -- do not re-diagnose". Under that reading those 3 would
   be misfiled as posture artifacts. The new rule's second clause ("genuine only if it
   reproduces at the Interactive posture") gives the right call: they reproduce, they are
   genuine. This is the negative control that keeps (d) from being over-read as "all daily
   reds are noise".
4. **2026-09-04, `chip-scriptscorpus-dlaptop-sweep-12-1b245ba6309fc0b3`.** Same shape as case
   2: one genuine red (`test_corpus_run_lock.py`, fixed f87f3ec37) inside 11 other members,
   absence-resolved without anyone reading it. Seven of those 11 are in today's 22 and pass in
   P2; the other four (`test_audit_hook_gating.py`, `test_audit_stale_claims_governance_lock.py`,
   `test_hygiene_removed_worktree_live_worker.py`, `test_test_provenance.py`) are unmeasured
   here. New posture: a chip naming the genuine defect and at most those four; the genuine
   defect cannot be lost inside a set that flaps.

A case where old and new AGREE, listed so it is not mistaken for a held-out case: the
2026-08-28 three-concurrent-runs incident. The cross-run mutex is right regardless of posture
and stays. Likewise the per-file isolation rule and the TIMEOUT/FAIL split are untouched.

**Counterweight, stated rather than skipped.** This check cost about ninety minutes of box
time (P1-P5 ran ~65 minutes of wall-clock on a live machine, pushing load to 22 for five
minutes during P2) and two subagent research passes. Cases 2 and 4 are predictions from P2
rather than re-runs of the original days, which no longer exist as results files (the JSON
is overwritten daily and the launchd log is empty). The acceptance criterion is what converts
them from prediction to record. The Interactive posture also means the 05:15 run competes with
overnight headless campaigns on the performance cores for roughly five minutes at nice 10;
that is the cost of a verdict the fleet can trust, and it is bounded.

## 8. Decision requested

See `chip-20260908-scriptscorpus-qos-decision`. Options: proceed with (d) as written
(recommended); proceed with (d) plus (e); (d) constrained to `ProcessType Standard` rather
than Interactive (softer, but not the measured-green posture -- would need its own
measurement first); hold and keep resolving the daily chip by hand. (c) alone is refuted by
P5 and is not offered.
