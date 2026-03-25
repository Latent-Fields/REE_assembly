# Pending Experiment Review

Generated: `2026-03-25T06:09:15Z`  
Last review: `2026-03-24T21:30:00Z`  
Pending: **4** item(s) -- 2 PASS, 2 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke)

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_095_harm_forward_model_sd003_20260325T021349Z_v3` | 2026-03-25T02:13 | ARC-033, SD-003, SD-011 | — |
| `v3_exq_096_full_integration_benchmark_20260325T050529Z_v3` | 2026-03-25T05:05 | ARC-007, ARC-016, MECH-089, MECH-090, MECH-093, MECH-094, SD-005, SD-006 | — |

## PASS (verify & close)

| Run ID | Timestamp | Claims |
|--------|-----------|--------|
| `v3_exq_047k_tpj_routing_larger_n_20260325T021558Z_v3` | 2026-03-25T02:15 | MECH-095, SD-005 |
| `v3_exq_096a_full_integration_benchmark_20260325T055416Z_v3` | 2026-03-25T05:54 | ARC-007, ARC-016, MECH-089, MECH-090, MECH-093, MECH-094, SD-005, SD-006 |

---

## How to mark runs as reviewed

- PASS/FAIL runs: add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
