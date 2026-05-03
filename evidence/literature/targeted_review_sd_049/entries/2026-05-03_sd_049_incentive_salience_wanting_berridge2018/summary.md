# Berridge 2018 -- Evolving Concepts of Emotion and Motivation

## What the paper does

Berridge surveys three decades of evidence for a tripartite separation in
how mammalian brains construct motivation. The argument is that what we
loosely call "wanting" decomposes into at least two distinct processes:
*incentive salience*, an unconscious mesocorticolimbic-dopamine-mediated
attribution of motivational urgency to a stimulus, and *cognitive desire*,
a propositional, declarative, prefrontal process that says "I want this".
These two ordinarily run together, but they can dissociate -- in
addiction, in depression, in clinical anhedonia, and in some cases of
schizophrenia. A third process, *hedonic impact* or "liking", is the
sensory-pleasure response to consuming the reward; it has its own
neural substrate (opioid hedonic hotspots in NAc and ventral pallidum)
and can dissociate from "wanting" in addictive disorders (extreme
"wanting" without "liking" of the drug).

## Key findings relevant to SD-049

Three things matter for the substrate roadmap.

First, the wanting/liking dissociation is mechanistically real and well-
characterised. It is not a philosopher's distinction; it is two anatomically
separable signal channels with characteristic behavioral signatures.
That is the architectural shape MECH-229 asserts about REE.

Second, the dissociation is *observable at the behavioral level* via
trajectory analysis: an addict animal will work harder for a drug
whose hedonic impact has waned, will pursue the cue more vigorously
than the consummatory act, and will self-administer despite no longer
preferring the substance in choice tests. These are exactly the kind
of trajectory-level metrics that V3-EXQ experiments can score on a
grid-world agent, *if* the substrate provides the option for wanting-
target to differ from liking-target.

Third, the framework is universalist about the dissociation but specific
about the conditions under which it is observable. Berridge is clear
that with normal mammalian motivation, "wanting" and "liking" usually
co-occur and converge on the same target. Dissociation appears under
specific perturbations: pharmacological (drugs, opioid antagonism),
clinical (addiction, depression), or experimental (artificial cue
sensitisation). For SD-049, this means the substrate has to give the
*possibility* of dissociation, but the *test* will involve seeding
specific contexts where the dissociation should appear.

## How this maps to SD-049

The novelty channel is the lynchpin. Without it, every resource is
homeostatic, and "wanting" and "liking" both track the same drive
deficit -- in Berridge's terms, this is the normal-mammalian convergent
case where the dissociation is invisible. With novelty, the agent can
"want" a novel target whose consumption does not reduce a homeostatic
deficit, while concurrently "liking" food consumption that does. The
trajectory diverges: the agent approaches the novelty cell first even
though the food cell would satiate. That trajectory class is the
behavioral analog of Berridge's incentive-sensitisation cases (drug-
seeking despite no current "liking"), and it is the operational
target of MECH-229's pre-registered "wanting != liking trajectory
fraction" metric.

The per-axis drive system implements the corollary. With a single
scalar drive, "wanting" can never dissociate from "current depletion".
With per-axis drives, the agent's persistent goal state (z_goal)
can carry an identity that differs from the axis currently most
depleted -- which is the structural shape of MECH-230's z_goal latent
structure claim.

## Caveats and confidence reasoning

Berridge is the originator of the framework, and the review is
authoritative but not new evidence -- it is a theoretical synthesis
across thirty years of his lab's work. The mapping to a grid-world
agent is structural, not implementational: there is no
mesocorticolimbic dopamine system in CausalGridWorldV3. The transfer
risk is moderate: the architectural dissociation is at the level of
signal-channel separability, which generalises to any system that has
multiple separable signal channels with characteristic behavioral
signatures, but the *content* of those signals (drug-cue salience,
opioid-mediated pleasure) is mammalian-specific. The proposed
substrate-level metric ("wanting != liking trajectory fraction") is the
right level of abstraction for the transfer.

Confidence 0.84. Source quality 0.88 (canonical, peer-reviewed,
authoritative). Mapping fidelity 0.85 (the structural dissociation is
exactly what MECH-229 asserts). Transfer risk 0.30 (architectural
shape transfers; neural substrate does not).

## Attribution

Source: PubMed PMID 30245654. DOI:
[10.3389/fpsyg.2018.01647](https://doi.org/10.3389/fpsyg.2018.01647).
Berridge KC. Evolving Concepts of Emotion and Motivation. Front Psychol.
2018;9:1647.
