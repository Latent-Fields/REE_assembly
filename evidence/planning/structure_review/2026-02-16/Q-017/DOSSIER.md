# Structure Review Dossier: Q-017

Generated: `2026-02-16T15:09:35.524567Z`
Cycle: `2026-02-16`

## Claim Description

Q-017 is an open question about control plane / minimal orthogonal axis set.

## Where This Fits in REE as a Whole

This sits in REE's uncertainty layer and defines what remains unresolved before stronger commitments. It depends on 3 upstream claim(s): `MECH-063`, `ARC-005`, `MECH-055`. No downstream claims currently list it as a dependency. Primary architecture anchor: `docs/architecture/control_plane.md#q-017`.

## Structural Pressure Signals

- Recommendation: `escalate_architecture_decision` (consider_new_structure=true)
- Trigger signals: external_precedence_pressure, high_conflict_ratio, recurring_failure_signatures
- Conflict ratio: 0.866
- Overall confidence: 0.713

## Evidence Mix and Why It Looks This Way

- Direction counts: supports=38, weakens=29, mixed=1, unknown=0.
- Experimental mix: supports=31, weakens=29, mixed=0, unknown=0.
- Literature mix: supports=7, weakens=0, mixed=1, unknown=0.
- Direction narrative: Evidence is directionally split between support and weakening, which indicates either claim over-breadth or hidden context dependence.
- Source narrative: Both experiment and literature are present. Use disagreement between these sources as a cue to refine claim scope before making status promotions.

## Evidence Pull (Current Findings + Alternatives)

| alternative | confidence_estimate | current_findings | next_pull_focus |
|---|---:|---|---|
| control plane / minimal orthogonal axis set is broadly correct, but failures are boundary-condition failures. | 0.561 | Supporting evidence dominates enough to keep the core mechanism plausible. | Target stress regimes where failures cluster and test whether boundary constraints recover stability.; Pull replication papers that test similar mechanisms under distribution shift. |
| control plane / minimal orthogonal axis set is over-scoped and should be narrowed or split. | 0.425 | Weakening evidence indicates at least one sub-regime where the current claim phrasing breaks. | Extract disconfirming sources and isolate the exact violated assumption.; Run claim-splitting experiments with explicit sub-claim tags in manifests. |
| A hybrid architecture is needed: keep the core of control plane / minimal orthogonal axis set but add explicit gating or interface separation. | 0.425 | Mixed evidence and conflict patterns suggest partial validity with missing structural guardrails. | Evaluate an ablation that isolates the proposed guardrail/interface addition.; Collect one adjacent-domain source that uses a similar split architecture. |

## Source Wording vs REE Translation

| timestamp | source | direction | confidence | evidence wording (preserved) | REE translation |
|---|---|---|---:|---|---|
| `2026-02-15T21:36:57.486711Z` | Run-pack `exp_0006_20260215T213657486711Z` in `control_axis_ablation` | `supports` | 0.75 | PASS with supporting direction | In REE terms, this is positive pressure on `control plane / minimal orthogonal axis set` and supports keeping the mechanism, with tighter boundary conditions where failures recur. |
| `2026-02-15T21:23:00Z` | Neuromodulation of neuronal circuits: back to the future (2012, Neuron) | `mixed` | 0.72 | Highlights degeneracy and context dependence, which weakens strict orthogonality claims while still allowing useful functional axes. | In REE terms, this implies `control plane / minimal orthogonal axis set` may hold only in some regimes; the next step is to formalize those regimes explicitly. |
| `2026-02-15T21:22:00Z` | Inverted-U-shaped dopamine actions on human working memory and cognitive control (2011, Biological Psychiatry) | `supports` | 0.74 | Constrains precision/vigor control to a nonlinear regime, supporting axis-specific guardrails rather than global monotone tuning. | In REE terms, this is positive pressure on `control plane / minimal orthogonal axis set` and supports keeping the mechanism, with tighter boundary conditions where failures recur. |
| `2026-02-15T21:21:00Z` | An integrative theory of locus coeruleus-norepinephrine function: adaptive gain and optimal performance (2005, Annual Review of Neuroscience) | `supports` | 0.8 | Strongly supports an interrupt/arousal control channel with separable network-level gain effects. | In REE terms, this is positive pressure on `control plane / minimal orthogonal axis set` and supports keeping the mechanism, with tighter boundary conditions where failures recur. |
| `2026-02-15T21:20:00Z` | Uncertainty, neuromodulation, and attention (2005, Neuron) | `supports` | 0.78 | Provides a principled separation between expected and unexpected uncertainty channels, consistent with multiple control-plane axes rather than a single scalar modulation. | In REE terms, this is positive pressure on `control plane / minimal orthogonal axis set` and supports keeping the mechanism, with tighter boundary conditions where failures recur. |
| `2026-02-15T21:11:17.186174Z` | Run-pack `exp_0001_20260215T211117186174Z` in `control_axis_ablation` | `supports` | 0.75 | PASS with supporting direction | In REE terms, this is positive pressure on `control plane / minimal orthogonal axis set` and supports keeping the mechanism, with tighter boundary conditions where failures recur. |
| `2026-02-15T20:52:56.872005Z` | Run-pack `exp_0001_20260215T205256872005Z` in `control_axis_ablation` | `supports` | 0.75 | PASS with supporting direction | In REE terms, this is positive pressure on `control plane / minimal orthogonal axis set` and supports keeping the mechanism, with tighter boundary conditions where failures recur. |
| `2026-02-15T20:52:56.766352Z` | Run-pack `exp_0001_20260215T205256766352Z` in `control_axis_ablation` | `supports` | 0.75 | PASS with supporting direction | In REE terms, this is positive pressure on `control plane / minimal orthogonal axis set` and supports keeping the mechanism, with tighter boundary conditions where failures recur. |

## Left-Field Suggestions

1. Split the claim into two narrower claims and route evidence independently.
- Why it may inspire: Can reduce hidden regime-mixing that creates persistent conflict ratios.
- First test: Create two scoped proposal tracks with explicit condition tags.
2. Run one synthetic extreme-condition probe outside normal benchmark regime.
- Why it may inspire: Can expose assumptions that are invisible in standard task distributions.
- First test: Add one adversarial scenario and compare signature incidence.
3. Bring in one adjacent-domain analogy as an explicit design option, not just evidence.
- Why it may inspire: Can surface architecture moves that current in-domain framing misses.
- First test: Add a parallel option in next governance packet and score it with the same gates.

## Decision Prompts

1. Which part of the claim appears stable across both supporting and weakening evidence?
2. If this claim were split into two sub-claims, where is the cleanest boundary?
3. What is the smallest architecture change that would most likely remove the top recurring failure signature?
4. What evidence next week would most likely change your current decision?
