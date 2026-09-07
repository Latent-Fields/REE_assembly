# Prescott, Montes Gonzalez, Gurney, Humphries and Redgrave (2006) -- a robot model of the basal ganglia

**Question served:** Q3 (does BG persistence dissociate competence from robustness?) and, as a boundary condition, Q1/Q2.

## What the paper did

The fuller Sheffield study of the GPR basal ganglia model embedded in a robot, with a task inspired by animal foraging observations and an analysis of the model's intrinsic processing (striatal, pallidal and nigral output patterns) alongside its behaviour. The headline result is that the embedded model produces "effective action selection ... under a wide range of sensory and motivational conditions," and that it illuminates neurobiological findings on behavioural switching and sequencing.

## The result that matters here

"When confronted with multiple, high salience alternatives, the robot also exhibits forms of behavioral disintegration that show similarities to animal behavior in conflict situations." A basal-ganglia selector with a persistence loop, in other words, does not protect against everything. Girard et al. (2003) showed that persistence prevents dithering when two saliences are *close and modest* -- near-tie noise. Here, when two or more options are *strongly and equally* supported, selection breaks down even with the latch, and the breakdown looks like an animal in conflict.

## How this bears on MECH-536 and MECH-535

For MECH-536 the entry is *mixed*: persistence adds robustness across a wide range of conditions, but the protection is bounded, and the bound is symmetric high conflict rather than degraded input. That is consistent with the claim's functional reading (persistence is a robustness layer, not a competence source) while marking a limit the claim does not currently state. For MECH-535 the paper supplies the alternative explanation the claim must be discriminated from. Ambitendency-like output can arise on the *gating* axis, when two well-represented options are both strongly supported -- which is precisely the shape of the clinical elicitation (offer a handshake, instruct not to shake) -- with no representational degradation at all. The 978 case is the opposite configuration: nothing is strongly supported, the directional head is flat, and the two tendencies come from one impoverished magnitude reading on two adjacent cells. So the discriminator between the two routes is whether the competing tendencies arise from a rich but conflicted representation or from an impoverished one, and the MECH-536 latch test is informative precisely because a latch should *resolve* conflict-driven disintegration (competence recovers) and merely *freeze* representation-driven cycling (competence flat).

## Caveats

Scored from the abstract; the exact conditions and metrics of "behavioural disintegration" were not extracted. Robot foraging with hand-set saliences; no representational manipulation, so the MECH-536 dissociation is not tested. "Similarities to animal conflict behaviour" is the authors' qualitative reading. Confidence 0.45.
