# Sutton (1988) -- the learned prediction as a dense progress proxy

**Claim strand:** D -- on-path inference / progress estimation as a maintenance signal.
**Wires to:** MECH-217 (temporal_wanting_propagation), INV-065 (proxy_goal_necessity), and the prospective candidate `on_path_progress_inference`.

## What it establishes

This is the foundational paper for temporal-difference learning. Its central move: "whereas conventional prediction-learning methods assign credit by means of the difference between predicted and actual outcomes, the new methods assign credit by means of the difference between *temporally successive predictions*." A later prediction becomes the learning target for an earlier one -- bootstrapping. That is precisely how a learned value/prediction comes to act as a *dense, intermediate* stand-in for a distal or sparse terminal outcome. Sutton proves linear TD(0) converges to the correct predictions for the data-generating Markov process and shows TD needs less memory/compute and yields more accurate multi-step predictions than outcome-based methods.

## Mapping to REE

Daniel's "even a predicted subgoal" and "inference system" components reduce, computationally, to this: the agent maintains a goal partly by *inferring it is on-trajectory*, and a bootstrapped value estimate is the canonical way to produce that on-path signal between sparse terminal confirmations. This grounds a candidate `on_path_progress_inference` claim and supplies the formal substrate under MECH-217's temporal wanting-propagation (reverse replay spreading value backward along approach trajectories is, mechanically, a TD/eligibility-trace operation). It also connects to the biological reading -- dopaminergic reward-prediction-error (Schultz, Montague) is the in-brain instantiation.

## Caveat

The 1988 guarantees are for the *prediction* problem with a fixed policy and largely linear approximation. REE operates in deep, control-coupled territory on a learned latent that may be non-Markov -- the regime where TD can diverge (the deadly triad) and where the bootstrap target is only as faithful as the state representation. So "learned value = faithful dense progress proxy" is a *design target*, and a value head over an impoverished latent can be a confidently-biased proxy -- which loops straight back to the Strand-B tethering concern (a biased progress proxy is exactly an untethered one). Confidence 0.72, direction supports.
