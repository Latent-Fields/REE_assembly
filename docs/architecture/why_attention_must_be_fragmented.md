# Why Attention Must Be Fragmented

**Claim Type:** mechanism_hypothesis  
**Scope:** Rationale for fragmented attention control axes  
**Depends On:** INV-009, ARC-005  
**Status:** provisional  
**Claim ID:** MECH-007
<a id="mech-007"></a>

---

Source: `docs/processed/legacy_tree/architecture/why_attention_must_be_fragmented.md`


Part 3

Why Attention Must Be Fragmented

⸻

Status

Normative architectural rationale

This document explains why REE treats “attention” not as a single mechanism, but as a fragmented control surface distributed across multiple orthogonal dimensions. This fragmentation is not an implementation detail; it is a safety and coherence requirement.

⸻

1. The Problem with Unitary Attention

Modern AI architectures often treat attention as:
	•	a single scalar or vector field
	•	applied uniformly across representations
	•	responsible for relevance, learning, and action selection

This leads to an implicit assumption:

If the system attends strongly to something, it should both learn from it and act on it.

Biological cognition violates this assumption everywhere.

REE must violate it too.

⸻

2. Attention Is Not One Thing

In REE, “attention” decomposes into three independent questions:
	1.	How much should this signal influence local updating?
	2.	How urgently must the system commit or reorient?
	3.	How exclusive must interpretations be?

A single mechanism cannot answer all three without contradiction.

⸻

3. The Three Control Axes (Canonical)

REE therefore fragments attention into three orthogonal control axes, each implemented as a separate modulation channel:

Axis	Signal	Governs	Core Question
Precision	Dopamine-like	Error influence (πτ)	How much should this matter locally?
Commitment Pressure	Noradrenaline-like	Path authority & interruptibility	Must I act or reorient now?
Exclusivity / Collapse	Serotonin-like	Hypothesis pruning & plasticity	Must I choose one interpretation?

No axis substitutes for another.
No axis writes to the same register.

⸻

4. Fragmentation Preserves Logical Consistency

4.1 Separation of Learning and Acting
	•	Dopamine-like precision updates learning without forcing action
	•	Noradrenaline-like urgency forces action without rewriting belief
	•	Serotonin-like collapse governs belief structure without urgency

This prevents classic failure modes:
	•	surprise → certainty
	•	urgency → belief rigidity
	•	salience → value corruption

⸻

4.2 Separation of Imagination and Commitment
	•	θ-level paths may proliferate freely
	•	serotonin permits coexistence
	•	noradrenaline determines whether choice is forced
	•	E3 commits only after constraints are satisfied

Thus:

The system can imagine without acting, and act without believing prematurely.

⸻

5. Fragmentation Across τ (Temporal Depth)

Attention-like effects are τ-scoped, not global.
	•	γ always updates (sensorium never pauses)
	•	β tracks affordances continuously
	•	θ simulates futures without obligation
	•	δ maintains slow constraints

Fragmented attention ensures:
	•	γ salience does not become δ certainty
	•	θ imagination does not become β compulsion
	•	δ identity does not micromanage γ perception

⸻

6. Fragmentation Across ρ (Representational Depth)

Similarly, attention must not collapse abstraction levels.
	•	serotonin regulates ρ-level exclusivity
	•	dopamine regulates ρ-local learning
	•	noradrenaline regulates ρ-crossing urgency

This allows:
	•	multiple perceptual narratives
	•	plural futures
	•	revisable identities

without loss of coherence.

⸻

7. Why “Attention Is All You Need” Is Incomplete

The phrase is directionally right but structurally wrong.

What is actually needed is:

Fragmented attention with typed authority.

A single attention mechanism cannot safely decide:
	•	what to learn,
	•	what to do,
	•	what to believe,
	•	and what to discard.

REE enforces this separation architecturally, not heuristically.

⸻

8. Alignment Implications (Non-Optional)

If attention is not fragmented:
	•	reward spikes rewrite values
	•	rare events dominate policy
	•	internal simulations compel action
	•	identity collapses under noise

Fragmentation ensures:
	•	learning is conservative
	•	commitment is contextual
	•	belief revision is protected
	•	imagination remains safe

This is alignment by structure, not by objective tuning.

⸻

9. Axiomatic Summary (Safe to Quote)

You can safely include the following as a design axiom:

Attention is not a unitary resource.
Any system that learns, imagines, and acts under uncertainty must fragment attention into orthogonal control axes governing precision, urgency, and representational collapse.

⸻

10. Relationship to the Rest of REE

This document underwrites:
	•	precision_scoping.md
	•	path_authority_and_interrupts.md
	•	serotonin.md
	•	the τ × ρ × φ coordinate system
	•	the non-compilability of ethics

Without fragmented attention, REE degenerates into an optimiser.
With it, REE remains a viable cognitive architecture.

⸻

11. Summary
	•	Attention is control, not content
	•	Control has multiple irreducible dimensions
	•	Fragmentation prevents pathological collapse
	•	REE encodes this explicitly and normatively
---

## Open Questions

None noted in preserved sources.

## Related Claims (IDs)

- MECH-007

## References / Source Fragments

- `docs/processed/legacy_tree/architecture/why_attention_must_be_fragmented.md`
