# Prescott, Montes Gonzalez, Gurney, Humphries and Redgrave (2024) -- simulated dopamine modulation of a neurorobotic basal ganglia

**Questions served:** Q1 (the D2-blockade / dopamine route and where it puts the deficit) and Q3 (persistence over intact inputs).

## What the paper did

The GPR basal ganglia model -- now with D1 and D2 striatal pathways, GPe, STN and output nuclei, plus thalamocortical feedback loops controlling five action subsystems -- was embedded in a foraging robot that wall-follows, seeks cylinders and deposits them in lit corners. Tonic simulated dopamine was swept from far below to far above baseline and the robot's behaviour scored for movement, completion, switching and failure.

## What it found

Low dopamine "caused slowed behaviour and, at low levels, an inability to initiate movement": movement slowed to three-quarters vigour by about lambda 0.12, and at lambda 0.06 and 0.03 the robot spent on average 14 and 38 seconds per trial not moving, with "failure to express movement despite being motivated." Weakly selected behaviours became "vulnerable to interruption," and cylinder grasps failed through premature deselection of the arm -- a loss of persistence. These states "were partially relieved by increased salience levels": successful low-dopamine trials had higher-salience cylinder encounters (p = 0.007). High dopamine produced the mirror image: "distortion of the robot's motor acts through partially expressed motor activity relating to losing actions," failed grasps and wall-tracking, and increased switching (21.3 bouts vs 9.2 for winner-takes-all controls, p = 0.041). Levels far from baseline in either direction "could cause a loss of behavioural integration, sometimes leaving the robot in a 'behavioral trap'" -- a lowered gripper blocking the infrared sensor and triggering "slow circling behaviour until end of trial," or "repeated cycles of cylinder-seek and (unsuccessful) cylinder-pickup."

## Where it puts the deficit, and how this bears on the claims

This is the D2-blockade / hypodopaminergic route to catatonic-type signs rendered as a selection model, and the locus is unambiguous: gain on the basal-ganglia selection loop, with the representation of what to do intact throughout. For MECH-536 that is supportive. Low dopamine weakens the persistence the thalamocortical loop supplies; the robot then fails to complete acts it is both motivated and informed to perform; and the fact that higher salience rescues it shows the input side was never the problem. Persistence is doing protective work over adequate inputs, which is the claim's functional reading -- though the paper never degrades the inputs, so the dissociating prediction (latch plus direction-blind input gives cycle gone, competence flat) is not run.

For MECH-535 the paper is a caution rather than a support. One gating parameter yields both a stationary phenotype (no movement; stuck circling) and cyclic ones (repeated failed pickups; hyper-switching). "Stupor and ambitendency from one deficit, selected by initial condition" is therefore a property a *gating* route can also have, and the co-occurrence of the two signs does not by itself pick out the representational route. What picks it out in 978 is the flat directional head: the representation, not the gain, is what is missing. The entry is scored mixed for MECH-535 to keep that distinction in view.

## Caveats

Hand-set saliences and a scalar dopamine parameter; "catatonia" is the authors' analogy to dopamine dysregulation (Parkinsonism, dyskinesia), not a claim about the syndrome. Part of the trapping comes from a gripper blocking a sensor, a body-environment interaction with no fishtank analogue. Small run counts per dopamine level; modest venue. Confidence 0.5.
