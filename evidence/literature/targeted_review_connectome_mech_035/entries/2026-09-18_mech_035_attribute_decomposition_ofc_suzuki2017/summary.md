# Elucidating the underlying components of food valuation in human OFC (Suzuki, Cross & O'Doherty, 2017)

**Claim tested:** MECH-035 -- VALENCE is vector-valued and ranked without scalar collapse.
**Direction:** mixed | **Confidence:** 0.71

## What the paper does

Suzuki, Cross and O'Doherty ask what a food's subjective value is *made of*. Participants reported
their beliefs about the nutritive constituents of a set of foods -- protein, fat, carbohydrate,
vitamin content -- and were scanned while valuing and choosing among them. Subjective value turned out
to be predictable from those beliefs. More interestingly for our purposes, the two things were
represented in different places: lateral orbitofrontal cortex carried the elemental attributes
separately, while medial orbitofrontal cortex carried the integrated overall value assembled from
them.

## What it says about MECH-035

Of the six papers in this directory, this is the one that changed how I think the claim should be
tested, and it did so by refusing to take a side.

MECH-035 is posed as a binary: VALENCE is a vector ranked without collapse, or it is a scalar wearing
a vector's clothes. Suzuki et al. show a brain doing both, in sequence, in separate tissue. The
component-wise representation is real and separable. The integrated scalar is also real. They are not
competing hypotheses about one stage; they are two stages. Which means the claim's actual content is
not "vector or scalar" at all. It is: *at which stage does the ranking read?* If E3 (ARC-003) consumes
the uncollapsed vector and compares candidates by dominance, MECH-035 holds. If E3 consumes an
integrated summary, then the vector upstream is decoration, and the claim is false in exactly the
manner it specifies -- "functioning as a de facto scalar reward regardless of its vector
representation".

That reframing is worth more to MECH-035's first experiment than either of the partisan entries in
this directory. It says the experiment must instrument the *read*, not the representation. Showing
that REE's VALENCE components are independently computable per candidate -- the claim's own
non-degeneracy precondition -- is necessary and, on this paper's evidence, nowhere near sufficient. A
lateral-OFC-shaped result is fully compatible with a medial-OFC-shaped collapse sitting downstream of
it.

## Limitations and what could go wrong

The attributes here are the wrong kind of components for the question REE is asking. Macronutrients
compose. Protein and fat both contribute to how good a food is, on the same axis, in the same
direction; integrating them into one number is not a loss of structure so much as the point. REE's
streams are asserted to be non-composable in precisely the way macronutrients are composable -- HARM
and option volume are not two ingredients of a single super-good. So the paper demonstrates attribute
decomposition in the benign case and is silent on the contested one. If anything, the ease with which
these attributes integrate is a caution: integration is the default when components are commensurable,
and the burden is on MECH-035 to show REE's are not.

The second limitation is about direction of inference. The staging is read off representational
content, not off a causal manipulation. Nothing here shows that medial OFC's integrated value is what
choice consumes; it shows only that both quantities are present and that one is decodable from the
other's constituents. The same caution applies double to any REE analogue.

I have also not independently verified the sample size -- it is not stated in the abstract and I did
not obtain the full text for this entry. Nothing in the reasoning above depends on it, but a
governance reader should know it was not checked.

## Confidence reasoning

Source quality 0.85: Nature Neuroscience, an unusually clean design that models attributes explicitly
rather than fitting a parametric value regressor after the fact. Mapping fidelity 0.65 is held down by
commensurability -- the components tested are the easy kind. Transfer risk 0.40 covers both the
human-BOLD-to-substrate gap and the representation-to-consumption inference. The aggregate of 0.71
sits above the mapping figure because this entry earns its keep as design guidance for MECH-035's
falsifier rather than as evidence for or against the claim's truth.
