# Strigo & Craig (2016) — Interoception, homeostatic emotions and sympathovagal balance

## What the paper does

Strigo and Craig update the interoceptive-cortex framework that Craig had been developing since his 2002 Nature Reviews Neuroscience paper. They argue that the primate and human brain contains a hierarchical sensorimotor architecture specifically dedicated to interoception: afferent representations of body state converge in the insular cortex (especially the dorsal posterior and then anterior insula), where they substantialize as felt body states; these feelings are conjoined in cingulate cortex with homeostatic motivations that drive adaptive behaviour. Their specific contribution in this paper is to show how this architecture accommodates bivalent feeling states (positive/negative, approach/avoidance, parasympathetic/sympathetic) through asymmetric organization of activation patterns rather than through architectural reorganization. They provide original supporting evidence from cardiorespiratory vagal activity recordings in macaques and from human functional imaging during paced breathing and passively viewed emotional images.

## Key findings relevant to SD-011 context-stability

This is the single most relevant paper in the pull for the architectural-stability question, because it directly addresses whether the interoceptive substrate (which is the z_harm_a analogue in SD-011) changes its structure across states or whether it expresses state differences through asymmetric activation of a stable structure. Craig and Strigo argue for the latter, unambiguously.

For SD-011 the implication is: the dual-stream architecture — A-delta/S1 vs C-fiber/medial-thalamic/insula-cingulate — is not reshuffled under affective-state shifts. What changes is the pattern of activation across the stable substrate. When I move from a positive-valence approach context to a negative-valence avoidance context, the insular interoceptive map does not reorganize — different components of it light up asymmetrically.

Combined with the Apkarian 2011 and Baliki 2014 evidence that downstream integration can drift under sustained context, the synthesis is: the streams themselves are architecturally fixed, their downstream couplings are plastic, and the distinction is diagnostic — if the architecture itself reorganized across context, that would be pathological reorganization (as in chronic pain), not normal context-sensitivity.

## How this translates to REE

The direct architectural translation to SD-011 is strong. REE's z_harm_a (C-fiber/insula-cingulate-analogue) should be a fixed architectural component whose activation pattern varies with context. It should not be implemented as a dynamically reorganizing module. Context-dependent behavioural changes should be encoded through asymmetric activation weights on a stable substrate, not through changes in which modules are coupled to which.

Daniel's V3 implementation note in claims.yaml already captures this: "The two encoders should not be orthogonally constrained — their separation emerges from distinct training targets (forward-predictable vs EMA-integrated), not from a hard independence requirement." That maps well onto Strigo & Craig's asymmetric-activation-of-stable-architecture principle. The encoders exist in fixed architectural positions; their activation patterns respond to context.

## Limitations and caveats

The paper is synthesis rather than dedicated empirical test. The architectural-stability claim is defended on convergent-evidence grounds across primate anatomy, human imaging, and cardiorespiratory physiology — individually, each of those sources is weaker than a dedicated test would be. There is also an ontological gap: Strigo & Craig argue the insular architecture is what substantialises feelings, which is a philosophical claim REE does not need to accept in full. SD-011's dual-stream design can be motivated by the anatomy and functional dissociation without inheriting the full feelings-are-made-in-the-insula framework.

## Confidence reasoning

I put this at 0.75. The paper's claim that interoceptive architecture is stable across affective states is exactly the context-stability claim SD-011 needs, and it comes from the author who has done the most anatomical groundwork on the substrate in question. The mapping is direct because SD-011 explicitly draws on Craig's prior work. I held confidence at 0.75 rather than higher because the evidence is synthetic rather than from a single decisive empirical test, and because the paper's philosophical framing (insula as substantialiser of feelings) goes further than SD-011 requires or can adjudicate. The clear take-home for the pull: the dual-stream architecture is expected to be stable across context; context-sensitivity is expected to appear in activation patterns, not in architectural reorganization.
