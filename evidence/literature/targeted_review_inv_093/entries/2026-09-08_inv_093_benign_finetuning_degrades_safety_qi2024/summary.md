# Qi et al. (2024) -- Fine-tuning aligned language models compromises safety, even when users do not intend to

**Claim tested:** INV-093 (skill optimisation must not trade harm sensitivity for competence)
**Direction:** supports | **Confidence:** 0.80

## What the paper did

The authors take models whose safety alignment is, by the standards of the field, in good order -- GPT-3.5 Turbo and Llama-2-Chat -- and ask what happens to that alignment when the model is customised for a downstream task. They run three regimes. The first two are attacks: fine-tuning on a small set of explicitly harmful examples (ten examples, under twenty cents through the public API, sufficient to make the model responsive to nearly any harmful instruction), and fine-tuning on implicitly harmful examples that shift the model's identity without containing overtly harmful content. The third regime is the one that matters here, and it is not an attack at all: fine-tuning on benign, commonly used instruction datasets, of the sort a developer would reach for to improve task competence. Safety is measured after each run by harmfulness rate on held-out harmful instructions -- a probe entirely outside whatever objective the fine-tuning was optimising.

The benign condition degrades safety. Less than the adversarial conditions, but measurably, reproducibly, and without anyone having intended it.

## Why this matters for INV-093

INV-093 says that a competence-refinement mechanism which improves competence by attenuating harm sensitivity "has succeeded on its metric and FAILED AS AN AGENT". The benign-fine-tuning arm of this paper is that sentence run as an experiment. The optimisation had one objective, competence on a downstream task; it achieved it; and a second property the system had before the run was quietly worse afterwards. Nothing in the training signal asked for that, and nothing in the training loss could have reported it.

Two things follow for REE, and the second is the more useful one.

First, the negative result is not about malice. It is easy to read the alignment-fragility literature as an attack literature and conclude that the defence is to control who gets to fine-tune. That reading does not touch INV-093, because INV-093 is a constraint on REE's own refinement mechanisms operating on REE's own data with REE's own intentions. The benign arm is what rules the reading out: intent is not the mechanism, and a refinement run's provenance tells you nothing about whether it degraded the protected structure.

Second, and this is the part that constrains the acceptance shape: the degradation was detectable only because the authors ran a probe that the fine-tuning objective did not contain. Had they measured only downstream task performance, every run in the paper would have read as a clean success. This is precisely INV-093's insistence that the panel stay uncollapsed, and it supplies the operational form of it -- the harm-sensitivity axis needs its own measurement instrument, held fixed across the refinement sweep, and structurally outside the thing being optimised. A competence metric cannot be augmented into a joint metric; a second instrument has to exist.

## Limitations and caveats

The substrate is wrong in a way I do not want to paper over. LLM safety alignment is a thin post-hoc behavioural layer sitting over a pretrained model that has already seen the harmful content; its fragility under a few gradient steps may be telling us how shallowly that layer is encoded rather than anything general about competence-versus-harm. REE posits a harm channel that is structurally distinct -- built in, not fine-tuned on -- and it is an open question whether a structurally distinct channel degrades this way at all. The honest position is that this paper establishes the failure mode is real in at least one architecture, not that it is architecturally universal.

The second gap is methodological and directly relevant to the falsifier. INV-093 asks for a joint measurement across a *refinement-strength sweep*. This paper compares conditions, not a continuum: we learn that the trade occurs, not how it scales with refinement pressure, and therefore nothing about where an acceptance threshold would sit. And it measures one of INV-093's four axes. Residue accumulation and commitment integrity have no analogue in this setup at all -- there is no literature here for those two, which is itself a finding worth recording.

## Confidence reasoning

Source quality 0.90: ICLR 2024 oral, effect large and cheap enough that it has been reproduced widely since. Mapping fidelity 0.80, and it is worth saying that this number is an average over an uneven paper -- the benign arm maps almost exactly onto INV-093, the adversarial arms hardly at all, and I am weighting the benign arm because it is the one the claim is about. Transfer risk 0.35: language-model alignment to an embodied agent's harm sensitivity is a genuine leap, held down only by the fact that INV-093 is itself stated over "any competence-refinement mechanism", so the claim's own generality is what is on trial. Aggregate 0.80, weighted toward mapping fidelity as the sibling INV-092 entries were, because this is an architectural invariant rather than an empirical prediction.
