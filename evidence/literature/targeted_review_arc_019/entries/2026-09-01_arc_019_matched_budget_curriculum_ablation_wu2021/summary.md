# Wu, Dyer & Neyshabur (2021) -- When Do Curricula Work?

**Claim tested:** ARC-019 | **Direction:** mixed | **Confidence:** 0.66

## What the paper did

This is the most methodologically relevant paper in the pull, and its design deserves attention
independently of its result. Wu et al. ask whether ordering training examples by difficulty helps,
and they answer it with an ablation large enough to settle the question in their setting: thousands
of orderings over CIFAR10, CIFAR100 and CIFAR100-with-noisy-labels, spanning three regimes --
curriculum (easy first), anti-curriculum (hard first), and a third arm they introduce called
*random-curriculum*, in which the training set grows over time exactly as it does under a
curriculum but the examples entering it are randomly ordered.

That third arm is the crux. It separates two things that every prior curriculum result had
confounded: the *ordering* and the *dynamically growing training-set size*. Their result is that on
standard benchmarks curricula give only marginal benefits and random-curriculum performs as well or
better -- so whatever benefit exists is attributable to the set-size schedule, not to the ordering
at all. They separately show that the networks have a strong *implicit* curriculum anyway: samples
are learned in a highly consistent order across seeds and architectures regardless of the order
they are presented in.

But they do not stop there, and the second half is what makes this "mixed" rather than "weakens".
Motivated by how curriculum learning is actually used in practice, they test two non-standard
regimes and find that curriculum -- specifically curriculum, not anti-curriculum -- *does* improve
performance under a limited training-time budget, and *does* improve performance in the presence of
noisy data.

## Why this bears on ARC-019, in both directions

Against: ARC-019's CONFIRMING branch asks for the staged arm to beat "an unstaged/ungated baseline
trained on the identical total episode budget and identical eventual feature set". Wu et al. run
that comparison at scale in their domain and find nothing, once the set-size confound is removed.
More usefully, they show REE's currently-specified comparison is *underpowered against a confound
we have not controlled*: an ARM_2-beats-ARM_0 result at matched total budget is still consistent
with the benefit coming entirely from ARM_2's smaller effective early task set. The design lesson
transfers even where the empirical result does not -- a shuffled-phase arm (same phase-size
schedule, phases in random order) belongs in whatever experiment eventually tests ARC-019.

For: REE's regime is *precisely* the two conditions under which Wu et al. found curricula do help.
Developmental training here is episode-budget-constrained by construction, and the learning signal
is noisy. If their conditional holds, ARC-019 should be expected to survive -- but as the weaker
claim, "staging is a budget- and noise-efficiency device", rather than the strong claim that it is
architecturally load-bearing for outcome quality in the limit.

## Limitations

The domain gap is large and I do not want to paper over it. A CIFAR curriculum orders *examples by
difficulty* within an i.i.d. supervised problem where every example is available and learnable at
every point in training. REE's phases order *environment states and feature availability* in a
sequential embodied problem where later phases are not merely harder but structurally unreachable
until earlier competences exist -- an agent that cannot locomote cannot generate the data that
phase 3 is about. That structural dependency has no analogue in image classification, and it is the
main reason a null result there does not straightforwardly refute ARC-019.

Note also the direction of the implicit-curriculum finding. If REE's substrate also imposes a
consistent implicit ordering on what gets learned when, then the explicit gate may be redundant
with something the learner does anyway -- which is a testable prediction, and a cheaper one than
the full staged-vs-flat run.

## Confidence reasoning

`source_quality` 0.85 -- ICLR oral, very large systematic ablation, public code, and the honest
inclusion of the conditions under which their own headline finding does not hold. `mapping_fidelity`
0.60 and `transfer_risk` 0.60 -- both limited by the supervised/i.i.d. gap above. Aggregate 0.66,
deliberately above the component mean, because the paper's contribution to ARC-019 is as much
methodological as empirical: the random-curriculum control is a design REE should adopt, and that
part transfers cleanly regardless of what CIFAR says about curricula.
