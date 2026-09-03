# Strachan et al. (2024) -- Testing theory of mind in large language models and humans

## What the paper did

This is the counterweight entry in the pull, and it is included deliberately: a governance record
assembled only from the failure literature would be reporting a selected corpus, and this is the
strongest available evidence against EXT-006's behavioural surface.

The authors administered a five-test battery drawn from established psychological instruments --
false belief, irony comprehension, faux pas recognition, the hinting task, and strange stories --
to GPT-4, GPT-3.5 and LLaMA2 at three sizes, across multiple runs, and to a human comparison sample
totalling 1,907 participants. On false belief, humans and models were both at ceiling. On irony,
hinting and strange stories, GPT-4 performed significantly better than the human sample. The single
exception was faux pas, where GPT-4 "scored notably lower than human levels". LLaMA2-70B, much the
weaker model everywhere else, was the only model to beat humans on faux pas, achieving "100%
accuracy in all but one run".

The authors' own interpretation of that inversion is the most valuable thing in the paper. They
attribute LLaMA2's faux-pas success not to superior mentalizing but to a bias towards attributing
ignorance -- a response tendency that happens to produce the right answer on this instrument. And
they decline the mechanism inference in general terms: the models show "a dissociation between
competence and performance", and "while LLMs are designed to emulate human-like responses, this does
not mean that this analogy extends to the underlying cognition giving rise to those responses."

## How this maps onto EXT-006

Two jobs, pulling in opposite directions, which is why the direction here is recorded as mixed
rather than weakens.

The corrective job first. If EXT-006 is read as predicting that language models will fail
theory-of-mind assessment, that reading is false and this is the study that makes it false. Four of
five measures, well powered, peer reviewed, with a real human comparison. The claim as registered
does not actually say that -- it says the ToM is produced by pattern completion over text rather
than by a maintained structural model of another agent's latent state -- but the distinction is easy
to lose in summary, and anyone citing EXT-006 should have to walk past this result to do it.

The second job is the more interesting one, and it is that the paper contains a clean demonstration
of EXT-006's mechanism claim inside the data that otherwise weakens it. LLaMA2 achieves near-perfect
scores on a theory-of-mind test via a response bias that involves modelling nobody's mind at all.
That is the pattern-completion diagnosis in its purest available form, and it is exactly why a high
score on such an instrument is uninformative about whether an other-model is present. GPT-4's
faux-pas deficit points the same way, if more softly: faux pas is the one item in the battery
requiring two agents' states to be held at once -- what the speaker knows, and how the listener is
affected -- which is the nearest this battery comes to FANToM's multi-agent state maintenance, and it
is where the strong model is weakest.

For ARC-010 the net reading is worth stating plainly, because it should change how REE describes its
own contribution. Behavioural theory-of-mind competence is not the bottleneck and should not be
presented as REE's differentiator; on narrative instruments the models are at or above human level.
What REE claims to add is the coupling of the other-model into selection -- predicted degradation of
another agent registering as a penalty in the same residue field that governs the agent's own
trajectory. Nothing in this literature, supportive or contrary, speaks to that at all.

## Limitations and caveats

The governing one is that this is a behavioural battery and EXT-006 is a claim about mechanism, so
the study cannot adjudicate it in either direction. The authors say as much themselves. This entry
must not be cited as having refuted EXT-006; it refutes a stronger and less careful claim that
EXT-006 does not make.

The instruments are used in close to their canonical published form, and their canonical form is
well represented in training corpora. Contamination is not controlled for, which is the standing
objection to positive ToM results of this shape -- Ullman (2023) in this same pull is the direct
methodological rejoinder, and the two entries should be read as a pair. The human comparison sample
of 1,907 is a baseline the authors collected, not a normative population sample, so "better than
humans" means better than this sample on these instruments. And, as with almost all of this
literature, the items are single-shot narratives: they cannot speak to whether a model of another
agent is maintained across an extended interaction, which is the half of EXT-006 that FANToM
addresses and finds against.

## Confidence

0.71, which is high source quality pulled down by modest mapping fidelity. Source quality 0.9:
Nature Human Behaviour, a large human comparison sample, multiple models and multiple runs, and
authors who state the limits of their own inference rather than overselling it. Mapping fidelity
0.55 is what caps the entry -- EXT-006 asserts the absence of a maintained structural other-model,
and a battery of narrative instruments measures output, which is consistent with a structural model
and equally consistent with very good completion, as the paper's own LLaMA2 result shows within its
own data. Transfer risk 0.30: human-designed instruments applied to a machine respondent, plus
uncontrolled contamination, which is a live risk for the positive findings specifically rather than
for the paper as a whole.
