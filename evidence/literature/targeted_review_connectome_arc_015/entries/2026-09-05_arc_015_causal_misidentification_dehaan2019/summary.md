# de Haan, Jayaraman & Levine (2019) -- more information, worse policy

## What the paper shows

Behavioural cloning reduces policy learning to supervised learning: train a discriminative model to
predict the expert's action from the observation. The authors' point is that such a model is
non-causal -- nothing in the training procedure knows anything about the causal structure of the
interaction between the expert and the environment -- and that this matters far more than it
sounds, because imitation learning is run under distributional shift.

The result is what they call causal misidentification, and its signature is counter-intuitive
enough to be diagnostic: *access to more information can yield worse performance*. The canonical
instance is a policy that learns to key on a variable which is a consequence of the action rather
than a cause of it -- the brake indicator that lights up *because* the expert braked becomes the
model's predictor for braking, and the policy that has access to it performs worse than the policy
that does not. They demonstrate the phenomenon across several benchmark control domains and in a
realistic driving setting, and show that fixing it requires *targeted intervention* -- interacting
with the environment, or querying the expert -- to identify the correct causal model. Adding
passive data does not do it.

## Why this earns a place under ARC-015

The other three entries in this directory establish the claim by two routes: human pathology (what
breaks when the attribution machinery fails) and formal theory (why an agent that ignores its own
influence has an ill-posed learning problem). Both are strong, and both are arguments from outside
the class of system we are actually building. This paper is the measured, artificial-agent
counterpart. Here is a learning system with no representation of who caused what, and here is what
it costs, in benchmark numbers.

Two things transfer particularly cleanly. First, the shape of the confusion: a model treating its
own downstream effect as an environmental predictor is exactly the error a self-impact attribution
channel exists to prevent. Second -- and this is the part I would actually use -- the inverted
scaling gives ARC-015 a cheap, runnable diagnostic. If E3's attribution path is missing or
severed, adding an observation channel should *degrade* competence rather than improve it. That is
a falsifiable prediction we can test on our own substrate rather than argue about, and it is
considerably more tractable than trying to measure responsibility flow directly.

The remedy is the other half of the lesson, and it agrees with the Perdomo entry: intervention, not
more data. Both papers arrive independently at the conclusion that this class of failure is immune
to scaling the observational dataset. For an architecture claim that is a useful convergence,
because it means the missing channel cannot be silently compensated for by a bigger corpus.

## The step I am taking, and want flagged

The confusion in this paper is primarily about the *expert's* causal structure in a cloning setup,
not about the learner attributing its own impact to itself. ARC-015 is a first-person claim. The
bridge -- that a system which cannot represent action-consequence direction in general will also
fail to represent it for its own actions -- is reasonable but is an inference the paper does not
make. Relatedly, the result concerns causal structure broadly; self-caused confounders are the most
damaging instance rather than the only one, so some of the effect size here is not about
self-impact at all. And the domains are benchmark control and a driving simulator, not an embodied
sequential agent of E3's kind.

## Confidence

0.7. Good source, genuinely measured rather than argued, and it hands ARC-015 a testable signature.
Mapping fidelity is the limiting factor at 0.65, for the expert-causality versus self-causality gap
above.
