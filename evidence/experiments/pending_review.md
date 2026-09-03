# Pending Experiment Review

Generated: `2026-09-03T06:58:31Z`  
Last review: `2026-09-02T17:21:49Z`  
Pending: **10** item(s) -- 4 PASS, 6 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s), 0 ERROR manifest(s); 0 diagnostic self-route(s) flagged for adjudication

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_969_contextmemory_write_content_h2_operating_point_20260902T203931Z_v3` | 2026-09-02T20:39 | (no claim tags) | — |
| `v3_exq_970_contextmemory_write_content_h1_contrastive_loss_20260902T205703Z_v3` | 2026-09-02T20:57 | (no claim tags) | — |
| `v3_exq_971_contextmemory_write_content_h3_task_coupled_20260902T211117Z_v3` | 2026-09-02T21:11 | (no claim tags) | — |
| `v3_exq_981_mech027_control_plane_pathological_modes_20260903T053044Z_v3` | 2026-09-03T05:30 | MECH-027 | — |
| `v3_exq_993_ext003_arc021_merged_channel_ablation_20260903T053340Z_v3` | 2026-09-03T05:33 | ARC-021, EXT-003, MECH-069 | — |
| `v3_exq_994_claim_probe_ext_007_consolidation_retention_20260903T053351Z_v3` | 2026-09-03T05:33 | EXT-007 | — |

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_972_contextmemory_write_content_h4_input_distribution_20260902T211758Z_v3` | 2026-09-02T21:17 | (no claim tags) |
| `v3_exq_980_sd_e1_h1c_readout_regime_e1_alone_20260902T212300Z_v3` | 2026-09-02T21:23 | (no claim tags) |
| `v3_exq_982_claim_probe_ext_001_sycophancy_channel_separation_20260903T014226Z_v3` | 2026-09-03T01:42 | EXT-001 |
| `v3_exq_591h_isef005_phase01_gate_live_20260903T024528Z_v3` | 2026-09-03T02:45 | ARC-019 |

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
