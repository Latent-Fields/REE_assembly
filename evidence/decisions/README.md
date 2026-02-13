# Decision Log

This folder stores human decisions for promotion/demotion review.

## Files

- `decision_log.v1.jsonl`: append-only human decision log.
- `decision_state.v1.json`: generated latest decision per claim snapshot.
- `schemas/v1/decision_log_entry.schema.json`: reference schema for log entries.

## Why this exists

Generated recommendation files are refreshed every ingestion run.
This log preserves your decisions across regenerations.

## Record a decision

```bash
python3 evidence/experiments/scripts/record_decision.py \
  --claim-id MECH-056 \
  --recommendation hold_candidate_resolve_conflict \
  --decision-needed "Conflict resolution before promotion" \
  --decision-status approved \
  --selected-option "Keep candidate and run conflict-resolution experiments (most balanced)" \
  --rationale "Need one replication sweep before promotion review" \
  --actor dgolden
```

Then refresh indexes:

```bash
python3 evidence/experiments/scripts/build_experiment_indexes.py
```
