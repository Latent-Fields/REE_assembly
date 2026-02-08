# Regulatory Stack Model

This document introduces the **regulatory stack** framing: a layered architecture in which monoamines are reinterpreted as **meta-regulatory broadcast signals** rather than direct control knobs.

## The stack (top to bottom)

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

## Layer-by-layer breakdown

### Layer 1: Monoamines (Broadcast Tags / Requests)

**Old interpretation (direct-knob model):**

> Dopamine directly increases precision. Serotonin directly decreases commitment. Noradrenaline directly increases gain.

**New interpretation (meta-regulatory model):**

> Monoamines are **broadcast requests** that propagate diffusely across large regions of the brain. They do not directly modify synaptic parameters. Instead, they **bias the regulatory substrate** (astrocytes), which then mediates the actual parameter changes.

**Why broadcast?**

- Monoamine neurons have diffuse axonal projections (e.g., ventral tegmental area → entire cortex).
- This allows a single source to tag large regions with a common "policy bias."

**Why not direct?**

- The actual synaptic response to monoamines depends on:
  - Local receptor expression (heterogeneous).
  - Concurrent astrocytic state (permissive or suppressive).
  - Recent activity history (desensitization, adaptation).

### Layer 2: Astrocytic Regulatory Field

The **regulatory field** \(R(x,t)\) is a slowly varying state variable distributed over L-space. It mediates between broadcast monoaminergic signals and local synaptic parameters.

**Inputs to the field:**

- Monoaminergic tone (diffuse, slow-changing).
- Local neural activity (synaptic firing rates, prediction errors).
- Metabolic availability (glucose, lactate, O₂).
- Past regulatory state (history-dependence via slow dynamics).

**Field dynamics (schematic):**

\[
\frac{\partial R(x,t)}{\partial t} = -\frac{R(x,t)}{\tau_R} + f_{\text{mono}}(M(t)) + f_{\text{local}}(A(x,t)) + f_{\text{meta}}(E(x,t)) + \nabla^2 R(x,t)
\]

Where:

- \(\tau_R\): regulatory timescale (seconds to minutes; much slower than neuronal dynamics).
- \(f_{\text{mono}}(M(t))\): monoaminergic bias term (broadcast, spatially uniform or weakly varying).
- \(f_{\text{local}}(A(x,t))\): local activity term (neural firing, prediction error magnitude).
- \(f_{\text{meta}}(E(x,t))\): metabolic constraint term (energy availability).
- \(\nabla^2 R(x,t)\): spatial coupling (diffusion / gap junction coupling between astrocytes).

**Key properties:**

- **Slow:** \(\tau_R \gg \tau_{\text{neural}}\). Regulatory changes lag behind monoaminergic shifts.
- **Spatially heterogeneous:** \(R(x,t)\) varies across L-space depending on local conditions.
- **History-dependent:** past states influence current dynamics (integration over time).

### Layer 3: Local Synaptic Gain / Plasticity / Timing

The regulatory field state \(R(x,t)\) determines local synaptic parameters:

- **Gain:** \(g(x,t) = g_0 \cdot h_g(R(x,t))\)
- **Plasticity rate:** \(\eta(x,t) = \eta_0 \cdot h_\eta(R(x,t))\)
- **Precision weights (REE):** \(\alpha_k(x,t) = \alpha_{k,0} \cdot h_\alpha(R(x,t))\)

Where \(h_\bullet\) are monotonic functions mapping regulatory state to parameter multipliers.

**Result:** even if monoaminergic tone is globally uniform, local synaptic parameters can differ across space due to heterogeneous regulatory state.

### Layer 4: E2 / E1 Predictive Dynamics

The fast neuronal prediction machinery (E2, E1) operates at millisecond timescales, with parameters set by Layer 3. This is the "standard" REE computational substrate, now understood as modulated by the slower regulatory stack above it.

## ASCII diagram summary

```
Monoamines (broadcast)
    ↓ (seconds-minutes latency)
Astrocytic Regulatory Field R(x,t) (slow, spatial, history-dependent)
    ↓ (sub-second latency)
Synaptic Gain / Plasticity / Precision (alpha_k, eta, g)
    ↓ (millisecond timescale)
E2/E1 Prediction (fast neuronal dynamics)
```

## Reframing monoamines: from "direct knobs" to "meta-regulatory signals"

**Old model:**

- Dopamine → precision ↑
- Serotonin → precision ↓
- Noradrenaline → gain ↑

**New model:**

- Dopamine → *requests* increased commitment; actual effect depends on local regulatory state \(R(x,t)\) and metabolic capacity.
- Serotonin → *requests* option-holding; actual effect emerges from regulatory field mediation.
- Noradrenaline → *requests* reset/gain increase; implementation is slow and spatially heterogeneous.

**Key insight:**

> Monoamines are not control knobs. They are **advisory signals** that bias a deeper, slower regulatory substrate. The actual control is implemented by astrocytes, which integrate these signals with local activity and metabolic constraints.

## Implications for computational models

1. **Do not treat \(\alpha_k\) as an instantaneous function of monoaminergic "level."**
2. **Model the regulatory field \(R(x,t)\) as a separate dynamical system with its own timescale.**
3. **Allow for spatial heterogeneity:** different parts of L-space can have different precision/plasticity states simultaneously.
4. **Include metabolic constraints:** regulatory state should saturate or be suppressed when energy is low.

## Open questions

- What is the appropriate spatial resolution for \(R(x,t)\)? (Single field vs. depth-stratified fields?)
- Should \(R(x,t)\) be a scalar or a vector (multiple regulatory dimensions)?
- How to calibrate \(\tau_R\) relative to E1/E2 timescales?
- Can offline integration (sleep) be modeled as a "resetting" or "annealing" of \(R(x,t)\)?

These are research questions. This document establishes the framing; future work must fill in the details.
