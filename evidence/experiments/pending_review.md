# Pending Experiment Review

Generated: `2026-06-22T04:18:22Z`  
Last review: `2026-06-21T19:26:04Z`  
Pending: **5** item(s) -- 3 PASS, 2 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s), 0 ERROR manifest(s); 0 diagnostic self-route(s) flagged for adjudication

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_485k_sd033b_demotion_devalued_rerank_behavioural_20260621T192541Z_v3` | 2026-06-21T19:25 | MECH-263, SD-033b | — |
| `v3_exq_654i_arc062_gapb_rule_apprehension_behavioural_falsifier_20260622T014706Z_v3` | 2026-06-22T01:47 | ARC-062, MECH-309 | — |

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_689f_nogo_necessity_falsifier_20260621T200543Z_v3` | 2026-06-21T20:05 | ARC-107, MECH-449 |
| `v3_exq_689g_mech449_go_nogo_conversion_falsifier_20260621T205542Z_v3` | 2026-06-21T20:55 | ARC-107, MECH-449 |
| `v3_exq_689e_mech448_channel_adaptive_envelope_readiness_20260621T224206Z_v3` | 2026-06-21T22:42 | (no claim tags) |

---

## How to mark runs as reviewed

- PASS/FAIL runs (claim-tagged): add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Unclaimed manifests (PASS/FAIL, no claim tags): add the manifest stem (filename minus `.json`) to `discussed_experiment_dirs`
- ERROR manifests (crash-before-manifest / runner ERROR record): run `/diagnose-errors`, re-queue under a NEW letter, then add the manifest stem to `discussed_experiment_dirs`
- Diagnostic self-route flagged (`precondition_unmet` / `vacuous_pass`): adjudicate via `/failure-autopsy` before the label drives a governance action; clearing the run for review does not clear the adjudication flag (the manifest's `interpretation` is the source of truth -- a re-queued successor supersedes it).
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
