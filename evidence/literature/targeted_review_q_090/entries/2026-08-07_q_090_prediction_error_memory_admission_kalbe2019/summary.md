# Kalbe & Schwabe 2020 -- a magnitude signal really does decide what gets kept

**Claim tested:** Q-090 -- is the retained-alternative admission criterion the same scale as the interrupt threshold at a lower cut, or an independent relevance criterion?

**Direction:** supports the same-cut-scale horn. **Confidence: 0.5.**

## What the paper does

The starting puzzle is an old one. Things you saw shortly before something bad happened are remembered well, and for decades the explanation was arousal: the aversive event floods the system, and the flood consolidates whatever was nearby. Kalbe and Schwabe ask whether that is the whole story, or whether what actually does the work is the *unpredictedness* of the bad event rather than its badness.

The design is a Pavlovian fear-conditioning paradigm with incidental encoding stitched into it. Participants see neutral pictures from two categories, one of which carries shock risk. Skin conductance indexes arousal; trial-by-trial explicit shock-expectancy ratings yield an unsigned binary prediction error. A surprise recognition test follows about a day later. Experiment 1 finds both effects present and, critically, model fits showing the prediction-error contribution is dissociable from the arousal contribution. Experiment 2 replicates and extends, showing the memory-promoting effect of prediction error survives controlling for arousal.

## Why it bears on Q-090

Of the five sources in this pull, this is the one that speaks most directly to the mechanism the same-scale horn needs. That horn requires that a scalar magnitude signal be capable of gating admission to retention -- that "retain if magnitude exceeds a low cut" is a thing a nervous system does. Kalbe and Schwabe show it is. A quantity of the prediction-error family determines what gets kept, and it does so as a mechanism in its own right rather than as an epiphenomenon of general activation.

The arousal control matters more than it might look. Arousal is precisely the confound that would let a magnitude story appear true while something else drove the retention. Having it excluded means the magnitude term is doing real causal work.

## Caveats and where the mapping strains

Here is the honest problem, and it is not small: the paper rules out the wrong rival.

Q-090's contest is magnitude-versus-goal-match. Kalbe and Schwabe's contest is prediction-error-versus-arousal. Goal relevance was never manipulated, never measured, and has no place in the design. Nothing in these results excludes a reading on which what actually gated encoding was relevance to the participant's current goal -- which in a shock paradigm is "do not get shocked", and which therefore correlates almost perfectly with shock-predictiveness. Both horns of Q-090 predict this paper's result. That is why the mapping fidelity is set low and why it, not the source quality, sets the aggregate.

Two further strains. The retained item here is an experienced percept -- a picture that was actually on the screen. MECH-485 leg 3 retains something categorically different: an alternative that was *computed and not acted on*, a branch of a forward rollout with no perceptual trace at all. Whether the machinery that admits a seen object to episodic memory is the machinery that admits a rejected plan is an open question this paper does not touch, and I am not willing to assume the identity.

And the prediction-error construct is binary and unsigned. The same-scale horn does not merely need "prediction error promotes encoding"; it needs a *continuous* scale on which a second, lower cut-point can be placed. A binary predictor is compatible with that but does not demonstrate it. The fear-conditioning frame also pins valence to harm, so MECH-485's predicted-*success* magnitude gets no coverage here at all.

## Confidence reasoning

Source quality 0.75: peer-reviewed, two experiments, an internal replication that specifically adds the control the paper's argument turns on, and explicit trial-wise computational modelling. Held below 0.8 by modest sample sizes typical of the paradigm and by the coarse PE construct. Mapping fidelity 0.45: the right mechanism family, the wrong contrast, and a different kind of retained object. Transfer risk 0.5 for the laboratory-to-agent leap plus the aversive-only valence restriction. Weighting mapping fidelity heavily gives 0.5 -- a record that the magnitude mechanism is real and demonstrated, paired with a frank admission that this study could not have distinguished the two horns even in principle.
