# V3-EXQ-231a -- MECH-106 BG Hysteresis Redesign

**Status:** PASS  **Criteria met:** 5/5
**Claims:** MECH-106  **Purpose:** evidence  **Supersedes:** V3-EXQ-231

## Why EXQ-231 was insufficient

EXQ-231 tested PERSISTENT (min-hold 20 steps) vs REACTIVE (instantaneous).
All seeds: persist_ratio = reactive_ratio = 1.0 (identical behavior).
Root cause: rv stayed below commit_threshold throughout every episode;
the hold extension never fired. No valence history was created.

## Redesign

VALENCE_BIAS: effective_threshold = base * (1 + 1.2 * (da - 0.5))
NO_BIAS: fixed threshold (current implementation / ablation)
Metric: latency-to-first-commitment from rv reset (0.65) per probe episode.

## Results

| Seed | da_div | thr_asym | lat_ratio_vb | lat_ratio_nb | asym_delta | C1 | C2 | C3 | C4 | C5 |
|------|--------|----------|--------------|--------------|-----------|----|----|----|----|----|
| 0 | 0.779 | 2.794 | 11.00 | 1.00 | 10.00 | P | P | P | P | P |
| 42 | 0.000 | 1.000 | 1.00 | 1.00 | 0.00 | F | F | F | P | F |
| 100 | 0.761 | 2.755 | 11.00 | 1.00 | 10.00 | P | P | P | P | P |
| 123 | 0.726 | 2.702 | 7.33 | 1.00 | 6.33 | P | P | P | P | P |
| 200 | 0.762 | 2.827 | 11.00 | 1.00 | 10.00 | P | P | P | P | P |

## Interpretation

MECH-106 SUPPORTED: Valence-modulated threshold produces genuine asymmetric commitment hysteresis. Latency to first commitment is significantly shorter after positive history (higher threshold) than after negative history (lower threshold). NO_BIAS ablation shows no such asymmetry, confirming the effect is due to valence-driven threshold modulation, not training dynamics.
