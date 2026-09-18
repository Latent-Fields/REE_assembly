# The root of all value: a neural common currency for choice (Levy & Glimcher, 2012)

**Claim tested:** MECH-035 -- VALENCE is vector-valued and ranked without scalar collapse.
**Direction:** weakens | **Confidence:** 0.70

## What the paper does

Levy and Glimcher ask the question that makes the common-currency hypothesis testable rather than
merely appealing: when a person chooses between goods from *different categories* -- money against
food, food against a consumer item -- where in the brain do the two become comparable? They synthesise
thirteen human fMRI studies built around exactly that cross-category structure and report convergence
on a subregion of ventromedial prefrontal and orbitofrontal cortex whose BOLD signal tracks subjective
value irrespective of which category the good came from. The economic reading is that this region
holds the exchange rate: incommensurable goods are converted into one quantity, and choice proceeds by
comparing that quantity.

## What it says about MECH-035

This is the paper MECH-035 is written against, and it is filed here for that reason. I would rather
this directory carry the strongest version of the opposing case than an assembly of agreeable
citations; a claim registered as `candidate` with zero literature evidence is not helped by being
surrounded only by its friends.

If the brain's answer to comparing incommensurables is to collapse them into a common scale, then
REE's architecture -- VALENCE held as a vector of predicted stream deltas, E3 (ARC-003) ranking
candidates constraint-first by dominance or lexicographic order -- is taking a route that biology
apparently declined. That is not fatal; REE is not obliged to be biomimetic, and MECH-035 is a claim
about a running substrate, not about primates. But it does mean the burden sits on MECH-035's side,
and the claim's first experiment must be powered to detect the common-currency alternative rather than
merely to confirm its own.

## Limitations and what could go wrong

Two boundaries matter, and together they are why this is filed at 0.70 rather than as a decisive
refutation.

The first is scope, and it is the more important. Every comparison in this synthesis is between
*appetitive* goods. Money, food, consumer items. Nothing here tests whether a harm dimension, a
constraint, or another agent's welfare enters the same scale -- and MECH-035's substantive assertion
is precisely about those. A common currency for money-versus-chocolate is entirely compatible with a
lexicographic barrier around harm; indeed most people's introspective report is that both are true at
once. So this paper weakens the universal form of the claim ("no scalar collapse anywhere") much more
than the form REE actually needs.

The second is resolution. Convergent coordinates across studies establish a common *region* far more
securely than a common *code*. Several stream-specific populations, interdigitated at a scale fMRI
cannot resolve, would produce the same blob. Hayden and Niv's entry in this directory makes the
sharper version of this objection, and a governance reading of MECH-035 should hold the two papers
against each other rather than adopting either.

A methodological note for whoever runs the first MECH-035 experiment: this is a review by the
position's leading proponents, not a neutral survey, and should be read as the best statement of a
hypothesis rather than as a field verdict.

## Confidence reasoning

Source quality 0.80 -- Current Opinion in Neurobiology, canonical, heavily cited, authored by people
who built the framework. Mapping fidelity 0.62 is held down by the appetitive-only scope and by the
coordinate-versus-code gap; both mean the paper bears less directly on REE's architecture than its
headline suggests. Transfer risk 0.45 covers the human-BOLD-to-artificial-substrate analogy and the
over-reading hazard. The aggregate of 0.70 records this as serious counter-evidence that does not
settle the question, which I think is the accurate state of the field in 2026.
