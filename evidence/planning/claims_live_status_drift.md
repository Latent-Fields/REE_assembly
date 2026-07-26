# Claims live_status Drift Report

Generated: 2026-07-26T15:40:00Z

Mirror of the closure-plan / claims-doc drift reports, for the claims registry's `live_status` status plane (SHP-4). Flags claims whose stored `live_status` block has fallen out of step with the value re-derived from the claim's own current fields (`status` + `v3_pending` + `epistemic_category`). Resolution + derivation are shared with `scripts/apply_live_status.py`. Only the **Reading drift** bucket is a hard signal (fails `--strict`); the rest are review/info hints.

Warn-only by default -- run with `--strict` for a blocking gate.

Claims in registry: 939

## Reading drift -- HARD (10)

Stored `live_status` != re-derived value. Re-run `scripts/apply_live_status.py`; if it persists, the block was hand-edited or the claim's fields changed without a re-stamp.

| claim | stored reading | derived reading | drifted fields |
|-------|----------------|-----------------|----------------|
| ARC-007 | `active` | `provisional` | reading: stored='active' derived='provisional' |
| ARC-018 | `active` | `provisional` | reading: stored='active' derived='provisional' |
| Q-020 | `resolved` | `candidate` | reading: stored='resolved' derived='candidate' |
| MECH-314b | `candidate_substrate_landed` | `candidate_substrate_landed/substrate_ceiling` | reading: stored='candidate_substrate_landed' derived='candidate_substrate_landed/substrate_ceiling' |
| MECH-314c | `candidate_substrate_landed` | `candidate_substrate_landed/substrate_ceiling` | reading: stored='candidate_substrate_landed' derived='candidate_substrate_landed/substrate_ceiling' |
| Q-044 | `open` | `open/substrate_ceiling` | reading: stored='open' derived='open/substrate_ceiling' |
| MECH-448 | `provisional` | `candidate` | reading: stored='provisional' derived='candidate' |
| MECH-477 | `candidate/v3_pending` | `candidate` | reading: stored='candidate/v3_pending' derived='candidate' |
| MECH-478 | `candidate/v3_pending` | `candidate/v3_pending/substrate_conditional` | reading: stored='candidate/v3_pending' derived='candidate/v3_pending/substrate_conditional' |
| MECH-479 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |

## Unstamped -- SOFT (2)

Registered claims with no `live_status` block. Run `scripts/apply_live_status.py`.

| claim | would-derive |
|-------|--------------|
| MECH-464 | `candidate` |
| MECH-465 | `candidate/substrate_conditional` |

## Internal inconsistency -- REVIEW (0)

Claims whose own current-state fields contradict each other (`needs_review` true): a promoted status still carrying the V3-pending gate, or a promoted status tagged `substrate_ceiling` (GOV-CEIL-1 floors ceilings to candidate). The derived `live_status` is a best-effort; a human should reconcile the fields.

_None._

## Event-provenance drift -- SOFT (57)

The `live_status.evidence` sub-block (SHP-4 augmentation: `from` / `as_of` / `verdict`) is projected from the append-only event log via project_status_head. This flags claims whose stored `evidence` block no longer matches the freshly re-projected head -- i.e. a newer autopsy / PASS manifest / decision landed (or one changed) since `apply_live_status.py` last ran. It fluctuates legitimately as the fleet produces evidence, so it is **warn-only and never a --strict failure**: re-run `scripts/apply_live_status.py` (under a TASK_CLAIMS claim on docs/claims/claims.yaml) to refresh. Reading drift (HARD, above) is the gate; provenance drift is a hint.

| claim | stored evidence.from | re-projected from |
|-------|----------------------|-------------------|
| ARC-003 | `decision:ARC-003@2026-02-25T16:56:17.901452Z` | `failure_autopsy_backlog_2026-07-24#V3-EXQ-804` |
| ARC-005 | `_none_` | `failure_autopsy_backlog_2026-07-24#V3-EXQ-802` |
| ARC-007 | `decision:ARC-007@2026-03-16T18:20:19.360735Z` | `failure_autopsy_backlog_2026-07-24#V3-EXQ-800` |
| ARC-016 | `v3_exq_818_arc016_eval_derived_noise_precision_sweep_20260725T185821Z_v3` | `failure_autopsy_backlog_2026-07-24#V3-EXQ-805` |
| ARC-018 | `decision:ARC-018@2026-03-16T18:20:19.361124Z` | `failure_autopsy_backlog_2026-07-24#V3-EXQ-801` |
| MECH-048 | `_none_` | `failure_autopsy_backlog_2026-07-24#V3-EXQ-799` |
| Q-020 | `decision:Q-020@2026-04-10T18:06:06.975132Z` | `decision:Q-020@2026-07-25T16:55:22.930722Z` |
| MECH-094 | `failure_autopsy_V3-EXQ-466d_2026-06-24#V3-EXQ-466d` | `failure_autopsy_V3-EXQ-466d_2026-06-24#V3-EXQ-466d` |
| SD-004 | `_none_` | `failure_autopsy_batch-793a-817-819_2026-07-26#V3-EXQ-817` |
| MECH-140 | `failure_autopsy_V3-EXQ-710_2026-07-03` | `failure_autopsy_V3-EXQ-710_2026-07-20` |
| INV-047 | `failure_autopsy_V3-EXQ-778h_2026-07-19` | `failure_autopsy_V3-EXQ-778a_2026-07-20` |
| MECH-168 | `failure_autopsy_V3-EXQ-778h_2026-07-19` | `failure_autopsy_V3-EXQ-778a_2026-07-20` |
| MECH-169 | `failure_autopsy_V3-EXQ-778h_2026-07-19` | `failure_autopsy_V3-EXQ-778a_2026-07-20` |
| MECH-204 | `failure_autopsy_V3-EXQ-794_2026-07-22` | `failure_autopsy_backlog_2026-07-24#V3-EXQ-794a` |
| INV-088 | `failure_autopsy_MECH-457-fanout-752-753-754_2026-07-15#V3-EXQ-754` | `failure_autopsy_batch-793a-817-819_2026-07-26#V3-EXQ-819` |
| SD-024 | `_none_` | `decision:SD-024@2026-07-26T15:35:35.089092Z` |
| SD-025 | `failure_autopsy_V3-EXQ-767a_2026-07-17` | `failure_autopsy_V3-EXQ-767a_2026-07-17` |
| MECH-245 | `_none_` | `v3_exq_825_mech245_generative_dominance_deafferentation_20260726T152102Z_v3` |
| SD-032a | `failure_autopsy_SD-034-closure-cluster-ext_2026-06-12#V3-EXQ-467c` | `failure_autopsy_backlog_2026-07-24#V3-EXQ-797` |
| MECH-266 | `failure_autopsy_SD-034-closure-cluster-ext_2026-06-12#V3-EXQ-467c` | `failure_autopsy_backlog_2026-07-24#V3-EXQ-797` |
| SD-049 | `failure_autopsy_V3-EXQ-538a_2026-07-10` | `failure_autopsy_batch-793a-817-819_2026-07-26#V3-EXQ-793a` |
| MECH-314 | `failure_autopsy_V3-EXQ-732_2026-07-10` | `failure_autopsy_V3-EXQ-604c_2026-07-20` |
| MECH-314a | `failure_autopsy_batch9_2026-06-12#V3-EXQ-590b` | `failure_autopsy_V3-EXQ-604c_2026-07-20` |
| MECH-314b | `failure_autopsy_V3-EXQ-604c_2026-07-20` | `failure_autopsy_V3-EXQ-604c_2026-07-20` |
| MECH-314c | `failure_autopsy_V3-EXQ-604c_2026-07-20` | `failure_autopsy_V3-EXQ-604c_2026-07-20` |
| Q-044 | `failure_autopsy_V3-EXQ-604c_2026-07-20` | `failure_autopsy_V3-EXQ-604c_2026-07-20` |
| ARC-070 | `decision:ARC-070@2026-05-16T19:08:31Z` | `failure_autopsy_V3-EXQ-816b_2026-07-26` |
| ARC-071 | `decision:ARC-071@2026-05-16T19:08:31Z` | `failure_autopsy_backlog_2026-07-24#V3-EXQ-810` |
| MECH-321 | `_none_` | `failure_autopsy_V3-EXQ-816b_2026-07-26` |
| MECH-323 | `_none_` | `failure_autopsy_backlog_2026-07-24#V3-EXQ-810` |
| MECH-324 | `_none_` | `failure_autopsy_backlog_2026-07-24#V3-EXQ-810` |
| MECH-342 | `failure_autopsy_V3-EXQ-732_2026-07-10` | `failure_autopsy_backlog_2026-07-24#V3-EXQ-629c` |
| Q-054 | `failure_autopsy_MECH-341-cluster_2026-05-31#V3-EXQ-616` | `failure_autopsy_MECH-341-cluster_2026-05-31#V3-EXQ-616` |
| SD-059 | `failure_autopsy_batch9_2026-06-12#V3-EXQ-603o` | `failure_autopsy_batch9_2026-06-12#V3-EXQ-603o` |
| MECH-358 | `failure_autopsy_batch9_2026-06-12#V3-EXQ-603o` | `failure_autopsy_batch9_2026-06-12#V3-EXQ-603o` |
| SD-068 | `failure_autopsy_V3-EXQ-778h_2026-07-19` | `failure_autopsy_V3-EXQ-778a_2026-07-20` |
| SD-076 | `failure_autopsy_V3-EXQ-794_2026-07-22` | `failure_autopsy_backlog_2026-07-24#V3-EXQ-794a` |
| SD-078 | `v3_exq_806_sd078_centered_rule_field_context_key_20260725T191042Z_v3` | `failure_autopsy_816c-822_2026-07-26#V3-EXQ-822` |
| SD-079 | `v3_exq_823_sd079_ghost_goal_retrieval_consumer_20260726T075327Z_v3` | `v3_exq_823_sd079_ghost_goal_retrieval_consumer_20260726T075327Z_v3` |
| SD-080 | `_none_` | `failure_autopsy_batch-793a-817-819_2026-07-26#V3-EXQ-817` |
| MECH-439 | `failure_autopsy_V3-EXQ-732_2026-07-10` | `failure_autopsy_V3-EXQ-711-713_2026-07-20#V3-EXQ-713` |
| MECH-440 | `failure_autopsy_V3-EXQ-708a_2026-07-22` | `failure_autopsy_backlog_2026-07-24#V3-EXQ-708b` |
| MECH-448 | `failure_autopsy_V3-EXQ-689i_2026-07-24` | `failure_autopsy_backlog_2026-07-24#V3-EXQ-699b` |
| MECH-449 | `failure_autopsy_V3-EXQ-699_2026-07-20` | `failure_autopsy_backlog_2026-07-24#V3-EXQ-699b` |
| ARC-108 | `failure_autopsy_V3-EXQ-732_2026-07-10` | `failure_autopsy_V3-EXQ-711-713_2026-07-20#V3-EXQ-713` |
| MECH-450 | `failure_autopsy_V3-EXQ-710_2026-07-03` | `failure_autopsy_V3-EXQ-710_2026-07-20` |
| ARC-110 | `failure_autopsy_V3-EXQ-707c_2026-07-25#V3-EXQ-707c` | `failure_autopsy_V3-EXQ-707c_2026-07-25` |
| MECH-457 | `failure_autopsy_competence-objective-cluster-734-737b-742a_2026-07-22#V3-EXQ-742b` | `failure_autopsy_batch-793a-817-819_2026-07-26#V3-EXQ-819` |
| MECH-459 | `failure_autopsy_MECH-457-gov-fanout-1-cluster-780-781-782_2026-07-18#V3-EXQ-782` | `failure_autopsy_V3-EXQ-782_2026-07-20` |
| MECH-463 | `failure_autopsy_mech463-exogenous-inertness_2026-07-20` | `failure_autopsy_mech463-exogenous-inertness_2026-07-20#V3-EXQ-785b` |
| Q-081 | `_none_` | `decision:Q-081@2026-07-26T15:35:34.741714Z` |
| MECH-466 | `_none_` | `decision:MECH-466@2026-07-26T15:35:34.678027Z` |
| INV-091 | `_none_` | `decision:INV-091@2026-07-26T15:35:34.371476Z` |
| ARC-112 | `_none_` | `decision:ARC-112@2026-07-26T15:35:34.308685Z` |
| Q-082 | `_none_` | `decision:Q-082@2026-07-26T15:35:34.898138Z` |
| Q-084 | `_none_` | `decision:Q-084@2026-07-26T15:35:34.975552Z` |
| MECH-477 | `failure_autopsy_V3-EXQ-811_2026-07-24` | `failure_autopsy_V3-EXQ-811_2026-07-24` |

## Never reviewed (no `last_reviewed`) -- INFO (918 of 939)

Claims with no `last_reviewed` history value -- not yet reviewed under the history plane. `last_reviewed` is record-once and legitimately absent for most claims (seeded from `adjudicated_at_utc`, or set with `apply_live_status.py --mark-reviewed <ID>`). Count + sample only.

Sample: INV-001, INV-002, INV-003, INV-004, INV-005, INV-006, INV-007, INV-008, INV-009, INV-010, INV-011, INV-012, INV-013, INV-014, INV-015, INV-016, INV-017, ARC-001, ARC-002, ARC-004 ...

