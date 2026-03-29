# Barrett, Quigley, and Hamilton (2016) -- An active inference theory of allostasis and interoception in depression

**Claim tested:** Q-021 (does pure harm-avoidance training produce behavioral flatness?)

## What the paper did

Barrett, Quigley, and Hamilton proposed a unified theory of depression grounded in active inference and allostatic regulation. Their framework integrates the embodied predictive interoception coding (EPIC) model with predictive processing accounts of emotion to propose that depression is fundamentally a disorder of allostasis -- the brain's failure to correctly predict and regulate its physiological state. The 'locked-in' metaphor is central: through a positive feedback loop, the depressed brain becomes progressively less sensitive to sensory context (because it has learned that its predictions are unreliable or that allostatic correction fails) and more reliant on prior predictions (which are themselves dysfunctional). Behavioral avoidance is not a secondary symptom but a central maintaining mechanism: by avoiding approach behaviors, the agent prevents the very sensory experiences that would disconfirm its dysfunctional priors.

## Key findings relevant to Q-021

The locked-in dynamic is the key contribution for Q-021. Barrett et al. propose that depression involves a form of approach-avoidance imbalance where avoidance is elevated not because harm is more salient but because approach signals are insufficiently predictive or insufficiently reinforced. The behavioral consequence is progressive withdrawal: the agent converges on a policy that minimises prediction error (not maximises reward) by avoiding states of high sensory uncertainty. This converges on quiescence and passivity -- behavioral flatness -- because rest minimises unexpected sensory inputs.

For Q-021, the paper provides a direct theoretical bridge: the 'locked-in' state is what an agent trained only on prediction-error minimisation in the avoidance direction looks like once it has converged. The agent is not fearful; it is not in a state of elevated harm-avoidance activation. It is simply in a stable attractor state where non-action is the policy because action generates unpredicted sensory change. This is the Q-021 prediction made explicit: pure harm-avoidance (equivalent to pure prediction-error minimisation in the harm direction) converges on quiescence, not on active safe behavior.

## REE translation

Q-021 asks whether a pure harm-avoidance trained REE agent would show behavioral flatness. Barrett et al. 2016 describe the clinical dynamic that corresponds to this: the depressed brain has, through a positive feedback loop, learned to treat approach as high-risk (high prediction error territory) and rest as low-risk (low prediction error). This is architecturally equivalent to an agent where every action increases harm signal variance (because any action might produce harm), but inaction reliably produces zero harm signal. Under pure harm-avoidance, the agent that minimises harm signal variance converges on inaction. The locked-in self-maintaining aspect predicts that this policy should be difficult to reverse even if the training signal is subsequently changed -- the quiescent attractor has low policy entropy and may be difficult to escape.

The paper also addresses Q-021's two-pathway analysis indirectly. The locked-in positive feedback loop maps to Pathway B: even when drive is present (the patient is not globally apathetic), commitment is suppressed because the prediction error from acting is too high. This could occur in REE even when z_goal seeding is successful, if the action-harm relationship is learned to be too uncertain.

## Limitations and caveats

This is a theoretical paper in the active inference tradition. REE does not use an active inference framework -- it uses gradient descent with explicit loss functions -- so translating the locked-in dynamic to REE requires conceptual bridging. The active inference framing treats behavioral avoidance as a strategy for minimising surprise, which maps only approximately to REE's harm minimisation training objective. Also, the paper's clinical target is major depressive disorder in humans, which involves many factors (cortisol dysregulation, inflammatory signalling, social withdrawal) that have no analog in REE. The behavioral flatness in REE may arise from simpler mechanisms that do not require the full locked-in feedback loop.

## Confidence reasoning

Confidence is 0.72. The paper provides a coherent theoretical framework for how approach-signal failure leads to behaviorally flat quiescence, which maps to Q-021's Pathway A prediction. The confidence is moderate because the active inference framing requires translation, the clinical mechanism differs from the REE training regime question, and the positive feedback loop that maintains depression has no clear analog in REE's architecture.
