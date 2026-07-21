# DLIF Next Action: Claims-Index Pilot Plan

Status: processed
Processed in:
- `docs/claims/claims.yaml` (plan doc for the claims-index pilot whose RESULT is `2026-06-20_dlif_claims_index_pilot_result.md`; that result is cited in SD-062 and Q-079 `sources`. Discharged via its own result, not cited directly.)


**Date:** 2026-06-20  
**Status:** next_action_plan / pilot_seed  
**Scope:** Dynamic Latent Information Field (DLIF), REE_assembly claims index, thought-intake governance  
**Source:** follow-up after DLIF critical review and learning capture  
**Primary benchmark note:** preserve the REE-v3 strict green-board target of **Sunday 19 July 2026**. This pilot is useful only if it remains lightweight and does not draw effort away from current REE-v3 experiments.

---

## Purpose

This document converts the DLIF critical review into a small next-action plan.

The aim is to test whether DLIF can produce useful claims-index outputs without building a new agent environment or making DLIF a REE-v3 dependency.

---

## Current best framing

DLIF should not claim novelty merely because it is field-like.

Field-like cognition has strong ancestors:

- Kurt Lewin's psychological field theory / life space;
- Dynamic Field Theory in embodied cognition and cognitive development;
- neural field theory and continuous attractor models;
- decision field theory;
- active inference and dynamical cognition;
- energy / attractor landscape models.

DLIF's possible usefulness is narrower:

```text
DLIF is useful if it provides a minimal computable bridge between field-native uncertainty, graph/claim projection, latent-structure discovery, granularity control, and residue-preserving governance.
```

---

## Why claims-index first

A claims-index pilot is safer and more useful than an agent-world pilot right now.

Reasons:

1. REE_assembly already has thought intakes, claims, evidence, conflicts, roadmap stage, and implementation dependencies.
2. The pilot can be documentation / analysis only at first.
3. It can generate immediately useful outputs: hidden assumptions, conflict / residue reports, scale recommendations, and next-experiment suggestions.
4. It avoids expanding REE-v3 implementation scope before strict green-board.
5. It tests whether DLIF improves governance before claiming architectural necessity.

---

## Pilot name

```text
Claims-Index DLIF Pilot
```

Possible later file/folder:

```text
docs/research/dlif/claims_index_pilot.md
```

Do not create a large new folder until the pilot proves useful.

---

## Minimal input set

Use a tiny curated sample:

```text
10-30 thought-intake documents
selected claims from docs/claims/claims.yaml if available
known conflicts / unresolved questions
roadmap tags or v3/v4/v5 relevance
experiment dependencies
```

The pilot should not begin by ingesting everything.

---

## Minimal field schema

Each candidate claim / thought / unresolved tension receives field-like values:

```text
belief
uncertainty
salience
coherence_cost
residue
scale
implementation_dependency
roadmap_relevance
```

Keep this deliberately small.

Possible scales:

```text
fragment
claim
mechanism
architecture_principle
experiment
roadmap
research_line
```

---

## Projection outputs

The pilot should output:

```text
projected claim graph
hidden assumption list
conflict / residue report
scale recommendation
next experiment recommendation
```

The value of DLIF is judged by these outputs, not by how elegant the field description is.

---

## First manual workflow

Before coding, run one manual pass.

1. Select 10-30 DLIF-related notes / claims.
2. Assign the minimal field values manually.
3. Project a claim graph.
4. Identify hidden assumptions.
5. Identify unresolved residue / conflict.
6. Recommend claim split / merge / defer / experiment.
7. Compare against ordinary reading of the same documents.

If manual DLIF does not produce better insight than ordinary reading, do not code it.

---

## Baseline comparison

Compare against:

```text
ordinary tag list
ordinary claim graph
scalar confidence score
human summary without field values
```

DLIF should only continue if it improves at least one of:

```text
hidden-assumption detection
conflict preservation
scale selection
next-experiment recommendation
claim split / merge quality
residue tracking
```

---

## Kill criteria

Demote or narrow DLIF if:

1. It performs no better than an ordinary claim graph.
2. Residue predicts nothing beyond salience or uncertainty.
3. Scale-shift adds vocabulary without improving decisions.
4. Projection loss cannot be described or reviewed.
5. Human review finds the outputs less clear than the original documents.
6. It creates scope creep for REE-v3.

---

## Useful near-term outputs

If the manual pilot works, create:

```text
DLIF_FIELD_SCHEMA.md
DLIF_PROJECTION_SCHEMA.md
DLIF_CLAIMS_INDEX_PILOT.md
```

Only then consider a script.

Possible script later:

```text
scripts/dlif_claims_index_pilot.py
```

But no script is needed until the manual version proves useful.

---

## Research anchors to preserve

The literature drill should include ancestors and distinguish DLIF from them.

Important anchor questions:

1. What does Dynamic Field Theory already solve?
2. What do neural fields and continuous attractors already solve?
3. What does decision field theory already solve?
4. What does active inference already solve?
5. What do information geometry and information bottleneck already solve?
6. What remains distinct about DLIF?

Current candidate distinctiveness:

```text
graph / claim projection
latent assumption discovery
granularity control
residue / non-erasure
claims-index governance
next-experiment recommendation
```

---

## Do / don't before REE-v3 strict green-board

### Do

```text
use DLIF to clarify thought intake
use DLIF to identify hidden assumptions
use DLIF to avoid premature graph-freezing
use DLIF to preserve unresolved conflict
use DLIF to suggest lightweight next experiments
```

### Don't

```text
rewrite REE-v3 around DLIF
create a large standalone repo yet
turn DLIF into a new benchmark dependency
make continuous-field mathematics a prerequisite
add major code before manual usefulness is shown
```

---

## Immediate next step

Perform a manual Claims-Index DLIF pass over the existing DLIF thought cluster:

```text
structured uncertainty layer for REE agent design
claims index as structured uncertainty graph
brain-native hybrid inference objects
dynamic latent-scale inference field capture
dynamic latent-scale inference field research map
latent information fields: graphs as projections
minimal formal specification
critical review and learning
```

Output:

```text
projected claim graph
hidden assumptions
conflict / residue report
scale recommendations
next action recommendation
```

This is the lowest-cost way to find out if DLIF is useful.
