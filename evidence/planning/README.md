# Evidence Planning Subsystem

This folder closes the architecture loop by converting current evidence into a machine-readable work queue.

## Generated Outputs

- `evidence_backlog.v1.json`: claims requiring new evidence and why.
- `experiment_proposals.v1.json`: concrete proposed work items for experimental/literature producers.
- `EXPERIMENT_BRIEFS.md`: human-readable explanation of what each experimental proposal tests and why it is routed.
- `architecture_trace_audit.v1.json`: trace-based audit of interface wiring from sensory roots.
- `ARCHITECTURE_TRACE_AUDIT.md`: human-readable architecture trace findings.
- `claim_stub_suggestions.v1.json`: suggested claim stubs for unowned or ambiguous interfaces.
- `INDEX.md`: generated summary.

## Inputs

- `evidence/experiments/claim_evidence.v1.json`
- `evidence/experiments/conflicts.md`
- `evidence/experiments/promotion_demotion_recommendations.md`
- `evidence/experiments/conflict_adjudication.v1.yaml`
- `evidence/decisions/decision_log.v1.jsonl`
- `docs/architecture/interfaces.v1.yaml`
- `docs/claims/interface_ownership.v1.yaml`

## Configuration

- `planning_criteria.v1.yaml`: thresholds and repo-routing hints.

## Generation

```bash
python3 evidence/experiments/scripts/build_experiment_indexes.py
python3 evidence/planning/scripts/architecture_trace_audit.py
```

The planning files are regenerated on each run.
Claim-specific dispatch requirements (for example, `MECH-056` metric keys) are embedded into experimental proposals.
Capability-gated routing can force fallback from default experimental repo to exploratory repo when required producer
capabilities are missing/unknown.

## Governance Cycle Helper

Run non-decision maintenance steps and generate a discussion agenda:

```bash
python3 evidence/planning/scripts/run_governance_cycle.py
```

This helper now runs the architecture trace audit by default. Use `--skip-trace-audit` if needed.

Generated agenda outputs:

- `governance_agenda.v1.json`
- `GOVERNANCE_AGENDA.md`

Strict thought gate mode:

```bash
python3 evidence/planning/scripts/run_governance_cycle.py --strict-thoughts
```
