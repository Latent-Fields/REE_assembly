# Evidence Conflict Report

Generated: `2026-03-18T02:55:24.893431Z`
Conflict scope: `current_epoch_applicable,epoch=ree_hybrid_guardrails_v1`

## Conflict Queue

| claim_id | conflict_types | supports | weakens | conflict_ratio | latest | entries_considered |
|---|---|---|---|---|---|---|
| `ARC-007` | directional | 1 | 1 | 1 | `20260316T061908_path_memory_ablation_v2` | 2 |

## Conflict Details

### ARC-007
- Conflict types: directional
- Evidence breakdown: supports=1, weakens=1, conflict_ratio=1, overall_confidence=0.671
- Recent entries:
  - `2026-03-08T11:46:44.792784+00:00` `experimental` `claim_probe_arc_007` direction=`weakens` confidence=0.75
  - `2026-03-16T06:19:08.594368+00:00` `experimental` `claim_probe_arc_007` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `v2_verdict_fail:path_memory_ablation` (1)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.
