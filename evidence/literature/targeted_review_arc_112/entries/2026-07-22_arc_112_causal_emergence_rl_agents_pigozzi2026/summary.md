# The Causally Emergent Alignment Hypothesis (Pigozzi & Levin, 2026) -- ARC-112, Q-081

## What the paper did

Pigozzi and Levin take the causal-emergence machinery from the Rosas/Mediano line and run it on
reinforcement-learning agents. For each agent they record the latent representation z_t produced by
the feature extractor at every step, compute the lag-1 mutual information matrix over the latent
units under a Gaussian approximation, and solve for the PhiID atoms; causal emergence is the sum of
the downward-causation and causal-decoupling atoms. They do this across six Gymnasium-family
environments arranged on a complexity spectrum (Pendulum, LunarLander, BipedalWalker, Walker2D,
Ant, CrafterReward), two architectures (MLP and GRU, chosen to contrast static against temporally
dependent inductive biases), and two algorithm families, over each agent's whole training lifetime.
Code is released.

Two headline results. Causal emergence's trajectory in embedding space aligns globally with the
direction of reward improvement -- 0.99, 1.00, 0.86, 0.35, 0.49 in five environments -- and,
measured over only the first 20% of training, it predicts final reward better than baseline
representation metrics.

## Why this is in the pull

Search 10 was told to prefer literature yielding a computable quantity over literature yielding a
vocabulary, and this is the only item found whose *substrate* is REE's own kind of object: trained
neural-network agents with latent states, not brains and not cellular automata. The Rosas et al.
entry in this directory supplies the criterion; its worked examples are flocking models and
Gaussian systems, which leaves open whether the estimator survives contact with a learned
representation. This paper closes that gap. The pipeline -- per-step latent trace, lag-1 MI matrix,
Gaussianisation, PhiID, causal emergence -- runs, produces a non-degenerate quantity, and beats a
random-projection null.

For ARC-112 that converts "compute Psi over REE's streams" from a proposal into a procedure with
an implementation someone has already debugged.

## The three things that hold it down, and one of them is a gift

**The macro variable was chosen for tractability, not for meaning.** The authors state plainly that
they "cannot handle systems with many parts due to the combinatorial complexity", so they reduce
dimensionality with a minimum-information bipartition -- bisecting the latent graph via the Fiedler
vector, averaging within each half, and comparing the two halves' dynamics to the whole. Their own
analogy is slicing a watermelon and asking how well the seed count in one half predicts the other.
That is emergence across an *algorithmically chosen split of one homogeneous layer*. REE's question
is emergence across *named heterogeneous streams* with different dimensionalities and different
update clocks. Those are not the same measurement, and the bipartition was adopted precisely to
dodge the combinatorics that REE's multi-stream case would incur. This is the single largest gap
between the paper and our use.

**The quantity may not be doing distinct work.** The authors ran the right control and reported the
unflattering answer: causal emergence's alignment scores were significantly above random
projections but *not* significantly different from those of standard representation metrics
(entropy, Shannon mutual information, autocorrelation, effective dimension, latent magnitude). They
conclude it "did not capture a quantitatively different direction but instead summarized
information scattered across many (weaker and heterogeneous) signals". That is a discriminant-
validity failure, and for us it is the gift -- because it is exactly the control REE's prospective
run should copy. Report the causal-emergence statistic alongside those five cheap metrics computed
on the same traces, and treat any result that a cheap metric reproduces as uninformative about
ARC-112. Without that control, a positive Psi in REE could be autocorrelation wearing a costume.

**The sign flipped.** Global reward alignment was strongly positive in five environments and
-0.95 in CrafterReward, which the authors attribute post hoc to more time spent on early
exploration. A quantity whose relation to function reverses with the task is not behaving like a
substrate-independent organisational invariant, which is what search 10 was hunting for. It might
be a real effect with a real explanation; the paper does not establish one.

A fourth, narrower point matters for Q-081 specifically. Local, step-by-step alignment was
approximately zero in *every* environment -- the quantity tracks slow representational drift across
training, not moment-to-moment coordination. Q-081 asks whether REE's streams occupy shared
recurrent configurations per step. This measurement operates on a completely different timescale
and cannot address that question, however tempting the shared vocabulary makes it look.

## Caveats on the estimator

Gaussian information theory assumes joint normality. The authors apply a copula-based rank-normal
transform and report that 28.53% of units still reject normality on a D'Agostino K2 test. So the
numbers come from a linear-Gaussian approximation to non-Gaussian neural activations -- acceptable,
disclosed, and worth carrying forward as a known source of bias rather than treated as solved.

This is not a neuroscience source, so GOV-ANALOGY-1 is not engaged.

## Confidence reasoning

0.45. It is an unrefereed preprint, and the macro variable it measures is not the one ARC-112
needs. What earns it a place rather than a footnote is that it is the only demonstration that this
machinery runs on a learned agent at all, that it releases code, and that it ran and published its
own negative control -- which is both a mark of quality and the most directly useful thing in it
for us.

Direction is `mixed`: it supports the feasibility half of ARC-112's programme and simultaneously
supplies the strongest reason to doubt that a positive causal-emergence result in REE would mean
anything on its own.

lit_conf only. exp_conf on ARC-112 and Q-081 remains 0.0.
