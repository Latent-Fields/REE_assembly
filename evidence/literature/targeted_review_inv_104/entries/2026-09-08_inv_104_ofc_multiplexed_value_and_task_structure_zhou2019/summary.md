# Multiplexed but dissociable value and task structure in rat OFC (Zhou et al., Current Biology 2019)

## What they found

The orbitofrontal cortex has been claimed by two literatures that do not obviously agree: one in
which it signals expected value, another in which it is a cognitive map of task space (Wilson,
Takahashi, Schoenbaum & Niv, Neuron 2014). Zhou and colleagues recorded OFC ensembles in rats
performing an odor sequence task and asked whether the two accounts are in competition. Their answer
is that they are not: the representations are multiplexed but dissociable.

The decomposition is what makes the result usable here. A single LDA component separated rewarded
from non-rewarded trials with perfect value selectivity. The remaining ~150 components retained
detailed sequence structure and carried essentially no value information. Under progressive
filtering, value information dominated only at the very lowest threshold and "declined precipitously
even at a threshold of 2-3%", whereas structure information held up across 10-40%. Crucially, the
retention was *selective*: cross-positional decoding was above chance in the sequence where sequence
position was task-critical, and not in the sequence where it was irrelevant. And on error trials --
and on the trials preceding them -- the ensembles miscoded which sequence the animal was in, in
register with the animal's behavioural mistake.

## What it evidences for INV-104

This is the biological anchor of the pull, and it speaks to three different parts of the claim.

**Against value-only compression.** INV-104 imports MECH-520 as a counter-constraint: preservation
by regulatory relevance alone over-compresses, and the predictive obligation across timescales is
what keeps the classes recoverable rather than encoded as a value projection. Zhou et al. are that
counter-constraint measured. If a biological compression of task experience were organised around
value, the value axis would not be one component out of ~150 with the rest carrying orthogonal
structure. A V3 z_world that collapses toward a value projection is not a neutral engineering
simplification; it is a departure from the biological reference in the specific direction MECH-520
warns about.

**Conditional, not blanket, preservation.** The claim can be misread as "preserve everything in five
categories, everywhere". The selective-retention finding is a corrective: position was represented
where position mattered and not where it did not. That is closer to INV-104's actual per-class,
per-site structure -- and to its own warning against over-specification, the mature ontology
smuggled into targets -- than a uniform reading would be.

**Class 2, in its hardest form.** INV-104's class 2 includes "internal-state consequence invisible in
the scene". The error-trial analysis is exactly that: the ensemble encoded the animal's *belief*
about which sequence it was in, a variable with no external correlate at the moment of coding, and
encoded it wrongly precisely when the animal was about to act wrongly. A representation scored only
against ground-truth scene labels would call this an error. Scored against what the organism was
about to do, it is the representation working correctly and the belief being wrong. That distinction
is one REE will have to make if class 2 ever gets a falsifier through the
`e2_action_contrastive_enabled` path.

## What this cannot do

It cannot supply the normative half. INV-104 does not only say that organism-relevant distinctions
*are* preserved in adequate systems; it says that destroying one *is a developmental regression* --
that access matters. Zhou et al. show the pattern without testing the counterfactual: there is no
ablation, no capacity-matched adapter, no encoder trained without structure to compare against. F2
(no-cost) is the falsifier route that targets the normative half, and nothing in this paper is
admissible against it.

I would also resist the transfer more generally than usual. This is rat lateral OFC in a
well-learned, discrete, experimenter-designed task, where "behaviourally relevant" is relevant by
construction rather than discovered by the animal. The quantitative thresholds (value gone by 2-3%,
structure surviving to 40%) are properties of the LDA-plus-filtering analysis and should not travel
to REE as calibrated numbers. And there is a standing methodological hazard in this class of
argument: "the brain does it this way, therefore the architecture must" is precisely the inference
INV-104's falsifier was written to avoid needing.

## Confidence

0.71. Good lab, good journal, ensemble-level analysis, corroborated by the same group's companion
hippocampus/OFC paper (PMID 31588004). Transfer risk is the highest in this pull at 0.45, and it is
the component doing the most work in holding the number down.
