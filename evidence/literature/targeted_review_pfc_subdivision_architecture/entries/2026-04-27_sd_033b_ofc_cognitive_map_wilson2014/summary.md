# Wilson, Takahashi, Schoenbaum & Niv 2014 -- OFC as cognitive map of task space

## What the paper does

This is the theoretical paper from the Niv/Schoenbaum collaboration that crystallises the OFC-as-cognitive-map hypothesis. The authors notice a long-standing tension in the OFC literature: lesions disrupt reversal learning, devaluation sensitivity, extinction, and delayed alternation -- but no single existing account (value caching, expected outcome, abstract rule) fits all of these. They propose a unifying alternative: OFC encodes the agent's current state in task space, including state information that cannot be read off sensory input alone (task phase, working-memory contents, latent context).

The mechanism is functional rather than circuit-level: OFC supplies a state label that downstream reinforcement-learning machinery (in this paper's framing, dopaminergic VTA + striatum) uses to retrieve the appropriate value or expectation. When the state is fully observable from sensory input, OFC contribution is minimal and lesions do little. When the state is partially observable (the same stimulus means different things in different task phases), OFC becomes critical and lesions catastrophic. The authors lay out testable predictions to distinguish this from competing accounts and note that classical OFC findings in reversal and devaluation fall out as special cases -- the deficit is not in value updating per se but in identifying which state the agent is in.

## Findings relevant to SD-033b

SD-033b's functional restatement explicitly cites the cognitive-map framing as one of two complementary representations the OFC-analog must hold (the other being specific-outcome prediction, the Rudebeck/Murray oracle framing). Wilson/Niv 2014 is the canonical theoretical statement of that cognitive-map function. The paper's claim that OFC labels states for downstream RL maps directly onto SD-033b's claim that the OFC-analog supplies E2's substrate address: E2 in ree-v3 is a transition model f(z, a) -> z' whose specific-outcome predictions are conditioned on which state the agent is in. Without a structured task-state representation upstream, those predictions degenerate to sensory-driven habit; with it, E2 can produce different rollouts in different task phases even when sensory input is identical.

The paper is also notable for what it argues against: a pure value-encoding reading of OFC. The authors marshal evidence that OFC neurons multiplex value with task-phase information in ways that pure-value accounts cannot explain, and that OFC lesions disrupt behaviours that would be invariant under a value-only deficit. This is precisely the dissociation SD-033b uses to separate itself from SD-033c (vmPFC-analog value integration) -- the two substrates do related but distinct things.

## Mapping to REE -- caveats

The clean part of the mapping: state-labeling for downstream prediction is exactly what SD-033b framing (ii) describes, and the cognitive-map view is well-supported by subsequent empirical work (Schuck 2016 in humans, Zhou et al. 2019 in rats -- both in this review directory). The less clean part: Wilson/Niv frame the downstream consumer as TD-style RL machinery operating on scalar value, whereas REE's E2 is a deterministic transition model. So the paper supports the existence and function of the OFC-analog substrate but does not endorse a particular implementation of how E2 reads from it. SD-033c is the closer analog of the TD-RL consumer; SD-033b is specifically the structured-prediction consumer. The functional story still goes through: OFC labels states, something downstream uses those labels to predict.

## Limitations

This is a theoretical synthesis, not a direct empirical demonstration. The strongest evidence in the paper comes from re-interpreting older lesion literature; the direct empirical confirmation came later (Schuck 2016 human fMRI, the Zhou/Stalnaker rodent ensemble papers already in this review directory). I have weighted confidence accordingly -- the paper carries the field's canonical framing of the cognitive-map function but its weight comes from being theoretically generative rather than from a single decisive experiment. The empirical confirmations sit alongside it as the actual evidentiary backbone.

## Confidence reasoning

Confidence 0.86. Source quality very high (Neuron, foundational paper). Mapping fidelity strong: the paper's state-labeling role and SD-033b framing (ii) describe the same substrate function. Transfer risk modest -- the paper is cross-species in scope and the cognitive-map framing is at a level of abstraction that travels cleanly. The 0.86 rather than 0.90+ reflects the theoretical-vs-empirical balance: this paper is the framework, not the proof. Combined with the empirical entries already in this directory (Schuck 2016, Zhou 2019, Stalnaker 2021), the evidence base for SD-033b framing (ii) is strong.
