# Pending Experiment Review

Generated: `2026-06-10T04:19:35Z`  
Last review: `2026-06-09T21:00:13Z`  
Pending: **5** item(s) -- 2 PASS, 3 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 0 unclaimed manifest(s); 0 diagnostic self-route(s) flagged for adjudication

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_569f_gapa_e2wf_matched_entropy_falsifier_20260610T001255Z_v3` | 2026-06-10T00:12 | ARC-065 | — |
| `v3_exq_661_mech294_compose_coherence_behavioural_readiness_20260610T002349Z_v3` | 2026-06-10T00:23 | (no claim tags) | — |
| `v3_exq_654a_arc062_gapb_rule_apprehension_behavioural_falsifier_20260610T004025Z_v3` | 2026-06-10T00:40 | ARC-062, MECH-309 | — |

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_485d_sd033b_ofc_trainable_head_readiness_20260610T003756Z_v3` | 2026-06-10T00:37 | (no claim tags) |
| `v3_exq_588c_mech189_super_ordinal_seeding_20260610T004619Z_v3` | 2026-06-10T00:46 | MECH-189 |

---

## How to mark runs as reviewed

- PASS/FAIL runs (claim-tagged): add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Unclaimed manifests (PASS/FAIL, no claim tags): add the manifest stem (filename minus `.json`) to `discussed_experiment_dirs`
- Diagnostic self-route flagged (`precondition_unmet` / `vacuous_pass`): adjudicate via `/failure-autopsy` before the label drives a governance action; clearing the run for review does not clear the adjudication flag (the manifest's `interpretation` is the source of truth -- a re-queued successor supersedes it).
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
