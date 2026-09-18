# Adams & Horton (2006) -- Monocular cells without ocular dominance columns

**Claim tested:** MECH-050 (functional locality supports attribution without requiring anatomical columns)
**Direction:** supports | **Confidence:** 0.72

## What the paper did

The two review entries in this pull argue from nulls. This one measures something, and it is the
reason it earned a place here despite a narrower reach.

Adams and Horton exploit a genuine natural experiment. In the squirrel monkey, ocular dominance
columns are expressed variably -- some animals have them, some do not -- so the comparison can be
made *within* a species, without confounding it against everything else that differs between a
macaque and a mouse. They recorded single cells in nine squirrel monkeys, then labelled ocular
dominance columns in layer 4C post mortem and ran cytochrome oxidase histochemistry in the same
animals. Outside layer 4C, cells tended to respond to either eye whether columns were present or
not. Then the finding that matters: in three animals that *lacked* ocular dominance columns
altogether, 20 percent of layer 4C cells were nonetheless monocular.

A second result comes along with it. In squirrel monkeys that did have columns, the columns failed
to reorganise the functional architecture into anything macaque-like -- cytochrome oxidase patches
and ocular dominance columns were spatially uncorrelated, and koniocellular input to the patches
was binocular. So in this species the presence of the geometry predicts rather little about the
functional organisation downstream of it.

## How this bears on MECH-050

MECH-050 says a selective response property can be carried by local circuitry -- modular recurrence,
sparse routing, bounded update -- without spatially bundling like-tuned cells into cylinders. This
paper is the closest thing in the literature to a direct test of the antecedent: remove the bundling,
look for the property, find it. Monocularity is present with the geometry absent. Whatever produces
eye-selective responses in layer 4C, it is not the columnar arrangement of eye-selective cells,
because the arrangement was not there.

That is a different and stronger kind of evidence than "no faculty correlates with columns". A null
correlation can always be blamed on the assay. An existence proof cannot.

## Limitations, and the one that matters most

The gap between what was measured and what MECH-050 asserts is large, and I do not want the
existence-proof framing to paper over it.

What was dissociated is one receptive-field property, from one column type, in one cortical layer,
of one primate species, with n=3 animals in the critical condition. MECH-050 generalises over
modular recurrent substructure, lateral spillover limits, routing sparsity and bounded update
regions, and it does so in service of error attribution and corrigibility. None of those words has
a referent in this experiment.

And here is the limitation I take most seriously. **No behavioural or performance measure was taken
at all.** The study establishes that monocular cells *occur* without columns. It says nothing about
whether any computation is performed as *well* without them. "Present without columns" is not
"unimpaired without columns", and the difference is precisely the thing MECH-050 stakes a claim on.
The 20 percent figure sharpens this rather than settling it: the paper does not establish that 20
percent is what column-bearing conspecifics show, so a quantitative degradation in the absence of
geometry remains entirely live. Mapped onto REE, that is the failure mode worth naming -- reducing
locality might preserve the *kind* of representation while quietly degrading its *degree*, which
would show up in attribution quality long before it showed up in whether a selective unit exists.

The second result cuts both ways too. That columns, when present in squirrel monkey, do not
macaque-ify the functional architecture weakens geometry as an explanatory variable -- good for
MECH-050. But it also means this species' cortex is doing something idiosyncratic with respect to
both conditions, which weakens any confident inference from it to a substrate as unlike it as REE.

## Confidence reasoning

Source quality 0.85: a well-controlled natural experiment with physiology and anatomy in the same
animals, in a solid specialist journal, discounted for thin n in the critical condition. Mapping
fidelity 0.65 is the limiting component and is doing most of the work in the aggregate -- one
property, one column type, no performance measure, against a claim that generalises over a whole
class of locality constraints. Transfer risk 0.35, a little above the reviews here, because the
inference runs from anaesthetised primate V1 single-unit physiology to an artificial substrate's
error-attribution behaviour and crosses more than one boundary on the way. Aggregate 0.72: the
best-evidenced entry in the pull and the most narrowly scoped, and those two facts are in tension
by design.
