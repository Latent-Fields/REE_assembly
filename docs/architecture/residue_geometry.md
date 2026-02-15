# Residue Geometry

**Claim Type:** architectural_commitment  
**Scope:** Persistent moral curvature over latent space; path-dependent ethical cost  
**Depends On:** INV-006 (post-commit consequence traces cannot be erased), INV-004 (post-commit consequence traces are persistent), [L-space](l_space.md)  
**Status:** stable  
**Claim ID:** ARC-013
<a id="arc-013"></a>

---

Residue is stored as persistent curvature over latent space.

Clarification: residue is **not** generic reward learning. It is the durable imprint of post‑commitment consequences
(harm, benefit, viability, coherence) that bends future trajectory selection without collapsing into a scalar objective.
Viability mapping tracks which paths are stable or fragile; residue encodes what those paths *mean* ethically.

**Subsystem abstract (core claims):** ARC‑013 defines residue as persistent ethical curvature, while MECH‑034 distinguishes
curvature updates from viability mapping. Supporting context includes ARC‑018 (viability mapping), ARC‑007 (path memory),
ARC‑004 (L‑space), and INV‑004/INV‑006 (residue persistence constraints).

### Residue integration (neuro‑anchored functional analog)

Evidence anchors: P1, P16, P37–P39.

Residue integration can be treated as a **two‑rate consolidation pipeline**:

1. **Online (awake) imprinting**  
   - After commitment, consequences update local curvature \(\phi(z)\) cautiously.  
   - E2 affordances and E1 priors receive small, precision‑weighted shifts.  
   - Hippocampus logs the path and viability signals.

2. **Offline (sleep) consolidation**  
   - Hippocampal replay selects and re‑encodes trajectories.  
   - Slow cortical consolidation reshapes longer‑horizon priors.  
   - Affective weighting biases which traces consolidate without turning residue into reward.  

This keeps residue **structural** and path‑dependent while allowing slow, system‑level learning that does not override
sensory corrigibility. These anchors are functional, not anatomical, and are meant to guide implementation choices
about scheduling, replay bias, and consolidation depth (see `docs/notes/evidence_map.md`).

### Implementation hints (non‑binding)

- Maintain a **replay scheduler** that can bias which trajectories are re‑encoded (e.g., high residue curvature, high
  uncertainty, or recent commitment).  
- Maintain a **consolidation queue** with two phases: fast local updates (awake) and slow structural updates (sleep).  
- Keep **residue updates separate from reward**: store curvature deltas and apply them to selection bias, not as a scalar
  objective.  
- Allow **affective weighting** to influence replay priority, not to overwrite curvature directly.

## Minimal representation

- Maintain a function \(\phi(z)\) over latent space (implemented as a small neural network, radial basis functions, or a k-nearest neighbors map).
- Update \(\phi\) after executing a trajectory to increase the cost around visited latent states proportional to ethical cost.

<a id="mech-034"></a>
## Residue vs Viability Map Updates (MECH-034)

**Claim Type:** mechanism_hypothesis  
**Scope:** Distinguish ethical curvature updates from navigability updates  
**Depends On:** ARC-013, ARC-018  
**Status:** provisional  
**Claim ID:** MECH-034

Post-commitment viability mapping updates a navigability surface using predicted–observed self-sensory mismatch and
resulting WORLD/HOMEOSTASIS/HARM shifts, marking paths as stable, fragile, or path-closing. Residue updates, by
contrast, adjust ethical curvature \(\phi(z)\) based on harm or violation outcomes. Both are post-action signals,
but they encode different information: path stability vs ethical cost.

Residue also drives **longer‑horizon training pressure** in E1/E2: slow shifts in priors and fast affordance pruning
should reflect accumulated ethical curvature, while hippocampal viability mapping remains a feasibility filter rather
than a value signal. Online updates can be conservative; deeper integration occurs during offline/sleep consolidation.

<a id="mech-056"></a>
## Trajectory-First Residue Placement (MECH-056)

**Claim Type:** mechanism_hypothesis
**Scope:** Prefer trajectory-space gating before representational distortion
**Depends On:** ARC-013, ARC-018, ARC-003, ARC-004, MECH-034
**Status:** candidate
**Claim ID:** MECH-056

REE should preferentially place residue pressure in **trajectory feasibility and commitment gating** (hippocampal
rollout costs, E3 thresholds, and control-plane vetoes) rather than distorting core E1/E2 representational geometry.

Design preference:
- Preserve detailed world modelling in E1/E2.
- Suppress harmful enactment by increasing trajectory cost and commitment resistance.
- Allow only bounded, slow representational bias when trajectory-level constraints are insufficient.

This keeps epistemic richness and corrigibility while still enforcing behavioral constraints:
**know broadly, enact selectively**.

Operational implication:
- Apply residue first to rollout sampling weights and E3 gating.
- Treat latent distortion as a secondary, capped channel with explicit safeguards against blind spots.

### Loop-specific trajectory-first policy

Trajectory-first placement is not uniform across all gate families. The same ordering rule must be parameterized by
gate manifold:

- `gate_motor`: strict trajectory-first gating before action release; representational distortion stays a last-resort lane.
- `gate_cognitive_set`: trajectory-first preferred, but allows broader rehearsal depth and delayed commitment under low
  urgency.
- `gate_motivational`: salience/value gating may prune candidate sets before full trajectory expansion; trajectory-first
  applies inside the selected motivational band.

This keeps "trajectory-first" from becoming an over-broad global rule while preserving the core commitment that residue
pressure should mainly constrain enactment, not perception.

Cross-claim alignment:

- MECH-062 defines tri-loop gate separation and arbitration.
- MECH-060/061 define where updates are legal across the commit boundary.

### DMN-like rehearsal lane (implementation contract)

Uncommitted trajectory generation should be treated as a default-mode-network-like rehearsal/search lane:
generate, compare, and prune candidate trajectories before commitment.

Hard invariants:
- Rehearsal traces are pre-commit only and must not write policy/ledger state.
- Rehearsal may update temporary search statistics, but durable residue updates require commit.
- Commitment gating, not rehearsal score alone, decides action eligibility.

Required routing:
- Inputs: current latent state, goals/constraints, control-plane state, replay seeds.
- Outputs (pre-commit): trajectory risk, feasibility, and veto hints to E3 gate family.
- Outputs (post-commit only): attributable consequence traces routed to residue/viability updates.

Validation hooks for MECH-056:
- Keep `ledger_edit_detected_count == 0` in rehearsal-only windows.
- Keep `explanation_policy_divergence_rate <= 0.05` across seed sweeps.
- Keep `domination_lock_in_events == 0` under rehearsal-heavy regimes.
- Track `commitment_reversal_rate` to ensure rehearsal does not leak into unstable enactment.

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

Residue integration is therefore a two‑rate process:
- **Awake/online:** local, cautious adjustments tied to committed outcomes.
- **Offline/sleep:** deeper consolidation that reshapes long‑horizon priors without sensory override.

This preserves immediate corrigibility while letting ethical curvature accumulate structurally.

---

## Open Questions

None noted in preserved sources.

## Related Claims (IDs)

- ARC-013
- ARC-007
- ARC-004
- INV-006
- INV-004
- MECH-034
- MECH-056

## References / Source Fragments

- `docs/processed/legacy_tree/docs/architecture/residue_geometry.md`
- `docs/processed/legacy_tree/architecture/residue_geometry.md`
- `docs/thoughts/2026-02-09_viability_mapping_vs_residue.md`
- `docs/thoughts/2026-02-12_TRAJECTORY-RESIDUE-VS-REPRESENTATIONAL-DISTORTION.md`
