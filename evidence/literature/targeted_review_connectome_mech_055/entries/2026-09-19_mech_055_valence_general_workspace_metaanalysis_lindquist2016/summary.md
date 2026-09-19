# The brain basis of positive and negative affect: a neuroimaging meta-analysis

Lindquist, Satpute, Wager, Weber & Barrett (2016), *Cerebral Cortex* 26(5):1910-1922.
DOI [10.1093/cercor/bhv001](https://doi.org/10.1093/cercor/bhv001) - PMID 25631056 - PMC4830281.
First published online 28 January 2015. Retrieved via PubMed.

## What the paper does

397 fMRI and PET studies, 914 experimental contrasts, 6827 participants, and -- unusually and to its
credit -- three *pre-specified competing* hypotheses rather than one favoured one. The bipolarity
hypothesis: positive and negative affect supported by a brain system monotonically tracking a single
valence dimension. The bivalent hypothesis: positive and negative affect supported by *independent*
brain systems. The affective workspace hypothesis: both supported by a flexible set of
valence-general regions recruited differently per instance.

Little evidence for the first two. The findings supported the third: at the level of brain activity
measurable by fMRI, valence is flexibly implemented across instances by valence-general limbic and
paralimbic regions.

## How it bears on MECH-055

The bivalent hypothesis that this meta-analysis specifically tested and specifically failed to
support is the closest human-neuroimaging analogue of MECH-055's architectural premise -- that
affect is carried by channels which stay distinct rather than collapsing. This is therefore the
strongest human evidence against the claim in the corpus, and it is recorded as `weakens` on that
basis. MECH-055 cannot claim biological-plausibility support from the human record for its premise
that affect maintains dedicated separate channels.

But the more interesting contribution is a third option that MECH-055's confirming/falsifying
dichotomy does not currently contain. The claim frames the question as: distinct channels, or one
collapsed scalar wearing several labels? Lindquist et al. reject *both* -- the bipolarity hypothesis
fails too, so there is no fallback to a single well-behaved signed valence scalar either. What they
support is channels that are neither dedicated nor collapsed, but constructed per-instance from
shared valence-general machinery.

That third option deserves attention because it is the architecturally closest description of what
a shared RBF residue field, driven by common upstream state, would actually be expected to produce.
It is plausibly the true state of REE's own valence vector -- and it is exactly the hypothesis
MECH-055's test as worded is least equipped to detect, since a context-dependently-constructed
channel will show non-degenerate variance on the episodes where it happens to be recruited and
collapse on the ones where it is not. A distinctness test that samples both and averages gets an
answer that means nothing.

## Two ways the weakening must be kept narrow

I do not want to over-sell this entry, because the instrument is genuinely limited and the corpus
contains its own counterexample.

**Instrument limits.** Univariate fMRI and PET meta-analysis has poor sensitivity to population-level
codes. Multivariate pattern analyses routinely recover valence information from regions where
univariate contrasts show none, and the cellular-resolution work -- Namburi et al. 2015, in this
same pull -- demonstrates anatomically, physiologically and transcriptionally distinct valence
populations that no fMRI meta-analysis could ever resolve. The authors themselves frame the finding
as being about what is "measurable by fMRI". A null at this resolution is weak evidence of absence,
and the two entries in this pull are less contradictory than they first appear: separable cell
populations intermingled within valence-general regions would produce exactly this pattern at both
resolutions.

**Target mismatch.** This paper bears on whether REE's design is *brain-like*. It does not and
cannot bear on whether MECH-055's internal falsifiers fire, because those are a measurement of REE's
own channels against each other. No human neuroimaging result passes or fails that test. What
justifies recording it as `weakens` at all is that MECH-055 is a `mechanism_hypothesis` whose
warrant is partly biological homology -- and that warrant is what erodes here.

## Confidence

0.70. Source quality 0.90: large, well-powered, hypothesis-competitive, from groups with serious
methodological track records; much harder to dismiss than a single null. Mapping fidelity 0.55,
deliberately the lowest in this pull, for the target mismatch above. Transfer risk 0.55 -- high, and
driven by the instrument rather than by the species or the task. The net effect on MECH-055 should
be to lower confidence in the claim's biological warrant by a modest amount, and to add a third
hypothesis to its test design, rather than to count as a demonstration of collapse.
