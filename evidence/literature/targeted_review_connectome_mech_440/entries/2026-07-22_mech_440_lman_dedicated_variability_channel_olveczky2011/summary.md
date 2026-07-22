# Ölveczky, Otchy, Goldberg, Aronov & Fee 2011 — a dedicated circuit that injects motor variability

**Claims:** MECH-440 (primary), MECH-313 (secondary)
**Direction:** mixed · **confidence 0.74**

## What the paper did

Juvenile zebra finches sing variable, sloppy song and gradually sharpen it. The authors recorded single units in RA — the motor-cortex analogue that actually drives the vocal muscles — across that developmental window, and then did the experiment that matters: they reversibly inactivated each of RA's two main inputs during singing and watched what happened to the motor program.

Inactivating LMAN, the output nucleus of a basal-ganglia-forebrain loop, made RA's song-aligned firing patterns adultlike in their stereotypy — *without* dramatically affecting spike statistics or the overall firing patterns. Inactivating HVC, the premotor input, destroyed stereotypy of both the song and the underlying motor program entirely. And across development, LMAN's relative contribution falls away while HVC's grows.

## The question this was pulled to answer

The autopsy of V3-EXQ-708a flagged that MECH-440's levers are engineering imports — "temperature" from Boltzmann/softmax, weight noise from NoisyNet — and asked whether a global temperature knob is the right translation *at all*. This paper is about as direct an answer as the biology offers, and the answer is no.

Read the LMAN inactivation result carefully. Removing the variability source left the content of the motor program essentially intact and simply made it stereotyped. That is a dissociation a global temperature *cannot* reproduce, because a scalar on the selection distribution has no way to perturb the spread without acting on the very quantity that specifies the action. In the bird, exploration and specification are carried by two different anatomical channels converging on one target, and you can knock out one and leave the other standing. The double dissociation with HVC makes the point twice over.

Three further details sharpen the design implication:

**The variability channel is not a noise source.** LMAN also contributes a corrective bias to the vocal output — it carries structure, an actual teaching signal, not zero-mean jitter. So the biological object is a second *proposing* input, not a perturbation term.

**The annealing is architectural.** MECH-440 asserts self-annealing, and the bird does anneal — but it does so by shifting the balance between two inputs as the circuits mature, not by decaying a scalar on one of them. That is a materially different mechanism from a gradient-trained per-parameter sigma falling toward zero, even though both produce "less variability late in learning."

**Variability injection targets a population, not a parameter set.** LMAN projects onto RA. It does not perturb RA's own weights.

## Why mixed, and what it means for V3-EXQ-708b

This is the part I want to be careful about, because it cuts against MECH-440's two halves in opposite directions.

It strongly supports the half of MECH-440 that says the post-softmax temperature framing is biologically under-specified. That half now has causal, not merely correlational, backing.

But it also undercuts the sufficiency of the replacement MECH-440 proposes. NoisyNet weight noise is still noise on the selection head's *own* parameters. It is state-conditioned, it propagates, it self-anneals — all genuine improvements on a global temperature, and all reasons the claim was worth registering. What it is not is a separate channel. On this evidence the biological form is a distinct input that proposes alternatives into the selection pathway, and a per-parameter sigma on the existing head is a different object wearing similar clothes.

That matters for interpreting the queued 708b. The autopsy recorded that with a demonstrably working instrument — 862 fresh E3 `select()` calls against a floor of 30 — neither a temperature perturbation nor supra-floor weight noise raised pre-commit sampling-class entropy on a strict majority of divergent seeds (0/4 and 1/4 against a bar of 2). One live reading was that the levers never reach the stage where the pre-commit distribution is formed. This literature offers a second reading that 708b should be able to separate from the first: both levers may reach the stage and still fail, because both act on the parameters of the pathway that specifies the action rather than injecting an independent proposal into it. If 708b shows the levers *do* reach the distribution-forming stage and entropy still does not move, that is not a null result about noise magnitude — it is evidence that the injection *form* is wrong, and the indicated next build is a separate variability-proposing input rather than a bigger sigma.

## Limitations

The transfer risk here is real and I have priced it at 0.50. This is a songbird vocal-motor circuit producing continuously-parameterised acoustic output; MECH-440 concerns discrete action selection in E3. Adding jitter to a continuous motor parameter is not the same operation as raising entropy over a categorical action set, and I would not want the structural analogy to smuggle in that equivalence. The developmental timescale is also wrong by orders of magnitude — LMAN anneals over days to weeks of ontogeny, MECH-440's self-annealing is a within-training gradient effect. The analogy is structural, not temporal.

And there is a selection worry worth naming: the songbird is *the* canonical system for dedicated variability circuitry, which is exactly why it is the clearest evidence and also why it may not be representative. The Churchland 2010 entry filed alongside is the broader-cortex counterweight, and it complicates this picture rather than confirming it.

`lit_conf` 0.74, reported separately and not blended. MECH-440's `exp_conf` remains unset; V3-EXQ-708a returned a null on both levers and 708b is queued and pending. Tagged GOV-ANALOGY-1: this is neuroscience being mapped onto REE, and the mapping does substantive work in the argument above.
