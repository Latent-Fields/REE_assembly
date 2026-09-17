# Cellier et al. (2025, preprint) -- Aperiodic neural timescales in prefrontal cortex dilate with increased task abstraction

## What the paper did

Cellier, Riddle, Hammonds, Frohlich and Voytek recorded human scalp EEG during a cognitive-control task in which the abstraction of task-relevant contextual information was varied. Rather than working with oscillatory band power, they isolated the *aperiodic* component of the signal and estimated neural timescales from its autocorrelation function -- a methodological choice that matters, since it separates the timescale estimate from oscillatory confounds that have muddied parts of this literature. The finding is that these aperiodic timescales dilate over prefrontal regions as task abstraction increases. The integration window, on this measure, is not a constant of the architecture; it expands with what the task demands.

## Why I included a preprint

I included this deliberately and with its weight set low, because it is the only source I found that bears on a question the other four entries cannot touch: is the width of the now a *fixed parameter* or an *actively set* one? That question does not affect whether MECH-021 is true. It affects whether MECH-021's falsifier, as currently specified, can answer it.

MECH-021's discriminative pair holds `theta_buffer_size` at 1 versus the default 10 (and/or `rollout_horizon` at 1 versus 30) for the duration of a run. If the biological window is adaptive -- expanding when more context must be integrated, contracting when it need not be -- then the REE manipulation tests a narrower proposition than the claim states. It tests whether a *fixed wide* window outperforms a *fixed narrow* one. The claim, read fully, is about whether the now functions as a *control surface*, and a surface that cannot be adjusted is a strange sort of control surface. This is the tension I want on the record before anyone runs the experiment.

There is a sharper version of the worry, and it is the one I would want a governance reviewer to see. Suppose REE returns a flat anticipatory-restraint fraction across window settings -- the FALSIFYING branch. On the claim's current wording that reads as "'now' as a horizon-integrating control surface has no substrate content in V3." But if the biological mechanism is adaptive window-setting, a fixed-buffer substrate might produce exactly that flat result while the underlying claim remains true of any system that can set its own window. The falsifier would then be recording an artefact of the implementation as a fact about the architecture. That is worth pre-registering as an interpretive caveat rather than discovering afterwards.

## Limitations -- and they are substantial

I do not want to overstate a preprint. The inferential chain here is long. Aperiodic autocorrelation decay measured at the scalp is several steps from anything one would confidently call the width of an integrated present; the same measure is sensitive to excitation-inhibition balance, so a dilation may index a shift in cortical gain rather than in temporal integration. The abstract does not state a sample size. It has not been refereed, and as of this pull (September 2026) it remains a preprint despite having been posted in April 2025 -- which is itself mild negative information about its reception.

The causal direction is also unresolved, and only one direction helps MECH-021. If timescales dilate *because* more abstract context is being held, the dilation is a consequence and the control-surface reading gains nothing. If they dilate *in order to* hold it, the window is genuinely part of the control apparatus. The paper as it stands cannot separate these, and I have raised transfer risk to 0.55 on that account.

## Confidence reasoning

0.45, which places it below the threshold at which I would let an entry move a claim's standing. Source quality 0.45 (unrefereed, proxy measure, sample size not stated), mapping fidelity 0.60, transfer risk 0.55. Direction is `mixed` and I mean that literally rather than as a hedge: it supports the claim's *spirit* -- the temporal window is bound up with control rather than being inert plumbing -- while complicating the claim's *test*, because REE's fixed per-arm buffer cannot express the adaptivity the finding describes.

The value of this entry is not evidential. It is that it names a design risk in MECH-021's falsifier which no other source in this pull would have surfaced, and which is cheap to mitigate now (by pre-registering the interpretation of a flat result) and expensive to discover after a run.
