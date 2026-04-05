# Targeted Review: INV-049 -- Offline Update Necessity (General Computational Principle)

**Claims:** INV-049 (offline update phases as general computational necessity for model-building agents)

**Session:** cowork-2026-04-06-sleep-lit / wave_1 / inv049_inv050
**Date:** 2026-04-06

## Research Question

Is the necessity of periodic offline phases (during which action is suspended and the world model is reorganised via replay and simulation) a general computational principle for model-building agents, or is it a contingency of biological implementation?

## Key Questions Addressed

1. Is online sequential learning provably problematic for distributed representations? -- YES (McClelland 1995: catastrophic interference)
2. Has the offline replay solution been independently rediscovered in non-biological ML systems? -- YES (Kumaran 2016: DQN convergence)
3. Is there a capacity-saturation argument for offline necessity beyond interference? -- YES, with caveats (Tononi 2006: synaptic homeostasis)

## Entries

| Entry ID | Authors | Year | Evidence Direction | Confidence | Claims |
|----------|---------|------|-------------------|------------|--------|
| 2026-04-06_inv_049_cls_offline_necessity_mcclelland1995 | McClelland, McNaughton, O'Reilly | 1995 | supports | 0.92 | INV-049 |
| 2026-04-06_inv_049_cls_updated_ml_agents_kumaran2016 | Kumaran, Hassabis, McClelland | 2016 | supports | 0.88 | INV-049 |
| 2026-04-06_inv_049_shy_offline_necessity_tononi2006 | Tononi, Cirelli | 2006 | supports | 0.78 | INV-049 |

## Summary Assessment

All 3 entries support INV-049. The evidence package covers:
- Formal grounding of the catastrophic interference problem and replay as the necessary solution (McClelland 1995)
- Independent convergence on replay in artificial systems without biological constraints, confirming generality (Kumaran 2016)
- A second computational argument based on capacity saturation and homeostatic renormalisation (Tononi 2006)

**Main gap remaining:** INV-049 claims universality across all model-building architectures. The CLS evidence is strongest for gradient-descent distributed systems specifically. Whether non-gradient architectures (Bayesian updaters, symbolic planners) face equivalent offline necessity is not addressed in this evidence package. The claim is well-supported for the class of architectures REE uses.
