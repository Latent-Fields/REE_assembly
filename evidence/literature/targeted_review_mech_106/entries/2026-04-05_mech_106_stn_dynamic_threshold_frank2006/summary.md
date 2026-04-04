# Frank 2006 -- Hold Your Horses: STN Dynamic Threshold in Decision Making: MECH-106 Mapping

**Source:** Frank, M.J. (2006). Hold your horses: a dynamic computational role for the subthalamic nucleus in decision making. *Neural Networks*, 19(8), 1120-1136. DOI: [10.1016/j.neunet.2006.03.006](https://doi.org/10.1016/j.neunet.2006.03.006)

---

## What the Paper Does

Frank 2006 extends the basal ganglia model of Frank 2005 to include the subthalamic nucleus (STN) and the hyperdirect pathway. The STN receives direct cortical input and projects to the globus pallidus interna (GPi), bypassing the striatal pathways. This creates a fast inhibitory override that can raise the global response threshold before the slower direct and indirect pathways have resolved the competition. Frank's model shows that when cortical activity reflects high response conflict -- multiple competing actions are simultaneously active -- the STN's hyperdirect pathway fires, elevating GPi output and effectively telling the system to wait before committing to any option. This is the "hold your horses" function: a dynamic, context-sensitive threshold elevation that delays commitment until conflict is resolved.

The model accounts for impulsive decision-making when the STN is lesioned (or its function disrupted by deep brain stimulation) and explains the emergent oscillatory dynamics that appear in the simulated parkinsonian state when dopamine depletion destabilises the normal balance between direct, indirect, and hyperdirect pathways.

## Key Findings

The key finding for MECH-106 is not about outcome valence specifically -- Frank 2006 does not directly address valence-asymmetric hysteresis. What it establishes is that the BG is already capable of dynamic, context-sensitive commit threshold adjustment through an anatomically distinct pathway operating in real time. This is important because it answers a prior question MECH-106 needs to take as given: is the commit threshold dynamically adjustable at all, or is it a fixed architectural parameter? Frank 2006 establishes it is dynamically adjustable -- the STN/hyperdirect mechanism proves it in the conflict domain. The implication for MECH-106 is that extending this dynamic threshold adjustment to the outcome-valence domain (via D1/D2 modulation, Frank 2005) is architecturally coherent with what the BG already does.

The STN's rapid global suppression also provides a candidate mechanism for one aspect of MECH-106 that the Frank 2005/2004 papers do not directly address: the de-commitment response to a sudden negative outcome (harm contact). If a large prediction error or harm event creates a sudden high-salience signal, the STN pathway could produce rapid threshold elevation -- a fast break from commitment -- before the slower D2-indirect pathway learning has time to operate. This is not what Frank 2006 explicitly tests, but it is consistent with his model's architecture.

## REE Mapping to MECH-106

MECH-106 requires asymmetric commitment threshold dynamics: negative outcomes raise the threshold, positive outcomes lower it, with hysteresis. Frank 2006 contributes the third piece of evidence: the BG architecture already implements dynamic threshold adjustment as a design principle (for conflict). The D1/D2 asymmetry (Frank 2005, 2004) and its behavioural consequences (Frank & O'Reilly 2006) provide the valence-specific evidence. Frank 2006 establishes the broader architectural context within which those valence effects operate.

For the specific case of de-commitment from an active committed sequence following a negative outcome -- which MECH-106 predicts should be easier after harm contact -- the STN hyperdirect pathway provides a candidate rapid mechanism: harm salience -> cortical activity reflecting the harm state -> hyperdirect pathway elevation -> threshold raised above the persistence point of the committed state -> de-commitment. The timescale would be fast (within the current step), rather than the slower D2-mediated learning effect. This would produce a two-timescale picture of MECH-106: fast de-commitment via STN, sustained threshold elevation via D2 learning. That picture is not explicitly proposed in Frank 2006 but is architecturally available.

## Limitations and Confidence Reasoning

The mapping caveat here is significant: Frank 2006 is about conflict-driven threshold adjustment, not valence-driven hysteresis. The paper does not study what happens to the commit threshold after an outcome is received -- it studies what happens during the selection process when conflict is present. These are temporally distinct stages of the commitment episode (conflict during selection vs. valence during feedback), and while they may interact, they are not the same mechanism.

There is also a timescale mismatch: the STN mechanism operates on the order of hundreds of milliseconds; MECH-106's hysteresis is meant to persist for multiple decision steps (potentially seconds or longer). The two mechanisms could both contribute to threshold asymmetry at different timescales, but Frank 2006 does not address the slower component.

The paper's contribution to MECH-106's evidence base is indirect -- it supports the general principle that BG commit thresholds are dynamically adjustable, but the specific form of adjustment MECH-106 claims is not directly tested here. Confidence: 0.68.

*Based on article retrieved from PubMed (PMID: 16945502, DOI: [10.1016/j.neunet.2006.03.006](https://doi.org/10.1016/j.neunet.2006.03.006)).*
