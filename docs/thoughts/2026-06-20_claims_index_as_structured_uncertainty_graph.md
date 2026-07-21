# Claims Index as a Structured Uncertainty Graph

Status: processed
Processed in:
- `docs/claims/claims.yaml` (SD-062 `claims-index as a typed multi-axis structured-uncertainty graph` -- the surviving constructive outcome of the DLIF line, applied to the claims registry rather than to REE cognition. This file is cited in that claim's `sources`.)


**Date:** 2026-06-20  
**Status:** thought_intake  
**Scope:** REE_assembly claims index, evidence graph, experiment prioritisation, and implementation dispatch  
**Source:** Gmail capture on Bayesian networks / Markov networks; follow-up discussion with Daniel Golden  
**Primary benchmark note:** potentially useful before the REE-v3 strict green-board benchmark of **Sunday 19 July 2026** if implemented lightly. Do not turn this into a large mathematical project before v3.

---

## Core thought

The REE claims index may itself need to become a **structured uncertainty graph**.

The claims index is already doing externalised cognition. It preserves claims, evidence, conflicts, experimental tests, implementation dependencies, roadmap relevance, and unresolved questions. This resembles probabilistic graphical modelling, but a pure Bayesian network or pure Markov network would be too limiting.

The better representation may be:

```text
A typed claim graph with optional probabilistic / coherence-propagation semantics.
```

---

## Why ordinary confidence is insufficient

A REE claim is not just true or false.

A claim may be:

- well-supported but not implementation-relevant yet;
- weakly supported but v3-blocking;
- architecturally central but empirically under-tested;
- ethically important but not currently executable;
- contradicted by another claim;
- superseded by a newer formulation;
- useful as a scaffold even if not finally true;
- v4-only, v5-only, or v6+;
- not a claim at all, but a question, dependency, or deferred research line.

Therefore a single scalar confidence score cannot carry enough structure.

---

## Why Bayesian networks are not enough

Bayesian network structure is useful for directed relationships such as:

```text
evidence -> claim
claim -> implementation decision
experiment -> result -> claim update
```

This is useful for evidence propagation and claim updating.

But the REE claims index contains loops:

```text
architecture claim -> experiment design -> result -> architecture claim
mechanism claim -> implementation -> observed behaviour -> mechanism claim
ethical claim -> governance rule -> release gate -> ethical claim revision
```

A pure Bayesian network is too rigid because many REE dependencies are cyclic, revisable, and governance-like.

---

## Why Markov networks are not enough

Markov-style representations are useful for mutual coherence and compatibility constraints:

```text
Claim A coheres with Claim B.
Claim C conflicts with Claim D.
Claim E requires Claim F.
Claim G becomes urgent if v3 implementation depends on it.
```

This is useful for conflict burden, coherence, and dependency pressure.

But a pure Markov network loses too much directionality. It does not naturally distinguish:

```text
evidence supports claim
claim motivates experiment
experiment tests claim
result weakens claim
claim gates implementation
```

The claims index needs both directed update and undirected coherence.

---

## Proposed structure

The claims index should be representable as a typed graph.

### Possible node types

- Claim
- Evidence
- Experiment
- Result
- Implementation decision
- Roadmap stage
- Risk
- Open question
- Deferred idea
- Literature source
- External repository dispatch
- Governance rule

### Possible edge types

- supports
- contradicts
- requires
- refines
- supersedes
- tested_by
- implemented_by
- blocks
- informs
- deferred_to
- increases_priority_of
- decreases_confidence_in
- narrows
- generalises
- depends_on
- dispatches_to

---

## Multi-axis claim state

Claim confidence should be decomposed.

Possible axes:

| Axis | Meaning |
|---|---|
| truth confidence | how likely the claim is to be true |
| evidence strength | how strong the evidence is |
| implementation dependence | how much current code depends on the claim |
| conflict burden | how many unresolved contradictions touch it |
| roadmap relevance | v3 / v4 / v5 / v6+ relevance |
| experiment status | untested / partially tested / contradicted / supported |
| ethical risk | consequence if wrong |
| v3-blocking status | whether this must be resolved before strict green-board |
| dispatch status | where implementation or testing belongs |

This prevents claims from being promoted or deferred for the wrong reason.

---

## Practical queries this would enable

A structured uncertainty graph could help answer:

1. Which claims are most load-bearing?
2. Which claims are under-evidenced?
3. Which claims are in unresolved conflict?
4. Which experiment would reduce the most uncertainty?
5. Which implementation decision depends on the weakest claim?
6. Which claims are v3-blocking?
7. Which claims are important but safely deferrable?
8. Which claims are ethically significant but not implementation-ready?
9. Which claims are being treated as settled despite weak support?
10. Which thought-intake documents should be promoted, merged, or archived?

---

## Relation to REE-v3 strict green-board

This may be operationally useful before the REE-v3 strict green-board target, but only in a light form.

Before **Sunday 19 July 2026**, likely safe actions:

- add explicit typed edges where missing;
- distinguish v3-blocking from v4+ important;
- preserve multi-axis claim status in documentation;
- use the graph to prevent scope creep;
- use the graph to choose the next experiment.

Likely unsafe actions before strict green-board:

- building a full probabilistic inference engine;
- requiring factor-graph-style message passing before v3;
- restructuring the whole claims registry if that delays experiments;
- making mathematical elegance more important than green-board evidence.

---

## Repo-level implication

This belongs primarily in REE_assembly, not ree-v3.

REE_assembly is already acting as the governance / claims / evidence / dispatch layer. A structured uncertainty graph is most useful there first.

Possible future destinations:

```text
docs/claims/
docs/thoughts/
docs/governance/
docs/architecture/
evidence/literature/
```

---

## Provisional claim

```text
The REE claims index should be representable as a typed dependency-and-coherence graph with optional probabilistic semantics, allowing evidence, conflict, experiment results, roadmap stage, ethical risk, and implementation dependency to propagate without collapsing claims into false certainty.
```

---

## Provisional status

**Operational relevance:** high  
**Mathematical implementation relevance before v3:** low  
**Lightweight schema relevance before v3:** medium-to-high  
**Do not block:** REE-v3 strict green-board

---

## Open questions

1. Does the current `claims.yaml` already have enough fields to approximate this?
2. Which missing edge types would produce the biggest immediate gain?
3. Should v3-blocking status be a first-class claim field?
4. Should claims be allowed to have separate truth confidence and implementation-dependence scores?
5. Can a simple explorer view surface load-bearing / under-evidenced / conflict-burdened claims without full probabilistic inference?
