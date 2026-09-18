# A simple unified framework for detecting OOD samples and adversarial attacks (Lee et al., 2018)

## What the paper did

Take a deep classifier that is already trained. Do not touch it. Fit class-conditional Gaussians to
its intermediate feature activations -- low-level and high-level layers both -- under Gaussian
discriminant analysis, and score a test sample by its Mahalanobis distance to the nearest class
conditional. That score turns out to detect both out-of-distribution inputs and adversarial
examples better than methods that read the network's softmax output, across standard image
benchmarks, and it holds up when the training labels are noisy or the training set is small.

The motivating sentence in the abstract is the one that matters for us: deep networks with a
softmax classifier "are known to produce highly overconfident posterior distributions even for such
abnormal samples."

## Why this is the entry I most wanted for MECH-042

The other four entries in this directory transfer across a substrate gap -- a neonate, an epileptic
brain, a concurrent program, a spacecraft. This one does not. It is a neural network with
intermediate activations, probed by an instrument attached from outside, and REE is a neural
network with intermediate activations. Transfer risk is the lowest in the file (0.3) for that
reason alone.

And it supports both halves of MECH-042 at once, which none of the others do.

On the **read-only** half: the detector requires no retraining, no gradient, no modification of the
forward computation. It is an instrument bolted onto a pre-trained network that carries on
computing exactly what it computed before. That is a stronger and more directly relevant prior for
sub-claim (1) than Gait's concurrent-programs result -- Gait tells us non-interference is
conditional, this tells us the condition is routinely met in precisely REE's kind of system.

On the **diagnostic value** half: the paper's whole premise is that internal representation carries
abnormality information the output surface does not expose, and worse, that the output surface is
*confidently wrong* about it. Translated: a detector reading `current_precision`,
`running_variance`, commit-readiness state and mode telemetry ought to be able to identify an
abnormal internal regime while harm and reward still look nominal. That is MECH-042's intuition in
its own substrate.

## The disanalogy that keeps this at 0.65

There is no time axis. Lee et al. compare two detectors on a *static, per-sample* decision, and
what they show is that internal features are more informative *at the same instant*. MECH-042
sub-claim (2) asks something strictly stronger: that the telemetry detector fires *earlier* on a
temporally-extended trajectory.

Those come apart. A channel can be strictly more informative and still confer zero lead time, if
the behaviour stream degrades at the same moment. So this paper supports the informational premise
that sub-claim (2) rests on, without testing the temporal assertion sub-claim (2) actually makes.
Mapping fidelity 0.55 is that gap, and I would rather record it than let the substrate match do
rhetorical work the design does not support.

Two smaller ones. The abnormality here is an out-of-distribution or adversarial *input*, whereas
MECH-042 injects a fault in the system's own control plane -- an internal pathology with no
distributional shift at the input at all. And the detector is a learned statistical model fitted on
a calibration corpus, considerably heavier than the pre-registered threshold-style detector the
claim envisages.

## Two design constraints this hands to the experiment

The calibration question. Lee et al.'s detector needs class-conditional statistics estimated from
training data -- a corpus of "normal". MECH-042's telemetry detector needs the same thing, and the
claim as written does not say where it comes from. If the calibration corpus is drawn from the same
runs on which lead time is then reported, the result is in-sample and uninterpretable. The Mormann
entry in this directory documents that exact mistake costing a field three decades, so this should
be settled before the run, not after.

The channel-selection question. Performance here depended on which layers were used and on
ensembling across them. The REE analogue is that lead time will depend on which of the seven-plus
telemetry channels the detector reads -- and a channel set chosen after seeing the pathology runs
would inflate the result just as surely as a threshold chosen that way. Fix the channel set in
advance, alongside the threshold rule.

## One thing that would strengthen the claim if it holds

The paper's premise that the output surface is *confidently wrong* on abnormal inputs, rather than
merely uninformative, has a sharp consequence if it carries over. If REE's behaviour stream looks
nominal under an injected control-plane pathology -- not noisy, but nominal -- then the
behaviour-stream detector is systematically biased and not simply slower. Matching false-alarm
rates on control runs would not correct for that, because the bias appears only on pathology runs.
That is worth checking directly, and it would convert a lead-time result into something rather
more interesting than a lead-time result.

## Confidence

0.65. Source quality 0.8 (NeurIPS 2018, very heavily cited, long since a standard baseline),
mapping fidelity 0.55, transfer risk 0.3.
