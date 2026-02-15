# Structure Review Dossier: MECH-058

Generated: `2026-02-15T11:20:45.691375Z`
Cycle: `2026-02-15`

## Claim Description

MECH-058 is a mechanism hypothesis about jepa substrate / ema target anchor timescale separation.

## Where This Fits in REE as a Whole

This sits in REE's mechanism layer and links architecture commitments to testable signatures. It depends on 5 upstream claim(s): `ARC-001`, `ARC-002`, `ARC-004`, `ARC-015`, `MECH-057`. It currently feeds 1 downstream claim(s): `IMPL-023`. Primary architecture anchor: `docs/architecture/agency_responsibility_flow.md#mech-058`.

## Structural Pressure Signals

- Recommendation: `consider_new_structure` (consider_new_structure=true)
- Trigger signals: external_precedence_pressure, high_conflict_ratio, recurring_failure_signatures
- Conflict ratio: 0.957
- Overall confidence: 0.676

## Evidence Mix and Why It Looks This Way

- Direction counts: supports=24, weakens=22, mixed=1, unknown=0.
- Experimental mix: supports=22, weakens=22, mixed=0, unknown=0.
- Literature mix: supports=2, weakens=0, mixed=1, unknown=0.
- Direction narrative: Evidence is directionally split between support and weakening, which indicates either claim over-breadth or hidden context dependence.
- Source narrative: Both experiment and literature are present. Use disagreement between these sources as a cue to refine claim scope before making status promotions.

## Evidence Pull (Current Findings + Alternatives)

| alternative | confidence_estimate | current_findings | next_pull_focus |
|---|---:|---|---|
| jepa substrate / ema target anchor timescale separation is broadly correct, but failures are boundary-condition failures. | 0.529 | Supporting evidence dominates enough to keep the core mechanism plausible. | Target stress regimes where failures cluster and test whether boundary constraints recover stability.; Pull replication papers that test similar mechanisms under distribution shift. |
| jepa substrate / ema target anchor timescale separation is over-scoped and should be narrowed or split. | 0.449 | Weakening evidence indicates at least one sub-regime where the current claim phrasing breaks. | Extract disconfirming sources and isolate the exact violated assumption.; Run claim-splitting experiments with explicit sub-claim tags in manifests. |
| A hybrid architecture is needed: keep the core of jepa substrate / ema target anchor timescale separation but add explicit gating or interface separation. | 0.449 | Mixed evidence and conflict patterns suggest partial validity with missing structural guardrails. | Evaluate an ablation that isolates the proposed guardrail/interface addition.; Collect one adjacent-domain source that uses a similar split architecture. |

## Source Wording vs REE Translation

| timestamp | source | direction | confidence | evidence wording (preserved) | REE translation |
|---|---|---|---:|---|---|
| `2026-02-15T09:51:20.253293Z` | Run-pack `exp_0015_20260215T095120253293Z` in `jepa_anchor_ablation` | `weakens` | 0.75 | FAIL with weakening direction | In REE terms, this is negative pressure on `jepa substrate / ema target anchor timescale separation` and suggests the claim is likely too strong or missing a key gating variable. |
| `2026-02-14T22:45:00Z` | Bootstrap your own latent: A new approach to self-supervised Learning (2020, arXiv preprint) | `supports` | 0.78 | BYOL directly uses a slow EMA target with a fast online predictor and shows stable learning without collapse, closely matching target-anchor/predictor timescale separation. | In REE terms, this is positive pressure on `jepa substrate / ema target anchor timescale separation` and supports keeping the mechanism, with tighter boundary conditions where failures recur. |
| `2026-02-14T21:10:00Z` | Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture (2023, CVPR 2023) | `mixed` | 0.76 | I-JEPA strongly supports latent predictive substrate and target-anchor timescale separation, but leaves action-conditioned control routing, ethical constraints, and uncertainty calibration interfaces underspecified for direct REE control-plane mapping. | In REE terms, this implies `jepa substrate / ema target anchor timescale separation` may hold only in some regimes; the next step is to formalize those regimes explicitly. |
| `2026-02-14T20:00:00Z` | Run-pack `2026-02-14T200000Z_jepa-anchor-ablation_seed47_ema_anchor_on` in `jepa_anchor_ablation` | `supports` | 0.75 | PASS with supporting direction | In REE terms, this is positive pressure on `jepa substrate / ema target anchor timescale separation` and supports keeping the mechanism, with tighter boundary conditions where failures recur. |
| `2026-02-14T20:00:00Z` | Run-pack `2026-02-14T200000Z_jepa-anchor-ablation_seed47_ema_anchor_off` in `jepa_anchor_ablation` | `weakens` | 0.75 | FAIL with weakening direction | In REE terms, this is negative pressure on `jepa substrate / ema target anchor timescale separation` and suggests the claim is likely too strong or missing a key gating variable. |
| `2026-02-14T20:00:00Z` | Run-pack `2026-02-14T200000Z_jepa-anchor-ablation_seed29_ema_anchor_on` in `jepa_anchor_ablation` | `supports` | 0.75 | PASS with supporting direction | In REE terms, this is positive pressure on `jepa substrate / ema target anchor timescale separation` and supports keeping the mechanism, with tighter boundary conditions where failures recur. |
| `2026-02-14T20:00:00Z` | Run-pack `2026-02-14T200000Z_jepa-anchor-ablation_seed29_ema_anchor_off` in `jepa_anchor_ablation` | `weakens` | 0.75 | FAIL with weakening direction | In REE terms, this is negative pressure on `jepa substrate / ema target anchor timescale separation` and suggests the claim is likely too strong or missing a key gating variable. |
| `2026-02-14T20:00:00Z` | Run-pack `2026-02-14T200000Z_jepa-anchor-ablation_seed11_ema_anchor_on` in `jepa_anchor_ablation` | `supports` | 0.75 | PASS with supporting direction | In REE terms, this is positive pressure on `jepa substrate / ema target anchor timescale separation` and supports keeping the mechanism, with tighter boundary conditions where failures recur. |

## Left-Field Suggestions

1. Try a three-timescale anchor (slow/medium/fast) with disagreement alarms.
- Why it may inspire: Could reveal whether current failures come from anchor lag mismatch rather than anchor concept failure.
- First test: Measure drift and collapse signatures under timescale triad ablations.
2. Introduce anchor reset checkpoints only on validated low-drift windows.
- Why it may inspire: Could reduce catastrophic anchor drift under distribution shift.
- First test: Compare drift under continuous EMA vs gated reset.
3. Use predictor ensembles to stress-test anchor stability assumptions.
- Why it may inspire: Could separate target-anchor instability from predictor idiosyncrasy.
- First test: Track cluster collapse frequency across single vs ensemble predictor runs.

## Decision Prompts

1. Which part of the claim appears stable across both supporting and weakening evidence?
2. If this claim were split into two sub-claims, where is the cleanest boundary?
3. What is the smallest architecture change that would most likely remove the top recurring failure signature?
4. What evidence next week would most likely change your current decision?
