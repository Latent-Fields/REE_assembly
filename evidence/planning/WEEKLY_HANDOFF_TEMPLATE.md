# Weekly Producer Handoff Template (v1)

Use this template for weekly producer handoffs from:

- `ree-v2` (qualification lane)
- `ree-experiments-lab` (stress lane)
- `ree-v1-minimal` (parity/backstop lane)

Recommended producer output path:

- `evidence/planning/weekly_handoff/latest.md`

---

## Required Fields and Sections

1. Metadata
- `week_of_utc` (date for cycle week start)
- `producer_repo`
- `producer_commit`
- `generated_utc`

2. Contract sync
- `ree_assembly_repo`
- `ree_assembly_commit`
- `contract_lock_path`
- `contract_lock_hash`
- `schema_version_set` (for example `experiment_pack/v1`, `jepa_adapter_signals/v1`)

3. CI gates
- `schema_validation` (`PASS|FAIL`)
- `seed_determinism` (`PASS|FAIL`)
- `hook_surface_coverage` (`PASS|FAIL|N/A`)
- `remote_export_import` (`PASS|FAIL|N/A`)

4. Run-pack inventory table (required columns)
- `experiment_type`
- `run_id`
- `seed`
- `condition_or_scenario`
- `status`
- `evidence_direction`
- `claim_ids_tested`
- `failure_signatures`
- `execution_mode` (`local|remote`)
- `compute_backend` (for example `local_cpu`, `cloud_gpu_a10g`)
- `runtime_minutes`
- `pack_path`

5. Claim summary table (required columns)
- `claim_id`
- `runs_added`
- `supports`
- `weakens`
- `mixed`
- `unknown`
- `recurring_failure_signatures`

6. Open blockers
- short list of blockers/risks affecting next cycle handoff

7. Local compute options watch (required for `ree-v2`, optional for other producers)
- `local_options_last_updated_utc`
- `rolling_3mo_cloud_spend_eur`
- `local_blocked_sessions_this_week`
- `recommended_local_action` (`hold_cloud_only|upgrade_low|upgrade_mid|upgrade_high`)
- short rationale tied to observed runtime/cost pressure

---

## Markdown Skeleton

```md
# Weekly Handoff - <producer_repo> - <week_of_utc>

## Metadata
- week_of_utc: `<YYYY-MM-DD>`
- producer_repo: `<repo-name>`
- producer_commit: `<git-sha>`
- generated_utc: `<RFC3339 UTC>`

## Contract Sync
- ree_assembly_repo: `REE_assembly`
- ree_assembly_commit: `<git-sha>`
- contract_lock_path: `<path>`
- contract_lock_hash: `<sha256>`
- schema_version_set: `<comma-separated versions>`

## CI Gates
| gate | status | evidence |
| --- | --- | --- |
| schema_validation | PASS | `<command or workflow run id>` |
| seed_determinism | PASS | `<command or workflow run id>` |
| hook_surface_coverage | PASS/N/A | `<command or workflow run id>` |
| remote_export_import | PASS/N/A | `<command or workflow run id>` |

## Run-Pack Inventory
| experiment_type | run_id | seed | condition_or_scenario | status | evidence_direction | claim_ids_tested | failure_signatures | execution_mode | compute_backend | runtime_minutes | pack_path |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |

## Claim Summary
| claim_id | runs_added | supports | weakens | mixed | unknown | recurring_failure_signatures |
| --- | --- | --- | --- | --- | --- | --- |
| ... | ... | ... | ... | ... | ... | ... |

## Open Blockers
- `<blocker 1>`
- `<blocker 2>`

## Local Compute Options Watch
- local_options_last_updated_utc: `<RFC3339 UTC or N/A>`
- rolling_3mo_cloud_spend_eur: `<number or N/A>`
- local_blocked_sessions_this_week: `<integer or N/A>`
- recommended_local_action: `<hold_cloud_only|upgrade_low|upgrade_mid|upgrade_high|N/A>`
- rationale: `<short decision rationale>`
```

---

## Validation Rules

- Do not omit required columns.
- Use stable claim IDs and failure signature IDs.
- Keep `evidence_direction` in `supports|weakens|mixed|unknown`.
- If a gate fails, explicitly mark it `FAIL` and include next action.
- For `ree-v2`, `Local Compute Options Watch` section is mandatory.
- For `ree-v2`, `recommended_local_action` should follow the hobby-mode thresholds in `docs/ops/local_compute_options.md` unless explicitly overridden with rationale.
