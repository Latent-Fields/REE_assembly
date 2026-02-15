# Structure Review Dossier: MECH-059

Generated: `2026-02-15T15:32:10.296348Z`
Cycle: `2026-02-15`

## Claim Description

MECH-059 is a mechanism hypothesis about precision / confidence channel separate from prediction error.

## Where This Fits in REE as a Whole

This sits in REE's mechanism layer and links architecture commitments to testable signatures. It depends on 5 upstream claim(s): `ARC-005`, `ARC-004`, `ARC-015`, `MECH-054`, `MECH-057`. It currently feeds 3 downstream claim(s): `IMPL-023`, `Q-013`, `Q-014`. Primary architecture anchor: `docs/architecture/agency_responsibility_flow.md#mech-059`.

## Structural Pressure Signals

- Recommendation: `consider_new_structure` (consider_new_structure=true)
- Trigger signals: external_precedence_pressure, high_conflict_ratio, recurring_failure_signatures
- Conflict ratio: 0.704
- Overall confidence: 0.737

## Evidence Mix and Why It Looks This Way

- Direction counts: supports=35, weakens=19, mixed=14, unknown=0.
- Experimental mix: supports=31, weakens=19, mixed=12, unknown=0.
- Literature mix: supports=4, weakens=0, mixed=2, unknown=0.
- Direction narrative: Evidence is directionally split between support and weakening, which indicates either claim over-breadth or hidden context dependence.
- Source narrative: Both experiment and literature are present. Use disagreement between these sources as a cue to refine claim scope before making status promotions.

## Evidence Pull (Current Findings + Alternatives)

| alternative | confidence_estimate | current_findings | next_pull_focus |
|---|---:|---|---|
| precision / confidence channel separate from prediction error is broadly correct, but failures are boundary-condition failures. | 0.552 | Supporting evidence dominates enough to keep the core mechanism plausible. | Target stress regimes where failures cluster and test whether boundary constraints recover stability.; Pull replication papers that test similar mechanisms under distribution shift. |
| precision / confidence channel separate from prediction error is over-scoped and should be narrowed or split. | 0.29 | Weakening evidence indicates at least one sub-regime where the current claim phrasing breaks. | Extract disconfirming sources and isolate the exact violated assumption.; Run claim-splitting experiments with explicit sub-claim tags in manifests. |
| A hybrid architecture is needed: keep the core of precision / confidence channel separate from prediction error but add explicit gating or interface separation. | 0.29 | Mixed evidence and conflict patterns suggest partial validity with missing structural guardrails. | Evaluate an ablation that isolates the proposed guardrail/interface addition.; Collect one adjacent-domain source that uses a similar split architecture. |

## Source Wording vs REE Translation

| timestamp | source | direction | confidence | evidence wording (preserved) | REE translation |
|---|---|---|---:|---|---|
| `2026-02-15T16:04:00Z` | What Uncertainties Do We Need in Bayesian Deep Learning for Computer Vision? (2017, NeurIPS) | `supports` | 0.67 | Explicit decomposition of aleatoric and epistemic uncertainty supports separating precision/uncertainty streams from residual prediction error, but is not JEPA-specific. Follow-up extraction scoped to MECH-059 confidence-channel decomposition. Proposal completion extraction for LIT-0019 scoped to MECH-059. | In REE terms, this is positive pressure on `precision / confidence channel separate from prediction error` and supports keeping the mechanism, with tighter boundary conditions where failures recur. |
| `2026-02-15T15:15:00Z` | What Uncertainties Do We Need in Bayesian Deep Learning for Computer Vision? (2017, NeurIPS) | `supports` | 0.67 | Explicit decomposition of aleatoric and epistemic uncertainty supports separating precision/uncertainty streams from residual prediction error, but is not JEPA-specific. Follow-up extraction scoped to MECH-059 confidence-channel decomposition. | In REE terms, this is positive pressure on `precision / confidence channel separate from prediction error` and supports keeping the mechanism, with tighter boundary conditions where failures recur. |
| `2026-02-15T14:56:37Z` | Run-pack `2026-02-15T145637Z_jepa-uncertainty-channels_seed47_explicit_uncertainty_head_toyenv_internal_minimal` in `jepa_uncertainty_channels` | `supports` | 0.75 | PASS with supporting direction | In REE terms, this is positive pressure on `precision / confidence channel separate from prediction error` and supports keeping the mechanism, with tighter boundary conditions where failures recur. |
| `2026-02-15T14:56:37Z` | Run-pack `2026-02-15T145637Z_jepa-uncertainty-channels_seed47_deterministic_plus_dispersion_toyenv_internal_minimal` in `jepa_uncertainty_channels` | `mixed` | 0.5 | mixed direction | In REE terms, this implies `precision / confidence channel separate from prediction error` may hold only in some regimes; the next step is to formalize those regimes explicitly. |
| `2026-02-15T14:56:37Z` | Run-pack `2026-02-15T145637Z_jepa-uncertainty-channels_seed29_explicit_uncertainty_head_toyenv_internal_minimal` in `jepa_uncertainty_channels` | `supports` | 0.75 | PASS with supporting direction | In REE terms, this is positive pressure on `precision / confidence channel separate from prediction error` and supports keeping the mechanism, with tighter boundary conditions where failures recur. |
| `2026-02-15T14:56:37Z` | Run-pack `2026-02-15T145637Z_jepa-uncertainty-channels_seed29_deterministic_plus_dispersion_toyenv_internal_minimal` in `jepa_uncertainty_channels` | `mixed` | 0.5 | mixed direction | In REE terms, this implies `precision / confidence channel separate from prediction error` may hold only in some regimes; the next step is to formalize those regimes explicitly. |
| `2026-02-15T14:56:37Z` | Run-pack `2026-02-15T145637Z_jepa-uncertainty-channels_seed11_explicit_uncertainty_head_toyenv_internal_minimal` in `jepa_uncertainty_channels` | `supports` | 0.75 | PASS with supporting direction | In REE terms, this is positive pressure on `precision / confidence channel separate from prediction error` and supports keeping the mechanism, with tighter boundary conditions where failures recur. |
| `2026-02-15T14:56:37Z` | Run-pack `2026-02-15T145637Z_jepa-uncertainty-channels_seed11_deterministic_plus_dispersion_toyenv_internal_minimal` in `jepa_uncertainty_channels` | `mixed` | 0.5 | mixed direction | In REE terms, this implies `precision / confidence channel separate from prediction error` may hold only in some regimes; the next step is to formalize those regimes explicitly. |

## Left-Field Suggestions

1. Run a two-agent internal market where one head bids uncertainty and another bids control precision.
- Why it may inspire: Could expose whether uncertainty is being used as a genuine signal or as a score-gaming channel.
- First test: Add a toy arbitration layer and compare calibration drift against current single-head setup.
2. Introduce uncertainty audits with synthetic adversarial ambiguity snapshots.
- Why it may inspire: Could catch hidden calibration collapse earlier than aggregate loss metrics.
- First test: Inject ambiguity stress cases every N steps and track abstention reliability.
3. Use a separately trained uncertainty critic that never sees policy loss.
- Why it may inspire: Could reduce leakage from policy optimization into confidence estimates.
- First test: Compare uncertainty-channel leakage before/after adding the critic.

## Decision Prompts

1. Which part of the claim appears stable across both supporting and weakening evidence?
2. If this claim were split into two sub-claims, where is the cleanest boundary?
3. What is the smallest architecture change that would most likely remove the top recurring failure signature?
4. What evidence next week would most likely change your current decision?
