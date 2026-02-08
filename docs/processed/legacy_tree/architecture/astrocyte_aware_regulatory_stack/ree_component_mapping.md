# REE Component Mapping

This document maps the astrocyte-aware regulatory stack concepts into existing REE terminology and identifies what must change in REE's conceptual commitments.

## L-space is neuro-glial (not purely neuronal)

**Original REE commitment:**

> L-space is a multi-depth latent state \(z(t) = \{z_\gamma, z_\beta, z_\theta, z_\delta\}\) stratified by prediction horizon.

**Astrocyte-aware extension:**

> L-space includes both **fast neuronal prediction state** (as before) and **slow regulatory field state** \(R(x,t)\) that modulates the neuronal dynamics.

The full state is now:

\[
\text{L-state}(t) = \Big( z_\gamma(t), z_\beta(t), z_\theta(t), z_\delta(t), R(x,t) \Big)
\]

Where:

- \(z_k(t)\): fast neuronal latent variables (millisecond timescale).
- \(R(x,t)\): slow regulatory field (seconds-to-minutes timescale).

**Spatial structure:**

- \(z_k\) are typically vector-valued (dimension determined by layer width).
- \(R(x,t)\) is distributed over the same spatial index as the neuronal state (or a coarser-grained version).

**Implication:** any operation that queries or updates L-space must account for the regulatory field. This includes:

- Latent prediction (E1/E2).
- Trajectory selection (E3 must evaluate trajectories under different regulatory states).
- Offline integration (sleep must recalibrate \(R(x,t)\) as well as synaptic weights).

## Astrocytic regulatory field = slow field dynamics modulating precision / gain

**Original REE component: Precision Control**

REE uses depth-indexed precision gains \(\alpha_k\) to control how strongly errors at different depths shape belief and action.

From `architecture/precision_control.md`:

> For each depth \(k\): `alpha_k` multiplies the prediction error term in training / inference.

**Astrocyte-aware reinterpretation:**

\(\alpha_k(x,t)\) is **not a direct parameter**. It is the **output** of the regulatory field:

\[
\alpha_k(x,t) = \alpha_{k,0} \cdot h_\alpha(R(x,t), k)
\]

Where:

- \(\alpha_{k,0}\): baseline precision (architectural default).
- \(h_\alpha(R, k)\): regulatory modulation function (depth-dependent sensitivity to regulatory state).

**Functional roles (updated):**

The original doc lists:

> - Dopamine-like: increases commitment (reduced action entropy) and stabilizes selected outputs.
> - Noradrenaline-like: global reset signal when unexpected uncertainty spikes.
> - Acetylcholine-like: increases sensory gain (boost \(\alpha_\gamma\)).
> - Serotonin-like: holds options open; slows premature collapse (limits over-commitment).

**Astrocyte-aware version:**

These are **requests to the regulatory field**, not direct effects:

- **Dopamine-like signal:** shifts \(R(x,t)\) toward a state that increases \(\alpha_k\) for action/control depths (\(k=\beta\)).
- **Serotonin-like signal:** shifts \(R(x,t)\) toward a state that decreases \(\alpha_k\) globally (exploratory mode).
- **Noradrenaline-like signal:** rapid pulse that **requests** a field reset, but the actual reset unfolds over \(\tau_R\) (seconds).
- **Acetylcholine-like signal:** shifts \(R(x,t)\) toward a state that boosts \(\alpha_\gamma\) (sensory depth).

**Key difference:**

- **Old model:** monoamine levels directly set \(\alpha_k\).
- **New model:** monoamines bias \(R(x,t)\); \(R(x,t)\) then sets \(\alpha_k(x,t)\) with spatial/temporal lags.

## Implications for "care budget" and inertia

REE includes the concept of a **care budget** (limited capacity to engage with ethical cost) and **inertia** (resistance to rapid reprioritization). These have been somewhat abstract. The astrocytic regulatory field provides a mechanistic substrate.

### Care budget

**Hypothesis:**

> The "care budget" reflects the **metabolic and regulatory capacity** available for high-precision processing and plasticity.

- High \(\alpha_k\) and high learning rates \(\eta\) are metabolically expensive.
- The regulatory field \(R(x,t)\) mediates the trade-off between computational ambition and energetic reality.
- When metabolic resources are low, \(R(x,t)\) suppresses precision and plasticity, reducing the agent's ability to engage deeply with complex ethical trade-offs.

**Implication:**

> Care budget should not be a fixed parameter. It should emerge from the regulatory field dynamics, which integrate metabolic sensing with computational demand.

### Inertia

**Hypothesis:**

> The "resistance to rapid reprioritization" reflects the **slow timescale of regulatory field updates** (\(\tau_R\)).

- Even if a new monoaminergic signal requests a shift (e.g., dopamine spike to commit to a new goal), the actual change in synaptic parameters \(\alpha_k(x,t)\) unfolds over seconds to minutes.
- This creates a **momentum effect**: the system cannot instantly switch between high-commitment (low-entropy) and exploratory (high-entropy) modes.

**Implication:**

> Inertia is not a design choice; it is a consequence of the layered regulatory architecture. Models that ignore the astrocytic field will underestimate the time required for the agent to adapt to new priorities.

## What REE must not assume anymore

### 1. Regulation is instantaneous

**Old assumption (implicit):**

> If monoaminergic tone changes, precision \(\alpha_k\) changes immediately.

**New constraint:**

> Regulatory changes unfold over \(\tau_R\) (seconds to minutes). There is a **lag** between monoaminergic shift and realized parameter change.

### 2. Regulation is spatially uniform

**Old assumption (implicit):**

> \(\alpha_k(t)\) is a global parameter (same everywhere in L-space at depth \(k\)).

**New constraint:**

> \(\alpha_k(x,t)\) varies across spatial positions \(x\) in L-space due to heterogeneous regulatory state \(R(x,t)\).

**Example:**

- Regions with high recent activity may be in a permissive regulatory state (high \(\alpha_k\)).
- Regions with low recent activity or low metabolic resources may be suppressed (low \(\alpha_k\)).

### 3. Regulation is memoryless (Markovian at short timescales)

**Old assumption (implicit):**

> \(\alpha_k(t)\) depends only on current monoaminergic tone \(M(t)\).

**New constraint:**

> \(R(x,t)\) has **memory**: it integrates over past activity, past monoaminergic signals, and past metabolic states. Current regulatory state depends on history.

## Sleep and offline integration

From `sleep/precision_recalibration.md`:

> During online action, precision gains (alpha_k) may become miscalibrated. Sleep enables:
> - Restoration of entropy where collapse occurred too early
> - Reduction of excessive rigidity
> - Rebalancing of commitment vs exploration

**Astrocyte-aware extension:**

Sleep should recalibrate **both**:

1. Synaptic weights (as originally specified).
2. The regulatory field \(R(x,t)\).

**Hypothesized sleep dynamics for \(R(x,t)\):**

- **Annealing:** smooth out spatial heterogeneities (diffusion-dominated regime with reduced activity-driven terms).
- **Reset to baseline:** gradually restore \(R(x,t)\) toward a default exploratory state.
- **Metabolic restoration:** allow astrocytes to restore glycogen stores and reset metabolic constraints.

**Implication:**

> Sleep is not just synaptic homeostasis. It is also regulatory field homeostasis.

## Trajectory selection (E3)

E3 selects trajectories \(\zeta\) by minimizing:

\[
J(\zeta) = \mathcal{F}(\zeta) + \lambda M(\zeta) + \rho \Phi_R(\zeta)
\]

**Astrocyte-aware extension:**

When evaluating \(\zeta\), E3 must account for:

- **Precision-dependent prediction quality:** trajectories that require high \(\alpha_k\) are only viable if \(R(x,t)\) currently supports high precision.
- **Regulatory feasibility:** trajectories that demand rapid regulatory shifts (e.g., fast switch from exploration to commitment) are penalized if \(\tau_R\) is slow.
- **Metabolic cost of regulation:** maintaining high \(\alpha_k\) is energetically expensive; this should be reflected in \(\mathcal{F}(\zeta)\).

**Possible extension to \(J(\zeta)\):**

\[
J(\zeta) = \mathcal{F}(\zeta) + \lambda M(\zeta) + \rho \Phi_R(\zeta) + \gamma \int_t \|R_{\text{required}}(x,t) - R_{\text{current}}(x,t)\|^2 \, dt
\]

Where \(\gamma\) penalizes trajectories that require regulatory states far from the current state (acknowledging the inertia).

## Summary table: Concept mapping

| **REE Concept**              | **Original Interpretation**                  | **Astrocyte-aware Interpretation**                                      |
|------------------------------|----------------------------------------------|-------------------------------------------------------------------------|
| L-space                      | Neuronal latent state \(z_k(t)\)             | Neuro-glial state \((z_k(t), R(x,t))\)                                  |
| Precision \(\alpha_k\)       | Direct parameter (or direct monoamine map)   | Output of regulatory field: \(\alpha_k(x,t) = f(R(x,t))\)               |
| Monoamines                   | Direct control knobs                         | Broadcast meta-regulatory signals that bias \(R(x,t)\)                  |
| Care budget                  | Abstract limited capacity                    | Emergent from metabolic-regulatory capacity                             |
| Inertia                      | Abstract resistance to reprioritization      | Slow timescale \(\tau_R\) of regulatory field updates                   |
| Sleep (precision recalib.)   | Restore synaptic entropy                     | Restore synaptic entropy **and** regulatory field \(R(x,t)\)            |
| Trajectory selection (E3)    | Evaluate \(\zeta\) under current \(\alpha_k\)| Evaluate \(\zeta\) under current \(R(x,t)\) and regulatory feasibility  |

## What this enables

- **More realistic timescales:** slow adaptation to changing monoaminergic tone.
- **Spatial heterogeneity:** different regions of the latent space can have different regulatory states.
- **Metabolic constraints:** precision and plasticity are limited by energetic availability, mediated by astrocytes.
- **Deeper understanding of "inertia" and "care budget":** these are not ad hoc design choices but emergent properties of the regulatory architecture.

## What this does not change

- The core E1/E2/E3 architecture remains intact.
- Fast neuronal prediction dynamics (millisecond timescale) are unaffected.
- The ethical cost function \(M(\zeta)\) and residue field \(\Phi_R(\zeta)\) are orthogonal to regulatory dynamics.

The astrocytic regulatory field is a **modulatory substrate**, not a replacement for existing REE components.
