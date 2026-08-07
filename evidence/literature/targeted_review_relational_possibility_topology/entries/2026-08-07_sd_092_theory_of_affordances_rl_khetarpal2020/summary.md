# What can I do here? A Theory of Affordances in Reinforcement Learning (Khetarpal et al. 2020, ICML)

This is the one purely formal paper in the set, and it earns its place by doing something the
neuroscience papers cannot: giving a mathematically precise definition to one of the relation types
the intake's candidate topology proposes, and proving something useful about it. Khetarpal, Ahmed,
Comanici, Abel and Precup start from Gibson's informal notion of an affordance -- what an
environment lets an agent do -- and formalize it inside the standard MDP framework. An "intent" is a
target state-distribution an action should produce; an affordance is the subset of states where a
given action's intent is actually satisfiable to some precision. Restricting planning to only the
affordance-permitted state-action pairs (an "affordance-based partial model") is then shown to bound
the loss in value relative to planning with the full, unrestricted model -- both when affordances are
handed to the agent and, more usefully, when they are learned from data. Empirically, agents that
plan and generalize over affordance-restricted models do better and more stably than ones that
don't.

The reason this belongs in a pull about a "general relational topology of possibilities" is that it
is, in effect, a rigorous existence proof for exactly one of the listed relation types: "enables."
The intake's Section 6 proposes a family of relations beyond parent/subgoal -- requires, enables,
is-part-of, prevents, conflicts-with, substitutes-for, provides-information-about, may-become-useful-
under-another-context. This paper does not attempt all of them, but it takes "enables" and shows it
is (a) definable with mathematical precision, (b) learnable from experience rather than needing to be
hand-specified, and (c) provably useful for planning once represented explicitly. That is directly
relevant to whether SD-092's existing parent/subgoal relation is really the natural stopping point,
or whether a second, independently well-behaved relation type sitting alongside it is a reasonable
next step rather than speculative overreach.

The limits are worth stating without softening them. This paper formalizes ONE relation type at a
time -- it does not build or analyze a graph carrying several DIFFERENT relation types
simultaneously over the same possibility set, so it says nothing about whether such a multi-relation
structure remains tractable, or whether the relation types would interact or conflict. It also
assumes affordances are learned from a stationary data distribution and then used; it does not model
an agent discovering a brand-new affordance mid-episode as an incidental side effect of pursuing an
unrelated goal, which is the "discovery through action" mechanism the intake's Section 8 formulation
actually needs. And because it is a pure ML-theory paper with gridworld-scale empirical illustrations,
there is no biological grounding step here at all -- unlike the hippocampal entries in this pull, this
one says nothing about whether or how a brain-like substrate would implement this.

Confidence: 0.62, the lowest of the "supports" entries in this pull. Source quality is solid (top ML
venue, formal proofs, not merely a position paper). Mapping fidelity is real but narrow -- it
supports the FORMAL FEASIBILITY of a second labeled relation type, not the full multi-relation,
in-action-discovery topology the intake proposes -- and transfer risk from tabular/function-
approximation MDP theory to REE's actual substrate is not small.
