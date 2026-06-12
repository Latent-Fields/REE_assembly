# Action understanding as inverse planning (Baker, Saxe & Tenenbaum 2009)

**Claims:** MECH-129 (harm-to-agency signal) · MECH-164 (love as agent-indexed terrain inference)
**Direction:** supports (both) · **Confidence:** 0.70 · **Class:** computational_model

## What the paper did

Baker, Saxe and Tenenbaum take the qualitative idea behind Dennett's "intentional stance" and
Gergely & Csibra's "teleological stance" and give it a precise computational form. If you assume
an agent plans approximately rationally to reach its goals given its beliefs, then observing the
agent's behaviour and asking "what goal makes this behaviour rational?" is a Bayesian *inversion*
of that planning process. Goals are inferred by integrating the likelihood of the observed actions
under a rational planner with a prior over possible goals. They test this against human judgements
in three psychophysics experiments using animated agents moving through simple mazes, and show
that inverse-planning models predict human goal inferences quantitatively -- including the
flexible, online way humans revise a goal hypothesis as an agent's path unfolds.

## Why it matters for MECH-129 and MECH-164

This is the entry where the developmental evidence (Woodward, Gergely & Csibra) becomes a
*computation REE can actually run*, which is why I have tagged it to both claims.

For **MECH-129**, inverse planning supplies the missing piece between a represented goal and a
detected obstruction. Once you have inferred the other's goal by inverting their planner, you can
also score how your own (or the joint) trajectory changes the cost of *their* plan. An action that
raises the cost of the other's optimal plan -- forces a less efficient route, or makes the goal
unreachable -- is exactly the goal-interference signal MECH-129 wants to feed into E3 alongside
the existing harm-to-agent signal. Discriminant (2), "whether your action obstructs it," becomes a
quantity you can compute rather than merely assert.

For **MECH-164**, the mapping is even tighter, and it is worth being exact about it. MECH-164's
component 1 is "agent-indexed terrain instantiation: infer what another agent would be inferring
about the hippocampal terrain (their goal and harm gradients)... indexed to them, not to self."
Inverse planning *is* that inference, written down: inverting the other's planner over the residue
field recovers their goal gradient (and, with a harm-augmented cost, their harm gradient), indexed
to their perspective. The project's own implementation note for MECH-164 says z_world is already a
residue field rather than a fixed self-centred map, so "agent-indexing is a matter of whose context
seeds the terrain model" -- which is precisely the prior-over-goals-plus-rational-planner that
Baker et al. formalise. This paper is the computational backbone for component 1.

## Limitations and caveats

The honest boundary, and the reason this is 0.70 rather than higher, is twofold. First, the
validation is toy: 2D mazes, fully-observed actions, discrete goals, human looking/judging as the
criterion. It proves the computation is humanlike in a small domain, not that it scales to a
multiagent REE terrain with partial observability and a real inference budget. Second -- and this
is the important conceptual limit -- inverse planning covers goal *recovery* (MECH-164 component 1)
but says nothing about self-like *weighting* of the recovered goals into one's own value function
(component 2). Recovering what the other wants is not yet caring about it; that is the structural
symmetry MECH-164 adds, and the calibration RHM-5 leaves open. There is also a failure mode REE
inherits directly: inverse planning only works when the observer's model of the other's planning is
approximately right. Under model mismatch, goal inference degrades -- and a degraded, badly-inferred
terrain is exactly what RHM-5 warns must *not* be weighted self-like (the route to mis-attributed
care). That failure signature is a useful design constraint to carry into the RHM-1/RHM-4 substrate.

According to PubMed, the citation is Baker, C. L., Saxe, R., & Tenenbaum, J. B. (2009), *Cognition*
113(3):329-349,
[DOI 10.1016/j.cognition.2009.07.005](https://doi.org/10.1016/j.cognition.2009.07.005).
