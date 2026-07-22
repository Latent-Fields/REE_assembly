# Conservative Skill Refinement and Multi-Timescale Learning in REE

Status: processed

Processed in:
- `evidence/planning/thought_intake_2026-07-19_conservative_skill_refinement_multi_timescale_learning.md` (structured intake, already-owned split, routing)
- `docs/claims/claims.yaml` -- MECH-471 (competence updates need the bounded/provenanced/rollback discipline consolidation already has), MECH-472 (held-out context distinguishes acquisition from memorisation), MECH-473 (rejected-adaptation memory -- v4, DO NOT build in V3), MECH-474 (learning-regime meta-selection, narrow form), INV-093 (skill optimisation must not trade harm sensitivity for competence)
- `evidence/planning/manual_proposals.v1.json` -- EXP-0399 (local-update interference test), EXP-0400 (held-out-context acquisition vs memorisation), EXP-0401 (learning-regime meta-selection, narrow)

REE COGNITIVE ARCHITECTURE half of the SkillOpt source. The Assembly half is `2026-07-19_bounded_knowledge_artifact_optimisation_for_ree_assembly.md`; the split is deliberate and is preserved in the registry (see GOV-ANALOGY-1). INV-093 is registered as a SIBLING of INV-092 (2026-07-12 distractor thought).

---

**Date:** 2026-07-19  
**Status:** thought_intake / literature_seed  
**Source:** Microsoft SkillOpt — Executive Strategy for Self-Evolving Agent Skills  
**Scope:** REE cognitive architecture only. REE Assembly implications are handled separately.

---

## Core thought

SkillOpt is primarily a system for optimising externally represented agent skills through rollout, reflection, bounded edits, validation, and retention of successful revisions.

REE should not be assumed to require literal optimisation of text-based skill documents. Its internal learning architecture is richer and more deeply integrated with prediction, action, harm, goals, residue, and offline consolidation.

The transferable value lies instead in several organisational principles:

- skill refinement should be bounded rather than globally rewriting behaviour;
- updates should be validated before becoming durable;
- successful competencies should be protected against catastrophic overwrite;
- failed revisions should leave informative traces rather than disappear;
- learning should occur at multiple characteristic timescales;
- slow structural change should be separated from fast behavioural adaptation;
- meta-learning may govern which learning process is used and when.

---

## REE-facing interpretation

A skill in REE is not merely an instruction document. It may be distributed across:

- action objects;
- learned affordances;
- predictive models;
- hippocampal trajectories;
- goal-conditioned policies;
- rule-state persistence;
- context-sensitive control settings;
- residue-shaped avoidance and repair tendencies.

Accordingly, SkillOpt should be treated as a neighbouring implementation strategy rather than a direct architectural template.

The useful question is:

> How should REE refine behavioural competence without erasing previously viable structure or allowing one recent success to rewrite the whole agent?

---

## Candidate organisational principles

### 1. Bounded refinement

Skill change should usually be local, attributable, and reversible enough to inspect.

### 2. Validation before promotion

A new behaviour should not become durable merely because it improves one rollout. It should survive comparison across contexts, perturbations, and held-out situations.

### 3. Protection against catastrophic overwrite

Fast adaptation should not silently destroy slow-acquired competencies, commitments, harm sensitivity, or residue.

### 4. Multiple learning rates

REE likely requires at least:

```text
fast situational adaptation
medium-term skill refinement
slow schema and structural learning
very slow architectural consolidation
```

### 5. Rejected-change memory

A failed adaptation should remain available as evidence about what was tried, why it failed, and under what conditions it might later become useful.

### 6. Meta-selection of learning strategy

The system may need to choose among:

```text
practice
exploration
imitation
counterfactual simulation
offline consolidation
rule apprehension
language-mediated scaffolding
```

rather than applying one learning rule universally.

---

## Relation to current REE design

These principles appear broadly compatible with existing REE commitments:

- asynchronous multi-rate learning and control;
- separation of fast prediction from slower persistent modelling;
- offline integration;
- event- and mode-conditioned plasticity;
- preservation of residue;
- anti-collapse through partially independent control systems;
- behavioural validation across repeated periods and contexts.

The likely contribution of SkillOpt is therefore external convergence and a compact optimisation vocabulary, not a new foundational REE mechanism.

---

## Possible future tests

1. Can REE improve a competence through local updates without degrading unrelated skills?
2. Do held-out contexts distinguish genuine skill acquisition from task memorisation?
3. Does preserving rejected adaptations improve later recovery or transfer?
4. Which updates should occur online, during replay, or during offline consolidation?
5. Can the control plane select the appropriate learning timescale and mechanism?
6. How should residue constrain skill optimisation when a behaviour is effective but harmful?

---

## Cautions

- Text-space skill optimisation is not equivalent to embodied cognitive learning.
- Performance gain is not sufficient evidence of viability or ethical adequacy.
- A validated skill may still conflict with commitments, harm constraints, or broader goals.
- Meta-learning itself requires governance so that it cannot optimise away protected structures.

---

## Current working claim

REE should refine skills through conservative, multi-timescale, behaviourally validated updates that preserve established competence, protected constraints, and consequence history. SkillOpt provides a useful neighbouring example of bounded optimisation, but not a direct model of REE cognition.
