---
nav_exclude: true
---

# Compact Consolidation Principle

**Claim Type:** mechanism_hypothesis
**Scope:** Shared representational basis + consolidation operator as the source of behavioural selectivity
**Depends On:** ARC-001, ARC-003, ARC-005, INV-014
**Status:** candidate
**Claim ID:** MECH-068
<a id="mech-068"></a>

---

## Summary

Behavioural selectivity in a predictive cognitive system emerges at the **consolidation/gating layer**,
not at the shared representational basis. The feature basis (E1) is canonical and largely shared;
the consolidation operator (E3 + control plane gating) determines which trajectories, values, and
behaviours are selected.

This principle is grounded in empirical evidence from compact modelling of macaque V4 (Cowley et al.
2023), and is structurally coherent with REE's existing E1/E3 separation.

---

## Formal statement

Let:

- **F** = shared representational basis (E1 latent stack)
- **G_i** = consolidation operator for unit or mode *i* (E3 gating + control plane)
- **x** = sensory/world input

Then:

```
Behaviour_i(x) = G_i( F(x) )
```

Diversity in behaviour arises from **G_i**, not from **F**.

---

## Three sub-claims

### CSH-1: Selectivity at consolidation, not at basis

Representational diversity — including trajectory preference, ethical weighting, and value
selectivity — emerges at the consolidation/gating operator (E3, MECH-062 tri-loop gates), not
at the E1 feature basis.

**Implication:** E1 ablations should leave selectivity patterns relatively intact; E3/gate
ablations should change trajectory preference directly, without disrupting E1 latent structure.

**Discriminating test:** Vary E3 consolidation weights (λ, ρ in J(ζ)) while freezing E1.
Observe: trajectory preference changes; E1 latent representations do not drift.
See `ree-v1-minimal/experiments/consolidation_ablation.py`.

### CSH-2: Compressibility as a viability constraint

A viable cognitive architecture must admit large compression without functional collapse.

Cowley et al. (2023) demonstrate ~5000× compression in V4 models with no accuracy loss.
The implication: high-dimensional representations are heavily redundant, and the operational
core is compact. Architectures that cannot be compressed without collapse likely encode
behavioural function in the wrong place (e.g., in distributed weight patterns with no
structural basis for selective gating).

**REE implication:** The L-space latent stack should have a compact core. REE subsystems
should be designed to support compression/pruning analysis as a diagnostic tool.

### CSH-3: Canonical operations are sufficient primitives

The canonical cortical computational motifs — **surround suppression**, **divisive
normalisation**, and **winner-take-all competition** — are empirically sufficient to account
for a wide range of selective responses when applied over a shared basis.

**REE implication:** The control plane does not require exotic or novel operations.
The existing MECH-040, MECH-054, MECH-062, MECH-063 mechanisms are grounded in these
canonical primitives. See control_plane.md.

---

## REE architectural mapping

| Paper concept | REE component |
|---|---|
| Shared early filter bank | E1 latent stack (shared canonical basis) |
| Consolidation step | E3 tri-loop commit gating (MECH-062) |
| Selective pooling | Precision-weighted trajectory scoring in E3 |
| Divisive normalisation | Gain control plane (ARC-005, MECH-063) |
| Winner-take-all competition | Commit threshold + disinhibitory sweep (MECH-062) |
| Surround suppression | Precision modulation (MECH-040, MECH-054) |
| Feature basis (encoder) | E1 → F(x) |
| Neuron-specific readout | E3 → G_i(F(x)) |
| Compression viability | L-space compactness invariant (CSH-2) |

---

## JEPA scope clarification

JEPA (I-JEPA, V-JEPA) covers **stage 1** of this framework: the shared feature basis / early
filter bank. Stage 2 — the consolidation step that determines behavioural selectivity — is
not in JEPA's architecture.

JEPA should therefore be treated as a **reference architecture for E1 representation only**,
not as a complete REE substrate. E3 trajectory gating and the control plane are not
JEPA-scoped. This is not a limitation of JEPA; it is simply outside its design intent.

See `docs/glossary.md#impl-020` for the canonical JEPA–REE alignment table.

---

## Empirical anchor

**Primary source:** Cowley BR, Stan PL, Pillow JW, Smith MA (2023).
"Compact deep neural network models of visual cortex."
bioRxiv. DOI: 10.1101/2023.11.22.568315

Key findings:
- V4 neurons share an early filter bank; stimulus preference is determined by a
  neuron-specific consolidation step.
- Accurate models compress ~5000× without accuracy loss.
- Canonical operations identified: edge/curve detectors, surround suppression,
  winner-take-all, divisive normalisation.
- Preferred stimuli predictions validated causally via adversarial image synthesis.

Full literature entry: `evidence/literature/visual_cortex_compact_models/entries/2026-02-26_cowley_2023_compact_v4/`

**Transfer caveat:** The paper studies macaque V4 (mid-level visual cortex). Extension to
full cognitive architecture, trajectory selection, and ethical weighting is inferential.
Canonical operation sub-claims (CSH-3) carry lower transfer risk than CSH-1 applied to
high-level cognition.

---

## Open questions

- **Q (CSH-1 test):** Does freezing E1 and varying E3 λ/ρ weights in ree-v1-minimal
  GridWorld produce predictably different trajectory preference without E1 latent drift?
  (This is the primary discriminating experiment for CSH-1.)

- **Q (CSH-2 target):** What is a meaningful compression ratio target for the REE L-space
  core? 5000× is a V4-specific result; the cognitive architecture target is unknown.

- **Q (E3 identity):** Is E3's tri-loop structure (MECH-062) the correct REE analogue for
  the consolidation step, or does the consolidation step sit between E1 and E3?

---

## Related Claims

- ARC-001 (E1 Persistent Substrate)
- ARC-003 (E3 Trajectory Selection)
- ARC-005 (Control Plane)
- INV-014 (Separation of representation and regulation)
- MECH-062 (Tri-Loop Commitment Gating)
- MECH-063 (Orthogonal Control-Plane Axes)
- MECH-040 (Safety Baseline vs Volatility)
- MECH-054 (Signed Harm/Benefit PE Precision)

## References

- Cowley et al. 2023 (primary): `evidence/literature/visual_cortex_compact_models/`
- Carandini & Heeger 2012: Divisive normalization as a canonical neural computation
  (cited in Cowley et al.; supports CSH-3)
