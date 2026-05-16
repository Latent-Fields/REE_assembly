# PAIRED: Unsupervised Environment Design (Dennis et al., NeurIPS 2020)

## What the paper did

Dennis, Jaques, Vinitsky, Bayen, Russell, Critch, and Levine formalised the problem of automatic curriculum generation as unsupervised environment design (UED). They use decision theory to characterise what a "good" training environment looks like: an environment is good if the agent has high regret in it -- defined as the gap between the best return achievable in that environment and the agent's actual return. This formalisation avoids two failure modes: pure minimax (generate the hardest possible environment, which the agent cannot solve at all) and random domain randomisation (generates environments that may be trivially easy and produce no learning signal). The PAIRED algorithm trains a third agent, the environment generator, to maximise the protagonist's regret while keeping the environment solvable (the antagonist provides the solvability ceiling). The result is a natural curriculum of increasingly challenging environments calibrated to the protagonist's current capability edge.

## Key findings

PAIRED produces an automatic curriculum without specifying which skills should be learned. In grid-world navigation, agents trained with PAIRED learn more complex behaviours and generalise better to novel held-out environments (zero-shot transfer) than agents trained with domain randomisation or minimax adversarial methods. The key structural insight is that an environment that the agent can almost-but-not-quite handle will expose exactly the behavioural weaknesses in the current policy -- forcing the agent to develop capabilities it lacks, including trying routes or strategies it has not yet explored.

## Translation to REE

REE's V_s monostrategy problem is precisely an environment-difficulty calibration failure: the bipartite reef (SD-054) provides competing attractors (safety zones + foraging zones), but if one attractor's reward gradient is always steeper than the other, the agent's policy will converge on the dominant attractor and never genuinely explore the competing mode. PAIRED's regret principle says: the relative salience of the two attractors must be dynamically calibrated to match the agent's current competence across both. A fixed bipartite environment is not a curriculum; it is just a slightly richer static environment that may still produce monostrategy. The practical implication is that REE should treat attractor salience (e.g. foraging reward magnitude, reef safety reward magnitude) as curriculum parameters adjusted based on which behavioural mode is currently underperforming -- a manual approximation of regret-based curriculum without requiring the full two-agent setup.

## Limitations and caveats

Implementing full PAIRED requires a second antagonist agent as the regret estimator. REE does not currently have this infrastructure. The practical extraction is the curriculum principle: track which behavioural modes are currently underexplored (proxy regret signal) and temporarily amplify their environmental salience. This is an approximation, not the full algorithm. Grid-world navigation is close to REE's CausalGridWorld domain (good ecological validity), but REE's action space and reward structure differ enough that specific transfer parameters cannot be read off from PAIRED results.

## Confidence

0.76. Solid NeurIPS paper with decision-theoretic grounding and zero-shot transfer results. Transfer risk is the main moderator: REE would need to implement curriculum parameter adjustment as a proxy for the full regret-based design mechanism.
