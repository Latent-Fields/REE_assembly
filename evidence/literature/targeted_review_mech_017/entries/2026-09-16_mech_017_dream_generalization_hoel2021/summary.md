# The overfitted brain: Dreams evolved to assist generalization (Hoel, 2021)

Hoel's paper is not an experiment and does not pretend to be one. It is an argument, and the
argument is worth having in MECH-017's evidence set because it addresses a question the claim's
own architecture note leaves unasked: why should there be an offline phase at all? If sleep merely
strengthened what was learned in waking, more waking would do. Hoel's answer is that a model
trained exclusively on the episodes it happened to encounter will fit those episodes and not the
world that generated them -- the overfitting problem -- and that dreams are the brain's noise
injection against it. Dreams are sparse, distorted and narratively odd on this account not because
they are degraded replay but because corruption is the point: they are augmented samples that pull
representations off the training set.

What this buys MECH-017 is a definition. The claim says sleep improves "the fidelity of the
generative world model" and lists prediction error minimisation among its operations, but fidelity
to what, and error measured against what? Hoel's framing says: out-of-sample error, not
reconstruction error on stored episodes. Those are different quantities and a mechanism can improve
one while degrading the other. That distinction is the contribution here, and it is the reason this
entry sits alongside the computational and behavioural ones rather than being omitted as
speculation.

The honest accounting is that the paper supplies no measurement. Its central prediction -- that
dream loss specifically, dissociated from sleep loss, produces a brain that still memorises but
fails to generalise -- is stated as a test to be run, not a test that was run. Nor does the
hypothesis currently distinguish itself from the synaptic homeostasis account: if generalisation
improves overnight, global downscaling predicts that too, and no result in this paper adjudicates.
An entry that matches REE's wording this closely is exactly the kind that should not be allowed to
inflate a claim's confidence, which is why the aggregate here (0.55) sits below the mapping
fidelity (0.85) rather than tracking it.

There is a second caution about direction of inference. REE's usual transfer risk runs from
biology to substrate. Hoel's runs the other way: the warrant for the hypothesis is that deep
networks overfit and are fixed by noise injection, therefore brains plausibly do the same. That is
a legitimate move but it is an analogy carrying the evidential load, and it presupposes that the
biological system is in the overfitting regime -- data-poor relative to model capacity. Whether
REE's own substrate is in that regime, with its replay budget and its data scale, is an open
question and not one this paper can answer. Read it for the framing; look to Deperrois and to the
human behavioural entries in this directory for whether the framing survives contact with results.
