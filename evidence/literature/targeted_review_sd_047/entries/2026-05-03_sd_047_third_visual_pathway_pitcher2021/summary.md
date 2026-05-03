# Pitcher & Ungerleider (2021): Third Visual Pathway

The two-pathway model of primate visual cortex — ventral for identity,
dorsal for location and affordance — has been the textbook story since
Ungerleider's own 1982 paper. Pitcher and Ungerleider's 2021 *TICS*
review proposes a revision that is directly relevant to where SD-047
sits architecturally. They argue that a third pathway, lateral on the
brain surface, projects from early visual cortex via motion-selective
areas (V5/MT and surroundings) into the superior temporal sulcus
(STS), and that this pathway is specialised for *dynamic* social
signals: facial expressions, eye-gaze, audio-visual integration,
intention, and mood.

The mapping into REE is unusually direct. MECH-095 commits the
architecture to a TPJ-analog agency-detection comparator. The
substrate-ceiling diagnosis on MECH-095 (annotated 2026-05-02 from
EXQ-506) is that CausalGridWorldV3's "other-caused" change is too
sparse and too scheduled to give such a comparator the input
distribution it needs to learn the agent-vs-not-agent distinction
robustly. The Pitcher and Ungerleider account is the strongest
biological grounding I can find for the *kind* of input the comparator
expects: dynamic, time-extended, motion-laden, interactional. Sparse
scheduled hazards generate none of those statistics. SD-047's three
sources (smooth perturbation field, transient Poisson events,
background drift sources) are an attempt to deliver something closer
to that distribution without yet attempting the V4 multi-agent
ecology where genuinely intentional other-agents live.

Where the mapping has slack: the review does not directly establish
that environmental richness is *necessary* for the comparator to
converge. It establishes that the comparator's *input vocabulary* in
biology is dynamic and interactional. The inference from input
vocabulary to env-substrate requirement is plausible but is one step
removed from the empirical evidence the paper provides. A clean
falsification of SD-047 would be: implement the multi-source dynamics,
find that the comparator still fails C1-C3, conclude that the
discriminative features at issue are not the smoothness /
autocorrelation / sparsity dimensions SD-047 manipulates but
something else (motion contingency, goal-directedness, biological-
motion signatures) that the V3 substrate cannot deliver without
genuine other-agents. That would route MECH-095 from substrate-
ceiling under V3 to V4-bound under v4_spec.md.

Confidence reasoning: this is a TICS review by the senior figure in
visual pathway architecture, so source quality is high. Mapping
fidelity is moderate because the inference chain is two steps.
Transfer risk from primate cortex to a continuous-attractor REE-style
agent is low for the architectural commitment, higher for the
specific feature-vocabulary claim. Net confidence ~0.78 — clearly
supportive but not load-bearing alone.

According to PubMed, [DOI: 10.1016/j.tics.2020.11.006](https://doi.org/10.1016/j.tics.2020.11.006).
