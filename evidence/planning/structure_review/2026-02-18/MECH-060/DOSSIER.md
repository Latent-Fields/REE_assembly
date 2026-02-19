# Structure Review Dossier: MECH-060

Generated: `2026-02-18T19:44:27.698616Z`
Cycle: `2026-02-18`

## Claim Description

MECH-060 is a mechanism hypothesis about commitment / dual error channels pre post commit.

## Where This Fits in REE as a Whole

This sits in REE's mechanism layer and links architecture commitments to testable signatures. It depends on 5 upstream claim(s): `ARC-003`, `ARC-005`, `ARC-015`, `INV-012`, `MECH-057`. It currently feeds 4 downstream claim(s): `IMPL-023`, `INV-019`, `MECH-056`, `MECH-061`. Primary architecture anchor: `docs/architecture/agency_responsibility_flow.md#mech-060`.

## Structural Pressure Signals

- Recommendation: `escalate_architecture_decision` (consider_new_structure=true)
- Trigger signals: external_precedence_pressure, high_conflict_ratio, recurring_failure_signatures
- Conflict ratio: 0.875
- Overall confidence: 0.707

## Evidence Mix and Why It Looks This Way

- Direction counts: supports=81, weakens=63, mixed=4, unknown=0.
- Experimental mix: supports=72, weakens=63, mixed=0, unknown=0.
- Literature mix: supports=9, weakens=0, mixed=4, unknown=0.
- Direction narrative: Evidence is directionally split between support and weakening, which indicates either claim over-breadth or hidden context dependence.
- Source narrative: Both experiment and literature are present. Use disagreement between these sources as a cue to refine claim scope before making status promotions.

## Evidence Pull (Current Findings + Alternatives)

| alternative | confidence_estimate | current_findings | next_pull_focus |
|---|---:|---|---|
| commitment / dual error channels pre post commit is broadly correct, but failures are boundary-condition failures. | 0.555 | Supporting evidence dominates enough to keep the core mechanism plausible. | Completed 2026-02-19: stress ablations comparing `single_error_stream` vs `pre_post_split_streams` in `commit_dual_error_channels` (`2026-02-17T225311Z_*` and `2026-02-17T225337Z_*`) show boundary-conditioned recovery when channels are split.; Completed 2026-02-19: replication/adjacent pull captured in `targeted_review_v3_prefrontal_control` and `targeted_review_connectome_mech_060` entries. |
| commitment / dual error channels pre post commit is over-scoped and should be narrowed or split. | 0.421 | Weakening evidence indicates at least one sub-regime where the current claim phrasing breaks. | Completed 2026-02-19: disconfirming evidence isolated from failing `single_error_stream` runs with recurring signatures `mech060:postcommit_channel_contamination`, `mech060:attribution_reliability_break`, `mech060:commitment_reversal_spike`.; Completed 2026-02-19: claim-scoped split probes captured in `claim_probe_mech_060` manifests (`2026-02-17T225245Z_*`, `2026-02-17T225311Z_*`, `2026-02-17T225337Z_*`). |
| A hybrid architecture is needed: keep the core of commitment / dual error channels pre post commit but add explicit gating or interface separation. | 0.421 | Mixed evidence and conflict patterns suggest partial validity with missing structural guardrails. | Completed 2026-02-19: guardrail ablation isolating split-channel interface added via `commit_dual_error_channels` split-vs-merged condition pairs.; Completed 2026-02-19: adjacent-domain split-architecture source captured (e.g., `targeted_review_connectome_mech_060/entries/2026-02-15_mech060_connectome_agency_comparator_review_nrn2017`). |

## Evidence Pull Completion (2026-02-19)

1. Stress-regime boundary pull completed.
- Evidence: split/merged comparisons in `evidence/experiments/commit_dual_error_channels/runs/2026-02-17T225311Z_commit-dual-error-channels_seed89_single_error_stream_toyenv_internal_minimal` and paired split run `...seed89_pre_post_split_streams...`, plus follow-on seed expansions in `2026-02-17T225337Z_*`.

2. Disconfirming-source extraction completed.
- Evidence: weakening signatures extracted from `single_error_stream` manifests (post-commit contamination + attribution break + commitment reversal spike).

3. Claim-splitting pull completed.
- Evidence: claim-scoped probe manifests under `evidence/experiments/claim_probe_mech_060/runs/` with explicit `experiment_type=claim_probe_mech_060`.

4. Adjacent-domain split-architecture pull completed.
- Evidence: `evidence/literature/targeted_review_connectome_mech_060/entries/2026-02-15_mech060_connectome_agency_comparator_review_nrn2017` and related connectome entries.

## Source Wording vs REE Translation

| timestamp | source | direction | confidence | evidence wording (preserved) | REE translation |
|---|---|---|---:|---|---|
| `2026-02-17T22:53:37Z` | Run-pack `2026-02-17T225337Z_commit-dual-error-channels_seed151_pre_post_split_streams_toyenv_internal_minimal` in `commit_dual_error_channels` | `supports` | 0.75 | PASS with supporting direction | In REE terms, this is positive pressure on `commitment / dual error channels pre post commit` and supports keeping the mechanism, with tighter boundary conditions where failures recur. |
| `2026-02-17T22:53:37Z` | Run-pack `2026-02-17T225337Z_commit-dual-error-channels_seed131_pre_post_split_streams_toyenv_internal_minimal` in `commit_dual_error_channels` | `supports` | 0.75 | PASS with supporting direction | In REE terms, this is positive pressure on `commitment / dual error channels pre post commit` and supports keeping the mechanism, with tighter boundary conditions where failures recur. |
| `2026-02-17T22:53:37Z` | Run-pack `2026-02-17T225337Z_commit-dual-error-channels_seed101_pre_post_split_streams_toyenv_internal_minimal` in `commit_dual_error_channels` | `supports` | 0.75 | PASS with supporting direction | In REE terms, this is positive pressure on `commitment / dual error channels pre post commit` and supports keeping the mechanism, with tighter boundary conditions where failures recur. |
| `2026-02-17T22:53:37Z` | Run-pack `2026-02-17T225337Z_claim-probe-mech-060_seed151_pre_post_split_streams_toyenv_internal_minimal` in `claim_probe_mech_060` | `supports` | 0.75 | PASS with supporting direction | In REE terms, this is positive pressure on `commitment / dual error channels pre post commit` and supports keeping the mechanism, with tighter boundary conditions where failures recur. |
| `2026-02-17T22:53:37Z` | Run-pack `2026-02-17T225337Z_claim-probe-mech-060_seed131_pre_post_split_streams_toyenv_internal_minimal` in `claim_probe_mech_060` | `supports` | 0.75 | PASS with supporting direction | In REE terms, this is positive pressure on `commitment / dual error channels pre post commit` and supports keeping the mechanism, with tighter boundary conditions where failures recur. |
| `2026-02-17T22:53:37Z` | Run-pack `2026-02-17T225337Z_claim-probe-mech-060_seed101_pre_post_split_streams_toyenv_internal_minimal` in `claim_probe_mech_060` | `supports` | 0.75 | PASS with supporting direction | In REE terms, this is positive pressure on `commitment / dual error channels pre post commit` and supports keeping the mechanism, with tighter boundary conditions where failures recur. |
| `2026-02-17T22:53:11Z` | Run-pack `2026-02-17T225311Z_commit-dual-error-channels_seed89_single_error_stream_toyenv_internal_minimal` in `commit_dual_error_channels` | `weakens` | 0.75 | FAIL with weakening direction | In REE terms, this is negative pressure on `commitment / dual error channels pre post commit` and suggests the claim is likely too strong or missing a key gating variable. |
| `2026-02-17T22:53:11Z` | Run-pack `2026-02-17T225311Z_commit-dual-error-channels_seed89_pre_post_split_streams_toyenv_internal_minimal` in `commit_dual_error_channels` | `supports` | 0.75 | PASS with supporting direction | In REE terms, this is positive pressure on `commitment / dual error channels pre post commit` and supports keeping the mechanism, with tighter boundary conditions where failures recur. |

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
