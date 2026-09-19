# Xue et al. 2026 -- identifying the unattributed feature-interference anchor

This entry exists to close a specific hole rather than to add support. Sections 4 and 6 of
`docs/thoughts/2026-09-10_phase_as_address_phase_conditioned_communication_subspaces.md` lean on "the recent
feature-interference work" and "the task-uncertainty result" -- and the document contains no bibliography, no
DOI, no author name and no year anywhere in its 471 lines. Both intake documents flagged this and routed it
here; MECH-561's notes record it as "cited WITHOUT a reference anywhere in the source document, so it cannot
be checked at all". The task was to identify it or to record that it cannot be identified.

It can be identified, and the match is about as good as an unattributed identification gets. Xue, Markman,
Chen, Kramer and Cohen, *Feature interference underlies a neuronal basis for the behavioral cost of task
uncertainty*, **Nature Neuroscience**, doi 10.1038/s41593-026-02430-w, PMID 42722796. The title alone
contains both of the thought's two naming phrases -- "feature interference" and "task uncertainty" -- and a
PubMed search for either phrase in combination returns this paper and essentially nothing else. The content
match is closer still. The thought's line 25 says task uncertainty "can leave irrelevant information strongly
represented while making normally separable task dimensions interfere with one another"; the paper's abstract
says that under uncertain conditions "feature interference causes errors by inducing stronger representations
of irrelevant features and entangled neuronal representations of different features". That is the same
sentence twice. The decisive detail is the date: the paper went online on **10 September 2026**, and the
thought document is dated **10 September 2026**. Daniel was writing the day it appeared, which is exactly how
a citation goes missing.

I record the residual uncertainty honestly, because the identification is inferential. No REE document names
this paper, so this is a reconstruction from content, phrasing and date rather than a confirmed reference. I
think it is right; a future session that finds a different source should overwrite this entry rather than
accumulate a second one.

What the paper actually establishes: across two distinct perceptual tasks, both humans and monkeys make less
accurate decisions when the task is uncertain, and the cost is traced -- behaviourally, physiologically and
causally -- to irrelevant features being represented more strongly and to different features becoming
entangled. This supports the reframing that section 6 of the thought builds on, namely that interference is
better understood as a loss of segregation between relevant and irrelevant causal channels than as a failure
to filter irrelevant content out. That reframing matters to REE because it changes what a routing failure
would look like: not too much irrelevant signal, but insufficiently separated channels.

Two cautions, one of which cuts against the family's whole programme and should not be buried. First, the
paper says nothing about oscillatory phase. MECH-561's content is that the receiver-potent communication
subspace is indexed by an endogenous cyclic coordinate; this study supports the premise that segregation is
the right frame and offers no evidence at all that phase is the segregating variable. Tagging it as support
for MECH-561 without that caveat would be exactly the confirmation error this pass exists to avoid. Second,
and more awkwardly: the artificial neural network trained on the same tasks did **not** show the uncertainty
cost. The effect is a property of biological systems under capacity pressure, not of trained networks as
such. A REE substrate might therefore not reproduce it, and an assay designed on the assumption that it will
could fail for reasons that have nothing to do with phase addressing. Confidence 0.5, and per
`feedback_lit_exp_decoupled` this raises no claim's confidence regardless.
