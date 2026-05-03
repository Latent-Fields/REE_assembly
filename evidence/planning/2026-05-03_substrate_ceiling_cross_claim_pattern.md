# Substrate-Ceiling Cross-Claim Pattern — V3-EXQ-504/506/508

**Date:** 2026-05-03
**Author:** session draft-conflicted-claim-experiments-2026-05-03T0129Z
**Status:** Observation note — for governance / planning consideration. No claim status changes proposed.
**Related:** EQN annotations 2026-05-02 on MECH-095, MECH-102, and 11 Q-claims tagging substrate-ceiling as the failure mode.

## Summary

Three of five experiments queued and run on 2026-05-03 (V3-EXQ-504, V3-EXQ-506, V3-EXQ-508) FAILed in the same shape: **the absolute / negative-control criterion passes, but every discrimination criterion fails.** Each was designed to probe a different claim with a different substrate. The convergent failure mode is the substrate-ceiling pattern already annotated for MECH-095 and MECH-102 yesterday — it now appears to be a wider phenomenon than originally scoped.

The two PASSes (V3-EXQ-505 MECH-093, V3-EXQ-507 ARC-026) are exactly the experiments where the test does not require inter-condition discrimination on a learned substrate — V3-EXQ-505 drives `MultiRateClock.update_e3_rate_from_beta` directly with synthetic z_beta, and V3-EXQ-507 measures monotone non-collapse of an env-derived metric across capacity. Neither passes through a substrate that has to learn to distinguish conditions.

## The pattern

| Experiment | Claim | Negative-control / absolute criterion | Discrimination criteria | Read |
|---|---|---|---|---|
| V3-EXQ-504 | MECH-153 | C1 ARM_A no-loss cosine=1.0000 in all 5 seeds — collapse confirmed | C2 ARM_B hard_CE cosine=1.0000 (FAIL); C3 ARM_C soft_contrastive cosine=1.0000 (FAIL); ARM_C harm_r2 = **−3036** (probe blew up); ARM_B harm_r2 = **−0.094** (no signal) | Both supervised arms FAIL to differentiate. Supervised objective is **necessary but insufficient**. |
| V3-EXQ-506 | MECH-095 | C4 absolute gap_agent = **4.04** (≥0.10 threshold, PASS 3/3) | C1/C2/C3 condition ratios all ≈ **1.00** (FAIL 0/3 each) | E2_harm_s produces a large counterfactual gap **regardless of whether the underlying process is action-controlled.** Forward model learned "actions matter" universally. |
| V3-EXQ-508 | ARC-033 | C2 ARM_B world-only SNR = **1.01** (≤1.2 threshold, PASS — collapses as architecturally predicted) | C1 ARM_A E2_harm_s SNR = **0.96** (FAIL — also collapses) | World-only ablation collapses as predicted, but E2_harm_s **also fails to discriminate harm-event vs quiet-tick** ticks. The relative gap exists but is below threshold. |

In each case the **easy half** of the prediction holds (the substrate exists, the negative control behaves as expected, the absolute scale is in range), and the **hard half** — that the substrate carries the specific causal/structural signal the claim asserts — does not.

## Why this matters more than three individual FAILs

Each FAIL on its own would be candidate-recommendation noise: tune a hyperparameter, increase warmup, redesign the metric. The convergent shape across three structurally-different claims, on three different substrates (E1 ContextMemory; E2_harm_s comparator on synthetic; E2_harm_s comparator in env), is the load-bearing signal:

- **MECH-153** ContextMemory has the supervised-objective wiring but the resulting cue_context vectors do not differentiate even under a continuous-hazard contrastive loss. The substrate IS active (ContextMemory.write fires; gradients flow) but the resulting representations remain degenerate. Upstream z_world capacity is the prime suspect.
- **MECH-095** E2_harm_s with SD-013 interventional loss produces large absolute counterfactual gaps but does not encode a sense of *which conditions are agent-controlled*. The comparator's signal is structurally action-sensitive but generatively oblivious — it cannot distinguish action-genuine from action-correlated conditions.
- **ARC-033** On the body-damage substrate, the world-only ablation collapses as architecturally predicted (good — SD-010 perpendicularity is real), but E2_harm_s on the harm stream does not significantly outperform it. The predicted dual-stream signal is below detection threshold within 100 warmup eps.

These are **not three independent bugs**. They are three instances of the same structural property: the V3 substrate **has** the wiring the claim asserts, but the wiring does not carry the **information** at the granularity the claim asserts.

## Relation to the existing substrate-ceiling annotation

The 2026-05-02 governance work added EQN annotations to MECH-095, MECH-102, and 11 Q-claims tagging substrate-ceiling as the failure mode. Those annotations were retrospective — the claims had already accumulated FAILs and the substrate-ceiling reading was the diagnosis. Today's three FAILs are **prospective evidence in the same shape, from claims that were not yet flagged**. MECH-153 and ARC-033 should now also be considered for the same EQN annotation.

The Phase 3 wave 2 `epistemic_category` schema landed 2026-05-02 with `substrate_ceiling` as one of seven canonical values. Of the three FAILing claims here, only MECH-095 currently carries it. MECH-153 and ARC-033 are candidates for re-annotation under the same field.

## What this implies for the next planning step

Two readings, both load-bearing for the substrate roadmap:

**Reading A (substrate enrichment):** the V3 latent stack as currently parameterised does not carry enough information for the claims to be testable. The substrate roadmap (`docs/architecture/substrate_roadmap.md`) lists three H-priority enrichments (foreclosure primitives, multi-resource heterogeneity, long-horizon dynamics). None of them directly addresses "z_world / z_harm_s representational capacity for fine-grained discrimination." A fourth H-priority enrichment — **representational capacity at the encoder** — may be warranted.

**Reading B (test-design ceiling):** the experimental templates are at substrate ceiling. The synthetic-injection style (V3-EXQ-505/506) cleanly tests the implementation but cannot test what the claim predicts about generative structure. The full-env style (V3-EXQ-504/508) tests generative structure but is bounded by env complexity (CausalGridWorldV2 is a small substrate). A third class of test — agent-vs-agent or richer-action-repertoire — may be required, which is V4 territory per `docs/architecture/v4_spec.md`.

Both readings could be true. The convergent shape of today's FAILs is consistent with both. The next planning decision is whether to (i) commission a representational-capacity enrichment as part of the V3 substrate roadmap, or (ii) accept that several backlog claims are V4-bound for test-design reasons even if their architectures land in V3.

## Specific actions worth considering

These are *suggestions* for the next governance walk, not decisions:

1. **Add EQN annotation to MECH-153** noting the V3-EXQ-504 substrate-ceiling pattern (both supervised arms collapse; not just the no-loss baseline). Mirror the MECH-095 annotation language.
2. **Add EQN annotation to ARC-033** noting the V3-EXQ-508 result: world-only ablation collapses as predicted (architectural prediction confirmed) but E2_harm_s does not carry sufficient signal at current substrate parameterisation.
3. **Consider `epistemic_category: substrate_ceiling`** for MECH-153 and ARC-033 (currently neither carries the field).
4. **Review V3-EXQ-505 PASS as load-bearing for MECH-093.** The substrate-level dissociation is exactly the kind of evidence the EXQ-097 negative rate-gap puzzle needed; it shows the implementation is correct and the failure must be upstream (z_beta encoder under env-loop conditions). MECH-093 may be promotable on this evidence (substrate clean) plus a follow-up env-loop experiment to characterise the z_beta-vs-arousal correlation directly.
5. **Defer behavioural-grade follow-ups** to V3-EXQ-504/506/508 until the representational-capacity question is settled. Re-running with more warmup is unlikely to change the shape of the result.

## Numbers for the record

```
V3-EXQ-504 MECH-153 (FAIL):
  ARM_A no-loss      cosine=1.0000  (5/5 seeds collapsed)
  ARM_B hard_CE      cosine=1.0000  (0/5 seeds <0.80)   harm_r2 = -0.094
  ARM_C soft_contras cosine=1.0000  (0/5 seeds <0.80)   harm_r2 = -3036

V3-EXQ-506 MECH-095 (FAIL):
  gap_agent    = 4.04  (3/3 seeds >= 0.10)
  ratio_a/env  = 1.005  (0/3 seeds >= 1.5)
  ratio_a/col  = 1.002  (0/3 seeds >= 1.5)
  ratio_a/corr = 0.991  (0/3 seeds >= 1.5)

V3-EXQ-508 ARC-033 (FAIL):
  ARM_A E2_harm_s ON   SNR = 0.962  (0/3 seeds >= 1.5)
  ARM_B world-only     SNR = 1.010  (3/3 seeds <= 1.2 — ablation collapse confirmed)

V3-EXQ-505 MECH-093 (PASS): all 3 criteria 3/3 — substrate dissociation clean.
V3-EXQ-507 ARC-026 (PASS): all 3 criteria 3/3 — capacity sweep no crowding-out.
```

## Provenance

This note was prepared by the session that drafted V3-EXQ-504..508. Recommendation: bring to the next governance walk for review. No claim status changes have been made on the basis of this note.
