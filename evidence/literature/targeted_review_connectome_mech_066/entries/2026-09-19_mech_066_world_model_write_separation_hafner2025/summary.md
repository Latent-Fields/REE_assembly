# Mastering diverse control tasks through world models (Hafner et al., 2025)

## Why an ML paper belongs in a connectome-named pull

MECH-066 is a claim about write topology, and the four neuroscience entries in this pull all pay a translation cost: Kaufman's boundary is transient rather than durable, Yagishita's gate is temporal rather than typed, Simons' discrimination is retrospective rather than prospective, Dijkstra's boundary is a readout rather than a write. Each is informative and each requires an inference REE supplies rather than the paper.

DreamerV3 pays almost none of that cost, because the comparison is between two artificial agents whose write topology can be read off the training code. That is why this entry carries the pull's lowest `transfer_risk` (0.20) and its highest `mapping_fidelity` (0.85), and why it ends up the most useful entry despite being, like Dijkstra, a `mixed` verdict.

## What the architecture actually does

DreamerV3 is the third generation of Dreamer: one algorithm, one hyperparameter configuration, over 150 tasks spanning proprioceptive and pixel-based continuous and discrete control, and the first system to collect diamonds in Minecraft from scratch with no human data and no curriculum. The scale of validation is not incidental to its evidential value -- this is a working system under load, not a demonstration.

The training topology is the relevant part, and it is clean:

- The **world model** parameters are optimised on a prediction loss over batches of *replayed real* inputs, actions, rewards and continuation flags.
- The **actor and critic** learn behaviours *purely* from abstract trajectories of representations predicted by the world model, imagined over a 16-step horizon starting from representations of replayed inputs.
- Imagined trajectories **never** update world model parameters. The flow is one-way.

Both channels operate over one shared latent state space.

## The mapping, and the refinement MECH-066 should absorb

The permissive half of MECH-066 holds exactly, and more strongly than the claim requires. Pre-commit (imagined) and post-commit (replayed-real) processing share not merely overlapping representations but the *same* latent state space. Nothing is duplicated and nothing is segregated.

The restrictive half holds at the world-model write locus, and holds by construction. Imagined rollouts cannot reach the world model's parameters. This is the same topology REE already has: `compute_prediction_loss` trains E1 only on actual observations, `update_residue` accumulates only post-commit harm. Finding the identical separation independently arrived at in the strongest general model-based agent published is real corroboration that MECH-066 names a design constraint rather than a stylistic preference.

And then DreamerV3 does the thing MECH-066 as written appears to forbid. Actor and critic parameters -- durable, persistent, consequence-bearing -- are written *entirely* from imagined data. Not as a compromise, not as an efficiency hack: it is the core of the method and the reason it works across 150 tasks.

So MECH-066 as currently stated is over-general. "Durable write boundaries" without qualification is not what the best working instance of this architecture does, and not what it should do. The principle that survives is narrower and, I think, better: **the protected locus is the component whose function is to be veridical about the world.** The world model must not be allowed to learn from its own output, because a model trained on its own predictions has no correction signal and drifts without bound. A policy has no such requirement -- its job is to be *good*, not *true*, and training it on simulation is exactly how you get sample efficiency. If MECH-066 goes to governance, this is the amendment I would put in front of the user: the claim should name the protected component by its epistemic role, not quantify over all persistent stores.

## Where the risk relocates rather than disappearing

The second failure signature is worth dwelling on, because it is the price of the design. Since all policy learning is mediated by imagined rollouts, the world model's accuracy becomes the *sole* contamination channel into policy. A system can have perfect write-boundary hygiene -- no simulated data anywhere near the model parameters -- and still consolidate systematically wrong policy from clean-but-inaccurate simulation. The boundary stops one contamination path and makes the remaining one load-bearing.

This is directly relevant to REE, where the residue field is the store MECH-060's EVB-0043 showed to be contamination-sensitive (46-fold `total_residue` inflation under the CONT_RESIDUE ablation, 8520 versus 186). DreamerV3 has no residue-field analogue at all. It gives us a precedent for E1's protection and nothing at all about residue, which is part of why `mapping_fidelity` is 0.85 and not higher.

## The main limitation: convergence is not necessity

DreamerV3 contains no ablation of the separation. There is no arm in which imagined rollouts are permitted to update the world model, so the paper shows that the separated topology *works* and never that the unseparated one fails. That is existence-of-a-working-instance evidence, which is categorically weaker than MECH-060's EVB-0043, where the boundary was manipulated directly and the contamination measured.

It is also weaker than the pathology argument in the Simons entry. A clinical failure mode is evidence that machinery is *required*; a successful engineering choice is evidence that it is *sufficient and chosen*. I have held confidence at 0.78 for this reason, below what the source quality and mapping fidelity alone would suggest.

The third failure signature is the practical one. DreamerV3's separation is a static property of which loss touches which parameters -- nothing detects a violation at runtime, because a violation would be a different program. If we ever audit MECH-066 compliance in REE, the right instrument is a static read of the write topology, not a runtime statistic. That is a genuinely different instrument from the `|pre_post_corr| = 0.044` correlation MECH-061 was confirmed on, and the Kaufman entry's second failure signature makes the same point from the biological side: representational overlap measured at the wrong locus can report contamination on a correctly gated architecture.

## Confidence

0.78. Source quality 0.90 (Nature; single configuration across 150+ tasks; the Minecraft diamond result). Mapping fidelity 0.85 -- the highest here, because no cross-domain translation is needed. Transfer risk 0.20, and what remains is role-analogy risk rather than domain-transfer risk: the open question is whether E1 plays the world model's role, not whether an artificial agent's topology transfers to REE's.
