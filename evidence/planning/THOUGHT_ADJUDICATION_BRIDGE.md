# Thought Adjudication Bridge

Generated: `2026-02-25T14:08:31.357244Z`

This report surfaces claims where thought-intake progression likely needs adjudication refresh or direct
status-application follow-through.

- total bridge items: `7`
- approved decisions pending apply: `0`
- thought newer than latest decision: `5`
- thought-enriched claims lacking decision timestamp: `2`

## Candidate Queue

| claim_id | status | reason | latest_decision | latest_thought | action |
|---|---|---|---|---|---|
| `ARC-003` | `active` | `thought_newer_than_decision` | `2026-02-15T18:46:42.773429Z` | `2026-02-26` | `refresh_decision_brief_and_record_adjudication_outcome` |
| `MECH-057` | `candidate` | `thought_newer_than_decision` | `2026-02-15T20:58:38.602475Z` | `2026-02-23` | `refresh_decision_brief_and_record_adjudication_outcome` |
| `MECH-060` | `candidate` | `thought_newer_than_decision` | `2026-02-15T20:58:38.602475Z` | `2026-02-24` | `refresh_decision_brief_and_record_adjudication_outcome` |
| `MECH-061` | `candidate` | `thought_newer_than_decision` | `2026-02-15T20:58:38.602475Z` | `2026-02-26` | `refresh_decision_brief_and_record_adjudication_outcome` |
| `MECH-062` | `stable` | `thought_newer_than_decision` | `2026-02-25T14:07:04.606327Z` | `2026-02-26` | `refresh_decision_brief_and_record_adjudication_outcome` |
| `Q-006` | `active` | `no_decision_for_thought_enriched_claim` | `` | `2026-02-08` | `open_decision_lane_for_thought_enriched_claim` |
| `Q-016` | `active` | `no_decision_for_thought_enriched_claim` | `` | `2026-02-15` | `open_decision_lane_for_thought_enriched_claim` |

## Details

### ARC-003
- claim_type: `architectural_commitment`
- status: `active`
- reason: `thought_newer_than_decision`
- location: `docs/architecture/e3.md#arc-003`
- recommended_action: `refresh_decision_brief_and_record_adjudication_outcome`
- decision: status=`applied` recommendation=`retain_ree` timestamp=`2026-02-15T18:46:42.773429Z`
- thought_signals: processed_source_count=`3` latest_file=`2026-02-26_task_loop_extraction_and_latent_field_ethics.md` latest_date=`2026-02-26`
- thought_sources:
  - `docs/thoughts/2026-02-09_starting_with_sensory_streams.md`
  - `docs/thoughts/2026-02-24_prefrontal_primitives.md`
  - `docs/thoughts/2026-02-26_task_loop_extraction_and_latent_field_ethics.md`

### MECH-057
- claim_type: `mechanism_hypothesis`
- status: `candidate`
- reason: `thought_newer_than_decision`
- location: `docs/architecture/agency_responsibility_flow.md#mech-057`
- recommended_action: `refresh_decision_brief_and_record_adjudication_outcome`
- decision: status=`applied` recommendation=`hold_candidate_resolve_conflict` timestamp=`2026-02-15T20:58:38.602475Z`
- thought_signals: processed_source_count=`3` latest_file=`2026-02-23_some_subjective_experience_mapping.md` latest_date=`2026-02-23`
- thought_sources:
  - `docs/thoughts/2026-02-13_LeCun_developed_lots_of_REE.md`
  - `docs/thoughts/2026-02-13_subjective_experience_pre_post_commit.md`
  - `docs/thoughts/2026-02-23_some_subjective_experience_mapping.md`

### MECH-060
- claim_type: `mechanism_hypothesis`
- status: `candidate`
- reason: `thought_newer_than_decision`
- location: `docs/architecture/agency_responsibility_flow.md#mech-060`
- recommended_action: `refresh_decision_brief_and_record_adjudication_outcome`
- decision: status=`applied` recommendation=`hold_candidate_resolve_conflict` timestamp=`2026-02-15T20:58:38.602475Z`
- thought_signals: processed_source_count=`3` latest_file=`2026-02-24_determinism_action_gating_boundary.md` latest_date=`2026-02-24`
- thought_sources:
  - `docs/thoughts/2026-02-13_subjective_experience_pre_post_commit.md`
  - `docs/thoughts/2026-02-23_some_subjective_experience_mapping.md`
  - `docs/thoughts/2026-02-24_determinism_action_gating_boundary.md`

### MECH-061
- claim_type: `mechanism_hypothesis`
- status: `candidate`
- reason: `thought_newer_than_decision`
- location: `docs/architecture/e3.md#mech-061`
- recommended_action: `refresh_decision_brief_and_record_adjudication_outcome`
- decision: status=`applied` recommendation=`hold_candidate_resolve_conflict` timestamp=`2026-02-15T20:58:38.602475Z`
- thought_signals: processed_source_count=`4` latest_file=`2026-02-26_task_loop_extraction_and_latent_field_ethics.md` latest_date=`2026-02-26`
- thought_sources:
  - `docs/thoughts/2026-02-15_basal_ganglia.md`
  - `docs/thoughts/2026-02-15_basal_ganglia_commit_gating_control_plane_axes.md`
  - `docs/thoughts/2026-02-24_determinism_action_gating_boundary.md`
  - `docs/thoughts/2026-02-26_task_loop_extraction_and_latent_field_ethics.md`

### MECH-062
- claim_type: `mechanism_hypothesis`
- status: `stable`
- reason: `thought_newer_than_decision`
- location: `docs/architecture/e3.md#mech-062`
- recommended_action: `refresh_decision_brief_and_record_adjudication_outcome`
- decision: status=`applied` recommendation=`promote_to_stable` timestamp=`2026-02-25T14:07:04.606327Z`
- thought_signals: processed_source_count=`6` latest_file=`2026-02-26_task_loop_extraction_and_latent_field_ethics.md` latest_date=`2026-02-26`
- thought_sources:
  - `docs/thoughts/2026-02-13_subjective_experience_pre_post_commit.md`
  - `docs/thoughts/2026-02-15_basal_ganglia.md`
  - `docs/thoughts/2026-02-15_basal_ganglia_commit_gating_control_plane_axes.md`
  - `docs/thoughts/2026-02-23_some_subjective_experience_mapping.md`
  - `docs/thoughts/2026-02-24_prefrontal_primitives.md`
  - `docs/thoughts/2026-02-26_task_loop_extraction_and_latent_field_ethics.md`

### Q-006
- claim_type: `open_question`
- status: `active`
- reason: `no_decision_for_thought_enriched_claim`
- location: `docs/architecture/agency_responsibility_flow.md#q-006`
- recommended_action: `open_decision_lane_for_thought_enriched_claim`
- decision: status=`` recommendation=`` timestamp=``
- thought_signals: processed_source_count=`1` latest_file=`2026-02-08_control_plane_modes_responsibility_flow.md` latest_date=`2026-02-08`
- thought_sources:
  - `docs/thoughts/2026-02-08_control_plane_modes_responsibility_flow.md`

### Q-016
- claim_type: `open_question`
- status: `active`
- reason: `no_decision_for_thought_enriched_claim`
- location: `docs/architecture/e3.md#q-016`
- recommended_action: `open_decision_lane_for_thought_enriched_claim`
- decision: status=`` recommendation=`` timestamp=``
- thought_signals: processed_source_count=`1` latest_file=`2026-02-15_basal_ganglia.md` latest_date=`2026-02-15`
- thought_sources:
  - `docs/thoughts/2026-02-15_basal_ganglia.md`
