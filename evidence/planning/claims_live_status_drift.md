# Claims live_status Drift Report

Generated: 2026-09-24T06:05:14Z

Mirror of the closure-plan / claims-doc drift reports, for the claims registry's `live_status` status plane (SHP-4). Flags claims whose stored `live_status` block has fallen out of step with the value re-derived from the claim's own current fields (`status` + `v3_pending` + `epistemic_category`). Resolution + derivation are shared with `scripts/apply_live_status.py`. Only the **Reading drift** bucket is a hard signal (fails `--strict`); the rest are review/info hints.

Warn-only by default -- run with `--strict` for a blocking gate.

Claims in registry: 1186

## Reading drift -- HARD (2)

Stored `live_status` != re-derived value. Re-run `scripts/apply_live_status.py`; if it persists, the block was hand-edited or the claim's fields changed without a re-stamp.

| claim | stored reading | derived reading | drifted fields |
|-------|----------------|-----------------|----------------|
| MECH-038 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| MECH-125 | `candidate/substrate_conditional` | `candidate` | reading: stored='candidate/substrate_conditional' derived='candidate' |

## Unstamped -- SOFT (1)

Registered claims with no `live_status` block. Run `scripts/apply_live_status.py`.

| claim | would-derive |
|-------|--------------|
| ARC-150 | `candidate/substrate_conditional` |

## Internal inconsistency -- REVIEW (2)

Claims whose own current-state fields contradict each other (`needs_review` true): a promoted status still carrying the V3-pending gate, or a promoted status tagged `substrate_ceiling` (GOV-CEIL-1 floors ceilings to candidate). The derived `live_status` is a best-effort; a human should reconcile the fields.

| claim | derived reading | why |
|-------|-----------------|-----|
| SD-016 | `implemented/substrate_ceiling` | promoted status 'implemented' but epistemic_category substrate_ceiling (GOV-CEIL-1 floors ceilings to candidate) |
| SD-017 | `stable/substrate_ceiling` | promoted status 'stable' but epistemic_category substrate_ceiling (GOV-CEIL-1 floors ceilings to candidate) |

## Event-provenance drift -- SOFT (22)

The `live_status.evidence` sub-block (SHP-4 augmentation: `from` / `as_of` / `verdict`) is projected from the append-only event log via project_status_head. This flags claims whose stored `evidence` block no longer matches the freshly re-projected head -- i.e. a newer autopsy / PASS manifest / decision landed (or one changed) since `apply_live_status.py` last ran. It fluctuates legitimately as the fleet produces evidence, so it is **warn-only and never a --strict failure**: re-run `scripts/apply_live_status.py` (under a TASK_CLAIMS claim on docs/claims/claims.yaml) to refresh. Reading drift (HARD, above) is the gate; provenance drift is a hint.

| claim | stored evidence.from | re-projected from |
|-------|----------------------|-------------------|
| ARC-023 | `failure_autopsy_V3-EXQ-942_2026-08-21` | `failure_autopsy_V3-EXQ-942_reread_2026-09-23` |
| ARC-148 | `_none_` | `failure_autopsy_V3-EXQ-942_reread_2026-09-23` |
| MECH-091 | `failure_autopsy_V3-EXQ-944_2026-08-22` | `failure_autopsy_V3-EXQ-942_reread_2026-09-23` |
| SD-006 | `failure_autopsy_V3-EXQ-942_2026-08-21` | `failure_autopsy_V3-EXQ-942_reread_2026-09-23` |
| SD-008 | `failure_autopsy_grandfathered-sd003-cluster_2026-08-08` | `failure_autopsy_V3-EXQ-1079_2026-09-23` |
| INV-063 | `failure_autopsy_INV-063-1060-1063-1069-cluster_2026-09-20#V3-EXQ-1069` | `failure_autopsy_V3-EXQ-1079_2026-09-23` |
| INV-069 | `_none_` | `v3_exq_1078_inv069_zself_coherence_unsettled_20260923T182046Z_v3` |
| ARC-065 | `failure_autopsy_substrate-readiness-cluster_2026-09-02` | `failure_autopsy_MECH-320-defect-cluster_2026-09-23#V3-EXQ-544a` |
| MECH-313 | `failure_autopsy_substrate-readiness-cluster_2026-09-02` | `failure_autopsy_MECH-320-defect-cluster_2026-09-23#V3-EXQ-544a` |
| ARC-068 | `failure_autopsy_V3-EXQ-603g-624c-651a_2026-06-07#V3-EXQ-624c` | `failure_autopsy_MECH-320-defect-cluster_2026-09-23#ARC-068-claim-level` |
| ARC-070 | `failure_autopsy_V3-EXQ-938_2026-08-20` | `failure_autopsy_MECH-320-defect-cluster_2026-09-23#V3-EXQ-904` |
| MECH-321 | `failure_autopsy_V3-EXQ-938_2026-08-20` | `failure_autopsy_MECH-320-defect-cluster_2026-09-23#V3-EXQ-919` |
| INV-086 | `failure_autopsy_V3-EXQ-1039a_2026-09-20` | `failure_autopsy_V3-EXQ-1075_2026-09-23` |
| MECH-428 | `failure_autopsy_V3-EXQ-1039a_2026-09-20` | `failure_autopsy_V3-EXQ-1075_2026-09-23` |
| MECH-439 | `failure_autopsy_V3-EXQ-1012a_2026-09-14` | `failure_autopsy_V3-EXQ-1039_2026-09-16` |
| GOV-FROZEN-1 | `_none_` | `failure_autopsy_GFLAG-0404-govfrozen-control_2026-09-23` |
| MECH-547 | `failure_autopsy_V3-EXQ-1044_2026-09-17` | `failure_autopsy_V3-EXQ-1043b_2026-09-23` |
| SD-106 | `failure_autopsy_V3-EXQ-1023a_2026-09-17` | `failure_autopsy_V3-EXQ-1043b_2026-09-23` |
| MECH-572 | `failure_autopsy_V3-EXQ-1073_2026-09-22` | `failure_autopsy_V3-EXQ-1079_2026-09-23` |
| MECH-573 | `v3_exq_1079_sdppb10_alphaworld_operating_point_probe_20260923T172400Z_v3` | `failure_autopsy_V3-EXQ-1079_2026-09-23` |
| MECH-574 | `v3_exq_1079_sdppb10_alphaworld_operating_point_probe_20260923T172400Z_v3` | `failure_autopsy_V3-EXQ-1079_2026-09-23` |
| MECH-582 | `v3_exq_1079_sdppb10_alphaworld_operating_point_probe_20260923T172400Z_v3` | `failure_autopsy_V3-EXQ-1079_2026-09-23` |

## Never reviewed (no `last_reviewed`) -- INFO (1165 of 1186)

Claims with no `last_reviewed` history value -- not yet reviewed under the history plane. `last_reviewed` is record-once and legitimately absent for most claims (seeded from `adjudicated_at_utc`, or set with `apply_live_status.py --mark-reviewed <ID>`). Count + sample only.

Sample: INV-001, INV-002, INV-003, INV-004, INV-005, INV-006, INV-007, INV-008, INV-009, INV-010, INV-011, INV-012, INV-013, INV-014, INV-015, INV-016, INV-017, ARC-001, ARC-002, ARC-004 ...

