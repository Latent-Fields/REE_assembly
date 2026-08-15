# Neural circuit underlying individual differences in visual escape habituation

Liu, Lai, Han, Zhong, Huang, Liu, Zhu, Wei, Tan, Xu & Wang (2025), *Neuron* 113(14):2344-2357.e5. DOI 10.1016/j.neuron.2025.04.018. PMID 40347942.

## What the paper did

Repeatedly present a looming stimulus to a mouse and the escape response weakens. The obvious reading is fatigue -- the pathway tires, the response shrinks. This paper argues that reading is wrong, and does so by finding the circuit.

The authors identify parallel routes from superior colliculus to basolateral amygdala. One runs via the ventral tegmental area; the other via the mediodorsal thalamus, which integrates collicular input with insular cortex input and modulates arousal and defensive behaviour. Which route dominates tracks a stable behavioural phenotype. Some animals (T1) keep escaping across repeated presentations and sustain heightened arousal; others (T2) habituate quickly and run at lower arousal. Same stimulus sequence, systematically different decrement.

That last fact is the argument in miniature. If response decrement were adaptation or fatigue, it would be a function of the stimulus history, and animals given identical histories would decrement alike. They do not.

## Why this bears on MECH-489

MECH-489 asserts an "epistemic-sufficiency override" -- the arrest ends when the triggering surprise has been resolved into an identification. The confirmed autopsy on V3-EXQ-910a code-traced `identification_confidence` and found it to be a pure signal-decay and habituation tracker with, in the autopsy's words, zero epistemic content: release is driven by decay of the same channel that triggered the arrest, and no epistemic quantity can influence it. The autopsy called this a decisive finding. The open question it leaves is whether that is a defect or a defensible simplification, and this is the closest biological check on it I could find.

The answer is genuinely two-sided, which is why I have recorded `mixed`.

On one side, it is a partial vindication of building release as habituation. Decrement of a defensive response is not a degenerate non-mechanism in the biology; it is an active, circuit-implemented computation with its own anatomy. "The release is habituation rather than identification" is therefore not, on its own, evidence that something is broken. REE would not be alone in ending a defensive state without having identified anything.

On the other side, the biological version has two properties REE's does not. It is modulated by arousal state, carried on an identifiable pathway -- so the release rate is coupled to something outside the triggering channel itself. And it varies systematically and stably between individuals. A pure decay constant applied uniformly to the trigger channel has neither property. So even granting that habituation is the right family of mechanism, REE's instantiation is the degenerate member of that family.

And there is a third point which cuts against the claim rather than the implementation: the modulating variable here is *arousal*, not resolution of what the stimulus was. If this is the biological template, then the honest reading is that MECH-489's "epistemic-sufficiency" framing may be the part that needs revising -- not because the implementation failed to achieve it, but because it is not obviously what the biology does either. I flag that as a possibility, not a conclusion; see the limitation below, which is severe enough that I would not want anyone acting on this alone.

## Limitations, and the first one is decisive

This is habituation **across repeated presentations**, over a session. MECH-489's `identification_confidence` governs release **within a single arrest episode**. Those are different timescales, and the paper says nothing about within-episode dynamics. Treating across-trial habituation as a model of within-episode release is an extrapolation the authors never make, and I cannot justify it from the data. This single gap is why the confidence sits at 0.58 against a source quality of 0.90 -- the paper is excellent and the mapping is the problem.

Second, the behaviour whose decrement is measured is escape, i.e. flight. MECH-489 arrests. The response being habituated is not the response being released.

Third, mouse, innate, single modality, and the individual-difference phenotypes are a between-animal finding whose analogue in a single REE agent is not obvious.

The right way to use this entry: as a constraint on what a defensible release mechanism looks like, not as evidence about what REE's release mechanism currently does. The autopsy's own code trace is the load-bearing evidence on the latter, and it is experimental evidence, which outranks this.

## Confidence

0.58. Source quality 0.90; mapping fidelity 0.45, the lowest in this directory and deservedly so; transfer risk 0.45. The aggregate sits well below source quality because the timescale mismatch is a real structural gap rather than a caveat I am hedging with. A within-episode study of freeze release would replace this entry outright, and I would welcome it.
