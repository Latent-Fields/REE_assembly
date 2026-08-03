# Does Learning Require Memorization? A Short Tale about a Long Tail (Feldman, STOC 2020)

**Claim under test:** MECH-472 -- held-out context distinguishes skill acquisition from task memorisation; promote to durable only on evidence from contexts that did not generate the competence.

This entry is deliberately the counterweight to the other three in the MECH-472 pull. Cobbe, Zhang, and Lake & Baroni all sharpen the case that in-context success can be counterfeit. Feldman asks the opposite question and finds an answer that qualifies -- without overturning -- MECH-472's design.

## What the paper did

Feldman builds a theoretical model in which data is drawn from a mixture of subpopulations with long-tailed frequencies -- the shape that real image and text data are known to have. He then proves a lower bound: to achieve close-to-optimal generalisation error on such distributions, a learner **must memorise the labels of atypical, low-frequency training examples**. Memorisation is not a pathology of over-parameterised models to be regularised away; on long-tailed data it is a *requirement* for optimal learning, because the rare examples carry information that cannot be recovered from the rest of the distribution.

## Key findings relevant to the claim

The bearing on MECH-472 is precise and worth stating carefully. MECH-472 proposes to read the in-context-vs-held-out gap as a memorisation-vs-acquisition signal and threshold it. Feldman's result says: some instance-specific retention is exactly what an optimal learner *should* do, so a nonzero gap does not by itself prove that acquisition failed. A promotion rule that treated *any* held-out gap as "memorised, therefore block" would suppress competences that legitimately encode tail-specific structure -- and thereby *harm* generalisation, the opposite of what MECH-472 intends. The lesson is that MECH-472's gap is a graded, threshold-calibrated signal, not a binary gate; the non-degeneracy guard and the "beyond a threshold" wording in the claim are load-bearing, and this paper is the theoretical reason why.

## How this translates to REE

This does not refute MECH-472 -- held-out evidence remains the right way to test whether a competence transfers, and the other three entries establish that firmly. What Feldman adds is calibration. He warns against the strong reading in which the mere existence of a gap condemns a competence to "provisional". For REE, this argues for: (a) a threshold rather than a zero-gap requirement; (b) attention to whether the held-out set is drawn from the *tail* of the task distribution (where some gap is expected even for a genuinely competent agent); and (c) treating the promotion decision as trading off transfer against the functional value of instance-specific learning.

The mapping has real caveats, which is why the direction is "mixed" and confidence is 0.6. Feldman's "memorisation" (retaining labels of rare examples) is related to but not identical with MECH-472's "memorisation" (a competence that only works in its generating contexts). His result is theoretical, under a specific mixture model, about supervised classification error -- it does not measure an agent's held-out competence and so cannot confirm or refute MECH-472 directly. It bounds the *strong interpretation* of the claim; it does not test the claim.

## Confidence reasoning

Source quality is high -- a STOC paper with a clean, influential theorem. But its role in this pull is to calibrate the threshold and guard against an over-strong reading, not to confirm the core mechanism, so mapping fidelity is the limiting component. The two senses of "memorisation" overlap but are not the same, and the domain is supervised theory rather than agentic RL. A moderate, honestly-mixed confidence is the right record for a paper whose value is precisely that it complicates the other three.
