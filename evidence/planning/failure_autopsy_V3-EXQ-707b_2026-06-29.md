# Failure Autopsy -- V3-EXQ-707b (ARC-110 loop-segregation C2 release validation)

- **Generated (UTC):** 2026-06-29T19:22:13Z
- **Scope:** single
- **Status:** confirmed (user-gated 2026-06-29)
- **Run:** `v3_exq_707b_arc110_loop_segregation_c2_release_20260629T144004Z_v3`
- **Queue:** V3-EXQ-707b (supersedes V3-EXQ-707a/707; diagnostic; PROMOTES NOTHING)
- **Claim:** ARC-110 (parallel segregated cortico-BG-thalamic loops) -- `candidate`, `architectural_commitment`, `epistemic_category: substrate_conditional`, `implementation_phase: v3`. This run was ARC-110's `awaiting: v3_exq_707b_c2_release_validation_run_result`.
- **Outcome:** FAIL / `evidence_direction: weakens` / label `valid_null_loops_vary_but_no_conversion_ceiling_intrinsic_weakens_arc110`

## 1. Facts (no interpretation)

A pre-registered, decisive-either-way design. **All six readiness / non-degeneracy gates PASSED** -- this is NOT a substrate-not-ready artifact:

| precondition | measured | threshold | met |
|---|---|---|---|
| enough_divergent_seeds | 3.0 | 3.0 | yes |
| loops_carry_live_cross_loop_variance (flip/disagree) | 0.372 | 0.05 | yes |
| named_channel_routing_live (limbic routed per-candidate range) | **1.414** | 0.001 | **yes** |
| in_layer_null_live (S2 same-layer null perturbs committed selection) | 3 seeds | 2 | yes |
| learning_engaged + finer channels dissociable + delta_t non-flat | 0.00287 | 0.0001 | yes |
| candidate_pool_divergent (GAP-A) | 0.0234 | -- | yes |

`named_channel_routing_live` = 1.414 >> 0.001 is the gate that killed 707 (where DROP_LIMBIC was byte-identical to A1 = vacuous). This time the limbic loop genuinely carried per-candidate range, and `C2_drop_differs_from_a1 = True` on 3/3 seeds.

Committed-class entropy (the conversion DV; higher = more committed-action-class diversity):
- A0_SINGLE_ARENA: **0.9144**
- A1_LOOPS: **0.8385** (below A0)
- ARM_NOISE (valid in-layer null): 0.8232
- ARM_DROP_LIMBIC: 0.9328

C1 (A1_LOOPS strict-above A0 AND the live null) -- **FAILED, 0/3 seeds** (`C1_a1_n_seeds = 0`). C2 (A1 strict-above ARM_DROP_LIMBIC) -- **FAILED** (DROP_LIMBIC 0.933 > A1 0.838). Per ARC-110's own pre-registered grid (DECISIVE branch): a VALID null + loops carry live cross-loop variance BUT A1 does NOT lift committed-class entropy above A0/the null -> single-arena collapse was NOT the binding constraint -> ceiling INTRINSIC -> **weakens ARC-110**.

## 2. Claim-layer map

ARC-110's central HYPOTHESIS (verbatim): "the F-dominance conversion ceiling (MECH-439) is partly an ARTEFACT of the single-arena collapse -- ... with segregated loops F could dominate only the motor loop and could not drown the limbic 'is this worth committing to' computation." 707b tested exactly this with a fully-live segregated substrate and found A1_LOOPS ~ A0 (slightly below). **The artefact hypothesis is weakened**: loop segregation, as built (with static arithmetic cross-loop arbitration), does not lift the conversion ceiling. The weakens is valid and decisive **against the narrow single-arena-artefact hypothesis** -- it is NOT a falsification of ARC-110's architectural assertion that committed-action selection runs through segregated loops (which is biologically grounded).

## 3. Biological-reference triage (the core move)

Closest reference: the Alexander / DeLong / Strick (1986) parallel segregated cortico-basal ganglia-thalamic loops (motor / associative-dorsolateral-prefrontal / limbic-orbitofrontal-cingulate). These loops are biologically real and load-bearing -- a strong existence proof for the **class**. ARC-110 itself states the translation target is FUNCTIONAL, not anatomical mimicry.

Critical dependency in real brains: the segregated loops coexist with **dopamine-gated striatal plasticity** -- D1/D2 pathways LEARN the arbitration via dopamine. 707b built the loop STRUCTURE (segregation, ARC-109 D1/D2 split, MECH-452 loop-local traces) but the cross-loop arbitration is **static arithmetic** (per-loop z-score normalisation + a fixed Haber ascending-spiral combine), within an F + MECH-449 eligible set. Per the BG-assembly map (basal_ganglia_assembly_map_2026-06-22): the V3 gating/arbitration is pure arithmetic with NO dopamine-gated plasticity -- "learning is at valuation, not arbitration," and that IS the conversion-ceiling root.

So the FAIL matches a **missing-dependency signature**: segregated loops WITHOUT learned/dopamine-gated cross-loop arbitration. The limbic loop carries real range (gate passed) but never WINS, because the cross-loop combine is fixed arithmetic that still inherits F's static dominance -- it cannot learn to let the limbic "worth committing to" value override. ARC-110 was therefore **not tested under conditions where it could fully express itself** (a known dependency was absent), which is why the result NARROWS rather than falsifies.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **weakened (narrow hypothesis)** | the single-arena-artefact prediction is weakened; the architectural assertion is not falsified |
| Biological reference | **clear** | Alexander/DeLong/Strick loops real + load-bearing; but co-require DA-gated arbitration |
| Prerequisites / dependency | **missing** | dopamine-gated cross-loop arbitration plasticity (MECH-448/449/ARC-107) absent; only static arithmetic combine |
| Implementation completeness | partial | loop STRUCTURE built + live (all gates passed); arbitration LEARNING absent |
| Environment adequacy | adequate | same GAP-A reef-bipartite foraging substrate as the matched 704b arms |
| Measurement adequacy | **adequate (strong)** | all 6 non-degeneracy gates passed; committed-class entropy is the right DV; decisive either way |
| Integration adequacy | coupled-but-inert | loops segregate + carry variance, but the fixed arbitration doesn't convert it |
| Scale / capacity | adequate | not the binding constraint |

Dominant diagnosis: **missing-dependency (DA-gated cross-loop arbitration) -> narrow ARC-110, not demote.** The conversion ceiling is confirmed **intrinsic** to the F-dominance root (MECH-439), not a single-arena artefact.

## 5. Re-derive brake

First autopsy targeting ARC-110, and the direction is `weakens` (not `substrate_ceiling` / `non_contributory`). Brake does not fire and does not count.

## 6. Learning extracted

- Loop segregation ALONE (with static arithmetic cross-loop arbitration) does NOT lift the F-dominance conversion ceiling -- decisively, with a fully-live substrate (A1 0.838 ~ A0 0.914).
- The conversion ceiling is **intrinsic** to the F-dominance root (MECH-439), confirmed not to be an artefact of single-arena collapse. This is the pre-registered positive datum that fires the contingent MECH-439 /claim-synthesis.
- The loop substrate was successfully built and demonstrably live (all 6 non-degeneracy gates passed) -- positive evidence the v4_loop_segregation substrate works as engineered; it just isn't the conversion release.
- Discovered dependency: loop segregation needs coupling with learned/dopamine-gated cross-loop arbitration (MECH-448/449/ARC-107 dopamine-into-gating) to convert. This is the named next attack in the BG-assembly map.

## 7. Routing (user-confirmed)

1. **NARROW ARC-110** (not demote): record the `weakens` against the narrow single-arena-artefact hypothesis; narrow the claim to "loop segregation is necessary-but-not-sufficient; alone, with static arithmetic arbitration, it does not lift the F-dominance ceiling; the conversion route requires coupling with learned/dopamine-gated cross-loop arbitration (MECH-448/449/ARC-107)." Biology supports the architecture class; the dependency was absent, so this is NOT a clean falsification. Stays `candidate` / `substrate_conditional` / PROMOTES NOTHING.
2. **TRIGGER the pre-registered contingent /claim-synthesis on MECH-439** -- 707b failing to convert MEETS the condition set in failure_autopsy_700d-708-single-arena-ceiling_2026-06-29 ("run /claim-synthesis IF 707b also fails to convert"). The F-dominance conversion ceiling is now confirmed intrinsic across the decisive loop-segregation test. Surfaced as a follow-on chip at session close.
3. **Follow-on experiment NOT queued now**: the natural next test is A1_LOOPS coupled with dopamine-gated cross-loop arbitration (MECH-448/449/ARC-107) -- a redesign testing a DIFFERENT mechanism (new EXQ number, different claim_ids), gated on that arbitration-plasticity substrate being built. Noted, not queued.

## Draft evidence_quality_note (for governance; do not write here)

> V3-EXQ-707b (2026-06-29, C2-release validation, supersedes 707a/707) -> weakens (NARROW). DECISIVE pre-registered test with a FULLY-LIVE substrate: all 6 non-degeneracy gates passed (named_channel_routing_live 1.414 >> 0.001 -- limbic loop carried real per-candidate range, C2_drop_differs_from_a1 True 3/3; the 707 vacuous DROP==A1 is resolved). Committed-class entropy A1_LOOPS 0.838 ~ A0_SINGLE_ARENA 0.914 (BELOW); C1 0/3 seeds, C2 fail (DROP_LIMBIC 0.933 > A1). Per ARC-110's own pre-registered grid -> the conversion ceiling is INTRINSIC, NOT a single-arena-collapse artefact. WEAKENS the narrow single-arena-artefact hypothesis ONLY; does NOT falsify the architectural assertion (segregated loops are biologically real + load-bearing). NARROWED: loop segregation is necessary-but-not-sufficient; alone (with static arithmetic cross-loop arbitration) it does not lift the F-dominance ceiling. Missing dependency = dopamine-gated cross-loop arbitration plasticity (MECH-448/449/ARC-107); segregation built+live but arbitration does not LEARN, so F's static dominance persists in the cross-loop combine. Substrate build itself SUCCEEDED (positive datum). Stays candidate / substrate_conditional / PROMOTES NOTHING. Fires the contingent MECH-439 /claim-synthesis (conversion ceiling confirmed intrinsic).
