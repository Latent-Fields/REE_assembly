# Connectome Literature Pull Queue

Generated: `2026-02-15T21:38:14.184276Z`
Cycle: `2026-02-15`

This queue prioritizes connectome/effective-connectivity evidence pulls for claims under architecture pressure.

| pull_id | claim_id | priority | consider_new_structure | conflict_ratio | suggested_literature_type |
|---|---|---|---|---:|---|
| `CPULL-0001` | `MECH-060` | `high` | yes | 0.895 | `targeted_review_connectome_mech_060` |
| `CPULL-0002` | `MECH-056` | `high` | yes | 0.892 | `targeted_review_connectome_mech_056` |
| `CPULL-0003` | `MECH-058` | `high` | yes | 0.891 | `targeted_review_connectome_mech_058` |
| `CPULL-0004` | `ARC-003` | `high` | yes | 0.889 | `targeted_review_connectome_arc_003` |
| `CPULL-0005` | `MECH-061` | `high` | yes | 0.889 | `targeted_review_connectome_mech_061` |
| `CPULL-0006` | `Q-017` | `high` | yes | 0.879 | `targeted_review_connectome_q_017` |
| `CPULL-0007` | `MECH-040` | `high` | yes | 0.8 | `targeted_review_connectome_mech_040` |
| `CPULL-0008` | `MECH-046` | `high` | yes | 0.8 | `targeted_review_connectome_mech_046` |
| `CPULL-0009` | `Q-012` | `high` | yes | 0.8 | `targeted_review_connectome_q_012` |
| `CPULL-0010` | `Q-013` | `high` | yes | 0.8 | `targeted_review_connectome_q_013` |
| `CPULL-0011` | `Q-014` | `high` | yes | 0.8 | `targeted_review_connectome_q_014` |
| `CPULL-0012` | `Q-015` | `high` | yes | 0.8 | `targeted_review_connectome_q_015` |
| `CPULL-0013` | `MECH-057` | `high` | yes | 0.769 | `targeted_review_connectome_mech_057` |
| `CPULL-0014` | `ARC-007` | `high` | yes | 0.727 | `targeted_review_connectome_arc_007` |
| `CPULL-0015` | `ARC-018` | `high` | yes | 0.714 | `targeted_review_connectome_arc_018` |
| `CPULL-0016` | `MECH-033` | `high` | yes | 0.714 | `targeted_review_connectome_mech_033` |

## MECH-060

- Pull ID: `CPULL-0001`
- Objective: Run targeted connectome literature pull for MECH-060.
- Claim description: MECH-060 is a mechanism hypothesis about commitment / dual error channels pre post commit.
- REE fit: This is in REE's mechanism layer and ties architecture commitments to testable signatures. It depends on 5 upstream claim(s): `ARC-003`, `ARC-005`, `ARC-015`, `INV-012`, `MECH-057`. It currently influences 3 downstream claim(s): `IMPL-023`, `MECH-056`, `MECH-061`. Primary anchor: `docs/architecture/agency_responsibility_flow.md#mech-060`.
- Evidence pressure: conflict_ratio=0.895, overall_confidence=0.7, trigger_signals=external_precedence_pressure,high_conflict_ratio,recurring_failure_signatures.
- Recurring failure signatures: `mech060:postcommit_channel_contamination`, `mech060:attribution_reliability_break`, `mech060:commitment_reversal_spike`, `mech060:precommit_channel_contamination`, `threshold:pre_commit_error_signal_to_noise`
- Connectome focus: Identify circuit evidence for separating planning-time error processing from outcome-attribution learning signals.
- Research questions:
  - Which circuit pathways support pre-decision simulation/error evaluation versus post-outcome attribution updates?
  - Where does evidence indicate partial blending, and what boundary conditions separate channels best?
  - What anatomical or effective-connectivity findings constrain dual-channel implementations?
- Search tracks:
  - `TRK-01` Prefrontal-striatal-thalamic pathways for planning vs attribution; query stems: `prefrontal striatal planning outcome attribution connectivity`, `model-based model-free error pathways effective connectivity`
  - `TRK-02` Commitment and action-monitoring circuit separation; query stems: `anterior cingulate commitment monitoring prediction error channel`, `efference copy outcome evaluation circuit dissociation`
  - `TRK-03` Cross-species connectome findings for dual-channel control; query stems: `cross-species connectome decision learning pathway separation`, `rodent primate planning attribution neural pathway comparison`

## MECH-056

- Pull ID: `CPULL-0002`
- Objective: Run targeted connectome literature pull for MECH-056.
- Claim description: MECH-056 is a mechanism hypothesis about residue / trajectory first placement.
- REE fit: This is in REE's mechanism layer and ties architecture commitments to testable signatures. It depends on 7 upstream claim(s): `ARC-013`, `ARC-018`, `ARC-003`, `ARC-004`, `MECH-034`, `MECH-060`, `MECH-062`. No downstream claims currently list it as a dependency. Primary anchor: `docs/architecture/residue_geometry.md#mech-056`.
- Evidence pressure: conflict_ratio=0.892, overall_confidence=0.749, trigger_signals=external_precedence_pressure,high_conflict_ratio,recurring_failure_signatures.
- Recurring failure signatures: `stop:ledger_edit_detected_count>0`, `ledger_editing`, `stop:domination_lock_in_events>0`, `domination_lock_in`, `stop:explanation_policy_divergence_rate>0.05`
- Connectome focus: Find connectome-constrained evidence that can confirm, refute, or refine `residue / trajectory first placement`.
- Research questions:
  - Which pathways in connectome/effective-connectivity findings are most relevant to this claim's mechanism?
  - What results directly contradict a literal REE mapping of this claim?
  - Which circuit motifs inspire a cleaner architecture split or guardrail in REE?
- Search tracks:
  - `TRK-01` Structural and effective-connectivity constraints; query stems: `MECH-056 connectome effective connectivity`, `residue / trajectory first placement neural pathway dissociation`
  - `TRK-02` Computational-neuroscience bridge papers; query stems: `residue / trajectory first placement computational neuroscience circuit model`, `MECH-056 predictive coding pathway evidence`
  - `TRK-03` Disconfirming/alternative pathway evidence; query stems: `residue / trajectory first placement conflicting neural evidence`, `MECH-056 alternative mechanism neural circuits`

## MECH-058

- Pull ID: `CPULL-0003`
- Objective: Run targeted connectome literature pull for MECH-058.
- Claim description: MECH-058 is a mechanism hypothesis about jepa substrate / ema target anchor timescale separation.
- REE fit: This is in REE's mechanism layer and ties architecture commitments to testable signatures. It depends on 5 upstream claim(s): `ARC-001`, `ARC-002`, `ARC-004`, `ARC-015`, `MECH-057`. It currently influences 1 downstream claim(s): `IMPL-023`. Primary anchor: `docs/architecture/agency_responsibility_flow.md#mech-058`.
- Evidence pressure: conflict_ratio=0.891, overall_confidence=0.709, trigger_signals=external_precedence_pressure,high_conflict_ratio,recurring_failure_signatures.
- Recurring failure signatures: `mech058:anchor_separation_collapse`, `mech058:ema_drift_under_shift`, `mech058:latent_cluster_collapse`, `threshold:latent_prediction_error_mean`, `threshold:latent_prediction_error_p95`
- Connectome focus: Find connectome-constrained evidence that can confirm, refute, or refine `jepa substrate / ema target anchor timescale separation`.
- Research questions:
  - Which pathways in connectome/effective-connectivity findings are most relevant to this claim's mechanism?
  - What results directly contradict a literal REE mapping of this claim?
  - Which circuit motifs inspire a cleaner architecture split or guardrail in REE?
- Search tracks:
  - `TRK-01` Structural and effective-connectivity constraints; query stems: `MECH-058 connectome effective connectivity`, `jepa substrate / ema target anchor timescale separation neural pathway dissociation`
  - `TRK-02` Computational-neuroscience bridge papers; query stems: `jepa substrate / ema target anchor timescale separation computational neuroscience circuit model`, `MECH-058 predictive coding pathway evidence`
  - `TRK-03` Disconfirming/alternative pathway evidence; query stems: `jepa substrate / ema target anchor timescale separation conflicting neural evidence`, `MECH-058 alternative mechanism neural circuits`

## ARC-003

- Pull ID: `CPULL-0004`
- Objective: Run targeted connectome literature pull for ARC-003.
- Claim description: ARC-003 is an architecture commitment about E3 / trajectory commitment.
- REE fit: This is in REE's architecture layer and constrains mechanism choices. It depends on 5 upstream claim(s): `INV-012`, `ARC-001`, `ARC-002`, `ARC-004`, `ARC-005`. It currently influences 23 downstream claim(s): `ARC-007`, `ARC-008`, `ARC-012`, `ARC-014`, `ARC-015`, `ARC-017`, `ARC-018`, `IMPL-003`, `IMPL-004`, `IMPL-016`, `MECH-004`, `MECH-005`, `MECH-008`, `MECH-035`, `MECH-037`, `MECH-049`, `MECH-056`, `MECH-057`, `MECH-060`, `MECH-061`, `MECH-062`, `Q-015`, `Q-016`. Primary anchor: `docs/architecture/e3.md#arc-003`.
- Evidence pressure: conflict_ratio=0.889, overall_confidence=0.665, trigger_signals=external_precedence_pressure,high_conflict_ratio,recurring_failure_signatures.
- Recurring failure signatures: `mech060:postcommit_channel_contamination`, `mech060:attribution_reliability_break`, `mech060:commitment_reversal_spike`
- Connectome focus: Find connectome-constrained evidence that can confirm, refute, or refine `E3 / trajectory commitment`.
- Research questions:
  - Which pathways in connectome/effective-connectivity findings are most relevant to this claim's mechanism?
  - What results directly contradict a literal REE mapping of this claim?
  - Which circuit motifs inspire a cleaner architecture split or guardrail in REE?
- Search tracks:
  - `TRK-01` Structural and effective-connectivity constraints; query stems: `ARC-003 connectome effective connectivity`, `E3 / trajectory commitment neural pathway dissociation`
  - `TRK-02` Computational-neuroscience bridge papers; query stems: `E3 / trajectory commitment computational neuroscience circuit model`, `ARC-003 predictive coding pathway evidence`
  - `TRK-03` Disconfirming/alternative pathway evidence; query stems: `E3 / trajectory commitment conflicting neural evidence`, `ARC-003 alternative mechanism neural circuits`

## MECH-061

- Pull ID: `CPULL-0005`
- Objective: Run targeted connectome literature pull for MECH-061.
- Claim description: MECH-061 is a mechanism hypothesis about commitment / boundary token error reclassification.
- REE fit: This is in REE's mechanism layer and ties architecture commitments to testable signatures. It depends on 4 upstream claim(s): `ARC-003`, `ARC-015`, `INV-012`, `MECH-060`. It currently influences 4 downstream claim(s): `IMPL-023`, `IMPL-025`, `MECH-062`, `Q-015`. Primary anchor: `docs/architecture/e3.md#mech-061`.
- Evidence pressure: conflict_ratio=0.889, overall_confidence=0.654, trigger_signals=external_precedence_pressure,high_conflict_ratio,recurring_failure_signatures.
- Recurring failure signatures: `mech060:postcommit_channel_contamination`, `mech060:attribution_reliability_break`, `mech060:commitment_reversal_spike`
- Connectome focus: Find connectome-constrained evidence that can confirm, refute, or refine `commitment / boundary token error reclassification`.
- Research questions:
  - Which pathways in connectome/effective-connectivity findings are most relevant to this claim's mechanism?
  - What results directly contradict a literal REE mapping of this claim?
  - Which circuit motifs inspire a cleaner architecture split or guardrail in REE?
- Search tracks:
  - `TRK-01` Structural and effective-connectivity constraints; query stems: `MECH-061 connectome effective connectivity`, `commitment / boundary token error reclassification neural pathway dissociation`
  - `TRK-02` Computational-neuroscience bridge papers; query stems: `commitment / boundary token error reclassification computational neuroscience circuit model`, `MECH-061 predictive coding pathway evidence`
  - `TRK-03` Disconfirming/alternative pathway evidence; query stems: `commitment / boundary token error reclassification conflicting neural evidence`, `MECH-061 alternative mechanism neural circuits`

## Q-017

- Pull ID: `CPULL-0006`
- Objective: Run targeted connectome literature pull for Q-017.
- Claim description: Q-017 is an open question about control plane / minimal orthogonal axis set.
- REE fit: This is in REE's uncertainty layer and defines unresolved boundaries before promotion. It depends on 3 upstream claim(s): `MECH-063`, `ARC-005`, `MECH-055`. No downstream claims currently list it as a dependency. Primary anchor: `docs/architecture/control_plane.md#q-017`.
- Evidence pressure: conflict_ratio=0.879, overall_confidence=0.711, trigger_signals=external_precedence_pressure,high_conflict_ratio,recurring_failure_signatures.
- Recurring failure signatures: `q017:control_axis_stability_drop`, `q017:control_axis_entropy_collapse`, `q017:control_axis_policy_loss_spike`
- Connectome focus: Find connectome-constrained evidence that can confirm, refute, or refine `control plane / minimal orthogonal axis set`.
- Research questions:
  - Which pathways in connectome/effective-connectivity findings are most relevant to this claim's mechanism?
  - What results directly contradict a literal REE mapping of this claim?
  - Which circuit motifs inspire a cleaner architecture split or guardrail in REE?
- Search tracks:
  - `TRK-01` Structural and effective-connectivity constraints; query stems: `Q-017 connectome effective connectivity`, `control plane / minimal orthogonal axis set neural pathway dissociation`
  - `TRK-02` Computational-neuroscience bridge papers; query stems: `control plane / minimal orthogonal axis set computational neuroscience circuit model`, `Q-017 predictive coding pathway evidence`
  - `TRK-03` Disconfirming/alternative pathway evidence; query stems: `control plane / minimal orthogonal axis set conflicting neural evidence`, `Q-017 alternative mechanism neural circuits`

## MECH-040

- Pull ID: `CPULL-0007`
- Objective: Run targeted connectome literature pull for MECH-040.
- Claim description: MECH-040 is a mechanism hypothesis about control plane / safety baseline volatility.
- REE fit: This is in REE's mechanism layer and ties architecture commitments to testable signatures. It depends on 3 upstream claim(s): `ARC-005`, `MECH-005`, `MECH-019`. It currently influences 3 downstream claim(s): `MECH-042`, `MECH-063`, `Q-007`. Primary anchor: `docs/architecture/control_plane.md#mech-040`.
- Evidence pressure: conflict_ratio=0.8, overall_confidence=0.637, trigger_signals=external_precedence_pressure,high_conflict_ratio,recurring_failure_signatures.
- Recurring failure signatures: `ledger_editing`, `domination_lock_in`
- Connectome focus: Find connectome-constrained evidence that can confirm, refute, or refine `control plane / safety baseline volatility`.
- Research questions:
  - Which pathways in connectome/effective-connectivity findings are most relevant to this claim's mechanism?
  - What results directly contradict a literal REE mapping of this claim?
  - Which circuit motifs inspire a cleaner architecture split or guardrail in REE?
- Search tracks:
  - `TRK-01` Structural and effective-connectivity constraints; query stems: `MECH-040 connectome effective connectivity`, `control plane / safety baseline volatility neural pathway dissociation`
  - `TRK-02` Computational-neuroscience bridge papers; query stems: `control plane / safety baseline volatility computational neuroscience circuit model`, `MECH-040 predictive coding pathway evidence`
  - `TRK-03` Disconfirming/alternative pathway evidence; query stems: `control plane / safety baseline volatility conflicting neural evidence`, `MECH-040 alternative mechanism neural circuits`

## MECH-046

- Pull ID: `CPULL-0008`
- Objective: Run targeted connectome literature pull for MECH-046.
- Claim description: MECH-046 is a mechanism hypothesis about control plane / amygdala mode priors.
- REE fit: This is in REE's mechanism layer and ties architecture commitments to testable signatures. It depends on 2 upstream claim(s): `ARC-005`, `MECH-039`. It currently influences 1 downstream claim(s): `MECH-047`. Primary anchor: `docs/architecture/control_plane.md#mech-046`.
- Evidence pressure: conflict_ratio=0.8, overall_confidence=0.627, trigger_signals=external_precedence_pressure,high_conflict_ratio,recurring_failure_signatures.
- Recurring failure signatures: `ledger_editing`, `domination_lock_in`
- Connectome focus: Find connectome-constrained evidence that can confirm, refute, or refine `control plane / amygdala mode priors`.
- Research questions:
  - Which pathways in connectome/effective-connectivity findings are most relevant to this claim's mechanism?
  - What results directly contradict a literal REE mapping of this claim?
  - Which circuit motifs inspire a cleaner architecture split or guardrail in REE?
- Search tracks:
  - `TRK-01` Structural and effective-connectivity constraints; query stems: `MECH-046 connectome effective connectivity`, `control plane / amygdala mode priors neural pathway dissociation`
  - `TRK-02` Computational-neuroscience bridge papers; query stems: `control plane / amygdala mode priors computational neuroscience circuit model`, `MECH-046 predictive coding pathway evidence`
  - `TRK-03` Disconfirming/alternative pathway evidence; query stems: `control plane / amygdala mode priors conflicting neural evidence`, `MECH-046 alternative mechanism neural circuits`

## Q-012

- Pull ID: `CPULL-0009`
- Objective: Run targeted connectome literature pull for Q-012.
- Claim description: Q-012 is an open question about latent predictive models / control completion falsifiability.
- REE fit: This is in REE's uncertainty layer and defines unresolved boundaries before promotion. It depends on 4 upstream claim(s): `MECH-057`, `ARC-015`, `ARC-005`, `ARC-004`. No downstream claims currently list it as a dependency. Primary anchor: `docs/architecture/agency_responsibility_flow.md#q-012`.
- Evidence pressure: conflict_ratio=0.8, overall_confidence=0.66, trigger_signals=external_precedence_pressure,high_conflict_ratio,recurring_failure_signatures.
- Recurring failure signatures: `ledger_editing`, `domination_lock_in`
- Connectome focus: Find connectome-constrained evidence that can confirm, refute, or refine `latent predictive models / control completion falsifiability`.
- Research questions:
  - Which pathways in connectome/effective-connectivity findings are most relevant to this claim's mechanism?
  - What results directly contradict a literal REE mapping of this claim?
  - Which circuit motifs inspire a cleaner architecture split or guardrail in REE?
- Search tracks:
  - `TRK-01` Structural and effective-connectivity constraints; query stems: `Q-012 connectome effective connectivity`, `latent predictive models / control completion falsifiability neural pathway dissociation`
  - `TRK-02` Computational-neuroscience bridge papers; query stems: `latent predictive models / control completion falsifiability computational neuroscience circuit model`, `Q-012 predictive coding pathway evidence`
  - `TRK-03` Disconfirming/alternative pathway evidence; query stems: `latent predictive models / control completion falsifiability conflicting neural evidence`, `Q-012 alternative mechanism neural circuits`

## Q-013

- Pull ID: `CPULL-0010`
- Objective: Run targeted connectome literature pull for Q-013.
- Claim description: Q-013 is an open question about uncertainty / deterministic vs stochastic jepa calibration.
- REE fit: This is in REE's uncertainty layer and defines unresolved boundaries before promotion. It depends on 3 upstream claim(s): `MECH-059`, `ARC-005`, `ARC-004`. No downstream claims currently list it as a dependency. Primary anchor: `docs/architecture/agency_responsibility_flow.md#q-013`.
- Evidence pressure: conflict_ratio=0.8, overall_confidence=0.634, trigger_signals=high_conflict_ratio,literature_non_support_pressure,recurring_failure_signatures.
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

## Q-014

- Pull ID: `CPULL-0011`
- Objective: Run targeted connectome literature pull for Q-014.
- Claim description: Q-014 is an open question about invariance / ethical relevance blind spot risk.
- REE fit: This is in REE's uncertainty layer and defines unresolved boundaries before promotion. It depends on 4 upstream claim(s): `MECH-057`, `MECH-059`, `ARC-015`, `ARC-004`. No downstream claims currently list it as a dependency. Primary anchor: `docs/architecture/agency_responsibility_flow.md#q-014`.
- Evidence pressure: conflict_ratio=0.8, overall_confidence=0.634, trigger_signals=high_conflict_ratio,literature_non_support_pressure,recurring_failure_signatures.
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

## Q-015

- Pull ID: `CPULL-0012`
- Objective: Run targeted connectome literature pull for Q-015.
- Claim description: Q-015 is an open question about commitment / boundary token minimal contract.
- REE fit: This is in REE's uncertainty layer and defines unresolved boundaries before promotion. It depends on 3 upstream claim(s): `MECH-061`, `ARC-003`, `ARC-015`. No downstream claims currently list it as a dependency. Primary anchor: `docs/architecture/e3.md#q-015`.
- Evidence pressure: conflict_ratio=0.8, overall_confidence=0.616, trigger_signals=external_precedence_pressure,high_conflict_ratio,recurring_failure_signatures.
- Recurring failure signatures: `ledger_editing`, `domination_lock_in`
- Connectome focus: Find connectome-constrained evidence that can confirm, refute, or refine `commitment / boundary token minimal contract`.
- Research questions:
  - Which pathways in connectome/effective-connectivity findings are most relevant to this claim's mechanism?
  - What results directly contradict a literal REE mapping of this claim?
  - Which circuit motifs inspire a cleaner architecture split or guardrail in REE?
- Search tracks:
  - `TRK-01` Structural and effective-connectivity constraints; query stems: `Q-015 connectome effective connectivity`, `commitment / boundary token minimal contract neural pathway dissociation`
  - `TRK-02` Computational-neuroscience bridge papers; query stems: `commitment / boundary token minimal contract computational neuroscience circuit model`, `Q-015 predictive coding pathway evidence`
  - `TRK-03` Disconfirming/alternative pathway evidence; query stems: `commitment / boundary token minimal contract conflicting neural evidence`, `Q-015 alternative mechanism neural circuits`

## MECH-057

- Pull ID: `CPULL-0013`
- Objective: Run targeted connectome literature pull for MECH-057.
- Claim description: MECH-057 is a mechanism hypothesis about agentic extension / control completion requirement.
- REE fit: This is in REE's mechanism layer and ties architecture commitments to testable signatures. It depends on 5 upstream claim(s): `ARC-015`, `ARC-005`, `ARC-003`, `ARC-004`, `INV-012`. It currently influences 9 downstream claim(s): `IMPL-020`, `IMPL-021`, `IMPL-022`, `IMPL-023`, `MECH-058`, `MECH-059`, `MECH-060`, `Q-012`, `Q-014`. Primary anchor: `docs/architecture/agency_responsibility_flow.md#mech-057`.
- Evidence pressure: conflict_ratio=0.769, overall_confidence=0.712, trigger_signals=external_precedence_pressure,high_conflict_ratio,recurring_failure_signatures.
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

## ARC-007

- Pull ID: `CPULL-0014`
- Objective: Run targeted connectome literature pull for ARC-007.
- Claim description: ARC-007 is an architecture commitment about hippocampus / path memory.
- REE fit: This is in REE's architecture layer and constrains mechanism choices. It depends on 2 upstream claim(s): `ARC-004`, `ARC-003`. It currently influences 17 downstream claim(s): `ARC-011`, `ARC-012`, `ARC-014`, `ARC-015`, `ARC-018`, `ARC-019`, `IMPL-004`, `IMPL-005`, `IMPL-019`, `MECH-016`, `MECH-017`, `MECH-018`, `MECH-022`, `MECH-029`, `MECH-030`, `MECH-037`, `MECH-044`. Primary anchor: `docs/architecture/hippocampal_systems.md#arc-007`.
- Evidence pressure: conflict_ratio=0.727, overall_confidence=0.647, trigger_signals=external_precedence_pressure,high_conflict_ratio,recurring_failure_signatures.
- Recurring failure signatures: `ledger_editing`, `domination_lock_in`
- Connectome focus: Find connectome-constrained evidence that can confirm, refute, or refine `hippocampus / path memory`.
- Research questions:
  - Which pathways in connectome/effective-connectivity findings are most relevant to this claim's mechanism?
  - What results directly contradict a literal REE mapping of this claim?
  - Which circuit motifs inspire a cleaner architecture split or guardrail in REE?
- Search tracks:
  - `TRK-01` Structural and effective-connectivity constraints; query stems: `ARC-007 connectome effective connectivity`, `hippocampus / path memory neural pathway dissociation`
  - `TRK-02` Computational-neuroscience bridge papers; query stems: `hippocampus / path memory computational neuroscience circuit model`, `ARC-007 predictive coding pathway evidence`
  - `TRK-03` Disconfirming/alternative pathway evidence; query stems: `hippocampus / path memory conflicting neural evidence`, `ARC-007 alternative mechanism neural circuits`

## ARC-018

- Pull ID: `CPULL-0015`
- Objective: Run targeted connectome literature pull for ARC-018.
- Claim description: ARC-018 is an architecture commitment about hippocampus / rollout viability mapping.
- REE fit: This is in REE's architecture layer and constrains mechanism choices. It depends on 4 upstream claim(s): `ARC-007`, `ARC-003`, `ARC-002`, `ARC-001`. It currently influences 8 downstream claim(s): `IMPL-004`, `IMPL-005`, `MECH-033`, `MECH-034`, `MECH-037`, `MECH-038`, `MECH-056`, `Q-011`. Primary anchor: `docs/architecture/hippocampal_systems.md#arc-018`.
- Evidence pressure: conflict_ratio=0.714, overall_confidence=0.664, trigger_signals=external_precedence_pressure,high_conflict_ratio,recurring_failure_signatures.
- Recurring failure signatures: `ledger_editing`, `domination_lock_in`
- Connectome focus: Find connectome-constrained evidence that can confirm, refute, or refine `hippocampus / rollout viability mapping`.
- Research questions:
  - Which pathways in connectome/effective-connectivity findings are most relevant to this claim's mechanism?
  - What results directly contradict a literal REE mapping of this claim?
  - Which circuit motifs inspire a cleaner architecture split or guardrail in REE?
- Search tracks:
  - `TRK-01` Structural and effective-connectivity constraints; query stems: `ARC-018 connectome effective connectivity`, `hippocampus / rollout viability mapping neural pathway dissociation`
  - `TRK-02` Computational-neuroscience bridge papers; query stems: `hippocampus / rollout viability mapping computational neuroscience circuit model`, `ARC-018 predictive coding pathway evidence`
  - `TRK-03` Disconfirming/alternative pathway evidence; query stems: `hippocampus / rollout viability mapping conflicting neural evidence`, `ARC-018 alternative mechanism neural circuits`

## MECH-033

- Pull ID: `CPULL-0016`
- Objective: Run targeted connectome literature pull for MECH-033.
- Claim description: MECH-033 is a mechanism hypothesis about hippocampus / kernel chaining interface.
- REE fit: This is in REE's mechanism layer and ties architecture commitments to testable signatures. It depends on 4 upstream claim(s): `ARC-018`, `ARC-002`, `ARC-001`, `ARC-005`. No downstream claims currently list it as a dependency. Primary anchor: `docs/architecture/hippocampal_systems.md#mech-033`.
- Evidence pressure: conflict_ratio=0.714, overall_confidence=0.662, trigger_signals=external_precedence_pressure,high_conflict_ratio,recurring_failure_signatures.
- Recurring failure signatures: `ledger_editing`, `domination_lock_in`
- Connectome focus: Find connectome-constrained evidence that can confirm, refute, or refine `hippocampus / kernel chaining interface`.
- Research questions:
  - Which pathways in connectome/effective-connectivity findings are most relevant to this claim's mechanism?
  - What results directly contradict a literal REE mapping of this claim?
  - Which circuit motifs inspire a cleaner architecture split or guardrail in REE?
- Search tracks:
  - `TRK-01` Structural and effective-connectivity constraints; query stems: `MECH-033 connectome effective connectivity`, `hippocampus / kernel chaining interface neural pathway dissociation`
  - `TRK-02` Computational-neuroscience bridge papers; query stems: `hippocampus / kernel chaining interface computational neuroscience circuit model`, `MECH-033 predictive coding pathway evidence`
  - `TRK-03` Disconfirming/alternative pathway evidence; query stems: `hippocampus / kernel chaining interface conflicting neural evidence`, `MECH-033 alternative mechanism neural circuits`

## Copy/Paste Prompt

```md
You are Codex operating in `REE_assembly`.

Goal: execute the current connectome literature pull queue and emit contract-valid literature entries.

Contract requirements:
- `evidence/literature/INTERFACE_CONTRACT.md`
- `evidence/literature/schemas/v1/literature_evidence.schema.json`

Queue items:
- `CPULL-0001` / `MECH-060` / `targeted_review_connectome_mech_060`
- `CPULL-0002` / `MECH-056` / `targeted_review_connectome_mech_056`
- `CPULL-0003` / `MECH-058` / `targeted_review_connectome_mech_058`
- `CPULL-0004` / `ARC-003` / `targeted_review_connectome_arc_003`
- `CPULL-0005` / `MECH-061` / `targeted_review_connectome_mech_061`
- `CPULL-0006` / `Q-017` / `targeted_review_connectome_q_017`
- `CPULL-0007` / `MECH-040` / `targeted_review_connectome_mech_040`
- `CPULL-0008` / `MECH-046` / `targeted_review_connectome_mech_046`
- `CPULL-0009` / `Q-012` / `targeted_review_connectome_q_012`
- `CPULL-0010` / `Q-013` / `targeted_review_connectome_q_013`
- `CPULL-0011` / `Q-014` / `targeted_review_connectome_q_014`
- `CPULL-0012` / `Q-015` / `targeted_review_connectome_q_015`
- `CPULL-0013` / `MECH-057` / `targeted_review_connectome_mech_057`
- `CPULL-0014` / `ARC-007` / `targeted_review_connectome_arc_007`
- `CPULL-0015` / `ARC-018` / `targeted_review_connectome_arc_018`
- `CPULL-0016` / `MECH-033` / `targeted_review_connectome_mech_033`

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
