# Weisman, Quintner & Masharawi (2019) -- the layer this pull could have conflated

## What the paper did

This is a short conceptual commentary in The Journal of Pain arguing that the term "congenital
insensitivity to pain" is a misnomer. The authors' case is epistemological rather than empirical:
the label "is epistemologically incorrect and is the product of historical circumstances," and it
"conflates pain and nociception and, thus, prevents researchers and caregivers from grasping the
full dimensions of these conditions." They propose "congenital nociceptor deficiency" instead, on
the grounds that what these patients demonstrably lack is nociceptive transduction, not necessarily
the capacity for pain as an experience. They note the conditions are valuable precisely because they
"shed light on the poorly understood relationship concerning nociception and the experience of pain."

## Key findings relevant to the claim

I included this entry as the disconfirming source LIT-0721 requires, and it turns out to earn the
role rather than fill it. It attacks the interpretive basis of the strongest supporting entry in
this pull.

The Cox et al. (2006) argument, as I made it, runs: remove the harm signal, hold everything else
fixed, watch protective behaviour fail catastrophically, conclude the harm signal is load-bearing.
Weisman and colleagues would say that what Cox removed was the *nociceptor*, and that inferring
anything about pain -- about harm as something that matters -- from a transduction deficit is
exactly the conflation they are objecting to. If they are right, Cox et al. establish the weaker of
the two propositions INV-095 needs: that afferent harm transduction is necessary for protective
behaviour. That is worth knowing, but it is not yet the claim.

And INV-095's claim really does live at the other layer. The axiom's language is "harm matters
because existence matters. If existence had no value, harm signals would be noise rather than
information." Mattering, not transduction. A nociceptor-deficient human tells us about the input
channel; the claim is about what the architecture does with the input.

## How this translates to REE

The consequence is a concrete warning about which REE component to perturb. `z_harm_a`, `z_harm_s`
and `ResidueField` output are the transduction-analogue -- they are where harm gets represented. The
valuation layer is whatever weights that representation in E3's harm-weighted trajectory scoring,
via the amygdala BLA/CeA analogue (SD-035) and dACC (MECH-258). Weisman et al.'s distinction says
these can come apart, and Berthier et al. (1988) is the clinical demonstration that they do.

So a noise substitution applied only at the `z_harm` layer could leave the valuation structure
intact and still perturb the wrong thing -- and if the architecture is robust enough to reconstruct
usable hazard information downstream, the experiment would return a behavioural null that reads as
"the harm signal is decorative" when the true situation is "the perturbation missed the layer that
matters." Combined with Lipton et al.'s proof of robustness to classification errors in a danger
model, this is the second independent reason in this pull to distrust a bare null from the
V3-EXQ-533 successor. The design should perturb both layers separately and report them separately.

The distinction also cuts the other way, which is why I have recorded this as `mixed` rather than
`weakens`. In separating transduction from valuation, the paper strengthens the Berthier line of
evidence at the same time as it weakens the Cox line -- pain asymbolia is precisely a valuation
deficit with transduction intact, which is the layer INV-095 cares about. The net effect on the
claim is not straightforwardly negative; it is a redistribution of where the support actually comes
from.

## Limitations and confidence reasoning

The main limitation is genre. This is a four-page commentary advancing a terminological reform, not
a study. Its central assertion -- that these patients retain pain experience despite deficient
nociceptors -- is an interpretive position in a live dispute, not a measurement, and the authors
offer no data that could adjudicate the layer question they are raising. It constrains how
confidently Cox (2006) transfers to INV-095; it does not settle anything.

I want to be careful not to overstate it in the other direction either. Nothing here is evidence
that REE's harm signal is decorative. It is evidence that one of my supporting inferences was
resting on a conflation, and that the experiment which would settle the claim needs to be more
careful about layers than I would have been without having read it.

Confidence 0.58. Source quality 0.60 is capped by genre. Mapping fidelity 0.72 is higher than the
genre would suggest because the distinction it draws is the exact one the claim's testable leg turns
on. Transfer risk 0.45 is the highest in this pull, since an argument about human clinical
nosology transfers to an artificial architecture only by analogy.
