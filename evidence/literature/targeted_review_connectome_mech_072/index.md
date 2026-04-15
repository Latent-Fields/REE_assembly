# Literature Review Index: MECH-072

**Claim:** Foreseeable-harm gating on residue accumulation reduces false attribution without degrading harm avoidance.

**Subject:** residue.foreseeable_harm_gating_reduces_false_attribution

**Status:** candidate, v3_pending

---

## Entries

| Entry ID | Source | Year | Class | Direction | Confidence |
|----------|--------|------|-------|-----------|------------|
| 2026-03-29_mech_072_ptsd_contextual_amnesia_desmedt2021 | Desmedt A, Chronic Stress | 2021 | behavioral_animal | supports | 0.58 |
| 2026-03-29_mech_072_stress_memory_decontextualization_schwabe2024 | Schwabe L, Biological Psychiatry | 2024 | theoretical_review | supports | 0.60 |
| 2026-04-15_mech_072_neural_causal_attribution_self_external_seidel2009 | Seidel et al., Social Neuroscience | 2009 | fmri_connectivity | supports | 0.62 |
| 2026-04-15_mech_072_moral_luck_foreseeability_attribution_young2010 | Young, Nichols & Saxe, Rev Phil Psych | 2010 | fmri_connectivity | supports | 0.68 |
| 2026-04-15_mech_072_counterfactual_credit_assignment_mesnard2021 | Mesnard et al., ICML 2021 | 2021 | computational_model | supports | 0.70 |
| 2026-04-15_mech_072_causal_influence_detection_rl_seitzer2021 | Seitzer et al., NeurIPS 2021 | 2021 | computational_model | supports | 0.65 |

---

## Coverage Summary

**Neuroscience domain (biological gate evidence):**
- Desmedt 2021: contextual memory as harm gating mechanism (rodent PTSD model)
- Schwabe 2024: stress-induced decontextualization causes miscalibrated attribution (review)
- Seidel 2009: fMRI neural dissociation of self vs external causal attribution (TPJ, dorsal striatum, dACC)
- Young 2010: moral luck / foreseeability gates blame -- "it's not what you do but what you know" (behavioral + fMRI)

**Computational/ML domain (discriminator gate design):**
- Mesnard 2021: counterfactual credit assignment disentangles agent vs environment contributions (ICML 2021)
- Seitzer 2021: situation-dependent causal influence detection via forward-model conditional mutual information (NeurIPS 2021)

---

## Key gaps remaining

- No paper directly tests real-time action-contingent harm attribution gating (all neuroscience evidence is retrospective/verbal)
- No paper specifically tests harm-channel asymmetric gating (Mesnard/Seitzer work with generic rewards)
- SD-011 (E2_harm_s) implementation needed before full biological grounding can be claimed
