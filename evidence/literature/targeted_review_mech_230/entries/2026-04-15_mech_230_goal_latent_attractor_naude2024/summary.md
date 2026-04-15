# MECH-230 Literature Entry: Naude et al. 2024

**Entry ID:** 2026-04-15_mech_230_goal_latent_attractor_naude2024
**Claim:** MECH-230 -- z_goal as structured positive attractor distinct from harm avoidance
**DOI:** https://doi.org/10.1038/s41467-024-53976-x

---

## What the paper did

Naude and colleagues (2024) ask how dopamine unifies two apparently distinct roles it is known to play: a teaching signal that reinforces rewarded behaviors, and a motivational neuromodulator that drives behavior toward goals. They construct the MAGNet model -- a recurrent network-based decision architecture in which the agent acts through an action-perception loop with the task environment. The key move is to allow dopamine to do two separable things: (1) dopamine-dependent synaptic plasticity *builds* latent attractors in the network's state space that correspond to rewarded locations, and (2) dopamine neuromodulation (modulating synaptic excitability rather than synaptic weights) *widens* the basin of those attractors, making them accessible globally rather than only from nearby states. They validate this architecture with optogenetic dopamine stimulation in mice performing navigational tasks, showing that dopamine neuromodulation specifically and rapidly attracts animals toward rewarded locations without off-target motor effects.

## Key findings relevant to MECH-230

The central finding is that the recurrent network spontaneously develops a structured latent state -- a stable attractor in the network's internal space -- whose basin of attraction encodes a reward-associated goal location. This is not merely an associative weight between stimulus and response: the attractor has geometry in state space, and that geometry is what makes goal-directed navigation possible. Critically, the attractor is at first "latent" in the sense that it is locally stable but not globally accessible; only with motivational dopamine (the neuromodulatory effect) does the basin widen enough that the agent can converge to the goal attractor from arbitrary starting states. This provides a mechanistic answer to why motivation -- not just learning -- is required for goal-directed behavior.

## REE translation

MECH-230 proposes that E3 maintains z_goal as a structured positive attractor in a dedicated sub-space, seeded by homeostatic drive (SD-012). The MAGNet finding maps naturally onto this: the latent attractor in MAGNet is the biological analogue of z_goal_norm > 0 in REE. The role of dopamine neuromodulatory widening in MAGNet parallels SD-012's drive_level mechanism: without homeostatic drive, the z_goal seed may be locally present but globally inaccessible, explaining why EXQ-085 through 085d all produced z_goal_norm < 0.1 when SD-012 was not active. The MAGNet architecture thus provides a mechanistic rationale for why SD-012 (homeostatic drive scaling benefit_exposure) is a prerequisite for z_goal to develop into a useful navigational attractor rather than a near-zero trace.

One important limitation to note: MAGNet models only approach-to-reward and does not include an explicit harm/avoidance representation in the same latent space. MECH-230 makes the additional, stronger claim that z_goal and z_harm occupy distinct sub-spaces. This paper supports the existence of a structured goal attractor but does not directly evidence that the attractor is geometrically separate from harm encoding.

## Limitations and caveats

The biological substrate in MAGNet is the mesolimbic dopamine system and cortico-striatal circuits, not hippocampal terrain navigation specifically. REE's hippocampal terrain is a distinct computational structure in which z_goal serves as the navigational target -- this paper does not address whether the attractor representation in hippocampal-like maps shares the same geometry as striatal attractors. Transfer risk is further elevated because the model uses a continuous recurrent network, while REE implements z_goal as a discrete sub-space vector; whether attractor dynamics translate from one to the other requires direct experimental test.

## Confidence reasoning

Confidence is set at 0.72. Source quality is high (Nature Communications, peer-reviewed, with in vivo optogenetic validation). Mapping fidelity is good for the attractor-formation and drive-dependence components of MECH-230 but partial: the approach/harm separation is not evidenced here. Transfer risk is moderate. The paper provides the clearest available mechanistic story for why a latent goal state requires motivational drive to become globally accessible -- which is precisely the problem SD-012 is designed to solve. This is the most direct computational evidence for the positive-attractor half of MECH-230 currently in the literature.
