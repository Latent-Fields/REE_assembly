# Mesoscale cortex-wide neural dynamics predict self-initiated actions in mice several seconds prior to movement

**Mitelut et al. (2022) — eLife**
DOI: [10.7554/eLife.76506](https://doi.org/10.7554/eLife.76506)
*Based on articles retrieved from PubMed*

## What the paper did

Mitelut and colleagues used widefield calcium imaging -- a technique that captures activity across most of the dorsal mouse cortex simultaneously -- to ask whether there is structured neural activity preceding self-initiated actions, and if so, how early it begins. Mice performed a rewarded lever-pull task under conditions where they could initiate the pull whenever they chose. The team used variance-based analyses and decoding approaches to characterise the temporal profile and spatial distribution of pre-movement signals.

## Key findings

Upcoming lever pulls could be predicted from cortical activity 3-5 seconds before movement, and in some animals even earlier. The spatial pattern was not concentrated in a single area: prediction improved systematically when using all cortical areas versus single areas, pointing to a distributed pre-movement representation. Strikingly, motor cortex showed a biphasic profile -- inhibition starting around 5 seconds prior to movement, followed by activation starting around 2 seconds prior. This inhibition-then-activation sequence is consistent with a preparatory suppression phase that prevents premature execution while the commitment matures, followed by an execution-permitting phase. The authors explicitly argue that the results support structured (not merely random-fluctuation-driven) multi-second volition dynamics in mice.

## REE translation

For Q-015, this paper makes a case that the commitment process is a trajectory, not a point. If the neural precursor of a self-initiated action begins 5 seconds before movement and is distributed across multiple cortical areas, then a commit token that only marks the moment of gate-opening loses the entire pre-commit history that distinguishes a deliberate choice from an impulsive one. In REE, this maps onto the distinction between E3's long-horizon planning phase (when the 'warming up to commit' signal is building across the distributed representation) and the actual commit-gate opening (when E1's sensorium loop is permitted to lock onto the committed action). A minimal token contract that supports multi-timescale attribution needs at minimum a trajectory start time in addition to the gate-open timestamp. The inhibition-before-activation pattern also supports REE's pre-commit/post-commit channel separation: the inhibitory phase maps onto the pre-commit simulation window where the action is mentally rehearsed but execution is actively suppressed.

## Limitations

The mouse lever-pull is far removed from the abstract, ethically-laden commitments that REE models. The timescales observed (3-5 seconds) may not generalise across species or action types -- human planning for complex decisions may extend over hours or days, rendering the specific temporal window uninformative. Calcium imaging captures slow population dynamics but not the fine-grained sequential coding that might resolve the structure of a commit token. The distributed prediction advantage does not resolve whether the pre-commit signal is a single latent variable broadcast across areas or genuinely parallel channels that must be integrated at gate-open time.

## Confidence reasoning

I rate this 0.65. The strongest contribution is the conceptual reframing: commitment is a trajectory with structured multi-second dynamics, not a switch. This constrains what the minimal token contract needs to contain. The confidence penalty is primarily the species transfer risk and the simplicity of the motor paradigm relative to REE's planning horizon requirements.
