# check_dispatch_fleet_health.py -- recurrence root cause

**Status: AWAITING USER REVIEW**

Written 2026-09-18T13:08Z by session `unruffled-northcutt-777a0f`
(`/metaworker-learning`), resolving
`chip-20260918-fleethealth-falsepositive-rootcause` (task_dac11683), which the
user routed here on 2026-09-18 via `orchestrate-20260918-gc` in preference to
(a) adding a fourth classifier branch and (b) inverting the detector to require
positive fault evidence immediately.

Method precedent (method only, no conclusions imported):
`scripts/pause_pressure.py`'s module docstring and
`pause_pressure_gate_root_cause_20260917.md`.

---

## 0. Summary

- The brief counted **four** structurally distinct causes. The real count is
  **six in this module**, plus **three more in the heartbeat producer** for the
  twin symptom. Every session that met one saw its own cause as novel; the
  undercount is itself part of the generator.
- **Root cause.** The fault predicate is `age(last_tick_utc) >= threshold`. That
  single number silently answers three independent questions -- *should this box
  be ticking?*, *can I see its ticks?*, *is it failing?* -- and returns the
  answer to the third regardless of the first two. Because it never asks the
  first, every legitimate reason for silence has to be enumerated after the fact
  as an exception. That is a complement set, and it grows with the architecture.
- **The evidence needed to answer question one already exists in this repo, and
  the adjacent check in the same skill step already reads it.**
  `scripts/dispatcher_pauses.json` has declared BOTH resident dispatchers
  `retired: true` since 2026-08-25; `dispatcher_control.json` has carried
  ree-cloud-4 at `requested_state: "stop"` since 2026-09-14T21:48:18Z.
  `check_metaworker_timer_state.py` consults the first and reports RETIRED (not
  a fault). `check_dispatch_fleet_health.py` runs ~10 lines earlier in
  `/metaworker-dispatch` Step 1, reads neither, and calls the same box a fault.
- **Measured precision: 1 clean true positive in 22 repair chips (4.5%)** -- and
  that one had already self-resolved (the box rebooted) before anyone acted on
  it, so the detector's single genuine catch drove no action either.
- **Live reading, 2026-09-18T13:06:44Z: 2 of 2 known machines flagged**, at
  least one a confirmed non-fault. The finding rate today is 100% of the fleet.
- **Recommendation: NARROW, do not retire and do not add branch four.** Gate on
  a positive EXPECTATION declaration first, and split the OBSERVABILITY arm out
  of the FAULT arm. This is *not* the "require positive fault evidence"
  inversion the user declined -- see section 6, which answers the blinding
  objection head-on.

---

## 1. The six generations (the table the brief asked for)

Each row is one remedy shipped against one instance of "a legitimately-idle box
is read as faulty". Commits are in `REE_Working`.

| G | Date | Cause | Remedy | Commits | Did it move the metric? |
|---|------|-------|--------|---------|--------------------------|
| **G1** | 2026-08-19/20 | **MIRROR LAG.** The *reading* box's own `REE_assembly` checkout lagged origin. Compounded: a box that writes its own heartbeat is permanently `[ahead N]` (the writer's throwaway-worktree cherry-pick is an "ACCEPTED RESIDUAL"), so `--ff-only` can never succeed there again and the refresh froze silently. | `refresh_heartbeats_repo()`; then an `origin/master` read-through fallback; then splitting fetch from merge so a merge timeout cannot discard a good fetch. | `b66c82a8`, `888e3d49`, `06cdf4c4` | Partly. Closed the cases it was written for. Left `chip-20260820-metaworker-repair-cloud4-heartbeat-stale` explicitly **unresolved**, which is what motivated the SSH probe. |
| **G2** | 2026-08-20 | **SCALER POWER-OFF.** The cloud-scaler cleanly powered an idle box off (`reason=scaler_idle_after_grace`). Silence was correct and intentional. | STALE-OFFLINE: corroborate against the sibling plain-runner heartbeat's `state == "offline"`, bounded to `--offline-suppression-hours` (6). | `d94b5c34` | Yes, for the case. **5 repair chips in ~36h** preceded it, every one resolving to this same non-fault. Applies only to dual-role boxes; a single-role dispatcher can never take the branch. |
| **G3** | 2026-08-20 | **SSH AUTH GAP.** A newly-added box's outbound key was never cross-provisioned, so an ssh probe got `Permission denied` from a box that was fully up. Raised repair chips against **two innocent boxes, in both directions, the same day.** | `SSH_AUTH_GAP` status; `refine_with_ssh_probe()` treats it like an unattempted probe. | `fa5c92c2` (probe), `e026298f` (auth gap) | **Only cosmetically.** Verified today at `check_dispatch_fleet_health.py:1046-1054`: on `SSH_AUTH_GAP` the pre-probe **STALE verdict survives**, and `STALE` is in `FAULT_STATUSES`. So the innocent box still gets a fault and still gets a repair chip; only the wording softened. |
| **G4** | 2026-08-21 | **COMMIT CADENCE != DISPATCH CADENCE.** The producer commits on state-change with a 30-minute `LIVENESS_FLOOR_MINUTES` fallback, so a healthy box legitimately presents a 30-35 minute-old tick. The threshold had been tuned against the 5-minute *dispatch* cadence. | `DEFAULT_STALE_MULTIPLIER` 3.0 -> 9.0 (15min -> 45min). | `0040be16` | Yes. Two identical false positives within ~1h on 2026-08-21 triggered it; no recurrence of that shape since. This is the one remedy that **recalibrated a threshold instead of adding an arm**, and it is also the one with no follow-on. |
| **G5** | 2026-09-01 | **PHANTOM MACHINE.** `test_ree_metaworker_heartbeat.py` posted a real `machine="ree-test-5"` row to the production coordinator; nothing was ever going to refresh it, so it surfaced as a permanent STALE dispatcher. | `KNOWN_ORCHESTRATOR_MACHINES` filter. | `e7e7b560` | Yes, for the case. Note the timing: the coordinator overlay landed **the same day** (`e3eddeb7`). A new source of truth arrived carrying a new false positive. |
| **G6** | 2026-09-17 | **LEASE STOP.** Resident dispatch timers retired 2026-08-25; dispatch now runs only under an Orchestrator lease. `orchestrate-20260913-1643` set ree-cloud-4 to `stop` at 2026-09-14T21:48:18Z. ~68.6h later the box is correctly not ticking and is flagged ALIVE-STALLED. | **None shipped** -- routed here. | -- | n/a |

**Not counted above, same symptom shape, different module.** The heartbeat
*producer* accreted three more remedies to "a correctly non-dispatching cycle is
reported as `health=stalled`": an independent `dispatch_usage_cooldown.py`
cross-check (`chip-20260820-...-stalled-13cyc`), `derive_health()` rule 6b
withheld-coverage (`...-stalled-withheld-explained`), and a second uncovered
narration path for the same rule, which itself had to be routed to
`/metaworker-learning` (`chip-20260822-metaworkerlearning-stall-coverage-gap-recurrence`).
So the honest total is **nine remedies across two modules for one symptom
shape.**

### 1a. Did the fixes work? The measurement, and its confound

| Window | Dispatch cycles (cloud-5 counter) | Fleet-health repair chips minted | Chips per 100 cycles |
|---|---|---|---|
| 2026-08-19T19:46Z (c3153) -> 2026-08-22T07:17Z (c3528) | 375 | 20 | **5.3** |
| 2026-08-22T07:17Z (c3528) -> 2026-09-17 (c3936) | 408 | 2 | **0.49** |

An ~11x drop in mint rate per cycle. **Do not read that as an 11x precision
gain.** Three reasons, all of which cut the same way:

1. **The chip count is deduplicated against open chips** ("raise a chip if none
   open"). Post-retirement the STALE conditions are *persistent* -- a
   lease-stopped box stays stale indefinitely -- so one chip absorbs hundreds of
   cycles of the same finding. The FINDING rate is not measured by this table.
2. **Both post-retirement chips were false positives** (G5 phantom, G6 lease
   stop). Per-chip precision in the post-fix window is **0/2**.
3. **A live reading today settles it.**
   `check_dispatch_fleet_health.py --no-pull --no-ssh-probe --json` at
   2026-09-18T13:06:44Z returns `findings: ["ree-cloud-4-metaworker",
   "ree-cloud-5"]` -- **every known machine, flagged**. ree-cloud-4 is the
   confirmed lease-stop non-fault. A detector whose finding set is "all
   machines, always" carries no information, which is the same degeneracy
   `pause_pressure.py` was retired as a gate for.

So: **the fixes reduced chip churn; they did not improve the classifier.** The
absolute quiet since 2026-08-25 is mostly because the detector stopped being
*run* (dispatch cycles fell ~10x when resident timers were retired), not because
it stopped being wrong.

### 1b. The cost

- **22 repair chips** minted by this detector's findings, each costing a
  `/metaworker-repair`-style diagnostic session.
- **8 further chips** spent fixing the detector itself (6 remedy chips, the
  decision chip, and this root-cause pass).
- **3 producer chips** for the twin STALLED symptom.
- **~33 sessions**, of which **one** (`chip-20260819-...-cloud4-orchestrator-stale-15h`)
  concerned a genuinely faulty dispatcher -- and that box had rebooted itself
  before the session started, so no repair was performed there either.

Outcome tally of the 22:

| Outcome | n | share |
|---|---|---|
| Probed dispatcher genuinely faulty | 1 | 4.5% |
| Real defect found, but in the heartbeat PRODUCER, not the probed dispatcher | 4 | 18% |
| Confirmed non-fault / self-resolved, no defect anywhere | 15 | 68% |
| Undetermined (claim contention, deferred) | 2 | 9% |

---

## 2. Testing the three candidate readings from the brief

### (a) "The detector infers fault from absence." TRUE, but not the whole shape.

All six causes do share that shape. But the naive corollary -- *stop inferring
from absence* -- is contradicted by the producer's history: `derive_health()`
already reports **positive**, self-observed evidence (`health=stalled`,
`dead-on-arrival`, computed by the box's own wrapper at the cycle it describes),
and it **still** produced three false-positive generations of its own. Positive
evidence is not sufficient, because the producer was also asking "did the
expected action happen?" without asking "was it supposed to?".

The sharper statement is therefore: **fault is inferred from the non-occurrence
of an expected action, while the expectation itself is never modelled.**

### (b) "The architecture moved and the detector did not." TRUE, and it is the generator.

| G | Architecture change the detector was never told about | Detector predates it? |
|---|---|---|
| G1 | `retry_push_via_worktree`'s permanently-`[ahead N]` checkout (documented as an ACCEPTED RESIDUAL in the producer) | yes |
| G2 | cloud-scaler idle power-off | yes |
| G3 | ree-cloud-4 became a dual-role dispatcher 2026-08-18 with a key never cross-provisioned | yes |
| G4 | producer commits on state-change + a 30min liveness floor | yes |
| G5 | coordinator `/shadow/status` overlay (landed the **same day** as the false positive) | same day |
| G6 | resident timers retired 2026-08-25 -> lease-gated dispatch | yes |

Six for six. The detector duplicates, rather than derives, its assumptions about
who ticks, how often, and why they would stop -- and each of those is owned by a
different component that changes independently.

### (c) "The detector is solving the wrong problem." PARTLY -- and this is the decisive part.

**Who consumes the verdict?** Exactly one live consumer:
`.claude/skills/metaworker-dispatch/SKILL.md` Step 1 (mirrored in `.agents/`).
Nothing else reads it -- no cron, no dashboard, no gate. The documented action
on a fault is: report it in the cycle summary, and raise a `/metaworker-repair`
chip if none is open. Given section 1b, that pipeline has spent ~22 sessions to
surface one already-self-resolved outage.

**But the sharper problem is that the detector's subject has been deleted.** Its
question is "is every OTHER resident dispatcher actually dispatching?". Since
2026-08-25 there are no resident dispatchers: the orchestrator heartbeat is
written by the dispatch wrapper, the wrapper runs only inside a dispatch cycle,
and dispatch cycles happen only while an Orchestrator holds a lease. So heartbeat
freshness no longer measures dispatcher health -- it measures *whether an
Orchestrator happened to be driving that box recently*, which the detector has no
model of at all. G6 is not an edge case; it is the ordinary state of the fleet.

**This is why retirement is tempting and still wrong.** The 2026-08-19 incident
(both cloud dispatchers out 12+ hours while the Mac reported healthy) was real
and expensive, and its successor shape is live: *a box holding a `run` lease that
is not ticking*. Today's reading shows exactly that for ree-cloud-5 (lease
granted 12:18:08Z today, expires 15:18:08Z; last tick 2026-09-17T16:08:26Z, ~21h
old). Under the proposal in section 3 that finding **survives**. Under retirement
it disappears.

---

## 3. Proposed durable fix

Split the one predicate into three, mirroring `pause_pressure.py`'s BACKLOG /
GENERATOR arm split -- two arms that trip independently and **route to different
remedies**.

### Arm 1 -- EXPECTATION gate, evaluated first, no I/O

Before any staleness arithmetic, ask the authoritative declarations already in
the repo whether this box is supposed to be emitting ticks:

- `scripts/dispatcher_pauses.json` -- `retired: true` => NOT-EXPECTED
  (permanent); a live `paused_at..clear_at` window => NOT-EXPECTED.
- `dispatcher_control.json` -- `requested_state != "run"`, or a `run` lease whose
  `expires_at` has passed, or no entry at all => NOT-EXPECTED.

A NOT-EXPECTED box reports `NOT-EXPECTED` with the declaration and its
timestamp, is **not** a fault, mints no chip, and **skips the ssh probe
entirely** (so the arm is also strictly cheaper than today).

This is the same mechanism `check_metaworker_timer_state.py` already uses
(`PAUSED-DECLARED` / `RETIRED`), against the same ledger, in the same skill step.
It is not a new idea in this codebase; it is an idea this module was never given.

### Arm 2 -- OBSERVABILITY, separated from FAULT

When a box IS expected and its tick is stale, the existing evidence chain
(`heartbeats_repo_refresh` status, the ssh probe) decides whether the *checker*
can see it:

- refresh failed, `SSH_AUTH_GAP`, or `ALIVE_MIRROR_LAG` => an **observability**
  finding, named against the **observer** (fix the checkout, provision the key,
  fix the push pipeline). Reported, but it **must not** raise a
  `/metaworker-repair` chip against the probed box.
- Today `SSH_AUTH_GAP` leaves `STALE` standing, and `STALE` is a fault. That is
  the recorded 2026-08-20 harm, still live in the code.

### Arm 3 -- FAULT

Expected + observable + not ticking => the real finding, and the only one that
mints a repair chip. `DOWN_UNREACHABLE` and `ALIVE_STALLED` stay exactly as they
are.

### Files

- `scripts/check_dispatch_fleet_health.py` -- new `NOT_EXPECTED` and
  `OBSERVABILITY` statuses, an `expectation_for_machine()` reader over the two
  declaration files, ordering the gate before `classify_machine()`;
  `FAULT_STATUSES` narrowed accordingly. Fail-open convention preserved: an
  unreadable or malformed declaration file means **EXPECTED** (fail toward
  flagging), the opposite direction from the ssh probe and matching
  `check_metaworker_timer_state.py`'s `load_declared_pauses()` asymmetry.
- `scripts/test_check_dispatch_fleet_health.py` -- extend (do not add a parallel
  suite), following the existing tempdir/injected-fixture pattern. Negative
  controls for each arm, plus a regression test replaying G3's shape end to end.
- `.claude/skills/metaworker-dispatch/SKILL.md` **and**
  `.agents/skills/metaworker-dispatch/SKILL.md` -- Step 1's bucket list, both
  copies, identical.

---

## 4. Held-out check (GOV-HELDOUT-1)

The rule was written from **G6** (lease stop), which is therefore excluded.
Cases are replayed against the **current** code, not the code of their day;
degenerate cases (old and new agree) are reported, not hidden.

### Genuinely differ -- 3 found

1. **`chip-20260820-metaworkerrepair-cloud4-unreachable-sshdenied` and its
   mirror-direction sibling `chip-20260820-cloud5-heartbeat-stale-ssh-permdenied`**
   (counted as ONE root cause per `/metaworker-learning` Step 1). CURRENT: the
   auth gap leaves `STALE` standing, `STALE` is in `FAULT_STATUSES`, so a repair
   chip is owed against a box the checker demonstrably cannot see -- which is
   what happened, against two innocent boxes, in both directions. NEW: arm 2
   routes it to the observer (key provisioning), no repair chip against either
   box. **Different, and right.** Held out: the rule was written from a lease,
   not from ssh keys.
2. **The live fleet reading, 2026-09-18T13:06:44Z.** CURRENT: both machines
   STALE, two findings, two repair chips owed. NEW: ree-cloud-4 declared `stop`
   since 2026-09-14T21:48:18Z => NOT-EXPECTED, no chip; **ree-cloud-5 holds a
   live `run` lease and is 21h stale => still a FAULT, chip owed.** Different on
   one machine, identical on the other -- which is the point: the gate removes
   the false positive and keeps the real one. (Recorded honestly: this is a
   same-day case, but it is one the rule was not written from -- the
   leased-and-silent shape was found during this pass, not before it.)
3. **`/governance`-adjacent class evidence: `chip-20260829-metaworkerlearning-staleclaim-orchestrator-lease-recurrence`.**
   `audit_stale_claims.py` kept flagging the Orchestrator's own long-running
   dispatcher-LEASE claim as `C_no_trace` stale, every ~4h tick, each one costing
   a manual Healer review. CURRENT fleet-health wording has nothing to say about
   it. NEW: the same rule -- *a declared, live lease is an expectation, and
   silence under it is not evidence of abandonment* -- gives the right call in a
   **third** module. Different, right, and from a module the rule was not written
   against. This is the case that argues the rule is class-level rather than
   scoped to its incident.

### Do NOT differ -- reported for honesty

- **G5 (`chip-20260901-...-reetest5-stale`).** CURRENT already filters it via
  `KNOWN_ORCHESTRATOR_MACHINES`. NEW also drops it (no declaration). Same
  verdict. **DEGENERATE.**
- **G2 (`chip-20260820-...-cloud4-stale-127min`).** CURRENT: STALE-OFFLINE via
  sibling corroboration, not a fault. NEW: `retired: true`, not a fault. Same
  verdict, different route. **DEGENERATE** on verdict. (They *would* differ past
  the 6h suppression bound, where CURRENT reverts to a fault -- but that is the
  same shape as G6 and is not independent of it, so it is not counted.)
- **G4 and the various sub-45-minute cadence chips** (`...-cloud4-stale-3414`
  18.5min, `...-cloud4-heartbeat-stale` 16.5min). CURRENT: under the 45-minute
  threshold, HEALTHY. NEW: identical. **DEGENERATE.**
- **The STALLED family** (`...-stalled-withheld-explained`,
  `...-stalled-allwithheld-cycle3528`). Fixed in the producer's
  `derive_health()`; the expectation gate passes and arm 3 still reports a fault.
  **DEGENERATE** -- this proposal does not touch the STALLED twin, and should
  not be sold as if it did.

**Verdict: 3 non-degenerate cases found, from three different modules.** The
threshold is met. The honest counterweight: case 2 is same-day rather than
historical, and cases 1 and 3 both turn on the *routing* of a finding rather than
its truth value, so the check establishes that the rule is class-level and
correctly routed -- it does not independently establish that arm 1 never
suppresses a real outage. Section 6 addresses that separately.

**Cost of this check, stated rather than skipped:** roughly 40 minutes of the
pass, mostly spent replaying cases against current rather than contemporaneous
code -- and it changed the proposal, by killing two cases (G2, G5) that a
cheaper check would have counted.

---

## 5. Why this is not branch four

The brief's binding constraint. The test is whether the change *terminates* the
enumeration or joins it.

- **A branch enumerates one more member of a complement set.** "Silence is a
  fault unless it matches one of {scaler-off, mirror-lag, auth-gap,
  commit-cadence, phantom-row, lease-stop}". That set has no closure condition:
  it grows whenever anything upstream changes the reasons a box may legitimately
  stop, which section 2(b) shows happened six times in four weeks.
- **Arm 1 inverts the quantifier on one of the three questions.** "Silence is a
  fault only where a declaration says the box should be running." That set is
  positively enumerated with a single source of truth, and it is a source that
  **already receives** new architectural stops: the 2026-08-25 retirement went
  into `dispatcher_pauses.json`, the lease went into `dispatcher_control.json`.
  G2, G5 and G6 would each have required **zero** detector change under the new
  shape.
- **Stated scope limit, so this is not oversold.** Arm 1 does **not** prevent
  G1, G3 or G4 -- those are observability and cadence problems, and they will
  keep occurring. Arm 2 does not stop them either; it stops them from being
  *mis-routed as faults of the probed box*, which is the recorded harm. G4's
  class (a producer-cadence assumption duplicated into the detector) remains
  genuinely open, and the only honest mitigation is the one G4 itself used:
  recalibrate the threshold, do not add an arm. `pause_pressure.py`'s failure
  mode (b) -- "every generation added an arm; none recalibrated one" -- applies
  to this module too and should be written into its docstring.

---

## 6. Does the gate blind the detector to a real outage?

The user's explicit objection to the direct inversion, and the reason this pass
exists. Taken in three parts.

1. **For a box declared to be running, nothing changes.** Arm 1 only ever
   suppresses a box whose declaration says it should NOT be ticking. A box under
   a live `run` lease is still judged exactly as it is today -- demonstrated on
   live data in held-out case 2, where ree-cloud-5's finding survives.
2. **Replaying the one genuine outage.**
   `chip-20260819-...-cloud4-orchestrator-stale-15h` (~16.25h, box powered off).
   With its contemporaneous declarations -- no lease system, no retirement, timer
   armed -- ree-cloud-4 was EXPECTED, so arm 1 passes and the fault stands.
   **Still caught.**
3. **The residual, named rather than papered over.** The gate is only as good as
   the declaration. Two failure modes: a `run` lease that expires while an
   Orchestrator is still driving (silence then reads as NOT-EXPECTED when it is
   really a fault), and a retirement the user reverses without editing the file.
   Both are the *same* residual `check_metaworker_timer_state.py` already carries
   and already manages, with `PAUSE-EXPIRED` and `RETIRED-BUT-ARMED` -- i.e. the
   ledger is itself audited for staleness. The mitigation here is the mirror
   image: **an EXPECTED-but-silent box is a fault (arm 3), and a NOT-EXPECTED box
   that IS ticking should be reported too** (something is dispatching unleased,
   which is the ~513-ticks/day runaway the retirement exists to prevent). That
   second report is a capability the current detector does not have at all, and
   it is a net gain in coverage, not a loss.

**This is materially narrower than the inversion the user declined.** That option
was "require positive fault evidence"; this is "require positive *expectation*
before absence counts as fault evidence". Absence remains admissible evidence --
for exactly the boxes that are supposed to be up.

---

## 7. Options for the decision chip

- **A (recommended).** Build arms 1-3 as specified: expectation gate, plus the
  observability/fault split. Full scope, ~1 session.
- **B (cheap 80%).** Arm 1 only. Removes G2/G5/G6 and the current 100% finding
  rate; leaves the G3 mis-routing harm in place.
- **C.** Retire the detector. Defensible on the 4.5% precision number alone, and
  explicitly licensed by the brief -- but it discards the leased-and-silent
  finding that is live on ree-cloud-5 today, which is the direct successor of the
  incident the detector was built for. Not recommended.
- **D.** Hold. Not recommended: the detector currently flags 100% of the fleet
  every run, which trains readers to ignore it -- the failure mode
  `check_metaworker_timer_state.py`'s own docstring names as how the 2026-08-15
  outage went unnoticed for 8h02m.

---

## 8. Loose end found in passing, NOT part of this proposal

**ree-cloud-5 holds a live `run` lease (granted 2026-09-18T12:18:08Z by
`orchestrate-20260918-gc`, expires 15:18:08Z) and its last orchestrator tick is
2026-09-17T16:08:26Z, ~21h old.** Under either the current or the proposed
classifier that is a genuine finding. It is outside this chip's scope and is not
being diagnosed here; flagging it so it is not lost.
