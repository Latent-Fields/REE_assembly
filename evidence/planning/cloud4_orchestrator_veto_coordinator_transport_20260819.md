# ree-cloud-4 orchestrator veto: git heartbeat -> coordinator, and the power-on bootstrap deadlock

**Date:** 2026-08-19
**Chip:** `chip-20260819-cloud4-orchestrator-veto-bootstrap-deadlock`
**Status: LANDED.** ree-v3 `c7f2355f8c`, REE_Working `2292c68188` + `432ced3f`.
Deployed to the hub (`ree-worker-1`) and to `ree-worker-4`; verified live.

---

## 1. The defect, one level up from the reported symptom

The reported symptom was a bootstrap deadlock: `cloud-scaler.py`'s orchestrator
shutdown-veto fails open on a stale heartbeat, an OFF box has no fresh
heartbeat, so a box powered on by hand was shut down again within one 5-minute
tick and could never survive long enough to publish the signal that would have
kept it alive.

The **root defect** is a transport choice, and it was user-identified: an
**operational** decision -- power a billable box off, killing live `claude -p`
workers -- was being made from a channel this codebase had already demoted for
operations.

Verified in `coordinator/deploy/cloud-scaler.py` as it stood at `3b6df21`:

| signal | transport | freshness |
|---|---|---|
| runner liveness/state/current_exq | `COORDINATOR_URL/shadow/status` (`fetch_coordinator_status`), git mirror only as fallback | sub-second, DB-authoritative |
| **orchestrator veto** (`read_orchestrator`, added 2026-08-18) | **git file only** -- `runner_heartbeats/<affinity>-metaworker.json` | commit + push + hub pull |

Both appear in the SAME log line: `hb_src=coord ... orch=none`.

CLAUDE.md states the git transport is deliberately stale by design -- the
phase3 heartbeat writer commits on **state-changes only** (the 30-minute forced
liveness tick was retired to stop `REE_assembly` history bloat) -- and warns in
terms: *"DO NOT read intra-run progress from `runner_heartbeats/*.json` on
`origin/master` and assume it is current."* `ORCHESTRATOR_FRESH_MIN` had to be
**50 minutes** purely to absorb that lag (30 liveness floor + ~13 observed
checkout lag + ~7 margin). `ree_metaworker_heartbeat.py` gates its own commit
the same way via `should_commit()`.

## 2. Measurements (hub journal + coordinator DB, not inferred)

* `ree-cloud-4-metaworker.json` `last_tick_utc = 2026-08-19T01:32:44Z`;
  box off since ~01:39Z; `in_flight_dispatches: 2`, `chips_open_work: 80`
  frozen in the file.
* `16:45:04Z [ree-worker-4 affinity=ree-cloud-4] claimable=0 held_by_self=0`
  `status=running idle_ok=1 reason=clean_idle hb_src=coord lease=none orch=none`
  `-> no matching work AND runner idle past grace window, shutting down`
  `ree-worker-4`, then `16:45:05 Sent shutdown signal to server 131490371`.
* The operator's `hcloud server poweron` was in that same minute. **The box was
  shut down one second after the tick observed it, while it was still booting.**
  Zero chips claimed between power-on and power-off.

### 2a. The measurement that settles "band-aid vs structural"

The 16:45:04Z kill happened **before the box could speak on any channel**. No
box-side transport, however fast, publishes during its own boot. So moving the
veto to the coordinator -- necessary, and the user's instruction -- **does not
on its own** break the deadlock. Something must cover the interval in which the
box is physically unable to answer. That is why the wake hold below is
structural rather than cosmetic, and it is bounded so it cannot become a
billing hazard.

### 2b. Two options investigated and rejected on evidence

* **Hub reads the chip ledger directly.** `chips_open_work` is a property of
  the shared ledger, not of the box, so the hub could compute it with no box
  telemetry and no staleness. **Rejected: the hub has no umbrella checkout.**
  `/home/ree/REE_Working/TASK_CHIPS.json` does not exist there; the directory
  holds only `REE_assembly/` and `ree-v3/`. Adding one is a new dependency and
  a new git-writer surface on the box that must never wedge.
* **Hub SSH-probes the worker for `systemctl is-active`.** The chip's
  correction offered SSH as a sanctioned operational channel. **Rejected: the
  hub cannot SSH to the workers.** `~/.ssh` on `ree-worker-1` holds
  `authorized_keys` and `known_hosts` and **no private key**, and the WireGuard
  allowed-ips are `10.8.0.11-.20` (no route to `10.8.0.5`). The working
  direction is worker -> hub, which is exactly how the dispatch wrapper writes
  its lease. Anything wanting a hub->worker probe needs key provisioning first.

## 3. What was built

**(a) Transport -- the primary fix.** `read_orchestrator()` is now
COORDINATOR-PRIMARY: it reads the `<affinity>-metaworker` row from
`/shadow/status`, with the git file unchanged as the unreachable-coordinator
fallback -- the same shape `fetch_coordinator_status`/`evaluate_heartbeat`
established for runner telemetry on 2026-06-23. `judge_orchestrator()` is a
SINGLE decision function applied to whichever transport supplied the tick, so
the two cannot drift in what they conclude. Windows differ deliberately:
`ORCHESTRATOR_COORD_FRESH_MIN = 12` vs `ORCHESTRATOR_FRESH_MIN = 50`. That
tightening is the payoff -- a dead metaworker now stops vetoing in ~12 minutes
instead of ~50.

`ree_metaworker_heartbeat.py` POSTs `/heartbeat` as `<affinity>-metaworker`
every tick, best-effort and never fatal, with the demand fields in `progress`.
**Unconditional** -- including the ticks `should_commit()` correctly declines,
which is exactly when the git file goes stale on a box that is still alive.

**Deliberately no `payload` key.** The coordinator stores a POSTed `payload` in
`heartbeats.heartbeat_payload_json`, and `sync_daemon.phase3_heartbeat_writer`
materialises `runner_heartbeats/<machine>.json` from **every** row where that
column is non-NULL. Sending it would hand this heartbeat file a SECOND git
writer, on a different cadence, racing `ree_metaworker_heartbeat.py`. Verified
after deployment: the `ree-cloud-4-metaworker` row has
`heartbeat_payload_json IS NULL`.

**(b) Bootstrap -- `orchestrator_wake_hold()`.** For an affinity in
`ORCHESTRATOR_AFFINITIES` only, and only while `status == "running"`, the
scaler holds the box for `ORCHESTRATOR_WAKE_GRACE_MIN` (12) minutes after it
first observes the box running following an off/unknown observation. State is
one small hub-local JSON per affinity in `/home/ree/scaler_state/`, same shape
and same reasoning as `PYTEST_LEASE_DIR`. A lost state file reads as "first
sight running", which starts the window NOW and therefore self-expires; an
unwritable state dir yields NO hold rather than an unbounded one.

**(c) `ORCHESTRATOR_AFFINITIES` is CONFIG, not telemetry.** Which boxes are
resident dispatchers is a standing fact. Inferring it from "an orchestrator
heartbeat exists" *is* the deadlock: an OFF box publishes nothing, so it reads
as "not an orchestrator" and is powered off before it can ever publish.

**(d) GHA backstop holds no shutdown authority over a declared orchestrator
box.** A GitHub-hosted runner cannot reach the WireGuard-only coordinator or
the hub-local wake state, so it can only read the stale channel -- the one that
powered `ree-cloud-4` off at `2026-08-19T01:39:26Z` with 2 dispatches in flight
and 80 open chips, undetected for ~15h. **Power-ON authority is retained.** The
hub timer (~5 min, coordinator-connected) remains fully authoritative,
including for shutting the box down when both planes are genuinely empty.

**(e) `ree-metaworker.timer` `OnBootSec` 5min -> 20s**, so the first coordinator
POST lands well inside the wake window rather than at its far edge.

### Safety properties preserved (explicitly, none weakened)

* **Fail-open on stale is UNCHANGED.** Every defect path -- missing row, no
  progress blob, role mismatch, no timestamp, stale, missing/non-integer demand
  fields, unreadable git file, no coordinator at all -- still returns *no veto*.
* **Freshness alone is still not a veto.** `in_flight > 0` (strong) or
  `chips_open_work > 0` (weak); idle-and-empty falls through to the ordinary
  shutdown test, which independently requires `claimable == 0`. The box is
  therefore stopped only when BOTH planes are empty -- so it is usually on *as a
  consequence of there being work*, not always-on by fiat.
* **The wake hold is a MAX AGE**, like `PYTEST_LEASE_MAX_MIN` and
  `ORCHESTRATOR_FRESH_MIN`. A box whose metaworker never comes up is shut down
  when it expires.
* **The git heartbeat keeps being written**, by the same writer as before. It
  remains the scaler's fallback and `serve.py`'s `/machines` card source, and
  the `<affinity>-metaworker` identity split is untouched.

## 4. Live verification

```
17:47:05Z [ree-worker-4] status=running ... orch=none orch_src=git wake=hold
          -> ree-cloud-4 is a declared orchestrator box that has just come up,
             holding ree-worker-4 (orchestrator_wake_hold up=0min<=12min ...)
```
That is the identical tick shape that killed the box at 16:45:04Z.

```
17:52:14Z  worker-4 dispatch log: coordinator: ok
             (ree-cloud-4-metaworker -> http://10.8.0.1:8787)
17:54:15Z  [ree-worker-4] ... lease=held orch=active orch_src=coord wake=hold
```
`/shadow/status` carries the row with `role: orchestrator`,
`chips_open_work: 69`, `lifecycle_state: live`.

## 5. Incidental findings on `ree-worker-4` (NOT fixed here)

1. **No `/etc/ree-coordinator.env`.** That file is a HUB convention; the
   workers carry `COORDINATOR_URL`/`COORDINATOR_TOKEN` as systemd
   `Environment=` lines in a `ree-runner.service.d` drop-in. A resolver reading
   only EnvironmentFile syntax would have been present, green and **inert** on
   the one box this change exists for. `discover_coordinator_config()` now
   handles both formats and both shapes.
2. **The box was 522 commits behind on `REE_Working`** and its `--ff-only`
   autosync was blocked by two dirty files. Fixed by hand (see 3 below). The
   wrapper's own header records this class of failure as endemic on this box
   (1299 FAILED vs 853 ok to 2026-08-16).
3. **Two files held unique uncommitted content** -- `scripts/chip_ledger.py`
   and `scripts/task_claim.py`, matching **no commit in any ref**. They were
   preserved two ways before the pull, not dropped:
   * `git stash@{0}` on that box, message `cloud4 pre-pull preserve
     20260819T1750Z chip-20260819-cloud4-orchestrator-veto-bootstrap-deadlock`
   * a file copy at `/home/ree/_preserve_20260819T1750Z_chip20260819cloud4/`
     with `blob_hashes.txt`
     (`147e46e7fb0569410da127f1acaf98e3c7507c12`,
      `dbd181bf5e3929432e73f6d81bdaea1061a023d5`).
   **`scripts/audit_stashes.py` does NOT cover cloud boxes**, so this stash is
   invisible to every session-startup audit. It needs a human decision.
4. **The live dispatch wrapper was behind its tracked reference copy** and was
   re-synced from `coordinator/deploy/ree-metaworker-dispatch.sh`.

## 6. Tests

* `ree-v3/coordinator/test_cloud_scaler_orchestrator_transport.py` -- 30, time-
  independent; **29 verified to FAIL against the pre-change script** (the one
  that passes is an unchanged-invariant control).
* `ree-v3/coordinator/test_cloud_scaler_transport_parity.py` -- +6 (affinity
  parity, exclusion branch ordering, power-on authority retained), 36 total.
* `REE_Working/scripts/test_ree_metaworker_heartbeat_coordinator.py` -- 27,
  driven against a REAL loopback HTTP server so the request is genuinely built,
  sent and parsed rather than pattern-matched.

Roughly half of each set are negative controls: every fail-open path, both
bounds, "never fatal", "never a `payload` key", and "must fire on the ticks
that are not committed".
