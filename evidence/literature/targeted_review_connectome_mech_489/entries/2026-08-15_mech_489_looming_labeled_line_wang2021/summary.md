# OFF-transient alpha RGCs mediate looming triggered innate defensive response

Wang, Li, De, Wu & Zhang (2021), *Current Biology* 31(11):2263-2273.e3. DOI 10.1016/j.cub.2021.03.025. PMID 33798432.

## What the paper did

The authors went after a question that is easy to state and hard to answer: when a mouse sees something rushing toward it and runs for shelter, what actually detected the threat? They identified a single genetically-defined retinal ganglion cell type -- OFF-transient alpha RGCs, marked by Kcnip2 -- and showed that these cells encode the size of a looming object and project to the superior colliculus. Then they did both halves of the causal test in the same paper. Ablating that one cell type eliminated the looming-evoked defensive response. Selectively activating their axon terminals in the superior colliculus was sufficient to trigger escape on its own. Their conclusion is stated in strong terms: ethologically significant visual information is encoded by a labeled-line strategy as early as the retina.

Loss-of-function and gain-of-function in the same preparation, on a genetically identified cell type, is about as close to a clean causal argument as this kind of question admits.

## Why this bears on MECH-489

MECH-489 states its trigger as a disjunction. The phasic defensive arrest fires on a positive-derivative onset in *either* `residue_surprise` -- an unsigned prediction-error magnitude -- *or* a sensory-discriminative harm norm. Both disjuncts are on the table in the claim as registered, and nothing in the claim text adjudicates between them.

This paper adjudicates. The biological system it describes does not detect threat by thresholding a general-purpose surprise signal. It detects threat with a dedicated, feature-tuned line that is separable from everything else vision is doing, and it does so early -- in the retina, before any cortical model of what is expected has had a chance to weigh in. A looming object is not salient to this pathway because it was unpredicted. It is salient because it is looming.

That is a genuine and, I think, useful result for REE, and it is why I have recorded the direction as `mixed` rather than `weakens`. It weakens the first disjunct and supports the second. The claim as written is not falsified by this; it is *narrowed*, and narrowed in a direction that happens to be actionable.

I want to be careful about what this does and does not say about the two experimental runs that landed against MECH-489. It says nothing about them directly -- literature evidence and experimental evidence are separate registers, and the runs are the load-bearing kind. What it does is speak to a question the confirmed autopsies left open. Those autopsies established, and independently corroborated from a second analysis, that this substrate's `residue_surprise` channel concentrates its largest peaks on reef-boundary crossings and resource events rather than on hazard-type events, and concluded that a correctly-built onset detector over that channel would under-fire regardless. The autopsies graded the biological reference as "partial -- channel-type translation is reasonable". This paper is a reason to think the channel-type translation was the weaker half of the design, not merely a calibration matter: a generic-surprise trigger is not the architecture the biology uses, so a generic-surprise channel whose composition does not concentrate on hazards is a predictable failure rather than a surprising one.

## Limitations, and they are not small

The transfer here is architectural and nothing below that level survives it. REE has no retina, no visual system, and no looming feature; there is no sense in which it should grow an OFF-transient alpha RGC analogue. What transfers is the shape of the answer -- dedicated threat-tuned line rather than threshold on a general salience magnitude -- and that is a coarse lesson to carry from mouse retina to an abstract latent-space agent.

Three further caveats. This is an *innate* response, not a learned one, and MECH-489's chain involves identification and valence-gated action selection that this pathway does not perform. The behaviour measured is fast escape to shelter, which is one point on the defensive repertoire and specifically not the freeze-then-orient chain MECH-489 asserts. And the dissociation between threat-specific and generic-novelty signals is *inferred* -- from the fact that ablating one cell type abolishes the response while the rest of vision remains intact -- rather than demonstrated by an explicit surprise-versus-threat contrast. I would want that contrast before leaning on this too hard.

## Confidence

0.62. Source quality is high (0.88) and I do not think the causal claim within its own domain is seriously contestable. Mapping fidelity (0.55) is what holds the number down, and transfer risk is set deliberately high (0.50) rather than charitably. The honest summary is that this is a strong result in its own domain that licenses one architectural inference for REE and nothing more specific than that -- but the architectural inference it licenses happens to land squarely on the sub-component MECH-489's own experimental evidence has been struggling with.
