# Lipton et al. (2016) -- a harm signal that is load-bearing in an artificial agent

## What the paper did

Lipton and colleagues address what they call deep reinforcement learning's Sisyphean curse: agents
periodically revisit catastrophic states, not because they never learned to avoid them, but because
function approximation causes them to forget experiences that have become unlikely under the current
policy. "For as long as they continue to train, DQNs may periodically relive catastrophic mistakes."

Their intervention is intrinsic fear: a separate fear model trained to predict the probability of
imminent catastrophe, whose output penalises the Q-learning objective. They bound the reduction in
average return caused by optimising the perturbed objective, prove robustness to classification
errors in the fear model, and report that "on Adventure Seeker, all Intrinsic Fear models cease to
'die' within 14 runs, giving unbounded reward thereafter," with improvements on several Atari games.

## Key findings relevant to the claim

Of the four entries in this pull, this is the one on REE's own side of the biological/artificial
divide, and its architecture is the closest structural match. A learned model predicts harm; that
prediction discounts the value of trajectories that approach it; the agent's terminal-state
avoidance depends on that discounting. That is REE's harm gradient feeding E3's harm-weighted
trajectory scoring, implemented in a simpler system and with the ablation actually run. Removing the
danger signal does not leave behaviour unchanged -- it produces an agent that repeatedly dies.

The result also speaks to a subtlety in INV-095's framing. The claim's falsifier imagines a signal
that might be "architecturally decorative." Lipton et al. exhibit a failure mode more interesting
than decoration: a signal that is load-bearing but *forgettable*. Their agents had learned the
hazard and lost it, because nothing in the architecture kept the representation alive once the
policy moved away. That is a third possibility between load-bearing and decorative, and it suggests
the REE experiment should measure hazard-avoidance over training time rather than only at
convergence. A signal that matters early and decays could look decorative in an endpoint
measurement.

## How this translates to REE

The most useful thing this paper contributes is a constraint on the experiment, not a vote on the
claim. The authors prove robustness to classification errors: the fear model can be substantially
wrong and the behavioural benefit survives. Transposed to INV-095's falsifier, that is a warning
with teeth. If REE's harm signal is replaced with a noise substitute that is only partially
decorrelated from hazard -- or matched on marginal statistics while retaining some usable structure
-- the architecture may absorb the corruption and show no measurable degradation, *even though the
signal is genuinely load-bearing*. The falsifying observation as written ("no measurable
degradation") would then be recorded, and it would be wrong.

So the successor to V3-EXQ-533 needs a manipulation check: a positive demonstration that the noise
substitute is in fact uninformative about hazard, measured directly (for instance, that a probe
trained on the substitute cannot predict hazard above chance), before any null on the behavioural
readout is interpreted. Without that, a null is ambiguous between "the signal is decorative" and
"the noise was not noisy enough." Given that V3-EXQ-533 already returned
`non_contributory/measurement_test_design_defect`, this is exactly the class of defect worth
designing against explicitly.

## Limitations and confidence reasoning

Source quality is the weak term. This is an unrefereed arXiv preprint; it was submitted to ICLR 2017
(OpenReview `r1tHvHKge`) and not accepted, and the evaluation is a toy pathological environment plus
Atari games rather than anything with the structure of REE's world. The theoretical results are the
more durable contribution.

There are three mapping boundaries. The contrast is presence versus absence of the fear model, not
intact versus distribution-matched noise, so like Cox (2006) it establishes necessity rather than
informativeness. The fear model is a bolt-on shaping term over a standard DQN, whereas REE's harm
gradient is architecturally integral -- `ResidueField`, `z_harm_a`/`z_harm_s`, the amygdala analogue
(SD-035), dACC (MECH-258) -- and feeds a model-based selector rather than a model-free Q-function;
deleting an add-on and corrupting an integral signal are not the same perturbation. And "catastrophe"
here is an environment-defined terminal state, narrower than REE's commitment-relevant behaviour.

One further confound the authors themselves flag as a benefit: "IF models tend to learn faster,
owing to reward shaping." Faster learning could reduce catastrophe counts without the danger signal
being load-bearing at convergence, which muddies the ablation somewhat.

Confidence 0.66. Transfer risk is the lowest in this pull at 0.20 -- artificial to artificial, no
species inference -- and mapping fidelity is high at 0.78. Source quality of 0.62 is what holds the
aggregate down. I have not weighted it lower than that despite the venue, because the architectural
correspondence is what this entry is being asked to carry, and that correspondence does not depend
on the empirical results being definitive.
