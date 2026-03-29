# Culbreth et al. (2023) -- RL and goal-directed exploration in schizophrenia spectrum disorders

**Claim tested:** MECH-117 (wanting and liking signals are functionally dissociable in trajectory scoring)

## What the paper did

Culbreth et al. used a computational modelling approach -- specifically Michael Frank's exploration-exploitation decomposition -- applied to a reinforcement learning task with fMRI in schizophrenia spectrum patients versus healthy controls. Their goal was to determine which computational component of RL was specifically impaired in schizophrenia. The task permitted dissociating two forms of exploration: random exploration (occasionally choosing options at random, independent of their expected value -- a liking-adjacent process, driven by basic reward sensitivity) and directed/goal-directed exploration (specifically choosing options with high uncertainty, because learning their value serves future goal pursuit -- a wanting-adjacent process, requiring a persistent prospective representation of the value of information). The fMRI component allowed them to ask which brain regions mediated each form of exploration.

## Key findings relevant to MECH-117

The paper found that schizophrenia patients showed specifically reduced goal-directed (directed/uncertainty-driven) exploration, while random exploration was less impaired. The neural signature of the directed exploration deficit was rlPFC hypoactivation -- rostrolateral prefrontal cortex, the region associated with maintaining representations of future exploration value (wanting-like: prospective, frontal-maintained, persistent). In contrast, striatal reward learning signals (more liking-adjacent: driven by current reward feedback, not by prospective uncertainty) were relatively less impaired.

This supports MECH-117's dissociation because directed exploration requires a wanting-like signal -- a persistent prospective representation that the current option has unexplored value worth pursuing -- whereas random exploration requires only a liking-like signal -- responding to current reward feedback with sufficient stochasticity. The specific impairment of the wanting-adjacent process with relative preservation of the liking-adjacent process maps to the MECH-117 prediction.

## REE translation

MECH-117 claims that benefit_eval_head (liking, proximity spike at receipt) and z_goal_latent (wanting, smooth gradient from distance) are functionally dissociable in trajectory scoring. Culbreth et al. 2023 provide neuroimaging evidence that in schizophrenia, the prospective/goal-directed component (rlPFC-mediated) is preferentially impaired relative to basic reward feedback processing. This is not a direct test of MECH-117, but it provides convergent evidence that prospective goal-directed processing and consummatory reward processing are supported by distinct neural substrates that can be selectively disrupted -- which is the biological analog of what MECH-117 requires for z_goal and benefit_eval_head to be architecturally distinct.

The rlPFC finding also has architectural relevance beyond MECH-117: it maps to the prefrontal goal-maintenance role that MECH-116 describes. Goal context is maintained in frontal cortex (rlPFC/PFC) and communicated to hippocampal/striatal navigation circuits. This is the wanting pathway. If rlPFC is specifically impaired in schizophrenia negative symptoms, and if negative symptoms specifically impair wanting while liking is preserved, this is evidence that the prefrontal goal-maintenance (wanting) pathway is architecturally separable from the striatal reward-evaluation (liking) pathway.

## Limitations and caveats

The paper's primary claim is about exploration-exploitation in reinforcement learning, not about the wanting/liking dissociation directly. Treating directed exploration as wanting-adjacent and random exploration as liking-adjacent is an inferential step that the authors do not make explicitly. The rlPFC correlation is associative (fMRI connectivity) and cannot establish causation. Also, schizophrenia spectrum disorders are heterogeneous -- the same symptom can arise from different mechanisms in different patients, and the computational model parameters (epsilon for random exploration, directed exploration bonus) may not uniquely identify the wanting versus liking pathways.

## Confidence reasoning

Confidence is 0.68. The paper provides useful convergent evidence from computational psychiatry, but the connection to MECH-117 requires inferential bridging. The source quality is good (Psychological Medicine, Frank lab computational model) but the mapping fidelity is moderate. The evidence supports MECH-117 as a consistent finding in the schizophrenia literature but is not a direct test of the REE wanting/liking dissociation.
