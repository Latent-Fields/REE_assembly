# Barnes et al. 2011 -- Task-bracketing in sensorimotor striatum

## Source
Barnes TD, Mao JB, Hu D, Kubota Y, Dreyer AA, Stamoulis C, Brown EN, Graybiel AM. Advance cueing produces enhanced action-boundary patterns of spike activity in the sensorimotor striatum. J Neurophysiol 105(4):1861-1878. DOI: 10.1152/jn.00871.2010

## Finding
Sensorimotor striatal neurons develop characteristic spike patterns at the start and end of learned action sequences -- the "task-bracketing" signature. When advance cues increase the predictability of sequence onset, the end-bracket becomes more pronounced, indicating that the end-of-sequence representation sharpens when the animal has a better model of what counts as "completion".

## Why it maps to SD-034
SD-034 proposes a closure operator that emits a release signal on rule_state satisfaction. The end-bracket observed by Graybiel's lab is the closest empirical analog in the biology: a specific neural event that fires at sequence completion, distinct from mid-sequence activity. It is not diffuse; it is a named, replicable signature.

Under advance cueing -- when the agent has a clearer predictive model of where the sequence will terminate -- the end-bracket sharpens. This is consistent with SD-034's view that closure detection is grounded in a model of what rule satisfaction looks like, not just a reaction to post-completion feedback.

## Confidence: 0.68 (supports)
- source_quality 0.80 (J Neurophysiol, Graybiel programme, replicated signature)
- mapping_fidelity 0.55 (procedural sensorimotor boundary, not cognitive rule completion)
- transfer_risk 0.45 (substrate and abstraction level differ from SD-034 target; analogical)

## Key limitations
- The bracketing signature is a property of sensorimotor striatum after substantial training. SD-034 closure must also function on cognitive rule_states -- likely a PFC/OFC/cortico-striatal phenomenon rather than purely sensorimotor.
- Bracketing marks procedural sequence endpoints. The analogy to cognitive rule-completion is motivated but not demonstrated in this paper.
- The paper establishes that the end-bracket exists as a neural signature; it does not show that downstream structures use it as a commitment-release signal. If the bracket is a correlate rather than a causally consumed signal, SD-034's closure-token framing is over-mechanistic.

## Failure signatures
- If closure operators in cognitive domains use a different mechanism than sensorimotor bracketing, this evidence is analogical at best.
- If task-bracketing only emerges under heavy over-training, the closure operator needs a separate early-learning mechanism.
- If the bracket is merely an observable signature rather than a downstream-consumed signal, it is a correlate of completion, not the closure token.
