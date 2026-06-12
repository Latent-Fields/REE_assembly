# The self-other coupling upper bound — moderate vs high similarity (Salles, Fadel & Mograbi 2024)

**Claims grounded:** INV-082 (loveability as safe-base structural prerequisite — the *bound*)
**Direction:** supports · **Confidence:** 0.60

## What the paper did

Eighty-seven adults watched a video of an athlete in pain, each preceded by a short clip describing the athlete's trajectory that primed low, moderate, or high perceived similarity to the participant. Vicarious emotion was measured with emotional self-reports, facial action coding, gaze behaviour, and pupil diameter. The result is a non-monotone, inverted-U relationship between similarity and the *quality* of the empathic response. Moderate- and high-similarity groups both showed greater empathic concern (more sadness) than the low-similarity group. But the moderate-similarity group additionally showed *less* personal distress — reduced disgust and avoidance — whereas the high-similarity group displayed just as much disgust (the personal-distress / avoidance signature) as the low-similarity group. In short: empathic concern without personal distress is optimised at intermediate, not maximal, self-other overlap; pushing similarity to the maximum re-introduces personal distress.

## Why it matters for the claim

This is the specific paper the LOVE-7 node names under L3, and it does a job none of the other three entries can. INV-082 does not merely assert that care must be internalised — it asserts that the coupling is **bounded**. The claim text reads "care internalised as personally-applicable **and stable** (Salles 2024, bounded)," and the plan's DEV-NEED-017 readout makes this concrete: `loveability_coupling_gain` is held to the interval [0.1, 0.7], with the upper limit explicitly credited to this study, on the reasoning that "above ~0.7 coupling inverts into personal distress." That is the inverted-U Salles et al. measured. The architectural significance is large: it is the standing guard against a naïve LOVE-2 design in which more loveability/coupling is simply better. Over-coupling is itself a failure mode — the adult analogue of the MECH-158 collapse, except instead of "love exists but not for me," the failure is "the other's pain becomes my own distress and I withdraw." Salles supplies the empirical shape that turns the upper bound from a free parameter into a load-bearing constraint.

## Limitations and caveats

I have kept this at 0.60 deliberately, because the mapping has two real seams. First, the coupling Salles measures is *between two people* — an observer and an injured target — whereas INV-082's `loveability_coupling_gain` is a *within-agent* coupling of received care into the self-valence model. The inverted-U is the right qualitative shape, but the transfer across that reframing is an analogy, not an identity. Second — and this matters for governance honesty — the study supports only the *qualitative existence* of an upper bound. It is a single n=87 lab study with personal distress operationalised through indirect behavioural proxies (facial disgust, avoidance, gaze, pupil) rather than a validated distress instrument. It does **not** validate the specific numeric interval [0.1, 0.7]; that interval remains a design choice informed by the inversion, not a measured threshold. Any governance reading of this entry should resist quoting the paper as if it located the 0.7 ceiling — it located the *direction*, not the *number*.

## Confidence reasoning

0.60. Moderate source quality (single study, indirect distress measures), moderate mapping fidelity (correct shape, interpersonal-to-intra-agent reframing, no numeric pin), substantial transfer risk. The entry earns its place because it is the only one of the four that grounds the *bound* — the non-obvious half of INV-082 that distinguishes it from a generic "loveability is good" claim — and because it is the named L3 anchor the node was written around. It should be read as qualitative support for "an upper bound exists and over-coupling inverts into distress," with the numeric interval flagged as still a modelling decision.

*According to PubMed* — Salles, Fadel & Mograbi (2024), PsyCh Journal, [DOI: 10.1002/pchj.720](https://doi.org/10.1002/pchj.720) (PMID 38105597).
