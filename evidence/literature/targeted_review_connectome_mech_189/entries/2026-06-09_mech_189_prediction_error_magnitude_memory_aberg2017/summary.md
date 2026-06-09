# Aberg, Müller & Schwartz 2017 — Trial-by-trial PE and anticipation modulate associative memory

According to PubMed. Source: Aberg KC, Müller J, Schwartz S. *Frontiers in Human Neuroscience* 11:56, 2017. [DOI](https://doi.org/10.3389/fnhum.2017.00056)

## What the paper did

The authors set out to disentangle two ways reward might help memory: the *anticipation* of reward (expected value) and the *delivery* of reward (which carries a prediction error). Participants performed an associative memory task embedded in a reinforcement-learning structure, and the authors fit a biologically-plausible computational model of dopaminergic prediction error and expected value. The headline result is that *both* reward delivery (mediated by PE magnitude) *and* reward anticipation (mediated by expected-value magnitude) independently improved memory — and strikingly, these effects emerged in the trial-by-trial model even when *no* effect was visible in standard analyses that collapse across trials. Effects interacted with individual reward/punishment sensitivity and with retention interval (20 minutes vs 24 hours).

## Why it matters for MECH-189

This is the most direct support for running the WRITE gate from an *external, quantitative prediction-error signal* — i.e. `super_ordinal_complexity_mode="external"`. It shows that a trial-by-trial PE magnitude is a genuine encoding determinant specifically for *value-associated* memory, which is MECH-189's domain. It also points to a concrete implementation: REE already computes an E1/E2 world-model prediction error, and the MECH-205 surprise-gated-replay pathway already consumes a surprise signal. Deriving the super-ordinal complexity term from that same machinery would keep REE's two surprise gates consistent rather than introducing a third, idiosyncratic novelty metric.

But the paper earns its place as much for its honesty as for its result, and that honesty is a caution. It is explicit that the prior literature reports the PE-vs-memory relationship as *positive in some studies, negative in others, and null in others*, depending on task and on individual reward/punishment sensitivity. The clean effects here required computational modelling to surface and were modulated by personality traits and delay. So an external PE-driven complexity signal is *not* a free lunch: its sign and gain need calibration, and a naive `|PE|` default could behave inconsistently across regimes. The dissociation between anticipation and delivery also suggests that compressing everything into a single "complexity" scalar may be underspecified — the brain keeps expected value and PE as separate terms.

## Limitations and caveats

The reward PE here is a *value/RL* prediction error, whereas REE's E1/E2 PE is a *forward-model* (perceptual) prediction error. Treating them as functionally analogous for the write gate is an assumption, not an established identity. The sample is modest and single-lab, the effects are model-derived rather than visible in raw behaviour, and they interact with traits and retention interval. These are why I hold confidence at 0.63 despite the strong directional fit.

## Confidence reasoning

Confidence 0.63, direction `supports`. The study supports an externally-computed PE signal as the operationalisation of gate (b), and usefully suggests reusing REE's existing forward-model PE / MECH-205 surprise channel. The documented heterogeneity (sign-and-gain dependence, trait and delay interactions) is exactly why the validation EXQ should compare an external-PE arm against the novelty proxy rather than switching the default blind. Lit confidence only; not blended into experimental confidence.
