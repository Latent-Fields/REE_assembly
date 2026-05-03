# Kidd & Hayden 2015 -- The Psychology and Neuroscience of Curiosity

## What the paper does

Kidd and Hayden survey the neuroscience and psychology of curiosity,
making three arguments. First, that curiosity is a real motivational
class with its own behavioral and neural signatures, distinct from
primary-reward seeking. Second, that the field has been hampered by an
over-attachment to defining curiosity narrowly -- they argue for a
broader, ethologically-grounded approach where information-seeking
behaviors are studied in their natural contexts and the question of
"what counts as curiosity" is held open. Third, that curiosity's neural
substrates partially overlap with reward processing (dopamine, OFC,
ACC) but are not reducible to it, and that the function of curiosity
is best understood as motivating learning rather than producing
consummatory satisfaction.

## Key findings relevant to SD-049

The load-bearing claim for SD-049 is that *curiosity is non-homeostatic*.
Curiosity does not reduce a physiological deficit in the way that food
reduces hunger. Its consummatory phase is the act of attending,
exploring, or extracting information, and its reward signal is
uncertainty-reduction or information-gain rather than need-satisfaction.
The behavioral signature is approach toward novel or uncertain stimuli
that does not satiate in the homeostatic sense -- the animal will
seek out information again the next time it has the opportunity, even
if its previous information-seeking was successful. The neural signature
includes characteristic dopaminergic responses to novelty and
information cues that are mechanistically distinct from primary-reward
dopamine responses.

The second relevant finding is that curiosity is not a single
phenomenon. Kidd and Hayden distinguish epistemic curiosity (drive
toward conceptual knowledge), perceptual curiosity (drive toward
sensory novelty), and information-seeking-for-future-reward (drive
toward information that will improve later decision-making). These
share neural substrate but are behaviorally distinct.

## How this maps to SD-049

The novelty channel in SD-049 is the architectural lynchpin
distinguishing fuller scope from minimal 2-type scope. Without it,
food and water are isomorphic-modulo-drive-axis, and "wanting" reduces
to "which axis is currently most depleted". With novelty as a
non-homeostatic third type, the agent can want a target whose
consumption does not reduce a homeostatic deficit, which is the
structural shape MECH-229 needs to test the wanting/liking dissociation.

Kidd and Hayden's framework licenses the novelty channel biologically.
It is not a hedge or workaround for a substrate limitation; it is the
substrate-level analog of a real motivational class that mammalian
nervous systems implement. The decay-with-familiarity benefit profile
(SD-049's `novelty_decay` curve) is the closest the V3 substrate can
get to the ethological signature -- benefit drops with repeated
exposure to the same cell, then the agent moves on to the next novel
target.

The implementation choice (perceptual habituation rather than
uncertainty-reduction) is one specific operationalisation. Kidd and
Hayden's framework would license other operationalisations too --
e.g. benefit proportional to predictive uncertainty about the cell's
contents -- which could be registered as future child mechanisms after
SD-049 lands. For the initial substrate, the per-cell-decay
implementation is the cleanest design.

The novelty channel is also the substrate connection to MECH-216's
schema-wanting claim. MECH-216 asserts that the E1 schema seeds
salience for cues that predict reward -- but to date the only "reward"
in V3 is homeostatic-deficit-reduction, so the schema cannot be
generalised across motivational classes. With a non-homeostatic class
in the substrate, MECH-216's generalisation across motivational classes
becomes testable.

## Caveats and confidence reasoning

The main caveat is that SD-049 implements one specific
operationalisation of one corner of Kidd and Hayden's curiosity class.
Generalising MECH-229 evidence obtained on this substrate to curiosity-
class claims as a whole would over-reach. The substrate licenses
claims about *this particular* form of non-homeostatic motivation, not
the full class. Future child mechanisms (e.g. MECH-(TBD): predictive
uncertainty as benefit signal) would extend the substrate to other
forms.

A second caveat is that Kidd and Hayden's framework is at the species
level (mammalian, primarily primate); SD-049 is a substrate for a
grid-world agent with no analog of OFC, ACC, or dopaminergic systems.
The transfer risk is low because the framework is functional and
explicitly cross-species, but the implementational details do not
transfer.

Confidence 0.86. Source quality 0.85 (Neuron, comprehensive review,
authoritative voices). Mapping fidelity 0.85 (the non-homeostatic
character of curiosity is exactly what the novelty channel needs to be
biologically licensed). Transfer risk 0.20 (functional framework
transfers cleanly; implementational neuroanatomy does not).

## Attribution

Source: PubMed PMID 26539887. DOI:
[10.1016/j.neuron.2015.09.010](https://doi.org/10.1016/j.neuron.2015.09.010).
Kidd C, Hayden BY. The Psychology and Neuroscience of Curiosity.
Neuron. 2015 Nov 4;88(3):449-60.
