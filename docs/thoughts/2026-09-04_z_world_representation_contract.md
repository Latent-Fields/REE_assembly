# `z_world` Representation Contract: Preserve What the Organism Needs to Know

Status: design thought / falsifiable architecture hypothesis  
Date: 2026-09-04  
Parent thought: `2026-09-04_from_regulation_to_knowledge_organizing_subjective_experience.md`

## Purpose

The current `z_world` problem should not be approached first as a demand to discover the one correct compact representation of an external scene. The narrower engineering question is:

> What information must survive the observation → `z_world` boundary so that the rest of REE can learn a coherent, predictive, actionable world without having the ontology hand-written for it?

The regulation-first hypothesis suggests a representation contract rather than a fixed semantic schema.

## Proposed contract

A useful `z_world` representation should preserve, or make recoverable through its dynamics, distinctions that are consequential to the organism across time.

At minimum this includes information sufficient to differentiate:

- **consequence:** harmful, beneficial, neutral or uncertain effects on the organism;
- **opportunity and threat:** not merely where objects are, but which future interactions they afford;
- **controllability:** outcomes the organism can influence versus outcomes it cannot;
- **agency:** self-caused, potentially self-caused, and externally caused changes;
- **persistence:** what remains the same entity, relation or source across changing observations;
- **internal consequence:** changes in organism state that may not be visible in the external scene;
- **uncertainty and ambiguity:** cases where multiple causal or world explanations remain live;
- **temporal relation:** enough structure to distinguish transient coincidence from stable predictive regularity.

These are proposed organizing dimensions, not labels that every latent coordinate must explicitly encode.

## What the contract does *not* require

It does not require a hand-coded mature ontology of resources, predators, goals, agents, emotions or moral categories. Nor does it require `z_world` to be interpretable one dimension at a time.

The contract is satisfied if downstream systems can reliably recover the distinctions needed for prediction, counterfactual comparison, memory, planning and regulation, including when surface observations change.

## Why this matters at the observation boundary

Information destroyed before E1/E2 cannot be reconstructed by better downstream reasoning. A representation can therefore be excellent at observation reconstruction while still being unsuitable as the organism's world substrate.

This gives a concrete interpretation of failures in which visually or statistically similar situations require different actions: the encoder may be collapsing distinctions that are small perceptually but large regulatorily.

Auxiliary supervision such as directional resource information, where present in the live implementation, should therefore be interpreted as a **probe of the representation contract**, not proof that the correct ontology is a resource-vector ontology.

## Deep constraints versus temporary training scaffolds

A useful distinction is needed between:

1. **organizing constraints** — information classes the organism repeatedly needs to preserve; and
2. **training scaffolds** — labels or auxiliary heads used temporarily to test whether the representation can learn those distinctions.

A successful scaffold should be removable without destroying the acquired organization. If performance depends permanently on privileged labels at inference, the experiment has demonstrated supervision dependence rather than emergence of a useful world representation.

## Developmental requirement

The contract should permit the ontology to change during development.

Early REE may only distinguish broad classes such as good/bad, controllable/uncontrollable, self-linked/external and persistent/transient. Later learning may split these into finer structures as experience demands it.

Thus `z_world` should not merely estimate values inside a permanently fixed set of categories. It should have enough representational freedom for useful distinctions to split, merge, reweight and become conditionally relevant.

## Failure modes to guard against

- **Perceptual adequacy without organism adequacy:** good reconstruction, poor action or rollout.
- **Label memorisation:** auxiliary-target accuracy without better transfer or counterfactual behaviour.
- **Premature collapse:** ambiguous states mapped to a single confident representation.
- **Over-compression:** regulatorily distinct states become neighbours because they look alike.
- **Over-specification:** the desired mature ontology is smuggled into targets rather than learned.
- **Static ontology:** representation cannot reorganize after the organism's vulnerabilities or affordances change.

## Minimal acceptance criteria

A candidate representation objective is more credible if it improves more than its own probe score. In particular, it should improve some combination of:

- E1/E2 rollout quality;
- behavioural success under changed layouts or contingencies;
- counterfactual discrimination;
- recovery after perturbation;
- transfer when sensory statistics remain similar but consequences change;
- persistence of useful structure after auxiliary supervision is removed;
- appropriate reorganization following replay or development.

## Working principle

> `z_world` should not be asked to know what the universe *is* in advance. It should be required not to throw away what the organism repeatedly needs in order to discover what its world is.

This is a hypothesis about the representation boundary and should be tested against equally capable non-regulatory baselines rather than protected as an architectural axiom.
