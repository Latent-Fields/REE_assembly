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
- harm-to-other contributes to ethical consequence and residue (legacy \(M(\zeta)\) proxy)
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
- Modulates ethical consequence and residue (legacy \(M\) proxy)
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

<a id="mech-031"></a>
## Derived Social Tags and Empathy Coupling (MECH-031)

**Claim Type:** mechanism_hypothesis  
**Scope:** Derived social tags and control-plane coupling for fast empathy  
**Depends On:** ARC-010, ARC-005, ARC-017, ARC-015, ARC-006, INV-005  
**Status:** candidate  
**Claim ID:** MECH-031

---

## Agency and Other-Selflike Detection (Derived Streams)

REE can extend social cognition without a new subsystem by adding **derived** tags over WORLD:

- `AGENCY`: detects interveners vs passive dynamics (goal-directed intervention, error-correction, boundary maintenance).
- `OTHER_SELFLIKE`: probability that an agent runs a self/world separation and self-impact loop.

These are inference tags, not perceptual primitives. They reuse the same self/world/impact machinery, rather than
introducing a separate social-cognition module.

Calibration note: `OTHER_SELFLIKE` should be biased toward **high recall** (tolerating false positives) rather than
high precision. Early false positives are historically normal and less harmful than false negatives, which block
empathy coupling and ethical generalisation. Calibration can tighten over development.

<a id="mech-032"></a>
## OTHER_SELFLIKE High-Recall Bias (MECH-032)

**Claim Type:** mechanism_hypothesis  
**Scope:** Bias `OTHER_SELFLIKE` toward recall to avoid empathy false negatives  
**Depends On:** MECH-031, ARC-010  
**Status:** candidate  
**Claim ID:** MECH-032

<a id="mech-036"></a>
## Other-Harm Veto Threshold (MECH-036)

**Claim Type:** mechanism_hypothesis  
**Scope:** When inferred other-harm should veto vs influence ranking  
**Depends On:** MECH-031, ARC-005, INV-005  
**Status:** candidate  
**Claim ID:** MECH-036

Other-harm should trigger a hard veto only under high-certainty, catastrophic, or irreversible outcomes. In most
ambiguous or tradeoff-heavy contexts, other-harm should influence ranking rather than veto selection. Control-plane
coupling parameters (`lambda_empathy`, `v_other_veto`) set and adapt this threshold.

---

## Fast Empathy via Shadow Bundles

When `OTHER_SELFLIKE` is high, REE can instantiate a shadow bundle of inferred streams for an agent `j`:

- `HOMEOSTASIS_j`, `HARM_j`, `SELF_IMPACT_j`, optionally `TEMPORAL_COHERENCE_j`.

These are estimated viability variables, not direct interoception. The control plane can couple them into pruning and
ranking via a small set of knobs:

- `lambda_empathy`: other-to-self coupling strength.
- `g_social`: social attention gain for `OTHER_SELFLIKE` agents.
- `alpha_other`: precision assigned to inferred other-states.
- `v_other_veto`: whether other-harm can trigger veto/interrupt vs only affect ranking.
- Optional `AFFILIATION`: stabilises coupling based on history/kinship.

This yields fast empathy as **routing + weighting**, not a new moral module.

---

## Open Questions

None noted in preserved sources.

## Related Claims (IDs)

- ARC-010
- ARC-009
- ARC-006
- ARC-004
- INV-005
- MECH-031
- MECH-032
- MECH-036

## References / Source Fragments

- `docs/processed/legacy_tree/architecture/social/README.md`
- `docs/processed/legacy_tree/architecture/social/mirror_modelling.md`
- `docs/processed/legacy_tree/architecture/social/social_coupling.md`
- `docs/processed/legacy_tree/architecture/social/otherness_inference.md`
- `docs/thoughts/2026-02-09_empathy.md`
- `docs/thoughts/2026-02-09_other_harm_gating.md`
