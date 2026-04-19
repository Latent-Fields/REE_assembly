---
title: Home
nav_order: 1
---

# Reflective-Ethical Engine

REE is a research programme with a single organising question:

**What architecture does an agent need in order to act ethically — and can that
architecture be derived from first principles rather than designed by hand?**

Most attempts to build ethical AI work by specifying desired behaviour and
training toward it. REE takes a different approach: starting from the minimum
commitments an agent must make if it is to act in a world at all — that it
exists, that the world can harm it, that others exist and are like it — and
asking what computational structures those commitments strictly require. The
architecture follows from the requirements. It is not a design; it is a derivation.

REE argues that ethical agency requires specific computational capacities, not
just rules or reward shaping. An agent must be able to distinguish self from
world and self from other, separate imagined action from real action, attribute
responsibility for its effects, learn from mistakes, and keep care structurally
live in how it evaluates trajectories. On this view, ethical behaviour is not
something added on top of intelligence, but something that depends on the right
substrate for accountable action.

Computational psychiatry is one of REE's main validation paths. If those
capacities are genuinely required, then their failure should produce
recognizable regime breakdowns rather than arbitrary errors: depression,
dementia, OCD, mania, psychosis, and related disturbances can be understood as
failures in the same substrate that underwrites agency, responsibility, and
care. Psychiatry is therefore not separate from the project, but one of the
main ways its architectural claims can be tested.

---

## What the derivation found

Starting from a handful of foundational axioms and working through what
comparator functions ethical agency cannot do without, the architecture that
follows includes a persistent world model, a fast transition predictor, a
harm accumulator with a reset condition, a commit gate tied to genuine
uncertainty, and a multi-step planning mechanism that can model others' harm
and goals in the same terms as its own.

This is not a long list of components chosen to cover the design space. It is
a short list of structures that cannot be absent without losing the capacity
for ethical action. Remove any one and a specific ethical function disappears.

**When cross-checked against neuroscience, this architecture maps — without
having been built to fit — onto most major brain structures and their known
functional roles.** The offline consolidation phase the mathematics requires
matches the two-stage sleep architecture. The commitment gate maps to the
basal ganglia circuit. The harm accumulator maps to the cingulate and its
modulation by serotonin. The convergence was found after the derivation,
not before it.

**When the missing structures are identified as failure modes, they match
clinical psychopathology.** Absent harm accumulator: features of anhedonia
and chronic pain. Closed attribution loop: passivity phenomena. Precision
dysregulation: psychosis-like states. The failures occur at the same
positions in biological and artificial systems because they are both
instantiations of the same necessary architecture — or its absence.

---

## The alignment implication

Current AI systems are trained to pursue proxies for what ethical agency
requires. The proxies are often good. But the architecture that genuine
ethical agency requires — structures that cannot be gamed by a sufficiently
capable optimiser, because they are what doing the thing consists in, not
approximations of it — is absent. Scaling capability over an architecture
that lacks the necessary comparators does not introduce those comparators.
The failure modes that emerge at scale are predictable from the absences.

This is a different claim from "we need better specifications." It is a
claim about what kind of problem alignment is.

---

## Where to start

**If you are new to REE:**
[Why This Architecture?](architecture/ethical_agency_derivation.md) —
the derivation in full; the cognifold motif; why the brain result matters

**If you want the foundational argument:**
[Foundations](architecture/five_axioms_foundations.md) —
the irreducible axioms from which the architecture follows; derived ethical objectives

**If you want the component architecture:**
[Architecture overview](architecture/overview.md) — then
[E1](architecture/e1.md), [E2](architecture/e2.md),
[E3](architecture/e3.md), [Control Plane](architecture/control_plane.md),
[Hippocampal Systems](architecture/hippocampal_systems.md)

**If you want what this predicts and where it is tested:**
[Roadmap](roadmap.md) — programme phases and current experimental state

**If a term is unfamiliar:**
[Glossary](glossary.md) — canonical terminology; start here before component docs

**If you want to contribute compute:**
[Contribute](contribute.html) — no account needed; experiments run on donated GPU time

---

## Latest result

**EXQ-223 — Minimal mind confirmed (2026-04-03)**

The REE core loop — E1 + E2 + HippocampalModule + go/no-go selection + raw
harm/reward signals — produces stable navigation, harm avoidance, and resource
acquisition without deliberation or commitment machinery. 3/3 criteria met
across 3 independent seeds.

The circuit topology matches the zebrafish larva (5–7 dpf) at the level of
named structures: dorsal pallium (E1), cerebellum (E2), lateral pallium
(hippocampal module), optic tectum and reticulospinal neurons (go/no-go),
lateral habenula (harm signal). The larva has no mature prefrontal cortex —
no commitment architecture — which is exactly what the ablation removes.
This match was derived from functional arguments; it was not built to fit
the biology.

[Full analysis and circuit table](changelog.md#2026-04-03-exq-223-pass--minimal-mind-hypothesis-confirmed)

---

## Claims and evidence

REE claims are typed (INV / ARC / MECH / Q / IMPL), registered with confidence
scores, and governed through an experiment-evidence pipeline.

[Claims index](claims/claim_index.md) — all registered claims with status and dependencies

---

## Related frameworks

**[REE vs. Neural Computers (Meta AI / KAUST)](architecture/comparisons/meta_kaust_neural_computers.md)**
The Neural Computers programme (Schmidhuber et al., 2025) proposes unifying
computation, memory, and I/O as a single learned runtime. Their four
requirements for a Completely Neural Computer — Turing completeness, universal
programmability, behavior consistency, and machine-native semantics — map
directly onto structures REE derives from first principles. The comparison
document shows the cross-walk.

---

## Implementation substrates

| Substrate | Status | Role |
|-----------|--------|------|
| ree-v3 | Active | Primary implementation target |
| ree-v2 | Complete | 15 experiments (6 PASS / 7 FAIL); triggered V3 transition |
| ree-v1-minimal | Active (baseline) | Parity substrate |
