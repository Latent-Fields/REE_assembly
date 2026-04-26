# runner_commands/

Per-machine command queues for remote control of running runners.
One file per hostname: `<hostname>.json`.

Written by:
- `serve.py` `append_machine_command()` (POST `/api/machines/<host>/command`)
  when a button is clicked on the `/machines` dashboard.
- Anyone with push access to this repo can also append commands directly
  via git (the `/machines` UI is just a convenience).

Read and processed by `experiment_runner.py` each loop tick when started
with `--remote-control`. The runner marks `pending -> ack -> done|failed`,
writes the file back, and pushes it (when `--auto-sync` is on).

Supported command kinds:
- `stop`           &mdash; graceful drain after current experiment
- `force_stop`     &mdash; kill current experiment process and exit
- `pause`          &mdash; runner stays alive but skips picking up new work
- `resume`         &mdash; clear pause state
- `kick`           &mdash; `args.queue_id` moved to head of `experiment_queue.json`
- `release_claim`  &mdash; `args.queue_id` has its `claimed_by` cleared

`start` is **not** supported through this channel: a stopped runner cannot
read its own command file. Use serve.py's `/api/runner/v3/start` for the
local machine, SSH or a dedicated supervisor for remote machines.

Trust model: push access = command access. Same level of trust as for
adding experiments to `experiment_queue.json`.

Schema:
```
{
  "schema_version": "v1",
  "machine": "DLAPTOP-4.local",
  "commands": [
    {
      "id": "cmd-2026-04-26T19:30:00Z-abc123",
      "kind": "kick",
      "args": {"queue_id": "V3-EXQ-490"},
      "issued_at_utc": "2026-04-26T19:30:00Z",
      "issued_by": "explorer | smoke-test | etc",
      "status": "pending | ack | done | failed",
      "ack_at_utc": null | iso,
      "completed_at_utc": null | iso,
      "error": null | "explanatory string",
      "result_note": "human-readable summary"
    },
    ...
  ]
}
```

History is pruned to the last 50 done/failed entries per file to bound
file growth. Pending and ack commands are always retained.
