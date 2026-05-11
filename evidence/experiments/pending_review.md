# Pending Experiment Review

Generated: `2026-05-11T04:18:09Z`  
Last review: `2026-05-10T12:51:30Z`  
Pending: **9** item(s) -- 0 PASS, 2 FAIL, 2 runner-only (ERROR/UNKNOWN/smoke), 5 unclaimed manifest(s)

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_141c_mech111_novelty_drive_measurement_fix_20260510T164545Z_v3` | 2026-05-10T16:45 | MECH-111 | — |
| `v3_exq_543b_arc062_phase3_optimized_falsifier_20260510T172558Z_v3` | 2026-05-10T17:25 | ARC-062, MECH-309, SD-029 | — |

## Unclaimed manifests (PASS/FAIL with no claim tags)

These manifests are on disk with PASS/FAIL but their run_id is absent from `claim_evidence.v1.json`. Common causes: substrate-readiness or environment-probe diagnostics that intentionally tag no claims, or runs the runner mis-logged as ERROR/UNKNOWN while the manifest landed cleanly. Mark discussed by adding the **manifest stem** (filename minus `.json`) to `discussed_experiment_dirs` -- queue_id-level marking is unsafe here, see header docstring.

| Result | Manifest stem | Experiment type | Queue ID | Direction |
|--------|---------------|-----------------|----------|-----------|
| PASS | `v3_exq_545_mech314_structured_curiosity_substrate_readiness_v3_20260510T164550Z` | v3_exq_545_mech314_structured_curiosity_substrate_readiness | ? | supports |
| PASS | `v3_exq_546_mech319_simulation_mode_rule_gate_substrate_readiness_v3_20260510T164557Z` | v3_exq_546_mech319_simulation_mode_rule_gate_substrate_readiness | ? | supports |
| PASS | `v3_exq_545_mech314_structured_curiosity_substrate_readiness_v3_20260510T172604Z` | v3_exq_545_mech314_structured_curiosity_substrate_readiness | ? | supports |
| PASS | `v3_exq_546_mech319_simulation_mode_rule_gate_substrate_readiness_v3_20260510T172610Z` | v3_exq_546_mech319_simulation_mode_rule_gate_substrate_readiness | ? | supports |
| PASS | `v3_exq_547_mech320_tonic_vigor_substrate_readiness_v3_20260510T205612Z` | v3_exq_547_mech320_tonic_vigor_substrate_readiness | ? | supports |

## Needs discussion (ERROR / UNKNOWN / smoke)

These entries completed in the runner but have no indexed result file (ERROR/UNKNOWN) or are onboarding smoke runs. They must be discussed and then added to `discussed_experiment_dirs` in review_tracker.json.

| Queue ID | Result | Script | Notes |
|----------|--------|--------|-------|
| `V3-EXQ-545` | PASS | `?` | PASS (index stale — run build_experiment_indexes.py) |
| `V3-EXQ-546` | PASS | `?` | PASS (index stale — run build_experiment_indexes.py) |

---

## How to mark runs as reviewed

- PASS/FAIL runs (claim-tagged): add run IDs to `reviewed_run_ids` in review_tracker.json
- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json
- Unclaimed manifests (PASS/FAIL, no claim tags): add the manifest stem (filename minus `.json`) to `discussed_experiment_dirs`
- Update `last_review_utc`, then re-run this script to confirm the list clears.

```bash
python scripts/generate_pending_review.py
```
