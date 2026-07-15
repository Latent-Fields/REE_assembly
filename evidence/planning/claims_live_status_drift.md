# Claims live_status Drift Report

Generated: 2026-07-15T13:34:54Z

Mirror of the closure-plan / claims-doc drift reports, for the claims registry's `live_status` status plane (SHP-4). Flags claims whose stored `live_status` block has fallen out of step with the value re-derived from the claim's own current fields (`status` + `v3_pending` + `epistemic_category`). Resolution + derivation are shared with `scripts/apply_live_status.py`. Only the **Reading drift** bucket is a hard signal (fails `--strict`); the rest are review/info hints.

Warn-only by default -- run with `--strict` for a blocking gate.

Claims in registry: 884

## Reading drift -- HARD (4)

Stored `live_status` != re-derived value. Re-run `scripts/apply_live_status.py`; if it persists, the block was hand-edited or the claim's fields changed without a re-stamp.

| claim | stored reading | derived reading | drifted fields |
|-------|----------------|-----------------|----------------|
| MECH-095 | `candidate/substrate_ceiling/v5-reassigned` | `candidate/substrate_ceiling` | reading: stored='candidate/substrate_ceiling/v5-reassigned' derived='candidate/substrate_ceiling' |
| INV-064 | `candidate/pending_substrate_reconfirmation` | `candidate` | reading: stored='candidate/pending_substrate_reconfirmation' derived='candidate' |
| INV-088 | `candidate/pending_substrate_reconfirmation` | `candidate` | reading: stored='candidate/pending_substrate_reconfirmation' derived='candidate' |
| MECH-456 | `provisional/substrate_conditional_satisfied (independent-seed replicated)` | `provisional/substrate_conditional` | reading: stored='provisional/substrate_conditional_satisfied (independent-seed replicated)' derived='provisional/substrate_conditional' |

## Unstamped -- SOFT (0)

Registered claims with no `live_status` block. Run `scripts/apply_live_status.py`.

_None._

## Internal inconsistency -- REVIEW (0)

Claims whose own current-state fields contradict each other (`needs_review` true): a promoted status still carrying the V3-pending gate, or a promoted status tagged `substrate_ceiling` (GOV-CEIL-1 floors ceilings to candidate). The derived `live_status` is a best-effort; a human should reconcile the fields.

_None._

## Event-provenance drift -- SOFT (11)

The `live_status.evidence` sub-block (SHP-4 augmentation: `from` / `as_of` / `verdict`) is projected from the append-only event log via project_status_head. This flags claims whose stored `evidence` block no longer matches the freshly re-projected head -- i.e. a newer autopsy / PASS manifest / decision landed (or one changed) since `apply_live_status.py` last ran. It fluctuates legitimately as the fleet produces evidence, so it is **warn-only and never a --strict failure**: re-run `scripts/apply_live_status.py` (under a TASK_CLAIMS claim on docs/claims/claims.yaml) to refresh. Reading drift (HARD, above) is the gate; provenance drift is a hint.

| claim | stored evidence.from | re-projected from |
|-------|----------------------|-------------------|
| MECH-046 | `v3_exq_473_sd035_cea_mode_prior_20260421T195533Z_v3` | `v3_exq_762_mech046_cea_mode_prior_context_conditioning_20260714T204708Z_v3` |
| MECH-092 | `decision:MECH-092@2026-03-29T21:16:41.333183Z` | `v3_exq_761_mech092_quiescent_replay_selectivity_20260714T204501Z_v3` |
| MECH-095 | `V3-EXQ-741` | `failure_autopsy_V3-EXQ-741_2026-07-12` |
| INV-064 | `failure_autopsy_V3-EXQ-740_2026-07-11` | `failure_autopsy_V3-EXQ-740a_2026-07-12` |
| INV-088 | `v3_exq_744a_inv088_world_goal_evaluator_dv_coupling_20260712T144028Z_v3` | `failure_autopsy_MECH-457-fanout-752-753-754_2026-07-15#V3-EXQ-754` |
| INV-089 | `v3_exq_746a_inv089_harm_eval_z_harm_calibrated_bound_v2_20260712T170011Z_v3` | `failure_autopsy_morning-digest-742-744a-745-746-746a_2026-07-13#V3-EXQ-746a` |
| MECH-456 | `V3-EXQ-733c` | `failure_autopsy_morning-digest-742-744a-745-746-746a_2026-07-13#V3-EXQ-745` |
| MECH-302 | `V3-EXQ-517d` | `failure_autopsy_V3-EXQ-517b_2026-05-30` |
| MECH-303 | `decision:MECH-303@2026-05-07T04:14:02Z` | `v3_exq_760_mech303_contextual_safety_terrain_discrimination_20260714T202728Z_v3` |
| MECH-304 | `decision:MECH-304@2026-07-14T20:39:20.788928Z` | `v3_exq_763_mech304_conditioned_inhibition_behavioural_falsifier_20260715T081944Z_v3` |
| MECH-457 | `v3_exq_747_748_749_mech457_fanout (GOV-FANOUT-1 discrimination portfolio, diagnostic)` | `failure_autopsy_MECH-457-fanout-752-753-754_2026-07-15#V3-EXQ-754` |

## Never reviewed (no `last_reviewed`) -- INFO (866 of 884)

Claims with no `last_reviewed` history value -- not yet reviewed under the history plane. `last_reviewed` is record-once and legitimately absent for most claims (seeded from `adjudicated_at_utc`, or set with `apply_live_status.py --mark-reviewed <ID>`). Count + sample only.

Sample: INV-001, INV-002, INV-003, INV-004, INV-005, INV-006, INV-007, INV-008, INV-009, INV-010, INV-011, INV-012, INV-013, INV-014, INV-015, INV-016, INV-017, ARC-001, ARC-002, ARC-004 ...

