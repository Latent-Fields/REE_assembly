# Neural Markers of Event Boundaries (Bilkey & Jensen 2019)

**Claim tested:** MECH-321 (policy_decomposition_via_event_segmenter)
**Direction:** supports · **Confidence:** 0.58

## What the paper does

Bilkey and Jensen review the brain activity that accompanies the processing of events and the transitions between them, with an explicit goal: to identify signals that could serve as *event boundary markers* (EBMs). They concentrate on the hippocampus, and specifically on sharp-wave ripples (SWRs) — brief high-frequency bursts that, they note, tend to occur following the cessation of a unit of behaviour. Their move is interpretive rather than empirical. Most models treat SWRs as serving memory consolidation, or as preplay tied to future thinking and prediction; the authors argue that an EBM reading should be folded into that account, since the same bursts sit at exactly the junctures where a segmentation account would predict a boundary.

## Why this matters for MECH-321

MECH-321 rests on a specific architectural bet inherited from the 2026-05-10 ARC-070 bidirectional-consumer commitment: that the event segmenter is **one detector reading a stream label**, not two detectors. MECH-288 supplies the detector; MECH-321 wires the rollout/imagination stream into it and consumes the resulting boundary pulses at the policy-primitive layer. The alternative design — a separate imagination-side segmenter — is perfectly buildable, and nothing internal to REE adjudicates between them.

This paper is the closest thing in the biological literature to an adjudication. If a single physiological signal class genuinely sits at the intersection of (a) boundaries between units of real behaviour and (b) preplay sequences oriented toward future thinking, then the parsimonious biological design is one marker generator serving both directions. That is the design MECH-321 assumes. It is worth being clear that this is a *design-plausibility* argument rather than a mechanistic result — but design plausibility is precisely what a claim at MECH-321's stage of registration needs, and it is the axis on which the parent ARC-070 lit set (Zacks 2007, Schapiro 2017, Badre & D'Esposito 2009, Koechlin & Summerfield 2007) is silent, since all of those are observation-side or hierarchy-side rather than bidirectionality-side.

## Where the mapping breaks

Two gaps, and I do not want to soften either.

First, and most seriously: the paper supports shared *markers*, not the *operation* MECH-321 specifies. MECH-321 does not merely need boundaries to be detectable on imagined trajectories; it needs a boundary detected on an imagined trajectory to cause that trajectory to be **re-segmented at finer grain**, feeding a decomposed sub-element stream to ARC-062. SWRs during preplay are at least as easily read as a *generation* signal — the mechanism by which the imagined sequence is produced — as a signal that segments an already-produced sequence. Those are different computational roles that happen to be visible as the same burst, and this review does not distinguish them.

Second, the timing. The paper repeatedly characterises SWRs as following the *cessation* of a behavioural unit. That is a post-hoc marker. MECH-321 commits to supporting both a pre-commit phase and a **mid-execution** phase through the same mechanism; a boundary signal that arrives only after the chunk has completed cannot serve the mid-execution case. This may be an artefact of which SWR literature the review draws on rather than a real constraint, but as stated it is a mismatch, and it sharpens the open Q-claim already registered in MECH-321's notes about whether mid-execution decomposition is the same mechanism as reactive replanning or a distinct one. If the boundary marker is intrinsically post-hoc, the mid-execution case is probably the *other* mechanism.

There is also a straightforward transfer risk: identifying a hippocampal burst marker with REE's V_s-drop-on-region trigger is an analogy, not an established correspondence, and the rodent-to-human-to-artificial-agent chain is long.

## Confidence reasoning

Source quality is decent but not high — a peer-reviewed review by authors with genuine hippocampal expertise, in *Topics in Cognitive Science*, but a hypothesis piece carrying no new data. Mapping fidelity is the binding constraint at 0.6: the paper licenses the one-detector-two-streams design at the level of marker sharing, and stops well short of the re-segmentation operation. Because MECH-321 is an architectural claim, I have weighted mapping fidelity heavily, which pulls the aggregate to 0.58 — below what source quality alone would suggest. That feels right. This entry should be read as raising confidence that the bidirectional substrate design is biologically sane, not as evidence that rollout-side decomposition happens in brains.
