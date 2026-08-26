# Lease-outlives-claim recurrence investigation (2026-08-26)

chip-20260826-lease-outlives-claim-recurrence, spawned off
chip-20260826-cloud4metaworker-orchestrator-stalled-2hr-cycle743 (a Healer /
`/metaworker-repair` finding on ree-cloud-4). Question asked: should
`dispatcher_control.py grant`/renew require or verify a live `TASK_CLAIMS.json`
claim before granting or renewing an Orchestrator's Dispatcher run lease?

## tl;dr

**No, do not gate `grant`/renew on a live TASK_CLAIMS claim.** The lease
already has the correct safety property (fail-closed, bounded expiry) and
every confirmed occurrence of this recurrence stayed inside that bound --
none was the unbounded-runaway failure the lease exists to prevent. Coupling
two independently-designed subsystems (a resource-contention ledger and a
spend-control lease) on a free-text identity match that nothing enforces
would trade a real, working safety property for a fragile one, to guard
against a risk that is already capped.

**What was actually wrong, once traced:** the one confirmed no-live-session
case was an Orchestrator session that had already run `/session-land` once
(closing its TASK_CLAIMS claim), was later **resumed**, and kept renewing the
lease for hours without re-opening a claim. CLAUDE.md's "open a claim first"
is written as a before-starting step, which is easy to skip on a resume
because the session already feels oriented.

**What shipped (low-risk, print-only, does not touch the lease's safety
contract):**
- `scripts/dispatcher_control.py`: `grant` now prints an advisory
  `WARNING: no active TASK_CLAIMS.json claim for session_id=...` when the
  `--by` identity has no matching active claim, via a new `claim_advisory()`
  helper. It is informational only -- it never refuses the grant, never
  changes the exit code, and fails open (no warning) on any read/parse
  problem with `TASK_CLAIMS.json`, exactly the opposite failure direction
  from the lease itself. Gated the same way `commit_control_file` already
  gates git activity (`_path_inside_base`, extracted from that function so
  both share it): a `--path` outside `BASE` (every pre-existing test
  fixture) never touches the real `TASK_CLAIMS.json`.
- `.claude/skills/metaworker-orchestrate/SKILL.md` (+ its `.agents/` mirror)
  Step 1: an explicit resume-case instruction to re-check the TASK_CLAIMS
  claim before renewing, naming the new warning and this chip.
- Tests: `ClaimAdvisoryTests` (8 cases) and `PathInsideBaseTests` (3 cases)
  in `scripts/test_dispatcher_control.py`. Full file green (59 tests) and
  the pre-existing `test_dispatcher_control_push_default.py` (12 tests)
  unaffected by the `commit_control_file` refactor.

## Background: what the two subsystems actually are

**`dispatcher_control.json` (the lease)** exists to bound unattended spend.
Per its own module docstring, it was built after ~513 dispatch ticks/day
across two boxes burned a weekly token budget in under two days because
nothing ever told the Dispatcher to stop when its Orchestrator went away. It
is deliberately **fail-closed**: missing, unreadable, malformed, or expired
all mean STOP, inverting this codebase's usual fail-open convention, because
"failing open here spends money unattended and is invisible until the budget
is gone, while failing closed costs one Orchestrator cycle to notice and
fix." A grant **expires** (`expires_at`) and is clamped to
`MAX_LEASE_HOURS` (6) regardless of what is requested, so even a session that
dies without ever calling `stop` bounds the Dispatcher's unattended runway to
at most 6 hours -- mirroring `remote_pytest.sh`'s `PYTEST_LEASE_MAX_MIN` for
the identical reason: "a lease holder that dies without cleaning up should
bill for a bounded time, not forever."

**`TASK_CLAIMS.json` (the claim)** exists to prevent resource contention
between sessions editing the *same shared files*. Per CLAUDE.md's
Concurrency Rules, a claim is a "cheap broadcast," opened once when a
session knows the task and its resources, and arbitrated (`task_claim.py
open` refuses with exit 3) only on an exact match of a **file**-shaped
resource against another *active* claim. It has no expiry of its own; the
closest thing is the 6-hour "stale" threshold `audit_stale_claims.py` uses
to *flag* (never auto-close, except in narrow reaped buckets) an old active
claim for human review.

These solve different problems, for different failure directions, with
different lifecycles. The lease's danger is *silence licensing spend*; the
claim's danger is *silence causing two sessions to collide on a file*. There
is no existing contract that a claim must be open for a lease to be valid,
and the Orchestrate skill does not create one: `metaworker-orchestrate/
SKILL.md`'s "Before starting" section opens ONE claim, once, before Step 1;
Step 1 says to renew the **lease** "on every cycle... not once at the
start," with no parallel instruction to renew or re-verify the claim on the
same cadence.

## Root-cause trace of the actual incident

From the raising chip (`chip-20260826-cloud4metaworker-orchestrator-stalled-2hr-cycle743`):

- `dispatcher_control.json` held an active, valid lease for both
  `ree-cloud-4` and `ree-cloud-5`, `requested_by: "insights-7fd98a"`,
  `requested_at` ~07:50Z, `expires_at` ~09:50Z (the 2-hour default --
  nobody passed `--lease-hours`).
- `TASK_CLAIMS.json` had **zero** active claims for `session_id
  "insights-7fd98a"`. Its most recent entry for that session_id had been
  **closed with `status: "done"` at 01:20:41Z** -- 6.5 hours *before* the
  07:50Z lease renewal.
- The dispatch tick itself (`ree-cloud-4-metaworker.json`) had stalled at
  cycle 743 since 07:32:53Z, >2h before the finding.
- This exact shape (ALIVE-STALLED dispatch tick, correlated by hand against
  TASK_CLAIMS) had recurred **6+ times**; the prior 5 all self-resolved
  within 18-30 minutes (the orchestrator ticked again, or the stall was a
  legitimate cooldown / a since-fixed `WITHHELD`-coverage false positive).
  This 6th was the first to persist for hours and affect both boxes at once.

That a *closed* claim preceded a *later* lease renewal under the same
`session_id` is the interesting fact, and it points at a specific mechanism
rather than a generic "sessions forget to claim things" shrug: something
calling itself `insights-7fd98a` renewed the lease at 07:50Z, **after** a
session by that same name had already gone through a proper close (a
`status: done` closure, not an abandoned `active` entry going stale). The
natural explanation, and the one this investigation adopts, is a **resumed**
session: `CLAUDE.md`'s Worktree Session Naming section documents `cd
<worktree> && claude --resume` as the standard way to pick a session back up,
and the HEADLESS WORKER CONTRACT preamble independently confirms
`claude -p --resume` is now a live mechanism for delivering an Orchestrator
session a further turn. A session resumed hours after its own
`/session-land` would re-enter its conversation already "oriented" and would
have no textual cue in the skill telling it to re-open a claim -- only to
re-run Step 1's lease renewal, which it evidently did.

This reframes the finding: it is **not** evidence that the lease design is
unsafe (the lease did exactly what it is supposed to do -- it expired
naturally at ~09:50Z, which is within the 6.5h `chip-20260826-
cloud4metaworker-orchestrator-stalled-2hr-cycle743` was raised inside). It
**is** evidence of a narrower, already-known class of gap: CLAUDE.md's own
"why the first-action claim instruction is a mitigation, not a solution"
note already documents that nothing enforces a spawned or resumed session
actually running its claim-open step, and a **code-level auto-claim was
tried once for a structurally similar case (`chip_ledger.py record
--task-id`, 2026-08-22 to 2026-08-25) and reverted** because it inferred
liveness from the wrong signal (a `task_id` existing does not mean a session
is running yet). That precedent argues for the same caution here: do not
infer TASK_CLAIMS liveness from the lease, or vice versa, by code.

## Should `grant`/`renew` require a live claim? No -- three independent reasons

1. **Identity is not actually shared between the two systems.** `--by` in
   `dispatcher_control.py` is free text ("this session's slug"); TASK_CLAIMS'
   `session_id` is populated by a separate `task_claim.py open` invocation.
   In the confirmed incident they happened to match
   (`insights-7fd98a` both places), but nothing enforces that -- a session
   that opens its claim under one label and renews the lease under another
   (a typo, a different worktree-derived default, a human editing `--by` by
   hand) would be a **legitimate, live** Orchestrator that a live-claim gate
   would incorrectly refuse. The task explicitly asked to avoid exactly this
   failure mode, and there is no reliable way to close it without inventing
   a new, enforced identity contract between two subsystems that were built
   independently and are documented as solving different problems.

2. **The risk this would guard against is already bounded, and the gate
   would not even close the actual gap.** The lease's own expiry already
   caps the downside at `MAX_LEASE_HOURS` (6). Every one of the 6+
   recorded occurrences resolved within that bound -- none matched the
   unbounded ~513-ticks/day pathology the lease exists to prevent. A
   liveness gate on `grant` could, at best, shorten that bound slightly (by
   refusing a *renewal* once the claim is gone); it could not have prevented
   the *original* grant, since the very first `grant` of a session's lease
   is legitimately called before Step 0's "open a claim" reliably lands in
   every path (skills are followed by convention, not enforced order), so
   gating the primitive itself risks a chicken-and-egg refusal on the
   ordinary happy path, not just the failure path.

3. **This mirrors a fix already tried and reverted nearby.** Auto-claiming
   a chip at `record --task-id` time (2026-08-22 to 2026-08-25) was reverted
   specifically because it inferred "session is live" from the wrong
   artifact (`task_id` existing, when `spawn_task`'s launch is not
   immediate). A TASK_CLAIMS-liveness gate on `grant` has the same shape:
   inferring "Orchestrator is live" from an artifact (a claim entry) that a
   legitimate live session may simply not be holding at that instant for
   reasons unrelated to being dead (mid-transition between two claims,
   claim intentionally scoped narrower than the whole session's lifetime,
   etc.). CLAUDE.md's own held-out-check discipline (GOV-HELDOUT-1) asks for
   >=3 non-degenerate historical cases before shipping a standing-rule
   change; this investigation found exactly one confirmed no-live-session
   case (the rest self-resolved as ordinary tick-cadence noise), which is
   itself evidence the rule would be scoped to a single incident rather than
   a real recurring failure of the *lease*, as opposed to a real recurring
   *false alarm* from the health check that correlates the two signals.

## A cheaper/more robust liveness signal? Investigated and also rejected

The task asked to investigate recording the issuing PID/session and checking
it is still live, as a cheaper alternative to cross-referencing
TASK_CLAIMS.json. This does not actually work here, for a structural reason
specific to this fleet:

- The Orchestrator "must run locally, interactively" (per
  `metaworker-orchestrate/SKILL.md`'s opening line) -- in practice, on the
  Mac. The Healer that raised this finding runs on `ree-cloud-4`/`ree-cloud-5`.
- Every SSH path in this codebase runs **Mac -> cloud only** (documented in
  the same skill's Step 2, confirmed live: the Mac's sshd is reachable over
  WireGuard but no cloud box's key is in its `authorized_keys`). A remote
  Healer has **no way to `ps -p <pid>` the Mac** at all, so a PID recorded in
  the lease would be unverifiable from the one place that actually needs to
  verify it.
- `TASK_CLAIMS.json`, by contrast, is git-tracked and therefore already
  propagated to every box via the normal commit/pull cycle -- which is
  exactly why the Healer was *able* to read it and notice the mismatch in
  the first place, despite its other weaknesses (see above). It is already
  the cheaper cross-host-readable signal; a PID would be a *more* expensive,
  *less* available one for this specific direction of check.

A different candidate -- treating `requested_at` staleness (i.e. "this lease
hasn't been *renewed* in longer than expected, even though it hasn't
*expired* yet") as the liveness signal, by analogy with
`check_dispatch_fleet_health.py`'s well-tuned 45-minute STALE threshold for
Dispatcher tick heartbeats -- was also considered and rejected for now: that
threshold is tunable because the Dispatcher has a documented, fixed
`DEFAULT_CADENCE_MINUTES` (5) to compare against. The Orchestrator has no
declared renewal cadence anywhere (`metaworker-orchestrate/SKILL.md` says
"every cycle," never a number), because it is a human-paced interactive
session, not a timer. Any threshold chosen here would be an unfounded guess
at how often a human actually re-visits the session, and a wrong guess in
either direction reproduces exactly the false-positive-vs-missed-detection
tradeoff `check_dispatch_fleet_health.py`'s own docstring spent multiple
incidents tuning for the *Dispatcher's* cadence. Worth revisiting only if
the Orchestrate skill ever gains a declared, enforced renewal cadence.

## What shipped, and why it is safe

Given the above, the fix targets the actual traced root cause (a resumed
session skipping claim re-verification) rather than the lease's contract:

- **`dispatcher_control.claim_advisory(by, claims_path=None)`** (`scripts/
  dispatcher_control.py`): reads `TASK_CLAIMS.json`, returns a warning
  string when no entry has `session_id == by and status == "active"`, else
  `None`. Fails open (returns `None`, i.e. no warning) on any missing file,
  unreadable file, malformed JSON, or unexpected shape -- deliberately the
  opposite failure direction from the lease itself, because a false
  "you forgot to claim" nag from a transient read glitch is worse than an
  occasional missed one for something print-only.
- Wired into `main()`'s `grant` handler only (which is also what "renew"
  is -- there is no separate renew subcommand; renewing a lease means
  calling `grant` again). It never affects the exit code or return value,
  and is gated behind `_path_inside_base(args.path)` (extracted from
  `commit_control_file`'s pre-existing BASE-containment check, now shared)
  so every existing test, which points `--path` at an isolated tempdir
  outside `BASE`, continues to run with zero real filesystem or git access
  -- confirmed by `test_grant_cli_never_touches_the_real_task_claims_for_a_
  test_fixture_path` and the full pre-existing suite staying green.
- `.claude/skills/metaworker-orchestrate/SKILL.md` (+ `.agents/` mirror)
  Step 1 gained an explicit instruction for the resume case, naming the new
  warning and this chip so a session seeing it knows exactly what to do
  (`task_claim.py open` again) without having to re-derive the reasoning.

This is a `worktree_edit_guard.py`-shaped intervention: informational,
always exits/returns cleanly, never blocks the action it observes. It gives
a human (or a resumed session) at the point of `grant` exactly the same
signal the Healer had to reconstruct after the fact, hours later, from a
different box -- for one extra local file read, on a code path that already
does file I/O.

## What did NOT ship, and why

- **No requirement that `grant`/`renew` have a matching active claim.** See
  "Should grant/renew require a live claim? No" above.
- **No PID-based liveness recording.** Unverifiable from the box that would
  need to verify it (see above); would also do nothing for the confirmed
  incident, since the Mac was never asked whether its own PID was alive --
  the Healer's finding traversed TASK_CLAIMS.json, not a process table.
- **No change to `check_dispatch_fleet_health.py`'s STALE/ALIVE-STALLED
  classification, or to the ad hoc TASK_CLAIMS correlation the Healer
  performed by hand.** That correlation is not implemented as a reusable
  check anywhere in this codebase today -- the raising chip's own text shows
  it was a manual `grep`/read of TASK_CLAIMS.json during the Healer's
  investigation, not a scripted signal. Formalizing that correlation (e.g.
  "do not escalate to a decision chip purely from ALIVE-STALLED + no
  matching active claim while the lease is still within its validity
  window; only escalate once the lease has actually expired and eligible
  work is still sitting undispatched") looks like the more precisely-targeted
  fix for the *alerting noise* (5 of 6 occurrences were benign), but it
  belongs in `metaworker-repair/SKILL.md` or
  `check_dispatch_fleet_health.py`'s own escalation logic, is a bigger
  change than this chip's scope, and needs someone who owns that skill's
  Step 5 recurrence-to-`/metaworker-learning` handoff to weigh in -- flagged
  here as the natural next step, not built unilaterally by this
  investigation.

## Recommendation for follow-on

Per CLAUDE.md's Session Land Protocol chip discipline, this is genuine
follow-on work distinct from what this chip was asked to do (a design
decision about the *alerting* logic, not the lease/claim primitives), so it
is reported here rather than built: consider whether
`check_dispatch_fleet_health.py` (or `metaworker-repair/SKILL.md`'s Step 5)
should stop treating "valid lease, no matching active claim" as inherently
decision-chip-worthy while the lease has not yet expired, and instead only
escalate once `dispatcher_control.py check` would itself return STOP *and*
eligible work is still sitting undispatched -- the one state that actually
needs a human ("start a fresh Orchestrator"), as opposed to a state the
system is already handling correctly on its own.
