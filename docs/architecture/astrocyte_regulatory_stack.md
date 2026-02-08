# Astrocyte-Aware Regulatory Stack (Control Plane Mechanism)

**Claim Type:** mechanism_hypothesis  
**Scope:** Slow regulatory field mediating control-plane signals and precision routing  
**Depends On:** ARC-005 (control plane), INV-008 (precision routing), ARC-004 (L-space)  
**Status:** candidate  
**Claim ID:** MECH-001
<a id="mech-001"></a>

---

## Regulatory Stack Model (Excerpt)

This document introduces the **regulatory stack** framing: a layered architecture in which monoamines are reinterpreted as **meta-regulatory broadcast signals** rather than direct control knobs.

### The stack (top to bottom)

```
┌─────────────────────────────────────────────────────────────────┐
│  Monoamines (Dopamine, Serotonin, Noradrenaline, etc.)         │
│  ───────────────────────────────────────────────────────────    │
│  Broadcast meta-regulatory signals (tags / requests)            │
│  • "commit to this" (DA-like)                                   │
│  • "hold options open" (5-HT-like)                              │
│  • "reset / increase gain" (NA-like)                            │
│  • "focus sensory processing" (ACh-like)                        │
└───────────────────────┬─────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────────────┐
│  Astrocytic Regulatory Field                                    │
│  ───────────────────────────────────────────────────────────    │
│  Slow, spatially resolved, history-dependent control substrate  │
│  • Integrates monoaminergic tone over seconds-to-minutes        │
│  • Modulated by local activity, metabolic state, past history   │
│  • Coupled across space (gap junction syncytium)                │
│  • State: R(x,t) — regulatory field over L-space positions      │
└───────────────────────┬─────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────────────┐
│  Local Synaptic Gain / Plasticity / Timing                      │
│  ───────────────────────────────────────────────────────────    │
│  Fast parameters shaped by regulatory field                     │
│  • Synaptic efficacy (gain)                                     │
│  • Plasticity rate (learning rate / eta)                        │
│  • Temporal integration window                                  │
│  • Precision weights (alpha_k in REE)                           │
└───────────────────────┬─────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────────────┐
│  E2 / E1 Predictive Dynamics                                    │
│  ───────────────────────────────────────────────────────────    │
│  Fast neuronal prediction and inference                         │
│  • E2: short-horizon prediction (z_gamma, z_beta)               │
│  • E1: long-horizon prediction (z_theta, z_delta)               │
│  • Driven by prediction errors weighted by alpha_k              │
└─────────────────────────────────────────────────────────────────┘
```

### Key insight

Monoamines are not control knobs. They are **advisory signals** that bias a deeper, slower regulatory substrate. The actual control is implemented by astrocytes, which integrate these signals with local activity and metabolic constraints.

### Implications for computational models

1. Do not treat alpha_k as an instantaneous function of monoaminergic "level."
2. Model the regulatory field R(x,t) as a separate dynamical system with its own timescale.
3. Allow for spatial heterogeneity: different parts of L-space can have different precision/plasticity states simultaneously.
4. Include metabolic constraints: regulatory state should saturate or be suppressed when energy is low.

Source: `docs/processed/legacy_tree/docs/astrocyte_aware_regulatory_stack/regulatory_stack_model.md`

---

## Open Questions

<a id="q-002"></a>
### Q-002: What is the appropriate spatial resolution for R(x,t)?

<a id="q-003"></a>
### Q-003: Should R(x,t) be a scalar or a vector (multiple regulatory dimensions)?

<a id="q-004"></a>
### Q-004: How should tau_R be calibrated relative to E1/E2 timescales?

<a id="q-005"></a>
### Q-005: Can offline integration be modeled as a resetting or annealing of R(x,t)?

Source: `docs/processed/legacy_tree/docs/astrocyte_aware_regulatory_stack/regulatory_stack_model.md`

## Related Claims (IDs)

- MECH-001
- ARC-005
- INV-008
- ARC-004
- Q-002
- Q-003
- Q-004
- Q-005

## References / Source Fragments

- `docs/processed/legacy_tree/docs/astrocyte_aware_regulatory_stack/regulatory_stack_model.md`
- `docs/processed/legacy_tree/docs/astrocyte_aware_regulatory_stack/astrocytes_in_brief.md`
- `docs/processed/legacy_tree/docs/astrocyte_aware_regulatory_stack/implementation_hooks.md`
- `docs/processed/legacy_tree/docs/astrocyte_aware_regulatory_stack/ree_component_mapping.md`
- `docs/processed/legacy_tree/docs/astrocyte_aware_regulatory_stack/README.md`
