# Residue geometry

Residue is stored as persistent curvature over latent space.

## Minimal representation

- Maintain a function \(\phi(z)\) over latent space (implemented as a small neural network, radial basis functions, or a k-nearest neighbors map).
- Update \(\phi\) after executing a trajectory to increase the cost around visited latent states proportional to ethical cost.

## Why geometry

If residue were a scalar penalty, it would be easily traded off against reward and optimized away.

A spatial field \(\phi(z)\) makes residue *path dependent* and supports moral continuity.

## Path memory (hippocampal braid)

Residue geometry \(\phi(z)\) defines a *field* over latent space, but ethical identity and continuity
arise from the **paths taken through that field**.

Let a lived trajectory be represented as a time‑ordered path:
\[
\gamma(t) = z(t), \quad t \in [t_0, t_1]
\]
where movement through latent space is shaped by the local curvature induced by \(\phi(z)\).

The hippocampal analogue in REE does not compute value, select actions, or overwrite perception.
Its role is to **index, store, and replay trajectories** \(\gamma(t)\) through latent space,
together with contextual and salience annotations.

These stored paths provide:
- Episodic memory as *experienced traversal* rather than state snapshots
- A record of how the agent moved through its own ethical geometry
- A substrate for offline replay and counterfactual exploration without erasing residue

Replay samples alternative traversals over a fixed residue field, supporting reflection,
regret, and character formation while preserving the path‑dependence of ethical cost.
