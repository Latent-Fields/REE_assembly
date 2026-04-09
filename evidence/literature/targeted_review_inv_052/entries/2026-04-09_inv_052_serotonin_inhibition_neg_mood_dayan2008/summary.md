# Summary: Dayan & Huys 2008 -- Serotonin, Inhibition, and Negative Mood

**Entry:** 2026-04-09_inv_052_serotonin_inhibition_neg_mood_dayan2008
**Claim tested:** INV-052
**Evidence direction:** supports

## What the paper did

Dayan and Huys built a simplified reinforcement learning model to ask a deceptively clean question: why would a system whose primary computational function involves aversive prediction benefit from being the target of reuptake-inhibitor antidepressants? Their model assigns serotonin the role of pruning a sequential decision tree -- removing branches whose expected outcome is sufficiently negative that engaging them would be instrumentally irrational. The model operates across a tree of possible action sequences, and serotonin's role is to suppress the pursuit of paths predicted to end badly.

## Key findings

The central prediction is that reduced serotonin tone does not merely increase experienced negativity -- it structurally degrades the organism's ability to avoid accumulating harm. When inhibitory pruning fails, low-value branches remain in the decision space, and the agent traverses them. Each traversal then produces unexpectedly large negative prediction errors (because the branch was not pruned when it should have been), which further suppress expectation of benefit from future action. This is a cascade: low 5-HT floor -> failed pruning -> harm-path traversal -> escalating negative prediction errors -> further depression of expected value -> further loss of motivation. The model accounts for the apparent paradox that serotonin is associated with aversive processing yet its enhancement is antidepressant: it is the failure to inhibit aversive branches that produces the negative spiral, not the signalling of aversion per se.

## Translation to INV-052

INV-052 claims that goal-directed behaviour in harm-rich environments requires a tonic regulatory system maintaining benefit orientation across terrain, transduction, and maintenance. The Dayan-Huys model is most directly relevant to the terrain stage. The benefit terrain -- in REE terms, the latent representation of where benefit opportunities reside -- depends on serotonin's pruning function to prevent harm-laden branches from overwriting the gradient structure. If we ask what happens when the tonic 5-HT floor drops, the model's answer is that the terrain representation becomes dominated by aversive paths: benefit gradients are not merely weakened but are actively replaced by repeated harm-exposure cascades. This is a mechanistic account of benefit terrain collapse that directly supports MECH-186.

The transduction and maintenance stages of INV-052 (MECH-187, MECH-188) are less directly addressed. The paper does not explicitly model goal representation persistence or the gain on VALENCE_WANTING seeding. However, the cascading negative prediction error mechanism suggests that once terrain collapses, both downstream stages would be deprived of their upstream input -- a necessary-condition argument for the tonic floor requirement.

## Limitations

The model is highly simplified: a flat RL tree without latent state, without explicit terrain geometry, and without a distinction between terrain representation and goal seeding. The tonic floor concept is implicit in the failure mode (what happens when 5-HT drops) rather than positively articulated as a requirement for benefit orientation. The paper also does not distinguish between the three stages INV-052 specifies; it operates at a level of abstraction that conflates terrain, transduction, and maintenance under the single rubric of "negative mood." Transfer to REE's latent architecture requires inferential extension.

## Confidence reasoning

Source quality is high -- this is a foundational paper in computational psychiatry, well-cited, and the computational model is internally coherent. Mapping fidelity is moderate: the pruning/cascade account aligns well with terrain collapse but the positive claim about tonic floor maintenance is implicit. The overall confidence of 0.72 reflects solid support for the necessity argument but the paper does not deliver a three-stage dissociation.
