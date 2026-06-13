# The behavioural final common path (McFarland & Sibly 1975)

**Claim(s):** MECH-394 (multidrive arbitration policy)
**Direction:** supports · **Confidence:** 0.66
**Source:** McFarland & Sibly (1975), *Philosophical Transactions of the Royal Society of London B* 270(907):265-293. [DOI: 10.1098/rstb.1975.0009](https://doi.org/10.1098/rstb.1975.0009).

## What the paper did

This is the classic ethological statement of the problem MECH-394 exists to solve. McFarland and Sibly start from a deceptively simple observation: an animal cannot do more than one thing at a time. Eating, drinking, fleeing, grooming -- these are mutually exclusive at the level of overt behaviour. From that constraint they build a formal apparatus. Any model of the reversible motivational processes governing behaviour, they argue, can be represented as isoclines in a multidimensional "causal-factor space," where the causal factors are the internal and external variables (hunger signals, water deficit, cue presence) driving each behaviour. The isoclines join all the points in that space that confer a given "degree of competitiveness" on a particular **candidate** for behavioural expression. Competition between candidates is then the inevitable consequence of the one-thing-at-a-time constraint, and it is resolved in what they name the **behavioural final common path** -- the single channel through which the winning candidate reaches expression. They make it concrete by measuring hunger and thirst in doves and showing the competition can be quantified in this space.

## Key findings relevant to the claim

What makes this paper worth grounding MECH-394 against is not a result but a *framework* -- and a strikingly REE-shaped one. The objects are drives-as-causal-factors; the behavioural options are "candidates"; and arbitration is the competition among candidates for a single output, scored by each candidate's degree of competitiveness. That is, almost word for word, how REE's E3 already works: candidates carry per-candidate score contributions (the score_bias terms of MECH-295), and selection is a competition among them. MECH-394 -- a soft-competitive orchestration over simultaneously-active drives producing one behaviour -- is recognisably the modern descendant of the behavioural final common path. It is fair to say McFarland and Sibly supply the conceptual ancestor of REE's arbitration vocabulary.

## How it translates to REE

For MECH-394 the translation is at the level of architecture-justification. The claim that multiple active drives must somehow be funnelled into one behavioural output is not a REE invention; it is a fifty-year-old ethological commitment with a worked formalism behind it. More usefully, the paper sharpens the central V4 design fork. McFarland and Sibly's framework is built on *strict mutual exclusivity* -- exactly one behaviour wins, a behavioural winner-take-all. MECH-394 deliberately chooses something softer ("soft-competitive orchestration ... not a single-axis winner"). So this paper is best read as anchoring one *pole* of the design space: the WTA endpoint that the REE policy is positioning itself against. Naming that pole precisely is what lets MECH-394's "soft" be a real commitment rather than a vague gesture.

## Limitations and caveats

Two caveats, and the first is the substantive one. The mutual-exclusivity axiom is a genuine divergence from MECH-394, not a wrinkle: McFarland and Sibly get a clean winner-take-all *because* they assume behavioural classes cannot co-occur, whereas REE wants to allow blended, partially-concurrent expression (approach-while-vigilant, forage-while-grooming). So this evidences the candidate-competition *skeleton* of MECH-394 while actively marking the WTA position the soft policy must argue against -- I have logged that as a failure signature rather than burying it. Second, it is a 1975 descriptive/behavioural framework validated on dove hunger and thirst; it specifies a functional form for competition but is silent on neural mechanism, and the transfer to a computational drive register assumes the causal-factor-space abstraction is substrate-general.

## Confidence reasoning

Source quality is solid-canonical (Phil Trans R Soc, foundational ethology) but it is theory-with-modest-empirics, not a modern circuit study, so I set 0.75. Mapping fidelity is the highest in this whole set on conceptual grounds -- the candidate/competitiveness/final-common-path language is almost REE's own E3 vocabulary -- which pulls the aggregate up; but transfer risk is elevated by the 1975 vintage, the narrow dove-behavioural base, and the WTA-vs-soft-blend tension. Net 0.66, raising MECH-394's literature confidence only; the claim stays substrate_conditional V4 with exp_conf = 0.
