# Diagnose Staging Report -- 2026-04-29

**Session:** afternoon scheduled diagnose-errors (staging mode)
**Generated UTC:** 2026-04-29T14:18:00Z
**Status:** **NO FIX SCRIPTS REQUIRED** (4 governance handoffs; 3 carryovers from 2026-04-28)

---

## Summary

| Metric | Value |
|--------|-------|
| Total ERRORs in runner_status (monolithic + per-machine) | 84 |
| ERRORs without a successor ID | 10 |
| Already in `discussed_experiment_dirs` | 6 |
| Requiring fresh audit | **4** |
| Requiring a fix script | **0** |
| Runner status sync gap | 0 |
| Pending queue depth | 0 items |

All four audited ERRORs are duplicate-machine artifacts where the experiment already has an authoritative outcome (FAIL/FAIL/PASS/UNKNOWN) on at least one other machine. None require a fix script. Three of the four are unchanged carryovers from the 2026-04-28 staging report (governance walk has not yet absorbed them); one is new (V3-EXQ-498, already addressed via run-level reviewed_run_id and the 2026-04-28T22Z governance cycle).

| Queue ID | When | Failure | Authoritative result | Disposition |
|----------|------|---------|---------------------|-------------|
| V3-EXQ-125a | 2026-04-06T15:56Z | exit 1 (1.3s startup) on ree-cloud-1 | FAIL on Daniel-PC + EWIN-PC | Mark discussed (carryover) |
| V3-EXQ-247  | 2026-04-06T15:56Z | exit 1 (1.4s startup) on ree-cloud-1 | FAIL on DLAPTOP-4 + Daniel-PC | Mark discussed (carryover) |
| V3-EXQ-249b | 2026-04-07T14:02Z | SIGTERM (-15) after 78min on ree-cloud-1 | PASS on EWIN-PC | Mark discussed (carryover) |
| V3-EXQ-498  | 2026-04-28T21:13Z | exit 1 on ree-cloud-2 | UNKNOWN on DLAPTOP-4 (already governance-classified non_contributory) | Mark discussed (new) |

---

## V3-EXQ-498 (OCD Layer 1 closure threshold sweep) -- new this session

**Root cause:** Duplicate-machine run artifact on `ree-cloud-2`. The DLAPTOP-4.local entry at 2026-04-28T20:29:54Z (non-ERROR, classified UNKNOWN) is the authoritative completion. Cloud-2 picked up duplicate work and crashed at exit 1 -- same multi-machine claim-race pattern as 125a / 247 / 249b / 490.

**Already addressed:**
- Run-level: `v3_exq_498_ocd_layer1_closure_threshold_sweep_20260428T201903Z_v3` is in `reviewed_run_ids`.
- Governance: discussed in the 2026-04-28T22Z cycle. Manifest classified `non_contributory` (OCD Layer 1 disconfirmed; escalates to Layer 2/3).
- Monolithic `runner_status.json` already prefers the non-ERROR DLAPTOP-4 entry via merge.

**Disposition:** Governance handoff -- add `V3-EXQ-498` to `review_tracker.discussed_experiment_dirs` so future scans don't re-surface the per-machine ERROR row.

---

## Carryovers (unchanged from 2026-04-28 staging)

### V3-EXQ-125a (ARC-029 committed-mode harm redesign)
Duplicate-machine run on ree-cloud-1; FAIL already authoritative on Daniel-PC (2026-04-05T23:48Z) + EWIN-PC (2026-04-06T02:28Z). No fix needed.

### V3-EXQ-247 (SD-011/SD-012 Full Integration Validation)
Duplicate-machine run on ree-cloud-1; FAIL already authoritative on DLAPTOP-4 (2026-04-06T08:09Z) + Daniel-PC (2026-04-07T10:50Z). Evidence dir `v3_exq_247_sd011_sd012_integration/` carries the FAIL.

### V3-EXQ-249b (INV-053 Depression Attractor Replication)
SIGTERM on ree-cloud-1 after 78min; PASS already authoritative on EWIN-PC (2026-04-07T02:29Z, ~10h before the kill). Evidence dir `v3_exq_249_inv053_depression_attractor_replication/` carries the PASS.

---

## Runner status reconciliation

No sync gap detected between monolithic `runner_status.json` and per-machine files in `runner_status/`. All per-machine `completed` IDs are present in the monolithic list. Auto-merge on startup (added 2026-04-06) is healthy.

---

## Optional infrastructure follow-up (carryover, informational)

The recurring duplicate-claim ERROR pattern continues. Now four examples in this report (125a / 247 / 249b / 498) plus V3-EXQ-490 from the 2026-04-27T05:25Z session. Same root-cause: a small window between `git pull` and `git push` where two machines can claim the same queue_id. The first machine's PASS/FAIL/UNKNOWN is authoritative; the second machine's run becomes a duplicate that crashes at startup, gets SIGTERM'd, or completes redundantly. Not a code bug -- a coordination protocol question -- so it lives outside diagnose-errors scope.

---

## Awaiting human confirmation

**None.** No fix experiments proposed; no draft scripts written; no queue edits made. This staging report is informational only.

**Recommended next action:** Step 2 of the scheduled task (queue-experiment skill).
