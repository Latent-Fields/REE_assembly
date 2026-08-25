# Causal Mediation Analysis for Interpreting Neural NLP: The Case of Gender Bias (Vig et al., NeurIPS 2020)

This paper is one of the founding methodological references for what later became "activation
patching" or "causal tracing" in mechanistic interpretability, and it is a near-perfect
external instance of the NON-ORACLE, SILKY quadrant of GOV-INTERVENE-1's 2x2 intervention
taxonomy. The authors intervene on individual neurons and attention heads inside a
Transformer language model by substituting one word in a sentence's context (an ambiguous
profession term becomes gender-specific) and tracing how that single, minimally disruptive
perturbation propagates through the network to influence a downstream prediction. Crucially,
the intervention does not supply the model any privileged or target-correct answer -- it
perturbs a suspected causal variable and measures sensitivity, which is exactly GOV-INTERVENE-1's
definition of a non-oracle injection. And because the substitution is a single-word,
distribution-preserving edit rather than a deliberately unnatural combination of states, it is
also silky in GOV-INTERVENE-1's sense: diagnostic for localisation and sensitivity, not a
stress test for shortcut-dependence.

What makes this paper more than a passing analogy is its explicit decomposition of the total
intervention effect into a direct effect (bypassing all measured mediators) and an indirect
effect (flowing specifically through the neurons/heads under test), together with the finding
that gender-bias effects are sparse and synergistic -- concentrated in a small subset of
components, and amplified or suppressed depending on which other components are also active.
That is a direct, worked demonstration of why GOV-INTERVENE-1 insists on recording *provenance*
(which stage, variable, or relation was altered) rather than treating "we ran an intervention
and got an effect" as a single undifferentiated positive-control result: a single-mediator
intervention here would have systematically mis-attributed or under-attributed causal
responsibility, exactly the failure mode GOV-INTERVENE-1's taxonomy exists to prevent. The
paper is also disciplined in exactly the direction GOV-INTERVENE-1 requires: at no point do
Vig et al. claim the network "wants," "prefers," or "naturally exhibits" the traced bias
pathway during ordinary operation -- the finding is scoped strictly to what the intervention
demonstrated, with endogenous behaviour left as a separate, unaddressed question.

The mapping is methodological rather than substrate-literal, and that limit should be stated
plainly. This is a study of a static, feedforward-at-inference language model doing a
classification-style probing task, not a recurrent, multi-rate, continually-learning agent
like REE -- the specific technique (single-token context substitution scored via KL divergence
on a profession-gender proxy task) has no literal REE equivalent. What transfers is the
discipline itself: minimal single-variable perturbation, explicit effect decomposition, and a
hard line between "the intervention showed this pathway is sensitive to the manipulated
variable" and "the organism ordinarily uses this pathway." Confidence is set at a moderate
0.65: high source quality (a now-canonical NeurIPS methodology paper) offset by real transfer
risk from a static classifier to REE's recurrent, distributed architecture.
