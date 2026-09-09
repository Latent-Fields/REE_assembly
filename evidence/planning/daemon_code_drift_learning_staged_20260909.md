# Daemon code drift -- /metaworker-learning root-cause pass

**Status: R1+R2 LANDED 2026-09-09. R3 (restart automation) DEFERRED by user decision.**

- Date: 2026-09-09
- Session: `metaworker-learning-daemondrift-20260909`
- Skill: `/metaworker-learning` (Steps 1-3 complete; Step 4 consent gate NOT satisfied -- nothing built, nothing landed)
- Governing open decision chip: `chip-20260908-decision-daemondrift-class-drift-aware-restart` (kind=decision, spawned 2026-09-08T18:23:50Z, **still open**)

---

## Headline

The pending decision chip frames this class as *"the restart is the fix; automate the restart."*
That framing is incomplete, and building on it first would be unsafe.

This pass found a **second, independent root cause in the detection/resolution path**: the
Mac half of the drift detector silently degrades to "clean" on any internal failure, and the
resolve pass credits that silence as a *clean observation*, which then satisfies the 6h
hysteresis and auto-resolves the standing chip with the note **"-- remedied"** for a
condition that was never remedied.

**Verified right now, on this box:** `serve.py` (PID 78075) has run unrestarted since
`2026-09-07T12:51:22Z`; the detector reports `DRIFT` when run by hand; and
`chip-daemondrift-dlaptop-mac-serve-g2` was nevertheless auto-resolved at
`2026-09-09T16:13:32Z` as *"episodic class quiet for 8.1h (>= 6h hysteresis; 1 episode(s)
recorded) -- remedied"*. `-g3` re-raised **21 minutes later** with an identical process start
stamp. Nothing was restarted at any point.

**Consequence for the pending proposal:** an auto-restart that FAILED would be auto-resolved
as "remedied" by exactly the same path. The proposed capability would therefore report
success it did not achieve. **The resolution defect must be fixed first, or the restart must
carry positive post-verification** -- ordering is the main finding of this pass.

---

## Step 1 -- recurrence is genuine

Threshold is 2 confirmed occurrences of the same root cause (`/metaworker-learning` Step 1,
mirroring `RE_DERIVE_BRAKE_THRESHOLD`). This class is far past it.

Same root cause throughout: *a long-running Python process keeps executing the bytecode it
bound at import, so landed code never reaches it* (OPERATOR_GUIDE.md "Daemon code drift").

| Subject | Generations | Chips |
|---|---|---|
| `ree-cloud-1` / ree-explorer | 3 | g1 2026-09-02, g2 09-03, g3 09-07 |
| `ree-cloud-1` / ree-sync-daemon | 2 | g1 2026-09-02, g2 09-07 |
| `ree-cloud-1` / ree-coordinator | 1 | g1 2026-09-02 |
| `DLAPTOP` / mac-serve | 3 | g1 2026-09-03, g2 09-09, g3 09-09 (open) |
| `DLAPTOP` / mac-runner | 1 | g1 2026-09-08 (open) |

10 chips, 5 subjects, 2 host families, 8 days. None withdrawn as a false positive.

**But the counting itself needs a correction, and it is load-bearing.** Not every generation
is a genuine recurrence. Resolution notes split cleanly in two:

- **Genuine remediation (`resolution_note_auto: false`)** -- a real, user-authorised
  `systemctl restart` with post-verification. Two events: 2026-09-02T21:47:42Z (sync-daemon +
  coordinator) and 2026-09-08T18:21:24Z (sync-daemon-g2 + explorer-g3).
- **Auto-resolution on quiet (`resolution_note_auto: true`)** -- *"quiet for N h ... --
  remedied"*, with no restart evidence. Four: explorer g1, explorer g2, mac-serve g1,
  mac-serve g2.

For mac-serve g2 the auto-resolution is **provably false** (process start unchanged, see
Headline). So the hub subjects are the genuinely-recurring ones; the Mac subjects are
recurring *and* generation-inflated by false remediation. Both are real problems; they are
different problems.

---

## Step 2 -- what the machinery actually is

### There are TWO detectors, not one

| Concern | Canonical (hub) | Mac re-implementation |
|---|---|---|
| Location | `ree-v3/coordinator/deploy/daemon_code_drift.py` | `scripts/hygiene_routine_tick.py:8955-9015` |
| Unit registry | `UNITS` (:97-140) | `_DAEMON_DRIFT_MAC_UNITS` (:8956-8961) |
| Process start | btime + `ExecMainStartTimestampMonotonic` | `pgrep -f` + `ps -o etime=` (`_proc_start_dt`) |
| Newest surface commit | HEAD **and** `origin/<branch>` | HEAD **only** |
| Statuses | 5: `CURRENT`/`DRIFT`/`BEHIND-ORIGIN`/`UNKNOWN`/`INACTIVE` | 1: literal `"DRIFT"` |

The canonical checker is inert on macOS: `check_all` returns `[]` when `/proc/stat` is
unreadable (:415-419), and `render_markdown` then prints `_(not checked -- not a systemd
host)_`. The hygiene tick shells the *real* checker over ssh for the hub's units
(`_hub_daemon_drift_rows`) and hand-rolls the Mac half.

Divergences that matter (not stylistic):

1. **No `UNKNOWN` on the Mac half.** Every failure path is a bare `continue` -- process not
   found, `pgrep`/`ps` exception, `git log` failure. "Cannot look" and "clean" are
   indistinguishable. **This is the defect at the centre of this pass.**
2. **No `BEHIND-ORIGIN`.** The Mac half grades HEAD only, so a stale Mac checkout reads
   clean -- the exact false-all-clear the canonical checker's docstring exists to prevent.
   Note this box currently has `chip-refwedge-dlaptop-ree-assembly-master-g4` open and a chip
   for 12 stranded `REE_assembly` commits, i.e. the preconditions are live.
3. **Two hand-maintained import surfaces, already out of sync.** Mac `mac-runner` names
   `experiment_protocol.py`; canonical `ree-runner` names `runner_checkpoint.py`. Neither
   names both. No shared constant.

### How the false "remedied" is produced

`_episodic_update_clean_streaks` (`hygiene_routine_tick.py:5391-5444`) credits a subject with
a clean observation whenever its source scanned OK (`scan_ok`) and the subject's ref is not in
this tick's `active_refs`. Six hours of that satisfies `_EPISODIC_HYSTERESIS_HOURS` and the
standing chip is auto-resolved "-- remedied".

The W5a observation-streak fix (2026-09-07, `queue_floor_detector_respec_staged_20260907.md`)
closed the *outage* hole: a tick that never ran cannot credit quiet. It does **not** close
this one. Its own comment anticipates the distinction:

> NOTE the `scan_ok` gate in run_tick is NOT this, and does not subsume it: that one asks
> "did the source parse its input on THIS tick" ... This asks "has the source been watching
> CONTINUOUSLY for the whole hysteresis window".

There is a **third** question neither asks: *did the source successfully evaluate THIS
SUBJECT on this tick?* `scan_ok` is per-source and per-tick; the streak is per-subject across
ticks; nothing is per-subject **and** per-tick. A Mac row that silently vanishes leaves
`scan_ok` True and the subject un-fired -- which reads as clean.

### What was ruled out (checked, not assumed)

- **Generational-ref mismatch** (`-g3` vs base ref in `active_refs`) -- REFUTED.
  `_record_episodic_finding` mutates `f["chip_ref"]` to the generational ref before
  `active_refs` is built. Simulated against live ledger state: the streak entries for both Mac
  subjects are correctly popped when the finding fires.
- **launchd Background posture starving `pgrep`/`ps`** ([memory]
  `reference_launchd_background_posture_efficiency_cores`) -- REFUTED by measurement.
  `_proc_start_dt` under `taskpolicy -b`: 0.06-0.09s, correct result, 3/3.

### What remains open -- `puzzle (known rules)`, not `mystery`

Which specific failure empties the Mac row is not yet pinned. Leading candidate: the
`git log -1 --format=%cI -- <surface>` call in `_mac_daemon_drift_rows` failing under
contention in the currently-wedged `REE_assembly` checkout (`except Exception: continue`).
One instrumented tick that logs per-subject evaluation outcomes resolves it. **The structural
fix does not depend on the answer** -- every candidate funnels through the same missing
`UNKNOWN` state.

---

## Step 3 -- proposed durable fix

Sequenced deliberately. **R1 is a prerequisite for the pending decision chip's proposal, not
an alternative to it.**

### R1 (prerequisite) -- the Mac half must be able to say "I could not tell"

- `_mac_daemon_drift_rows` returns an `UNKNOWN` row instead of `continue` on: process not
  found, `_proc_start_dt` returning None, `git log` failure/empty. Distinguish *genuinely not
  running* (a real `INACTIVE`, which IS clean) from *could not determine* (`UNKNOWN`).
- `_daemon_drift_findings` counts `UNKNOWN` subjects in `meta` and exports them so the resolve
  pass can withhold the clean vote **for that subject only** -- a per-subject analogue of
  `scan_ok`, which is what is missing today. `UNKNOWN` mints no chip (it is not a finding);
  it only suppresses the clean vote. Fail-safe direction: withholding a vote holds a standing
  chip open one more window and can never cause a false resolve, matching
  `_episodic_streak_load`'s stated convention.
- Add `BEHIND-ORIGIN` to the Mac half, or state explicitly in-code why HEAD-only grading is
  accepted there.
- Files: `scripts/hygiene_routine_tick.py`, `scripts/test_hygiene_tick_daemon_drift.py`
  (unittest style, `_test_provenance` pins, injected rows, frozen `NOW`, `Pins:` docstring
  entry).

### R2 -- auto-resolution must not claim remediation it cannot see

For classes whose remediation has a **positive, observable signature**, the auto-resolve note
must assert it rather than infer it from quiet. For daemon drift the signature is exact and
free: *the process start stamp moved*. Withhold auto-resolution while the observed
`started_utc` is unchanged, and say so in the note.

This is the change that makes the pending decision chip's proposal safe to build: a restart
that did not take is then visible instead of self-certifying.

### R3 (the pending chip's own proposal) -- NOT buildable as written

Two independent reasons, both found in this pass:

**(a) The held-out check fails it** (below): Option A is wrong on 3 of 5 non-degenerate cases.

**(b) One of its five gates does not exist.** The chip requires *"no phase3 writer tick is
mid-commit (sync-daemon idle marker / lock absent)"*. There is no such marker.
`_WRITER_HEALTH` records `last_tick_at` on tick **entry** and `last_commit_at` on successful
push (`sync_daemon.py:624-651`), with **no in-tick flag**. The only available signals are a
60s-cadence timing inference and a `.git/index.lock` test that is racy in one direction only
(lock present => definitely mid-git; lock absent => *not* "not mid-tick", since the tick spends
most of its time in DB reads and `git fetch`). The unit this gate exists to protect is exactly
the one with the worst failure mode: a mid-tick kill of `ree-sync-daemon` leaves
staged-not-committed files or a stale `index.lock`, and the writers then refuse **silently,
every subsequent tick** -- precedents 5h31m (2026-07-18) and 7.5h / ~4049 restart crash-loop
(2026-08-01).

**Prerequisite R3a:** add a real tick-boundary marker (`in_tick` set/cleared around the writer
block, `sync_daemon.py:3208-3272`, surfaced on `/writer-health`) so the gate becomes a
predicate instead of a timing guess. Without it, `ree-sync-daemon` must be excluded from any
allowlist regardless of A/B.

**Scope corrections to the allowlist, independent of the above:**
- **`ree-coordinator`** -- exclude (held-out case B2; also `db.init_db()` runs
  `executescript(schema.sql)` at process start, so an unattended restart applies schema DDL to
  the live authoritative coordination DB). This is Option B's position, and the corpus supports it.
- **`ree-runner`** -- exclude. RETIRED 2026-08-30 by user decision.
- **`ree-live-status`** -- never a subject. It is `Type=oneshot` on 3 min and hosts the checker
  precisely so the checker cannot go stale; adding it would make the checker grade itself.
- **`mac-serve`** -- exclude. Confirmed **not programmatically restartable**: there is no
  launchd plist for it: it is an unsupervised foreground child of the user's Terminal via
  `Start Explorer.command`, whose `trap ... HUP` + foreground `wait` bind it structurally to a
  live interactive session. Automating it would first require installing a `com.ree.serve`
  LaunchAgent -- a separate decision with its own trade-off (the explorer stops being a
  terminal the user can Ctrl-C).
- **`mac-runner`** -- the cleanest candidate. `POST {"kind":"stop"}` is a *drain*, not a kill;
  launchd `KeepAlive=true` respawns on current code. Prefer posting to the hub coordinator's
  `/commands/issue` directly rather than through `127.0.0.1:8000`, so the path does not depend
  on the possibly-stale `mac-serve`.

So the defensible residue of R3 is narrow: **`ree-explorer` and `mac-runner`**, after R1+R2,
with the tree-resolution fix, a deferral marker, and R3a before `ree-sync-daemon` is even
considered.

### Deliberately NOT proposed

- **Collapsing the two detectors into one.** Tempting and wrong to do here: the hub path is
  ssh-to-canonical, the Mac path is local, and merging them is a larger change than the
  defect warrants. R1 makes the Mac half *honest*, not identical. Record the duplication as
  known debt.
- **Lowering `_EPISODIC_HYSTERESIS_HOURS`.** Treats the symptom and re-arms the
  resolve-and-refire loop W5a closed.

### Honest counterweight

R1+R2 will make some standing chips stay open longer, which reads as "more open chips" on
`/workset`. That is the intended trade: an open chip is a true report; "-- remedied" on a
live condition is a false one. GOV-HELDOUT-1 validation costs real cycles and is not free.

---

## Held-out check (GOV-HELDOUT-1)

**Result: the rule as proposed (Option A) FAILS this check.** Recorded per CLAUDE.md
"General Rules" -- the outcome is the claim's only admissible evidence, and the outcome here
is *caught an over-broad rule*.

**Scope correction first: `A-62` (2026-08-08 concurrent-rebase race) is DISQUALIFIED as
held-out evidence.** The proposing chip names it verbatim as the failure shape its gates
defend against, so scoring it would degenerate the check into the rubber stamp CLAUDE.md
warns about. The same disqualification applies to every 2026-09-02/09-08 daemondrift chip:
the rule was written from them.

Non-degenerate cases (old and new behaviour genuinely differ):

| # | Date | Case | Rule's call |
|---|---|---|---|
| A1 | 2026-07-18 | `ree-sync-daemon` ran pre-fix bytecode ~3.4h after `b2d2ef1` fixed a `phase3_queue_writer` self-deadlock (5h31m wedge, workers re-claiming completed work off a frozen queue file) | **RIGHT** |
| B1 | 2026-07-18 | `ree-explorer` running from the stale `Documents/GitHub` clone (845 modified files, auto-pull silently refusing). Restart made it current *with that clone* and did nothing about a ~6-week code gap; it needed **repointing**, not restarting | **WRONG** (silencing) |
| B2 | 2026-08-29 | Three PHASE-4 coordinator slices landed with commit messages saying **"INERT until restart"**; activation was a single deliberate, user-authorised restart gated on the full worker suite | **WRONG** under A; **RIGHT** under B |
| B3 | 2026-09-09 | `/chip/amend-note` (`ree-v3 63aa9f2cf0`) held back on purpose: *"deliberately left to the user/orchestrator as it interrupts the coordination plane"* | **WRONG** (latent) |
| B4 | 2026-09-06 | `serve.py` drift on a **comment-only diff** -- WORKSPACE_STATE records *"comment-only diff, no restart needed"* | **WRONG** |

Tally: **1 right, 3 wrong, 1 that Option B converts to right.**

### What the corpus exposes, beyond the A/B choice

1. **The pre-flight grades the wrong tree.** It checks `~/REE_Working/{REE_assembly,ree-v3}`,
   while `daemon_code_drift.py` grades each unit's own `WorkingDirectory` (`resolve_repo`).
   Case B1 *is* that mismatch, already realised once. The guide's own line applies to the gate
   as much as the checker: *"A check that confidently grades the wrong tree is worse than no
   check."*
2. **The detector is timestamp-based and content-blind**, and `ree-explorer`'s entire import
   surface is the single file `serve.py`. B4 (comment-only) and B2 (schema DDL via
   `db.init_db()` -> `executescript(schema.sql)` at process start) both ride on that.
3. **No predicate corresponds to "a human deliberately deferred this activation."** B2 and B3
   are both authors explicitly writing *INERT until restart* / *left to the user*. A
   machine-readable deferral marker (a commit trailer the restarter refuses on) converts both
   from WRONG to RIGHT and is the single highest-value addition to the gate set.
4. **The counterweight is sharper than expected:** the rule's one clean win (A1) is blocked by
   its own pre-flight, because the wedge there *was a staged file* -- i.e. a dirty tree. The
   incidents where an automatic restart pays are disproportionately the ones where the
   pre-flight refuses.

### Degenerate cases (same answer both ways -- scope evidence, not scored)

- **2026-05-30**: a fleet-wide `shadow.conf` push mis-including
  `PHASE3_DISABLE_RUNNER_HEARTBEAT_WRITE` wedged cloud-2/3/4 for 6-12h. Config, not code, so
  the detector never fires -- but it is the direct precedent that *automatic restart machinery
  amplifies one bad input into a fleet-wide outage*, and the reason the fix was a runtime
  self-guard rather than a config gate. The proposed rule currently has only config gates.
- **2026-07-30 / 2026-08-29**: hub `ree-runner` ran 10-day, then **27.4-day** old bytecode
  with its DRIFT row public throughout. Not in the allowlist -- and must not be: OPERATOR_GUIDE
  is categorical (*"Do not restart a runner to apply a non-urgent config change"*), because
  `TimeoutStopSec=10min` SIGKILLs a longer experiment mid-flight. These are the pressure to
  widen the allowlist, and the reason not to.
- **2026-06-02**: a queue-writer rebase wedge sat ~4.5h and was fixed by
  `PHASE3_QUEUE_CONFLICT_RECOVERY=1`, not a restart. Negative control: *wedged* and *stale* are
  different classes and restart fixes neither.
- **2026-09-07**: coordinator `/intent/replace` returned HTTP 500 for **218 consecutive
  intents over five days** (`repo_not_configured`, a missing env line). `daemon_code_drift.py`
  was all-green throughout -- the detector's blind spot.

### Consequence for the recommendation

R3 must not be built as Option A. The defensible minimum is Option B **plus** the tree-resolution
fix (finding 1) and a deferral marker (finding 3); B1 and B4 remain unaddressed by any variant
in the chip today.

---

## Incidental live defects found (report-and-chip, not part of this design)

Found while researching; each is independent of the decision above.

1. **The daemondrift chip prompt instructs a prohibited action.** Every chip this class mints
   carries a restart recipe whose step 2 is
   `ssh ... && sudo systemctl restart ree-runner` (`hygiene_routine_tick.py:9126-9128`). The
   hub runner was **RETIRED 2026-08-30 by user decision** (CLAUDE.md: *"Do NOT re-enable it...
   Reversal is user-approved only"*). A session following the prompt literally would violate a
   standing prohibition. The prompt text needs that step removed.
2. **`serve.py`'s `draining` flag is permanently False.** `runner_status()["v3"]["draining"]`
   reads `evidence/experiments/runner_status/*.json`; those directories were removed in the
   2026-09-06 heartbeat retirement, and the Mac runner runs `PHASE3_RUNNER_TELEMETRY_OFF_GIT=1`
   and never wrote them. `STATUS_DIR.is_dir()` is False, so `draining_any` can never be True.
   Any idle-gate built on it would silently always pass. Use coordinator `/shadow/status`.
3. **The Mac half has no working-directory guard.** `pgrep -f "serve.py --port 8000"` matches
   that process in *any* clone, while `repo_rel` is hardcoded -- so the Mac can grade a
   different tree than the process actually runs from. This is the `Documents/GitHub` failure
   class (held-out case B1), unguarded on the Mac side.
4. **The two import surfaces for the same process class disagree** (Mac names
   `experiment_protocol.py`, canonical names `runner_checkpoint.py`; neither names both).

---

## Step 4 -- consent, and what was actually built

The decision was put to the user live rather than through a second chip (a decision chip on
this class was already open and unanswered; duplicating it would have been noise).

**User decision, 2026-09-09: "R1+R2 first, restart deferred."** Recorded in the
recommendation-agreement ledger (entry_id 195, recommendation matched).

### Landed

`REE_Working 3f9324f26` (on `origin/master`) -- `scripts/hygiene_routine_tick.py`,
`scripts/test_hygiene_tick_daemon_drift.py`.

- `_proc_start_dt` returns `_PROC_START_UNKNOWN` on lookup failure, distinct from `None`
  ("not running", which is a real and clean observation).
- `_mac_daemon_drift_rows` always emits one row per unit -- `DRIFT` / `CURRENT` / `INACTIVE` /
  `UNKNOWN`. No silent drops.
- `_hub_daemon_drift_rows` no longer pre-filters to stale, so hub subjects can also be
  observed `CURRENT` (without this they could never be auto-resolved under the new rule).
- `_daemon_drift_findings` classifies every row and exports `clean_bases` / `unknown_bases`.
- `_episodic_update_clean_streaks` takes `positive_clean_bases`: for a listed prefix, the
  absence of a finding **breaks** the streak instead of extending it. Other prefixes keep
  absence-is-quiet semantics unchanged.

**R2 is satisfied by the same mechanism rather than by a separate start-stamp comparison:**
`CURRENT` means the process started *after* the newest import-surface commit, so an
auto-resolution now requires positive evidence that a restart actually happened.

**Verification against the live case** (the one that motivated the pass): on a simulated tick
where the source scans OK but the mac-serve row is silently absent, the streak entry is now
removed rather than credited -- so the false `-- remedied` auto-resolution cannot recur.
Tests: 6 existing pins unchanged, 8 new (pins 5-6); 39/39 green across every `scripts/` test
importing `hygiene_routine_tick`.

### Deferred

R3 (drift-aware restart) is NOT built. The open
`chip-20260908-decision-daemondrift-class-drift-aware-restart` remains the governing gate for
it, and this document is the evidence that its Option A must not be actioned as written --
see the held-out check above, plus the missing in-tick marker (R3a).

### GOV-HELDOUT-1 record

Outcome: **caught an over-broad rule.** The held-out check rejected the proposed Option A on
3 of 5 non-degenerate cases and surfaced a gate that does not exist. It also required a scope
correction to its own corpus (A-62 disqualified as derivation-chain evidence). This is the
claim's admissible evidence for this edit.
