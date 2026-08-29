# Eban-Rothschild et al. (2017) — sleep onset as arbitration, which cuts both ways for MECH-492

**Claim tested:** MECH-492 (MECH-286's sleep-permission threat conjunct is an uncalibrated, undeclared-source consumer of the shared `z_harm_a.norm()` expression)
**Direction:** mixed — deliberately

## What the paper did

This is a short invited review from the de Lecea group, and its contribution is a framing rather than a measurement. The question it poses is the one MECH-286 is trying to answer in code: how does an animal decide, each day, when to stop responding to the environment and go to sleep?

The answer it assembles from the rodent optogenetic and chemogenetic literature is that the two textbook processes — circadian rhythm and homeostatic sleep pressure — are not sufficient. *Motivational* processes modulate sleep and wake as well, and the review names predator evasion explicitly among them, alongside food seeking. It then walks through the neuronal populations known to control sleep/wake transitions and how motivational state reaches them.

## What this says about MECH-492 — and why I filed it as mixed

The supporting half is straightforward. It vindicates the *design* MECH-286 implements. Sleep onset really is a multi-input decision; threat really is one of the inputs; a gate that consults something other than sleep pressure alone is well-motivated rather than gratuitous. And if a threat input is going to sit in that decision, the review's framing implies it must carry actual threat information to earn its seat. That is MECH-492's premise.

The other half is why I would not file this as `supports`, and I think it is the more useful half for governance.

The review describes sleep onset as *arbitration* — inputs modulating a decision, competing and weighting. MECH-286 implements something structurally different: a hard three-way boolean AND, in which any single false conjunct vetoes sleep outright. Those are not the same topology, and the difference matters for exactly the outcome MECH-492 itself pre-registered as *also falsifying*. Under competitive arbitration, a weak or uninformative input is simply outvoted. It contributes nothing, and nothing breaks. MECH-492's own `what_would_answer` anticipates this: if `threat_ok` turns out near-constant but the gate's behaviour is unchanged because `override_ok` or `staleness_ok` is always the binding conjunct, the claim "should be narrowed rather than supported."

I am filing this entry partly to keep that branch visible. V3-EXQ-950 established the term measures at chance; it did not establish that the conjunction's *behaviour* changes as a result, and this review is the clearest literature statement of why those are separable questions.

## Limitations, stated plainly

It is a review. It cites others' measurements and makes none of its own, so it can ground an architectural premise and can never adjudicate a substrate defect. It predates V3-EXQ-917 and V3-EXQ-950 entirely and has nothing whatever to say about the 0.4 threshold.

I should be explicit that the arbitration-versus-conjunction reading is *my* inference from the review's language about modulation. The authors are not describing an implementation and make no claim about gate topology; they should not be cited as endorsing either. The evidence base is rodent-dominated, and the motivational processes the review actually spends its length on are chiefly feeding and mating drives — the predator-evasion case that MECH-286 concerns gets a mention rather than a section.

## Why confidence 0.55

The lowest of the three MECH-492 entries, and it should be. Source quality is high (0.80) — authoritative group, good venue — but mapping fidelity is only 0.52 because the review supports the design and the claim's falsifying branch simultaneously, so it does not discriminate between them. Transfer risk 0.45. Filing this as `supports` would have overstated what a framing review can do for a substrate-defect claim and would have buried the competitive-arbitration reading, which is the thing here most likely to change what governance does.
