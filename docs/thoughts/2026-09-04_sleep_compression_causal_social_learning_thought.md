# From episodic traces to causally usable social schemas

**Date:** 2026-09-04  
**Status:** Research-bounded thought intake  
**Scope:** Waking-versus-sleep updating; E1/E2/hippocampal memory; later social attribution and counterfactual learning  
**Sources:**  
- Jiang et al. (2026), [*Compressed representations underpin knowledge awareness in sequence learning*](https://www.biorxiv.org/content/10.64898/2026.08.22.746376v1) (preprint; posted 2026-08-26).  
- Rafiuddin & Sen (2026), [*C³T: Counterfactual Causal Reasoning for Sentiment Shifts in Social-Media Conversation Trees*](https://arxiv.org/abs/2609.02131) (preprint; posted 2026-09-02).

## Core proposition

REE should distinguish at least three achievements that can otherwise be collapsed into one vague notion of “learning”:

1. **Episode retention:** a waking agent preserves what occurred, including relevant perceptual, interoceptive, action, and outcome traces.
2. **Compressed schema formation:** offline or low-interference processing discovers a simpler reusable representation of regularity across episodes.
3. **Causally usable social knowledge:** the agent can later query the schema counterfactually: not merely “what followed what?”, but “what action of mine or another agent plausibly changed this other agent’s state or trajectory?”

The crucial bridge is not a generic replay buffer. It is the conversion of causally annotated episodes into abstractions that preserve intervention-relevant distinctions while discarding incidental detail.

## What the new work contributes

Jiang et al. report that compressed posterior representations in sequence learning relate to both acquired knowledge and conscious awareness of that knowledge. This is preliminary human evidence, not a validated computational mechanism. It nevertheless sharpens a useful distinction for REE: behavioural competence can precede a representation that is available for flexible inspection, report, or higher-level control.

C³T makes a complementary point in a social setting. It represents conversational events as a branching temporal structure, identifies candidate upstream causes of later affective shifts, and evaluates counterfactual interventions on those candidate events. Its findings are specific to social-media conversations and the proposed model; they do not establish a general theory of social cognition. The transferable methodological insight is that social learning needs event ancestry, competing causal candidates, and counterfactual tests—not only correlated state transitions.

## REE interpretation

During waking, REE should favour bounded, reversible updates: store episodes and attach uncertainty rather than rapidly rewriting durable schemas. An event record suitable for later consolidation may include:

- a compact local world/self state;
- the acting agent, action, and relevant affordances;
- the observed response of self and other;
- outcome and affective/interoceptive consequences;
- temporal/causal ancestry candidates;
- confidence, novelty, prediction error, and replay priority.

During sleep or an explicitly offline consolidation mode, selected traces can be replayed, clustered, re-bucketed, and compressed. The resulting schema must retain counterfactual handles: agent identity/type, action class, contextual preconditions, and uncertainty over causal contribution. Compression that loses those handles may improve predictive loss while damaging later social understanding.

This creates a useful separation:

| Representation | Primary function | Failure if conflated |
|---|---|---|
| Episodic trace | Preserve contingent lived experience | Over-generalisation from one event |
| Compressed schema | Reuse stable structure efficiently | Loss of intervention-relevant detail |
| Counterfactual query | Estimate causal contribution to another trajectory | Correlation mistaken for agency or intent |

## Testable predictions

1. Agents with replay/compression should generalise from fewer social episodes than agents trained only on online transition updates.
2. A sleep-like process that preserves causal annotations should outperform equally sized compression that is blind to actor/action ancestry on held-out social attribution tasks.
3. The benefit should be most visible where temporal coincidence is misleading: for example, another agent changes course after both a resource shift and the focal agent’s signal.
4. Premature schema commitment should create a recognisable pathology: persistent over-attribution or under-attribution of agency despite contradictory episodes.
5. Inspectability should lag competence in at least some tasks: the agent may behave adaptively before it can answer a later query about why its policy changed.

## Minimal experimental path

Build a small two-agent extension of the current gridworld with deliberately confounded events. On each trial, a focal agent observes another agent’s state shift after one or more possible causes: resource change, obstacle, direct contact, signal, or a third-party action.

Compare:

- online-only episode learning;
- episode storage plus random replay;
- episode storage plus prioritised sleep replay and schema compression;
- the same compression with causal annotations ablated.

Evaluate predictive accuracy, policy adaptation, causal-attribution calibration, and resilience when the surface correlation reverses. The key score is not whether the agent predicts a response, but whether it selects the correct intervention when asked to help, avoid harm, repair, or cooperate.

## Architectural caution

This thought does not imply that sleep is the sole location of abstraction or counterfactual processing. Waking can support local replay and provisional restructuring. The narrower claim is that any durable re-bucketing process needs safeguards: protected episodic evidence, uncertainty retention, and tests that distinguish improved compression from improved causal understanding.

## Candidate downstream fan-out

- **Thought digestion:** decide whether causal ancestry belongs in hippocampal episode records, a social-event ledger, or both.
- **Candidate claim:** waking/offline update asymmetry should be explicit: waking preserves evidence and calibrates local predictions; offline processing proposes durable schema updates subject to validation.
- **Experiment seed:** “causal replay preservation” ablation suite for sleep and social attribution.
- **Evaluation seed:** separate latent behavioural competence, explicit/queryable schema access, and causal-attribution calibration.
