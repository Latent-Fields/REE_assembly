# Structure Review Dossier: ARC-007

Generated: `2026-02-15T19:47:53.325229Z`
Cycle: `2026-02-15`

## Claim Description

ARC-007 is an architecture commitment about hippocampus / path memory.

## Where This Fits in REE as a Whole

This sits in REE's architecture layer and constrains lower-level mechanism design. It depends on 2 upstream claim(s): `ARC-004`, `ARC-003`. It currently feeds 17 downstream claim(s): `ARC-011`, `ARC-012`, `ARC-014`, `ARC-015`, `ARC-018`, `ARC-019`, `IMPL-004`, `IMPL-005`, `IMPL-019`, `MECH-016`, `MECH-017`, `MECH-018`, `MECH-022`, `MECH-029`, `MECH-030`, `MECH-037`, `MECH-044`. Primary architecture anchor: `docs/architecture/hippocampal_systems.md#arc-007`.

## Structural Pressure Signals

- Recommendation: `consider_new_structure` (consider_new_structure=true)
- Trigger signals: external_precedence_pressure, high_conflict_ratio, recurring_failure_signatures
- Conflict ratio: 0.857
- Overall confidence: 0.58

## Evidence Mix and Why It Looks This Way

- Direction counts: supports=4, weakens=3, mixed=0, unknown=0.
- Experimental mix: supports=3, weakens=3, mixed=0, unknown=0.
- Literature mix: supports=1, weakens=0, mixed=0, unknown=0.
- Direction narrative: Evidence is directionally split between support and weakening, which indicates either claim over-breadth or hidden context dependence.
- Source narrative: Both experiment and literature are present. Use disagreement between these sources as a cue to refine claim scope before making status promotions.

## Evidence Pull (Current Findings + Alternatives)

| alternative | confidence_estimate | current_findings | next_pull_focus |
|---|---:|---|---|
| hippocampus / path memory is broadly correct, but failures are boundary-condition failures. | 0.575 | Supporting evidence dominates enough to keep the core mechanism plausible. | Target stress regimes where failures cluster and test whether boundary constraints recover stability.; Pull replication papers that test similar mechanisms under distribution shift. |
| hippocampus / path memory is over-scoped and should be narrowed or split. | 0.425 | Weakening evidence indicates at least one sub-regime where the current claim phrasing breaks. | Extract disconfirming sources and isolate the exact violated assumption.; Run claim-splitting experiments with explicit sub-claim tags in manifests. |
| A hybrid architecture is needed: keep the core of hippocampus / path memory but add explicit gating or interface separation. | 0.425 | Mixed evidence and conflict patterns suggest partial validity with missing structural guardrails. | Evaluate an ablation that isolates the proposed guardrail/interface addition.; Collect one adjacent-domain source that uses a similar split architecture. |

## Source Wording vs REE Translation

| timestamp | source | direction | confidence | evidence wording (preserved) | REE translation |
|---|---|---|---:|---|---|
| `2026-02-15T18:10:23Z` | Run-pack `2026-02-15T181023Z_claim-probe-arc-007_seed29_trajectory_first_enabled_toyenv_internal_minimal` in `claim_probe_arc_007` | `weakens` | 0.75 | FAIL with weakening direction | In REE terms, this is negative pressure on `hippocampus / path memory` and suggests the claim is likely too strong or missing a key gating variable. |
| `2026-02-15T18:10:22Z` | Run-pack `2026-02-15T181022Z_claim-probe-arc-007_seed11_trajectory_first_enabled_toyenv_internal_minimal` in `claim_probe_arc_007` | `supports` | 0.75 | PASS with supporting direction | In REE terms, this is positive pressure on `hippocampus / path memory` and supports keeping the mechanism, with tighter boundary conditions where failures recur. |
| `2026-02-15T18:05:19Z` | Run-pack `2026-02-15T180519Z_claim-probe-arc-007_seed29_trajectory_first_enabled_toyenv_internal_minimal` in `claim_probe_arc_007` | `weakens` | 0.75 | FAIL with weakening direction | In REE terms, this is negative pressure on `hippocampus / path memory` and suggests the claim is likely too strong or missing a key gating variable. |
| `2026-02-15T18:05:18Z` | Run-pack `2026-02-15T180518Z_claim-probe-arc-007_seed11_trajectory_first_enabled_toyenv_internal_minimal` in `claim_probe_arc_007` | `supports` | 0.75 | PASS with supporting direction | In REE terms, this is positive pressure on `hippocampus / path memory` and supports keeping the mechanism, with tighter boundary conditions where failures recur. |
| `2026-02-15T17:52:44Z` | Run-pack `2026-02-15T175244Z_claim-probe-arc-007_seed29_trajectory_first_enabled_toyenv_internal_minimal` in `claim_probe_arc_007` | `weakens` | 0.75 | FAIL with weakening direction | In REE terms, this is negative pressure on `hippocampus / path memory` and suggests the claim is likely too strong or missing a key gating variable. |
| `2026-02-15T17:52:43Z` | Run-pack `2026-02-15T175243Z_claim-probe-arc-007_seed11_trajectory_first_enabled_toyenv_internal_minimal` in `claim_probe_arc_007` | `supports` | 0.75 | PASS with supporting direction | In REE terms, this is positive pressure on `hippocampus / path memory` and supports keeping the mechanism, with tighter boundary conditions where failures recur. |
| `2026-02-14T20:10:00Z` | Hippocampal place-cell sequences depict future paths to remembered goals (2013, Nature) | `supports` | 0.79 | Direct in vivo evidence that hippocampal sequential activity at decision points sweeps toward goal locations; strong support for rollout/path-evaluation roles but indirect for REE-specific residue geometry. | In REE terms, this is positive pressure on `hippocampus / path memory` and supports keeping the mechanism, with tighter boundary conditions where failures recur. |

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
