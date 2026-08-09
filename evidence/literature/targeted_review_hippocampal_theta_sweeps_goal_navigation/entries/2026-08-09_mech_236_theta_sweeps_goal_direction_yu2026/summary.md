# Yu, Ji, Ormond, O'Keefe & Burgess 2026 -- Hippocampal theta sweeps indicate goal direction during navigation

This is the primary source behind the medicalxpress press report that prompted the 2026-08-08
REE thought ("prospective navigation through goal topology") this whole lit-pull traces back to.
Yu and colleagues used the "Honeycomb" maze -- a task purpose-built to dissociate three variables
that are normally confounded in an open arena: which way the rat's head is pointing, which way
it is actually moving, and where its remembered goal lies. Against that dissociation, they found
that hippocampal theta sweeps -- rapid, sub-second sequences of place-cell activity within a
single theta cycle -- form directional vectors that point toward the remembered goal location,
and that this goal-pointing is independent of the rat's current heading or movement direction.
The strength of this goal-modulation predicted whether the rat then made the correct navigational
choice.

The paper's own abstract states plainly that before this and the companion Tang et al. paper
(entry `2026-08-09_mech_289_theta_sweeps_swr_pfc_tang2026`), whether theta sweeps reflect
movement, perceptual targets, or genuine cognitive goal-directed planning was "unresolved" -- this
is not incidental framing; it is the field's own acknowledgement that goal-directedness had to be
established, not assumed, and the dissociation design is what makes this paper more than a
confirmation of Pfeiffer & Foster 2013's older, less controlled result.

For REE, this maps most directly onto MECH-236's specific architectural premise: that a hippocampal
trajectory proposer needs a dedicated, goal-conditioned input channel (`z_goal`) distinct from raw
positional information, because without it "the hippocampal module generates only position-based
trajectories." Yu et al. is direct biological evidence that the brain's own analogous system does
exactly this dissociation -- goal-direction coding that survives controlling for movement and
heading. It also bears on MECH-289's online/theta-analog generative mode specifically.

It says nothing about SD-098's actual claim (whether goal/subgoal status is a stored node property
or a relationally-computed one) -- that is an implementation-level distinction the biology cannot
adjudicate, and this entry's `claim_ids_tested` deliberately omits SD-098 for that reason, matching
the honesty already recorded in SD-098's own `literature_evidence` field in `claims.yaml`.

**Confidence: 0.72.** The verbatim abstract was independently verified, and the paper's design and
authorship (O'Keefe, Burgess -- both long-standing, leading names in hippocampal place-cell and
cognitive-map research) are strong. Held below 0.8 because I could not reach the full text --
`nature.com` redirects to an authentication wall and the bioRxiv preprint returned HTTP 403 to
automated fetch -- so effect sizes, sample sizes, and statistical tests are not independently
confirmed here, only the qualitative claim in the abstract.
