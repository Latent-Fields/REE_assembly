# State Entropy Maximization with Random Encoders for Efficient Exploration (Seo et al., ICML 2021)

## Why this paper is in an SD-080 folder

The two other entries in this directory support SD-080. This one is here to argue with it, and I think it earns its place by changing what the claim is actually about.

SD-080's statement leads with the fact that `E2.action_object_head` is "a frozen random projection fixed at initialisation, not the learned world-effect compression SD-004 specifies". Read quickly, the force of that sentence sits on *frozen and random*. RE3 is the cleanest available demonstration that frozen and random is not, by itself, a defect.

## What the paper did

Seo and colleagues need to estimate state entropy in high-dimensional observation spaces in order to use it as an intrinsic exploration reward. Estimating entropy over raw pixels is hopeless, so they compute a k-nearest-neighbour entropy estimate in the low-dimensional output space of a convolutional encoder. The surprise is the encoder: "we find that the state entropy can be estimated in a stable and compute-efficient manner by utilizing a randomly initialized encoder, which is fixed throughout training." No gradients ever pass through it. RE3 then improves sample efficiency for both model-free and model-based RL across DeepMind Control Suite and MiniGrid, and outperforms ICM and RND -- two methods that *do* learn their representations.

So a never-trained random encoder beat two learned-representation methods at the downstream task, and the authors chose it deliberately, on both stability and compute grounds.

## How this bears on SD-080

Two things follow, pulling in opposite directions.

Against SD-080 as framed: the inference "the head is a frozen random projection, therefore the space it defines is unfit for its consumer" does not go through. Random projections approximately preserve the geometry of whatever they are given, which is exactly why the k-NN estimator works in RE3's space, and it is why one cannot conclude from frozen-ness alone that a downstream geometric computation is impaired. If SD-080 is presented to governance as "it's random, so it's broken", that presentation is not supported.

For SD-080 as measured: and this is the part I find genuinely clarifying. If REE's head is a random *linear-ish* map applied to `(z_world_t, a_t)`, and `z_world` demonstrably varies across states -- the spike's control confirms it, total variance 0.0031, mean per-dimension std 0.0096, and the same variation drives `world_forward` perfectly well -- then a random projection should have *inherited* that variation. It did not. The measured between-state variance of the action-object output is about 6e-05, `r2_explained_by_action_alone` is 0.9947, and the pairwise-distance matrix across five actions is the same in every one of 120 sampled states to within 1%. A random map does not do that to a varying input. Something else is doing it: initialisation scale, a saturating nonlinearity, a concatenation where the action term dwarfs the state term, or an architectural path where `z_world` barely reaches the output at all.

That reframes the defect, and I think usefully. SD-080's load-bearing content is not "the head is random" -- it is "the head is state-invariant", which is a stronger and stranger finding than randomness predicts. A repair that only connects a gradient to the head, without diagnosing why the state input is being annihilated in the first place, may well train a head that is *still* state-invariant, because the gradient would have to fight whatever is currently suppressing that pathway.

## Limitations and caveats

The analogy is structural, not empirical. RE3 encodes states for an entropy estimate; REE's head encodes state-action pairs for a CEM search. The two consumers want different things. RE3 needs only that distances be roughly preserved, which any random projection of sufficient width will give it. SD-004 needs something much stronger -- that distance in O *track similarity of world-effect*, so that two actions with the same consequence embed alike. No random map supplies that, however well-conditioned. So nothing here says REE's frozen head is acceptable. It says the argument against it has been aimed at the wrong property.

There is also a practical warning worth recording. RE3's authors chose the random encoder partly because it is cheap -- no gradient updates, no extra forward passes, latents cacheable in the replay buffer. If REE builds the SD-080 repair, the experiment should carry a frozen-but-non-collapsed control arm, not merely frozen-versus-learned, or it will not be able to tell "learning the map helped" apart from "un-annihilating the state input helped".

## Confidence reasoning

0.62, and filed as `mixed` rather than `weakens`. Source quality is high. Mapping fidelity is the weak component -- deliberately, because this paper speaks to SD-080 by contrast rather than by test, and an entry whose contribution is analytic should not carry the same weight as one that probes the mechanism. It is `mixed` because it does genuinely both things: it undercuts SD-080's framing and it corroborates SD-080's measurement, by making the state-invariance result harder to explain away as a mere consequence of being untrained.
