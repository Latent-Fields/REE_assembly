# Wallis, Anderson & Miller 2001 -- Abstract rules are explicitly represented in PFC

**Claim touched:** ARC-063 element (i), distributed CandidateRule field representation -- the foundational fact that a rule is a represented object. Cross-ref MECH-309.

## What the paper did
Recording single neurons in macaque PFC while monkeys applied one of two abstract same/different rules to pictures -- including pictures never seen before -- Wallis and colleagues found that the most prevalent neural activity coded *which abstract rule was currently in effect*. Because the rules transferred to novel stimuli, the animals had learned general principles, not stimulus-specific associations, and the PFC explicitly represented those principles.

## Why it matters for ARC-063
MECH-309's worry is that, without a rule-creator, gradient descent collapses to one smooth policy and there is no *rule* to speak of. Wallis is the canonical refutation that the brain can carry rules as explicit, abstract, generalising representations -- the substrate ARC-063's CandidateRule field is built on. Before designing how a field of candidate rules is stored, gated, and credited, this establishes that "a represented rule" is a real neural object, not a modelling fiction.

## The honest caveat
The experiment had exactly two rules in effect and reported coding at the single-neuron level. It grounds that rules are *represented*; it does not show a *distributed field* holding many candidate rules at once, nor the per-rule attributes ARC-063 needs (tolerance, context-tags, evidence traces). Those are covered, respectively, by the mixed-selectivity subspace work (Weber 2023, this review) and remain partly design hypothesis. So this is the existence proof, not the field architecture.

## Confidence
0.74 -- supports. A landmark result with high source quality; the discount reflects the gap between "rules are coded by PFC neurons" and "a distributed CandidateRule field with graded availability and per-rule attributes."