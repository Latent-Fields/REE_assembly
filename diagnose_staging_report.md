# Diagnose Staging Report -- 2026-05-06

**Session:** afternoon scheduled diagnose-errors (staging mode)
**Generated UTC:** 2026-05-06T14:17:00Z
**Status:** **NO FIX SCRIPTS REQUIRED** (6 unaddressed ERRORs; 0 are code bugs)

---

## Summary

| Metric | Value |
|--------|-------|
| Total ERRORs in runner_status (monolithic + per-machine) | 72 |
| ERRORs without a successor ID | 6 |
| Requiring a fix script | **0** |
| Runner status sync gap | 0 |
| Pending queue depth | 0 items |

The six unaddressed ERRORs split into three categories. None require a code-fix script.

| Queue ID | When | Failure | Category | Disposition |
|----------|------|---------|----------|-------------|
| V3-EXQ-008  | 2026-03-17T18:09Z | exit 1 (0.9s) | stale_abandoned | Mark discussed (carryover from 2026-04-29) |
| V3-EXQ-455a | 2026-04-23T23:23Z | NotImplementedError (0.05s) | intentional_placeholder | Awaits V3-EXQ-476 PASS + MECH-284 Phase 3 (carryover) |
| V3-EXQ-449c | 2026-04-24T02:18Z | NotImplementedError (0.1s)  | intentional_placeholder | Awaits V3-EXQ-476 PASS + V3-EXQ-445d PASS + MECH-074b consumer wiring (carryover) |
| V3-EXQ-495  | 2026-04-28T21:13Z | SIGTERM (-15) after 4h on ree-cloud-1 | infrastructure_sigterm | User decides re-queue |
| V3-EXQ-530  | 2026-05-06T09:28Z | SIGTERM (-15) after 10min on ree-cloud-1 | infrastructure_sigterm | User decides re-queue (smoke-tested PASS prior) |
| V3-EXQ-244a | 2026-05-06T09:28Z | SIGTERM (-15) after 80min on ree-cloud-2 | infrastructure_sigterm | User decides re-queue; **delete smoke-test JSON first** |

---

## Infrastructure root cause IDENTIFIED 2026-05-06T14:30Z

**Cause: race in this project's own GitHub Actions cloud-scaler workflow. NOT an hcloud TOS / process-length limit.**

Mechanism (code path traced end-to-end):
1. `experiment_runner.py:466` -- when the runner claims an item via `attempt_claim()`, it sets
   `item["status"] = "claimed"` (NOT `"pending"`) on the queue file and pushes.
2. `ree-v3/.github/workflows/cloud-scaler.yml:48-58` -- the every-15-minute scaler counts
   ONLY items with `status == "pending"`:
   ```python
   n = sum(1 for i in q.get('items', [])
           if i.get('status') == 'pending'
           and i.get('machine_affinity') in ('any', aff))
   ```
3. `cloud-scaler.yml:73-76` -- when CLAIMABLE drops to 0 and the server is `running`, it
   issues `hcloud server shutdown`. The comment even acknowledges this triggers SIGTERM:
   ```
   # shutdown (not poweroff) so systemd sends SIGTERM for graceful drain
   hcloud server shutdown "$SERVER_NAME"
   ```
4. Result: every long-running cloud experiment is at risk every 15 minutes. As soon as a
   runner claims its item (legitimately, status="claimed"), the scaler thinks "no claimable
   pending work" and turns the machine off mid-experiment.

Timing fingerprint matches GitHub Actions cron schedule (every */15 with the typical 0-15
min delay from cron event to job execution):

| Event | SIGTERM (UTC) | Prev :00/:15/:30/:45 tick | Delay |
|-------|---------------|---------------------------|-------|
| V3-EXQ-325c | 22:18:04 | 22:15 | +3.1 min |
| V3-EXQ-495  | 21:13:57 | 21:00 | +13.9 min |
| V3-EXQ-514a | 17:12:18 | 17:00 | +12.3 min |
| V3-EXQ-244a | 09:28:53 | 09:15 | +13.9 min |
| V3-EXQ-530  | 09:28:51 | 09:15 | +13.8 min |

All five SIGTERMs land inside the 15-minute cron window. The 2026-05-06T09:28Z coincident
kill on both clouds is a single GitHub Actions run hitting both servers in the same loop
iteration.

**Why this didn't surface earlier:** when the queue had multiple `pending` items at the
same affinity, CLAIMABLE stayed > 0 even with one claimed item, so the scaler did not
shut anything down. The kill rate scales with *fraction of time the queue is empty-of-
pending while the runner is mid-experiment* -- precisely when the runner is doing its job.

**Fixes (pick one; option 1 is the minimal one-line change):**
1. `cloud-scaler.yml` -- count `claimed` as well as `pending`:
   ```python
   if i.get('status') in ('pending', 'claimed')
   ```
   Original intent of the scaler was "is there anything for this machine to work on or
   already working on?" Items with `status=claimed` and `claimed_by.machine ==
   server_affinity` are exactly that.
2. `cloud-scaler.yml` -- additionally consult heartbeats: if
   `runner_heartbeats/<server>.json` reports `current_exq != null`, never shut down.
   Race-free even if the queue file is stale.
3. `experiment_runner.py:466` -- keep `status="pending"` and rely on `claimed_by` alone
   to signal claim. Need to confirm nothing else (explorer, validate_queue, governance)
   consumes `status="claimed"` before doing this.
4. `cloud-scaler.yml` -- disable scheduled shutdown; rely on manual stop / billing
   alerts. Simplest if the auto-stop savings are small.

Recommend **option 1 + option 2 together**. Option 1 fixes the dominant case; option 2 is
defence in depth against any future status-state addition.

**Other implications for the SIGTERM list:**
- V3-EXQ-249b (2026-04-07, ree-cloud-1, ~78 min): same mechanism. Already tagged in
  2026-04-29 staging as duplicate-machine artifact -- diagnosis was incomplete, the
  SIGTERM was scaler-induced, not duplicate-machine churn.
- V3-EXQ-490 (cited in earlier diagnosis as same pattern): same mechanism.
- DLAPTOP-4.local SIGTERMs (2026-03-29/30, V3-EXQ-157/158/159/157a) are NOT this
  mechanism (laptop has no auto-scaler) -- those are local cancels / OS sleep, separate
  issue.

**Confidence:** high. Code path traced end-to-end (runner-status mutation -> scaler-
counting logic -> shutdown command -> systemd SIGTERM). Timing fits cron cadence with
characteristic 0-15 min Actions delay. No alternative explanation needed.

**Workers stuck off?** If V3-EXQ-244a / V3-EXQ-530 caused the scaler shutdown, the
servers will be `off` until the next cron tick fires with `CLAIMABLE > 0` -- the queue is
currently empty so they will stay off. Either restart manually via `hcloud server
poweron`, or queue a new experiment (the next */15 tick will start them once a `pending`
item is visible). Either is fine; the queue is supposed to be empty right now anyway
(today's batch already ran).

---

## V3-EXQ-008 (SD-003 larger-world / smaller-observation)

**Root cause:** March 17 2026 startup crash, exit 1 in 0.9s. Pre-runner.log retention; no traceback recoverable.

**Why no fix:** SD-003 has had 27 follow-on experiments since March; V3-EXQ-525 PASSed today (06:51Z) as the SD-003 anchor. The larger-world question is functionally absorbed into the SD-003 program via different EXQ numbers. Already listed in 2026-04-29 staging report's `errors_already_discussed_no_action` -- carryover.

**Disposition:** Governance handoff -- add to `review_tracker.discussed_experiment_dirs`.

---

## V3-EXQ-455a (SD-032a salience coordinator -- V_s-enabled re-run)

**Root cause:** Script raises `NotImplementedError` at top of run with self-documenting message:
> V3-EXQ-455a full implementation pending: awaiting V3-EXQ-476 cascade gate PASS and MECH-284 Phase 3 consumer landing.

Exit 1 in 0.05s. Intentional precondition gate.

**Why no fix:** V3-EXQ-476 is itself a `NotImplementedError` placeholder; V3-EXQ-476a and V3-EXQ-476b both UNKNOWN. Until MECH-284 Phase 3 + V_s flag plumbing in `REEConfig.from_dims()` are complete, no work on V3-EXQ-455a is meaningful. Carryover from 2026-04-29.

**Disposition:** Governance handoff (mark discussed) + upstream tracking.

---

## V3-EXQ-449c (MECH-074b BLA retrieval bias on action selection -- V_s-gated)

**Root cause:** Script raises `NotImplementedError` at top of run with self-documenting message:
> V3-EXQ-449c full implementation pending: awaiting (a) V3-EXQ-476 PASS, (b) V3-EXQ-445d PASS, and (c) MECH-074b hippocampal consumer wiring landed on SD-035.

Exit 1 in 0.1s. Intentional gate.

**Why no fix:** All three prerequisites unmet. V3-EXQ-476 ERROR (placeholder), V3-EXQ-445d ERROR (placeholder also awaiting V3-EXQ-476), MECH-074b retrieval-bias-aware replay path not yet present in SD-035. Pure dependency chain. Carryover from 2026-04-29.

**Disposition:** Governance handoff (mark discussed) + upstream tracking.

---

## V3-EXQ-495 (MECH-163 V3 full-completion gate -- VTA / hippocampally-planned arm)

**Root cause:** Ran 4.0 hours on ree-cloud-1 starting 2026-04-28T17:14Z, then SIGTERM (exit -15) at 21:13Z. SIGTERM is an external signal -- cloud worker process killed by parent (timeout, restart, or remote shutdown). No Python traceback.

**Why no fix:** Not a code bug. The estimate budget for this heavyweight full-completion gate likely exceeded the cloud worker's runtime ceiling, or the worker was restarted mid-run.

**Disposition:** User decides whether to re-queue. If yes:
- Confirm scientific necessity (MECH-163 may have other evidence routes)
- Re-queue with `force_rerun=true` under same ID, OR fresh letter `V3-EXQ-495a`
- Pin `machine_affinity` to a host with sufficient runtime headroom (DLAPTOP-4.local typically OK for long runs)

---

## V3-EXQ-530 (ARC-016 precision-to-commitment circuit: dACC precision_commit_ratio)

**Root cause:** Ran 10.0 minutes on ree-cloud-1 starting 2026-05-06T09:18:48Z, then SIGTERM at 09:28:51Z. Coincident with V3-EXQ-244a SIGTERM on ree-cloud-2 at 09:28:53Z. Both cloud workers shut down within 2 seconds of each other.

**Why no fix:** Smoke-tested PASS earlier today (~70s, all code paths exercised; per WORKSPACE_STATE entry `write-exq530-arc016-precision-commit 2026-05-06T09:18Z`). The 10-minute SIGTERM is purely an infrastructure event, not a script regression.

**Disposition:** User decides whether to re-queue. Suggested approach:
- Re-queue under same ID with `force_rerun=true`, OR assign `V3-EXQ-530a`
- `claim_ids: ["ARC-016"]` unchanged (SIGTERM produced no measurement)
- Consider `machine_affinity` adjustment if cloud-restart pattern repeats

---

## V3-EXQ-244a (MECH-165 reverse replay diversity validation)

**Root cause:** Ran 1.34 hours on ree-cloud-2 starting 2026-05-06T08:08:44Z, then SIGTERM at 09:28:53Z. Same cloud-shutdown event as V3-EXQ-530.

**Why no fix:** Not a code bug.

**Pre-requeue cleanup required:** There is a flat-JSON evidence file at
`REE_assembly/evidence/experiments/v3_exq_244a_mech165_replay_diversity_validation_v3.json`
with `outcome: PASS`, but:
- run_id has no timestamp suffix (bare `v3_exq_244a_mech165_replay_diversity_validation_v3`)
- file is **untracked in git**
- condition_stats show NO_REPLAY/FORWARD_REPLAY retentions of -9.3e-11 (essentially zero noise) and BALANCED_REPLAY at 0.013 driven by a single seed -- implausibly clean for a real run

This is a smoke-test artifact from a local dry-run, NOT a real production run. **It must be deleted before any re-queue** so the indexer cannot mistake it for evidence.

**Disposition:** User decides whether to re-queue. Suggested:
1. `rm REE_assembly/evidence/experiments/v3_exq_244a_mech165_replay_diversity_validation_v3.json`
2. Re-queue with `force_rerun=true` under same ID, OR assign `V3-EXQ-244b`
3. `claim_ids: ["MECH-165"]` unchanged

---

## Next actions

1. **Governance handoff:** add V3-EXQ-008, V3-EXQ-455a, V3-EXQ-449c, V3-EXQ-495, V3-EXQ-530, V3-EXQ-244a to `review_tracker.discussed_experiment_dirs` in the next `/governance` walk so they stop appearing as undiagnosed ERRORs.
2. **User decisions:** confirm whether V3-EXQ-495 / V3-EXQ-530 / V3-EXQ-244a should be re-queued. For V3-EXQ-244a, **delete the smoke-test JSON before re-queuing**.
3. **Infra investigation:** the 2026-05-06T09:28Z coincident SIGTERM on ree-cloud-1 and ree-cloud-2 (heartbeats stale; restart runners if still down). Recurring pattern (V3-EXQ-249b, V3-EXQ-495 same machine); worth a root-cause look.
4. **Upstream blockers:** V3-EXQ-455a and V3-EXQ-449c will keep ERRORing until V3-EXQ-476 lands (which itself awaits MECH-284 Phase 3 + V_s flag plumbing in `REEConfig.from_dims()`).
5. **Carryover note:** the 2026-04-29 staging report's governance handoffs (V3-EXQ-125a / V3-EXQ-247 / V3-EXQ-249b / V3-EXQ-498) have not yet been absorbed into `review_tracker.discussed_experiment_dirs` -- ideally batch with today's six.

**Status:** AWAITING HUMAN CONFIRMATION (governance handoff + user decisions on re-queue)
