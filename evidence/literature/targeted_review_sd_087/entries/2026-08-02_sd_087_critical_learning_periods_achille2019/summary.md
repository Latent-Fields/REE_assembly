# Critical Learning Periods in Deep Networks (Achille, Rovere & Soatto, ICLR 2019)

## What the paper did

Achille and colleagues took a standard deep convolutional network and did something that sounds more like developmental ophthalmology than machine learning: they imposed a simulated sensory deficit -- cataract-like blur -- for a fixed window of training epochs, then removed it and let training continue to convergence. The question was whether the network recovers. It does not. The final performance loss depends on the *onset* and *length* of the deficit window in a way that closely tracks the animal literature on monocular deprivation, and on network size. Crucially, they ran a control: vertical flipping of the images, a deficit that scrambles high-level semantics but leaves low-level image statistics intact. That one produced no lasting impairment at all and was fully overcome with further training.

To explain the dissociation they measured the Fisher Information of the weights as a proxy for effective connectivity between layers. Information rises sharply in the first few epochs and then *falls*, and once the strong inter-layer connections have formed they do not appear to change with additional training. They name this a loss of "Information Plasticity", and argue that the initial learning transient -- under-studied relative to asymptotic behaviour -- largely determines the outcome of the whole training process.

## Why this matters for SD-087

SD-087's evidence_quality_note, written after V3-EXQ-856, leaves two live branches. Either (a) `harm_surprise_pe_enabled` must be set from the *start* of training for SD-020's validated benefit to appear, or (b) the V3-EXQ-664 saturation-and-inversion signature comes from a defect in the encoder or environment rather than from this training-target choice. This paper is the closest published analogue to branch (a), and it supplies a named mechanism rather than an intuition.

The fit to the observed data is uncomfortably good. V3-EXQ-856 flipped the flag on an already-trained agent, and got a clean dissociation: the manipulation demonstrably took (`mean_harm_obs_ema` moved 0.0 -> 0.0245) while the downstream signature did not budge (`mean_cov_z_harm_a` barely moved, far below the 0.05 saturation floor). That is exactly the shape Information Plasticity predicts -- you can change the gradient the network receives, but if the effective connectivity was fixed during the early transient there is nothing left to redistribute. On this reading the 856 `on_reduces_signature` FAIL is the *expected* result of a post-hoc flip, and should not be counted as evidence against SD-087. It is evidence that the falsifier, as designed, could not reach the causal question it was built to ask.

## Limitations, and the part that cuts the other way

I want to be careful not to let a good analogy do more work than it can bear. The paper manipulates the *input distribution*; SD-087 manipulates a *training target* for one auxiliary head, with the data stream unchanged. Those are different interventions, and the paper's own control shows the difference is not cosmetic: the vertical-flip deficit, which left low-level statistics alone, was entirely recoverable. If flipping `harm_surprise_pe_enabled` changes only what `z_harm_a` is regressed against, and leaves the encoder's low-level statistics untouched, then by this paper's own criterion we should expect recovery, not irreversibility. That is a genuine disconfirming route and it is written into the entry's `failure_signatures` rather than buried.

Two further gaps. The effect is reported to scale with network size, and REE's harm head is small -- it may sit outside the regime where information plasticity is lost at all. And the mechanism is defined on the Fisher Information Matrix of the weights, which V3-EXQ-856 did not instrument, so at present the explanation is unfalsifiable against REE's own run.

## Confidence reasoning

Source quality is high (0.85): ICLR, heavily cited, with a mechanistic account rather than a bare empirical curiosity. Mapping fidelity is the binding constraint at 0.62, and since SD-087 is a `design_decision` claim rather than an effect-size claim I have weighted mapping fidelity heavily in the aggregate. Transfer risk sits at 0.35 for the vision-classification-to-RL-harm-regression leap.

I have set the aggregate at 0.72 -- above the component mean, because the paper converts branch (a) from a hunch into a proposition with a measurable signature (compute the FIM on the harm head, or better, run the arm with the flag on from initialization); and below 0.8, because the vertical-flip control is a live route by which this whole mapping could turn out not to apply. Direction is `supports`, scoped to branch (a) of the explanation, *not* to SD-087's literal scoping claim -- that SD-020's validation is flag-on-scoped is a fact about REE's own configuration and claim registry, and no external paper can adjudicate it.
