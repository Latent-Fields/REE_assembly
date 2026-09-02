# Baarendse et al. (2013) -- Early social experience is critical for the development of cognitive control and dopamine modulation of prefrontal cortex function

*Entry for ARC-073, second clause: premature transition leaves policy structure undertrained.*

## What the paper did

Rats were socially isolated from postnatal day 21 to 42 -- the window of peak social play in this species -- and then re-socialised until adulthood. In adulthood they were tested on two dimensions of impulsivity (impulsive action in the five-choice serial reaction time task; impulsive choice in a delayed reward task) and on decision making in the rat gambling task. A separate cohort provided medial prefrontal slice recordings.

Isolated animals showed impaired impulsive action and impaired decision making, but specifically under novel or challenging conditions. Impulsive choice was unaffected. They also showed a reduced behavioural response to enhancement of dopaminergic transmission (amphetamine or GBR12909) under challenging conditions, and this was accompanied by a loss of dopamine sensitivity in medial prefrontal pyramidal neurons. Re-socialisation to adulthood did not rescue any of it.

## Why I pulled this for ARC-073

ARC-073 has two clauses, and the second one -- "premature transition leaves policy structure undertrained" -- has essentially no evidence behind it anywhere in the REE corpus, no computational analogue in the intrinsic-motivation literature, and no falsifier currently queued. It is also the clause that carries the practical weight. If a badly-set threshold merely wasted compute, the parameter would not matter much. If it permanently degrades what the agent becomes, it matters a great deal.

This is the closest biological test I could find. Remove the play window; restore the environment afterwards; measure what did not develop. The answer is that the capacities the window was building do not come back.

Three features of the result sharpen ARC-073 in ways the claim text does not currently anticipate.

**The deficit is selective, not global.** It appeared under novel or challenging conditions, and one of the three behavioural dimensions was spared entirely. An REE falsifier that compares mean task performance between an agent transitioned at saturation and one transitioned early, in familiar conditions, would very likely find nothing and report the claim unsupported. The measurement has to be made under novelty or load.

**The deficit is not recoverable.** Re-socialisation ran for weeks and did not restore function. If that transfers, then extra play *after* a premature transition does not repair the damage, and the two error directions around `play_lp_saturation_threshold` are asymmetric: transitioning late costs time, transitioning early costs capability permanently. Read alongside the Colas et al. entry -- which shows the saturation test is a noisy statistical decision with a real false-positive rate -- this argues the threshold should be set conservatively rather than at the point that maximises expected efficiency.

**The deficit showed up as lost modulation, not missing behaviour.** The prefrontal neurons had lost their sensitivity to dopamine. The policy was there; what was missing was the capacity to modulate it. An REE readout that inspects policy content would not see this. Whatever REE's analogue of neuromodulatory gain over the control substrate is, that is where to look.

## Where this does not reach

Social isolation removes far more than play. Three weeks with no social contact, no tactile input from conspecifics, much less environmental variety -- the manipulation is a sledgehammer, and this is a study about a developmental window mattering, not about *how that window should be closed*. Crucially, a fixed-duration play period of adequate length would have produced exactly the same protection in this design. So this supports ARC-073's undertraining clause while being entirely neutral between the competence-saturation criterion and the scheduled duration the claim is arguing against. The Smith, Forgie & Pellis entry in this directory takes up that question directly and answers it uncomfortably for the claim.

The species and mechanism gaps are wide: adolescent rodent social development to an REE play episode closed by MECH-196, and prefrontal dopamine modulation to a substrate with no current counterpart for it.

## Confidence

0.58, with `transfer_risk` deliberately set high at 0.52. The study is good and the venue is strong; the number reflects that the intervention shape (deprive the window entirely) is not the intervention ARC-073 is about (end the window from within, at the wrong moment). Recorded as `supports` because it is directional evidence for a clause that currently has none, and because the three specific features above make that clause considerably more falsifiable than it was.
