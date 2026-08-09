# Pfeiffer & Foster 2013 -- Hippocampal place-cell sequences depict future paths to remembered goals

Pfeiffer and Foster recorded hippocampal place cells in rats navigating an open arena toward a
learned "HOME" goal from varying, sometimes novel, start locations. Before the rat set off, brief
sequences of place-cell activity -- the same class of event previously characterised as "replay"
in linear-track experiments -- swept ahead of the animal's actual position, encoding trajectories
strongly biased toward the goal. Critically, these sequences predicted the specific path the
animal was about to take, including for start-goal combinations the animal had never previously
traversed. This is the foundational demonstration that hippocampal sequence events are not merely
a record of the past (recapitulating recently-travelled routes) but a generative, forward-looking
mechanism that can compose novel trajectories toward a currently-relevant destination.

For REE, this is the closest thing to a canonical citation for the pairing MECH-236 (hippocampal
trajectory proposals must be goal-conditioned) and MECH-289 (the hippocampal trajectory generator
actively generates novel-path sequences, not merely recency-weighted replay of executed paths)
already assert independently. Pfeiffer & Foster is the paper that establishes both properties
together in the same recordings: goal-directedness AND novel-sequence generation. It predates and
underlies the two 2026 papers this pull was primarily commissioned to formalise (Yu et al.,
entry `2026-08-09_mech_236_theta_sweeps_goal_direction_yu2026`; Tang et al., entry
`2026-08-09_mech_289_theta_sweeps_swr_pfc_tang2026`), which refine the mechanism (theta-cycle
resolution, egocentric goal-direction coding, dissociation from movement/heading) rather than
establish the basic phenomenon for the first time.

The mapping caveat is the same one that applies to the whole cluster of evidence this pull covers,
and it is worth stating plainly rather than letting the strength of the primary result obscure it:
this is physical spatial navigation in rats. The REE claims it grounds (MECH-236, MECH-289) are
about hippocampal-analog machinery operating over SD-004's action-object space, and the further
hypothesis this pull was commissioned by (the 2026-08-08 thought's proposal that this primitive
generalises to abstract, non-spatial goal-directed cognition) is not tested by this paper at all --
it is architectural extrapolation, honestly flagged as such in SD-098's own claims.yaml entry.

**Confidence: 0.78.** Source quality is high -- this is a landmark, heavily-replicated single-unit
electrophysiology result in a top venue. Mapping fidelity is capped at moderate because the paper's
domain (literal 2D space) is narrower than what REE's hippocampal-module claims actually need to
be true of (a compressed action-object or possibility-topology space), and transfer risk is
correspondingly non-trivial -- the paper cannot distinguish "this primitive is spatial-navigation-
specific" from "this primitive generalises," which is exactly the open question SD-098's own
epistemic boundary names.
