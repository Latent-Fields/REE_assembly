# Residue Geometry

**Claim Type:** architectural_commitment  
**Scope:** Persistent moral curvature over latent space; path-dependent ethical cost  
**Depends On:** INV-006 (residue cannot be erased), INV-004 (ethical cost is persistent), [L-space](l_space.md)  
**Status:** stable  
**Claim ID:** ARC-013
<a id="arc-013"></a>

---

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

Taken together, \(\phi(z)\) is the terrain and the hippocampal braid records the actual path.
Residue is therefore both a geometric map and a record of traversal, which lets "map of thoughts"
mean the lived sequence of latent-space moves, not just a static field.

These stored paths provide:
- Episodic memory as *experienced traversal* rather than state snapshots
- A record of how the agent moved through its own ethical geometry
- A substrate for offline replay and counterfactual exploration without erasing residue

Replay samples alternative traversals over a fixed residue field, supporting reflection,
regret, and character formation while preserving the path‑dependence of ethical cost.

---

## Open Questions

None noted in preserved sources.

## Related Claims (IDs)

- ARC-013
- ARC-007
- ARC-004
- INV-006
- INV-004

## References / Source Fragments

- `docs/processed/legacy_tree/docs/architecture/residue_geometry.md`
- `docs/processed/legacy_tree/architecture/residue_geometry.md`
