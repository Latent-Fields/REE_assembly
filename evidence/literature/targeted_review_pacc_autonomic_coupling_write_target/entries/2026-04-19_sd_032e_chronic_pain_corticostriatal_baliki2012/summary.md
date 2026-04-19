# Baliki et al 2012 — Corticostriatal connectivity predicts chronic pain transition

## What the paper did

Baliki and colleagues followed 39 patients with subacute back pain longitudinally across approximately one year, scanning them three times. At each timepoint they measured resting-state functional connectivity and pain phenomenology, and sorted patients post-hoc into those whose pain recovered and those who transitioned to chronic. The central finding: the transition was predicted not by properties of the nociceptive input (intensity, duration, peripheral markers) but by progressive reorganisation of connectivity between medial prefrontal cortex and the nucleus accumbens. Patients destined to chronify showed increasing mPFC-NAc coupling over the year; recoverers did not. The effect was robust across several analytic choices and partly replicated in reanalysis papers over the following decade.

## Key findings relevant to SD-032e

Two findings matter for this scoping question. First, sustained nociceptive input *does* produce slow, cumulative changes in a baseline neural variable on the timescale of months — this directly licenses the general architectural move SD-032e is making. Second, and more consequentially, the drift localises to corticostriatal reward-valuation circuitry rather than to ACC-to-autonomic or ACC-to-interoceptive pathways. The mPFC-NAc circuit in humans is widely interpreted as tracking value, reward prediction, and motivational state — not interoceptive drive in the homeostatic sense.

## Translation to REE

The paper supports SD-032e's existence claim — there is a real biological process by which sustained affective pain exposure shifts a slow baseline and reshapes downstream evaluation. It does not, however, support the specific claim that the write target is SD-012's drive_level (an interoceptive/energetic scalar). If Baliki 2012 is the strongest mechanistic anchor, the cleanest REE mapping would write z_harm_a drift into a *valuation* baseline — closer in spirit to SD-032b's action-value machinery than to SD-012's homeostatic drive. REE currently has no explicit reward-predictor module, so using drive_level as a proxy is defensible as a first approximation but should be flagged in the SD doc as an architectural simplification rather than a biologically-tight mapping.

## Limitations and caveats

The study is correlational; mPFC-NAc reorganisation could be cause, consequence, or shared effect of chronification. Human-to-agent transfer is always risky, especially for a mechanism that plausibly depends on dopaminergic learning dynamics REE does not simulate. The paper does not test whether the drift is reversible, which matters for deciding whether SD-032e needs an explicit offline-decay term.

## Confidence reasoning

I have placed confidence at 0.72. Source quality is high (Nature Neuroscience, longitudinal design, widely cited and partially replicated). Mapping fidelity is the weak axis: the paper evidences the *general* architectural move but points toward a reward-valuation target rather than a homeostatic-drive target. Transfer risk is moderate — the macroscopic claim transfers, the microscopic substrate does not. I would not cite this paper as sole justification for writing into drive_level; I would cite it as evidence that *some* slow baseline must be writeable, and then let the other papers in this review disambiguate which baseline.
