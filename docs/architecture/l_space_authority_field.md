---
title: "L-space Authority Field (MECH-534, Q-103)"
parent: "Core Engines & Forward Models"
grandparent: Architecture
nav_order: 15
status: candidate
status_asof: 2026-09-04
status_claim: MECH-534
---

# L-space Authority Field

**Registered:** 2026-09-04
**Source thought:**
[`docs/thoughts/2026-09-04_authority_field_analog_cognition_ephaptic_coupling.md`](../thoughts/2026-09-04_authority_field_analog_cognition_ephaptic_coupling.md)
(precursor: `docs/thoughts/2026-09-02_temporary_coordinated_representational_transformations.md`).
**Intake:**
[`thought_intake_2026-09-04_authority_field_analog_cognition.md`](../../evidence/planning/thought_intake_2026-09-04_authority_field_analog_cognition.md).
**Related:** [Latent Stack (L-space)](l_space.md) (ARC-004), the cognifold signed-edge spec (ARC-084,
MECH-363), typed coalition instantiation (MECH-481, MECH-503), field coherence (MECH-499, MECH-500).

> **DOC + GOVERNANCE ONLY.** Research-bounded mechanism hypothesis. The thought's own instruction --
> "no implementation should follow directly from this intake" -- and the same-day routing note's
> brake -- "do not infer yet that an authority/gating mechanism is needed beyond existing precision,
> policy, or control-plane machinery" -- both stand. Neither claim below asserts that REE *needs* the
> mechanism.

---

## MECH-534 -- authority field: L-space coupling as dynamic causal geometry {#mech-534}

The moment-to-moment functional conformation of L-space -- the effective directed distance /
permeability / gain between representational regions, its direction and asymmetry, its persistence
and decay, the compatibility or interference of simultaneously active routes, and a local coalition's
capacity to recruit wider participation -- is a **state variable in its own right**: continuous,
graded, state-dependent, endogenously recruited from the organism's own prediction error, goal
progress, residue and learned relevance, with its own competition and dynamics, and *not* identical
to stored content, to the slow regulatory / neuromodulatory field, or to the final policy. Sketch:
`r_i(t+1) = f_i(r(t), u(t), d(t), g(t))`, `d_ij(t+1) = h_ij(d(t), E1, E2, memory, goal, self_other,
g(t))`; a first implementation could be a small set of channel / trajectory gates with decay,
competition and phase-like timing, not a dense matrix or a neural-field simulation.

**Falsifiable consequences.** (1) Two runs with materially similar content state but different field
state show systematic differences in retrieval, commitment and distractor recovery. (2) An
equally-parameterised **static scalar or global gate cannot reproduce** the same context-sensitive
behaviour across matched tasks and seeds -- this is the PRIMARY test and the claim dies on it. (3)
High-salience but currently irrelevant memories or attractors exert less inappropriate influence.
(4) In useful regimes the field is neither permanently uniform nor permanently fragmented.
(5) Any gain that comes only from extra parameters, or from a field state that is injected rather
than recruited, refutes the claim as stated.

**Distinct from** ARC-084 (specifies cognifold edge *types* -- sign, gain, precision, gate,
timescale, write_authority -- as properties of a V4 multi-field layer; MECH-534 is those edges given
fast, endogenous dynamics: the gain is a state, not a parameter), MECH-481 (demand-typed,
template-driven coalition lookup at subsystem grain), MECH-500 (a distinct *readiness* authority axis;
MECH-534 is about who-influences-whom, not whether commitment may land), INV-008 (precision is routed
-- MECH-534 adds that the routing has its own dynamics), MECH-005 (one NE-like scalar), INV-037
(stored != active -- the static fact MECH-534 would make dynamic), SD-064 (a single access channel,
not a relational field), MECH-359 + ARC-065 GAP-A (a candidate-conditioned transform, built; the
nearest V3 instantiation to inspect first).

**Pre-registered probe (for digestion, not for building now):** five channels -- immediate
perception, goal state, recent residue, retrieved trajectory, harm/benefit signal -- each with graded
eligibility, persistence/decay, competition, endogenous recruitment and a logged path into E3;
matched episodes with content and policy weights held constant and authority state perturbed; a
static/scalar-gating baseline; readouts = distractor recovery, goal switching, obsolete-attractor
suppression, appropriate-vs-salient retrieval, prediction-error resolution, downstream commitment
change. Success is a reproducible behavioural change with endogenous recruitment, local operation,
competitive authority and committed throughput (ARC-130's ladder), not an activation plot.

**Consciousness note:** the thought's "sufficiently integrated, recurrently self-influencing field"
is recorded only as a SENT-1 indicator candidate; SENT-0 stands.

`substrate_conditional`, v4 / v4_v5. DO NOT build in V3; DO NOT queue.

---

## Q-103 -- routing-only or representational field? {#q-103}

Does the trajectory of L-space's coupling / authority state itself carry task-relevant relational
structure (spatial relations, sequence, recent history) beyond the instantaneous content state it
gates -- a **representational field** -- or does it only set eligibility, gain and topology over
content stored elsewhere -- a **routing-only field** -- or both?

**Pre-registered discriminator.** On the SAME stored representations, controlled for parameter
count and training exposure, compare an instantaneous decoder over `r(t)` with a trajectory decoder
over `r(t-k:t)` plus the authority variables. If the trajectory decoder predicts current global
structure, the appropriate retrieved path, or the next committed action better, the representational
branch is supported; if not, the more parsimonious routing-only account survives. Nearest existing
claims: MECH-499 (field coherence as content aggregation -- would predict the representational branch
for the hippocampal case); MECH-466 (event-relative coordination). Cited implementation evidence
(Jacobs et al. 2025, travelling waves integrating spatial information in locally connected RNNs) is
unverified pending the lit-pull.

Substrate-conditional on MECH-534 having any instantiation. Open.
