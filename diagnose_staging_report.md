# Diagnose Staging Report -- 2026-04-28

**Session:** afternoon scheduled diagnose-errors (staging mode)
**Generated UTC:** 2026-04-28T14:17:02Z
**Status:** **NO FIX SCRIPTS REQUIRED** (3 governance handoffs)

---

## Summary

| Metric | Value |
|--------|-------|
| Total ERRORs in runner_status (monolithic + per-machine) | 83 |
| ERRORs without a successor ID | 31 |
| Already in `discussed_experiment_dirs` (governance handled) | 28 |
| Requiring fresh audit | **3** |
| Requiring a fix script | **0** |
| Runner status sync gap | 0 |

All three audited ERRORs are duplicate-machine artifacts on `ree-cloud-1` where the experiment already has authoritative outcomes on at least one other machine (FAIL/FAIL/PASS). None require a fix script. Three governance handoffs requested (add to `review_tracker.discussed_experiment_dirs` on next /governance walk).

| Queue ID | When | Failure | Authoritative result(s) | Disposition |
|----------|------|---------|------------------------|-------------|
| V3-EXQ-125a | 2026-04-06T15:56Z | exit 1 (1.3s startup) on ree-cloud-1 | FAIL on Daniel-PC + FAIL on EWIN-PC | Mark discussed |
| V3-EXQ-247  | 2026-04-06T15:56Z | exit 1 (1.4s startup) on ree-cloud-1 | FAIL on DLAPTOP-4.local + FAIL on Daniel-PC | Mark discussed |
| V3-EXQ-249b | 2026-04-07T14:02Z | SIGTERM (-15) after 78min on ree-cloud-1 | PASS on EWIN-PC | Mark discussed |

---

## V3-EXQ-125a (ARC-029 committed-mode harm redesign)

**Root cause:** Duplicate-machine run artifact on `ree-cloud-1`. Exit code 1 within 1.3s of startup -- crashed before the experiment's main loop, almost certainly during environment initialization or pull race during early multi-machine deployment.

**Authoritative results already exist:**
- FAIL on Daniel-PC, 2026-04-05T23:48Z
- FAIL on EWIN-PC, 2026-04-06T02:28Z

**Fix applied:** None. Experiment outcome (FAIL on two machines) is the authoritative scientific result for ARC-029.

**Disposition:** Governance handoff -- add `V3-EXQ-125a` to `review_tracker.discussed_experiment_dirs` in next /governance walk.

---

## V3-EXQ-247 (SD-011/SD-012 Full Integration Validation)

**Root cause:** Duplicate-machine run artifact on `ree-cloud-1`. Exit code 1 within 1.4s of startup -- same pattern as V3-EXQ-125a.

**Authoritative results already exist:**
- FAIL on DLAPTOP-4.local, 2026-04-06T08:09Z
- FAIL on Daniel-PC, 2026-04-07T10:50Z
- Evidence dir: `evidence/experiments/v3_exq_247_sd011_sd012_integration/`

**Fix applied:** None. Experiment outcome (FAIL on two machines) is the authoritative scientific result for SD-011/SD-012 integration.

**Disposition:** Governance handoff -- add `V3-EXQ-247` to `review_tracker.discussed_experiment_dirs`.

---

## V3-EXQ-249b (INV-053 Depression Attractor Replication)

**Root cause:** Duplicate-machine run on `ree-cloud-1` killed by SIGTERM (-15) after 4672s (~78min). Same SIGTERM-on-cloud pattern observed in V3-EXQ-490 (handled by 2026-04-27T05:25 diagnose-errors session) -- shared-vCPU OOM neighbour pressure or transient cloud scheduler kill. Not a code crash.

**Authoritative result already exists:**
- **PASS on EWIN-PC, 2026-04-07T02:29Z** (~10h before the ree-cloud-1 kill)
- Evidence dir: `evidence/experiments/v3_exq_249_inv053_depression_attractor_replication/`

**Fix applied:** None. Experiment already PASSed on EWIN-PC; the ree-cloud-1 SIGTERM is an infrastructure event on a duplicate machine.

**Disposition:** Governance handoff -- add `V3-EXQ-249b` to `review_tracker.discussed_experiment_dirs`. The PASS evidence is already authoritative.

---

## Runner status reconciliation

No sync gap detected between monolithic `runner_status.json` and per-machine files in `runner_status/`. All per-machine `completed` IDs are present in the monolithic list. The runner's auto-merge on startup (added 2026-04-06) appears to be working.

---

## Optional infrastructure follow-up (informational, not for diagnose-errors)

The recurring `ree-cloud-1` duplicate-claim pattern (V3-EXQ-125a + V3-EXQ-247 + V3-EXQ-249b in this report, plus V3-EXQ-490 in the 2026-04-27 session) suggests the multi-machine git-claim race has a small window where two machines can pull and start work before the first push lands. The first machine's PASS/FAIL is authoritative; the second machine's run becomes a duplicate that either crashes (env race), gets SIGTERM'd (idle / OOM), or completes redundantly. This isn't a code bug -- it's a coordination protocol question -- so it lives outside the diagnose-errors scope.

---

## Awaiting human confirmation

**None.** No fix experiments proposed; no draft scripts written; no queue edits made. This staging report is informational only.

**Recommended next action:** Step 2 of the scheduled task (queue-experiment skill) for substrate-ready proposed experiments.
