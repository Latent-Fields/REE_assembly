# Claims live_status Drift Report

Generated: 2026-07-18T04:54:30Z

Mirror of the closure-plan / claims-doc drift reports, for the claims registry's `live_status` status plane (SHP-4). Flags claims whose stored `live_status` block has fallen out of step with the value re-derived from the claim's own current fields (`status` + `v3_pending` + `epistemic_category`). Resolution + derivation are shared with `scripts/apply_live_status.py`. Only the **Reading drift** bucket is a hard signal (fails `--strict`); the rest are review/info hints.

Warn-only by default -- run with `--strict` for a blocking gate.

Claims in registry: 889

## Reading drift -- HARD (5)

Stored `live_status` != re-derived value. Re-run `scripts/apply_live_status.py`; if it persists, the block was hand-edited or the claim's fields changed without a re-stamp.

| claim | stored reading | derived reading | drifted fields |
|-------|----------------|-----------------|----------------|
| MECH-095 | `candidate/substrate_ceiling/v5-reassigned` | `candidate/substrate_ceiling` | reading: stored='candidate/substrate_ceiling/v5-reassigned' derived='candidate/substrate_ceiling' |
| MECH-180 | `candidate/v3_pending` | `candidate/v3_pending/substrate_ceiling` | reading: stored='candidate/v3_pending' derived='candidate/v3_pending/substrate_ceiling' |
| INV-064 | `candidate/pending_substrate_reconfirmation` | `candidate` | reading: stored='candidate/pending_substrate_reconfirmation' derived='candidate' |
| INV-088 | `candidate/pending_substrate_reconfirmation` | `candidate` | reading: stored='candidate/pending_substrate_reconfirmation' derived='candidate' |
| MECH-456 | `provisional/substrate_conditional_satisfied (independent-seed replicated)` | `provisional/substrate_conditional` | reading: stored='provisional/substrate_conditional_satisfied (independent-seed replicated)' derived='provisional/substrate_conditional' |

## Unstamped -- SOFT (0)

Registered claims with no `live_status` block. Run `scripts/apply_live_status.py`.

_None._

## Internal inconsistency -- REVIEW (0)

Claims whose own current-state fields contradict each other (`needs_review` true): a promoted status still carrying the V3-pending gate, or a promoted status tagged `substrate_ceiling` (GOV-CEIL-1 floors ceilings to candidate). The derived `live_status` is a best-effort; a human should reconcile the fields.

_None._

## Event-provenance drift -- SOFT (22)

The `live_status.evidence` sub-block (SHP-4 augmentation: `from` / `as_of` / `verdict`) is projected from the append-only event log via project_status_head. This flags claims whose stored `evidence` block no longer matches the freshly re-projected head -- i.e. a newer autopsy / PASS manifest / decision landed (or one changed) since `apply_live_status.py` last ran. It fluctuates legitimately as the fleet produces evidence, so it is **warn-only and never a --strict failure**: re-run `scripts/apply_live_status.py` (under a TASK_CLAIMS claim on docs/claims/claims.yaml) to refresh. Reading drift (HARD, above) is the gate; provenance drift is a hint.

| claim | stored evidence.from | re-projected from |
|-------|----------------------|-------------------|
| MECH-046 | `v3_exq_762_mech046_cea_mode_prior_context_conditioning_20260714T204708Z_v3` | `decision:MECH-046@2026-07-15T13:44:33.349339Z` |
| MECH-076 | `_none_` | `v3_exq_773_mech076_residue_basin_geometry_doseresponse_20260717T160046Z_v3` |
| MECH-086 | `_none_` | `v3_exq_775_mech086_selection_gain_dose_response_20260717T152037Z_v3` |
| MECH-095 | `V3-EXQ-741` | `failure_autopsy_V3-EXQ-741_2026-07-12` |
| INV-047 | `_none_` | `v3_exq_sd068_consolidation_staging_power_diagnostic_20260717T163507Z_v3` |
| MECH-168 | `_none_` | `v3_exq_sd068_consolidation_staging_power_diagnostic_20260717T163507Z_v3` |
| MECH-169 | `_none_` | `v3_exq_sd068_consolidation_staging_power_diagnostic_20260717T163507Z_v3` |
| MECH-173 | `_none_` | `failure_autopsy_V3-EXQ-774_2026-07-17` |
| INV-064 | `failure_autopsy_V3-EXQ-740_2026-07-11` | `failure_autopsy_V3-EXQ-740a_2026-07-12` |
| INV-088 | `v3_exq_744a_inv088_world_goal_evaluator_dv_coupling_20260712T144028Z_v3` | `failure_autopsy_MECH-457-fanout-752-753-754_2026-07-15#V3-EXQ-754` |
| INV-089 | `v3_exq_743_inv089_harm_evaluator_z_harm_bounded_20260712T124006Z_v3` | `failure_autopsy_INV-089-INV-090-wellposedness_2026-07-16` |
| INV-090 | `_none_` | `failure_autopsy_INV-089-INV-090-wellposedness_2026-07-16` |
| SD-025 | `_none_` | `failure_autopsy_V3-EXQ-767a_2026-07-17` |
| MECH-232 | `_none_` | `failure_autopsy_V3-EXQ-766a_2026-07-16` |
| ARC-057 | `_none_` | `failure_autopsy_V3-EXQ-768a_2026-07-17` |
| MECH-456 | `V3-EXQ-733c` | `failure_autopsy_morning-digest-742-744a-745-746-746a_2026-07-13#V3-EXQ-745` |
| MECH-279 | `_none_` | `v3_exq_776_mech279_pag_freeze_gate_functional_signature_20260717T153724Z_v3` |
| MECH-302 | `V3-EXQ-517d` | `failure_autopsy_V3-EXQ-517b_2026-05-30` |
| SD-068 | `_none_` | `v3_exq_sd068_consolidation_staging_power_diagnostic_20260717T163507Z_v3` |
| MECH-423 | `v3_exq_680e_mech423_superadditivity_ablation_20260716T155711Z_v3` | `failure_autopsy_V3-EXQ-680d_2026-06-15` |
| MECH-457 | `v3_exq_747_748_749_mech457_fanout (GOV-FANOUT-1 discrimination portfolio, diagnostic)` | `failure_autopsy_MECH-457-fanout-770-771-772_2026-07-18#V3-EXQ-772` |
| MECH-458 | `V3-EXQ-767a + V3-EXQ-768a (both cloud PASS, non-degenerate) + re-analysis probe scratchpad/probe1_sd025_force_decomposition.py` | `_none_` |

## Never reviewed (no `last_reviewed`) -- INFO (871 of 889)

Claims with no `last_reviewed` history value -- not yet reviewed under the history plane. `last_reviewed` is record-once and legitimately absent for most claims (seeded from `adjudicated_at_utc`, or set with `apply_live_status.py --mark-reviewed <ID>`). Count + sample only.

Sample: INV-001, INV-002, INV-003, INV-004, INV-005, INV-006, INV-007, INV-008, INV-009, INV-010, INV-011, INV-012, INV-013, INV-014, INV-015, INV-016, INV-017, ARC-001, ARC-002, ARC-004 ...

