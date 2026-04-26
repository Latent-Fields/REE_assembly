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

Schema:
```
{
  "schema_version": "v1",
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

See also: `runner_status/` (per-machine experiment status, written every
~5s during a run) and `runner_commands/` (per-machine command queues for
remote control).
