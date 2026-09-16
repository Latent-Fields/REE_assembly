# Correlated individual differences in metacognition across perception and VSTM (Samaha & Postle, 2017)

**Claim under test:** MECH-003 -- *Precision must be tau-scoped with lossy projections.*
**Direction:** weakens

## Why a weakener was sought

The other four entries in this directory support MECH-003 in one way or another. That is not
because the search was rigged toward agreement; it is because the claim's *separation* requirement
is genuinely well-supported. But MECH-003 also makes an unusually strong **negative** assertion --
"There is no global precision scalar in REE," and collapsing πγ…πδ into "a single attention scalar"
is listed among the hard architectural violations. A directory that gathers four sources agreeing
with the positive half of a claim and none testing the negative half is a rhetorical exercise, not an
evidence base. So I went looking for the best available evidence that confidence is *shared* rather
than scoped.

The reason this is legitimate rather than a stretch: MECH-003 itself opens by declaring that REE
"treats precision and confidence as the same control variable operating at different temporal
depths." Having made that identification, REE inherits the empirical literature on whether confidence
is domain-general -- and that literature does not uniformly say it is scoped.

## What the paper found

Samaha and Postle had subjects estimate either the *perceived* or the *remembered* orientation of a
grating and rate their confidence. Across individuals, metacognitive accuracy in the perceptual task
correlated strongly with metacognitive accuracy in the short-term memory task. The correlation was
not explained away by differences in task performance or in average confidence level, and it held
across two different metrics of metacognition and in both of the first two experiments. Their
conclusion is a domain-general metacognitive architecture spanning perception and visual short-term
memory.

On REE's own identification of confidence with precision, that is a confidence signal that is not
strictly scoped to the process that generated it -- and perception and short-term memory sit at
different temporal depths on any reasonable mapping.

## Why I have weighted it at only 0.48

Three reasons, and the second is the one that matters most.

First, the axis is wrong. Samaha and Postle vary **task domain**; MECH-003 forbids collapsing across
**temporal depth**. The claim is silent on whether precision may be shared across modalities at a
fixed τ. Making this finding bite requires arguing that domain-generality and depth-generality are
the same kind of leak, and that is not obvious.

Second -- and this is the part that would be dishonest to omit -- **the paper's own third experiment
pulls in MECH-003's favour**. The cross-domain correlation emerged only when both tasks shared the
same task-relevant stimulus feature. When both required orientation judgements, metacognition
correlated; when the perceptual task was switched to contrast judgements, it did not. So what they
actually found is a *feature-conditional, scoped* shared resource, not the free-floating global
scalar MECH-003 prohibits. Read carefully, this paper is closer to "confidence is scoped, and the
scope boundary is representational content" than to "confidence is global."

Third, the authors themselves note that their result contrasts with prior work comparing perception
and *long-term* memory, which largely found domain-**specific** metacognition. That comparison spans
the widest temporal range -- and is therefore the closest available analogue to REE's τ axis -- and it
is the one that found separation. If anything, the temporal gradient in this literature runs in
MECH-003's direction.

## Limitations

The evidence base is correlations in individual differences, which are sensitive to the reliability
of the underlying metacognitive measures and to sample size, and psychophysics samples are modest for
stable correlation estimates. The metacognitive metrics themselves are contested quantities. And the
whole inference to MECH-003 passes through an analogy that the paper's own experiment 3 partly
undercuts.

## Confidence

0.48. Recorded as a real but weak weakener -- which I think is exactly the right weight. It is
genuinely relevant, because REE has tied precision to confidence by its own definition and cannot
then ignore what is known about confidence. It is genuinely indirect, because the study's axis is
domain rather than depth, and because its most careful experiment shows the sharing to be conditional
rather than global. Its main value to governance is as a marker of where MECH-003's strongest
sentence would be tested if anyone wanted to test it: the experiment MECH-003 needs is a
metacognitive-transfer study whose axis is temporal depth rather than stimulus domain, and as far as
I can tell nobody has run it.
