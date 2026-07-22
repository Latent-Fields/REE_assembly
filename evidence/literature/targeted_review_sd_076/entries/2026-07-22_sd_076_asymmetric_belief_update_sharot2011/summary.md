# Sharot, Korn & Dolan (2011) -- How unrealistic optimism is maintained in the face of reality

## What the paper did

Participants estimated their own likelihood of experiencing each of roughly eighty adverse life events, were then shown the actual population base rate, and re-estimated. The design gives a clean per-trial estimation error with a signed desirability: being told the true rate is *lower* than you guessed is good news, being told it is *higher* is bad news. Belief updates were measured as the change between the first and second estimate, and fMRI tracked how the brain coded the estimation error in each case.

## Key findings relevant to SD-076

The updates were asymmetric. People moved substantially toward the truth after good news and only weakly after bad news, which is a violation of the Bayesian norm -- the size of an update should track the size of the error, not its valence. Critically, the neural data locate the asymmetry in a specific place: distinct prefrontal regions tracked estimation errors calling for a positive update in everyone, but highly optimistic individuals showed *reduced* tracking of errors calling for a negative update in right inferior prefrontal gyrus. The bias is therefore not a symmetric pair of learning rates so much as a selective failure to register one class of error at all.

## How this translates to REE

SD-076 posits that the E3 selector's running-variance estimate over its own prediction error behaves as an asymmetric EMA: evidence that the agent is doing well is folded in fast, evidence that it is doing badly is folded in slowly, so the estimate settles below the true error mean and precision inflates across a waking episode. This paper is the clearest published warrant for the *shape* of that mechanism in biology, and it is the drift that the sleep-recalibration account behind MECH-204 quietly presupposes but never separately evidences. Without something like SD-076, MECH-204's corrective function has nothing to correct.

I want to be honest about where the mapping strains. Sharot and colleagues measure updating of first-order beliefs about the world -- how likely is it that I get burgled -- whereas SD-076 is a claim about a second-order quantity, the agent's estimate of its own accuracy. It is plausible that the same valence asymmetry governs both, and the confidence literature (see the Rollwage 2020 entry in this directory) makes that more plausible, but this paper does not establish it. There is also no per-step prediction error here in the reinforcement-learning sense; the trial structure is episodic and self-report-mediated.

## Limitations and confidence

The paradigm has been contested. Shah and colleagues argued in 2016 that the asymmetry is a statistical artefact of the base-rate structure rather than a psychological effect; Garrett and Sharot's rebuttal is recorded separately in this directory, and the Ni (2023) entry gives an independent reason to be careful -- learning-rate asymmetry estimates are confounded by the agent's initial value expectation, which for an EMA is precisely the initialisation term. That is a live methodological hazard for SD-076's own validation, not merely a citation caveat.

I have set confidence at 0.72: high source quality, a mechanism whose shape is directly the one SD-076 implements, but a real gap between first-order and second-order estimation that the experimental validation of SD-076 will have to bridge on its own evidence rather than inherit from here.

*Retrieved via PubMed. [DOI](https://doi.org/10.1038/nn.2949)*
