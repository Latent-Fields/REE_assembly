# REE Fleet -- Live Status

**Updated:** 2026-09-07T04:20:19Z &middot; refreshes every few minutes &middot; source: coordinator DB (live).

> This is the force-updated `live-status` branch -- a current snapshot, **not** part of `master` history. The branch is reset every tick so it never bloats the repo.

## Workers (8 total, 2 running)

| Machine | State | Experiment | Progress | ETA | Last seen |
|---|---|---|---|---|---|
| DLAPTOP | offline | -- | -- | -- | 158.9h ago |
| DLAPTOP-4.local | running | V3-EXQ-906c | Seed 0 / full_stack_observational_showcase - ep 30/220 - 13.6% | ~3.0h | 680.5h ago |
| ree-cloud-1 | offline | -- | -- | -- | 181.7h ago |
| ree-cloud-2 | running | V3-EXQ-1007 | Seed 43 / D3_hazard_free - ep 100/1350 - 40.2% | ~1m | 0s ago |
| ree-cloud-3 | offline | -- | -- | -- | 2.1h ago |
| ree-cloud-4 | offline | -- | -- | -- | 10.2h ago |
| ree-cloud-4-metaworker | runner | -- | -- | -- | 100.7h ago |
| ree-cloud-5 | dispatching | -- | -- | -- | 100.6h ago |

## Queue -- 0 pending, 1 claimed

| Queue ID | Status | Claimed by | Priority |
|---|---|---|---|
| V3-EXQ-1007 | claimed | ree-cloud-2 | 80 |

## Daemon code freshness -- 3 STALE

| Daemon | Status | Repo (graded) | Started | Last source commit |
|---|---|---|---|---|
| ree-coordinator | DRIFT | ~/REE_Working/ree-v3 | 2026-09-02T21:47:41Z | fccf81ca27 2026-09-06T21:58:23Z |
| ree-explorer | DRIFT | ~/REE_Working/REE_assembly | 2026-09-03T20:05:00Z | 5db1841520 2026-09-06T22:01:33Z |
| ree-runner | INACTIVE | ~/REE_Working_runner/ree-v3 | -- | -- |
| ree-sync-daemon | DRIFT | ~/REE_Working/ree-v3 | 2026-09-02T21:47:41Z | fccf81ca27 2026-09-06T21:58:23Z |

**A landed fix is not reaching a running process.** Python binds modules at import, so these daemons keep executing the code that existed when they started.

- `ree-sync-daemon` (~/REE_Working/ree-v3) -- started 2026-09-02T21:47:41Z, but fccf81ca27 (2026-09-06T21:58:23Z) touched its source 4.0d later -- process is running pre-commit bytecode
- `ree-coordinator` (~/REE_Working/ree-v3) -- started 2026-09-02T21:47:41Z, but fccf81ca27 (2026-09-06T21:58:23Z) touched its source 4.0d later -- process is running pre-commit bytecode
- `ree-explorer` (~/REE_Working/REE_assembly) -- started 2026-09-03T20:05:00Z, but 5db1841520 (2026-09-06T22:01:33Z) touched its source 3.1d later -- process is running pre-commit bytecode

Restart is a deliberate operator action with a pre-flight (clean trees + empty spool) -- see `ree-v3/coordinator/OPERATOR_GUIDE.md`, "Daemon code drift".

