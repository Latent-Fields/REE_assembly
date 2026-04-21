# Scientist-Agent Principle and Developmental Ordering

**Registered:** 2026-04-21
**Cluster:** ARC-059, MECH-275, MECH-276, MECH-277, MECH-278
**Sister cluster:** MECH-269/270/271 (anchor selection), MECH-272/273/274 (state-gated routing + sleep aggregation)

## Where this came from

The MECH-272/273/274 cluster (registered 2026-04-21 morning) established that:

- Sleep and waking have distinct informational jobs (MECH-272): waking = decision-support using existing schemas, sleep = full-Bayesian schema revision.
- The self-model has a waking half (single-episode SD-003 attribution via E2 counterfactuals) and a sleep half (MECH-273 full-Bayesian aggregation of those attributions across episodes, routed via MECH-271's anchored channel to E1/SD-033a).
- The same pattern extends to other-attribution in V4 (MECH-274).

A natural next question arose: is MECH-273's aggregation pattern specific to self-attribution, or is it a general mechanism? Initial instinct: generalise — attribution-tidying of the sense of self presumably works on many things in the world.

But the naive generalisation has a problem. MECH-273 works because SD-003 provides a strong attribution signal to aggregate over: a counterfactual-backed causal signature derived from E2's comparison of `E2(z, a_actual)` vs `E2(z, a_cf)`. The attribution is not mere correlation — it is a deliberately produced contrast that the agent had access to a counterfactual for. Full-Bayesian aggregation over noisy arbitrary correlations would not yield the same thing.

The generalisation has to carry the counterfactual-backed attribution forward, not just the aggregation step. That requires the agent to behave **like a scientist**: generate hypotheses, perform deliberate interventions to test them, observe consequences, then aggregate the attributions during sleep.

This cluster formalises that architecture and the developmental ordering it requires.

## Cluster members

### ARC-059 — Three-stage developmental ordering

Refines ARC-019 (generic staged curriculum). Specifies the ordering:

1. **Stage 1 — Self as object-of-study.** The agent must first discover its own action space. It does not initially know which sensory changes covary with its motor output vs external dynamics. Motor babbling / action-space discovery (MECH-277) closes this loop: the agent acts, observes consequences, and builds a model of what its own actions can do. This is where SD-003 becomes possible — the counterfactual requires knowing which actions are "self-initiated" candidates.

2. **Stage 2 — Objects as special patterns in the world.** Once the agent can attribute change to self vs world, it can decompose the world into stable patterns (objects) via experimental action (MECH-278). Moving an object and watching it move together, pushing and feeling resistance, occluding and re-revealing — these are the interventions that produce object-schemas. The object is the set of features that behave causally together under experimental perturbation.

3. **Stage 3 — Others as special objects.** Other agents are recognised as a subclass of objects whose internal dynamics resist the simple interventional signature — they have their own policies, their own counterfactuals. V4's fast-empathy and other-modelling (ARC-010, MECH-274) are the stage-3 operations, built on top of stages 1 and 2.

The ordering is not decorative. Without a self-model, objects cannot be distinguished from self-produced sensory change. Without object-schemas, other-agents cannot be recognised as different kinds of objects.

### MECH-275 — General sleep-phase Bayesian aggregation

Extracts the abstract mechanism of MECH-273/274 to its general form: sleep phases run full-Bayesian aggregation over multi-episode evidence whose waking-phase form is counterfactual-backed attribution (MECH-276 output). Input is not arbitrary correlation — it is attribution contrast produced by deliberate intervention. Output is schema revision: updated priors, new buckets for experiences that did not fit, revised causal graphs.

MECH-273 (self-model aggregation) is the stage-1 specialisation. MECH-274 (other-model aggregation, V4) is the stage-3 specialisation. Stage-2 object-schema revision is a further specialisation under this mechanism.

INV-049 (offline phases are a mathematical necessity for model-building agents) is operationalised by MECH-275: what sleep is mathematically necessary *for* is the aggregation of counterfactual-backed attributions across episodes.

### MECH-276 — Scientist-agent principle (waking-phase counterfactual attribution via intervention)

The waking-phase mechanism that feeds MECH-275. The agent generates hypotheses, selects actions that will produce informative contrast under those hypotheses, executes the actions, observes the outcomes, and computes the counterfactual-backed attribution. The probe channel of MECH-269 is the proposer-side hypothesis generator (low-V / high-PE regions are where probes are seeded); MECH-276 is the whole-agent closure of that loop — the agent actually performs the consequential action and registers the outcome.

Three specialisation levels correspond to the three developmental stages:
- Stage 1: motor experimentation (MECH-277) — hypothesis about own action space.
- Stage 2: experimental action on objects (MECH-278) — hypothesis about world's object decomposition.
- Stage 3: social intervention (V4, parallel to MECH-278 for other-agents) — hypothesis about another agent's dispositions.

Without MECH-276, sleep-phase aggregation (MECH-275) has nothing coherent to aggregate over. The agent's waking phase must generate the structured attribution signal.

### MECH-277 — Action-space discovery via motor experimentation (stage 1)

First-stage specialisation of MECH-276. The agent does not arrive with a model of its own action space; it discovers it via motor babbling — performing motor acts and observing which sensory changes covary with them. The output of this stage is the substrate SD-003 requires: a set of actions the agent has reason to believe are self-initiated and for which it has counterfactual expectations.

Prerequisite for SD-003. In developmental ordering, MECH-277 must run meaningfully before SD-003's single-episode counterfactual attribution is sensible. An agent that has not yet explored its action space cannot produce well-formed counterfactuals because the space of `a_cf` is not yet known to it.

### MECH-278 — Object-schema formation via experimental action (stage 2)

Second-stage specialisation of MECH-276. Once the agent can distinguish self-produced from world-produced sensory change (stage 1 complete), it can perform experimental actions on the world and observe which features behave causally together under perturbation. An object is the stable bundle: pushing here moves these features together, occluding this feature hides that cluster, etc.

**V3 architectural note — possible shortcut:** V3's z_world latent is currently provided by the encoder as a pre-specified split from z_self (SD-005). This is an engineering convenience. It effectively provides the object/world decomposition without the agent earning it via stage 2. Whether this matters for V3 validity is an open question — V3 is not claiming to demonstrate developmental ordering, only the mature architecture. But the architectural shortcut should be noted: V3's z_world is a gift, not a construction. V4 (or a V3 developmental sub-experiment) should test whether experimental action can produce an object-schema decomposition that matches the engineered z_world, or whether the engineered version carries assumptions the agent would not make on its own.

## Resonances with existing claims

- **ARC-019** (staged developmental curriculum, provisional): generic ancestor. ARC-059 refines and operationalises.
- **SD-003** (counterfactual self-attribution): the stage-1 closure of MECH-276 for self — it is the output of MECH-276 Stage 1 applied to self-attribution, aggregated by MECH-273.
- **INV-049** (offline phases mathematically necessary): the what-for is specified by MECH-275.
- **MECH-269** (probe channel, hypothesis generator): the proposer-side mechanism that seeds MECH-276's hypotheses. The agent-level closure of "probe → consequential action → observed outcome → attribution" is MECH-276.
- **MECH-271** (routing signature): anchored routing carries MECH-275's aggregated output to consolidation consumers.
- **MECH-272** (state-gated routing): specifies which regime MECH-275 runs in (sleep-dominant probe) vs which regime MECH-276 runs in (waking).
- **MECH-273** (self-model sleep aggregation): stage-1 specialisation of MECH-275.
- **MECH-274** (other-model sleep aggregation, V4): stage-3 specialisation of MECH-275.
- **ARC-010** (social/mirror modelling, V4): stage-3 substrate.
- **SD-004** (action objects as hippocampal map backbone): supports MECH-278 — object-schema formation uses action-object pairings as the granular building block.
- **SD-005** (z_self / z_world split): currently engineered in V3; MECH-278 describes what a developmental construction of this split would look like.

## V3 experimental implications

- **Validation of MECH-276 (stage 1)**: an experiment that seeds a confuser — sensory change that is not self-caused but correlates with action — and tests whether the agent's SD-003 attribution corrects over episodes. If MECH-276 closure is working (hypothesis → intervention → counterfactual), the agent should isolate the confuser; if the architecture collapses to bare SD-003 without the intervention loop, it will not.
- **Validation of MECH-275 (sleep aggregation)**: natural pair for the MECH-273 experiment (seed a spurious self-attribution, test whether sleep aggregation corrects it). MECH-275 is the general form — the same experiment template, parameterised over which attribution is being aggregated, should test the generalisation.
- **V3 stage-2 test (optional, flagged in MECH-278 notes)**: ablate the engineered z_world and test whether experimental action can reconstruct an object-schema decomposition. This is likely out of V3 scope but is the natural V4 experiment.

## Why the cluster registers now

The conversation that produced MECH-272/273/274 made the naive generalisation salient: if sleep aggregates self-attributions, it should aggregate many attributions. User flagged the concern that this needs consequential-reasoning input — the aggregation is only coherent if the waking-phase feedstock is counterfactual-backed. That correction pushed the cluster into existence:

- MECH-275 is the *general* aggregation mechanism MECH-273/274 specialise from.
- MECH-276 is the *scientist-agent* principle that produces the counterfactual-backed feedstock MECH-275 needs.
- ARC-059 is the *developmental ordering* that specifies when each specialisation of MECH-276 becomes possible.
- MECH-277 and MECH-278 are the stage-1 and stage-2 specialisations of MECH-276.

Registering the cluster now reserves the IDs, fixes the architectural relationships, and flags the V3 z_world shortcut for later investigation.

## How to apply

- Treat MECH-273 and MECH-274 as specialisations of MECH-275, not freestanding claims. When MECH-275 gets V3 evidence, MECH-273 gains lineage evidence automatically; the reverse is not true.
- Do not try to validate MECH-276 with a correlational experiment — the whole point is that correlational aggregation is insufficient. MECH-276 validation requires an intervention-structured task.
- V3 experiments that use z_world directly are implicitly assuming stage-2 complete. This is fine for V3 purposes but should be tagged in experiment notes where relevant.
- MECH-277 is a prerequisite for SD-003. In practice V3 hand-wires action knowledge into the agent, so MECH-277 is not actively tested — but SD-003 experiments should note the assumption.
- MECH-278's V4 developmental sub-experiment (experimental action reconstructing z_world) is the clean test for the whole ordering. Reserve that as a flagship V4 experiment.
