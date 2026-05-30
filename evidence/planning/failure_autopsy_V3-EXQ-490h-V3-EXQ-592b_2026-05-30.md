# Failure Autopsy: V3-EXQ-490h + V3-EXQ-592b (manifest-pipeline cluster)

**Generated:** 2026-05-30T06:02:38Z
**Resolved:** 2026-05-30T06:22:29Z
**Scope:** cluster (2 FAILs sharing a manifest-pipeline failure shape)
**Status:** RESOLVED — bug fixed at ree-v3 commit [`41c3411`](ree-v3/experiment_runner.py) (2026-05-29T21:24:08Z); re-runs queued as V3-EXQ-490i + V3-EXQ-592c.
**Autopsy session:** failure-autopsy-490h-592b-20260530T060238Z
**Diagnose-errors session:** diagnose-errors-490h-592b-requeue-20260530T062229Z
**Routing decision:** `/diagnose-errors` for both targets. This was NOT a substrate FAIL of MECH-295 or MECH-090; it was a Phase-3 result-pipeline failure shape that the 2026-05-29 fix at commit `41c3411` resolves.

## Resolution (2026-05-30T06:22:29Z)

Diagnose-errors session confirmed the bug was already diagnosed and fixed by a parallel session before this autopsy was authored. The fix landed at ree-v3 commit [`41c3411`](ree-v3/experiment_runner.py) titled "runner: fix V3-EXQ-592b FAIL/ERROR silent-drop" — explicitly authored against this exact failure. The FAIL branch (`experiment_runner.py:2299-2367`) and ERROR branch (`experiment_runner.py:2261-2297`) now enforce the same manifest contract the PASS branch already had: present manifest → `git_push_results` → `coordinator_client.report_result` → `report_queue_remove`; missing manifest → WARN + release claim + leave queue entry for operator. Contract tests added at `ree-v3/tests/contracts/test_runner_fail_branch_persists_result.py`.

Runner fleet state at resolution:
- DLAPTOP-4.local (Mac): runner PID 31449 started 2026-05-30T05:46:22Z, post-fix. Live.
- ree-cloud-1 (hub): runner disabled by design (hub co-location guard).
- ree-cloud-2: powered off by cloud-scaler (last heartbeat 2026-05-29T23:06:31Z). Will pull post-fix code at next boot — `git log` on cloud-2's working tree at autopsy time confirms commit `41c3411` is in HEAD's history.
- ree-cloud-3, ree-cloud-4: stale heartbeats; will pull post-fix on next start.

Re-runs queued (the runner silently skips queue_ids already in `runner_status.json` completed list, so new letters are mandatory):
- **V3-EXQ-490i** ([v3_exq_490i_mech295_cascade_gap4_tier1.py](ree-v3/experiments/v3_exq_490i_mech295_cascade_gap4_tier1.py)) supersedes V3-EXQ-490h. Bit-identical script body; only EXPERIMENT_TYPE / QUEUE_ID / SUPERSEDES constants and docstring change. claim_ids unchanged: `["MECH-295"]`.
- **V3-EXQ-592c** ([v3_exq_592c_mech090_commit_readiness_gate_validation.py](ree-v3/experiments/v3_exq_592c_mech090_commit_readiness_gate_validation.py)) supersedes V3-EXQ-592b. Bit-identical script body. claim_ids unchanged: `["MECH-090"]`.

Smoke tested both with `--dry-run`; both initialize, step, write outcomes, print the new queue_id correctly. `validate_queue.py` PASS after `git add`. Section 4 below (the recommended diagnostic order) is preserved for provenance but is now historical — the diagnose-errors session traced the bug to its already-landed fix in five steps rather than the six laid out.

---

## 1. Targets and the failure mode

| Field | V3-EXQ-490h | V3-EXQ-592b |
|---|---|---|
| Script | `ree-v3/experiments/v3_exq_490h_mech295_cascade_gap4_tier1.py` | `ree-v3/experiments/v3_exq_592b_mech090_commit_readiness_gate_validation.py` |
| claim_ids (script) | `MECH-295` | `MECH-090` |
| experiment_purpose | `evidence` | `diagnostic` |
| supersedes | V3-EXQ-490g (post-library-rebuild successor) | V3-EXQ-592 (R-c gate amendment) |
| machine | `ree-cloud-2` (Hetzner CX22) | `DLAPTOP-4.local` (Mac, local) |
| runner sentinel | `verdict: FAIL`, `elapsed=5661.5s` | `Experiment: FAIL`, `elapsed=4162.6s` |
| completed_at (runner) | 2026-05-29T21:46:08Z | 2026-05-29T08:32:39Z |
| manifest on disk | **absent** at the path the runner advertised | **absent** at the path the runner advertised |
| coordinator `results` row | **absent** | **absent** |
| coordinator `spool` payload | empty | empty |
| `_runner_signals/V3-EXQ-XXX.json` sentinel | **absent** | **absent** |

## 2. Cluster shape — what is load-bearing

Both runs share the **same failure shape**, on the same day, on two different machines, in two different result-pipeline paths:

- Runner protocol reported FAIL via the experiment's print/sentinel stream.
- The coordinator `results` table has no row for either queue_id.
- The phase3 result-writer's git log shows no `phase3:` commit for either run.
- The next sibling completion in the runner queue arrived seconds later AND DID land cleanly:
  - V3-EXQ-612c PASS at 2026-05-29T21:46:09Z (ree-cloud-2) — **1s after** 490h's sentinel.
  - V3-EXQ-613 PASS at 2026-05-29T08:32:43Z (DLAPTOP-4) — **3s after** 592b's sentinel.

Two independent manifest-pipeline losses on the same day, both on FAIL outcomes, both with a clean sibling PASS landing within seconds, is not a coincidence of two unrelated bugs — it is the **fingerprint of an outcome-conditional bug in the result-publish path** (FAIL outcomes hitting a code branch the PASS path does not). The known runner UNKNOWN-result silent-drop bug at `experiment_runner.py:1394` is consistent with the ree-cloud-2 side; whether the same branch runs on the Mac is the diagnostic question.

This shape is the load-bearing observation. Per-claim behavioural autopsy on MECH-295 (490h) or MECH-090 R-c (592b) **cannot proceed** because the per-condition acceptance metrics are unrecoverable.

## 3. Why this is `/diagnose-errors` not failure-autopsy

- The skill's stated rule: ERROR / no-output / UNKNOWN routes to `/diagnose-errors`. The runner reported FAIL — but the operational failure mode is "manifest never landed", which is mechanistically a delivery / IO failure and not a scientific FAIL of the underlying claim.
- The four-layer diagnosis cannot fire: claim-alignment, biological-reference triage, prerequisites, implementation completeness, environment adequacy, measurement adequacy, integration, scale — none of them can be evaluated without the manifest's `evidence{}` flags and `per_condition_results`.
- The 490h script encodes a five-row interpretation grid (C1 cue / C2 dACC bias / C3 commit / C3 lift / C4 goal-active). Each FAIL mode routes to a different remedy (dACC wiring vs MECH-295 sub-gain sweep vs APPROACH_WANTING_THRESH sweep vs bridge activation probe). Without knowing which mode fired, autopsy would have to fabricate an interpretation.
- The 592b script is a 2-arm joint-PASS gate validation (ARM_0 GATED falsifier + ARM_1 GATED_FORCED_READY admit). Without knowing which arm fell over, the disposition (gate too restrictive vs gate too permissive vs both broken) cannot be selected.

## 4. What `/diagnose-errors` needs to do

This artifact is the handoff. A `/diagnose-errors` session should investigate, in this order:

1. **Confirm the manifest-loss vs incomplete-write distinction.** Read `REE_assembly/runner.log` (or `ree-v3/runner.log` on the Mac) for the time windows 2026-05-29T08:32:30–08:33:00Z and 2026-05-29T21:46:00–21:47:00Z. The 490h and 592b scripts both build the manifest dict in memory and write it via `with open(out_path, "w") as f: json.dump(...)` BEFORE calling `emit_outcome(...)`. If the runner.log shows the script's `Result written to: <path>` print, the manifest was created on disk and a later step deleted/lost it. If the runner.log shows the acceptance summary but NOT the `Result written to:` print, the script crashed at the JSON write step before producing the file.
2. **Trace the result-publish path.** Under Phase 3 the runner POSTs `/result` to the coordinator with the manifest bytes; the coordinator persists to the `results` table; the `phase3_git_writer` commits the manifest file. Empty `results` table rows for both queue_ids means either (a) the runner did not POST, or (b) the POST failed and the runner did not retry, or (c) the POST succeeded but the coordinator did not insert. Hit the coordinator log around the same timestamps to discriminate.
3. **Outcome-conditional code-path inspection.** Is there a branch in the runner's result-publish path that treats `outcome == "FAIL"` differently from `outcome == "PASS"`? The known `experiment_runner.py:1394` UNKNOWN-result silent-drop bug operates on the UNKNOWN path, not the FAIL path — but the cluster-shape evidence (two FAIL losses with sibling-PASS landings) suggests the FAIL path may share a code site with UNKNOWN that is not exercised by PASS.
4. **Once the bug is identified and fixed,** re-queue 490h-rerun and 592b-rerun (use new letters per the EXQ versioning rule — these IDs are now in `runner_status.json` completed list and the runner will silently skip a re-queue under the same ID). The re-queues are the scientific re-acquisition; the bug-fix is the substrate side.

## 5. What this artifact does NOT do

- Does NOT modify `claims.yaml`. MECH-295 and MECH-090 confidence is untouched. The runs left no governance-weight evidence (the indexer cannot ingest a non-existent manifest).
- Does NOT recommend any `evidence_direction` per claim. There is no manifest to set the field on.
- Does NOT modify `review_tracker.json`. Neither queue_id appears in `pending_review.md` (no manifest path to enumerate). 490h and 592b are unreviewable as run.
- Does NOT modify `substrate_queue.json`. No substrate gap was demonstrated; what was demonstrated is a result-pipeline bug, which is a runner / coordinator issue, not a substrate one.

## 6. Recommended routing (handoff to governance)

- **Route both targets to `/diagnose-errors`** with the recommended pipeline-trace order above as the starting probe.
- **No claim-weight change** for MECH-295 or MECH-090 from this session.
- **No supersession** of 490h or 592b (the re-queues will be new letter siblings, e.g. 490i / 592c — selected at the time the bug is fixed).
- **Concurrent-session protection**: my TASK_CLAIMS entry covers ONLY the two `failure_autopsy_V3-EXQ-490h-V3-EXQ-592b_2026-05-30.{md,json}` paths; no overlap with the active IGW-021 MECH-341 substrate claim.

## 7. Provenance

| Source | What it told us |
|---|---|
| `REE_assembly/evidence/experiments/runner_status/ree-cloud-2.json` | 490h runner-side FAIL sentinel; output_file path; elapsed time |
| `REE_assembly/evidence/experiments/runner_status/DLAPTOP-4.local.json` | 592b runner-side FAIL sentinel; output_file path; elapsed time |
| coordinator DB on `ree@91.98.130.117` (`/home/ree/REE_Working/ree-v3/coordinator/coordinator.db`) | `results` table contains no row for either queue_id; recent landings PASS-only; spool empty |
| `git -C REE_assembly log --all --since=2026-05-25 --oneline \| grep phase3:` | No `phase3:` result-commit for 490h or 592b; the writer would have committed if a `results` row existed |
| `ree-v3/experiments/v3_exq_490h_mech295_cascade_gap4_tier1.py` | five-row interpretation grid that the autopsy cannot consume without per-condition metrics |
| `ree-v3/experiments/v3_exq_592b_mech090_commit_readiness_gate_validation.py` | 2-arm joint-PASS gate validation; ARM_0 / ARM_1 acceptance disposition cannot be determined without the manifest |
| `REE_assembly/evidence/planning/failure_autopsy_V3-EXQ-490g-cohort_2026-05-29.md` | Prior cohort autopsy that 490h was built to remediate (library rebuild post-490g); confirms the script-design changes vs the predecessor were the intended C2 / C3-lift fix |

---

## 8. User decision (interactive gate, satisfied)

Asked 2026-05-30T06:01Z, answered the same minute: **Route both to `/diagnose-errors`.** The substrate-level autopsy options were rejected as fabricating an interpretation without manifest evidence. The manifest-recovery option was not selected — the cluster shape (two simultaneous, both on FAIL outcomes, both with clean sibling PASS landings) is sufficient evidence to diagnose the bug from the runner / coordinator logs without needing to reconstruct the lost manifests.
