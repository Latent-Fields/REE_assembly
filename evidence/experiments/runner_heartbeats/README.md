# runner_heartbeats/

Per-machine runner heartbeat snapshots. One file per hostname:
`<hostname>.json`.

Written by `experiment_runner.py` each loop tick when started with
`--remote-control`. Read by `serve.py`'s `read_machines()` aggregator (used
by `/api/machines` and the `/machines` dashboard).

A machine is considered "fresh" when its `last_tick_utc` is within 180
seconds of now (3x the default 60s `--loop-interval`). Stale heartbeats
are kept on disk so you can see when a machine last checked in; they're
just rendered with a different colour in the dashboard.

Schema (role: "runner", the default -- omitting `role` entirely is read as
"runner" for backward compatibility with every heartbeat written before this
field existed):
```
{
  "schema_version": "v1",
  "role": "runner",
  "machine": "DLAPTOP-4.local",
  "hostname": "Mac",
  "last_tick_utc": "2026-04-26T19:33:00Z",
  "state": "starting | idle | paused | draining",
  "current_exq": null | "V3-EXQ-490",
  "current_exq_started_utc": null | iso,
  "queue_depth": 12,
  "queue_id_at_head": "V3-EXQ-490",
  "recent_completed": [{queue_id, result, completed_at}, ...],
  "runner_pid": 82342,
  "runner_version": null,
  "gpu": {available: bool, device_name?, total_memory_gb?, device_index?}
}
```

Schema (role: "orchestrator" -- a `/loop metaworker-dispatch` box; see the
cloud-metaworker plan's Phase H. Written by `scripts/ree_metaworker_heartbeat.py`,
not by `experiment_runner.py`. Carries no experiment fields at all -- a
metaworker box runs no experiments, it dispatches chip-ledger work to bounded
`claude -p` child sessions):
```
{
  "schema_version": "v1",
  "role": "orchestrator",
  "machine": "ree-cloud-5",
  "hostname": "ree-cloud-5",
  "last_tick_utc": "2026-08-02T20:55:00Z",
  "state": "starting | idle | dispatching | paused | throttled | locked-out | timed-out | runner | draining-to-runner | yielding-to-experiment",
  "health": "dispatching | idle | not-dispatching | holding | stalled | dead-on-arrival | unknown",
  "health_reason": "dispatched 1 chip(s) this cycle",
  "no_dispatch_streak": 0,
  "session_outcome": "ok | usage-limit | died-on-arrival | error-exit | unknown",
  "cycles_completed": 143,
  "chips_dispatched_total": 7,
  "chips_open_work": 1,
  "chips_open_decision": 2,
  "eligible_work": 1,
  "dispatched_this_cycle": 1,
  "in_flight_dispatches": 1,
  "last_dispatch_chip_ref": null | "chip-proposal-exp-0400",
  "coordination_plane_paused": false,
  "last_cycle_note": null | "dispatched chip-proposal-exp-0400"
}
```

**`state` is what the wrapper DECIDED; `health` is what came of it. Read
`health`.** `state` is written by the systemd-timer wrapper around the
`claude -p` invocation, so it attests only that the timer fired. Confirmed
2026-08-19: ree-cloud-5 published `state: "dispatching"` with a timestamp fresh
to the minute for ~12 hours while every cycle died within seconds on
`You've hit your weekly limit`; the disproving fields (`chips_dispatched_total`
frozen, `last_dispatch_chip_ref` null, `in_flight_dispatches` 0 against
`chips_open_work` 61) were all present in the same file and unread. `health` is
that verdict, derived in `scripts/ree_metaworker_heartbeat.py` from observations
of WORK.

| `health` | meaning | alarming? |
|---|---|---|
| `dispatching` | dispatched this cycle, or has live workers, or a sibling cycle holds the per-box lock | no |
| `idle` | nothing eligible to dispatch (`eligible_work == 0`) | **no** -- a box with nothing it is allowed to take is fine |
| `not-dispatching` | eligible work, none dispatched, below the stall threshold | not yet -- watch `no_dispatch_streak` |
| `holding` | dispatch deliberately withheld: plane paused, resource throttle, or the experiment runner owns the box | no |
| `stalled` | eligible work and no dispatch for `no_dispatch_streak` >= 12 consecutive cycles (1h) | **yes** |
| `dead-on-arrival` | this cycle's own `claude -p` died without acting (usage limit, or no output at all) | **yes** |
| `unknown` | health could not be determined -- e.g. an older wrapper supplying no work observations | **yes, weakly** -- it is never a green light |

`unknown` is the fail-safe default everywhere. The failure this replaced was a
confident false green, so no path that cannot determine health may report a
healthy value.

`eligible_work` counts open, **unclaimed** `kind: "work"` chips -- deliberately
narrower than `chips_open_work`, which includes chips another dispatcher is
already running. It can only understate a stall, never invent one.
`read_machines()` (serve.py) passes `role` and the orchestrator fields through
unchanged for any entry that carries them; the `/machines` dashboard renders a
role=="orchestrator" card with a distinct template (cycle/dispatch counts, no
GPU/queue-depth/current-exq fields) instead of forcing it through the runner
card. Freshness/staleness (`fresh`, `age_seconds`, `STALE_EXCLUDE_SECONDS`) is
role-agnostic -- both roles are keyed off the same `last_tick_utc`.

See also: `runner_status/` (per-machine experiment status, written every
~5s during a run) and `runner_commands/` (per-machine command queues for
remote control) -- both runner-only; an orchestrator box has neither.
