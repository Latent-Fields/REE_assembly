# Astrocyte‑aware Regulatory Stack

This module reframes **monoaminergic regulation** in REE by introducing the neuroscientific reality that astrocytes—non-neuronal glial cells—implement a slow, spatially resolved, history-dependent control substrate that mediates neuromodulation. Instead of treating monoamines (dopamine, serotonin, noradrenaline, etc.) as direct, instantaneous gain knobs, this perspective recognizes them as broadcast meta-regulatory signals that bias a deeper astrocytic regulatory field, which in turn modulates local synaptic gain, precision, plasticity, and timing.

## Table of contents

1. **[Astrocytes in Brief](astrocytes_in_brief.md)** — What astrocytes do relevant to computation.
2. **[Regulatory Stack Model](regulatory_stack_model.md)** — The layered control architecture: monoamines → astrocytic field → synaptic dynamics → E2/E1.
3. **[REE Component Mapping](ree_component_mapping.md)** — How astrocytic control integrates with L-space, precision control, and "care budget."
4. **[Implementation Hooks](implementation_hooks.md)** — Practical guidance for future code integration (module interfaces, time-scale separation).
5. **[References](references.md)** — Annotated bibliography of key neuroscience sources.

## How this changes REE

**Conceptual shift:**
> Monoamines are broadcast signals that bias a deeper regulatory substrate; astrocytes implement slow, spatially resolved control of gain/precision/plasticity.

**Implications for REE design:**

- **L-space is neuro-glial, not purely neuronal:** the latent state includes slow regulatory field dynamics alongside fast neuronal prediction.
- **Precision control is not instantaneous:** \(\alpha_k\) should be understood as the output of a slow field integrator, not a direct knob.
- **Regulation is spatially resolved and history-dependent:** different regions of L-space may have different gain/plasticity states at the same time, shaped by past activity and metabolic constraints.
- **Care budget / inertia acquire a mechanistic substrate:** the "resistance to rapid reprioritization" may reflect the slow dynamics of astrocytic regulatory state.
- **Sleep must recalibrate the regulatory field:** offline integration should restore not only synaptic weights but also the regulatory field state.

**What REE must not assume anymore:**

- Regulation is instantaneous.
- Regulation is spatially uniform across L-space.
- Regulation is memoryless (Markovian at short timescales).

This is **documentation-first:** no immediate code changes are required, but future implementations of precision control, learning rate modulation, and sleep recalibration should account for these layered dynamics.
