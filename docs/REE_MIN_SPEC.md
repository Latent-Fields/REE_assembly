# REE minimum instantiation specification (REE‑v0)

**Claim Type:** implementation_note  
**Scope:** Minimum implementation commitments for an REE prototype  
**Depends On:** ARC-001, ARC-002, ARC-003, ARC-004, ARC-005, ARC-013, ARC-011  
**Status:** stable  
**Claim ID:** IMPL-003
<a id="impl-003"></a>

This document lists the minimal commitments needed to implement a runnable REE prototype.

## 1. World interface

Define the environment as a partially observable process with:

- Observations \(o_t\) composed of:
  - **Exteroception** (at least two modalities).
  - **Interoception** (internal body/state variables).
  - **Damage / harm sensors** (integrity degradation signals).
  - **Homeostatic sensors** (viability-relevant signals, e.g., energy, temperature, resource levels, error load).
- Actions \(a_t\): discrete or continuous control signals.
- A time step \(\Delta t\) that is consistent across hippocampal rollouts.

## 2. Latent stack (L-space)

Represent state using a multi-timescale latent stack:

- \(z_\gamma(t)\): fast sensory binding (short horizon)
- \(z_\beta(t)\): action-set / control state (short horizon)
- \(z_\theta(t)\): contextual sequence state (medium horizon)
- \(z_\delta(t)\): regime / motivational state (long horizon)

Each level must support:

- Temporal prediction: \(z_k(t)\to z_k(t+1)\)
- Top-down prediction: \(z_{k+1}(t)\to z_k(t)\)

E2 primarily refreshes \(z_\gamma,z_\beta\); E1 primarily stabilizes \(z_\theta,z_\delta\).

## 3. Trajectory type

Define a candidate trajectory as:

\[
\zeta = (z_{t:t+H}, a_{t:t+H})
\]

Where \(H\) is a planning horizon.

## 4. Reality constraint \(\mathcal{F}(\zeta)\)

Implement a computable proxy for Variational Free Energy (VFE) using:

\[
\mathcal{F}(\zeta) \approx
\underbrace{\mathbb{E}[\|o_{t+1}-\hat{o}_{t+1}\|]}_{\text{exteroceptive prediction error}}
+
\underbrace{\mathbb{E}[\|h_{t+1}-\hat{h}_{t+1}\|]}_{\text{interoceptive/homeostatic prediction error}}
+
\underbrace{\mathrm{KL}(q(z)\|p(z))}_{\text{complexity / prior cost (Kullback–Leibler divergence, KL)}}
\]

Where \(h\) denotes homeostatic variables.

## 5. Legacy ethical cost \(M(\zeta)\)

Current canonical framing: E3 does not require an explicit ethical cost term. Ethical consequence is encoded via residue, mirror modelling, control-plane gating, hippocampal systems, and commitment-gated learning (see `docs/architecture/e3.md`). The legacy formulation below is preserved for traceability and evaluation only.

Legacy ethical cost is environment-specific but must be computable from hippocampal rollout predictions.

Minimal requirement:

- Define **degradation** as predicted loss of viability-relevant variables (self) and predicted degradation of homologous variables in other models.

Example form:

\[
M(\zeta) = \mathbb{E}[\mathrm{degrade}_{self}(\zeta)] + \kappa\,\mathbb{E}[\mathrm{degrade}_{other}(\zeta)]
\]

Where \(\kappa\) is a coupling factor representing “otherness” precision.

## 6. Residue object \(R\) and residue field \(\Phi_R\)

Moral continuity requires persistent residue.

- Store residue as:
  1) a **latent-space dent field** \(\phi(z)\) over visited latent regions, and
  2) optional **context-keyed** residue \(R(z_\theta)\) or \(R(z_\delta)\) for narrative/regime dependence.

Define residue contribution to a hippocampal rollout as:

\[
\Phi_R(\zeta) = \sum_{t'=t}^{t+H} \phi(z(t'))
\]

Update rule (minimal):

- After executing \(\zeta^*\), increase \(\phi\) along the realized latent path in proportion to realized/estimated ethical degradation proxy (legacy \(M\)).

## 7. Precision routing \(\alpha_k\)

Maintain depth-indexed precision gains \(\alpha_\gamma,\alpha_\beta,\alpha_\theta,\alpha_\delta\).

Minimal commitment:

- \(\alpha_k\) must modulate either:
  - weighting of prediction errors at depth \(k\), and/or
  - sampling temperature / entropy at depth \(k\).

Interpretation:

- Higher \(\alpha_\gamma\): more sensory-driven.
- Higher \(\alpha_\delta\): regime becomes stickier (harder to exit).
- Dopamine-like commitment corresponds to temporarily raising precision for the selected trajectory’s action predictions.

## 8. Selection rule

Current canonical framing: E3 selection does not require an explicit ethical cost term. The legacy objective below is preserved for traceability.

E3 selects \(\zeta\) by minimizing:

\[
J(\zeta)=\mathcal{F}(\zeta)+\lambda\,M(\zeta)+\rho\,\Phi_R(\zeta)
\]

with \(\lambda,\rho\ge 0\).

## Wiring
- Offline integration (“sleep”) contract and components: see `sleep/` (required for long-term stability).
- Self/other, mirror modelling, and coupling: see `social/` (used by residue and legacy ethical cost proxies).
- Language as emergent symbolic mediation (trust-weighted; cannot override harm): see `language/`.

---

## Open Questions

None noted in preserved sources.

## Related Claims (IDs)

- IMPL-003
- ARC-001
- ARC-002
- ARC-003
- ARC-004
- ARC-005
- ARC-011
- ARC-013
- ARC-012

## References / Source Fragments

- `docs/processed/legacy_tree/docs/REE_MIN_SPEC.md`
