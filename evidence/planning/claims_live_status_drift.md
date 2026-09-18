# Claims live_status Drift Report

Generated: 2026-09-18T18:51:02Z

Mirror of the closure-plan / claims-doc drift reports, for the claims registry's `live_status` status plane (SHP-4). Flags claims whose stored `live_status` block has fallen out of step with the value re-derived from the claim's own current fields (`status` + `v3_pending` + `epistemic_category`). Resolution + derivation are shared with `scripts/apply_live_status.py`. Only the **Reading drift** bucket is a hard signal (fails `--strict`); the rest are review/info hints.

Warn-only by default -- run with `--strict` for a blocking gate.

Claims in registry: 1168

## Reading drift -- HARD (0)

Stored `live_status` != re-derived value. Re-run `scripts/apply_live_status.py`; if it persists, the block was hand-edited or the claim's fields changed without a re-stamp.

_None._

## Unstamped -- SOFT (3)

Registered claims with no `live_status` block. Run `scripts/apply_live_status.py`.

| claim | would-derive |
|-------|--------------|
| MECH-566 | `candidate/v3_pending` |
| MECH-567 | `candidate/v3_pending` |
| MECH-568 | `candidate/v3_pending` |

## Internal inconsistency -- REVIEW (2)

Claims whose own current-state fields contradict each other (`needs_review` true): a promoted status still carrying the V3-pending gate, or a promoted status tagged `substrate_ceiling` (GOV-CEIL-1 floors ceilings to candidate). The derived `live_status` is a best-effort; a human should reconcile the fields.

| claim | derived reading | why |
|-------|-----------------|-----|
| SD-016 | `implemented/substrate_ceiling` | promoted status 'implemented' but epistemic_category substrate_ceiling (GOV-CEIL-1 floors ceilings to candidate) |
| SD-017 | `stable/substrate_ceiling` | promoted status 'stable' but epistemic_category substrate_ceiling (GOV-CEIL-1 floors ceilings to candidate) |

## Event-provenance drift -- SOFT (5)

The `live_status.evidence` sub-block (SHP-4 augmentation: `from` / `as_of` / `verdict`) is projected from the append-only event log via project_status_head. This flags claims whose stored `evidence` block no longer matches the freshly re-projected head -- i.e. a newer autopsy / PASS manifest / decision landed (or one changed) since `apply_live_status.py` last ran. It fluctuates legitimately as the fleet produces evidence, so it is **warn-only and never a --strict failure**: re-run `scripts/apply_live_status.py` (under a TASK_CLAIMS claim on docs/claims/claims.yaml) to refresh. Reading drift (HARD, above) is the gate; provenance drift is a hint.

| claim | stored evidence.from | re-projected from |
|-------|----------------------|-------------------|
| MECH-017 | `_none_` | `failure_autopsy_V3-EXQ-1048_2026-09-17` |
| MECH-019 | `_none_` | `decision:MECH-019@2026-09-17T18:27:48.004829Z` |
| MECH-021 | `_none_` | `failure_autopsy_V3-EXQ-1050_2026-09-18` |
| MECH-482 | `failure_autopsy_V3-EXQ-1047_2026-09-17` | `failure_autopsy_V3-EXQ-1047_2026-09-17` |
| SD-098 | `_none_` | `sd098_ghost_goal_readtime_rerank_20260918T182337Z_v3` |

## Never reviewed (no `last_reviewed`) -- INFO (1147 of 1168)

Claims with no `last_reviewed` history value -- not yet reviewed under the history plane. `last_reviewed` is record-once and legitimately absent for most claims (seeded from `adjudicated_at_utc`, or set with `apply_live_status.py --mark-reviewed <ID>`). Count + sample only.

Sample: INV-001, INV-002, INV-003, INV-004, INV-005, INV-006, INV-007, INV-008, INV-009, INV-010, INV-011, INV-012, INV-013, INV-014, INV-015, INV-016, INV-017, ARC-001, ARC-002, ARC-004 ...

