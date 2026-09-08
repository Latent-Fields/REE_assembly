# Learning Invariant Representations for RL without Reconstruction (Zhang et al., ICLR 2021)

## What the paper did

Zhang and colleagues attack a problem that is structurally identical to the one INV-104 names: an
encoder that compresses rich observations into a latent for downstream control, trained on a loss
that does not know what the agent needs. Their diagnosis is that pixel reconstruction allocates
representational capacity in proportion to pixel variance, and pixel variance is not consequence.
Their fix is to train the encoder so that L1 distance in latent space equals the bisimulation
distance between the underlying states -- two states are near each other in the latent exactly when
they are behaviourally interchangeable, in the technical sense of yielding the same reward and the
same transition distribution over aggregated states. They test it on DeepMind Control Suite tasks
whose backgrounds have been swapped for moving distractors and natural video, and on a CARLA
first-person driving task where the nuisance variation is clouds, weather and time of day.

## What it evidences for INV-104

The paper is the cleanest external statement I have found of INV-104's most awkward clause: that a
compression step can destroy downstream access to something consequential *regardless of
reconstruction or prediction loss*. That clause is what stops INV-104 collapsing into ordinary
representation learning, and it is also the clause most likely to be dismissed as a technicality.
Zhang et al. show it is not a technicality -- it is the failure mode a whole line of work exists to
route around. The distractor benchmarks are constructed precisely so that the reconstruction
objective can be satisfied while the control-relevant distinctions are starved of capacity, and the
reconstruction-based baselines (SAC+AE, and the Dreamer-family comparisons) degrade under exactly
that manipulation.

For the V3 instantiation this matters at one specific site. INV-104's falsifier is written for the
observation -> z_world step in `ree_core/latent/stack.py` (SplitEncoder world path, SD-005), and
condition (ii) requires that restoring class-1 access must NOT visibly move `world_obs`
reconstruction loss or E2 one-step prediction MSE -- otherwise the result is indistinguishable from
generic representation learning. Zhang et al. supply the reason to expect that dissociation is real
and measurable rather than a hedge: they built a benchmark family out of it.

## Where the mapping stops

I want to be careful not to over-claim this. Bisimulation is a *narrower* preservation criterion
than INV-104's, not a formalisation of it. Bisimulation says: keep what changes reward or dynamics
now. INV-104 says: keep five classes of distinction consequential to the organism *across time*,
including persistence and temporal relation (class 3), causal ancestry and intervention handles
(class 4), and independently evolving trajectories (class 5) -- several of which are, at any given
moment, reward-neutral. A DBC-trained encoder would discard those and be behaving correctly by its
own lights. So the paper supports INV-104's negative half (reconstruction is not the criterion)
considerably more strongly than its positive half (these five classes are the criterion). Read as
support for the positive half, it would actually be evidence for MECH-520's counter-constraint --
that preservation by current relevance alone over-compresses.

The second limit is the oracle. In these benchmarks the experimenter *knows* which variation is
task-irrelevant, because they inserted it. REE has no such oracle over its own environment, which
is why INV-104 carries NDP-3: without a raw-input ceiling arm showing the class is determinable
from the encoder's own input at >= 0.90, a "not preserved" verdict is a statement about the
environment, not about the compression.

## Confidence

0.74. The source is strong -- ICLR 2021, code released, and the critical literature that has grown
around bisimulation representations in offline RL is itself evidence that the result was taken
seriously enough to stress-test. The discount is entirely on mapping fidelity: this is a
simulation-only, benchmark-control result whose notion of what must survive is a proper subset of
INV-104's, and whose invariance is defined against a fixed reward at a fixed developmental moment,
which sits awkwardly with INV-104's requirement that the ontology within a class stay free to split,
merge and reweight over development.
