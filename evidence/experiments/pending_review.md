# Pending Experiment Review

Generated: `2026-09-09T09:07:51Z`  
Last review: `2026-09-09T02:18:08Z`  
Pending: **4** item(s) -- 0 PASS, 3 FAIL, 0 runner-only (ERROR/UNKNOWN/smoke), 1 unclaimed manifest(s), 0 ERROR manifest(s); 0 diagnostic self-route(s) flagged for adjudication; 3 evidence PASS/FAIL flagged degenerate (route to /failure-autopsy)

## FAIL (action required)

| Run ID | Timestamp | Claims | Failure signatures |
|--------|-----------|--------|--------------------|
| `v3_exq_999a_mech161_vigilance_inverted_u_heartbeat_20260909T054013Z_v3` | 2026-09-09T05:40 | MECH-161 | — |
| `v3_exq_1017_inv104_arc138_regulatory_anchoring_matched_aux_20260909T054654Z_v3` | 2026-09-09T05:46 | ARC-138, INV-104 | — |
| `v3_exq_981a_mech027_control_plane_pathological_modes_20260909T061022Z_v3` | 2026-09-09T06:10 | MECH-027 | — |

## Evidence PASS/FAIL flagged degenerate (route to /failure-autopsy)

These `experiment_purpose: "evidence"` results carry a manifest-level `non_degenerate: false` (or a `false` entry in `non_degenerate_per_claim`) -- the driver's own pre-registered non-degeneracy check on its load-bearing criterion failed. The indexer already excludes them from scoring (`scoring_excluded: "degenerate"`), but nothing else routes them for review: `_compute_adjudication` only fires for `experiment_purpose` in {diagnostic, baseline}, so an evidence-purpose degenerate PASS/FAIL sails into the plain PASS/FAIL table above with no flag (confirmed: V3-EXQ-1007). **Route to `/failure-autopsy` (it accepts a PASS target too); do not verify-and-close.**

| Run ID | Status | Claims | Degeneracy reason |
|--------|--------|--------|--------------------|
| `v3_exq_999a_mech161_vigilance_inverted_u_heartbeat_20260909T054013Z_v3` | FAIL | MECH-161 | readiness agent_starves_safe_bin |
| `v3_exq_1017_inv104_arc138_regulatory_anchoring_matched_aux_20260909T054654Z_v3` | FAIL | ARC-138, INV-104 | p0a_objective_invisible_to_adapter_dv |
| `v3_exq_981a_mech027_control_plane_pathological_modes_20260909T061022Z_v3` | FAIL | MECH-027 | gate_a_unmet: positive_control_hazard_sensitivity |

## Unclaimed manifests (PASS/FAIL with no claim tags)

These manifests are on disk with PASS/FAIL but their run_id is absent from `claim_evidence.v1.json`. Common causes: substrate-readiness or environment-probe diagnostics that intentionally tag no claims, or runs the runner mis-logged as ERROR/UNKNOWN while the manifest landed cleanly. Mark discussed by adding the **manifest stem** (filename minus `.json`) to `discussed_experiment_dirs` -- queue_id-level marking is unsafe here, see header docstring.

| Result | Manifest stem | Experiment type | Queue ID | Direction |
|--------|---------------|-----------------|----------|-----------|
| PASS | `_dry_v3_exq_918a_sd_residue_valence_bound_validation_20260909T062139Z_v3` | v3_exq_918a_sd_residue_valence_bound_validation | ? | supports |

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
