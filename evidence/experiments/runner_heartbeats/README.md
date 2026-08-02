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
  "state": "starting | idle | dispatching | paused",
  "cycles_completed": 143,
  "chips_dispatched_total": 7,
  "chips_open_work": 1,
  "chips_open_decision": 2,
  "in_flight_dispatches": 1,
  "last_dispatch_chip_ref": null | "chip-proposal-exp-0400",
  "coordination_plane_paused": false,
  "last_cycle_note": null | "dispatched chip-proposal-exp-0400"
}
```
`read_machines()` (serve.py) passes `role` and the orchestrator fields through
unchanged for any entry that carries them; the `/machines` dashboard renders a
role=="orchestrator" card with a distinct template (cycle/dispatch counts, no
GPU/queue-depth/current-exq fields) instead of forcing it through the runner
card. Freshness/staleness (`fresh`, `age_seconds`, `STALE_EXCLUDE_SECONDS`) is
role-agnostic -- both roles are keyed off the same `last_tick_utc`.

See also: `runner_status/` (per-machine experiment status, written every
~5s during a run) and `runner_commands/` (per-machine command queues for
remote control) -- both runner-only; an orchestrator box has neither.
