# Learning the value of information in an uncertain world (Behrens et al., 2007)

**Claim under test:** MECH-003 -- *Precision must be tau-scoped with lossy projections.*
**Direction:** mixed

## What the paper did

Behrens, Woolrich, Walton and Rushworth asked a question that sounds simple and is not: how much
should any one past outcome influence your next decision? Their answer is that the weight should
track how *informative* that outcome is about the future, and that this in turn depends on how
volatile the environment is. In a stable world, one surprising outcome is noise and should barely
move you; in a changeable world, the same outcome may be the first sign that the rules have shifted
and should move you a great deal.

They show that human subjects estimate volatility close to optimally and adjust their learning rates
accordingly. In the scanner, the anterior cingulate signal at the moment each outcome is observed
reflects that outcome's salience for predicting future outcomes -- and, tellingly, between-subject
variation in this ACC signal predicts between-subject variation in learning rate.

## The property this entry is aimed at

MECH-003 requires cross-τ influence to pass through a projection operator with four named properties:
slow (many samples required), directional (usually short → long τ only), lossy (cannot preserve sharp
spikes), and context-gated (φ-dependent). Those four are not equally supported, and it seemed worth
finding a source that speaks precisely to one rather than gesturing at all of them.

This paper is the cleanest human demonstration that **slowness** is real and behaviourally
consequential. An estimate of how changeable the world is *cannot* be formed from a single
observation; it is in fact accumulated across many trials; and once accumulated it governs how much
each subsequent single outcome is permitted to move belief. That is a long-τ quantity behaving as a
genuinely separate register with its own time constant -- not as a smoothed copy of the fast one.
MECH-003's separation requirement, observed in humans.

## Why this is filed as mixed rather than supports

Because the same result cuts the other way on directionality, and I would rather record that than
launder it.

The control relationship Behrens et al. actually demonstrate runs **from the slow register to the
fast one**: the volatility estimate sets the learning rate applied to the next outcome. That is
long → short. MECH-003 says cross-τ projection is "Directional (usually short → long τ only)."

This is now the *second* independent source in this directory pointing the same way -- the Mathys
entry documents the identical reversal in the hierarchical Gaussian filter, where the higher level
sets the lower level's step size. Two highly-cited, methodologically unrelated sources agreeing
against a sub-clause is no longer a caveat to note in passing. My reading is that MECH-003's
directionality clause is probably **wrong as written**, and that the architecture doc should either
be corrected to bidirectional coupling (ascending prediction errors updating slow registers;
descending precision estimates setting fast learning rates) or should state explicitly why REE wants
to forbid the descending arrow that both the modelling and the empirical literature rely on. I have raised this
as an `evidence_discrepancy` governance flag against MECH-003; it is the single most actionable
output of this pull.

## Limitations

The hierarchy tested is two-level -- outcome rate, and the volatility of that rate -- whereas
MECH-003 posits four τ bands with a specific ordering constraint on their update rates. A two-level
result is *consistent* with that ordering but supplies no evidence for four bands. The ACC finding is
a BOLD correlate of a model-derived regressor rather than a directly measured control signal, and the
individual-differences result is correlational across subjects, so nothing here establishes that the
ACC signal *causes* the learning-rate adjustment. The operator's **lossiness** is untested: no
manipulation here asks whether a single sharp surprise can propagate to the slow estimate, which is
exactly what MECH-003 needs ruled out. And φ/context-gating is not addressed at all.

## Confidence

0.60 -- below what the source quality alone (0.85, *Nature Neuroscience*, foundational, much
replicated) would suggest. That gap is intentional. A high-quality paper that speaks precisely to one
of a claim's four sub-properties, is silent on two, and contradicts the fourth should not be recorded
as strong support for the claim as a whole.
