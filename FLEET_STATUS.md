# REE Fleet -- Live Status

**Updated:** 2026-09-13T09:07:16Z &middot; refreshes every few minutes &middot; source: coordinator DB (live).

> This is the force-updated `live-status` branch -- a current snapshot, **not** part of `master` history. The branch is reset every tick so it never bloats the repo.

## Workers (8 total, 1 running)

| Machine | State | Experiment | Progress | ETA | Last seen |
|---|---|---|---|---|---|
| DLAPTOP | offline | -- | -- | -- | 40.3h ago |
| DLAPTOP-4.local | running | V3-EXQ-906c | Seed 0 / full_stack_observational_showcase - ep 30/220 - 13.6% | ~3.0h | 829.3h ago |
| ree-cloud-1 | offline | -- | -- | -- | 330.5h ago |
| ree-cloud-2 | offline | -- | -- | -- | 27.9h ago |
| ree-cloud-3 | idle | -- | -- | -- | 38.8h ago |
| ree-cloud-4 | offline | -- | -- | -- | 57.2h ago |
| ree-cloud-4-metaworker | dispatching | -- | -- | -- | 60.8h ago |
| ree-cloud-5 | dispatching | -- | -- | -- | 60.7h ago |

## Queue -- 0 pending, 0 claimed

_(queue empty)_

## Daemon code freshness -- all current

| Daemon | Status | Repo (graded) | Started | Last source commit |
|---|---|---|---|---|
| ree-coordinator | CURRENT | ~/REE_Working/ree-v3 | 2026-09-09T18:00:34Z | 63aa9f2cf0 2026-09-09T17:55:14Z |
| ree-explorer | CURRENT | ~/REE_Working/REE_assembly | 2026-09-11T03:36:11Z | e8ac729495 2026-09-09T20:24:23Z |
| ree-runner | INACTIVE | ~/REE_Working_runner/ree-v3 | -- | -- |
| ree-sync-daemon | CURRENT | ~/REE_Working/ree-v3 | 2026-09-09T18:00:34Z | 63aa9f2cf0 2026-09-09T17:55:14Z |

