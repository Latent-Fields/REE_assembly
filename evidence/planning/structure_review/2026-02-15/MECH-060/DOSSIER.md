# Structure Review Dossier: MECH-060

Generated: `2026-02-15T14:41:04.790242Z`
Cycle: `2026-02-15`

## Claim Description

MECH-060 is a mechanism hypothesis about commitment / dual error channels pre post commit.

## Where This Fits in REE as a Whole

This sits in REE's mechanism layer and links architecture commitments to testable signatures. It depends on 5 upstream claim(s): `ARC-003`, `ARC-005`, `ARC-015`, `INV-012`, `MECH-057`. It currently feeds 2 downstream claim(s): `IMPL-023`, `MECH-061`. Primary architecture anchor: `docs/architecture/agency_responsibility_flow.md#mech-060`.

## Structural Pressure Signals

- Recommendation: `consider_new_structure` (consider_new_structure=true)
- Trigger signals: external_precedence_pressure, high_conflict_ratio, recurring_failure_signatures
- Conflict ratio: 0.931
- Overall confidence: 0.687

## Evidence Mix and Why It Looks This Way

- Direction counts: supports=31, weakens=27, mixed=3, unknown=0.
- Experimental mix: supports=27, weakens=27, mixed=0, unknown=0.
- Literature mix: supports=4, weakens=0, mixed=3, unknown=0.
- Direction narrative: Evidence is directionally split between support and weakening, which indicates either claim over-breadth or hidden context dependence.
- Source narrative: Both experiment and literature are present. Use disagreement between these sources as a cue to refine claim scope before making status promotions.

## Evidence Pull (Current Findings + Alternatives)

| alternative | confidence_estimate | current_findings | next_pull_focus |
|---|---:|---|---|
| commitment / dual error channels pre post commit is broadly correct, but failures are boundary-condition failures. | 0.524 | Supporting evidence dominates enough to keep the core mechanism plausible. | Target stress regimes where failures cluster and test whether boundary constraints recover stability.; Pull replication papers that test similar mechanisms under distribution shift. |
| commitment / dual error channels pre post commit is over-scoped and should be narrowed or split. | 0.431 | Weakening evidence indicates at least one sub-regime where the current claim phrasing breaks. | Extract disconfirming sources and isolate the exact violated assumption.; Run claim-splitting experiments with explicit sub-claim tags in manifests. |
| A hybrid architecture is needed: keep the core of commitment / dual error channels pre post commit but add explicit gating or interface separation. | 0.431 | Mixed evidence and conflict patterns suggest partial validity with missing structural guardrails. | Evaluate an ablation that isolates the proposed guardrail/interface addition.; Collect one adjacent-domain source that uses a similar split architecture. |

## Source Wording vs REE Translation

| timestamp | source | direction | confidence | evidence wording (preserved) | REE translation |
|---|---|---|---:|---|---|
| `2026-02-15T14:17:52Z` | Run-pack `2026-02-15T141752Z_commit-dual-error-channels_seed47_single_error_stream_toyenv_internal_minimal` in `commit_dual_error_channels` | `weakens` | 0.75 | FAIL with weakening direction | In REE terms, this is negative pressure on `commitment / dual error channels pre post commit` and suggests the claim is likely too strong or missing a key gating variable. |
| `2026-02-15T14:17:52Z` | Run-pack `2026-02-15T141752Z_commit-dual-error-channels_seed47_pre_post_split_streams_toyenv_internal_minimal` in `commit_dual_error_channels` | `supports` | 0.75 | PASS with supporting direction | In REE terms, this is positive pressure on `commitment / dual error channels pre post commit` and supports keeping the mechanism, with tighter boundary conditions where failures recur. |
| `2026-02-15T14:17:52Z` | Run-pack `2026-02-15T141752Z_commit-dual-error-channels_seed29_single_error_stream_toyenv_internal_minimal` in `commit_dual_error_channels` | `weakens` | 0.75 | FAIL with weakening direction | In REE terms, this is negative pressure on `commitment / dual error channels pre post commit` and suggests the claim is likely too strong or missing a key gating variable. |
| `2026-02-15T14:17:52Z` | Run-pack `2026-02-15T141752Z_commit-dual-error-channels_seed29_pre_post_split_streams_toyenv_internal_minimal` in `commit_dual_error_channels` | `supports` | 0.75 | PASS with supporting direction | In REE terms, this is positive pressure on `commitment / dual error channels pre post commit` and supports keeping the mechanism, with tighter boundary conditions where failures recur. |
| `2026-02-15T14:17:52Z` | Run-pack `2026-02-15T141752Z_commit-dual-error-channels_seed11_single_error_stream_toyenv_internal_minimal` in `commit_dual_error_channels` | `weakens` | 0.75 | FAIL with weakening direction | In REE terms, this is negative pressure on `commitment / dual error channels pre post commit` and suggests the claim is likely too strong or missing a key gating variable. |
| `2026-02-15T14:17:52Z` | Run-pack `2026-02-15T141752Z_commit-dual-error-channels_seed11_pre_post_split_streams_toyenv_internal_minimal` in `commit_dual_error_channels` | `supports` | 0.75 | PASS with supporting direction | In REE terms, this is positive pressure on `commitment / dual error channels pre post commit` and supports keeping the mechanism, with tighter boundary conditions where failures recur. |
| `2026-02-15T14:16:00Z` | Sense of agency in the human brain (2017, Nature Reviews Neuroscience) | `supports` | 0.69 | Review-level synthesis supports comparator-based self-attribution after action outcomes, consistent with a pre/post boundary in error interpretation; support is indirect for explicit tokenized routing primitives. | In REE terms, this is positive pressure on `commitment / dual error channels pre post commit` and supports keeping the mechanism, with tighter boundary conditions where failures recur. |
| `2026-02-15T14:00:29Z` | Run-pack `2026-02-15T140029Z_commit-dual-error-channels_seed11_single_error_stream_toyenv_internal_minimal` in `commit_dual_error_channels` | `weakens` | 0.75 | FAIL with weakening direction | In REE terms, this is negative pressure on `commitment / dual error channels pre post commit` and suggests the claim is likely too strong or missing a key gating variable. |

## Left-Field Suggestions

1. Add a hard temporal write barrier after commit events.
- Why it may inspire: Could reduce cross-channel contamination by forcing delayed attribution writes.
- First test: Ablate commit barrier windows and measure post-commit attribution gain.
2. Tag each error packet with causal provenance tokens before learning attribution.
- Why it may inspire: Could improve channel separation by preserving source traceability.
- First test: Track contamination signatures with and without provenance tags.
3. Maintain physically separate replay buffers for pre-commit vs post-commit errors.
- Why it may inspire: Could prevent accidental blending during optimization.
- First test: Run identical seeds with shared vs split replay and compare leakage rate.

## Decision Prompts

1. Which part of the claim appears stable across both supporting and weakening evidence?
2. If this claim were split into two sub-claims, where is the cleanest boundary?
3. What is the smallest architecture change that would most likely remove the top recurring failure signature?
4. What evidence next week would most likely change your current decision?
