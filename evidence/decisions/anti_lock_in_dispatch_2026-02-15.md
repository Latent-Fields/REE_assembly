# Anti-Lock-In Decision Dispatch (2026-02-15)

Generated: `2026-02-15T18:43:48Z`

Purpose: focused human adjudication packet for claims currently flagged with `anti_lock_in_review_required`.

## Recommended Outcomes

| claim_id | conflict_ratio | lit-exp delta | overall_conf | latest_decision_status | recommended_outcome | basis |
| --- | ---: | ---: | ---: | --- | --- | --- |
| `Q-017` | `0.967` | `None` | `0.72` | `none` | `hybridize` | `high_conflict` |
| `MECH-058` | `0.947` | `None` | `0.707` | `applied` | `hybridize` | `already_applied` |
| `MECH-060` | `0.944` | `None` | `0.692` | `approved` | `hybridize` | `high_conflict` |
| `ARC-007` | `0.857` | `None` | `0.58` | `none` | `hybridize` | `high_conflict` |
| `MECH-056` | `0.85` | `None` | `0.761` | `applied` | `hybridize` | `already_applied` |
| `ARC-003` | `0.667` | `None` | `0.597` | `none` | `retain_ree` | `conflict_below_hybrid_threshold` |
| `MECH-040` | `0.667` | `None` | `0.607` | `none` | `retain_ree` | `conflict_below_hybrid_threshold` |
| `MECH-046` | `0.667` | `None` | `0.597` | `none` | `retain_ree` | `conflict_below_hybrid_threshold` |
| `MECH-061` | `0.667` | `None` | `0.586` | `none` | `retain_ree` | `conflict_below_hybrid_threshold` |
| `Q-012` | `0.667` | `None` | `0.634` | `none` | `retain_ree` | `conflict_below_hybrid_threshold` |
| `Q-015` | `0.667` | `None` | `0.586` | `none` | `retain_ree` | `conflict_below_hybrid_threshold` |
| `ARC-018` | `0.6` | `None` | `0.639` | `none` | `retain_ree` | `conflict_below_hybrid_threshold` |
| `MECH-033` | `0.6` | `None` | `0.637` | `none` | `retain_ree` | `conflict_below_hybrid_threshold` |
| `MECH-059` | `0.588` | `None` | `0.767` | `approved` | `retain_ree` | `conflict_below_hybrid_threshold` |

## Execution Notes

- This packet does not auto-apply outcomes; it dispatches explicit recommendations for user approval/application.
- To apply, append `decision_log.v1.jsonl` entries with `decision_status: applied` and recommendation in `{retain_ree, hybridize, adopt_jepa_structure, retire_ree_claim}`, then run governance cycle.
- Use `adopt_jepa_structure` / `retire_ree_claim` only when you want claim status transitioned to `legacy` and dependency cascade reopening to trigger.
