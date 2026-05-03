# Smith & Berridge 2007 -- Hedonic Hotspots in NAc and VP

## What the paper does

Smith and Berridge ran a targeted double-dissociation experiment on
the neural circuitry of wanting versus liking. They microinjected the
mu-opioid agonist DAMGO into either the nucleus accumbens (NAc) shell
hedonic hotspot or the ventral pallidum (VP) hedonic hotspot in
Sprague-Dawley rats, and measured two behaviors separately: orofacial
"liking" reactions to sucrose (the taste reactivity test, well-validated
as a hedonic-impact measure that does not require consummatory motor
behavior), and "wanting" as indexed by spontaneous food intake. They
also used Fos immunohistochemistry to assess whether activating one
hotspot recruited the other.

## Key findings

Two findings matter for SD-049.

The first is that *liking is cooperative*. Activating either hotspot
alone produced a partial increase in liking reactions; activating both
together produced a non-additive amplification, and the two hotspots
reciprocally modulated each other's Fos expression. This is the kind
of cross-region cooperation that defines a circuit, not two parallel
loci.

The second is that *wanting is hotspot-dominated*. Activating NAc alone
was sufficient to drive a full increase in food intake; concurrent VP
activation added nothing detectable. Wanting and liking therefore live
on different architectural shapes -- one is a cooperative two-node
circuit, the other is a single-node-dominated function. They share the
NAc shell as a common substrate, but they recruit different
extra-NAc circuitry.

## How this maps to SD-049

For REE substrate purposes the takeaway is not the specific
neuroanatomy but the experimental template: *targeted perturbation of
one channel while measuring response in the other*. Smith and Berridge's
paradigm is "microinject DAMGO here, measure that behavior". SD-049's
analog is "satiate this drive axis, measure trajectory choice across
identities". The substrate's per-axis drive system is what makes the
perturbation possible -- without per-axis drives, satiating "hunger"
also reduces every other approach signal because there is only one
drive scalar. With per-axis drives, you can drive hunger to zero while
leaving novelty-deficit intact, then observe whether the agent still
routes toward the novelty cell. If wanting and liking are architecturally
dissociable in the agent, the answer is yes; if they are not, the
agent's trajectory will follow whichever axis happens to be most
depleted, and MECH-229 fails on that substrate.

The paper is also relevant to ARC-030's approach-avoidance symmetry
claim. The cooperative-vs-dominant asymmetry between liking and wanting
is a structural symmetry-breaking result in the neural circuitry.
ARC-030 asks whether REE's go and nogo channels are symmetric across
goal types; with multi-resource heterogeneity in place, that question
becomes testable in a way it currently is not.

## Caveats and confidence reasoning

The mapping from rodent NAc-VP microinjection to a grid-world agent's
substrate-level perturbation is structural, not implementational. There
is no opioid system, no NAc, no VP in CausalGridWorldV3. What transfers
is the architectural principle that wanting and liking are separable
channels that respond differently to targeted perturbations -- and the
experimental template for testing whether they are separable in a given
substrate. The substrate-level perturbation analog is coarser than the
microinjection paradigm, but it is the right grain for substrate-level
testing.

A second caveat is that Smith and Berridge document a *cooperative*
architecture for liking (two-node) versus a *dominant* architecture for
wanting (one-node). SD-049 does not encode any prediction about which
architecture the agent will learn -- the substrate is permissive on
this point. The cooperative-vs-dominant distinction is a higher-order
architectural claim worth flagging for future SD work but it is beyond
SD-049's current scope. SD-049's job is to make the dissociation
observable; it does not claim to test which architecture the agent
acquires.

Confidence 0.82. Source quality 0.85 (J Neurosci, well-controlled
microinjection design, statistically robust). Mapping fidelity 0.78
(the most direct neural-substrate evidence for the framework SD-049
implements behaviorally; gap is anatomical specificity). Transfer risk
0.32 (architectural shape transfers; implementation does not).

## Attribution

Source: PubMed PMID 17301168. DOI:
[10.1523/JNEUROSCI.4205-06.2007](https://doi.org/10.1523/JNEUROSCI.4205-06.2007).
Smith KS, Berridge KC. Opioid limbic circuit for reward: interaction
between hedonic hotspots of nucleus accumbens and ventral pallidum.
J Neurosci. 2007 Feb 14;27(7):1594-605.
