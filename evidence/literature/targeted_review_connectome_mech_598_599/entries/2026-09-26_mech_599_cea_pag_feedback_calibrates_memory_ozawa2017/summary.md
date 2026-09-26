# A feedback neural circuit for calibrating aversive memory strength (Ozawa et al. 2017)

Claims: MECH-599. Direction: supports. Confidence: 0.60. PMID 27842071, DOI 10.1038/nn.4439.

Ozawa and colleagues, from Johansen's lab, found the circuit behind the expectation effect reported in 2010. A cue that predicts shock drives a descending projection from the central amygdala to pain-modulating neurons in the ventrolateral PAG, and these suppress the shock's teaching signal to the lateral amygdala. Block the projection and a predicted shock teaches again as if it were unexpected, and fear learning resets.

For MECH-599 this is how an event-taught store gets its prediction error. The store's own prediction feeds back and cancels the part of the harm signal it already predicted. That closed loop is what makes learning saturate and keeps the store from over-learning. It also connects to the extinction criterion in MECH-599's what_would_answer.

The design implication for REE is concrete. If a ConditionedThreat store is built as a mirror of SD-051, its output should be what subtracts from its own teaching signal. The alternative, a PE computed somewhere else and fed in, would lose this property.

Confidence 0.60. Strong causal work that concerns memory strength and saturation, not cue specificity.
