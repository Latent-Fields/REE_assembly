# A circuit mechanism for differentiating positive and negative associations

Namburi, Beyeler, Yorozu, Calhoon, Halbert, Wichmann, Holden, Mertens, Anahtar, Felix-Ortiz,
Wickersham, Gray & Tye (2015), *Nature* 520(7549):675-678.
DOI [10.1038/nature14366](https://doi.org/10.1038/nature14366) - PMID 25925480 - PMC4418228.
Retrieved via PubMed.

## What the paper does

Within a single structure -- the basolateral amygdala -- how does a brain keep "this cue predicts
something good" apart from "this cue predicts something bad"? Namburi et al. answer with a
projection-defined dissociation. BLA neurons projecting to nucleus accumbens and BLA neurons
projecting to centromedial amygdala are intermingled but distinguishable, and they undergo
*opposing* synaptic changes after conditioning: reward conditioning potentiates the NAc projectors,
fear conditioning potentiates the CeM projectors. Optogenetic photostimulation of NAc projectors
supports positive reinforcement; photostimulation of CeM projectors mediates negative reinforcement.
Photoinhibition of CeM projectors impairs fear conditioning and enhances reward conditioning. The
two populations differ further in electrophysiological, morphological and transcriptional profile.

Four methodologically independent lines -- ex vivo synaptic physiology, optogenetic gain- and
loss-of-function, rabies circuit tracing, transcriptomics -- converge on the same population
distinction. That convergence is what makes this hard to dismiss.

## How it bears on MECH-055

MECH-055's NON-DEGENERACY PRECONDITION (b) requires the VALENCE vector's components to be
"independently computable and independently perturbable" with non-zero cross-candidate variance on
at least two components simultaneously. This is the cleanest biological existence proof that such a
condition is satisfiable in a real affective system: two valence channels of opposite sign, inside
one structure, each independently drivable and silenceable, each with a different behavioural
consequence. Mapped onto REE, it supports the design decision behind `VALENCE_COMPONENTS` in
`ree_core/residue/field.py` -- several slots rather than one signed scalar -- and specifically
supports a benefit-approach channel (`VALENCE_WANTING`/`VALENCE_LIKING`) separable from a
harm-avoidance channel (`VALENCE_HARM_DISCRIMINATIVE`).

It also supplies the methodological template. The distinctness verdict here comes from perturbing
one channel's generator and reading *both* channels' downstream roles, which is precisely the form
MECH-055 asks for and precisely what a passive correlation over a free-running rollout would not
give.

## Where it cuts against the claim -- and this is the interesting part

The photoinhibition result is partially adverse, and it should not be buried. Silencing the CeM
projectors both impaired fear conditioning *and* enhanced reward conditioning. One perturbation,
two channels, moving in a fixed opponent relation. Structurally that is MECH-055's own FALSIFIER (i)
-- "any two axes move in a fixed, predictable ratio under manipulations designed to perturb only
one". So the mammalian amygdala, the system we are pointing at as the proof that separate valence
channels are real, would arguably *fail* MECH-055's confirming criterion as currently worded. The
honest reading is that these populations are separable but opponent, not separable and orthogonal,
and that the claim's wording may not have distinguished the two. That is a finding about the claim,
not only about the paper.

Two further limits. The separability here is anatomical, secured by physical segregation into
different projection classes; REE's valence components are slots in one shared residue field driven
by common upstream state, with no such segregation to fall back on, so the precedent supports the
design *goal* without evidencing that REE achieves it. And the axis tested is positive versus
negative valence, which cannot speak to MECH-055's actual COLLAPSE-RISK CHECK -- whether
`VALENCE_HARM_DISCRIMINATIVE` and the dACC-consumed harm forward-model PE carry independent
variance. Those are two representations on the *same* side of the valence axis, and no
positive-versus-negative design can address a within-negative collapse.

## Confidence

0.72. Source quality 0.90 -- Nature, four converging methods, broadly corroborated since. Mapping
fidelity 0.62, the weak component: projection-defined cell classes are a structurally different way
of keeping channels apart than shared-field latent slots, and the positive/negative axis is not
REE's six-component carve-up. Transfer risk 0.50: rodent conditioning to a latent affect vector in
a grid-world agent, no shared task, no shared timescale, and a demonstrated opponent coupling that
REE's falsifier (i) would read as collapse. Recorded as `supports` on the strength of the
independent-perturbability demonstration, with the opponency caveat carried explicitly in
`failure_signatures` rather than allowed to quietly inflate the confidence.
