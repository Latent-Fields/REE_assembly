# Connectome Literature Pull Queue

Generated: `2026-02-21T15:24:34.336995Z`
Cycle: `2026-02-21`

This queue prioritizes connectome/effective-connectivity evidence pulls for claims under architecture pressure.

Active queue items: `3`. Completed items tracked: `3`.

| pull_id | claim_id | priority | consider_new_structure | conflict_ratio | suggested_literature_type |
|---|---|---|---|---:|---|
| `CPULL-0004` | `MECH-057` | `high` | yes | 0.769 | `targeted_review_connectome_mech_057` |
| `CPULL-0005` | `Q-013` | `high` | yes | 0.727 | `targeted_review_connectome_q_013` |
| `CPULL-0006` | `Q-014` | `high` | yes | 0.727 | `targeted_review_connectome_q_014` |

## MECH-057

- Pull ID: `CPULL-0004`
- Status: `proposed`
- Objective: Run targeted connectome literature pull for MECH-057.
- Claim description: MECH-057 is a mechanism hypothesis about agentic extension / control completion requirement.
- REE fit: This is in REE's mechanism layer and ties architecture commitments to testable signatures. It depends on 5 upstream claim(s): `ARC-015`, `ARC-005`, `ARC-003`, `ARC-004`, `INV-012`. It currently influences 9 downstream claim(s): `IMPL-020`, `IMPL-021`, `IMPL-022`, `IMPL-023`, `MECH-058`, `MECH-059`, `MECH-060`, `Q-012`, `Q-014`. Primary anchor: `docs/architecture/agency_responsibility_flow.md#mech-057`.
- Evidence pressure: conflict_ratio=0.769, overall_confidence=0.705, trigger_signals=external_precedence_pressure,high_conflict_ratio,recurring_failure_signatures.
- Recurring failure signatures: `ledger_editing`, `domination_lock_in`
- Connectome focus: Find connectome-constrained evidence that can confirm, refute, or refine `agentic extension / control completion requirement`.
- Research questions:
  - Which pathways in connectome/effective-connectivity findings are most relevant to this claim's mechanism?
  - What results directly contradict a literal REE mapping of this claim?
  - Which circuit motifs inspire a cleaner architecture split or guardrail in REE?
- Search tracks:
  - `TRK-01` Structural and effective-connectivity constraints; query stems: `MECH-057 connectome effective connectivity`, `agentic extension / control completion requirement neural pathway dissociation`
  - `TRK-02` Computational-neuroscience bridge papers; query stems: `agentic extension / control completion requirement computational neuroscience circuit model`, `MECH-057 predictive coding pathway evidence`
  - `TRK-03` Disconfirming/alternative pathway evidence; query stems: `agentic extension / control completion requirement conflicting neural evidence`, `MECH-057 alternative mechanism neural circuits`
- Completion check: entries_total=0, non_support_entries=0, status_reason=awaiting_connectome_evidence

## Q-013

- Pull ID: `CPULL-0005`
- Status: `proposed`
- Objective: Run targeted connectome literature pull for Q-013.
- Claim description: Q-013 is an open question about uncertainty / deterministic vs stochastic jepa calibration.
- REE fit: This is in REE's uncertainty layer and defines unresolved boundaries before promotion. It depends on 3 upstream claim(s): `MECH-059`, `ARC-005`, `ARC-004`. No downstream claims currently list it as a dependency. Primary anchor: `docs/architecture/agency_responsibility_flow.md#q-013`.
- Evidence pressure: conflict_ratio=0.727, overall_confidence=0.645, trigger_signals=high_conflict_ratio,literature_non_support_pressure,recurring_failure_signatures.
- Recurring failure signatures: `ledger_editing`, `domination_lock_in`
- Connectome focus: Find connectome-constrained evidence that can confirm, refute, or refine `uncertainty / deterministic vs stochastic jepa calibration`.
- Research questions:
  - Which pathways in connectome/effective-connectivity findings are most relevant to this claim's mechanism?
  - What results directly contradict a literal REE mapping of this claim?
  - Which circuit motifs inspire a cleaner architecture split or guardrail in REE?
- Search tracks:
  - `TRK-01` Structural and effective-connectivity constraints; query stems: `Q-013 connectome effective connectivity`, `uncertainty / deterministic vs stochastic jepa calibration neural pathway dissociation`
  - `TRK-02` Computational-neuroscience bridge papers; query stems: `uncertainty / deterministic vs stochastic jepa calibration computational neuroscience circuit model`, `Q-013 predictive coding pathway evidence`
  - `TRK-03` Disconfirming/alternative pathway evidence; query stems: `uncertainty / deterministic vs stochastic jepa calibration conflicting neural evidence`, `Q-013 alternative mechanism neural circuits`
- Completion check: entries_total=0, non_support_entries=0, status_reason=awaiting_connectome_evidence

## Q-014

- Pull ID: `CPULL-0006`
- Status: `proposed`
- Objective: Run targeted connectome literature pull for Q-014.
- Claim description: Q-014 is an open question about invariance / ethical relevance blind spot risk.
- REE fit: This is in REE's uncertainty layer and defines unresolved boundaries before promotion. It depends on 4 upstream claim(s): `MECH-057`, `MECH-059`, `ARC-015`, `ARC-004`. No downstream claims currently list it as a dependency. Primary anchor: `docs/architecture/agency_responsibility_flow.md#q-014`.
- Evidence pressure: conflict_ratio=0.727, overall_confidence=0.645, trigger_signals=high_conflict_ratio,literature_non_support_pressure,recurring_failure_signatures.
- Recurring failure signatures: `ledger_editing`, `domination_lock_in`
- Connectome focus: Find connectome-constrained evidence that can confirm, refute, or refine `invariance / ethical relevance blind spot risk`.
- Research questions:
  - Which pathways in connectome/effective-connectivity findings are most relevant to this claim's mechanism?
  - What results directly contradict a literal REE mapping of this claim?
  - Which circuit motifs inspire a cleaner architecture split or guardrail in REE?
- Search tracks:
  - `TRK-01` Structural and effective-connectivity constraints; query stems: `Q-014 connectome effective connectivity`, `invariance / ethical relevance blind spot risk neural pathway dissociation`
  - `TRK-02` Computational-neuroscience bridge papers; query stems: `invariance / ethical relevance blind spot risk computational neuroscience circuit model`, `Q-014 predictive coding pathway evidence`
  - `TRK-03` Disconfirming/alternative pathway evidence; query stems: `invariance / ethical relevance blind spot risk conflicting neural evidence`, `Q-014 alternative mechanism neural circuits`
- Completion check: entries_total=0, non_support_entries=0, status_reason=awaiting_connectome_evidence

## Completed Pulls

These claims currently satisfy completion criteria and are excluded from the active queue unless reopened.

| pull_id | claim_id | status_reason | conflict_ratio |
|---|---|---|---:|
| `CPULL-0001` | `MECH-060` | completion_criteria_met | 0.875 |
| `CPULL-0002` | `MECH-058` | completion_criteria_met | 0.871 |
| `CPULL-0003` | `Q-017` | completion_criteria_met | 0.848 |

## Copy/Paste Prompt

```md
You are Codex operating in `REE_assembly`.

Goal: execute the current connectome literature pull queue and emit contract-valid literature entries.

Contract requirements:
- `evidence/literature/INTERFACE_CONTRACT.md`
- `evidence/literature/schemas/v1/literature_evidence.schema.json`

Queue items:
- `CPULL-0004` / `MECH-057` / `targeted_review_connectome_mech_057`
- `CPULL-0005` / `Q-013` / `targeted_review_connectome_q_013`
- `CPULL-0006` / `Q-014` / `targeted_review_connectome_q_014`

Per-entry requirements (mandatory):
- preserve source wording in summary and add explicit REE translation
- include mapping fields in `record.json`:
  - `mapping.source_claim_statement`
  - `mapping.ree_translation`
  - `mapping.mapping_caveat`
- include confidence split in `record.json`:
  - `confidence_components.source_quality`
  - `confidence_components.mapping_fidelity`
  - `confidence_components.transfer_risk`
- include at least 3 primary sources and 1 disconfirming/mixed source per claim pull

After entry creation run:
- `python3 evidence/experiments/scripts/build_experiment_indexes.py`
- `python3 evidence/planning/scripts/build_structure_review_dossiers.py`
- `python3 evidence/planning/scripts/build_connectome_literature_pull.py`
- `python3 evidence/planning/scripts/run_governance_cycle.py`
```
