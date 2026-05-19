---
title: Founder ontology (E1 / E2 / E3)
parent: Architecture
nav_order: 2
---

# Founder ontology -- how to read E1, E2, and E3

**Status:** plan-of-record for *intent* (how the architecture was meant to be read).
**Authority for behaviour:** [claims registry](../claims/claims.yaml) and linked
experiments. Where this doc and a claim conflict, the claim wins until governance
updates it.

**Audience:** contributors, reviewers, and agents working on REE. Read this
**before** proposing "standard" ML stacks (world model + policy + critic, monolithic
transformer planner, etc.).

---

## 1. Why this document exists

REE's three-engine split (E1 / E2 / E3) was defined from a **biology-first**
picture of cortex and cerebellum, plus a separate **commitment and comparison**
loop -- not from default deep-RL or LLM-agent templates.

Early sessions often **re-expressed** that picture in familiar AI terms (extra
planners, trajectory generators in the wrong module, "E2 as long-horizon world
model"). Much of the [claims index](../claims/claims.yaml) and repeated review
cycles exist to **record the founder reading** and demote drift.

This page is the short, stable map between:

- **Founder concepts** (what you meant),
- **REE names** (modules and claim subjects),
- **Biology analogs** (functional, not homology).

---

## 2. The three functions in founder terms

### E1 -- perception-association matrix (cerebral base)

| | |
|--|--|
| **Founder concept** | The **base perception-association matrix**: slow integration of "what is going on" in the world and self. Not optimized for fast action; holds context when movement and attention pause. |
| **REE names** | `E1`, `e1.*`, `predictors/e1_deep.py`, L-space / `z_world`, ARC-001 (persistent predictive substrate). |
| **Biology analog** | **Cerebrum** -- especially deep and associational cortex (slow predictive tissue), not "a chat model in a box." |
| **Not** | A separate ethics module, a fast policy, or the module that commits action. |

Goals, values, and "what matters" live in the **cerebral world** in biology: accidents
of structure that **specialize repeatedly**. In REE they are **distributed** (PFC,
vmPFC, residue terrain, hippocampal valence maps, ghost-goal cue system) -- not a
single `goals/` package. That distribution is intentional.

### E2 -- fast forward predictor (cortical edge + cerebellum)

| | |
|--|--|
| **Founder concept** | The **fast forward predictor**: given current state and intended action, what happens next at short horizon? Efference-copy style bridging so perception and action stay coupled. |
| **REE names** | `E2`, `e2.*`, `predictors/e2_fast.py`, ARC-002 (fast forward predictor). |
| **Biology analog** | **Outer cortical fast inference** plus **cerebellar forward model** (state + action -> next state, ~one step). Literature in the registry often cites cerebellum explicitly (MECH-057, MECH-231). |
| **Not** | The deep world model (that is E1), the multi-step rollout engine (hippocampus / E3 complex), or a long-horizon planner. Experiments such as EXQ-132 / EXQ-212 reinforce **short** E2 horizon vs E1. |

Historical **implementation drift:** E2 was sometimes wired to do **hippocampal**
trajectory-proposal work under the E2 label. Claims and refactors treat that as
**misplacement**, not as the founder design (see MECH-057 note on E2 vs hippocampal
module).

### E3 -- commitment and comparison (basal ganglia system)

| | |
|--|--|
| **Founder concept** | Hard to name at first; settled as **commitment and comparison**: perception and action as a **giant experiment** -- generate candidates, compare predicted vs actual / harm vs goal, **commit or withhold**. |
| **REE names** | `E3`, `e3.*`, `predictors/e3_selector.py`, comparator / harm streams, `policy/`, `heartbeat/beta_gate.py`, basal_ganglia.* claims, three-loop gating (MECH-057 family). |
| **Biology analog** | **Basal ganglia** and related gating (plus thalamic routing): which candidate gets access to execution and cognitive resources, not "another cerebellum." |
| **Not** | A third big predictive world model parallel to E1. |

E3 is the **arbiter of the experiment**, not the slow matrix and not the one-step
forward model.

---

## 3. One diagram (founder reading)

```text
  CEREBRAL WORLD (slow + goals + context)
  +------------------------------------------+
  |  E1  perception-association matrix       |
  |      + goal / value specializations      |
  |        (PFC, vmPFC, terrain, cues, ...)  |
  +------------------+-----------------------+
                     | priors / state
                     v
  FAST FORWARD       |         CANDIDATE EXPERIMENTS
  +----------------+ |  +---------------------------+
  | E2  next-state | |  | Hippocampus: rollouts,     |
  |     (cerebellar| |  | paths, terrain (partner)  |
  |      + fast    | |  +-------------+-------------+
  |      cortical) | |                |
  +--------+-------+ |                v
           |         |         +------+------+
           +---------+-------->| E3 / BG     |
                               | compare &   |
                               | COMMIT      |
                               +-------------+
```

**Hippocampus** is a **partner** for explicit multi-step candidates and path memory;
it is not "E2 renamed." **Control plane** modulates *when* updates and modes run;
it is not a fourth lobe.

---

## 4. Drift catalog (what to push back on)

| Drift pattern | Typical AI default | Founder / claims correction |
|---------------|-------------------|---------------------------|
| "E2 plans the future" | Planner head, long rollout in E2 | E2 = short forward; rollouts in hippocampal / E3 complex |
| "E3 is another predictor" | Critic or value network only | E3 = commitment + comparison + gating (BG analog) |
| "Goals are a module" | `GoalEnv`, reward wrapper | Goals cerebral, distributed across claims |
| "One world model does all" | Single transformer | E1/E2/E3 irreducible (ARC-035 family); typed error targets |
| Brain map shows E1-E3 as side boxes | Engineering strip only | **v1.1 intent:** E1 on cerebrum, E2 on cerebellum, E3/BG on gate (see [brain_map.md](brain_map.md)) |

When an agent proposes architecture, ask: **does this preserve the experiment loop
(compare then commit) and the E1/E2 split (slow matrix vs fast forward)?**

---

## 5. Mapping table (quick reference)

| Founder | Primary REE artifacts | Claim subjects (examples) | Biology (functional) |
|---------|----------------------|---------------------------|----------------------|
| Perception-association matrix | `e1_deep`, L-space, `z_world` | `e1.*`, `latent_stack.*`, `architecture.*` | Cerebrum / deep cortex |
| Fast forward | `e2_fast`, action-object kernels | `e2.*`, `e1_e2.*` | Cerebellum + fast cortical edge |
| Commitment & comparison | `e3_selector`, policy, beta gate, comparator | `e3.*`, `basal_ganglia.*`, `commitment.*`, `harm_stream.*` | Basal ganglia, striatal gating |
| Rollouts & path memory | `hippocampal/` | `hippocampus.*`, `hippocampal.*` | Hippocampal formation |
| Goals (distributed) | PFC, residue, ghost goals | `pfc.*`, `vmPFC.*`, `goal.*`, `hippocampus.*` | Frontal + medial temporal specializations |

---

## 6. For agents and reviewers

1. **Default frame:** cerebrum (E1 + goal tissue) -> fast forward (E2) -> candidate
   experiments (hippocampus) -> commit (E3/BG).
2. **Before adding a module:** say which founder function it serves; do not duplicate
   E2 as planner or E3 as world model without a claim.
3. **Brain map / diagrams:** use [founder ontology](founder_ontology.md) for layout
   intent; use `/api/brain-map` for live claim/evidence overlays.
4. **Promoting or demoting claims:** cite experiments; founder ontology does not
   override `evidence_direction` on manifests.

---

## 7. Related docs

- [E1](e1.md), [E2](e2.md), [E3](e3.md) -- interface contracts
- [Brain map](brain_map.md) -- visualization and region YAML
- [Hippocampal systems](hippocampal_systems.md) -- rollouts (not E2)
- [Rule apprehension / BG](rule_apprehension_layer.md) -- commitment layer
- [Architecture overview](overview.md) -- public three-engine introduction

---

*Recorded 2026-05-19 from founder review and brain-map discussion. Update via
governance when intent changes; do not let session drift silently rewrite this file.*
