# Empathy for pain involves the affective but not sensory components of pain (Singer et al. 2004)

**Claim:** MECH-164 (love as agent-indexed terrain inference with self-like gradient weighting)
**Direction:** supports · **Confidence:** 0.74 · **Class:** fmri_connectivity

## What the paper did

Singer and colleagues scanned people in two conditions: receiving a painful stimulus themselves,
and receiving a *cue* that their romantic partner -- present in the same room -- was getting a
similar painful stimulus. The comparison isolates the neural signature of empathising with
another's pain from the neural signature of feeling pain oneself. The result is clean and has
become one of the most-cited findings in social neuroscience. A subset of the "pain matrix" --
bilateral anterior insula (AI) and rostral anterior cingulate cortex (ACC) -- was active in *both*
conditions: when I hurt and when my loved one hurts. The sensory-discriminative regions (primary
and secondary somatosensory cortex, posterior insula, caudal ACC) were active *only* for
first-person pain. And the strength of AI/ACC activation in the empathy condition correlated with
the subject's questionnaire empathy score. Empathy, on this picture, is the re-use of the
*affective* representation of pain -- its felt badness -- without the sensory representation of
*where and how* it hurts.

## Why it matters for MECH-164

MECH-164's load-bearing architectural claim is that another agent's terrain (their harm and goal
gradients) is weighted into E3 with the *same motivational force* as one's own -- "not a scaled copy
or a discounted proxy" -- so that care falls out of ordinary trajectory selection with no separate
ethics module (consistent with INV-001). Singer et al. are the human-neuroscience grounding for the
negative-side half of that terrain. The brain does not appear to build a dedicated "other's pain"
valuation circuit; it routes the other's harm through the *self's own* affective valuation code (AI,
rostral ACC). That is structural symmetry in the weighting of harm gradients -- exactly what
MECH-164 asserts and what its precursor INV-005 (harm to others via mirror modelling) already names.
It is also a direct empirical answer to a sceptic who asks why REE doesn't need a bespoke ethics
module: in biology, the substrate for caring about another's harm *is* the substrate for one's own.

There is a second, subtler payoff. The finding aligns with the project's existing empathy design
(`docs/thoughts/2026-02-09_empathy.md`), which proposes a *gated projection* of another agent's
state into a shadow copy of self-streams rather than a wholesale merge. Singer et al. show the
biology does something equally selective: it shares the affective layer and withholds the sensory
layer. That selectivity is the design hint -- self-like weighting should operate on the *valuation*
of the other's terrain, not on a full duplication of their sensorimotor state.

## Limitations and caveats

Three boundaries keep this at 0.74. First, it grounds shared representation of *harm*, and says
nothing about the *goal*-gradient half of MECH-164's terrain -- the positive side (supporting
another's goal-finding) needs separate grounding, which is why the goal-inference papers
(Woodward, Gergely & Csibra, Baker) carry the other half of this pull. Second, co-activation is not
weighting: that AI/ACC fires for both self and other shows a *common representation*, but it does
not measure whether the other's harm signal carries *equal motivational force* in action selection
-- the step from shared activation to self-like weighting in E3 is a mapping assumption I am making,
not a quantity the paper reports. Third, the paradigm uses a loved one, so it speaks to the
high-coupling end of empathy and not to RHM-5's central open question: how coupling is *calibrated*
across strangers, and how it avoids both collapse and callousness. Indeed the sensory/affective
dissociation is itself a warning for the substrate -- a REE design that shadow-copies the *entire*
self-stream into the other-index would over-share and lose the self-other distinction that RHM-5
needs. Used carefully, though, this is strong, direct, human evidence for MECH-164's core
commitment, which is why it earns "supports."

According to PubMed, the citation is Singer, T., Seymour, B., O'Doherty, J., Kaube, H., Dolan, R. J.,
& Frith, C. D. (2004), *Science* 303(5661):1157-1162,
[DOI 10.1126/science.1093535](https://doi.org/10.1126/science.1093535).
