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

## Model-Adjudication Outcomes

For architecture adjudication decisions, use one of these recommendation tokens:

- `retain_ree`
- `hybridize`
- `adopt_jepa_structure`
- `retire_ree_claim`

When a decision is ready to execute, set `decision_status=applied` and run:

```bash
python3 evidence/planning/scripts/apply_adjudication_cascade.py --decision-statuses applied
```

This updates `docs/claims/claims.yaml` (adjudication metadata + dependent reopen cascade) and emits:

- `evidence/decisions/adjudication_cascade_state.v1.json`
- `evidence/planning/ADJUDICATION_CASCADE_PATCH_QUEUE.md`
