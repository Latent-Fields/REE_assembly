# State of the Art: Reproducibility in Artificial Intelligence (Gundersen & Kjensmo, AAAI 2018)

## What the paper did

Gundersen and Kjensmo asked a simple question with an uncomfortable answer: if you took a published AI paper and tried to reproduce it, is there enough written down to do so? They assembled the variables that would have to be documented, grouped them into three factors -- Experiment, Data, Method -- built six metrics over those factors, and scored 400 papers from IJCAI and AAAI. None of the 400 documented all of the variables. Between 20% and 30% of the variables for each factor were documented. One metric improved significantly over time; the others did not move.

Alongside the survey they set out the degrees-of-reproducibility ladder that has since become standard vocabulary in this literature: **R1 Experiment Reproducible** (the same implementation run on the same data), **R2 Data Reproducible** (an alternative implementation on the same data), **R3 Method Reproducible** (an alternative implementation on different data). Documentation requirements fall as you move up the ladder, and generality rises.

## Why a documentation survey is relevant to INV-109

Not for its findings, which are about what authors write down. For its ladder -- and specifically for where the ladder stops.

INV-109 draws a line between reconstituting an operating **regime** and possessing the **endpoint** a prior run measured. The natural objection to registering it as a separate standard is that the field already has this covered: surely "reproducibility", properly practised, includes getting the same model back? Gundersen and Kjensmo's taxonomy is the cleanest available answer to that objection, because all three of its rungs live entirely on the regime side of the line. Every rung grades how much of the **method** can be reconstructed from what was documented. None of them asks whether you hold the artifact.

The detail that makes this sharp rather than merely suggestive is what R1 -- the *most demanding* rung, same implementation on same data -- actually promises. The results are expected to be the same "except for minor differences due to hardware changes". That clause is INV-109's entire subject matter. The hardware-induced difference which R1 files as a tolerable residual is exactly what makes a re-derived endpoint a different tensor from the one a prior run measured. So the field's strongest reproducibility guarantee explicitly *concedes* the thing INV-109 says voids an endpoint-identity claim.

That is why a session can satisfy every documentation norm the field recognises -- pin the substrate commit, record the recipe, publish the seeds -- and still assert an unmeasured sentence about "the banked 1002/1008 latent". The norms were never designed to catch it. This is the same structural point INV-109 makes about INV-105: a claim can climb the whole evidential ladder against a silently different endpoint, and the ladder will not notice.

## Honesty about what this entry is doing

Two caveats, both of which I would rather state than let a future reader discover.

First, this is a survey of documentation practice. It contains no evidence whatever about training dynamics, weight divergence, or endpoint identity. It cannot corroborate INV-109's factual assertion -- that job belongs to Summers & Dinneen, Zhuang et al., and Jia et al. in this same directory. What it establishes is contextual: that INV-109 is filling a real hole in the field's vocabulary rather than restating an existing norm under a new name.

Second, the reading of R1's hardware clause as "exactly INV-109's gap" is an interpretation, not a report. Gundersen and Kjensmo treat hardware-induced difference as a tolerable residual and move on; INV-109 treats it as the thing that voids the identity claim. Both can be right, because they are answering different questions -- but the *juxtaposition* is mine, and governance should weigh it as argued rather than as found. The R1/R2/R3 glosses above are the standard restatements current in the reproducibility-review literature; the primary paper's abstract names three degrees without defining them in the material retrieved during this pull.

There is also a possibility worth leaving open rather than arguing away. A field-wide taxonomy that stops at recipe-level reproduction might reflect a considered judgement that artifact identity is unnecessary for most scientific purposes, not an oversight. If that is right, INV-109 is correct in its narrow case -- where a claim *names* a specific prior endpoint -- and would be over-broad if applied as a general standard for reproduction. The claim's own wording is already narrow in this respect. The risk lies in how it gets applied downstream.

## Confidence

0.58. Well-cited meta-research and the canonical source for the taxonomy, so source quality is not in question. Mapping fidelity is held at 0.5 because the support is terminological and arrives by omission, and the aggregate is pulled below the component mean deliberately: for a methodological invariant, a taxonomy paper sets the context in which the claim is non-redundant, which is worth recording but is not evidence that the claim is true.
