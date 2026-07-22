# Bounded Knowledge Artefact Optimisation for REE Assembly

Status: processed

Processed in:
- `evidence/planning/thought_intake_2026-07-19_bounded_knowledge_artifact_optimisation_assembly.md` (structured intake, already-owned split, routing)
- `docs/claims/claims.yaml` -- GOV-HELDOUT-1 (held-out validation for Assembly workflow and rule changes), GOV-STRAT-1 (artefact-layer authority stratification), GOV-REJECT-1 (rejected-edit memory with reconsideration conditions), GOV-META-1 (meta-optimisation subordinate to provenance, honesty and human authority; carries the kill criteria)

REE ASSEMBLY half of the SkillOpt source, registered as `claim_type: governance_rule` per the INV-077 / GOV-PROC-1 / GOV-CEIL-1 / SD-062 precedent -- NO MECH-* minted. The REE-cognition half is `2026-07-19_conservative_skill_refinement_and_multi_timescale_learning.md`; keep separate (GOV-ANALOGY-1). Intake candidate 4 (skill-registry metadata) deliberately NOT registered -- routed straight to implementation. Self-reference hazard recorded in the intake: the proposed pilot target is the intake workflow itself, so that intake is not held-out evidence about intake quality.

---

**Date:** 2026-07-19  
**Status:** thought_intake / assembly_design_seed  
**Source:** Microsoft SkillOpt — Executive Strategy for Self-Evolving Agent Skills  
**Scope:** REE Assembly scientific-development and governance machinery. This document is explicitly separate from REE cognitive architecture.

---

## Core thought

SkillOpt may be more directly useful to REE Assembly than to REE itself.

REE Assembly already works through external, editable knowledge artefacts such as:

- thought intakes;
- claims;
- literature reviews;
- architecture notes;
- experiment protocols;
- failure autopsies;
- prompts and workflow instructions;
- governance decisions;
- implementation and routing notes.

These artefacts can be treated as governed objects that are iteratively improved through evidence, review, bounded revision, and validation.

The important analogy is not that claims or thought intakes are "weights." They are governed knowledge artefacts with provenance, scope, authority, and consequences.

---

## Candidate optimisation loop

```text
source material or operational problem
        ↓
candidate knowledge artefact or workflow change
        ↓
reflection and conflict search
        ↓
bounded edit proposal
        ↓
validation against explicit criteria
        ↓
accept / reject / revise
        ↓
promotion with provenance
        ↓
monitor downstream consequences
```

This closely resembles existing REE Assembly practice, but SkillOpt suggests ways to make the loop more explicit, measurable, and self-improving.

---

## Candidate Assembly principles

### 1. Bounded edits by default

Prefer small, attributable changes over broad rewrites.

Edit operations may include:

```text
add
remove
replace
split
merge
reclassify
supersede
cross-reference
```

Each edit should state what problem it is intended to solve.

### 2. Validation before promotion

A change should not survive only because it improves the artefact that generated it.

Possible validation dimensions:

- consistency with axioms and existing organisational principles;
- compatibility with current architecture;
- evidence quality;
- performance on held-out examples or later governance cases;
- preservation of provenance and uncertainty;
- absence of silent scope expansion;
- usefulness to implementation or experiment selection;
- resistance to reviewer-specific overfitting.

### 3. Held-out review

Some evaluation material should not participate in generating the candidate edit.

Examples:

- reserve papers or cases for later validation;
- use a separate reviewer role to inspect the final artefact;
- test prompts against unseen repository tasks;
- evaluate workflows on later governance cycles rather than the cycle that produced them.

### 4. Rejected-edit memory

Rejected changes should be retained with:

- the proposed edit;
- why it was proposed;
- why it was rejected;
- evidence considered;
- conditions under which reconsideration would be appropriate.

This prevents repeated rediscovery and preserves informative failure.

### 5. Different update rates for different artefacts

Not every layer should change equally quickly.

```text
prompts and local workflow hints: relatively fast
thought-intake structure: moderate
claims and mechanism status: evidence-gated
architecture commitments: slow
organisational principles: very slow
axioms: exceptional
```

This is an Assembly governance hierarchy, not a description of REE cognition.

### 6. Optimise workflows, not only documents

Potential optimisation targets include:

- literature-search strategy;
- source-tracing workflow;
- reviewer selection;
- repository-routing decisions;
- thought-intake templates;
- conflict adjudication;
- failure-autopsy prompts;
- experiment proposal quality;
- claim-promotion and demotion procedures;
- handoff between human and agent reviewers.

### 7. Meta-optimisation under governance

REE Assembly may learn which workflow or skill combination works best for a class of task.

However, meta-optimisation must remain subordinate to provenance, epistemic honesty, governance boundaries, and explicit human authority.

---

## Possible SkillOpt-inspired components

### Assembly skill registry

A registry of reusable scientific and engineering workflows, each with:

- intended use;
- inputs and outputs;
- prerequisites;
- known failure modes;
- evaluation history;
- version and provenance;
- confidence and scope.

### Workflow selector

Selects a workflow bundle based on task type, for example:

```text
paper tracing
thought digestion
architecture comparison
claims conflict review
experiment design
failure autopsy
implementation review
```

### Bounded editor

Produces explicit patch-like changes rather than silently rewriting whole artefacts.

### Validation harness

Evaluates candidate workflow or document changes against historical and held-out Assembly tasks.

### Rejection buffer

Stores failed edits and workflow choices with reasons and reconsideration conditions.

### Slow-promotion gate

Requires repeated evidence before changes reach higher-authority layers.

---

## Candidate pilot

A low-risk first pilot could optimise one reusable Assembly skill rather than modifying architecture or governance directly.

Example target:

```text
thought-intake generation and review workflow
```

Pilot steps:

1. Select a small historical set of completed thought-intake conversations.
2. Define quality criteria: source fidelity, separation of REE from REE Assembly, repo grounding, novelty discipline, actionable research questions, and absence of scope creep.
3. Run the current workflow on a training subset.
4. Propose bounded changes to the workflow instructions.
5. Test on held-out thought-intake cases.
6. Retain only changes that improve quality without increasing unsupported claims or process burden.
7. Preserve rejected edits and reasons.

---

## Metrics

Possible measures include:

- factual and source accuracy;
- repo-grounding rate;
- unsupported-novelty rate;
- distinction between REE and REE Assembly;
- duplicate-claim creation rate;
- reviewer correction burden;
- time or steps to a usable artefact;
- downstream usefulness to claims, experiments, or implementation;
- frequency of later supersession caused by avoidable intake defects.

No single metric should become the optimiser's sole target.

---

## Risks

- Optimising for easily measured quality may reduce originality or conceptual depth.
- A workflow may overfit to historical REE tasks.
- Automated edits may erase authorship distinctions or uncertainty.
- Faster production can increase low-quality artefact volume.
- Meta-optimisation may silently shift governance authority.
- Treating knowledge artefacts as weights may obscure meaning, provenance, and responsibility.
- Reviewer selection could create epistemic monoculture.

---

## Kill criteria

Demote or stop the approach if it:

- produces no held-out improvement;
- increases unsupported claims or duplicate artefacts;
- makes provenance harder to inspect;
- optimises superficial formatting over scientific quality;
- increases governance burden more than it reduces it;
- repeatedly proposes changes already rejected for known reasons;
- weakens human review or authority boundaries.

---

## Current working claim

REE Assembly may benefit from SkillOpt-like bounded optimisation of its external knowledge artefacts and reusable workflows, provided that edits remain small, validation is held out where possible, rejected changes are preserved, higher-authority layers update slowly, and optimisation remains subordinate to provenance and governance.
