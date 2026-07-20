# Claims live_status Drift Report

Generated: 2026-07-20T15:57:39Z

Mirror of the closure-plan / claims-doc drift reports, for the claims registry's `live_status` status plane (SHP-4). Flags claims whose stored `live_status` block has fallen out of step with the value re-derived from the claim's own current fields (`status` + `v3_pending` + `epistemic_category`). Resolution + derivation are shared with `scripts/apply_live_status.py`. Only the **Reading drift** bucket is a hard signal (fails `--strict`); the rest are review/info hints.

Warn-only by default -- run with `--strict` for a blocking gate.

Claims in registry: 901

## Reading drift -- HARD (4)

Stored `live_status` != re-derived value. Re-run `scripts/apply_live_status.py`; if it persists, the block was hand-edited or the claim's fields changed without a re-stamp.

| claim | stored reading | derived reading | drifted fields |
|-------|----------------|-----------------|----------------|
| MECH-314b | `candidate_substrate_landed` | `candidate_substrate_landed/substrate_ceiling` | reading: stored='candidate_substrate_landed' derived='candidate_substrate_landed/substrate_ceiling' |
| MECH-314c | `candidate_substrate_landed` | `candidate_substrate_landed/substrate_ceiling` | reading: stored='candidate_substrate_landed' derived='candidate_substrate_landed/substrate_ceiling' |
| Q-044 | `open` | `open/substrate_ceiling` | reading: stored='open' derived='open/substrate_ceiling' |
| MECH-448 | `provisional` | `candidate` | reading: stored='provisional' derived='candidate' |

## Unstamped -- SOFT (0)

Registered claims with no `live_status` block. Run `scripts/apply_live_status.py`.

_None._

## Internal inconsistency -- REVIEW (0)

Claims whose own current-state fields contradict each other (`needs_review` true): a promoted status still carrying the V3-pending gate, or a promoted status tagged `substrate_ceiling` (GOV-CEIL-1 floors ceilings to candidate). The derived `live_status` is a best-effort; a human should reconcile the fields.

_None._

## Event-provenance drift -- SOFT (24)

The `live_status.evidence` sub-block (SHP-4 augmentation: `from` / `as_of` / `verdict`) is projected from the append-only event log via project_status_head. This flags claims whose stored `evidence` block no longer matches the freshly re-projected head -- i.e. a newer autopsy / PASS manifest / decision landed (or one changed) since `apply_live_status.py` last ran. It fluctuates legitimately as the fleet produces evidence, so it is **warn-only and never a --strict failure**: re-run `scripts/apply_live_status.py` (under a TASK_CLAIMS claim on docs/claims/claims.yaml) to refresh. Reading drift (HARD, above) is the gate; provenance drift is a hint.

| claim | stored evidence.from | re-projected from |
|-------|----------------------|-------------------|
| MECH-094 | `failure_autopsy_V3-EXQ-466d_2026-06-24#V3-EXQ-466d` | `failure_autopsy_V3-EXQ-466d_2026-06-24#V3-EXQ-466d` |
| MECH-140 | `failure_autopsy_V3-EXQ-710_2026-07-03` | `failure_autopsy_V3-EXQ-710_2026-07-20` |
| MECH-163 | `decision:MECH-163@2026-04-03T22:00:00Z` | `failure_autopsy_V3-EXQ-786_2026-07-20` |
| INV-047 | `failure_autopsy_V3-EXQ-778h_2026-07-19` | `failure_autopsy_V3-EXQ-778a_2026-07-20` |
| MECH-168 | `failure_autopsy_V3-EXQ-778h_2026-07-19` | `failure_autopsy_V3-EXQ-778a_2026-07-20` |
| MECH-169 | `failure_autopsy_V3-EXQ-778h_2026-07-19` | `failure_autopsy_V3-EXQ-778a_2026-07-20` |
| SD-025 | `failure_autopsy_V3-EXQ-767a_2026-07-17` | `failure_autopsy_V3-EXQ-767a_2026-07-17` |
| MECH-314 | `failure_autopsy_V3-EXQ-732_2026-07-10` | `failure_autopsy_V3-EXQ-604c_2026-07-20` |
| MECH-314a | `failure_autopsy_batch9_2026-06-12#V3-EXQ-590b` | `failure_autopsy_V3-EXQ-604c_2026-07-20` |
| MECH-314b | `failure_autopsy_V3-EXQ-604c_2026-07-20` | `failure_autopsy_V3-EXQ-604c_2026-07-20` |
| MECH-314c | `failure_autopsy_V3-EXQ-604c_2026-07-20` | `failure_autopsy_V3-EXQ-604c_2026-07-20` |
| Q-044 | `failure_autopsy_V3-EXQ-604c_2026-07-20` | `failure_autopsy_V3-EXQ-604c_2026-07-20` |
| Q-054 | `failure_autopsy_MECH-341-cluster_2026-05-31#V3-EXQ-616` | `failure_autopsy_MECH-341-cluster_2026-05-31#V3-EXQ-616` |
| SD-059 | `failure_autopsy_batch9_2026-06-12#V3-EXQ-603o` | `failure_autopsy_batch9_2026-06-12#V3-EXQ-603o` |
| MECH-358 | `failure_autopsy_batch9_2026-06-12#V3-EXQ-603o` | `failure_autopsy_batch9_2026-06-12#V3-EXQ-603o` |
| SD-068 | `failure_autopsy_V3-EXQ-778h_2026-07-19` | `failure_autopsy_V3-EXQ-778a_2026-07-20` |
| MECH-439 | `failure_autopsy_V3-EXQ-732_2026-07-10` | `failure_autopsy_V3-EXQ-711-713_2026-07-20#V3-EXQ-713` |
| MECH-448 | `failure_autopsy_V3-EXQ-699_2026-07-20` | `failure_autopsy_V3-EXQ-689d-D3_2026-07-20` |
| ARC-108 | `failure_autopsy_V3-EXQ-732_2026-07-10` | `failure_autopsy_V3-EXQ-711-713_2026-07-20#V3-EXQ-713` |
| MECH-450 | `failure_autopsy_V3-EXQ-710_2026-07-03` | `failure_autopsy_V3-EXQ-710_2026-07-20` |
| ARC-110 | `failure_autopsy_V3-EXQ-713_2026-07-05#V3-EXQ-713` | `failure_autopsy_V3-EXQ-711-713_2026-07-20#V3-EXQ-713` |
| MECH-457 | `failure_autopsy_MECH-457-gov-fanout-1-cluster-780-781-782_2026-07-18#V3-EXQ-781` | `failure_autopsy_mech457-retention-portfolio_2026-07-20` |
| MECH-459 | `failure_autopsy_MECH-457-gov-fanout-1-cluster-780-781-782_2026-07-18#V3-EXQ-782` | `failure_autopsy_V3-EXQ-782_2026-07-20` |
| MECH-463 | `failure_autopsy_V3-EXQ-785_2026-07-19` | `failure_autopsy_mech463-exogenous-inertness_2026-07-20#V3-EXQ-785b` |

## Never reviewed (no `last_reviewed`) -- INFO (880 of 901)

Claims with no `last_reviewed` history value -- not yet reviewed under the history plane. `last_reviewed` is record-once and legitimately absent for most claims (seeded from `adjudicated_at_utc`, or set with `apply_live_status.py --mark-reviewed <ID>`). Count + sample only.

Sample: INV-001, INV-002, INV-003, INV-004, INV-005, INV-006, INV-007, INV-008, INV-009, INV-010, INV-011, INV-012, INV-013, INV-014, INV-015, INV-016, INV-017, ARC-001, ARC-002, ARC-004 ...

