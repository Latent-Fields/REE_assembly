# Yu & Dayan 2005 — Uncertainty, neuromodulation, and attention

**Source:** Yu AJ, Dayan P. *Neuron* 46(4):681-692 (2005). [DOI](https://doi.org/10.1016/j.neuron.2005.04.026). PMID 15944135. According to PubMed.

## What the paper did

Yu & Dayan offer a computational theory in which the brain represents two structurally different kinds of uncertainty and broadcasts each via a different neuromodulator. Within a fixed context, cues are unreliable in a known way -- this is "expected uncertainty," and ACh is the carrier signal. Across contexts, the world's structure can change unsignalled -- this is "unexpected uncertainty," and NE is the carrier signal. The two interact: high ACh suppresses top-down priors (because cues are unreliable, weight the bottom-up); high NE triggers a context reset, increasing learning rate and discounting accumulated priors. The model is presented analytically and tested against existing pharmacological and behavioural literature on cholinergic and noradrenergic manipulation in humans and animals.

## Why it matters for Q-041

Q-041 asks the architectural question: unified supervisor or scattered loci? Yu & Dayan are exactly the right anchor because they are not silent on architecture -- they propose a specific hybrid. Two global signals, each computed at and broadcast from a separate neuromodulator nucleus, each with its own dynamics, with one signal handling the chronic baseline-uncertainty regime and the other handling the regime-shift regime. This is neither "single supervisor" nor "scattered loci"; it's a small number of system-level signals that together act as the threshold-coordination layer.

REE's current four adaptive loci (ARC-016 dynamic precision, SD-032c AIC baseline, SD-032d PCC stability, SD-032e pACC drive bias) all live in the *expected uncertainty / volatility* track of the Yu-Dayan taxonomy. They are local timescale-EMAs over their own substrate; they accumulate continuously, and they do not include any mechanism that fires specifically on a context switch or sudden regime change. Q-041's first motivating gap (cross-substrate volatility tracking) is well-described by the missing NE / unexpected-uncertainty channel. The Yu-Dayan reading sharpens the question: REE may not need a single supervisor, but it almost certainly needs at least one more channel -- a "unexpected uncertainty" signal that is structurally distinct from continuous EMA tracking.

## Mapping to REE

The architectural take-away transfers cleanly. The neurotransmitter assignments do not, and should not be lifted directly. Later work (Marshall et al. 2016, [DOI](https://doi.org/10.1371/journal.pbio.1002575)) uses systematic pharmacological dissection in humans and finds that NE, ACh, and DA each contribute to multiple uncertainty quantities in entangled ways -- the clean Yu-Dayan dichotomy is a useful theoretical scaffold but not the literal mapping. For REE, the right move is to name the architectural slot ("a fast change-point detector that fires on regime shifts") and leave the substrate underdetermined.

## Caveats

The 2005 model is purely theoretical. The pharmacological evidence cited in support is correlational and pre-dates the more rigorous causal studies of the 2010s. Critics have argued that the ACh/NE division of labour is too clean; in particular, dopamine carries some uncertainty signal that the original framework does not accommodate. None of this changes the relevance to Q-041, which is the architectural proposal -- multiple system-level uncertainty signals coordinated through neuromodulator dynamics rather than through a single executive supervisor.

## Confidence reasoning

0.74 mixed for Q-041. Source quality high (foundational, Neuron, heavily cited). Mapping fidelity high-moderate (0.75) -- the paper directly addresses the supervisor-vs-distributed question Q-041 raises. Transfer risk moderate (0.30) -- the architectural proposal transfers cleanly but the specific channel assignments do not. Direction is mixed because the paper supports neither the strong "single supervisor" reading nor the strong "scattered loci" reading; it specifically argues for a small number of system-level channels, and that intermediate position is what REE should consider.
