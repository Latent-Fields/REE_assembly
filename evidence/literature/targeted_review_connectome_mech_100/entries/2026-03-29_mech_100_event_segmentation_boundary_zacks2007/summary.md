# Zacks and Tversky (2001): Event structure in perception and conception

**Claim tested:** MECH-100 -- z_world encoder requires event-type cross-entropy auxiliary loss during training

## What the paper did

Zacks and Tversky proposed event segmentation theory: the idea that human (and animal) perceptual systems do not process experience as an undifferentiated continuous stream but actively parse it into discrete events -- stable periods separated by event boundaries. An event is defined as a period of time at a particular location with a beginning and end, during which some aspect of the situation is stable or unfolding in a predictable way. Boundaries mark the transitions. The paper reviewed evidence from action perception (people agree remarkably well on where action sequences begin and end), narrative comprehension, and spatial cognition, arguing that event-level organization is a fundamental computational strategy for managing experience.

## Key findings relevant to MECH-100

Two findings matter for MECH-100. First, event boundaries are consistently associated with heightened perceptual attention and prediction error -- the moments when one event type ends and another begins are the moments where prediction is most uncertain and neural systems must update their situation model. Second, hierarchical event structure is pervasive: events nest within larger events (putting milk in coffee is an event within the event of making coffee), and the hierarchical organization maps to hierarchical goal structure. These two findings together support the design decision to use discrete event-type labels for z_world supervision: the labels (none / env_hazard / agent_hazard) correspond to stable event periods, and the boundaries between them are exactly the moments of elevated prediction error that MECH-100 wants z_world to represent.

## REE translation

MECH-100's core claim is that reconstruction loss trains z_world to represent the most statistically prominent continuous features (locomotion) rather than the event-type distinctions that matter for harm evaluation. Event segmentation theory provides a theoretical basis for why this is the right problem framing: the perceptual system should represent event type (the stable content of the current period) rather than only the ongoing feature trajectory. The CE auxiliary loss forces z_world to maintain event-type categorical information, which is architecturally consistent with a system that organizes its representations around event segments. The none/env_hazard/agent_hazard labels are coarse event categories, but they capture the harm-relevant event structure that the agent needs to navigate safely.

## Limitations and caveats

The main limitation is the level of description. Event segmentation theory is a cognitive account of how humans parse naturalistic experience -- it does not speak to gradient-based training of neural network encoders. The claim that "this is the right unit for z_world supervision" draws on the theory for motivation but requires additional computational justification that the theory does not provide. Furthermore, the grid-world events in REE are simpler and more abrupt than the naturalistic events Zacks studies (a hazard tile either is or is not present; this is not the same as the gradual scene changes that constitute event boundaries in video-watching experiments). The theory provides conceptual framing but is not a mechanistic grounding for MECH-100.

## Confidence reasoning

Confidence is 0.58. The paper supports the conceptual decision to use discrete event-type categories as z_world training supervision, but the mechanistic connection between event segmentation theory and CE auxiliary loss training is indirect. This entry is best understood as providing theoretical motivation for the label design rather than direct mechanistic evidence for MECH-100. The strongest evidence for MECH-100 remains the experimental results (EXQ-020 PASS) that directly demonstrated selectivity improvement with the CE auxiliary loss. This entry adds biological and cognitive grounding to why that design choice is principled.
