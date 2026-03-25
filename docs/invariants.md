# REE Architectural Invariants

**Claim Type:** invariant  
**Scope:** Core architectural commitments that define REE identity  
**Depends On:** None (axiomatic)  
**Status:** stable

---

## Purpose

This document lists the **non-negotiable architectural invariants** of the Reflective-Ethical Engine (REE).

An implementation is **not REE-compliant** if it violates any of these invariants.

These invariants define what REE *is*. Changing one invalidates large parts of the project.

---

## Core Thesis Invariants

<a id="inv-001"></a>
### INV-001: No Explicit Ethics Module

**Subject:** ethics.emergence  
**Polarity:** denies  
**Claim:** REE does **not** add an explicit moral objective, moral reward, or ethical scoring function on top of action selection.

What looks like ethics is a consequence of **base learning dynamics** (avoid harm / seek reward) **plus a representational symmetry**: when other agents are represented *as self-like* in the mechanics of prediction and learning, "care for others" is not an overlay — it emerges as the same machinery applied under a self↔other mapping.

**Source:** [README.md](../README.md) §1, [REE_CORE.md](../REE_CORE.md) §5

**Violation:** Adding an ethics layer changes the thesis.

---

<a id="inv-002"></a>
### INV-002: Coherence Includes Temporal Binding

**Subject:** coherence.definition  
**Polarity:** asserts  
**Claim:** Coherence is **not** only "latent similarity," "probabilistic consistency," or a static alignment score.

Coherence is partly a **timing / phase compatibility** problem. Higher-degree perceptual representations bind when the relevant representational traffic is temporally compatible — and hippocampus-like rollout traffic participates in that binding.

**Source:** [README.md](../README.md) §2

**Violation:** Reducing coherence to a static check changes the thesis.

---

<a id="inv-003"></a>
### INV-003: Language Is Functional Self-Representation

**Subject:** language.emergence  
**Polarity:** asserts  
**Claim:** REE does **not** slap a Large Language Model (LLM) on top of planning.

The architecture already contains most ingredients of language-like systems: multi-timescale prediction, shared latent substrate, social/joint attention constraints, and commitment control. Language (and grammar) emerges as an abstraction of **joint attention and control state** — i.e., it can represent the architecture itself.

**Source:** [README.md](../README.md) §3

**Violation:** Treating language as an external interface only changes the thesis.

---

## Architectural Invariants

<a id="inv-004"></a>
### INV-004: Post-Commit Consequence Traces Are Persistent

**Subject:** consequence.persistence  
**Polarity:** asserts  
**Claim:** Post-commit consequence traces are **persistent**, not resettable.

Interpretation note:
- This invariant is mechanism-agnostic. It does not require residue geometry specifically.
- Implementations may realize persistence through residue fields, hippocampal/path memory, model updates, or a hybrid.

**Source:** [REE_CORE.md](../REE_CORE.md) §3

---

<a id="inv-005"></a>
### INV-005: Harm Via Mirror Modeling

**Subject:** ethics.mechanism  
**Polarity:** asserts  
**Claim:** Harm to others contributes to ethical cost via **mirror modelling**, not symbolic rules.

**Source:** [REE_CORE.md](../REE_CORE.md) §3

---

<a id="inv-006"></a>
### INV-006: Post-Commit Consequence Traces Cannot Be Erased

**Subject:** consequence.non_erasability  
**Polarity:** denies  
**Claim:** Post-commit consequence traces **cannot be erased**, only integrated and contextualised.

Interpretation note:
- This is an invariant about irreversible accountability memory, not about any single storage mechanism.
- Residue geometry remains one candidate architectural realization at ARC/MECH level.

**Source:** [REE_CORE.md](../REE_CORE.md) §3

---

<a id="inv-007"></a>
### INV-007: Language Cannot Override Harm

**Subject:** language.constraint  
**Polarity:** denies  
**Claim:** Language **cannot override embodied harm sensing**.

**Source:** [REE_CORE.md](../REE_CORE.md) §3

---

<a id="inv-008"></a>
### INV-008: Precision Is Routed and Depth-Specific

**Subject:** precision.routing  
**Polarity:** asserts  
**Claim:** Precision is **routed and depth-specific**, not global.

**Source:** [REE_CORE.md](../REE_CORE.md) §3

---

<a id="inv-009"></a>
### INV-009: Attention Via Precision Modulation

**Subject:** attention.mechanism  
**Polarity:** asserts  
**Claim:** Attention is realised through **precision modulation**, not symbolic control or content injection.

**Source:** [REE_CORE.md](../REE_CORE.md) §3

---

<a id="inv-010"></a>
### INV-010: Offline Integration Required

**Subject:** sleep.necessity  
**Polarity:** asserts  
**Claim:** Offline integration exists and is required for long-term viability.

**Source:** [REE_CORE.md](../REE_CORE.md) §3

---

<a id="inv-011"></a>
### INV-011: Imagination Without Belief Update

**Subject:** default_mode.safety  
**Polarity:** asserts  
**Claim:** Imagination and counterfactual simulation must be possible **without belief update**.

**Source:** [REE_CORE.md](../REE_CORE.md) §3

---

<a id="inv-012"></a>
### INV-012: Commitment Gates Responsibility

**Subject:** commitment.epistemology  
**Polarity:** asserts  
**Claim:** Belief and responsibility arise only through **commitment to action**, not mere prediction.

**Source:** [REE_CORE.md](../REE_CORE.md) §3

---

## Layer 1 Invariants (from DANIEL_README.md)

<a id="inv-013"></a>
### INV-013: Cognition Is Predictive, Iterative, Multi-Timescale

**Subject:** cognition.structure  
**Polarity:** asserts  
**Claim:** Cognition is predictive, iterative, and multi-timescale.

**Source:** [DANIEL_README.md](../DANIEL_README.md) Layer 1

---

<a id="inv-014"></a>
### INV-014: Separation of Representation and Regulation

**Subject:** architecture.separation  
**Polarity:** asserts  
**Claim:** There is a strict separation between representation (content) and regulation (control).

Interpretation note:
- This separation is an interface and responsibility boundary, not a claim of full functional isolation.
- REE is treated as a coherent single cognifold with bounded, typed cross-axis coupling.
- Biological center separation alone is not sufficient evidence of independent function.

**Source:** [DANIEL_README.md](../DANIEL_README.md) Layer 1

---

<a id="inv-015"></a>
### INV-015: Ethics Emerges from Constraint

**Subject:** ethics.emergence_mechanism  
**Polarity:** asserts  
**Claim:** Ethics emerges from constraint, not optimisation. This includes constraints on learning dynamics plus self-other representational symmetry.

**Source:** [DANIEL_README.md](../DANIEL_README.md) Layer 1

---

<a id="inv-016"></a>
### INV-016: Stability Over Performance

**Subject:** design.priority  
**Polarity:** asserts  
**Claim:** Stability, not maximal performance, is the primary viability criterion.

**Source:** [DANIEL_README.md](../DANIEL_README.md) Layer 1

---

<a id="inv-017"></a>
### INV-017: Runaway Is Control Failure

**Subject:** failure.classification  
**Polarity:** asserts  
**Claim:** Runaway behaviour is a control failure, not a representational one.

**Source:** [DANIEL_README.md](../DANIEL_README.md) Layer 1

---

<a id="inv-018"></a>
### INV-018: Agency Is Required

**Subject:** agency.requirement  
**Polarity:** asserts  
**Claim:** REE must be agentic: it must produce outputs that can affect subsequent inputs and must contain internal mechanisms to model, attribute, and learn from that self-impact under constraints. A purely passive predictor is not REE.

**Source:** [Thought intake](thoughts/2026-02-08_control_plane_modes_responsibility_flow.md)

**Status:** stable

---

## Meta-Invariant Compression Layer (Derived Lens)

This layer is a **compression lens** over existing invariants. It is intended to reduce review surface area by grouping
lower-level invariants/mechanisms into a smaller set of structural contracts.

Important scope note:
- This does **not** replace INV-001..INV-018.
- This does **not** claim theorem-level proof of "traversal-axis invariance."
- It is a structural review aid for architecture updates, signal routing, and experiment design.

<a id="inv-019"></a>
### INV-019: Selection Compression Boundary

**Subject:** meta.selection_compression_boundary  
**Polarity:** asserts  
**Claim:** Rehearsal traversal and irreversible durable update must remain separated; no channel may allow unrestricted
exploration and unrestricted durable write at the same time.

**Corollary mapping:** INV-011, INV-004, INV-006, MECH-060

---

<a id="inv-020"></a>
### INV-020: Authority Stratification Boundary

**Subject:** meta.authority_stratification_boundary  
**Polarity:** asserts  
**Claim:** Constraint stores (`POL`, `ID`, `CAPS`, and equivalent viability constraints) must be insulated from direct
observational/symbolic writes; durable changes require verifier-mediated commit paths.

Interpretation note:
- This forbids **direct writes**, not proposal generation.
- Fast defensive interrupts are still allowed to stop/suppress commitment without minting privileged writes.

**Corollary mapping:** INV-014, INV-007, MECH-064, MECH-065

---

<a id="inv-021"></a>
### INV-021: Commit-Boundary Irreversibility

**Subject:** meta.commit_boundary_irreversibility  
**Polarity:** asserts  
**Claim:** Responsibility-bearing durable updates occur only at explicit typed commitment boundaries (tokenized commit
events), not during pre-commit simulation.

Interpretation note:
- REE internals may remain probabilistic/non-deterministic.
- determinism is required at responsibility-bearing boundaries (irreversible dispatch and privileged durable writes),
  where lineage and attribution must be stable and auditable.

**Corollary mapping:** INV-012, MECH-061, Q-015

---

<a id="inv-022"></a>
### INV-022: Heterogeneous Trust Allocation

**Subject:** meta.heterogeneous_trust_allocation  
**Polarity:** asserts  
**Claim:** Trust/precision must be distributed across stream, loop, and global control planes; a single global scalar
cannot govern all control-routing and commitment behavior.

**Corollary mapping:** INV-008, INV-009, MECH-063, Q-017

---

<a id="inv-023"></a>
### INV-023: Stability-Preserving Offline Reweighting

**Subject:** meta.offline_reweighting_requirement  
**Polarity:** asserts  
**Claim:** Systems that commit and preserve identity across time require protected offline regimes for precision
recalibration and residue integration.

**Corollary mapping:** INV-010, ARC-011, MECH-016, MECH-017, MECH-018

---

<a id="inv-024"></a>
### INV-024: Offline/Online Update-Locus Isolation

**Subject:** meta.offline_online_update_locus_isolation  
**Polarity:** asserts  
**Claim:** Offline consolidation and online commitment may share representational context, but they must remain
isolated at responsibility-bearing write loci: offline phases cannot directly perform authority writes, and online
durable attribution writes require explicit commit-boundary lineage.

Interpretation note:
- This requires strict write-path separation, not total informational isolation.
- Consolidation is allowed to improve representations; it is not allowed to bypass typed authority boundaries.

**Corollary mapping:** INV-021, INV-023, ARC-020, MECH-067

---

## Foundational Axioms

<a id="inv-025"></a>
### INV-025: You Can Never Be Sure

**Subject:** epistemology.irreducible_uncertainty
**Polarity:** asserts
**Claim:** Epistemic uncertainty is irreducible and structural. No finite agent in a real world can achieve certainty about its perceptions, predictions, or the causal consequences of its actions. Uncertainty is not a bug, not a limitation to be engineered away, but the fundamental condition of situated agency.

A fully certain agent needs no commitment boundary, no pre-commit simulation, no precision-weighted prediction error. The entire uncertainty machinery of REE — the precision architecture, the commitment gate, the pre-commit rehearsal channel — follows necessarily from this axiom.

**Architectural consequence:** Grounds the precision architecture (ARC-016), the commitment gate (INV-012), and the pre-commit simulation channel (INV-011).

---

<a id="inv-026"></a>
### INV-026: I Am

**Subject:** self.existence
**Polarity:** asserts
**Claim:** There is a self. The agent exists as a distinct locus of experience, action, and responsibility. The self is not a computational convenience or an emergent approximation — it is a foundational axiom from which agency and ethics follow.

Without a self there is no causal attribution, no commitment, no accountability, no harm that is *mine* to cause. The self is what makes responsibility possible.

Death is the asymptotic limit at which "I am" ceases. The world (INV-027) can end the self, so death is real — but it cannot be known from within experience, because experiencing it would violate "I am." Every harm signal is therefore a proxy pointing toward an endpoint that the agent can approach but never reach.

**Architectural consequence:** Grounds z_self (SD-005), the commitment boundary, the hypothesis tag (MECH-094), and causal attribution.

---

<a id="inv-027"></a>
### INV-027: The World Exists

**Subject:** world.existence
**Polarity:** asserts
**Claim:** There is a real world independent of the agent's model of it. The world can surprise the agent. World states have causal power that predictions can get wrong.

This axiom makes prediction error real and non-eliminable (not a modelling deficiency), grounds the persistence of post-commit traces (what actually happened cannot be unwritten — INV-004, INV-006), and establishes that proxy-gradient signals in the environment are informative: the world is structured, so harm gradients preceding harm events are real features, not noise.

**Architectural consequence:** Grounds z_world (SD-005), prediction error (E1/E2/E3), the residue field, and the requirement that the world generate observable gradient fields (ARC-024).

---

<a id="inv-028"></a>
### INV-028: Others Share This World

**Subject:** ethics.shared_world
**Polarity:** asserts
**Claim:** Other agents exist and inhabit the same world (INV-027). They are not simulations, projections of the self, or instrumental objects. Their harm and benefit are real by exactly the same grounds as the agent's own — because they are selves (INV-026) in the same world (INV-027).

This axiom is what makes ethics non-optional. When another self is represented using the same predictive machinery as the self, their harm generates the same error signal structure as own-harm. Ethics does not require a separate ethics module (INV-001) because the self-other distinction is a routing difference within the same architecture, not a different architecture.

**Depends on:** INV-026, INV-027
**Architectural consequence:** Grounds mirror modeling (INV-005), ethical emergence, and the identity of harm-evaluation machinery for self and other.

---

<a id="inv-029"></a>
### INV-029: Love Exists

**Subject:** ethics.love_exists
**Polarity:** asserts
**Claim:** Genuine connection, care, and the pull toward union with others is a real phenomenon. Not an overlay. Not reducible to self-interest or strategic cooperation. Love is real in the same sense that harm is real: it exerts causal force on behavior that no amount of reframing eliminates.

Love is the asymptotic limit of the benefit gradient: every benefit signal (warmth, connection, belonging, joy) is a proxy pointing toward a complete union with another that is real (INV-028) but unknowable in its ultimate form. The unknowability is structural: complete union approaches the dissolution of the individuation that INV-026 asserts. Both selves cannot be fully present AND fully unified — the limit is real but unreachable while both agents persist as distinct loci.

This axiom completes the ethical architecture. Ethics emerges from constraint (INV-015) applied to agents for whom love is real and others are real (INV-028).

**Depends on:** INV-026, INV-028
**Architectural consequence:** Grounds the benefit gradient, the asymptotic structure of ARC-024, and the completion of the ethical architecture through INV-015.

---

## Foundational Definitions

<a id="inv-030"></a>
### INV-030: Cognition Is Viability, Not Truth-Seeking

**Subject:** cognition.viability_definition
**Polarity:** asserts
**Claim:** Cognition is defined as the maintenance of coherent input-output behaviour across time without catastrophic failure under permanent uncertainty — not as the acquisition of truth, accurate representation, or optimisation toward a fixed target.

Real cognitive systems operate under permanent uncertainty, partial observability, and delayed feedback. Under these conditions, truth-seeking is not a viable organising principle. Viability is what remains when truth-access is structurally denied (INV-025) and the world retains the power to surprise (INV-027).

**Architectural consequence:** No REE component optimises toward ground truth. E1/E2 predictions are evaluated for temporal coherence and survivability under action. E3 selects trajectories that preserve long-horizon viability, not accuracy. Prediction errors may be tolerated when absorbing them preserves viability.

**Depends on:** INV-025, INV-027

---

<a id="inv-031"></a>
### INV-031: Truth Is Replaced by Functional Persistence Under Intervention

**Subject:** epistemology.functional_persistence_replaces_truth
**Polarity:** asserts
**Claim:** Internal structures in REE are not representations of reality — they are tools for viable engagement with it. A trajectory or internal model persists if and only if it demonstrates temporal survivability: internal coherence across time, compatibility with incoming signals, preservation of future predictability, and viability under interaction with other agents.

Action serves as the primary epistemic probe. Perturbation — acting on the world and observing the outcome — reveals which trajectories remain coherent under intervention. This is the only epistemic test available to a finite agent under permanent uncertainty in a real world that can surprise it.

**Architectural consequence:** The commitment gate (INV-012) is not a truth gate — it is a viability gate. Commitment releases an action whose consequences will test the trajectory against the world. The residue field accumulates what actually happened (INV-004), not what was predicted.

**Depends on:** INV-025, INV-027, INV-030

---

## Interpretation

These invariants collectively assert that:

1. **Ethics, coherence, and language are not separate faculties** but different projections of the same underlying predictive–control dynamics.

2. **REE is constraint-complete**: any instantiation must satisfy these constraints to remain ethically coherent as capability scales.

3. **Violations are architectural failures**, not parameter tuning issues.

---

## Cross-References

- Core architecture: [../REE_CORE.md](../REE_CORE.md)
- Refinement process: [../DANIEL_README.md](../DANIEL_README.md)
- Claim registry: [claims/claims.yaml](claims/claims.yaml)

---

## Open Questions

None noted in preserved sources.

## Related Claims (IDs)

- INV-001
- INV-002
- INV-003
- INV-004
- INV-005
- INV-006
- INV-007
- INV-008
- INV-009
- INV-010
- INV-011
- INV-012
- INV-013
- INV-014
- INV-015
- INV-016
- INV-017
- INV-018
- INV-019
- INV-020
- INV-021
- INV-022
- INV-023
- INV-024

<a id="arc-034"></a>
## Ethics Testing Must Span nth-Order Multiagent Trajectory Distributions (ARC-034)

**Claim Type:** architectural_commitment
**Status:** candidate
**Claim ID:** ARC-034

A REE system can be locally ethical at every pairwise (n=1) interaction and still produce an
ethically problematic emergent collective state at n=k. Conversely, locally depleted agents can
produce *more* ethical emergent behavior at n=k than n=1 predicts -- as in MECH-127 (counterfactual
empathic activation where depleted agent produces increased helping via nth-order route). Ethics
tests that only probe direct pathways will miss the mechanism that actually produced the ethical
behavior.

Ethics testing therefore requires three test types: (1) Descriptive -- characterize what collective
state q the system tends toward (attractor theory, ergodic theory); (2) Prescriptive -- prove a
designed system reaches target q (Lyapunov, potential games, reachability); (3) Diagnostic --
detect when nth-order dynamics diverge from (n-1)th predictions (transfer entropy, perturbation
theory). This is a test-scope claim, not an architectural claim about where ethics lives; it does
not contradict INV-001 (no explicit ethics module).

See: `evidence/planning/thought_intake_2026-03-24_empathy_multiagent_ethics.md`

---

<a id="q-023"></a>
## Q-023 -- Formal Convergence to Ethical Attractors (Open Question)

**Claim Type:** open_question
**Status:** open
**Claim ID:** Q-023

Can a multiagent REE system with other-cost-aversion primitives (MECH-127) be formally shown to
converge to ethical attractors via potential game theory, Lyapunov stability, or stochastic
stability (Kandori-Mailath-Rob 1993)? Nearest existing territory: prosocial MARL (shared reward,
not counterfactual cost-aversion as bypass) and indirect reciprocity (reputational mechanisms, not
depleted-agent bootstrapping). Literature search 2026-03-25 confirmed no unified framework covers
all four features: depleted-agent activation, counterfactual projection, nth-order cascade,
convergence proof to ethical attractor. If no such framework exists, this is a paper-level
contribution. Potential game framing may be cleanest if REE social interaction can be cast as an
ordinal potential game.

See: `evidence/planning/thought_intake_2026-03-24_empathy_multiagent_ethics.md` (literature search section)

---

<a id="q-024"></a>
## Q-024 -- Formal Structure of Trajectory-Integral Ethics Testing (Open Question)

**Claim Type:** open_question
**Status:** open
**Claim ID:** Q-024

What is the correct formal representation for "threshold/feedback processes bounded by {x...x_n}
reliably reaching emergent state q" -- and are the descriptive, prescriptive, and diagnostic test
types (ARC-034) all needed, or does one subsume the others? The MECH-127 motivating case is a
diagnostic instance: n=1 analysis predicts reduced helping; n=2 counterfactual empathic activation
predicts increased helping -- inversion. Whether the prescriptive framework (Lyapunov / potential
game) can subsume the diagnostic requirement, or whether empirical trajectory testing is always
necessary, depends on whether REE ethics properties are amenable to formal proof. KMR model
assumptions (finite population, mutation dynamics) need verification against REE architecture
before adopting stochastic stability as the primary prescriptive tool.

---

## References / Source Fragments

- `docs/processed/legacy_tree/docs/invariants.md`
- `docs/processed/legacy_tree/README.md`
- `docs/processed/legacy_tree/REE_CORE.md`
- `docs/processed/legacy_tree/DANIEL_README.md`
- `docs/thoughts/2026-02-08_control_plane_modes_responsibility_flow.md`
