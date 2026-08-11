# V3-EXQ-228d -- ARC-032 Theta-Rate Pathway PHASE-WEIGHTED-READOUT test

**Status:** FAIL  **Evidence direction:** does_not_support  **Decision:** inconclusive
**Supersedes:** V3-EXQ-228c
**Claims:** ARC-032

## Gates

| Gate | Frac seeds | Pass |
|---|---|---|
| Precondition (goal_norm >= 0.05) | 1.00 | True |
| C1 persistence (active-zeroed cos >= 0.02) | 0.00 | False |
| C2 prox-noise (zeroed-active >= 0.005) | 0.00 | False |

## Direct-readout deltas (mean across seeds)

- persistence_cos (active - zeroed): -0.0000 (std_effect -0.12)
- prox_noise_temporal (zeroed - active): -0.1095 (std_effect -6.10)
- E3-tick resource lift (active - zeroed, info): +0.0000
- e3_tick_ratio (ACTIVE): 0.066

## Interpretation

ARC-032 DOES NOT SUPPORT: with the precondition met (goal_norm >= 0.05 on 1.00 of seeds), neither the persistence readout (C1, 0.00 of seeds) nor the proximity-noise readout (C2, 0.00 of seeds) showed the ARC-032-predicted effect at E3-tick granularity, measuring the claim's own pre-registered CONFIRMING DVs directly. REVERSED-TREND FINDING (registered, not dismissed): theta ACTIVE was the WORSE arm on >= 0.67 of seeds (less persistent on 0.67, noisier on 1.00) -- EVEN WITH SD-100's phase-weighted, order-sensitive summary in place of the flat mean 228c used. This is a STRONGER finding than 228c's reversal: it is no longer attributable to the flat mean's permutation-invariance (the 228c autopsy's diagnosed cause), since 228d's THETA_ACTIVE arm does not use a flat mean. Route: flag for governance re-examination of ARC-032's implementation-gap disposition (rather than a further /implement-substrate iteration) -- either the SD-100 kernel's parameterisation (theta_phase_concentration) is itself inadequate, or the reversal is not a ThetaBuffer-packaging artifact at all and the claim-level frontal-hippocampal-synchrony hypothesis should be reconsidered against this substrate.
