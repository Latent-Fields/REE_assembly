# Curated pause-window agenda -- 2026-09-11

- **Assembled at:** 2026-09-11T23:20:50Z (session `curated-pause-g6-20260911`, DLAPTOP)
- **Authorisation:** user approved "Run the curated pause now" at pause-pressure gate
  generation 6 (2026-09-10, Orchestrator decision lane), re-affirmed 2026-09-11
  (recommendation ledger entry 239).
- **Chip:** `chip-20260910-curated-pause-window-g6` (claimed by this session
  2026-09-11T23:16:54Z after sitting OPEN and UNCLAIMED for ~27h).
- **Status of this document: PROPOSAL ONLY. NOTHING HAS BEEN HALTED, WITHDRAWN, OR
  RESOLVED.** The user was promised the agenda comes back before any halt. No other
  session's chip or claim was touched; no pause or hold sentinel was removed.

## 0. What this document is, and what it deliberately is not

It is **not** a third root-cause pass. That work is done twice already:
`pause_pressure_recurrence_rootcause_staged_20260902.md` (g3), and g5's 2026-09-08
resolution which fixed both generator drivers at source (pacing Fix A + Fix B).

It is **not** the execution of a codified playbook, because there is none.
`fleet_commit_sequencing_redesign_20260829.md` sections 10-11 describe a **one-time
bespoke campaign that already landed** -- a worked example, not a procedure. Section 12
records that this gate is itself still a **TRIAL**. (This framing was mis-read before and
corrected by the user on 2026-09-02; it is restated here so the next reader does not
re-make the error.)

It **is** the artifact the gate has asked for at six consecutive generations and never
received: a verified-halt proposal, a curated ranked agenda, and -- the half that has
never been written at all -- **restart criteria**.

**Headline finding, stated up front because it reframes everything below:** the backlog is
not stale, it is **unclaimed**. 118 chips are open; **exactly 2 are claimed**, one of them
by this session. The oldest open authored-and-unheld chip is **7 days** old and the median
is ~2 days. Nine of the ten open `proposal_tick` chips were minted in the last 24h and are
queue-experiment proposals -- i.e. the science-bearing generator is working. Meanwhile the
experiment queue sits at **depth 1, zero pending**, against a floor of 3. Chips are being
authored far faster than anything claims them, and the thing in short supply is **dispatch
and execution capacity, not curation**. Curating a young, unclaimed backlog cannot fix a
claim-rate problem, which is why five generations of symptom-curation have not held.

---

## 1. (a) Verified halt -- PROPOSAL, not executed

### 1a. What a halt would actually have to cover

| Plane | Component | Current state (measured 2026-09-11T23:17-23:20Z) |
|---|---|---|
| Control plane | `dispatcher_control.py` local | **STOP** -- lease by `orchestrate-20260830-closeout`, 2026-08-30T06:33:56Z (12 days) |
| Control plane | `dispatcher_control.py` ree-cloud-4 | **STOP** -- `orchestrate-20260910-2213`, 2026-09-10T23:12:21Z |
| Control plane | `dispatcher_control.py` ree-cloud-5 | **STOP** -- `orchestrate-20260910-2213`, 2026-09-10T23:12:28Z |
| Process plane | `dispatch_service.py` | **LIVE, pid 2500, uptime 4d 16h** |
| Process plane | `dispatch_executor.py` | **LIVE, pid 1436, uptime 4d 16h** |
| Mac capacity gate | `mac_dispatch_load.json` | `max_claude_sessions: 0`, `min_avail_mb: 0`, 4 live sessions, 1236 MB avail |
| Tick agents (launchd) | hygienetick, proposaldripfeed, igwroutine, steward, autopsystaging, chiparchive, workspacestaterotate, scriptscorpus, +11 | all **loaded** |
| Mac runner | `com.ree.runner` | **not loaded -- deliberately so** (standing user decision; see item R5) |

### 1b. The load-bearing point: a control-plane STOP is not a halt

The 2026-08-29 campaign learned this the hard way. Section 11's Phase A records: *"halt
made real (dispatch-service was live at pid 3750 despite the control-plane stop --
unloaded + verified)"*. **The same shape is true right now**: both dispatch processes have
been alive for 4d 16h while all three control-plane lanes read STOP.

This is not necessarily a fault -- section 11's restart note says dispatchers were left
"idling against the standing stop leases until the Orchestrator grants new ones (by
design)". A live-but-idling process is the intended steady state. **But that means
liveness cannot be read off `dispatcher_control.py status`, in either direction**, and
therefore:

> **A halt must be verified at the process plane and asserted from evidence, never
> inferred from the control plane.** Phase A's mistake is available to be repeated exactly
> because `status` returning three STOPs looks like proof and is not.

### 1c. Proposed verified-halt procedure (for the user to approve or decline)

Ordered, each step producing its own evidence line:

1. **Confirm no work is in flight before touching anything.**
   `task_claim.py list --status active` -- at assembly time five claims were active, of
   which `queue-stranded-1018-1003-20260911` and `igw-machinery-bundle-20260911` were
   actively mid-commit on coordination-plane paths. **A halt taken now would land on top
   of live work.** Wait for those to close, or exclude their paths.
2. **Confirm the queue has nothing running.** Currently `V3-EXQ-1023` is `claimed`.
   Halting while a run is claimed risks the duplicate-run failure the 6h stale-claim floor
   exists to prevent -- absence of telemetry is not abandonment.
3. **Stop the generators, not the executors first.** Unload the *authoring* agents
   (`com.ree.hygienetick`, `com.ree.proposaldripfeed`, `com.ree.igwroutine`,
   `com.ree.autopsystaging`) so the backlog stops growing during the window. This is the
   only step that actually addresses minting rate.
4. **Then make the dispatch halt real:** unload `com.ree.dispatch-service` and
   `com.ree.dispatch-executor`, and **verify by pid absence**
   (`ps -eo pid,command | grep dispatch_`), not by the control plane.
5. **Cloud side:** the two `ree-metaworker-healer.timer` units are *already* inactive on
   cloud-4 and cloud-5 (see R5) -- that half of the halt is, accidentally, already in
   force and has been reported as an enablement FINDING rather than as a halt.
6. **Record the halt in `wedge_repairs.jsonl`-adjacent evidence and in
   `WORKSPACE_STATE.md`**, with pids and timestamps, so the restart check in section 3 has
   a baseline to compare against.

**Explicitly NOT proposed:** stopping `com.ree.gitsyncrepair`,
`com.ree.gitwedgewatchdog`, `com.ree.indexlockwatch`, `com.ree.coordinatorbackup`, or the
hub's `sync_daemon`. Those are the coordination-data plane's safety machinery; halting them
converts a pause into an outage. Per standing doctrine the commit-guard and ref-move gates
must also stay **off** the hub and cloud workers throughout.

---

## 2. (b) The curated agenda

Ranked by how much each item unblocks, grouped by class. Every item carries a
work-graph debt classification. Dispositions are **recommendations to the user**; none has
been applied.

### Class A -- Capacity and throughput (the binding constraint)

| # | Item | Debt class | Source | Why it is on the list | Recommended disposition |
|---|---|---|---|---|---|
| **R1** | **Dispatch capacity, not chip authoring, is the binding constraint.** 118 open / 2 claimed (1 is this session). All 3 dispatchers STOP; local STOP for 12 days. `mac_dispatch_load.json` reports `max_claude_sessions: 0`. | `complicated (buildable)` -- the remedy is known and buildable; the *authorisation* to grant leases is a user decision, not a debt node | Measured this cycle; g7 episode; `dispatcher_control.py`; `mac_dispatch_load.json` | Five generations of curation have attacked authoring volume. The claim rate (1/119, 0.8%) is the actual failure. Nothing on the agenda below can execute while nothing claims. | **ESCALATE (decision D1).** Either grant dispatch leases and raise `max_claude_sessions` above 0, or accept the backlog as a deliberate parked queue and stop tripping a gate on its size. |
| **R2** | **Experiment queue STARVED: depth 1, 0 pending, floor 3** -- standing chip `chip-queuefloor-fleet-g9` at **generation 9**, the highest on the board. | `complicated (buildable)` -- 9 fresh proposals are already authored and ready to queue | g7 `episodic_generations`; `experiment_queue.json` | Generation 9 means 8 prior fires did not hold. **But the cause is now visibly NOT proposal supply**: 9 of 10 open `proposal_tick` chips were minted in the last 24h and are exactly "queue experiment X" tasks. The proposals exist; nothing claims them. Same root as R1. | **HOLD OPEN, do not withdraw**, and re-point it: its remedy is R1, not more proposals. `queue-stranded-1018-1003-20260911` is already recovering two orphaned scripts -- let it land first. |
| **R3** | **`chip-queuefloor-fleet-g9` is itself listed in the HOLD lane.** The single most science-bearing signal on the board is parked by a plan of record. | `complicated (buildable)` | `hold_lane.v1.json`, `held[]` | A hold is legitimate machinery, but holding the *starvation alarm* while the queue starves suppresses the one signal that measures scientific throughput. It re-trips the gate anyway via the `episodic generation >= 2` arm, so the hold buys nothing and costs visibility. | **ESCALATE (decision D2):** remove `chip-queuefloor-fleet-g9` from the hold lane at the next wave-planning regeneration. Recommend queue-floor alarms be made structurally non-holdable. |

### Class B -- The hold lane expires today (time-critical)

| # | Item | Debt class | Source | Why it is on the list | Recommended disposition |
|---|---|---|---|---|---|
| **R4** | **`hold_lane.v1.json` has a single global `review_after: "2026-09-11"` -- i.e. it expires as this document is written.** 45 entries; 24 are still-open **authored** chips. | `complicated (buildable)` | `hold_lane.v1.json` (`generated_at` 2026-09-08, `generated_by` campaign-w5-20260908) | The file's own schema note says *"a hold whose review_after has passed counts again automatically (a hold is not a hide)"*. So within hours `open_chips_authored_actionable` jumps from **68 to ~92** with no new chip authored at all, and the backlog arm trips harder. **The next gate fire will be an artifact of hold expiry, not of new pressure** -- and would be read as "the pause failed". No wave-planning session has regenerated the file since 2026-09-08. | **ESCALATE (decision D3), time-critical.** Either regenerate the hold lane from a current wave plan with per-entry review dates, or consciously let it lapse and accept the count. Doing neither produces a false generation-8 fire. |
| **R5** | **One global review date for 45 heterogeneous entries** is the stale-claim problem recreated one level up: a single expiry cannot express 45 different "why" and "when" pairs. | `complicated (buildable)` | `hold_lane.v1.json` schema | Per-entry `review_by` is a small schema change; the `held[]` array is currently bare strings with no reason and no per-entry date, so nothing can tell a 3-day hold from a 3-week one. | **RE-CHIP NARROWER:** move `held` from `list[str]` to `list[{chip_ref, why, review_by}]` and have `pause_pressure.py` evaluate per entry. |

### Class C -- Gate instrument defects (the gate is mis-measuring itself)

| # | Item | Debt class | Source | Why it is on the list | Recommended disposition |
|---|---|---|---|---|---|
| **R6** | **`wedge_repairs_7d` reported 0 while `logs/wedge_repairs.jsonl` holds 62 entries in the same 7 days.** `pause_pressure.wedge_repairs_7d()` counts only `outcome == "repaired"`; **all 91 log entries ever written are `not_repaired`**, 88 of them `REE_assembly/master`, 62 in the last 7 days, every one `reconcile_wedge_content: REFUSING -- the ahead range touches 46 path(s) outside the reconcilable allowlist`. | `complicated (buildable)` | `logs/wedge_repairs.jsonl`; `scripts/pause_pressure.py:276-294`; g7 episode `wedge_repairs_7d: 0` | The gate's wedge arm **has never been able to fire** and reports a clean zero while a repair path refuses 62 times a week. The plan of record names *"wedge_repairs.jsonl rate staying near zero"* as one of three falsifiable outcome measures -- so a measure the plan relies on is reading the wrong field. Note the class went quiet after 2026-09-10T10:01:59Z (~37h), consistent with the g4 refwedge class having been resolved 2026-09-09. | **RE-CHIP NARROWER:** count refusals and repairs on separate counters; alert on either. Until then treat "wedge_repairs_7d 0" as **no information**. |
| **R7** | **W7 enablement audit: 3 findings, of which 1 is a false positive.** Real: `ree-metaworker-healer.timer` **inactive on ree-cloud-4** and **inactive on ree-cloud-5**. False: `launchd:com.ree.runner local expected=loaded actual=NOT LOADED`. | `complicated (buildable)` | `scripts/audit_mitigation_enablement.py` (3 findings / 38 rows) | The Mac runner is **deliberately off by standing user decision** -- its absence is the user, not a fault. The audit encodes `expected=loaded`, so it will emit this finding forever, and it is one of the four arms that trips the pause gate (`enablement_findings 2 > 0`). A permanently-wrong expectation in a gate arm guarantees the gate can never reach a clean state. | **Two actions: (i)** start both healer timers (concrete commands already printed by the audit); **(ii) RE-CHIP NARROWER:** correct the `com.ree.runner` expectation to `ABSENT (doctrine)`, matching how cloud-4/5 commit-guard rows are already encoded. |

### Class D -- Leaked leases and stranded work

| # | Item | Debt class | Source | Why it is on the list | Recommended disposition |
|---|---|---|---|---|---|
| **R8** | **`chip-proposal-exp-1069` has been claimed by dispatched worker `5c4ff3c2` since 2026-09-10T20:20:59Z (>27h)** and has a matching stranded-worktree chip on ree-cloud-5 (`chip-strandedwt-ree-cloud-5-metaworker-chip-proposal-6655cdb581cc`). | `puzzle (known rules)` -- the rules are known; the missing fact is whether that worker is alive | Measured this cycle; `chip-strandedwt-*` chips | This is the one chip in the entire ledger that is genuinely blocked on a *lease*, and it is a science-bearing queue-experiment chip. Two sibling stranded-worktree chips (exp-0973, exp-0893) show the same leak. Absence of telemetry is not abandonment -- resolve by **ssh liveness check**, never by timeout. | **ESCALATE (decision D4):** check the worker over ssh. If dead, recover the stranded worktree content *before* unclaiming. Do not unclaim on age alone. |
| **R9** | **3 stranded-uncommitted-work chips on ree-cloud-5** (`metaworker-chip-proposal-exp-0973 / -0893 / -1069`), all minted today. | `complicated (buildable)` | `hygiene_tick` chips | Uncommitted work in a worktree is a loss risk, and all three are proposal-queueing work -- i.e. exactly the science-bearing lane R2 says is starved. | **Keep open, raise priority.** Recover content before any GC sweep touches those worktrees. |
| **R10** | **GC sweep: 79 worktrees** (`chip-metaworkergc-sweep-79-...`), plus **`chip-wtremoved-dlaptop-wizardly-meninsky-e6c09c`: a live worker in a REMOVED worktree.** | `complicated (buildable)` | `hygiene_tick` chips | 79 worktrees is the drift population; a live worker in a removed worktree is active data loss in progress. **Sequencing matters:** R9's recovery must precede any sweep, or the sweep destroys the stranded work. | **Keep open; sequence AFTER R9.** A merged branch with a clean tree is not sufficient evidence a worktree is safe to remove. |

### Class E -- Inert-awaiting-activation slices (the fifth gate signal, still manual)

| # | Item | Debt class | Source | Why it is on the list | Recommended disposition |
|---|---|---|---|---|---|
| **R11** | **Six phase-4 slices remain deliberately INERT pending one batched coordinator restart:** `/intent/replace` CAS + `ree_commit` transport branch; igw tick intake client; governance-flag verbs; chip-archive DB-strip verb; review_tracker; typed queue verbs. | `complicated (buildable)`, gated on a user-authorised restart | `fleet_commit_sequencing_redesign_20260829.md` section 11 "Deferred to post-restart phase-4 slices" | Section 12 makes this the gate's fifth signal and marks it **manual by design** -- so it is counted by a human or not at all, and at g7 it was not counted (the episode has no field for it). One slice is in flight now (`igw-intent-soak-eval-20260911` is evaluating the `/intent/replace` dual-write soak). The rest are shipped code that does nothing. | **ESCALATE (decision D5):** authorise one batched coordinator restart once the soak eval reports green. Note this is exactly the restart the 2026-08-29 campaign used as its W2 step, so the shape is proven. |
| **R12** | **The inert count has no machine-readable source**, so the gate's fifth arm cannot be evaluated, only remembered. | `complicated (buildable)` | `pause_pressure.py:364` `manual_reminder` | A gate arm that depends on a human remembering to count is an arm that reads 0 forever -- the same structural defect as R6 and R7. Three of five arms are therefore unreliable. | **RE-CHIP NARROWER:** add an `inert_slices.v1.json` alongside `hold_lane.v1.json`, regenerated at the same wave-planning step. |

### Class F -- Lower-priority, listed for completeness

| # | Item | Debt class | Source | Disposition |
|---|---|---|---|---|
| R13 | `scripts/` test corpus RED: 6 files (`chip-scriptscorpus-dlaptop-sweep-6-...`) | `complicated (buildable)` | hygiene_tick | Keep open. Note a worktree run is not a trunk verdict -- re-run from the main checkout before believing the count. |
| R14 | 2 stale-claim review chips, both `codex-showcase-build-20260911`, U_undetermined bucket | `puzzle (known rules)` | hygiene_tick (`audit_stale_claims`) | Keep open. An undetermined stale claim is never auto-closed; needs the per-commit content audit, not a shape argument. |
| R15 | 4 open `igw_tick` chips | `complicated (buildable)` | g7 `open_chips_by_origin` | Leave to the IGW lane; `igw-machinery-bundle-20260911` is actively fixing three tick/ledger defects right now. |
| R16 | 70 open authored-and-unheld work chips, oldest **7 days**, median ~2 days | see R1 | measured this cycle | **Do NOT bulk-curate.** These are young and unclaimed, not stale. Withdrawing fresh, still-valid work to make a counter go down is the failure mode this document exists to name. |

---

## 3. (c) RESTART CRITERIA

This is the half that has never been written. The pause ends -- and the generation counter
may legitimately be considered reset -- when **all** of the following are simultaneously
true, each checked by the named command, and the check recorded with its output.

### C1. Instrument integrity (must come FIRST -- an uncalibrated gate cannot certify anything)

| ID | Criterion | Check |
|---|---|---|
| C1.1 | `wedge_repairs_7d` counts refusals as well as repairs; refusal count is reported separately and is `<= 3/day` | `pause_pressure.py --json`, cross-read against `wc -l logs/wedge_repairs.jsonl` for the same window |
| C1.2 | `com.ree.runner`'s expectation is `ABSENT (doctrine)`, so the audit stops emitting a permanent false finding | `audit_mitigation_enablement.py` -- that row reads OK |
| C1.3 | Inert-awaiting-activation has a machine-readable source and a non-`None` count | the gate's fifth arm evaluates without a `manual_reminder` |
| C1.4 | Hold lane carries **per-entry** `review_by` | `hold_lane.v1.json` entries are objects, not bare strings |

**Rationale:** at generation 7, three of the gate's five arms were structurally unable to
fire (R6, R7, R12). Until C1 passes, a "clean" reading is not evidence of a clean state,
and a "pressure" reading may be an instrument artifact. **C1 is the real deliverable of
this pause.**

### C2. Substantive state

| ID | Criterion | Threshold | Check |
|---|---|---|---|
| C2.1 | Enablement findings | `== 0` (after C1.2) | `audit_mitigation_enablement.py` |
| C2.2 | Experiment queue | `depth >= 3` **and** `pending >= 1` | `experiment_queue.json` |
| C2.3 | No standing episodic chip at generation `>= 2` | `chip-queuefloor-fleet-g9` resolved on the merits (not withdrawn, not held) | `chip_ledger.py list` |
| C2.4 | Authored actionable open chips | `<= 40`, measured against a **non-expired** hold lane, with the held count reported alongside | `pause_pressure.py --json` |
| C2.5 | Authored `recorded_7d` | `<= 150` | `pause_pressure.py --json` |
| C2.6 | Claim rate | `>= 10%` of open chips claimed, **or** dispatchers deliberately STOP and the gate's backlog arms suspended accordingly | `chip_ledger.py list` + `dispatcher_control.py status` |
| C2.7 | No chip claimed `> 24h` unresolved | 0 | `chip_ledger.py list`; verify liveness by ssh, never by timeout |
| C2.8 | Stranded-worktree chips | 0 open, content recovered before any GC sweep | `hygiene_tick` chips |

### C3. The trend criterion (the one that actually tests whether the pause worked)

> **C3.1 -- Net authored chip delta `<= 0` for two consecutive 7-day windows.**

A single clean week can be produced by a quiet weekend. Two consecutive non-positive
windows is the weakest claim that distinguishes a real sink from a lull. The plan of record
already named this as one of its three falsifiable predictions; it has never been evaluated
against a threshold. **See section 4 -- it currently fails.**

### C4. Explicit anti-gaming clauses

These exist because the cheapest way to satisfy C2.4 is to destroy information:

- **C4.1** A chip withdrawn without a substantive reason does **not** count toward C2.4.
  Withdrawal is for work that is genuinely stale, duplicate, or superseded -- never for
  making a counter go down. R16's 70 young unclaimed chips are the specific temptation.
- **C4.2** Moving a chip into the hold lane does **not** satisfy C2.4. A hold is a stated
  reason plus a review date, per the file's own schema note; it is not a hide.
- **C4.3** Restart requires **C1 to pass first**. A restart certified by an instrument
  known to be mis-measuring is not a restart, and would generate generation 8 from the same
  blind spots.

---

## 4. (d) The NET CHIP SINK question, answered with numbers

Reconstructed from `TASK_CHIPS.json` (3,434 chips; birth timestamp available for all of
them) by counting, at each weekly boundary, chips born before the boundary and not yet
resolved at it. "AUTH" = `origin` in {`spawn_task`, `headless`} -- the authored population
the gate's backlog arm measures.

| Week ending | Open | Open AUTH | Recorded 7d (AUTH) | Resolved 7d (AUTH) | **Net AUTH 7d** |
|---|---|---|---|---|---|
| 2026-07-31 | 4 | 0 | 0 | 0 | +0 |
| 2026-08-07 | 15 | 14 | 92 | 78 | **+14** |
| 2026-08-14 | 9 | 8 | 312 | 318 | **-6** |
| 2026-08-21 | 23 | 18 | 373 | 363 | **+10** |
| 2026-08-28 | 57 | 45 | 284 | 257 | **+27** |
| 2026-09-04 | 106 | 86 | 294 | 253 | **+41** |
| 2026-09-11 | **119** | **95** | 299 | 290 | **+9** |

### The answer: NO. Curation is not a net sink. It trends UP.

Stated plainly, as the Orchestrator skill requires:

- **Open authored chips grew from 8 to 95 in four weeks -- an 11.9x increase.**
- **The net authored delta has been positive in five of the last six weeks**, and the one
  negative week (-6, 2026-08-14) is the only exception in the series.
- **The 2026-08-29 campaign did not reverse the trend.** The week *after* the campaign
  landed was the worst in the series (+41).
- **By the plan of record's own falsifiable prediction -- "open-chip count + chips/week
  trending DOWN under curation" -- the redesign is FALSIFIED as of 2026-09-11.**

### The one piece of genuine good news, stated with its caveat

The most recent week is **+9**, down from +41. Authored minting fell from 294 to 299 (flat)
while authored *resolution* rose from 253 to 290 -- so the improvement is on the
**resolution** side, consistent with the g5 pacing fixes (Fix A/Fix B) having landed
2026-09-08. That is real and worth saying.

**But +9 is still positive, and C3.1 requires `<= 0` for two consecutive windows.** One
decelerating week is not a sink. And **~24 hold-lane expiries land inside the next
window** (R4), which will push the measured actionable count up by ~24 with no new
authoring at all. **Expect the next reading to look worse for a purely mechanical reason.**
That artifact must not be read as the pause having failed -- which is precisely the
mis-reading this section exists to pre-empt.

---

## 5. (e) Why the approved remedy has never executed, twice running

This is the most useful thing in this document, so it is stated concretely rather than
diagnostically.

### The mechanism

1. **2026-09-10:** user approves "Run the curated pause now" at g6. The approval is
   discharged into a chip: `chip-20260910-curated-pause-window-g6`.
2. **The chip is authored `open` and `unclaimed`.** A `spawn_task` chip is, in the tool's
   own words, a *clickable UI suggestion* -- "a chip is showing for the user -- they can
   start it in a fresh worktree with one click, or dismiss it". **Authoring a chip is not
   scheduling work.** Nothing in the fleet claims chips autonomously.
3. **All three dispatchers were STOP** -- local since 2026-08-30, both cloud lanes since
   2026-09-10T23:12Z, i.e. ~3 hours *after* the approval. So the only machinery that could
   have picked the chip up was switched off within hours of the decision being taken.
4. **The Mac's own capacity gate reads `max_claude_sessions: 0`.** Even with a GO lease,
   the local lane would have dispatched nothing.
5. **27 hours later the chip is still unclaimed**, so the 6h-hysteresis gate re-evaluates
   the same unchanged world and mints **generation 7** (`chip-pausepressure-dlaptop-g7`).
6. **g7 is a duplicate of the consented g6, not a new decision** -- but it *looks* like
   escalating pressure, and its generation counter is read as "the symptom fixes are not
   holding". The counter is partly measuring its own unexecuted output.

### The three structural causes, named

- **C-I: The remedy is delivered by the same mechanism whose saturation is the problem.**
  The pause window's job is to reduce an unclaimed-chip backlog, and it is itself queued
  as an unclaimed chip. It lands at the back of the queue it was created to shorten. This
  is why it fails *specifically*, and why it will fail again next generation unless
  approved pause windows are executed **in-session at the point of approval** rather than
  chipped. **A user decision is not follow-on work; it is an instruction with an owner.**
- **C-II: Nothing claims chips, and the gate does not measure that.** 1 of 119 open chips
  was claimed before this session. The gate measures *authoring* (`open_chips`,
  `recorded_7d`) and never measures *claim rate*, so a total collapse of execution capacity
  presents as a backlog-size problem. Five generations of remedy have therefore been aimed
  at the wrong variable. (Criterion C2.6 exists to close this.)
- **C-III: The generation counter cannot distinguish "the fix did not work" from "the fix
  was never run".** g6 and g7 have identical evidence: the same unchanged metrics, because
  no remedy executed between them. A counter that increments on non-execution reads as
  worsening pressure and invites a *stronger* remedy, when the correct inference is that
  the previous remedy is still sitting in the queue. **Recommend the gate record, per
  generation, whether the prior generation's remedy chip was ever claimed** -- and suppress
  the increment when it was not. That single change would have prevented g7 from existing.

### What was different at the one time this DID work

The 2026-08-29 campaign executed in a single day because a **live session took the halt,
ran the sequence, and restarted the fleet in one continuous motion** -- it was never
chipped. Section 11's landing record is one session's work. That is the shape that worked,
and the shape that has not been used since.

---

## 6. Trial addendum (section 12 asks for this explicitly)

Section 12 makes the gate a TRIAL pending ~3 recorded outcomes, then a user decision to
codify, retune, or drop. This is one recorded outcome.

- **Did agenda assembly produce a manageable list?** **Yes** -- 16 ranked items from five
  named sources, ~35 minutes. The sources are well chosen: each contributed at least one
  item nothing else surfaced. This step is not the bottleneck and never was.
- **What was missing?** Three of the five gate signals could not be evaluated as
  specified: the wedge arm reads the wrong field (R6), the enablement arm carries a
  permanently-wrong expectation (R7), and the inert arm has no machine-readable source
  (R12). **The gate's own instrumentation was the largest finding of running it.**
- **Was this useful, just-discharged, or noise?** **Useful, but for an unintended reason.**
  The gate fired on backlog size; the finding is a claim-rate collapse and a
  self-referential generation counter. The gate detected real pressure via a proxy that
  mis-attributes its cause.
- **Recommendation on the trial:** **retune, do not drop, and do not yet codify.** Add a
  claim-rate arm (C2.6) and the prior-remedy-executed check from C-III; fix the three
  broken arms per C1. Codifying a skill around the current arms would codify the
  mis-attribution.
- **One honest limitation of this document:** it is a proposal assembled by one session in
  one sitting. It has not been checked against 3 historical cases where its restart
  criteria and the previous (absent) criteria would give *different* answers, because there
  are no previous criteria to differ from -- restart criteria have never been written. That
  is stated rather than papered over: **the restart criteria in section 3 are
  incident-scoped to generations 1-7 and should be treated as such** until a future
  generation tests them.

---

## 7. Decisions required from the user BEFORE any halt is taken

| ID | Decision | Why it cannot be taken without the user | Urgency |
|---|---|---|---|
| **D1** | **Grant dispatch leases and raise `max_claude_sessions` above 0, or formally accept the backlog as parked and suspend the gate's backlog arms.** | This is the binding constraint (R1/R2). Both answers are coherent; they lead to opposite agendas. Curating harder while nothing claims is the third option, and it is the one that has already failed five times. | **Highest** |
| **D2** | Remove `chip-queuefloor-fleet-g9` from the hold lane; make queue-floor alarms structurally non-holdable. | Changes what a plan of record parked. | High |
| **D3** | **Regenerate `hold_lane.v1.json` (per-entry review dates) or consciously let it lapse.** | `review_after: 2026-09-11` expires now; ~24 authored chips re-enter within hours and will produce a false generation-8 fire. | **Time-critical (hours)** |
| **D4** | Authorise an ssh liveness check on worker `5c4ff3c2` (chip-proposal-exp-1069, claimed >27h) and recovery of 3 stranded ree-cloud-5 worktrees before any GC sweep. | Touching another session's claim, and a wrong call here duplicates a run or destroys uncommitted work. | High |
| **D5** | Authorise ONE batched coordinator restart to activate the 6 inert phase-4 slices, once `igw-intent-soak-eval-20260911` reports green. | A coordinator restart kills anything in flight; user-authorised only. | Medium |
| **D6** | **Approve or decline the verified-halt procedure in section 1c**, including unloading the four *generator* agents and both dispatch processes. | Nothing has been halted. The user was promised this agenda first. **Note two active claims are mid-commit on coordination-plane paths and one queue item is `claimed` -- a halt taken right now would land on live work.** | Blocks the halt |

### Standing recommendation, independent of the above

**Stop chipping approved user decisions.** When the user approves an action in the decision
lane, the approving session should execute it, or hand it to a session with a granted lease
and confirm the claim -- not mint an `open` chip and consider the decision discharged.
Cause C-I is the whole reason this agenda is 27 hours late, and it is the cheapest of all
the findings to fix.
