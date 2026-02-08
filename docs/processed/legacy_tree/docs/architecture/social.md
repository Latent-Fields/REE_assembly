# Social Cognition (Self/Other)

**Claim Type:** architectural_commitment  
**Scope:** Social cognition via mirror modelling, coupling, and otherness inference  
**Depends On:** INV-005 (harm via mirror modelling), ARC-004 (L-space), ARC-006 (entities and binding)  
**Status:** stable  
**Claim ID:** ARC-010
<a id="arc-010"></a>

---

> **Elaborates Section 5 (Social Extension: Self/Other) of `REE_CORE.md`.**

## Social Cognition (REE)

This folder specifies **social cognition mechanisms** in the Reflective-Ethical Engine (REE).

Social cognition in REE is grounded in:
- reuse of the self generative model,
- precision-weighted coupling to others,
- and persistence of harm via moral residue.

It precedes language and enables empathy, coordination,
and ethical generalisation without symbolic rules.

Source: `docs/processed/legacy_tree/architecture/social/README.md`

---

## Mirror Modelling

### Definition
Mirror modelling is the reuse of the **self generative model**
to simulate other agents, with reduced coupling and without interoceptive closure.

It enables:
- prediction of others' behaviour,
- empathy as predicted self-like degradation,
- generalisation of harm without explicit moral rules.

### Mechanism
- Same latent variables as self-model (shared L-space)
- Lower precision gains (alpha_k reduced)
- No direct interoceptive error correction
- Coupling strength modulates empathic resonance

### Harm Equivalence Principle
Predicted degradation in a mirrored other-model
is treated as homologous to degradation of the self,
discounted by coupling strength.

### Role in Ethics
Mirror modelling is the primary pathway by which:
- harm-to-other contributes to ethical cost M(zeta)
- moral residue R forms without direct self-harm

Note: legacy sources use the ethical cost term M. Current canonical framing removes the explicit cost term while retaining residue and mirror modelling (see `docs/architecture/e3.md`).

### Failure Modes
- Low gain: psychopathy / callousness
- Excessive gain: empathic overwhelm / paralysis
- Miscalibrated gain: burnout, moral injury

Source: `docs/processed/legacy_tree/architecture/social/mirror_modelling.md`

---

## Social Coupling

Social coupling determines how strongly mirrored models influence selection.

### Coupling Factors
- Structural similarity
- Temporal synchrony
- History of interaction
- Language-mediated trust signals

### Coupling Effects
- Scales harm equivalence contribution
- Modulates ethical cost M
- Affects residue accumulation

### Dynamics
Coupling is:
- context-dependent,
- history-sensitive,
- recalibrated during offline sleep.

This allows empathy without global collapse.

Source: `docs/processed/legacy_tree/architecture/social/social_coupling.md`

---

## Otherness Inference

REE distinguishes self from other via coupling structure.

### Self
- Tight action–prediction coupling
- Interoceptive and proprioceptive closure
- High precision on internal error signals

### Other
- Structural similarity to self-model
- Loose coupling
- No interoceptive closure

Otherness is inferred when an entity:
- behaves coherently,
- predicts similarly to self,
- but does not respond to self action commands.

This avoids symbolic identity assignment.

Source: `docs/processed/legacy_tree/architecture/social/otherness_inference.md`

---

## Open Questions

None noted in preserved sources.

## Related Claims (IDs)

- ARC-010
- ARC-009
- ARC-006
- ARC-004
- INV-005

## References / Source Fragments

- `docs/processed/legacy_tree/architecture/social/README.md`
- `docs/processed/legacy_tree/architecture/social/mirror_modelling.md`
- `docs/processed/legacy_tree/architecture/social/social_coupling.md`
- `docs/processed/legacy_tree/architecture/social/otherness_inference.md`
