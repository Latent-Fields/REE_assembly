# REE Fleet -- Live Status

**Updated:** 2026-09-26T18:41:47Z &middot; refreshes every few minutes &middot; source: coordinator DB (live).

> This is the force-updated `live-status` branch -- a current snapshot, **not** part of `master` history. The branch is reset every tick so it never bloats the repo.

## Workers (7 total, 1 running)

| Machine | State | Experiment | Progress | ETA | Last seen |
|---|---|---|---|---|---|
| DLAPTOP | offline | -- | -- | -- | 26.5h ago |
| ree-cloud-1 | offline | -- | -- | -- | 652.1h ago |
| ree-cloud-2 | offline | -- | -- | -- | 6m ago |
| ree-cloud-3 | running | V3-EXQ-1105b | Seed 304 / full_arms - ep 11/11 - 12.5% | ~13.2h | 1s ago |
| ree-cloud-4 | offline | -- | -- | -- | 3.9h ago |
| ree-cloud-4-metaworker | dispatching (stale) | -- | -- | -- | 44.6h ago |
| ree-cloud-5 | dispatching (stale) | -- | -- | -- | 44.5h ago |

## Queue -- 0 pending, 1 claimed

| Queue ID | Status | Claimed by | Priority |
|---|---|---|---|
| V3-EXQ-1105b | claimed | ree-cloud-3 | 40 |

## Daemon code freshness -- 2 STALE

| Daemon | Status | Repo (graded) | Started | Last source commit |
|---|---|---|---|---|
| ree-coordinator | CURRENT | ~/REE_Working/ree-v3 | 2026-09-26T11:25:20Z | 436a988742 2026-09-26T11:22:03Z |
| ree-explorer | DRIFT | ~/REE_Working/REE_assembly | 2026-09-23T16:29:18Z | c28fc5768f 2026-09-26T16:46:45Z |
| ree-runner | INACTIVE | ~/REE_Working_runner/ree-v3 | -- | -- |
| ree-sync-daemon | DRIFT | ~/REE_Working/ree-v3 | 2026-09-18T12:34:47Z | 436a988742 2026-09-26T11:22:03Z |

**A landed fix is not reaching a running process.** Python binds modules at import, so these daemons keep executing the code that existed when they started.

- `ree-sync-daemon` (~/REE_Working/ree-v3) -- started 2026-09-18T12:34:47Z, but 436a988742 (2026-09-26T11:22:03Z) touched its source 7.9d later -- process is running pre-commit bytecode
- `ree-explorer` (~/REE_Working/REE_assembly) -- started 2026-09-23T16:29:18Z, but c28fc5768f (2026-09-26T16:46:45Z) touched its source 3.0d later -- process is running pre-commit bytecode

Restart is a deliberate operator action with a pre-flight (clean trees + empty spool) -- see `ree-v3/coordinator/OPERATOR_GUIDE.md`, "Daemon code drift".

