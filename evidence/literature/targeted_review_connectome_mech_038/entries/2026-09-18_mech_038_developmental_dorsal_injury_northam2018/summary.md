# Northam et al. (2018) -- Developmental conduction aphasia after neonatal stroke

**Claim tested:** MECH-038 (arcuate-like sequence-to-motor channel nudges language emergence)
**Direction:** supports | **Confidence:** 0.76

## What the paper did

Thirty term-born individuals who had a confirmed neonatal stroke -- twenty-one of them left-sided -- were studied at
ages 7 to 18, alongside forty matched controls. Structural MRI and diffusion tractography classified who had dorsal
and/or ventral language stream injury; fMRI established language lateralisation; standardised batteries measured
repetition and broader language.

Those with left dorsal stream injury showed a selective speech repetition impairment: nonwords at p = 0.021, sentences
at p < 0.0001. Other language deficits were present in the repetition-impaired group but the authors describe them as
more subtle and variable. The authors also found that where language had reorganised to the right hemisphere, this was
protective against the repetition deficit.

The framing the title gives it is the right one: this is conduction aphasia, but developmental -- the disconnection was
there before there was anything to disconnect.

## How this bears on MECH-038

Of the entries in this directory, this is the one that addresses what MECH-038 actually asserts. The other lesion work
tells us what the dorsal channel does in an adult who already has language. MECH-038 is a claim about *emergence*: that
the channel nudges a system toward symbolic use without being the thing that makes symbolic use possible. Its confirming
criterion says so explicitly -- ON must beat LESION on rate and latency, *and* LESION must still show some emergence,
because emergence in ON with zero in LESION would make the channel a required module and weaken the claim as written.

Northam et al. is the human developmental instance of that exact pattern. Language was acquired by people whose dorsal
channel was damaged before any language existed. What did not develop normally was the sequence-to-motor function in
particular. Language did not fail to emerge; it emerged degraded along the axis the channel serves. If the REE
experiment is run and the LESION arm coordinates worse, later, and less consistently but still coordinates, that is
what this paper would have led one to expect.

It is also, and I want to be direct about this, the counterweight to the Schomers entry in this directory. That model
showed the target capacity failing to appear at all without the jumping links -- the module pattern, read strictly. This
paper shows the nudge pattern in humans over eighteen years. The two are not straightforwardly reconcilable, and the
honest position before running the REE experiment is that the nudge-versus-module question is genuinely open, with the
in-silico prior pointing one way and the human developmental prior pointing the other.

## Limitations and where the mapping strains

The caveat that matters most cuts against the claim rather than for it. The LESION condition here is not "no fast
route". It is "no fast route, plus years of compensatory reorganisation" -- and the paper's own finding that
right-hemisphere reorganisation protects repetition says exactly that. A REE LESION arm that severs the routing and
offers nothing in its place is a *stricter* lesion than the one studied here. So if that arm shows little or no
emergence, this paper does not license concluding the channel is a required module; it licenses asking whether the REE
lesion was harsher than the human one.

Second, the scaffold. Human language acquisition proceeds inside caregiver input, shared attention, and cultural
transmission -- a vast amount of structure supplied from outside. A two-agent CausalGridWorld supplies essentially none
of that. "Language emerged despite the lesion" in a child leans on that scaffold; it is not evidence that symbolic
coordination will emerge despite an analogous lesion in agents that have to find the pressure themselves. This is, in
fact, the same concern MECH-038's non-degeneracy precondition already encodes: if no emergence occurs in *either* arm,
the result is uninterpretable, because there was no pressure, not because there was no nudge.

Third, the usual lesion caveats: neonatal stroke damages grey matter as well as tracts, lesion extent varies across the
thirty cases, the design is cross-sectional and observational, and stream-injury classification comes from tractography
rather than from a controlled disconnection.

And a correction to any over-reading of "selective": deficits beyond repetition were present. Subtle and variable, but
present. "Language emerged intact apart from repetition" is a sentence this paper does not support.

## Confidence reasoning

Mapping fidelity 0.78, the highest in this directory, because the paper's subject is emergence-under-lesion rather than
function-under-lesion. Transfer risk 0.40, also the highest here, and for the same reason: developmental plasticity and
the cultural scaffold of acquisition have no analog in ree_core, so the *direction* transfers more safely than the
*magnitude*. Source quality 0.80 -- Annals of Neurology, a good cohort for neonatal stroke, but observational.
Aggregate 0.76.
