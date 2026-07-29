# Demixed PCA and the common-mode problem (Kobak et al. 2016)

Kobak and colleagues built dPCA to solve a nuisance that anyone who has looked at prefrontal
population data knows well: single neurons in higher cortex are tuned to almost everything at once,
so the raw population response is a tangle. Their method decomposes population activity into
components tied to particular task parameters -- stimulus, decision, their interaction -- plus a
*condition-independent* component that varies with time within a trial but is identical across
every condition. They then applied it to four independent single-unit datasets: macaque prefrontal
cortex in two tasks, macaque PFC in a delayed working-memory task, and rat orbitofrontal cortex
during olfactory discrimination.

The result that matters here is not the method but what the method reveals. Across every dataset,
the condition-independent marginalisation absorbs a large share of the explained variance, while
the stimulus and decision components are individually small. Standard PCA, which ranks by variance,
returns leading components that mix the two -- so the components that look most important are
precisely the ones that carry the least task information. The task-relevant structure is there, and
it is robust, and it is invisible unless you subtract the part that every condition shares.

That is the shape of SD-082's failure, restated in recorded cortex. V3-EXQ-822 found a genuinely
differentiated rule pool -- `on_rule_state_diff` 0.644, sixteen live rules -- propagating to the
action bias at exactly 0.0. The temptation is to read a zero at the output as evidence that the
upstream differentiation was not real. Kobak et al. say that inference is unsound: a differentiated
signal riding on a much larger shared component simply does not survive a read-out taken from the
raw state. Under the SD-008 cone every candidate summary sits within about 0.98 cosine of every
other, which is the extreme case of exactly this geometry, and the hard clamp then finishes the job
by railing every candidate to the same value. SD-082's per-tick subtraction of the mean summary
across candidates is a small in-model version of what dPCA does analytically.

Two things keep me from scoring this higher, and both are honest limits rather than quibbles.
First, dPCA is something an *analyst* does, with knowledge of the task design in hand; the paper
does not claim -- and offers no evidence -- that any neural circuit performs the demixing. So this
is strong warrant for SD-082's diagnosis and weak warrant for SD-082's remedy. Second, the
marginalisation axis is not the same one: dPCA averages over conditions and time, SD-082 subtracts
across candidates within a single tick. Both strip a shared component, but the correspondence is an
analogy. Nothing in this paper tells us how much of REE's candidate-wise common mode is genuinely
uninformative as opposed to carrying state the bias head ought to be using -- and if some of it is
informative, mean subtraction throws it away.

Confidence 0.72. The finding is well established and directly on point for the premise; it is the
translation from an offline decomposition to an online architectural operator that carries the risk.
