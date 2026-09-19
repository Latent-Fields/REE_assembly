# The brain does not inspect the content either (Whitford, 2019)

**Claim tested:** MECH-064 -- typed authority and control-store separation blocks direct exteroceptive
writes into policy and identity stores.
**Direction:** supports. **Confidence:** 0.55.

## Why a psychiatry review is in a prompt-injection pull

The four AI-security entries in this pull establish that MECH-064's architecture works and that its
rivals do not. None of them can answer a prior question: is typed authority separation an engineering
convenience, or is it a constraint that anything with a self/world boundary has to satisfy? That
question is the reason the claim sits in `control_plane_signal_map.md` rather than in a security
appendix, and it is answerable only from biology.

## What the paper did

Speaking-induced suppression (SIS) is the observation that "the sounds one generates by overt speech
elicit a smaller neurophysiological response in the auditory cortex than comparable sounds that are
externally generated." It is well established in nonhuman animals and in healthy humans, where it is
measured with EEG or MEG in the Talk-Listen paradigm, and it "is believed to involve the action of
corollary discharges." A growing set of Talk-Listen studies reports subnormal SIS in patients with
schizophrenia.

Whitford's argument is that this is theoretically significant because it gives the first-rank symptoms
a mechanism. "The failure to suppress the neural consequences of self-generated movements ... provides
a prima facie explanation for delusions of control", and "the failure to suppress the neural
consequences of self-generated inner speech provides a plausible explanation for certain classes of
auditory-verbal hallucinations, such as audible thoughts."

## What it says about MECH-064

Look closely at the Talk-Listen design, because the design *is* the argument. A participant speaks and
hears their own voice; then they hear a recording of the same vocalisation played back. The acoustic
content is the same. The neural response is not. Whatever distinguishes the two cases, it cannot be a
property of the sound -- there is no property of the sound to use.

What distinguishes them is an efference copy: a signal emitted by the motor system, arriving
out-of-band, which tags the expected sensory consequence as self-generated. The tag rides a separate
channel because it *has* to. The content does not carry the information.

That is MECH-064's third bullet -- "authority labels come from channel metadata, not text content" --
implemented in wetware, and arrived at by evolution rather than by a security committee. It is also,
notably, the same reason the Zhan et al. entry in this pull found content-inspection defences
breakable: a detector examining content for signs of untrustworthiness is attempting something the
brain does not attempt, because the information is not in there to find.

The second contribution is about stakes rather than mechanism. When provenance tagging fails,
misattribution follows across the self/world boundary, and the clinical presentation is delusions of
control and audible thoughts. Described architecturally rather than phenomenologically, that is an
identity and agency store accepting writes it should have refused. MECH-064 asserts that a control
plane must forbid exteroceptive content from writing policy and identity. Psychiatry is the discipline
that describes what a system looks like after that has happened. The correspondence is worth taking
seriously, and it belongs in the MECH-088 psychiatric-taxonomy thread where it can be developed
properly rather than asserted here in passing.

## Limitations, which are substantial

I want to be blunt about these, because the entry is seductive and its confidence is low for reasons
that matter.

*The clinical half is the author's prediction, not his result.* He says so: "While the empirical
evidence for a relationship between SIS and the first-rank symptoms is currently limited, I predict
that future studies with more sensitive experimental designs will confirm its existence." The
provenance-tagging mechanism is solidly evidenced. The step from tagging failure to identity-boundary
symptoms is a stated hypothesis. Citing this entry as showing that authority-labelling failure
*causes* identity corruption would be borrowing an author's prediction and reporting it as a finding.

*The direction is converse to the claim's threat model.* SIS failure means self-generated content is
read as external. MECH-064 forbids external content from writing into `POL`/`ID`/`CAPS`. These are two
failure modes of a single labelling mechanism -- not the same failure. The biology directly evidences
the direction the claim is *not* about. Whether a substrate that mislabels one way also mislabels the
other is an assumption I cannot discharge from this paper.

*The scale gap is severe.* Corollary discharge operates on a sensorimotor prediction at roughly N1
latency -- hundreds of milliseconds. MECH-064 governs stores that persist across episodes and
constitute policy and identity. The precedent here is unflattering and close to hand: the
Papez-circuit thread went looking for gate inputs and found that every nominated one turned out to be
a slow process downstream of the fast gate. That the brain solves the fast provenance problem with
out-of-band tagging is suggestive for the slow case and evidence for nothing about it.

And a methodological note: single-author narrative review, so the evidence selection is unchecked by a
second reader, and the underlying Talk-Listen literature has a known spread in patient-control effect
size across laboratories. The phenomenon in healthy participants is not in doubt. The magnitude of the
clinical difference is softer than a review makes it feel.

## Confidence reasoning

0.55 -- the lowest in this pull, and the entry still earns its place, because it is the only one that
speaks to the claim's necessity rather than its feasibility. Source quality 0.72: good journal,
well-established phenomenon, discounted for single authorship and effect-size spread. Mapping fidelity
0.50 is the number doing the work: the *mechanism* maps tightly onto the claim's third bullet, while
the failure *direction* is converse and the clinical inference is a prediction. Transfer risk 0.60, by
far the highest here and correctly so -- human electrophysiology at N1 latency to a persistent
artificial policy store crosses a species-to-substrate boundary and a fast-to-slow timescale boundary,
and it is the second that has already cost this project time elsewhere.

What this entry legitimately supports is narrow and worth having: out-of-band provenance tagging is
the solution biology reached for the same problem, for the same reason, and its failure has a
recognisable pathology. It supports nothing about REE's stores.

Source: Whitford TJ. *Biol Psychiatry Cogn Neurosci Neuroimaging* 2019;4(9):791-804. PMID 31399393,
[DOI](https://doi.org/10.1016/j.bpsc.2019.05.011). Retrieved via PubMed.
