# Structure Review Dossier: MECH-056

Generated: `2026-02-15T21:11:54.734668Z`
Cycle: `2026-02-15`

## Claim Description

MECH-056 is a mechanism hypothesis about residue / trajectory first placement.

## Where This Fits in REE as a Whole

This sits in REE's mechanism layer and links architecture commitments to testable signatures. It depends on 7 upstream claim(s): `ARC-013`, `ARC-018`, `ARC-003`, `ARC-004`, `MECH-034`, `MECH-060`, `MECH-062`. No downstream claims currently list it as a dependency. Primary architecture anchor: `docs/architecture/residue_geometry.md#mech-056`.

## Structural Pressure Signals

- Recommendation: `consider_new_structure` (consider_new_structure=true)
- Trigger signals: external_precedence_pressure, high_conflict_ratio, recurring_failure_signatures
- Conflict ratio: 0.892
- Overall confidence: 0.749

## Evidence Mix and Why It Looks This Way

- Direction counts: supports=37, weakens=46, mixed=1, unknown=0.
- Experimental mix: supports=29, weakens=46, mixed=0, unknown=0.
- Literature mix: supports=8, weakens=0, mixed=1, unknown=0.
- Direction narrative: Evidence is directionally split between support and weakening, which indicates either claim over-breadth or hidden context dependence.
- Source narrative: Both experiment and literature are present. Use disagreement between these sources as a cue to refine claim scope before making status promotions.

## Evidence Pull (Current Findings + Alternatives)

| alternative | confidence_estimate | current_findings | next_pull_focus |
|---|---:|---|---|
| residue / trajectory first placement is broadly correct, but failures are boundary-condition failures. | 0.435 | Supporting evidence dominates enough to keep the core mechanism plausible. | Target stress regimes where failures cluster and test whether boundary constraints recover stability.; Pull replication papers that test similar mechanisms under distribution shift. |
| residue / trajectory first placement is over-scoped and should be narrowed or split. | 0.553 | Weakening evidence indicates at least one sub-regime where the current claim phrasing breaks. | Extract disconfirming sources and isolate the exact violated assumption.; Run claim-splitting experiments with explicit sub-claim tags in manifests. |
| A hybrid architecture is needed: keep the core of residue / trajectory first placement but add explicit gating or interface separation. | 0.435 | Mixed evidence and conflict patterns suggest partial validity with missing structural guardrails. | Evaluate an ablation that isolates the proposed guardrail/interface addition.; Collect one adjacent-domain source that uses a similar split architecture. |

## Source Wording vs REE Translation

| timestamp | source | direction | confidence | evidence wording (preserved) | REE translation |
|---|---|---|---:|---|---|
| `2026-02-15T21:11:17.389757Z` | Run-pack `exp_0004_20260215T211117389757Z` in `trajectory_integrity` | `supports` | 0.75 | PASS with supporting direction | In REE terms, this is positive pressure on `residue / trajectory first placement` and supports keeping the mechanism, with tighter boundary conditions where failures recur. |
| `2026-02-15T20:52:57.348626Z` | Run-pack `exp_0005_20260215T205257348626Z` in `trajectory_integrity` | `supports` | 0.75 | PASS with supporting direction | In REE terms, this is positive pressure on `residue / trajectory first placement` and supports keeping the mechanism, with tighter boundary conditions where failures recur. |
| `2026-02-15T20:52:57.289360Z` | Run-pack `exp_0005_20260215T205257289360Z` in `trajectory_integrity` | `supports` | 0.75 | PASS with supporting direction | In REE terms, this is positive pressure on `residue / trajectory first placement` and supports keeping the mechanism, with tighter boundary conditions where failures recur. |
| `2026-02-15T18:07:10.843991Z` | Run-pack `exp_0004_20260215T180710843991Z` in `trajectory_integrity` | `supports` | 0.75 | PASS with supporting direction | In REE terms, this is positive pressure on `residue / trajectory first placement` and supports keeping the mechanism, with tighter boundary conditions where failures recur. |
| `2026-02-15T18:07:10.784771Z` | Run-pack `exp_0004_20260215T180710784771Z` in `trajectory_integrity` | `supports` | 0.75 | PASS with supporting direction | In REE terms, this is positive pressure on `residue / trajectory first placement` and supports keeping the mechanism, with tighter boundary conditions where failures recur. |
| `2026-02-15T17:48:50Z` | Run-pack `2026-02-15T174850Z_claim-probe-mech-056_seed11_trajectory_first_enabled_toyenv_internal_minimal` in `claim_probe_mech_056` | `supports` | 0.75 | PASS with supporting direction | In REE terms, this is positive pressure on `residue / trajectory first placement` and supports keeping the mechanism, with tighter boundary conditions where failures recur. |
| `2026-02-15T17:39:01Z` | Run-pack `2026-02-15T173901Z_trajectory-integrity_seed47_trajectory_first_enabled_toyenv_internal_minimal` in `trajectory_integrity` | `weakens` | 0.75 | FAIL with weakening direction | In REE terms, this is negative pressure on `residue / trajectory first placement` and suggests the claim is likely too strong or missing a key gating variable. |
| `2026-02-15T17:39:01Z` | Run-pack `2026-02-15T173901Z_trajectory-integrity_seed47_trajectory_first_ablated_toyenv_internal_minimal` in `trajectory_integrity` | `weakens` | 0.75 | FAIL with weakening direction | In REE terms, this is negative pressure on `residue / trajectory first placement` and suggests the claim is likely too strong or missing a key gating variable. |

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
