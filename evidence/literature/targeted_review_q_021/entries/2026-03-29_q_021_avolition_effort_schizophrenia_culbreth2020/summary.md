# Culbreth et al. (2020) -- Effort, avolition, and motivational experience in schizophrenia

**Claim tested:** Q-021 (does pure harm-avoidance training produce behavioral flatness?)

## What the paper did

Culbreth, Moran, Kandala, Westbrook, and Barch designed a multi-method study that connected laboratory effort-cost decision making with real-world motivational behavior in schizophrenia. The laboratory component used a task where participants chose between low-effort/low-reward and high-effort/high-reward options, allowing measurement of effort discounting -- how much reward value is lost per unit of required effort in the participant's subjective evaluation. The real-world component used ecological momentary assessment (EMA), pinging participants repeatedly throughout daily life to ask what they were doing and whether they found it motivated. The neuroimaging component measured striatal activation during effort allocation choices. The three components were related to each other and to clinical ratings of avolition and negative symptoms.

## Key findings relevant to Q-021

The key finding is a gradient of impairment: individuals with greater avolition showed greater effort discounting in the laboratory (steeper cost function for effort), reduced striatal activation during effort allocation, and fewer goal-directed activities in daily life as measured by EMA. The ecological validity component is particularly important for Q-021: the behavioral flatness was not limited to the structured laboratory task. It generalised to naturalistic behavior across the full range of daily activities, confirming that the motivational impairment produces a stable, generalized reduction in behavioral output -- what Q-021 calls a "quiescent degenerate policy."

The striatal correlation is also informative: striatal activation during effort allocation (wanting circuitry activation, approach drive signal) predicted both laboratory effort discounting and daily-life goal-directed activity. This provides neural evidence that the behavioral flatness in avolition is specifically linked to wanting circuitry hypoactivity, not to elevated harm circuitry. The patients are not actively avoiding -- they are simply not being pulled toward.

## REE translation

Q-021 predicts that a pure harm-avoidance trained agent would show reduced policy entropy and action rate -- behavioral flatness generalised across contexts. Culbreth et al. 2020 document exactly this signature in a clinical population with impaired approach drives: reduced action rate (effort discounting), reduced goal-directed activity (EMA), striatal wanting-signal hypoactivity. The EMA component is the most important for Q-021: it shows that the flatness is not an artifact of the test context but a stable generalized property of the agent's behavioral policy -- which is what Q-021 predicts for a trained agent converging on the quiescent attractor.

The striatal mechanism (wanting circuitry hypoactivity) maps to what Q-021 would expect in an agent with no approach training signal: without z_goal seeding and benefit_exposure signals, the approach circuitry (striatum in biology; whatever implements trajectory scoring toward positive attractors in REE) never develops appropriate activation, and the behavioral policy defaults to non-initiation.

## Limitations and caveats

Schizophrenia involves multiple mechanisms including dopamine dysregulation, cognitive impairment, and social cognition deficits -- not all of which map to the pure-avoidance training scenario in Q-021. Effort discounting in schizophrenia may partly reflect elevated subjective cost of cognitive effort (which would correspond to MECH-113/114's D_eff pathway) rather than purely absent approach drive (Pathway A). The paper cannot cleanly dissociate the two Q-021 pathways. Also, EMA measures motivational activity in natural daily life, not in a controlled task -- this improves ecological validity but reduces experimental control. The finding that striatal activation predicts daily-life behavior is correlational and cannot establish causation.

## Confidence reasoning

Confidence is 0.70. Good multi-method study with ecological validity from EMA data. The behavioral flatness generalising from laboratory to daily life is strong evidence for the stable quiescent policy that Q-021 predicts. Confidence is moderate because the mechanism (schizophrenia wanting-circuit impairment vs. pure-avoidance training) requires inference, and the two Q-021 pathways are not dissociated in this study.
