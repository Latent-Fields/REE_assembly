# Structure Review Dossier: MECH-060

Generated: `2026-02-14T20:53:08.942075Z`
Cycle: `2026-02-14`

## Claim Description

MECH-060 is a mechanism hypothesis about commitment / dual error channels pre post commit.

## Where This Fits in REE as a Whole

This sits in REE's mechanism layer and links architecture commitments to testable signatures. It depends on 5 upstream claim(s): `ARC-003`, `ARC-005`, `ARC-015`, `INV-012`, `MECH-057`. It currently feeds 1 downstream claim(s): `IMPL-023`. Primary architecture anchor: `docs/architecture/agency_responsibility_flow.md#mech-060`.

## Structural Pressure Signals

- Recommendation: `consider_new_structure` (consider_new_structure=true)
- Trigger signals: external_precedence_pressure, high_conflict_ratio, literature_non_support_pressure, recurring_failure_signatures
- Conflict ratio: 0.9
- Overall confidence: 0.693

## Evidence Mix and Why It Looks This Way

- Direction counts: supports=22, weakens=18, mixed=3, unknown=0.
- Experimental mix: supports=19, weakens=18, mixed=0, unknown=0.
- Literature mix: supports=3, weakens=0, mixed=3, unknown=0.
- Direction narrative: Evidence is directionally split between support and weakening, which indicates either claim over-breadth or hidden context dependence.
- Source narrative: Both experiment and literature are present. Use disagreement between these sources as a cue to refine claim scope before making status promotions.

## Evidence Pull (Current Findings + Alternatives)

| alternative | confidence_estimate | current_findings | next_pull_focus |
|---|---:|---|---|
| commitment / dual error channels pre post commit is broadly correct, but failures are boundary-condition failures. | 0.536 | Supporting evidence dominates enough to keep the core mechanism plausible. | Target stress regimes where failures cluster and test whether boundary constraints recover stability.; Pull replication papers that test similar mechanisms under distribution shift. |
| commitment / dual error channels pre post commit is over-scoped and should be narrowed or split. | 0.4 | Weakening evidence indicates at least one sub-regime where the current claim phrasing breaks. | Extract disconfirming sources and isolate the exact violated assumption.; Run claim-splitting experiments with explicit sub-claim tags in manifests. |
| A hybrid architecture is needed: keep the core of commitment / dual error channels pre post commit but add explicit gating or interface separation. | 0.4 | Mixed evidence and conflict patterns suggest partial validity with missing structural guardrails. | Evaluate an ablation that isolates the proposed guardrail/interface addition.; Collect one adjacent-domain source that uses a similar split architecture. |

## Source Wording vs REE Translation

| timestamp | source | direction | confidence | evidence wording (preserved) | REE translation |
|---|---|---|---:|---|---|
| `2026-02-14T22:55:00Z` | Model-based influences on humans' choices and striatal prediction errors (2011, Neuron) | `mixed` | 0.66 | Evidence for separable planning and prediction-error computations exists, but measured neural signals show partial blending, yielding mixed support for strict dual-channel separation. | In REE terms, this implies `commitment / dual error channels pre post commit` may hold only in some regimes; the next step is to formalize those regimes explicitly. |
| `2026-02-14T21:25:00Z` | Video Representation Learning with Joint-Embedding Predictive Architectures (2024, arXiv) | `mixed` | 0.69 | VJ-VCR provides useful latent uncertainty decomposition evidence for precision stream design, but uncertainty semantics and policy coupling remain underdefined for commitment-stage dual-channel control and ethical blind-spot handling. | In REE terms, this implies `commitment / dual error channels pre post commit` may hold only in some regimes; the next step is to formalize those regimes explicitly. |
| `2026-02-14T20:55:00Z` | The architecture of cognitive control in the human prefrontal cortex (2003, Science) | `supports` | 0.74 | Evidence for hierarchical PFC control organization supports multi-level control routing and staged arbitration; direct mapping to specific REE mode priors and aversive-gating mechanics remains incomplete. | In REE terms, this is positive pressure on `commitment / dual error channels pre post commit` and supports keeping the mechanism, with tighter boundary conditions where failures recur. |
| `2026-02-14T20:40:00Z` | Anterior cingulate conflict monitoring and adjustments in control (2004, Science) | `supports` | 0.78 | Empirical conflict-monitoring evidence links ACC signals to downstream control adjustment, strongly supporting control routing claims; mapping to specific habenula-style aversive gating and dual-error channel implementation is still partial. | In REE terms, this is positive pressure on `commitment / dual error channels pre post commit` and supports keeping the mechanism, with tighter boundary conditions where failures recur. |
| `2026-02-14T20:25:00Z` | Prioritized memory access explains planning and hippocampal replay (2018, Nature Neuroscience) | `supports` | 0.73 | The prioritized replay account reproduces multiple replay signatures and links replay selection to gain/need-like utility, consistent with precision-weighted rollout selection; evidence remains model-based and indirect for dual commit channels. | In REE terms, this is positive pressure on `commitment / dual error channels pre post commit` and supports keeping the mechanism, with tighter boundary conditions where failures recur. |
| `2026-02-14T18:53:25.221110Z` | Run-pack `bridge_v2_mech_060_cross_channel_contamination_stress_s60022_20260214t185325220849z` in `commit_dual_error_channels` | `weakens` | 0.75 | FAIL with weakening direction | In REE terms, this is negative pressure on `commitment / dual error channels pre post commit` and suggests the claim is likely too strong or missing a key gating variable. |
| `2026-02-14T18:53:25.220388Z` | Run-pack `bridge_v2_mech_060_cross_channel_contamination_stress_s60021_20260214t185325220131z` in `commit_dual_error_channels` | `weakens` | 0.75 | FAIL with weakening direction | In REE terms, this is negative pressure on `commitment / dual error channels pre post commit` and suggests the claim is likely too strong or missing a key gating variable. |
| `2026-02-14T18:53:25.219464Z` | Run-pack `bridge_v2_mech_060_planning_leakage_probe_s60022_20260214t185325219106z` in `commit_dual_error_channels` | `supports` | 0.75 | PASS with supporting direction | In REE terms, this is positive pressure on `commitment / dual error channels pre post commit` and supports keeping the mechanism, with tighter boundary conditions where failures recur. |

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
