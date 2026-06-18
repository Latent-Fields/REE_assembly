# Daw et al. 2006 -- frontopolar substrate for exploratory decisions (MECH-314)

According to PubMed, Daw, O'Doherty, Dayan, Seymour & Dolan (2006), *Cortical substrates for
exploratory decisions in humans*, Nature ([DOI](https://doi.org/10.1038/nature04766)).

**What the paper did.** In a four-armed "restless bandit" gambling task, human choices were fit by
a computationally principled explore/exploit strategy, and each decision was classified as
exploratory or exploitative. fMRI then showed a clean dissociation: **frontopolar cortex** and
intraparietal sulcus were preferentially active during *exploratory* decisions, whereas striatum
and ventromedial prefrontal cortex showed activity characteristic of value-based *exploitative*
decisions. The authors frame action selection under uncertainty as switching between exploratory
and exploitative behavioural modes.

**Why it matters for MECH-314 (secondary).** This is the secondary leg of the CDQ-002 intake. The
RND/Plan2Explore family is the *directed-curiosity* analog (novelty / model-disagreement), mapped
to REE's MECH-314 `structured_curiosity_bonus` and ARC-065's substrate (b) frontopolar
uncertainty-driven curiosity. Daw et al. is the neural warrant that a dedicated directed-exploration
substrate exists and is anatomically distinct from value-based exploitation -- which is precisely
the architectural commitment ARC-065 makes (diversity generation is a substantive function, not a
by-product of softmax sampling). It complements the MECH-313 primary anchors (Aston-Jones & Cohen;
Tervo et al.): NoisyNet is the undirected-floor leg (a), RND/Plan2Explore the directed-curiosity
leg (b), and biology distributes the two.

**Caveat and confidence.** The paper localises exploration to frontopolar/IPS but does *not* show
that the exploratory drive is computed as model-disagreement or prediction-error novelty
specifically; the RND/Plan2Explore disagreement form is a computational choice, evidenced here only
at the level of "a directed-exploration substrate exists." The human bandit task is also a step
removed from REE's per-candidate-curiosity-into-E3-selection locus (and from the V3-EXQ-590a
non-propagation problem the secondary candidate must address). I score it `supports` at 0.72:
foundational Nature source, moderate mapping fidelity (right substrate, not the specific
computation), moderate transfer risk.
