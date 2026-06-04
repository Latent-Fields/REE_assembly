# Brzosko, Schultz & Paulsen 2015 -- A synaptic eligibility trace is the retroactive-credit mechanism

**Claim touched:** ARC-063 element (iv), per-action evidence-trace records and how they acquire credit. Cross-ref MECH-309.

## What the paper did
The authors showed, in mouse hippocampal slices, that dopamine can act *retroactively*: a synaptic event that would have produced timing-dependent depression is converted into potentiation when dopamine arrives afterwards, provided the conversion is within the window of a pre-established synaptic eligibility trace (NMDA-receptor and cAMP/PKA dependent). This is a direct cellular demonstration of how a reward signal that arrives *after* the activity that earned it can still strengthen the right synapse -- the "distal reward problem" of reinforcement learning.

## Why it matters for ARC-063
ARC-063's evidence-trace records are the learning substrate of the rule field: each rule-use leaves a record (which rules were active, which rollouts generated, the outcome, prediction error, harm, moral residue) that later refinement acts on. For that to be a learning loop rather than a logbook, a delayed outcome must be able to credit the rule that was active at use-time. Brzosko shows the biological form of exactly this retroactive credit -- an eligibility trace that holds an event "creditable" until the reinforcement signal lands. This grounds the *mechanism* by which ARC-063's evidence traces can carry credit back to a rule.

## The honest caveat
What is credited here is a single synapse over a ~1s window, not an abstract, distributed CandidateRule. ARC-063 lifts the eligibility-trace principle to the rule level; that lift is biologically motivated but is an REE extension, not something this slice experiment demonstrates. There is also a hippocampal-slice-to-PFC-rule_state transfer to discount. This is why the gap the pre-design audit flagged -- "no literature on credit to individual rules" -- is only *partially* closed: the general retroactive-credit mechanism is well grounded; rule-level specificity remains design hypothesis.

## Confidence
0.70 -- supports. Strong source, canonical mechanism, but the credited target (synapse) is not the rule, so it grounds the credit *mechanism* for ARC-063, not its *granularity*.