# Causal Confusion in Imitation Learning (de Haan, Jayaraman & Levine, NeurIPS 2019)

## The result

Behavioural cloning trains a discriminative model to predict the expert's action from the
observation. de Haan and colleagues point out that this procedure has no access to the causal
structure of the expert-environment interaction, and that under the distribution shift imitation
learning inevitably induces, that ignorance is actively harmful. Their headline finding is stated as
a paradox and is worth quoting in the form they give it: *access to more information can yield worse
performance*. The canonical instance is a driving agent given a dashboard brake indicator. The
indicator is a downstream *effect* of the expert's braking, and it is a near-perfect predictor of
the action to be cloned. The cloner latches onto it, the training loss falls, and the deployed
policy is broken -- because at deployment the indicator is a function of the agent's own past
action, not of the world state that should trigger braking. They reproduce the phenomenon across
several benchmark control domains and a realistic driving setting, and offer a remedy based on
targeted interventions (environment interaction or expert queries) to identify the correct causal
model.

## What it evidences for INV-104

Two of INV-104's assertions, and one of them is the assertion the claim most needs external support
for.

The first is class 4. INV-104 lists causal ancestry and intervention handles -- agent identity,
action class, preconditions, uncertainty over causal contribution -- as a preservation requirement in
its own right, not as something that falls out of getting prediction right. The natural objection is
that this is redundant: a representation good enough to predict is surely good enough to act. de Haan
et al. are a counterexample in the sharpest available form. Their model is not merely predictively
adequate, it is predictively *excellent*, and it is causally wrong, and the wrongness is what breaks
it.

The second is condition (ii) -- "the losses do not see it". INV-104 requires that restoring class-k
access must not visibly move reconstruction or one-step prediction loss, on pain of the result being
indistinguishable from generic representation learning. That requirement can look like a hedge until
you see a system in which the loss curve is clean throughout a catastrophic representational failure.
This is that system. The training objective registers the causal misidentification as an improvement.

There is a third, sharper lesson that cuts *against* an easy reading of INV-104. The preservation
contract might tempt one to satisfy it by preserving more -- widen z_world, keep everything, let
downstream sort it out. Causal misidentification says that does not work: it is a failure caused by
adding an informative variable. Preservation of the five classes is not monotone in retained
information, which means the contract cannot be discharged by capacity.

## The limits of the mapping

The unit of analysis differs. de Haan et al. study what a policy conditions on; INV-104 studies what
survives a compression. The shared mechanism -- correlational sufficiency masking causal inadequacy
-- is real, but the identification is analogical, and I would not want an INV-104 falsifier to cite
this as though it were a measurement of z_world.

More consequentially, their remedy does not port. Identifying the correct causal model requires
intervention: either acting in the environment under a modified policy, or querying the expert. The
observation -> z_world encoder has neither. So this paper diagnoses the failure INV-104 predicts
without indicating how the contract could be satisfied at that site. It is also worth being plain
that class 4's REE substrate (MECH-430, the multi-dimensional provenance source vector) is scoped v4
and unbuilt; this entry supplies motivation for it, not evidence that it works.

One methodological note that matters for the falsifier as written: causal misidentification is
invisible on-distribution. It appears only once the agent's own actions move the state distribution.
An offline probe on a frozen dataset -- T1, and arguably T2 as currently specified -- cannot see it.
A high R_k for class 4 would therefore not establish that intervention handles were preserved in the
sense that matters, and if class 4 ever gets a falsifier it will need an interventional or
closed-loop leg that classes 1 and 2 do not.

## Confidence

0.68. Strong source, independently reproduced phenomenon, direct bearing on the claim's hardest
clause -- discounted for the policy-input/compression-output shift and for the fact that the paper's
constructive half is unavailable at the site INV-104 constrains.
