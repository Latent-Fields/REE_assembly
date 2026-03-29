# A Survey on Bias and Fairness in Machine Learning — Mehrabi et al. (2022)

## Relevance to Q-014

Q-014 concerns a structural risk: that JEPA invariances might hide distinctions that are ethically relevant to REE's attribution pipeline. Mehrabi et al.'s canonical survey on ML fairness offers a useful conceptual anchor because it documents, at scale, how a seemingly neutral design choice -- removing sensitive information from representations -- systematically produces ethical blind spots. The mechanism, not the specific application domain, is what transfers to Q-014.

## The Fairness Through Unawareness failure

The survey's treatment of Fairness Through Unawareness (FTU) is directly relevant. FTU holds that fairness can be achieved by training models that are blind to protected attributes: if the representation does not encode race or gender, downstream decisions cannot discriminate on those grounds. The survey documents comprehensively why this fails in practice: protected attributes correlate with non-protected features, and a model blind to the protected attribute but sensitive to the correlated proxy will make the same discriminatory decisions while appearing to comply with the fairness constraint. The invariance creates not neutrality but a blind spot -- the information is effectively hidden from audit while still influencing the outcome.

The authors catalogue the failure modes: historical bias encodes past discrimination into training data, which reappears in the learned representation despite invariance; feature correlations allow proxy discrimination; representation shift between training and deployment means the invariance trained on one distribution does not hold in another.

## The structural analogy to Q-014

JEPA's invariance training is not designed to suppress protected demographic attributes -- it is designed to suppress what the training protocol treats as perceptual noise. But the structural failure is analogous: if the invariance objective is trained against variation that happens to correlate with causally relevant event-structure in the world model, then the representation will be blind to that event-structure at inference time. E3's attribution pipeline, operating on JEPA-derived latent states, would then make causal attributions on the basis of proxy features -- whatever correlates with the suppressed distinction without being suppressed itself.

In REE's specific context, the worry is about distinctions like agent-caused versus environment-caused harm. These may differ in specific trajectory features that a JEPA world model trained on prediction tasks would treat as noise: the exact sequence of actions that led to an adverse state, fine-grained event ordering, low-frequency causal signatures. If JEPA invariance suppresses these, attribution becomes blind to the causal distinction while remaining sensitive to correlated but non-causal features.

## Why the analogy has limits

The survey concerns discrimination against people in downstream decisions -- a different ethical harm type from REE's causal attribution problem. More importantly, FTU involves deliberate suppression of a defined attribute, while JEPA's invariance is not attribute-targeted -- it is trained against augmentations that the designer selects. Whether the invariance protocol selected for a REE world model would actually suppress attribution-relevant features is an empirical question the survey cannot answer.

The survey is therefore useful as a diagnostic frame -- it tells us that the failure mode Q-014 identifies has historical precedent and is structurally plausible -- but not as direct evidence that JEPA in REE will fail in this way.

## Calibration note

Confidence is 0.58 -- supports but with substantial caveats. The source is excellent (canonical ACM Computing Surveys reference) but the mapping requires a conceptual translation from demographic fairness to causal attribution that introduces real ambiguity. The entry is best understood as providing theoretical grounding for Q-014's concern rather than empirical confirmation of it.
