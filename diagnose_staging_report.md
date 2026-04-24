# Diagnose-Errors Staging Report

**Session**: ree-diagnose-queue-2026-04-23T14 / afternoon automated run
**Generated**: 2026-04-23T14:19:02Z
**Mode**: STAGING (headless, scheduled task)

---

## Summary (2026-04-23 afternoon)

**0 unaddressed errors requiring new fix scripts.**

All ERROR entries in runner_status.json (62 total) were cross-referenced against
the current queue, completed IDs, and TASK_CLAIMS.json. No new errors since the
last diagnose run on 2026-04-20. Queue is currently empty (0 items).

### Gap reconciliation

Monolithic runner_status.json is in sync with per-machine files. Gap: 0.

### Error chain analysis

| Queue ID | Status | Notes |
|---|---|---|
| V3-EXQ-008 | Architecturally obsolete | SD-003 superseded 2026-04-18; r2/r3 successors ran at time of error |
| V3-ONBOARD-smoke-EWIN-PC | Infrastructure test | Not a scientific experiment; no fix needed |
| V3-ONBOARD-smoke-ree-cloud-1 | Infrastructure test | Not a scientific experiment; no fix needed |
| All other ERRORs | Addressed | Each has completed successor in runner_status |

### New errors since 2026-04-20

None.

---

## Pending experiment reviews (for user reference)

10 items in pending_review.md (all UNKNOWN due to stale index):

| Queue ID | Result | Notes |
|---|---|---|
| V3-EXQ-456 | UNKNOWN | Index stale — run build_experiment_indexes.py |
| V3-EXQ-460 | UNKNOWN | Index stale |
| V3-EXQ-462 | UNKNOWN | Index stale |
| V3-EXQ-463 | UNKNOWN | Index stale |
| V3-EXQ-464 | UNKNOWN | Index stale |
| V3-EXQ-465 | UNKNOWN | Index stale |
| V3-EXQ-466 | UNKNOWN | Index stale |
| V3-EXQ-467 | UNKNOWN | Index stale |
| V3-EXQ-468 | UNKNOWN | Index stale |
| V3-EXQ-471 | UNKNOWN | Index stale |

These require human review once index is rebuilt.

---

## Active stale claims noted (all > 6h)

| Session | Age | Task |
|---|---|---|
| exq397c-diagnosis + queue exq397d | 14.3h | Fix EXQ-397/397c manifests + queue EXQ-397d |
| sd033-ocd-manifest-hygiene | 15.3h | Fix 24 SD-033 OCD battery manifest hygiene issues |
| diagnose-errors: V3-EXQ-433c + V3-EXQ-470a | 15.9h | Scripts written (draft); not queued yet |
| fix-sd016-cue-action-proj | 16.0h | EXQ-449b script written; not queued |
| governance-cycle-2026-04-22 | 16.5h | Full governance cycle not completed |

Scripts exist for V3-EXQ-433c, V3-EXQ-470a, V3-EXQ-449b but they are NOT in
experiment_queue.json. User confirmation needed before queuing.

---

*Structured data: `evidence/planning/diagnose_staging.json`*
