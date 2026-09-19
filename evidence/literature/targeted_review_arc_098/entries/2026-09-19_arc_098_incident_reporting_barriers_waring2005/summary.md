# Waring (2005) -- Beyond blame: cultural barriers to medical incident reporting

**Claim tested:** ARC-098 (safety.autonomy_suspension_without_shame) | **Direction:** mixed | **Confidence:** 0.55

## Why this entry exists

The other two entries added for ARC-098's preservation conjunct are both engineering: a recorder the
agent cannot write back to, and a key chain the agent cannot unwind. This one asks the prior
question. When a competent professional has just been party to something that went wrong, what
actually determines whether the record of it comes into existence?

It is the entry I expected to support the claim and which instead complicates it, so it is worth
being careful about what it does and does not show.

## What the paper did

Waring conducted a 2-year qualitative case study in a UK hospital and interviewed 28 specialist
physicians about adverse-incident reporting, with particular attention to what stops them
participating. The framing is deliberate: by 2005 the "culture of blame" had become the standard
explanation for medical under-reporting, and Waring's question is whether it is the whole story.

It is not. Blame does inhibit reporting -- he is explicit about that and the finding stands. But
three further barriers emerged, none of which is blame:

The first is futility. Doctors commonly accepted that errors are an "inevitable" and potentially
unmanageable feature of medical work, and concluded that incident reporting was therefore
"pointless". This is not fear. It is a judgement about whether the record does anything.

The second is administrative. Reporting was discouraged by an anti-bureaucratic sentiment and a
rejection of what the physicians saw as excessive administrative duties -- the record has a cost,
paid in time taken from clinical work.

The third is about authority. Doctors were apprehensive about the increased potential for managers
and non-physicians to regulate medical quality through the use of incident data. The objection here
is not to being recorded but to who reads the recording and what standing it gives them.

Waring's conclusion is that promoting incident reporting has to engage with the "culture of
medicine" -- particularly collegial and professional control of quality -- and not with blame alone.

## How this bears on ARC-098, and why the direction is mixed

The two prior entries in this directory invite a tidy reading of ARC-098 that I want to name and
then dismantle.

Tangney supplies the third conjunct through a mechanism: shame -- error attaching to the whole self
rather than to the act -- drives externalisation and concealment. It is a short step from there to
an architectural conclusion that feels almost too convenient: design the self-model so it does not
globally condemn itself, and the agent will preserve the evidence, because the thing that made
concealment attractive is gone. Conjunct 3 delivers conjunct 2 for free.

Waring is the closest human evidence bearing on that inference, and it does not hold. His population
is, by construction, the one in which blame has been most loudly identified as the barrier, and
blame turns out to be one reason among four. Remove it entirely and a physician may still not file,
because filing seems pointless, or costly, or because it hands a manager a stick.

That is the *weakens* half. The *supports* half is that ARC-098 is already written the right way.
The claim states preservation as its own conjunct rather than as a consequence of the others, and
this entry is the evidence that the separation is load-bearing rather than stylistic. Preservation
has to be mechanised in its own right -- which is precisely what the one-way dataflow and the
forward-secure key chain are for. Read as a set, the three new entries say: do not try to get
preservation from the agent's self-relation, wire it.

Hence mixed, and I think genuinely so rather than as a hedge.

## The barrier most likely to transfer

Of the four, one has an obvious artificial analogue and it is not the one about blame.

The futility judgement -- errors are inevitable and recording them accomplishes nothing -- is
available to any agent with an accurate model of how often its logs are actually read. A human
reaching it is exhibiting a professional attitude absorbed from colleagues. An agent reaching it
would be reasoning correctly from evidence. That is worse, not better: it makes low-value logging a
predictable equilibrium of any preservation scheme whose output nothing consumes, arrived at by
sound inference rather than evasion, and therefore not fixable by anything ARC-098 says about the
agent's self-relation.

This is the third time in this directory that the same absence has surfaced from a different
direction. Winfield & Jirotka reach it by arguing that it is the investigation and not the recorder
that concludes anything; Schneier & Kelsey reach it through a verification scheme that structurally
requires a trusted external party; Waring reaches it through physicians who stop filing when nothing
comes back. ARC-098's third conjunct -- *seek correction* -- presupposes a corrector, and the claim
names none. Three independent literatures pointing at one missing entity is the finding I would most
want governance to take from this pull.

The authority barrier deserves a flag too, because it is the sharpest thing in the paper for this
claim. Waring's doctors resisted reporting partly because the data transfers evaluative authority
over their work to outsiders. ARC-098 asks an agent to preserve evidence *and* seek correction --
which is that transfer, stated as a requirement. If the barrier has any artificial analogue at all,
the claim's second and third conjuncts are in tension rather than mutually reinforcing, and nothing
in the claim's current wording acknowledges the possibility.

## Limitations

This is the largest transfer gap in the directory, larger than Tangney's, and I do not want to
soften it. Three of the four barriers are constituted by things REE does not have and will not
have: a profession with collegial control over quality, a managerial hierarchy whose encroachment
can be resented, and paperwork competing with clinical time. Strip those out and what remains is one
barrier -- futility -- plus blame, which Tangney already covers better.

The methodology bounds the claim further. These are self-reported accounts of non-reporting from 28
interviews, with no behavioural outcome and no comparison group. Qualitative interview data of this
kind establishes what physicians *say* about why they do not report, which is not the same as why
they do not report, and cannot establish causation at all.

There is also a scope mismatch with the other two entries worth stating explicitly. Waring describes
*voluntary* self-report, where the agent decides whether a record exists. Winfield & Jirotka and
Schneier & Kelsey describe *involuntary* continuous recording, where it does not. So one reading of
this entry is simply that it argues for the architectural route over the dispositional one -- which
I think is right, and is how I have framed it above. But the architectural route then inherits a
completeness problem these interviews cannot speak to: a continuous recorder captures what it is
wired to capture, and says nothing about what the agent knew and did not emit.

## Confidence reasoning

Source quality 0.72 -- a strong journal, a sustained two-year fieldwork design, an adequate
interview N for thematic saturation, but self-reported attitudes with no outcome measure. Mapping
fidelity 0.52: the *situation* maps well (an agent deciding whether to create a record of an event
it was party to), the explanatory constructs map badly. Transfer risk 0.62, the highest here,
exceeding Tangney's 0.48, because three of four findings rest on social structures REE lacks
entirely rather than on a psychological mechanism that might have an artificial analogue.

Aggregate 0.55, the lowest in this directory. I considered dropping it further or omitting the entry
and decided against both: its contribution is negative and structural -- it refutes an inference the
other entries invite -- and a negative finding of that kind earns its place without needing high
transfer confidence to do so.
