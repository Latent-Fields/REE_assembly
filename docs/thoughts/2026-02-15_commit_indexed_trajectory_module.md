Status: processed

Processed in:
- `docs/architecture/hippocampal_systems.md` (ARC-018, MECH-033, Q-011)

---

Thought: Commit-Indexed Trajectory Module (CITM)

Core claim

Given REE already implements:
- pre-commit reference
- commit (intervention emission)
- post-commit reference
- reafferent comparison

REE has sufficient structural primitives to support a hippocampal-analogue system without adding an explicit map
module. Space, time, and trajectory simulation can emerge from a Commit-Indexed Trajectory Module (CITM) layered on
top of the existing commit loop.

1. Structural premise

At time t:
- S_pre(t) = pre-commit predicted state
- A(t) = commit (action/output)
- S_post(t) = post-commit observed state
- Delta(t) = S_post(t) - S_pre(t)

Each commit generates a transition tuple:

tau(t) = (S_pre(t), A(t), Delta(t))

This tuple is self-indexed by construction and encodes:
- causation (agent-linked change)
- error (prediction divergence)
- directionality

2. CITM definition

CITM is a memory and replay system that:
1. stores transition tuples tau(t)
2. chains compatible tuples into trajectories
3. detects compositional structure in Delta
4. performs replay for compression and counterfactual simulation

It does not store space directly; it stores commit-linked transitions.

3. Emergence of geometry

If transition vectors satisfy:
1. compositionality: Delta(a) + Delta(b) ~= Delta(ab)
2. cycle consistency: closed loops produce near-zero net displacement
3. metric regularity: transition magnitudes exhibit stable scaling

then latent geometry can emerge.

4. Emergence of time

Time arises from:
- directed commit sequence ordering
- non-commutative transition chains
- replay with forward bias

Temporal coding is expected to emerge when relative position in replayed chains is represented and reward/error
propagation shifts activation backward along stored trajectories.

5. Replay operator

Replay over ordered transitions:

R(tau1, tau2, ..., taun)

supports:
- compression
- loop detection
- counterfactual evaluation
- long-horizon simulation

6. Responsibility as structural property

Because transitions are self-indexed, CITM supports:
- attribution of downstream divergence
- counterfactual path comparison
- long-range consequence modeling

Responsibility becomes detection of systematic post-commit divergence along replayed trajectories.

7. Minimal implementation requirements

REE already has:
- E1 stable state embeddings
- E2 fast transition prediction
- commit gate
- reafferent error comparison

CITM adds:
- transition tuple store
- replay mechanism
- compositionality detection
- loop consistency regularization

8. Architectural position

Input: commit loop outputs.
Storage: structured transition memory.
Interaction:
- feeds trajectory simulations to E3
- feeds error statistics to control plane
- supplies counterfactual paths for ethical evaluation

9. Strong-form claim

If REE has:
- pre-commit prediction
- commit emission
- post-commit reafference
- structured error encoding

then a hippocampal-like mapping system is a natural structural extension.

10. Research predictions

If implemented:
1. latent geometry should emerge without explicit spatial supervision
2. replay should enable backward error propagation
3. time-position coding should appear during replay
4. ethical trajectory evaluation should improve with replay depth

11. Open questions

- Does Delta need explicit vector form, or can it remain implicit in embedding difference?
- How deep must replay chains be before geometry stabilizes?
- Is separate metric regularization required?
- Should exogenous transitions be stored differently from endogenous commits?

Summary

CITM formalizes hippocampal-like functionality in REE as self-indexed, replayable transition graphs. Space, time,
trajectory simulation, and responsibility can emerge from this structure without introducing an explicit spatial module.

