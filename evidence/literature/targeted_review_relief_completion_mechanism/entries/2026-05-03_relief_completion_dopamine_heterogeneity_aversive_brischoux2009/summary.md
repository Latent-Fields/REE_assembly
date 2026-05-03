# Brischoux, Chakraborty, Brierley & Ungless 2009 — Phasic excitation of dopamine neurons in ventral VTA by noxious stimuli

## What the paper did

The Ungless lab recorded from individual ventral tegmental area dopamine neurons in anaesthetised rats during noxious footshock, with two methodological strengths that put this paper in a different class to most aversive-DA work. First, they used juxtacellular labelling — a technique that lets you mark the recorded neuron and confirm its dopaminergic identity post hoc, instead of inferring it from electrical properties (which famously misclassifies a substantial fraction of cells). Second, they tracked the precise anatomical position of each cell within VTA. So when they report population differences, those differences are anchored to confirmed cell type and confirmed location.

## Key finding

Dorsal-VTA dopamine neurons were *inhibited* by footshock — consistent with the canonical reward-prediction-error picture, in which DA codes value and an aversive event drives a negative deflection. Ventral-VTA dopamine neurons, in contrast, were *phasically excited* by the same footshock. Both populations were confirmed-dopaminergic and lived a few hundred microns apart. The same noxious stimulus produced opposite responses in two populations of the same neurochemical type, separated only by anatomical position.

This is the empirical anchor for what later became the Bromberg-Martin / Matsumoto-Hikosaka value-vs-salience framework. It is the cleanest demonstration that "dopamine = reward signal" is a coarse generalisation hiding a real architectural split.

## How it translates to REE

The relevance to the relief-completion question is essentially as a qualifier on Model 1. The Andreatta 2012 and Navratilova 2012 results establish that pain offset / relief recruits the mesolimbic DA system; the Brischoux 2009 result reminds us that not all VTA DA neurons are doing reward-coding work, and a subset fires *during* the aversive event itself. So if an REE substrate simply read "phasic DA in VTA" as a teaching signal, it would inherit a sign-confusion failure: the same gross signal would mark "pain has just happened" (ventral-VTA salience-firing) and "pain has just stopped" (dorsal/value-coding DA firing).

The architectural implication is that the relief-completion mechanism in REE should not be modelled as a generic DA pulse. Either the teaching signal is restricted to the value-coding DA population specifically (which is what the Andreatta and Navratilova results actually localise), or the tag-write is gated on a derived comparator — something like suffering-state-derivative crossing a threshold — rather than on raw dopaminergic activity. The latter is closer to what MECH-094 already does at the categorical level for goal-achievement, and is probably the cleaner architectural choice.

This entry therefore refines rather than refutes the M1 recommendation: relief uses the value-coding DA channel, REE has to be careful not to treat all DA firing as equivalent, and the actual write-gate should be the suffering-derivative comparator.

## Limitations and caveats

The recordings are in anaesthetised animals. Awake-behaving recordings show more nuance, and some of the population separation gets fuzzier with task context, attention, and learned associations. The paper does not record during aversive *offset* directly — the relief-relevant inference comes from combining this with later work (Matsumoto & Hikosaka 2009; Bromberg-Martin et al. 2010) rather than from this paper alone. So its role in this slate is as a structural qualifier, not as direct evidence of relief signalling.

## Confidence

Source quality is high (PNAS, juxtacellular labelling, well-replicated). Mapping fidelity is moderate because the paper documents the heterogeneity rather than directly testing the relief-completion question. Transfer risk is moderate (anaesthetised preparation). Net confidence 0.80, mixed — qualifies Model 1 by adding the value/salience subtlety but does not unseat the M1 recommendation for the value-coding DA channel.
