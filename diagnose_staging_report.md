# Diagnose-Errors Staging Report

**Session**: ree-diagnose-queue-2026-04-20T14 / afternoon automated run
**Generated**: 2026-04-20T14:19:14Z
**Mode**: STAGING (headless, scheduled task)

---

## Summary (2026-04-20 afternoon)

**0 unaddressed errors requiring new fix scripts.**

All recent ERROR entries (2026-04-17 onward) in runner_status.json were cross-referenced
against the current queue, completed IDs, and TASK_CLAIMS.json. All chains are addressed.

### Gap reconciliation

Monolithic runner_status.json is in sync with per-machine files. Gap: 0.

### Error chain analysis (2026-04-17+)

| Queue ID | Error date | Chain status |
|---|---|---|
| V3-EXQ-375 | 2026-04-17 | 375a completed (chain resolved) |
| V3-EXQ-406 | 2026-04-17 | 406a completed (chain resolved) |
| V3-EXQ-396 | 2026-04-17 | 396a completed (chain resolved) |
| V3-EXQ-397 | 2026-04-17 | 397a ERROR -> 397b FAIL -> 397c **pending in queue** |
| V3-EXQ-429 | 2026-04-17 | 429a completed (chain resolved) |
| V3-EXQ-430 | 2026-04-17 | 430a ERROR -> 430b FAIL (scientific) |
| V3-EXQ-324b | 2026-04-17 | 324c completed (chain resolved) |
| V3-EXQ-418a | 2026-04-17 | 418b completed (chain resolved) |
| V3-EXQ-385a | 2026-04-17 | 385b completed (chain resolved) |
| V3-EXQ-355a | 2026-04-17 | 355b completed (chain resolved) |
| V3-EXQ-430a | 2026-04-18 | 430b FAIL (scientific, not code) |
| V3-EXQ-397a | 2026-04-18 | 397b FAIL -> 397c pending in queue |
| V3-EXQ-325c | 2026-04-19 | 325d **claimed by DLAPTOP-4.local** (in progress) |

### Older errors (pre-2026-04-17)

All resolved in prior sessions. V3-EXQ-008 architecturally obsolete (SD-003 superseded
2026-04-18, confirmed in session diagnose-325c-2026-04-20T05).

---

## Pending experiment reviews (for user reference)

These were noted in pending_review.md at time of this session; they require human review:

| Run / Queue ID | Result | Claims |
|---|---|---|
| v3_exq_397_arc007_...20260419T153153Z_v3 | FAIL | ARC-007, SD-004 |
| v3_exq_433a_sd029_...20260419T161931Z_v3 | FAIL | MECH-256, SD-029 |
| v3_exq_445_sd032b_...20260419T205642Z_v3 | FAIL | ARC-033, ARC-058, MECH-258, MECH-260, SD-032b |
| v3_exq_446_sd032a_...20260420T013457Z_v3 | PASS | MECH-259, MECH-261, SD-032a |
| V3-EXQ-445 | UNKNOWN | runner-only |
| V3-EXQ-325c | ERROR | runner-only; fix queued as V3-EXQ-325d |

---

*Structured data: `evidence/planning/diagnose_staging.json`*
