# Dissociating language and thought in large language models (Mahowald et al., Trends in Cognitive Sciences 2024)

## What the paper argues

Mahowald, Ivanova, Blank, Kanwisher, Tenenbaum and Fedorenko propose a single distinction and then run the entire LLM-capability debate through it. *Formal linguistic competence* is knowledge of linguistic rules and patterns -- morphology, syntax, the ability to produce and judge well-formed strings. *Functional linguistic competence* is using language in the world -- reasoning with it, tracking situations, modelling interlocutors, knowing what follows from what.

The distinction is not invented for the occasion. It is grounded in human neuroscience, much of it from Fedorenko's own lab: the language network identified by functional localisers is remarkably selective, and it is dissociable from the networks supporting reasoning, social cognition and world knowledge. Formal and functional competence rely on different neural mechanisms in people.

Applied to LLMs, the verdict is a clean split. Formal competence is, in their phrase, surprisingly good. Functional competence is spotty, and where it works it typically requires specialised fine-tuning or coupling with external modules. Their conclusion is that a model using language in human-like ways would need both, and that this may require mechanisms specialised for formal competence that are distinct from functional ones.

## Why this is the right defence of ARC-100

ARC-100 is a negative architectural commitment, and negative commitments are epistemically awkward. It is easy to write down "do not import transformer architecture; do not treat an LLM as a cognitive authority" and hard to say why in terms that are not simply a statement of taste. The strongest available defence of a prohibition is a principled account of why the prohibited move would have failed anyway -- and better still, one that simultaneously licenses the permitted alternative.

That is what this paper is, almost exactly. ARC-100 has two halves. The positive half (GRAM-1's framing) says grammar is a fossil record of recurrent cognitive relations, worth mining for candidate primitive cuts. The negative half says the mined structure is not the cognitive substrate and must not be imported as one. Both fall out of the single dissociation. Formal competence is real and high -- so there genuinely is structure in there worth mining, and the mining method is not wishful. Functional competence is separate, mechanistically distinct in humans, and not delivered -- so the structure is not the mind, and importing it would buy form without substrate.

What makes this better than the usual symbol-grounding argument is where the warrant comes from. Harnad-style grounding arguments are philosophical; one can simply decline the premise. This one rests on localiser-based neuroimaging showing that the human language network is separable from the systems doing the thinking. ARC-100 does not have to assert its prohibition as a design preference. It can point at a dissociation.

There is a practical corollary worth recording. *Because* formal competence is high, an imported LLM would produce output that passes surface inspection while the functional substrate underneath is simply absent. For any REE component whose grounding is assessed by reading what it emits, that is the worst possible failure mode -- a component that looks grounded and is not.

## Where it does not support ARC-100, which is not nowhere

Two boundaries, and the first is genuinely uncomfortable.

This paper argues that LLMs are not a complete cognitive system. It does *not* argue that importing transformer components into a larger architecture is a mistake. Those are different propositions, and the difference matters here, because the paper's own suggested remedy for spotty functional competence is "coupling with external modules" -- which is precisely the hybrid strategy that ARC-100's blanket prohibition forecloses. Read strictly, Mahowald et al. support "no LLM as cognitive authority" strongly and "no imported transformer block" not at all. If anything the second half of the prohibition takes mild counter-pressure from this source. I have scored the entry `supports` because the authority half is the load-bearing one for REE's design, but the asymmetry should be recorded rather than smoothed over: half of ARC-100's prohibition is evidenced here and half is not.

The second boundary is scope. ARC-100's sharpest operational content is its grounding criterion -- a mined cut counts as grounded only if it changes perception, attention, action, memory, rule-availability or coordination. That is a claim about *causal use inside a substrate*, and this paper does not address it. Establishing that form and function are separable in principle is a long way from a test of whether a particular mined cut is doing work in a particular system. That job belongs to the amnesic-probing entry alongside this one.

## Confidence

0.79, `supports`. Source quality 0.84 -- a TiCS feature review with an author list spanning computational linguistics and cognitive neuroscience, widely cited within a year, and crucially the human-neuroimaging leg is primary work from the same group rather than borrowed authority. Transfer risk 0.22, low, because for the authority half of ARC-100 the claim being evidenced is itself a claim about LLMs and no cross-domain transfer is needed. Mapping fidelity 0.78 is the constraint, and it is the asymmetry above doing the work: clean support for one half of the prohibition, none for the other, and nothing on the grounding criterion.
