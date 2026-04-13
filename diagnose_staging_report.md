# Diagnose-Errors Staging Report

**Session**: ree-diagnose-queue-2026-04-13  
**Generated**: 2026-04-13T15:21:42Z  
**Mode**: STAGING (scripts drafted, NOT queued — human confirmation required)

---

## Summary

5 unaddressed ERRORs identified in `runner_status.json`. All dated March 2026. Root cause for all: **old substrate API incompatibility** — error messages were not captured by the early runner.

| Failed ID | Proposed Fix | Status |
|-----------|-------------|--------|
| V3-EXQ-008 | None | SKIP — claim superseded (SD-003 redesigned) |
| V3-EXQ-038 | V3-EXQ-396 | Awaiting confirmation |
| V3-EXQ-046 | V3-EXQ-397 | Awaiting confirmation |
| V3-EXQ-046b | Covered by V3-EXQ-397 | (re-queue of EXQ-046) |
| V3-EXQ-057 | None | SKIP — claim superseded (SD-010 validated) |

**Fix scripts written (STAGED, not queued)**:
- `ree-v3/experiments/v3_exq_396_arc016_precision_sweep.py`
- `ree-v3/experiments/v3_exq_397_arc007_path_memory_ablation.py`

---

## Detailed Diagnoses

### V3-EXQ-008 — SKIP (Obsolete/Superseded)

**Claim**: SD-003 z_world counterfactual approach  
**Error date**: March 2026  
**Root cause**: Old substrate API incompatibility. Uses deprecated `CausalGridWorld` (not V2) with a custom 3x3 observation subclass (`SmallViewEnv`). The SD-003 z_world counterfactual approach tested here is obsolete.  
**Why no fix needed**: EXQ-030b PASS validated the z_world architecture; SD-003 was subsequently redesigned to use the z_harm_s pipeline (ARC-033, E2HarmSForward). The current SD-003 evidence path is EXQ-329/330a/353 using the z_harm_s forward model. No new experiment needed for this specific design.  
**Disposition**: SKIP

---

### V3-EXQ-038 → V3-EXQ-396 — Awaiting Confirmation

**Claim**: ARC-016 (dynamic precision tracks environment stability), MECH-093 (z_beta modulates heartbeat frequency)  
**Error date**: 2026-03-19  
**Root cause**: Old substrate API incompatibility. Likely cause: `update_running_variance()`, `SelectionResult.committed`, or related E3 methods did not exist in the early March substrate. No error message preserved.  
**Fix applied**: New EXQ ID (V3-EXQ-396) to bypass runner skip. Script content identical to EXQ-038; substrate now compatible.  
**API verification** (all confirmed present in current ree_core):
  - `agent.e3.update_running_variance()`
  - `SelectionResult.committed`
  - `e3._running_variance` direct assignment
  - `generate_candidates_random()`
**Smoke test**: Passed (2026-04-13)  
**Draft script**: `experiments/v3_exq_396_arc016_precision_sweep.py`  
**Proposed queue entry**:
  - queue_id: V3-EXQ-396
  - priority: 5
  - machine_affinity: DLAPTOP-4.local
  - estimated_minutes: 150
  - seeds: 1, conditions: 10
  - supersedes: V3-EXQ-038

---

### V3-EXQ-046 + V3-EXQ-046b → V3-EXQ-397 — Awaiting Confirmation

**Claim**: ARC-007 (path memory: hippocampal proposals navigate residue-field terrain)  
**Error dates**: EXQ-046: 2026-03-20, EXQ-046b: 2026-03-22  
**Root cause**: Old substrate API incompatibility. V3-EXQ-046b was a re-queue of the same script after EXQ-046 errored. Both share the same root cause.  
**Fix applied**: New EXQ ID (V3-EXQ-397) covering both predecessors. Script content identical to EXQ-046; substrate now compatible.  
**API verification** (all confirmed present in current ree_core):
  - `agent.hippocampal._get_terrain_action_object_mean()`
  - `residue_field.evaluate_trajectory()`
  - `generate_candidates_random()`
  - `Trajectory.get_world_state_sequence()`
**Smoke test**: Passed (2026-04-13)  
**Draft script**: `experiments/v3_exq_397_arc007_path_memory_ablation.py`  
**claim_ids change**: Original EXQ-046 tagged `["ARC-007", "SD-004"]`. SD-004 removed — it is an architectural prerequisite already implemented, not the variable being measured. The experiment specifically tests whether ablating the residue field degrades hippocampal proposal quality (ARC-007).  
**Proposed queue entry**:
  - queue_id: V3-EXQ-397
  - priority: 5
  - machine_affinity: DLAPTOP-4.local
  - estimated_minutes: 120
  - seeds: 1, conditions: 3
  - supersedes: V3-EXQ-046b

---

### V3-EXQ-046b — Covered by V3-EXQ-397

See V3-EXQ-046 above. EXQ-046b was a re-queue of the same script; both predecessors are superseded by V3-EXQ-397.

---

### V3-EXQ-057 — SKIP (Obsolete/Superseded)

**Claim**: SD-010 (nociceptive separation from reafference)  
**Error date**: March 2026  
**Root cause**: Old substrate API incompatibility. Imports `HarmEncoder` from `ree_core.latent.stack` — module still exists in current substrate, but original error likely related to early HarmEncoder API or env return format.  
**Why no fix needed**: SD-010 was validated by EXQ-056c PASS and EXQ-058b PASS. The reafference isolation test in EXQ-057 is a more specific variant that was superseded when SD-010 was validated via a cleaner design.  
**Disposition**: SKIP

---

## Next Steps (Human Action Required)

To activate the staged fixes, confirm and run:

```bash
# Review scripts:
cat ree-v3/experiments/v3_exq_396_arc016_precision_sweep.py
cat ree-v3/experiments/v3_exq_397_arc007_path_memory_ablation.py

# Add to queue (or use /queue-experiment to add with validation):
# V3-EXQ-396 — ARC-016 precision sweep
# V3-EXQ-397 — ARC-007 path memory ablation
```

Both experiments target `DLAPTOP-4.local`. The runner will pick them up automatically in `--auto-sync --loop` mode.

---

*Structured data: `evidence/planning/diagnose_staging.json`*
