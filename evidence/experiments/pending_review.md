# Pending Experiment Review

Generated: `2026-09-03T20:20:42Z`  
Last review: `2026-09-03T07:23:52Z`  
Pending: **9** item(s) -- 3 PASS, 6 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s), 0 ERROR manifest(s); 0 diagnostic self-route(s) flagged for adjudication

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_981_mech027_control_plane_pathological_modes_20260903T053044Z_v3` | 2026-09-03T05:30 | MECH-027 | — |
| `v3_exq_993_ext003_arc021_merged_channel_ablation_20260903T053340Z_v3` | 2026-09-03T05:33 | ARC-021, EXT-003, MECH-069 | — |
| `v3_exq_994_claim_probe_ext_007_consolidation_retention_20260903T053351Z_v3` | 2026-09-03T05:33 | EXT-007 | — |
| `v3_exq_978_sd018_directional_field_fishtank_20260903T111718Z_v3` | 2026-09-03T11:17 | INV-088, MECH-457 | — |
| `v3_exq_991_claim_probe_ext_004_residue_cross_context_penalty_20260903T122245Z_v3` | 2026-09-03T12:22 | EXT-004 | — |
| `v3_exq_983_ext002_residue_error_persistence_20260903T150005Z_v3` | 2026-09-03T15:00 | EXT-002 | — |

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_977_arc052_harm_stream_conditional_precision_20260903T112134Z_v3` | 2026-09-03T11:21 | ARC-052 |
| `v3_exq_951c_mech320_vt_floor_diagnostic_sd054_20260903T140538Z_v3` | 2026-09-03T14:05 | MECH-320 |
| `v3_exq_995_claim_probe_ext_005_causal_signature_20260903T194456Z_v3` | 2026-09-03T19:44 | EXT-005 |

---

## How to mark runs as reviewed

- PASS/FAIL runs (claim-tagged): add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Unclaimed manifests (PASS/FAIL, no claim tags): add the manifest stem (filename minus `.json`) to `discussed_experiment_dirs`
- ERROR manifests (crash-before-manifest / runner ERROR record): run `/diagnose-errors`, re-queue under a NEW letter, then add the manifest stem to `discussed_experiment_dirs`
- Diagnostic self-route flagged (`precondition_unmet` / `vacuous_pass`): adjudicate via `/failure-autopsy` before the label drives a governance action; clearing the run for review does not clear the adjudication flag (the manifest's `interpretation` is the source of truth -- a re-queued successor supersedes it).
- Diagnostic (`experiment_purpose: "diagnostic"`), no confirmed autopsy: ALL diagnostic PASS/FAIL results require a confirmed `/failure-autopsy` target before governance marks them reviewed -- not only ones the indexer flagged untrustworthy. Run `/failure-autopsy` (accepts a PASS target too), then mark reviewed once confirmed.
- Reviewed FAIL with no confirmed autopsy (blind-spot net): a claim-tagged, non-diagnostic FAIL that is already `reviewed` but was never autopsied. Run `/failure-autopsy` on it; the row clears automatically once a CONFIRMED autopsy target covers the run_id. Do NOT re-mark it reviewed to silence it (it is already reviewed -- that is the blind spot). Legacy such runs are grandfathered in `fail_autopsy_grandfather.json` and never listed; do not hand-edit that file.
- Recorded (non-gating) preconditions: nothing to clear. The run is reviewed and closed by the normal PASS/FAIL route above; the recorded finding is an audit trail to read alongside the result, not a flag to adjudicate.
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
