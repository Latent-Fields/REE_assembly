# Muscogiuri et al. (2021) -- PWS hyperphagia as clinical anchor for the saturated-override phenotype

## What the paper does

This is a clinical review in the *Journal of Endocrinological Investigation* covering
Prader-Willi syndrome (PWS) -- the genetic disorder that arises from loss of paternally
inherited gene expression on chromosome 15q11-q13 -- with a particular focus on the
mechanisms of hyperphagia and obesity. The authors lay out the canonical PWS clinical
trajectory: infantile failure to thrive and hypotonia, transition through childhood to
food-seeking and hyperphagia, and adult morbidity dominated by obesity and its
complications. They synthesise the mechanistic story (disrupted hypothalamic satiety
pathways, elevated ghrelin, blunted PYY, reduced energy expenditure, growth-hormone and
TSH deficiencies) and review nutritional and pharmacological management approaches.

## Findings relevant to SD-037

SD-037's secondary falsifiable predicts two diagnostic failure phenotypes: a *lost
override* phenotype (override_signal absent -> z_harm and drive_level compute normally
but fail to integrate into coordinated behaviour, mapping to narcolepsy/cataplexy) and a
*saturated override* phenotype (override_signal pinned high -> compulsive drive pursuit
despite negative outcomes, mapping to PWS-analog hyperphagia). The Muscogiuri review is
the clinical anchor for the second phenotype. The behavioural description it provides --
absent or markedly delayed post-prandial satiety, compulsive food-seeking persisting
across hours, persistence despite negative consequences (medical advice to restrict
intake, family environmental controls, even physical aversive consequences) -- maps
cleanly onto the SD-037 saturated-override prediction at the behavioural level.

## REE translation and mapping caveats

This is the entry where mapping caveats matter most, and I am setting evidence_direction
to MIXED rather than supports for that reason.

The behavioural phenotype matches. The mechanism does not match cleanly. PWS is a genetic
disorder of imprinted gene expression that disrupts multiple hypothalamic populations --
SNORD116 loss affects oxytocin neurons, MAGEL2 affects POMC and melanocortin signalling,
and the broader 15q11-q13 region affects circadian and metabolic gene expression. Orexin
biology is one of several hypothalamic systems affected (and not the most prominent
one); the dominant satiety-failure mechanism is melanocortin and oxytocin disruption.

So PWS supports SD-037 as a *phenotype-level falsifiable anchor* -- if SD-037 saturation
produces a state that does NOT resemble PWS hyperphagia, the architectural commitment
loses its clinical correspondence. But PWS does NOT support SD-037 as the mechanistic
explanation for PWS itself. The honest reading is that PWS is a multi-system genetic
disorder whose clinical signature happens to overlap with SD-037's saturated-override
prediction at the behavioural level.

This is a useful but secondary entry. Its role is to anchor the falsifiable prediction
in human clinical reality rather than to provide direct mechanistic support for the
override architecture.

## Confidence reasoning

I am setting confidence to 0.62 with evidence_direction MIXED. Source quality is
moderate (J Endocrinol Invest review, peer-reviewed, comprehensive but not by leading
PWS researchers). Mapping fidelity is moderate -- the behavioural phenotype maps
cleanly onto SD-037's saturated-override prediction, but the underlying mechanism is
upstream of and broader than the orexin-analog layer. Transfer risk is moderate-to-high
because PWS is a multi-system genetic disorder, and reading SD-037 mechanism into PWS
biology would be a mistake that this entry must not encourage.

The honest reading: PWS is the clinical anchor for the saturation prediction, not the
mechanistic confirmation. The falsifiable retains its empirical content (an SD-037
saturation experiment must produce PWS-analog behavioural signatures or the secondary
falsifiable fails); the entry provides the necessary reference standard for what those
signatures look like in humans.
