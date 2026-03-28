# Seymour et al. 2004 — Temporal Difference Models Describe Higher-Order Learning in Humans

**Source:** Seymour B, O'Doherty JP, Dayan P, Koltzenburg M, Jones AK, Dolan RJ, Friston KJ, Frackowiak RS (2004). *Nature* 429(6992):664–7. [DOI: 10.1038/nature02581](https://doi.org/10.1038/nature02581)

---

## What the paper did

Healthy human participants underwent sequential aversive conditioning while in an fMRI scanner. A cue sequence (cue1 -> cue2 -> noxious stimulus) was used, where cue1 predicted cue2 and cue2 predicted pain. The design allowed the authors to ask whether the brain learns about harm through a simple stimulus-response association or through a richer, temporally structured predictive model. They fitted the BOLD signal from ventral striatum and anterior insula to temporal difference (TD) learning signals — specifically prediction errors that update harm predictions at each stage of the cue sequence. The paper was principally a demonstration that a computational model from reinforcement learning, originally developed for reward, extends naturally to aversive learning.

## Key findings relevant to ARC-024

The core finding is that neural activity in the ventral striatum and anterior insula tracks TD prediction error signals for incoming harm. The brain does not simply respond to the painful stimulus at the moment of contact; it generates a sequence of updating harm predictions across the cue chain — a graded anticipatory signal that approaches the harmful event from a temporal distance. When cue2 appeared, the brain registered a prediction error transferring harm expectation backward along the cue chain, consistent with TD learning. This is the temporal analogue of spatial gradient: the harm signal is not zero until contact, then suddenly large — it builds continuously across the cue sequence.

The broader computational implication is that the brain implements something like the hazard_field in CausalGridWorldV2, but in the temporal domain: harm-signal magnitude increases as the agent approaches the harmful event along a trajectory, whether that trajectory is spatial (closing distance to a hazard) or temporal (traversing a cue sequence leading to pain). Both are expressions of the same underlying structure — harm is a proxy gradient with an asymptotic limit.

## Translation to REE / ARC-024

ARC-024 claims that harm signals have proxy structure — they are graded and precede the contact event. The TD aversive learning result supports this at the computational level: the architecture required to produce this learning is one where harm signal magnitude is non-zero before contact and increases toward the contact asymptote. If the brain used binary harm signals (zero everywhere, then maximum at contact), TD learning would collapse to simple stimulus-response association and no sequential learning would occur. The fact that sequential aversive learning is observed and follows TD dynamics implies that the underlying representation of harm must be graded.

This paper is particularly relevant because REE's E2 (forward model) and E3 (evaluation) architecture is explicitly modelled on predictive coding and temporal difference learning. The Seymour et al. result provides empirical grounding for the claim that aversive prediction in a biologically realistic system operates through a gradient representation rather than a binary contact-only signal.

## Limitations and caveats

The study demonstrates temporal gradients (harm signal builds across a cue sequence over time) rather than spatial proximity gradients (harm signal builds across space toward a hazard). ARC-024's primary operationalisation in the REE environment is spatial, so the inference requires treating temporal distance and spatial distance as equivalent parameterisations of the same gradient structure. This is theoretically motivated but not directly tested. Additionally, the study used controlled electrical pain stimuli with known temporal structure, which may produce cleaner TD dynamics than the continuous, partially observable harm signals an agent would encounter in a naturalistic grid world.

## Confidence reasoning

Confidence assigned 0.70. Source quality is excellent (Nature, 8-author team including Dayan, Friston, and Dolan — a who's-who of computational neuroscience). Mapping fidelity is moderate rather than high because the temporal-vs-spatial distinction is real and requires an additional inferential step. Transfer risk is elevated for the same reason. The paper earns its place in this batch because it provides the computational-level grounding that the spatial-proximity papers (Mobbs, Fanselow) do not: it shows directly that the brain's representation of harm is structured in a way that requires a gradient signal before contact.

*According to PubMed, this article is available at PMID 15190354. [DOI: 10.1038/nature02581](https://doi.org/10.1038/nature02581)*
