# Commitment and Effectiveness of Situated Agents (Kinny & Georgeff 1991, IJCAI)

This entry was chosen deliberately to argue the OTHER side of the question this literature pull
exists to answer, in direct response to the intake's own Section 12 worry: "how can the proposal be
falsified without merely implementing a symbolic graph planner and calling it hippocampal?" Kinny and
Georgeff built one of the first systematic empirical testbeds for exactly this class of question,
using the Tileworld simulated environment and the PRS real-time reasoning system. They varied one
environmental parameter -- gamma, the rate at which the world changes relative to the agent's own
clock -- and one agent parameter: how many plan steps a "bold" agent (which never reconsiders a
committed plan mid-execution) versus a "cautious" agent (which reconsiders after every step) will
tolerate before checking whether its commitment is still worthwhile. Agent effectiveness was measured
as the fraction of achievable score actually achieved.

The result is clean and, for this pull's purposes, uncomfortable in a useful way. At low dynamism, a
bold agent that reconsiders nothing achieves essentially perfect effectiveness (E approx. 1) -- the
world doesn't change fast enough to invalidate its plans before it finishes them. As dynamism
increases past a threshold, effectiveness falls off sharply and then more gradually toward zero,
and a more reconsideration-happy strategy starts to win because it can adapt, at the cost of spending
some of its budget on reconsideration itself. In other words: a large, unremarkable class of
environments requires NO extra machinery at all beyond "have a plan and follow it," and where extra
machinery does help, the paper's own account of why is almost entirely captured by a single scalar
(how fast is the world changing), not by any stored relational structure.

This matters for the intake's candidate claim in a specific, narrow way, and it would be dishonest to
overstate it. Kinny and Georgeff's agents have no analog of a retained topology of possibilities at
all -- reconsideration here means re-planning from the current state, not consulting a persistent
structure of previously-noticed subgoals, superordinate goals, or orthogonal side-possibilities. So
this paper cannot show that REE's fuller proposal (which explicitly wants to RETAIN low-relevance
possibilities across time and across contexts, the job MECH-292's ghost-goal bank already does) is
unnecessary -- Tileworld-style bold/cautious agents simply don't attempt that job at all. What the
paper DOES show is that the narrower question of "when should an agent reconsider or abandon its
current commitment" -- one strand of what the intake's Section 1 describes -- is, in a well-studied
class of environments, almost fully explained by a cheap policy tied to environmental dynamism. That
is a real burden of proof: before registering a claim that a general multi-relation-type topology is
NEEDED (not merely sufficient or elegant) for goal reconsideration behaviour, the discriminative test
this intake's Section 12 called for should be built to show behaviour this paper's simple model
cannot already produce.

Confidence: 0.55, and evidence_direction is "mixed" rather than "weakens" precisely because the paper
argues both ways depending on the dynamism regime -- it is exactly as much evidence that richer
machinery becomes necessary as dynamism rises as it is evidence that no machinery beyond ordinary
commitment is needed when dynamism is low. Source quality is good for a 34-year-old result: it has
been systematically replicated and extended (Schut & Wooldridge and others cite it as the founding
empirical study of intention reconsideration). Mapping fidelity is moderate-low because the paper's
"world" has no persistent, typed relational structure to compare against, and transfer risk from a
1991 discrete symbolic Tileworld agent to REE's continuous learned V3 substrate is real and openly
accepted here -- this entry earns its place as a sceptical baseline, not as a mechanism to import.
