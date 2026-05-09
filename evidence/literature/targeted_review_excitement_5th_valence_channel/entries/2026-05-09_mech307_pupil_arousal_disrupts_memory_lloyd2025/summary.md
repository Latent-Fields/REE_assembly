# Lloyd, Miletic and Nieuwenhuis 2025 — Pupil-linked arousal counteracts the positive effects of reward anticipation on incidental memory encoding

**Source:** Lloyd B, Miletic S, Nieuwenhuis S. *Cognition* 264:106237 (2025). [DOI: 10.1016/j.cognition.2025.106237](https://doi.org/10.1016/j.cognition.2025.106237). PMID: 40651362.

## What the paper did

Lloyd, Miletic, and Nieuwenhuis ran 33 healthy young adults through a monetary incentive delay (MID) encoding task. On each trial, a cue indicated potential reward, then an incidental scene was shown briefly. Twenty-four hours later, participants returned for a surprise recognition memory test on those scenes. Pupil dilation was recorded continuously during encoding, giving a trial-by-trial measure of arousal.

The hypothesis was straightforward: pupil-linked arousal during encoding mediates the positive effect of reward anticipation on subsequent memory. The standard expectation, drawing on Adcock 2006 and the broader memory-consolidation literature, is that anticipatory arousal helps consolidation — high arousal during encoding should produce better memory.

The result went the other way. Reward anticipation did produce the expected positive direct effect on memory (replicating Adcock 2006). But trial-by-trial pupil-linked arousal had a *negative* effect on memory, partially counteracting the reward-anticipation benefit. The mediation analysis suggested the mechanism is decision urgency: high arousal pushed participants toward faster, more reactive responses to the cue, and that fast/reactive processing mode disrupted incidental encoding of the scene that followed.

## Key findings relevant to MECH-307 Gap 3

This is the most uncomfortable entry in the MECH-307 lit base, and that's why it matters. Gap 3 of MECH-307 says: when MECH-216 schema readout fires above threshold, also raise z_beta arousal proportionally. The architectural assumption — implicit in the synthesis text and explicit in the consumer-side wiring — is that the z_beta raise is monotonically helpful for downstream memory consolidation. It feeds into the Adcock-style prediction that anticipation-marked locations get higher replay priority.

Lloyd et al. break that assumption. In humans, the same kind of anticipatory arousal that ought to help consolidation also produces decision urgency that disrupts encoding. The relationship between anticipatory arousal and memory is not monotonic; it is inverted-U or context-gated, with the cost depending on whether the arousal channels into "engage with this stimulus" or "respond fast."

For MECH-307, the architectural lesson is a *constraint*, not a refutation. The Gap-3 z_beta coupling cannot be implemented as a simple monotonic raise. There must be either an inverted-U (high z_beta beyond some threshold becomes counterproductive) or a context gate that distinguishes encoding-relevant arousal (good for consolidation) from urgency-relevant arousal (bad for encoding). The substrate must somehow distinguish these two arousal sources, or it will produce conjunction-state writes at locations where the high z_beta is actually corrupting the residue field rather than amplifying its functional role.

This complicates the V3-EXQ-540 successor design. The current acceptance metric measures conjunction-fire-rate and approach-commit-rate elevation, both of which would be insensitive to the Lloyd et al. failure mode. A more discriminating metric — replay-priority elevation specifically *with* downstream memory benefit, not just conjunction-fire detection — would catch the case where high z_beta is firing the conjunction predicate but corrupting consolidation. That's a more expensive metric to implement (requires sleep substrate + encoding-quality measurement) but it's what the lit base actually demands.

## How the findings translate to REE

The translation runs through one specific design question: does REE need an inverted-U on z_beta coupling, or a context gate, or both? An inverted-U is simpler — z_beta_increment = f(schema_salience) where f is monotonically increasing for low-to-moderate schema_salience and decreasing thereafter. A context gate is more architecturally interesting — z_beta_increment is gated by some signal that distinguishes "this arousal is helping me engage" from "this arousal is making me rush." Biology probably uses both (LC-NE has a well-documented inverted-U on cognitive performance; PFC top-down control supplies the context gate).

For MECH-307's first implementation pass (V3-EXQ-540 ARM_2_full), the simplest defensible choice is to clamp z_beta_increment at a moderate ceiling and not try to capture the context gate yet. The Lloyd et al. result then becomes a follow-on validation question: does the substrate-with-clamp produce the Adcock-style replay-priority elevation without the Lloyd-style memory disruption? If yes, the simple ceiling is enough. If no, the context gate is needed and there's a substrate-design question about what signal supplies the gate.

## Limitations and caveats

This is one paper, one paradigm (MID with delayed surprise memory), one population (n=33 young adults), and the proposed mechanism (decision urgency) is inferred from a mediation analysis rather than demonstrated by causal manipulation. The result is statistically robust within the paradigm, but its generalisation across paradigms is unclear. Other studies (notably Murty and Adcock 2014, building on the original Adcock 2006 work) have shown the positive arousal-memory effect more cleanly in different paradigms, so the Lloyd et al. finding is a real but bounded phenomenon, not a wholesale overturning of the Adcock framework.

For MECH-307's purpose, the paper functions as a *constraint* on Gap 3 implementation rather than a falsification of MECH-307 as a whole. The architectural commitment (z_beta couples to schema readout) survives; the implementation detail (monotonic vs context-gated) is what Lloyd et al. inform. The published 2025 date matters here too — this is recent, well-controlled work that the original 2026-05-08 lit-pull (which closed before Lloyd et al. became available) couldn't have considered.

## Confidence reasoning

I assign confidence 0.62 — mixed/weakens direction, moderate confidence. Source quality is solid (Cognition, peer-reviewed, statistically defensible) but capped because it's a single behavioural study with n=33 and the causal mechanism is inferred from mediation rather than manipulated. Mapping fidelity is moderate — the result speaks to Gap 3 implementation specifically but not to the conjunction-state architecture as a whole. Transfer risk is moderate-elevated because the decision-urgency mechanism may be human-task-specific (REE doesn't have the same fast/reactive vs slow/deliberative dichotomy at the action-selection level that human MID tasks expose).

The paper is included as a critical balancing entry. Without it, the MECH-307 lit base reads as uniformly supportive, which would mis-represent the architectural risk. With it, the synthesis acknowledges that Gap 3 specifically has a real failure mode that the substrate must engineer against. That kind of honest accounting is what the lit-pull is for.
