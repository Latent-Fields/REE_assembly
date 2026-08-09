# V3-EXQ-228c -- ARC-032 Theta-Rate Pathway DIRECT-READOUT test

**Status:** FAIL  **Evidence direction:** does_not_support  **Decision:** inconclusive
**Supersedes:** V3-EXQ-228b
**Claims:** ARC-032

## Gates

| Gate | Frac seeds | Pass |
|---|---|---|
| Precondition (goal_norm >= 0.05) | 1.00 | True |
| C1 persistence (active-zeroed cos >= 0.02) | 0.00 | False |
| C2 prox-noise (zeroed-active >= 0.005) | 0.00 | False |

## Direct-readout deltas (mean across seeds)

- persistence_cos (active - zeroed): +0.0000 (std_effect +0.51)
- prox_noise_temporal (zeroed - active): -0.0671 (std_effect -1.33)
- E3-tick resource lift (active - zeroed, info): +0.0000
- e3_tick_ratio (ACTIVE): 0.063

## Interpretation

ARC-032 DOES NOT SUPPORT: with the precondition met (goal_norm >= 0.05 on 1.00 of seeds), neither the persistence readout (C1, 0.00 of seeds) nor the proximity-noise readout (C2, 0.00 of seeds) showed the ARC-032-predicted effect at E3-tick granularity, measuring the claim's own pre-registered CONFIRMING DVs directly. REVERSED-TREND FINDING (registered, not dismissed): theta ACTIVE was the WORSE arm on >= 0.67 of seeds (less persistent on 0.33, noisier on 1.00). This converges with MECH-089's own already-confirmed EXQ-066/EXQ-122 result that static/uniform theta-averaging measurably HURTS E3's fine-grained discrimination -- implicating the flat-mean ThetaBuffer 'packaging' implementation, not the frontal-hippocampal-synchrony hypothesis itself. Route: investigate a phase/sequence-order-aware theta summary (Dragoi 2006 / Colgin 2016) rather than demoting ARC-032.
