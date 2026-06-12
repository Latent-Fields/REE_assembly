# Kumaran, Hassabis & McClelland (2016) — replay as the integration engine, and schema-consistency as the super-additive regime

**Claim grounded:** MECH-423 (cross-model super-additivity) — readiness condition R3 (active replay) and the scoping of *when* super-additivity appears.
**Direction:** supports. **Confidence:** 0.74.

## What the paper did

Twenty years after the 1995 paper, the same lineage (now with the DeepMind founders who built replay into deep RL agents) updated CLS theory. Two updates matter here. First, they broadened the role of replay: hippocampal replay is not just a rehearsal buffer but a mechanism for *goal-dependent weighting of experience statistics* — the system can preferentially replay the experiences that most need integrating. Second, they qualified the "slow cortex" story: neocortical learning can be *rapid* when the new information is consistent with already-known structure (the schema-consistency result). They close by drawing the explicit line to artificial agent design, noting that the neuroscience and machine-learning accounts of why you need two systems are converging.

## Why it speaks to MECH-423

This paper is unusually well-matched to MECH-423 because it lives in the same cross-domain register: it is a neuroscience theory written for people building integrated learning agents. It supports the readiness precondition directly — replay is *the* route by which structured, shared knowledge is built, so REE's MECH-121 replay must be running and weighting traces across modules for the integrated arm to accrue any cross-pollination advantage. That is readiness condition R3.

More valuably, it sharpens *where* super-additivity should be expected. The schema-consistency result implies the integrated arm beats the additive baseline specifically when the modules sharing the L-space latent carry mutually-consistent structure. This is the empirical bite for EXP-0380's interpretation: a null or negative result on a poorly-matched module pairing is about task-relatedness, not about broken integration machinery. It tells the experiment designer to pick modules (E1 world-model + E2 affordance-model) whose features genuinely overlap — which is exactly the Topic-2 pairwise instance the proposal already uses as its INTEGRATED-PAIR arm.

## Limitations and mapping caveats

It is a review and position paper. It establishes that replay is the integration route and that schema-consistency governs the speed of gain, but it does not measure a super-additive margin — the magnitude that EXP-0380 must pre-register is not supplied here. The "intelligent agent" framing is programmatic. So this entry, like the 1995 anchor, grounds the prerequisite and the regime, not the headline number.

## Confidence reasoning

Top-venue review, authoritative authorship spanning precisely the neuro/ML bridge MECH-423 occupies, hence source quality 0.85 and a slightly higher overall confidence than the 1995 entry. Held below 0.8 because review-level evidence asserts the super-additive plausibility rather than demonstrating the margin, and the agent-design transfer is argued rather than benchmarked.
