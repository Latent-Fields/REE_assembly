# Churchland et al. 2010 — stimulus onset quenches neural variability

**Claim:** MECH-440
**Direction:** mixed · **confidence 0.70**

## What the paper did

This is a survey with unusual reach. Fourteen datasets, seven cortical areas across all four lobes, monkeys and cats, extracellular single units, intracellular membrane potential, and correlated variability measured on 96-electrode arrays. In every case, the onset of a stimulus caused response variability to decline.

Two features of that result do the work here. First, the decline happened *even when the stimulus produced little change in mean firing rate* — variance and mean move independently. Second, it happened for every stimulus tested, in every area, whether the animal was awake, behaving, or anaesthetised. The authors' proposed interpretation is that this reflects a general property of cortex: its state is stabilised by input.

## Why this bears on MECH-440 and on the 708a null

The pull was owed on a specific question — what modulates the spread of the pre-commitment distribution, and how are multiple candidates kept live up to commitment. This paper speaks to the second half directly, and it does so in a way that complicates MECH-440 rather than confirming it.

The supporting reading is straightforward. There is a genuine high-variability regime before drive arrives, and it collapses as the network is pushed toward a determinate response. So the stage V3-EXQ-708a was probing — a pre-commit distribution with a modulable spread — is not an artefact of the software architecture. Biology has one, and its spread really is regulated.

The complicating reading is the one I think matters more, and it is a candidate explanation for the null that 708a returned.

Recall the autopsy's finding: with a demonstrably working instrument — 862 fresh E3 `select()` calls against a floor of 30 — neither a temperature perturbation nor supra-floor weight noise raised pre-commit sampling-class entropy on a majority of divergent seeds (0/4 and 1/4 against a bar of 2). The reading recorded at the time was that the levers may never reach the stage where the pre-commit distribution is formed. Churchland 2010 suggests a second possibility that would look identical from the outside: the levers reach it, and the stage suppresses the variance they inject. If cortex stabilises under drive as a general property, then variance injected upstream of a strongly input-driven selection stage should be expected to be attenuated *by default*. Propagation is the thing that needs explaining, not attenuation.

The first finding above makes this worse in a way worth stating explicitly as a methodological warning. Variability declined even where the mean barely moved. That means a lever can be verified as live by its effect on the mean while its variance contribution is independently killed. Any instrument check that confirms "the knob is reaching the pathway" by looking at mean-level effects does not thereby establish that the variance survives to commitment — and those are exactly the two things 708b needs to separate.

So the practical value of this entry is discriminative. If 708b shows the levers *do* reach the distribution-forming stage and entropy still does not move, the indicated conclusion is not "we need more noise." It is that the injection form is being actively suppressed at the commitment stage, which — read together with the Ölveczky 2011 entry filed alongside — points toward a separate variability-*proposing* input rather than a larger perturbation on the selection head's own parameters. Those two entries were pulled independently and converge on the same design implication, which is the main reason I would not treat either as merely contextual.

## Limitations, and they are substantial

I am mapping a sensory phenomenon onto a decision-commitment stage, and I should not pretend otherwise. "Stimulus onset" in visual or premotor cortex is not "commitment" in E3's selection pathway. This paper does not test action selection under uncertainty at all; it tests responses to stimuli, largely in sensory areas. The state-stabilisation-by-input frame is the authors' proposed interpretation, not a demonstrated mechanism, and my extension of it to "the pre-commit action distribution gets quenched" is an extrapolation on top of an interpretation.

There is also a measurement mismatch that no amount of care dissolves. Variability here is trial-to-trial variance in spike count and membrane potential. MECH-440's observable is entropy over a discrete action set at argmax. These are not the same quantity, and there is no clean correspondence between them.

For those reasons I have set mapping fidelity at 0.50 and transfer risk at 0.55 despite source quality near ceiling at 0.92, giving 0.70 overall. I want the record to be clear that this entry is filed as a **hypothesis-generator for interpreting the queued V3-EXQ-708b**, not as evidence bearing on MECH-440's falsifier. It should not be counted as support for the claim's mechanism.

`lit_conf` 0.70, reported separately per standing discipline and not blended with `exp_conf`, which for MECH-440 remains unset. Tagged GOV-ANALOGY-1 — neuroscience mapped onto REE, with the mapping load-bearing and, here, admittedly stretched.
