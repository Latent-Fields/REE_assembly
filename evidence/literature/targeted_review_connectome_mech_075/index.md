# Literature Review: targeted_review_connectome_mech_075

**Claim:** MECH-075 -- Basal ganglia perform dopaminergic gain/threshold setting on hippocampal attractor dynamics.
**Review focus:** BG-hippocampal dopaminergic circuit; LC vs VTA specificity in dorsal vs ventral HPC; attractor/plasticity threshold effects.
**Date initiated:** 2026-04-15

---

## Key anatomical finding

Dopamine in **dorsal HPC** (E3 viability map substrate) originates primarily from **locus coeruleus (LC)**, not VTA.
Dopamine in **ventral HPC** (motivational/affective) originates primarily from **VTA**.
This bifurcates MECH-075 into:
- dorsal arm: LC-mediated arousal/novelty gain
- ventral arm: VTA-mediated RPE/reinforcement gain

## Entries

| entry_id | Paper | Year | Evidence direction | Confidence |
|----------|-------|------|-------------------|------------|
| 2026-04-15_mech_075_lc_dorsal_hpc_kempadoo2016 | Kempadoo et al. -- LC dopamine to dorsal HPC promotes spatial learning | 2016 | mixed | 0.80 |
| 2026-04-15_mech_075_lc_vta_memory_update_galvez2022 | Galvez-Marquez et al. -- LC (not VTA) gates dorsal HPC memory updating via D1/D5 and LTP | 2022 | supports | 0.78 |
| 2026-04-15_mech_075_d1_ltp_threshold_lemon2006 | Lemon and Manahan-Vaughan -- D1/D5 dopamine gates LTP and LTD threshold in CA1 | 2006 | supports | 0.82 |
| 2026-04-15_mech_075_vta_novelty_two_systems_duszkiewicz2018 | Duszkiewicz et al. -- Two dopaminergic systems (LC vs VTA) for distinct vs common novelty | 2018 | supports | 0.70 |
| 2026-08-11_mech_075_lc_ne_decision_time_gain_astonjones2005 | Aston-Jones & Cohen -- adaptive gain theory; phasic LC IS decision-locked (~100-150ms) but evidence is cortical, not hippocampal | 2005 | mixed | 0.55 |
| 2026-08-11_mech_075_lc_ca3_encoding_not_decisiontime_wagatsuma2018 | Wagatsuma et al. -- LC->CA3 optogenetic causal role is at ENCODING, readout is next-day retention | 2018 | weakens | 0.75 |
| 2026-08-11_mech_075_global_remapping_crossexposure_grella2019 | Grella et al. -- phasic LC triggers "global remapping," but only demonstrated across 20-min-separated exposures | 2019 | weakens | 0.65 |
| 2026-08-11_mech_075_ne_attractor_minutes_timescale_mckenzie2025 | McKenzie et al. -- NE tracks real-time hippocampal attractor deviation, but on a ~10-minute decay clock | 2025 (preprint) | mixed | 0.60 |
| 2026-08-11_mech_075_noradrenaline_plasticity_gate_not_online_prince2021 | Prince et al. -- current CA3 computational models code NE as a plasticity gate only, no online/fast channel | 2021 | weakens | 0.60 |

## Construct-validity finding (chip-20260810-mech075-litpull-lc-decision-time, 2026-08-11)

**Question posed by /failure-autopsy on V3-EXQ-905a:** does the LC-arousal literature this claim's anatomical_note cites (Kempadoo 2016 et al.) ground DECISION-TIME hippocampal attractor effects (the timescale V3-EXQ-905a's `basin_width` metric operates at -- computed synchronously with the LC_GAIN manipulation, within a single CEM decision step), or only PLASTICITY-TIMESCALE effects (learning/consolidation over minutes-to-hours)?

**Finding: the literature grounds plasticity/consolidation-timescale effects, not decision-time effects, and this holds across every methodology surveyed (optogenetics, pharmacology+IEG, computational modeling, and the one real-time electrophysiology/photometry study available):**

- The original four entries above (Kempadoo, Galvez-Marquez, Lemon & Manahan-Vaughan, Duszkiewicz) all ground LC/VTA dopaminergic gain in LTP/LTD threshold-setting and spatial *learning* -- synaptic-plasticity constructs, not within-trial geometry.
- Wagatsuma et al. 2018 (the closest existing causal LC->CA3 study) demonstrates the LC-CA3 causal window is at *encoding*, with the behavioral/representational readout deferred to a *next-day* retention test; silencing the same pathway during retrieval itself has no effect.
- Grella et al. 2019 -- the paper whose own vocabulary ("global remapping," "network reset") most resembles a decision-time attractor claim -- can only detect the effect via IEG expression compared across two exposures 20 minutes apart, and the authors state explicitly that their method cannot resolve within-session dynamics.
- McKenzie et al. 2025 is the single most direct match: real-time NE photometry and CA1 population dynamics are explicitly described in attractor language ("NE perturbed neural activity away from the stored attractor"). But the reported timescale is an exponential decay over **minutes** (first-minute vs. 10-minutes-in comparison), not seconds -- roughly two orders of magnitude slower than a single V3 decision step.
- Prince et al. 2021's computational model of CA3 ensemble formation gives acetylcholine a fast/online channel (immediate depolarization, immediate recurrent-weight change) but gives noradrenaline **only** a plasticity-gating role (STDP enablement) -- reflecting the same sparse, plasticity-oriented empirical base surveyed above.
- Aston-Jones & Cohen's 2005 adaptive gain theory establishes that phasic LC firing genuinely IS decision-locked (~90-150ms latency) and is proposed to modulate downstream *cortical* target-neuron gain at that timescale -- so decision-time LC effects are not implausible in principle -- but this evidentiary base is entirely cortical/oculomotor decision circuitry, never extended or tested for hippocampal attractor geometry.

**Conclusion for governance:** this is a genuine construct-validity gap, not a falsification of MECH-075's dorsal-leg mechanism. V3-EXQ-905a's null `basin_width` result under a correctly-calibrated LC_GAIN manipulation is consistent with -- arguably predicted by -- the field's own literature and models, none of which measure or model an LC/NE effect on hippocampal attractor geometry at decision-time. The nearest empirical analog that IS attractor-framed and within-session (McKenzie 2025) still operates on a ~10-minute clock. A future test of the dorsal leg should either (a) measure representational change over an extended window comparable to McKenzie's ~10-minute timescale rather than within a single CEM decision step, or (b) reframe the decisive metric toward an encoding/retention-style readout (matching Wagatsuma's design) rather than a same-step basin_width computation. Disposition on MECH-075's status/epistemic_category is left to governance.

## EXQ-192a interpretation

EXQ-192a probed a VTA-like novelty loop gain on dorsal HPC terrain and found a null result.
Consistent interpretation: the probe mis-targeted the VTA arm on a substrate (dorsal HPC) where the
relevant gain operator is LC-mediated. Not a falsification of MECH-075.

## Source: PubMed

All primary papers retrieved via PubMed search (2026-04-15). DOIs cited in each record.json.
