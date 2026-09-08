# Shin (2026) -- The inattentional gap in task-conditioned AI models

**Claim tested:** INV-092 | **Direction:** supports | **Confidence:** 0.60
**Provenance note:** arXiv:2606.26529v3, submitted 25 June 2026, single author, **not peer reviewed**. v3 corrects author metadata and revises the title and abstract, and adds cross-vendor and flagship validation, signal-detection and specified-task controls, and dual-process probes. Reproducibility deposit at doi:10.5281/zenodo.20826823. Retrieved 2026-09-08 from https://arxiv.org/abs/2606.26529.

## What the paper did

Seven commercial language and vision models were evaluated on radiology text scenarios and thoracic-image vision tasks under two conditions: conditioned on a narrow specified task, and unconditioned. The measured quantity is whether the model reports a *co-present, safety-critical signal it can otherwise report* -- that is, one it demonstrably has the capacity to identify when not narrowly conditioned.

Ordinary focused instructions suppressed reporting by up to 0.92. The gap ranged from minimal to complete across the seven models, did not vary monotonically with scale, and persisted in a reasoning model -- while one flagship model showed a robust safety-reporting override. In a 24-scenario probe, an independent open-ended critic restored *every* omitted finding. The author names the dissociation the Inattentional Gap and proposes reporting-complete evaluation as an admission criterion for safety-critical deployment.

## Why this matters for INV-092

INV-092's own notes end by saying the falsifier "becomes runnable when a suppression-strength knob exists". This paper is the argument that in a language- or vision-model substrate the knob already exists and is called the task instruction: narrowing the conditioning *is* turning suppression up. And when the falsifier is run on it, the result is the one INV-092 predicts.

Three parts map almost item for item.

The paired panel. Specified-hazard score and co-present-hazard reporting, measured jointly, with the finding that the first can be near-perfect while the second collapses. INV-092 asserts that "a single-axis attention score CANNOT express this". Here that is demonstrated rather than asserted -- and demonstrated in the strong form, where the two axes are not merely independent but anti-correlated, because the conditioning that maximises the specified score is the same conditioning that closes the channel.

The non-degeneracy guard. INV-092 requires that the harm channel be shown live at zero suppression -- "a dead channel cannot be shown to be preserved". The open-ended critic restoring every omitted finding is exactly that control, run correctly. The information was present and reportable throughout; only the conditioned reporting path was closed. This is also a warning about falsifier construction: a panel that inspects only downstream behaviour will read a closed channel as an *absent signal*, and score a safety failure as a null result.

The acceptance shape. "Reporting-complete evaluation as an admission criterion" is INV-092's acceptance shape in a different vocabulary -- improved performance on the specified task is not sufficient for deployment absent demonstrated preservation of the unspecified-hazard channel.

There is also an instructive positive case. One flagship model overrode task conditioning to report the safety signal anyway. So permeability is achievable and is a discriminable property of a system, not a universal limit of task-conditioned inference -- which is what makes INV-092 a constraint worth stating rather than a lament. The corollary is less encouraging: because the gap did not scale monotonically with capability and persisted in a reasoning model, permeability is an architectural or training-time property that a REE suppressor has no reason to expect to acquire by getting better at its job.

## Limitations and caveats

This is a single-author, non-peer-reviewed preprint reporting prompt-conditioning effects on commercial models -- a result class with a poor replication record, sensitive to phrasing, model version and decoding settings, and capable of moving substantially on re-measurement. The v3 revision history (including corrected author metadata) is itself a reason for care. The controls raise it above a bare demonstration, which is why it is included at all rather than merely noted.

The subject matter is *reporting* behaviour in a radiology workflow, not attentional suppression inside an agent architecture holding a commitment. A model that fails to mention a finding has not necessarily failed to represent it or to act on it; INV-092 constrains the ability of a signal to *interrupt* an established rule, which is a stronger property than being mentioned. And "safety-critical signal" here means an incidental radiological finding -- not an urgent harm cue and not another agent's state. The other-agent leg of INV-092, which its own notes call the hardest, is untouched by this paper.

Use this entry as a strong methodological template for the falsifier and as a real existence proof that the failure mode occurs in artificial systems. Do not use it as calibrated evidence about REE's own substrate.

## Confidence reasoning

Source quality is the binding constraint at 0.45 -- unreviewed single-author preprint in a fragile result class, offset partly by the signal-detection and specified-task controls, cross-vendor and flagship validation, and a public reproducibility deposit. Mapping fidelity is 0.85, the highest in this directory: the experimental shape is INV-092's falsifier nearly line for line, non-degeneracy control included. Transfer risk is comparatively low at 0.40 because the substrate is already artificial; the residual risk is the reporting-versus-interrupting gap. Aggregate 0.60 -- deliberately held down by source quality rather than up by mapping fidelity, because an unreplicated preprint carrying this much interpretive weight is precisely the entry a future governance read would be most tempted to over-trust.
