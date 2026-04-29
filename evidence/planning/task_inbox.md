# Task Inbox

Use this as the low-friction capture surface.

- Add new work as `- [ ] task`.
- Mark complete as `- [x] task` (exact same text).
- `run_governance_cycle.py` syncs this file into `manual_carryover_items.v1.json` automatically.
- Completed checkbox lines are removed automatically on sync (use `--no-prune-completed` to keep them).

## Tasks

- Add tasks below this line using checkbox format.

- [ ] Queue V3-EXQ-325e (SD-032c AIC drive-dependence, supersedes V3-EXQ-325d) once V3-EXQ-476 passes and the MECH-269 V_s invalidation circuit is validated end-to-end. Action: flip `VS_CIRCUIT_READY=True` in `ree-v3/experiments/v3_exq_325e_sd032c_aic_drive_dependence.py`, then add a queue entry (claim_ids=[SD-032c, SD-021], experiment_purpose=evidence, supersedes=v3_exq_325d_sd032c_aic_descending_modulation, estimated_minutes=~240, machine_affinity=any). Reason for gate: without V_s-driven mode-switch variation, the MECH-090 bistable commit latch keeps the agent committed for every eval tick and `safe_ratio` returns the 1.0 empty-uncommitted fallback, making C1/C4b untestable. Root-cause diagnosis of EXQ-325d bit-identical `aic_salience_mean` is documented in the new script's docstring (drive_level never fed into `update_z_goal`; single-ablation arm hit both AIC knobs simultaneously; urgency threshold unreachable pre-V_s).
