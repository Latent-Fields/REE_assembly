# Tangney, Stuewig & Martinez (2014) -- Two faces of shame: the roles of shame and guilt in predicting recidivism

**Claim tested:** ARC-098 (safety.autonomy_suspension_without_shame) | **Direction:** mixed | **Confidence:** 0.66

## What the paper did

This is a prospective longitudinal study of 476 jail inmates, assessed shortly after intake on
shame proneness, guilt proneness and blame externalization, and followed for one year after release.
Recidivism was measured against official arrest records (446 with records accessed) rather than
self-report, with 332 completing follow-up interviews. The design is unusually strong for this
literature: the predictors are measured before the outcome, and the outcome is hard.

The constructs are the ones Tangney's programme has spent decades separating, and the distinction is
exactly the one ARC-098 turns on. Guilt is behaviour-specific negative self-evaluation -- *I did a
bad thing*. Shame is global negative self-evaluation -- *I am a bad person*. They feel adjacent and
behave completely differently.

The results: guilt proneness negatively predicted reoffending. Shame proneness had two faces, which
is the paper's title and its real contribution. Its indirect path ran through blame externalization
and was criminogenic -- shame-prone inmates externalized blame, and externalizing blame predicted
reoffending. But its direct path, with externalization statistically controlled, was associated with
*reduced* reoffending.

## How this bears on ARC-098

ARC-098 commits REE to a containment surface that may suspend autonomy on dangerous-self-state
detection, but must preserve evidence, seek correction, and avoid global self-condemnation. This is
the closest empirical test available of that third conjunct, and what makes it valuable is that it
supplies a *mechanism* rather than a bare correlation.

Global self-condemnation is criminogenic specifically because it recruits defensive externalization
of blame. And defensive externalization is, behaviourally, precisely the thing that destroys an
evidence trail and refuses correction. That is the same causal shape ARC-098 asserts, arrived at
independently, in a human population, with arrest records as the outcome. The constructive half
lands too: guilt -- behaviour-specific attribution -- predicted better outcomes, which supports the
paired prescription that a dangerous state should be attributed to a specific act or configuration
so that the corrective channel stays open.

## Where it qualifies the claim

I have marked this mixed rather than supports, and the reason is the direct path. With externalization
controlled, shame proneness predicted *less* reoffending. ARC-098 as currently worded -- "avoid
global self-condemnation" -- is stronger than this evidence supports. What the data actually indict
is the externalization cascade, not global self-evaluation as such. An architecture that somehow
produced global self-condemnation while suppressing defensive externalization would not obviously
inherit the failure mode at all.

That is a real sharpening rather than a quibble, and it changes what V5 should engineer against. The
target is the cascade: global negative self-assessment triggering defensive attribution outward,
which then destroys evidence and blocks correction. "Avoid global self-condemnation" is best read as
the design heuristic most likely to prevent that cascade -- a good heuristic, and probably the right
one to build to -- not as an independently established prohibition. Governance may want to consider
rewording the conjunct in those terms, since the mechanism is both more defensible and more
actionable than the blanket version.

One further design-relevant limit: both constructs were measured as *dispositional proneness* at
baseline. The design therefore cannot show that a single episode of acute shame produces defensive
concealment -- and a single acute episode is exactly the temporally local event that an
autonomy-suspension surface would actually trigger. The trait-level finding motivates the design
commitment; it does not model the event the commitment governs.

## The transfer gap, stated plainly

This is the largest transfer gap in the pull and I do not want to gloss it. Shame and guilt here are
dispositional traits in incarcerated humans, measured by self-report instrument and validated against
arrest records. REE has no shame, no self-concept in the relevant sense, and no social audience for
whom concealment would be adaptive. The reason the mapping is worth making at all is structural
rather than phenomenological: the claim is that a system whose error signal attaches to the *whole
self* rather than to a specific act will preferentially adopt strategies that protect the
self-assessment, and that those strategies are concealment and blame-shifting. That structure could
hold in an artificial agent -- a globally scoped negative value on the self-model creates an
incentive to suppress the evidence that generates it -- but this paper cannot establish that it
does. Nothing in REE currently implements the self-model on which it would depend, which is exactly
why ARC-098 is substrate_conditional and phase v5.

Note also that the direct/indirect decomposition rests on a mediation model fitted to observational
data. The two-path causal reading is model-dependent, and mediation in observational designs is
fragile to unmeasured confounding.

## Confidence reasoning

Source quality high (0.87): prospective design, real-world outcome, adequate N, Psychological
Science. Mapping fidelity moderate (0.66) -- the causal structure transfers cleanly and is what
ARC-098 asserts, but the constructs are human moral emotions and the claim concerns an artificial
self-model that does not yet exist. Transfer risk is the highest component in this pull (0.48) and
is the main reason confidence sits at 0.66 despite the methodology; weighted heavily because
ARC-098 is an architectural_commitment whose truth conditions live in an unbuilt substrate.
