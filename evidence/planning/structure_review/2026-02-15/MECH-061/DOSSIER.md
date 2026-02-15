# Structure Review Dossier: MECH-061

Generated: `2026-02-15T21:38:14.133109Z`
Cycle: `2026-02-15`

## Claim Description

MECH-061 is a mechanism hypothesis about commitment / boundary token error reclassification.

## Where This Fits in REE as a Whole

This sits in REE's mechanism layer and links architecture commitments to testable signatures. It depends on 4 upstream claim(s): `ARC-003`, `ARC-015`, `INV-012`, `MECH-060`. It currently feeds 4 downstream claim(s): `IMPL-023`, `IMPL-025`, `MECH-062`, `Q-015`. Primary architecture anchor: `docs/architecture/e3.md#mech-061`.

## Structural Pressure Signals

- Recommendation: `consider_new_structure` (consider_new_structure=true)
- Trigger signals: external_precedence_pressure, high_conflict_ratio, recurring_failure_signatures
- Conflict ratio: 0.889
- Overall confidence: 0.654

## Evidence Mix and Why It Looks This Way

- Direction counts: supports=5, weakens=4, mixed=0, unknown=0.
- Experimental mix: supports=3, weakens=4, mixed=0, unknown=0.
- Literature mix: supports=2, weakens=0, mixed=0, unknown=0.
- Direction narrative: Evidence is directionally split between support and weakening, which indicates either claim over-breadth or hidden context dependence.
- Source narrative: Both experiment and literature are present. Use disagreement between these sources as a cue to refine claim scope before making status promotions.

## Evidence Pull (Current Findings + Alternatives)

| alternative | confidence_estimate | current_findings | next_pull_focus |
|---|---:|---|---|
| commitment / boundary token error reclassification is broadly correct, but failures are boundary-condition failures. | 0.55 | Supporting evidence dominates enough to keep the core mechanism plausible. | Target stress regimes where failures cluster and test whether boundary constraints recover stability.; Pull replication papers that test similar mechanisms under distribution shift. |
| commitment / boundary token error reclassification is over-scoped and should be narrowed or split. | 0.45 | Weakening evidence indicates at least one sub-regime where the current claim phrasing breaks. | Extract disconfirming sources and isolate the exact violated assumption.; Run claim-splitting experiments with explicit sub-claim tags in manifests. |
| A hybrid architecture is needed: keep the core of commitment / boundary token error reclassification but add explicit gating or interface separation. | 0.45 | Mixed evidence and conflict patterns suggest partial validity with missing structural guardrails. | Evaluate an ablation that isolates the proposed guardrail/interface addition.; Collect one adjacent-domain source that uses a similar split architecture. |

## Source Wording vs REE Translation

| timestamp | source | direction | confidence | evidence wording (preserved) | REE translation |
|---|---|---|---:|---|---|
| `2026-02-15T21:36:06Z` | Run-pack `2026-02-15T213606Z_claim-probe-mech-061_seed1001_single_error_stream_toyenv_internal_minimal` in `claim_probe_mech_061` | `weakens` | 0.75 | FAIL with weakening direction | In REE terms, this is negative pressure on `commitment / boundary token error reclassification` and suggests the claim is likely too strong or missing a key gating variable. |
| `2026-02-15T21:10:36Z` | Run-pack `2026-02-15T211036Z_claim-probe-mech-061_seed11_pre_post_split_streams_toyenv_internal_minimal` in `claim_probe_mech_061` | `supports` | 0.75 | PASS with supporting direction | In REE terms, this is positive pressure on `commitment / boundary token error reclassification` and supports keeping the mechanism, with tighter boundary conditions where failures recur. |
| `2026-02-15T20:52:15Z` | Run-pack `2026-02-15T205215Z_claim-probe-mech-061_seed11_single_error_stream_toyenv_internal_minimal` in `claim_probe_mech_061` | `weakens` | 0.75 | FAIL with weakening direction | In REE terms, this is negative pressure on `commitment / boundary token error reclassification` and suggests the claim is likely too strong or missing a key gating variable. |
| `2026-02-15T18:09:24.601905Z` | Run-pack `exp_0007_20260215T180924601905Z` in `claim_probe_mech_061` | `supports` | 0.75 | PASS with supporting direction | In REE terms, this is positive pressure on `commitment / boundary token error reclassification` and supports keeping the mechanism, with tighter boundary conditions where failures recur. |
| `2026-02-15T18:09:24.550177Z` | Run-pack `exp_0007_20260215T180924550177Z` in `claim_probe_mech_061` | `supports` | 0.75 | PASS with supporting direction | In REE terms, this is positive pressure on `commitment / boundary token error reclassification` and supports keeping the mechanism, with tighter boundary conditions where failures recur. |
| `2026-02-15T17:52:35Z` | Run-pack `2026-02-15T175235Z_claim-probe-mech-061_seed29_single_error_stream_toyenv_internal_minimal` in `claim_probe_mech_061` | `weakens` | 0.75 | FAIL with weakening direction | In REE terms, this is negative pressure on `commitment / boundary token error reclassification` and suggests the claim is likely too strong or missing a key gating variable. |
| `2026-02-15T17:52:34Z` | Run-pack `2026-02-15T175234Z_claim-probe-mech-061_seed11_single_error_stream_toyenv_internal_minimal` in `claim_probe_mech_061` | `weakens` | 0.75 | FAIL with weakening direction | In REE terms, this is negative pressure on `commitment / boundary token error reclassification` and suggests the claim is likely too strong or missing a key gating variable. |
| `2026-02-15T14:16:00Z` | Sense of agency in the human brain (2017, Nature Reviews Neuroscience) | `supports` | 0.69 | Review-level synthesis supports comparator-based self-attribution after action outcomes, consistent with a pre/post boundary in error interpretation; support is indirect for explicit tokenized routing primitives. | In REE terms, this is positive pressure on `commitment / boundary token error reclassification` and supports keeping the mechanism, with tighter boundary conditions where failures recur. |

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
