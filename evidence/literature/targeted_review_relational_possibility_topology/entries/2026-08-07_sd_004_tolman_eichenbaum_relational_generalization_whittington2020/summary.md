# The Tolman-Eichenbaum Machine (Whittington et al. 2020, Cell)

Whittington, Muller, Mark, Chen, Barry, Burgess and Behrens set out to answer a specific question:
is the hippocampal-entorhinal system fundamentally a spatial-navigation device that got repurposed
for other memory tasks, or is it fundamentally a *relational-structure* device for which spatial
navigation is just one instance? They build the Tolman-Eichenbaum Machine (TEM) to test the second
hypothesis directly. Medial entorhinal cells in TEM learn a "structural basis" -- an abstract
description of how states relate to one another under the available transitions/actions --
independent of what the states actually contain. Hippocampal cells then bind that structural basis
to whatever sensory or task content is currently present. After training, the model spontaneously
reproduces grid cells, place cells, border cells and object-vector cells as different views of the
same underlying mechanism, and -- crucially for this pull -- it also reproduces recorded hippocampal
and entorhinal activity on non-spatial relational-inference tasks using the identical machinery.

The finding most relevant to the intake this pull was commissioned for is the remapping result. When
TEM is dropped into a new environment, hippocampal cells "remap" (fire in an apparently new,
unpredictable pattern), which historically read as the hippocampus discarding old structure and
starting fresh. TEM predicts, and the paper confirms in simultaneously-recorded real place and grid
cells, that this is not what happens: the *entorhinal* structural code is preserved across the
remap, and only its binding to the new environment's sensory content changes. In other words, the
relational scaffold persists and gets re-used; what looks like forgetting at the hippocampal level is
actually context-switching on top of a stable relational backbone.

For REE, this is close to the strongest available biological argument that SD-004's claim --
action-object structure forming a general hippocampal map backbone, not a spatial-navigation-only one
-- is on the right track, and it does real work for the broader "relational possibility topology"
question this pull exists to inform. If a persistent, content-independent relational code is what the
hippocampal formation actually does, then a topology of possibilities that outlives any single active
goal (Section 3 of the intake: "possibility != desirability != goal candidacy") is exactly the kind of
representation this substrate is built to hold, and TEM's remapping-preserves-structure result is a
plausible mechanism for how a possibility could sit "below active goal status" (candidate 2 in
Section 11) without being deleted between contexts.

The honest limitation, and the reason this entry doesn't push confidence above the high-0.7s, is
that TEM's structural basis is a single homogeneous relational code per task -- it is not built to
hold several *qualitatively distinct, explicitly labeled* relation types (requires, enables,
conflicts-with, is-part-of...) over the same possibility set simultaneously, which is the specific
extension Section 6 of the intake proposes beyond parent/subgoal. Nor does the paper test whether
that relational structure gets *revised* online, during active goal pursuit, the way the intake's key
formulation in Section 8 requires ("goal pursuit is simultaneously traversal of, and learning about,
the relational structure of possible action"). TEM shows the substrate can hold and re-use general
relational structure; it does not show that structure being differentiated by relation type or
rewritten mid-pursuit. Those remain open, and are exactly the falsifiable residue the intake's Section
12 worried about protecting from being "merely a symbolic graph planner called hippocampal."

Confidence: 0.78. Source quality is high (flagship venue, validated against real single-unit
recordings, widely cited and not superseded). Mapping fidelity to SD-004 itself is strong; mapping
fidelity to the specific novel candidate (typed multi-relation, in-action revision) is only partial,
which is the right way to read this entry -- it grounds the substrate's plausibility without closing
the discriminative-test question the intake explicitly deferred to this literature pull.
