# Structure Review Dossier: ARC-003

Generated: `2026-02-15T21:38:14.133109Z`
Cycle: `2026-02-15`

## Claim Description

ARC-003 is an architecture commitment about E3 / trajectory commitment.

## Where This Fits in REE as a Whole

This sits in REE's architecture layer and constrains lower-level mechanism design. It depends on 5 upstream claim(s): `INV-012`, `ARC-001`, `ARC-002`, `ARC-004`, `ARC-005`. It currently feeds 23 downstream claim(s): `ARC-007`, `ARC-008`, `ARC-012`, `ARC-014`, `ARC-015`, `ARC-017`, `ARC-018`, `IMPL-003`, `IMPL-004`, `IMPL-016`, `MECH-004`, `MECH-005`, `MECH-008`, `MECH-035`, `MECH-037`, `MECH-049`, `MECH-056`, `MECH-057`, `MECH-060`, `MECH-061`, `MECH-062`, `Q-015`, `Q-016`. Primary architecture anchor: `docs/architecture/e3.md#arc-003`.

## Structural Pressure Signals

- Recommendation: `consider_new_structure` (consider_new_structure=true)
- Trigger signals: external_precedence_pressure, high_conflict_ratio, recurring_failure_signatures
- Conflict ratio: 0.889
- Overall confidence: 0.665

## Evidence Mix and Why It Looks This Way

- Direction counts: supports=5, weakens=4, mixed=0, unknown=0.
- Experimental mix: supports=3, weakens=4, mixed=0, unknown=0.
- Literature mix: supports=2, weakens=0, mixed=0, unknown=0.
- Direction narrative: Evidence is directionally split between support and weakening, which indicates either claim over-breadth or hidden context dependence.
- Source narrative: Both experiment and literature are present. Use disagreement between these sources as a cue to refine claim scope before making status promotions.

## Evidence Pull (Current Findings + Alternatives)

| alternative | confidence_estimate | current_findings | next_pull_focus |
|---|---:|---|---|
| E3 / trajectory commitment is broadly correct, but failures are boundary-condition failures. | 0.557 | Supporting evidence dominates enough to keep the core mechanism plausible. | Target stress regimes where failures cluster and test whether boundary constraints recover stability.; Pull replication papers that test similar mechanisms under distribution shift. |
| E3 / trajectory commitment is over-scoped and should be narrowed or split. | 0.443 | Weakening evidence indicates at least one sub-regime where the current claim phrasing breaks. | Extract disconfirming sources and isolate the exact violated assumption.; Run claim-splitting experiments with explicit sub-claim tags in manifests. |
| A hybrid architecture is needed: keep the core of E3 / trajectory commitment but add explicit gating or interface separation. | 0.443 | Mixed evidence and conflict patterns suggest partial validity with missing structural guardrails. | Evaluate an ablation that isolates the proposed guardrail/interface addition.; Collect one adjacent-domain source that uses a similar split architecture. |

## Source Wording vs REE Translation

| timestamp | source | direction | confidence | evidence wording (preserved) | REE translation |
|---|---|---|---:|---|---|
| `2026-02-15T21:36:03Z` | Run-pack `2026-02-15T213603Z_claim-probe-arc-003_seed1001_single_error_stream_toyenv_internal_minimal` in `claim_probe_arc_003` | `weakens` | 0.75 | FAIL with weakening direction | In REE terms, this is negative pressure on `E3 / trajectory commitment` and suggests the claim is likely too strong or missing a key gating variable. |
| `2026-02-15T21:10:33Z` | Run-pack `2026-02-15T211033Z_claim-probe-arc-003_seed11_pre_post_split_streams_toyenv_internal_minimal` in `claim_probe_arc_003` | `supports` | 0.75 | PASS with supporting direction | In REE terms, this is positive pressure on `E3 / trajectory commitment` and supports keeping the mechanism, with tighter boundary conditions where failures recur. |
| `2026-02-15T20:52:13Z` | Run-pack `2026-02-15T205213Z_claim-probe-arc-003_seed11_single_error_stream_toyenv_internal_minimal` in `claim_probe_arc_003` | `weakens` | 0.75 | FAIL with weakening direction | In REE terms, this is negative pressure on `E3 / trajectory commitment` and suggests the claim is likely too strong or missing a key gating variable. |
| `2026-02-15T18:09:24.496279Z` | Run-pack `exp_0006_20260215T180924496279Z` in `claim_probe_arc_003` | `supports` | 0.75 | PASS with supporting direction | In REE terms, this is positive pressure on `E3 / trajectory commitment` and supports keeping the mechanism, with tighter boundary conditions where failures recur. |
| `2026-02-15T18:09:24.416725Z` | Run-pack `exp_0006_20260215T180924416725Z` in `claim_probe_arc_003` | `supports` | 0.75 | PASS with supporting direction | In REE terms, this is positive pressure on `E3 / trajectory commitment` and supports keeping the mechanism, with tighter boundary conditions where failures recur. |
| `2026-02-15T17:52:25Z` | Run-pack `2026-02-15T175225Z_claim-probe-arc-003_seed29_single_error_stream_toyenv_internal_minimal` in `claim_probe_arc_003` | `weakens` | 0.75 | FAIL with weakening direction | In REE terms, this is negative pressure on `E3 / trajectory commitment` and suggests the claim is likely too strong or missing a key gating variable. |
| `2026-02-15T17:52:24Z` | Run-pack `2026-02-15T175224Z_claim-probe-arc-003_seed11_single_error_stream_toyenv_internal_minimal` in `claim_probe_arc_003` | `weakens` | 0.75 | FAIL with weakening direction | In REE terms, this is negative pressure on `E3 / trajectory commitment` and suggests the claim is likely too strong or missing a key gating variable. |
| `2026-02-14T20:55:00Z` | The architecture of cognitive control in the human prefrontal cortex (2003, Science) | `supports` | 0.74 | Evidence for hierarchical PFC control organization supports multi-level control routing and staged arbitration; direct mapping to specific REE mode priors and aversive-gating mechanics remains incomplete. | In REE terms, this is positive pressure on `E3 / trajectory commitment` and supports keeping the mechanism, with tighter boundary conditions where failures recur. |

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
