# Developmental Ontology and Replay

Status: thought / organising hypothesis  
Date: 2026-09-04  
Related thought: `2026-09-04_from_regulation_to_knowledge_organizing_subjective_experience.md`

## Core idea

Development may not merely improve estimates inside a fixed representational scheme. It may change the scheme itself: what distinctions exist, which experiences are grouped together, which causal relations are represented, and which variables are treated as important.

This suggests a stronger role for replay and sleep:

> Replay may help reorganise the ontology through which experience is subsequently interpreted.

## Fixed-schema versus developmental-ontology views

A fixed-schema model assumes that the right representational axes are available from the beginning and learning mostly fills in values.

A developmental-ontology model instead allows the agent to discover that previously separate experiences belong together, that previously grouped experiences differ in consequence, or that a new causal distinction has become necessary.

Examples include learning distinctions such as:

- harmless versus harmful versions of a similar cue;
- controllable versus uncontrollable transitions;
- self-caused versus externally caused outcomes;
- temporary versus persistent resource structure;
- perceptually different states that share the same regulatory consequence.

## Why replay matters

Online experience is constrained by immediate action and local context. Replay can compare episodes that never occurred adjacently and can therefore expose structure unavailable in the moment.

Possible functions include:

- regrouping episodes under newly discovered regularities;
- splitting over-broad categories;
- merging superficially different but causally equivalent states;
- updating old episodes after a new causal interpretation is learned;
- weakening categories that no longer predict consequences;
- preserving unresolved alternatives until later evidence arrives.

## Prediction

If replay changes ontology rather than merely strengthening memory, then after replay the same incoming observation may be encoded differently even when no further environmental experience has occurred.

That is a stronger prediction than improved recall.

## Developmental staging

A plausible trajectory is:

1. broad regulatory distinctions dominate early learning;
2. recurrent action-outcome structure creates controllability distinctions;
3. repeated temporal structure supports persistence and causal expectation;
4. replay reorganises episodes around these emerging abstractions;
5. later representations become more compressed yet more behaviourally informative.

This means developmental curricula may alter not only performance but the geometry and semantics of `z_world`.

## Minimal experiments

### Replay-induced recoding

Record `z_world` for a probe set before replay. Run replay without new external experience. Re-present the identical probe set and measure whether latent organisation changes systematically.

### Category split

Train two perceptually similar states as initially equivalent, then introduce a regulatory consequence that distinguishes them. Test whether replay accelerates separation in latent space.

### Category merge

Train perceptually different states that later prove to have the same action/consequence structure. Test whether replay increases representational similarity and transfer.

### Retrospective causal update

Introduce a delayed revelation that changes the interpretation of earlier events. Test whether replay alters predictions about those earlier event classes without direct re-exposure.

## Controls

Distinguish genuine reorganisation from simple parameter drift or memorisation by including:

- no-replay controls;
- replay of consequence-neutral episodes;
- matched numbers of gradient steps;
- held-out probe episodes;
- behavioural tests requiring transfer rather than recognition.

## Red team

Replay may not be necessary for ontology change; ordinary online gradient updates may be sufficient.

Alternatively, replay may change only downstream predictors while `z_world` itself remains stable.

A third possibility is that forcing latent geometry to reorganise creates instability and catastrophic forgetting, making a more stable world representation preferable.

These are empirical alternatives.

## Relation to the current frontier

If observation → `z_world` → E1/E2 remains a bottleneck, the problem may not be only missing information. The latent may also be insufficiently plastic in *what distinctions it treats as real*.

The key diagnostic question is therefore:

> Is the system failing to preserve the right information, or failing to revise the categories through which that information is organised?

## Decision rule

Before adding special replay machinery, measure whether current replay changes latent organisation at all, and whether those changes improve transfer, causal discrimination, or downstream rollout. If replay only improves reconstruction or memorisation, the stronger developmental-ontology hypothesis remains unsupported.
