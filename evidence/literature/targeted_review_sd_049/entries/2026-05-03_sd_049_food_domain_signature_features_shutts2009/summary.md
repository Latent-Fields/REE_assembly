# Shutts, Condry, Santos & Spelke 2009 -- Core Knowledge and the Food Domain

## What the paper does

Shutts and colleagues investigated the origins of a striking
cross-species pattern: adults, preschool children, and adult rhesus
macaques all categorise food objects using substance properties
(primarily color and texture), but categorise artifacts using shape
and rigidity. The same observers, looking at the same kinds of objects,
deploy different feature dimensions depending on what category the
object belongs to. The question Shutts et al. asked is whether this
category-specific use of feature dimensions is innate (an instance of
core knowledge in Spelke's sense) or whether it is learned. They ran
six experiments using looking-time paradigms with 8-9-month-old human
infants and identical displays with adult macaques.

## Key findings

The authors found a clear dissociation. Adult macaques showed the
category-specific feature use that prior work has documented in adult
humans -- they generalised food properties by color but artifact
properties by shape. Eight-month-old human infants did not. They
*detected* substance information for foods (they could remember it
when tested), but they did not privilege substance information during
categorisation. They treated food and artifact stimuli the same way.
The category-specific signature is therefore acquired across
development, not present at birth.

This is a tighter claim than "infants don't know things". They have
the perceptual sensitivity; what they lack is the categorisation
priority -- the structural rule that says "for foods, attend to
substance; for tools, attend to shape". That rule emerges with
experience.

## How this maps to SD-049

The architectural constraint for SD-049 is that biological agents do
not categorise all goal types using the same feature dimensions. If
the substrate gives the agent food cells, water cells, and novelty
cells that differ only in an identity tag (one-hot embedding) but are
otherwise perceptually identical, the substrate has not really tested
identity-distinct goal selection -- it has tested whether the agent
can attach an arbitrary tag to identical stimuli. That is a much
weaker test than what the cohort wants.

The substrate-design implication is that food, water, and novelty
should differ in qualitatively different feature dimensions, not just
in identity tag. SD-049's default config goes part of the way:
different drive axes (hunger vs thirst vs curiosity), different
satiation curves (sigmoidal vs sharp vs novelty-decay), and different
spawn distributions. These are reasonable analogs, but the choice has
not been validated against the Shutts finding. A future iteration of
the substrate could vary the spatial signature per type more strongly
(e.g. food in clusters, water in lines along grid edges, novelty
scattered uniformly), to give the encoder a richer set of features to
attend to per type.

For SD-015, this constrains the z_resource encoder design. The encoder
should not be a generic identity classifier that just learns to read
the one-hot tag; it should be permissive of type-specific feature
attendance, so the encoder learns to attend to the right features for
each type. This is a soft constraint -- the substrate provides the
features, the encoder learns the attention -- but it should be built
into the validation: the encoder identity-recovery accuracy metric in
the SD-049 design doc should be tested under spatial-feature ablations
(can the encoder still recover identity if you remove spatial bias?
benefit-curve shape? both?).

For Q-030 (the 6-cell z_resource x z_world routing sweep), the
implication is that routing asymmetries should respect type-specific
feature dimensions, not collapse to a generic identity-routing. This
sharpens the question: it is not just "does z_resource route to
z_world", but "does z_resource route to z_world via the right features
for each resource identity".

The curriculum hook is also relevant. Shutts et al.'s developmental
finding -- that the category-specific feature use takes time to
emerge -- suggests that a developmentally-staged introduction of
resource types should respect the timescale on which the agent
acquires identity-distinct categorisation. For the immediate substrate
work, this is a downstream concern; for the broader developmental-
schedule scaffold, the curriculum hook is the right place to express
this.

## Caveats and confidence reasoning

The paper studied perceptual categorisation in primate looking-time
paradigms; SD-049 is grid-world goal selection. The architectural
takeaway (different goal classes warrant different feature dimensions)
transfers cleanly; the specific feature taxonomy (color/texture for
food, shape/rigidity for artifacts) does not, because grid-world
features are not the same as visual scene features.

A second caveat is that this paper is one step removed from MECH-229's
wanting/liking dissociation, which is the primary cohort SD-049
unblocks. The Shutts finding is more directly relevant to SD-015 (the
z_resource encoder design) and Q-030 (the routing sweep). For MECH-229,
the relevance is structural: the wanting/liking dissociation is more
likely to emerge when the substrate carries genuine type-specific
features rather than identity-only differences.

A third caveat: the developmental finding (8-month-olds don't yet show
the dissociation) is a falsifier-adjacent observation for the
curriculum hook. If type-specific categorisation requires substantial
training-time exposure to develop, then the validation experiment
should report whether identity discrimination emerges within a single
training run. If it does not, the curriculum hook becomes load-bearing
earlier than expected and the staged-introduction design becomes part
of the validation rather than a downstream concern.

Confidence 0.74. Source quality 0.85 (Cognition, Spelke lab, rigorous
multi-experiment design). Mapping fidelity 0.65 (substrate-design
implication is real but one step removed from the primary MECH-229
cohort). Transfer risk 0.45 (looking-time paradigms in primates do not
directly transfer to grid-world agents, but the architectural principle
does).

## Attribution

Source: PubMed PMID 19409538. DOI:
[10.1016/j.cognition.2009.03.005](https://doi.org/10.1016/j.cognition.2009.03.005).
Shutts K, Condry KF, Santos LR, Spelke ES. Core knowledge and its
limits: the domain of food. Cognition. 2009 May;112(1):120-40.
