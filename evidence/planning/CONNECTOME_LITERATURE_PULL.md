# Connectome Literature Pull Queue

Generated: `2026-02-21T17:40:43.408298Z`
Cycle: `2026-02-21`

This queue prioritizes connectome/effective-connectivity evidence pulls for claims under architecture pressure.

Active queue items: `7`. Completed items tracked: `5`.

| pull_id | claim_id | priority | consider_new_structure | conflict_ratio | suggested_literature_type |
|---|---|---|---|---:|---|
| `CPULL-0003` | `MECH-026` | `high` | no | 0 | `targeted_review_connectome_mech_026` |
| `CPULL-0004` | `MECH-029` | `high` | no | 0 | `targeted_review_connectome_mech_029` |
| `CPULL-0005` | `MECH-030` | `high` | no | 0 | `targeted_review_connectome_mech_030` |
| `CPULL-0006` | `MECH-047` | `high` | no | 0 | `targeted_review_connectome_mech_047` |
| `CPULL-0010` | `MECH-057` | `high` | yes | 0.769 | `targeted_review_connectome_mech_057` |
| `CPULL-0011` | `Q-013` | `high` | yes | 0.727 | `targeted_review_connectome_q_013` |
| `CPULL-0012` | `Q-014` | `high` | yes | 0.727 | `targeted_review_connectome_q_014` |

## MECH-026

- Pull ID: `CPULL-0003`
- Status: `proposed`
- Objective: Run targeted connectome literature pull for MECH-026.
- Claim description: MECH-026 is a mechanism hypothesis about cognitive modes / ready vigilance.
- REE fit: This is in REE's mechanism layer and ties architecture commitments to testable signatures. It depends on 2 upstream claim(s): `ARC-016`, `ARC-005`. No downstream claims currently list it as a dependency. Primary anchor: `docs/architecture/modes_of_cognition.md#mech-026`.
- Evidence pressure: conflict_ratio=0, overall_confidence=0.5, trigger_signals=manual_mode_transition_pull.
- Connectome focus: Disambiguate ready-vigilance from action commitment using inhibitory priming and salience routing evidence.
- Research questions:
  - Which circuits express high sensitivity/priming while still suppressing motor release?
  - What signatures separate restraint-oriented vigilance from imminent action preparation?
  - What evidence suggests vigilance and action are not cleanly dissociable?
- Search tracks:
  - `TRK-01` Inhibitory control and orienting circuits; query stems: `ready vigilance inhibitory control network`, `orienting salience motor inhibition effective connectivity`
  - `TRK-02` Threat/salience and restraint coupling; query stems: `threat vigilance without action neural circuits`, `salience network motor suppression pathways`
  - `TRK-03` Boundary cases between vigilance and action; query stems: `hypervigilance transition to action neural markers`, `false alarm motor gating neural evidence`
- Completion check: entries_total=0, non_support_entries=0, status_reason=awaiting_connectome_evidence

## MECH-029

- Pull ID: `CPULL-0004`
- Status: `proposed`
- Objective: Run targeted connectome literature pull for MECH-029.
- Claim description: MECH-029 is a mechanism hypothesis about default mode / reflective ethics.
- REE fit: This is in REE's mechanism layer and ties architecture commitments to testable signatures. It depends on 3 upstream claim(s): `ARC-014`, `ARC-005`, `ARC-007`. No downstream claims currently list it as a dependency. Primary anchor: `docs/architecture/default_mode.md#mech-029`.
- Evidence pressure: conflict_ratio=0, overall_confidence=0.5, trigger_signals=manual_mode_transition_pull.
- Connectome focus: Test DMN-like reflective replay constraints against action-network suppression and hippocampal-cortical coupling.
- Research questions:
  - Which data best supports DMN-like reflective replay with commitment suppression?
  - How strong is evidence for hippocampal-cortical coupling during internally generated simulation?
  - Where does DMN activity fail to support safe replay assumptions?
- Search tracks:
  - `TRK-01` DMN architecture and anti-correlation with action networks; query stems: `default mode network anti-correlation task positive network`, `DMN executive control dynamic coupling transitions`
  - `TRK-02` Hippocampal replay and autobiographical simulation; query stems: `hippocampal cortical replay default mode simulation`, `episodic future thinking hippocampus default mode`
  - `TRK-03` DMN instability/pathology boundary evidence; query stems: `rumination default mode control failure connectivity`, `psychosis default mode internal model intrusion evidence`
- Completion check: entries_total=0, non_support_entries=0, status_reason=awaiting_connectome_evidence

## MECH-030

- Pull ID: `CPULL-0005`
- Status: `proposed`
- Objective: Run targeted connectome literature pull for MECH-030.
- Claim description: MECH-030 is a mechanism hypothesis about sleep / modes consolidation.
- REE fit: This is in REE's mechanism layer and ties architecture commitments to testable signatures. It depends on 4 upstream claim(s): `ARC-011`, `ARC-005`, `ARC-007`, `INV-010`. No downstream claims currently list it as a dependency. Primary anchor: `docs/architecture/sleep.md#mech-030`.
- Evidence pressure: conflict_ratio=0, overall_confidence=0.5, trigger_signals=manual_mode_transition_pull.
- Connectome focus: Constrain sleep/offline consolidation mode assumptions with replay, renormalization, and boundary-protection evidence.
- Research questions:
  - Which sleep-stage mechanisms support consolidation without online commit leakage?
  - What evidence supports replay-driven integration across modes?
  - Which findings suggest offline updates can distort rather than stabilize mode boundaries?
- Search tracks:
  - `TRK-01` Sleep replay and consolidation pathways; query stems: `sleep replay hippocampal cortical consolidation pathways`, `sleep stage memory consolidation network connectivity`
  - `TRK-02` Precision recalibration and homeostatic renormalization; query stems: `sleep synaptic homeostasis precision recalibration`, `offline neural renormalization predictive processing`
  - `TRK-03` Failure signatures of offline integration; query stems: `sleep disturbance mode switching instability`, `maladaptive consolidation replay bias evidence`
- Completion check: entries_total=0, non_support_entries=0, status_reason=awaiting_connectome_evidence

## MECH-047

- Pull ID: `CPULL-0006`
- Status: `proposed`
- Objective: Run targeted connectome literature pull for MECH-047.
- Claim description: MECH-047 is a mechanism hypothesis about control plane / precommitment mode manager.
- REE fit: This is in REE's mechanism layer and ties architecture commitments to testable signatures. It depends on 2 upstream claim(s): `ARC-005`, `MECH-046`. No downstream claims currently list it as a dependency. Primary anchor: `docs/architecture/mode_manager.md#mech-047`.
- Evidence pressure: conflict_ratio=0, overall_confidence=0.5, trigger_signals=manual_mode_transition_pull.
- Connectome focus: Evaluate mode-commitment hysteresis and switching-cost hypotheses with state-transition neuroscience evidence.
- Research questions:
  - What evidence supports hysteresis-like switching inertia in brain state transitions?
  - Which control variables predict stable mode commitment versus thrash?
  - Where does evidence support continuous adaptation over explicit switching-cost dynamics?
- Search tracks:
  - `TRK-01` State-transition and metastability analyses; query stems: `brain state transition hysteresis metastability`, `dynamic functional connectivity state switching costs`
  - `TRK-02` Salience/LC-NE and transition gating; query stems: `locus coeruleus salience network state transitions`, `arousal modulation cognitive state switching`
  - `TRK-03` Disconfirming evidence for explicit mode manager dynamics; query stems: `continuous control model cognitive state dynamics evidence`, `noisy manifold transitions versus discrete states`
- Completion check: entries_total=0, non_support_entries=0, status_reason=awaiting_connectome_evidence

## MECH-057

- Pull ID: `CPULL-0010`
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

- Pull ID: `CPULL-0011`
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

- Pull ID: `CPULL-0012`
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
| `CPULL-0001` | `ARC-016` | completion_criteria_met | 0 |
| `CPULL-0002` | `MECH-025` | completion_criteria_met | 0 |
| `CPULL-0007` | `MECH-060` | completion_criteria_met | 0.875 |
| `CPULL-0008` | `MECH-058` | completion_criteria_met | 0.871 |
| `CPULL-0009` | `Q-017` | completion_criteria_met | 0.848 |

## Copy/Paste Prompt

```md
You are Codex operating in `REE_assembly`.

Goal: execute the current connectome literature pull queue and emit contract-valid literature entries.

Contract requirements:
- `evidence/literature/INTERFACE_CONTRACT.md`
- `evidence/literature/schemas/v1/literature_evidence.schema.json`

Queue items:
- `CPULL-0003` / `MECH-026` / `targeted_review_connectome_mech_026`
- `CPULL-0004` / `MECH-029` / `targeted_review_connectome_mech_029`
- `CPULL-0005` / `MECH-030` / `targeted_review_connectome_mech_030`
- `CPULL-0006` / `MECH-047` / `targeted_review_connectome_mech_047`
- `CPULL-0010` / `MECH-057` / `targeted_review_connectome_mech_057`
- `CPULL-0011` / `Q-013` / `targeted_review_connectome_q_013`
- `CPULL-0012` / `Q-014` / `targeted_review_connectome_q_014`

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
