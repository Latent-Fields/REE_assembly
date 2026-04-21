# Sesack & Grace 2010 -- Cortico-BG Reward Network Microcircuitry

**Claim tested:** ARC-028 (HippocampalModule completion signal -> BetaGate wiring)
**Direction:** supports | **Confidence:** 0.72

## What the paper did

Sesack and Grace (both also involved in the original Lisman & Grace 2005 loop proposal) wrote a detailed review of the nucleus accumbens microcircuitry, covering all major afferent and efferent systems. The paper characterizes the NAc as an integrative hub receiving glutamatergic input from the ventral subiculum (contextual/spatial information), the basolateral amygdala (affective valence), and the prefrontal cortex (executive/goal-directed information), all under modulatory control of VTA dopamine. Critically, the review distinguishes tonic and phasic dopamine effects: phasic DA release when reward conditions are met selectively potentiates the ventral subicular drive to the NAc, maintaining ongoing approach behavior; failure to obtain expected reward decreases DA transmission, which shifts control to PFC, favoring behavioral switching.

## Key findings relevant to ARC-028

This paper extends the Lisman-Grace circuit in a direction directly relevant to ARC-028. First, it places the ventral subicular projection to NAc in a functional context: subicular input carries spatial and contextual information, including current position in a trajectory. Second, the paper explicitly links reward conditions to phasic dopamine selectively potentiating subicular -> NAc drive -- establishing a positive feedback: approach success amplifies the hippocampal-NAc-VTA loop. Third, the paper's description of the overall circuit ("the dopamine system to bias goal-directed behavior based on internal drives and environmental contingencies") is precisely the computational role ARC-028 assigns to the completion signal: biasing BetaGate toward release when a trajectory completes.

## REE translation

ARC-028's proposed wiring can be read directly from this microcircuit diagram. HippocampalModule's subiculum-analog output provides spatial/trajectory-context information to the NAc-analog. When the trajectory completion criterion is met (analogous to "reward conditions"), phasic dopamine release potentiates this subicular drive and activates the loop back through VP -> VTA. Dopamine then reaches striatal targets and suppresses beta synchrony (BetaGate), completing the coupling MECH-057b -> ARC-028 -> MECH-090 that the claim requires.

## Limitations and caveats

The critical phrase "conditions that result in reward" refers to actual reward receipt in the paper -- not trajectory completion per se. In a goal-directed navigation task, reward is obtained at the end of a successful trajectory, but in REE's CausalGridWorldV2, a trajectory completion event is distinct from resource contact (the resource is at the end of the planned path, but the agent may not yet have reached it). Whether the dopamine circuit fires on trajectory plan completion or only on resource contact is unclear. Additionally, the paper focuses on ventral subicular projections, whereas the REE HippocampalModule outputs may not have a clean biological subiculum analog.

## Confidence reasoning

This is a stronger reference than Lisman & Grace 2005 for the specific NAc microcircuit because it provides functional detail about what the subicular input does and how dopamine potentiates it. Confidence 0.72 reflects high source quality, good (but not perfect) mapping, and the same caveat as the Lisman paper about reward vs. completion.
