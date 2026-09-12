# Jin, Krishnamurthy, Simchowitz & Yu 2020 -- the formal analogue, and a citation correction

Jin and colleagues formalise exactly the two-phase structure ARC-074 proposes. In their reward-free
RL framework the agent first collects trajectories from an MDP with no pre-specified reward function,
and is then tasked with computing near-optimal policies for a collection of given reward functions.
They give an efficient algorithm that returns epsilon-suboptimal policies for arbitrarily many reward
functions, achieved by finding exploratory policies that visit each significant state with
probability proportional to its maximum visitation probability under any possible policy, together
with a nearly-matching lower bound. The planning step can be instantiated by any black-box
approximate planner.

Before the substance, a provenance matter that came out of this pull and that I think is the most
actionable finding in it. ARC-074's `description` field currently cites three biological and
computational anchors: "Doupe & Kuhl 1999", "Griffin et al. 2026 (reward-free exploration epoch
before goal-directed RL)", and "Garcia-Guzman 2026 (pre-reward Hebbian phase as prerequisite for
structured curriculum)". Doupe & Kuhl 1999 is real and checks out -- it is the *Annual Review of
Neuroscience* paper on common themes in birdsong and human speech, PMID 10202549. The other two do
not resolve. Neither a PubMed author search nor web search surfaces any such work, and the phrasing
of both reads as a plausible-sounding placeholder rather than a citation. Jin et al. 2020 is the
genuine canonical reference for the thing "Griffin et al. 2026" was standing in for, and I have
entered it partly so the claim has a real anchor to point at. ARC-074's description should be
corrected; I have not edited `claims.yaml` here, since amending a claim's substance is governance
work and not a lit-pull's to do unilaterally.

On the substance, I have marked this `mixed` with the lowest confidence in the pull, and the reason
is a motivation mismatch that is easy to miss because the shape matches so well. Jin et al. explore
once in order to serve *many* reward functions -- the framework is an amortisation result, and it is
explicitly pitched at the case where there are many rewards of interest or where reward is shaped
externally. ARC-074 has a single objective and claims the prologue prevents a *representational
pathology*: without it, E3 cold-starts on a flat residue field and the proposer collapses to
monostrategy. Nothing in this theory speaks to that. A near-optimal sample-complexity bound for
covering an MDP is not an argument that a single-objective agent learns better for having explored
first, and a null result on ARC-074's A/B would contradict nothing here.

The second mismatch is mechanical and, I think, the more dangerous one to gloss. The exploration
policy that makes Jin et al.'s guarantee work is *coverage-maximising by construction* -- it
deliberately visits each significant state in proportion to how visitable it is. ARC-074's Phase 0 is
undirected Hebbian babbling with a residue-entropy gate. That is precisely not a coverage guarantee.
So the property the theory depends on is the property the REE proposal lacks, and citing the theory
as support for the proposal borrows a result whose precondition is unmet. If ARC-074 wants this
literature's backing, the honest route is to make Phase 0 directed -- which would be a real design
change, and would also sit awkwardly beside the claim's Hebbian framing.

Confidence 0.55. Source quality 0.90: foundational, heavily cited, with a matching lower bound, and I
have no doubt about the mathematics. Mapping fidelity 0.50 and transfer risk 0.45 carry the discount
-- finite-horizon tabular MDP theory to a deep embodied agent is a stretch even before the motivation
and mechanism mismatches. Included despite that, because replacing an unverifiable citation with a
real one and then naming precisely where the real one fails to reach is more useful to governance
than leaving the formal analogy unexamined.
