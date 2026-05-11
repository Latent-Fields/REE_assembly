# Diagnose Staging Report -- 2026-05-11

**Session:** ree-diagnose-queue (afternoon scheduled, staging mode)
**Session ID:** diagnose-errors-staging-2026-05-11T1421Z
**Generated UTC:** 2026-05-11T14:21:02Z
**Status:** **NO FIX SCRIPTS REQUIRED** (7 unaddressed ERRORs; 0 are code bugs)

---

## Summary

| Metric | Value |
|--------|-------|
| Total ERRORs in runner_status (monolithic + per-machine) | 75 |
| Runner status sync gap before merge | 2 IDs (V3-EXQ-514i, V3-EXQ-547) -- merged |
| ERRORs without a successor ID | 7 |
| Requiring a fix script | **0** |
| Deliberate stubs blocked on upstream | 2 (V3-EXQ-449c, V3-EXQ-455a) |
| False ERRORs (manifest on disk) | 3 (V3-EXQ-244a, V3-EXQ-542, V3-EXQ-544) |
| Infrastructure failures (need rerun decision) | 2 (V3-EXQ-495, V3-EXQ-538) |
| Queue entries proposed (awaiting human confirmation) | 2 (V3-EXQ-495a, V3-EXQ-538a) |
| Governance actions proposed | rebuild_indexes + mark_discussed |

The seven unaddressed ERRORs split into three buckets. None require a code-fix script.

---

## Bucket 1: Deliberate stubs (no fix possible)

These scripts intentionally `raise NotImplementedError` because the experiment
they would run is gated on substrate or cascade-gate landings that have not
yet completed. They are NOT code bugs -- the runner correctly reports ERROR
because the script exited non-zero, but the ERROR is the point.

### V3-EXQ-449c -> proposed fix: NONE (no_fix_needed_deliberate_stub)

**Root cause:** Script raises `NotImplementedError` on purpose. Stub message:
"V3-EXQ-449c gated. MECH-284 Phase 3 substrate landed 2026-04-24 but cascade
gate V3-EXQ-476a/476b ran FAIL (V_s wired-but-inert -- catatonic-lock at
policy layer). Remaining blockers: (a) SD-037 (broadcast override regulator,
orexin-analog); (b) MECH-074b hippocampal consumer wiring landed on SD-035."
Exit code 1, ~0.1s.
**Fix applied:** None. SD-037 substrate DID land 2026-04-25 (CLAUDE.md
confirms). Remaining blockers: (i) V_s cascade-gate retest after SD-037 +
2026-04-29 staleness-into-gate wiring -- V3-EXQ-476-equivalent successor;
(ii) MECH-074b retrieval-bias-aware replay path on SD-035. Both outside the
diagnose-errors workflow.
**Draft script:** -- (no fix script)
**Proposed claim_ids:** -- (no experiment to re-tag)
**Status:** BLOCKED ON UPSTREAM PREREQUISITES
**Next step for user:** Add to `review_tracker.discussed_experiment_dirs`
(carryover from prior staging reports). When V3-EXQ-476 cascade gate
PASSes, /queue-experiment a fresh ID for MECH-074b validation.

### V3-EXQ-455a -> proposed fix: NONE (no_fix_needed_deliberate_stub)

**Root cause:** Script raises `NotImplementedError` on purpose. Stub
message: "V3-EXQ-455a gated. ... Remaining blocker is SD-037 (broadcast
override regulator, orexin-analog)." Exit code 1, ~0.05s.
**Fix applied:** None. SD-037 DID land 2026-04-25; remaining blocker is
V_s cascade-gate retest. Outside diagnose-errors scope.
**Draft script:** --
**Proposed claim_ids:** --
**Status:** BLOCKED ON UPSTREAM PREREQUISITES
**Next step for user:** Same as 449c -- mark discussed; re-queue as fresh
EXQ once V_s cascade-gate retest passes.

---

## Bucket 2: False ERRORs (manifest on disk; needs governance, not diagnose)

These experiments PRODUCED valid PASS manifests on disk. The runner mis-
classified them either because the runner state was stale (244a) or the
script did not emit the runner-expected sentinel line on stdout (542, 544).
None need a rerun.

### V3-EXQ-244a -> proposed fix: NONE (false_error_manifest_exists)

**Root cause:** runner_status reports ERROR (exit -15 on ree-cloud-2 at
2026-05-06T09:28:53Z after 80min). But a real PASS manifest exists at
`REE_assembly/evidence/experiments/v3_exq_244a_mech165_replay_diversity_validation_v3.json`
with `elapsed_seconds=19395` (~5.4h) and `outcome=PASS`,
`evidence_direction=supports`, `claim_ids=['MECH-165']`. Manifest committed
2026-05-07T05:27Z (the day after the SIGTERM). A follow-on production run
completed normally; runner_status was never updated.

> NOTE: the 2026-05-06 staging report initially flagged this manifest as a
> smoke-test artifact -- correct at the time of writing (elapsed was
> implausibly small) but the file was overwritten by a real production run.

**Fix applied:** None at experiment level.
**Draft script:** --
**Proposed claim_ids:** MECH-165 (inherited from on-disk manifest)
**Status:** NEEDS GOVERNANCE ACTION (not diagnose-errors)
**Next step for user:** Run /governance to ingest the manifest into
`claim_evidence.v1.json` and mark V3-EXQ-244a discussed in
`review_tracker.json`. No rerun needed.

### V3-EXQ-542 -> proposed fix: NONE (runner_sentinel_parse_gap)

**Root cause:** Runner reported ERROR ("No runner sentinel emitted and no
PASS/FAIL on stdout; exit=0; secs=2.2") on 2026-05-09T20:22:11Z on Mac.
But a real PASS manifest exists at
`REE_assembly/evidence/experiments/v3_exq_542_arc062_gated_policy_substrate_readiness_v3_20260509T202211Z.json`
with `result=PASS`, `evidence_direction=supports`, claim_ids include
ARC-062. Script ran cleanly and wrote PASS to the canonical manifest but
did not print the runner-expected `verdict:` / `PASS` sentinel line to
stdout. CLAUDE.md ARC-062 Phase 1 entry confirms "V3-EXQ-542 5/5 PASS
2026-05-09T20:22:11Z".
**Fix applied:** None at experiment level. Script could be patched to add
a sentinel print so future smoke runs are correctly classified, but no
rerun needed.
**Draft script:** --
**Proposed claim_ids:** ARC-062 (inherited from on-disk manifest)
**Status:** NEEDS GOVERNANCE ACTION (not diagnose-errors)
**Next step for user:** (a) /governance ingest; (b) mark V3-EXQ-542
discussed; (c) optional template patch to emit sentinel for substrate-
readiness-diagnostic scripts.

### V3-EXQ-544 -> proposed fix: NONE (runner_sentinel_parse_gap)

**Root cause:** Runner reported ERROR ("No runner sentinel emitted and no
PASS/FAIL on stdout; exit=0; secs=2.8") on 2026-05-10T10:44:58Z on Mac.
A real PASS manifest exists at
`REE_assembly/evidence/experiments/v3_exq_544_mech313_noise_floor_substrate_readiness_v3_20260510T104458Z.json`
with `result=PASS`, `evidence_direction=supports`, claim_ids include
MECH-313. Same root cause as V3-EXQ-542. CLAUDE.md MECH-313 entry confirms
"V3-EXQ-544 substrate-readiness diagnostic ... Smoke 5/5 PASS 2026-05-10".
**Fix applied:** None at experiment level.
**Draft script:** --
**Proposed claim_ids:** MECH-313 (inherited from on-disk manifest)
**Status:** NEEDS GOVERNANCE ACTION (not diagnose-errors)
**Next step for user:** Same as 542. Already in pending_review.md
unclaimed-manifests table.

---

## Bucket 3: Infrastructure failures (Mac-pinned reruns proposed)

These experiments were killed by external SIGTERM on cloud workers (Hetzner
CX22). No code bug; no manifest. Recommend Mac-pinned reruns. Two queue
entries are proposed -- AWAITING HUMAN CONFIRMATION before they are
appended to `experiment_queue.json`.

### V3-EXQ-495 -> proposed fix: V3-EXQ-495a (Mac-pinned rerun, no code change)

**Root cause:** MECH-163 V3 full-completion gate (VTA / hippocampally-
planned arm) ran 14383s (~4h) on ree-cloud-1 starting 2026-04-28T17:14Z,
then exit -15 (SIGTERM) at 21:13Z. estimated_minutes was 1500 (~25h) --
ran a quarter of expected duration before the worker killed the process.
Hetzner CX22 (cloud-1) is undersized per memory note
`reference_cloud_workers.md`; cloud-1 throughput is ~0.23 min/ep at 200
steps/ep vs ~0.10 min/ep on Mac, so this experiment's full duration was
~40h on cloud-1 vs ~17h on Mac. The 4h SIGTERM is most consistent with a
Hetzner platform-side restart/limit. No manifest on disk.
**Fix applied:** No code change. Successor V3-EXQ-495a re-queues the same
script with `machine_affinity=DLAPTOP-4.local`.
**Draft script:** experiments/v3_exq_495_mech163_planned_system_gate.py
(no change)
**Proposed claim_ids:** [MECH-163] -- inherited and re-evaluated; same
script tests same claim, machine affinity is the only diff.
**Draft queue entry:** see `diagnose_staging.json`.
**Status:** AWAITING HUMAN CONFIRMATION
**Next step for user:** Confirm Mac-pinned rerun (vs. shrinking scope,
splitting into smaller arms, or moving to Daniel-PC). 17h on Mac is a
substantial commitment -- worth confirming science value before queueing.

### V3-EXQ-538 -> proposed fix: V3-EXQ-538a (Mac-pinned rerun, no code change)

**Root cause:** SD-049 Phase 2 reef behavioural validation, sleep-on
ablation, ran 1470s (~24min) on ree-cloud-1 starting 2026-05-08T12:29Z then
SIGTERM at 12:54Z. Same 2026-05-08 cloud-1 silent-fail cluster as
V3-EXQ-433f and V3-EXQ-537 (see V3-EXQ-537a queue note in git history
flagging the pattern explicitly). The 2026-05-09 manifest-leak fix in
`experiment_runner._git_push_with_retry` addresses the conflict-recovery
path that was destroying manifests, but did not necessarily resolve all
cloud-1 capacity / push-instability issues.
**Fix applied:** No code change. Successor V3-EXQ-538a re-queues with
`machine_affinity=DLAPTOP-4.local` per the V3-EXQ-537a precedent.
**Draft script:** experiments/v3_exq_538_sd049_phase2_with_sleep.py
(no change)
**Proposed claim_ids:** [SD-049] -- re-evaluated; still the correct tag.
**Draft queue entry:** see `diagnose_staging.json`.
**Status:** AWAITING HUMAN CONFIRMATION
**Next step for user:** Confirm Mac-pinned rerun. Append draft entry to
`ree-v3/experiment_queue.json` and validate.

---

## Infrastructure observation

**Recurring pattern:** Hetzner CX22 cloud workers (ree-cloud-1, ree-cloud-2)
periodically SIGTERM long-running experiments or silently drop manifests.
Confirmed incidents:

- 2026-04-28 -- V3-EXQ-495 (4h cloud-1 SIGTERM)
- 2026-05-06 -- V3-EXQ-244a / V3-EXQ-530 (coincident cloud-1+cloud-2 SIGTERM)
- 2026-05-08 -- V3-EXQ-433f / V3-EXQ-537 / V3-EXQ-538 silent-fail cluster on cloud-1

**Partial mitigation 2026-05-09:**
`experiment_runner._git_push_with_retry` manifest-leak in conflict-recovery
FIXED. Captures pre-reset HEAD SHA; restores result_files via
`git checkout` from pre-reset SHA after reset+stash-pop. Contract test
C1/C2/C3 in `tests/contracts/test_runner_manifest_survives_conflict_recovery.py`.
This addresses the specific path that destroyed manifests during
conflict-recovery push retries; does not necessarily address all cloud-1
capacity / push-instability issues.

**Recommendation:** For high-priority or long-duration experiments, prefer
Mac-pinning over cloud-1 until the platform-side cause is understood. The
cloud workers remain useful for short / lower-priority runs where a SIGTERM
or manifest drop is recoverable. Consider whether a watchdog / re-queue
mechanism in the runner could auto-retry SIGTERM runs (currently they are
silently dropped from the queue per queue completion behaviour rules).

---

## Summary of next steps for the user

1. **Two queue appends awaiting confirmation** -- V3-EXQ-495a (Mac-pinned
   ~17h MECH-163 rerun; substantial commitment) and V3-EXQ-538a (Mac-pinned
   ~3.5h SD-049 Phase 2 rerun). Both have draft entries in
   `diagnose_staging.json`. Append to `experiment_queue.json` after
   confirming science value, then run `validate_queue.py`.

2. **Three governance ingestions** -- V3-EXQ-244a / V3-EXQ-542 / V3-EXQ-544
   all have valid PASS manifests on disk that aren't yet ingested into
   `claim_evidence.v1.json`. Run `/governance` (or
   `python evidence/experiments/scripts/build_experiment_indexes.py` then
   `python scripts/generate_pending_review.py`) to ingest, then mark these
   discussed in `review_tracker.json`. V3-EXQ-542 and V3-EXQ-544 are already
   listed in `pending_review.md` unclaimed-manifests table.

3. **Two carryover stubs** -- V3-EXQ-449c and V3-EXQ-455a. Mark discussed
   in `review_tracker.json` to stop them from re-appearing in future
   diagnose-errors runs. Re-queue as fresh EXQ IDs (not letter suffixes)
   when their upstream blockers (V_s cascade-gate retest, MECH-074b
   consumer wiring) clear.

4. **Optional template patch** -- substrate-readiness-diagnostic scripts
   should emit a `verdict: PASS` (or similar) sentinel line so the runner
   correctly classifies them. Two such scripts (V3-EXQ-542 substrate-
   readiness for ARC-062 Phase 1; V3-EXQ-544 substrate-readiness for
   MECH-313) hit this gap on the same day. The pattern will likely recur
   for sibling substrate-readiness diagnostics (V3-EXQ-545 / V3-EXQ-546 /
   V3-EXQ-547 already passed but may have hit the same misclassification).
