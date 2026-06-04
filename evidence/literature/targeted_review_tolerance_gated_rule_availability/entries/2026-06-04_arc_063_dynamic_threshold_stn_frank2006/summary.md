# Frank 2006 -- The STN supplies a dynamic, conflict-driven threshold ('hold your horses')

**Claim touched:** ARC-063 design element (ii), specifically the *adaptive* (not fixed) character of the tolerance gate. Cross-ref MECH-309, ARC-062.

## What the paper did
Frank extended a basal-ganglia network model -- one that had already accounted for Parkinsonian response-selection deficits and been confirmed under dopaminergic challenge -- by adding the subthalamic nucleus. The STN's role in the model is temporal: by modulating *when* a response is executed, it reduces premature responding, and this in turn changes *which* response is ultimately selected, especially when several responses compete. The key computational claim is that increased cortical response conflict produces *dynamic adjustments* in the response threshold through cortico-subthalamic-pallidal pathways.

## Why it matters for ARC-063
The companion to Cavanagh's empirical result. Where Cavanagh measured the conflict-scaled threshold, Frank's model shows *how* a cortico-subthalamic loop computes it -- and the load-bearing point for us is that the threshold is **dynamic**. A tolerance gate that was merely a fixed bar would not capture the biology; the gate is raised specifically under competition. ARC-063 should therefore make tolerance an adaptive quantity -- rising with the number of competing candidate rules or accumulated exceptions -- rather than a static constant, and the cortico-subthalamic template tells us such adaptivity is computationally cheap and biologically attested.

## The honest caveat
This is a response-selection model with no abstract-rule layer; the "competition" it resolves is between motor responses, not between candidate rules. The transfer to rule availability is ours, not the paper's, and it is a simulation rather than a measurement -- though an unusually well-validated one. I have kept mapping_fidelity at 0.55 for the target gap.

## Confidence
0.62 -- supports. A foundational, repeatedly-confirmed model that grounds the *adaptive* requirement of ARC-063's gate. The discount reflects that the modelled target is response timing, not rule admission, and that the rule-domain transfer remains an REE extension.