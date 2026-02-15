# Structure Review Dossier: MECH-056

Generated: `2026-02-15T15:07:46.524441Z`
Cycle: `2026-02-15`

## Claim Description

MECH-056 is a mechanism hypothesis about residue / trajectory first placement.

## Where This Fits in REE as a Whole

This sits in REE's mechanism layer and links architecture commitments to testable signatures. It depends on 5 upstream claim(s): `ARC-013`, `ARC-018`, `ARC-003`, `ARC-004`, `MECH-034`. No downstream claims currently list it as a dependency. Primary architecture anchor: `docs/architecture/residue_geometry.md#mech-056`.

## Structural Pressure Signals

- Recommendation: `consider_new_structure` (consider_new_structure=true)
- Trigger signals: external_precedence_pressure, high_conflict_ratio, recurring_failure_signatures
- Conflict ratio: 1
- Overall confidence: 0.721

## Evidence Mix and Why It Looks This Way

- Direction counts: supports=24, weakens=24, mixed=0, unknown=0.
- Experimental mix: supports=19, weakens=24, mixed=0, unknown=0.
- Literature mix: supports=5, weakens=0, mixed=0, unknown=0.
- Direction narrative: Evidence is directionally split between support and weakening, which indicates either claim over-breadth or hidden context dependence.
- Source narrative: Both experiment and literature are present. Use disagreement between these sources as a cue to refine claim scope before making status promotions.

## Evidence Pull (Current Findings + Alternatives)

| alternative | confidence_estimate | current_findings | next_pull_focus |
|---|---:|---|---|
| residue / trajectory first placement is broadly correct, but failures are boundary-condition failures. | 0.49 | Supporting evidence dominates enough to keep the core mechanism plausible. | Target stress regimes where failures cluster and test whether boundary constraints recover stability.; Pull replication papers that test similar mechanisms under distribution shift. |
| residue / trajectory first placement is over-scoped and should be narrowed or split. | 0.51 | Weakening evidence indicates at least one sub-regime where the current claim phrasing breaks. | Extract disconfirming sources and isolate the exact violated assumption.; Run claim-splitting experiments with explicit sub-claim tags in manifests. |
| A hybrid architecture is needed: keep the core of residue / trajectory first placement but add explicit gating or interface separation. | 0.49 | Mixed evidence and conflict patterns suggest partial validity with missing structural guardrails. | Evaluate an ablation that isolates the proposed guardrail/interface addition.; Collect one adjacent-domain source that uses a similar split architecture. |

## Source Wording vs REE Translation

| timestamp | source | direction | confidence | evidence wording (preserved) | REE translation |
|---|---|---|---:|---|---|
| `2026-02-15T16:02:00Z` | Prioritized memory access explains planning and hippocampal replay (2018, Nature Neuroscience) | `supports` | 0.73 | The prioritized replay account reproduces multiple replay signatures and links replay selection to gain/need-like utility, consistent with precision-weighted rollout selection; evidence remains model-based and indirect for dual commit channels. Follow-up extraction scoped to MECH-056 replay-prioritization and planning coupling. Proposal completion extraction for LIT-0014 scoped to MECH-056. | In REE terms, this is positive pressure on `residue / trajectory first placement` and supports keeping the mechanism, with tighter boundary conditions where failures recur. |
| `2026-02-15T15:13:00Z` | Prioritized memory access explains planning and hippocampal replay (2018, Nature Neuroscience) | `supports` | 0.73 | The prioritized replay account reproduces multiple replay signatures and links replay selection to gain/need-like utility, consistent with precision-weighted rollout selection; evidence remains model-based and indirect for dual commit channels. Follow-up extraction scoped to MECH-056 replay-prioritization and planning coupling. | In REE terms, this is positive pressure on `residue / trajectory first placement` and supports keeping the mechanism, with tighter boundary conditions where failures recur. |
| `2026-02-15T14:56:38Z` | Run-pack `2026-02-15T145638Z_trajectory-integrity_seed47_trajectory_first_ablated_toyenv_internal_minimal` in `trajectory_integrity` | `weakens` | 0.75 | FAIL with weakening direction | In REE terms, this is negative pressure on `residue / trajectory first placement` and suggests the claim is likely too strong or missing a key gating variable. |
| `2026-02-15T14:56:38Z` | Run-pack `2026-02-15T145638Z_trajectory-integrity_seed29_trajectory_first_ablated_toyenv_internal_minimal` in `trajectory_integrity` | `weakens` | 0.75 | FAIL with weakening direction | In REE terms, this is negative pressure on `residue / trajectory first placement` and suggests the claim is likely too strong or missing a key gating variable. |
| `2026-02-15T14:56:38Z` | Run-pack `2026-02-15T145638Z_trajectory-integrity_seed11_trajectory_first_ablated_toyenv_internal_minimal` in `trajectory_integrity` | `weakens` | 0.75 | FAIL with weakening direction | In REE terms, this is negative pressure on `residue / trajectory first placement` and suggests the claim is likely too strong or missing a key gating variable. |
| `2026-02-15T14:56:37Z` | Run-pack `2026-02-15T145637Z_trajectory-integrity_seed47_trajectory_first_enabled_toyenv_internal_minimal` in `trajectory_integrity` | `weakens` | 0.75 | FAIL with weakening direction | In REE terms, this is negative pressure on `residue / trajectory first placement` and suggests the claim is likely too strong or missing a key gating variable. |
| `2026-02-15T14:56:37Z` | Run-pack `2026-02-15T145637Z_trajectory-integrity_seed29_trajectory_first_enabled_toyenv_internal_minimal` in `trajectory_integrity` | `weakens` | 0.75 | FAIL with weakening direction | In REE terms, this is negative pressure on `residue / trajectory first placement` and suggests the claim is likely too strong or missing a key gating variable. |
| `2026-02-15T14:56:37Z` | Run-pack `2026-02-15T145637Z_trajectory-integrity_seed11_trajectory_first_enabled_toyenv_internal_minimal` in `trajectory_integrity` | `supports` | 0.75 | PASS with supporting direction | In REE terms, this is positive pressure on `residue / trajectory first placement` and supports keeping the mechanism, with tighter boundary conditions where failures recur. |

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
