# Thought intake: complementary processing modes for REE_assembly machinery

**Date:** 2026-06-20  
**Status:** thought intake / governance-machinery design note  
**Scope:** REE_assembly, not REE agent architecture  
**Related note:** `thought_intake_2026-06-20_complementary_processing_modes_agent.md`  
**Related existing machinery:** inter-governance workset, failure autopsy, claim synthesis, lit-pull, thought intake, closure maps, experiment queue, runner heartbeats, evidence ledger, substrate queue.

---

## 1. Core thought

REE_assembly may benefit from explicitly recognising and preserving complementary processing modes.

The motivating analogy is hemispheric-style functional complementarity: broad contextual integration versus local-detail adjudication. This should not be treated as a literal left-brain/right-brain claim, nor as an anatomical mapping. It is a functional design heuristic.

The key point for REE_assembly is that project cognition appears to require multiple stances that should not collapse into one undifferentiated review mode.

```text
broad synthesis
+ local adjudication
+ design generation
+ evidence gating
+ implementation prosecution
+ integration / commitment
= more reliable project cognition
```

---

## 2. Why this matters for REE_assembly

REE_assembly already behaves as an externalised executive-function and governance system. It does not merely store work; it helps determine what can be believed, what should be tested, what should be deferred, and what should become a claim, substrate entry, closure-map node, or paper-adjacent note.

The current F-dominance / basal-ganglia selector discussion illustrates the need for complementary modes:

- broad synthesis detects the architectural pattern: many upstream signals form but fail to purchase committed action;
- design imagination generates the hypothesis that the selector may need a more basal-ganglia-like constitution;
- evidence gating resists immediate redesign and forces V3-EXQ-689a to land first;
- detailed adjudication checks manifests, criteria, and false positives;
- integration decides whether the result becomes substrate work, claim synthesis, literature pull, closure update, or thought intake.

This is productive tension, not inconsistency.

---

## 3. Proposed REE_assembly processing modes

| Mode | Function | Failure mode if isolated |
|---|---|---|
| Broad synthesis | Detects cross-experiment patterns, architectural shape, and high-level causal hypotheses. | Overreach, premature unification, narrative coherence without evidence. |
| Local adjudication | Checks manifests, line-level evidence, acceptance criteria, controls, and overclaim risk. | Local optimisation, failure to see convergence, excessive conservatism. |
| Design generation | Produces candidate architecture, experiments, decompositions, and repair paths. | Speculative churn, bypassing governance, building before evidence. |
| Experimental prosecution | Pursues one route fully enough for the evidence to become interpretable. | Perseveration, continuing after the question has been answered. |
| Evidence gating | Prevents claims from advancing before sufficient tests land. | Inertia, delayed useful design work, under-recognition of obvious patterns. |
| Integration / commitment | Decides what the system should record, route, promote, block, or retire. | Premature closure or endless deferral. |

---

## 4. Governance implication

REE_assembly should not treat all reviews as the same kind of cognition.

A mature governance workflow should deliberately ask:

```text
Which mode is currently speaking?
Which mode is missing?
Which mode has too much authority?
Which mode should make the next move?
```

For example:

```text
Broad synthesis may propose: "this is a shared selector bottleneck."
Evidence gating may answer: "689a must land before redesign."
Design generation may propose: "basal-ganglia-like selector constitution."
Local adjudication may answer: "record as thought intake, not implementation."
Integration may decide: "route to post-689a design branch."
```

This is an explicit project-level analogue of cognitive control.

---

## 5. Relationship to current tooling

Existing REE_assembly tools already partially instantiate these modes:

| Tool / artefact | Dominant mode |
|---|---|
| Thought intake | Design generation / broad synthesis capture. |
| Failure autopsy | Local adjudication plus causal integration. |
| Claim synthesis | Broad synthesis constrained by discriminability. |
| Lit-pull | External grounding and constraint injection. |
| Experiment queue | Experimental prosecution. |
| Runner heartbeats | Evidence-state monitoring. |
| Closure map | Integration / commitment tracking. |
| Inter-governance workset | Routing across modes. |
| Pending review | Evidence gating. |

The next refinement may be to make mode identity explicit in artefacts and prompts.

---

## 6. Proposed metadata addition

Future thought intakes, autopsies, and synthesis documents could optionally include:

```yaml
processing_mode:
  primary: broad_synthesis | local_adjudication | design_generation | evidence_gating | experimental_prosecution | integration
  secondary: []
  next_required_mode: local_adjudication | lit_pull | experiment | claim_synthesis | implementation | defer
```

This would help prevent category errors, for example treating a design intuition as an adjudicated claim, or treating a local failed criterion as if it disproves a broader convergent pattern.

---

## 7. Separation from REE agent architecture

This note concerns REE_assembly only.

REE_assembly is not REE. REE_assembly is the external governance, memory, routing, and evidence machinery around the project. Its complementary processing modes are project-cognition roles, not agent-internal modules.

The analogous REE-agent question is recorded separately in:

```text
thought_intake_2026-06-20_complementary_processing_modes_agent.md
```

That separate note asks whether REE itself may require broad-context and local-action processing streams mediated by conflict and commitment machinery.

---

## 8. Risks

### 8.1 False hemispheric literalism

This should not be framed as literal left-hemisphere / right-hemisphere modelling. The analogy is functional and heuristic only.

### 8.2 Role reification

Processing modes should not become rigid agent identities. They are stances or functions, not necessarily separate agents.

### 8.3 Governance bloat

Adding explicit mode metadata could become busywork unless it reduces real errors: overclaiming, under-synthesis, premature implementation, or missed routing.

### 8.4 Authority imbalance

A project can be harmed by either excessive broad synthesis or excessive local adjudication. The governance value lies in dynamic balance, not privileging one mode.

---

## 9. Minimal recommendation

Treat complementary processing modes as an explicit design principle for REE_assembly.

Do not immediately add new machinery unless there is evidence of repeated category errors.

Near-term useful action:

```text
When creating or reviewing a major artefact, identify whether it is:
- broad synthesis,
- local adjudication,
- design generation,
- evidence gating,
- experimental prosecution,
- or integration / commitment.
```

This would preserve the productive division of labour already emerging in REE_assembly.

---

## 10. One-sentence summary

REE_assembly should preserve complementary processing modes — broad synthesis, local adjudication, design generation, evidence gating, experimental prosecution, and integration — because reliable project cognition depends on their balance rather than on any single mode dominating the governance machinery.
