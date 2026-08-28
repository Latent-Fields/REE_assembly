# Friston, Rigoli, Ognibene, Mathys, Fitzgerald & Pezzulo (2015) -- Active inference and epistemic value

**Cognitive Neuroscience 6(4):187-214. DOI: 10.1080/17588928.2015.1020053. PMID: 25689102.**

## What the paper did

This is the paper that formally introduces the decomposition of *expected free energy* -- the quantity an active-inference agent minimizes when choosing between policies (candidate action sequences) -- into an extrinsic term (expected reward/pragmatic value, evaluated against prior preferences) and an epistemic term (expected information gain: how much a policy's likely outcomes would reduce the agent's uncertainty about hidden states of the world). The authors derive this decomposition formally and illustrate it with simulations of exploratory behavior, showing that agents which minimize expected free energy naturally trade off exploiting known reward against exploring to resolve uncertainty.

## Key findings

The central formal result is that evaluating a policy's expected free energy requires the agent to *imagine* that policy's likely outcomes under its own current generative model -- a purely internal, counterfactual computation -- and score them for both pragmatic and epistemic value. This imagining, by construction, never touches the generative model's own parameters: the model used to imagine outcomes is the same model being scored, and it is left untouched by the act of scoring. The model is updated only afterward, through ordinary perceptual inference over *real, enacted* observations.

## How this maps to REE (ARC-092)

ARC-092 licenses "counterfactual exploration whose outputs are priors for future waking testing, not knowledge" and forbids treating imagined outcomes as validated new facts. This paper is the formal argument for exactly why that separation is coherent and not merely a convenient architectural rule: expected-free-energy policy evaluation is *defined* as an operation that consumes the current model to produce a preference over actions, and is categorically distinct from the operation that updates the model. REE's E3 stage -- scoring differentiated imagined candidate futures to select among them -- is the architectural analogue of expected-free-energy policy scoring, and MECH-094's provenance write-gate is what keeps that scoring pathway from leaking into the world-model-update pathway, mirroring the clean separation this paper's mathematics assumes. It also grounds why counterfactual exploration is not confabulation-by-default (contrast with the Schnider-style clinical failure mode): information-seeking over imagined outcomes is a normal, well-motivated part of adaptive behavior, provided the imagined content stays confined to the policy-scoring role.

## Limitations and caveats

This is a normative, computational-level theory with illustrative simulations, not a test of any biological system -- let alone REE -- actually respecting the imagined/real separation in practice. REE is architecturally analogous to an active-inference agent (candidate scoring over imagined futures feeding a selection decision) but is not a literal free-energy-minimizing implementation, so the mapping is at the level of shared computational structure, not formal equivalence. The paper does not itself audit any code path for violations; it only explains why the LICIT/FORBIDDEN boundary is the theoretically correct place to draw the line.

## Confidence reasoning

Source quality is high -- a foundational, widely cited paper from the active-inference literature's originating group. Mapping fidelity is moderate: the theoretical structure maps cleanly onto REE's E3-scoring / MECH-094-gate architecture, but the correspondence is an analogy between REE's design intent and active inference's formal framework rather than a direct empirical test of REE. Net confidence 0.7: strong formal grounding for the LICIT-side "counterfactual exploration as prior-formation, not knowledge" argument.
