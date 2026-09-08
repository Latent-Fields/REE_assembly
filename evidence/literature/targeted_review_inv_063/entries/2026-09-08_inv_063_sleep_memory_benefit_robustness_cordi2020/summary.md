# How robust are sleep-mediated memory benefits? (Cordi & Rasch, 2020)

## Why this entry exists

Every other paper in this pull is about whether INV-063's mechanism is plausible. This one is about
whether the *measuring instrument* works, and I think it is the most consequential entry of the five
-- which is an uncomfortable thing to record against a claim I find genuinely interesting.

## What the review says

Cordi and Rasch survey the last several years of the sleep-and-memory literature and catalogue what
has happened when its central findings were re-tested: replication failures, null findings,
meta-analyses returning smaller effects than the original reports, and boundary-condition studies
showing effects that hold only under particular task and design constraints. Their summary judgement
is that the effects of sleep on declarative memory are smaller, more task-dependent, less
slow-wave-sleep-related, less robust and less long-lasting than the field had assumed.

The provenance matters. This is not a hostile external critique. Rasch is one of the significant
contributors to the sleep-consolidation research programme, and the review is an insider's accounting
of where the programme's evidence base is weaker than its textbook presentation. That makes it costly
testimony, and I weight it accordingly.

## What it does to INV-063

Two distinct things, and it is worth keeping them apart.

Substantively, it lowers the prior. INV-063 asserts a starvation gradient in offline function. If the
base phenomenon -- sleep produces a measurable functional benefit -- is itself unstable at a single
contrast in its native domain, the existence of a clean gradient across four levels of it is a
stronger claim than it first appears, not a weaker one.

Methodologically, and this is the part I would actually act on, it is a direct warning about our
design's power budget. C1 asks for a monotone ordering of the offline benefit across four intake
arms at three seeds. C2 -- the leg that carries the claim's distinctive content -- asks whether the
drop between the two lowest arms exceeds the drop between the two highest by a margin scaled to the
cross-seed SD. That is a *second difference* on a base quantity this review says is noisy and
condition-dependent. Differencing amplifies noise. If the biology is any guide to the substrate's
signal-to-noise here, C2 at three seeds is very unlikely to return an interpretable answer either
way, and a null would then be uninformative rather than falsifying -- which defeats the entire
purpose of pre-registering F1 as a genuine falsification rather than a shrug.

There is a second, sharper point buried in the review's list. It reports that the observed effects
are *less SWS-related* than assumed. INV-063's architecture routes intake to function through the
slow-wave and REM offline budget, and our P2 gate pins exactly that budget on the assumption it is
the operative channel. If, in biology, the benefit is not principally carried by slow-wave sleep,
then pinning SWS writes and REM rollouts may be controlling something that is not the mediator. P2
would still be a necessary control -- it excludes the consumer's arithmetic, which is its stated job
-- but it would be a narrower one than the design's confidence in it implies.

## What I am not claiming

The review's subject is human declarative memory measured behaviourally, and part of its diagnosis is
sociological: small samples, publication bias, analytic flexibility. A simulated substrate is immune
to several of these by construction. We can raise seed counts at will, our analysis is pre-registered
and genuinely so, and there is no file drawer. So the honest transfer is not "the effect probably
does not exist in REE". It is narrower and, I think, more useful: the phenomenon this claim is
modelled on is weak and unstable in its own domain, which lowers the prior on a robust analogue and
raises the evidential bar the run has to clear. Reading it as a prediction about our substrate would
be over-claiming in the opposite direction from the usual error, and I would rather not trade one
over-read for another.

## Confidence

0.7, the highest in the pull. Source quality 0.8, mapping fidelity 0.7 -- the highest here, because
the target is the claim's dependent variable itself, and a DV transfers across domains much more
cleanly than a mechanism does. Transfer risk 0.35, the lowest of the five but not negligible, for the
reasons in the previous section. If this pull changes one thing about how INV-063 is run, it should
be the seed count on the C2 leg.

According to PubMed: [DOI 10.1016/j.conb.2020.06.002](https://doi.org/10.1016/j.conb.2020.06.002),
PMID 32711356.
