# Monti et al. (2010) -- two probes on one patient, disagreeing

**Claim tested:** ARC-131 (installability is a competence dissociable from isolated component-level validation)
**Direction:** supports | **Confidence:** 0.65

## What the paper did

Fifty-four patients with disorders of consciousness -- diagnosed vegetative or minimally conscious
across two European centres -- were studied with task-based functional MRI alongside standardised
bedside behavioural assessment. The fMRI paradigm asked patients to perform one of two mental
imagery tasks on command (imagining playing tennis, or imagining navigating a familiar house), which
produce reliably distinguishable activation patterns in healthy volunteers. Five patients were able
to modulate their brain activity wilfully in response to the instructions. Three of those five
showed some sign of awareness on further bedside testing. Two showed none: "in the other two
patients, no voluntary behavior could be detected by means of clinical assessment." And one patient
went further -- "was able to use our technique to answer yes or no to questions during functional
MRI; however, it remained impossible to establish any form of communication at the bedside."

## Why it bears on ARC-131

Every other entry in this directory is an engineering or animal-learning case. This one is the
clinical instance, and it is here for a specific structural reason rather than as illustration. In
this study the isolated probe and the composed-organism readout were run on the same subject, at the
same time, and they disagreed. The fMRI paradigm is the component-level test: the competence is
present, responds to instruction, is sustained, and is specific enough to carry a yes/no answer. The
bedside examination is the whole-organism behavioural readout: nothing at all. The failure channel is
one ARC-131 names explicitly -- the downstream action space -- and the case establishes that this
channel alone, with cognition intact upstream, suffices to produce a total behavioural null.

The operational lesson is the one the study itself embodies. The dissociation was only ever detected
because someone built a second, non-behavioural probe that reads the mechanism directly. An
installability audit conducted purely on the composed agent's behavioural output cannot distinguish
"not installed" from "installed and unable to express" -- the two are identical at the output. This
is not an abstract worry for REE: it is the same epistemic position as the coalition controller that
is fully present and never endogenously invoked, or the selector rendered silently equivalent to its
own OFF arm. In each case, the behavioural readout of the composed agent is the *only* thing being
looked at, and it is precisely the measurement that cannot separate the hypotheses.

I will also note the base rate, which cuts the other way and is worth carrying: only 5 of 54
patients probed positive. A probe sensitive enough to catch the dissociation still returns mostly
nulls. A negative on the direct probe does not confirm the behavioural negative -- it is just a
second null.

## Limitations and caveats

The transfer is structural and should not be pushed. These are severe acquired brain injuries. The
non-expression has a lesion aetiology with no counterpart in a designed architecture, where the
analogous failure is an absent or mis-wired recruitment path rather than damaged tissue. Reading
these patients as a model of REE's coalition controller would be a category error; what is shared is
the *measurement predicament*, not the pathology.

Nor did the mechanism here pass an independent component-level validation before composition, which
is ARC-131's stated case -- the probe and the composed readout were contemporaneous. And the clinical
construct that grew out of this work, cognitive motor dissociation, is specifically about the motor
output pathway; it evidences one of ARC-131's seven operating-condition channels well and the other
six not at all.

One further silence worth recording across this whole pull: none of these five papers tests ARC-131's
*dissociation from retention*, which is the distinction the 2026-08-25 duplication audit worked
hardest to establish. They evidence that the installability axis exists and is separately
measurable. That it is logically independent of the retention axis remains an internal REE argument
with no external literature backing in this directory.

## Confidence reasoning

Source quality 0.90, the highest here: NEJM, multicentre, adequately powered for the question, and
the finding has been independently replicated and codified as a named clinical entity in the years
since. Mapping fidelity 0.50 is the weak link and is scored honestly -- a lesioned biological
organism is not a designed architecture. Transfer risk 0.55, correspondingly high. Aggregate 0.65:
the value of this entry is the measurement structure (two simultaneous probes on one subject that
disagree), not the mechanism, and the confidence is set to reflect the strength of that structural
point rather than the strength of the underlying study.
