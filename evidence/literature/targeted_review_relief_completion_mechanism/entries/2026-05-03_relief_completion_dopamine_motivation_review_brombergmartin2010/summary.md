# Bromberg-Martin, Matsumoto & Hikosaka 2010 — Dopamine in motivational control: rewarding, aversive, and alerting

## What the paper did

This is a synthesis review pulling together a decade of single-unit recording from midbrain dopamine neurons in monkeys, rats, and human imaging, asking whether the textbook "DA = reward prediction error" picture survives confrontation with the aversive-stimulus data. The authors argue it does not — at least not as a unitary signal. They propose that midbrain dopamine neurons fall into at least two functionally distinct populations.

## Key finding

The first population is *value-coding*: excited by reward and reward-predictive cues, inhibited by aversive events and aversive-predictive cues. This is the canonical Schultz / RPE picture. It is anatomically biased toward the ventromedial substantia nigra and ventral VTA, and projects preferentially to the ventral striatum / NAc. The second population is *salience-coding*: excited by both reward *and* aversive events, signalling something like "important thing is happening" rather than "good thing is happening." It is anatomically biased toward dorsolateral SNc and projects preferentially to dorsal striatum and prefrontal regions. Both populations are augmented by an alerting signal that responds rapidly to behaviourally significant sensory cues.

The Brischoux 2009 paper (separate entry in this slate) is one of the original empirical anchors for this framework — ventral-VTA DA neurons that *fire* to footshock onset are exactly the salience-coding population, and they sit alongside, not within, the value-coding system that Navratilova 2012 implicates in relief.

## How it translates to REE

The simple version of Model 1 — "relief just fires the dopamine pathway" — is too coarse. What the empirical literature converges on is more specific: relief fires the *value-coding* dopamine population, the same one that handles reward, with the polarity of the signal set by the underlying state-change (suffering goes down, value goes up). The salience-coding population fires for both reward and aversive events and serves a different function (orienting, motivational arousal, gating attention to important cues).

For an REE substrate, this matters in two ways. First, if the architecture treats dopaminergic teaching as a single channel, it will inherit the Brischoux-style failure mode — phasic DA firing at *aversive onset* (salience-coding) will look identical to phasic DA firing at *aversive offset* (value-coding) and the model will be unable to learn the correct sign. Second, the tag-and-release pipeline that Model 1 wants to share between goal-achievement and relief-completion is on the value-coding side. The salience signal is upstream of MECH-091 (phase-reset / orienting) but should not feed MECH-094 (the categorical write gate that determines what gets reinforced).

So the cleanest reading is: Model 1 wins for the *value-coding* DA channel, but REE needs to model the value/salience distinction explicitly to avoid contamination. This refines the recommendation rather than overturning it.

## Limitations and caveats

The value-vs-salience boundary is sharper in the review than it is in the underlying empirical work. Subsequent papers have shown DA populations with mixed properties, gradient distributions rather than clean categories, and projection-target specificity that complicates the simple two-types story. REE should treat the distinction as a useful abstraction at the substrate level rather than a hard anatomical claim.

The review is synthesis rather than direct test, so its evidence direction is "mixed" with respect to the M1/M2 question — it qualifies Model 1 (DA heterogeneity matters) without contradicting it (the value-coding DA population does the relief job).

## Confidence

Source quality is very high (Neuron review, central to current DA framework). Mapping fidelity is moderate — the review organises the empirical work rather than testing the architectural claim directly. Transfer risk is low because the value/salience distinction is a structural insight, not a paradigm-specific finding. Net confidence 0.79, mixed.
