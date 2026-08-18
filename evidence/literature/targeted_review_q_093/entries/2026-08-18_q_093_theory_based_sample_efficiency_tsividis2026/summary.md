# EMPA: matched-competence sample efficiency from structured causal models

Tsividis and colleagues studied how people learn 90 simple but genuinely challenging video
games, and found that most are learned within a few minutes. They then built an agent — EMPA,
the exploring, modelling and planning agent — around what they call theory-based reinforcement
learning: rich, abstract, causal representations of objects, agents and their interactions,
used to explore, model the environment, and plan toward goals. EMPA matches human learning
efficiency, generalises to new game situations and levels as humans do, and shows similar
exploration and learning dynamics. The comparison class — leading machine RL — reaches
comparable competence only with vastly more experience.

This is the strongest entry in the Q-093 pull, and the reason is methodological as much as
substantive. Q-093 goes out of its way to state a non-degeneracy precondition: comparing
lifetime cost at *unmatched* competence proves nothing about efficiency, only about the
competence gap, and the claim declares itself untestable until matched comparison points
exist. Nearly every efficiency argument in this literature quietly violates that. This one does
not. The comparison is anchored to human performance on a shared task family, so it is made at
approximately matched competence by construction — and what is then measured is exactly one of
Q-093's cost terms, environmental experience per acquired capability. It is the nearest thing
in the published literature to a worked example of the protocol Q-093 says it needs, which is
worth more to the claim than another perplexity result would be.

Substantively it is an existence proof for the architectural bet. Persistent structured causal
state plus selective computation over it reaches a competence level that model-free scaling
reaches only through brute experience. That is REE's wager in a different accent.

Now the three things that keep this at 0.72 rather than higher, in descending order of how much
they worry me. First and most seriously: EMPA matches human *sample* efficiency, and the paper
does not establish matched *compute*. Theory-based exploration and planning are expensive per
decision. Under Q-093's total-lifetime-cost denominator, experiential efficiency bought with
inference cost may net to nothing — and this is precisely the term the Sardana entry in this
same directory shows can relocate an optimum. It is the single most important unresolved
quantity for the claim, and neither paper closes it.

Second, EMPA's structured priors over objects and agents are hand-specified. Q-093's confirming
direction requires that *acquired* structure persists and pays off — that a mature system stays
efficient because it has built something, not because it was given something. A demonstration
resting on built-in structure evidences the value of having the right abstractions, not the
value of having learned them. For REE, where z_world and the episodic and semantic structures
are meant to be developmentally acquired, that gap is the whole interesting part.

Third, the task family is 90 2D games organised around objects, agents and interactions —
exactly the domain intuitive theories are well matched to. An efficiency dividend demonstrated
where the right abstractions are effectively handed over may not survive where they must first
be found. Worth holding lightly: it is a limitation of the demonstration, not evidence against
the hypothesis.
