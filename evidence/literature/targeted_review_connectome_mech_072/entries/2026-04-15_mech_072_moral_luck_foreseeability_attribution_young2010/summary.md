# Moral luck and foreseeability: it is not what you do but what you know

**Source:** Young, Nichols & Saxe (2010), Review of Philosophy and Psychology. DOI: 10.1007/s13164-010-0027-y

## The question this paper asks

The legal and philosophical concept of moral luck describes the uncomfortable fact that we hold people responsible for outcomes that partly depend on chance. A driver running a red light is blamed more if a pedestrian happened to be crossing than if the street was empty -- even though both drivers made identical choices. This is irrational if responsibility should track what the agent could have controlled. Young and colleagues asked whether human moral cognition is actually irrational here, or whether blame is secretly tracking something subtler: not the bad outcome, but whether the agent had good reasons to believe harm would not result.

## The experimental finding

In a series of behavioural experiments (n=24 and n=42) and an fMRI study (n=19), participants evaluated agents in moral scenarios that independently varied whether the agent had a false belief about potential harm, whether that false belief was justified (the agent had good reasons for it), and whether harm actually occurred. The key result: moral blame depended far more on belief justification than on outcome. An agent who could not have known harm was coming -- who had genuinely good reasons for their false belief -- received substantially less blame, regardless of whether harm occurred. An agent whose false beliefs were unjustified (they should have known, or had no good reason to think harm was absent) received more blame even when no harm occurred.

This is a direct behavioural demonstration that the human moral system implements a foreseeability gate. Blame is conditioned on what-the-agent-could-have-known, not on what-actually-happened.

## The fMRI signature of the gate

When participants made blame judgments that required reasoning about mental states -- specifically about whether the agent could have foreseen harm -- activation increased in right and left TPJ, precuneus, and dorsal and ventral medial PFC. These are precisely the regions associated with mental state reasoning and theory-of-mind processing. The finding suggests that the foreseeability gate, biologically, is implemented by the same machinery that models other minds: the system asks what information was available to the agent, constructs a model of what the agent could have anticipated, and uses that to condition blame.

## Why this matters for MECH-072

MECH-072 proposes a foreseeable-harm gate: residue accumulation should be conditioned on whether the agent could have anticipated the harm given their current z_world state. Young et al. provide the most direct available evidence that this gate principle is not merely computationally convenient -- it is how biological moral cognition actually works. The medial PFC / TPJ network as the substrate for this foreseeability computation is the biological ground truth that MECH-072 is approximating with the z_world-based discriminator.

The finding also sharpens the design requirement. In the biological system, the foreseeability gate appears to operate over belief-states -- representations of what the agent could have known. In REE, z_world is the analogue: the agent's model of world state available at decision time. A gate on residue accumulation that queries z_world at action time is architecturally implementing the same computation that the TPJ/mPFC network implements in humans.

## Caveats

This study measures blame judgments by observers about agents in stories. MECH-072 describes a self-referential gate -- the agent's own learning system deciding whether to accumulate residue. Whether the brain implements the same foreseeability computation for self-attribution as for observer blame is not directly tested here. The gap between deliberate verbal moral judgment and implicit real-time residue gating remains the primary transfer risk.
