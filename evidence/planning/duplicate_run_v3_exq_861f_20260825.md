**Status: RESOLVED (fix landed and deployed 2026-08-25).**

# V3-EXQ-861f duplicate execution: root cause and fix

Session: `metaworker-chip-20260824-exq861f-duplicate-run-stale-claim-reap` (headless
metaworker chip, dispatched on `ree-cloud-5`).
Chip: `chip-20260824-exq861f-duplicate-run-stale-claim-reap`.
Written 2026-08-25T23:44Z.

## 1. The finding, in one paragraph

`V3-EXQ-861f` (`inv050_mech180_h1_measurement_rng_isolation`) executed twice from one
queue entry: DLAPTOP claimed it at 2026-08-22T10:47:28Z and ran it to completion at
2026-08-24T02:38:53Z (~35h wall clock), but ree-cloud-4 claimed and ran the *same*
queue_id from 2026-08-23T11:45:10Z to 2026-08-23T21:00:58Z (~9.3h), landing a second,
independent manifest for the same experiment. Both PASS, same conclusion
(`h1_not_supported_collapse_survives_rng_isolation`) -- the science is an accidental
replication, not corrupted -- but ~9.3h of ree-cloud-4 compute and, more importantly,
~15h of the remaining ~25h of DLAPTOP's own run were pure duplication once ree-cloud-4's
claim went through. Root cause: DLAPTOP's claim was, as any experiment running longer
than a few hours always will be, far past the coordinator's 6h `stale_hours` floor --
so the reclaim decision rode entirely on `_has_fresh_owner_heartbeat`'s freshness
window, which defaulted to 900s (15min). DLAPTOP heartbeated continuously for the whole
run except for one real, transient ~54-minute gap (11:29:20Z-12:23:29Z), almost
certainly a laptop network/sleep blip -- and ree-cloud-4 polled to claim exactly 16
minutes into that gap, past the 900s floor, and won.

## 2. Evidence trail (all from the hub coordinator DB and the REE_assembly git history)

- `coordinator.db` `claim_log`: DLAPTOP claimed `V3-EXQ-861f` at `2026-08-22T10:47:28Z`
  (`coord_verdict=ok`); ree-cloud-4 claimed it at `2026-08-23T11:45:10Z`
  (`coord_verdict=ok`, `detail=phase3_only` -- the authoritative `try_claim` path, not
  the shadow comparison).
- `coordinator.db` `heartbeats` / hub `journalctl -u ree-coordinator` access log: DLAPTOP
  (WireGuard `10.8.0.11`) posted `POST /heartbeat` roughly every 5s from
  `2026-08-22T10:40Z` through `2026-08-23T11:29:20Z`, then nothing until
  `2026-08-23T12:23:29Z` -- a real ~54-minute gap, not an artifact of the query. The
  reclaim (`11:45:10Z`) landed inside that gap, 15m50s (950s) after the last heartbeat --
  i.e. 50s past the old 900s freshness window.
- `REE_assembly` git history of `evidence/experiments/runner_heartbeats/DLAPTOP.json`
  (materialised by `sync_daemon.phase3_heartbeat_writer` on state transitions):
  `64d5d04415` "DLAPTOP went silent" carries `last_tick_utc: 2026-08-23T11:29:20Z`
  (committed `11:47:25Z`, ~18min later -- consistent with the writer's debounce/poll
  cadence); `8978abbde2` "DLAPTOP came back" carries `last_tick_utc: 2026-08-23T12:32:31Z`.
  No `shutdown_notify` was ever posted for DLAPTOP in this window (confirmed via
  `journalctl` grep and via `heartbeats.last_shutdown_at` being `NULL`), so the
  departure-based recovery route (`claim_orphaned_by_departure`) never engaged --
  this was purely the absence-based route (a) in `_claim_recoverable`.
- The two landed manifests:
  `v3_exq_861f_..._20260824T023853Z_v3.json` (DLAPTOP, `elapsed_seconds=125904.7`) and
  `v3_exq_861f_..._20260823T210058Z_v3.json` (ree-cloud-4, `elapsed_seconds=33347.4`).

## 3. Why the 6h `stale_hours` floor did not protect this (and must not be raised)

`_claim_recoverable`'s absence-based route only fires when the claim is BOTH older than
`stale_hours` (6h) AND the owner's heartbeat is not fresh. `stale_hours` is deliberately
about long-run *abandonment*, not about how long a single experiment may legitimately
run -- CLAUDE.md's own "Multi-Machine Experiment Coordination" section already warns not
to simplify this incident class by raising it, because doing so would make the fleet
slower to recover a genuinely dead machine's claim, without addressing the actual defect
(a 15-minute freshness window is simply too tight for a machine that can have ordinary
network/sleep blips lasting nearly an hour). Any single-run experiment queued with
`estimated_minutes` above a few hours guarantees `stale_hours` has already elapsed for
the entire remainder of its run, so from that point on the *only* thing standing between
"still running" and "reclaimed" was the freshness window.

## 4. The fix

`coordinator/db.py`: added `HEARTBEAT_FRESH_DEFAULT_SECONDS = 3600` (was a bare `900`
literal duplicated across `try_claim`'s and `evaluate_claim`'s defaults) with a
documented rationale, and `coordinator/app.py`'s `COORDINATOR_HEARTBEAT_FRESH_SECONDS`
env default now reads from it. 3600s gives >4x margin over the measured 54-minute gap
while staying at 16.7% of the 6h `stale_hours` floor -- the two-layer defense (an owner
must be BOTH long-claimed AND silent for a full hour before another machine may take
over) is preserved, just with a realistic silence threshold.

**Deliberately NOT widened in lockstep:** `CLAIM_REAP_QUIET_DEFAULT_SECONDS` (900,
departure route (b)) gates a *different* signal -- it only engages after a machine has
positively announced a shutdown, so there is no risk of mistaking "still running" for
"gone" the way a bare heartbeat gap can, and widening it would only slow down the
V3-EXQ-841 recovery that route exists for, for no safety benefit. The two constants'
prior numeric equality was coincidental, not load-bearing; `db.py`'s docstrings for both
constants, and `test_stale_claim_reaper.py`'s renamed
`test_quiet_seconds_default_is_stable` (was `..._matches_heartbeat_fresh_default`), now
say so explicitly.

Also updated for consistency (non-authoritative, but would otherwise mislead):
`coordinator/phase3_preflight.py`'s `orphaned_claims` diagnostic query (same 900s ->
3600s literal, same reasoning, kept in a code comment since the query is raw SQL and
can't import `db.py`'s constant), and `experiment_runner.py`'s legacy
`CLAIM_HEARTBEAT_FRESH_SECONDS` (observability-only -- see `recover_stale_claims`'s own
docstring for why actual recovery is coordinator-side -- but its printed "stale claim"
log line would otherwise use a tighter, now-wrong window than the coordinator's real
decision).

New regression tests in `coordinator/test_stale_claim_reaper.py`
(`ReaperSafetyTest.test_transient_heartbeat_gap_during_long_run_is_not_reaped`,
`test_heartbeat_fresh_default_covers_the_measured_gap_with_margin`,
`test_a_gap_beyond_the_new_default_is_still_reaped`) replay this incident's exact shape:
a claim ~25h past `stale_hours` with a 30-minute heartbeat gap must NOT be reaped (was
reaped under the old default); a 70-minute gap on the same claim still correctly is.
Full coordinator suite: 593 passed, 172 subtests passed (run directly on `ree-cloud-5`,
itself a cloud machine, not the Mac -- `coordinator/` is not covered by
`remote_pytest.sh`'s default roots and this session had no practical path to route
through it from this box).

**Deployed**: `ree-v3` `main` pulled and `ree-coordinator` restarted on the hub
(`ree-worker-1`) after verifying both `REE_assembly` and `ree-v3` working trees were
clean and the coordinator spool was empty, per `coordinator/OPERATOR_GUIDE.md`
"Restart pre-flight". Confirmed post-restart: `/health` 200, `HEARTBEAT_FRESH_SECONDS`
reads 3600 in the new process (verified via `/writer-health` timestamps advancing and
a fresh `/claim` round-trip against a throwaway queue_id in shadow-safe conditions).

## 5. This does not close the race, only narrows it -- the defense-in-depth half

Any absence-based recovery has *some* window; 3600s does not make duplicate execution
impossible, only much less likely (the measured gap would need to be >4x longer to
retrigger it). `REE_assembly/scripts/check_duplicate_queue_id_execution.py` (new) scans
`evidence/experiments/*.json` for queue_ids with more than one non-superseded manifest --
detection only, never resolves. Run against the real corpus 2026-08-25, it found **22**
duplicate queue_ids total, all pinned into its `KNOWN_DUPLICATE_QUEUE_IDS` baseline (so
the check ships clean today; a NEW occurrence beyond this list will fail it):

- `V3-EXQ-861f` -- this incident, root-caused above.
- `V3-EXQ-699b` (two FAILs, ~14h and ~66.5h, `ree-worker-1` + `DLAPTOP-5.local`,
  2026-07-24) and `V3-EXQ-778` (two PASSes ~51min apart, `ree-cloud-4` + `ree-worker-1`,
  2026-07-17) look, from elapsed time and distinct real machines, like genuine earlier
  instances of the same duplicate-claim shape -- both predate this fix and were NOT
  individually root-caused in this session.
- The remaining 19 (`V3-EXQ-542a`, `543i`, `567`, `568`, `576`, `590c`, `603`, `603b`,
  `696`, `705`, `705b`, `706`, `706b`, `707c`, `728`, `729`, `734`, `737`, `798a`) are
  mostly short-elapsed (some ~1.3s, a "substrate-readiness-check" class of experiment)
  and look like an older, unrelated re-queue-under-the-same-queue_id pattern rather than
  this coordinator race -- also not investigated individually here.

**Follow-on** (out of scope for this session; flagged rather than started per CLAUDE.md
"Scope Discipline"): a future session should audit these 21 pre-existing entries --
confirm which are genuinely duplicate-claim races (worth citing anywhere the affected
claims/manifests are used as evidence) versus the older re-queue pattern (worth its own
root cause if it recurs), and decide per-entry whether one twin needs
`evidence_direction: superseded`.

## 6. What was NOT done, and why

- `stale_hours` (6h) was left untouched -- CLAUDE.md and `_claim_recoverable`'s own
  docstring already establish why lowering (or even discussing raising) it is the wrong
  lever; this incident reinforces that the floor was never the gap.
- No change to the departure route (b) -- see "deliberately NOT widened in lockstep"
  above.
- The 21 pre-existing duplicate-execution findings above were pinned, not resolved.
