# Leblois, Boraud & Hansel (2025) — Reward-driven adaptation of movements requires strong recurrent basal ganglia-cortical loops

According to PubMed ([DOI](https://doi.org/10.1073/pnas.2515994122); PMID 41379994; PMC12718356).

## What the paper did

A computational model of the basal ganglia-thalamo-cortical multi-regional network, designed to explain a long-standing puzzle: BG output is not required to execute many well-learned movements, yet plasticity at BG inputs (cortico-striatal projections) is essential for the acquisition and adaptation of those movements. The model integrates anatomical, physiological, and behavioural evidence and tests how the network's dynamics shape execution and reward-based adaptation of reaching movements.

## Key findings

The model demonstrates that the BG-cortical network shapes cortical motor output through three interacting mechanisms: (i) the diverse dynamics emerging from closed-loop architecture between cortex and BG, (ii) attractor dynamics driven by recurrent cortical connections, and (iii) reinforcement learning via dopamine-dependent cortico-striatal plasticity. The closed-loop architecture is essential: a feedforward-only architecture cannot reproduce the observed pattern where BG plasticity contributes to adaptation that subsequently does not require BG output for execution. The model also offers a mechanism for early-stage reaching acquisition through motor babbling.

## Mapping to Q-019

Q-019 frames the architectural debate as three-gate vs single-gate. Leblois introduces a constraint orthogonal to that framing but consequential for it: whichever gate count one chooses, the architecture must be closed-loop with strong recurrent dynamics, not feedforward gating. The paper integrates a broad range of empirical evidence (anatomy, physiology, behaviour) to show that a feedforward model — single or multi-gate — does not capture the cortex-BG interaction during movement adaptation.

For REE this constrains both the substrate question and the V3/V4 implementation. ARC-021's three-loop framing would need each loop wired as a closed cortex-BG-thalamus-cortex loop with internal recurrence, not as a feedforward gate that emits a one-shot selection decision. The implementation implication is non-trivial: closed-loop dynamics with attractors require time-stepping at a finer granularity than single-step gating, and the reinforcement-learning-via-cortico-striatal-plasticity component fixes a particular learning-signal locus (cortico-striatal synapses) which interacts with REE's existing claims about RPE pathways.

The mapping needs care on two fronts. First, the computational model is specifically about the motor loop (reaching movements). Q-019's framing covers sensorium, thought, and action loops; the closed-loop prediction is most directly tested for the action loop and is inferred to extend to the others by analogy. Second, the model demonstrates that closed-loop architecture is *sufficient* for the empirical pattern; it does not strictly demonstrate that no single-gate feedforward architecture *could* be made to work with different mechanisms. The argument is by integration of evidence rather than by exhaustive comparison.

## Caveats

Single-locus motor-loop test; the extension to thought and sensorium loops is by analogy. The paper is computational modelling, so the empirical anchors are integrative rather than primary new measurements. Recent (2025) so the computational community has not yet had time to fully evaluate the model's specific commitments.

## Confidence reasoning

I land at 0.78. Source quality is high (PNAS 2025; Leblois/Boraud/Hansel collaboration with established credentials). Mapping fidelity is good — the closed-loop constraint applies to whichever gate-count Q-019 ends up favouring, and constrains REE's implementation accordingly. Transfer risk is the standard computational-model-to-architecture caveat. I include this entry because it adds a structural constraint Q-019's existing 14-entry coverage does not articulate clearly.
