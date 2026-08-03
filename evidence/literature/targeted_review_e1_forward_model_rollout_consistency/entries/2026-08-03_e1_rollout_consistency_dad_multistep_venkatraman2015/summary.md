# Venkatraman, Hebert & Bagnell 2015 -- Data as Demonstrator

**Claim(s):** MECH-135 | **Direction:** supports | **Confidence:** 0.74

## What the paper did

This is the paper that states our failure mode in its general form, and states it better than anything else I found. The setup: most statistical and machine-learning approaches to time-series modelling optimise a *single-step* prediction error. To simulate multiple steps you iterate the model, feeding the previous output back in as the new input. The authors' observation is that this quietly breaks the assumption the training procedure rested on -- "these compounding errors change the input distribution for future prediction steps, breaking the train-test i.i.d assumption common in supervised learning."

That reframing is the contribution. Compounding error is usually described as an *accuracy* problem: small errors multiply. Venkatraman and colleagues point out that it is more precisely a *distribution-shift* problem. By step k of a rollout, the model is being asked to predict from a state that no training example ever presented to it. Its one-step accuracy was measured under a distribution the rollout departs from immediately, so that accuracy carries almost no information about rollout quality.

Their fix follows from the reframing. If the problem is that the model visits states its training data does not cover, treat multi-step prediction as imitation learning and let the training data act as a *demonstrator* that supplies corrections. Data as Demonstrator (DaD) rolls the current model forward, collects the states it actually drifts into, pairs each with the ground-truth continuation from the original data, adds those pairs to the training set, and refits -- iterating. It is a no-regret meta-algorithm in the DAgger family, and it is architecture-agnostic: no change to the model class, no change to the loss form, only to what the model is trained on.

## How this maps to REE

The 108b driver trains E1 by `agent.e1(total_prev, horizon=1)` under MSE against the next real transition, and then `_score_sequence_e1coe_with_endpoint` iterates that same E1 thirty times, feeding each prediction back in. That is, exactly and without any reinterpretation on my part, the construction this paper is about. Where the PlaNet entry required me to argue about whether a technique developed for variational RSSMs transfers to a deterministic LSTM, this paper's claim is about the *construction* rather than the architecture, so it applies to E1 directly.

It also grounds the autopsy's second named candidate. "Scheduled multi-step unrolling during training (curriculum from 1-step to N-step)" is a reasonable instinct; DaD is the principled version of that instinct, with a reduction argument behind it. For REE the concrete shape would be: roll the current E1 forward from real start states, harvest the (drifted-prediction, true-next-state) pairs along its own trajectory, add them to E1's training set, refit, repeat. No architecture change and no new loss form -- which makes this the cheapest of the four interventions surveyed in this review, and therefore the natural first thing to try.

## Limitations and the caveat that matters most

Three boundaries, and I want to be blunt about the third because it is the one that constrains the substrate recommendation.

The no-regret guarantee is an imitation-learning reduction over a hypothesis class, demonstrated on the era's linear and shallow time-series models operating on observable state. E1 operates on a *learned* latent, and the ground-truth correction target for a drifted z_world is itself an encoder output that can move while the encoder trains. The guarantee does not obviously survive that; the intuition does.

The paper is a decade old and predates deep latent-dynamics work entirely. Read it for the diagnosis and the cheap first intervention, not as a current state-of-the-art recommendation.

And the one that matters: **DaD corrects distribution shift along a rollout; it does not create discriminative structure the model's inputs cannot express.** E1's transition takes no action argument at all. A DaD-trained E1 would track the real trajectory distribution much more faithfully over thirty steps, and the forty candidate action sequences would still reach z_world only through the z_self-to-`prior_generator` bottleneck. On my reading, DaD alone should not be expected to move C3. That is not an argument against doing it -- a rollout that stays on-distribution is worth having on its own terms, and it is cheap -- but it should not be sold to governance as the fix.

## Confidence reasoning

Source quality 0.80: AAAI 2015, well-cited, Bagnell's group; solid rather than headline, and the empirical work is on models far simpler than E1. Mapping fidelity 0.78, the highest in this review's ML set, because the paper's claim is about the general single-step-trained-then-iterated construction and REE instantiates that construction literally. Transfer risk 0.35 -- the *mechanism* transfers cleanly, the *guarantee* does not.

Aggregate 0.74, direction **supports**. I am confident this paper correctly describes what is wrong with E1's training. I am considerably less confident that fixing what it describes is sufficient to pass C3, and the record's `mapping_caveat` says so.
