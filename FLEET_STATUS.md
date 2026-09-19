# REE Fleet -- Live Status

**Updated:** 2026-09-19T19:15:45Z &middot; refreshes every few minutes &middot; source: coordinator DB (live).

> This is the force-updated `live-status` branch -- a current snapshot, **not** part of `master` history. The branch is reset every tick so it never bloats the repo.

## Workers (8 total, 1 running)

| Machine | State | Experiment | Progress | ETA | Last seen |
|---|---|---|---|---|---|
| DLAPTOP | idle | -- | -- | -- | 7s ago |
| DLAPTOP-4.local | running | V3-EXQ-906c | Seed 0 / full_stack_observational_showcase - ep 30/220 - 13.6% | ~3.0h | 983.4h ago |
| ree-cloud-1 | offline | -- | -- | -- | 484.7h ago |
| ree-cloud-2 | offline | -- | -- | -- | 4.8h ago |
| ree-cloud-3 | idle | -- | -- | -- | 8.7h ago |
| ree-cloud-4 | offline | -- | -- | -- | 8.9h ago |
| ree-cloud-4-metaworker | dispatching | -- | -- | -- | 12.1h ago |
| ree-cloud-5 | dispatching | -- | -- | -- | 12.1h ago |

## Queue -- 0 pending, 0 claimed

_(queue empty)_

## Daemon code freshness -- 2 STALE

| Daemon | Status | Repo (graded) | Started | Last source commit |
|---|---|---|---|---|
| ree-coordinator | DRIFT | ~/REE_Working/ree-v3 | 2026-09-18T18:52:04Z | 0ddac64fad 2026-09-19T10:25:21Z |
| ree-explorer | CURRENT | ~/REE_Working/REE_assembly | 2026-09-16T18:05:33Z | 05962ac103 2026-09-14T23:36:43Z |
| ree-runner | INACTIVE | ~/REE_Working_runner/ree-v3 | -- | -- |
| ree-sync-daemon | DRIFT | ~/REE_Working/ree-v3 | 2026-09-18T12:34:47Z | 0ddac64fad 2026-09-19T10:25:21Z |

**A landed fix is not reaching a running process.** Python binds modules at import, so these daemons keep executing the code that existed when they started.

- `ree-sync-daemon` (~/REE_Working/ree-v3) -- started 2026-09-18T12:34:47Z, but 0ddac64fad (2026-09-19T10:25:21Z) touched its source 21.8h later -- process is running pre-commit bytecode
- `ree-coordinator` (~/REE_Working/ree-v3) -- started 2026-09-18T18:52:04Z, but 0ddac64fad (2026-09-19T10:25:21Z) touched its source 15.6h later -- process is running pre-commit bytecode

Restart is a deliberate operator action with a pre-flight (clean trees + empty spool) -- see `ree-v3/coordinator/OPERATOR_GUIDE.md`, "Daemon code drift".

