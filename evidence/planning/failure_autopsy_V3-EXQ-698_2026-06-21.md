# Failure Autopsy -- V3-EXQ-698 (MECH-175 anticholinergic dual-pathway)

- **Generated:** 2026-06-21T12:45:21Z
- **Status:** `confirmed` (user-adjudicated, interactive /governance walk 2026-06-21T12:15Z)
- **Run:** `v3_exq_698_mech175_anticholinergic_dual_pathway_20260621T115716Z_v3`
- **Claim:** MECH-175 (anticholinergic burden → dementia risk via REM-suppression + cholinergic-deficit, additive) — `mechanism_hypothesis`, candidate, **standard** (no epistemic_category set), **not** v3_pending
- **Outcome:** FAIL, **self-stamped `weakens`** → **OVERTURNED to `non_contributory`**

## Verdict

This is the only pending FAIL this cycle whose self-stamped `weakens` would actually weight a claim (MECH-175 is standard, not substrate_ceiling/v3_pending) — which is exactly why the overturn matters. **Two independent reasons it is non_contributory, not a weakens:**

1. **Measurement floor.** The outcome DVs are at the noise floor *in the healthy ARM_A*: `harm_discrimination_mean 0.022` with per-seed **sign flips** (seed42 +0.047, seed43 −0.048, seed44 ~+0.06); `slot_differentiation` ranges 0.056–0.87 across 3 seeds. You cannot detect an *additive dual-pathway degradation* by differencing a baseline that is itself indistinguishable from noise. C5 manipulation checks passing (REM rollouts 30→0, encoder magnitude 1.0→0.3) confirms the *arms were applied* — not that the *readout discriminates*.

2. **Domain mismatch.** MECH-175 is a **clinical pharmacology / epidemiology** claim; its own notes say it is "testable via mediation analysis" on an anticholinergic-burden cohort (ACB → dementia conversion). A CausalGridWorld memory-consolidation proxy is not a fair test of a dementia-risk / additivity prediction. The grid-world rendering is at best a loose pathway-1 (REM→consolidation) analog; pathway-2 is a 0.3× encoder-lr knob and the dementia-risk endpoint has no grid-world referent.

## Manipulation worked, readout couldn't

| criterion | result |
|---|---|
| C5 manipulation checks | **PASS 3/2** (arms applied) |
| C1 slot-diff normal-vs-dual | FAIL 0/2 |
| C2 harm-disc normal-vs-dual | FAIL 0/2 |
| C3/C4 additivity (dual < min single) | FAIL 0/2 |

The "fair test passing manipulation checks" surface is misleading: the DV has no signal in the control arm.

## Routing → governance-reclassify (no substrate, no re-queue)

- **Mandatory:** overturn `weakens` → `non_contributory`; do not let it weight MECH-175.
- **Recommended (user decision at apply):** set `epistemic_category: out_of_domain` on MECH-175 — its decisive test is a clinical cohort mediation analysis, outside REE's substrate at any level; `out_of_domain` suppresses promote/demote + narrow_open_question and routes it to `research_anchor` / `literature_synthesis` handling rather than further grid-world experiments. If you'd rather keep it testable-in-principle, the non_contributory overturn alone is the floor.
- `recommended_substrate_queue_entry.action: none`. No re-queue.

## claim_ids note

`pending_review.md` showed "(no claim tags)" because the indexer reads flat `claim_ids` while this manifest carries `claim_ids_tested: [MECH-175]`. The tag is present and accurate — cosmetic display gap, no correction needed.

## Learning

A FAIL with passing manipulation checks is **not** automatically a fair weakens — check whether the outcome DV has signal in the healthy/control arm first. And a clean-running experiment can still test the wrong *layer*: MECH-175's decisive evidence is clinical, not a grid-world ablation.
