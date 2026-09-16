# REE Fleet -- Live Status

**Updated:** 2026-09-16T02:28:44Z &middot; refreshes every few minutes &middot; source: coordinator DB (live).

> This is the force-updated `live-status` branch -- a current snapshot, **not** part of `master` history. The branch is reset every tick so it never bloats the repo.

## Workers (8 total, 2 running)

| Machine | State | Experiment | Progress | ETA | Last seen |
|---|---|---|---|---|---|
| DLAPTOP | idle | -- | -- | -- | 55s ago |
| DLAPTOP-4.local | running | V3-EXQ-906c | Seed 0 / full_stack_observational_showcase - ep 30/220 - 13.6% | ~3.0h | 894.7h ago |
| ree-cloud-1 | offline | -- | -- | -- | 395.9h ago |
| ree-cloud-2 | offline | -- | -- | -- | 4.2h ago |
| ree-cloud-3 | running | V3-EXQ-935a | Seed 51 / CURRICULUM_BUILT_NORMALISED_CAP_RULE_935A_FRESH_SEEDS - ep 30/340 - 81.8% | ~10.4h | 2s ago |
| ree-cloud-4 | offline | -- | -- | -- | 25.9h ago |
| ree-cloud-4-metaworker | runner | -- | -- | -- | 32.2h ago |
| ree-cloud-5 | dispatching | -- | -- | -- | 32.1h ago |

## Queue -- 0 pending, 1 claimed

| Queue ID | Status | Claimed by | Priority |
|---|---|---|---|
| V3-EXQ-935a | claimed | ree-cloud-3 | 55 |

## Daemon code freshness -- 3 STALE

| Daemon | Status | Repo (graded) | Started | Last source commit |
|---|---|---|---|---|
| ree-coordinator | DRIFT | ~/REE_Working/ree-v3 | 2026-09-09T18:00:34Z | 61d8e24ce2 2026-09-15T01:54:56Z |
| ree-explorer | DRIFT | ~/REE_Working/REE_assembly | 2026-09-11T03:36:11Z | 05962ac103 2026-09-14T23:36:43Z |
| ree-runner | INACTIVE | ~/REE_Working_runner/ree-v3 | -- | -- |
| ree-sync-daemon | DRIFT | ~/REE_Working/ree-v3 | 2026-09-09T18:00:34Z | 61d8e24ce2 2026-09-15T01:54:56Z |

**A landed fix is not reaching a running process.** Python binds modules at import, so these daemons keep executing the code that existed when they started.

- `ree-sync-daemon` (~/REE_Working/ree-v3) -- started 2026-09-09T18:00:34Z, but 61d8e24ce2 (2026-09-15T01:54:56Z) touched its source 5.3d later -- process is running pre-commit bytecode
- `ree-coordinator` (~/REE_Working/ree-v3) -- started 2026-09-09T18:00:34Z, but 61d8e24ce2 (2026-09-15T01:54:56Z) touched its source 5.3d later -- process is running pre-commit bytecode
- `ree-explorer` (~/REE_Working/REE_assembly) -- started 2026-09-11T03:36:11Z, but 05962ac103 (2026-09-14T23:36:43Z) touched its source 3.8d later -- process is running pre-commit bytecode

Restart is a deliberate operator action with a pre-flight (clean trees + empty spool) -- see `ree-v3/coordinator/OPERATOR_GUIDE.md`, "Daemon code drift".

