# Scripts-corpus daily-run timeouts: root cause and durable fix (staged design)

**Status: APPLIED (d) 2026-09-14 (REE_Working cfa7c8191, timer re-bootstrapped 23:20 local); (e) approved by user 2026-09-16 -- re-checked 2026-09-24: 0 of 9 known-FAIL-set daily runs clean since bootstrap (09-22 undetermined, not credited clean), so the three-consecutive-clean-runs trigger is not met and, per section 6's own escalation clause, ESCALATED TO (b) -- serial lane build chipped `chip-20260924-scriptscorpus-optionb-serial-lane` (section 10)**

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

## 9. Item (e) check, 2026-09-16 (chip `chip-20260916-scriptscorpus-item-e-residual-timeouts`, session `keen-pare-09e5ab`)

**2026-09-16T22:49Z addendum: 0 of 2 post-fix daily runs clean; next expected run 2026-09-17 05:15
local; earliest possible third consecutive clean run 2026-09-19; nothing chipped per file.**

`launchctl print gui/501/com.ree.scriptscorpus` reports `runs = 2` since the 2026-09-14 23:20
bootstrap, and the installed plist is byte-identical (normalised) to the repo copy
(`ProcessType Interactive`, `Nice 10`, no `LowPriorityIO`), so both runs below ran at the
measured-green posture. The results JSON is overwritten daily and the launchd log is empty, so
the 09-15 run survives only as its hygiene-tick sweep chip (which names FAILs and, by the
2026-08-28 decision, never timeouts).

| run (05:15 local) | elapsed | FAIL | TIMEOUT | record |
|---|---|---|---|---|
| 2026-09-15 | unknown | 4: `test_dev_doctor_worktrees`, `test_dispatch_budget_gate`, `test_prune_task_claims_push_default`, `test_session_startup_checklist` | unrecorded | `chip-scriptscorpus-dlaptop-sweep-4-6bae84413e5c7ce4`, absence-resolved 09-16 unexamined |
| 2026-09-16 | 2502 s (241 files, 232 pass, 2 script) | 5: the four above + `test_taskclaims_writer_lock` | 2: `test_hygiene_routine_tick`, `test_ref_convergence` | `logs/scripts_corpus_test_results.json`; `chip-scriptscorpus-dlaptop-sweep-5-2d5ce4f9d0da9775` OPEN |

Read against section 6's acceptance (three consecutive runs under 900 s, every red reproducible
by hand): both post-fix runs fail the elapsed bound and neither red set has been re-run by hand
yet. Two of 09-16's FAILs (`test_dev_doctor_worktrees`, `test_taskclaims_writer_lock`) are in
P4's five and `test_ref_convergence` is P5's timeout -- a partial P4 signature at the
Interactive posture, which is exactly the condition section 6 says would falsify the
`taskpolicy -b` / `ProcessType Background` equivalence assumption and make (b) (serial lane for
the self-spawning and live-state files) the next step. Three files have now failed on every one
of the last three daily runs (09-14 pre-fix, 09-15, 09-16): `test_dev_doctor_worktrees`,
`test_dispatch_budget_gate`, `test_prune_task_claims_push_default`; the 09-14 metaworker-repair
re-run found all five of that day's reds green by hand (40 s), so daily recurrence at the new
posture with by-hand green is the shape to test for on the re-check, not a foregone artifact.

Per the user's 2026-09-16 decision (judge (e) after three clean runs) nothing is chipped per
file here. One headless re-check chip is recorded, dated after the 2026-09-19 run, with the
instruction to (i) count clean runs from the hygiene sweep chips plus the current JSON, (ii) if
three clean runs exist, run item (e)'s per-file pass as this chip's step 2 specified, and
(iii) if the reds persist with the shape above, escalate to (b) per section 6 rather than
waiting indefinitely. The open sweep-5 chip covers the by-hand re-run of 09-16's five FAILs.

## 10. Item (e) re-check, 2026-09-24 (chip `chip-20260916-scriptscorpus-item-e-recheck-after-0919`, session `orchb0924-h3`)

`launchctl print gui/501/com.ree.scriptscorpus` reports `runs = 10` since the 2026-09-14 23:20
bootstrap (one per day 09-15..09-24). Run history reconstructed from hygiene-tick sweep chips
(FAIL sets only, per the 2026-08-28 no-timeout-chip decision) plus the current results JSON
(latest run only, elapsed known):

| date | elapsed | FAIL (n) | record |
|---|---|---|---|
| 09-15 | unknown | 4: `test_dev_doctor_worktrees`, `test_dispatch_budget_gate`, `test_prune_task_claims_push_default`, `test_session_startup_checklist` | `sweep-4-6bae84413e5c7ce4` |
| 09-16 | 2502 s | 5 (+ `test_taskclaims_writer_lock`) + 2 TIMEOUT | `sweep-5-2d5ce4f9d0da9775` (section 9) |
| 09-17 | 728 s | 5: `test_dispatch_budget_gate`, `test_prune_task_claims_push_default`, `test_push_default_drift_guard`, `test_session_startup_checklist`, `test_test_provenance` | `sweep-5-d4b68d8be310ae2c` (withdrawn, superseded by the in-chip run-3 record) |
| 09-18 | unknown | 3: `test_dispatch_budget_gate`, `test_prune_task_claims_push_default`, `test_session_startup_checklist` | `sweep-3-8966f4e726fc3a06` |
| 09-19 | unknown | 6 (+ `test_check_metaworker_timer_state`, `test_test_provenance`) | `sweep-6-623d1d2f8a9c90ce` |
| 09-20 | unknown | 5 (as 09-19 minus `test_dev_doctor_worktrees`) | `sweep-5-4a401afd109b9b4c` |
| 09-21 | unknown | 7 (+ `test_check_worker_work_landed`, `test_dev_doctor_worktrees`) | `sweep-7-b7ba77e9f120d6e4` |
| **09-22** | **UNDETERMINED** | **UNDETERMINED -- no sweep chip exists for this date** | none |
| 09-23 | unknown | 6 (+ `test_audit_dangling_claim_refs`) | `sweep-6-daa2aef09c5295e1` |
| 09-24 | 573 s | 7: `test_audit_dangling_claim_refs`, `test_check_metaworker_timer_state`, `test_dispatch_budget_gate`, `test_prune_task_claims_push_default`, `test_push_default_drift_guard`, `test_session_startup_checklist`, `test_test_provenance` | `sweep-7-a4038443fbde9a48` (matches `logs/scripts_corpus_test_results.json`, mtime 05:24 local) |

**09-22 is a genuine gap, not assumed clean.** `_scripts_corpus_findings()` (`scripts/hygiene_routine_tick.py:8362`)
mints no chip both when `failures` is empty (clean) AND when the results file is stale, from a
worktree, or unparseable -- the same negative-instrument ambiguity CLAUDE.md's "Negative
instruments" rule warns about. Nothing durable survives to distinguish the two for a date whose
JSON has since been overwritten, so 09-22 is recorded as UNDETERMINED rather than credited as a
clean run.

**Verdict: item (e)'s three-consecutive-clean-runs trigger is NOT met -- not close.** Every
known-FAIL-set day from 09-15 to 09-24 (9 of the 10 runs; 09-22 undetermined) reported at least
3 FAILs; there is no run, consecutive or otherwise, with a confirmed 0-FAIL/0-TIMEOUT result
since the 2026-09-14 posture fix. Elapsed, where known, is no longer the blocking factor (728 s,
573 s, both under the 900 s bound; only 09-16 at 2502 s exceeded it) -- consistent with the
09-17 addendum's finding that elapsed and redness are decoupled post-fix. This is exactly
section 6's escalation shape (reds persist at the Interactive posture without the P4 timeout
signature), so per this chip's step 3 the response is: separate genuine defects from artifact
class by hand, chip only what is not already covered, and escalate the artifact class to option
(b) -- not another deferral.

**By-hand re-run, main checkout, 2026-09-24T12:19Z** (STOP-CHECK before the run recorded above):
`run_scripts_tests.sh test_dispatch_budget_gate.py test_prune_task_claims_push_default.py test_session_startup_checklist.py test_check_worker_work_landed.py test_audit_dangling_claim_refs.py`
-> 5 selected / 5 passed / 0 failed / 0 timeout, 89 s. All five are BY-HAND-GREEN.

**Persistent artifact class (9/9 known days red in the daily run, 0/1 by hand today):**
`test_dispatch_budget_gate.py`, `test_prune_task_claims_push_default.py`,
`test_session_startup_checklist.py` -- red on every known run 09-15 through 09-24 with no code
change to any of them or their subjects in that window (`git log --since=2026-09-15 -- <file>`:
empty), and green alone every time they have been checked by hand (09-17 addendum; today). This
is the artifact class section 6 anticipated: self-spawning/live-state contention under the
daily run's 7-way parallelism, not a code defect. No new chip needed -- covered by the option
(b) build chip below, which did not previously exist (checked: no open or resolved chip titled
for a serial lane / option (b) build against this doc).

**Genuine-defect-shaped recurrences, already remediated by concurrent sessions this window --
not re-chipped:**
- `test_test_provenance.py` -- fixed via `chip-20260919-provenance-pin-test-claim-session-link`
  (resolved done 2026-09-24 by session `orchb0924-h1`).
- `test_push_default_drift_guard.py` -- fixed today, REE_Working `4a1500c83` ("classify
  episodic_class_dispositions.py"), landed after the 09-24 05:24 run captured above.
- `test_check_metaworker_timer_state.py` -- fixed today, REE_Working `1d017933c` ("pin the
  2026-09-18 paused-not-retired decision"), landed after the 09-24 05:24 run.
- `test_audit_dangling_claim_refs.py` -- fixed today, REE_Working `9c8da1739` ("fix
  GovernanceWiring fixture to source gov_audit_run").
- `test_dev_doctor_worktrees.py` -- intermittent (red 09-15/16/19/21, green other known days,
  by-hand-green in the 09-17 addendum); no fix landed for it specifically this window and it is
  not in the persistent-3 set, so left unchipped as a likely artifact-class member pending the
  option (b) build.
- `test_check_worker_work_landed.py` -- single occurrence (09-21 only), by-hand-green today;
  not chipped (clean by hand, not recurring).

**Chipped this session:** one headless `kind:work` chip to build option (b) (the serial lane in
`run_scripts_tests.sh` for the three self-spawning files and four live-state files named in
section 3), since the persistent-artifact-class evidence above is now three occurrences deep
and no such build chip existed. See `chip-20260924-scriptscorpus-optionb-serial-lane`.

**Status header updated below** to reflect: item (e) still not judged clean; escalated to
option (b) per section 6's own escalation clause rather than deferred again.
