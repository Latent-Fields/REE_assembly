# Alexander & Brown (2011) -- Medial prefrontal cortex as an action-outcome predictor

**Claim tested:** MECH-065 -- *Reality-coherence conflict lane modulates loop precision and commitment thresholds before execution lock-in.*
**Direction:** weakens (lane separability) | **Confidence:** 0.69

## Why a weakening entry belongs in this pull

Three of the five entries here support MECH-065 in one respect or another. That is a warning sign, not
a result, and it would be a poor governance record if I left the strongest available counter-argument
out of it. Alexander and Brown's Prediction of Response Outcome model is that counter-argument, and it
goes at MECH-065's *premise* rather than at its mechanism.

## What the paper argues

The authors observe that medial prefrontal cortex has attracted a crowd of competing theories -- error
detection, conflict monitoring, error likelihood prediction, volatility, reward -- each fitted to its
own slice of the evidence, with no single account reconciling them. They then show that one model
built from standard learning rules reproduces an unprecedented range of those findings. The model does
two things: it learns to predict the possible outcomes of a planned action, and it detects
discrepancies between predicted and actual outcomes, which in turn update the predictions. From that
single construct, cognitive control emerges as a consequence of evaluating probable against actual
outcomes.

The consequence for anyone building a control plane is uncomfortable and worth sitting with. If
*conflict* was never a primitive signal -- if it is a re-description of outcome-prediction discrepancy
under a particular task structure -- then a control architecture that instantiates conflict as its own
named lane may be describing one underlying computation twice.

## How this bears on MECH-065

MECH-065 writes its own falsifier in these terms: the claim is refuted if the manipulation produces no
separable effect and any downstream change "is better explained by existing signals (S1/S3) alone."
Alexander and Brown supply the strongest general statement of that alternative. Applied to REE: a
provenance or authority mismatch violates an expectation, like any other violated expectation; it
therefore generates prediction error; a threshold effect follows from the prediction error; and no
distinct reality-coherence lane is required anywhere in the story.

I want to be precise about what this does and does not do to the claim. It does *not* weaken the
threshold mechanism -- this paper says nothing about decision thresholds, and the Cavanagh and Frank
entries stand untouched. What it weakens is the assertion that RC_conflict is a *separate lane*, which
is the part of MECH-065 carrying the actual architectural commitment.

The operational consequence is a design requirement, and I would treat it as binding. **A MECH-065
experiment must include an arm that holds generic prediction error or surprise MATCHED while varying
provenance mismatch specifically.** Without such an arm, a confirming result -- RC_conflict up,
threshold up, lock-in pressure down -- is equally predicted by the unified account, and should not be
scored as support for MECH-065 at all. This is a stronger constraint than the claim's current
`what_would_answer` text imposes, and I would recommend it be folded in when the claim is next
revised.

## Where the weakening argument itself is vulnerable

Parsimony is not proof. A model that reproduces a set of effects is not thereby the mechanism producing
them, and the PRO model's scope claim was contested when it appeared. More pointedly, the same group's
subsequent empirical work cuts partly the other way: Jahn et al. (NeuroImage 2014) found prediction and
evaluation signals loading on *distinct* regions within anterior cingulate, and Jahn et al. (J Neurosci
2016) found a dorsal-ventral dissociation separating cognitive effects from pain within medial
prefrontal cortex. Both argue for more internal structure than a single undifferentiated signal --
which is to say the anti-lane reading I am taking here is the strong form of the argument, and the
authors' own later data qualify it.

And there is a question I do not think this entry can settle. Alexander and Brown are arguing about how
the *brain* factorises these computations. REE is an engineered control plane, where separating lanes
may be justified on legibility, auditability or safety grounds regardless of whether biology factorises
them the same way. A finding that the brain uses one signal where REE uses four is a reason to check
whether REE's four lanes are empirically correlated -- it is not automatically a reason to merge them.

## Confidence reasoning

Source quality 0.82 -- Nature Neuroscience, genuinely influential, but a modelling-and-reinterpretation
paper rather than a decisive experiment, and with its strong parsimony claim since qualified by its own
authors. Mapping fidelity 0.66 -- the alternative hypothesis maps cleanly onto MECH-065's stated
falsifier, which is what earns the entry its place, but the neuroscience-to-engineered-control-plane
transfer is uncertain in both directions. Transfer risk 0.40. Aggregate 0.69. Scored as **weakens on
the lane-separability premise specifically** -- not on the threshold mechanism, which this paper does
not address.
