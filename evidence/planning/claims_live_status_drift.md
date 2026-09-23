# Claims live_status Drift Report

Generated: 2026-09-23T17:48:25Z

Mirror of the closure-plan / claims-doc drift reports, for the claims registry's `live_status` status plane (SHP-4). Flags claims whose stored `live_status` block has fallen out of step with the value re-derived from the claim's own current fields (`status` + `v3_pending` + `epistemic_category`). Resolution + derivation are shared with `scripts/apply_live_status.py`. Only the **Reading drift** bucket is a hard signal (fails `--strict`); the rest are review/info hints.

Warn-only by default -- run with `--strict` for a blocking gate.

Claims in registry: 1185

## Reading drift -- HARD (11)

Stored `live_status` != re-derived value. Re-run `scripts/apply_live_status.py`; if it persists, the block was hand-edited or the claim's fields changed without a re-stamp.

| claim | stored reading | derived reading | drifted fields |
|-------|----------------|-----------------|----------------|
| MECH-037 | `provisional` | `candidate` | reading: stored='provisional' derived='candidate' |
| INV-063 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| SD-071 | `candidate` | `provisional` | reading: stored='candidate' derived='provisional' |
| GOV-UNWRITTEN-1 | `candidate/negative_pilot_no_skill` | `candidate` | reading: stored='candidate/negative_pilot_no_skill' derived='candidate' |
| ARC-149 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| MECH-575 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| MECH-576 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| MECH-577 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| MECH-578 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| MECH-579 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| MECH-580 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |

## Unstamped -- SOFT (11)

Registered claims with no `live_status` block. Run `scripts/apply_live_status.py`.

| claim | would-derive |
|-------|--------------|
| MECH-566 | `candidate/v3_pending` |
| MECH-567 | `candidate/v3_pending` |
| MECH-568 | `candidate/v3_pending` |
| MECH-572 | `candidate/v3_pending` |
| MECH-573 | `candidate/v3_pending` |
| MECH-574 | `candidate/v3_pending` |
| MECH-581 | `candidate/v3_pending/substrate_conditional` |
| MECH-582 | `candidate/v3_pending/substrate_conditional` |
| MECH-583 | `candidate/v3_pending` |
| MECH-584 | `candidate/v3_pending` |
| MECH-585 | `candidate/v3_pending/substrate_conditional` |

## Internal inconsistency -- REVIEW (2)

Claims whose own current-state fields contradict each other (`needs_review` true): a promoted status still carrying the V3-pending gate, or a promoted status tagged `substrate_ceiling` (GOV-CEIL-1 floors ceilings to candidate). The derived `live_status` is a best-effort; a human should reconcile the fields.

| claim | derived reading | why |
|-------|-----------------|-----|
| SD-016 | `implemented/substrate_ceiling` | promoted status 'implemented' but epistemic_category substrate_ceiling (GOV-CEIL-1 floors ceilings to candidate) |
| SD-017 | `stable/substrate_ceiling` | promoted status 'stable' but epistemic_category substrate_ceiling (GOV-CEIL-1 floors ceilings to candidate) |

## Event-provenance drift -- SOFT (62)

The `live_status.evidence` sub-block (SHP-4 augmentation: `from` / `as_of` / `verdict`) is projected from the append-only event log via project_status_head. This flags claims whose stored `evidence` block no longer matches the freshly re-projected head -- i.e. a newer autopsy / PASS manifest / decision landed (or one changed) since `apply_live_status.py` last ran. It fluctuates legitimately as the fleet produces evidence, so it is **warn-only and never a --strict failure**: re-run `scripts/apply_live_status.py` (under a TASK_CLAIMS claim on docs/claims/claims.yaml) to refresh. Reading drift (HARD, above) is the gate; provenance drift is a hint.

| claim | stored evidence.from | re-projected from |
|-------|----------------------|-------------------|
| MECH-018 | `_none_` | `decision:MECH-018@2026-09-18T19:04:17.464654Z` |
| MECH-019 | `_none_` | `decision:MECH-019@2026-09-18T19:04:17.506193Z` |
| MECH-021 | `_none_` | `failure_autopsy_V3-EXQ-1050_2026-09-18` |
| MECH-035 | `_none_` | `decision:MECH-035@2026-09-18T19:04:17.543781Z` |
| MECH-037 | `_none_` | `decision:MECH-037@2026-09-20T14:16:26.077350Z` |
| MECH-050 | `_none_` | `decision:MECH-050@2026-09-20T12:17:03.116022Z` |
| MECH-055 | `_none_` | `failure_autopsy_V3-EXQ-1062a_2026-09-23` |
| MECH-065 | `_none_` | `decision:MECH-065@2026-09-20T12:17:03.676535Z` |
| INV-024 | `_none_` | `v3_exq_1072_inv024_offline_online_isolation_audit_20260922T152522Z_v3` |
| MECH-079 | `_none_` | `decision:MECH-079@2026-09-23T09:24:25.106806Z` |
| MECH-080 | `_none_` | `decision:MECH-080@2026-09-23T09:24:25.160463Z` |
| INV-063 | `decision:INV-063@2026-09-08T15:30:04.464955Z` | `failure_autopsy_INV-063-1060-1063-1069-cluster_2026-09-20#V3-EXQ-1069` |
| ARC-054 | `decision:ARC-054@2026-09-11T16:54:08.598899Z` | `decision:ARC-054@2026-09-18T19:04:17.348743Z` |
| SD-032 | `_none_` | `decision:SD-032@2026-09-23T09:24:24.727105Z` |
| SD-033 | `_none_` | `decision:SD-033@2026-09-23T09:24:24.778721Z` |
| SD-033c | `_none_` | `decision:SD-033c@2026-09-23T09:24:24.832431Z` |
| SD-033d | `_none_` | `decision:SD-033d@2026-09-23T09:24:24.887020Z` |
| SD-038 | `_none_` | `decision:SD-038@2026-09-23T09:24:24.942314Z` |
| MECH-305 | `_none_` | `decision:MECH-305@2026-09-23T09:24:23.609382Z` |
| MECH-354 | `_none_` | `decision:MECH-354@2026-09-23T09:24:23.716179Z` |
| MECH-356 | `_none_` | `decision:MECH-356@2026-09-23T09:24:23.768098Z` |
| MECH-316 | `decision:MECH-316@2026-08-16T11:57:28.897709Z` | `decision:MECH-316@2026-09-20T14:16:26.207734Z` |
| MECH-317 | `decision:MECH-317@2026-08-16T11:57:28.937162Z` | `decision:MECH-317@2026-09-20T14:16:26.277428Z` |
| ARC-080 | `decision:ARC-080@2026-06-06T07:53:48.739107Z` | `decision:ARC-080@2026-09-23T09:24:23.343475Z` |
| ARC-083 | `decision:ARC-083@2026-06-06T07:53:48.739107Z` | `decision:ARC-083@2026-09-18T19:04:17.387476Z` |
| ARC-086 | `_none_` | `decision:ARC-086@2026-09-23T09:24:23.397475Z` |
| MECH-525 | `_none_` | `decision:MECH-525@2026-09-23T09:24:24.088931Z` |
| MECH-526 | `_none_` | `decision:MECH-526@2026-09-23T09:24:24.143336Z` |
| SD-080 | `failure_autopsy_V3-EXQ-1043_2026-09-17` | `failure_autopsy_V3-EXQ-1043b_2026-09-23` |
| SD-071 | `_none_` | `decision:SD-071@2026-09-20T12:17:02.529572Z` |
| MECH-423 | `failure_autopsy_V3-EXQ-1026_2026-09-14` | `failure_autopsy_INV-063-1060-1063-1069-cluster_2026-09-20#V3-EXQ-1060` |
| INV-086 | `failure_autopsy_V3-EXQ-1039a_2026-09-20` | `failure_autopsy_V3-EXQ-1075_2026-09-23` |
| MECH-426 | `_none_` | `decision:MECH-426@2026-09-23T09:24:23.821258Z` |
| MECH-428 | `failure_autopsy_V3-EXQ-1039a_2026-09-20` | `failure_autopsy_V3-EXQ-1075_2026-09-23` |
| MECH-430 | `_none_` | `decision:MECH-430@2026-09-23T09:24:23.873283Z` |
| MECH-439 | `failure_autopsy_V3-EXQ-1012a_2026-09-14` | `failure_autopsy_V3-EXQ-1039_2026-09-16` |
| MECH-441 | `decision:MECH-441@2026-06-27T10:54:49.591342Z` | `decision:MECH-441@2026-09-23T09:24:23.928589Z` |
| SD-081 | `_none_` | `decision:SD-081@2026-09-23T09:24:24.993828Z` |
| MECH-482 | `failure_autopsy_V3-EXQ-1047_2026-09-17` | `failure_autopsy_V3-EXQ-1047_2026-09-17` |
| SD-097 | `_none_` | `decision:SD-097@2026-09-23T09:24:25.045779Z` |
| SD-098 | `_none_` | `sd098_ghost_goal_readtime_rerank_20260918T182337Z_v3` |
| ARC-133 | `_none_` | `decision:ARC-133@2026-09-23T09:24:23.450317Z` |
| MECH-520 | `_none_` | `decision:MECH-520@2026-09-23T09:24:23.981986Z` |
| MECH-521 | `_none_` | `decision:MECH-521@2026-09-23T09:24:24.035872Z` |
| MECH-529 | `_none_` | `decision:MECH-529@2026-09-23T09:24:24.196288Z` |
| MECH-537 | `failure_autopsy_V3-EXQ-1043a_2026-09-20` | `failure_autopsy_V3-EXQ-1043b_2026-09-23` |
| MECH-539 | `_none_` | `decision:MECH-539@2026-09-23T09:24:24.302197Z` |
| ARC-140 | `_none_` | `decision:ARC-140@2026-09-23T09:24:23.502773Z` |
| ARC-142 | `_none_` | `decision:ARC-142@2026-09-23T09:24:23.555500Z` |
| MECH-545 | `_none_` | `decision:MECH-545@2026-09-23T09:24:24.410268Z` |
| MECH-547 | `failure_autopsy_V3-EXQ-1044_2026-09-17` | `failure_autopsy_V3-EXQ-1043b_2026-09-23` |
| MECH-548 | `failure_autopsy_V3-EXQ-1044_2026-09-17` | `failure_autopsy_V3-EXQ-1044_2026-09-17` |
| SD-106 | `failure_autopsy_V3-EXQ-1023a_2026-09-17` | `failure_autopsy_V3-EXQ-1043b_2026-09-23` |
| MECH-555 | `failure_autopsy_V3-EXQ-1043_2026-09-17` | `failure_autopsy_V3-EXQ-1043b_2026-09-23` |
| MECH-561 | `_none_` | `decision:MECH-561@2026-09-20T12:17:03.975416Z` |
| MECH-562 | `_none_` | `decision:MECH-562@2026-09-23T09:24:24.571621Z` |
| MECH-566 | `_none_` | `failure_autopsy_V3-EXQ-1065_2026-09-20` |
| MECH-572 | `_none_` | `failure_autopsy_V3-EXQ-1073_2026-09-22` |
| MECH-573 | `_none_` | `v3_exq_1079_sdppb10_alphaworld_operating_point_probe_20260923T172400Z_v3` |
| MECH-574 | `_none_` | `v3_exq_1079_sdppb10_alphaworld_operating_point_probe_20260923T172400Z_v3` |
| ... | | (+2 more) |

## Never reviewed (no `last_reviewed`) -- INFO (1164 of 1185)

Claims with no `last_reviewed` history value -- not yet reviewed under the history plane. `last_reviewed` is record-once and legitimately absent for most claims (seeded from `adjudicated_at_utc`, or set with `apply_live_status.py --mark-reviewed <ID>`). Count + sample only.

Sample: INV-001, INV-002, INV-003, INV-004, INV-005, INV-006, INV-007, INV-008, INV-009, INV-010, INV-011, INV-012, INV-013, INV-014, INV-015, INV-016, INV-017, ARC-001, ARC-002, ARC-004 ...

