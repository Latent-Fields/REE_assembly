# Jamali et al. (2021) -- Single-neuronal predictions of others' beliefs in humans

## What the paper did

Four of the five entries in this pull are about language models. This one is not, and the reason it
belongs here is a word in EXT-006 that is easy to read past: *homologous*. The claim is not simply
that other agents should be modelled. It is that they should be modelled in a substrate continuous
with the one carrying the self-model, so that predicted harm to another can register in the same
residue field that governs the agent's own trajectory selection. That is a commitment about
representational format, and no behavioural benchmark on any system can bear on it.

Jamali and colleagues recorded single neurons in the human dorsomedial prefrontal cortex during
awake deep-brain-stimulation surgery -- 324 putative neurons across 15 participants (11 in the
primary task, mean age 62, undergoing surgery for essential tremor, Parkinson's disease or
dystonia), using custom arrays of five tungsten microelectrodes advanced incrementally while the
patient performed a verbal false-belief task. Of the primary-task neurons, 20.0% (n=42) predicted
whether the participant was currently considering another person's beliefs, with 83±2% collective
decoding accuracy, and 23% (n=49) predicted whether the belief under consideration was false or
true, at 78±3%. Population decoding recovered all four belief features simultaneously on 36±2% of
trials against a 6.25% chance rate.

Two control results are what make the paper useful here rather than merely interesting. First, only
11 of the 49 belief-discriminating neurons also discriminated false from true *physical*
representations -- so the code is specific to belief, not a generic signal that something is being
represented counterfactually. Second, in a control task 27.7% of 112 neurons encoded the
participant's own imagined false versus true beliefs, and these were "largely distinct" from the
other-belief neurons. Population prediction accuracy also tracked behaviour: 72% on trials the
participant got right, 56% on trials they got wrong.

## How this maps onto EXT-006 and ARC-010

The self/other result is the one that matters. In the same cortical region, recorded through the
same electrodes in the same sessions, there are cells encoding another's belief and cells encoding
one's own imagined belief, and the two populations are largely separable. That is precisely the
shape ARC-010 assumes -- shared substrate, separable indexing -- and it is not the only shape
available a priori. A single merged representation would have predicted overlap; two unrelated
systems would have predicted the other-belief code to live somewhere else entirely. Neither is what
was found.

The belief-specificity result supplies a second constraint that I think is underappreciated. If an
agent's model of another agent were simply a special case of its world-model -- another object whose
states are tracked -- then the neurons discriminating true from false beliefs should also
discriminate true from false physical states, because both are the same operation applied to
different content. Fewer than a quarter of them do. Whatever biology is doing here, it is not
getting the other-model for free out of the world-model, which is worth knowing for an architecture
deciding whether to build one explicitly.

The behavioural coupling -- 72% versus 56% -- is the first faint gesture towards what ARC-010
actually asserts, which is that the other-model has consequences for what the agent does. I want to
be careful not to make more of it than it is. A correlation between population decoding accuracy and
trial correctness is an enormous distance from a penalty term entering a selection objective.

## Limitations and caveats

The transfer distance here is the largest in this pull, and five boundaries should be stated
explicitly. The paper says nothing about language models; its relevance to EXT-006 is entirely as
grounding for the architectural alternative REE proposes, never as evidence about what LLMs have or
lack. It establishes that a self-separable other-belief code *exists*; it does not establish that
such a code is *necessary* for social competence, which is what EXT-006 would need and which would
require lesion or causal-perturbation evidence. It says nothing about coupling into action selection,
so ARC-010's kappa coupling remains unevidenced by this or by anything else found in this review. The
sample is 11 adults undergoing awake surgery for movement disorders, mean age 62 -- small, clinical,
older, and recorded intraoperatively, with all the generalisation caveats that human single-unit
work carries. And the beliefs are propositional, about object identity and location in verbal
vignettes, not the affective or latent states that ARC-010's coupling would actually need to model.

One provenance note that anyone citing this for anatomy must read first. An Author Correction was
published two years later (Nature 618, E25, 2023; doi 10.1038/s41586-023-06263-6). Reconstructing the
recording locations on a standardised 3D brain model placed the sites somewhat more posterolaterally
and more broadly distributed than originally estimated, spanning the superior frontal gyrus and part
of its medial middle frontal gyrus border. The authors state that the neuronal findings, the
analyses and the other figures are unaffected. That reads as a genuine correction of localisation
rather than of result, but it does mean the precise dmPFC attribution should be quoted from the
correction and not from the original.

## Confidence

0.63. Source quality 0.88 -- Nature, human single-unit recording, a rare and technically demanding
preparation, with the physical-state and self-belief controls that the interpretation requires, and
effects large relative to the stated chance levels; held below 0.9 by the small clinical sample
intrinsic to intraoperative work and by the anatomical correction. Mapping fidelity 0.55: the
self/other separability maps onto ARC-010's architectural assumption unusually well, but the paper
concerns propositional belief in humans while EXT-006 concerns latent-state modelling in artificial
systems, so most of the claim is untouched. Transfer risk 0.45, the highest in this pull and set
there deliberately: human cortex to artificial architecture, an older clinical sample to general
cognition, and propositional belief to the affective latent state the coupling would need.
