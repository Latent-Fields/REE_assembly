# Capkova, Ainsworth, Mansouri & Buckley (2025) -- dissociating frontal lesion deficits in rule value learning

Of everything surfaced in this pull, this is the paper whose *shape* most closely matches what
ARC-113 asks for. The authors took eighteen macaques across five bilateral frontal lesion groups --
orbitofrontal cortex, principal sulcus, anterior cingulate, superior dorsolateral PFC and
frontopolar cortex -- ran them on a computerised Wisconsin Card Sorting analog before and after
surgery, and then, crucially, did not stop at "performance dropped". They fitted a reinforcement
learning model to the behaviour and asked *which latent parameter* each lesion had damaged. That
second move is the whole point. ARC-113's falsifier explicitly refuses undifferentiated performance
decrement as evidence; it requires that removing one stage produce a signature distinguishable from
removing another. This design is built to answer exactly that question.

The answer is that the signatures do separate, and they separate qualitatively rather than by
degree. OFC lesions slowed rule value learning from both positive feedback (alpha+ 0.75 to 0.37,
p=0.0083) and negative feedback (alpha- 0.96 to 0.69, p=0.013). ACC lesions spared positive-feedback
learning (p=0.062, not significant) and selectively damaged negative-feedback learning (alpha- 0.92
to 0.64, p=0.0043). Principal sulcus lesions touched *neither* learning rate (p=0.40, p=0.69) and
instead degraded the ability to repeat correct choices once rule values were already well
established (p=0.029) -- a maintenance failure, not a learning failure. The authors also note that
perseverative errors after a rule change had different time courses in the OFC and ACC groups
(errors from trial 2 versus trial 4), and that all lesioned animals were normal on control tasks
without rule switching, which isolates the deficits to rule handling rather than perception or
motor control.

Translated into ARC-113's vocabulary, this is a three-way dissociation across adjacent stages of the
cycle: representation (principal sulcus, holding the rule), outcome comparison and regularity
refinement (OFC, updating rule value against feedback), and the control of transitions between
trial-and-error apprehension and working-memory-based application (ACC). If those stages were one
reasoning module operating at different intensities, three different lesions could not selectively
damage three different model parameters while leaving the others intact. That is the support.

The honesty is in what the paper also shows. Two of the five lesion groups -- superior dorsolateral
PFC and frontopolar cortex -- produced no significant effect on any learning parameter and no
overall WCST impairment. I record this as a failure signature rather than a null to be waved past,
because it directly engages ARC-113's non-degeneracy guard: the claim requires that the intact
baseline show live variance on a discriminating metric *for each stage*, and here two regions that
a one-region-per-stage story would want to load-bear simply do not. The dissociation is also only
partial in the other direction: OFC and ACC lesions both raised choice stochasticity and both
impaired repeat-after-surprising-reward, so some post-ablation signatures are shared. And the
authors concede that model fit dropped after lesion in three groups, meaning real post-ablation
structure escaped their model.

Confidence 0.75. Source quality is high for a lesion study -- within-subject pre/post design, an
explicit generative model, published in eNeuro -- though per-group n is only three or four and
aspiration lesions carry acknowledged white-matter damage that weakens region-to-stage attribution.
Mapping fidelity is capped at 0.7 because the task exercises perhaps three of ARC-113's eleven
stages in a colour-and-shape rule space of trivial dimensionality; nothing here touches
counterfactual simulation, generalisation, or long-term integration, and the *ordered cycle* -- the
genuinely new part of ARC-113 -- is untested. What this paper licenses is the weaker and still
useful proposition that stage non-collapsibility is a real empirical phenomenon in at least one
biological rule-learning system, and that a parameter-level model is the instrument that reveals it.
That last point is a design lesson for the eventual REE ablation, not just a citation.
