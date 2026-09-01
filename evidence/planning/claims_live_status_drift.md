# Claims live_status Drift Report

Generated: 2026-09-01T07:42:29Z

Mirror of the closure-plan / claims-doc drift reports, for the claims registry's `live_status` status plane (SHP-4). Flags claims whose stored `live_status` block has fallen out of step with the value re-derived from the claim's own current fields (`status` + `v3_pending` + `epistemic_category`). Resolution + derivation are shared with `scripts/apply_live_status.py`. Only the **Reading drift** bucket is a hard signal (fails `--strict`); the rest are review/info hints.

Warn-only by default -- run with `--strict` for a blocking gate.

Claims in registry: 1077

## Reading drift -- HARD (141)

Stored `live_status` != re-derived value. Re-run `scripts/apply_live_status.py`; if it persists, the block was hand-edited or the claim's fields changed without a re-stamp.

| claim | stored reading | derived reading | drifted fields |
|-------|----------------|-----------------|----------------|
| INV-012 | `active` | `active/substrate_conditional` | reading: stored='active' derived='active/substrate_conditional' |
| ARC-007 | `active` | `provisional` | reading: stored='active' derived='provisional' |
| ARC-009 | `active` | `active/substrate_conditional` | reading: stored='active' derived='active/substrate_conditional' |
| ARC-010 | `active` | `active/substrate_conditional` | reading: stored='active' derived='active/substrate_conditional' |
| MECH-001 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| MECH-010 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| ARC-015 | `provisional` | `provisional/substrate_conditional` | reading: stored='provisional' derived='provisional/substrate_conditional' |
| MECH-022 | `provisional` | `provisional/substrate_conditional` | reading: stored='provisional' derived='provisional/substrate_conditional' |
| ARC-018 | `active` | `provisional` | reading: stored='active' derived='provisional' |
| ARC-020 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| MECH-026 | `provisional` | `provisional/substrate_conditional` | reading: stored='provisional' derived='provisional/substrate_conditional' |
| MECH-032 | `provisional` | `provisional/substrate_conditional` | reading: stored='provisional' derived='provisional/substrate_conditional' |
| MECH-036 | `provisional` | `provisional/substrate_conditional` | reading: stored='provisional' derived='provisional/substrate_conditional' |
| MECH-041 | `provisional` | `provisional/substrate_conditional` | reading: stored='provisional' derived='provisional/substrate_conditional' |
| MECH-051 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| MECH-052 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| INV-021 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| INV-028 | `active` | `active/substrate_conditional` | reading: stored='active' derived='active/substrate_conditional' |
| INV-029 | `active` | `active/substrate_conditional` | reading: stored='active' derived='active/substrate_conditional' |
| INV-033 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| Q-020 | `resolved` | `candidate` | reading: stored='resolved' derived='candidate' |
| Q-021 | `open` | `open/substrate_conditional` | reading: stored='open' derived='open/substrate_conditional' |
| MECH-083 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| ARC-023 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| MECH-092 | `provisional` | `provisional/substrate_conditional` | reading: stored='provisional' derived='provisional/substrate_conditional' |
| MECH-103 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| ARC-030 | `candidate` | `candidate/substrate_ceiling` | reading: stored='candidate' derived='candidate/substrate_ceiling' |
| SD-007 | `implemented` | `implemented` | needs_review: stored=True derived=False |
| MECH-108 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| MECH-114 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| INV-034 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| INV-037 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| INV-038 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| MECH-123 | `candidate/substrate_conditional` | `candidate/v3_pending/substrate_conditional` | reading: stored='candidate/substrate_conditional' derived='candidate/v3_pending/substrate_conditional' |
| ARC-034 | `candidate/v3_pending` | `candidate/v3_pending/substrate_conditional` | reading: stored='candidate/v3_pending' derived='candidate/v3_pending/substrate_conditional' |
| ARC-035 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| ARC-036 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| ARC-039 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| MECH-140 | `candidate/standard` | `candidate` | reading: stored='candidate/standard' derived='candidate' |
| ARC-041 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| INV-043 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| MECH-165 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| SD-016 | `implemented` | `implemented/substrate_ceiling` | reading: stored='implemented' derived='implemented/substrate_ceiling'; needs_review: stored=False derived=True |
| SD-017 | `stable` | `stable/substrate_ceiling` | reading: stored='stable' derived='stable/substrate_ceiling'; needs_review: stored=False derived=True |
| ARC-045 | `candidate` | `candidate/substrate_ceiling` | reading: stored='candidate' derived='candidate/substrate_ceiling' |
| MECH-166 | `candidate` | `candidate/substrate_ceiling` | reading: stored='candidate' derived='candidate/substrate_ceiling' |
| INV-045 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| INV-046 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| INV-048 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| MECH-174 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| INV-049 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| INV-051 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| ARC-047 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| INV-058 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| INV-059 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| INV-094 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| INV-096 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| MECH-484 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| ARC-122 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| INV-060 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| MECH-210 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| MECH-212 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| MECH-214 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| INV-065 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| MECH-216 | `provisional` | `provisional/substrate_conditional` | reading: stored='provisional' derived='provisional/substrate_conditional' |
| MECH-217 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| SD-021 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| INV-068 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| INV-070 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| INV-071 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| INV-073 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| ARC-056 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| MECH-225 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| MECH-235 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| MECH-238 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| SD-026 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| SD-027 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| MECH-254 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| SD-029 | `candidate/v3_pending` | `candidate/v3_pending/substrate_ceiling` | reading: stored='candidate/v3_pending' derived='candidate/v3_pending/substrate_ceiling' |
| MECH-257 | `candidate/v3_pending` | `candidate/v3_pending/substrate_ceiling` | reading: stored='candidate/v3_pending' derived='candidate/v3_pending/substrate_ceiling' |
| SD-032 | `candidate/v3_pending` | `candidate/v3_pending/substrate_conditional` | reading: stored='candidate/v3_pending' derived='candidate/v3_pending/substrate_conditional' |
| SD-032c | `candidate/v3_pending` | `candidate/v3_pending/substrate_conditional` | reading: stored='candidate/v3_pending' derived='candidate/v3_pending/substrate_conditional' |
| SD-033a | `candidate/v3_pending` | `candidate/v3_pending/substrate_conditional` | reading: stored='candidate/v3_pending' derived='candidate/v3_pending/substrate_conditional' |
| SD-033e | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| MECH-264 | `candidate/v3_pending` | `candidate/v3_pending/substrate_conditional` | reading: stored='candidate/v3_pending' derived='candidate/v3_pending/substrate_conditional' |
| MECH-271 | `candidate/v3_pending` | `candidate/v3_pending/substrate_conditional` | reading: stored='candidate/v3_pending' derived='candidate/v3_pending/substrate_conditional' |
| ARC-059 | `candidate/v3_pending` | `candidate/v3_pending/substrate_conditional` | reading: stored='candidate/v3_pending' derived='candidate/v3_pending/substrate_conditional' |
| MECH-277 | `candidate/v3_pending` | `candidate/v3_pending/substrate_conditional` | reading: stored='candidate/v3_pending' derived='candidate/v3_pending/substrate_conditional' |
| SD-039 | `candidate/v3_pending` | `candidate/v3_pending/substrate_conditional` | reading: stored='candidate/v3_pending' derived='candidate/v3_pending/substrate_conditional' |
| SD-040 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| ARC-063 | `candidate/v3_pending` | `candidate/v3_pending/substrate_conditional` | reading: stored='candidate/v3_pending' derived='candidate/v3_pending/substrate_conditional' |
| MECH-337 | `candidate/v3_pending` | `candidate/v3_pending/substrate_conditional` | reading: stored='candidate/v3_pending' derived='candidate/v3_pending/substrate_conditional' |
| MECH-338 | `candidate/v3_pending` | `candidate/v3_pending/substrate_conditional` | reading: stored='candidate/v3_pending' derived='candidate/v3_pending/substrate_conditional' |
| MECH-314c | `candidate_substrate_landed` | `candidate_substrate_landed/substrate_conditional` | reading: stored='candidate_substrate_landed' derived='candidate_substrate_landed/substrate_conditional' |
| Q-044 | `open` | `open/substrate_ceiling` | reading: stored='open' derived='open/substrate_ceiling' |
| ARC-064 | `candidate/v3_pending` | `candidate/v3_pending/substrate_conditional` | reading: stored='candidate/v3_pending' derived='candidate/v3_pending/substrate_conditional' |
| MECH-316 | `candidate/v3_pending` | `candidate/v3_pending/substrate_conditional` | reading: stored='candidate/v3_pending' derived='candidate/v3_pending/substrate_conditional' |
| MECH-318 | `candidate/v3_pending` | `candidate/v3_pending/substrate_conditional` | reading: stored='candidate/v3_pending' derived='candidate/v3_pending/substrate_conditional' |
| ARC-069 | `candidate/v3_pending` | `candidate/v3_pending/substrate_conditional` | reading: stored='candidate/v3_pending' derived='candidate/v3_pending/substrate_conditional' |
| ARC-071 | `candidate/v3_pending` | `candidate/v3_pending/substrate_conditional` | reading: stored='candidate/v3_pending' derived='candidate/v3_pending/substrate_conditional' |
| ARC-072 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| ARC-074 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| ARC-078 | `candidate/v3_pending` | `candidate/v3_pending/substrate_conditional` | reading: stored='candidate/v3_pending' derived='candidate/v3_pending/substrate_conditional' |
| ARC-079 | `candidate/v3_pending` | `candidate/v3_pending/substrate_conditional` | reading: stored='candidate/v3_pending' derived='candidate/v3_pending/substrate_conditional' |
| MECH-343 | `candidate/v3_pending/substrate_conditional` | `candidate/v3_pending/substrate_ceiling` | reading: stored='candidate/v3_pending/substrate_conditional' derived='candidate/v3_pending/substrate_ceiling' |
| INV-076 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| Q-096 | `candidate/substrate_conditional` | `candidate/substrate_conditional` | needs_review: stored=True derived=False |
| SD-064 | `candidate/v3_pending` | `candidate/v3_pending/substrate_conditional` | reading: stored='candidate/v3_pending' derived='candidate/v3_pending/substrate_conditional' |
| MECH-441 | `candidate/v3_pending/substrate_ceiling` | `candidate/v3_pending/substrate_conditional` | reading: stored='candidate/v3_pending/substrate_ceiling' derived='candidate/v3_pending/substrate_conditional' |
| MECH-448 | `provisional` | `candidate` | reading: stored='provisional' derived='candidate' |
| MECH-475 | `retired` | `retired/v3_pending` | reading: stored='retired' derived='retired/v3_pending' |
| MECH-476 | `retired` | `retired/v3_pending` | reading: stored='retired' derived='retired/v3_pending' |
| MECH-477 | `candidate/v3_pending` | `candidate` | reading: stored='candidate/v3_pending' derived='candidate' |
| MECH-478 | `candidate/v3_pending` | `candidate/v3_pending/substrate_conditional` | reading: stored='candidate/v3_pending' derived='candidate/v3_pending/substrate_conditional' |
| MECH-479 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| Q-086 | `answered_pending_confirmatory_pass` | `candidate` | reading: stored='answered_pending_confirmatory_pass' derived='candidate' |
| Q-087 | `answered` | `resolved` | reading: stored='answered' derived='resolved' |
| ARC-115 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| ARC-116 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| ARC-119 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| ARC-117 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| ARC-118 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| SENT-17 | `candidate` | `candidate/v3_pending` | reading: stored='candidate' derived='candidate/v3_pending' |
| MECH-480 | `candidate` | `candidate/v3_pending` | reading: stored='candidate' derived='candidate/v3_pending' |
| SD-091 | `candidate` | `candidate/v3_pending/substrate_conditional` | reading: stored='candidate' derived='candidate/v3_pending/substrate_conditional' |
| MECH-481 | `candidate` | `candidate/v3_pending/substrate_conditional` | reading: stored='candidate' derived='candidate/v3_pending/substrate_conditional' |
| SD-093 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| MECH-485 | `candidate/v3_pending/substrate_conditional` | `candidate/substrate_conditional` | reading: stored='candidate/v3_pending/substrate_conditional' derived='candidate/substrate_conditional' |
| Q-090 | `candidate/v3_pending/substrate_conditional` | `candidate/substrate_conditional` | reading: stored='candidate/v3_pending/substrate_conditional' derived='candidate/substrate_conditional' |
| MECH-487 | `candidate/v3_pending/substrate_conditional` | `candidate/substrate_conditional` | reading: stored='candidate/v3_pending/substrate_conditional' derived='candidate/substrate_conditional' |
| SD-097 | `candidate/v3_pending/substrate_conditional` | `candidate/substrate_conditional` | reading: stored='candidate/v3_pending/substrate_conditional' derived='candidate/substrate_conditional' |
| SD-098 | `candidate/v3_pending/substrate_conditional` | `candidate/substrate_conditional` | reading: stored='candidate/v3_pending/substrate_conditional' derived='candidate/substrate_conditional' |
| MECH-516 | `candidate` | `candidate/v3_pending` | reading: stored='candidate' derived='candidate/v3_pending' |
| MECH-517 | `candidate` | `candidate/v3_pending` | reading: stored='candidate' derived='candidate/v3_pending' |
| MECH-518 | `candidate` | `candidate/v3_pending` | reading: stored='candidate' derived='candidate/v3_pending' |
| MECH-523 | `candidate` | `candidate/v3_pending` | reading: stored='candidate' derived='candidate/v3_pending' |
| ARC-135 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| MECH-527 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| MECH-528 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| ARC-136 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |
| MECH-529 | `candidate` | `candidate/substrate_conditional` | reading: stored='candidate' derived='candidate/substrate_conditional' |

## Unstamped -- SOFT (29)

Registered claims with no `live_status` block. Run `scripts/apply_live_status.py`.

| claim | would-derive |
|-------|--------------|
| MECH-464 | `candidate` |
| MECH-465 | `candidate` |
| Q-092 | `open` |
| INV-101 | `candidate/substrate_conditional` |
| Q-093 | `open/substrate_conditional` |
| MECH-491 | `candidate/substrate_conditional` |
| ARC-127 | `candidate/substrate_conditional` |
| SD-100 | `candidate/substrate_conditional` |
| MECH-492 | `candidate` |
| MECH-493 | `candidate/substrate_conditional` |
| MECH-494 | `candidate` |
| MECH-495 | `candidate` |
| MECH-496 | `candidate/substrate_conditional` |
| Q-094 | `open` |
| Q-095 | `open` |
| INV-102 | `candidate/v3_pending/substrate_conditional` |
| MECH-504 | `candidate/v3_pending/substrate_conditional` |
| MECH-506 | `candidate/v3_pending/substrate_conditional` |
| MECH-505 | `candidate/v3_pending/substrate_conditional` |
| MECH-507 | `candidate/substrate_conditional` |
| MECH-508 | `candidate/substrate_conditional` |
| MECH-509 | `candidate/substrate_conditional` |
| MECH-510 | `candidate/substrate_conditional` |
| MECH-511 | `candidate/substrate_conditional` |
| MECH-512 | `candidate/substrate_conditional` |
| INV-103 | `candidate/substrate_conditional` |
| ARC-132 | `candidate/substrate_conditional` |
| MECH-513 | `candidate/substrate_conditional` |
| MECH-514 | `candidate/substrate_conditional` |

## Internal inconsistency -- REVIEW (2)

Claims whose own current-state fields contradict each other (`needs_review` true): a promoted status still carrying the V3-pending gate, or a promoted status tagged `substrate_ceiling` (GOV-CEIL-1 floors ceilings to candidate). The derived `live_status` is a best-effort; a human should reconcile the fields.

| claim | derived reading | why |
|-------|-----------------|-----|
| SD-016 | `implemented/substrate_ceiling` | promoted status 'implemented' but epistemic_category substrate_ceiling (GOV-CEIL-1 floors ceilings to candidate) |
| SD-017 | `stable/substrate_ceiling` | promoted status 'stable' but epistemic_category substrate_ceiling (GOV-CEIL-1 floors ceilings to candidate) |

## Event-provenance drift -- SOFT (284)

The `live_status.evidence` sub-block (SHP-4 augmentation: `from` / `as_of` / `verdict`) is projected from the append-only event log via project_status_head. This flags claims whose stored `evidence` block no longer matches the freshly re-projected head -- i.e. a newer autopsy / PASS manifest / decision landed (or one changed) since `apply_live_status.py` last ran. It fluctuates legitimately as the fleet produces evidence, so it is **warn-only and never a --strict failure**: re-run `scripts/apply_live_status.py` (under a TASK_CLAIMS claim on docs/claims/claims.yaml) to refresh. Reading drift (HARD, above) is the gate; provenance drift is a hint.

| claim | stored evidence.from | re-projected from |
|-------|----------------------|-------------------|
| INV-010 | `_none_` | `failure_autopsy_grandfathered-r5-batch01-mixed-findings_2026-08-08` |
| INV-013 | `_none_` | `failure_autopsy_V3-EXQ-942_2026-08-21` |
| ARC-003 | `decision:ARC-003@2026-02-25T16:56:17.901452Z` | `failure_autopsy_backlog_2026-07-24#V3-EXQ-804` |
| ARC-004 | `_none_` | `failure_autopsy_V3-EXQ-942_2026-08-21` |
| ARC-005 | `v3_exq_848b_arc005_precision_only_finer_ladder_20260804T064758Z_v3#failure_autopsy_2026-08-05_pending_review_batch` | `failure_autopsy_2026-08-05_pending_review_batch#V3-EXQ-848b` |
| ARC-007 | `decision:ARC-007@2026-03-16T18:20:19.360735Z` | `failure_autopsy_grandfathered-r6-closure-sweep_2026-08-08` |
| Q-001 | `_none_` | `failure_autopsy_grandfathered-r6-closure-sweep_2026-08-08` |
| Q-002 | `failure_autopsy_V3-EXQ-783_2026-07-18` | `failure_autopsy_grandfathered-r5-batch01-mixed-findings_2026-08-08` |
| Q-003 | `_none_` | `failure_autopsy_grandfathered-r6-closure-sweep_2026-08-08` |
| Q-004 | `_none_` | `v3_exq_149b_q004_tau_r_largebudget_20260804T234245Z_v3` |
| Q-005 | `_none_` | `failure_autopsy_20260329-legacy-cluster_2026-08-08#V3-EXQ-150` |
| ARC-014 | `v3_exq_880_arc014_simulation_mode_commitment_20260802T214058Z_v3` | `v3_exq_880_arc014_simulation_mode_commitment_20260802T214058Z_v3` |
| MECH-022 | `failure_autopsy_V3-EXQ-190a_2026-08-09` | `failure_autopsy_V3-EXQ-190a_2026-08-09` |
| Q-006 | `decision:Q-006@2026-02-25T16:51:50.794689Z` | `failure_autopsy_20260329-legacy-cluster_2026-08-08#V3-EXQ-151` |
| Q-007 | `decision:Q-007@2026-03-16T18:20:19.361155Z` | `failure_autopsy_grandfathered-r6-closure-sweep_2026-08-08` |
| Q-008 | `_none_` | `failure_autopsy_grandfathered-r5-legacy-provenance-sweep_2026-08-08` |
| Q-009 | `_none_` | `failure_autopsy_grandfathered-r5-legacy-provenance-sweep_2026-08-08` |
| ARC-016 | `v3_exq_818_arc016_eval_derived_noise_precision_sweep_20260725T185821Z_v3` | `failure_autopsy_grandfathered-r6-closure-sweep_2026-08-08` |
| ARC-017 | `_none_` | `failure_autopsy_ARC-017-EXQ-129-135_2026-08-07#V3-EXQ-135` |
| ARC-018 | `decision:ARC-018@2026-03-16T18:20:19.361124Z` | `failure_autopsy_grandfathered-r5-legacy-provenance-sweep_2026-08-08` |
| MECH-025 | `decision:MECH-025@2026-08-10` | `failure_autopsy_grandfathered-r6-closure-sweep_2026-08-08` |
| MECH-026 | `_none_` | `failure_autopsy_grandfathered-r6-closure-sweep_2026-08-08` |
| MECH-029 | `_none_` | `failure_autopsy_grandfathered-misc2-ninethread-cluster_2026-08-08` |
| MECH-030 | `_none_` | `failure_autopsy_grandfathered-superseded-batch1_2026-08-08` |
| MECH-033 | `v3_exq_308_mech033_kernel_chain_discriminative_20260409T183908Z_v3` | `failure_autopsy_grandfathered-r5-batch01-mixed-findings_2026-08-08` |
| MECH-044 | `failure_autopsy_V3-EXQ-688_2026-06-18` | `failure_autopsy_grandfathered-r5-batch01-mixed-findings_2026-08-08` |
| MECH-047 | `_none_` | `failure_autopsy_grandfathered-r5-batch01-mixed-findings_2026-08-08` |
| MECH-048 | `_none_` | `failure_autopsy_backlog_2026-07-24#V3-EXQ-799` |
| MECH-056 | `decision:MECH-056@2026-02-15T20:58:38.602475Z` | `failure_autopsy_grandfathered-r5-legacy-provenance-sweep_2026-08-08` |
| MECH-057a | `decision:MECH-057a@2026-03-29T21:15:31.848348Z` | `failure_autopsy_grandfathered-r5-batch23-mixed-findings_2026-08-08` |
| MECH-057b | `failure_autopsy_V3-EXQ-672-series_2026-06-15#V3-EXQ-672b` | `failure_autopsy_grandfathered-superseded-batch1_2026-08-08` |
| MECH-058 | `decision:MECH-058@2026-02-25T16:39:07.573674Z` | `failure_autopsy_grandfathered-r5-legacy-provenance-sweep_2026-08-08` |
| MECH-059 | `decision:MECH-059@2026-02-15T20:58:38.602475Z` | `failure_autopsy_grandfathered-r5-legacy-provenance-sweep_2026-08-08` |
| MECH-060 | `decision:MECH-060@2026-02-25T16:35:40.759224Z` | `failure_autopsy_grandfathered-r5-legacy-provenance-sweep_2026-08-08` |
| MECH-063 | `failure_autopsy_V3-EXQ-779b_2026-07-19` | `failure_autopsy_V3-EXQ-963_2026-08-30` |
| MECH-067 | `_none_` | `failure_autopsy_grandfathered-r5-legacy-provenance-sweep_2026-08-08` |
| MECH-068 | `_none_` | `v3_exq_835_mech068_consolidation_selectivity_ablation_20260728T201442Z_v3` |
| Q-012 | `decision:Q-012@2026-03-02T00:00:00.000000Z` | `failure_autopsy_grandfathered-r5-batch23-mixed-findings_2026-08-08` |
| Q-014 | `decision:Q-014@2026-02-25T16:51:50.758372Z` | `failure_autopsy_20260329-legacy-cluster_2026-08-08#V3-EXQ-154` |
| Q-015 | `decision:Q-015@2026-02-15T18:46:42.773429Z` | `failure_autopsy_20260329-legacy-cluster_2026-08-08#V3-EXQ-155` |
| Q-016 | `decision:Q-016@2026-02-25T16:51:50.829631Z` | `failure_autopsy_20260329-legacy-cluster_2026-08-08#V3-EXQ-156` |
| Q-017 | `decision:Q-017@2026-02-25T16:51:50.648196Z` | `failure_autopsy_grandfathered-r6-closure-sweep_2026-08-08` |
| INV-029 | `_none_` | `failure_autopsy_grandfathered-wanting-liking-cluster_2026-08-08` |
| ARC-024 | `decision:ARC-024@2026-03-19T20:35:00Z` | `failure_autopsy_grandfathered-r6-closure-sweep_2026-08-08` |
| ARC-026 | `decision:ARC-026@2026-05-03T02:50:00Z` | `failure_autopsy_grandfathered-wanting-liking-cluster_2026-08-08` |
| MECH-102 | `v3_exq_533_mech102_harm_stream_ablation_20260506T094157Z_v3` | `failure_autopsy_grandfathered-r6-closure-sweep_2026-08-08` |
| ARC-021 | `_none_` | `failure_autopsy_grandfathered-r6-closure-sweep_2026-08-08` |
| MECH-069 | `decision:MECH-069@2026-03-19T19:52:00Z` | `failure_autopsy_grandfathered-r6-closure-sweep_2026-08-08` |
| MECH-070 | `decision:MECH-070@2026-04-03T22:00:00Z` | `failure_autopsy_grandfathered-r5-batch23-mixed-findings_2026-08-08` |
| MECH-071 | `decision:MECH-071@2026-03-16T18:20:19.361137Z` | `failure_autopsy_grandfathered-r6-closure-sweep_2026-08-08` |
| MECH-072 | `v3_exq_213_mech072_foreseeable_harm_gating_20260403T202320Z_v3` | `failure_autopsy_grandfathered-r6-closure-sweep_2026-08-08` |
| MECH-074 | `decision:MECH-074@2026-04-25T15:42:09.107823Z` | `v3_exq_888_mech074_readwrite_head_route_dissociation_20260804T075257Z_v3` |
| MECH-074a | `v3_exq_659_mech074a_bla_encoding_gain_replay_bias_20260609T200751Z_v3` | `v3_exq_888_mech074_readwrite_head_route_dissociation_20260804T075257Z_v3` |
| MECH-074b | `_none_` | `decision:MECH-074b@2026-08-08T08:30:48.470619Z` |
| MECH-074c | `v3_exq_895_mech074c_cea_fast_prime_dynamics_20260808T012422Z_v3` | `v3_exq_895_mech074c_cea_fast_prime_dynamics_20260808T012422Z_v3` |
| MECH-074d | `failure_autopsy_V3-EXQ-894c_2026-08-11` | `failure_autopsy_V3-EXQ-894c_2026-08-11` |
| MECH-075 | `decision:MECH-075@2026-04-03T22:00:00Z` | `failure_autopsy_mech075-second-cluster_2026-08-10#V3-EXQ-905a` |
| Q-020 | `decision:Q-020@2026-04-10T18:06:06.975132Z` | `failure_autopsy_grandfathered-superseded-batch1_2026-08-08` |
| Q-021 | `failure_autopsy_V3-EXQ-866c_2026-08-08` | `failure_autopsy_V3-EXQ-899_2026-08-09` |
| MECH-094 | `failure_autopsy_V3-EXQ-466d_2026-06-24#V3-EXQ-466d` | `failure_autopsy_grandfathered-r5-batch23-mixed-findings_2026-08-08` |
| ... | | (+224 more) |

## Never reviewed (no `last_reviewed`) -- INFO (1056 of 1077)

Claims with no `last_reviewed` history value -- not yet reviewed under the history plane. `last_reviewed` is record-once and legitimately absent for most claims (seeded from `adjudicated_at_utc`, or set with `apply_live_status.py --mark-reviewed <ID>`). Count + sample only.

Sample: INV-001, INV-002, INV-003, INV-004, INV-005, INV-006, INV-007, INV-008, INV-009, INV-010, INV-011, INV-012, INV-013, INV-014, INV-015, INV-016, INV-017, ARC-001, ARC-002, ARC-004 ...

