# Tolman & Honzik (1930) -- latent learning as the canonical competence/expression dissociation

**Claim tested:** ARC-131 (installability is a competence dissociable from isolated component-level validation)
**Direction:** supports | **Confidence:** 0.60

## What the paper did

Three groups of rats ran the same complex maze under different reward regimes. One group was
rewarded with food on every successful completion. A second was never rewarded. A third was run
unrewarded for the first ten days and then rewarded from day eleven onwards. Through the first ten
days the third group's error curve tracked the never-rewarded controls -- by the only measure
anyone was taking, they were not learning. On introducing reward, their performance collapsed onto
(and by some measures below) the always-rewarded group's within one to two trials. Tolman and
Honzik's reading, which became the standard one, is that the maze representation had been acquired
throughout the unrewarded period and was simply not being expressed in behaviour; what changed on
day eleven was not knowledge but the conditions under which knowledge got used.

The finding founded the learning-performance distinction, which is why it is worth pulling here
rather than something more recent. It is not a curiosity in the animal-learning literature; it is
the case that literature settled on to mark the difference between what an organism has and what an
organism does.

## Why it bears on ARC-131

ARC-131's assertion is that a mechanism can pass component-level validation and still never appear
in the composed organism, because the rest of the organism sets the conditions under which the
mechanism would express. The obvious objection to that claim -- and the one worth taking seriously,
since ARC-131 is otherwise dangerously convenient as an explanation for any null result -- is that
it might be unfalsifiable special pleading: *the mechanism is there, honestly, you just cannot see
it*. What Tolman and Honzik establish is that this shape of explanation is sometimes simply true,
and that a discipline can tell the difference. The rats' competence was not asserted from a null; it
was demonstrated by changing one composition-level variable and watching the competence appear
whole, faster than any account in which it was being learned at that moment could allow.

That is the real transferable lesson, and it is methodological rather than mechanistic. The
dissociation was established by a manipulation that changed the composed system's operating
conditions while holding the component constant. An REE installability check should have the same
shape: not "did the mechanism fire", which returns a null under both hypotheses, but "does the
mechanism's expression change when we change the composition-level condition we think is gating it".
The audit that cleared ARC-131 against MECH-459 (`evidence/planning/arc131_mech459_duplication_audit_20260825.md`,
section 2) identified this paper as the discipline-standard external analog and recommended exactly
this pull; this entry discharges that recommendation.

## Limitations and caveats

Three, and none of them are small. First, the direction of the dissociation is not the same as
REE's. Tolman's animals acquired the competence *inside* the composed organism and failed to express
it; ARC-131's motivating REE cases -- the coalition controller that exists and is typed but is never
endogenously invoked, the selector rendered silently equivalent to its own OFF arm by a permissive
fallback envelope -- concern a mechanism validated in isolation and then failing to be recruited on
composition. The shared structure is competence-without-expression. The acquisition path is
different, and an REE probe modelled too literally on the maze would be testing the wrong thing.

Second, the gating variable here is drive. ARC-131 enumerates seven channels by which composition
alters a mechanism's operating conditions, and motivational state is at best one of them. This paper
evidences the *existence* of the dissociation, not its breadth, and citing it for the latter would be
over-reach.

Third, a provenance point that belongs on the record rather than buried: this session verified the
citation and the study design through the bibliographic record and standard secondary accounts, not
by reading the 1930 primary text, which is not available online in full. The design as described
here is consistent across every secondary source consulted, and the construct has been replicated in
many later forms, so I do not think the reading is wrong -- but the confidence is set at 0.60 partly
for that reason, and a future reader who needs the original numbers should go to the primary.

## Confidence reasoning

Source quality 0.70: canonical and heavily replicated as a construct, discounted for 1930
methodology (no effect sizes, no variance reporting in the record consulted) and for the secondary
verification above. Mapping fidelity 0.70: the structural correspondence to ARC-131 is close, capped
below 0.8 by the acquisition-path mismatch. Transfer risk 0.50: rodent behaviour to a designed
computational architecture is an analogy about the shape of the failure, not a mechanistic transfer.
Aggregate 0.60, weighted toward mapping fidelity as the skill directs for an architectural claim --
this entry is doing conceptual work for ARC-131, not supplying a measurement.
